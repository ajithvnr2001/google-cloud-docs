---
url: https://docs.cloud.google.com/data-studio/regexpextract/
title: REGEXP_EXTRACT \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:42.526997+00:00
---

# REGEXP_EXTRACT  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/regexpextract/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  REGEXP_EXTRACT Stay organized with collections  Save and categorize content based on your preferences. 

Returns the first matching substring in the target value which matches the regular expression pattern.

## Sample usage

`REGEXP_EXTRACT(Campaign, 'TYPE:(.*)')`

## Syntax

`REGEXP_EXTRACT(X, regular_expression)`

### Parameters

  * `X` \- a field or expression that includes a field.

  * `regular_expression` \- a regular expression that extracts a portion of `X`. `regular_expression` must contain a valid extraction pattern.




### Returns

The `REGEXP_EXTRACT` function returns **Text** data type values.

## Example

Example formula  |  Input  |  Output   
---|---|---  
` REGEXP_EXTRACT( URL, '\^https://\[\^/\]+/(\[\^/\]+)/' ) ` |  https://support.google.com/looker-studio/answer/7050487  |  looker-studio   
` REGEXP_EXTRACT( URL, '\^https://\[\^/\]+/(\[\^/\]+)/' ) ` |  https://cloud.google.com/bigquery/docs/reference/standard-sql/functions-and-operators  |  bigquery   
  
## Notes

Data Studio uses the RE2 expression syntax. For more details, see [Regular Expressions in Data Studio](https://docs.cloud.google.com/data-studio/regular-expressions).

Note that patterns containing escape characters such as `\` may require additional escaping in Data Studio, which can be avoided with the use of [raw string literals](https://docs.cloud.google.com/data-studio/literals).

## Related resources

  * [Regular expressions in Data Studio](https://docs.cloud.google.com/data-studio/regular-expressions)
  * [Calculated fields](https://docs.cloud.google.com/data-studio/about-calculated-fields)
  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
