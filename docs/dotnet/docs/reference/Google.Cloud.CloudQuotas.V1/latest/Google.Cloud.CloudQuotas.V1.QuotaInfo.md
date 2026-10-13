---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo
title: Cloud Quotas v1 API - Class QuotaInfo (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:26.696222+00:00
---

# Cloud Quotas v1 API - Class QuotaInfo (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Quotas v1 API - Class QuotaInfo (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0-beta05 
    
    
    public sealed class QuotaInfo : IMessage<QuotaInfo>, IEquatable<QuotaInfo>, IDeepCloneable<QuotaInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Quotas v1 API class QuotaInfo.

QuotaInfo represents information about a particular quota for a given project, folder or organization.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > QuotaInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudQuotas.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1)

## Assembly

Google.Cloud.CloudQuotas.V1.dll

## Constructors 

### QuotaInfo()
    
    
    public QuotaInfo()

### QuotaInfo(QuotaInfo)
    
    
    public QuotaInfo(QuotaInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)`  
  
  
## Properties 

### ContainerType
    
    
    public QuotaInfo.Types.ContainerType ContainerType { get; set; }

The container type of the QuotaInfo.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.Types)[ContainerType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo.Types.ContainerType)` |   
  
### Dimensions
    
    
    public RepeatedField<string> Dimensions { get; }

The dimensions the quota is defined on.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DimensionsInfos
    
    
    public RepeatedField<DimensionsInfo> DimensionsInfos { get; }

The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[DimensionsInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.DimensionsInfo)` |   
  
### IsConcurrent
    
    
    public bool IsConcurrent { get; set; }

Whether the quota is a concurrent quota. Concurrent quotas are enforced on the total number of concurrent operations in flight at any given time.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsFixed
    
    
    public bool IsFixed { get; set; }

Whether the quota value is fixed or adjustable

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsPrecise
    
    
    public bool IsPrecise { get; set; }

Whether this is a precise quota. A precise quota is tracked with absolute precision. In contrast, an imprecise quota is not tracked with precision.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Metric
    
    
    public string Metric { get; set; }

The metric of the quota. It specifies the resources consumption the quota is defined for. For example, `compute.googleapis.com/cpus`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MetricDisplayName
    
    
    public string MetricDisplayName { get; set; }

The display name of the quota metric

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MetricUnit
    
    
    public string MetricUnit { get; set; }

The unit in which the metric value is reported, e.g., "MByte".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Resource name of this QuotaInfo. The ID component following "locations/" must be "global". For example, `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaDisplayName
    
    
    public string QuotaDisplayName { get; set; }

The display name of the quota.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaId
    
    
    public string QuotaId { get; set; }

The id of the quota, which is unique within the service. For example, `CpusPerProjectPerRegion`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QuotaIncreaseEligibility
    
    
    public QuotaIncreaseEligibility QuotaIncreaseEligibility { get; set; }

Whether it is eligible to request a higher quota value for this quota.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaIncreaseEligibility](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaIncreaseEligibility)` |   
  
### QuotaInfoName
    
    
    public QuotaInfoName QuotaInfoName { get; set; }

[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfo#Google_Cloud_CloudQuotas_V1_QuotaInfo_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[QuotaInfoName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudQuotas.V1/latest/Google.Cloud.CloudQuotas.V1.QuotaInfoName)` |   
  
### RefreshInterval
    
    
    public string RefreshInterval { get; set; }

The reset time interval for the quota. Refresh interval applies to rate quota only. For example, "minute" for per minute, "day" for per day, or "10 seconds" for every 10 seconds.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Service
    
    
    public string Service { get; set; }

The name of the service in which the quota is defined. For example, `compute.googleapis.com`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceRequestQuotaUri
    
    
    public string ServiceRequestQuotaUri { get; set; }

URI to the page where users can request more quota for the cloud service—for example, <https://console.cloud.google.com/iam-admin/quotas>.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
