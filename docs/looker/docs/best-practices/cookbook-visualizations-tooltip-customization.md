---
url: https://docs.cloud.google.com/looker/docs/best-practices/cookbook-visualizations-tooltip-customization/
title: Getting the most out of Looker visualizations cookbook: Tooltip customization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:00.348133+00:00
---

# Getting the most out of Looker visualizations cookbook: Tooltip customization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/cookbook-visualizations-tooltip-customization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Getting the most out of Looker visualizations cookbook: Tooltip customization Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page is part of the [Looker cookbook: Getting the most out of Looker visualizations](https://docs.cloud.google.com/looker/docs/best-practices/cookbook-visualizations-in-looker).**Tip:** Starting in Looker 24.0, you can use the [Chart Config Editor](https://docs.cloud.google.com/looker/docs/chart-config-editor#customize_tooltip_color) to further customize tooltip style and color.**Tip:** Starting in Looker 26.4, the **Custom Tooltips** setting lets you configure tooltips within the [Explore visualization editor](https://docs.cloud.google.com/looker/docs/creating-visualizations#quick_guide) by using a combination of UI settings and an HTML editor that supports Liquid templating. [Learn more about custom tooltips](https://docs.cloud.google.com/looker/docs/custom-tooltips).

The [visualization tooltip](https://docs.cloud.google.com/looker/docs/creating-visualizations#the_visualization_tooltip) displays the value of the selected dimensions and measures by default and can help users understand the significance of a single point of data.

For example, a tooltip for a map visualization that is based on **Total Gross Margin** grouped by **State** will display values for both fields when a user hovers over the state of California.

![A user hovers their cursor over California to display a tooltip with the State value 'California' and Total Gross Margin value '$988,018.58'.](https://docs.cloud.google.com/static/looker/docs/images/tooltip-default-2214.png)

However, what if you want to include fields _other_ than the default in the tooltip so that users can get more information or context about a datapoint without needing to look elsewhere?

You can customize the tooltip to display values from multiple specified fields — including fields that are not in the Explore query.

**Caution:** HTML formatting only renders in [table](https://docs.cloud.google.com/looker/docs/table-options), [table (legacy)](https://docs.cloud.google.com/looker/docs/legacy-table-options), and [single value](https://docs.cloud.google.com/looker/docs/single-value-options) chart visualizations and in visualization tooltips when multiple fields are combined. Any interactive content that is placed in a [map chart's](https://docs.cloud.google.com/looker/docs/map-options#viewing_map_charts_in_the_new_dashboard_experience) tooltip with the `html` parameter will not be accessible on dashboards that use the [new dashboard experience](https://docs.cloud.google.com/looker/docs/viewing-dashboards), although the content will be accessible on Looks and Explores.

## Ingredients

  * [Liquid variables](https://docs.cloud.google.com/looker/docs/liquid-variable-reference) — Liquid variables render the values of other fields in conjunction with the existing Explore query.
  * [`html` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-html) — The fields that are defined in the `html` parameter of a measure will render in the tooltip when a user hovers over a visualization.
  * Visualization — The tooltip will appear when a user hovers their cursor over a datapoint in certain visualization types. 
    * [Cartesian charts](https://docs.cloud.google.com/looker/docs/visualization-guide#cartesian_charts)
    * [Pie or donut charts](https://docs.cloud.google.com/looker/docs/visualization-guide#pie_and_donut_charts)
    * [Progression charts](https://docs.cloud.google.com/looker/docs/visualization-guide#progression_charts)
    * [Map charts](https://docs.cloud.google.com/looker/docs/visualization-guide#maps)



## Prerequisites

Customizing the tooltip requires the following:

  * Permissions to [create Explores](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) and permissions to [develop LookML](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop).
  * Knowledge of SQL and LookML development.
  * A basic knowledge of using Liquid in Looker and HTML coding. Visit the [Using Liquid variables in the `html` parameter](https://docs.cloud.google.com/looker/docs/reference/param-field-html#using_liquid_variables_in_the_html_parameter) section of the [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) documentation page for necessary background information.
  * Permissions to [save content](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#save_content) (if you want to save the visualization as a Look or a dashboard)



## Considerations for tooltip customization

It is important to consider the following when you're customizing a tooltip:

  * The values in the `html` parameter become the y-axis of a visualization.
  * The value that you want to display on the y-axis should be the value in the `sql` parameter of the measure.
  * When you're using any formatted measure (a measure of `type: percent_of_total` or a measure with a `value_format_name` or `value_format` parameter), make sure to use the Liquid syntax for the rendered value `{{ field_name._rendered_value }}` (where `field_name` is the actual name of the measure or dimension).



## Example

**Note:** The example in this section extrapolates upon the example map **Total Gross Margin** grouped by **State** introduced earlier on this page.

By default, the tooltip for the visualization data points will include the values for **Total Gross Margin** and **State**. However, what if you wanted to provide users with additional information that is not indicated on the map or included in the Explore query? What if you wanted to include the value for a field called **Percent of Total Gross Margin** instead of **State**? Including **Percent of Total Gross Margin** will help users understand how the **Total Gross Margin** value for an individual data point compares to the total gross margin across the data set.

To customize the tooltip, follow these steps:
    
    
    measure: total_gross_margin {
      type: sum
      value_format_name: decimal_2
      sql: ${gross_margin} ;;
      html: {{ rendered_value }} | {{percent_of_gross_margin._rendered_value }} of total ;;
    }
    

  1. In [**Development Mode**](https://docs.cloud.google.com/looker/docs/dev-mode-prod-mode#development_mode), navigate to the LookML definition for the field that you want to customize.

You can navigate directly to a field's LookML definition [from an Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#features_for_developers).

  2. Determine the fields and values that you want to include in the tooltip in addition to the original field. For example, **Percent of Total Gross Margin**.

  3. Add an `html` parameter to the original measure that is referenced in the Explore query and displayed in the tooltip. In this case, the measure that is currently in the Explore query and displayed in the tooltip is **Total Gross Margin**.

  4. In the `html` parameter, create an expression with Liquid variables that appends the additional fields to the existing measure's value.

     * This example uses the Liquid variable `_rendered_value` to display [Looker formatted values](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name). For example, `total_gross_margin` uses Looker formatting for two decimals, and `percent_of_total_gross_margin` uses Looker formatting for percentage with two decimals.
     * You can use a pipe character,`|`, to separate the values for different fields.
     * You can also append other words that might clarify the meaning of the other values that are rendered in the tooltip. In this case, `of total` is added to clarify what the percentage value means.
  5. Save, validate, and push your code to production after verifying that it works as expected.


**Note:** The input of the `html` parameter only impacts how the value is rendered to users. It does _not_ change the underlying value in the database.

The tooltip will now display two values when a user hovers over a data point with the tooltip: the `total_gross_margin` value of the data point, and the corresponding `percent_of_total_gross_margin` value.

![](https://docs.cloud.google.com/static/looker/docs/images/tooltip-custom-2214.png)

## Next steps

Once you have created your visualization with a customized tooltip, you can share it with others:

  * [Save your Explore as a Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks)
  * [Add the Explore to a dashboard](https://docs.cloud.google.com/looker/docs/creating-user-defined-dashboards#adding_query_tiles_from_an_explore)
  * [Share the Explore with a URL](https://docs.cloud.google.com/looker/docs/sharing-urls)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
