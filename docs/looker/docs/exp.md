---
url: https://docs.cloud.google.com/looker/docs/exp/
title: exp \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:24.056692+00:00
---

# exp  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/exp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  exp Stay organized with collections  Save and categorize content based on your preferences. 

The `exp` function can be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [table calculations](https://docs.cloud.google.com/looker/docs/table-calculations) to get _e_ raised to the power of a value.

## Syntax

**`exp(value)`**

The `exp` function evaluates a `value` by calculating _e_ raised to the power of that value.

## Examples

The `exp` function can be used to calculate compound interest. For example, the [compound interest](https://en.wikipedia.org/wiki/Compound_interest) formula, _pe rt_, can be written as follows:
    
    
    ${investment.principal) * exp(${investment.rate} * ${investment.term})
    

## Things to know

The number _e_ (2.7182818284590...) is an important mathematical constant, which you can read more about [in this Wikipedia article](https://en.wikipedia.org/wiki/E_\(mathematical_constant\)). It has many applications, including calculating compound interest, performing certain probability calculations, generating normal distributions, and so on.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
