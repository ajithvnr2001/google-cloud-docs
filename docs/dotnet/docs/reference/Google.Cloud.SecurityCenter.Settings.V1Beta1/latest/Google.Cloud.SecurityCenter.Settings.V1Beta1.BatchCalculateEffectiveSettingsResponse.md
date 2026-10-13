---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse
title: Google Cloud Security Command Center Settings v1beta1 API - Class BatchCalculateEffectiveSettingsResponse (2.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:14.672892+00:00
---

# Google Cloud Security Command Center Settings v1beta1 API - Class BatchCalculateEffectiveSettingsResponse (2.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Security Command Center Settings v1beta1 API - Class BatchCalculateEffectiveSettingsResponse (2.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta05 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse)
  * [ 2.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/2.0.0-beta04/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse)
  * [ 1.0.0-beta04 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/1.0.0-beta04/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse)


    
    
    public sealed class BatchCalculateEffectiveSettingsResponse : IMessage<BatchCalculateEffectiveSettingsResponse>, IEquatable<BatchCalculateEffectiveSettingsResponse>, IDeepCloneable<BatchCalculateEffectiveSettingsResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Security Command Center Settings v1beta1 API class BatchCalculateEffectiveSettingsResponse.

Response message for BatchGetEffectiveSettings.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchCalculateEffectiveSettingsResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchCalculateEffectiveSettingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchCalculateEffectiveSettingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchCalculateEffectiveSettingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.SecurityCenter.Settings.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1)

## Assembly

Google.Cloud.SecurityCenter.Settings.V1Beta1.dll

## Constructors 

### BatchCalculateEffectiveSettingsResponse()
    
    
    public BatchCalculateEffectiveSettingsResponse()

### BatchCalculateEffectiveSettingsResponse(BatchCalculateEffectiveSettingsResponse)
    
    
    public BatchCalculateEffectiveSettingsResponse(BatchCalculateEffectiveSettingsResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchCalculateEffectiveSettingsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.BatchCalculateEffectiveSettingsResponse)`  
  
  
## Properties 

### Settings
    
    
    public RepeatedField<Settings> Settings { get; }

Settings requested.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Settings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.SecurityCenter.Settings.V1Beta1/latest/Google.Cloud.SecurityCenter.Settings.V1Beta1.Settings)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
