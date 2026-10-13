---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference
title: Cloud Quotas v1 API - Class QuotaPreference (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:29.651184+00:00
---

# Cloud Quotas v1 API - Class QuotaPreference (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class QuotaPreference (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public sealed class QuotaPreference : IMessage<QuotaPreference>, IEquatable<QuotaPreference>, IDeepCloneable<QuotaPreference>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1 API class QuotaPreference.

QuotaPreference represents the preferred quota configuration specified for a project, folder or organization. There is only one QuotaPreference resource for a quota value targeting a unique set of dimensions.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuotaPreference

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### QuotaPreference()
    
    
    public QuotaPreference()

### QuotaPreference(QuotaPreference)
    
    
    public QuotaPreference(QuotaPreference other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QuotaPreference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference)`  
  
  
## Properties 

### ContactEmail
    
    
    public string ContactEmail { get; set; }

Input only. An email address that can be used to contact the user, in case Google Cloud needs more information to make a decision before additional quota can be granted.

When requesting a quota increase, the email address is required. When requesting a quota decrease, the email address is optional. For example, the email address is optional when the `QuotaConfig.preferred_value` is smaller than the `QuotaDetails.reset_value`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time stamp

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Dimensions
    
    
    public MapField<string, string> Dimensions { get; }

Immutable. The dimensions that this quota preference applies to. The key of the map entry is the name of a dimension, such as `region`, `zone`, `network_id`, and the value of the map entry is the dimension value.

If a dimension is missing from the map of dimensions, the quota preference applies to all the dimension values except for those that have other quota preferences configured for the specific value.

Note: QuotaPreferences can only be applied across all values of `user` and `resource` dimension. Do not set values for `user` or `resource` in the dimension map.

For example: `{"provider" : "Example Organization"}` where `provider` is a service-specific quota dimension and `Example Organization` is the provider name.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Optional. The current etag of the quota preference. If an etag is provided on update and does not match the current server's etag of the quota preference, the request will be blocked and an ABORTED error will be returned. See <https://google.aip.dev/134#etags> for more details on etags.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Justification
    
    
    public string Justification { get; set; }

The reason / justification for this quota preference.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Required except in the CREATE requests. The resource name of the quota preference. The path that follows `/locations` must be `/global`. For example: `projects/123/locations/global/quotaPreferences/my-config-for-us-east1`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaConfig
    
    
    public QuotaConfig QuotaConfig { get; set; }

Required. Preferred quota configuration.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaConfig)` |   
  
### QuotaId
    
    
    public string QuotaId { get; set; }

Required. The id of the quota to which the quota preference is applied. A quota name is unique in the service. For example, `CpusPerProjectPerRegion`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaPreferenceName
    
    
    public QuotaPreferenceName QuotaPreferenceName { get; set; }

[QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreference#Google_Cloud_CloudQuotas_V1_QuotaPreference_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaPreferenceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaPreferenceName)` |   
  
### Reconciling
    
    
    public bool Reconciling { get; set; }

Output only. Is the quota preference pending Google Cloud approval and fulfillment.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Service
    
    
    public string Service { get; set; }

Required. The name of the service to which the quota preference is applied.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Update time stamp

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
