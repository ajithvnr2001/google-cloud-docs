---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_gemma/
title: Run inference with a Gemma open model \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:51.954068+00:00
---

# Run inference with a Gemma open model  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_gemma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Run inference with a Gemma open model Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_gemma.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_gemma.ipynb) Gemma is a family of lightweight, state-of-the art open models built from research and technology used to create the Gemini models. You can use Gemma models in your Apache Beam inference pipelines with the `RunInference` transform. This notebook demonstrates how to load the preconfigured Gemma 2B model and then use it in your Apache Beam inference pipeline. The pipeline runs examples by using a built-in model handler and a custom inference function. For more information about using RunInference, see [Get started with AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) in the Apache Beam documentation.

## Requirements

Serving and using Gemma models requires a substantial amount of RAM. To run this example, we recommend that you use a notebook instance with GPUs. At a mimumum, use a machine that has the T4 GPU type. This configuration provides sufficient memory for running inference with a saved model. **Note:** When you complete this workflow in Google Colab, if you don't have Colab Enterprise, you might run into resource constraints.

## Before you begin

  * To use a fine-tuned version of the model, follow the steps in [Gemma fine-tuning](https://ai.google.dev/gemma/docs/lora_tuning).
  * For testing this workflow, we recommend using the instruction tuned model in your Apache Beam workflow. For example, if you use the Gemma 2B model in your pipeline, when you load the model, change the `GemmaCausalLM.from_preset()` argument from `gemma_2b_en` to `gemma_instruct_2b_en`. For more information, see [Create a model](https://ai.google.dev/gemma/docs/get_started#create_a_model) in "Get started with Gemma using KerasNLP". For a list of models, see [Gemma models](https://www.kaggle.com/models/keras/gemma).



## Install Dependencies

To use the `RunInference` transform with the built-in TensorFlow model handler, install Apache Beam version 2.46.0 or later. The model class is contained in the Keras natural language processing (NLP) package versions 0.8.0 and later.
    
    
    !pip install -q -U protobuf
    !pip install -q -U apache_beam[interactive,gcp]
    !pip install -q -U keras_nlp>=0.8.0
    !pip install -q -U keras>3
    
    # To use the newly installed versions, restart the runtime.
    exit()
    

## Authenticate with Kaggle

The pipeline defined here automatically pulls the model weights from Kaggle. First, accept the terms of use for Gemma models on the Keras [Gemma](https://www.kaggle.com/models/keras/gemma) page. Next, generate an API token by following the instructions in [How to use Kaggle](https://www.kaggle.com/docs/api). Provide your username and token.
    
    
    import kagglehub
    
    kagglehub.login()
    
    
    
    VBox(children=(HTML(value='<center> <img\nsrc=https://www.kaggle.com/static/images/site-logo.png\nalt=\'Kaggle…
    Kaggle credentials set.
    Kaggle credentials successfully validated.
    

## Import dependencies and provide a model preset

Use the following code to import dependencies. Replace the value for the `model_preset` variable with the name of the Gemma preset to use. For example, to use the default English weights, use the value `gemma_2b_en`. This example uses the instruction-tuned preset `gemma_instruct_2b_en`. Optionally, to run the model at half-precision and reduce GPU memory usage, use Keras.
    
    
    import numpy as np
    
    import apache_beam as beam
    import keras_nlp
    import keras
    from apache_beam.ml.inference import utils
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.tensorflow_inference import TFModelHandlerNumpy
    from apache_beam.options.pipeline_options import PipelineOptions
    
    model_preset = "gemma_instruct_2b_en"
    # Optionally set the model to run at half-precision
    # (recommended for smaller GPUs)
    keras.config.set_floatx("bfloat16")
    

## Run the pipeline

To run the pipeline, use a custom model handler.

### Provide a custom model handler

To simplify model loading, this notebook defines a custom model handler that loads the model by pulling the model weights directly from Kaggle presets. To customize the behavior of the handler, implement `load_model`, `validate_inference_args`, and `share_model_across_processes`. The Keras implementation of the Gemma models has a `generate` method that generates text based on a prompt. To route the prompts properly, use this function in the `run_inference` method.
    
    
    # To load the model and perform the inference, define `GemmaModelHandler`.
    
    from apache_beam.ml.inference.base import ModelHandler
    from apache_beam.ml.inference.base import PredictionResult
    from typing import Any
    from typing import Dict
    from typing import Iterable
    from typing import Optional
    from typing import Sequence
    from keras_nlp.src.models.gemma.gemma_causal_lm import GemmaCausalLM
    
    class GemmaModelHandler(ModelHandler[str,
                                         PredictionResult,GemmaCausalLM
                                         ]):
        def __init__(
            self,
            model_name: str = "gemma_2b_en",
        ):
            """ Implementation of the ModelHandler interface for Gemma using text as input.
    
            Example Usage::
    
              pcoll | RunInference(GemmaModelHandler())
    
            Args:
              model_name: The Gemma model preset. Default is gemma_2b_instruct_en.
            """
            self._model_name = model_name
            self._env_vars = {}
        def share_model_across_processes(self)  -> bool:
            return True
    
        def load_model(self) -> GemmaCausalLM:
            """Loads and initializes a model for processing."""
            return keras_nlp.models.GemmaCausalLM.from_preset(self._model_name)
    
        def validate_inference_args(self, inference_args: Optional[Dict[str, Any]]):
            """Validates the inference arguments."""
            for key, value in inference_args.items():
                if key != "max_length":
                    raise ValueError(f"Invalid inference argument: {key}")
    
        def run_inference(
            self,
            batch: Sequence[str],
            model: GemmaCausalLM,
            inference_args: Optional[Dict[str, Any]] = None
        ) -> Iterable[PredictionResult]:
            """Runs inferences on a batch of text strings.
    
            Args:
              batch: A sequence of examples as text strings.
              model:
              inference_args: Any additional arguments for an inference.
    
            Returns:
              An Iterable of type PredictionResult.
            """
            # Loop each text string, and use a tuple to store the inference results.
            predictions = []
            for one_text in batch:
                result = model.generate(one_text, **inference_args)
                predictions.append(result)
            return utils._convert_to_result(batch, predictions, self._model_name)
    

### Execute the pipeline

Use the following code to run the pipeline. The code includes the path to the trained TensorFlow model. This cell can take a few minutes to run, because the model is downloaded and then loaded onto the worker. This delay is a one-time cost per worker. The `max_length` argument determines how long the response from Gemma is. The response includes your input, so the response length includes your input and the output. For longer prompts, use a larger maximum length. Longer lengths require more time to generate. **Note:** When the pipeline completes, the memory used to load the model in the pipeline isn't freed automatically. As a result, if you run the pipeline more than once, your pipeline might fail with an out of memory (OOM) error.
    
    
    class FormatOutput(beam.DoFn):
      def process(self, element, *args, **kwargs):
        yield "Input: {input}, Output: {output}".format(input=element.example, output=element.inference)
    
    # Instantiate a NumPy array of string prompts for the model.
    examples = np.array(["Tell me the sentiment of the phrase 'I like pizza': "])
    # Specify the model handler, providing a path and the custom inference function.
    model_handler = GemmaModelHandler(model_preset)
    with beam.Pipeline() as p:
      _ = (p | beam.Create(examples) # Create a PCollection of the prompts.
             | RunInference(model_handler, inference_args={'max_length': 32}) # Send the prompts to the model and get responses.
             | beam.ParDo(FormatOutput()) # Format the output.
             | beam.Map(print) # Print the formatted output.
      )
    
    
    
    WARNING:apache_beam.runners.interactive.interactive_environment:Dependencies required for Interactive Beam PCollection visualization are not available, please use: `pip install apache-beam[interactive]` to install necessary dependencies to enable all data visualization features.
    Input: Tell me the sentiment of the phrase 'I like pizza': , Output: Tell me the sentiment of the phrase 'I like pizza': 
    
    The sentiment of the phrase "I like pizza" is positive. It expresses a personal
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
