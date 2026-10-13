---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest
title: Service Directory v1beta1 API - Class DeleteServiceRequest (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:59.673245+00:00
---

# Service Directory v1beta1 API - Class DeleteServiceRequest (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Service Directory v1beta1 API - Class DeleteServiceRequest (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/2.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/1.0.0-beta06/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest)


    
    
    public sealed class DeleteServiceRequest : IMessage<DeleteServiceRequest>, IEquatable<DeleteServiceRequest>, IDeepCloneable<DeleteServiceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Service Directory v1beta1 API class DeleteServiceRequest.

The request message for [RegistrationService.DeleteService][google.cloud.servicedirectory.v1beta1.RegistrationService.DeleteService].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteServiceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ServiceDirectory.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1)

## Assembly

Google.Cloud.ServiceDirectory.V1Beta1.dll

## Constructors 

### DeleteServiceRequest()
    
    
    public DeleteServiceRequest()

### DeleteServiceRequest(DeleteServiceRequest)
    
    
    public DeleteServiceRequest(DeleteServiceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteServiceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The name of the service to delete.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceName
    
    
    public ServiceName ServiceName { get; set; }

[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ServiceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.DeleteServiceRequest#Google_Cloud_ServiceDirectory_V1Beta1_DeleteServiceRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ServiceDirectory.V1Beta1/latest/Google.Cloud.ServiceDirectory.V1Beta1.ServiceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
