---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest
title: Discovery Engine v1 API - Class AnswerQueryRequest (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:53.672660+00:00
---

# Discovery Engine v1 API - Class AnswerQueryRequest (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class AnswerQueryRequest (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public sealed class AnswerQueryRequest : IMessage<AnswerQueryRequest>, IEquatable<AnswerQueryRequest>, IDeepCloneable<AnswerQueryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1 API class AnswerQueryRequest.

Request message for [ConversationalSearchService.AnswerQuery][google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnswerQueryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Constructors 

### AnswerQueryRequest()
    
    
    public AnswerQueryRequest()

### AnswerQueryRequest(AnswerQueryRequest)
    
    
    public AnswerQueryRequest(AnswerQueryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)`  
  
  
## Properties 

### AnswerGenerationSpec
    
    
    public AnswerQueryRequest.Types.AnswerGenerationSpec AnswerGenerationSpec { get; set; }

Answer generation specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[AnswerGenerationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.AnswerGenerationSpec)` |   
  
### AsynchronousMode
    
    
    [Obsolete]
    public bool AsynchronousMode { get; set; }

Deprecated: This field is deprecated. Streaming Answer API will be supported.

Asynchronous mode control.

If enabled, the response will be returned with answer/session resource name without final answer. The API users need to do the polling to get the latest status of answer/session by calling [ConversationalSearchService.GetAnswer][google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer] or [ConversationalSearchService.GetSession][google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession] method.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EndUserSpec
    
    
    public AnswerQueryRequest.Types.EndUserSpec EndUserSpec { get; set; }

Optional. End user specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[EndUserSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.EndUserSpec)` |   
  
### GroundingSpec
    
    
    public AnswerQueryRequest.Types.GroundingSpec GroundingSpec { get; set; }

Optional. Grounding specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[GroundingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.GroundingSpec)` |   
  
### Query
    
    
    public Query Query { get; set; }

Required. Current user query.

**Property Value**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Query)` |   
  
### QueryUnderstandingSpec
    
    
    public AnswerQueryRequest.Types.QueryUnderstandingSpec QueryUnderstandingSpec { get; set; }

Query understanding specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[QueryUnderstandingSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.QueryUnderstandingSpec)` |   
  
### RelatedQuestionsSpec
    
    
    public AnswerQueryRequest.Types.RelatedQuestionsSpec RelatedQuestionsSpec { get; set; }

Related questions specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[RelatedQuestionsSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.RelatedQuestionsSpec)` |   
  
### SafetySpec
    
    
    public AnswerQueryRequest.Types.SafetySpec SafetySpec { get; set; }

Model specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[SafetySpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.SafetySpec)` |   
  
### SearchSpec
    
    
    public AnswerQueryRequest.Types.SearchSpec SearchSpec { get; set; }

Search specification.

**Property Value**  
---  
**Type** | **Description**  
`[AnswerQueryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types)[SearchSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest.Types.SearchSpec)` |   
  
### ServingConfig
    
    
    public string ServingConfig { get; set; }

Required. The resource name of the Search serving config, such as `projects/*/locations/global/collections/default_collection/engines/*/servingConfigs/default_serving_config`, or `projects/*/locations/global/collections/default_collection/dataStores/*/servingConfigs/default_serving_config`. This field is used to identify the serving configuration name, set of models used to make the search.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServingConfigAsServingConfigName
    
    
    public ServingConfigName ServingConfigAsServingConfigName { get; set; }

[ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ServingConfigName)-typed view over the [ServingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest#Google_Cloud_DiscoveryEngine_V1_AnswerQueryRequest_ServingConfig) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServingConfigName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.ServingConfigName)` |   
  
### Session
    
    
    public string Session { get; set; }

The session resource name. Not required.

When session field is not set, the API is in sessionless mode.

We support auto session mode: users can use the wildcard symbol `-` as session ID. A new ID will be automatically generated and assigned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SessionAsSessionName
    
    
    public SessionName SessionAsSessionName { get; set; }

[SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SessionName)-typed view over the [Session](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.AnswerQueryRequest#Google_Cloud_DiscoveryEngine_V1_AnswerQueryRequest_Session) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SessionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.SessionName)` |   
  
### UserLabels
    
    
    public MapField<string, string> UserLabels { get; }

The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.



See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UserPseudoId
    
    
    public string UserPseudoId { get; set; }

A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.

This field should NOT have a fixed value such as `unknown_visitor`.

The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
