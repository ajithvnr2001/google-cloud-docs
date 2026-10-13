---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.HookOrBuilder
title: Interface HookOrBuilder (0.69.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:48:40.717286+00:00
---

# Interface HookOrBuilder (0.69.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.HookOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HookOrBuilder (0.69.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.69.0 (latest)  0.65.0  0.64.0  0.63.0  0.61.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.50.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.34.0  0.33.0  0.32.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface HookOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Create timestamp.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Create timestamp.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisabled()
    
    
    public abstract boolean getDisabled()

Optional. Determines if the hook disabled or not. Set to true to stop sending traffic.

`bool disabled = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disabled.  
  
### getEvents(int index)
    
    
    public abstract Hook.HookEventType getEvents(int index)

Optional. The events that trigger hook on.

` repeated .google.cloud.securesourcemanager.v1.Hook.HookEventType events = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[Hook.HookEventType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.Hook.HookEventType)` | The events at the given index.  
  
### getEventsCount()
    
    
    public abstract int getEventsCount()

Optional. The events that trigger hook on.

` repeated .google.cloud.securesourcemanager.v1.Hook.HookEventType events = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of events.  
  
### getEventsList()
    
    
    public abstract List<Hook.HookEventType> getEventsList()

Optional. The events that trigger hook on.

` repeated .google.cloud.securesourcemanager.v1.Hook.HookEventType events = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HookEventType](https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.Hook.HookEventType)>` | A list containing the events.  
  
### getEventsValue(int index)
    
    
    public abstract int getEventsValue(int index)

Optional. The events that trigger hook on.

` repeated .google.cloud.securesourcemanager.v1.Hook.HookEventType events = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of events at the given index.  
  
### getEventsValueList()
    
    
    public abstract List<Integer> getEventsValueList()

Optional. The events that trigger hook on.

` repeated .google.cloud.securesourcemanager.v1.Hook.HookEventType events = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for events.  
  
### getName()
    
    
    public abstract String getName()

Identifier. A unique identifier for a Hook. The name should be of the format: `projects/{project}/locations/{location_id}/repositories/{repository_id}/hooks/{hook_id}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. A unique identifier for a Hook. The name should be of the format: `projects/{project}/locations/{location_id}/repositories/{repository_id}/hooks/{hook_id}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPushOption()
    
    
    public abstract Hook.PushOption getPushOption()

Optional. The trigger option for push events.

` .google.cloud.securesourcemanager.v1.Hook.PushOption push_option = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Hook.PushOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.Hook.PushOption)` | The pushOption.  
  
### getPushOptionOrBuilder()
    
    
    public abstract Hook.PushOptionOrBuilder getPushOptionOrBuilder()

Optional. The trigger option for push events.

` .google.cloud.securesourcemanager.v1.Hook.PushOption push_option = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Hook.PushOptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securesourcemanager/latest/com.google.cloud.securesourcemanager.v1.Hook.PushOptionOrBuilder)` |   
  
### getSensitiveQueryString()
    
    
    public abstract String getSensitiveQueryString()

Optional. The sensitive query string to be appended to the target URI.

`string sensitive_query_string = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The sensitiveQueryString.  
  
### getSensitiveQueryStringBytes()
    
    
    public abstract ByteString getSensitiveQueryStringBytes()

Optional. The sensitive query string to be appended to the target URI.

`string sensitive_query_string = 10 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for sensitiveQueryString.  
  
### getTargetUri()
    
    
    public abstract String getTargetUri()

Required. The target URI to which the payloads will be delivered.

`string target_uri = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetUri.  
  
### getTargetUriBytes()
    
    
    public abstract ByteString getTargetUriBytes()

Required. The target URI to which the payloads will be delivered.

`string target_uri = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for targetUri.  
  
### getUid()
    
    
    public abstract String getUid()

Output only. Unique identifier of the hook.

` string uid = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uid.  
  
### getUidBytes()
    
    
    public abstract ByteString getUidBytes()

Output only. Unique identifier of the hook.

` string uid = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uid.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Update timestamp.

`.google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Update timestamp.

`.google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Create timestamp.

`.google.protobuf.Timestamp create_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasPushOption()
    
    
    public abstract boolean hasPushOption()

Optional. The trigger option for push events.

` .google.cloud.securesourcemanager.v1.Hook.PushOption push_option = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pushOption field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Update timestamp.

`.google.protobuf.Timestamp update_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
