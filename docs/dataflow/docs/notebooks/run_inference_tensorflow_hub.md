---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow_hub/
title: RunInference with Sentence-T5 (ST5) model \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:12:26.381573+00:00
---

# RunInference with Sentence-T5 (ST5) model  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_tensorflow_hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  RunInference with Sentence-T5 (ST5) model Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow_hub.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_tensorflow_hub.ipynb) This example demonstrates the use of the RunInference transform with the pre-trained [ST5 text encoder model](https://tfhub.dev/google/sentence-t5/st5-base/1) from TensorFlow Hub. The transform runs locally using the [Interactive Runner](https://beam.apache.org/releases/pydoc/2.11.0/apache_beam.runners.interactive.interactive_runner.html).

## Download and install the dependencies
    
    
    pip install apache_beam[gcp,interactive]==2.41.0
    pip install tensorflow==2.10.0
    pip install tensorflow_text==2.10.0
    pip install keras==2.10.0
    pip install tfx_bsl==1.10.0
    pip install pillow==8.4.0
    
    
    import tensorflow as tf
    import tensorflow_hub as hub
    import tensorflow_text
    
    from tensorflow import keras
    
    import apache_beam as beam
    import apache_beam.runners.interactive.interactive_beam as ib
    
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.base import ModelHandler
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    
    from tfx_bsl.public.beam.run_inference import CreateModelHandler
    from tfx_bsl.public.proto import model_spec_pb2
    

## Authenticate with Google Cloud

This notebook relies on saving the model to Google Cloud. To use your Google Cloud account, authenticate this notebook.
    
    
    from google.colab import auth
    auth.authenticate_user()
    

## Create a Keras Model from TensorFlow Hub image

Replace `GCS_BUCKET` with the name of your bucket. Your model will be saved in `MODEL_EXPORT_DIR`.
    
    
    GCS_BUCKET = '<GCS Bucket>'
    
    MODEL_EXPORT_DIR = f'gs://{GCS_BUCKET}/st5-base/1'
    
    
    
    inp = tf.keras.layers.Input(shape=[], dtype=tf.string, name='input')
    hub_url = "https://tfhub.dev/google/sentence-t5/st5-base/1"
    imported = hub.KerasLayer(hub_url)
    outp = imported(inp)
    model = tf.keras.Model(inp, outp)
    
    
    
    # The ST5 model returns a 768-dimensional vector for an English text input.
    model.summary()
    
    
    
    Model: "model"
    _________________________________________________________________
     Layer (type)                Output Shape              Param #   
    =================================================================
     input (InputLayer)          [(None,)]                 0         
                                                                     
     keras_layer (KerasLayer)    [(None, 768)]             0         
                                                                     
    =================================================================
    Total params: 0
    Trainable params: 0
    Non-trainable params: 0
    _________________________________________________________________
    

## Save the model

Save the model with a TF function definition for RunInference.
    
    
    RAW_DATA_PREDICT_SPEC = {
        'input': tf.io.FixedLenFeature([], tf.string),
    }
    
    @tf.function(input_signature=[tf.TensorSpec(shape=[None], dtype=tf.string)])
    def call(serialized_examples):
        features = tf.io.parse_example(serialized_examples, RAW_DATA_PREDICT_SPEC)
        return model(features)
    
    tf.saved_model.save(model, MODEL_EXPORT_DIR, signatures={'serving_default': call})
    

## Create and test the RunInference pipeline locally

Use TFX_BSL's [CreateModelHandler](https://www.tensorflow.org/tfx/tfx_bsl/api_docs/python/tfx_bsl/public/beam/run_inference/CreateModelHandler) function for RunInference with TensorFlow models.
    
    
    # Creates a TensorFlow example to feed to the model handler.
    class ExampleProcessor:
        def create_example(self, feature: tf.string):
            return tf.train.Example(
                features=tf.train.Features(
                      feature={'input' : self.create_feature(feature)})
                )
    
        def create_feature(self, element: tf.string):
            return tf.train.Feature(bytes_list=tf.train.BytesList(value=[element.encode()], ))
    
    
    
    saved_model_spec = model_spec_pb2.SavedModelSpec(model_path=MODEL_EXPORT_DIR)
    inference_spec_type = model_spec_pb2.InferenceSpecType(saved_model_spec=saved_model_spec)
    model_handler = CreateModelHandler(inference_spec_type)
    
    questions = [
        'what is the official slogan for the 2018 winter olympics?',
    ]
    
    pipeline = beam.Pipeline(InteractiveRunner())
    
    inference = (pipeline | 'CreateSentences' >> beam.Create(questions)
                   | 'Convert input to Tensor' >> beam.Map(lambda x: ExampleProcessor().create_example(x))
                   | 'RunInference with T5' >> RunInference(model_handler))
    
    
    
    ib.show(inference)
    
    
    
    WARNING:tensorflow:From /usr/local/lib/python3.8/dist-packages/tfx_bsl/beam/run_inference.py:615: load (from tensorflow.python.saved_model.loader_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.loader.load or tf.compat.v1.saved_model.load. There will be a new function for importing SavedModels in Tensorflow 2.0.
    2022-12-06 09:30:47.084208: I tensorflow/compiler/mlir/mlir_graph_optimization_pass.cc:354] MLIR V1 optimization pass is not enabled
    2022-12-06 09:30:54.471173: I tensorflow/compiler/xla/service/service.cc:173] XLA service 0x4a3e0a00 initialized for platform Host (this does not guarantee that XLA will be used). Devices:
    2022-12-06 09:30:54.471244: I tensorflow/compiler/xla/service/service.cc:181]   StreamExecutor device (0): Host, Default Version
    2022-12-06 09:30:54.537285: I tensorflow/compiler/mlir/tensorflow/utils/dump_mlir_util.cc:268] disabling MLIR crash reproducer, set env var `MLIR_CRASH_REPRODUCER_DIRECTORY` to enable.
    2022-12-06 09:31:00.441479: I tensorflow/compiler/jit/xla_compilation_cache.cc:476] Compiled cluster using XLA!  This line is logged at most once for the lifetime of the process.
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
