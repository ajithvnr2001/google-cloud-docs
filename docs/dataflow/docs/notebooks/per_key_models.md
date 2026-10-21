---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/per_key_models/
title: Run ML inference with multiple differently-trained models \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:50:50.554726+00:00
---

# Run ML inference with multiple differently-trained models  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/per_key_models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Run ML inference with multiple differently-trained models Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/per_key_models.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/per_key_models.ipynb) Running inference with multiple differently-trained models performing the same task is useful in many scenarios, including the following examples:

  * You want to compare the performance of multiple different models.
  * You have models trained on different datasets that you want to use conditionally based on additional metadata.

In Apache Beam, the recommended way to run inference is to use the `RunInference` transform. By using a `KeyedModelHandler`, you can efficiently run inference with O(100s) of models without having to manage memory yourself. This notebook demonstrates how to use a `KeyedModelHandler` to run inference in an Apache Beam pipeline with multiple different models on a per-key basis. This notebook uses pretrained pipelines from Hugging Face. Before continuing with this notebook, it is recommended that you walk through the [Use RunInference in Apache Beam](https://colab.sandbox.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_inference_pytorch_tensorflow_sklearn.ipynb) notebook.

## Install dependencies

Install both Apache Beam and the dependencies needed by Hugging Face.
    
    
    !pip install apache_beam[interactive,gcp]>=2.51.0 --quiet
    !pip install torch --quiet
    !pip install transformers --quiet
    
    # To use the newly installed versions, restart the runtime.
    exit()
    
    
    
    from typing import Dict
    from typing import Iterable
    from typing import Tuple
    
    from transformers import pipeline
    
    import apache_beam as beam
    from apache_beam.ml.inference.base import KeyedModelHandler
    from apache_beam.ml.inference.base import KeyModelMapping
    from apache_beam.ml.inference.base import PredictionResult
    from apache_beam.ml.inference.huggingface_inference import HuggingFacePipelineModelHandler
    from apache_beam.ml.inference.base import RunInference
    

## Define the model configurations

A model handler is the Apache Beam method used to define the configuration needed to load and invoke models. Because this example uses two models, we define two model handlers, one for each model. Because both models are incapsulated within Hugging Face pipelines, we use the model handler `HuggingFacePipelineModelHandler`. For this example, load the models using Hugging Face, and then run them against an example. The models produce different outputs.
    
    
    distilbert_mh = HuggingFacePipelineModelHandler('text-classification', model="distilbert-base-uncased-finetuned-sst-2-english")
    roberta_mh = HuggingFacePipelineModelHandler('text-classification', model="roberta-large-mnli")
    
    distilbert_pipe = pipeline('text-classification', model="distilbert-base-uncased-finetuned-sst-2-english")
    roberta_large_pipe = pipeline(model="roberta-large-mnli")
    
    
    
    Downloading (…)lve/main/config.json:   0%|          | 0.00/629 [00:00<?, ?B/s]
    Downloading model.safetensors:   0%|          | 0.00/268M [00:00<?, ?B/s]
    Downloading (…)okenizer_config.json:   0%|          | 0.00/48.0 [00:00<?, ?B/s]
    Downloading (…)solve/main/vocab.txt:   0%|          | 0.00/232k [00:00<?, ?B/s]
    Downloading (…)lve/main/config.json:   0%|          | 0.00/688 [00:00<?, ?B/s]
    Downloading model.safetensors:   0%|          | 0.00/1.43G [00:00<?, ?B/s]
    Downloading (…)olve/main/vocab.json:   0%|          | 0.00/899k [00:00<?, ?B/s]
    Downloading (…)olve/main/merges.txt:   0%|          | 0.00/456k [00:00<?, ?B/s]
    Downloading (…)/main/tokenizer.json:   0%|          | 0.00/1.36M [00:00<?, ?B/s]
    
    
    
    distilbert_pipe("This restaurant is awesome")
    
    
    
    [{'label': 'POSITIVE', 'score': 0.9998743534088135}]
    
    
    
    roberta_large_pipe("This restaurant is awesome")
    
    
    
    [{'label': 'NEUTRAL', 'score': 0.7313134670257568}]
    

## Define the examples

Define examples to input into the pipeline. The examples include the correct classifications.
    
    
    examples = [
        ("This restaurant is awesome", "positive"),
        ("This restaurant is bad", "negative"),
        ("I feel fine", "neutral"),
        ("I love chocolate", "positive"),
    ]
    

To feed the examples into RunInference, you need distinct keys that can map to the model. In this case, to make it possible to extract the actual sentiment of the example later, define keys in the form `<model_name>-<actual_sentiment>`.
    
    
    class FormatExamples(beam.DoFn):
      """
      Map each example to a tuple of ('<model_name>-<actual_sentiment>', 'example').
      Use these keys to map our elements to the correct models.
      """
      def process(self, element: Tuple[str, str]) -> Iterable[Tuple[str, str]]:
        yield (f'distilbert-{element[1]}', element[0])
        yield (f'roberta-{element[1]}', element[0])
    

Use the formatted keys to define a `KeyedModelHandler` that maps keys to the `ModelHandler` used for those keys. The `KeyedModelHandler` method lets you define an optional `max_models_per_worker_hint`, which limits the number of models that can be held in a single worker process at one time. If your worker might run out of memory, use this option. For more information about managing memory, see [Use a keyed ModelHandler](https://beam.apache.org/documentation/ml/about-ml/#use-a-keyed-modelhandler-object).
    
    
    per_key_mhs = [
        KeyModelMapping(['distilbert-positive', 'distilbert-neutral', 'distilbert-negative'], distilbert_mh),
        KeyModelMapping(['roberta-positive', 'roberta-neutral', 'roberta-negative'], roberta_mh)
    ]
    mh = KeyedModelHandler(per_key_mhs, max_models_per_worker_hint=2)
    

## Postprocess the results

The `RunInference` transform returns a tuple that contains the following objects:

  * the original key
  * a `PredictionResult` object containing the original example and the inference Use those outputs to extract the relevant data. Then, to compare each model's prediction, group this data by the original example.


    
    
    class ExtractResults(beam.DoFn):
      """
      Extract the relevant data from the PredictionResult object.
      """
      def process(self, element: Tuple[str, PredictionResult]) -> Iterable[Tuple[str, Dict[str, str]]]:
        actual_sentiment = element[0].split('-')[1]
        model = element[0].split('-')[0]
        result = element[1]
        example = result.example
        predicted_sentiment = result.inference[0]['label']
    
        yield (example, {'model': model, 'actual_sentiment': actual_sentiment, 'predicted_sentiment': predicted_sentiment})
    

Finally, print the results produced by each model.
    
    
    class PrintResults(beam.DoFn):
      """
      Print the results produced by each model along with the actual sentiment.
      """
      def process(self, element: Tuple[str, Iterable[Dict[str, str]]]):
        example = element[0]
        actual_sentiment = element[1][0]['actual_sentiment']
        predicted_sentiment_1 = element[1][0]['predicted_sentiment']
        model_1 = element[1][0]['model']
        predicted_sentiment_2 = element[1][1]['predicted_sentiment']
        model_2 = element[1][1]['model']
    
        if model_1 == 'distilbert':
          distilbert_prediction = predicted_sentiment_1
          roberta_prediction = predicted_sentiment_2
        else:
          roberta_prediction = predicted_sentiment_1
          distilbert_prediction = predicted_sentiment_2
    
        print(f'Example: {example}\nActual Sentiment: {actual_sentiment}\n'
              f'Distilbert Prediction: {distilbert_prediction}\n'
              f'Roberta Prediction: {roberta_prediction}\n------------')
    

## Run the pipeline

To run a single Apache Beam pipeline, combine the previous steps.
    
    
    with beam.Pipeline() as beam_pipeline:
    
      formatted_examples = (
                beam_pipeline
                | "ReadExamples" >> beam.Create(examples)
                | "FormatExamples" >> beam.ParDo(FormatExamples()))
      inferences = (
                formatted_examples
                | "Run Inference" >> RunInference(mh)
                | "ExtractResults" >> beam.ParDo(ExtractResults())
                | "GroupByExample" >> beam.GroupByKey()
      )
    
      inferences | beam.ParDo(PrintResults())
    
    
    
    Example: This restaurant is awesome
    Actual Sentiment: positive
    Distilbert Prediction: POSITIVE
    Roberta Prediction: NEUTRAL
    ------------
    Example: This restaurant is bad
    Actual Sentiment: negative
    Distilbert Prediction: NEGATIVE
    Roberta Prediction: NEUTRAL
    ------------
    Example: I love chocolate
    Actual Sentiment: positive
    Distilbert Prediction: POSITIVE
    Roberta Prediction: NEUTRAL
    ------------
    Example: I feel fine
    Actual Sentiment: neutral
    Distilbert Prediction: POSITIVE
    Roberta Prediction: ENTAILMENT
    ------------
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
