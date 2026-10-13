---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest
title: Service Directory v1 API - Class UpdateServiceRequest (2.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:15.629048+00:00
---

# Service Directory v1 API - Class UpdateServiceRequest (2.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Directory v1 API - Class UpdateServiceRequest (2.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.7.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.6.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.5.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.4.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.3.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.2.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.1.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/2.0.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.4.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.3.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.2.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.1.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/1.0.0/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)


    
    
    public sealed class UpdateServiceRequest : IMessage<UpdateServiceRequest>, IEquatable<UpdateServiceRequest>, IDeepCloneable<UpdateServiceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Directory v1 API class UpdateServiceRequest.

The request message for [RegistrationService.UpdateService][google.cloud.servicedirectory.v1.RegistrationService.UpdateService].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateServiceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceDirectory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1)

## Assembly

Google.Cloud.ServiceDirectory.V1.dll

## Constructors 

### UpdateServiceRequest()
    
    
    public UpdateServiceRequest()

### UpdateServiceRequest(UpdateServiceRequest)
    
    
    public UpdateServiceRequest(UpdateServiceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.UpdateServiceRequest)`  
  
  
## Properties 

### Service
    
    
    public Service Service { get; set; }

Required. The updated service.

**Property Value**  
---  
**Type** | **Description**  
`[Service](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1/latest/Google.Cloud.ServiceDirectory.V1.Service)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. List of fields to be updated in this request.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
