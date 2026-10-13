---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoOrBuilder
title: Interface QuotaInfoOrBuilder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:18.124552+00:00
---

# Interface QuotaInfoOrBuilder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QuotaInfoOrBuilder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface QuotaInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContainerType()
    
    
    public abstract QuotaInfo.ContainerType getContainerType()

The container type of the QuotaInfo.

`.google.api.cloudquotas.v1.QuotaInfo.ContainerType container_type = 7;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaInfo.ContainerType](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaInfo.ContainerType)` | The containerType.  
  
### getContainerTypeValue()
    
    
    public abstract int getContainerTypeValue()

The container type of the QuotaInfo.

`.google.api.cloudquotas.v1.QuotaInfo.ContainerType container_type = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for containerType.  
  
### getDimensions(int index)
    
    
    public abstract String getDimensions(int index)

The dimensions the quota is defined on.

`repeated string dimensions = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The dimensions at the given index.  
  
### getDimensionsBytes(int index)
    
    
    public abstract ByteString getDimensionsBytes(int index)

The dimensions the quota is defined on.

`repeated string dimensions = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the dimensions at the given index.  
  
### getDimensionsCount()
    
    
    public abstract int getDimensionsCount()

The dimensions the quota is defined on.

`repeated string dimensions = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of dimensions.  
  
### getDimensionsInfos(int index)
    
    
    public abstract DimensionsInfo getDimensionsInfos(int index)

The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.

`repeated .google.api.cloudquotas.v1.DimensionsInfo dimensions_infos = 14;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionsInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.DimensionsInfo)` |   
  
### getDimensionsInfosCount()
    
    
    public abstract int getDimensionsInfosCount()

The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.

`repeated .google.api.cloudquotas.v1.DimensionsInfo dimensions_infos = 14;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsInfosList()
    
    
    public abstract List<DimensionsInfo> getDimensionsInfosList()

The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.

`repeated .google.api.cloudquotas.v1.DimensionsInfo dimensions_infos = 14;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DimensionsInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.DimensionsInfo)>` |   
  
### getDimensionsInfosOrBuilder(int index)
    
    
    public abstract DimensionsInfoOrBuilder getDimensionsInfosOrBuilder(int index)

The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.

`repeated .google.api.cloudquotas.v1.DimensionsInfo dimensions_infos = 14;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DimensionsInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.DimensionsInfoOrBuilder)` |   
  
### getDimensionsInfosOrBuilderList()
    
    
    public abstract List<? extends DimensionsInfoOrBuilder> getDimensionsInfosOrBuilderList()

The collection of dimensions info ordered by their dimensions from more specific ones to less specific ones.

`repeated .google.api.cloudquotas.v1.DimensionsInfo dimensions_infos = 14;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.cloudquotas.v1.DimensionsInfoOrBuilder>` |   
  
### getDimensionsList()
    
    
    public abstract List<String> getDimensionsList()

The dimensions the quota is defined on.

`repeated string dimensions = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the dimensions.  
  
### getIsConcurrent()
    
    
    public abstract boolean getIsConcurrent()

Whether the quota is a concurrent quota. Concurrent quotas are enforced on the total number of concurrent operations in flight at any given time.

`bool is_concurrent = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isConcurrent.  
  
### getIsFixed()
    
    
    public abstract boolean getIsFixed()

Whether the quota value is fixed or adjustable

`bool is_fixed = 13;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isFixed.  
  
### getIsPrecise()
    
    
    public abstract boolean getIsPrecise()

Whether this is a precise quota. A precise quota is tracked with absolute precision. In contrast, an imprecise quota is not tracked with precision.

`bool is_precise = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The isPrecise.  
  
### getMetric()
    
    
    public abstract String getMetric()

The metric of the quota. It specifies the resources consumption the quota is defined for. For example, `compute.googleapis.com/cpus`

`string metric = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metric.  
  
### getMetricBytes()
    
    
    public abstract ByteString getMetricBytes()

The metric of the quota. It specifies the resources consumption the quota is defined for. For example, `compute.googleapis.com/cpus`

`string metric = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for metric.  
  
### getMetricDisplayName()
    
    
    public abstract String getMetricDisplayName()

The display name of the quota metric

`string metric_display_name = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metricDisplayName.  
  
### getMetricDisplayNameBytes()
    
    
    public abstract ByteString getMetricDisplayNameBytes()

