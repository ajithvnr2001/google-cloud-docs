---
url: https://docs.cloud.google.com/data-studio/regexpcontains/
title: REGEXP_CONTAINS \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:58.372457+00:00
---

# REGEXP_CONTAINS  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regexpcontains/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  REGEXP_CONTAINS Stay organized with collections  Save and categorize content based on your preferences. 

## Sample usage

`REGEXP_CONTAINS(Page, 'home')`

## Syntax

`REGEXP_CONTAINS(X, regular_expression)`

### Parameters

  * _`X`_ \- a field or expression to evaluate.

  * _`regular_expression`_ \- a regular expression.




### Returns

The `REGEXP_CONTAINS` function returns **Boolean** data type values.

### Examples

Example formula  |  Input  |  Output   
---|---|---  
` REGEXP_CONTAINS(Field, 'A') ` |  ABC123  |  true   
` REGEXP_CONTAINS(Field, 'A.\*') ` |  ABC123  |  true   
` REGEXP_CONTAINS(Field, 'AC') ` |  ABC123  |  false   
  
### Notes

`REGEXP_CONTAINS` differs from the similar [`REGEXP_MATCH`](https://docs.cloud.google.com/data-studio/regexpmatch) function, which will only match the _entire_ value by default. Thus, `REGEXP_CONTAINS(field,"pattern")` is functionally equivalent to `REGEXP_MATCH(field,".*pattern.*")`.

Data Studio uses the RE2 expression syntax. For more details, see [Regular Expressions in Data Studio](https://docs.cloud.google.com/data-studio/regular-expressions).

Note that patterns containing escape characters such as `\` may require additional escaping in Data Studio, which can be avoided with the use of [raw string literals](https://docs.cloud.google.com/data-studio/literals).

## Related resources

  * [Regular expressions in Data Studio](https://docs.cloud.google.com/data-studio/regular-expressions)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
