---
url: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-base-64-function-reference/
title: TO_BASE_64 function \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:37.791780+00:00
---

# TO_BASE_64 function  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-base-64-function-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TO_BASE_64 function

## `TO_BASE_64` function

Function Name | Description | Usage | Input parameter | Return value  
---|---|---|---|---  
`TO_BASE_64` | Encodes a string to base64 format using the UTF-8 charset. | `TO_BASE_64()` | N/A | A base64 encoded string.  
  
## Supported data type

The `TO_BASE_64` function supports the following data type: 

  * String



## Example: Encode a string to base64 format

**Sample data** : `$var1$ = "Hello World!"`

**Usage** : `$var1$.TO_BASE_64()`

Encode var1 in base64 format. 

**Output** : `SGVsbG8gV29ybGQh`

## Recommendation

  * Learn how to add and configure a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
