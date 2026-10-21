---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/scale_data/
title: Use MLTransform to scale data \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:15:59.989485+00:00
---

# Use MLTransform to scale data  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/scale_data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Use MLTransform to scale data Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/data_preprocessing/scale_data.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/data_preprocessing/scale_data.ipynb) Scaling data is an important preprocessing step for training machine learning (ML) models, because it helps to ensure that all features have a similar weight or influence on the model. The following are benefits of scaling data:

  * **Improved convergence of gradient descent algorithms:** Many machine learning algorithms, such as linear regression and neural networks, use gradient descent to optimize their parameters. Gradient descent iteratively moves the parameters of the model in the direction that reduces the loss function. If the features aren't scaled, features with larger ranges can have a much larger impact on the gradient, making it difficult for the model to converge. Scaling the features helps to ensure that all features contribute equally to the gradient, which can lead to faster and more stable convergence.
  * **Uniformity in features:** If one feature has a much larger range than the other features, it can dominate the model and make it difficult for the model to learn from the other features. This lack of uniformity can cause poor performance and biased predictions. Scaling the features brings all of the features into a similar range.

To scale your dataset using Apache Beam, use `MLTransform` with one of the following transforms:

  * `ScaleTo01`: Calculates the minimum and maximum of an entire dataset, and then scales the dataset between 0 and 1 based on minimum and maximum values.
  * `ScaleToZScore`: Calculates the mean and variance of an entire dataset, and then scales the dataset based on those values.
  * `ScaleByMinMax`: Scales the data in a dataset, taking minimum and maximum values as input parameters.

For each data processing transform, `MLTransform` runs in both `write` mode and `read` mode. For more information about using `MLTransform`, see [Preprocess data with MLTransform](https://beam.apache.org/documentation/ml/preprocess-data/) in the Apache Beam documentation.

## MLTransform in write mode

When `MLTransform` is in `write` mode, it produces artifacts, such as minimum, maximum, and variance, for different data processing transforms. These artifacts allow you to ensure that you're applying the same artifacts, and any other preprocessing transforms, when you train your model and serve it in production, or when you test its accuracy.

## MLTransform in read mode

In read mode, `MLTransform` uses the artifacts generated in `write` mode to scale the entire dataset.

## Import the required modules

To use `MLTransfrom`, install `tensorflow_transform` and the Apache Beam SDK version 2.53.0 or later.
    
    
     pip install apache_beam[interactive]>=2.53.0 --quiet
     pip install tensorflow-transform --quiet
    
    
    import os
    import tempfile
    import apache_beam as beam
    from apache_beam.ml.transforms.base import MLTransform
    from apache_beam.ml.transforms.tft import ScaleTo01
    from apache_beam.ml.transforms.tft import ScaleByMinMax
    from apache_beam.ml.transforms.tft import ScaleToZScore
    
    
    
    artifact_location_scale_to_01 = tempfile.mkdtemp(prefix='scale_to_01_')
    artifact_location_scale_to_zscore = tempfile.mkdtemp(prefix='scale_to_zscore_')
    artifact_location_scale_by_min_max = tempfile.mkdtemp(prefix='scale_by_min_max_')
    
    
    
    # data used in MLTransform's write mode
    data = [
        {'int_feature_1' : 11, 'int_feature_2': -10},
        {'int_feature_1': 34, 'int_feature_2': -33},
        {'int_feature_1': 5, 'int_feature_2': -63},
        {'int_feature_1': 12, 'int_feature_2': -38},
        {'int_feature_1': 32, 'int_feature_2': -65},
        {'int_feature_1': 63, 'int_feature_2': -21},
    ]
    
    # data used in MLTransform's read mode
    test_data = [
        {'int_feature_1': 29, 'int_feature_2': -20},
        {'int_feature_1': -5, 'int_feature_2': -11},
        {'int_feature_1': 5, 'int_feature_2': -44},
        {'int_feature_1': 29, 'int_feature_2': -12},
        {'int_feature_1': 20, 'int_feature_2': -53},
        {'int_feature_1': 70, 'int_feature_2': -8}
    ]
    

## Scale the data between 0 and 1

Scale the data so that it's in the range of 0 to 1. To scale the data, the transform calculates minimum and maximum values on the whole dataset, and then performs the following calculation: `x = (x - x_min) / (x_max - x_min)` To scale the data, use the [ScaleTo01](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.transforms.tft.html#apache_beam.ml.transforms.tft.ScaleTo01) data processing transform in `MLTransform`.
    
    
    # MLTransform in write mode.
    with beam.Pipeline() as pipeline:
      data_pcoll = pipeline | "CreateData" >> beam.Create(data)
    
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(write_artifact_location=artifact_location_scale_to_01).with_transform(
              ScaleTo01(columns=['int_feature_1', 'int_feature_2'])
          )
      )
      transformed_pcoll | "Print" >> beam.Map(print)
    
    
    
    Row(int_feature_1=array([0.10344828], dtype=float32), int_feature_2=array([1.], dtype=float32))
    Row(int_feature_1=array([0.5], dtype=float32), int_feature_2=array([0.58181816], dtype=float32))
    Row(int_feature_1=array([0.], dtype=float32), int_feature_2=array([0.03636364], dtype=float32))
    Row(int_feature_1=array([0.12068965], dtype=float32), int_feature_2=array([0.4909091], dtype=float32))
    Row(int_feature_1=array([0.46551725], dtype=float32), int_feature_2=array([0.], dtype=float32))
    Row(int_feature_1=array([1.], dtype=float32), int_feature_2=array([0.8], dtype=float32))
    

