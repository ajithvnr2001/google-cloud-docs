---
url: https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1_1_1CompletionServiceConnection/
title: Class CompletionServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:44:17.016214+00:00
---

# Class CompletionServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1_1_1CompletionServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class CompletionServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

The [`CompletionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1_1_1CompletionServiceConnection) object for [`CompletionServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1_1_1CompletionServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`CompletionServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1_1_1CompletionServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`CompletionServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1_1_1CompletionServiceClient).

To create a concrete instance, see [`MakeCompletionServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/namespacegoogle_1_1cloud_1_1discoveryengine__v1).

For mocking, see [`discoveryengine_v1_mocks::MockCompletionServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/discoveryengine/latest/classgoogle_1_1cloud_1_1discoveryengine__v1__mocks_1_1MockCompletionServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CompleteQuery(google::cloud::discoveryengine::v1::CompleteQueryRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::discoveryengine::v1::CompleteQueryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::discoveryengine::v1::CompleteQueryResponse >` |   
  
### virtual ImportSuggestionDenyListEntries(google::cloud::discoveryengine::v1::ImportSuggestionDenyListEntriesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::discoveryengine::v1::ImportSuggestionDenyListEntriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::ImportSuggestionDenyListEntriesResponse > >` |   
  
### virtual ImportSuggestionDenyListEntries(NoAwaitTag, google::cloud::discoveryengine::v1::ImportSuggestionDenyListEntriesRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::discoveryengine::v1::ImportSuggestionDenyListEntriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ImportSuggestionDenyListEntries(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::ImportSuggestionDenyListEntriesResponse > >` |   
  
### virtual PurgeSuggestionDenyListEntries(google::cloud::discoveryengine::v1::PurgeSuggestionDenyListEntriesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::discoveryengine::v1::PurgeSuggestionDenyListEntriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::PurgeSuggestionDenyListEntriesResponse > >` |   
  
### virtual PurgeSuggestionDenyListEntries(NoAwaitTag, google::cloud::discoveryengine::v1::PurgeSuggestionDenyListEntriesRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::discoveryengine::v1::PurgeSuggestionDenyListEntriesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual PurgeSuggestionDenyListEntries(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::PurgeSuggestionDenyListEntriesResponse > >` |   
  
### virtual ImportCompletionSuggestions(google::cloud::discoveryengine::v1::ImportCompletionSuggestionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::discoveryengine::v1::ImportCompletionSuggestionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::ImportCompletionSuggestionsResponse > >` |   
  
### virtual ImportCompletionSuggestions(NoAwaitTag, google::cloud::discoveryengine::v1::ImportCompletionSuggestionsRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::discoveryengine::v1::ImportCompletionSuggestionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ImportCompletionSuggestions(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::ImportCompletionSuggestionsResponse > >` |   
  
### virtual PurgeCompletionSuggestions(google::cloud::discoveryengine::v1::PurgeCompletionSuggestionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::discoveryengine::v1::PurgeCompletionSuggestionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::PurgeCompletionSuggestionsResponse > >` |   
  
### virtual PurgeCompletionSuggestions(NoAwaitTag, google::cloud::discoveryengine::v1::PurgeCompletionSuggestionsRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::discoveryengine::v1::PurgeCompletionSuggestionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual PurgeCompletionSuggestions(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::discoveryengine::v1::PurgeCompletionSuggestionsResponse > >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
