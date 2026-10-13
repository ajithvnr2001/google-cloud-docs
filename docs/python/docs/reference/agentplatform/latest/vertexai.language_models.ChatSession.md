---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatSession
title: Class ChatSession (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:17.352451+00:00
---

# Class ChatSession (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatSession

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
        model: vertexai.language_models.ChatModel,
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
        stop_sequences: typing.Optional[typing.List[str]] = None,
    )

ChatSession represents a chat session with a language model.

Within a chat session, the model keeps context and remembers the previous conversation.

## Properties 

### message_history

List of previous messages.

## Methods 

### send_message
    
    
    send_message(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
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
        ] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Sends message to the language model and gets a response.

### send_message_async
    
    
    send_message_async(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
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
        ] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Asynchronously sends message to the language model and gets a response.

### send_message_streaming
    
    
    send_message_streaming(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.Iterator[vertexai.language_models.TextGenerationResponse]

Sends message to the language model and gets a streamed response.

The response is only added to the history once it's fully read.

### send_message_streaming_async
    
    
    send_message_streaming_async(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.AsyncIterator[vertexai.language_models.TextGenerationResponse]

Asynchronously sends message to the language model and gets a streamed response.

The response is only added to the history once it's fully read.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
