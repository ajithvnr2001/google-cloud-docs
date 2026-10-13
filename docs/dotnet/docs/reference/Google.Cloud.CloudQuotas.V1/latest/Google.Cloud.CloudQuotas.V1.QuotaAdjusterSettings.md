---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings
title: Cloud Quotas v1 API - Class QuotaAdjusterSettings (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:23.865320+00:00
---

# Cloud Quotas v1 API - Class QuotaAdjusterSettings (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class QuotaAdjusterSettings (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public sealed class QuotaAdjusterSettings : IMessage<QuotaAdjusterSettings>, IEquatable<QuotaAdjusterSettings>, IDeepCloneable<QuotaAdjusterSettings>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1 API class QuotaAdjusterSettings.

The QuotaAdjusterSettings resource defines the settings for the Quota Adjuster.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuotaAdjusterSettings

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### QuotaAdjusterSettings()
    
    
    public QuotaAdjusterSettings()

### QuotaAdjusterSettings(QuotaAdjusterSettings)
    
    
    public QuotaAdjusterSettings(QuotaAdjusterSettings other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)`  
  
  
## Properties 

### Enablement
    
    
    public QuotaAdjusterSettings.Types.Enablement Enablement { get; set; }

Optional. The configured value of the enablement at the given resource.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings.Types)[Enablement](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings.Types.Enablement)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. The current ETag of the QuotaAdjusterSettings. If an ETag is provided on update and does not match the current server's ETag in the QuotaAdjusterSettings, the request is blocked and returns an ABORTED error. See <https://google.aip.dev/134#etags> for more details on ETags.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Inherited
    
    
    public bool Inherited { get; set; }

Optional. Indicates whether the setting is inherited or explicitly specified.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### InheritedFrom
    
    
    public string InheritedFrom { get; set; }

Output only. The resource container from which the setting is inherited. This refers to the nearest ancestor with enablement set (either ENABLED or DISABLED). The value can be an organizations/{organization_id}, folders/{folder_id}, or can be 'default' if no ancestor exists with enablement set. The value will be empty when enablement is directly set on this container.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. Name of the configuration, in the formats below:

  * For a project: projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings
  * For a folder: folders/FOLDER_NUMBER/locations/global/quotaAdjusterSettings
  * For an organization: organizations/ORGANIZATION_NUMBER/locations/global/quotaAdjusterSettings



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaAdjusterSettingsName
    
    
    public QuotaAdjusterSettingsName QuotaAdjusterSettingsName { get; set; }

[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettings#Google_Cloud_CloudQuotas_V1_QuotaAdjusterSettings_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaAdjusterSettingsName)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. The timestamp when the QuotaAdjusterSettings resource was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
