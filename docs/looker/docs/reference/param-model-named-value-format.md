---
url: https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format/
title: named_value_format \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:18.902332+00:00
---

# named_value_format  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/reference/param-model-named-value-format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ LookML Reference ](https://docs.cloud.google.com/looker/docs/reference/lookml-quick-reference)



Send feedback 

#  named_value_format Stay organized with collections  Save and categorize content based on your preferences. 

## Usage
    
    
    named_value_format: desired_name {
      value_format: "excel formatting string"
      strict_value_format: yes | no
    }
    

Hierarchy [Model File](https://docs.cloud.google.com/looker/docs/reference/param-model) `named_value_format` |  Default Value None Accepts A name for your custom format plus an Excel-style formatting string that defines the format and a Boolean value for the optional `strict_value_format` subparameter   
---|---  
  
## Definition

The `named_value_format` parameter lets you create and save a custom format that can be applied to multiple dimensions and measures.

Custom formats in Looker are created and used in several steps:

  1. First, you use `named_value_format` in your model file to declare a name for your new custom format. This name must be a string without any spaces.
  2. Next, you use the [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) subparameter under `named_value_format` to define the formatting you want by providing an Excel-style format string.
  3. Finally, apply this custom format to dimensions and measures by referencing it in the [`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name) parameter at the field level.



You can define more than one custom format in a model, as shown in the following examples.

### Common `value_format` formatting strings

> The formatting used with the `value_format` parameter is the same as formatting used in the **Value Format** field in [visualizations](https://docs.cloud.google.com/looker/docs/creating-visualizations), except that the `value_format` parameter requires the formatting string to be enclosed in double quotes. See the [Column chart options](https://docs.cloud.google.com/looker/docs/column-options) documentation page for information about value formats in visualizations.

You can read Excel's complete guide about how to specify these formats [in their documentation](https://support.office.com/en-us/article/review-guidelines-for-customizing-a-number-format-c0a1d1fa-d3f4-4018-96b7-9c9354dd99f5). However, at this time, date formatting, color formatting, and hexadecimal conversion are not supported in Looker.

The following shows some of the most common formatting options. Some special characters, such as international currency symbols, must be enclosed in double quotes.
    
    
    value_format: "0"             # Integer (123)
    value_format: "*00#"          # Integer zero-padded to 3 places (001)
    value_format: "0 \" String\"" # Integer followed by a string (123 String)
                                  #   Please note "String" can be replaced with any other word
    
    value_format: "0.##"          # Number up to 2 decimals (1. or 1.2 or 1.23)
    value_format: "0.00"          # Number with exactly 2 decimals (1.23)
    value_format: "*00#.00"       # Number zero-padded to 3 places and exactly 2 decimals (001.23)
    value_format: "#,##0"         # Number with comma between thousands (1,234)
    value_format: "#,##0.00"      # Number with comma between thousands and 2 decimals (1,234.00)
    value_format: "0.000,,\" M\"" # Number in millions with 3 decimals (1.234 M)
                                  #   Please note division by 1 million happens automatically
    value_format: "0.000,\" K\""  # Number in thousands with 3 decimals (1.234 K)
                                  #   Please note division by 1 thousand happens automatically
    
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
    

### `strict_value_format` overrides the `number_format` user attribute

Typically, the number formatting set in the [`number_format`](https://docs.cloud.google.com/looker/docs/supported-user-interface-languages#localizing_number_formatting) user attribute is applied on top of the format created with `named_value_format`. However, if you set the optional `strict_number_format` subparameter to `yes`, the formatting from `number_format` will not be applied, and fields will retain the formatting from `named_value_format`. For an example, and to learn more, visit the [Localizing number formatting](https://docs.cloud.google.com/looker/docs/localizing-number-formatting#overriding_the_number_format_setting_with_strict_value_format) documentation page.

### Default formatting options

If you prefer to apply one of Looker's built-in value formats, you can choose from the formats listed on the [Default format names](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name#default_format_names) section of the `value_format_name` parameter's documentation page. See that page for instructions on using [`value_format_name`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format-name) to apply built-in formats.

## Examples

Create a custom format called `euro_in_thousands` that looks like **€1.23K** :
    
    
    named_value_format: euro_in_thousands {
      value_format: "\"€\"0.000,\" K\""
    }
    

Prevent the `number_formatting` user attribute from affecting the `euro_in_thousands` format:
    
    
    named_value_format: euro_in_thousands {
      value_format: "\"€\"0.000,\" K\""
      strict_value_format: yes
    }
    

Also see the [Localizing number formatting](https://docs.cloud.google.com/looker/docs/localizing-number-formatting#overriding_the_number_format_setting_with_strict_value_format) documentation page for another example.

Create a custom format called `usd_in_millions` that looks like **$1.23M** and a format called `phone_number` that looks like **(123) 456-7890** :
    
    
    named_value_format: usd_in_millions {
      value_format: "$0.000,,\" M\""
    }
    named_value_format: phone_number {
      value_format: "(###) ###-####"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
