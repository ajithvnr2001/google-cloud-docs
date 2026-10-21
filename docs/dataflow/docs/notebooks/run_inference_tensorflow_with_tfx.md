---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow_with_tfx/
title: Use RunInference with TFX Basic Shared Libraries \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:50.268050+00:00
---

# Use RunInference with TFX Basic Shared Libraries  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow_with_tfx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Use RunInference with TFX Basic Shared Libraries Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow_with_tfx.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow_with_tfx.ipynb) This notebook demonstrates how to use the Apache Beam [RunInference](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference) transform with TensorFlow and [TFX Basic Shared Libraries](https://github.com/tensorflow/tfx-bsl) (`tfx-bsl`). Use this approach when your trained model uses a `tf.Example` input. If you have `numpy` or `tf.Tensor` inputs, see the [Apache Beam RunInference with TensorFlow](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow.ipynb) notebook, which shows how to use the built-in TensorFlow model handlers. The Apache Beam RunInference transform accepts a model handler generated from [`tfx-bsl`](https://github.com/tensorflow/tfx-bsl) by using `CreateModelHandler`. This notebook demonstrates how to complete the following tasks:

  * Import `tfx-bsl`.
  * Build a simple TensorFlow model.
  * Set up example data.
  * Use the `tfx-bsl` model handler with the example data, and get a prediction inside an Apache Beam pipeline.

For more information about using RunInference, see [Get started with AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) in the Apache Beam documentation.

## Before you begin

Set up your environment and download dependencies.

### Import `tfx-bsl`

First, import `tfx-bsl`. Creating a model handler is supported in `tfx-bsl` versions 1.10 and later.
    
    
    pip install tfx_bsl==1.10.0 --quiet
    pip install protobuf --quiet
    pip install apache_beam[interactive] --quiet

### Authenticate with Google Cloud

This notebook relies on saving your model to Google Cloud. To use your Google Cloud account, authenticate this notebook.
    
    
    from google.colab import auth
    auth.authenticate_user()
    

### Import dependencies and set up your bucket

Use the following code to import dependencies and to set up your Google Cloud Storage bucket. Replace `PROJECT_ID` and `BUCKET_NAME` with the ID of your project and the name of your bucket. **Important:** If an error occurs, restart your runtime.
    
    
    import argparse
    
    import tensorflow as tf
    from tensorflow import keras
    from tensorflow_serving.apis import prediction_log_pb2
    
    import apache_beam as beam
    from apache_beam.ml.inference.base import RunInference
    import tfx_bsl
    from tfx_bsl.public.beam.run_inference import CreateModelHandler
    from tfx_bsl.public import tfxio
    from tfx_bsl.public.proto import model_spec_pb2
    from tensorflow_metadata.proto.v0 import schema_pb2
    
    import numpy
    
    from typing import Dict, Text, Any, Tuple, List
    
    from apache_beam.options.pipeline_options import PipelineOptions
    
    project = "PROJECT_ID" # @param {type:'string'}
    bucket = "BUCKET_NAME" # @param {type:'string'}
    
    save_model_dir_multiply = f'gs://{bucket}/tfx-inference/model/multiply_five/v1/'
    

## Create and test a simple model

This section creates and tests a model that predicts the 5 times multiplication table.

### Create the model

Create training data, and then build a linear regression model.
    
    
    # Create training data that represents the 5 times multiplication table for the numbers 0 to 99.
    # x is the data and y is the labels.
    x = numpy.arange(0, 100)   # Examples
    y = x * 5                  # Labels
    
    # Build a simple linear regression model.
    # Note that the model has a shape of (1) for its input layer and expects a single int64 value.
    input_layer = keras.layers.Input(shape=(1), dtype=tf.float32, name='x')
    output_layer= keras.layers.Dense(1)(input_layer)
    
    model = keras.Model(input_layer, output_layer)
    model.compile(optimizer=tf.optimizers.Adam(), loss='mean_absolute_error')
    model.summary()
    
    
    
    Model: "model"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     x (InputLayer)              [(None, 1)]               0         
                                                                     
     dense (Dense)               (None, 1)                 2         
                                                                     
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
    
    
    
    1/1 [==============================] - 0s 94ms/step
    Test Examples [20, 40, 60, 90]
    Predictions [[ 9.201942]
     [16.40566 ]
     [23.609379]
     [34.41496 ]]
    

