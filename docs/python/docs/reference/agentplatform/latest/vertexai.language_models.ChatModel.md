---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatModel
title: Class ChatModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:16.853093+00:00
---

# Class ChatModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ChatModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ChatModel(model_id: str, endpoint_name: typing.Optional[str] = None)

ChatModel represents a language model that is capable of chat.

Examples::
    
    
    chat_model = ChatModel.from_pretrained("chat-bison@001")
    
    chat = chat_model.start_chat(
        context="My name is Ned. You are my personal assistant. My favorite movies are Lord of the Rings and Hobbit.",
        examples=[
            InputOutputTextPair(
                input_text="Who do you work for?",
                output_text="I work for Ned.",
            ),
            InputOutputTextPair(
                input_text="What do I like?",
                output_text="Ned likes watching movies.",
            ),
        ],
        temperature=0.3,
    )
    
    chat.send_message("Do you know any cool events this weekend?")
    

## Methods 

### ChatModel
    
    
    ChatModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a LanguageModel.

This constructor should not be called directly. Use `LanguageModel.from_pretrained(model_name=...)` instead.

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

### start_chat
    
    
    start_chat(
        *,
        context: typing.Optional[str] = None,
        examples: typing.Optional[
            typing.List[vertexai.language_models.InputOutputTextPair]
        ] = None,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        message_history: typing.Optional[
            typing.List[vertexai.language_models.ChatMessage]
        ] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> vertexai.language_models.ChatSession

Starts a chat session with the model.

### tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        train_steps: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        default_context: typing.Optional[str] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None
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
`AttributeError` | If any attribute in the "tuning_evaluation_spec" is not supported  
  
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
