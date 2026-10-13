---
url: https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-min-max-scaler/
title: The ML.MIN_MAX_SCALER function \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:13.933517+00:00
---

# The ML.MIN_MAX_SCALER function  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-min-max-scaler/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The ML.MIN_MAX_SCALER function

This document describes the `ML.MIN_MAX_SCALER` function, which lets you scale a numerical_expression to the range `[0, 1]`. Negative values are set to `0`, and values above `1` are set to `1`.

When used in the [`TRANSFORM` clause](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#transform), the range of `[0,1]` is automatically used in prediction, and predicted values outside that range are similarly capped.

You can use this function with models that support [manual feature preprocessing](https://docs.cloud.google.com/bigquery/docs/manual-preprocessing). For more information, see the following documents:

  * [End-to-end user journeys for ML models](https://docs.cloud.google.com/bigquery/docs/e2e-journey)
  * [Contribution analysis user journey](https://docs.cloud.google.com/bigquery/docs/contribution-analysis#contribution_analysis_user_journey)



## Syntax
    
    
    ML.MIN_MAX_SCALER(numerical_expression) OVER()
    

### Arguments

`ML.MIN_MAX_SCALER` takes the following argument:

  * `numerical_expression`: the [numerical](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types) expression to scale.



## Output

`ML.MIN_MAX_SCALER` returns a `FLOAT64` value that represents the scaled numerical expression.

## Example

The following example scales a set of numerical expressions to values between `0` and `1`:
    
    
    SELECT
      f, ML.MIN_MAX_SCALER(f) OVER() AS output
    FROM
      UNNEST([1,2,3,4,5]) AS f;

The output looks similar to the following:
    
    
    +---+--------+
    | f | output |
    +---+--------+
    | 4 |   0.75 |
    | 2 |   0.25 |
    | 1 |    0.0 |
    | 3 |    0.5 |
    | 5 |    1.0 |
    +---+--------+
    

## What's next

  * For information about feature preprocessing, see [Feature preprocessing overview](https://docs.cloud.google.com/bigquery/docs/preprocess-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
