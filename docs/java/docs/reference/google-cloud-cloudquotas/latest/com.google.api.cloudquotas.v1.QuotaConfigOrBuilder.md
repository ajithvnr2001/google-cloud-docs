---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaConfigOrBuilder
title: Interface QuotaConfigOrBuilder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:16.804346+00:00
---

# Interface QuotaConfigOrBuilder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QuotaConfigOrBuilder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface QuotaConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsAnnotations(String key)
    
    
    public abstract boolean containsAnnotations(String key)

Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotations() (deprecated)
    
    
    public abstract Map<String,String> getAnnotations()

Use [#getAnnotationsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaConfigOrBuilder#com_google_api_cloudquotas_v1_QuotaConfigOrBuilder_getAnnotationsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsCount()
    
    
    public abstract int getAnnotationsCount()

Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAnnotationsMap()
    
    
    public abstract Map<String,String> getAnnotationsMap()

Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getAnnotationsOrDefault(String key, String defaultValue)
    
    
    public abstract String getAnnotationsOrDefault(String key, String defaultValue)

Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getAnnotationsOrThrow(String key)
    
    
    public abstract String getAnnotationsOrThrow(String key)

Optional. The annotations map for clients to store small amounts of arbitrary data. Do not put PII or other sensitive information here. See <https://google.aip.dev/128#annotations>

`map<string, string> annotations = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getGrantedValue()
    
    
    public abstract Int64Value getGrantedValue()

Output only. Granted quota value.

` .google.protobuf.Int64Value granted_value = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Int64Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64Value.html)` | The grantedValue.  
  
### getGrantedValueOrBuilder()
    
    
    public abstract Int64ValueOrBuilder getGrantedValueOrBuilder()

Output only. Granted quota value.

` .google.protobuf.Int64Value granted_value = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Int64ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int64ValueOrBuilder.html)` |   
  
### getPreferredValue()
    
    
    public abstract long getPreferredValue()

Required. The preferred value. Must be greater than or equal to -1. If set to -1, it means the value is "unlimited".

`int64 preferred_value = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The preferredValue.  
  
### getRequestOrigin()
    
    
    public abstract QuotaConfig.Origin getRequestOrigin()

Output only. The origin of the quota preference request.

` .google.api.cloudquotas.v1.QuotaConfig.Origin request_origin = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaConfig.Origin](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaConfig.Origin)` | The requestOrigin.  
  
### getRequestOriginValue()
    
    
    public abstract int getRequestOriginValue()

Output only. The origin of the quota preference request.

` .google.api.cloudquotas.v1.QuotaConfig.Origin request_origin = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for requestOrigin.  
  
### getStateDetail()
    
    
    public abstract String getStateDetail()

Output only. Optional details about the state of this quota preference.

`string state_detail = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateDetail.  
  
### getStateDetailBytes()
    
    
    public abstract ByteString getStateDetailBytes()

Output only. Optional details about the state of this quota preference.

`string state_detail = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateDetail.  
  
### getTraceId()
    
    
    public abstract String getTraceId()

Output only. The trace id that the Google Cloud uses to provision the requested quota. This trace id may be used by the client to contact Cloud support to track the state of a quota preference request. The trace id is only produced for increase requests and is unique for each request. The quota decrease requests do not have a trace id.

`string trace_id = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The traceId.  
  
### getTraceIdBytes()
    
    
    public abstract ByteString getTraceIdBytes()

Output only. The trace id that the Google Cloud uses to provision the requested quota. This trace id may be used by the client to contact Cloud support to track the state of a quota preference request. The trace id is only produced for increase requests and is unique for each request. The quota decrease requests do not have a trace id.

`string trace_id = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for traceId.  
  
### hasGrantedValue()
    
    
    public abstract boolean hasGrantedValue()

Output only. Granted quota value.

` .google.protobuf.Int64Value granted_value = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the grantedValue field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
