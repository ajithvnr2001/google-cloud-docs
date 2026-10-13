---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/run_custom_inference/
title: Bring your own ML model to Beam RunInference \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:37.247025+00:00
---

# Bring your own ML model to Beam RunInference  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/run_custom_inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Bring your own ML model to Beam RunInference Stay organized with collections  Save and categorize content based on your preferences. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/run_custom_inference.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/run_custom_inference.ipynb) This notebook demonstrates how to run inference on your custom framework using the [ModelHandler](https://beam.apache.org/releases/pydoc/current/apache_beam.ml.inference.base.html#apache_beam.ml.inference.base.ModelHandler) class. Named-entity recognition (NER) is one of the most common tasks for natural language processing (NLP). NLP locates named entities in unstructured text and classifies the entities using pre-defined labels, such as person name, organization, date, and so on. This example illustrates how to use the popular `spaCy` package to load a machine learning (ML) model and perform inference in an Apache Beam pipeline using the RunInference `PTransform`. For more information about the RunInference API, see [About Beam ML](https://beam.apache.org/documentation/ml/about-ml) in the Apache Beam documentation.

## Install package dependencies

The RunInference library is available in Apache Beam versions 2.40 and later. For this example, you need to install `spaCy` and `pandas`. A small NER model, `en_core_web_sm`, is also installed, but you can use any valid `spaCy` model.
    
    
    # Uncomment the following lines to install the required packages.
    # %pip install spacy pandas
    # %pip install "apache-beam[gcp, dataframe, interactive]"
    # !python -m spacy download en_core_web_sm
    

## Learn about `spaCy`

