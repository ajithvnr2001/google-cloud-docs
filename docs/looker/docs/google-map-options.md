---
url: https://docs.cloud.google.com/looker/docs/google-map-options/
title: Google Maps chart options \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:32.842776+00:00
---

# Google Maps chart options  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/google-map-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Google Maps chart options Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes visualization options for Looker. For information about Data Studio visualizations, see [Types of charts in Data Studio](https://docs.cloud.google.com/looker/docs/studio/types-of-charts-in-looker-studio).

Google Maps charts let you visualize geographic data on responsive and interactive maps, and they provide significant control over the way that map points are plotted. Google Maps charts have similar functionality to the [Map chart](https://docs.cloud.google.com/looker/docs/map-options) visualization type.

## Viewing a Google Maps chart

When users view a Google Maps chart, several icons appear on the chart that let them interact with the visualization.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-chart-icons-2212.png)

  1. **Zoom in and Zoom out icons** : Click the **+** icon to zoom in and the **-** icon to zoom out on the map view.
  2. **Toggle fullscreen view icon** : Click the **Toggle fullscreen view** icon to expand the map to fullscreen. Press the `esc` key on your keyboard or click the icon again to return to standard view.
  3. **Drag Pegman onto the map to open Street View** : Drag the Pegman icon to any location on the chart to switch the map to [Street View](https://support.google.com/maps/answer/3093484) for that location. Click the back arrow at the upper left of Street View to return to the chart.
  4. **Distance scale** : At the bottom of the chart, there is a scale in meters or kilometers for the current view of the map.
  5. **Keyboard shortcuts** : Click **Keyboard shortcuts** at the bottom of the chart to see a window with available keyboard shortcuts for interacting with the chart.
  6. **Value color scale** : If measures are plotted on the chart, a color scale appears at the the bottom left of the chart to indicate the range of colors between the minimum and maximum values. The settings in the **Value menu** can affect the appearance of the value color scale.
  7. **Open this area in Google Maps** : Click the Google logo at the bottom left of the chart to open the map in Google Maps. Google Maps opens in a new browser tab.



## Building a Google Maps chart

To create a Google Maps chart, your query must include at least one of the following fields:

  * A dimension based on latitude and longitude data. This is defined by a LookML developer as a dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location).
  * A dimension with a map layer assigned to it. LookML developers can add a [built-in map layer](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name#built-in_map_layers), a custom map layer by providing a URL to a TopoJSON file, or a [custom map layer](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer) to a dimension using the [`map_layer_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) parameter.
  * A zip code dimension, which automatically has a US zip code map layer assigned to it. This is defined by a LookML developer as a dimension of [`type: zipcode`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode). Zip code regions are based on the US zip code tabulation areas (ZCTAs). There may not be a one-to-one correspondence between zip codes and the ZCTAs used for map visualizations. It is possible that not all points will be visualized in the map.



Limit the precision of latitude and longitude data coordinates to no more than five to six decimal places. If coordinates exceed seven decimal places, the map won't display any data points.

To build a Google Maps chart, select the **Google Maps** visualization type in the **Visualization** bar. You can also edit your map visualization in the visualization menu. Click **Edit** in the upper right corner of the **Visualization** bar.

The options described on this page are available in the different tabs of the **Edit** menu. Options may be grayed out or hidden if they conflict with other settings that you have chosen.

## Plot menu options

The **Plot** tab lets you select the way that your location data is plotted. Each choice has slightly different formatting options, as appropriate for the plot type. **Plot** options also differ depending on whether a [map layer](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) is defined in the LookML for your dimension.

For visualizations that don't contain zip code dimensions or dimensions that have a defined map layer, the following **Plot** options are supported:

  * **Points**
  * **Automagic Heatmap**
  * **Density Heatmap**
  * **3D Heatmap**
  * **Connect with Lines**
  * **Connect with Areas**
  * **Custom Tooltip**



Each of the **Plot** menu options is described in this section.

### Points

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-points-option-2212.png)

You can plot each row in an underlying data table as a discrete point on the map.

For this plot type to work properly, you must select at least one dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

A location dimension by itself will place points of uniform size and color. Adding a measure to the underlying data table enables the points to be scaled by color or size in the **Points** menu tab.

