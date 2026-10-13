---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse
title: App Hub v1 API - Class LookupServiceProjectAttachmentResponse (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:47.666851+00:00
---

# App Hub v1 API - Class LookupServiceProjectAttachmentResponse (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Hub v1 API - Class LookupServiceProjectAttachmentResponse (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class LookupServiceProjectAttachmentResponse : IMessage<LookupServiceProjectAttachmentResponse>, IEquatable<LookupServiceProjectAttachmentResponse>, IDeepCloneable<LookupServiceProjectAttachmentResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the App Hub v1 API class LookupServiceProjectAttachmentResponse.

Response for LookupServiceProjectAttachment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > LookupServiceProjectAttachmentResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AppHub.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1)

## Assembly

Google.Cloud.AppHub.V1.dll

## Constructors 

### LookupServiceProjectAttachmentResponse()
    
    
    public LookupServiceProjectAttachmentResponse()

### LookupServiceProjectAttachmentResponse(LookupServiceProjectAttachmentResponse)
    
    
    public LookupServiceProjectAttachmentResponse(LookupServiceProjectAttachmentResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[LookupServiceProjectAttachmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.LookupServiceProjectAttachmentResponse)`  
  
  
## Properties 

### ServiceProjectAttachment
    
    
    public ServiceProjectAttachment ServiceProjectAttachment { get; set; }

Service project attachment for a project if exists, empty otherwise.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceProjectAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppHub.V1/latest/Google.Cloud.AppHub.V1.ServiceProjectAttachment)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
