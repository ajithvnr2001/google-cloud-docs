---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbeddingModel
title: Class TextEmbeddingModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:19.456405+00:00
---

# Class TextEmbeddingModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbeddingModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TextEmbeddingModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    TextEmbeddingModel(model_id: str, endpoint_name: typing.Optional[str] = None)

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
  
### count_tokens
    
    
    count_tokens(
        prompts: typing.List[str],
    ) -> vertexai.preview.language_models.CountTokensResponse

Counts the tokens and billable characters for a given prompt.

Note: this does not make a prediction request to the model, it only counts the tokens in the request.

**Parameter**  
---  
**Name** | **Description**  
`prompts` |  `List[str]`   
Required. A list of prompts to ask the model. For example: ["What should I do today?", "How's it going?"]  
  
### deploy_tuned_model
    
    
    deploy_tuned_model(
        tuned_model_name: str,
        machine_type: typing.Optional[str] = None,
        accelerator: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

### from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If model_name is unknown.  
`ValueError` | If model does not support this class.  
  
### get_embeddings
    
    
    get_embeddings(
        texts: typing.List[typing.Union[str, vertexai.language_models.TextEmbeddingInput]],
        *,
        auto_truncate: bool = True,
        output_dimensionality: typing.Optional[int] = None
    ) -> typing.List[vertexai.language_models.TextEmbedding]

Calculates embeddings for the given texts.

### get_embeddings_async
    
    
    get_embeddings_async(
        texts: typing.List[typing.Union[str, vertexai.language_models.TextEmbeddingInput]],
        *,
        auto_truncate: bool = True,
        output_dimensionality: typing.Optional[int] = None
    ) -> typing.List[vertexai.language_models.TextEmbedding]

Asynchronously calculates embeddings for the given texts.

### get_tuned_model
    
    
    get_tuned_model(*args, **kwargs)

Loads the specified tuned language model.

### list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

### tune_model
    
    
    tune_model(
        *,
        training_data: typing.Optional[str] = None,
        corpus_data: typing.Optional[str] = None,
        queries_data: typing.Optional[str] = None,
        test_data: typing.Optional[str] = None,
        validation_data: typing.Optional[str] = None,
        batch_size: typing.Optional[int] = None,
        train_steps: typing.Optional[int] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        task_type: typing.Optional[str] = None,
        machine_type: typing.Optional[str] = None,
        accelerator: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        output_dimensionality: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None
    ) -> vertexai.language_models._language_models._TextEmbeddingModelTuningJob

Tunes a model based on training data.

This method launches and returns an asynchronous model tuning job. Usage:
    
    
    tuning_job = model.tune_model(...)
    ... do some other work
    tuned_model = tuning_job.deploy_tuned_model()  # Blocks until tuning is complete
    

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the provided parameter combinations or values are not supported.  
`RuntimeError` | If the model does not support tuning  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