### Automagic Heatmap

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-automagic-heatmap-option-2212.png)

An automagic heatmap displays data as a heatmap grid, which readjusts in granularity when viewers zoom in or out on the map.

For this plot type to work properly, you must select both a dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location) and a measure.

To display data in a query as a heatmap grid, Looker divides the visible map into equal squares and then calculates which values in your data fit into each square. The squares are colored according to a measure that you choose. Zooming this map in or out will prompt Looker to recalculate the grid, so that the granularity is appropriate to the zoom level.

> The **Automagic Heatmap** option re-queries your data to construct the heatmap grid. A location dimension typically displays as distinct points with one latitude and longitude coordinate, but when you use an automagic heatmap, the dimension changes to the bounding boxes ("Heatmap region from ... to ..") of each square in the grid.

### Density Heatmap

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-density-heatmap-option-2212.png)

For this plot type to work properly, you must select at least one dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

A density heatmap is useful for displaying large amounts of location data with many points clustered densely together. The density heatmap displays the data using color intensity and a color scale to convey the concentration of data points in each area.

### 3D Heatmap

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is part of the **Google Maps Enhancements** preview feature. This preview feature must be enabled by a Looker admin on the [Admin settings - Preview Features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) page. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`looker-viz-preview-external@google.com`](mailto:looker-viz-preview-external@google.com). 

Creates a 3D heatmap out of geographic points. A 3D heatmap aggregates data points into hexagonal cells, using both color and height (elevation) to represent density or numerical values.

![](https://docs.cloud.google.com/static/looker/docs/images/3d-heatmap-2608.png)

For this plot type to work properly, you must select at least one dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

### Connect with Lines

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-connect-with-lines-option-2212.png)

For this plot type to work properly, you need two dimensions of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

The **Connect with Lines** option takes two fields of `type: location` from your query and then connects them together with a line in the visualization. Adding a measure to the query lets you add a color scale to the lines.

### Connect with Areas

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-connect-with-areas-option-2212.png)

For this plot type to work properly, you need one dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location). Optionally, you can add a measure.

The **Connect with Areas** map visualization takes one field of `type: location` and connects all the points in the order in which you've sorted them with lines, forming the boundaries of an area on the map. Adding a measure to the query lets you format the size and color of the individual location points that bound the area in the **Value** menu tab.

### Custom Tooltip

You can click the **Custom Tooltip** switch to configure tooltips within the [Explore visualization editor](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) by using a combination of UI settings and an HTML editor that supports Liquid templating. [Learn more about **Custom Tooltips**](https://docs.cloud.google.com/looker/docs/custom-tooltips).

## Map menu options

### Map Style

**Map Style** lets users change the type of background map, and whether map labels (like cities and streets) should be displayed. This option features a drop-down menu with a list of choices:

  * **Light:** Light-colored map designed to provide geographic context while highlighting your data.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-light-style-2210.png)

  * **Light (No Labels):** Same as **Light** , except the map omits labels such as city names.

  * **Dark:** Dark-colored map designed to provide geographic context while highlighting your data.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-dark-style-2210.png)

  * **Dark (No Labels):** Same as **Dark** , except the map omits labels such as city names.

  * **Satellite:** Map displaying global satellite and aerial imagery.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-satellite-style-2210.png)

  * **Satellite (No Labels):** Same as **Satellite** , except the map omits labels such as city names.

  * **Streets:** General-purpose map that emphasizes legible styling of road and transit networks.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-streets-style-2210.png)

  * **Outdoors:** General-purpose map tailored to hiking, biking, and other outdoor uses.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-outdoors-style-2210.png)

  * **Traffic (Day):** Light-colored map emphasizing transit networks and roads, including current traffic information.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-traffic-style-2210.png)

  * **Traffic (Night):** Dark-colored map emphasizing transit networks and roads, including current traffic information.

  * **Minimal:** Light colored map with no labels or boundary lines.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-minimal-style-2212.png)




### Map Position

You can change the center point and zoom level of a visible map:

  * **Fit to Data** : Automatically centers and zooms the map such that all the data points of your query are visible.
  * **Custom** : Lets you manually set a **Latitude** , **Longitude** , and **Zoom Level** (higher numbers create a closer zoom level).



