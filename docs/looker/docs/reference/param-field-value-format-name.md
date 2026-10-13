---
url: https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name/
title: value_format_name \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:40.433552+00:00
---

# value_format_name  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  value_format_name Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    view: view_name {
      dimension: field_name {
        value_format_name: format_name
      }
    }
    

Hierarchy [View File](https://docs.cloud.google.com/looker/docs/reference/param-view) [`view`](https://docs.cloud.google.com/looker/docs/reference/param-view-view) [Field Type](https://docs.cloud.google.com/looker/docs/reference/param-field) `value_format_name` |  Possible Field Types Dimension, Measure Accepts One of the default value formats listed on this documentation page, or the name of a format that you created with the [`named_value_format`](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format) parameter   
---|---  
  
## Definition

The `value_format_name` parameter lets you format data values using formats built into Looker or your own custom, reusable formats. If you want to apply an Excel-style format directly to a unique field, use [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) instead.

The `value_format_name` parameter can be used on both dimensions and measures. For example:
    
    
    measure: total_order_amount {
      type: sum
      sql: ${order_amount} ;;
      value_format_name: usd
    }
    

**Note:** `value_format_name` only affects how field values are displayed in Looker content. `value_format_name` does not change or affect the value in the database.

### Default format names

Looker has the default formats that are shown in the following tables. When using one of the default formats, Looker rounds up or down to remove digits, rather than truncating values. When a default format name is used on a measure, rounding occurs after the measure has been aggregated.

You can also create your own named formats by using the [`named_value_format`](https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format) parameter.

#### Numeric formats

The default formats for numeric field types are shown in the following table. They start with the underlying value "1234.56789":

Name | Example  
---|---  
`decimal_0` | 1,235  
`decimal_1` | 1,234.6  
`decimal_2` | 1,234.57  
`decimal_3` | 1,234.568  
`decimal_4` | 1,234.5679  
`usd_0` | $1,235  
`usd` | $1,234.57  
`gbp_0` | £1,235  
`gbp` | £1,234.57  
`eur_0` | €1,235  
`eur` | €1,234.57  
`id` | 1235  
  
> For numeric field types, `id` should only be used on numbers that have 16 digits or fewer. Beyond 16 digits, `id` may round results. For numbers with more than 16 digits, cast them as a string and use `id` on the string field type.

#### Percentage formats

For percentage formats, Looker takes the underlying decimal value and multiplies it by 100 to get a percentage. The following examples start with the underlying value "0.123456":

Name | Example  
---|---  
`percent_0` | 12%  
`percent_1` | 12.3%  
`percent_2` | 12.35%  
`percent_3` | 12.346%  
`percent_4` | 12.3456%  
  
## Things to know

To apply `value_format_name` to a field, the [`type`](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types) parameter must be defined for that field.

## Common challenges

### Using `value_format_name` with the `number_format` user attribute

If you use `value_format_name` to format fields in your models, the number format selected in the `number_format` user attribute is applied on top of the format given with `value_format_name`. For an example, and to learn more, see the [Localizing number formatting](https://docs.cloud.google.com/looker/docs/localizing-number-formatting) documentation page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
