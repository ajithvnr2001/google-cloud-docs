---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ProducerQuotaPolicyOrBuilder
title: Interface ProducerQuotaPolicyOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:06.700181+00:00
---

# Interface ProducerQuotaPolicyOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ProducerQuotaPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ProducerQuotaPolicyOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.7  2.2.8 
    
    
    public interface ProducerQuotaPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsDimensions(String key)
    
    
    public abstract boolean containsDimensions(String key)

If this map is nonempty, then this policy applies only to specific values for dimensions defined in the limit unit.

For example, a policy on a limit with the unit `1/{project}/{region}` could contain an entry with the key `region` and the value `us-east-1`; the policy is only applied to quota consumed in that region.

This map has the following restrictions:

  * Keys that are not defined in the limit's unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key.
  * `project` is not a valid key; the project is already specified in the parent resource name.
  * `user` is not a valid key; the API does not support quota policies that apply only to a specific user.
  * If `region` appears as a key, its value must be a valid Cloud region.
  * If `zone` appears as a key, its value must be a valid Cloud zone.
  * If any valid key other than `region` or `zone` appears in the map, then all valid keys other than `region` or `zone` must also appear in the map.



`map<string, string> dimensions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getContainer()
    
    
    public abstract String getContainer()

The cloud resource container at which the quota policy is created. The format is `{container_type}/{container_number}`

`string container = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The container.  
  
### getContainerBytes()
    
    
    public abstract ByteString getContainerBytes()

The cloud resource container at which the quota policy is created. The format is `{container_type}/{container_number}`

`string container = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for container.  
  
### getDimensions() (deprecated)
    
    
    public abstract Map<String,String> getDimensions()

Use [#getDimensionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-usage/latest/com.google.api.serviceusage.v1beta1.ProducerQuotaPolicyOrBuilder#com_google_api_serviceusage_v1beta1_ProducerQuotaPolicyOrBuilder_getDimensionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDimensionsCount()
    
    
    public abstract int getDimensionsCount()

If this map is nonempty, then this policy applies only to specific values for dimensions defined in the limit unit.

For example, a policy on a limit with the unit `1/{project}/{region}` could contain an entry with the key `region` and the value `us-east-1`; the policy is only applied to quota consumed in that region.

This map has the following restrictions:

  * Keys that are not defined in the limit's unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key.
  * `project` is not a valid key; the project is already specified in the parent resource name.
  * `user` is not a valid key; the API does not support quota policies that apply only to a specific user.
  * If `region` appears as a key, its value must be a valid Cloud region.
  * If `zone` appears as a key, its value must be a valid Cloud zone.
  * If any valid key other than `region` or `zone` appears in the map, then all valid keys other than `region` or `zone` must also appear in the map.



`map<string, string> dimensions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsMap()
    
    
    public abstract Map<String,String> getDimensionsMap()

If this map is nonempty, then this policy applies only to specific values for dimensions defined in the limit unit.

For example, a policy on a limit with the unit `1/{project}/{region}` could contain an entry with the key `region` and the value `us-east-1`; the policy is only applied to quota consumed in that region.

This map has the following restrictions:

  * Keys that are not defined in the limit's unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key.
  * `project` is not a valid key; the project is already specified in the parent resource name.
  * `user` is not a valid key; the API does not support quota policies that apply only to a specific user.
  * If `region` appears as a key, its value must be a valid Cloud region.
  * If `zone` appears as a key, its value must be a valid Cloud zone.
  * If any valid key other than `region` or `zone` appears in the map, then all valid keys other than `region` or `zone` must also appear in the map.



`map<string, string> dimensions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getDimensionsOrDefault(String key, String defaultValue)
    
    
    public abstract String getDimensionsOrDefault(String key, String defaultValue)

If this map is nonempty, then this policy applies only to specific values for dimensions defined in the limit unit.

For example, a policy on a limit with the unit `1/{project}/{region}` could contain an entry with the key `region` and the value `us-east-1`; the policy is only applied to quota consumed in that region.

This map has the following restrictions:

  * Keys that are not defined in the limit's unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key.
  * `project` is not a valid key; the project is already specified in the parent resource name.
  * `user` is not a valid key; the API does not support quota policies that apply only to a specific user.
  * If `region` appears as a key, its value must be a valid Cloud region.
  * If `zone` appears as a key, its value must be a valid Cloud zone.
  * If any valid key other than `region` or `zone` appears in the map, then all valid keys other than `region` or `zone` must also appear in the map.



`map<string, string> dimensions = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDimensionsOrThrow(String key)
    
    
    public abstract String getDimensionsOrThrow(String key)

If this map is nonempty, then this policy applies only to specific values for dimensions defined in the limit unit.

For example, a policy on a limit with the unit `1/{project}/{region}` could contain an entry with the key `region` and the value `us-east-1`; the policy is only applied to quota consumed in that region.

This map has the following restrictions:

  * Keys that are not defined in the limit's unit are not valid keys. Any string appearing in {brackets} in the unit (besides {project} or {user}) is a defined key.
  * `project` is not a valid key; the project is already specified in the parent resource name.
  * `user` is not a valid key; the API does not support quota policies that apply only to a specific user.
  * If `region` appears as a key, its value must be a valid Cloud region.
  * If `zone` appears as a key, its value must be a valid Cloud zone.
  * If any valid key other than `region` or `zone` appears in the map, then all valid keys other than `region` or `zone` must also appear in the map.



`map<string, string> dimensions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetric()
    
    
    public abstract String getMetric()

The name of the metric to which this policy applies.

An example name would be: `compute.googleapis.com/cpus`

`string metric = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metric.  
  
### getMetricBytes()
    
    
    public abstract ByteString getMetricBytes()

The name of the metric to which this policy applies.

An example name would be: `compute.googleapis.com/cpus`

`string metric = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for metric.  
  
### getName()
    
    
    public abstract String getName()

The resource name of the policy. This name is generated by the server when the policy is created.

Example names would be: `organizations/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/producerQuotaPolicies/4a3f2c1d`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The resource name of the policy. This name is generated by the server when the policy is created.

Example names would be: `organizations/123/services/compute.googleapis.com/consumerQuotaMetrics/compute.googleapis.com%2Fcpus/limits/%2Fproject%2Fregion/producerQuotaPolicies/4a3f2c1d`

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPolicyValue()
    
    
    public abstract long getPolicyValue()

The quota policy value. Can be any nonnegative integer, or -1 (unlimited quota).

`int64 policy_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The policyValue.  
  
### getUnit()
    
    
    public abstract String getUnit()

The limit unit of the limit to which this policy applies.

An example unit would be: `1/{project}/{region}` Note that `{project}` and `{region}` are not placeholders in this example; the literal characters `{` and `}` occur in the string.

`string unit = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unit.  
  
### getUnitBytes()
    
    
    public abstract ByteString getUnitBytes()

The limit unit of the limit to which this policy applies.

An example unit would be: `1/{project}/{region}` Note that `{project}` and `{region}` are not placeholders in this example; the literal characters `{` and `}` occur in the string.

`string unit = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for unit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
