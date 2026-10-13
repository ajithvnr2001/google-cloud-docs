---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginOrBuilder
title: Interface WasmPluginOrBuilder (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:32.834331+00:00
---

# Interface WasmPluginOrBuilder (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface WasmPluginOrBuilder (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface WasmPluginOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Set of labels associated with the `WasmPlugin` resource.

The format must comply with [the following requirements](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements).

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsVersions(String key)
    
    
    public abstract boolean containsVersions(String key)

Optional. All versions of this `WasmPlugin` resource in the key-value format. The key is the resource ID, and the value is the `VersionDetails` object.

Lets you create or update a `WasmPlugin` resource and its versions in a single request. When the `main_version_id` field is not empty, it must point to one of the `VersionDetails` objects in the map.

If provided in a `PATCH` request, the new versions replace the previous set. Any version omitted from the `versions` field is removed. Because the `WasmPluginVersion` resource is immutable, if a `WasmPluginVersion` resource with the same name already exists and differs, the request fails.

Note: In a `GET` request, this field is populated only if the field `GetWasmPluginRequest.view` is set to `WASM_PLUGIN_VIEW_FULL`.

` map<string, .google.cloud.networkservices.v1.WasmPlugin.VersionDetails> versions = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. A human-readable description of the resource.

`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. A human-readable description of the resource.

`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginOrBuilder#com_google_cloud_networkservices_v1_WasmPluginOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Set of labels associated with the `WasmPlugin` resource.

The format must comply with [the following requirements](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements).

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Set of labels associated with the `WasmPlugin` resource.

The format must comply with [the following requirements](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements).

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Set of labels associated with the `WasmPlugin` resource.

The format must comply with [the following requirements](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements).

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. Set of labels associated with the `WasmPlugin` resource.

The format must comply with [the following requirements](https://docs.cloud.google.com/compute/docs/labeling-resources#requirements).

`map<string, string> labels = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLogConfig()
    
    
    public abstract WasmPlugin.LogConfig getLogConfig()

Optional. Specifies the logging options for the activity performed by this plugin. If logging is enabled, plugin logs are exported to Cloud Logging. Note that the settings relate to the logs generated by using logging statements in your Wasm code.

` .google.cloud.networkservices.v1.WasmPlugin.LogConfig log_config = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin.LogConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.LogConfig)` | The logConfig.  
  
### getLogConfigOrBuilder()
    
    
    public abstract WasmPlugin.LogConfigOrBuilder getLogConfigOrBuilder()

Optional. Specifies the logging options for the activity performed by this plugin. If logging is enabled, plugin logs are exported to Cloud Logging. Note that the settings relate to the logs generated by using logging statements in your Wasm code.

` .google.cloud.networkservices.v1.WasmPlugin.LogConfig log_config = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin.LogConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.LogConfigOrBuilder)` |   
  
### getMainVersionId()
    
    
    public abstract String getMainVersionId()

Optional. The ID of the `WasmPluginVersion` resource that is the currently serving one. The version referred to must be a child of this `WasmPlugin` resource.

`string main_version_id = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mainVersionId.  
  
### getMainVersionIdBytes()
    
    
    public abstract ByteString getMainVersionIdBytes()

Optional. The ID of the `WasmPluginVersion` resource that is the currently serving one. The version referred to must be a child of this `WasmPlugin` resource.

`string main_version_id = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mainVersionId.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Name of the `WasmPlugin` resource in the following format: `projects/{project}/locations/{location}/wasmPlugins/{wasm_plugin}`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Name of the `WasmPlugin` resource in the following format: `projects/{project}/locations/{location}/wasmPlugins/{wasm_plugin}`.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getUsedBy(int index)
    
    
    public abstract WasmPlugin.UsedBy getUsedBy(int index)

Output only. List of all [extensions](https://cloud.google.com/service-extensions/docs/overview) that use this `WasmPlugin` resource.

` repeated .google.cloud.networkservices.v1.WasmPlugin.UsedBy used_by = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin.UsedBy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.UsedBy)` |   
  
### getUsedByCount()
    
    
    public abstract int getUsedByCount()

Output only. List of all [extensions](https://cloud.google.com/service-extensions/docs/overview) that use this `WasmPlugin` resource.

` repeated .google.cloud.networkservices.v1.WasmPlugin.UsedBy used_by = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUsedByList()
    
    
    public abstract List<WasmPlugin.UsedBy> getUsedByList()

Output only. List of all [extensions](https://cloud.google.com/service-extensions/docs/overview) that use this `WasmPlugin` resource.

` repeated .google.cloud.networkservices.v1.WasmPlugin.UsedBy used_by = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[UsedBy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.UsedBy)>` |   
  
### getUsedByOrBuilder(int index)
    
    
    public abstract WasmPlugin.UsedByOrBuilder getUsedByOrBuilder(int index)

Output only. List of all [extensions](https://cloud.google.com/service-extensions/docs/overview) that use this `WasmPlugin` resource.

` repeated .google.cloud.networkservices.v1.WasmPlugin.UsedBy used_by = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin.UsedByOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.UsedByOrBuilder)` |   
  
### getUsedByOrBuilderList()
    
    
    public abstract List<? extends WasmPlugin.UsedByOrBuilder> getUsedByOrBuilderList()

Output only. List of all [extensions](https://cloud.google.com/service-extensions/docs/overview) that use this `WasmPlugin` resource.

` repeated .google.cloud.networkservices.v1.WasmPlugin.UsedBy used_by = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.networkservices.v1.WasmPlugin.UsedByOrBuilder>` |   
  
### getVersions() (deprecated)
    
    
    public abstract Map<String,WasmPlugin.VersionDetails> getVersions()

Use [#getVersionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginOrBuilder#com_google_cloud_networkservices_v1_WasmPluginOrBuilder_getVersionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[VersionDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.VersionDetails)>` |   
  
### getVersionsCount()
    
    
    public abstract int getVersionsCount()

Optional. All versions of this `WasmPlugin` resource in the key-value format. The key is the resource ID, and the value is the `VersionDetails` object.

Lets you create or update a `WasmPlugin` resource and its versions in a single request. When the `main_version_id` field is not empty, it must point to one of the `VersionDetails` objects in the map.

If provided in a `PATCH` request, the new versions replace the previous set. Any version omitted from the `versions` field is removed. Because the `WasmPluginVersion` resource is immutable, if a `WasmPluginVersion` resource with the same name already exists and differs, the request fails.

Note: In a `GET` request, this field is populated only if the field `GetWasmPluginRequest.view` is set to `WASM_PLUGIN_VIEW_FULL`.

` map<string, .google.cloud.networkservices.v1.WasmPlugin.VersionDetails> versions = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getVersionsMap()
    
    
    public abstract Map<String,WasmPlugin.VersionDetails> getVersionsMap()

Optional. All versions of this `WasmPlugin` resource in the key-value format. The key is the resource ID, and the value is the `VersionDetails` object.

Lets you create or update a `WasmPlugin` resource and its versions in a single request. When the `main_version_id` field is not empty, it must point to one of the `VersionDetails` objects in the map.

If provided in a `PATCH` request, the new versions replace the previous set. Any version omitted from the `versions` field is removed. Because the `WasmPluginVersion` resource is immutable, if a `WasmPluginVersion` resource with the same name already exists and differs, the request fails.

Note: In a `GET` request, this field is populated only if the field `GetWasmPluginRequest.view` is set to `WASM_PLUGIN_VIEW_FULL`.

` map<string, .google.cloud.networkservices.v1.WasmPlugin.VersionDetails> versions = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[VersionDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.VersionDetails)>` |   
  
### getVersionsOrDefault(String key, WasmPlugin.VersionDetails defaultValue)
    
    
    public abstract WasmPlugin.VersionDetails getVersionsOrDefault(String key, WasmPlugin.VersionDetails defaultValue)

Optional. All versions of this `WasmPlugin` resource in the key-value format. The key is the resource ID, and the value is the `VersionDetails` object.

Lets you create or update a `WasmPlugin` resource and its versions in a single request. When the `main_version_id` field is not empty, it must point to one of the `VersionDetails` objects in the map.

If provided in a `PATCH` request, the new versions replace the previous set. Any version omitted from the `versions` field is removed. Because the `WasmPluginVersion` resource is immutable, if a `WasmPluginVersion` resource with the same name already exists and differs, the request fails.

Note: In a `GET` request, this field is populated only if the field `GetWasmPluginRequest.view` is set to `WASM_PLUGIN_VIEW_FULL`.

` map<string, .google.cloud.networkservices.v1.WasmPlugin.VersionDetails> versions = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[WasmPlugin.VersionDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.VersionDetails)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin.VersionDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.VersionDetails)` |   
  
### getVersionsOrThrow(String key)
    
    
    public abstract WasmPlugin.VersionDetails getVersionsOrThrow(String key)

Optional. All versions of this `WasmPlugin` resource in the key-value format. The key is the resource ID, and the value is the `VersionDetails` object.

Lets you create or update a `WasmPlugin` resource and its versions in a single request. When the `main_version_id` field is not empty, it must point to one of the `VersionDetails` objects in the map.

If provided in a `PATCH` request, the new versions replace the previous set. Any version omitted from the `versions` field is removed. Because the `WasmPluginVersion` resource is immutable, if a `WasmPluginVersion` resource with the same name already exists and differs, the request fails.

Note: In a `GET` request, this field is populated only if the field `GetWasmPluginRequest.view` is set to `WASM_PLUGIN_VIEW_FULL`.

` map<string, .google.cloud.networkservices.v1.WasmPlugin.VersionDetails> versions = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[WasmPlugin.VersionDetails](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin.VersionDetails)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasLogConfig()
    
    
    public abstract boolean hasLogConfig()

Optional. Specifies the logging options for the activity performed by this plugin. If logging is enabled, plugin logs are exported to Cloud Logging. Note that the settings relate to the logs generated by using logging statements in your Wasm code.

` .google.cloud.networkservices.v1.WasmPlugin.LogConfig log_config = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the logConfig field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the resource was updated.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
