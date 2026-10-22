---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/gemma/
title: Use Gemma open models with Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:40.980212+00:00
---

# Use Gemma open models with Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/gemma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Use Gemma open models with Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** NVIDIA T4 and P4 GPUs are deprecated on Dataflow and will reach End of Life on August 1, 2027. To avoid pipeline failures, migrate your workloads to the G2 (NVIDIA L4) VM family. For more information, see [Use the NVIDIA® L4 GPU type](https://docs.cloud.google.com/dataflow/docs/gpu/use-l4-gpus) and [Compute Engine feature deprecations](https://docs.cloud.google.com/compute/docs/deprecations).

Gemma is a family of lightweight, state-of-the art open models built from research and technology used to create the Gemini models. You can use Gemma models in your Apache Beam inference pipelines. The term _open weight_ means that a model's pretrained parameters, or weights, are released. Details such as the original dataset, model architecture, and training code aren't provided.

  * For a list of available models and the details about each model, see the [Gemma models overview](https://ai.google.dev/gemma/docs/).

  * To learn how to download and use models, see [Get started with Gemma using KerasNLP](https://ai.google.dev/gemma/docs/get_started).

  * To download a model, see [Gemma models](https://www.kaggle.com/models/keras/gemma).




## Use cases

You can use Gemma models with Dataflow for [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis). With Dataflow and the Gemma models, you can process events, such as customer reviews, as they arrive. Run the reviews through the model to analyze them, and then generate recommendations. By combining Gemma with Apache Beam, you can seamlessly complete this workflow.

## Support and limitations

Gemma open models are supported with Apache Beam and Dataflow with the following requirements:

  * Available for batch and streaming pipelines that use the Apache Beam Python SDK versions 2.46.0 and later.
  * Dataflow jobs must use [Runner v2](https://docs.cloud.google.com/dataflow/docs/portable-runner).
  * Dataflow jobs must use [GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support). For a list of GPU types supported with Dataflow, see [Availability](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support#availability). The L4 (G2) GPU type is recommended.
  * The model must be downloaded and saved in the `.keras` file format.
  * The [TensorFlow model handler](https://beam.apache.org/documentation/ml/about-ml/#tensorflow) is recommended but not required.



## Prerequisites

  * Access Gemma models through [Kaggle](https://www.kaggle.com/models/keras/gemma).
  * Complete the [consent form](https://www.kaggle.com/models/google/gemma/license/consent) and accept the terms and conditions.
  * Download the Gemma model. Save it in the `.keras` file format in a location that your Dataflow job can access, such as a Cloud Storage bucket. When you specify a value for the model path variable, use the path to this storage location.
  * To run your job on Dataflow, create a custom container image. This step makes it possible to run the pipeline with GPUs on the Dataflow service. 
    * To see a complete workflow that includes creating a Docker image, see [RunInference on Dataflow streaming with Gemma](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/gemma) in GitHub.
    * For more information about building the Docker image, see [Build a custom container image](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#custom-container) in "Run a pipeline with GPUs."
    * To push the container to Artifact Registry by using Docker, see the [Build and push the image](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#build_and_push_the_image) section in "Build custom container images for Dataflow."



## Use Gemma in your pipeline

To use a Gemma model in your Apache Beam pipeline, follow these steps.

  1. In your Apache Beam code, after you import your pipeline dependencies, include a path to your saved model:
         
         model_path = "MODEL_PATH"
         

Replace `MODEL_PATH` with the path where you saved the downloaded model. For example, if you save your model to a Cloud Storage bucket, the path has the format `gs://STORAGE_PATH/FILENAME.keras`.

  2. The Keras implementation of the Gemma models has a `generate()` method that generates text based on a prompt. To pass elements to the `generate()` method, use a custom inference function.
         
         def gemma_inference_function(model, batch, inference_args, model_id):
           vectorized_batch = np.stack(batch, axis=0)
           # The only inference_arg expected here is a max_length parameter to
           # determine how many words are included in the output.
           predictions = model.generate(vectorized_batch, **inference_args)
           return utils._convert_to_result(batch, predictions, model_id)
         

  3. Run your pipeline, specifying the path to the trained model. This example uses a TensorFlow model handler.
         
         class FormatOutput(beam.DoFn):
           def process(self, element, *args, **kwargs):
             yield "Input: {input}, Output: {output}".format(input=element.example, output=element.inference)
         
         # Instantiate a NumPy array of string prompts for the model.
         examples = np.array(["Tell me the sentiment of the phrase 'I like pizza': "])
         # Specify the model handler, providing a path and the custom inference function.
         model_handler = TFModelHandlerNumpy(model_path, inference_fn=gemma_inference_function)
         with beam.Pipeline() as p:
           _ = (p | beam.Create(examples) # Create a PCollection of the prompts.
                  | RunInference(model_handler, inference_args={'max_length': 32}) # Send the prompts to the model and get responses.
                  | beam.ParDo(FormatOutput()) # Format the output.
                  | beam.Map(print) # Print the formatted output.
           )
         




## What's next

  * [Create a Dataflow streaming pipeline that uses RunInference and Gemma](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/dataflow/gemma).
  * [Run inference with a Gemma open model in Google Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_gemma.ipynb) (requires Colab Enterprise).
  * [Run a pipeline with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).
  * [Tune your model](https://ai.google.dev/gemma/docs/lora_tuning).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
