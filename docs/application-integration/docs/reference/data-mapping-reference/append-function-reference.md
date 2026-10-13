---
url: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/append-function-reference/
title: APPEND function \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:28.018486+00:00
---

# APPEND function  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/append-function-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APPEND function

## `APPEND` function

Function Name | Description | Usage | Input parameter | Return value  
---|---|---|---|---  
`APPEND` | Appends the specified value to an array. | `APPEND(value)` | Value to append. The data type of the value to append should match the data type of the array. For example, for a `Boolean` array you can append only `True` or `False`.  | Array with the appended value.  
  
## Supported data type

The `APPEND` function supports the following data types: 

  * Boolean array
  * Double array
  * Integer array
  * String array



## Example 1: Append a value to an integer array

**Sample data** : `$var1$ = {3,6,8,1}`

**Usage** : `$var1$.APPEND(7)`

Append the value 7 to var1. 

**Output** : `{3,6,8,1,7}`

## Example 2: Append a value to a Boolean array. 

**Sample data** : `$var1$ = {True,False,True}`

**Usage** : `$var1$.APPEND(True) `

Append the value True to var1. 

**Output** : `{True,False,True,True}`

## Example 3: Append a value to a string array

**Sample data** : `$var1$ = {"Hello","Apigee"}`

**Usage** : `$var1$.APPEND("Integrations") `

Append the word `Integrations` to var1. 

**Output** : `{"Hello","Apigee","Integrations"}`

## Recommendation

  * Learn how to add and configure a [Data Mapping task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
