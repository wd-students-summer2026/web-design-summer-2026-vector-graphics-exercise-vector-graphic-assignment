# Vector Graphics Assignment

Welcome! In this assignment, you will create a vector graphic for the web in SVG format.

## Scalable Vector Graphics

Scalable Vector Graphic format (SVG) is a text file format that uses text to represent vector image data.

For example a simple SVG image file named 'circle.svg', representing a circle with a red stroke and yellow fill, might have the following text in the file:

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 69.45 69.45">
	<defs>
		<style>
			.cls-1{
				fill:#fff200;
				stroke:#ed1c24;
				stroke-miterlimit:10;
			}
		</style>
	</defs>
	<title>circle</title>
	<circle class="cls-1" cx="34.72" cy="34.72" r="34.22"/>
</svg>
```

An HTML document that wants to display this image might have the following img tag somewhere in the body:

```html
<img src="images/circle.svg" />
```

It is possible (and often recommended) to use a vector image editing application, such as [Adobe Illustrator](https://www.adobe.com/products/illustrator.html) or [Inkscape](https://inkscape.org/), to create vector images visually, and then export them as SVG-formatted text files for inclusion on web pages.

## Requirements

Do the following:

### Vector image requirements

Using Adobe Illustrator or Inkscape, create a vector graphic for your website. This could be a logo, a symbol, a user interface element, or an illustration. Your image should include unique forms, layers, and colors.

When your image is complete, save it as an SVG file (in Illustrator, use the following menu: `File` > `Save As...` > `Format: SVG (svg)` > `Save`; in Inkscape use the following menu: `File` > `Export` and choose `Plain SVG`). You can leave the SVG Options at their default settings. After you click OK you will have a web-ready scalable vector graphic.

### Publishing requirements

The image must be published onto a web page named `vector_graphics.html`.

- this file must be linked from your personal web site's home page.

### Example image

![A star in SVG format](images/star.svg)

### Copy existing web site files

The work you do in this assignment will be published to the same directory where your current web site currently exists. To prevent you from accidentally deleting any of your existing web site files, copy all the files from your existing web site into the main project directory for this assignment. This means copying any existing HTML, CSS, images, and other files and directories so a copy exists within this project directory. Then we will be able to upload everything in this directory to the web server and replace all existing files without worry about losing anything.

## Submit your work

In order to submit this assignment, you must publish all modified files to the web and upload the code to GitHub.

You **must** include your original Illustrator `.ai` or Inkscape `.svg` document in the `images` directory in the code you submit to GitHub, as well as the web-ready file in `.svg` format if not using Inkscape's native SVG format.

### Upload the web page to a web server

Upload all files you have created to a web server. Your instructor will have given you instructions for how to do this.

Take note of the web address (URL) of your web page - this is the address that can be plugged into the address bar of any web browser for the web browser to load and display your web page.

### Update the settings.json file

Make sure your name, NYU Net ID, and the exact URL of your web site's home page are placed into the `settings.json` file in the appropriate places. Make sure the URL works when plugged into a web browser beforehand.

### Submit your work on GitHub

You are now ready to submit this assignment. You can do so directly from Visual Studio Code with the following steps, in the indicated order:

1. Switch to the Source Control view in Visual Studio Code - this view will show you a list of the files you have modified.
1. In the "`Message`" text field towards the top-left, enter a unique message to yourself about what you have changed and, while still with the text field selected, type `Command`-`Enter` on Mac OS X, or `Control`-`Enter` on Windows, to "commit" the changes you've made with this custom message. If you forget to hit `Command`-`Enter` after typing the message, you can instead click the "`...`" button above the message field and click the "`Commit all`" option in the menu that appears.
1. Now, click the "`...`" button above the message field and click the "`Push`" option in the menu that appears - this will upload your changes to your personal code repository on GitHub.

You have now submitted your completed assignment. Your changes are now posted to GitHub.com, where the instructor and graders can access it. Your `settings.json` file has information about who you are and where we can view your page on the web.

You can verify all this yourself manually by visiting your repository on GitHub.com and making sure the code displayed there is what you submitted.
