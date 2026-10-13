---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest
title: Cloud Quotas v1beta API - Class GetQuotaAdjusterSettingsRequest (1.0.0-beta04) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:37.525328+00:00
---

# Cloud Quotas v1beta API - Class GetQuotaAdjusterSettingsRequest (1.0.0-beta04)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1beta API - Class GetQuotaAdjusterSettingsRequest (1.0.0-beta04) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta04 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/1.0.0-beta03/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest)


    
    
    public sealed class GetQuotaAdjusterSettingsRequest : IMessage<GetQuotaAdjusterSettingsRequest>, IEquatable<GetQuotaAdjusterSettingsRequest>, IDeepCloneable<GetQuotaAdjusterSettingsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1beta API class GetQuotaAdjusterSettingsRequest.

Request for getting QuotaAdjusterSettings

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetQuotaAdjusterSettingsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta)

## Assembly

Google.Cloud.CloudQuotas.V1Beta.dll

## Constructors 

### GetQuotaAdjusterSettingsRequest()
    
    
    public GetQuotaAdjusterSettingsRequest()

### GetQuotaAdjusterSettingsRequest(GetQuotaAdjusterSettingsRequest)
    
    
    public GetQuotaAdjusterSettingsRequest(GetQuotaAdjusterSettingsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetQuotaAdjusterSettingsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. Name of the `quotaAdjusterSettings` configuration. Only a single setting per project is supported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaAdjusterSettingsName
    
    
    public QuotaAdjusterSettingsName QuotaAdjusterSettingsName { get; set; }

[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettingsName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.GetQuotaAdjusterSettingsRequest#Google_Cloud_CloudQuotas_V1Beta_GetQuotaAdjusterSettingsRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1Beta/latest/Google.Cloud.CloudQuotas.V1Beta.QuotaAdjusterSettingsName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