## RunInference with Tensorflow using `tfx-bsl`

In versions 1.10.0 and later of `tfx-bsl`, you can create a TensorFlow `ModelHandler` to use with Apache Beam.

### Populate the data in a TensorFlow proto

Tensorflow data uses protos. If you are loading from a file, helpers exist for this step. Because this example uses generated data, this code populates a proto.
    
    
    # This example shows a proto that converts the samples and labels into
    # tensors usable by TensorFlow.
    
    class ExampleProcessor:
        def create_example_with_label(self, feature: numpy.float32,
                                 label: numpy.float32)-> tf.train.Example:
            return tf.train.Example(
                features=tf.train.Features(
                      feature={'x': self.create_feature(feature),
                               'y' : self.create_feature(label)
                      }))
    
        def create_example(self, feature: numpy.float32):
            return tf.train.Example(
                features=tf.train.Features(
                      feature={'x' : self.create_feature(feature)})
                )
    
        def create_feature(self, element: numpy.float32):
            return tf.train.Feature(float_list=tf.train.FloatList(value=[element]))
    
    # Create a labeled example file for the 5 times table.
    
    example_five_times_table = 'example_five_times_table.tfrecord'
    
    with tf.io.TFRecordWriter(example_five_times_table) as writer:
      for i in zip(x, y):
        example = ExampleProcessor().create_example_with_label(
            feature=i[0], label=i[1])
        writer.write(example.SerializeToString())
    
    # Create a file containing the values to predict.
    
    predict_values_five_times_table = 'predict_values_five_times_table.tfrecord'
    
    with tf.io.TFRecordWriter(predict_values_five_times_table) as writer:
      for i in value_to_predict:
        example = ExampleProcessor().create_example(feature=i)
        writer.write(example.SerializeToString())
    

### Fit the model

This step builds a model. Because RunInference requires pretrained models, this segment builds a usable model.
    
    
    RAW_DATA_TRAIN_SPEC = {
    'x': tf.io.FixedLenFeature([], tf.float32),
    'y': tf.io.FixedLenFeature([], tf.float32)
    }
    
    dataset = tf.data.TFRecordDataset(example_five_times_table)
    dataset = dataset.map(lambda e : tf.io.parse_example(e, RAW_DATA_TRAIN_SPEC))
    dataset = dataset.map(lambda t : (t['x'], t['y']))
    dataset = dataset.batch(100)
    dataset = dataset.repeat()
    
    model.fit(dataset, epochs=5000, steps_per_epoch=1, verbose=0)
    
    
    
    <keras.callbacks.History at 0x7f6960074c70>
    

### Save the model

This step shows how to save your model.
    
    
    RAW_DATA_PREDICT_SPEC = {
    'x': tf.io.FixedLenFeature([], tf.float32),
    }
    
    # tf.function compiles the function into a callable TensorFlow graph.
    # RunInference relies on calling a TensorFlow graph as a model.
    # Note: Use the input signature type tf.string, because it's supported by
    # tfx-bsl ModelHandlers.
    @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string , name='examples')])
    def serve_tf_examples_fn(serialized_tf_examples):
      """Returns the output to be used in the serving signature."""
      features = tf.io.parse_example(serialized_tf_examples, RAW_DATA_PREDICT_SPEC)
      return model(features, training=False)
    
    signature = {'serving_default': serve_tf_examples_fn}
    
    # Signatures define the input and output types for a computation. The optional
    # save signatures argument controls which methods in obj are available to
    # programs that consume SavedModels, such as serving APIs.
    # See https://www.tensorflow.org/api_docs/python/tf/saved_model/save
    tf.keras.models.save_model(model, save_model_dir_multiply, signatures=signature)
    

## Run the pipeline

