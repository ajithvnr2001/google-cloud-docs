---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest
title: Cloud Storage v2 API - Class UpdateOrganizationIntelligenceConfigRequest (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:28.540008+00:00
---

# Cloud Storage v2 API - Class UpdateOrganizationIntelligenceConfigRequest (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Storage v2 API - Class UpdateOrganizationIntelligenceConfigRequest (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1 
    
    
    public sealed class UpdateOrganizationIntelligenceConfigRequest : IMessage<UpdateOrganizationIntelligenceConfigRequest>, IEquatable<UpdateOrganizationIntelligenceConfigRequest>, IDeepCloneable<UpdateOrganizationIntelligenceConfigRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Storage v2 API class UpdateOrganizationIntelligenceConfigRequest.

Request message to update the `IntelligenceConfig` resource associated with your organization.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateOrganizationIntelligenceConfigRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2)

## Assembly

Google.Cloud.Storage.Control.V2.dll

## Constructors 

### UpdateOrganizationIntelligenceConfigRequest()
    
    
    public UpdateOrganizationIntelligenceConfigRequest()

### UpdateOrganizationIntelligenceConfigRequest(UpdateOrganizationIntelligenceConfigRequest)
    
    
    public UpdateOrganizationIntelligenceConfigRequest(UpdateOrganizationIntelligenceConfigRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateOrganizationIntelligenceConfigRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.UpdateOrganizationIntelligenceConfigRequest)`  
  
  
## Properties 

### IntelligenceConfig
    
    
    public IntelligenceConfig IntelligenceConfig { get; set; }

Required. The `IntelligenceConfig` resource to be updated.

**Property Value**  
---  
**Type** | **Description**  
`[IntelligenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.IntelligenceConfig)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. The ID that uniquely identifies the request, preventing duplicate processing.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Required. The `update_mask` that specifies the fields within the `IntelligenceConfig` resource that should be modified by this update. Only the listed fields are updated.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
