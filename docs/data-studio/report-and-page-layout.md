---
url: https://docs.cloud.google.com/data-studio/report-and-page-layout/
title: Report and page layout \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:42.796093+00:00
---

# Report and page layout  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/report-and-page-layout/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Report and page layout Stay organized with collections  Save and categorize content based on your preferences. 

You can use report and page layout settings to customize the appearance and navigation of your Data Studio reports. These settings help you adjust page size, configure navigation, define layout grid options, and control the order of components at the report level. By tailoring these elements, you can create reports with optimal readability and an improved user experience. You can also customize individual pages within a report by changing their size and background color to meet specific design requirements.

**Important:** Some of the features described on this page are not supported for responsive reports. Check the [Limitations of responsive reports](https://docs.cloud.google.com/data-studio/create-a-responsive-report#limitations) section of the **Create a responsive report** article for a list of unsupported features.

To customize layout for the whole report:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar, click **Theme and layout**.
  3. On the right, select **LAYOUT**.

**Tip:** You can also use the **View** menu to change some of the following settings.

### View mode settings

These settings are in effect when the report is in view mode.

#### Header visibility

The header visibility settings control the behavior of the report header in view mode. The header contains things like the report title, the share button, and edit button.

  * **Always show:** The report header is always visible.
  * **Auto hide:** The report header appears briefly, then is hidden. Hover your mouse over the header area to redisplay it.
  * **Initially hidden:** The report header is hidden until you hover your mouse over the header area.



#### Navigation type

The navigation type settings control how the pagination controls appear in your report.

  * **Left**. Pages appear in a collapsible drawer in the left margin of your report.
  * **Tab**. Pages appear as tabbed links at the top of the report.
  * **Top Left**. Pages appear in a drop-down menu at the top left of the report.
  * **Hidden**. No page navigation is displayed.



Learn more about [adding pages and report navigation](https://docs.cloud.google.com/data-studio/add-pages-and-report-navigation).

#### Respect report theme

Turn this on to have the page navigation background and text colors appear in a style that matches your theme.

**Tip:** For dark themes (for example, _Constellation_ , _Lagoon_ , _Simple Dark_) uncheck **Has margin** to create an unbroken, "app-like" appearance.

#### Display mode

The display mode settings govern how your report fits in the browser window.

  * When **Fit to width** is enabled, if the canvas is smaller than the browser window, Data Studio scales the report canvas and its components to the width of the window.

  * When **Actual size** is enabled, regardless of browser window size, Data Studio displays the report components at their actual size.

  * When **Has margin** is enabled, Data Studio shows a margin area surrounding the report. Hiding the margin makes the report appear to occupy the entire window.




### Canvas Size

The canvas size settings control the width and height of your report on the screen. Select a preset size or enter custom display dimensions. Preset sizes include the following:

  * US letter (4:3) – Portrait
  * US letter (4:3) – Landscape
  * A4 (1.41:1) – Portrait
  * A4 (1.41:1) – Landscape
  * Screen (16:9) – Portrait
  * Screen (16:9) – Landscape



#### Custom canvas size

You can set the canvas size from a minimum of 10px by 10px to a maximum of 2000px wide by 10,000px high.

**Note:** you can override the report canvas size for individual pages. If you are on a page with its own canvas size, you won't see canvas size changes made on the **LAYOUT** tab until you navigate away from the current page.

### Snap To

The snap to settings can help you lay out the components of your report.

**Smart guides** display colored lines to help you align, resize, and space the selected components:

  * **Align components** : While moving a component, a red line appears to show when it is aligned with other components on the canvas.

  * **Resize components** : While resizing a component, blue lines appear to show when that component is the same length or width as other components on the canvas, and the current size in pixels is also shown.

  * **Space components** : While moving one or more components, blue lines appear when those components are spaced equally with other components on the canvas.




**Grid** aligns the selected components to the visible grid on the report canvas.

### Grid Settings

**Tip:** To display or hide the grid on the report canvas, use the **View > View grid menu**.

The minimum canvas grid size is 10 px. You can adjust this with the _Grid Settings_ settings. Increasing the grid size makes it easier to lay out your charts, controls, and other components.

  * **Size** sets the height and width of the grid squares.
  * **Padding** adds space within the grid squares. Use this to separate components in adjacent squares.
  * **Horizontal offset** sets left and right margins on the edges of your report. Use a positive number for left offset. Use a negative number for the right offset.
  * **Vertical offset** sets top and bottom margins on the edges of your report. Use a positive number for top offset. Use a negative number for the bottom offset. Use this to provide space for headers and footers.

**Note:** Changing grid settings has no effect on components already on the page. It only applies to new components you add, or to components that you move.

When you place a new component on the canvas that can fit into one or more grid squares, the component "snaps" in position and fills the grid, making it easy to size and line up new components in rows and columns. ("Fill the square" behavior begins with a grid size of 15 px or greater.)

See the report grid in action in this [sample report](https://datastudio.google.com/reporting/16SxZr2IwyoxBj7ngGyJqnbvAazATw7bG/page/39uT/preview).

### Report-level component position

This option determines how report-level components interact with other components on the page.

  * **Top** positions report-level components in front of all other components (similar to using the **Arrange > Order > Bring to front** menu).
  * **Bottom** positions report-level components behind all other components (similar to using the **Arrange > Order > Send to back** menu).



To customize an individual page in the report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Navigate to that page.
  3. In the menus, select **Page > Current page settings;** then, on the right, select **STYLE**.



### Page

Select a background color for the current page.

### Canvas Size

By default, the canvas size for each page in your report is set to **Auto** , which means it inherits the canvas size from the report's **Layout** settings. You can change the canvas size for the current page to a preset or custom size.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
