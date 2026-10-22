---
url: https://docs.cloud.google.com/bigquery/docs/clustering-overview/
title: Clustering overview \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:13.278768+00:00
---

# Clustering overview  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/clustering-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Clustering overview

Clustering is an unsupervised machine learning technique you can use to group similar records together. It is a useful approach for when you want to understand what groups or clusters you have in your data, but don't have labeled data to train a model on. For example, if you had unlabeled data about subway ticket purchases, you could cluster that data by ticket purchase time to better understand what time periods have the heaviest subway usage. For more information, see [What is clustering?](https://developers.google.com/machine-learning/clustering/overview)

[K-means models](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-kmeans) are widely used to perform clustering. You can use k-means models with the [`ML.PREDICT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-predict) to cluster data, or with the [`ML.DETECT_ANOMALIES` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-detect-anomalies) to perform [anomaly detection](https://docs.cloud.google.com/bigquery/docs/anomaly-detection-overview).

K-means models use [centroid-based clustering](https://developers.google.com/machine-learning/clustering/clustering-algorithms#centroid-based_clustering) to organize data into clusters. To get information about a k-means model's centroids, you can use the [`ML.CENTROIDS` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-centroids).

## Recommended knowledge

By using the default settings in the `CREATE MODEL` statements and the inference functions, you can create and use a clustering model even without much ML knowledge. However, having basic knowledge about ML development, and clustering models in particular, helps you optimize both your data and your model to deliver better results. We recommend using the following resources to develop familiarity with ML techniques and processes:

  * [Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)
  * [Intro to Machine Learning](https://www.kaggle.com/learn/intro-to-machine-learning)
  * [Intermediate Machine Learning](https://www.kaggle.com/learn/intermediate-machine-learning)
  * [Clustering](https://developers.google.com/machine-learning/clustering)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
