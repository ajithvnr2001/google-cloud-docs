---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow/
title: Apache Beam RunInference with TensorFlow \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:44:44.157409+00:00
---

# Apache Beam RunInference with TensorFlow  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Apache Beam RunInference with TensorFlow Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow.ipynb) This notebook shows how to use the Apache Beam [RunInference](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference) transform for [TensorFlow](https://www.tensorflow.org/). Apache Beam has built-in support for two TensorFlow model handlers: [`TFModelHandlerNumpy`](https://github.com/apache/beam/blob/ca0787642a6b3804a742326147281c99ae8d08d2/sdks/python/apache_beam/ml/inference/tensorflow_inference.py#L91) and [`TFModelHandlerTensor`](https://github.com/apache/beam/blob/ca0787642a6b3804a742326147281c99ae8d08d2/sdks/python/apache_beam/ml/inference/tensorflow_inference.py#L184).

  * Use `TFModelHandlerNumpy` to run inference on models that use a `numpy` array as an input.
  * Use `TFModelHandlerTensor` to run inference on models that use a `tf.Tensor` as an input.

If your model uses `tf.Example` as an input, see the [Apache Beam RunInference with `tfx-bsl`](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow_with_tfx.ipynb) notebook. There are three ways to load a TensorFlow model:

  1. Provide a path to the saved model.
  2. Provide a path to the saved weights of the model.
  3. Provide a URL for pretrained model on TensorFlow Hub. For an example workflow, see [Apache Beam RunInference with TensorFlow and TensorFlow Hub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_with_tensorflow_hub.ipynb).

This notebook demonstrates the following steps:

  * Build a simple TensorFlow model.
  * Set up example data.
  * Run those examples with the built-in model handlers using one of the following methods, and then get a prediction inside an Apache Beam pipeline.: 
    * a saved model
    * saved weights

For more information about using RunInference, see [Get started with AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) in the Apache Beam documentation.

## Before you begin

Set up your environment and download dependencies.

### Install Apache Beam

To use RunInference with the built-in Tensorflow model handler, install Apache Beam version 2.46.0 or later.
    
    
    !pip install protobuf --quiet
    !pip install apache_beam[interactive]==2.46.0 --quiet
    
    # To use the newly installed versions, restart the runtime.
    exit()
    

### Authenticate with Google Cloud

This notebook relies on saving your model to Google Cloud. To use your Google Cloud account, authenticate this notebook.
    
    
    from google.colab import auth
    auth.authenticate_user()
    

### Import dependencies and set up your bucket

Use the following code to import dependencies and to set up your Google Cloud Storage bucket. Replace `PROJECT_ID` and `BUCKET_NAME` with the ID of your project and the name of your bucket.
    
    
    import argparse
    from typing import Dict, Text, Any, Tuple, List
    import numpy
    
    from google.protobuf import text_format
    
    import tensorflow as tf
    from tensorflow import keras
    import apache_beam as beam
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.base import KeyedModelHandler
    from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerNumpy
    from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerTensor
    from apache_beam.options.pipeline_options import PipelineOptions
    
    project = "PROJECT_ID" # @param {type:'string'}
    bucket = "BUCKET_NAME" # @param {type:'string'}
    
    save_model_dir_multiply = f'gs://{bucket}/tf-inference/model/multiply_five/v1/'
    save_weights_dir_multiply = f'gs://{bucket}/tf-inference/weights/multiply_five/v1/'
    

## Create and test a simple model

This step creates and tests a model that predicts the 5 times table.

### Create the model

Create training data and build a linear regression model.
    
    
    # Create training data that represents the 5 times multiplication table for the numbers 0 to 99.
    # x is the data and y is the labels.
    x = numpy.arange(0, 100)   # Examples
    y = x * 5                  # Labels
    
    # Use create_model to build a simple linear regression model.
    # Note that the model has a shape of (1) for its input layer and expects a single int64 value.
    def create_model():
      input_layer = keras.layers.Input(shape=(1), dtype=tf.float32, name='x')
      output_layer= keras.layers.Dense(1)(input_layer)
      model = keras.Model(input_layer, output_layer)
      model.compile(optimizer=tf.optimizers.Adam(), loss='mean_absolute_error')
      return model
    
    model = create_model()
    model.summary()
    
    
    
    Model: "model_1"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     x (InputLayer)              [(None, 1)]               0         
                                                                     
     dense_1 (Dense)             (None, 1)                 2         
                                                                     
    =================================================================
    Total params: 2
    Trainable params: 2
    Non-trainable params: 0
    _________________________________________________________________
    

### Test the model

