---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-value-format/
title: value_format \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:40.484640+00:00
---

# value_format  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-value-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  value_format Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        value_format:"$#.00;($#.00)"
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `value_format` |  Possible Field Types Dimension, Measure Accepts A string containing Excel-style formatting  
---|---  
  
## Definition

The `value_format` parameter lets you format data values in Looker using Excel-style formats. You can use `value_format` in the following ways:

  * On its own, at the field level, to apply Excel-style formatting directly to a specific dimension or measure
  * As a subparameter of the [`named_value_format`](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format) parameter, at the model level, to create a reusable custom format that can be applied to multiple fields

**Note:** `value_format` only affects how field values are displayed in Looker content. `value_format` does not change or affect the value in the database.

### Applying `value_format` directly to dimensions and measures

The `value_format` parameter can be used on both dimensions and measures. To apply Excel-style formatting to dimensions via `value_format`, the dimension type must be `number`. To apply Excel-style formatting to measures via `value_format`, make sure the measure is numeric and not of `type: string`. For example:
    
    
    dimension: order_amount {
      type: number
      sql: ${TABLE}.order_amount ;;
      value_format: "$#.00;($#.00)"
    }
    measure: total_order_amount {
      type: sum
      sql: ${order_amount} ;;
      value_format: "$#.00;($#.00)"
    }
    

### Using `value_format` to define a reusable custom format

For information about using `value_format` with `named_value_format` to define reusable formats, see the [`named_value_format`](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format) parameter's documentation page.

### Default formatting options

If you prefer to apply one of Looker's built-in value formats, you can choose from the formats listed on the [Default Format Names](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name#default_format_names) section of the `value_format_name` parameter's documentation page. See that page for instructions on using [`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name) to apply built-in formats.

## Common formatting strings

`value_format` accepts an Excel-style formatting string.

> The formatting used with the `value_format` parameter is the same as formatting used in the **Value Format** field in [visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations), except that the `value_format` parameter requires the formatting string to be enclosed in double quotes. See the [Column chart options](https://docs.cloud.google.com/looker/docs/column-options) documentation page for information about value formats in visualizations.

You can read Excel's complete guide about how to specify these formats [in their documentation](https://support.office.com/en-us/article/review-guidelines-for-customizing-a-number-format-c0a1d1fa-d3f4-4018-96b7-9c9354dd99f5). However, at this time, date formatting, color formatting, and hexadecimal conversion are not supported in Looker.

Some of the most common formatting options are shown here. Note that some special characters, such as international currency symbols, must be enclosed in double quotes.
    
    
    value_format: "0"             # Integer (123)
    value_format: "*00#"          # Integer zero-padded to 3 places (001)
    value_format: "0 \" String\"" # Integer followed by a string (123 String)
                                  #   Note \"String\" can be replaced with any other word
    
    value_format: "0.##"          # Number up to 2 decimals (1. or 1.2 or 1.23)
    value_format: "0.00"          # Number with exactly 2 decimals (1.23)
    value_format: "*00#.00"       # Number zero-padded to 3 places and exactly 2 decimals (001.23)
    value_format: "#,##0"         # Number with comma between thousands (1,234)
    value_format: "#,##0.00"      # Number with comma between thousands and 2 decimals (1,234.00)
    value_format: "0.000,,\" M\"" # Number in millions with 3 decimals (1.234 M)
                                  #   Note division by 1 million happens automatically
    value_format: "0.000,\" K\""  # Number in thousands with 3 decimals (1.234 K)
                                  #   Note division by 1 thousand happens automatically
    
    value_format: "$0"            # Dollars with 0 decimals ($123)
    value_format: "$0.00"         # Dollars with 2 decimals ($123.00)
    value_format: "\"€\"0"        # Euros with 0 decimals (€123)
    value_format: "$#,##0.00"     # Dollars with comma btwn thousands and 2 decimals ($1,234.00)
    value_format: "$#.00;($#.00)" # Dollars with 2 decimals, positive values displayed
                                  #   normally, negative values wrapped in parenthesis
    
    value_format: "0\%"           # Display as percent with 0 decimals (1 becomes 1%)
    value_format: "0.00\%"        # Display as percent with 2 decimals (1 becomes 1.00%)
    value_format: "0%"            # Convert to percent with 0 decimals (.01 becomes 1%)
    value_format: "0.00%"         # Convert to percent with 2 decimals (.01 becomes 1.00%)
    

For an example of more advanced conditional formatting with the `value_format` parameter, see the [Conditional formatting using `value_format`](https://docs.cloud.google.com/looker/docs/best-practices/how-to-conditional-formatting-with-value_format) Best Practices page.

## Common challenges

### Losing decimals when dividing

One common SQL quirk that arises when using `value_format` is the way that SQL handles integer math. If you divide 5 by 2, most people expect the result to be 2.5. However, many SQL dialects will return the result as just 2, because when it divides two integers it also gives the result as an integer. To address this, you can multiply the numerator by a decimal number (like 1.0 or 100.0) to force SQL into returning a decimal result. For example:
    
    
    measure: active_users_percent {
      type: number
      sql: 100.000 * ${active_users} / ${users} ;;
      value_format: "0.000"
    }
    

### Using `value_format` with the `number_format` user attribute

If you use `value_format` to format fields in your models, the number format selected in the `number_format` user attribute is applied on top of the format applied with `value_format`. For an example, and to learn more, visit the [Localizing number formatting](https://docs.cloud.google.com/looker/docs/localizing-number-formatting) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