To learn more about `spaCy`, create a `spaCy` language object in memory using `spaCy`'s trained models. You can install these models as Python packages. For more information, see spaCy's [Models and Languages](https://spacy.io/usage/models) documentation.
    
    
    import spacy
    
    nlp = spacy.load("en_core_web_sm")
    
    
    
    # Add text strings.
    text_strings = [
        "The New York Times is an American daily newspaper based in New York City with a worldwide readership.",
        "It was founded in 1851 by Henry Jarvis Raymond and George Jones, and was initially published by Raymond, Jones & Company."
    ]
    
    
    
    # Check which entities spaCy can recognize.
    doc = nlp(text_strings[0])
    
    
    
    for ent in doc.ents:
        print(ent.text, ent.start_char, ent.end_char, ent.label_)
    
    
    
    The New York Times 0 18 ORG
    American 25 33 NORP
    daily 34 39 DATE
    New York City 59 72 GPE
    
    
    
    # Visualize the results.
    from spacy import displacy
    displacy.render(doc, style="ent")
    
    
    
    # Visualize another example.
    displacy.render(nlp(text_strings[1]), style="ent")
    

## Create a model handler

This section demonstrates how to create your own `ModelHandler` so that you can use `spaCy` for inference.
    
    
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    
    import warnings
    warnings.filterwarnings("ignore")
    
    
    pipeline = beam.Pipeline()
    
    # Print the results for verification.
    with pipeline as p:
        (p 
        | "CreateSentences" >> beam.Create(text_strings)
        | beam.Map(print)
        )
    
    
    
    The New York Times is an American daily newspaper based in New York City with a worldwide readership.
    It was founded in 1851 by Henry Jarvis Raymond and George Jones, and was initially published by Raymond, Jones & Company.
    
    
    
    # Define `SpacyModelHandler` to load the model and perform the inference.
    
    from apache_beam.ml.inference.base import RunInference
    from apache_beam.ml.inference.base import ModelHandler
    from apache_beam.ml.inference.base import PredictionResult
    from spacy import Language
    from typing import Any
    from typing import Dict
    from typing import Iterable
    from typing import Optional
    from typing import Sequence
    
    class SpacyModelHandler(ModelHandler[str,
                                         PredictionResult,
                                         Language]):
        def __init__(
            self,
            model_name: str = "en_core_web_sm",
        ):
            """ Implementation of the ModelHandler interface for spaCy using text as input.
    
            Example Usage::
    
              pcoll | RunInference(SpacyModelHandler())
    
            Args:
              model_name: The spaCy model name. Default is en_core_web_sm.
            """
            self._model_name = model_name
            self._env_vars = {}
    
        def load_model(self) -> Language:
            """Loads and initializes a model for processing."""
            return spacy.load(self._model_name)
    
        def run_inference(
            self,
            batch: Sequence[str],
            model: Language,
            inference_args: Optional[Dict[str, Any]] = None
        ) -> Iterable[PredictionResult]:
            """Runs inferences on a batch of text strings.
    
            Args:
              batch: A sequence of examples as text strings. 
              model: A spaCy language model
              inference_args: Any additional arguments for an inference.
    
            Returns:
              An Iterable of type PredictionResult.
            """
            # Loop each text string, and use a tuple to store the inference results.
            predictions = []
            for one_text in batch:
                doc = model(one_text)
                predictions.append(
                    [(ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents])
            return [PredictionResult(x, y) for x, y in zip(batch, predictions)]
    
    
    
    # Verify that the inference results are correct.
    with pipeline as p:
        (p 
        | "CreateSentences" >> beam.Create(text_strings)
        | "RunInferenceSpacy" >> RunInference(SpacyModelHandler("en_core_web_sm"))
        | beam.Map(print)
        )
    
    
    
    The New York Times is an American daily newspaper based in New York City with a worldwide readership.
    It was founded in 1851 by Henry Jarvis Raymond and George Jones, and was initially published by Raymond, Jones & Company.
    PredictionResult(example='The New York Times is an American daily newspaper based in New York City with a worldwide readership.', inference=[('The New York Times', 0, 18, 'ORG'), ('American', 25, 33, 'NORP'), ('daily', 34, 39, 'DATE'), ('New York City', 59, 72, 'GPE')])
    PredictionResult(example='It was founded in 1851 by Henry Jarvis Raymond and George Jones, and was initially published by Raymond, Jones & Company.', inference=[('1851', 18, 22, 'DATE'), ('Henry Jarvis', 26, 38, 'PERSON'), ('Raymond', 39, 46, 'PERSON'), ('George Jones', 51, 63, 'PERSON'), ('Raymond, Jones & Company', 96, 120, 'ORG')])
    

## Use `KeyedModelHandler` to handle keyed data

If you have keyed data, use `KeyedModelHandler`.
    
    
    # You can use these text strings with keys to distinguish examples.
    text_strings_with_keys = [
        ("example_0", "The New York Times is an American daily newspaper based in New York City with a worldwide readership."),
        ("example_1", "It was founded in 1851 by Henry Jarvis Raymond and George Jones, and was initially published by Raymond, Jones & Company.")
    ]
    
    
    
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    from apache_beam.ml.inference.base import KeyedModelHandler
    from apache_beam.dataframe.convert import to_dataframe
    
    pipeline = beam.Pipeline(InteractiveRunner())
    
    keyed_spacy_model_handler = KeyedModelHandler(SpacyModelHandler("en_core_web_sm"))
    
    # Verify that the inference results are correct.
    with pipeline as p:
        results = (p 
        | "CreateSentences" >> beam.Create(text_strings_with_keys)
        | "RunInferenceSpacy" >> RunInference(keyed_spacy_model_handler)
        # Generate a schema suitable for conversion to a dataframe using Map to Row objects.
        | 'ToRows' >> beam.Map(lambda row: beam.Row(key=row[0], text=row[1][0], predictions=row[1][1]))
        )
    
    
    
    # Convert the results to a pandas dataframe.
    import apache_beam.runners.interactive.interactive_beam as ib
    
    beam_df = to_dataframe(results)
    df = ib.collect(beam_df)
    
    
    
    df
    

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
