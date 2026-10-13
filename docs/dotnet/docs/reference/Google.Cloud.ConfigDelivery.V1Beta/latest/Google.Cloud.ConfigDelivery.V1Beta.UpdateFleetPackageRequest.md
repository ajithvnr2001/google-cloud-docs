---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.UpdateFleetPackageRequest
title: Config Delivery v1beta API - Class UpdateFleetPackageRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:50:50.097197+00:00
---

# Config Delivery v1beta API - Class UpdateFleetPackageRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.UpdateFleetPackageRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1beta API - Class UpdateFleetPackageRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class UpdateFleetPackageRequest : IMessage<UpdateFleetPackageRequest>, IEquatable<UpdateFleetPackageRequest>, IDeepCloneable<UpdateFleetPackageRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Config Delivery v1beta API class UpdateFleetPackageRequest.

Message for updating a FleetPackage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateFleetPackageRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.UpdateFleetPackageRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.UpdateFleetPackageRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.UpdateFleetPackageRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta)

## Assembly

Google.Cloud.ConfigDelivery.V1Beta.dll

## Constructors 

### UpdateFleetPackageRequest()
    
    
    public UpdateFleetPackageRequest()

### UpdateFleetPackageRequest(UpdateFleetPackageRequest)
    
    
    public UpdateFleetPackageRequest(UpdateFleetPackageRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.UpdateFleetPackageRequest)`  
  
  
## Properties 

### FleetPackage
    
    
    public FleetPackage FleetPackage { get; set; }

Required. The resource being updated

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackage)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. Field mask is used to specify the fields to be overwritten in the FleetPackage resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
