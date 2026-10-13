---
url: https://docs.cloud.google.com/cpp/docs/reference/language/latest/classgoogle_1_1cloud_1_1language__v2_1_1LanguageServiceClient/
title: Class LanguageServiceClient (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:01.123357+00:00
---

# Class LanguageServiceClient (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/language/latest/classgoogle_1_1cloud_1_1language__v2_1_1LanguageServiceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class LanguageServiceClient (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Provides text analysis operations such as sentiment analysis and entity recognition. 

###### Equality

Instances of this class created via copy-construction or copy-assignment always compare equal. Instances created with equal `std::shared_ptr<*Connection>` objects compare equal. Objects that compare equal share the same underlying resources.

###### Performance

Creating a new instance of this class is a relatively expensive operation, new objects establish new connections to the service. In contrast, copy-construction, move-construction, and the corresponding assignment operations are relatively efficient as the copies share all underlying resources.

###### Thread Safety

Concurrent access to different instances of this class, even if they compare equal, is guaranteed to work. Two or more threads operating on the same instance of this class is not guaranteed to work. Since copy-construction and move-construction is a relatively efficient operation, consider using such a copy when using this class from multiple threads. 

## Constructors 

### LanguageServiceClient(LanguageServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `LanguageServiceClient const &`   
  
  
### LanguageServiceClient(LanguageServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `LanguageServiceClient &&`   
  
  
### LanguageServiceClient(std::shared_ptr< LanguageServiceConnection >, Options)

**Parameters**  
---  
**Name** | **Description**  
`connection` |  `std::shared_ptr< LanguageServiceConnection >`   
  
`opts` |  `Options`   
  
  
## Operators 

### operator=(LanguageServiceClient const &)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `LanguageServiceClient const &`   
  
**Returns**  
---  
**Type** | **Description**  
`LanguageServiceClient &` |   
  
### operator=(LanguageServiceClient &&)

Copy and move support

**Parameter**  
---  
**Name** | **Description**  
`` |  `LanguageServiceClient &&`   
  
**Returns**  
---  
**Type** | **Description**  
`LanguageServiceClient &` |   
  
## Functions 

### AnalyzeSentiment(google::cloud::language::v2::Document const &, google::cloud::language::v2::EncodingType, Options)

Analyzes the sentiment of the provided text. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`encoding_type` |  `google::cloud::language::v2::EncodingType`   
The encoding type used by the API to calculate sentence offsets.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnalyzeSentimentResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnalyzeSentimentResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L358)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnalyzeSentiment(google::cloud::language::v2::Document const &, Options)

Analyzes the sentiment of the provided text. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnalyzeSentimentResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnalyzeSentimentResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L358)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnalyzeSentiment(google::cloud::language::v2::AnalyzeSentimentRequest const &, Options)

Analyzes the sentiment of the provided text. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::language::v2::AnalyzeSentimentRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.language.v2.AnalyzeSentimentRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L349). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnalyzeSentimentResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnalyzeSentimentResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L358)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnalyzeEntities(google::cloud::language::v2::Document const &, google::cloud::language::v2::EncodingType, Options)

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`encoding_type` |  `google::cloud::language::v2::EncodingType`   
The encoding type used by the API to calculate offsets.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnalyzeEntitiesResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnalyzeEntitiesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L386)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnalyzeEntities(google::cloud::language::v2::Document const &, Options)

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnalyzeEntitiesResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnalyzeEntitiesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L386)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnalyzeEntities(google::cloud::language::v2::AnalyzeEntitiesRequest const &, Options)

Finds named entities (currently proper names and common nouns) in the text along with entity types, probability, mentions for each entity, and other properties. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::language::v2::AnalyzeEntitiesRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.language.v2.AnalyzeEntitiesRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L377). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnalyzeEntitiesResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnalyzeEntitiesResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L386)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ClassifyText(google::cloud::language::v2::Document const &, Options)

Classifies a document into categories. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::ClassifyTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.ClassifyTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L408)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ClassifyText(google::cloud::language::v2::ClassifyTextRequest const &, Options)

Classifies a document into categories. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::language::v2::ClassifyTextRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.language.v2.ClassifyTextRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L402). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::ClassifyTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.ClassifyTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L408)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ModerateText(google::cloud::language::v2::Document const &, Options)

Moderates a document for harmful and sensitive categories. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::ModerateTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.ModerateTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L449)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### ModerateText(google::cloud::language::v2::ModerateTextRequest const &, Options)

Moderates a document for harmful and sensitive categories. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::language::v2::ModerateTextRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.language.v2.ModerateTextRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L424). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::ModerateTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.ModerateTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L449)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnnotateText(google::cloud::language::v2::Document const &, google::cloud::language::v2::AnnotateTextRequest::Features const &, google::cloud::language::v2::EncodingType, Options)

A convenience method that provides all features in one call. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`features` |  `google::cloud::language::v2::AnnotateTextRequest::Features const &`   
Required. The enabled features.   
`encoding_type` |  `google::cloud::language::v2::EncodingType`   
The encoding type used by the API to calculate offsets.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnnotateTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnnotateTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L495)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnnotateText(google::cloud::language::v2::Document const &, google::cloud::language::v2::AnnotateTextRequest::Features const &, Options)

A convenience method that provides all features in one call. 

**Parameters**  
---  
**Name** | **Description**  
`document` |  `google::cloud::language::v2::Document const &`   
Required. Input document.   
`features` |  `google::cloud::language::v2::AnnotateTextRequest::Features const &`   
Required. The enabled features.   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnnotateTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnnotateTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L495)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
### AnnotateText(google::cloud::language::v2::AnnotateTextRequest const &, Options)

A convenience method that provides all features in one call. 

**Parameters**  
---  
**Name** | **Description**  
`request` |  `google::cloud::language::v2::AnnotateTextRequest const &`   
Unary RPCs, such as the one wrapped by this function, receive a single `request` proto message which includes all the inputs for the RPC. In this case, the proto message is a [google.cloud.language.v2.AnnotateTextRequest](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L466). Proto messages are converted to C++ classes by Protobuf, using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/).   
`opts` |  `Options`   
Optional. Override the class-level options, such as retry and backoff policies.   
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::language::v2::AnnotateTextResponse >` | the result of the RPC. The response message type ([google.cloud.language.v2.AnnotateTextResponse](https://github.com/googleapis/googleapis/blob/28769825ec5fa31815f172b0de490a84e74cb97a/google/cloud/language/v2/language_service.proto#L495)) is mapped to a C++ class using the [Protobuf mapping rules](https://protobuf.dev/reference/cpp/cpp-generated/). If the request fails, the [`StatusOr`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1StatusOr.html) contains the error details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
