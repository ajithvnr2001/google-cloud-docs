---
url: https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-type/
title: type (for LookML dashboards) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:33.674646+00:00
---

# type (for LookML dashboards)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  type (for LookML dashboards) Stay organized with collections  Save and categorize content based on your preferences. 

> This page refers to the `type` parameter that is part of a [dashboard element](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element).
> 
> `type` can also be used as part of a dashboard filter, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#type-for-filters) documentation page.
> 
> `type` can also be used as part of a join, described on the [`type`](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) documentation page.
> 
> `type` can also be used as part of a dimension, described on the [Dimension, filter, and parameter types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) documentation page.
> 
> `type` can also be used as part of a measure, described on the [Measure types](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) documentation page. 

The `type` parameter determines the [type of visualization](https://docs.cloud.google.com/looker/docs/visualization-types) to be used in a LookML dashboard element, which is created using the [`elements` parameter](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#elements_2). The `type` parameter is defined with other LookML dashboard parameters in a [`dashboard.lkml` file](https://docs.cloud.google.com/looker/docs/other-project-files#dashboard_files).

## Usage

The `type` parameter for LookML dashboards accepts the following values:
    
    
    elements:
    - name: element_name
      type: looker_column | looker_bar | looker_scatter | looker_line | looker_area | looker_pie |
            looker_donut_multiples | looker_funnel | looker_timeline | looker_waterfall | text | single_value |
            looker_single_record | table | looker_grid | looker_map | looker_google_map | looker_geo_coordinates |
            looker_geo_choropleth | looker_boxplot | button
    
    

## LookML dashboard element types

#### [`looker_column`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-column-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-column-610.png) If multiple measures are specified, each measure becomes a y-axis series. If pivots are present, each pivot and measure combination becomes a y-axis series. If no measures are specified, two dimensions can be plotted.  | 

#### [`looker_bar`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-bar-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-bar-610.png) If multiple measures are specified, each measure becomes an x-axis series. If pivots are present, each pivot and measure combination becomes an x-axis series. If no measures are specified, two dimensions can be plotted.   
---|---  
  
#### [`looker_scatter`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-scatter-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-scatter-610.png) If two dimensions are specified, the first dimension is placed on the y-axis and the second dimension is placed on the x-axis. If multiple measures are specified, each measure becomes a y-axis series. If pivots are present, each pivot and measure combination becomes a y-axis series. If no measures are specified, two dimensions can be plotted.  | 

#### [`looker_line`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-line-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-line-610.png) If multiple measures are specified, each measure becomes a y-axis series. If pivots are present, each pivot and measure combination becomes a y-axis series. If no measures are specified, two dimensions can be plotted.   
  
#### [`looker_area`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-area-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-area-610.png) If multiple measures are specified, each measure becomes a y-axis series. If pivots are present, each pivot and measure combination becomes a y-axis series. If no measures are specified, two dimensions can be plotted.  | 

#### [`looker_pie`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-pie-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-pie-610.png) Elements of `type: looker_pie` require one dimension and one measure.   
  
#### [`looker_donut_multiples`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-donut-multiples-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-donut-multiples-610.png) Elements of `type: looker_donut_multiples` require one regular dimension, one pivoted dimension, and one measure. Each value of the regular dimension defines the donuts, and each value of the pivoted dimension defines the slices.  | 

#### [`looker_funnel`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-funnel-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-funnel-610.png) Elements of `type: looker_funnel` are composed from a single set of numbers and a single set of labels, defined using the `dimensions` and `measures` parameters.   
  
#### [`looker_timeline`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-timeline-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-timeline-2214.png) To create an element of `type: looker_timeline`, your query must include values for the `dimensions` and `measures` parameters, including at least one dimension representing the label field, such as a name, as well as a start field and an end field, which can be a date or number. See the [Timeline chart options](https://docs.cloud.google.com/looker/docs/timeline-options#overview) documentation page for more information about the minimum requirements for creating timeline charts in Looker.  | 

#### [`looker_waterfall`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-waterfall-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-waterfall-610.png) Elements of `type: looker_waterfall` require either one dimension and one measure or no dimensions and one or more measures.   
  
#### [`text`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-text-tile)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-text-tile-610.png) Elements of `type: text` display static text elements with various text sizes.  | 

#### [`single_value`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-single-value-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-single-value-610.png) Elements of `type: single_value` display a single measure or dimension. If the query returns more than one cell, the first measure displays; if there are no measures, the first dimension displays.   
  
#### [`looker_single_record`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-single-record-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-single-record-2214.png) Elements of `type: looker_single_record` accept any number of dimensions and measures. Pivots are not supported. If the query returns multiple rows, only the first one is shown.  | 

#### [`table`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-table-chart-legacy)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-table-610.png) Elements of `type: table` accept any number of dimensions, pivots, and measures.   
  
#### [`looker_grid`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-table-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-new-table-624.png) Elements of `type: looker_grid` accept any number of dimensions, pivots, and measures.  | 

#### [`looker_map`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-map)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-interactive-map-610.png) Elements of `type: looker_map` are useful for visualizing geographic data on responsive and interactive maps. A `looker_map` element requires at least one dimension that is of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location) or [`type: zipcode`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode), or that has a [map layer](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) associated with it.   
  
#### [`looker_geo_coordinates`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-coordinate-map)

![](https://docs.cloud.google.com/static/looker/docs/images/looker_geo_coordinates_1.png) Elements of `type: looker_geo_coordinates` are useful for plotting data that is represented by points. To plot regions, use `looker_geo_choropleth`. Coordinates maps plot a single measure and a single dimension of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location) or [`type: zipcode`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode). Additional dimensions will show in the tooltip when you hold the pointer over the data point.  | 

#### [`looker_geo_choropleth`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-choropleth-map)

![](https://docs.cloud.google.com/static/looker/docs/images/looker_geo_choropleth_1.png) Elements of `type: looker_geo_choropleth` are useful for plotting data that is represented by regions. To plot individual points, use `looker_geo_coordinates`. Choropleth maps plot a single measure and a single dimension of [`type: string`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#string), which contains either a US state (`map: usa`) or an [ISO 3166-1 alpha-3 country code](http://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) (`map: world`). Additional dimensions will show in the tooltip when you hold the pointer over the data point.   
  
#### [`looker_google_map`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-google-maps)

![](https://docs.cloud.google.com/static/looker/docs/images/gmaps-automagic-heatmap-option-2212.png) Elements of `type: looker_google_map` are useful for plotting geographic data on responsive and interactive maps. A `looker_google_map` element requires at least one dimension that is of [`type: location`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#location) or [`type: zipcode`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#zipcode), or that has a [map layer](https://docs.cloud.google.com/looker/docs/reference/param-field-map-layer-name) associated with it. Google Map charts are supported only by LookML dashboards with [`preferred_viewer`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#preferred_viewer) set to `dashboards-next`.  | 

#### [`looker_boxplot`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-boxplot-chart)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-boxplot-720-v2.png) Elements of `type: looker_boxplot` are useful for visualizing the [distribution](https://en.wikipedia.org/wiki/Five-number_summary) and [spread](https://en.wikipedia.org/wiki/Statistical_dispersion) of values in your dataset. They can be especially useful for comparing values across categories. Boxplot elements require at least one dimension, along with either two, three, or five measures.   
  
#### [`button`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-button)

![](https://docs.cloud.google.com/static/looker/docs/images/dashboard-reference-button-2206.png) Elements of `type: button` are useful for placing links within your dashboards. You can link to Looker content, such as Looks and dashboards, or to other websites. Buttons are supported only by LookML dashboards with [`preferred_viewer`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#preferred_viewer) set to `dashboards-next`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
