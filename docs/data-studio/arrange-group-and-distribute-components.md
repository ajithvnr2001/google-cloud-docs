---
url: https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components/
title: Arrange, group, and distribute components \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:47.860882+00:00
---

# Arrange, group, and distribute components  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/arrange-group-and-distribute-components/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Arrange, group, and distribute components Stay organized with collections  Save and categorize content based on your preferences. 

In Data Studio, you can use the **Arrange** menu to control the layout and positioning of components in your report. Using the **Arrange** menu helps you organize visual elements, group them logically, and distribute them evenly to present your data clearly.

To apply options like alignment, distribution, or layering, select one or more components. Then, choose the action you want from the **Arrange** menu or right-click the selected components.

**Important:** Some of the features described on this page are not supported for responsive reports. Check the [Limitations of responsive reports](https://docs.cloud.google.com/data-studio/create-a-responsive-report#limitations) section of the **Create a responsive report** article for a list of unsupported features.

## Order options

The order options control how objects appear in front of or behind other object.

**Bring forward** —causes the selected component(s) to "take one step forward" in the display order.

**Send backward** —causes the selected component(s) to "take one step backward" in the display order.

**Bring to front** —causes the selected component(s) to appear in front of all the other components on the page.

**Send to back** —causes the selected component(s) to appear behind all the other components on the page.

## Alignment and distribution options

The alignment options help you arrange components so they line up, either vertically or horizontally. Select 2 or more components, then choose the horizontal or vertical alignment axis (top, bottom, right, left, center, etc).

Use the distribution options to adjust the amount of space vertically and horizontally between 3 or more components. This option uses the positions of the leftmost and rightmost components (for horizontal distribution), and the topmost and bottommost components (for vertical distribution) as "anchor points." It then moves the selected components so they are evenly spaced in the specified direction.

> Use the alignment options to first align your components horizontally or vertically. Then, while those objects are still selected, use the matching distribution options to space them evenly.

## Rotate components

You can rotate non-visualization components (such as shapes, text boxes, controls, and URL embeds) on the canvas to customize your report layout.

To rotate a component, select it and drag the rotation handle that appears at the top of the component.

Visualizations (charts) cannot be rotated.

## Make Report-Level / Make Page-Level

When you first create a component (chart, text box, shape, or image), it only exists in the page in which you create it. You can have a component appear on every page in a report by making it _report-level_.

To reverse this, use the Make **Page-Level** option (which only appears for report-level components). This makes a report-level component local to the current page.

> For example, to have your report title appear and a date range control appear on every page of your report, add those components to page 1 of your report. Then select them all and click **Arrange > Make Report-Level**.

> **Note** : By default, report-level components appear behind all other components on the page. To have report-level components appear in front of other components, edit the **Report-level component position** setting in the **[Theme and layout> LAYOUT](https://docs.cloud.google.com/data-studio/report-and-page-layout)** tab **.**

## Group / Ungroup

Grouping components has several benefits:

  1. It makes it easer to move them as a unit and to preserve their arrangement. For example, you might have a row of scorecards arranged just the way you want them. Creating a group with these components will prevent you from inadvertently jiggling just one of them. One for all and all for one!
  2. You can edit the **DATA** tab options of grouped components as a unit. For example, you can group a set of charts and change their data source. You can also configure the default date window and set filters on a group of components.
  3. When you include a report control, like a date range control or dimension filter, in a group of charts, that control applies just to the charts in that group.



To break up a group, right-click the group and select **Ungroup**.

> You can't group page-level components with report-level components.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
