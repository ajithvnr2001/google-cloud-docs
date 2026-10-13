---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest
title: Cloud Storage v2 API - Class ViewObjectFullContextRequest (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:59.126425+00:00
---

# Cloud Storage v2 API - Class ViewObjectFullContextRequest (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Storage v2 API - Class ViewObjectFullContextRequest (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1 
    
    
    public sealed class ViewObjectFullContextRequest : IMessage<ViewObjectFullContextRequest>, IEquatable<ViewObjectFullContextRequest>, IDeepCloneable<ViewObjectFullContextRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Storage v2 API class ViewObjectFullContextRequest.

Request message for ViewObjectFullContext.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ViewObjectFullContextRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2)

## Assembly

Google.Cloud.Storage.Control.V2.dll

## Constructors 

### ViewObjectFullContextRequest()
    
    
    public ViewObjectFullContextRequest()

### ViewObjectFullContextRequest(ViewObjectFullContextRequest)
    
    
    public ViewObjectFullContextRequest(ViewObjectFullContextRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ViewObjectFullContextRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest)`  
  
  
## Properties 

### ContextKey
    
    
    public string ContextKey { get; set; }

Required. The key of the object context to retrieve.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Generation
    
    
    public long Generation { get; set; }

Optional. If present, selects a specific revision of this object (as opposed to the latest version, the default).

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the object. Format: `projects/{project}/buckets/{bucket}/objects/{object}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ObjectName
    
    
    public ObjectName ObjectName { get; set; }

[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ViewObjectFullContextRequest#Google_Cloud_Storage_Control_V2_ViewObjectFullContextRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.ObjectName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
