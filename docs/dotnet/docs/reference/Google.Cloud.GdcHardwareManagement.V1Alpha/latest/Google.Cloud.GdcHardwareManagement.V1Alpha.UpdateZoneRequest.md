---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest
title: GDC Hardware Management v1alpha API - Class UpdateZoneRequest (1.0.0-alpha08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:49.789101+00:00
---

# GDC Hardware Management v1alpha API - Class UpdateZoneRequest (1.0.0-alpha08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  GDC Hardware Management v1alpha API - Class UpdateZoneRequest (1.0.0-alpha08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-alpha08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest)
  * [ 1.0.0-alpha07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/1.0.0-alpha07/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest)


    
    
    public sealed class UpdateZoneRequest : IMessage<UpdateZoneRequest>, IEquatable<UpdateZoneRequest>, IDeepCloneable<UpdateZoneRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the GDC Hardware Management v1alpha API class UpdateZoneRequest.

A request to update a zone.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateZoneRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateZoneRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateZoneRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateZoneRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.GdcHardwareManagement.V1Alpha](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha)

## Assembly

Google.Cloud.GdcHardwareManagement.V1Alpha.dll

## Constructors 

### UpdateZoneRequest()
    
    
    public UpdateZoneRequest()

### UpdateZoneRequest(UpdateZoneRequest)
    
    
    public UpdateZoneRequest(UpdateZoneRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateZoneRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.UpdateZoneRequest)`  
  
  
## Properties 

### RequestId
    
    
    public string RequestId { get; set; }

Optional. An optional unique identifier for this request. See [AIP-155](https://google.aip.dev/155).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. A mask to specify the fields in the Zone to overwrite with this update. The fields specified in the update_mask are relative to the zone, not the full request. A field will be overwritten if it is in the mask. If you don't provide a mask then all fields will be overwritten.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### Zone
    
    
    public Zone Zone { get; set; }

Required. The zone to update.

**Property Value**  
---  
**Type** | **Description**  
`[Zone](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.GdcHardwareManagement.V1Alpha/latest/Google.Cloud.GdcHardwareManagement.V1Alpha.Zone)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
