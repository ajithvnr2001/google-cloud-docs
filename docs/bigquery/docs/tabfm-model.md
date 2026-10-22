---
url: https://docs.cloud.google.com/bigquery/docs/tabfm-model/
title: The TabFM model \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:54.028582+00:00
---

# The TabFM model  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/tabfm-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# The TabFM model

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** For support during the preview, contact [bqml-feedback@google.com](mailto:bqml-feedback@google.com).

This document describes BigQuery's built-in TabFM tabular regression and classification model.

The built-in TabFM model is an implementation of Google Research's open source [TabFM model](https://github.com/google-research/tabfm). The Google Research TabFM model is a foundation model for tabular data that enables zero-shot regression and classification on structured data through in-context learning. Because the TabFM model is pre-trained on hundreds of millions of synthetic datasets generated using structural causal models, it captures complex feature interactions and generalizes well to unseen real-world tables across many domains.

You can use the TabFM model with the [`AI.PREDICT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-predict) to perform regression and classification on structured data in a single forward pass without having to train a model, optimize hyperparameters, or engineer features. The prediction results are comparable to conventional supervised tree-based algorithms such as XGBoost and random forests. If you want more model tuning options than the TabFM model offers, you can train a supervised model such as a [boosted tree](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-boosted-tree) or [random forest](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-random-forest) model and use it with the [`ML.PREDICT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) instead.

To generate predictions with the TabFM model on tabular data, use the [`AI.PREDICT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-predict).

To evaluate predicted values from the TabFM model against the actual values, use the [`AI.EVALUATE` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-evaluate).

To learn more about the Google Research TabFM model, use the following resources:

  * [Google Research blog](https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/)
  * [Google Cloud blog](https://cloud.google.com/blog/products/data-analytics/tabfm-adds-predictive-ml-to-bigquery)
  * [GitHub repository](https://github.com/google-research/tabfm)
  * [Hugging Face page](https://huggingface.co/google/tabfm-1.0.0-pytorch)



When you use TabFM through BigQuery, your usage is governed by the [Google Cloud Terms of Service](https://cloud.google.com/terms) and allows for commercial uses. The non-commercial license associated with the publicly downloadable TabFM weights on GitHub and Hugging Face applies only to self-hosted downloads and does not restrict usage within BigQuery. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
