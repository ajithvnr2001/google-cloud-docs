---
url: https://docs.cloud.google.com/bigquery/docs/dimensionality-reduction-overview/
title: Dimensionality reduction overview \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:09.881233+00:00
---

# Dimensionality reduction overview  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/dimensionality-reduction-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Dimensionality reduction overview

Dimensionality reduction is the common term for a set of mathematical techniques used to capture the shape and relationships of data in a high-dimensional space and translate this information into a low-dimensional space.

Reducing dimensionality is important when you are working with large datasets that can contain thousands of features. In such a large data space, the wider range of distances between data points can make model output harder to interpret. For example, it makes it difficult to understand which data points are more closely situated and therefore represent more similar data. Dimensionality reduction helps you reduce the number of features while retaining the most important characteristics of the dataset. Reducing the number of features also helps reduce the training time of any models that use the data as input.

BigQuery ML offers the following models for dimensionality reduction:

  * [Principal component analysis (PCA)](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-pca)
  * [Autoencoder](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-autoencoder)



You can use PCA and autoencoder models with the [`ML.PREDICT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) or [`AI.GENERATE_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate-embedding) functions to embed data into a lower-dimensional space, and with the [`ML.DETECT_ANOMALIES` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies) to perform [anomaly detection](https://docs.cloud.google.com/bigquery/docs/anomaly-detection-overview).

You can use the output from dimensionality reduction models for tasks such as the following:

  * **Similarity search** : Find data points that are similar to each other based on their embeddings. This is great for finding related products, recommending similar content, or identifying duplicate or anomalous items.
  * **Clustering** : Use embeddings as input features for k-means models in order to group data points together based on their similarities. This can help you discover hidden patterns and insights in your data.
  * **Machine learning** : Use embeddings as input features for classification or regression models.



## Recommended knowledge

By using the default settings in the `CREATE MODEL` statements and the inference functions, you can create and use a dimensionality reduction model even without much ML knowledge. However, having basic knowledge about ML development helps you optimize both your data and your model to deliver better results. We recommend using the following resources to develop familiarity with ML techniques and processes:

  * [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
  * [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
  * [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