Use the following code to run the pipeline.

  * `FormatOutput` demonstrates how to extract values from the output protos.
  * `CreateModelHandler` demonstrates the model handler that needs to be passed into the Apache Beam RunInference API.


    
    
    from tfx_bsl.public.beam.run_inference import CreateModelHandler
    
    class FormatOutput(beam.DoFn):
        def process(self, element: prediction_log_pb2.PredictionLog):
            predict_log = element.predict_log
            input_value = tf.train.Example.FromString(predict_log.request.inputs['examples'].string_val[0])
            input_float_value = input_value.features.feature['x'].float_list.value[0]
            output_value = predict_log.response.outputs
            output_float_value = output_value['output_0'].float_val[0]
            yield (f"example is {input_float_value:.2f} prediction is {output_float_value:.2f}")
    
    tfexample_beam_record = tfx_bsl.public.tfxio.TFExampleRecord(file_pattern=predict_values_five_times_table)
    saved_model_spec = model_spec_pb2.SavedModelSpec(model_path=save_model_dir_multiply)
    inference_spec_type = model_spec_pb2.InferenceSpecType(saved_model_spec=saved_model_spec)
    model_handler = CreateModelHandler(inference_spec_type)
    with beam.Pipeline() as p:
        _ = (p | tfexample_beam_record.RawRecordBeamSource()
               | RunInference(model_handler)
               | beam.ParDo(FormatOutput())
               | beam.Map(print)
            )
    
    
    
    WARNING:apache_beam.runners.interactive.interactive_environment:Dependencies required for Interactive Beam PCollection visualization are not available, please use: `pip install apache-beam[interactive]` to install necessary dependencies to enable all data visualization features.
    WARNING:tensorflow:From /usr/local/lib/python3.9/dist-packages/tfx_bsl/beam/run_inference.py:615: load (from tensorflow.python.saved_model.loader_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    Use `tf.saved_model.load` instead.
    WARNING:apache_beam.io.tfrecordio:Couldn't find python-snappy so the implementation of _TFRecordUtil._masked_crc32c is not as fast as it could be.
    example is 20.00 prediction is 104.36
    example is 40.00 prediction is 202.62
    example is 60.00 prediction is 300.87
    example is 90.00 prediction is 448.26
    

## Use `KeyedModelHandler` with `tfx-bsl`

By default, the `ModelHandler` does not expect a key.

  * If you know that keys are associated with your examples, use `beam.KeyedModelHandler` to wrap the model handler.
  * If you don't know whether keys are associated with your examples, use `beam.MaybeKeyedModelHandler`.

In addition to demonstrating how to use a keyed model handler, this step demonstrates how to use `tfx-bsl` examples.
    
    
    from apache_beam.ml.inference.base import KeyedModelHandler
    from google.protobuf import text_format
    import tensorflow as tf
    
    class FormatOutputKeyed(FormatOutput):
      # To simplify, inherit from FormatOutput.
      def process(self, tuple_in: Tuple):
        key, element = tuple_in
        output = super().process(element)
        yield ' : '.join([key, next(output)])
    
    def make_example(num):
      # Return keyed values in the form of (key num, example).
      key = f'key {num}'
      tf_proto = text_format.Parse(
        """
        features {
          feature {key: "x" value { float_list { value: %f } } }
        }
        """% num, tf.train.Example())
      return (key, tf_proto)
    
    # Make a list of examples of type tf.train.Example.
    examples = [
        make_example(5.0),
        make_example(50.0),
        make_example(40.0),
        make_example(100.0)
    ]
    
    tfexample_beam_record = tfx_bsl.public.tfxio.TFExampleRecord(file_pattern=predict_values_five_times_table)
    saved_model_spec = model_spec_pb2.SavedModelSpec(model_path=save_model_dir_multiply)
    inference_spec_type = model_spec_pb2.InferenceSpecType(saved_model_spec=saved_model_spec)
    keyed_model_handler = KeyedModelHandler(CreateModelHandler(inference_spec_type))
    with beam.Pipeline() as p:
        _ = (p | 'CreateExamples' >> beam.Create(examples)
               | RunInference(keyed_model_handler)
               | beam.ParDo(FormatOutputKeyed())
               | beam.Map(print)
            )
    
    
    
    key 5.0 : example is 5.00 prediction is 30.67
    key 50.0 : example is 50.00 prediction is 251.75
    key 40.0 : example is 40.00 prediction is 202.62
    key 100.0 : example is 100.00 prediction is 497.38
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
