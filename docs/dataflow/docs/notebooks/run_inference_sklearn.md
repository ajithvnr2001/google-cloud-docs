---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_sklearn/
title: Apache Beam RunInference for scikit-learn \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:49.188063+00:00
---

# Apache Beam RunInference for scikit-learn  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_sklearn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Apache Beam RunInference for scikit-learn Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_sklearn.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_sklearn.ipynb) This notebook demonstrates the use of the RunInference transform for [scikit-learn](https://scikit-learn.org/), also called sklearn. Apache Beam [RunInference](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference) has implementations of the [ModelHandler](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.ModelHandler) class prebuilt for scikit-learn. For more information about using RunInference, see [Get started with AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) in the Apache Beam documentation. You can choose the appropriate model handler based on your input data type:

  * [NumPy model handler](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.sklearn_inference.html#apache_beam.ml.inference.sklearn_inference.SklearnModelHandlerNumpy)
  * [Pandas DataFrame model handler](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.sklearn_inference.html#apache_beam.ml.inference.sklearn_inference.SklearnModelHandlerNumpy)

With RunInference, these model handlers manage batching, vectorization, and prediction optimization for your scikit-learn pipeline or model. This notebook demonstrates the following common RunInference patterns:

  * Generate predictions.
  * Postprocess results after RunInference.
  * Run inference with multiple models in the same pipeline.

The linear regression models used in these samples are trained on data that correspondes to the 5 and 10 times tables; that is,`y = 5x` and `y = 10x` respectively.

## Before you begin

Complete the following setup steps:

  1. Install dependencies for Apache Beam.
  2. Authenticate with Google Cloud.
  3. Specify your project and bucket. You use the project and bucket to save and load models.


    
    
    pip install google-api-core --quiet
    pip install google-cloud-pubsub google-cloud-bigquery-storage --quiet
    pip install apache-beam[gcp,dataframe] --quiet

## About scikit-learn versions

`scikit-learn` is a build-dependency of Apache Beam. If you need to install a different version of sklearn , use `%pip install scikit-learn==<version>`
    
    
    from google.colab import auth
    auth.authenticate_user()
    
    
    
    import pickle
    from sklearn import linear_model
    from typing import Tuple
    
    import numpy as np
    import apache_beam as beam
    
    from apache_beam.ml.inference.sklearn_inference import ModelFileType
    from apache_beam.ml.inference.sklearn_inference import SklearnModelHandlerNumpy
    from apache_beam.ml.inference.base import KeyedModelHandler
    from apache_beam.ml.inference.base import PredictionResult
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.options.pipeline_options import PipelineOptions
    
    # NOTE: If an error occurs, restart your runtime.
    
    
    
    import os
    
    # Constants
    project = "<PROJECT_ID>" # @param {type:'string'}
    bucket = "<BUCKET_NAME>" # @param {type:'string'}
    
    # To avoid warnings, set the project.
    os.environ['GOOGLE_CLOUD_PROJECT'] = project
    

## Create the data and the scikit-learn model

This section demonstrates the following steps:

  1. Create the data to train the scikit-learn linear regression model.
  2. Train the linear regression model.
  3. Save the scikit-learn model using `pickle`.

In this example, you create two models, one with the 5 times model and a second with the 10 times model.
    
    
    # Input data to train the sklearn model for the 5 times table.
    x = np.arange(0, 100, dtype=np.float32).reshape(-1, 1)
    y = (x * 5).reshape(-1, 1)
    
    def train_and_save_model(x, y, model_file_name):
      regression = linear_model.LinearRegression()
      regression.fit(x,y)
    
      with open(model_file_name, 'wb') as f:
          pickle.dump(regression, f)
    
    five_times_model_filename = 'sklearn_5x_model.pkl'
    train_and_save_model(x, y, five_times_model_filename)
    
    # Change y to be 10 times, and output a 10 times table.
    ten_times_model_filename = 'sklearn_10x_model.pkl'
    train_and_save_model(x, y, ten_times_model_filename)
    y = (x * 10).reshape(-1, 1)
    train_and_save_model(x, y, 'sklearn_10x_model.pkl')
    

### Create a scikit-learn RunInference pipeline

This section demonstrates how to do the following:

  1. Define a scikit-learn model handler that accepts an `array_like` object as input.
  2. Read the data from BigQuery.
  3. Use the scikit-learn trained model and the scikit-learn RunInference transform on unkeyed data.


    
    
    %pip install --upgrade google-cloud-bigquery --quiet
    
    
    
    gcloud config set project $project
    
    
    Updated property [core/project].
    
    
    
    # Populated BigQuery table
    
    from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
    
    client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(project=project)
    
    # Make sure the dataset_id is unique in your project.
    dataset_id = '{project}.maths'.format(project=project)
    dataset = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.dataset.Dataset.html)(dataset_id)
    
    # Modify the location based on your project configuration.
    dataset.location = 'US'
    dataset = client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset)(dataset, exists_ok=True)
    
    # Table name in the BigQuery dataset.
    table_name = 'maths_problems_1'
    
    query = """
        CREATE OR REPLACE TABLE
          {project}.maths.{table} ( key STRING OPTIONS(description="A unique key for the maths problem"),
        value FLOAT64 OPTIONS(description="Our maths problem" ) );
        INSERT INTO maths.{table}
        VALUES
          ("first_example", 105.00),
          ("second_example", 108.00),
          ("third_example", 1000.00),
          ("fourth_example", 1013.00)
    """.format(project=project, table=table_name)
    
    create_job = client.[query](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(query)
    [create_job](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_job).result()
    
    
    
    <google.cloud.bigquery.table._EmptyRowIterator at 0x7f97abb4e850>
    
    
    
    sklearn_model_handler = SklearnModelHandlerNumpy(model_uri=five_times_model_filename) 
    
    
    pipeline_options = PipelineOptions().from_dictionary(
                                          {'temp_location':f'gs://{bucket}/tmp'})
    
    # Define the BigQuery table specification.
    table_name = 'maths_problems_1'
    table_spec = f'{project}:maths.{table_name}'
    
    with beam.Pipeline(options=pipeline_options) as p:
      (
          p 
          | "ReadFromBQ" >> beam.io.ReadFromBigQuery(table=table_spec)
          | "ExtractInputs" >> beam.Map(lambda x: [x['value']]) 
          | "RunInferenceSklearn" >> RunInference(model_handler=sklearn_model_handler)
          | beam.Map(print)
      )
    
    
    
    PredictionResult(example=[1000.0], inference=array([5000.]))
    PredictionResult(example=[1013.0], inference=array([5065.]))
    PredictionResult(example=[108.0], inference=array([540.]))
    PredictionResult(example=[105.0], inference=array([525.]))
    

### Use sklearn RunInference on keyed inputs

This section demonstrates how to do the following:

  1. Wrap the `SklearnModelHandlerNumpy` object around `KeyedModelHandler` to handle keyed data.
  2. Read the data from BigQuery.
  3. Use the sklearn trained model and the sklearn RunInference transform on a keyed data.


    
    
    sklearn_model_handler = SklearnModelHandlerNumpy(model_uri=five_times_model_filename) 
    keyed_sklearn_model_handler = KeyedModelHandler(sklearn_model_handler)
    
    pipeline_options = PipelineOptions().from_dictionary(
                                          {'temp_location':f'gs://{bucket}/tmp'})
    with beam.Pipeline(options=pipeline_options) as p:
      (
      p 
      | "ReadFromBQ" >> beam.io.ReadFromBigQuery(table=table_spec)
      | "ExtractInputs" >> beam.Map(lambda x: (x['key'], [x['value']])) 
      | "RunInferenceSklearn" >> RunInference(model_handler=keyed_sklearn_model_handler)
      | beam.Map(print)
      )
    
    
    
    ('third_example', PredictionResult(example=[1000.0], inference=array([5000.])))
    ('fourth_example', PredictionResult(example=[1013.0], inference=array([5065.])))
    ('second_example', PredictionResult(example=[108.0], inference=array([540.])))
    ('first_example', PredictionResult(example=[105.0], inference=array([525.])))
    

## Run multiple models

This code creates a pipeline that takes two RunInference transforms with different models and then combines the output.
    
    
    from typing import Tuple
    
    def format_output(run_inference_output) -> str:
      """Takes input from RunInference for scikit-learn and extracts the output."""
      key, prediction_result = run_inference_output
      example = prediction_result.example[0]
      prediction = prediction_result.inference[0]
      return f"key = {key}, example = {example} -> predictions {prediction}"
    
    five_times_model_handler = KeyedModelHandler(
        SklearnModelHandlerNumpy(model_uri=five_times_model_filename))
    ten_times_model_handler = KeyedModelHandler(
        SklearnModelHandlerNumpy(model_uri=ten_times_model_filename))
    
    pipeline_options = PipelineOptions().from_dictionary(
                                          {'temp_location':f'gs://{bucket}/tmp'})
    with beam.Pipeline(options=pipeline_options) as p:
      inputs = (p 
        | "ReadFromBQ" >> beam.io.ReadFromBigQuery(table=table_spec))
      five_times = (inputs
        | "Extract For 5" >> beam.Map(lambda x: ('{} {}'.format(x['key'], '* 5'), [x['value']]))
        | "5 times" >> RunInference(model_handler = five_times_model_handler))
      ten_times = (inputs
        | "Extract For 10" >> beam.Map(lambda x: ('{} {}'.format(x['key'], '* 10'), [x['value']]))
        | "10 times" >> RunInference(model_handler = ten_times_model_handler))
      _ = ((five_times, ten_times) | "Flattened" >> beam.Flatten()
        | "format output" >> beam.Map(format_output)
        | "Print" >> beam.Map(print))
    
    
    
    key = third_example * 10, example = 1000.0 -> predictions 10000.0
    key = fourth_example * 10, example = 1013.0 -> predictions 10130.0
    key = second_example * 10, example = 108.0 -> predictions 1080.0
    key = first_example * 10, example = 105.0 -> predictions 1050.0
    key = third_example * 5, example = 1000.0 -> predictions 5000.0
    key = fourth_example * 5, example = 1013.0 -> predictions 5065.0
    key = second_example * 5, example = 108.0 -> predictions 540.0
    key = first_example * 5, example = 105.0 -> predictions 525.0
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
