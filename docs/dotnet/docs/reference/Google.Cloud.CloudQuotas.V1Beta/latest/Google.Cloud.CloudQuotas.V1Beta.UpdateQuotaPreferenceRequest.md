---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest
title: Cloud Quotas v1beta API - Class UpdateQuotaPreferenceRequest (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:50.541249+00:00
---

# Cloud Quotas v1beta API - Class UpdateQuotaPreferenceRequest (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1beta API - Class UpdateQuotaPreferenceRequest (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/1.0.0-beta03/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest)


    
    
    public sealed class UpdateQuotaPreferenceRequest : IMessage<UpdateQuotaPreferenceRequest>, IEquatable<UpdateQuotaPreferenceRequest>, IDeepCloneable<UpdateQuotaPreferenceRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1beta API class UpdateQuotaPreferenceRequest.

Message for updating a QuotaPreference

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UpdateQuotaPreferenceRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta)

## Assembly

Google.Cloud.CloudQuotas.V1Beta.dll

## Constructors 

### UpdateQuotaPreferenceRequest()
    
    
    public UpdateQuotaPreferenceRequest()

### UpdateQuotaPreferenceRequest(UpdateQuotaPreferenceRequest)
    
    
    public UpdateQuotaPreferenceRequest(UpdateQuotaPreferenceRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[UpdateQuotaPreferenceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.UpdateQuotaPreferenceRequest)`  
  
  
## Properties 

### AllowMissing
    
    
    public bool AllowMissing { get; set; }

Optional. If set to true, and the quota preference is not found, a new one will be created. In this situation, `update_mask` is ignored.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IgnoreSafetyChecks
    
    
    public RepeatedField<QuotaSafetyCheck> IgnoreSafetyChecks { get; }

The list of quota safety checks to be ignored.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[QuotaSafetyCheck](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaSafetyCheck)` |   
  
### QuotaPreference
    
    
    public QuotaPreference QuotaPreference { get; set; }

Required. The resource being updated

**Property Value**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaPreference)` |   
  
### UpdateMask
    
    
    public FieldMask UpdateMask { get; set; }

Optional. Field mask is used to specify the fields to be overwritten in the QuotaPreference resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten.

**Property Value**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)` |   
  
### ValidateOnly
    
    
    public bool ValidateOnly { get; set; }

Optional. If set to true, validate the request, but do not actually update. Note that a request being valid does not mean that the request is guaranteed to be fulfilled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
