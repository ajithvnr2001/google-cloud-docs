---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-conditional-formatting-with-value_format/
title: Conditional formatting using value_format \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:34.830776+00:00
---

# Conditional formatting using value_format  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-conditional-formatting-with-value_format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Conditional formatting using value_format Stay organized with collections  Save and categorize content based on your preferences. 

It's common for users to want to interact with short numbers. For example, they prefer $2.5M to a long string like $2,523,093.25. You can build short-number displays by creating multiple defined LookML measures, such as one to display as-is, one divided by 1,000, or one with limited decimal places, and so on. 

![](https://docs.cloud.google.com/static/looker/docs/images/hc-conditional-formatting-value_format-visualization-2210.png)

![](https://docs.cloud.google.com/static/looker/docs/images/hc-conditional-formatting-value_format-data-2210.png)

LookML can achieve these displays automatically with some more advanced [`value_format`](https://docs.cloud.google.com/looker/docs/reference/param-field-value-format) syntax. 

## Syntax

Use this pattern to set value formats with conditions: 
    
    
    [if_condition]format; [if_condition]format; else_format
    

Note that Looker only supports up to two `if_condition` conditions. If you add more than two conditions, any conditions after the first two will be ignored. 

Since the value of the `value_format` parameter is already enclosed in double quotes in LookML, any nested double quotes will need to be escaped using the backslash `\` character. 

##  Example with large numbers 

To make numbers such as 12.23M or 2.33K, you can use the following code: 
    
    
      [>=1000000]0.00,,\"M\";[>=1000]0.00,\"K\";
    

Or with no decimal places: 
    
    
      [>=1000000]0,,\"M\";[>=1000]0,\"K\";0
    

Here is the measure in LookML using this format, with dollar signs added: 
    
    
      measure: global_amount {
        type: sum
        sql: ${TABLE}.total
        value_format: "[>=1000000]$0.00,,\"M\";[>=1000]$0.00,\"K\";$0.00"
        drill_fields: invoices*
      }
    

##  Example with large negative numbers 

You can use similar syntax with negative numbers. To make numbers such as -12.23M or -2.33K, you can use the following code: 
    
    
      [<=-1000000]0.00,,\"M\";[<=-1000]0.00,\"K\";
    

Or with no decimal places: 
    
    
      [<=-1000000]0,,\"M\";[<=-1000]0,\"K\";0
    

Here is the measure in LookML using this format, with dollar signs added: 
    
    
      measure: global_amount_negative {
        type: sum
        sql: ${TABLE}.total
        value_format: "[<=-1000000]$0.00,,\"M\";[<=-1000]$0.00,\"K\";$0.00"
        drill_fields: invoices*
      }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
