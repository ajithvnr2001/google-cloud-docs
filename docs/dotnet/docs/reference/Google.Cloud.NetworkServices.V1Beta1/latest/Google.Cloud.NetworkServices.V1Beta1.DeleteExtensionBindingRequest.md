---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest
title: Network Services v1beta1 API - Class DeleteExtensionBindingRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:13.240550+00:00
---

# Network Services v1beta1 API - Class DeleteExtensionBindingRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Services v1beta1 API - Class DeleteExtensionBindingRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class DeleteExtensionBindingRequest : IMessage<DeleteExtensionBindingRequest>, IEquatable<DeleteExtensionBindingRequest>, IDeepCloneable<DeleteExtensionBindingRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Services v1beta1 API class DeleteExtensionBindingRequest.

Request used by the `DeleteExtensionBinding` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteExtensionBindingRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteExtensionBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteExtensionBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteExtensionBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkServices.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1)

## Assembly

Google.Cloud.NetworkServices.V1Beta1.dll

## Constructors 

### DeleteExtensionBindingRequest()
    
    
    public DeleteExtensionBindingRequest()

### DeleteExtensionBindingRequest(DeleteExtensionBindingRequest)
    
    
    public DeleteExtensionBindingRequest(DeleteExtensionBindingRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteExtensionBindingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest)`  
  
  
## Properties 

### Etag
    
    
    public string Etag { get; set; }

Optional. The etag of the ExtensionBinding to delete.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExtensionBindingName
    
    
    public ExtensionBindingName ExtensionBindingName { get; set; }

[ExtensionBindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ExtensionBindingName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.DeleteExtensionBindingRequest#Google_Cloud_NetworkServices_V1Beta1_DeleteExtensionBindingRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ExtensionBindingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkServices.V1Beta1/latest/Google.Cloud.NetworkServices.V1Beta1.ExtensionBindingName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. A name of the `ExtensionBinding` resource to delete. Must be in the format `projects/{project}/locations/{location}/extensionBindings/{extension_binding}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