### Allow Panning

This option lets you determine whether users can reposition the map by dragging it. This option is enabled by default.

### Allow Zooming

This option lets you determine whether a (+/-) button should appear in the upper left of the map visualization, allowing users to zoom in and out. This option is enabled by default.

### Show Full Field Name

This option lets you determine whether to show the view name along with the field name in map tooltips. Tooltips are displayed when users click map data points. This option is disabled by default.

Visit the Things to consider section on this page for more information about how tooltips are displayed on Google Map charts.

### Show Legend

This option lets you determine whether to show a map legend in the lower left of a visualization. The legend shows the color scale that the map is using, if you've added a measure to your visualization.

The **Show Legend** option is available for the following **Plot** options:

  * **Automagic Heatmap** mode
  * **Points** mode, when **Marker Color Mode** is set to **Based on Value**



### Show Region Field in Tooltip

The **Show Region Field in Tooltip** option is available when the query has at least one dimension with a map layer assigned to it. LookML developers can add a [built-in map layer](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name#built-in_map_layers) or a [custom map layer](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer) to a dimension using the [`map_layer_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) parameter.

This option lets you determine whether to display the region information in the tooltips that appear on the map.

When **Show Region Field in Tooltip** is enabled, if users hover over a region of the map, the region information (as provided by any dimensions with a map layer assigned to them) is displayed in the tooltip. In the following example, the query contains **State** and **Zipcode** dimensions with built-in map layers assigned to them:

![The tooltip displays the values New Mexico for State, 97106 for Zipcode, and 4 for Count.](https://docs.cloud.google.com/static/looker/docs/images/gmaps-show-region-2210.png)

When **Show Region Field in Tooltip** is disabled, if users hover over a region of the map, the tooltip contains only the values from the measures in the query. The following example uses the same query as the previous example, but **Show Region Field in Tooltip** is disabled:

![The tooltip displays only the value 4 for the Count field.](https://docs.cloud.google.com/static/looker/docs/images/gmaps-show-region-disabled-2210.png)

Visit the Things to consider section on this page for more information about how tooltips are displayed on Google Map charts.

### Draw Map Labels Above Data

If the data in your visualization contains a [map layer](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name), the **Draw Map Labels Above Data** menu option appears. The option defaults to disabled.

Enabling **Draw Map Labels Above Data** moves the map's labels above the heatmap data. This is helpful with higher heatmap opacity values. If a heatmap is opaque, the labels don't show unless **Draw Map Labels Above Data** is enabled.

## Points menu options

**Note:** The **Points** menu is not available for visualizations that contain dimensions with a defined map layer. When you select an automagic heatmap or a density heatmap, the options in the **Points** menu do not affect the visualization.

### Type

This option is available for maps with points, connect with lines, or connect with areas plot types.

**Type** specifies the type of point displayed on the map visualization:

  * **Circle** : Points on the map are displayed as circles of varying sizes and colors.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-points-circle-2210.png)
  * **Icon** : Points on the map are displayed as icons of varying colors. 

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-points-icon-2210.png)
  * **Both** : Points on the map are displayed as both circles and icons.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-points-both-2210.png)
  * **None** : No points are displayed on the map.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-points-none-2210.png)



Your point type selection impacts the other formatting options that are available. A **Type** of **Both** includes all options. A **Type** of **None** shows no options.

### Radius

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Circle** in the **Type** option of the **Points** menu, a **Radius** menu option appears. The **Radius** option lets you set the size of the circle points. You can choose one of three options:

  * **Proportional to Value:** Adjusts the relative size of the circles according to measures in your query. When you choose this option you can set a **Minimum Radius** and **Maximum Radius** of the circles, which correspond with the lowest and highest values in your data. You can also choose between a **Linear** and **Logarithmic** scale to size the circles.

  * **Equal to Value:** Adjusts the radius of the circles to the actual measure values in the underlying query. This likely only makes sense if you are plotting distance data — for example, if your measure contained the size of a territory.

  * **Fixed:** Choosing **Fixed** reveals and additional **Fixed Radius** option where you can set a fixed radius to apply to all map markers. The default value is 500 radius units.




