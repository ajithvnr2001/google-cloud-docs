---
url: https://docs.cloud.google.com/looker/docs/abs/
title: abs \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:23.962095+00:00
---

# abs  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/abs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  abs Stay organized with collections  Save and categorize content based on your preferences. 

The `abs` function can be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to get the absolute value of an expression.

## Syntax

**`abs(value)`**

The `abs` function returns the absolute value of the expression `value`. The "absolute value" of a number is its distance from zero as a positive number.

## Examples

The `abs` function can be used to return positive numbers from negative numbers. For instance, to return positive 4 from negative 4:
    
    
    abs(-4)
    

Typically, the `abs` function is used with a field reference or an expression. For example, you might want to determine how much the price of an item changed, but don't want to know if it went up or down:
    
    
    abs(${item.start_price} - ${item.end_price})
    

## Things to know

`abs` is useful for determining the difference between two values, regardless of which value is bigger. For instance, this returns 1:
    
    
    abs(2 - 1)
    

This also returns 1:
    
    
    abs(1 - 2)
    

As in the previous example, you could compare two fields this way:
    
    
    abs(${item.start_price} - ${item.end_price})
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
