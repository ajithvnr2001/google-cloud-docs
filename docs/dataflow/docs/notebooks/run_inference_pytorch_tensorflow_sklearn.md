---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_pytorch_tensorflow_sklearn/
title: Use RunInference in Apache Beam \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:23:22.971932+00:00
---

# Use RunInference in Apache Beam  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_pytorch_tensorflow_sklearn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Use RunInference in Apache Beam Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_pytorch_tensorflow_sklearn.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_pytorch_tensorflow_sklearn.ipynb) You can use Apache Beam versions 2.40.0 and later with the [RunInference API](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference) for local and remote inference with batch and streaming pipelines. The RunInference API leverages Apache Beam concepts, such as the `BatchElements` transform and the `Shared` class, to support models in your pipelines that create transforms optimized for machine learning inference. For more information about the RunInference API, see [About Beam ML](https://beam.apache.org/documentation/ml/about-ml) in the Apache Beam documentation. This example demonstrates how to use the RunInference API with three popular ML frameworks: PyTorch, TensorFlow, and scikit-learn. The three pipelines use a text classification model for generating predictions. Follow these steps to build a pipeline:

  * Read the images.
  * If needed, preprocess the text.
  * Run inference with the PyTorch, TensorFlow, or Scikit-learn model.
  * If needed, postprocess the output.



## RunInference with a PyTorch model

This section demonstrates how to use the RunInference API with a PyTorch model.

### Install dependencies

First, download and install the dependencies.
    
    
    pip install --upgrade pip
    pip install apache_beam[interactive,gcp]>=2.40.0
    pip install transformers
    pip install google-api-core==1.32

### Install the model

This example uses a pretrained text classification model, [distilbert-base-uncased-finetuned-sst-2-english](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english?text=I+like+you.+I+love+you). This model is a checkpoint of `DistilBERT-base-uncased`, fine-tuned on the SST-2 dataset.
    
    
     git lfs install
     git clone https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english
     ls
    
    
    Error: Failed to call git rev-parse --git-dir --show-toplevel: "fatal: not a git repository (or any of the parent directories): .git\n"
    Git LFS initialized.
    fatal: destination path 'distilbert-base-uncased-finetuned-sst-2-english' already exists and is not an empty directory.
    '=2.40.0'   distilbert-base-uncased-finetuned-sst-2-english   sample_data
    

### Install helper functions

The model also uses helper functions.
    
    
    from collections import defaultdict
    
    import torch
    from transformers import DistilBertForSequenceClassification, DistilBertTokenizer, DistilBertConfig
    
    import apache_beam as beam
    from apache_beam.ml.inference import RunInference
    from apache_beam.ml.inference.base import PredictionResult, KeyedModelHandler
    from apache_beam.ml.inference.pytorch_inference import PytorchModelHandlerKeyedTensor
    
    
    class HuggingFaceStripBatchingWrapper(DistilBertForSequenceClassification):
      """Wrapper around HugginFace model because RunInference requires a batch
      as a list of dicts instead of a dict of lists. Another workaround can be found
      here where they disable batching instead.
      https://github.com/apache/beam/blob/master/sdks/python/apache_beam/examples/inference/pytorch_language_modeling.py"""
      def forward(self, **kwargs):
        output = super().forward(**kwargs)
        return [dict(zip(output, v)) for v in zip(*output.values())]
    
    
    
    class Tokenize(beam.DoFn):
      def __init__(self, model_name: str):
        self._model_name = model_name
    
      def setup(self):
        self._tokenizer = DistilBertTokenizer.from_pretrained(self._model_name)
    
      def process(self, text_input: str):
        # Pad the token tensors to max length to make sure that all of the tensors
        # are of the same length and stack-able by the RunInference API. Normally, you would batch first
        # then tokenize the batch, padding each tensor the max length in the batch.
        # See: https://beam.apache.org/documentation/ml/about-ml/#unable-to-batch-tensor-elements
        tokens = self._tokenizer(text_input, return_tensors='pt', padding='max_length', max_length=512)
        # Squeeze because tokenization adds an extra dimension, which is empty,
        # in this case because we tokenize one element at a time.
        tokens = {key: torch.squeeze(val) for key, val in tokens.items()}
        return [(text_input, tokens)]
    
    class PostProcessor(beam.DoFn):
      def process(self, tuple_):
        text_input, prediction_result = tuple_
        softmax = torch.nn.Softmax(dim=-1)(prediction_result.inference['logits']).detach().numpy()
        return [{"input": text_input, "softmax": softmax}]
    

