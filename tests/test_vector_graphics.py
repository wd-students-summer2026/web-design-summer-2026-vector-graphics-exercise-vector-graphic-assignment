"""
Tests for the Vector Graphics assignment.

The student must:
  - publish a `vector_graphics.html` page that displays their SVG image
  - link to that page from their personal site's home page
  - serve a real SVG vector image on the page (either inline <svg> or
    an <img>/<object> that points to a .svg file)

Subjective requirements ("unique forms, layers, and colors") are not
testable automatically and are intentionally not enforced here.

Requires Selenium 4.6+ and Google Chrome.
"""

import json
import pytest
from urllib.parse import urljoin
from urllib.request import urlopen, Request
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


PAGE = "vector_graphics.html"


def _build_url(site_url, page=""):
  base = site_url.rstrip("/")
  if not page:
    return base + "/"
  return base + "/" + page.lstrip("/")


def _is_svg(url):
  """Fetch the URL and check that it really is an SVG document."""
  try:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=10) as resp:
      ct = resp.headers.get("Content-Type", "").lower()
      head = resp.read(1024).decode("utf-8", errors="ignore").lower()
      return "svg" in ct or "<svg" in head
  except Exception:
    return False


class Tests:

  @pytest.fixture(scope="class")
  def settings(self):
    with open('./settings.json', 'r') as f:
      yield json.load(f)

  @pytest.fixture(scope="class")
  def page_url(self, settings):
    return _build_url(settings["site_url"], PAGE)

  @pytest.fixture(scope="class")
  def driver(self, page_url):
    options = Options()
    options.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=options)
    driver.get(page_url)
    yield driver
    driver.quit()

  def test_page_loads(self, driver):
    """vector_graphics.html must load successfully."""
    assert driver.find_element(By.TAG_NAME, "body")

  def test_has_svg_reference(self, driver, page_url):
    """
    The page must include either:
      - an inline <svg> element, OR
      - an <img>/<object>/<embed> whose src/data points to an SVG file.
    """
    # inline svg first
    inline = driver.find_elements(By.TAG_NAME, "svg")
    if inline:
      return

    candidates = []
    for img in driver.find_elements(By.TAG_NAME, "img"):
      src = img.get_attribute("src") or ""
      if src:
        candidates.append(urljoin(page_url, src))
    for obj in driver.find_elements(By.TAG_NAME, "object"):
      data = obj.get_attribute("data") or ""
      if data:
        candidates.append(urljoin(page_url, data))
    for emb in driver.find_elements(By.TAG_NAME, "embed"):
      src = emb.get_attribute("src") or ""
      if src:
        candidates.append(urljoin(page_url, src))

    assert candidates, (
      "vector_graphics.html has no inline <svg> and no <img>/<object>/<embed> "
      "elements at all."
    )
    assert any(_is_svg(c) for c in candidates), (
      "None of the image references on vector_graphics.html point to a "
      "real SVG document. References checked: {}".format(candidates)
    )

  def test_images_have_alt(self, driver):
    """Any <img> on the page must have a non-empty alt attribute."""
    for img in driver.find_elements(By.TAG_NAME, "img"):
      alt = img.get_attribute("alt")
      assert alt is not None and alt.strip() != "", (
        "An <img> on vector_graphics.html is missing an alt attribute: {}"
        .format(img.get_attribute("src"))
      )

  def test_svg_scales(self, driver, page_url):
    """
    The SVG must remain crisp at large sizes - i.e. its rendered size
    grows with its CSS width without becoming a blurry raster. We
    confirm this indirectly by checking that the SVG element / image
    has a viewBox attribute (the hallmark of a scalable SVG) when
    inlined, OR that the referenced file declares one.
    """
    inline = driver.find_elements(By.TAG_NAME, "svg")
    if inline:
      vb = inline[0].get_attribute("viewBox") or ""
      assert vb.strip() != "", (
        "Inline <svg> on vector_graphics.html has no viewBox attribute, "
        "so it will not scale cleanly. Re-export it with the viewBox "
        "preserved."
      )
      return
    # external SVG file
    for img in driver.find_elements(By.TAG_NAME, "img"):
      src = urljoin(page_url, img.get_attribute("src") or "")
      if src.lower().endswith(".svg"):
        try:
          req = Request(src, headers={"User-Agent": "Mozilla/5.0"})
          with urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8", errors="ignore").lower()
            assert "viewbox" in body, (
              "{} has no viewBox attribute; it will not scale cleanly."
              .format(src)
            )
            return
        except Exception as e:
          raise AssertionError("Could not fetch {} : {}".format(src, e))
    # if we get here, the prior test already failed; mirror that.
    raise AssertionError("No SVG to check viewBox on.")

  def test_linked_from_home(self, settings):
    """The home page (index.html) must link to vector_graphics.html."""
    home = _build_url(settings["site_url"])
    options = Options()
    options.add_argument("--window-size=1400,1000")
    driver = webdriver.Chrome(options=options)
    try:
      driver.get(home)
      try:
        elem = driver.find_element(
          By.CSS_SELECTOR,
          "a[href='{0}'], a[href$='/{0}']".format(PAGE),
        )
      except NoSuchElementException:
        elem = None
      assert elem, "The home page has no link to vector_graphics.html."
    finally:
      driver.quit()
