---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.generative_models.GenerativeModel
title: Class GenerativeModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:24.026637+00:00
---

# Class GenerativeModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.generative_models.GenerativeModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class GenerativeModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    GenerativeModel(
        model_name: str,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        system_instruction: typing.Optional[PartsType] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None
    )

Initializes GenerativeModel.

Usage:
    
    
    ```
    model = GenerativeModel("gemini-pro")
    print(model.generate_content("Hello"))
    ```
    

## Methods 

### compute_tokens
    
    
    compute_tokens(
        contents: ContentsType,
    ) -> google.cloud.aiplatform_v1beta1.types.llm_utility_service.ComputeTokensResponse

Computes tokens.

**Returns**  
---  
**Type** | **Description**  
`A ComputeTokensResponse object that has the following attributes` | tokens_info: Lists of tokens_info from the input. The input `contents: ContentsType` could have multiple string instances and each tokens_info item represents each string instance. Each token info consists tokens list, token_ids list and a role.  
  
### compute_tokens_async
    
    
    compute_tokens_async(
        contents: ContentsType,
    ) -> google.cloud.aiplatform_v1beta1.types.llm_utility_service.ComputeTokensResponse

Computes tokens asynchronously.

**Returns**  
---  
**Type** | **Description**  
`And awaitable for a ComputeTokensResponse object that has the following attributes` | tokens_info: Lists of tokens_info from the input. The input `contents: ContentsType` could have multiple string instances and each tokens_info item represents each string instance. Each token info consists tokens list, token_ids list and a role.  
  
### count_tokens
    
    
    count_tokens(
        contents: ContentsType,
        *,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None
    ) -> google.cloud.aiplatform_v1beta1.types.prediction_service.CountTokensResponse

Counts tokens.

**Returns**  
---  
**Type** | **Description**  
`A CountTokensResponse object that has the following attributes` | total_tokens: The total number of tokens counted across all instances from the request. total_billable_characters: The total number of billable characters counted across all instances from the request.  
  
### count_tokens_async
    
    
    count_tokens_async(
        contents: ContentsType,
        *,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None
    ) -> google.cloud.aiplatform_v1beta1.types.prediction_service.CountTokensResponse

Counts tokens asynchronously.

**Returns**  
---  
**Type** | **Description**  
`And awaitable for a CountTokensResponse object that has the following attributes` | total_tokens: The total number of tokens counted across all instances from the request. total_billable_characters: The total number of billable characters counted across all instances from the request.  
  
### from_cached_content
    
    
    from_cached_content(
        cached_content: typing.Union[str, CachedContent],
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None
    ) -> _GenerativeModel

Creates a model from cached content.

Creates a model instance with an existing cached content. The cached content becomes the prefix of the requesting contents.

### generate_content
    
    
    generate_content(
        contents: ContentsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.Iterable[vertexai.generative_models._generative_models.GenerationResponse],
    ]

Generates content.

### generate_content_async
    
    
    generate_content_async(
        contents: ContentsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.AsyncIterable[
            vertexai.generative_models._generative_models.GenerationResponse
        ],
    ]

Generates content asynchronously.

### set_request_response_logging_config
    
    
    set_request_response_logging_config(
        *,
        enabled: bool,
        sampling_rate: float,
        bigquery_destination: str,
        enable_otel_logging: typing.Optional[bool] = None
    ) -> typing.Union[
        google.cloud.aiplatform_v1beta1.types.endpoint.PublisherModelConfig,
        google.cloud.aiplatform_v1beta1.types.endpoint.Endpoint,
    ]

Sets the request/response logging config.

### start_chat
    
    
    start_chat(
        *,
        history: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Content]
        ] = None,
        response_validation: bool = True,
        responder: typing.Optional[
            vertexai.generative_models._generative_models.AutomaticFunctionCallingResponder
        ] = None
    ) -> vertexai.generative_models._generative_models.ChatSession

Creates a stateful chat session.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
