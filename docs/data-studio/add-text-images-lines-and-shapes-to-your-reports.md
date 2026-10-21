---
url: https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports/
title: Add text, images, lines, and shapes to your reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:49:25.387797+00:00
---

# Add text, images, lines, and shapes to your reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Add text, images, lines, and shapes to your reports Stay organized with collections  Save and categorize content based on your preferences. 

Adding static design elements can add visual appeal and context to your data stories. As a best practice, use these elements sparingly to avoid distraction from the data.

**Important:** Some of the features described on this page are not supported for responsive reports. Check the [Limitations of responsive reports](https://docs.cloud.google.com/data-studio/create-a-responsive-report#limitations) section of the **Create a responsive report** article for a list of unsupported features.

Click the corresponding icon on the toolbar to add the following components to your reports:

  1. insert_text Text
  2. image Image
  3. shapes Shape
  4. diagonal_line Line



## Add text

Use text to add headings and descriptions to your reports. You can also use text to [create hyperlinks](https://docs.cloud.google.com/data-studio/link-to-a-page) to pages within your report, to other Data Studio reports, or to any web-accessible resource.

To add text to your report, follow these steps:

  1. In the toolbar, click the insert_text **Text** icon to add a text box to the report canvas.

Alternatively, you can scroll and select the **Line** option from the **Insert** menu.

  2. Click, hold, and drag the corners or sides of the text box to reposition or reshape the text box on the report canvas.

  3. Drag the rotation handle at the top of the text box to rotate it.

  4. Click inside the text box to add your text in the box.


**Tip:** To add a title directly to a chart, turn on the **Show title** switch in the **Style** tab of the chart's **Properties** panel.

### Style the text

To style the text, follow these steps:

  1. Click the text box.
  2. Use the **Text Properties** options to change the font, size, color, padding, and other aspects of the text.



### Make the text scrollable

To make the text box scrollable, from the **Overflow settings** section, select the **Hidden** option in the **Scroll text** menu.

## Add images

Use images to add logos and graphics to your report.

To add an image to your report, follow these steps:

  1. In the toolbar, click the image **Image** icon.

Alternatively, you can scroll and select the **Image** option from the **Insert** menu.

  2. Select an image file from your hard drive, or enter the URL for an image that's hosted on the web. You can add most common image file formats, such as PNG, JPG, or SVG.

**Tip:** You can also drag images directly from your hard drive or a web page to the report canvas. Data Studio can't display copyrighted images from Google Images. If you add a copyrighted image, you'll see an overlay on top of your report. To remove the overlay, refresh the report.
  3. Click, hold, and drag the inside, corners, or sides of the image to reposition or resize it on the report canvas.

  4. Drag the rotation handle at the top of the image to rotate it.




Next, you can style the image.

### Style the image

To style the image on your chart, click the image to open the **Properties** panel. You can customize the image by using the **Setup** tab and **Style** tab options.

The **Setup** tab of the **Properties** panel includes the following options:

  * **Image file:** Displays the filename or web URL of the image. Click the filename or URL to upload a different image.
  * **Preserve aspect ratio:** When this option is enabled, the aspect ratio of the image is preserved when a report viewer resizes the report.
  * **Image link URL:** Enter a URL to make the image a clickable link. The link must begin with the HTTPS protocol.
  * **Accessibility - Alt text:** Add alt text to the image to make it accessible to screen readers. See the [Web Content Accessibility Guidelines (WCAG) guidelines on alt text](https://www.wcag.com/blog/good-alt-text-bad-alt-text-making-your-content-perceivable/#What_is_alt_text_and_who_does_it_benefit) for more information about writing alt text.



The **Style** tab of the **Properties** panel include the following options:

  * **Background:** Sets the image background color.
  * **Opacity:** Sets the image opacity. 100% opacity completely hides objects behind the image. 0% opacity makes the image invisible.
  * **Border color:** Sets the image border color.
  * **Border radius:** Adds rounded borders to the image background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the image border line thickness.
  * **Border style:** Sets the image border line style.
  * **Add border shadow:** Adds a shadow to the image's lower and right borders.

**Tip:** You can also add images from your data to tables by using the [`IMAGE` function](https://docs.cloud.google.com/data-studio/image).

## Add shapes

Use shapes, arrows, and callouts to create visual separation of data elements, banners, and other graphical effects.

To add a shape, an arrow, or a callout to your report, follow these steps:

  1. In the toolbar, click the shapes **Shape** icon and select a shape, an arrow, or a callout to add to the report canvas.

Alternatively, you can scroll and select the **Shapes** option from the **Insert** menu.

  2. Click, hold, and drag the corners or sides of the shape box to reposition or resize the shape on the report canvas.

  3. Drag the rotation handle at the top of the shape to rotate it.

  4. Click the shape to open the **Shape properties** panel and customize the shape's appearance.




## Add lines

Use lines, arrows, and connectors to indicate areas of note or to connect elements in a report.

To add lines, arrows, or connectors to your report, follow these steps:

  1. In the toolbar, click the diagonal_line **Line** icon.

Alternatively, you can scroll and select the **Line** option from the **Insert** menu.

  2. Click, hold, and drag your pointer to draw a **Line** , **Arrow** , **Elbow Connector** , or **Curved Connector** on the canvas.

  3. Click the line to open the **Line Properties** panel options to change the appearance of the line, arrow, or connector.


**Tip:** To connect two components with a line, drag each end of the line over the component until the colored anchor points appear. Next, connect the line ends to the anchor points. If you move the components, the line will adjust to keep them connected.

![A column chart on a report is connected by a line and an arrow to a box that displays placeholder text.](https://docs.cloud.google.com/static/data-studio/images/line-tool-2019-06-06.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
