---
url: https://docs.cloud.google.com/looker/docs/power/
title: power \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:24.443461+00:00
---

# power  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/power/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  power Stay organized with collections  Save and categorize content based on your preferences. 

The `power` function can be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to raise a number to the power of a given exponent.

## Syntax

**`power(base, exponent)`**

The `power` function evaluates a `base` by raising it to the power of a given `exponent`.

## Examples

The `power` function can be used to raise a number to the power of another number. For example, 23 would be written as:
    
    
    power(2, 3)
    

Typically, the `power` function is used with a field reference or an expression. For example:
    
    
    power(${order_item.standard_deviation_profit}, 2)
    

## Things to know

The `power` function can also be used to take the nth root of a number by using 1/n as the `exponent`. For example, the cube root (the 3rd root) of 7 would be:
    
    
    power(7, 1/3)
    

For a square root (the 2nd root) just use the `sqrt` function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
