---
url: https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-button/
title: Button parameters for LookML dashboards \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:35.607508+00:00
---

# Button parameters for LookML dashboards  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-button/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Button parameters for LookML dashboards Stay organized with collections  Save and categorize content based on your preferences. 

Buttons are supported only by LookML dashboards with the following settings:

  * [`preferred_viewer`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#preferred_viewer) set to `dashboards-next`
  * [`layout`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout) set to `newspaper`



This page demonstrates how to add and customize a LookML dashboard element of `type: button` with LookML dashboard parameters in a [`dashboard.lkml` file](https://docs.cloud.google.com/looker/docs/other-project-files#dashboard_files). Buttons are useful for placing links within your dashboards. You can link to Looker content, such as Looks and dashboards, or to other websites.

For information about adding buttons to a dashboard through the Looker UI, see the [Creating user-defined dashboards](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_buttons) documentation page.

## Example usage
    
    
    ## BASIC PARAMETERS
    type: button
    name: text
    height: N
    width: N
    row: N
    col: N
    
    ## BUTTON PARAMETER
    rich_content_json: '{
     "text": "button text",
     "description": "description",
     "newTab": true | false,
     "alignment": "left" | "right" | "center",
     "size": "small" | "medium" | "large",
     "style": "OUTLINED" | "FILLED" | "TRANSPARENT",
     "color": "hex string or css color",
     "href": "link"
     }'
    
    

## Parameter definitions

Parameter Name | Description  
---|---  
Basic Parameters  
`type` (for elements) | Determines the type of visualization to be used in the element  
`name` (for elements) | Creates an element  
`height` (for elements) | Defines the height of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box). Height is in units of rows for [`layout: newspaper`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`width` (for elements) | Defines the width of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box). Width is in units of columns for [`layout: newspaper`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`row` | Defines the top-to-bottom position of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box) in units of rows for [`layout: newspaper`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
`col` | Defines the left-to-right position of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box) in units of columns for [`layout: newspaper`](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#layout) dashboards  
Button Parameter  
`rich_content_json` | A JSON object that contains key/value pairs with information about the button   
  
## Basic parameters

When defining a LookML dashboard element of `type: button`, you must specify values for at least the `name` and `type` parameters.

The `height`, `width`, `row`, and `col` parameters apply to a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box), not to the button itself.

### `name`

> This section refers to the `name` parameter that is part of a [dashboard element](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element).
> 
> `name` can also be used as part of a dashboard filter, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#name-for-filters) documentation page.

Each `name` declaration creates a new dashboard element and assigns it a name. Element names must be unique.

The `name` given to the button will not appear in the dashboard UI.
    
    
    - name: orders_by_date
    

### `type`

> This section refers to the `type` parameter that is part of a [dashboard element](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element).
> 
> `type` can also be used as part of a dashboard filter, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#type-for-filters) documentation page.
> 
> `type` can also be used as part of a join, described on the [`type` (for joins)](https://docs.cloud.google.com/looker/docs/reference/param-explore-join-type) parameter documentation page.
> 
> `type` can also be used as part of a dimension, described on the [Dimension, filter, and parameter types](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) documentation page.
> 
> `type` can also be used as part of a measure, described on the [Measure types](https://docs.cloud.google.com/looker/docs/reference/param-measure-types) documentation page.

The `type` parameter determines the type of visualization to be used in the element.
    
    
    - name: element_name
      type: text | looker_grid | table | single_value | looker_single_record |
            looker_column | looker_bar | looker_scatter | looker_line | looker_area |
            looker_pie | looker_donut_multiples | looker_funnel | looker_timeline |
            looker_map | looker_geo_coordinates | looker_geo_choropleth | looker_waterfall |
            looker_wordcloud | looker_boxplot | button
    

See the [`type` (for LookML dashboards)](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-type) documentation page for an overview of the different types of LookML dashboard elements.

### `height`

> This section refers to the `height` parameter that is part of a [dashboard element](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element).
> 
> `height` can also be used as part of a dashboard row, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#height-for-rows) documentation page.

The `height` parameter defines the height of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box), in units of row.

Button element tile boxes default to a height of 6 rows. The minimum height is 1 row. Changing button element height may affect other elements on the dashboard but will not affect the height of the button itself.

For example, the following code sets the button's tile box to be 12 rows tall:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        height: 12
        ...
    

### `width`

> This section refers to the `width` parameter that is part of a [dashboard element](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard-element).
> 
> `width` can also be used as part of a dashboard, described on the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#width-for-dashboard) documentation page.

The `width` parameter defines the width of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box), in units of columns.

