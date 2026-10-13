---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PrivateConnectionOrBuilder
title: Interface PrivateConnectionOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:55.729320+00:00
---

# Interface PrivateConnectionOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PrivateConnectionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PrivateConnectionOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PrivateConnectionOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.datastream.v1.PrivateConnectionOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.datastream.v1.PrivateConnectionOrBuilder)


    
    
    public interface PrivateConnectionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels.

`map<string, string> labels = 4;`

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

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. Display name.

`string display_name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. Display name.

`string display_name = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getError()
    
    
    public abstract Error getError()

Output only. In case of error, the details of the error in a user-friendly format.

`.google.events.cloud.datastream.v1.Error error = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Error](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.Error)` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract ErrorOrBuilder getErrorOrBuilder()

Output only. In case of error, the details of the error in a user-friendly format.

`.google.events.cloud.datastream.v1.Error error = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ErrorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.ErrorOrBuilder)` |   
  
### getLabels()
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PrivateConnectionOrBuilder#com_google_events_cloud_datastream_v1_PrivateConnectionOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels.

`map<string, string> labels = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels.

`map<string, string> labels = 4;`

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

Labels.

`map<string, string> labels = 4;`

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

Output only. The resource's name.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The resource's name.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getState()
    
    
    public abstract PrivateConnection.State getState()

Output only. The state of the Private Connection.

`.google.events.cloud.datastream.v1.PrivateConnection.State state = 6;`

**Returns**  
---  
**Type** | **Description**  
`[PrivateConnection.State](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.PrivateConnection.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The state of the Private Connection.

`.google.events.cloud.datastream.v1.PrivateConnection.State state = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getVpcPeeringConfig()
    
    
    public abstract VpcPeeringConfig getVpcPeeringConfig()

VPC Peering Config.

`.google.events.cloud.datastream.v1.VpcPeeringConfig vpc_peering_config = 100;`

**Returns**  
---  
**Type** | **Description**  
`[VpcPeeringConfig](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.VpcPeeringConfig)` | The vpcPeeringConfig.  
  
### getVpcPeeringConfigOrBuilder()
    
    
    public abstract VpcPeeringConfigOrBuilder getVpcPeeringConfigOrBuilder()

VPC Peering Config.

`.google.events.cloud.datastream.v1.VpcPeeringConfig vpc_peering_config = 100;`

**Returns**  
---  
**Type** | **Description**  
`[VpcPeeringConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.datastream.v1.VpcPeeringConfigOrBuilder)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The create time of the resource.

`.google.protobuf.Timestamp create_time = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Output only. In case of error, the details of the error in a user-friendly format.

`.google.events.cloud.datastream.v1.Error error = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The update time of the resource.

`.google.protobuf.Timestamp update_time = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
### hasVpcPeeringConfig()
    
    
    public abstract boolean hasVpcPeeringConfig()

VPC Peering Config.

`.google.events.cloud.datastream.v1.VpcPeeringConfig vpc_peering_config = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the vpcPeeringConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
