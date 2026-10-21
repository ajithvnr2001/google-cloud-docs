---
url: https://docs.cloud.google.com/data-studio/google-maps-reference/
title: Google Maps reference \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:16:36.696480+00:00
---

# Google Maps reference  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/google-maps-reference/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Google Maps reference Stay organized with collections  Save and categorize content based on your preferences. 

Adding Google Maps to your reports gives your viewers a familiar interactive environment where they can explore geographic data. Google Maps in Data Studio are highly customizable and integrate with any data source that contains valid geo fields.

## Before you begin

To add Google Maps to Data Studio, you'll need a data source with one or more geographic dimensions. Data sources that are based on Google Analytics and Google Ads automatically include fields that you can use, such as **Country** , **City** , **Region** , **Metro area** , and **Store location**.

For other data source types, such as Google Sheets or BigQuery, make sure that any geographic fields have the correctly assigned data type. To edit the geographic dimensions in your data source, follow these steps:

  1. [Edit the data source](https://docs.cloud.google.com/data-studio/edit-a-data-source).
  2. Locate the geographic dimension(s) that you want to use in Google Maps.
  3. Use the **Type** menu to select the appropriate Geo field type — for example, **Country** , **City** , or **Region**.



To learn more about geo dimensions, see the [Geo dimension reference](https://docs.cloud.google.com/data-studio/geo-dimension-reference).

## Tips and limits for working with BigQuery `GEOGRAPHY` data

Each Google Maps style in Data Studio can plot up to 1 million points (polygon vertices).

If your query returns more data, the map will show as many polygons as it can within the limit, and you may notice missing polygons.

To reduce the number of points, follow these steps:

  * Apply a [filter](https://docs.cloud.google.com/data-studio/about-filter-properties). 
    * Filters on a `GEOGRAPHY` field can select up to 1 GB of data. If your filters return more, you'll get an error.
  * Simplify the polygons in BigQuery by using the [ST_SIMPLIFY](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/geography_functions#st_simplify) function.



Blended and extracted data sources don't support `GEOGRAPHY` fields. To join a table that contains your `GEOGRAPHY` field with another table, use SQL to perform the join in BigQuery.

## Geo functions

Data Studio provides a number of geographic functions that you use to work with and transform geographic information in your data sources.

To learn more about these functions, view the [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list) and filter the functions by Geo type.

## Limits of Google Maps

  * Filled area maps don't support **Latitude** , **Longitude** , or **Address** geographic field types.
  * For bubble maps, **Postal Code** can be a US ZIP code (for example, 94043) or an international postal code (example: L4L 9H8). For filled area maps, **Postal Code** can be a US ZIP code.
  * Connection maps require points that have compatible geographic field types.
  * Maximum data limits are as follows: 
    * 1 million bubbles for **Latitude** or **Longitude** fields
    * 1 million points (polygon vertices) for **Geospatial** fields (BigQuery `GEOGRAPHY` )
    * 3,500 bubbles or filled areas for other geographic field types

**Warning:** Increasing a map's data limit can make it load more slowly.

  * You can't enable drill down in Google Maps.
  * Google Maps doesn't support using optional metrics.
  * Location names longer than 500 characters won't be geocoded.



## Plot your data with Google Maps

To visualize your data on a Google Map, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Navigate to the page that will contain the chart.
  3. In the toolbar, click ![Add a chart icon.](https://docs.cloud.google.com/static/data-studio/images/addchartgrey6002x48dp-2020-08-18-icon-rge.png)**Add a chart**.
  4. Select one of the preset **Google Maps** : 
     1. **Bubble maps** show your data as colored circles.
     2. **Filled maps** show your data as shaded areas.
     3. **Heatmaps** show your data using a color gradient.
     4. **Line maps** show your data as lines or paths over a geographic area.
     5. **Connection maps** show your data as pairs of points that are connected by a line or an arc.
     6. **Combo maps** show your data as a combination of a filled map and a bubble map.
  5. Click the canvas to add the chart to the report.
  6. Use the settings in the **Properties** panel to add or change the **Location** or **Geospatial** field so that your map displays the intended locations.
  7. Refer to the following sections for information on configuring the rest of your map.



## Configure a bubble map

Bubble maps depict your data as colored circles, or bubbles. Here's a bubble map that shows airline arrivals in California, where the quantity of flights (the **Flights** dimension) is represented by bubble size and the average arrival delay (the **Avg. Arrival Delay** metric) is represented by bubble color:

![A bubble map displays airline arrivals in California with the number of flights indicated by bubble size and the average arrival delay indicated by bubble color.](https://docs.cloud.google.com/static/data-studio/images/bubble-map-2020-08-18.png)

### Setup properties

The following setup properties are available for bubble maps.

#### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



#### Fields

Configure the options in the **Fields** section to set up the map chart data.

##### Location

The **Location** field requires a dimension that determines where the data appears on the map. Note that this field can be of any data type, as long as Google Maps can [geocode](https://developers.google.com/maps/documentation/geocoding/overview) the values appropriately.

##### Tooltip

(Optional) The **Tooltip** field requires a dimension that provides tooltips (labels) for the data. Providing a tooltip lets you override the default label that is provided by the **Location** dimension. For example, you can base the map location on a store's address but use the store's name in the tooltip.

The **Tooltip** option requires unique values for each **Location** value. If the **Tooltip** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Tooltip dimension has multiple values for the same location. Choose a Tooltip dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Color dimension

(Optional) A dimension that provides the categories that are used for the color of the geo data. If you choose this option, you can't use the **Color metric** option.

The **Color dimension** option requires unique values for each **Location** value. If the **Color dimension** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Color dimension has multiple values for the same location. Choose a Color dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Size

Use the size of the bubbles to convey relative metric values.

##### Color metric

(Optional) The **Color metric** field requires a metric that provides the values that are used as a color scale for the geo data. If you choose this option, you can't use the **Color dimension** option.

#### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



#### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

#### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



#### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

### Style properties

The following style properties are available for bubble maps.

#### Chart title

To add a title to your chart, enable the **Show title** option. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

To have Data Studio generate a title that is based on the chart type and the fields that are used in the chart, enable the **Autogenerate** option. This option is enabled by default when **Show title** is also enabled.

To add a custom title to your chart, enter it in the **Title** field. This will turn off the **Autogenerate** setting.

The following **Chart title** settings control how the map's title appears:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



#### Background layer

These settings control the appearance of the base map:

  * **Use vector graphics:** Enables tilt and optimized graphics. **Use vector graphics** is enabled by default for combo maps and connection maps.
  * **Show in 3D view:** Enables the map to be dragged and tilted in three dimensions. **Show in 3D view** is available only for combo maps and connection maps and is enabled by default.
  * **Type:** Sets the default map background. Options include **Map** , **Satellite with labels** , and **Satellite**. The **Satellite with label** type is available only when the **Use vector graphics** setting is enabled.
  * **Style:** Sets the color theme for the map. Use the report's current theme, or select one of the preset map styles. **Style** is available only when the **Map** type is selected. You can also create a custom map style.
  * **Roads, Landmarks, Labels:** Use the sliders to select the level of background details to display in the map background.



#### Layer type

The **Layer type** setting determines how locations on the map are shown. You can show locations in the following formats:

  * Bubbles
  * Filled areas
  * Line map
  * Connection map
  * Combo map
  * Heatmap



#### Default viewport

Sets the default location of the map's viewport, or inset.

To set a default viewport location, navigate to the chosen location and zoom level on the map chart. Under **Default viewport** in the style properties, select **Set as default view** to save the placement of the map's viewport.

When exploring the map, click the ![](https://docs.cloud.google.com/static/data-studio/images/mapsarbaselinep900fill0wght400grad0opsz24png.png)**Reset viewport** icon on the map chart to return to your default view.

If a map thumbnail and inset are displayed under **Default viewport** , a default viewport is already set for this map. To set a new default view, navigate the map to the new chosen location and zoom setting, and click **Set as default view**.

The **Default viewport** option is best used when the **Allow pan and zoom** map control option is enabled.

#### Bubble layer

  * **Max number of bubbles:** Sets the maximum number of bubbles appearing on the map.
  * **Opacity:** Sets the opacity of the bubbles.
  * **Border weight:** Sets the thickness of the bubble borders.



#### Colors

The **Colors** setting lets you manage the bubble or filled area colors for specific values of **Color dimension** or **Color metric** fields:

  * If you have defined the **Color dimension** option in the setup properties, both the filled area and bubble layer map colors are managed in the **Colors** style property by selecting **Manage dimension value colors**.
  * If you have defined the **Color metric** option in the setup properties, you can define a color scale by selecting color values for the scale's maximum (**Max color**), middle (**Mid color**), and minimum (**Min color**). You can also specify a color to represent missing data (**Dataless color**).



#### Map controls

These settings let you select which interactive map view controls will be shown or hidden:

  * **Allow tilt and rotation:** Enables the map to be dragged and tilted in three dimensions. **Allow tilt and rotation** is available when the **Use vector graphics Background Layer** style property is enabled. This control is not available for combo maps or connection maps.
  * **Allow pan and zoom:** Lets viewers adjust the map display with their mouse and keyboard. Users can still tilt the map when **Allow pan and zoom** is disabled if the **Allow tilt and rotation** setting is enabled (or if the **Show in 3D view** setting is enabled for combo maps or connection maps).
  * **Show zoom control:** Shows the ![Add icon.](https://docs.cloud.google.com/static/data-studio/images/gmaddgrey60048dp-2020-03-26.png) plus sign and ![Remove icon.](https://docs.cloud.google.com/static/data-studio/images/gmremovegrey60048dp-2020-03-26.png) minus sign buttons on the map to zoom in and out, respectively.
  * **Show Street View control:** Lets users display Street View images for supported locations.
  * **Show fullscreen control:** Lets users display the map in fullscreen view.
  * **Show map type control:** Lets users switch between map view and satellite view.
  * **Show scale control:** Lets users display the map scale in kilometers or miles.



#### Legends

Legends help your viewers understand the map by describing the colors and bubble sizes that are used.

The following legends are available:

  * A **Size legend** describes the **Size** metric in bubble maps and the **Thickness** metric in connection maps.
  * A **Color legend** describes the **Color dimension** or the **Color metric**. If your map specifies a **Color dimension** , the **Color legend** uses distinct colors for each value. If your map specifies a **Color metric** , the **Color legend** uses a color gradient.
  * A **Weight legend** describes the **Weight** metric.
  * A **Thickness legend** describes the **Thickness** metric that is used in a line map.
  * A **Height legend** describes the height of the **Additional Layer Metric** that is used in a combo map.



For example, here is a bubble map that displays sports venue capacities for different NCAA basketball conferences:

![A bubble map displays the NCAA venue_capacity metric by bubble size and represents the NCAA conf_name dimension with bubble color.](https://docs.cloud.google.com/static/data-studio/images/google-maps-bubble-map-legend-numbered-2020-10-28.png)

The map properties define the **Color metric** as **venue_capacity** , represented in the **Size legend** by bubble size, and the **Color dimension** as **conf_name** , represented in the **Color legend** by bubble color.

In another example, a filled area map of Spain and Portugal depicts the average time that a user spends on a page by their region:

![A filled area map of Spain and Portugal with a color legend displays a gradient of purple to blue based on Avg. Time on Page metric values that range from 00:00:00 to 00:24:40.](https://docs.cloud.google.com/static/data-studio/images/google-maps-filled-map-legend-2020-10-28.png)

The **Color legend** displays a color gradient of time that is spent on a page based on the **Avg. Time on Page** metric.

#### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



#### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



#### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Configure a filled map

A filled map depicts your data as a shaded area. Here's a filled map that shows median house prices by US ZIP codes in the San Francisco Bay Area, where the median house price in each ZIP code is represented in shades of red and green:

![A filled map displays median house prices by ZIP code in the San Francisco Bay Area in shades of green and red to convey values.](https://docs.cloud.google.com/static/data-studio/images/filledmap-2020-08-18.png)

### Setup properties

The following setup properties are available for filled maps.

#### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



#### Fields

Configure the options in the **Fields** section to set up the map chart data.

##### Location

The **Location** field requires a dimension that determines where the data appears on the map. Note that this field can be of any data type, as long as Google Maps can [geocode](https://developers.google.com/maps/documentation/geocoding/overview) the values appropriately.

##### Geospacial field

This option is available only when you connect to a BigQuery data source that contains [`GEOGRAPHY` data](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type). When you use a **Geospatial** field, the **Location** field provides information for the card that appears when you hover over a data point on the map.

To learn more about visualizing BigQuery GEOGRAPHY data, see the [Visualize BigQuery GEOGRAPHY polygons with Data Studio](https://docs.cloud.google.com/data-studio/visualize-bigquery-geography-polygons) tutorial.

##### Tooltip

(Optional) The **Tooltip** field requires a dimension that provides tooltips (labels) for the data. Providing a tooltip lets you override the default label that is provided by the **Location** dimension. For example, you can base the map location on a store's address but use the store's name in the tooltip.

The **Tooltip** option requires unique values for each **Location** value. If the **Tooltip** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Tooltip dimension has multiple values for the same location. Choose a Tooltip dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Color dimension

(Optional) A dimension that provides the categories that are used for the color of the geo data. If you choose this option, you can't use the **Color metric** option.

The **Color dimension** option requires unique values for each **Location** value. If the **Color dimension** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Color dimension has multiple values for the same location. Choose a Color dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Color metric

(Optional) The **Color metric** field requires a metric that provides the values that are used as a color scale for the geo data. If you choose this option, you can't use the **Color dimension** option.

#### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



#### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

#### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



#### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

### Style properties

The following style properties are available for filled maps.

#### Chart title

To add a title to your chart, enable the **Show title** option. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

To have Data Studio generate a title that is based on the chart type and the fields that are used in the chart, enable the **Autogenerate** option. This option is enabled by default when **Show title** is also enabled.

To add a custom title to your chart, enter it in the **Title** field. This will turn off the **Autogenerate** setting.

The following **Chart title** settings control how the map's title appears:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



#### Background layer

These settings control the appearance of the base map:

  * **Use vector graphics:** Enables tilt and optimized graphics. **Use vector graphics** is enabled by default for combo maps and connection maps.
  * **Show in 3D view:** Enables the map to be dragged and tilted in three dimensions. **Show in 3D view** is available only for combo maps and connection maps and is enabled by default.
  * **Type:** Sets the default map background. Options include **Map** , **Satellite with labels** , and **Satellite**. The **Satellite with label** type is available only when the **Use vector graphics** setting is enabled.
  * **Style:** Sets the color theme for the map. Use the report's current theme, or select one of the preset map styles. **Style** is available only when the **Map** type is selected. You can also create a custom map style.
  * **Roads, Landmarks, Labels:** Use the sliders to select the level of background details to display in the map background.



#### Layer type

The **Layer type** setting determines how locations on the map are shown. You can show locations in the following formats:

  * Bubbles
  * Filled areas
  * Line map
  * Connection map
  * Combo map
  * Heatmap



#### Default viewport

Sets the default location of the map's viewport, or inset.

To set a default viewport location, navigate to the chosen location and zoom level on the map chart. Under **Default viewport** in the style properties, select **Set as default view** to save the placement of the map's viewport.

When exploring the map, click the ![](https://docs.cloud.google.com/static/data-studio/images/mapsarbaselinep900fill0wght400grad0opsz24png.png)**Reset viewport** icon on the map chart to return to your default view.

If a map thumbnail and inset are displayed under **Default viewport** , a default viewport is already set for this map. To set a new default view, navigate the map to the new chosen location and zoom setting, and click **Set as default view**.

The **Default viewport** option is best used when the **Allow pan and zoom** map control option is enabled.

#### Filled area layer

  * **Max number of polygon vertices:** Sets the maximum number of data points that can be plotted. Only available for BigQuery data sources.
  * **Opacity:** Sets the opacity of the filled areas.
  * **Border color:** Sets the color of the filled area borders.
  * **Border weight:** Sets the thickness of the filled area borders.



#### Colors

The **Colors** setting lets you manage the bubble or filled area colors for specific values of **Color dimension** or **Color metric** fields:

  * If you have defined the **Color dimension** option in the setup properties, both the filled area and bubble layer map colors are managed in the **Colors** style property by selecting **Manage dimension value colors**.
  * If you have defined the **Color metric** option in the setup properties, you can define a color scale by selecting color values for the scale's maximum (**Max color**), middle (**Mid color**), and minimum (**Min color**). You can also specify a color to represent missing data (**Dataless color**).



#### Map controls

These settings let you select which interactive map view controls will be shown or hidden:

  * **Allow tilt and rotation:** Enables the map to be dragged and tilted in three dimensions. **Allow tilt and rotation** is available when the **Use vector graphics Background Layer** style property is enabled. This control is not available for combo maps or connection maps.
  * **Allow pan and zoom:** Lets viewers adjust the map display with their mouse and keyboard. Users can still tilt the map when **Allow pan and zoom** is disabled if the **Allow tilt and rotation** setting is enabled (or if the **Show in 3D view** setting is enabled for combo maps or connection maps).
  * **Show zoom control:** Shows the ![Add icon.](https://docs.cloud.google.com/static/data-studio/images/gmaddgrey60048dp-2020-03-26.png) plus sign and ![Remove icon.](https://docs.cloud.google.com/static/data-studio/images/gmremovegrey60048dp-2020-03-26.png) minus sign buttons on the map to zoom in and out, respectively.
  * **Show Street View control:** Lets users display Street View images for supported locations.
  * **Show fullscreen control:** Lets users display the map in fullscreen view.
  * **Show map type control:** Lets users switch between map view and satellite view.
  * **Show scale control:** Lets users display the map scale in kilometers or miles.



#### Legends

Legends help your viewers understand the map by describing the colors and bubble sizes that are used.

The following legends are available:

  * A **Size legend** describes the **Size** metric in bubble maps and the **Thickness** metric in connection maps.
  * A **Color legend** describes the **Color dimension** or the **Color metric**. If your map specifies a **Color dimension** , the **Color legend** uses distinct colors for each value. If your map specifies a **Color metric** , the **Color legend** uses a color gradient.
  * A **Weight legend** describes the **Weight** metric.
  * A **Thickness legend** describes the **Thickness** metric that is used in a line map.
  * A **Height legend** describes the height of the **Additional Layer Metric** that is used in a combo map.



For example, here is a bubble map that displays sports venue capacities for different NCAA basketball conferences:

![A bubble map displays the NCAA venue_capacity metric by bubble size and represents the NCAA conf_name dimension with bubble color.](https://docs.cloud.google.com/static/data-studio/images/google-maps-bubble-map-legend-numbered-2020-10-28.png)

The map properties define the **Color metric** as **venue_capacity** , represented in the **Size legend** by bubble size, and the **Color dimension** as **conf_name** , represented in the **Color legend** by bubble color.

In another example, a filled area map of Spain and Portugal depicts the average time that a user spends on a page by their region:

![A filled area map of Spain and Portugal with a color legend displays a gradient of purple to blue based on Avg. Time on Page metric values that range from 00:00:00 to 00:24:40.](https://docs.cloud.google.com/static/data-studio/images/google-maps-filled-map-legend-2020-10-28.png)

The **Color legend** displays a color gradient of time that is spent on a page based on the **Avg. Time on Page** metric.

#### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



#### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



#### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Configure a heatmap

A heatmap depicts your data using a color gradient. Here's a heatmap that shows bikeshare statistics for London, U.K. with "hotter" regions representing higher counts of bikeshare options.

![A heatmap displays London bikeshare data.](https://docs.cloud.google.com/static/data-studio/images/london-bikeshare-heatmap-2022-02-01.png)

### Setup properties

The following setup properties are available for heatmaps.

#### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



#### Fields

Configure the options in the **Fields** section to set up the map chart data.

##### Location

The **Location** field requires a dimension that determines where the data appears on the map. Note that this field can be of any data type, as long as Google Maps can [geocode](https://developers.google.com/maps/documentation/geocoding/overview) the values appropriately.

##### Weight

A metric that determines how much each individual point contributes to the appearance of your heatmap. By default, every point has the same value. You can specify a field with weights if you want to assign different values to the points.

This field is optional.

#### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



#### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

#### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



### Style properties

The following style properties are available for heatmaps.

#### Chart title

To add a title to your chart, enable the **Show title** option. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

To have Data Studio generate a title that is based on the chart type and the fields that are used in the chart, enable the **Autogenerate** option. This option is enabled by default when **Show title** is also enabled.

To add a custom title to your chart, enter it in the **Title** field. This will turn off the **Autogenerate** setting.

The following **Chart title** settings control how the map's title appears:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



#### Background layer

These settings control the appearance of the base map:

  * **Use vector graphics:** Enables tilt and optimized graphics. **Use vector graphics** is enabled by default for combo maps and connection maps.
  * **Show in 3D view:** Enables the map to be dragged and tilted in three dimensions. **Show in 3D view** is available only for combo maps and connection maps and is enabled by default.
  * **Type:** Sets the default map background. Options include **Map** , **Satellite with labels** , and **Satellite**. The **Satellite with label** type is available only when the **Use vector graphics** setting is enabled.
  * **Style:** Sets the color theme for the map. Use the report's current theme, or select one of the preset map styles. **Style** is available only when the **Map** type is selected. You can also create a custom map style.
  * **Roads, Landmarks, Labels:** Use the sliders to select the level of background details to display in the map background.



#### Layer type

The **Layer type** setting determines how locations on the map are shown. You can show locations in the following formats:

  * Bubbles
  * Filled areas
  * Line map
  * Connection map
  * Combo map
  * Heatmap



#### Heatmap layer

A heatmap aggregates points to create the visualization. To create the map, a circle is drawn around each point, and values in the circle decrease as the distance from the point increases.

These settings control the appearance of the circles:

  * **Heatmap aggregation:** When multiple circles overlap, their values are aggregated in one of two ways: 
    * Sum. The values on the overlapping portions of the circles are added.
    * Mean. The values on the overlapping portions of the circles are a weighted average of the nearest points.
  * **Slider control:** Sets the relative size of the circles.
  * **Opacity:** Sets the opacity of the circles.
  * **Color domain min/max:** Sets minimum and maximum values for the color range.
  * **Intensity:** Adjusts the range of colors in the heatmap towards the high or low end.

**Note:** Heatmaps in Data Studio are based on the deck.gl visualization library. To learn more about these settings, see the [heatmap layer documentation](https://deck.gl/docs/api-reference/aggregation-layers/heatmap-layer).

#### Default viewport

Sets the default location of the map's viewport, or inset.

To set a default viewport location, navigate to the chosen location and zoom level on the map chart. Under **Default viewport** in the style properties, select **Set as default view** to save the placement of the map's viewport.

When exploring the map, click the ![](https://docs.cloud.google.com/static/data-studio/images/mapsarbaselinep900fill0wght400grad0opsz24png.png)**Reset viewport** icon on the map chart to return to your default view.

If a map thumbnail and inset are displayed under **Default viewport** , a default viewport is already set for this map. To set a new default view, navigate the map to the new chosen location and zoom setting, and click **Set as default view**.

The **Default viewport** option is best used when the **Allow pan and zoom** map control option is enabled.

#### Colors

The **Colors** setting lets you manage the bubble or filled area colors for specific values of **Color dimension** or **Color metric** fields:

  * If you have defined the **Color dimension** option in the setup properties, both the filled area and bubble layer map colors are managed in the **Colors** style property by selecting **Manage dimension value colors**.
  * If you have defined the **Color metric** option in the setup properties, you can define a color scale by selecting color values for the scale's maximum (**Max color**), middle (**Mid color**), and minimum (**Min color**). You can also specify a color to represent missing data (**Dataless color**).



#### Map Controls

These settings let you select which interactive map view controls will be shown or hidden:

  * **Allow tilt and rotation:** Enables the map to be dragged and tilted in three dimensions. **Allow tilt and rotation** is available when the **Use vector graphics Background Layer** style property is enabled. This control is not available for combo maps or connection maps.
  * **Allow pan and zoom:** Lets viewers adjust the map display with their mouse and keyboard. Users can still tilt the map when **Allow pan and zoom** is disabled if the **Allow tilt and rotation** setting is enabled (or if the **Show in 3D view** setting is enabled for combo maps or connection maps).
  * **Show zoom control:** Shows the ![Add icon.](https://docs.cloud.google.com/static/data-studio/images/gmaddgrey60048dp-2020-03-26.png) plus sign and ![Remove icon.](https://docs.cloud.google.com/static/data-studio/images/gmremovegrey60048dp-2020-03-26.png) minus sign buttons on the map to zoom in and out, respectively.
  * **Show Street View control:** Lets users display Street View images for supported locations.
  * **Show fullscreen control:** Lets users display the map in fullscreen view.
  * **Show map type control:** Lets users switch between map view and satellite view.
  * **Show scale control:** Lets users display the map scale in kilometers or miles.



#### Legends

Legends help your viewers understand the map by describing the colors and bubble sizes that are used.

The following legends are available:

  * A **Size legend** describes the **Size** metric in bubble maps and the **Thickness** metric in connection maps.
  * A **Color legend** describes the **Color dimension** or the **Color metric**. If your map specifies a **Color dimension** , the **Color legend** uses distinct colors for each value. If your map specifies a **Color metric** , the **Color legend** uses a color gradient.
  * A **Weight legend** describes the **Weight** metric.
  * A **Thickness legend** describes the **Thickness** metric that is used in a line map.
  * A **Height legend** describes the height of the **Additional Layer Metric** that is used in a combo map.



For example, here is a bubble map that displays sports venue capacities for different NCAA basketball conferences:

![A bubble map displays the NCAA venue_capacity metric by bubble size and represents the NCAA conf_name dimension with bubble color.](https://docs.cloud.google.com/static/data-studio/images/google-maps-bubble-map-legend-numbered-2020-10-28.png)

The map properties define the **Color metric** as **venue_capacity** , represented in the **Size legend** by bubble size, and the **Color dimension** as **conf_name** , represented in the **Color legend** by bubble color.

In another example, a filled area map of Spain and Portugal depicts the average time that a user spends on a page by their region:

![A filled area map of Spain and Portugal with a color legend displays a gradient of purple to blue based on Avg. Time on Page metric values that range from 00:00:00 to 00:24:40.](https://docs.cloud.google.com/static/data-studio/images/google-maps-filled-map-legend-2020-10-28.png)

The **Color legend** displays a color gradient of time that is spent on a page based on the **Avg. Time on Page** metric.

#### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



#### Chart Header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



#### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Configure a line map

A line map depicts your data as lines or paths over a geographic area. Here's a line map that shows roads in the state of New York. The map is filtered by `route_type` to include only "I" (interstate) roads.

![A Google map displays interstate highways in New York State with a tooltip that identifies the selected route as I-90, route_type: I.](https://docs.cloud.google.com/static/data-studio/images/line-map-2022-05-24.png)

This example was created using the [BigQuery US Roads public dataset](https://console.cloud.google.com/marketplace/product/united-states-census-bureau/all-roads).

### Setup properties

The following setup properties are available for line maps.

#### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



#### Fields

Configure the options in the **Fields** section to set up the map chart data.

##### Location

The **Location** field requires a dimension that determines where the data appears on the map. Note that this field can be of any data type, as long as Google Maps can [geocode](https://developers.google.com/maps/documentation/geocoding/overview) the values appropriately.

##### Geospacial field

This option is available only when you connect to a BigQuery data source that contains [`GEOGRAPHY` data](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type). When you use a **Geospatial** field, the **Location** field provides information for the card that appears when you hover over a data point on the map.

The previous example of a line map uses **road_geom** as the **Geospatial** field.

##### Tooltip

(Optional) The **Tooltip** field requires a dimension that provides tooltips (labels) for the data. Providing a tooltip lets you override the default label that is provided by the **Location** dimension. For example, you can base the map location on a store's address but use the store's name in the tooltip.

The **Tooltip** option requires unique values for each **Location** value. If the **Tooltip** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Tooltip dimension has multiple values for the same location. Choose a Tooltip dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

The previous example of a line map uses **full_name** as the **Tooltip** field.

##### Color dimension

(Optional) A dimension that provides the categories that are used for the color of the geo data. If you choose this option, you can't use the **Color metric** option.

The **Color dimension** option requires unique values for each **Location** value. If the **Color dimension** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Color dimension has multiple values for the same location. Choose a Color dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

The previous example of a line map uses **route_type** as the Color dimension field.

##### Thickness metric

(Optional) A metric that determines the thickness of the lines.

##### Color metric

(Optional) The **Color metric** field requires a metric that provides the values that are used as a color scale for the geo data. If you choose this option, you can't use the **Color dimension** option.

#### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



#### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

#### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



#### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

### Style properties

The following style properties are available for line maps.

#### Chart title

To add a title to your chart, enable the **Show title** option. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

To have Data Studio generate a title that is based on the chart type and the fields that are used in the chart, enable the **Autogenerate** option. This option is enabled by default when **Show title** is also enabled.

To add a custom title to your chart, enter it in the **Title** field. This will turn off the **Autogenerate** setting.

The following **Chart title** settings control how the map's title appears:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



#### Background layer

These settings control the appearance of the base map:

  * **Use vector graphics:** Enables tilt and optimized graphics. **Use vector graphics** is enabled by default for combo maps and connection maps.
  * **Show in 3D view:** Enables the map to be dragged and tilted in three dimensions. **Show in 3D view** is available only for combo maps and connection maps and is enabled by default.
  * **Type:** Sets the default map background. Options include **Map** , **Satellite with labels** , and **Satellite**. The **Satellite with label** type is available only when the **Use vector graphics** setting is enabled.
  * **Style:** Sets the color theme for the map. Use the report's current theme, or select one of the preset map styles. **Style** is available only when the **Map** type is selected. You can also create a custom map style.
  * **Roads, Landmarks, Labels:** Use the sliders to select the level of background details to display in the map background.



#### Layer type

The **Layer type** setting determines how locations on the map are shown. You can show locations in the following formats:

  * Bubbles
  * Filled areas
  * Line map
  * Connection map
  * Combo map
  * Heatmap



#### Line map layer

  * **Max. number of line vertices:** Sets the maximum number of data points that can be plotted. Only available for BigQuery data sources.
  * **Opacity:** Sets the opacity of the lines.
  * **Thickness slider:** Sets the thickness of the lines.



#### Default viewport

Sets the default location of the map's viewport, or inset.

To set a default viewport location, navigate to the chosen location and zoom level on the map chart. Under **Default viewport** in the style properties, select **Set as default view** to save the placement of the map's viewport.

When exploring the map, click the ![](https://docs.cloud.google.com/static/data-studio/images/mapsarbaselinep900fill0wght400grad0opsz24png.png)**Reset viewport** icon on the map chart to return to your default view.

If a map thumbnail and inset are displayed under **Default viewport** , a default viewport is already set for this map. To set a new default view, navigate the map to the new chosen location and zoom setting, and click **Set as default view**.

The **Default viewport** option is best used when the **Allow pan and zoom** map control option is enabled.

#### Colors

The **Colors** setting lets you manage the bubble or filled area colors for specific values of **Color dimension** or **Color metric** fields:

  * If you have defined the **Color dimension** option in the setup properties, both the filled area and bubble layer map colors are managed in the **Colors** style property by selecting **Manage dimension value colors**.
  * If you have defined the **Color metric** option in the setup properties, you can define a color scale by selecting color values for the scale's maximum (**Max color**), middle (**Mid color**), and minimum (**Min color**). You can also specify a color to represent missing data (**Dataless color**).



#### Map Controls

These settings let you select which interactive map view controls will be shown or hidden:

  * **Allow tilt and rotation:** Enables the map to be dragged and tilted in three dimensions. **Allow tilt and rotation** is available when the **Use vector graphics Background Layer** style property is enabled. This control is not available for combo maps or connection maps.
  * **Allow pan and zoom:** Lets viewers adjust the map display with their mouse and keyboard. Users can still tilt the map when **Allow pan and zoom** is disabled if the **Allow tilt and rotation** setting is enabled (or if the **Show in 3D view** setting is enabled for combo maps or connection maps).
  * **Show zoom control:** Shows the ![Add icon.](https://docs.cloud.google.com/static/data-studio/images/gmaddgrey60048dp-2020-03-26.png) plus sign and ![Remove icon.](https://docs.cloud.google.com/static/data-studio/images/gmremovegrey60048dp-2020-03-26.png) minus sign buttons on the map to zoom in and out, respectively.
  * **Show Street View control:** Lets users display Street View images for supported locations.
  * **Show fullscreen control:** Lets users display the map in fullscreen view.
  * **Show map type control:** Lets users switch between map view and satellite view.
  * **Show scale control:** Lets users display the map scale in kilometers or miles.



#### Legends

Legends help your viewers understand the map by describing the colors and bubble sizes that are used.

The following legends are available:

  * A **Size legend** describes the **Size** metric in bubble maps and the **Thickness** metric in connection maps.
  * A **Color legend** describes the **Color dimension** or the **Color metric**. If your map specifies a **Color dimension** , the **Color legend** uses distinct colors for each value. If your map specifies a **Color metric** , the **Color legend** uses a color gradient.
  * A **Weight legend** describes the **Weight** metric.
  * A **Thickness legend** describes the **Thickness** metric that is used in a line map.
  * A **Height legend** describes the height of the **Additional Layer Metric** that is used in a combo map.



For example, here is a bubble map that displays sports venue capacities for different NCAA basketball conferences:

![A bubble map displays the NCAA venue_capacity metric by bubble size and represents the NCAA conf_name dimension with bubble color.](https://docs.cloud.google.com/static/data-studio/images/google-maps-bubble-map-legend-numbered-2020-10-28.png)

The map properties define the **Color metric** as **venue_capacity** , represented in the **Size legend** by bubble size, and the **Color dimension** as **conf_name** , represented in the **Color legend** by bubble color.

In another example, a filled area map of Spain and Portugal depicts the average time that a user spends on a page by their region:

![A filled area map of Spain and Portugal with a color legend displays a gradient of purple to blue based on Avg. Time on Page metric values that range from 00:00:00 to 00:24:40.](https://docs.cloud.google.com/static/data-studio/images/google-maps-filled-map-legend-2020-10-28.png)

The **Color legend** displays a color gradient of time that is spent on a page based on the **Avg. Time on Page** metric.

#### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



#### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



#### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Configure a connection map

A connection map lets you visualize your location data as sequences of points that are connected by a line.

This visualization also supports vector graphics and three-dimensional viewing. When the **Show in 3D view** style setting is enabled and the map is tilted, the line that connects your data points is displayed as an arc. When the **Show in 3D view** style setting is disabled and the map is tilted, or if the map is not tilted, the line that connects your data points is displayed as a line. Visualizing your data connections in three dimensions may be particularly useful if your data point connections appear to overlap when viewed in two dimensions.

Here's a connection map that depicts flights between US cities. Note how the two-dimensional visualization seems to hide the overlapping connections between cities in Georgia and Florida in the southeast. Tilting the map reveals both connections.

### Setup properties

The following setup properties are available for connection maps.

#### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



#### Location fields

These dimensions determine the locations and connection sequence for the data points that appear on the map. These fields can be of any data type, as long as Google Maps can [geocode](https://developers.google.com/maps/documentation/geocoding/overview) the values appropriately. Each dimension's data type should be identical, with the exception that you can connect **Location** values such as **City** or **Country** to latitude-longitude coordinates. For example, you can connect **City** to latitude-longitude or **Country** to latitude-longitude, but you cannot connect **City** to **Country**. If the **Location** types are incompatible, you'll see an error message:

`Warning: Can't show Google Maps Invalid combination of metrics and dimensions Please select dimensions with same geographical/administrative divisions to connect.`

> `To add a data point, enter a dimension for *Point 1*. To connect additional points, click *Add dimension* and select another dimension. When only *Point 1* is specified, the map connects all the values for that dimension. You can connect up to 10 dimensions. The connection map will graph the line between each point sequentially.`

For example, say that your US flight data contained data points for stops that were made before the flight arrived at its final destination. **Point 1** is the origin city, **Point 2** is a layover city, and **Point 3** is the destination city. The connection map will connect **Point 1** to **Point 2** and **Point 2** to **Point 3** to create one continuous line.

##### Tooltip

(Optional) The **Tooltip** field requires a dimension that provides tooltips (labels) for the data. Providing a tooltip lets you override the default label that is provided by the **Location** dimension. For example, you can base the map location on a store's address but use the store's name in the tooltip.

The **Tooltip** option requires unique values for each **Location** value. If the **Tooltip** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Tooltip dimension has multiple values for the same location. Choose a Tooltip dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Color dimension

(Optional) A dimension that provides the categories that are used for the color of the geo data. If you choose this option, you can't use the **Color metric** option.

The **Color dimension** option requires unique values for each **Location** value. If the **Color dimension** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Color dimension has multiple values for the same location. Choose a Color dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Color metric

(Optional) The **Color metric** field requires a metric that provides the values that are used as a color scale for the geo data. If you choose this option, you can't use the **Color dimension** option.

#### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



#### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

#### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



#### Sort

The **Sort** settings in the chart's setup panel control the default sorting behavior. You can select any metric in the chart's data source, or any dimension that is displayed in the chart, to use as the primary or secondary sorting field.

When you specify a metric as a sort field, you can [edit the field's aggregation](https://docs.cloud.google.com/data-studio/edit-fields-in-your-reports). For example, you can include a numeric field in the chart as a `SUM`, but sort on that same field's `AVERAGE` value.

#### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

### Style properties

The following style properties are available for connection maps.

#### Chart title

To add a title to your chart, enable the **Show title** option. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

To have Data Studio generate a title that is based on the chart type and the fields that are used in the chart, enable the **Autogenerate** option. This option is enabled by default when **Show title** is also enabled.

To add a custom title to your chart, enter it in the **Title** field. This will turn off the **Autogenerate** setting.

The following **Chart title** settings control how the map's title appears:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



#### Background layer

These settings control the appearance of the base map:

  * **Use vector graphics:** Enables tilt and optimized graphics. **Use vector graphics** is enabled by default for combo maps and connection maps.
  * **Show in 3D view:** Enables the map to be dragged and tilted in three dimensions. **Show in 3D view** is available only for combo maps and connection maps and is enabled by default.
  * **Type:** Sets the default map background. Options include **Map** , **Satellite with labels** , and **Satellite**. The **Satellite with label** type is available only when the **Use vector graphics** setting is enabled.
  * **Style:** Sets the color theme for the map. Use the report's current theme, or select one of the preset map styles. **Style** is available only when the **Map** type is selected. You can also create a custom map style.
  * **Roads, Landmarks, Labels:** Use the sliders to select the level of background details to display in the map background.



#### Layer type

The **Layer type** setting determines how locations on the map are shown. You can show locations in the following formats:

  * Bubbles
  * Filled areas
  * Line map
  * Connection map
  * Combo map
  * Heatmap



#### Default viewport

Sets the default location of the map's viewport, or inset.

To set a default viewport location, navigate to the chosen location and zoom level on the map chart. Under **Default viewport** in the style properties, select **Set as default view** to save the placement of the map's viewport.

When exploring the map, click the ![](https://docs.cloud.google.com/static/data-studio/images/mapsarbaselinep900fill0wght400grad0opsz24png.png)**Reset viewport** icon on the map chart to return to your default view.

If a map thumbnail and inset are displayed under **Default viewport** , a default viewport is already set for this map. To set a new default view, navigate the map to the new chosen location and zoom setting, and click **Set as default view**.

The **Default viewport** option is best used when the **Allow pan and zoom** map control option is enabled.

#### Connection map layer

  * **Thickness slider:** Sets the thickness of the lines.
  * **Path accuracy (geodesic):** Geodesic paths represent the shortest distance between two points on a sphere. This setting helps to visualize three-dimensional relationships on a two-dimensional surface. When this setting is enabled, when viewing the map in two dimensions, the connection between two points appears as a curved line. When this setting is disabled, when viewing the map in two dimensions, the connection between two points is displayed as a straight line.



#### Colors

The **Colors** setting lets you manage the bubble or filled area colors for specific values of **Color dimension** or **Color metric** fields:

  * If you have defined the **Color dimension** option in the setup properties, both the filled area and bubble layer map colors are managed in the **Colors** style property by selecting **Manage dimension value colors**.
  * If you have defined the **Color metric** option in the setup properties, you can define a color scale by selecting color values for the scale's maximum (**Max color**), middle (**Mid color**), and minimum (**Min color**). You can also specify a color to represent missing data (**Dataless color**).



#### Map controls

These settings let you select which interactive map view controls will be shown or hidden:

  * **Allow tilt and rotation:** Enables the map to be dragged and tilted in three dimensions. **Allow tilt and rotation** is available when the **Use vector graphics Background Layer** style property is enabled. This control is not available for combo maps or connection maps.
  * **Allow pan and zoom:** Lets viewers adjust the map display with their mouse and keyboard. Users can still tilt the map when **Allow pan and zoom** is disabled if the **Allow tilt and rotation** setting is enabled (or if the **Show in 3D view** setting is enabled for combo maps or connection maps).
  * **Show zoom control:** Shows the ![Add icon.](https://docs.cloud.google.com/static/data-studio/images/gmaddgrey60048dp-2020-03-26.png) plus sign and ![Remove icon.](https://docs.cloud.google.com/static/data-studio/images/gmremovegrey60048dp-2020-03-26.png) minus sign buttons on the map to zoom in and out, respectively.
  * **Show Street View control:** Lets users display Street View images for supported locations.
  * **Show fullscreen control:** Lets users display the map in fullscreen view.
  * **Show map type control:** Lets users switch between map view and satellite view.
  * **Show scale control:** Lets users display the map scale in kilometers or miles.



#### Legends

Legends help your viewers understand the map by describing the colors and bubble sizes that are used.

The following legends are available:

  * A **Size legend** describes the **Size** metric in bubble maps and the **Thickness** metric in connection maps.
  * A **Color legend** describes the **Color dimension** or the **Color metric**. If your map specifies a **Color dimension** , the **Color legend** uses distinct colors for each value. If your map specifies a **Color metric** , the **Color legend** uses a color gradient.
  * A **Weight legend** describes the **Weight** metric.
  * A **Thickness legend** describes the **Thickness** metric that is used in a line map.
  * A **Height legend** describes the height of the **Additional Layer Metric** that is used in a combo map.



For example, here is a bubble map that displays sports venue capacities for different NCAA basketball conferences:

![A bubble map displays the NCAA venue_capacity metric by bubble size and represents the NCAA conf_name dimension with bubble color.](https://docs.cloud.google.com/static/data-studio/images/google-maps-bubble-map-legend-numbered-2020-10-28.png)

The map properties define the **Color metric** as **venue_capacity** , represented in the **Size legend** by bubble size, and the **Color dimension** as **conf_name** , represented in the **Color legend** by bubble color.

In another example, a filled area map of Spain and Portugal depicts the average time that a user spends on a page by their region:

![A filled area map of Spain and Portugal with a color legend displays a gradient of purple to blue based on Avg. Time on Page metric values that range from 00:00:00 to 00:24:40.](https://docs.cloud.google.com/static/data-studio/images/google-maps-filled-map-legend-2020-10-28.png)

The **Color legend** displays a color gradient of time that is spent on a page based on the **Avg. Time on Page** metric.

#### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



#### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



#### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Configure a combo map

A combo map lets you combine the properties of a filled map and a bubble map. When you define the filled map with a dimension and the bubble map with a metric, the two map types are layered on a single chart.

Here's a combo map that shows countries with their median age depicted as an overlying bubble layer. Median age is represented by bubble size, with larger bubbles corresponding to higher ages.

![A filled map of African countries with bubbles indicating median population age. The mouse is hovering over Egypt, displaying a tooltip with the filled map layer and additional map layer fields.](https://docs.cloud.google.com/static/data-studio/images/googlemapcombo2d2023-10-24.png)

The **Show in 3D view** style property is available in the **Background layer** style property for combo maps. When this property is enabled, you can tilt the map perspective manually to emphasize the relative size difference of the bubble heights. Here's an example of the same map with the **Show in 3D view** style property enabled:

![A filled map of African countries with cylinders indicating median population age. The map perspective is tilted such that the bubble height indicates the relative scale of the ages.](https://docs.cloud.google.com/static/data-studio/images/googlemapscombo3d2023-10-24.png)

### Setup properties

The following setup properties are available for combo maps.

#### Data source

A data source provides the connection between the component and the underlying dataset.

  * To change the chart's data source, click the current data source name.
  * To view or edit the data source, click the ![](https://docs.cloud.google.com/static/data-studio/images/standard--inline-icon--edit.png)**Edit data source** icon. (You must have at least [Viewer permission](https://docs.cloud.google.com/data-studio/viewer-user-type) to see this icon.)
  * Click **Blend data** to see data from multiple data sources in the same chart. [Learn more about data blending](https://docs.cloud.google.com/data-studio/how-blends-work).



#### Fields

Configure the options in the **Fields** section to set up the map chart data.

##### Location

The **Location** field requires a dimension that determines where the data appears on the map. Note that this field can be of any data type, as long as Google Maps can [geocode](https://developers.google.com/maps/documentation/geocoding/overview) the values appropriately.

##### Additional Layer Metric

The **Additional Layer Metric** field requires a metric that determines the overlying layer on the map.

When the **Show in 3D view** style property is disabled, this layer appears similar to a standard bubble map, with bubble diameter indicating the metric's scale. When the **Show in 3D view** style property is enabled, this layer appears as columns with equal diameters and heights indicating the metric's scale.

##### Tooltip

(Optional) The **Tooltip** field requires a dimension that provides tooltips (labels) for the data. Providing a tooltip lets you override the default label that is provided by the **Location** dimension. For example, you can base the map location on a store's address but use the store's name in the tooltip.

The **Tooltip** option requires unique values for each **Location** value. If the **Tooltip** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Tooltip dimension has multiple values for the same location. Choose a Tooltip dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

##### Color dimension

(Optional) A dimension that provides the categories that are used for the color of the geo data. If you choose this option, you can't use the **Color metric** option.

The **Color dimension** option requires unique values for each **Location** value. If the **Color dimension** values are duplicated, you'll see an error message:

> `Warning: Can't show Google Maps`
> 
> `The Color dimension has multiple values for the same location. Choose a Color dimension that has a unique value for each location.`

To fix this error, use a dimension that has a 1:1 relationship with your **Location** dimension.

If you choose this option, the **Color metric** option is not available, and you cannot specify a color for the **Additional layer** style property.

##### Color metric

(Optional) The **Color metric** field requires a metric that provides the values that are used as a color scale for the geo data. If you choose this option, you can't use the **Color dimension** option.

#### Filter

Filters restrict the data that is displayed in the component by including or excluding the values that you specify. [Learn more about the filter property](https://docs.cloud.google.com/data-studio/about-filter-properties).

Filter options include the following:

  * **Filter name:** Click an existing filter to edit it. Mouse over the filter name and click **X** to delete it.
  * **Add filter:** Click this option to create a new filter for the chart.



#### Date range dimension

This option appears if your data source has a valid date dimension.

**Important:** This option does not appear for Google Ads or Google Analytics data sources, as these automatically select a dimension of type **Date** from the data source.

The date range dimension is used as the basis for limiting the date range of the chart. For example, this is the dimension that is used if you set a date range property for the chart or if a viewer of the report uses a date range control to limit the timeframe.

#### Default date range filter

The default date range filter lets you set a timeframe for an individual chart.

Default date range filter options include the following:

  * **Auto:** Uses the default date range, which is determined by the chart's data source.
  * **Custom:** Lets you use the calendar widget to select a custom date range for the chart.



#### Chart interactions

When the **Cross-filtering** option is enabled on a chart, that chart acts like a filter control. You can filter the report by clicking or brushing your mouse across the chart. [Learn more about cross-filtering](https://docs.cloud.google.com/data-studio/chart-cross-filtering).

### Style properties

The following style properties are available for combo maps.

#### Chart title

To add a title to your chart, enable the **Show title** option. Data Studio can automatically generate a title, or you can create a custom title for the chart. You can also customize the title's styling and placement.

To have Data Studio generate a title that is based on the chart type and the fields that are used in the chart, enable the **Autogenerate** option. This option is enabled by default when **Show title** is also enabled.

To add a custom title to your chart, enter it in the **Title** field. This will turn off the **Autogenerate** setting.

The following **Chart title** settings control how the map's title appears:

  * **Title:** Provides a text field where report editors can enter a custom title for the chart.
  * **Font family:** Sets the font type for the title text.
  * **Font size:** Sets the font size for the title text.
  * **Font color:** Sets the font color for the title text.
  * **Font styling options:** Applies bold, italic, or underline styling to the title text.
  * **Top:** Positions the chart title at the top of the chart.
  * **Bottom:** Positions the chart title at the bottom of the chart.
  * **Left** Aligns the chart title to the left side of the chart.
  * **Center:** Centers the chart title horizontally.
  * **Right:** Aligns the chart title to the right side of the chart.



#### Background layer

These settings control the appearance of the base map:

  * **Use vector graphics:** Enables tilt and optimized graphics. **Use vector graphics** is enabled by default for combo maps and connection maps.
  * **Show in 3D view:** Enables the map to be dragged and tilted in three dimensions. **Show in 3D view** is available only for combo maps and connection maps and is enabled by default.
  * **Type:** Sets the default map background. Options include **Map** , **Satellite with labels** , and **Satellite**. The **Satellite with label** type is available only when the **Use vector graphics** setting is enabled.
  * **Style:** Sets the color theme for the map. Use the report's current theme, or select one of the preset map styles. **Style** is available only when the **Map** type is selected. You can also create a custom map style.
  * **Roads, Landmarks, Labels:** Use the sliders to select the level of background details to display in the map background.



#### Layer type

The **Layer type** setting determines how locations on the map are shown. You can show locations in the following formats:

  * Bubbles
  * Filled areas
  * Line map
  * Connection map
  * Combo map
  * Heatmap



#### Default viewport

Sets the default location of the map's viewport, or inset.

To set a default viewport location, navigate to the chosen location and zoom level on the map chart. Under **Default viewport** in the style properties, select **Set as default view** to save the placement of the map's viewport.

When exploring the map, click the ![](https://docs.cloud.google.com/static/data-studio/images/mapsarbaselinep900fill0wght400grad0opsz24png.png)**Reset viewport** icon on the map chart to return to your default view.

If a map thumbnail and inset are displayed under **Default viewport** , a default viewport is already set for this map. To set a new default view, navigate the map to the new chosen location and zoom setting, and click **Set as default view**.

The **Default viewport** option is best used when the **Allow pan and zoom** map control option is enabled.

#### Additional layer

These options set the appearance of the **Additional Layer Metric** setup property:

  * **Cylinder slider control:** Sets the relative bubble heights, which are apparent when the map is tilted, when the **Show in 3D view** style property is enabled.
  * **Circle slider control:** Sets the relative size of the bubbles.
  * **Opacity:** Sets the opacity of the bubbles.
  * **Additional layer color:** Sets the color of the bubbles.



#### Filled area layer

These options set the appearance of the **Location** dimension:

  * **Opacity:** Sets the opacity of the filled areas.
  * **Border color:** Sets the color of the filled area borders.
  * **Border weight:** Sets the thickness of the filled area borders.



#### Colors

The **Colors** setting lets you manage the bubble or filled area colors for specific values of **Color dimension** or **Color metric** fields:

  * If you have defined the **Color dimension** option in the setup properties, both the filled area and bubble layer map colors are managed in the **Colors** style property by selecting **Manage dimension value colors**.
  * If you have defined the **Color metric** option in the setup properties, you can define a color scale by selecting color values for the scale's maximum (**Max color**), middle (**Mid color**), and minimum (**Min color**). You can also specify a color to represent missing data (**Dataless color**).



#### Map controls

These settings let you select which interactive map view controls will be shown or hidden:

  * **Allow tilt and rotation:** Enables the map to be dragged and tilted in three dimensions. **Allow tilt and rotation** is available when the **Use vector graphics Background Layer** style property is enabled. This control is not available for combo maps or connection maps.
  * **Allow pan and zoom:** Lets viewers adjust the map display with their mouse and keyboard. Users can still tilt the map when **Allow pan and zoom** is disabled if the **Allow tilt and rotation** setting is enabled (or if the **Show in 3D view** setting is enabled for combo maps or connection maps).
  * **Show zoom control:** Shows the ![Add icon.](https://docs.cloud.google.com/static/data-studio/images/gmaddgrey60048dp-2020-03-26.png) plus sign and ![Remove icon.](https://docs.cloud.google.com/static/data-studio/images/gmremovegrey60048dp-2020-03-26.png) minus sign buttons on the map to zoom in and out, respectively.
  * **Show Street View control:** Lets users display Street View images for supported locations.
  * **Show fullscreen control:** Lets users display the map in fullscreen view.
  * **Show map type control:** Lets users switch between map view and satellite view.
  * **Show scale control:** Lets users display the map scale in kilometers or miles.



#### Legends

Legends help your viewers understand the map by describing the colors and bubble sizes that are used.

The following legends are available:

  * A **Size legend** describes the **Size** metric in bubble maps and the **Thickness** metric in connection maps.
  * A **Color legend** describes the **Color dimension** or the **Color metric**. If your map specifies a **Color dimension** , the **Color legend** uses distinct colors for each value. If your map specifies a **Color metric** , the **Color legend** uses a color gradient.
  * A **Weight legend** describes the **Weight** metric.
  * A **Thickness legend** describes the **Thickness** metric that is used in a line map.
  * A **Height legend** describes the height of the **Additional Layer Metric** that is used in a combo map.



For example, here is a bubble map that displays sports venue capacities for different NCAA basketball conferences:

![A bubble map displays the NCAA venue_capacity metric by bubble size and represents the NCAA conf_name dimension with bubble color.](https://docs.cloud.google.com/static/data-studio/images/google-maps-bubble-map-legend-numbered-2020-10-28.png)

The map properties define the **Color metric** as **venue_capacity** , represented in the **Size legend** by bubble size, and the **Color dimension** as **conf_name** , represented in the **Color legend** by bubble color.

In another example, a filled area map of Spain and Portugal depicts the average time that a user spends on a page by their region:

![A filled area map of Spain and Portugal with a color legend displays a gradient of purple to blue based on Avg. Time on Page metric values that range from 00:00:00 to 00:24:40.](https://docs.cloud.google.com/static/data-studio/images/google-maps-filled-map-legend-2020-10-28.png)

The **Color legend** displays a color gradient of time that is spent on a page based on the **Avg. Time on Page** metric.

#### Background and border

These options control the appearance of the chart background container:

  * **Background:** Sets the chart background color.
  * **Opacity:** Sets the chart opacity. 100% opacity completely hides objects behind the chart. 0% opacity makes the chart invisible.
  * **Border color:** Sets the chart border color.
  * **Border radius:** Adds rounded borders to the chart background. When the radius is 0, the background shape has 90° corners. A border radius of 100° produces a circular shape.
  * **Border weight:** Sets the chart border line thickness.
  * **Border style:** Sets the chart border line style.
  * **Add border shadow:** Adds a shadow to the chart's lower and right borders.



#### Chart header

The chart header lets viewers perform various actions on the chart, such as exporting the data, drilling up or down, or sorting the chart. Chart header options include the following:

  * **Chart header:** Controls where the chart header appears on the chart. The **Chart header** options include the following: 
    * **Do not show:** The header options never appear. Note that report viewers can always access the options by right-clicking the chart.
    * **Always show:** The header options always appear.
    * **Show on hover (default):** Three vertical dots appear when you hold the pointer over the chart header. Click these to access the header options.
  * **Header font color:** Sets the color of the chart header options.



#### Reset to report theme

Click **Reset to report theme** to reset the chart settings to the report theme settings.

## Create a custom Google Maps map style

A Google Maps map style lets you customize the visibility and appearance of some map features. You can create a custom Google Maps style in the following ways:

  * Import a map style by editing the map's JSON
  * Create and import a map ID



### Import a map style using JSON

**Warning:** This option is available only when the **Use vector graphics** option of the **Background layer** style setting is disabled.

Create a JSON file for your map with the [Google Maps Platform Styling Wizard](https://mapstyle.withgoogle.com/):

  1. In the **Style** drop-down menu of the **Background layer** style setting, select **Edit JSON**.
  2. In the **Import map ID** dialog, select the [Google Maps Platform Styling Wizard](https://mapstyle.withgoogle.com/), and then select the **Use the legacy JSON styling wizard** option from the notification dialog.
  3. Customize the features and theme of your map style. Select **Finish**.
  4. To use this JSON styling, select **Copy JSON** from the **Use JSON styling** dialog.
  5. Return to the **Import map style** dialog in Data Studio, and paste in the copied JSON in the code block.
  6. Select **Import**.



Your new map style will be applied to your map. It will appear in the **Style** drop-down menu as **Custom**.

### Create and import a map ID

**Warning:** This option is available only when the **Use vector graphics** option of the **Background layer** style setting is enabled.

Before you can create and import a map ID, you must first [create a new map style](https://developers.google.com/maps/documentation/cloud-customization/map-styles#create-new-style) and a map ID in the Google Cloud console. To create a map ID in the Google Cloud console, you must have a role that includes the [`mapsadmin.clientMaps.list`](https://docs.cloud.google.com/iam/docs/permissions-reference) on a Google Cloud project.

To create and import a map style, follow these steps:

  1. In the **Style** drop-down menu of the **Background layer** style setting, select **Edit custom Map ID**.
  2. In the **Import map ID** dialog, select **Google Maps Platform**.
  3. On the **Map management** page in the Google Cloud console, select [Create map ID](https://developers.google.com/maps/documentation/get-map-id#create-a-map-id).
  4. In the **Create map ID** dialog, enter or select the following information, as applicable: 
     * In the **Name** field, enter a name for the new map style. This name will appear as an option in the **Style** drop-down menu of the Data Studio map settings.
     * Optionally, in the **Description** field, enter a description for the maps style.
     * In the **Map type** drop-down, select **JavaScript**. Then select **Vector**. Optionally, enable tile or rotation for your map style.
     * Select **Save**.
  5. On the **Map management** page, copy the map ID.
  6. Return to Data Studio. In the **Import map ID** dialog, paste in the copied map ID in the **Paste Map ID here** field.
  7. Select **Import**.



Your new map style will be applied to your map. It will appear in the **Style** drop-down menu as **Custom**.

## Related resources

  * [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)
  * [Dates and times](https://docs.cloud.google.com/data-studio/dates-and-times)
  * [About filter properties](https://docs.cloud.google.com/data-studio/about-filter-properties)
  * [Visualize BigQuery `GEOGRAPHY` polygons with Data Studio](https://docs.cloud.google.com/data-studio/visualize-bigquery-geography-polygons)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
