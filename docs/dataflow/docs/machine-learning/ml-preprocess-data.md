---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data/
title: Preprocess data with MLTransform \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:48.307490+00:00
---

# Preprocess data with MLTransform  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Preprocess data with MLTransform Stay organized with collections  Save and categorize content based on your preferences. 

This page explains why and how to use the [`MLTransform`](https://github.com/apache/beam/blob/3d501ee9dc208af2efef009daa98c49819b73ddc/sdks/python/apache_beam/ml/transforms/base.py#L112) feature to prepare your data for training machine learning (ML) models. By combining multiple data processing transforms in one class, `MLTransform` streamlines the process of applying Apache Beam ML data processing operations to your workflow.

For information about using `MLTransform` for embedding generation tasks, see [Generate embeddings with MLTransform](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-generate-embeddings).

![Diagram of the Dataflow ML workflow with the data processing step highlighted.](https://docs.cloud.google.com/static/dataflow/images/dataflow-ml-preprocess.png)

**Figure 1.** The complete Dataflow ML workflow. Use `MLTransform` in the preprocessing step of the workflow. 

## Benefits

The `MLTransform` class provides the following benefits:

  * Transform your data without writing complex code or managing underlying libraries.
  * Efficiently chain multiple types of processing operations with one interface.
  * Generate embeddings that you can use to push data into vector databases or to run inference.

For more information about embedding generation, see [Generate embeddings with MLTransform](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-generate-embeddings).




## Support and limitations

The `MLTransform` class has the following limitations:

  * Available for pipelines that use the Apache Beam Python SDK versions 2.53.0 and later.
  * Pipelines must use [default windows](https://beam.apache.org/documentation/programming-guide/#single-global-window).



**Data processing transforms that use TFT:**

  * Support Python 3.9, 3.10, 3.11.
  * Support batch pipelines.



## Use cases

The example notebooks demonstrate how to use `MLTransform` for embeddings-specific use cases.

[I want to compute a vocabulary from a dataset](https://docs.cloud.google.com/dataflow/docs/notebooks/compute_and_apply_vocab)
    Compute a unique vocabulary from a dataset and then map each word or token to a distinct integer index. Use this transform to change textual data into numerical representations for machine learning tasks.
[I want to scale my data to train my ML model](https://docs.cloud.google.com/dataflow/docs/notebooks/scale_data)
    Scale your data so that you can use it to train your ML model. The Apache Beam `MLTransform` class includes multiple data scaling transforms.

For a full list of available transforms, see [Transforms](https://beam.apache.org/documentation/ml/preprocess-data#transforms) in the Apache Beam documentation.

## Use MLTransform

To use the `MLTransform` class to preprocess data, include the following code in your pipeline:
    
    
      import apache_beam as beam
      from apache_beam.ml.transforms.base import MLTransform
      from apache_beam.ml.transforms.tft import TRANSFORM_NAME
      import tempfile
    
      data = [
          {
              DATA
          },
      ]
    
      artifact_location = gs://BUCKET_NAME
      TRANSFORM_FUNCTION_NAME = TRANSFORM_NAME(columns=['x'])
    
      with beam.Pipeline() as p:
        transformed_data = (
            p
            | beam.Create(data)
            | MLTransform(write_artifact_location=artifact_location).with_transform(
                TRANSFORM_FUNCTION_NAME)
            | beam.Map(print))
    

Replace the following values:

  * `TRANSFORM_NAME`: the name of the [transform](https://beam.apache.org/documentation/ml/preprocess-data/#transforms) to use
  * `BCUKET_NAME`: the name of your [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets#naming)
  * `DATA`: the input data to transform
  * `TRANSFORM_FUNCTION_NAME`: the name that you assign to your transform function in your code



## What's next

  * For more details about `MLTransform`, see [Preprocess data](https://beam.apache.org/documentation/ml/preprocess-data) in the Apache Beam documentation.
  * For more examples, see [`MLTransform` for data processing](https://beam.apache.org/documentation/transforms/python/elementwise/mltransform) in the Apache Beam transform catalog.
  * Run an [interactive notebook in Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/mltransform_basic.ipynb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
