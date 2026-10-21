---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_with_tensorflow_hub/
title: Apache Beam RunInference with TensorFlow and TensorFlow Hub \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:50.318634+00:00
---

# Apache Beam RunInference with TensorFlow and TensorFlow Hub  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_with_tensorflow_hub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Apache Beam RunInference with TensorFlow and TensorFlow Hub Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_with_tensorflow_hub.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_with_tensorflow_hub.ipynb) This notebook shows how to use the Apache Beam [RunInference](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference) transform for [TensorFlow](https://www.tensorflow.org/) with a trained model from [TensorFlow Hub](https://www.tensorflow.org/hub). Apache Beam includes built-in support for two TensorFlow model handlers: [TFModelHandlerNumpy](https://github.com/apache/beam/blob/ca0787642a6b3804a742326147281c99ae8d08d2/sdks/python/apache_beam/ml/inference/tensorflow_inference.py#L91) and [TFModelHandlerTensor](https://github.com/apache/beam/blob/ca0787642a6b3804a742326147281c99ae8d08d2/sdks/python/apache_beam/ml/inference/tensorflow_inference.py#L184).

  * Use `TFModelHandlerNumpy` to run inference on models that expect a NumPy array as an input.
  * Use `TFModelHandlerTensor` to run inference on models expecting a tensor as an input.

For more information about using RunInference, see [Get started with AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) in the Apache Beam documentation. **Note:** The image used for prediction is licensed in CC-BY. The creator is listed in the [LICENSE.txt](https://storage.googleapis.com/apache-beam-samples/image_captioning/LICENSE.txt) file.

## Before you begin

First, import `tensorflow`. To use RunInference with the TensorFlow model handler, install Apache Beam version 2.46 or later.
    
    
    pip install tensorflow
    pip install apache_beam[interactive]==2.46.0

## Use TensorFlow Hub's trained model URL

To use TensorFlow Hub's trained model URL, pass the model URL to the `model_uri` field of `TFModelHandler` class. **Note:** Only models that you save in the [TF2 format](https://www.tensorflow.org/tutorials/keras/save_and_load#save_the_entire_model) are compatible with `TFModelHandler`. To see TF2 models, go to the [TF2 section of the TensorFlow Hub](https://tfhub.dev/s?subtype=module,placeholder&tf-version=tf2).
    
    
    import tensorflow as tf
    import tensorflow_hub as hub
    import apache_beam as beam
    
    
    
    # URL of the trained model from TensorFlow Hub
    CLASSIFIER_URL ="https://tfhub.dev/google/tf2-preview/mobilenet_v2/classification/4"
    
    
    
    import numpy as np
    import PIL.Image as Image
    
    IMAGE_RES = 224
    img = tf.keras.utils.get_file(origin='https://storage.googleapis.com/apache-beam-samples/image_captioning/Cat-with-beanie.jpg')
    img = Image.open(img).resize((IMAGE_RES, IMAGE_RES))
    img
    
    
    
    Downloading data from https://storage.googleapis.com/apache-beam-samples/image_captioning/Cat-with-beanie.jpg
    1812110/1812110 [==============================] - 0s 0us/step
    

![png](https://docs.cloud.google.com/static/dataflow/docs/notebooks/run_inference_with_tensorflow_hub_files/output_q23ip_HkwL3G_1.png)
    
    
    # Convert the input image to the type and dimensions required by the model.
    img = np.array(img)/255.0
    img_tensor = tf.cast(tf.convert_to_tensor(img[...]), dtype=tf.float32)
    
    
    
    from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerTensor
    from apache_beam.ml.inference.base import PredictionResult
    from apache_beam.ml.inference.base import RunInference
    from typing import Iterable
    
    model_handler = TFModelHandlerTensor(model_uri=CLASSIFIER_URL)
    
    class PostProcessor(beam.DoFn):
      """Process the PredictionResult to get the predicted label.
      Returns predicted label.
      """
      def setup(self):
        labels_path = tf.keras.utils.get_file(
            'ImageNetLabels.txt',
            'https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt'
        )
        self._imagenet_labels = np.array(open(labels_path).read().splitlines())
    
      def process(self, element: PredictionResult) -> Iterable[str]:
        predicted_class = np.argmax(element.inference)
        predicted_class_name = self._imagenet_labels[predicted_class]
        yield "Predicted Label: {}".format(predicted_class_name.title())
    
    with beam.Pipeline() as p:
      _ = (p
        | "Create PCollection" >> beam.Create([img_tensor])
        | "Perform inference" >> RunInference(model_handler)
        | "Post Processing" >> beam.ParDo(PostProcessor())
        | "Print" >> beam.Map(print))
    
    
    
    Predicted Label: Tiger Cat
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