### Radius Units

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Circle** or **Both** in the **Type** option of the **Points** menu, a **Radius Units** menu option appears. The **Radius Units** option lets you set the units of the circle points as meters or pixels.

### Icon

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Icon** or **Both** in the **Type** option of the **Points** menu, an **Icon** menu option appears. Expanding the **Icon** drop-down menu lets you choose an icon to display on all map markers. The markers cannot be dynamic according to your data.

### Marker Color Mode

This option is available for maps with points, connect with lines, or connect with areas plot types.

If you select **Circle** , **Icon** , or **Both** in the **Type** option of the **Points** menu, a **Marker Color Mode** menu option appears. This option lets you customize the color of the map markers in an interactive map. You can choose one of two options:

  * **Based on Value** : Colors are dynamically assigned to markers based on the values of the underlying query. To configure the colors in the legend for this option, see the Value Colors option.
  * **Custom** : Lets you set a single color to use for all map markers. The color value can also be formatted as an RGB hex string, such as `#2ca6cd`, or as [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`.



## Value menu options

**Note:** The **Value** menu is not available if the **Marker Color Mode** option in the **Points** menu is set to **Custom**.

### Value Colors

You can set the color of map points or define the range of colors to be used if you are color coding according to a measure.

You can input a list of hex strings, such as `#2ca6cd`, or [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`. The colors you input first are associated with the lowest values.

### Dual-axis Map

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is part of the **Google Maps Enhancements** preview feature. This preview feature must be enabled by a Looker admin on the [Admin settings - Preview Features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) page. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`looker-viz-preview-external@google.com`](mailto:looker-viz-preview-external@google.com). 

The **Dual-axis Map** option is available when a query has at least two measures. This toggle lets you overlay a second measure as a grayscale layer on top of the primary color-coded map regions.

![](https://docs.cloud.google.com/static/looker/docs/images/dual-axis-map-2610.png)

  * The first measure in the query determines the color of the regions.
  * The second measure in the query determines the grayscale intensity (from white to black) of the overlay.



The grayscale layer uses semi-transparency to allow the primary color layer to show through, enabling you to visualize two different metrics simultaneously on the same map.

Note the following limitations for this feature:

  * A maximum of two measures is supported.
  * Pivoted data is not supported.



### Quantize Colors

By default, the **Quantize Colors** option is off, and Looker displays values using a gradient color scale.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-quantize-off-2212.png)

When turned on, **Quantize Colors** changes the color scale from a smooth gradient to blocks of specific colors.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-quantize-on-2212.png)

### Reverse Color Scale

When turned on, **Reverse Color Scale** switches the colors that indicate high and low values on the chart, reversing the color gradient.

### Minimum Value/Maximum Value

You can set the minimum and maximum values of the color range. This lets you color code all points under a certain threshold with the lowest color and all points over a certain threshold with the highest color.

By default this field is left blank, and the minimum and maximum values applied on the legend are the minimum and maximum values from your query.

## Layers menu options

The Layers menu options let you add Google Maps overlays.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is part of the **Google Maps Enhancements** preview feature. This preview feature must be enabled by a Looker admin on the [Admin settings - Preview Features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) page. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`looker-viz-preview-external@google.com`](mailto:looker-viz-preview-external@google.com). 

### Custom Layer