The display name of the quota metric

`string metric_display_name = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for metricDisplayName.  
  
### getMetricUnit()
    
    
    public abstract String getMetricUnit()

The unit in which the metric value is reported, e.g., "MByte".

`string metric_unit = 11;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metricUnit.  
  
### getMetricUnitBytes()
    
    
    public abstract ByteString getMetricUnitBytes()

The unit in which the metric value is reported, e.g., "MByte".

`string metric_unit = 11;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for metricUnit.  
  
### getName()
    
    
    public abstract String getName()

Resource name of this QuotaInfo. The ID component following "locations/" must be "global". For example, `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Resource name of this QuotaInfo. The ID component following "locations/" must be "global". For example, `projects/123/locations/global/services/compute.googleapis.com/quotaInfos/CpusPerProjectPerRegion`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getQuotaDisplayName()
    
    
    public abstract String getQuotaDisplayName()

The display name of the quota.

`string quota_display_name = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The quotaDisplayName.  
  
### getQuotaDisplayNameBytes()
    
    
    public abstract ByteString getQuotaDisplayNameBytes()

The display name of the quota.

`string quota_display_name = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for quotaDisplayName.  
  
### getQuotaId()
    
    
    public abstract String getQuotaId()

The id of the quota, which is unique within the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The quotaId.  
  
### getQuotaIdBytes()
    
    
    public abstract ByteString getQuotaIdBytes()

The id of the quota, which is unique within the service. For example, `CpusPerProjectPerRegion`

`string quota_id = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for quotaId.  
  
### getQuotaIncreaseEligibility()
    
    
    public abstract QuotaIncreaseEligibility getQuotaIncreaseEligibility()

Whether it is eligible to request a higher quota value for this quota.

`.google.api.cloudquotas.v1.QuotaIncreaseEligibility quota_increase_eligibility = 12; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaIncreaseEligibility](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaIncreaseEligibility)` | The quotaIncreaseEligibility.  
  
### getQuotaIncreaseEligibilityOrBuilder()
    
    
    public abstract QuotaIncreaseEligibilityOrBuilder getQuotaIncreaseEligibilityOrBuilder()

Whether it is eligible to request a higher quota value for this quota.

`.google.api.cloudquotas.v1.QuotaIncreaseEligibility quota_increase_eligibility = 12; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaIncreaseEligibilityOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaIncreaseEligibilityOrBuilder)` |   
  
### getRefreshInterval()
    
    
    public abstract String getRefreshInterval()

The reset time interval for the quota. Refresh interval applies to rate quota only. For example, "minute" for per minute, "day" for per day, or "10 seconds" for every 10 seconds.

`string refresh_interval = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The refreshInterval.  
  
### getRefreshIntervalBytes()
    
    
    public abstract ByteString getRefreshIntervalBytes()

The reset time interval for the quota. Refresh interval applies to rate quota only. For example, "minute" for per minute, "day" for per day, or "10 seconds" for every 10 seconds.

`string refresh_interval = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for refreshInterval.  
  
### getService()
    
    
    public abstract String getService()

The name of the service in which the quota is defined. For example, `compute.googleapis.com`

`string service = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The service.  
  
### getServiceBytes()
    
    
    public abstract ByteString getServiceBytes()

The name of the service in which the quota is defined. For example, `compute.googleapis.com`

`string service = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for service.  
  
### getServiceRequestQuotaUri()
    
    
    public abstract String getServiceRequestQuotaUri()

URI to the page where users can request more quota for the cloud service—for example, <https://console.cloud.google.com/iam-admin/quotas>.

`string service_request_quota_uri = 17;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The serviceRequestQuotaUri.  
  
### getServiceRequestQuotaUriBytes()
    
    
    public abstract ByteString getServiceRequestQuotaUriBytes()

URI to the page where users can request more quota for the cloud service—for example, <https://console.cloud.google.com/iam-admin/quotas>.

`string service_request_quota_uri = 17;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for serviceRequestQuotaUri.  
  
### hasQuotaIncreaseEligibility()
    
    
    public abstract boolean hasQuotaIncreaseEligibility()

Whether it is eligible to request a higher quota value for this quota.

`.google.api.cloudquotas.v1.QuotaIncreaseEligibility quota_increase_eligibility = 12; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the quotaIncreaseEligibility field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
