---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2
title: Cloud Natural Language v2 API - Namespace Google.Cloud.Language.V2 (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:47.870989+00:00
---

# Cloud Natural Language v2 API - Namespace Google.Cloud.Language.V2 (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Natural Language v2 API - Namespace Google.Cloud.Language.V2 (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/1.0.0-beta05/Google.Cloud.Language.V2)



## Classes 

### [AnalyzeEntitiesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnalyzeEntitiesRequest)

The entity analysis request message.

### [AnalyzeEntitiesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnalyzeEntitiesResponse)

The entity analysis response message.

### [AnalyzeSentimentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnalyzeSentimentRequest)

The sentiment analysis request message.

### [AnalyzeSentimentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnalyzeSentimentResponse)

The sentiment analysis response message.

### [AnnotateTextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnnotateTextRequest)

The request message for the text annotation API, which can perform multiple analysis types in one call.

### [AnnotateTextRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnnotateTextRequest.Types)

Container for nested types declared in the AnnotateTextRequest message type.

### [AnnotateTextRequest.Types.Features](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnnotateTextRequest.Types.Features)

All available features. Setting each one to true will enable that specific analysis for the input.

### [AnnotateTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.AnnotateTextResponse)

The text annotations response message.

### [ClassificationCategory](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassificationCategory)

Represents a category returned from the text classifier.

### [ClassifyTextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextRequest)

The document classification request message.

### [ClassifyTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ClassifyTextResponse)

The document classification response message.

### [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Document)

Represents the input to API methods.

### [Document.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Document.Types)

Container for nested types declared in the Document message type.

### [Entity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Entity)

Represents a phrase in the text that is a known entity, such as a person, an organization, or location. The API associates information, such as probability and mentions, with entities.

### [Entity.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Entity.Types)

Container for nested types declared in the Entity message type.

### [EntityMention](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EntityMention)

Represents a mention for an entity in the text. Currently, proper noun mentions are supported.

### [EntityMention.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EntityMention.Types)

Container for nested types declared in the EntityMention message type.

### [LanguageService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageService)

Provides text analysis operations such as sentiment analysis and entity recognition.

### [LanguageService.LanguageServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageService.LanguageServiceBase)

Base class for server-side implementations of LanguageService

### [LanguageService.LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageService.LanguageServiceClient)

Client for LanguageService

### [LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageServiceClient)

LanguageService client wrapper, for convenient use.

### [LanguageServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageServiceClientBuilder)

Builder class for [LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageServiceClient) to provide simple configuration of credentials, endpoint etc.

### [LanguageServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageServiceClientImpl)

LanguageService client wrapper implementation, for convenient use.

### [LanguageServiceSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageServiceSettings)

Settings for [LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.LanguageServiceClient) instances.

### [ModerateTextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ModerateTextRequest)

The document moderation request message.

### [ModerateTextRequest.Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ModerateTextRequest.Types)

Container for nested types declared in the ModerateTextRequest message type.

### [ModerateTextResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ModerateTextResponse)

The document moderation response message.

### [Sentence](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Sentence)

Represents a sentence in the input document.

### [Sentiment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Sentiment)

Represents the feeling associated with the entire text or entities in the text.

### [TextSpan](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.TextSpan)

Represents a text span in the input document.

## Enums 

### [Document.SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Document.SourceOneofCase)

Enum of possible cases for the "source" oneof.

### [Document.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Document.Types.Type)

The document types enum.

### [EncodingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EncodingType)

Represents the text encoding that the caller uses to process the output. Providing an `EncodingType` is recommended because the API provides the beginning offsets for various outputs, such as tokens and mentions, and languages that natively use different text encodings may access offsets differently.

### [Entity.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.Entity.Types.Type)

The type of the entity. The table below lists the associated fields for entities that have different metadata.

### [EntityMention.Types.Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.EntityMention.Types.Type)

The supported types of mentions.

### [ModerateTextRequest.Types.ModelVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V2/latest/Google.Cloud.Language.V2.ModerateTextRequest.Types.ModelVersion)

The model version to use for ModerateText.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
