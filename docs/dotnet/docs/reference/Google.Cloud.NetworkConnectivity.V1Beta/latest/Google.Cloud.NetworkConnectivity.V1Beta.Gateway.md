---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway
title: Network Connectivity v1beta API - Class Gateway (1.0.0-beta02) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:15.849534+00:00
---

# Network Connectivity v1beta API - Class Gateway (1.0.0-beta02)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1beta API - Class Gateway (1.0.0-beta02) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta02 (latest)  1.0.0-beta01 
    
    
    public sealed class Gateway : IMessage<Gateway>, IEquatable<Gateway>, IDeepCloneable<Gateway>, IBufferMessage, IMessage

Reference documentation and code samples for the Network Connectivity v1beta API class Gateway.

A gateway that can apply specialized traffic processing.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Gateway

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Gateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Gateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Gateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.NetworkConnectivity.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta)

## Assembly

Google.Cloud.NetworkConnectivity.V1Beta.dll

## Constructors 

### Gateway()
    
    
    public Gateway()

### Gateway(Gateway)
    
    
    public Gateway(Gateway other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Gateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway)`  
  
  
## Properties 

### Capacity
    
    
    public Gateway.Types.GatewayCapacity Capacity { get; set; }

Optional. The aggregate processing capacity of this gateway.

**Property Value**  
---  
**Type** | **Description**  
`[Gateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway.Types)[GatewayCapacity](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway.Types.GatewayCapacity)` |   
  
### CloudRouters
    
    
    public RepeatedField<string> CloudRouters { get; }

Output only. The list of Cloud Routers that are connected to this gateway. Should be in the form: https://www.googleapis.com/compute/v1/projects/{project}/regions/{region}/routers/{router}

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### IpRangeReservations
    
    
    public RepeatedField<Gateway.Types.IpRangeReservation> IpRangeReservations { get; }

Optional. A list of IP ranges that are reserved for this gateway's internal intfrastructure.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Gateway](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway.Types)[IpRangeReservation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway.Types.IpRangeReservation)` |   
  
### SacAttachment
    
    
    public string SacAttachment { get; set; }

Output only. The URI of the connected SACAttachment. Should be in the form: projects/{project}/locations/{location}/sacAttachments/{sac_attachment}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SacAttachmentAsSACAttachmentName
    
    
    public SACAttachmentName SacAttachmentAsSACAttachmentName { get; set; }

[SACAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SACAttachmentName)-typed view over the [SacAttachment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.Gateway#Google_Cloud_NetworkConnectivity_V1Beta_Gateway_SacAttachment) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SACAttachmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1Beta/latest/Google.Cloud.NetworkConnectivity.V1Beta.SACAttachmentName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
