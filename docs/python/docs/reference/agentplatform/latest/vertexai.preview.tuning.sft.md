---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.tuning.sft
title: Module sft (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:32.168694+00:00
---

# Module sft (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.tuning.sft

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module sft (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

Classes for supervised tuning.

## Classes 

### [SupervisedTuningJob](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.tuning.sft.SupervisedTuningJob)
    
    
    SupervisedTuningJob(tuning_job_name: str)

Initializes class with project, location, and api_client.

**Parameters**  
---  
**Name** | **Description**  
`project` |  `str`   
Project of the resource noun.  
`location` |  `str`   
The location of the resource noun.  
`credentials` |  `google.auth.credentials.Credentials`   
Optional custom credentials to use when accessing interacting with resource noun.  
`resource_name` |  `str`   
A fully-qualified resource name or ID.  
  
## Modules Functions 

### preview_train
    
    
    preview_train(
        *,
        source_model: typing.Union[
            str,
            vertexai.generative_models.GenerativeModel,
            vertexai.preview.tuning._tuning.SourceModel,
        ],
        train_dataset: typing.Union[
            str, google.cloud.aiplatform.preview.datasets.MultimodalDataset
        ],
        validation_dataset: typing.Optional[
            typing.Union[str, google.cloud.aiplatform.preview.datasets.MultimodalDataset]
        ] = None,
        tuned_model_display_name: typing.Optional[str] = None,
        tuning_mode: typing.Optional[typing.Literal["FULL", "PEFT_ADAPTER"]] = None,
        epochs: typing.Optional[int] = None,
        learning_rate: typing.Optional[float] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        adapter_size: typing.Optional[typing.Literal[1, 4, 8, 16, 32]] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        output_uri: typing.Optional[str] = None
    ) -> vertexai.preview.tuning._supervised_tuning.SupervisedTuningJob

Tunes a model using supervised training.

**Parameter**  
---  
**Name** | **Description**  
`source_model` |  `str`   
Model name for tuning, e.g., "gemini-1.0-pro-002".  
  
### rebase_tuned_model
    
    
    rebase_tuned_model(
        tuned_model_ref: str,
        *,
        artifact_destination: typing.Optional[str] = None,
        deploy_to_same_endpoint: typing.Optional[bool] = False
    )

Re-runs fine tuning on top of a new foundational model.

Takes a legacy Tuned GenAI model Reference and creates a TuningJob based on a new model.

### train
    
    
    train(
        *,
        source_model: typing.Union[
            str,
            vertexai.generative_models.GenerativeModel,
            vertexai.tuning._tuning.SourceModel,
        ],
        train_dataset: typing.Union[
            str, google.cloud.aiplatform.preview.datasets.MultimodalDataset
        ],
        validation_dataset: typing.Optional[
            typing.Union[str, google.cloud.aiplatform.preview.datasets.MultimodalDataset]
        ] = None,
        tuned_model_display_name: typing.Optional[str] = None,
        tuning_mode: typing.Optional[typing.Literal["FULL", "PEFT_ADAPTER"]] = None,
        epochs: typing.Optional[int] = None,
        learning_rate: typing.Optional[float] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        adapter_size: typing.Optional[typing.Literal[1, 4, 8, 16, 32]] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        output_uri: typing.Optional[str] = None
    ) -> vertexai.tuning._supervised_tuning.SupervisedTuningJob

Tunes a model using supervised training.

**Parameter**  
---  
**Name** | **Description**  
`source_model` |  `str`   
Model name for tuning, e.g., "gemini-1.0-pro-002".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
