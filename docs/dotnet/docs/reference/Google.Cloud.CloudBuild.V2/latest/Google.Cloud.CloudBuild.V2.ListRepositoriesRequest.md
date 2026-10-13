---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest
title: Cloud Build v2 API - Class ListRepositoriesRequest (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:49.976048+00:00
---

# Cloud Build v2 API - Class ListRepositoriesRequest (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v2 API - Class ListRepositoriesRequest (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.4.0/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.3.0/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.2.0/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.1.0/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.0.0/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)


    
    
    public sealed class ListRepositoriesRequest : IMessage<ListRepositoriesRequest>, IEquatable<ListRepositoriesRequest>, IDeepCloneable<ListRepositoriesRequest>, IBufferMessage, IMessage, IPageRequest

Reference documentation and code samples for the Cloud Build v2 API class ListRepositoriesRequest.

Message for requesting list of Repositories.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListRepositoriesRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html), [IPageRequest](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.IPageRequest.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudBuild.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2)

## Assembly

Google.Cloud.CloudBuild.V2.dll

## Constructors 

### ListRepositoriesRequest()
    
    
    public ListRepositoriesRequest()

### ListRepositoriesRequest(ListRepositoriesRequest)
    
    
    public ListRepositoriesRequest(ListRepositoriesRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListRepositoriesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest)`  
  
  
## Properties 

### Filter
    
    
    public string Filter { get; set; }

A filter expression that filters resources listed in the response. Expressions must follow API improvement proposal [AIP-160](https://google.aip.dev/160). e.g. `remote_uri:"https://github.com*"`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PageSize
    
    
    public int PageSize { get; set; }

Number of results to return in the list.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### PageToken
    
    
    public string PageToken { get; set; }

Page start.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The parent, which owns this collection of Repositories. Format: `projects/*/locations/*/connections/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsConnectionName
    
    
    public ConnectionName ParentAsConnectionName { get; set; }

[ConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ConnectionName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ListRepositoriesRequest#Google_Cloud_CloudBuild_V2_ListRepositoriesRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ConnectionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.ConnectionName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