In the this dataset, the following are the minimum and maximum values for the columns:

  * `int_feature_1`: 5 and 63.
  * `int_feature_2`: -65 and -10

In the output for the column `int_feature_1`, the data is scaled between 0 and 1 by using the values `5` and `63`. `5` is scaled to `0`, and `63` is scaled to `1`. The remaining values are scaled between 0 and 1 by using the formula `x = (x - x_min) / (x_max - x_min)`.
    
    
    # MLTransform in read mode
    with beam.Pipeline() as pipeline:
      data_pcoll = pipeline | "CreateData" >> beam.Create(test_data)
    
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(read_artifact_location=artifact_location_scale_to_01)
      )
      transformed_pcoll | "Print" >> beam.Map(print)
    
    
    
    Row(int_feature_1=array([0.41379312], dtype=float32), int_feature_2=array([0.8181818], dtype=float32))
    Row(int_feature_1=array([-0.1724138], dtype=float32), int_feature_2=array([0.9818182], dtype=float32))
    Row(int_feature_1=array([0.], dtype=float32), int_feature_2=array([0.38181818], dtype=float32))
    Row(int_feature_1=array([0.41379312], dtype=float32), int_feature_2=array([0.96363634], dtype=float32))
    Row(int_feature_1=array([0.25862068], dtype=float32), int_feature_2=array([0.21818182], dtype=float32))
    Row(int_feature_1=array([1.1206896], dtype=float32), int_feature_2=array([1.0363636], dtype=float32))
    

`MLTransform` learned in `write` mode that `int_feature_1` ranges from 5 to 63. In `read` mode, when it encounters 29 in `test_data` for `int_feature_1`, it scales it by using the following formula:
    
    
    (value - min) / (max - min)
    

The following calculation shows the formula with the values:
    
    
    (29 - 5) / (63 - 5) = 0.41379312
    

Twenty-nine is scaled based on the minimum and maximum values generated in `write` mode.

## Scale by using the z-score

