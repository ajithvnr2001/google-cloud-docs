---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest
title: Discovery Engine v1beta API - Class AdvancedCompleteQueryRequest (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:30.517221+00:00
---

# Discovery Engine v1beta API - Class AdvancedCompleteQueryRequest (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class AdvancedCompleteQueryRequest (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public sealed class AdvancedCompleteQueryRequest : IMessage<AdvancedCompleteQueryRequest>, IEquatable<AdvancedCompleteQueryRequest>, IDeepCloneable<AdvancedCompleteQueryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1beta API class AdvancedCompleteQueryRequest.

Request message for [CompletionService.AdvancedCompleteQuery][google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery] method. .

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AdvancedCompleteQueryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Constructors 

### AdvancedCompleteQueryRequest()
    
    
    public AdvancedCompleteQueryRequest()

### AdvancedCompleteQueryRequest(AdvancedCompleteQueryRequest)
    
    
    public AdvancedCompleteQueryRequest(AdvancedCompleteQueryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest)`  
  
  
## Properties 

### BoostSpec
    
    
    public AdvancedCompleteQueryRequest.Types.BoostSpec BoostSpec { get; set; }

Optional. Specification to boost suggestions matching the condition.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest.Types)[BoostSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest.Types.BoostSpec)` |   
  
### CompletionConfig
    
    
    public string CompletionConfig { get; set; }

Required. The completion_config of the parent dataStore or engine resource name for which the completion is performed, such as `projects/*/locations/global/collections/default_collection/dataStores/*/completionConfig` `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CompletionConfigAsCompletionConfigName
    
    
    public CompletionConfigName CompletionConfigAsCompletionConfigName { get; set; }

[CompletionConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CompletionConfigName)-typed view over the [CompletionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest#Google_Cloud_DiscoveryEngine_V1Beta_AdvancedCompleteQueryRequest_CompletionConfig) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CompletionConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CompletionConfigName)` |   
  
### ExperimentIds
    
    
    public RepeatedField<string> ExperimentIds { get; }

Optional. Experiment ids for this request.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IncludeTailSuggestions
    
    
    public bool IncludeTailSuggestions { get; set; }

Indicates if tail suggestions should be returned if there are no suggestions that match the full query. Even if set to true, if there are suggestions that match the full query, those are returned and no tail suggestions are returned.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Query
    
    
    public string Query { get; set; }

Required. The typeahead input used to fetch suggestions. Maximum length is 128 characters.

The query can not be empty for most of the suggestion types. If it is empty, an `INVALID_ARGUMENT` error is returned. The exception is when the suggestion_types contains only the type `RECENT_SEARCH`, the query can be an empty string. The is called "zero prefix" feature, which returns user's recently searched queries given the empty query.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QueryModel
    
    
    public string QueryModel { get; set; }

Specifies the autocomplete query model, which only applies to the QUERY SuggestionType. This overrides any model specified in the Configuration > Autocomplete section of the Cloud console. Currently supported values:

  * `document` \- Using suggestions generated from user-imported documents.
  * `search-history` \- Using suggestions generated from the past history of [SearchService.Search][google.cloud.discoveryengine.v1beta.SearchService.Search] API calls. Do not use it when there is no traffic for Search API.
  * `user-event` \- Using suggestions generated from user-imported search events.
  * `document-completable` \- Using suggestions taken directly from user-imported document fields marked as completable.



Default values:

  * `document` is the default model for regular dataStores.
  * `search-history` is the default model for site search dataStores.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SuggestionTypeSpecs
    
    
    public RepeatedField<AdvancedCompleteQueryRequest.Types.SuggestionTypeSpec> SuggestionTypeSpecs { get; }

Optional. Specification of each suggestion type.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest.Types)[SuggestionTypeSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest.Types.SuggestionTypeSpec)` |   
  
### SuggestionTypes
    
    
    public RepeatedField<AdvancedCompleteQueryRequest.Types.SuggestionType> SuggestionTypes { get; }

Optional. Suggestion types to return. If empty or unspecified, query suggestions are returned. Only one suggestion type is supported at the moment.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdvancedCompleteQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest.Types)[SuggestionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.AdvancedCompleteQueryRequest.Types.SuggestionType)` |   
  
### UserInfo
    
    
    public UserInfo UserInfo { get; set; }

Optional. Information about the end user.

This should be the same identifier information as [UserEvent.user_info][google.cloud.discoveryengine.v1beta.UserEvent.user_info] and [SearchRequest.user_info][google.cloud.discoveryengine.v1beta.SearchRequest.user_info].

**Property Value**  
---  
**Type** | **Description**  
`[UserInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UserInfo)` |   
  
### UserPseudoId
    
    
    public string UserPseudoId { get; set; }

Optional. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

This should be the same identifier as [UserEvent.user_pseudo_id][google.cloud.discoveryengine.v1beta.UserEvent.user_pseudo_id] and [SearchRequest.user_pseudo_id][google.cloud.discoveryengine.v1beta.SearchRequest.user_pseudo_id].

The field must be a UTF-8 encoded string with a length limit of 128

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
