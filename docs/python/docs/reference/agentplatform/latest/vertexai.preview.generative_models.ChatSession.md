---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.generative_models.ChatSession
title: Class ChatSession (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:20.913477+00:00
---

# Class ChatSession (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.generative_models.ChatSession

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ChatSession (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ChatSession(
        model: vertexai.generative_models._generative_models._GenerativeModel,
        *,
        history: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Content]
        ] = None,
        response_validation: bool = True,
        responder: typing.Optional[
            vertexai.generative_models._generative_models.AutomaticFunctionCallingResponder
        ] = None,
        raise_on_blocked: typing.Optional[bool] = None
    )

Chat session holds the chat history.

## Methods 

### send_message
    
    
    send_message(
        content: PartsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.Iterable[vertexai.generative_models._generative_models.GenerationResponse],
    ]

Generates content.

**Exceptions**  
---  
**Type** | **Description**  
`ResponseValidationError` | If the response was blocked or is incomplete.  
  
### send_message_async
    
    
    send_message_async(
        content: PartsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        typing.Awaitable[vertexai.generative_models._generative_models.GenerationResponse],
        typing.Awaitable[
            typing.AsyncIterable[
                vertexai.generative_models._generative_models.GenerationResponse
            ]
        ],
    ]

Generates content asynchronously.

**Exceptions**  
---  
**Type** | **Description**  
`ResponseValidationError` | If the response was blocked or is incomplete.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