Similar to `ScaleTo01`, use [ScaleToZScore](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.transforms.tft.html#apache_beam.ml.transforms.tft.ScaleToZScore) to scale the values by using the [z-score](https://www.tensorflow.org/tfx/transform/api_docs/python/tft/scale_to_z_score#:%7E:text=Scaling%20to%20z%2Dscore%20subtracts%20out%20the%20mean%20and%20divides%20by%20standard%20deviation.%20Note%20that%20the%20standard%20deviation%20computed%20here%20is%20based%20on%20the%20biased%20variance%20\(0%20delta%20degrees%20of%20freedom\)%2C%20as%20computed%20by%20analyzers.var).
    
    
    # MLTransform in write mode
    with beam.Pipeline() as pipeline:
      data_pcoll = pipeline | "CreateData" >> beam.Create(data)
    
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(write_artifact_location=artifact_location_scale_to_zscore).with_transform(
              ScaleToZScore(columns=['int_feature_1', 'int_feature_2'])
          )
      )
      transformed_pcoll | "Print" >> beam.Map(print)
    
    
    
    Row(int_feature_1=array([-0.76950264], dtype=float32), int_feature_2=array([1.401755], dtype=float32))
    Row(int_feature_1=array([0.3974355], dtype=float32), int_feature_2=array([0.2638597], dtype=float32))
    Row(int_feature_1=array([-1.0739213], dtype=float32), int_feature_2=array([-1.2203515], dtype=float32))
    Row(int_feature_1=array([-0.7187662], dtype=float32), int_feature_2=array([0.01649117], dtype=float32))
    Row(int_feature_1=array([0.2959626], dtype=float32), int_feature_2=array([-1.3192989], dtype=float32))
    Row(int_feature_1=array([1.8687923], dtype=float32), int_feature_2=array([0.8575442], dtype=float32))
    
    
    
    # MLTransform in read mode
    with beam.Pipeline() as pipeline:
      data_pcoll = pipeline | "CreateData" >> beam.Create(test_data)
    
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(read_artifact_location=artifact_location_scale_to_zscore)
      )
      transformed_pcoll | "Print" >> beam.Map(print)
    
    
    
    Row(int_feature_1=array([0.14375328], dtype=float32), int_feature_2=array([0.9070179], dtype=float32))
    Row(int_feature_1=array([-1.5812857], dtype=float32), int_feature_2=array([1.3522812], dtype=float32))
    Row(int_feature_1=array([-1.0739213], dtype=float32), int_feature_2=array([-0.28035107], dtype=float32))
    Row(int_feature_1=array([0.14375328], dtype=float32), int_feature_2=array([1.3028076], dtype=float32))
    Row(int_feature_1=array([-0.31287467], dtype=float32), int_feature_2=array([-0.7256144], dtype=float32))
    Row(int_feature_1=array([2.2239475], dtype=float32), int_feature_2=array([1.5007024], dtype=float32))
    

## Scale by using ScaleByMinMax

Use [ScaleByMinMax](https://github.com/apache/beam/blob/9e8a310f0c0faddfba28176df5893d8ad8fd10a0/sdks/python/apache_beam/ml/transforms/tft.py#L450) to scale your data into the range of `[min_value, max_value]`.
    
    
    min_value = 1
    max_value = 10
    
    # MLTransform in write mode
    with beam.Pipeline() as pipeline:
      data_pcoll = pipeline | "CreateData" >> beam.Create(data)
    
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(write_artifact_location=artifact_location_scale_by_min_max).with_transform(
              ScaleByMinMax(columns=['int_feature_1', 'int_feature_2'], min_value=min_value, max_value=max_value)
          )
      )
      transformed_pcoll | "Print" >> beam.Map(print)
    
    
    
    Row(int_feature_1=array([1.9310346], dtype=float32), int_feature_2=array([10.], dtype=float32))
    Row(int_feature_1=array([5.5], dtype=float32), int_feature_2=array([6.2363634], dtype=float32))
    Row(int_feature_1=array([1.], dtype=float32), int_feature_2=array([1.3272727], dtype=float32))
    Row(int_feature_1=array([2.086207], dtype=float32), int_feature_2=array([5.418182], dtype=float32))
    Row(int_feature_1=array([5.1896553], dtype=float32), int_feature_2=array([1.], dtype=float32))
    Row(int_feature_1=array([10.], dtype=float32), int_feature_2=array([8.200001], dtype=float32))
    
    
    
    # MLTransform in read mode
    with beam.Pipeline() as pipeline:
      data_pcoll = pipeline | "CreateData" >> beam.Create(test_data)
    
      transformed_pcoll = (
          data_pcoll
          | "MLTransform" >> MLTransform(read_artifact_location=artifact_location_scale_by_min_max)
      )
      transformed_pcoll | "Print" >> beam.Map(print)
    
    
    
    Row(int_feature_1=array([4.7241383], dtype=float32), int_feature_2=array([8.363636], dtype=float32))
    Row(int_feature_1=array([-0.5517242], dtype=float32), int_feature_2=array([9.836364], dtype=float32))
    Row(int_feature_1=array([1.], dtype=float32), int_feature_2=array([4.4363637], dtype=float32))
    Row(int_feature_1=array([4.7241383], dtype=float32), int_feature_2=array([9.672727], dtype=float32))
    Row(int_feature_1=array([3.3275862], dtype=float32), int_feature_2=array([2.9636364], dtype=float32))
    Row(int_feature_1=array([11.086206], dtype=float32), int_feature_2=array([10.327272], dtype=float32))
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
