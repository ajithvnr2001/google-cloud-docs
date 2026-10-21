---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/hierarchical/
title: Reduce forecasting bias with hierarchical aggregation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:38:24.462293+00:00
---

# Reduce forecasting bias with hierarchical aggregation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/hierarchical/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Reduce forecasting bias with hierarchical aggregation Stay organized with collections  Save and categorize content based on your preferences. 

To see an example of how to create hierarchical forecasting models using AutoML and perform batch prediction, run the "AutoML training hierarchical forecasting for batch prediction" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/automl/sdk_automl_forecasting_hierarchical_batch.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fautoml%2Fsdk_automl_forecasting_hierarchical_batch.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fvertex-ai-samples%2Fmain%2Fnotebooks%2Fofficial%2Fautoml%2Fsdk_automl_forecasting_hierarchical_batch.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/vertex-ai-samples/blob/main/notebooks/official/automl/sdk_automl_forecasting_hierarchical_batch.ipynb)

This page explains hierarchical forecasting, its objectives, and shows training strategies you can employ to reduce bias in your forecasting models.

For detailed instructions on how to configure hierarchical forecasting when training your forecasting model using the API, see [Train a forecast model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/train-model#api).

## What is hierarchical forecasting

Time series are often structured in a nested hierarchy. For example, a retailer's entire inventory of products can be divided into categories of products. The categories can be further divided into individual products. When forecasting future sales, the forecasts for a category's products must add up to the forecast for the category itself, and so forth up the hierarchy.

![A hierarchy of products and categories.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/images/hierarchy.svg)

Similarly, a single time series' time dimension can also exhibit a hierarchy. For example, forecasted sales for an individual product at the day level must add up to the product's forecasted weekly sales. The following figure shows this group and temporal hierarchy as a matrix:

![A time series matrix.](https://docs.cloud.google.com/static/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/images/matrix.svg)

Hierarchical forecasting has three objectives:

  * **Reduce overall bias** to improve metrics over all time series (total sales).
  * **Reduce temporal bias** to improve metrics over the horizon (season sales).
  * **Reduce group level bias** to improve metrics over a group of time series (item sales).



In Gemini Enterprise Agent Platform, hierarchical forecasting takes into account the hierarchical structure of time series by incorporating additional loss terms for aggregated inferences.
    
    
    Hierarchical loss = (1 x loss) +
                        (temporal total weight x temporal total loss) +
                        (group total weight x group total loss) +
                        (group temporal total weight x group temporal total loss)
    

For example, if the hierarchical group is "category", the inferences at the "category" level are the sum of inferences for all "products" in the category. If the model's objective is mean absolute error (MAE), the loss includes the MAE for inferences at both the "product" and "category" levels. This helps improve the consistency of forecasts at different levels of the hierarchy, and in some cases, might even improve metrics at the lowest level.

## Configure hierarchical aggregation for model training

Configure hierarchical aggregation when training your forecast models by configuring [`AutoMLForecastingTrainingJob`](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLForecastingTrainingJob) in the [Agent Platform SDK](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/start/client-libraries) or by [configuring `hierarchyConfig` in the Agent Platform API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/train-model#api).

Available parameters for `AutoMLForecastingTrainingJob` and `hierarchyConfig` include:

  * `group_columns`
  * `group_total_weight`
  * `temporal_total_weight`
  * `group_temporal_total_weight`



The parameters allow different combinations of group and time aggregated losses. They also allow you to assign weights to increase the priority of minimizing the aggregated loss relative to the individual loss. For example, if the weight is `2.0`, it is weighted twice as much as the individual loss.

### `group_columns`

Column names in your training input table identify the grouping for the hierarchy level. The column(s) must be `time_series_attribute_columns`. If you don't set the group column, all time series are treated as part of the same group and aggregate over all time series.

### `group_total_weight`

Weight of the group aggregated loss relative to the individual loss. Disabled if set to `0.0` or not set.

### `temporal_total_weight`

Weight of the time aggregated loss relative to the individual loss. Disabled if set to `0.0` or not set.

### `group_temporal_total_weight`

Weight of the total (group x time) aggregated loss relative to the individual loss. Disabled if set to `0.0` or not set. If you don't set the group column, all time series are treated as part of the same group and aggregate over all time series.

## Strategies to reduce bias

Start with one type of aggregation (group or time) with a weight of `10.0`, and then halve or double the value based on the results.

### Reduce overall bias

In fine-grained forecasts for distributing stock across stores where weighted absolute percentage error (WAPE) at the product x store x date level are used as a forecasting metric, forecasts often underpredict at the aggregate levels. To compensate for this overall bias, try the following:

  * Set `group_total_weight` to `10.0`.
  * Leave `group_columns` unset.
  * Leave other weights unset.



This aggregates over all time series and reduces overall bias.

### Reduce temporal bias

In long term planning, forecasts might be made at a product x region x week level, but the relevant metrics might be measured with respect to seasonal totals. To compensate for this temporal bias, try the following:

  * Set `temporal_total_weight` to `10.0`.
  * Leave `group_columns` unset.
  * Leave other weights unset.



This aggregates over all dates in a time series' horizon, and reduces temporal bias.

### Reduce group level bias

For forecasts that are multi-purpose in the replenishment process, fine-grained forecasts at the product x store x date or week level might aggregate up to product x distribution center x date levels for distribution or product category x date levels for materials orders. To do this, perform the following:

  * Set `group_total_weight` to `10.0`.
  * Set `group_columns`, for example, ["region"] or ["region", "category"]. Setting multiple group columns uses their combined value to define the group. For best results, use group columns with 100 or fewer distinct combined values.
  * Leave other weights unset.



This aggregates over all time series in the same group for the same date, and reduces bias at the group level.

## Limits

  * Only one level of time series aggregation is supported. If you specify more than one grouping column, such as "product, store", the time series is in the same group only if they share the same values of both "product" and "store".
  * We recommend using 100 or fewer groups.



## What's next

  * [Evaluate your model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/tabular-data/forecasting/evaluate-model).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
