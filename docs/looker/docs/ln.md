---
url: https://docs.cloud.google.com/looker/docs/ln/
title: ln \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:49.252392+00:00
---

# ln  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/ln/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  ln Stay organized with collections  Save and categorize content based on your preferences. 

The `ln` function can be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to get the natural logarithm of a value.

## Syntax

**`ln(value)`**

The `ln` function takes the logarithm of a `value` to the base of the mathematical constant _e_.

## Examples

The `ln` function can be used to model exponential growth linearly by taking `ln` of the dependent variable. For example:
    
    
    ln(order_items.growth_rate)
    

## Things to know

`ln` can be used to give you the time needed to reach a certain level of growth. For instance, modeling growth exponentially as:

_growth = e time_

_time_ can be determined using `ln` as follows:
    
    
    ln(growth)
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
