---
url: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-int-array-function-reference/
title: TO_INT_ARRAY function \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:31.447178+00:00
---

# TO_INT_ARRAY function  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-int-array-function-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TO_INT_ARRAY function

## `TO_INT_ARRAY` function

Function Name | Description | Usage | Input parameter | Return value  
---|---|---|---|---  
`TO_INT_ARRAY` | Converts a JSON array to an integer array. | `TO_INT_ARRAY()` | N/A | An integer array.  
  
## Supported data type

The `TO_INT_ARRAY` function supports the following data type: 

  * JSON



## Example: Convert JSON array to an integer array

**Sample data** : `$var1$ = [3, 8, 9]`

**Usage** : `$var1$.TO_INT_ARRAY()`

Convert var1 to an integer array. 

**Output** : `{3, 8, 9}`

## Recommendation

  * Learn how to add and configure a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
