---
url: https://docs.cloud.google.com/data-studio/how-to-color-your-reports/
title: How to color your reports \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:44.483743+00:00
---

# How to color your reports  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/how-to-color-your-reports/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  How to color your reports Stay organized with collections  Save and categorize content based on your preferences. 

Consistent and meaningful use of color makes your reports more attractive and easier to understand. You can apply color and style options to a variety of aspects of a report, including static elements, such as page and component backgrounds, text fonts and font colors, chart borders, grids, and more. You can also apply colors to data elements, such as bars and lines, metric and dimension values, pie slices, and geographic regions.

This page describes the ways that you can work with color in Data Studio.

## Themes

Built-in color themes let you quickly create attractive and visually consistent reports. When you apply a theme, it updates the settings for all the static and data elements in the report at once, saving you time and effort.

You can customize a theme by changing its properties.

Learn more about [themes](https://docs.cloud.google.com/data-studio/themes).

## Style components individually

You can change color and style settings for individual components:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select one or more components.
  3. Select the **STYLE** tab.
  4. Change the desired style settings. If you've selected more than one component, you'll see only the settings that are common to all the selected components.



When you style an individual component, that component is no longer part of the report theme. If you apply a different theme to the component, it won't inherit the new theme's settings.

## Color your data

You can use the following techniques to color the data that appears in charts:

  * **Color by the dimension value**. For example, you decide that "France" should always represented in blue, no matter where it appears in the chart. The dimension value colors are set by the current report theme, but you can override them by editing the dimension value color map.
  * **Color by the order of the dimension data**. For example, say you want to set the first series in the chart to always be blue. You can set the series colors by editing individual charts.
  * **Use shades of a single color**. For example, you want to color the data series using a single color from your company's logo. This option is most effective when you don't need to show exact differences between values in the chart.



You can mix different techniques in the same report, depending on your goals and tastes.

Learn more about [data coloring techniques](https://docs.cloud.google.com/data-studio/color-your-data).

## The color picker

![The color picker showing the palette, theme palette, and custom color palette.](https://docs.cloud.google.com/static/data-studio/images/color-picker-2019-10-25.png)

Use the color picker to select colors for themes and components. The color picker has three sections:

  1. The standard color palette. This is the same for all components in every report.
  2. The **THEME** palette. This will change depending on your current theme.
  3. The **CUSTOM** color palette. Custom colors that you create appear here.



### Access the color picker

To open the color picker, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select a component and then open the **STYLE** tab, or customize the current theme.
  3. Click a color option to display the color picker, and then select the color that you want for that option. ![In the Style tab menu of a bar chart, a cursor hovers over the Chart background icon to select a background color for the chart grid.](https://docs.cloud.google.com/static/data-studio/images/color-swatch2-2019-10-25.png)



### Create custom colors

![The custom color gradient picker displays the hex of the selected color, #3186ff.](https://docs.cloud.google.com/static/data-studio/images/color-gradient-picker-2016-02-17.png)

Click ![Add icon](https://docs.cloud.google.com/static/data-studio/images/gmaddcircleoutlinegrey60048dp-2020-03-09.png) in the **CUSTOM** colors row of the color picker to create a custom color. Click anywhere in the color bars to pick a base color, and then use the sliders to adjust the shade. You can also enter a color hex value to render that color. The current color's hex value can also be used to exactly duplicate a custom color in another component. For example, you can copy a color hex value from one component and paste it into another component's color picker to set it to the same color.

### Color gradients

![The custom gradient dialog configured for a linear, 90-degree gradient with 3 colors steps, fading left to right from dark blue to white.](https://docs.cloud.google.com/static/data-studio/images/gradient-control-2015-09-01image.png)

When one color fades into another, the effect is called a gradient. You can use a color gradient in a component's **Background** color property. To set a gradient, follow these steps:

  1. Select a component and then click **STYLE**.
  2. Click **Background** ![Background color icon](https://docs.cloud.google.com/static/data-studio/images/background-color-icon-2015-09-01.png).
  3. Click **Gradient.**
  4. Select the boxes at the beginning and end of the gradient bar, and then click the color drop-down menu to set the starting and ending colors for the gradient.
  5. To add more color steps to the gradient, click **Add**.
  6. To remove a color step from the gradient, click **Remove**.
  7. Use the **Type** menu to set the overall appearance of the gradient, either **Linear** or **Radial**.
  8. Use the **Angle** menu to set the direction of flow for the gradient: 
     * **Center**
     * **Top left**
     * **Top right**
     * **Bottom left**
     * **Bottom right**



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
