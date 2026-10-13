---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest
title: Config Delivery v1beta API - Class GetFleetPackageRequest (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:42.502422+00:00
---

# Config Delivery v1beta API - Class GetFleetPackageRequest (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Config Delivery v1beta API - Class GetFleetPackageRequest (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public sealed class GetFleetPackageRequest : IMessage<GetFleetPackageRequest>, IEquatable<GetFleetPackageRequest>, IDeepCloneable<GetFleetPackageRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Config Delivery v1beta API class GetFleetPackageRequest.

Message for getting a FleetPackage

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetFleetPackageRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ConfigDelivery.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta)

## Assembly

Google.Cloud.ConfigDelivery.V1Beta.dll

## Constructors 

### GetFleetPackageRequest()
    
    
    public GetFleetPackageRequest()

### GetFleetPackageRequest(GetFleetPackageRequest)
    
    
    public GetFleetPackageRequest(GetFleetPackageRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetFleetPackageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest)`  
  
  
## Properties 

### FleetPackageName
    
    
    public FleetPackageName FleetPackageName { get; set; }

[FleetPackageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackageName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.GetFleetPackageRequest#Google_Cloud_ConfigDelivery_V1Beta_GetFleetPackageRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FleetPackageName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfigDelivery.V1Beta/latest/Google.Cloud.ConfigDelivery.V1Beta.FleetPackageName)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Name of the resource

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
