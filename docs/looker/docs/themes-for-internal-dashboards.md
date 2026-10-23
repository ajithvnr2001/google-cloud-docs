---
url: https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards/
title: Themes for internal dashboards and Looks \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:13.496980+00:00
---

# Themes for internal dashboards and Looks  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Themes for internal dashboards and Looks Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes how to use custom themes with Looker internal (non-embedded) dashboards and Looks. For information about using custom themes with embedded dashboards, Looks, and Explores, see the [Themes for embedded dashboards, Looks, and Explores](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores) documentation page.

You can use custom themes to customize the appearance of your internal (non-embedded) Looker dashboards and Looks. You can use themes to customize font family, text color, background color, button color, tile color, and other visual elements. Themes can be applied to both [user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards) and [LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards).

For example, you can create a "dark" theme to change the appearance of your dashboard.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-themes-example-720-v2.png)

You can define themes from the **Themes** page in the **Platform** section of the **Admin** panel.

This page describes the following:

  * User and instance requirements
  * How themes are applied to dashboards
  * How themes are applied to Looks
  * How themes are applied to dashboards that are downloaded as a PDF
  * How to create, copy, edit, delete, and set as default a custom theme



## User and instance requirements

To manage themes for your internal Looker dashboards and Looks, you must meet the following requirements:

  * Your Looker admin must enable the [**Internal Dashboard Theming** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#internal-dashboard-theming).
  * Your Looker user must have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles) or the [`manage_internal_themes` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_internal_themes).



## Applying a theme to a dashboard

