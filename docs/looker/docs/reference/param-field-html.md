---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-html/
title: html \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:36.056555+00:00
---

# html  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-html/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  html Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        html: <img src="https://www.brettcase.com/
              product_images/{{ value }}.jpg"/> ;;
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `html` |  Possible Field Types Dimension, Dimension Group, Measure Accepts An HTML expression, possibly using Liquid template elements, followed by two semicolons  
---|---  
  
## Definition

The `html` parameter lets you specify the HTML that will be contained by a field.

You can also get access to the values that would typically be in the field by using [Liquid variables](https://github.com/Shopify/liquid/wiki/Liquid-for-Designers). This lets you create a number of useful functions, including links to other related Looks, links to external websites, or images.

HTML formatting only renders in [table](https://docs.cloud.google.com/looker/docs/table-options), [table (legacy)](https://docs.cloud.google.com/looker/docs/legacy-table-options), and [single value](https://docs.cloud.google.com/looker/docs/single-value-options) chart visualizations and in visualization [tooltips](https://docs.cloud.google.com/looker/docs/tooltip-customization) when multiple fields are combined. Any interactive content that is placed in a [map chart's](https://docs.cloud.google.com/looker/docs/map-options#viewing_map_charts_in_the_new_dashboard_experience) tooltip with the `html` parameter will not be accessible on dashboards that use the [new dashboard experience](https://docs.cloud.google.com/looker/docs/viewing-dashboards), although it will be accessible on Looks, Explores, and [legacy dashboards](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards).

When [downloading content](https://docs.cloud.google.com/looker/docs/downloading), HTML formatting is not applied to text-based download formats, such as TXT, CSV, Excel, or JSON.

### Using valid HTML

In order to prevent certain security exploits, Looker restricts which HTML tags and attributes may be used, as well as which CSS properties may be used. See our [HTML sanitization](https://docs.cloud.google.com/looker/docs/html-sanitization) documentation page for more details.

### Liquid variables

The `html` parameter supports Liquid variables. See the [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) documentation page for information about how to make full use of these variables.

## Examples

Here are some examples for using the `html` field parameter.

> HTML formatting only renders in [table](https://docs.cloud.google.com/looker/docs/table-options), and [single value](https://docs.cloud.google.com/looker/docs/single-value-options) chart visualizations and in visualization [tooltips](https://docs.cloud.google.com/looker/docs/creating-visualizations#the_visualization_tooltip) when multiple fields are combined. Any interactive content that is placed in a [map chart's](https://docs.cloud.google.com/looker/docs/map-options#viewing_map_charts_in_the_new_dashboard_experience) tooltip with the `html` parameter will not be accessible on [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards), although it will be accessible on Looks and Explores.

Additional examples of how to use HTML to customize the font and colors of field values in visualizations are available on the [Conditional formatting customization](https://docs.cloud.google.com/looker/docs/best-practices/cookbook-visualizations-conditional-formatting) page and [Visualization tooltip customization](https://docs.cloud.google.com/looker/docs/best-practices/cookbook-visualizations-tooltip-customization) page of the [Getting the most out of visualizations in Looker](https://docs.cloud.google.com/looker/docs/best-practices/cookbook-visualizations-in-Looker) cookbook.

### Using Liquid variables in the `html` parameter

This example shows how most of the Liquid variables would appear in an `html` parameter. Consider a `total_order_amount` definition:
    
    
    measure: total_order_amount {
      type: sum
      sql: ${order_amount} ;;
      value_format: "0.00"
      html:
        <ul>
          <li> value: {{ value }} </li>
          <li> rendered_value: {{ rendered_value }} </li>
          <li> linked_value: {{ linked_value }} </li>
          <li> link: {{ link }} </li>
          <li> model: {{ _model._name }} </li>
          <li> view: {{ _view._name }} </li>
          <li> explore: {{ _explore._name }} </li>
          <li> field: {{ _field._name }} </li>
          <li> dialect: {{ _dialect._name }} </li>
          <li> access filter: {{ _access_filters['company.name'] }} </li>
          <li> user attribute: {{ _user_attributes['region'] }} </li>
          <li> query timezone: {{ _query._query_timezone }} </li>
          <li> filters: {{ _filters['order.total_order_amount'] }} </li>
        </ul> ;;
    }
    

The cell value displayed for `total_order_amount` would look like this:
    
    
      • value: 8521935
      • rendered_value: 8,521,935.00
      • linked_value: 8,521,935.00
      • link: /explore/thelook/orders?fields=orders.order_amount&limit=500
      • model: thelook
      • view: orders
      • explore: order_items
      • field: total_order_amount
      • dialect: mysql
      • access filter: altostrat.com
      • user attribute: northeast
      • query timezone: America/Los_Angeles
      • filters: NOT NULL
    
    
    
    

### Conditionally format a measure

Conditionally format a count according to its values:
    
    
    measure: formatted_count {
      type: count
      html:
        {% if value > 100 %}
          <span style="color:darkgreen;">{{ rendered_value }}</span>
        {% elsif value > 50 %}
          <span style="color:goldenrod;">{{ rendered_value }}</span>
        {% else %}
          <span style="color:darkred;">{{ rendered_value }}</span>
        {% endif %} ;;
    }
    

### Exploring data with the `html` parameter

> HTML formatting only renders in [table](https://docs.cloud.google.com/looker/docs/table-options), [table (legacy)](https://docs.cloud.google.com/looker/docs/legacy-table-options), and [single value](https://docs.cloud.google.com/looker/docs/single-value-options) chart visualizations and in visualization [tooltips](https://docs.cloud.google.com/looker/docs/tooltip-customization) when multiple fields are combined. Any interactive content that is placed in a [map chart's](https://docs.cloud.google.com/looker/docs/map-options#viewing_map_charts_in_the_new_dashboard_experience) tooltip with the `html` parameter will not be accessible on dashboards that use the [new dashboard experience](https://docs.cloud.google.com/looker/docs/viewing-dashboards), although it will be accessible on Looks, Explores, and [legacy dashboards](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards).

Imagine you have a field in your data called `status`, which gives the status of each order. The possible values for `status` are:

  * `Paid`
  * `Shipped`
  * `Returned`



While exploring your data, you might want to have a separate background color for each status. This can be done using [Liquid](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) html in the `html:` parameter of a dimension. This would look something like:
    
    
    dimension: status {
      sql: ${TABLE}.status ;;
      html: {% if value == 'Paid' %}
          <p style="color: black; background-color: lightblue; font-size:100%; text-align:center">{{ rendered_value }}</p>
        {% elsif value == 'Shipped' %}
          <p style="color: black; background-color: lightgreen; font-size:100%; text-align:center">{{ rendered_value }}</p>
        {% else %}
          <p style="color: black; background-color: orange; font-size:100%; text-align:center">{{ rendered_value }}</p>
        {% endif %}
    ;;
    }
    

In your table, the background color of each cell will vary depending on the value of the `status` field. The background color will be light blue when the value is **Paid** , light green when it is **Shipped** , and orange when the value is anything else. For example, if your table contains a value **Returned** , that cell will have an orange background.

![](https://docs.cloud.google.com/static/looker/docs/images/develop-field-params-html-liquid-2316.png)

You can use the same syntax to add icons or images based on cell values:
    
    
    dimension: status {
        sql: ${TABLE}.status ;;
        html: {% if value == 'Shipped' or value == 'Complete' %}
             <p><img src="https://findicons.com/files/icons/573/must_have/48/check.png" alt="" height="20" width="20">{{ rendered_value }}</p>
          {% elsif value == 'Processing' %}
            <p><img src="https://findicons.com/files/icons/1681/siena/128/clock_blue.png" alt="" height="20" width="20">{{ rendered_value }}</p>
          {% else %}
            <p><img src="https://findicons.com/files/icons/719/crystal_clear_actions/64/cancel.png" alt="" height="20" width="20">{{ rendered_value }}</p>
          {% endif %}
    ;;
    }
    

In your table, this will look like:

Order Items Status | Order Items Count  
---|---  
![Cancelled icon.](https://docs.cloud.google.com/static/looker/docs/images/cancel.png)Cancelled | 6,316  
![Complete icon.](https://docs.cloud.google.com/static/looker/docs/images/check.png)Complete | 232,791  
![Processing icon.](https://docs.cloud.google.com/static/looker/docs/images/clock_blue.png)Processing | 809  
![Cancelled icon.](https://docs.cloud.google.com/static/looker/docs/images/cancel.png)Returned | 2,354  
![Complete icon.](https://docs.cloud.google.com/static/looker/docs/images/check.png)Shipped | 1,474  
  
### Generating product images

Here is an example of how to add the picture of a product into Looker using an `<img>` tag, based on the product's ID:
    
    
    dimension: product_image {
      sql: ${product_id} ;;
      html: <img src="https://www.altostrat.com/product_images/{{ value }}.jpg" /> ;;
    }
    

### Maintaining drill-down links

To maintain [drill-down](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#drilling_down_into_the_data) links when you're formatting output using the `html` parameter, you can include the HTML tag `<a href="#drillmenu" target="_self">`. For example:
    
    
    measure: count {
      type: count
      drill_fields: [detail*]
      html:
        <a href="#drillmenu" target="_self">
          {% if value > 10000 %}
            <span style="color:#42a338;">{{ rendered_value }}</span>
          {% elsif value > 5000 %}
            <span style="color:#ffb92e;">{{ rendered_value }}</span>
          {% else %}
            <span style="color:#fa4444;">{{ rendered_value }}</span>
          {% endif %}
        </a>;;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
