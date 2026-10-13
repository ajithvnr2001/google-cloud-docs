---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextGenerationModel
title: Class TextGenerationModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:20.435187+00:00
---

# Class TextGenerationModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextGenerationModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TextGenerationModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    TextGenerationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a LanguageModel.

This constructor should not be called directly. Use `LanguageModel.from_pretrained(model_name=...)` instead.

## Methods 

### batch_predict
    
    
    batch_predict(
        *,
        dataset: typing.Union[str, typing.List[str]],
        destination_uri_prefix: str,
        model_parameters: typing.Optional[typing.Dict] = None
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Starts a batch prediction job with the model.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | When source or destination URI is not supported.  
  
### from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If model_name is unknown.  
`ValueError` | If model does not support this class.  
  
### get_tuned_model
    
    
    get_tuned_model(
        tuned_model_name: str,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

### list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

### predict
    
    
    predict(
        prompt: str,
        *,
        max_output_tokens: typing.Optional[int] = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None,
        grounding_source: typing.Optional[
            typing.Union[
                vertexai.language_models._language_models.WebSearch,
                vertexai.language_models._language_models.VertexAISearch,
                vertexai.language_models._language_models.InlineContext,
            ]
        ] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Gets model response for a single prompt.

### predict_async
    
    
    predict_async(
        prompt: str,
        *,
        max_output_tokens: typing.Optional[int] = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None,
        grounding_source: typing.Optional[
            typing.Union[
                vertexai.language_models._language_models.WebSearch,
                vertexai.language_models._language_models.VertexAISearch,
                vertexai.language_models._language_models.InlineContext,
            ]
        ] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Asynchronously gets model response for a single prompt.

### predict_streaming
    
    
    predict_streaming(
        prompt: str,
        *,
        max_output_tokens: int = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> typing.Iterator[vertexai.language_models.TextGenerationResponse]

Gets a streaming model response for a single prompt.

The result is a stream (generator) of partial responses.

### predict_streaming_async
    
    
    predict_streaming_async(
        prompt: str,
        *,
        max_output_tokens: int = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> typing.AsyncIterator[vertexai.language_models.TextGenerationResponse]

Asynchronously gets a streaming model response for a single prompt.

The result is a stream (generator) of partial responses.

### tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        train_steps: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        max_context_length: typing.Optional[str] = None
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
  
### tune_model_rlhf
    
    
    tune_model_rlhf(
        *,
        prompt_data: typing.Union[str, pandas.core.frame.DataFrame],
        preference_data: typing.Union[str, pandas.core.frame.DataFrame],
        model_display_name: typing.Optional[str] = None,
        prompt_sequence_length: typing.Optional[int] = None,
        target_sequence_length: typing.Optional[int] = None,
        reward_model_learning_rate_multiplier: typing.Optional[float] = None,
        reinforcement_learning_rate_multiplier: typing.Optional[float] = None,
        reward_model_train_steps: typing.Optional[int] = None,
        reinforcement_learning_train_steps: typing.Optional[int] = None,
        kl_coeff: typing.Optional[float] = None,
        default_context: typing.Optional[str] = None,
        tuning_job_location: typing.Optional[str] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model using reinforcement learning from human feedback.

This method launches and returns an asynchronous model tuning job. Usage:
    
    
    tuning_job = model.tune_model_rlhf(...)
    ... do some other work
    tuned_model = tuning_job.get_tuned_model()  # Blocks until tuning is complete
    

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the "tuning_job_location" value is not supported  
`RuntimeError` | If the model does not support tuning  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