To apply a theme to a dashboard, make sure that the dashboard is in [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards), and click **Style** to open the **Style** panel. Select a theme from the **Theme** field, and the theme will be applied to your dashboard. If you select **None** , and your instance has a [default theme](https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards#setting_a_default_theme), the default theme will be applied.

## Applying a theme to a Look

To apply a theme to a Look, make sure that the Look is in [edit mode](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#editing_looks), and click **Style** to open the **Style** panel. Select a theme from the **Theme** field, and the theme will be applied to your Look. If you select **Default** , and your instance has a [default theme](https://docs.cloud.google.com/looker/docs/themes-for-internal-dashboards#setting_a_default_theme), the default theme will be applied.

## Downloading dashboards

[Downloads of dashboards as a PDF](https://docs.cloud.google.com/looker/docs/downloading#downloading_a_dashboard_as_a_pdf) will show any applied custom theme.

## Creating a custom theme

To create a custom theme, in the **Themes** admin page, select the **Internal** tab and click **Add Theme**.

Next, add style and color specifications for each setting that you want to customize on the **New Theme** page. You can change any of the settings, which are described in the following sections. Select **Save Theme** to keep your changes and save your new theme.

### Theme

**Name** : The name for the theme must be unique and can contain only alphanumeric characters and underscores. If you enter spaces in the theme name, the spaces will be replaced with underscores when you save the theme.

### General

**Key Color** : Dashboards use this color for primary buttons and filter controls. Looks use this color for links, primary buttons, and selected tabs.

**Text Color** : The hexadecimal color code for the text on dashboards and Looks, and for banners and icons on Looks.

**Background Color** : The hexadecimal color code for the background of Looks and dashboards.

**Font Family** : The name of the font family. This font will be used for all the text on the dashboard, including tile titles, text tiles, and legends in visualizations. This font will also be used for all the text in an Explore. If there is a space in the name of the font, use quotes around the name, such as "Open Sans".

If you are using a [common web-safe font](https://www.w3schools.com/cssref/css_websafe_fonts.asp), you can just type the font name in the **Font Family** field and leave the **Font Source** field blank. If you want to use a less common font, enter the font name in the **Font Family** field and then use the **Font Source** field, described next, to provide a URL to the definition of the font that you want to use.

**Font Source** : Leave this field blank unless you want to use a custom font — a font that is not a [common web-safe font](https://www.w3schools.com/cssref/css_websafe_fonts.asp). The **Font Source** must be a complete URL that starts with `https` and points to the `url` value that is specified in the `src` argument of [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face). We recommend using a web open font format (`.woff`) file, since `.woff2` files aren't supported by Internet Explorer 11.

  * For example, for PT Sans Narrow, you could enter "PT Sans Narrow" in the **Font Family** field and then enter `https://fonts.gstatic.com/s/ptsansnarrow/v7/UyYrYy3ltEffJV9QueSi4RdbPw3QSf9R-kE0EsQUn2A.woff` in the **Font Source** field.



### Dashboard page

**Color Collection** : Optionally, you can choose a [color collection](https://docs.cloud.google.com/looker/docs/color-collections), which is a set of coordinating palettes that work well together. When you assign a color collection to a dashboard, all the data series in all the dashboard's tiles are colored according to the palettes in the collection, ensuring that the data series' colors are coordinated over the entire dashboard.

When you assign a color collection to a theme, the theme's color collection will override any color collection that was previously assigned to a tile. However, a theme's color collection won't override [customized colors](https://docs.cloud.google.com/looker/docs/bar-options#customizations) assigned to a data series, nor will it override [conditional formatting](https://docs.cloud.google.com/looker/docs/legacy-table-options#enable_conditional_formatting) applied to a table visualization.

**Title Font Size** : Optionally adjust the font size of the dashboard title from a set of predefined sizes in pixels.

**Note:** Margins on dashboards are responsive by default. Setting a specific value for margins overwrites the responsiveness, so be sure to test your settings on different window sizes and mobile devices.

**Margin Top** : Optionally set a specific value for the margin at the top of a dashboard. Choose from predefined options in a drop-down menu. Margins are measured in pixels (px).

**Margin Bottom** : Optionally set a specific value for the margin at the bottom of a dashboard. Choose from predefined options in a drop-down menu. Margins are measured in pixels (px).

**Margin Sides** : Optionally set a specific value for the margin on the sides of a dashboard. Choose from predefined options in a drop-down menu. Margins are measured in pixels (px).

### Dashboard tiles

**Title Color** : The hexadecimal color code for the following elements:

  * Dashboard title
  * Titles of dashboard tiles
  * Titles and header level 1 text of [Markdown](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_markdown_tiles) tiles
  * Text color of [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options)



**Text Color** : The hexadecimal color code for the following elements:

  * Text on the dashboard, including legends in visualizations
  * Subtitles and body text, with the exception of header level 1 text, of [Markdown](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_markdown_tiles) tiles
  * Header level 1, header level 2, and normal text on [text tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_text)
  * Tile icons in [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options)



**Text Body Color** : The hexadecimal color code for the following elements:

  * Body text, with the exception of header level 2 and header level 3 text, in [Markdown](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_markdown_tiles) tiles.
  * Body text in [text tiles](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_text_tiles)

**Note:** If values are set for both **Text Color** and **Text Body Color** , the color code set in **Text Body Color** will be used for body text in Markdown and text tiles.

**Background Color** : The hexadecimal color code for the background of all tiles except text tiles.

**Text Background Color** : The hexadecimal color code for the background of text tiles.

**Title Alignment** : Set the alignment of tile titles to left, right, or center.

**Title Font Size** : Optionally adjust the font size of dashboard tiles from a set of predefined sizes in pixels.

**Box Shadow** : Create a shadow around dashboard tiles using CSS syntax. You can select from a predefined box shadow or create a custom one. To create a custom box shadow, enter your chosen `horizontal-offset vertical-offset blur-radius spread-radius color `, and select **Enter Custom Styling** to apply your settings. A preview of the box shadow settings is shown to the right.

**Column Gap Size** : Optionally adjust the size of the space between columns of dashboard tiles from a set of predefined sizes in pixels.

**Row Gap Size** : Optionally adjust the size of the space between rows of dashboard tiles from a set of predefined sizes in pixels.

**Note:** By default, column and row gap size are responsive on a dashboard. Adjusting the column and row gap size overwrites the responsiveness of dashboard tiles. Test your dashboard gap settings on different window sizes or mobile devices, or on both.

**Border Radius** : Optionally adjust the border radius of dashboard tiles to create square or rounded corners.

## Editing a theme

For all themes, you can click the associated **Edit** button to update theme settings.

You can edit the settings just as you would when you create a new theme. For a description of the settings, see the theme settings described previously. Be sure to select **Save** to keep your updates.

## Copying a theme

You can copy an existing theme by selecting the theme's menu and selecting **Copy Theme**.

When you make a copy of a theme, the new theme's name defaults to the name of the copied theme, followed by "(copy)". Be sure to manually change this name to a new, unique name with only alphanumeric characters and underscores, and be sure to remove the parentheses.

You can edit the rest of the settings just as you would when you create a new theme. For a description of the settings, see the theme settings described previously. Be sure to select **Save** to keep all your theme settings.

## Deleting a theme

To delete a theme, select the theme's menu and select **Delete Theme**.

## Setting a default theme

If you set a theme as a default theme, that theme will be applied to any dashboard where the user selects the option **None** from the **Themes** field when in edit mode.

To set a theme as the default theme, select the theme's menu and select **Set as Default**.

To remove the default setting from the default theme, select the theme's menu and select **Remove Default**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
