---
url: https://docs.cloud.google.com/data-studio/ifnull/
title: IFNULL \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:08.395888+00:00
---

# IFNULL  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/ifnull/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  IFNULL Stay organized with collections  Save and categorize content based on your preferences. 

Use `IFNULL` to replace NULL values in your data with a more suitable or meaningful value. This can be helpful when you want to avoid displaying NULLs in your charts or when you need a specific value for further calculations.

## Sample usage

`IFNULL(Discount, 0)`

## Syntax

`IFNULL( input_expression, null_result )`

### Parameters

  * **`input_expression`** \-- The expression to evaluate. You can use any valid expression as the `input_expression`.



  * **`null_result`** \-- The value to return if `input_expression` is null. If `input_expression` is not null, `IFNULL` returns the `input_expression`. You can use any valid expression as the `null_result`.



## Example

Calculate the average discount given to your customers, including orders that received no discount. However, your application sometimes represents "no discount" as null rather than 0.

The formula `AVG(Discount)` won't include null discounts. You'll need to convert those nulls to zero. To do this, create a new field called, for example, **Discount No Nulls** :

`IFNULL(Discount, 0)`

This formula can be read, "If the **Discount** field is null, return 0, otherwise return **Discount**."

You can then calculate the average discount including orders with no discount:

`AVG(Discount No Nulls)`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
