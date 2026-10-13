---
url: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-property-function-reference/
title: GET_PROPERTY function \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:31.212617+00:00
---

# GET_PROPERTY function  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-property-function-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GET_PROPERTY function

## `GET_PROPERTY` function

Function Name | Description | Usage | Input parameter | Return value  
---|---|---|---|---  
`GET_PROPERTY` | Returns the value of the specified property in a JSON object. | `GET_PROPERTY(value)` | Property name. | Value of the property.  
  
## Supported data type

The `GET_PROPERTY` function supports the following data type: 

  * JSON



## Example: Get the value of a property in a JSON object

**Sample data** : `$var1$ = {"productId": 23,"productName": "radio"}`

**Usage** : `$var1$.GET_PROPERTY("productId")`

Get the value of the property `productId`. 

**Output** : `23`

## Recommendation

  * Learn how to add and configure a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
