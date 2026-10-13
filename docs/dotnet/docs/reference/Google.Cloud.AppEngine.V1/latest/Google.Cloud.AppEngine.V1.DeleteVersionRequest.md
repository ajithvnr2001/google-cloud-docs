---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest
title: App Engine v1 API - Class DeleteVersionRequest (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:53:56.588860+00:00
---

# App Engine v1 API - Class DeleteVersionRequest (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Engine v1 API - Class DeleteVersionRequest (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.4.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.3.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.2.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.1.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/2.0.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.4.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.3.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.2.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.1.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/1.0.0/Google.Cloud.AppEngine.V1.DeleteVersionRequest)


    
    
    public sealed class DeleteVersionRequest : IMessage<DeleteVersionRequest>, IEquatable<DeleteVersionRequest>, IDeepCloneable<DeleteVersionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the App Engine v1 API class DeleteVersionRequest.

Request message for `Versions.DeleteVersion`.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteVersionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1)

## Assembly

Google.Cloud.AppEngine.V1.dll

## Constructors 

### DeleteVersionRequest()
    
    
    public DeleteVersionRequest()

### DeleteVersionRequest(DeleteVersionRequest)
    
    
    public DeleteVersionRequest(DeleteVersionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteVersionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppEngine.V1/latest/Google.Cloud.AppEngine.V1.DeleteVersionRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Name of the resource requested. Example: `apps/myapp/services/default/versions/v1`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
