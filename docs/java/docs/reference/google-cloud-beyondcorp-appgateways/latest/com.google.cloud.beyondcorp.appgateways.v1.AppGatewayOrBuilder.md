---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGatewayOrBuilder
title: Interface AppGatewayOrBuilder (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:05.120902+00:00
---

# Interface AppGatewayOrBuilder (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGatewayOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AppGatewayOrBuilder (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AppGatewayOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Resource labels to represent user provided metadata.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllocatedConnections(int index)
    
    
    public abstract AppGateway.AllocatedConnection getAllocatedConnections(int index)

Output only. A list of connections allocated for the Gateway

` repeated .google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection allocated_connections = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppGateway.AllocatedConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection)` |   
  
### getAllocatedConnectionsCount()
    
    
    public abstract int getAllocatedConnectionsCount()

Output only. A list of connections allocated for the Gateway

` repeated .google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection allocated_connections = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAllocatedConnectionsList()
    
    
    public abstract List<AppGateway.AllocatedConnection> getAllocatedConnectionsList()

Output only. A list of connections allocated for the Gateway

` repeated .google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection allocated_connections = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AllocatedConnection](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection)>` |   
  
### getAllocatedConnectionsOrBuilder(int index)
    
    
    public abstract AppGateway.AllocatedConnectionOrBuilder getAllocatedConnectionsOrBuilder(int index)

Output only. A list of connections allocated for the Gateway

` repeated .google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection allocated_connections = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AppGateway.AllocatedConnectionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnectionOrBuilder)` |   
  
### getAllocatedConnectionsOrBuilderList()
    
    
    public abstract List<? extends AppGateway.AllocatedConnectionOrBuilder> getAllocatedConnectionsOrBuilderList()

Output only. A list of connections allocated for the Gateway

` repeated .google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnection allocated_connections = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.beyondcorp.appgateways.v1.AppGateway.AllocatedConnectionOrBuilder>` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. An arbitrary user-provided name for the AppGateway. Cannot exceed 64 characters.

`string display_name = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. An arbitrary user-provided name for the AppGateway. Cannot exceed 64 characters.

`string display_name = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getHostType()
    
    
    public abstract AppGateway.HostType getHostType()

Required. The type of hosting used by the AppGateway.

` .google.cloud.beyondcorp.appgateways.v1.AppGateway.HostType host_type = 11 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AppGateway.HostType](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGateway.HostType)` | The hostType.  
  
### getHostTypeValue()
    
    
    public abstract int getHostTypeValue()

Required. The type of hosting used by the AppGateway.

` .google.cloud.beyondcorp.appgateways.v1.AppGateway.HostType host_type = 11 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for hostType.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGatewayOrBuilder#com_google_cloud_beyondcorp_appgateways_v1_AppGatewayOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Resource labels to represent user provided metadata.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Resource labels to represent user provided metadata.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Resource labels to represent user provided metadata.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

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

Optional. Resource labels to represent user provided metadata.

`map<string, string> labels = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

Required. Unique resource name of the AppGateway. The name is ignored when creating an AppGateway.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. Unique resource name of the AppGateway. The name is ignored when creating an AppGateway.

`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getState()
    
    
    public abstract AppGateway.State getState()

Output only. The current state of the AppGateway.

` .google.cloud.beyondcorp.appgateways.v1.AppGateway.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AppGateway.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGateway.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state of the AppGateway.

` .google.cloud.beyondcorp.appgateways.v1.AppGateway.State state = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getType()
    
    
    public abstract AppGateway.Type getType()

Required. The type of network connectivity used by the AppGateway.

` .google.cloud.beyondcorp.appgateways.v1.AppGateway.Type type = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AppGateway.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appgateways/latest/com.google.cloud.beyondcorp.appgateways.v1.AppGateway.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Required. The type of network connectivity used by the AppGateway.

` .google.cloud.beyondcorp.appgateways.v1.AppGateway.Type type = 7 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. A unique identifier for the instance generated by the system.

`string uid = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. A unique identifier for the instance generated by the system.

`string uid = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Timestamp when the resource was last modified.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Timestamp when the resource was last modified.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getUri()
    
    
    public abstract String getUri()

Output only. Server-defined URI for this resource.

`string uri = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

Output only. Server-defined URI for this resource.

`string uri = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Timestamp when the resource was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Timestamp when the resource was last modified.

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
