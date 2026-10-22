---
url: https://docs.cloud.google.com/looker/docs/modern-ui/
title: Using the modern user interface \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:35.700307+00:00
---

# Using the modern user interface  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/modern-ui/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using the modern user interface Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Provide feedback or report issues with this preview feature by completing the [Looker Modern UI - Preview Issues](https://docs.google.com/forms/d/e/1FAIpQLSe6INpo3hdIevRd7hIXUANTF_7GnA777b-XWJk7jGpl-k-dUA/viewform) form.

With modern visualization themes and dashboard styles, you can create clean, professional charts and streamlined dashboards with improved data density. By applying updated typography, intentional color hierarchy, and adaptive layouts, modern styling enhances data legibility and provides a cohesive viewing and editing experience.

To use these styling options, the [**Modern User Interface** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#modern_user_interface) on the **Preview** page of the Admin panel must be enabled. This preview feature is supported on all Looker deployment types, including Looker (original) and Looker (Google Cloud core), and is enabled by default.

When enabled, the **Modern User Interface** preview feature introduces the following settings and updates:

  * Modern visualizations: The **Visualization Theme** setting for Looker charts lets users pick a new Modern visualization theme for Looker charts.
  * Modern dashboards: The **Dashboard style** setting for dashboards lets users pick a new Modern style for Looker dashboards.



## Modern visualizations

When the **Modern User Interface** preview feature is enabled, you can use the **Visualization Theme** setting to select Modern or Classic visualization themes for your Looker charts. Choosing the **Modern** visualization theme helps you create clean, readable, and professional charts with a clear and modern look and feel.

The following image shows a comparison between the Modern and the Classic visualization themes.

![](https://docs.cloud.google.com/static/looker/docs/images/modern-vs-classic.png)

### Supported chart types

During the preview launch, the Modern visualization theme supports Looker's most popular built-in chart types:

  * Cartesian charts: [column](https://docs.cloud.google.com/looker/docs/column-options), [bar](https://docs.cloud.google.com/looker/docs/bar-options), [line](https://docs.cloud.google.com/looker/docs/line-options), and [area](https://docs.cloud.google.com/looker/docs/area-options) charts
  * Pie charts: [pie](https://docs.cloud.google.com/looker/docs/pie-options) and [donut multiples](https://docs.cloud.google.com/looker/docs/donut-multiples-options) charts
  * [Single value](https://docs.cloud.google.com/looker/docs/single-value-options) charts
  * Map charts: [static map (points)](https://docs.cloud.google.com/looker/docs/map-points-options), [static map (regions)](https://docs.cloud.google.com/looker/docs/map-regions-options)
  * [Table](https://docs.cloud.google.com/looker/docs/table-options) charts
  * [Word cloud](https://docs.cloud.google.com/looker/docs/word-cloud-options) charts



All other chart types (such as boxplot, Google Maps, map (legacy), funnel, scatter, table (legacy), timeline, and waterfall) aren't supported by the Modern visualization theme. If a Look or an Explore uses an unsupported chart type, the **Visualization Theme** setting won't appear in its edit menu.

### How Modern and Classic visualization themes differ

The Modern visualization theme is designed to optimize chart layout, typography, colors, and interactive behaviors.

The following table describes how visualizations that use the Modern theme differ from those that use the Classic style.

Visual element | Classic visualization theme | Modern visualization theme  
---|---|---  
**Typography** | 

  * Uses a single, uniform font (such as Roboto Regular) for all chart elements.
  * All chart text, including titles and values, shares the same dark color.
  * Labels on axes frequently rotate diagonally or are displayed with ellipses (...) to fit the space.

| 

  * **Google Sans:** Applied to titles, headers, and legends using intentional weight and color gradation for a clear hierarchy.
  * **Google Sans Text:** Applied to smaller labels and axes for legibility.
  * **Monospaced values:** Numbers along chart axes use a monospaced font to maintain clean vertical alignment.
  * **Adaptive scaling:** Labels resize dynamically and avoid diagonal or vertical rotations whenever possible.

  
**Default colors** | 

  * Defaults to the **Shoreline** [color collection](https://docs.cloud.google.com/looker/docs/color-collections) for new charts.
  * When the [**Default Visualization Colors** Admin setting](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#default_visualization_colors) is set to a color collection other than its default (in other words, set to a color collection other than Shoreline), that setting overrides the Shoreline color collection in new charts.
  * The Modern color collection isn't available for charts when the Classic visualization theme is selected.

| 

  * Defaults to the [**Modern** color collection](https://docs.cloud.google.com/looker/docs/color-collections#the_modern_color_collection) for new charts.
  * When the [**Default Visualization Colors** Admin setting](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#default_visualization_colors) is set to a color collection other than its default (in other words, set to a color collection other than Shoreline), that setting overrides the Modern color collection in new charts.
  * Automatically resolves and applies the optimal palette type (categorical, sequential, or diverging) based on your query's data.

  
**Cartesian charts (bar, column, line, area)** | 

  * Gridlines and axis lines are highly visible (dark grey).
  * Columns and bars render with sharp, 90-degree corners.

| 

  * Gridlines and axis lines are muted with a lighter, softer color to focus attention on the data.
  * Columns and bars render with rounded outer edges (4px corner radius).
  * Column and bar spacing is expanded to maintain clear separation between segments.

  
**Pie and donut charts** | 

  * Slices render with sharp corners and rest flush against each other.

| 

  * Slices feature rounded outer edges and subtle spacing between them.
  * Legend labels display values, percentages, or both side-by-side.

  
**Single value charts** | 

  * Standardized spacing that might scale in unexpected ways.

| 

  * Generous padding and adjusted line-heights to ensure that titles, values, and comparison labels are separated and scannable.

  
**Interactions and tooltips** | 

  * Basic hover actions without dynamic movement.
  * Tooltips feature sharp corners and standard grey backgrounds.

| 

  * Holding the pointer over or selecting pie slices causes them to subtly expand ("swell") and separate from the chart.
  * Holding the pointer over a line chart slightly thickens that specific line while dimming the others.
  * Tooltips feature rounded corners, refined spacing, and darker backgrounds for high contrast. Supports touchscreens and mobile devices.
  * Dashboard cross-filtering logic and drill-down behaviors remain unchanged.

  
  
### The Modern color collection

If the [**Modern User Interface** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#modern_user_interface) is enabled, you will see the Modern color collection as an option for the [**Default Visualization Colors** setting](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#default_visualization_colors). Even if you don't select the Modern color collection for this setting, if you select the Modern visualization theme for a visualization, it will use the Modern [color collection](https://docs.cloud.google.com/looker/docs/color-collections) by default.

The Modern color collection was developed with the following goals:

  * Ensure sufficient contrast between chart elements and backgrounds for visibility and accessibility.
  * Use a color sequence that is differentiable (has distinct visual contrast) for individuals with color vision deficiencies.
  * Prevent distraction and maintain focus on data by reducing the intensity of the color palette.



### Enabling the Modern visualization theme (for admins)

To make the Modern visualization theme available on an instance, the [**Modern User Interface** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#modern_user_interface) on the **Preview** page of the Admin panel must be enabled. The preview feature is enabled by default.

When the **Modern User Interface** feature is enabled, the Modern theme becomes the default theme for new query charts. However, charts that are created before the **Modern User Interface** feature is enabled don't automatically adopt the Modern theme.

If you want to set the Modern theme's color collection as the default palette for all new visualizations in Looker, including visualizations that don't support visualization themes, you can select it in the [**Default Visualization Colors** setting](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#default_visualization_colors) on the **Settings** page of the Admin panel once the **Modern User Interface** preview feature is enabled. This setting enables only the color palettes, not the other features of the Modern theme. If you enable the **Modern User Interface** feature and want new visualizations of all chart types to use the same default visualization colors, select **Modern** for this setting.

### Choosing themes for individual charts

To set a visualization theme for a chart, you must have the proper permissions and use the chart settings.

#### User permissions

To use and save visualizations with the Modern visualization theme, you must have the following Looker permissions:

  * **To configure Modern styles in Explores** : Users must have the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) permission for the relevant models.
  * **To save Modern visualization styles to individual Looks** : Users must have the [`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) , [`save_content`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_content), and [`save_looks`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_looks) permissions. Users also must have the **Manage Access, Edit** access level for any Looks that they want to edit.



#### Chart settings

When the **Modern User Interface** feature is enabled, you can change the visualization theme by using the following steps:

### Table charts

For table charts, you can choose which visualization theme you'd like applied by making a selection in the **Table Theme** field.

  1. If you are viewing a Look, click the **Edit** button to edit the Look.
  2. In a Look or an Explore, in the **Visualization** tab, click **Edit** to open the edit menu.
  3. Navigate to the **Plot** tab of the edit menu.
  4. In the **Table Theme** drop-down field, select **Modern** or one of the other [table themes](https://docs.cloud.google.com/looker/docs/table-options#table_theme). The visualization updates to show the chosen theme.
  5. Once you have selected your preferred theme, you can save the visualization as a Look or add it to a dashboard. Your theme selection is saved as part of the visualization's configuration.



### Other charts

For column, bar, line, area, pie, donut multiples, or single value charts, you can choose which visualization theme you'd like applied by making a selection in the **Visualization theme** field.

  1. If you are viewing a Look, click the **Edit** button to edit the Look.
  2. In a Look or an Explore, in the **Visualization** tab, click **Edit** to open the edit menu.
  3. Navigate to the **Plot** tab of the edit menu.
  4. In the **Visualization theme** drop-down field, select **Modern** or **Classic**. The visualization updates to show the chosen theme.
  5. Once you have selected your preferred theme, you can save the visualization as a Look or add it to a dashboard. Your theme selection is saved as part of the visualization's configuration.



### Dashboard tiles

  1. Place the dashboard in [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. [Open the **Edit Tile** window](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_a_tiles_query_or_look) for the tile.
  3. in the **Visualization** tab, click **Edit** to open the edit menu.
  4. Navigate to the **Plot** tab of the edit menu.
  5. In the **Visualization Theme** drop-down field, select **Modern** or **Classic**. The visualization updates to show the chosen theme.
  6. Once you have selected your preferred theme, you can save the change by clicking **Save** on the **Edit Tile** window and then clicking **Save** on the dashboard.



### LookML dashboard elements

The Modern and Classic themes can be used in [LookML dashboard elements](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element) for the supported chart types.

To use themes, use the `modern2026` parameter, and set it to `true` for the Modern theme or to `false` for the Classic theme.

To apply the Modern color collection to a dashboard element, use the `collection_id` parameter and set it to `looker_2026`.

### Custom style retention

When you apply the Modern visualization theme to an existing Explore or Look, Looker updates your visualization's underlying styles without discarding your custom configurations. Any custom formatting choices that you have explicitly saved take priority over the new theme defaults.

  * **Custom styles (preserved)** : If you have manually customized specific formatting properties (such as entering custom color codes, adjusting axis bounds to specific numbers, or manually defining chart series names), Looker preserves these overrides exactly as they are. Your custom choices won't be overwritten by the Modern theme.
  * **Untouched properties (updated)** : Any style settings that you didn't modify (properties left at their default states) are automatically upgraded to the Modern theme's styling, such as the new fonts, muted gridlines, and rounded corners.



For example, if you have a Classic theme column chart where you customized the column colors to match your company's brand, switching to the Modern theme preserves those specific brand colors. However, the chart's fonts, gridline styling, and column corners will still automatically upgrade to the Modern style.

#### Resetting to defaults

If you want to completely apply the Modern theme to a visualization that contains custom styles, you can reset customized properties back to their default states:

  1. From a [Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#editing_a_looks_source_query) or [dashboard](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_a_tiles_query_or_look), enter edit mode for the visualization.
  2. In the **Edit** menu, locate the properties that you want to reset (such as custom color selections or font sizes).
  3. Clear the custom values or select the default settings to remove the override. The properties will immediately inherit the Modern theme's defaults.



### Known limitations

While the Modern visualization theme is in preview, the following limitations are present:

  * The Modern theme is available only for the chart types that are listed in the Supported chart types section. All other built-in Looker visualizations, including maps, will render using the Classic theme.
  * The Modern visualization theme applies only to built-in Looker visualizations. It does not affect custom visualizations that are developed through the Looker Extension Framework or those installed from the Looker Marketplace.
  * Visualization themes can't be edited programmatically through the Looker API or the Embed SDK.



## Modern dashboards

When the **Modern User Interface** preview feature is enabled, new dashboards default to using the Modern dashboard style. Using the Modern dashboard style creates dashboards with a modern, streamlined appearance and an emphasis on data density. Alternatively, you can use Looker's pre-existing Classic dashboard style. Use the **Dashboard style** setting to select Modern or Classic dashboard styles for your dashboards.

Using the Modern dashboard style doesn't automatically update the charts in the dashboard to the Modern visualization theme. To use the Modern visualization theme in dashboard tiles, you must enter edit mode for the dashboard and edit each tile that uses a supported chart type to use the Modern visualization theme.

The following image shows an example of a dashboard that uses the Modern dashboard style with tiles that use the Modern visualization theme.

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-modern-example.png)

The Classic dashboard style is shown in the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) documentation.

### How Modern and Classic dashboard styles differ

The Modern dashboard style is designed to improve data density and provide a more precise, cohesive editing experience.

The following table describes how dashboards that use the Modern style differ from the Classic style.

Element | Classic dashboard style | Modern dashboard style  
---|---|---  
**Layout and density** | 

  * Uses a standard grid layout with wider spacing between tiles.

| 

  * **High-density design:** Streamlined interface that reduces visual clutter and focuses on data.

  
**Look and feel** | 

  * Features legacy Looker UI elements and navigation styling.

| 

  * **Modern aesthetic:** A clean design that's aligned with Google's design standards.
  * **Refreshed navigation:** Updated top and left navigation bars for a cohesive experience with the [new Explore experience](https://docs.cloud.google.com/looker/docs/creating-and-editing-new-explore-experience).

  
  
### Enabling the Modern dashboard style (for admins)

To make the Modern dashboard style available on an instance, the [**Modern User Interface** preview feature](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features#modern_user_interface) on the **Preview** page of the Admin panel must be enabled. The preview feature is enabled by default.

Dashboards that are created before the **Modern User Interface** feature is enabled retain the Classic dashboard style, but they can be updated to the Modern style by using the **Dashboard style** setting. Dashboards that are created after the **Modern User Interface** feature is enabled default to the Modern dashboard style.

### Setting a style for individual dashboards

To set a dashboard style, you must have the proper permissions and use the dashboard **Settings** menu.

#### User permissions

To use and save dashboards with the Modern style, users must have the [`save_dashboards`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_dashboards) Looker permission. Users also must have the **Manage Access, Edit** access level for any dashboards that they want to edit.

#### The Dashboard style setting

When the **Modern User Interface** feature is enabled, the Modern dashboard style is the default for new dashboards. You can set the dashboard style for new or pre-existing dashboards by using the following steps:

### User-defined dashboard

  1. Place the dashboard in [edit mode](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#entering_edit_mode_in_dashboards).
  2. Open the dashboard's [**Settings** menu](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#editing_dashboard_settings).
  3. In the **General** tab of the **Settings** menu, use the **Dashboard style** setting to select the **Modern** or the **Classic** dashboard style from the drop-down options. The dashboard updates to show the selected style.
  4. Click **Save** in the **Settings** menu.
  5. Click **Save** on the dashboard to apply the selected style.



### LookML dashboard

To use the Modern dashboard style, set the `style` dashboard parameter to `modern`. To use the Classic dashboard style, set the `style` dashboard parameter to `classic`.

### Embedded dashboards

For [embedded dashboards](https://docs.cloud.google.com/looker/docs/viewing-embedded-items) that use [embedded themes](https://docs.cloud.google.com/looker/docs/themes-for-embedded-dashboards-and-explores), some Modern styling will look different than styling in non-embedded dashboards. We recommend using the Classic dashboard style for embedded dashboards that use embedded themes.

## What's next:

  * [Creating visualizations and graphs](https://docs.cloud.google.com/looker/docs/creating-visualizations): Learn the basics of creating visualizations in Looker.
  * [Color collections](https://docs.cloud.google.com/looker/docs/color-collections): Explore the different color collections available in Looker, including the new Modern collection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
