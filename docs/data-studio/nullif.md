---
url: https://docs.cloud.google.com/data-studio/nullif/
title: NULLIF \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:34.955518+00:00
---

# NULLIF  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/nullif/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  NULLIF Stay organized with collections  Save and categorize content based on your preferences. 

Use ```NULLIF``` to selectively replace a specific value in your data with NULL. This can be helpful in situations where a particular value represents missing or invalid data, and you want to explicitly mark it as NULL for further analysis or processing.

## Sample usage

Replace -1 in the **Discount** field with NULL.

```NULLIF(Discount, -1)```

## Syntax

```NULLIF( input_expression, expression_to_match )```

### Parameters

#### input_expression

The expression to evaluate. You can use any valid expression as the `input_expression`.

#### expression_to_match

```NULLIF``` compares `expression_to_match` to `input_expression`. If the two are equal, ```NULLIF``` returns null, otherwise it returns the `input_expression`. You can use any valid expression as the `expression_to_match`.

## Example

Suppose you want to calculate the average discount given to your customers. Your application represents "no discount" as -1. The formula `AVG(Discount)` will count -1 and return an incorrect result. To avoid this, you can convert those -1s to NULLS. To do this, create a new field called, for example, **Discount With Nulls** :

```NULLIF(`**`Discount`**`, -1)```

This formula can be read, "If the **Discount** field is -1, return null, otherwise return **Discount**."

You can then calculate the average discount ignoring orders with no discount:

```AVG(`**`Discount With Nulls`**`)```

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
