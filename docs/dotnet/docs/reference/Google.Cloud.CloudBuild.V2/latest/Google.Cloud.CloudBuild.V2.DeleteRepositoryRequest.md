---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest
title: Cloud Build v2 API - Class DeleteRepositoryRequest (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:04.658746+00:00
---

# Cloud Build v2 API - Class DeleteRepositoryRequest (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v2 API - Class DeleteRepositoryRequest (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.4.0/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.3.0/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.2.0/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.1.0/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.0.0/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)


    
    
    public sealed class DeleteRepositoryRequest : IMessage<DeleteRepositoryRequest>, IEquatable<DeleteRepositoryRequest>, IDeepCloneable<DeleteRepositoryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Build v2 API class DeleteRepositoryRequest.

Message for deleting a Repository.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteRepositoryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudBuild.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2)

## Assembly

Google.Cloud.CloudBuild.V2.dll

## Constructors 

### DeleteRepositoryRequest()
    
    
    public DeleteRepositoryRequest()

### DeleteRepositoryRequest(DeleteRepositoryRequest)
    
    
    public DeleteRepositoryRequest(DeleteRepositoryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteRepositoryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest)`  
  
  
## Properties 

### Etag
    
    
    public string Etag { get; set; }

The current etag of the repository. If an etag is provided and does not match the current etag of the repository, deletion will be blocked and an ABORTED error will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the Repository to delete. Format: `projects/*/locations/*/connections/*/repositories/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RepositoryName
    
    
    public RepositoryName RepositoryName { get; set; }

[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.DeleteRepositoryRequest#Google_Cloud_CloudBuild_V2_DeleteRepositoryRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RepositoryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryName)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

If set, validate the request, but do not actually post it.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
