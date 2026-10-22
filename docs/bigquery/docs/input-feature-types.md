---
url: https://docs.cloud.google.com/bigquery/docs/input-feature-types/
title: Supported input feature types \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:41.471590+00:00
---

# Supported input feature types  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/input-feature-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported input feature types

BigQuery ML supports different input feature types for different model types. Supported input feature types are listed in the following table:

Model Category | [Model Types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create#model_option_list) | [Numeric types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types) ([INT64](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#integer_types), [NUMERIC](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#decimal_types), [BIGNUMERIC](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#decimal_types), [FLOAT64](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#floating_point_types)) | Categorical types ([BOOL](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#boolean_type), [STRING](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#string_type), [BYTES](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#bytes_type), [DATE](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#date_type), [DATETIME](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#datetime_type)) | [TIMESTAMP](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#timestamp_type) | [STRUCT](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type) | [GEOGRAPHY](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#geography_type) | [ARRAY](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type)<[Numeric types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types)> | [ARRAY](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type)<Categorical types> | [ARRAY](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#array_type)<[STRUCT](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#struct_type)<[INT64](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#integer_types), [Numeric types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types)>>  
---|---|---|---|---|---|---|---|---|---  
Supervised Learning | Linear & Logistic Regression | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔  
Deep Neural Networks | ✔ | ✔ |  | ✔ |  | ✔ | ✔ | ✔  
Wide-and-Deep | ✔ | ✔ |  | ✔ |  | ✔ | ✔ | ✔  
Boosted trees | ✔ | ✔ |  | ✔ |  | ✔ | ✔ | ✔  
AutoML Tables | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ |   
Unsupervised Learning | K-means | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |   
PCA | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ |   
Autoencoder | ✔ | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔  
Time Series Models | ARIMA_PLUS_XREG | ✔ | ✔ | ✔ | ✔ |  |  | ✔ | ✔  
**Note:** [Matrix Factorization](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-matrix-factorization#inputs) and [ARIMA_PLUS](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series#time_series_data_col) models have special input feature types. The input types listed for [ARIMA_PLUS_XREG](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series#time_series_data_col) are only for external regressors.

## Dense vector input

BigQuery ML supports `ARRAY<numeric>` as dense vector input during model training. The embedding feature is a special type of dense vector. see the [`AI.GENERATE_EMBEDDING` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding) for more information.

## Sparse input

BigQuery ML supports `ARRAY<STRUCT>` as sparse input during model training. Each struct contains an `INT64` value that represents its zero-based index, and a [numeric type](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types#numeric_types) that represents the corresponding value.

Below is an example of a sparse tensor input for the integer array `[0,1,0,0,0,0,1]`:
    
    
    ARRAY<STRUCT<k INT64, v INT64>>[(1, 1), (6, 1)] AS f1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