This step tests the model that you created.
    
    
    model.fit(x, y, epochs=500, verbose=0)
    test_examples =[20, 40, 60, 90]
    value_to_predict = numpy.array(test_examples, dtype=numpy.float32)
    predictions = model.predict(value_to_predict)
    
    print('Test Examples ' + str(test_examples))
    print('Predictions ' + str(predictions))
    
    
    
    1/1 [==============================] - 0s 38ms/step
    Test Examples [20, 40, 60, 90]
    Predictions [[21.896107]
     [41.795692]
     [61.69528 ]
     [91.544655]]
    

### Save the model

This step shows how to save your model.
    
    
    model.save(save_model_dir_multiply)
    

Instead of saving the entire model, you can [save the model weights for inference](https://www.tensorflow.org/guide/keras/save_and_serialize#saving_loading_only_the_models_weights_values). You can use this method when you need the model for inference but don't need any compilation information or optimizer state. In addition, when using transfer learning applications, you can use this method to load the weights with new models. With this approach, you need to pass the function to build the TensorFlow model to the `TFModelHandler` class that you're using, either`TFModelHandlerNumpy` or `TFModelHandlerTensor`. You also need to pass `model_type=ModelType.SAVED_WEIGHTS` to the class.
    
    
    model_handler = TFModelHandlerNumpy(path_to_weights, model_type=ModelType.SAVED_WEIGHTS, create_model_fn=build_tensorflow_model)
    
    
    
    model.save_weights(save_weights_dir_multiply)
    

## Run the pipeline

Use the following code to run the pipeline by specifying path to the trained TensorFlow model.
    
    
    class FormatOutput(beam.DoFn):
      def process(self, element, *args, **kwargs):
         yield "example is {example} prediction is {prediction}".format(example=element.example, prediction=element.inference)
    
    
    examples = numpy.array([20, 40, 60, 90], dtype=numpy.float32)
    model_handler = TFModelHandlerNumpy(save_model_dir_multiply)
    with beam.Pipeline() as p:
        _ = (p | beam.Create(examples)
               | RunInference(model_handler)
               | beam.ParDo(FormatOutput())
               | beam.Map(print)
            )
    
    
    
    WARNING:apache_beam.runners.interactive.interactive_environment:Dependencies required for Interactive Beam PCollection visualization are not available, please use: `pip install apache-beam[interactive]` to install necessary dependencies to enable all data visualization features.
    example is 20.0 prediction is [21.896107]
    example is 40.0 prediction is [41.795692]
    example is 60.0 prediction is [61.69528]
    example is 90.0 prediction is [91.544655]
    

Use the following code to run the pipeline with the saved weights of a TensorFlow model. To load the model with saved weights, the `TFModelHandlerNumpy` class requires a `create_model` function that builds and returns a TensorFlow model that is compatible with the saved weights.
    
    
    from apache_beam.ml.inference.tensorflow_inference import ModelType
    examples = numpy.array([20, 40, 60, 90], dtype=numpy.float32)
    model_handler = TFModelHandlerNumpy(save_weights_dir_multiply, model_type=ModelType.SAVED_WEIGHTS, create_model_fn=create_model)
    with beam.Pipeline() as p:
        _ = (p | beam.Create(examples)
               | RunInference(model_handler)
               | beam.ParDo(FormatOutput())
               | beam.Map(print)
            )
    
    
    
    example is 20.0 prediction is [21.896107]
    example is 40.0 prediction is [41.795692]
    example is 60.0 prediction is [61.69528]
    example is 90.0 prediction is [91.544655]
    

## Use a keyed model handler

To use a keyed model handler, use `KeyedModelHandler` with TensorFlow by using `TFModelHandlerNumpy`. By default, the `ModelHandler` does not expect a key.

  * If you know that keys are associated with your examples, use `beam.KeyedModelHandler` to wrap the model handler.
  * If you don't know whether keys are associated with your examples, use `beam.MaybeKeyedModelHandler`.


    
    
    class FormatOutputKeyed(FormatOutput):
      # To simplify, inherit from FormatOutput.
      def process(self, tuple_in: Tuple):
        key, element = tuple_in
        output = super().process(element)
        yield "{} : {}".format(key, [op for op in output])
    
    examples = numpy.array([(1,20), (2,40), (3,60), (4,90)], dtype=numpy.float32)
    keyed_model_handler = KeyedModelHandler(TFModelHandlerNumpy(save_model_dir_multiply))
    with beam.Pipeline() as p:
        _ = (p | 'CreateExamples' >> beam.Create(examples)
               | RunInference(keyed_model_handler)
               | beam.ParDo(FormatOutputKeyed())
               | beam.Map(print)
            )
    
    
    
    1.0 : ['example is 20.0 prediction is [51.815357]']
    2.0 : ['example is 40.0 prediction is [101.63492]']
    3.0 : ['example is 60.0 prediction is [151.45448]']
    4.0 : ['example is 90.0 prediction is [226.18384]']
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
