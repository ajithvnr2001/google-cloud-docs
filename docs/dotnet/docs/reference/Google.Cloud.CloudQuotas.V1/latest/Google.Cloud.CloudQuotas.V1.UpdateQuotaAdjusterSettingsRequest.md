---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest
title: Cloud Quotas v1 API - Class UpdateQuotaAdjusterSettingsRequest (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:28.163140+00:00
---

# Cloud Quotas v1 API - Class UpdateQuotaAdjusterSettingsRequest (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class UpdateQuotaAdjusterSettingsRequest (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public sealed class UpdateQuotaAdjusterSettingsRequest : IMessage<UpdateQuotaAdjusterSettingsRequest>, IEquatable<UpdateQuotaAdjusterSettingsRequest>, IDeepCloneable<UpdateQuotaAdjusterSettingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1 API class UpdateQuotaAdjusterSettingsRequest.

Request for updating QuotaAdjusterSettings

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateQuotaAdjusterSettingsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### UpdateQuotaAdjusterSettingsRequest()
    
    
    public UpdateQuotaAdjusterSettingsRequest()

### UpdateQuotaAdjusterSettingsRequest(UpdateQuotaAdjusterSettingsRequest)
    
    
    public UpdateQuotaAdjusterSettingsRequest(UpdateQuotaAdjusterSettingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.UpdateQuotaAdjusterSettingsRequest)`  
  
  
## Properties 

### QuotaAdjusterSettings
    
    
    public QuotaAdjusterSettings QuotaAdjusterSettings { get; set; }

Required. The QuotaAdjusterSettings to update.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Optional. The list of fields to update.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. If set to true, checks the syntax of the request but doesn't update the quota adjuster settings value. Note that although a request can be valid, that doesn't guarantee that the request will be fulfilled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
