---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-model-refresh/
title: Automatic model refresh \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:51.028560+00:00
---

# Automatic model refresh  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-model-refresh/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Automatic model refresh Stay organized with collections  Save and categorize content based on your preferences. 

With the automatic model refresh feature, when the underlying model changes, your pipeline updates to use the new model. Because the `RunInference` transform automatically updates the model handler, you don't need to redeploy the pipeline. With this feature, you can update your model in real time, even while the Apache Beam pipeline is running.

Automatic model refresh provides two methods for updating machine learning (ML) models, watch mode and event mode.

## Watch mode

Use one of the Apache Beam provided patterns, such as the [`WatchFilePattern`](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.utils.html) class, to watch for the latest file in your Cloud Storage bucket. `WatchFilePattern` uses timestamps to match a `file_pattern` and emits the latest [`ModelMetadata`](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html?highlight=modelmetadata#apache_beam.ml.inference.base.ModelMetadata), which the `RunInference PTransform` uses to update your ML model.

To learn more about using `WatchFilePattern` to automatically refresh ML models, see [Use WatchFilePattern to auto-update ML models in `RunInference`](https://beam.apache.org/documentation/ml/side-input-updates/) in the Apache Beam documentation.

## Event mode

Connect your pipeline to an unbounded source, such as Pub/Sub, to send update events directly to the transform, which initiates a model update. You configure a custom [side input](https://beam.apache.org/documentation/programming-guide/#side-inputs) `PCollection` that defines the logic for the model update.

To follow a tutorial that demonstrates how to update your model in production by using a side input `PCollection`, see [Update ML models in running pipelines](https://docs.cloud.google.com/dataflow/docs/notebooks/automatic_model_refresh).

## What's next

  * Read more about the [automatic model refresh](https://beam.apache.org/documentation/ml/about-ml/#automatic-model-refresh) feature in the Apache Beam documentation.

  * [Try this feature in a notebook](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/automatic_model_refresh.ipynb).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
