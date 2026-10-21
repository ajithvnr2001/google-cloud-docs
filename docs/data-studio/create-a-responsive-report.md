---
url: https://docs.cloud.google.com/data-studio/create-a-responsive-report/
title: Create a responsive report \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:45:42.197151+00:00
---

# Create a responsive report  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/create-a-responsive-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Create a responsive report Stay organized with collections  Save and categorize content based on your preferences. 

A responsive report scales well across many different screen sizes. Choose this report type if you expect your users to regularly view the report on a tablet or other mobile device.

## Create a responsive report

Follow these steps to create a responsive report:

  1. [Sign in to Data Studio.](https://datastudio.google.com)
  2. Click ![](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Create** and then select **Report**.
  3. [Add a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report) to the report.
  4. By default, the report type is set to **Freeform**. To use a responsive report, select the **Responsive** report type.
  5. Add sections, charts, and controls to your report, as described in the following sections.



## Add sections to your report

In a responsive report, components (charts and controls) are grouped into sections. Sections let you group together similar components, as well as filter on all section components at once.

### Create a section

To create a new section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the + button before or after an existing section. This button appears only when you hover over it.  
  
If your report doesn't contain any sections yet, click **Insert** , and then select a chart type. Data Studio will create a new section and put the new chart inside.



### Add charts and controls to a section

To create a new chart or control component in a section, follow these steps:

  1. [Edit your report.](https://docs.cloud.google.com/data-studio/edit-a-report)
  2. If the section is empty, click either the **Add chart** or the **Add control** button in the center of the section.
  3. If the section is not empty, click either the **Add chart** or the **Add control** button on the right edge of the section. These buttons appear when you hover over a section.



Data Studio arranges the components in a row of columns. You can drag a component to the left or right of an existing component to create a new column, or drag a component to a position that is higher or lower than an existing component to add the component to the column.

To move an existing chart or control from one section to another, drag the component to the section.

### Resize a section

The height of a section is determined by the height of its components.

The width of a section is not editable. Each section will always be the full width of the screen.

#### Change section height

Each section will automatically scale its height to the tallest column in the section.

To make a section taller, find the tallest column in the section. Then, either add components to the column or increase the height of one or more components in the column.

To make a section shorter, find the tallest column in the section. Then, either remove components from the column or decrease the height of one or more components in the column.

### Add a filter to a section

To add a filter to a section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the section, making sure not to click any of the components.  
  
If the section is crowded with components, try clicking the six-dot icon on the left of the section. This icon appears when you hover over a section.
  3. Open the **Properties** menu and select the **Setup** tab.
  4. In the **Filter** section, under **Filter On This Group** , click **\+ Add a filter**.



By default, filters in a section will apply to the entire report.

#### Limit section filters to a section

To limit filters in a section to apply to only the components in the section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the section, making sure not to click any of the components.  
  
If the section is crowded with components, try clicking the six-dot icon on the left of the section. This icon appears when you hover over a section.
  3. Open the **Properties** menu and select the **Setup** tab. 
     * To limit filters in this section to apply to only the components in the section, clear the **Apply filter controls to page** checkbox.
     * To allow filters in this section to apply to the rest of the report, select the **Apply filter controls to page** checkbox. This checkbox is selected by default.



### Style a section

To customize the style of a section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Hover over a section, and select **Open Style Menu** from the options on the right hand side of the section.
  3. Change the style settings. These settings will apply to every component in the section.

When you style a section, that section is no longer part of the report theme. If you apply a different theme to the report, the section won't inherit the new theme's settings.




### Reorder sections

To reorder sections, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the six-dot icon on the left of the section that you want to reorder.
  3. Drag the section to a new position to reorder the section.



### Change the data source for a section

To change the data source for all components in a section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the section, making sure not to click any of the components.

If the section is crowded with components, try right-clicking on the six-dot icon on the left of the section. This icon appears when you hover over a section.

  3. Open the **Properties** menu and select the **Setup** tab.

  4. In the **Data source** section, click the data source name to select another data source.




### Delete a section

To delete a section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Right-click the section, making sure not to click any of the components.

If the section is crowded with components, try right-clicking on the six-dot icon on the left of the section. This icon appears when you hover over a section.

  3. Click **Delete**.




## Preview a report for mobile devices

You can preview how your report will look on mobile devices such as a phone or tablet. To view a preview of your report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click the downward arrow button next to the View button on the toolbar, then select a device type. Data Studio opens a preview of your report.
  3. To change the device size, click the **Phone** , **Tablet** , or **Large** **Screen** buttons in the bottom right corner of the preview.
  4. To exit the preview, click the **Exit Preview** button in the bottom right corner of the preview.



## Change report types

You can change the layout mode of a report between freeform and responsive. To change the layout mode of your report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Click **Theme and layout**.
  3. Click the **Layout** tab.
  4. In the **Layout mode** section, select either **Freeform** or **Responsive**.



Note the following limitations and considerations when you change layouts:

  * Changing layouts may cause some formatting options to be lost — including chart positions, background fills, and borders.
  * You can only change from freeform layout to responsive layout if your report has one or fewer components per page. If your report does not meet this requirement, instead create a new responsive report and copy components from the freeform report into the new responsive report.



## Limitations of responsive reports

The following actions and settings are not supported for responsive reports:

  * [Adding lines or arrows](https://docs.cloud.google.com/data-studio/add-text-images-lines-and-shapes-to-your-reports).
  * [Configuring the canvas size](https://docs.cloud.google.com/data-studio/report-and-page-layout) and [configuring the page-level canvas size](https://docs.cloud.google.com/data-studio/report-and-page-layout): The canvas size is automatically set to fit the components of the report.
  * [Configuring the **Grid Settings**](https://docs.cloud.google.com/data-studio/report-and-page-layout): The grid is automatically set to a 12-column layout that responds to the viewer's device size.
  * [Configuring the **Snap To** settings](https://docs.cloud.google.com/data-studio/report-and-page-layout): Components are automatically arranged and aligned.
  * [Grouping components](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components): Instead of grouping components, add components to a section. You can apply filters at the page level or section level.
  * [Making a component report-level](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components).
  * [Rotating components](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components#rotate).
  * [Sending components forward or backward](https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components): In responsive reports, components can't overlap.
  * [Setting the **Display mode** to **Fit to Width** or **Actual size**](https://docs.cloud.google.com/data-studio/report-and-page-layout): Responsive reports scale to the width of the viewer's device.
  * [Setting the report-level component position](https://docs.cloud.google.com/data-studio/report-and-page-layout).
  * Two or more users [editing the same report](https://docs.cloud.google.com/data-studio/edit-a-report) simultaneously.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
