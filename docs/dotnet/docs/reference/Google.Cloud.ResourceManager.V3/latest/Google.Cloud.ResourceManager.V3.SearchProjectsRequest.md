---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest
title: Cloud Resource Manager v3 API - Class SearchProjectsRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:53:04.355045+00:00
---

# Cloud Resource Manager v3 API - Class SearchProjectsRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Resource Manager v3 API - Class SearchProjectsRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.5.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.4.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.3.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.2.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.1.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/2.0.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/1.2.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/1.1.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/1.0.0/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)


    
    
    public sealed class SearchProjectsRequest : IMessage<SearchProjectsRequest>, IEquatable<SearchProjectsRequest>, IDeepCloneable<SearchProjectsRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Resource Manager v3 API class SearchProjectsRequest.

The request sent to the [SearchProjects][google.cloud.resourcemanager.v3.Projects.SearchProjects] method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > SearchProjectsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[SearchProjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[SearchProjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[SearchProjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ResourceManager.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3)

## Assembly

Google.Cloud.ResourceManager.V3.dll

## Constructors 

### SearchProjectsRequest()
    
    
    public SearchProjectsRequest()

### SearchProjectsRequest(SearchProjectsRequest)
    
    
    public SearchProjectsRequest(SearchProjectsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[SearchProjectsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ResourceManager.V3/latest/Google.Cloud.ResourceManager.V3.SearchProjectsRequest)`  
  
  
## Properties 

### PageSize
    
    
    public int PageSize { get; set; }

Optional. The maximum number of projects to return in the response. The server can return fewer projects than requested. If unspecified, server picks an appropriate default.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Optional. A pagination token returned from a previous call to [ListProjects] [google.cloud.resourcemanager.v3.Projects.ListProjects] that indicates from where listing should continue.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Query
    
    
    public string Query { get; set; }

Optional. A query string for searching for projects that the caller has `resourcemanager.projects.get` permission to. If multiple fields are included in the query, then it will return results that match any of the fields. Some eligible fields are:

  * **`displayName`, `name`**: Filters by displayName.
  * **`parent`** : Project's parent (for example: `folders/123`, `organizations/*`). Prefer `parent` field over `parent.type` and `parent.id`.
  * **`parent.type`** : Parent's type: `folder` or `organization`.
  * **`parent.id`** : Parent's id number (for example: `123`).
  * **`id`, `projectId`**: Filters by projectId.
  * **`state`, `lifecycleState`**: Filters by state.
  * **`labels`** : Filters by label name or value.
  * **`labels.<key>` (where `<key>` is the name of a label)**: Filters by label name.



Search expressions are case insensitive.

Some examples queries:

  * **`name:how*`** : The project's name starts with "how".
  * **`name:Howl`** : The project's name is `Howl` or `howl`.
  * **`name:HOWL`** : Equivalent to above.
  * **`NAME:howl`** : Equivalent to above.
  * **`labels.color:*`** : The project has the label `color`.
  * **`labels.color:red`** : The project's label `color` has the value `red`.
  * **`labels.color:red labels.size:big`** : The project's label `color` has the value `red` or its label `size` has the value `big`.



If no query is specified, the call will return projects for which the user has the `resourcemanager.projects.get` permission.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
