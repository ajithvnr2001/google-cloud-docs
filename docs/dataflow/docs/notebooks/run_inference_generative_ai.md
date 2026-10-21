---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_generative_ai/
title: Use RunInference for Generative AI \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:50.380016+00:00
---

# Use RunInference for Generative AI  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_generative_ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Use RunInference for Generative AI Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_generative_ai.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_generative_ai.ipynb) This notebook shows how to use the Apache Beam [RunInference](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.RunInference) transform for generative AI tasks. It uses a large language model (LLM) from the [Hugging Face Model Hub](https://huggingface.co/models). This notebook demonstrates the following steps:

  * Load and save a model from the Hugging Face Model Hub.
  * Use the PyTorch model handler for RunInference.

For more information about using RunInference, see [Get started with AI/ML pipelines](https://beam.apache.org/documentation/ml/overview/) in the Apache Beam documentation.

## Install the Apache Beam SDK and dependencies

Use the following code to install the Apache Beam Python SDK, PyTorch, and Transformers.
    
    
    pip install apache_beam[interactive,gcp]==2.48.0
    pip install torch
    pip install transformers

Use the following code to import dependencies **Important:** If an error occurs, restart your runtime.
    
    
    import os
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    from apache_beam.ml.inference.base import PredictionResult
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.pytorch_inference import make_tensor_model_fn
    from apache_beam.ml.inference.pytorch_inference import PytorchModelHandlerTensor
    import torch
    from transformers import AutoConfig
    from transformers import AutoModelForSeq2SeqLM
    from transformers import AutoTokenizer
    from transformers.tokenization_utils import PreTrainedTokenizer
    
    
    MAX_RESPONSE_TOKENS = 256
    
    model_name = "google/flan-t5-small"
    state_dict_path = "saved_model"
    

## Download and save the model

This notebook uses the [auto classes](https://huggingface.co/docs/transformers/model_doc/auto) from Hugging Face to instantly load the model in memory. Later, the model is saved to the path defined previously.
    
    
    model = AutoModelForSeq2SeqLM.from_pretrained(
            model_name, torch_dtype=torch.bfloat16
        )
    
    directory = os.path.dirname(state_dict_path)
    torch.save(model.state_dict(), state_dict_path)
    

## Define utility functions

The input and output for the [`google/flan-t5-small`](https://huggingface.co/google/flan-t5-small) model are token tensors. These utility functions are used for the conversion of text to token tensors and then back to text.
    
    
    def to_tensors(input_text: str, tokenizer) -> torch.Tensor:
        """Encodes input text into token tensors.
        Args:
            input_text: Input text for the LLM model.
            tokenizer: Tokenizer for the LLM model.
        Returns: Tokenized input tokens.
        """
        return tokenizer(input_text, return_tensors="pt").input_ids[0]
    
    
    def from_tensors(result: PredictionResult, tokenizer) -> str:
        """Decodes output token tensors into text.
        Args:
            result: Prediction results from the RunInference transform.
            tokenizer: Tokenizer for the LLM model.
        Returns: The model's response as text.
        """
        output_tokens = result.inference
        return tokenizer.decode(output_tokens, skip_special_tokens=True)
    
    
    
    # Load the tokenizer.
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # Create an instance of the PyTorch model handler.
    model_handler = PytorchModelHandlerTensor(
                state_dict_path=state_dict_path,
                model_class=AutoModelForSeq2SeqLM.from_config,
                model_params={"config": AutoConfig.from_pretrained(model_name)},
                inference_fn=make_tensor_model_fn("generate"),
                )
    

## Run the Pipeline
    
    
    example = ["translate English to Spanish: We are in New York City."]
    
    pipeline = beam.Pipeline(options=PipelineOptions(save_main_session=True,pickle_library="cloudpickle"))
    
    with pipeline as p:
      _ = (
              p
              | "Create Examples" >> beam.Create(example)
              | "To tensors" >> beam.Map(to_tensors, tokenizer)
              | "RunInference"
                >> RunInference(
                    model_handler,
                    inference_args={"max_new_tokens": MAX_RESPONSE_TOKENS},
                )
              | "From tensors" >> beam.Map(from_tensors, tokenizer)
              | "Print" >> beam.Map(print)
          )
    
    
    
    Estamos en Nueva York City.
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
