---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest
title: Identity Access Context Manager v1 API - Class ListAccessLevelsRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:43.100571+00:00
---

# Identity Access Context Manager v1 API - Class ListAccessLevelsRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Identity Access Context Manager v1 API - Class ListAccessLevelsRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.5.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.4.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.3.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.2.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.1.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/2.0.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.5.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.4.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.3.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/1.2.0/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)


    
    
    public sealed class ListAccessLevelsRequest : IMessage<ListAccessLevelsRequest>, IEquatable<ListAccessLevelsRequest>, IDeepCloneable<ListAccessLevelsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Identity Access Context Manager v1 API class ListAccessLevelsRequest.

A request to list all `AccessLevels` in an `AccessPolicy`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListAccessLevelsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListAccessLevelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListAccessLevelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListAccessLevelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Identity.AccessContextManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1)

## Assembly

Google.Identity.AccessContextManager.V1.dll

## Constructors 

### ListAccessLevelsRequest()
    
    
    public ListAccessLevelsRequest()

### ListAccessLevelsRequest(ListAccessLevelsRequest)
    
    
    public ListAccessLevelsRequest(ListAccessLevelsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListAccessLevelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest)`  
  
  
## Properties 

### AccessLevelFormat
    
    
    public LevelFormat AccessLevelFormat { get; set; }

Whether to return `BasicLevels` in the Cloud Common Expression language, as `CustomLevels`, rather than as `BasicLevels`. Defaults to returning `AccessLevels` in the format they were defined.

**Property Value**  
---  
**Type** | **Description**  
`[LevelFormat](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.LevelFormat)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Number of [Access Levels] [google.identity.accesscontextmanager.v1.AccessLevel] to include in the list. Default 100.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Next page token for the next batch of [Access Level] [google.identity.accesscontextmanager.v1.AccessLevel] instances. Defaults to the first page of results.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. Resource name for the access policy to list [Access Levels] [google.identity.accesscontextmanager.v1.AccessLevel] from.

Format: `accessPolicies/{policy_id}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsAccessPolicyName
    
    
    public AccessPolicyName ParentAsAccessPolicyName { get; set; }

[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.AccessPolicyName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.ListAccessLevelsRequest#Google_Identity_AccessContextManager_V1_ListAccessLevelsRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AccessPolicyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Identity.AccessContextManager.V1/latest/Google.Identity.AccessContextManager.V1.AccessPolicyName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