The width of a button element's tile box defaults to 8 columns, which is one-third of the full width of a dashboard. The minimum width for a button's tile box is `2`.

For example, the following code sets a button's tile box to half the width of the dashboard:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        width: 12
        ...
    

If there is room within a button's tile box, the button's width will increase to accommodate a long string of text, which is defined in `text`. However, the button's width will not increase beyond the value set in the `width` parameter; and, if necessary, the string defined in `text` will be truncated on the button.

### `row`

The `row` parameter defines the row that the top edge of a button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box) is placed on.

A dashboard begins with row 0 at the top of the dashboard. Dashboard button elements default to an element height of 6 rows, meaning the dashboard elements at the top of a dashboard (`row: 0`) would default to taking up rows 0-5.

In the following example, the code sets a button's tile box to be placed on the second row of elements in the dashboard, assuming elements are set at the default height:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        row: 6
        ...
    

### `col`

The `col` parameter defines the column that the left edge of the button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box) is placed on.

Dashboards are divided into 24 columns. A dashboard begins with column 0 at the left of the dashboard. A dashboard with newspaper layout defaults to an element width of 8 columns, meaning the dashboard elements at the left of a dashboard (`col: 0`) would default to taking up columns 0-7.

For example, the following code sets an element to be set in the third column of elements in the dashboard:
    
    
    - dashboard: sales_overview
      layout: newspaper
      ...
    
      elements:
      - name: orders_by_date
        col: 16
        ...
    

## Button parameter

The parameter described in this section can be used to add content to a LookML dashboard element of `type: button`.

### `rich_content_json`

`rich_content_json` is a JSON object with several key and value pairs that define characteristics of the dashboard button.

The following example usage demonstrates a dashboard button that navigates to another dashboard.
    
    
    rich_content_json: '{
     "text": "Go to Sales Dashboard",
     "description": "View sales from the last 18 months.",
     "newTab": true,
     "alignment": "center",
     "size": "medium",
     "style": "FILLED",
     "color": "forestgreen",
     "href":"https://instance_name.looker.com/dashboards/152?State=California&Created+Fiscal+Quarter=2022"
     }'
    

The following example usage demonstrates a dashboard button that navigates to a [tab on the dashboard](https://docs.cloud.google.com/looker/docs/tabbed-dashboards).
    
    
    rich_content_json: '{
     "text": "Go to Users tab",
     "description": "View user data from the last 18 months.",
     "newTab": false,
     "alignment": "center",
     "size": "medium",
     "style": "FILLED",
     "color": "forestgreen",
     "targetTabName":"Users"
     "href":""
     }'
    

#### `text`

`text` defines the text that will appear on the button in the dashboard UI. The button expands in width to accommodate the text until it reaches the limit set by the `width` parameter, at which point the text will be truncated.

#### `description`

`description` defines text that appears as a tooltip when you hold your cursor over the button. If no description is provided, it defaults to show the link provided in `href`.

#### `newTab`

`newTab` is a Boolean that defines whether the button link will open in a new tab (`true`) or open in the current tab (`false`). `newTab` defaults to `true`.

#### `alignment`

`alignment` sets the alignment of the button within the button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box). `alignment` defaults to `center`.

#### size

`size` sets the size of the button and its text to `small`, `medium`, or `large`. The value of `size` does not affect the size of the button element's [tile box](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#tile-box) or the `height` parameter.

#### `style`

`style` sets the style of the button to one of the following values:

  * **`FILLED`** : The button's body is filled by the color set in `color`. The button's text is white. This is the default value.
  * **`OUTLINED`** : The button has an outline around its edge but its body is transparent. The color of the button text is set by `color`.
  * **`TRANSPARENT`** : The button's body is transparent. The color of the button text is set by `color`.



#### `color`

`color` sets the color of the button or the button's text, depending on the `style` setting. `color` defaults to the first color in the Looker instance's [default categorical color collection](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#default_visualization_colors).

Color values can be formatted as hex strings, such as `#2ca6cd`, or as [CSS color names](https://www.w3schools.com/cssref/css_colors.asp), such as `mediumblue`.

#### `targetTabName`

If your dashboard has tabs, `targetTabName` sets the dashboard tab to which the button will take users.

Learn more about [tabbed dashboards](https://docs.cloud.google.com/looker/docs/tabbed-dashboards).

#### `href`

`href` sets the URL to which the button will take users. Links to other Looker dashboards can contain filter parameters that set dashboard filters to specific values.

**Note:** In an [embedded experience](https://docs.cloud.google.com/looker/docs/private-embedding#embedding_a_dashboard), links to dashboards should contain `embed/` in the link URL.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