### Run the pipeline

This section demonstrates how to create and run the RunInference pipeline.
    
    
    inputs = [
        "This is the worst food I have ever eaten",
        "In my soul and in my heart, I’m convinced I’m wrong!",
        "Be with me always—take any form—drive me mad! only do not leave me in this abyss, where I cannot find you!",
        "Do I want to live? Would you like to live with your soul in the grave?",
        "Honest people don’t hide their deeds.",
        "Nelly, I am Heathcliff!  He’s always, always in my mind: not as a pleasure, any more than I am always a pleasure to myself, but as my own being.",
    ]
    
    
    
    model_handler = PytorchModelHandlerKeyedTensor(
        state_dict_path="./distilbert-base-uncased-finetuned-sst-2-english/pytorch_model.bin",
        model_class=HuggingFaceStripBatchingWrapper,
        model_params={"config": DistilBertConfig.from_pretrained("./distilbert-base-uncased-finetuned-sst-2-english/config.json")},
        device='cuda:0')
    
    keyed_model_handler = KeyedModelHandler(model_handler)
    
    with beam.Pipeline() as pipeline:
      _ = (pipeline | "Create inputs" >> beam.Create(inputs)
                    | "Tokenize" >> beam.ParDo(Tokenize("distilbert-base-uncased-finetuned-sst-2-english"))
                    | "Inference" >> RunInference(model_handler=keyed_model_handler)
                    | "Postprocess" >> beam.ParDo(PostProcessor())
                    | "Print" >> beam.Map(lambda x: print(f"Input: {x['input']} -> negative={100 * x['softmax'][0]:.4f}%/positive={100 * x['softmax'][1]:.4f}%"))
      )
    
    
    
    /usr/local/lib/python3.7/dist-packages/ipykernel_launcher.py:10: FutureWarning: PytorchModelHandlerKeyedTensor is experimental. No backwards-compatibility guarantees.
      # Remove the CWD from sys.path while we load stuff.
    WARNING:apache_beam.runners.interactive.interactive_environment:Dependencies required for Interactive Beam PCollection visualization are not available, please use: `pip install apache-beam[interactive]` to install necessary dependencies to enable all data visualization features.
    /usr/local/lib/python3.7/dist-packages/dill/_dill.py:472: FutureWarning: PytorchModelHandlerKeyedTensor is experimental. No backwards-compatibility guarantees.
      obj = StockUnpickler.load(self)
    /usr/local/lib/python3.7/dist-packages/dill/_dill.py:472: FutureWarning: PytorchModelHandlerKeyedTensor is experimental. No backwards-compatibility guarantees.
      obj = StockUnpickler.load(self)
    Input: This is the worst food I have ever eaten -> negative=99.9777%/positive=0.0223%
    Input: In my soul and in my heart, I’m convinced I’m wrong! -> negative=1.6313%/positive=98.3687%
    Input: Be with me always—take any form—drive me mad! only do not leave me in this abyss, where I cannot find you! -> negative=62.1188%/positive=37.8812%
    Input: Do I want to live? Would you like to live with your soul in the grave? -> negative=73.6841%/positive=26.3159%
    Input: Honest people don’t hide their deeds. -> negative=0.2377%/positive=99.7623%
    Input: Nelly, I am Heathcliff!  He’s always, always in my mind: not as a pleasure, any more than I am always a pleasure to myself, but as my own being. -> negative=0.0672%/positive=99.9328%
    

