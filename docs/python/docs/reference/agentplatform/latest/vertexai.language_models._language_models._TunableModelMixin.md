---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models._language_models._TunableModelMixin
title: Class _TunableModelMixin (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:16.407396+00:00
---

# Class _TunableModelMixin (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models._language_models._TunableModelMixin

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class _TunableModelMixin (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    _TunableModelMixin(model_id: str, endpoint_name: typing.Optional[str] = None)

Model that can be tuned with supervised fine tuning (SFT).

## Methods 

### _TunableModelMixin
    
    
    _TunableModelMixin(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a LanguageModel.

This constructor should not be called directly. Use `LanguageModel.from_pretrained(model_name=...)` instead.

### tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        corpus_data: typing.Optional[str] = None,
        queries_data: typing.Optional[str] = None,
        test_data: typing.Optional[str] = None,
        validation_data: typing.Optional[str] = None,
        batch_size: typing.Optional[int] = None,
        train_steps: typing.Optional[int] = None,
        learning_rate: typing.Optional[float] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None,
        default_context: typing.Optional[str] = None,
        task_type: typing.Optional[str] = None,
        machine_type: typing.Optional[str] = None,
        accelerator: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        max_context_length: typing.Optional[str] = None,
        output_dimensionality: typing.Optional[int] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model based on training data.

This method launches and returns an asynchronous model tuning job. Usage:
    
    
    tuning_job = model.tune_model(...)
    ... do some other work
    tuned_model = tuning_job.get_tuned_model()  # Blocks until tuning is complete
    

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the "tuning_job_location" value is not supported  
`ValueError` | If the "tuned_model_location" value is not supported  
`RuntimeError` | If the model does not support tuning  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
