---
url: https://docs.cloud.google.com/data-studio/themes/
title: Themes \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:54.400762+00:00
---

# Themes  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/themes/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Themes Stay organized with collections  Save and categorize content based on your preferences. 

Themes are a set of predefined color and style combinations you can apply to your reports. Applying a theme updates the style settings of your charts, tables, background color, and text, helping to ensure your reports are visually attractive and stylistically coherent.

## The default theme

All new reports start with a default theme. The colors and style settings of this theme are designed to be both attractive and accessible to viewers with color blindness.

## Apply a theme

  1. Edit the report.
  2. In the toolbar, click **Theme and layout**.
  3. In the THEME tab, click the theme that you want to apply.



## Create a custom theme

Create a custom theme by changing the current theme settings.

  1. [Sign in to Data Studio.](https://lookerstudio.google.com)
  2. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  3. In the toolbar, click **Theme and layout.**
  4. At the top of the panel, click **Customize**.
  5. Use the settings in the _Edit theme_ panel to customize the theme.



Then, customize the options in each section.

The **Edit theme** panel lets you customize the following settings:

### Primary styles

The settings in this section set the default background, text style, and border settings for the report.

  * **Primary font family** : Sets the default font family for text in the report, including text boxes, data labels, legend labels, and control labels.
  * **Primary font color** : Sets the default font color for text in the report, including text boxes, data labels, legend labels, and control labels.
  * **Report background color** : Sets a default page background color for all pages in report.



#### Component background and border

The settings in this section set the default background color, border color, border thickness, border shape, background opacity, and border line style for report components.

  * **Background color** : Sets the default background color for all components.
  * **Background opacity** : Sets the default opacity of the background for all components. 100% opacity makes the background solid, and 0% opacity makes the background fully transparent.
  * **Border color** : Sets the default outline color for all components.
  * **Border radius** : Sets the default rounded edges for all components. Choose a value from 0px (90° corners) to 20px (maximum rounding).
  * **Border weight** : Sets the default thickness of the border for all components.
  * **Border style** : Sets the default border line style for all components.
  * **Border shadow** : Sets the default appearance of the border shadow on all components.



### Accent styles

The settings in this section set the default settings for text accents, including table headers, filter control and date range control headers, and control "apply" buttons.

  * **Accent font family** : Sets the default font family for text accents.
  * **Accent font color** : Sets the default font color for text accents.
  * **Accent background color** : Sets the default background color for text accents.



### Textbox styles

The settings in this section set the default settings for text boxes.

  * **Font family** : Sets the default font family for text accents.
  * **Font color** : Sets the default font color for text accents.
  * **Background color** : Sets the default background color for text accents.
  * **Link text color** : Sets the default color for URLs in text boxes.
  * **Visited link text color** : Sets the default color for URLs that indicate that a user has clicked the URL.
  * **Hide textbox border** : When enabled, hides the border of text boxes.



### Data styles

The settings in this section determine the default appearance of data on charts.

#### Color By

  * **Series order:** Use the current theme to color the data according to its position in the chart. This option emphasizes the ranking of the data over the identity of the data. You can set specific colors by using the color picker.
  * **Dimension values:** This option colors each dimension value in the chart with the color that is specified in the **Manage dimension values** color map. This option ensures that your data uses color consistently, regardless of the position of that data in the chart.



#### Chart palette

Use the color pickers to set a palette for the charts on your report. These colors will determine the default colors for the data on your charts.

#### Chart styling defaults

  * **Chart title color** : Sets the default color for chart titles.
  * **"Others" color** : Sets the default color for the **Other** series when the **Group the rest as "Others"** setting is enabled in charts.
  * **Text contrast** : Sets the default text contrast for text that appears on charts.
  * **Bar border color** : Sets the default outline color for bars or columns in a chart.
  * **Bar width** : Sets the default width for each individual bar in an unstacked bar or column chart.
  * **Group bar width** : Sets the default bar width between 0% and 100% in a stacked bar or column chart.



#### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. The settings in this section determine the default actions for chart headers.

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Chart header color:** Sets the default font color of the chart header options.



#### Component grid style

The settings in this section determine the default grid style for chart grids.

  * **Grid color:** Sets the default color of the chart and table grids.



#### Positive and negative change style

The settings in this section determine the default style for charts that display positive and negative changes, such as [Gauge charts](https://docs.cloud.google.com/data-studio/gauge-chart-reference), [Scorecard charts](https://docs.cloud.google.com/data-studio/scorecard-reference), and [Waterfall charts](https://docs.cloud.google.com/data-studio/waterfall-chart-reference).

### Page navigation style

The settings in this section determine the display of page navigation components.

  * **Navigation font family** : Sets the default font family for page navigation text.
  * **Navigation font color** : Sets the default font color for page navigation text.
  * **Active navigation font color** : Sets the default font and background color in the page navigation panel to distinguish the report page that is open from the other pages in the report navigation. The background color appears with a lower opacity than the font.
  * **Navigation background color** : Sets the default background color for the page navigation panel.



## Override theme settings in a chart

Changing an individual component's style settings overrides the current theme settings. Those changes are preserved if you apply a new theme.

## Extract a theme from an image

You can generate a custom theme based on the colors in an image. This lets you coordinate the text and data colors with an image in your report, such as a logo or product photo.

To create a custom theme from an image that is already in the report, follow these steps:

  1. [Sign in to Data Studio.](https://lookerstudio.google.com)
  2. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  3. Right-click the image, then select **Extract theme from image**.



To create a custom theme from an uploaded or web-based image, follow these steps:

  1. [Sign in to Data Studio.](https://lookerstudio.google.com)
  2. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  3. Open the **Theme and Layout** panel.
  4. At the bottom of the Theme tab, click **Extract theme from image**.
  5. Upload an image or provide a link to an image on the web.



Data Studio will generate several themes from the colors in the selected image. Choose one, then click **Apply**.

## Reset a chart to the current theme

To restore a component you've changed back to the report theme:

  1. [Sign in to Data Studio.](https://lookerstudio.google.com)
  2. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  3. Select the component.
  4. In the properties panel on the right, select the _STYLE_ tab.
  5. At the bottom of the panel, click **Reset to report theme**.



Resetting a chart to the report theme won't reset any custom colors you've set in the [dimension value color map](https://docs.cloud.google.com/data-studio/the-dimension-value-color-map).

## Limits of themes

  * Custom themes aren't shared across reports. To reuse a custom theme in another report, make a copy of the report with the custom theme.
  * Themes apply to the entire report. It's not possible to apply different themes on separate pages of a report. You can, however, override themes by styling individual components.
  * You can have one custom theme at a time. Modifying an existing theme creates a new custom theme, overwriting any previous custom theme.
  * Changing themes doesn't override any custom styles you've applied to text boxes.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