When enabled, lets you specify a custom map layer by providing a URL to a TopoJSON file. This option is useful for rendering non-standard geographic regions or custom polygons directly in the visualization. This option is a alternative to using the LookML [`map_layer_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) parameter to define a custom map layer.

Enabling **Custom Layer** reveals the following options:

  * **TopoJSON URL** : The URL of the TopoJSON file. You can enter a full URL for an externally hosted file (for example, `https://example.com/map.json`) or a relative path to a file that's uploaded to your Looker project. 
    * For project files, the path must strictly follow the pattern `/projects/{project_id}/raw/{file_path}` (for example, `/projects/my_project/raw/my_map.json`). If you omit the `/raw/` directory, the request is blocked.
    * Project files must use a `.json` file extension (for example, `my_map.json` or `my_map.topojson.json`). Looker doesn't index files with a `.topojson` extension.
  * **TopoJSON Object Key** : The name of the object within the TopoJSON file to be rendered.
  * **TopoJSON Property Key** : The property in the TopoJSON file that matches the values in your query's dimension. Looker uses this property to map your data to the custom regions.
  * **TopoJSON Property Label Key** : The property in the TopoJSON file to use as the display label for each region (for example, in tooltips).
  * **Show Unmatched** : Toggle to display regions from the custom TopoJSON layer that don't have matching data in the query.
  * **Unmatched Region Color/Opacity** : Select the color and the opacity of the color that's used to render unmatched regions.

**Note:** An external server hosting the TopoJSON file must be configured to allow Cross-Origin Resource Sharing (CORS) requests from your Looker instance domain. For best performance, optimize your TopoJSON files and keep file sizes under 10MB. 

### Transit Layer

When enabled, adds a Google Maps transit layer that overlays transit lines and stations. The lines on the map show bus, subway, and rail routes. To find more information and to view upcoming trains or buses, choose a station stop icon.

### Bicycling Layer

When enabled, adds a Google Maps bicycling layer that highlights bicycle paths and bike-friendly streets. The colors show you the type of bicycling paths.

  * **Dark green** : Shows trails that don't have auto traffic.
  * **Green** : Shows dedicated lanes are roads that are shared with cars and have a separate bike lane.
  * **Dotted green line** : Shows bicycle-friendly roads are roads that don't have a bike lane but are recommended for cyclists.
  * **Dashed dark-green lines** : Shows unpaved trails are off-road dirt paths.



### Traffic Layer

When enabled, adds a Google Maps traffic layer that displays real-time traffic conditions. Traffic colors The color code shows you the speed of traffic on the road.

  * **Green** : No traffic delays.
  * **Orange** : Medium amount of traffic.
  * **Red** : Traffic delays. The darker the red, the slower the speed of traffic on the road.



Gray or blue lines on the map show your routes.

Traffic incidents include these types of delays:

  * Accidents
  * Construction
  * Road closures
  * Other incidents



## Heatmap menu options

**Note:** The **Heatmap** menu is available only when either the **Automagic Heatmap** , **Density Heatmap** , or **3D Heatmap** option is selected from the **Plot** menu.

The Heatmap menu options let you configure **Automagic Heatmap** , **Density Heatmap** , and **3D Heatmap** options.

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is part of the **Google Maps Enhancements** preview feature. This preview feature must be enabled by a Looker admin on the [Admin settings - Preview Features](https://docs.cloud.google.com/looker/docs/admin-panel-general-preview-features) page. We encourage you to share your feedback to help us improve. To report bugs or issues, send an email to [`looker-viz-preview-external@google.com`](mailto:looker-viz-preview-external@google.com). 

### Heatmap Gridlines

This option is available when **Automagic Heatmap** is selected from the **Plot** menu or when a [map layer](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer) is used in your chart. Enabling this option adds a border around each of the gridlines used for the automagic heatmap.

### Gridlines on Empty Regions

If the **Heatmap Gridlines** option is turned on and you're plotting a dimension that has a defined [map layer](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer), you can enable the **Gridlines on Empty Regions** toggle to display an outline around the map regions that have no associated data.

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-gridlines-on-empty-regions-2212.png)

### Heatmap Opacity

This option is available when **Automagic Heatmap** is selected or when a [map layer](https://docs.cloud.google.com/looker/docs/reference/param-model-map-layer) is used in your chart. This option lets you specify the opacity of the colors that are used in the heatmap. Enter a single-digit decimal between 0 and 1, where 0 means no color and 1 means totally opaque.

### Intensity

This option is available when **Density Heatmap** is selected from the **Plot** menu.

This slider controls the weight multiplier for the data points.

Increasing intensity makes the heatmap appear "hotter" overall. It biases the output color toward the higher end of the color spectrum (for example, shifting from blue/green to red/yellow), making areas with even moderate concentration look like hotspots. Decreasing intensity requires a higher concentration of points to reach the maximum color in the gradient.

### Threshold

This option is available when **Density Heatmap** is selected from the **Plot** menu.

This slider defines the ratio of the "fading weight" to the maximum weight. It controls the cutoff or transparency at the edges of the heatmap blobs.

Increasing the threshold makes the edges of the heatmap sharper and more defined. Pixels with relatively low density (below the threshold ratio) will fade out and become transparent more quickly. Decreasing the threshold creates a smoother, more gradual fade at the edges, allowing lower-density areas to remain visible.

### Elevation Scale

This option is available when **3D Heatmap** is selected from the **Plot** menu. This slider controls the height of the hexagons in the 3D heatmap.

### Hexagon Radius

This option is available when **3D Heatmap** is selected from the **Plot** menu. This slider controls the widths of the hexagons on the 3D heatmap.

### Colors

The color options are available when **3D Heatmap** is selected from the **Plot** menu. You can use these options to define colors for the heatmap.

#### Collection

A collection lets you create themed visualizations and dashboards that look good together. All of Looker's built-in color collections appear on the [Color collections](https://docs.cloud.google.com/looker/docs/color-collections) documentation page. Your Looker admin may also create a custom color collection for your organization.

You can choose a color collection from the **Collection** drop-down menu. The **Palette** section will update with a palette from your chosen color collection.

#### Palette

Once you've selected a color collection, you can choose a different palette from the collection, or customize your palette, by clicking the color palette itself. This opens the palette picker and displays all of the palettes from the collection.

Colors are assigned to each series in order. For a [categorical palette](https://docs.cloud.google.com/looker/docs/color-collections), the first color in the palette is assigned to the first series, and so on. For a [sequential or diverging palette](https://docs.cloud.google.com/looker/docs/color-collections), the color at the left end of the palette is assigned to the first series and the colors for each remaining series move to the right on the palette. If your query returns more data series than colors listed, the colors repeat from the beginning of the palette, first as a lighter version of each color, then as a darker version of each color.

#### Creating a custom color palette

To create a custom color palette, select the **Custom** tab on the palette picker. You can edit your palette in several ways:

  * Click on one of the colors present to edit it.
  * Click the **+** or **-** buttons to add a color to the end of the palette or to remove a selected color.
  * Click **EDIT ALL** at the bottom right of the menu to use a comma-separated list of color values.



![](https://docs.cloud.google.com/static/looker/docs/images/color-palette-custom-2106.png)

To change a selected color, or edit all colors at once, input [hex strings](https://www.w3schools.com/colors/colors_hexadecimal.asp), such as `#2ca6cd`, or [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`, into the color value box at the bottom of the picker.

![](https://docs.cloud.google.com/static/looker/docs/images/color-hex-value-2106.png)

To bring up a color picker to select a color, click the color wheel to the right of the color value box. The corresponding hex value for that color appears in the color value box.

![](https://docs.cloud.google.com/static/looker/docs/images/color-picker-2106.png)

If you click **EDIT ALL** , the color value box populates with the hex codes of the color palette you've chosen or customized. Copying and pasting this list is the best way to copy custom color palettes from one chart to another.

#### Reverse colors

You can reverse the colors used on a palette. For a [categorical palette](https://docs.cloud.google.com/looker/docs/color-collections), this applies the last color in the palette to the first series, the second-to-last color in the palette to the second series, and so on. For a [sequential or diverging palette](https://docs.cloud.google.com/looker/docs/color-collections), this applies the color at the right end of the palette to the first series and move left on the palette for the remaining series.

## Things to consider

### Tooltip behavior on Google Maps charts

[Tooltips](https://docs.cloud.google.com/looker/docs/creating-visualizations#the_visualization_tooltip) on Google Map charts can behave in specific ways.

When an entire country is visible on a Google Map chart (and it is not repeated):

  * The tooltip will be displayed at the country's geographical center by width.
  * The tooltip display will begin at the country's topmost latitude.



If an entire country is _not_ visible on a Google Map chart (a map is zoomed into a specific point of a country), the tooltip will be displayed next to the cursor.

When a Google Map chart map is zoomed out enough to display two instances of the same country (both geographical centers are displayed), the tooltip will appear in one of two ways:

  * If there is room above both instances of the country, the tooltip will be displayed above the midpoint of the two countries.
  * If there is only room above one instance of the country, the tooltip will only be displayed above that country.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