## RunInference with a TensorFlow model

This section demonstrates how to use the RunInference API with a TensorFlow model. **Note:** Tensorflow models are supported through `tfx-bsl`.

### Install dependencies

First, download and install the dependencies.
    
    
    pip install --upgrade pip
    pip install google-api-core==1.32
    pip install apache_beam[interactive,gcp]==2.41.0
    pip install tensorflow==2.8
    pip install tfx_bsl
    pip install tensorflow-text==2.8.1
    
    
    import numpy as np
    import tensorflow as tf
    import tensorflow_text as text
    from scipy.special import expit
    
    import apache_beam as beam
    import tfx_bsl
    from tfx_bsl.public.beam import RunInference
    from tfx_bsl.public import tfxio
    from tfx_bsl.public.proto import model_spec_pb2
    from tfx_bsl.public.tfxio import TFExampleRecord
    from tensorflow_serving.apis import prediction_log_pb2
    

### Install the model

Download a pretrained binary classifier to perform sentiment analysis on an IMDB dataset from Google Cloud Storage. This model was trained by following this [TensorFlow text classification tutorial](https://www.tensorflow.org/tutorials/keras/text_classification).
    
    
    model_dir = "gs://apache-beam-testing-ml-examples/imdb_bert"
    

### Install helper functions

The model also uses helper functions.
    
    
    class ExampleProcessor:
      """
      Process the raw text input to a format suitable for RunInference.
      TensorFlow model handler expects a serialized tf.Example as input
      """
      def create_example(self, feature):
        return tf.train.Example(
            features=tf.train.Features(
                  feature={'x' : self.create_feature(feature)})
            )
    
      def create_feature(self, element):
        return tf.train.Feature(bytes_list=tf.train.BytesList(value=[element]))
    
    class PredictionProcessor(beam.DoFn):
       """
       Process the RunInference output to return the input text and the softmax probability
       """
       def process(
               self,
               element: prediction_log_pb2.PredictionLog):
           predict_log = element.predict_log
           input_value = tf.train.Example.FromString(predict_log.request.inputs['text'].string_val[0])
           output_value = predict_log.response.outputs
          #  print(output_value)
           yield (f"input is [{input_value.features.feature['x'].bytes_list.value}] output is {expit(output_value['classifier'].float_val)}")
    

### Prepare the input

This section demonstrates how to prepare the input for your model.
    
    
    inputs = np.array([
        b"this is such an amazing movie",
        b"The movie was great",
        b"The movie was okish",
        b"The movie was terrible"
    ])
    
    
    
    input_strings_file = 'input_strings.tfrecord'
    
    # Because RunInference is expecting a serialized tf.example as an input, preprocess the input.
    # Write the processed input to a file. 
    # You can also do this preprocessing as a pipeline step by using beam.Map().
    
    with tf.io.TFRecordWriter(input_strings_file) as writer:
     for i in inputs:
       example = ExampleProcessor().create_example(feature=i)
       writer.write(example.SerializeToString())
    

### Run the pipeline

This section demonstrates how to create and run the RunInference pipeline.
    
    
    saved_model_spec = model_spec_pb2.SavedModelSpec(model_path=model_dir)
    inference_spec_type = model_spec_pb2.InferenceSpecType(saved_model_spec=saved_model_spec)
    
    # A Beam I/O that reads a file of serialized tf.Examples
    tfexample_beam_record = TFExampleRecord(file_pattern='input_strings.tfrecord')
    
    with beam.Pipeline() as pipeline:
        _ = ( pipeline | "Create Input PCollection" >> tfexample_beam_record.RawRecordBeamSource()
                       | "Do Inference" >> RunInference(model_spec_pb2.InferenceSpecType(
                                      saved_model_spec=model_spec_pb2.SavedModelSpec(model_path=model_dir)))
                       | "Post Process" >> beam.ParDo(PredictionProcessor())
                       | beam.Map(print)
            )
    
    
    
    WARNING:tensorflow:From /usr/local/lib/python3.7/dist-packages/tfx_bsl/beam/run_inference.py:615: load (from tensorflow.python.saved_model.loader_impl) is deprecated and will be removed in a future version.
    Instructions for updating:
    This function will only be available through the v1 compatibility library as tf.compat.v1.saved_model.loader.load or tf.compat.v1.saved_model.load. There will be a new function for importing SavedModels in Tensorflow 2.0.
    WARNING:apache_beam.io.tfrecordio:Couldn't find python-snappy so the implementation of _TFRecordUtil._masked_crc32c is not as fast as it could be.
    input is [[b'this is such an amazing movie']] output is [0.99906057]
    input is [[b'The movie was great']] output is [0.99307914]
    input is [[b'The movie was okish']] output is [0.03274685]
    input is [[b'The movie was terrible']] output is [0.00680008]
    

## RunInference with scikit-learn

This section demonstrates how to use the RunInference API with scikit-learn.

### Install dependencies

First, download and install the dependencies.
    
    
    pip install --upgrade pip
    pip install google-api-core==1.32
    pip install apache_beam[interactive,gcp]==2.41.0
    
    
    import pickle
    
    import apache_beam as beam
    from apache_beam.ml.inference import RunInference
    from apache_beam.ml.inference.sklearn_inference import SklearnModelHandlerNumpy, ModelFileType
    

### Install the model

To classify movie reviews as either positive or negative, train and save a sentiment analysis pipeline about movie reviews. This model was trained by following this [scikit-learn tutorial](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html#exercise-2-sentiment-analysis-on-movie-reviews)
    
    
    model_dir = "gs://apache-beam-testing-ml-examples/sklearn-text-classification/sklearn_sentiment_analysis_pipeline.pkl"
    

### Run the pipeline

This section demonstrates how to create and run the RunInference pipeline.
    
    
    inputs = [
        "In my soul and in my heart, I’m convinced I’m wrong!",
        "Be with me always—take any form—drive me mad! only do not leave me in this abyss, where I cannot find you!",
        "Do I want to live? Would you like to live with your soul in the grave?",
        "Honest people don’t hide their deeds.",
        "Nelly, I am Heathcliff!  He’s always, always in my mind: not as a pleasure, any more than I am always a pleasure to myself, but as my own being.",
    ]
    
    
    
    # Choose an sklearn model handler based on the input data type:
    # 1. SklearnModelHandlerNumpy: For using numpy arrays as input.
    # 2. SklearnModelHandlerPandas: For using pandas dataframes as input.
    
    # The sklearn model handler supports loading two serialized formats:
    # 1. ModelFileType.PICKLE: For models saved using pickle.
    # 2. ModelFileType.JOBLIB: For models saved using Joblib.
    
    model_handler = SklearnModelHandlerNumpy(model_uri=model_dir, model_file_type=ModelFileType.PICKLE)
    
    with beam.Pipeline() as pipeline:
      _ = (pipeline | "Create inputs" >> beam.Create(inputs)
                    | "Inference" >> RunInference(model_handler=model_handler)
                    | "Print" >> beam.Map(lambda x: print(f"input: {x.example} -> {'positive' if x.inference == 0 else 'negative'}"))
      )
    
    
    
    input: In my soul and in my heart, I’m convinced I’m wrong! -> negative
    input: Be with me always—take any form—drive me mad! only do not leave me in this abyss, where I cannot find you! -> positive
    input: Do I want to live? Would you like to live with your soul in the grave? -> positive
    input: Honest people don’t hide their deeds. -> negative
    input: Nelly, I am Heathcliff!  He’s always, always in my mind: not as a pleasure, any more than I am always a pleasure to myself, but as my own being. -> negative
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
