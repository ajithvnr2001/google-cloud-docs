---
url: https://docs.cloud.google.com/looker/docs/matches-filter/
title: matches_filter \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:25.006148+00:00
---

# matches_filter  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/matches-filter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  matches_filter Stay organized with collections  Save and categorize content based on your preferences. 

The `matches_filter` function can be used in [custom filters](https://docs.cloud.google.com/looker/docs/filtering-and-limiting#custom-filters) and [custom fields](https://docs.cloud.google.com/looker/docs/custom-fields) to determine whether the value of a field matches a [filter expression](https://docs.cloud.google.com/looker/docs/filter-expressions).

### Syntax

**`matches_filter(field,`filter expression`)`**

The `matches_filter` function applies the filter expression to the field and returns `Yes` if the value in the field matches the filter expression or `No` if it does not.

### Examples

This example returns `Yes` in a custom field if the invoice date is less than 30 days old:
    
    
    matches_filter(${billing.invoice_date}, `30 days`)
    

Use the [`if`](https://docs.cloud.google.com/looker/docs/functions-and-operators#functions_for_any_looker_expression_4) function with `matches_filter` to return different values. The next example shows syntax of a custom field that returns "Late" if the invoice date is over 30 days old:
    
    
    if(matches_filter(${billing.invoice_date}, `30 days`), "Current", "Late")
    

### Things to know

The string that defines the filter expression must be enclosed in backtick (`) characters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
