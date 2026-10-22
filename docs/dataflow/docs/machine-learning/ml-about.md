---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-about/
title: About Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:08.317775+00:00
---

# About Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  About Dataflow ML Stay organized with collections  Save and categorize content based on your preferences. 

You can use Dataflow ML's scale data processing abilities for prediction and inference pipelines and for data preparation for training.

![Diagram of the Dataflow ML
workflow.](https://docs.cloud.google.com/static/dataflow/images/dataflow-ml-workflow.png)

**Figure 1.** The complete Dataflow ML workflow. 

## Requirements and limitations

  * Dataflow ML supports batch and streaming pipelines.
  * The `RunInference` API is supported in Apache Beam 2.40.0 and later versions.
  * The `MLTransform` API is supported in Apache Beam 2.53.0 and later versions.
  * Model handlers are available for PyTorch, scikit-learn, TensorFlow, ONNX, and TensorRT. For unsupported frameworks, you can use a custom model handler.



## Data preparation for training

  * Use the `MLTransform` feature to prepare your data for training ML models. For more information, see [Preprocess data with `MLTransform`](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-preprocess-data).

  * Use Dataflow with ML-OPS frameworks, such as [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines/v1/introduction/) (KFP) or [TensorFlow Extended](https://www.tensorflow.org/tfx) (TFX). To learn more, see [Dataflow ML in ML workflows](https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-data).




## Prediction and inference pipelines

Dataflow ML combines the power of Dataflow with Apache Beam's [`RunInference` API](https://beam.apache.org/documentation/ml/about-ml/). With the `RunInference` API, you define the model's characteristics and properties and pass that configuration to the `RunInference` transform. This feature allows users to run the model within their Dataflow pipelines without needing to know the model's implementation details. You can choose the framework that best suits your data, such as TensorFlow and PyTorch.

## Run multiple models in a pipeline

Use the `RunInference` transform to add multiple inference models to your Dataflow pipeline. For more information, including code details, see [Multi-model pipelines](https://beam.apache.org/documentation/ml/about-ml/#multi-model-pipelines) in the Apache Beam documentation.

## Build a cross-language pipeline

To use RunInference with a Java pipeline, [create a cross-language Python transform](https://beam.apache.org/documentation/programming-guide/#1312-creating-cross-language-python-transforms). The pipeline calls the transform, which does the preprocessing, postprocessing, and inference.

For detailed instructions and a sample pipeline, see [Using RunInference from the Java SDK](https://beam.apache.org/documentation/ml/multi-language-inference/).

## Use GPUs with Dataflow

For batch or streaming pipelines that require the use of accelerators, you can run Dataflow pipelines on NVIDIA GPU devices. For more information, see [Run a Dataflow pipeline with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).

## Troubleshoot Dataflow ML

This section provides troubleshooting strategies and links that you might find helpful when using Dataflow ML.

### Stack expects each tensor to be equal size

If you provide images of different sizes or word embeddings of different lengths when using the `RunInference` API, the following error might occur:
    
    
    File "/beam/sdks/python/apache_beam/ml/inference/pytorch_inference.py", line 232, in run_inference batched_tensors = torch.stack(key_to_tensor_list[key]) RuntimeError: stack expects each tensor to be equal size, but got [12] at entry 0 and [10] at entry 1 [while running 'PyTorchRunInference/ParDo(_RunInferenceDoFn)']
    

This error occurs because the `RunInference` API can't batch tensor elements of different sizes. For workarounds, see [Unable to batch tensor elements](https://beam.apache.org/documentation/ml/about-ml/#unable-to-batch-tensor-elements) in the Apache Beam documentation.

### Avoid out-of-memory errors with large models

When you load a medium or large ML model, your machine might run out of memory. Dataflow provides tools to help avoid out-of-memory (OOM) errors when loading ML models. For more information, see [`RunInference` transform best practices](https://docs.cloud.google.com/dataflow/docs/machine-learning/runinference-best-practices#memory-management).

## What's next

  * Explore the [Dataflow ML notebooks](https://docs.cloud.google.com/dataflow/docs/machine-learning/notebooks) to view specific use cases.
  * Get in-depth information about using ML with Apache Beam in Apache Beam's [AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) documentation.
  * Learn more about the [`RunInference` API](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.html#apache_beam.ml.inference.RunInference).
  * Learn about [`RunInference` best practices](https://docs.cloud.google.com/dataflow/docs/machine-learning/runinference-best-practices).
  * Learn about the [metrics](https://beam.apache.org/documentation/ml/runinference-metrics/) that you can use to monitor your `RunInference` transform.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
