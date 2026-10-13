---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models
title: Package language_models (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:15.658712+00:00
---

# Package language_models (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package language_models (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

API documentation for `language_models` package.

## Classes 

### [ChatMessage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatMessage)

A chat message.

### [ChatModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatModel)

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
    

### [ChatSession](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.ChatSession)

ChatSession represents a chat session with a language model.

Within a chat session, the model keeps context and remembers the previous conversation.

### [CodeChatModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.CodeChatModel)

CodeChatModel represents a model that is capable of completing code.

.. rubric:: Examples

code_chat_model = CodeChatModel.from_pretrained("codechat-bison@001")

code_chat = code_chat_model.start_chat( context="I'm writing a large-scale enterprise application.", max_output_tokens=128, temperature=0.2, )

code_chat.send_message("Please help write a function to calculate the min of two numbers")

### [CodeChatSession](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.CodeChatSession)

CodeChatSession represents a chat session with code chat language model.

Within a code chat session, the model keeps context and remembers the previous converstion.

### [CodeGenerationModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.CodeGenerationModel)

Creates a LanguageModel.

This constructor should not be called directly. Use `LanguageModel.from_pretrained(model_name=...)` instead.

### [GroundingSource](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.GroundingSource)

API documentation for `GroundingSource` class.

### [InputOutputTextPair](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.InputOutputTextPair)

InputOutputTextPair represents a pair of input and output texts.

### [TextEmbedding](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbedding)

Text embedding vector and statistics.

### [TextEmbeddingInput](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbeddingInput)

Structural text embedding input.

### [TextEmbeddingModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextEmbeddingModel)

Creates a LanguageModel.

This constructor should not be called directly. Use `LanguageModel.from_pretrained(model_name=...)` instead.

### [TextGenerationModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextGenerationModel)

Creates a LanguageModel.

This constructor should not be called directly. Use `LanguageModel.from_pretrained(model_name=...)` instead.

### [TextGenerationResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models.TextGenerationResponse)

TextGenerationResponse represents a response of a language model. .. attribute:: text

The generated text

:type: str

## Modules 

### [_language_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models._language_models)

Classes for working with language models.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
