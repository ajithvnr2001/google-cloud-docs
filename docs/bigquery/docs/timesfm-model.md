---
url: https://docs.cloud.google.com/bigquery/docs/timesfm-model/
title: The TimesFM model \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:22.941546+00:00
---

# The TimesFM model  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/timesfm-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The TimesFM model

This document describes BigQuery ML's built-in TimesFM time series forecasting model.

The built-in TimesFM model is an implementation of Google Research's open source [TimesFM model](https://github.com/google-research/timesfm). The Google Research TimesFM model is a foundation model for time-series forecasting that has been pre-trained on billions of time-points from many real-world datasets, so you can apply it to new forecasting datasets across many domains. The TimesFM model is available in all BigQuery supported regions.

Using BigQuery ML's built-in TimesFM model with the [`AI.FORECAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast) lets you perform forecasting without having to create and train your own model, so you can avoid the need for model management. The forecast results from the TimesFM model are comparable to conventional statistical methods such as ARIMA. If you want more model tuning options than the TimesFM model offers, you can create an [`ARIMA_PLUS`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-time-series) or [`ARIMA_PLUS_XREG`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-multivariate-time-series) model and use it with the [`ML.FORECAST` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-forecast) instead.

To learn how to use a TimesFM model with the `AI.FORECAST` function, see the following tutorials:

  * [Forecast single or multiple time series with a TimesFM univariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-time-series-forecasting-tutorial)
  * [Forecast a single time series with a TimesFM multivariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-single-time-series-forecasting-tutorial) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * [Forecast multiple time series with a TimesFM multivariate model](https://docs.cloud.google.com/bigquery/docs/timesfm-multivariate-multi-time-series-forecasting-tutorial) ([Preview](https://cloud.google.com/products#product-launch-stages))



To use the TimesFM model to detect anomalies in time series data, use the [`AI.DETECT_ANOMALIES` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-detect-anomalies).

To evaluate forecasted values from the TimesFM model against the actual values, use the [`AI.EVALUATE` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-evaluate).

To learn more about the Google Research TimesFM model, use the following resources:

  * [Google Research blog](https://research.google/blog/a-decoder-only-foundation-model-for-time-series-forecasting/)
  * [GitHub repository](https://github.com/google-research/timesfm)
  * [Hugging Face page](https://huggingface.co/collections/google/timesfm-release-66e4be5fdb56e960c1e482a6)



When you use TimesFM through BigQuery, your usage is governed by the [Google Cloud Terms of Service](https://cloud.google.com/terms) and allows for commercial uses. The non-commercial license associated with the publicly downloadable `TimesFM 3.0` weights on GitHub and Hugging Face applies only to self-hosted downloads and does not restrict usage within BigQuery. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
