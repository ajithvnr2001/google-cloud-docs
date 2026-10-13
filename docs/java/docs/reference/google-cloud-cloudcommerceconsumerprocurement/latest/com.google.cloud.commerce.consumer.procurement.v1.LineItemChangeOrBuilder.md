---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeOrBuilder
title: Interface LineItemChangeOrBuilder (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:29:46.662334+00:00
---

# Interface LineItemChangeOrBuilder (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LineItemChangeOrBuilder (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 
    
    
    public interface LineItemChangeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getChangeEffectiveTime()
    
    
    public abstract Timestamp getChangeEffectiveTime()

Output only. A time at which the change became or will become (in case of pending change) effective.

` .google.protobuf.Timestamp change_effective_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The changeEffectiveTime.  
  
### getChangeEffectiveTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getChangeEffectiveTimeOrBuilder()

Output only. A time at which the change became or will become (in case of pending change) effective.

` .google.protobuf.Timestamp change_effective_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getChangeId()
    
    
    public abstract String getChangeId()

Output only. Change ID. All changes made within one order update operation have the same change_id.

`string change_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The changeId.  
  
### getChangeIdBytes()
    
    
    public abstract ByteString getChangeIdBytes()

Output only. Change ID. All changes made within one order update operation have the same change_id.

`string change_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for changeId.  
  
### getChangeState()
    
    
    public abstract LineItemChangeState getChangeState()

Output only. State of the change.

` .google.cloud.commerce.consumer.procurement.v1.LineItemChangeState change_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemChangeState](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeState)` | The changeState.  
  
### getChangeStateReasonType()
    
    
    public abstract LineItemChangeStateReasonType getChangeStateReasonType()

Output only. Predefined enum types for why this line item change is in current state. For example, a line item change's state could be `LINE_ITEM_CHANGE_STATE_COMPLETED` because of end-of-term expiration, immediate cancellation initiated by the user, or system-initiated cancellation.

` .google.cloud.commerce.consumer.procurement.v1.LineItemChangeStateReasonType change_state_reason_type = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemChangeStateReasonType](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeStateReasonType)` | The changeStateReasonType.  
  
### getChangeStateReasonTypeValue()
    
    
    public abstract int getChangeStateReasonTypeValue()

Output only. Predefined enum types for why this line item change is in current state. For example, a line item change's state could be `LINE_ITEM_CHANGE_STATE_COMPLETED` because of end-of-term expiration, immediate cancellation initiated by the user, or system-initiated cancellation.

` .google.cloud.commerce.consumer.procurement.v1.LineItemChangeStateReasonType change_state_reason_type = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for changeStateReasonType.  
  
### getChangeStateValue()
    
    
    public abstract int getChangeStateValue()

Output only. State of the change.

` .google.cloud.commerce.consumer.procurement.v1.LineItemChangeState change_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for changeState.  
  
### getChangeType()
    
    
    public abstract LineItemChangeType getChangeType()

Required. Type of the change to make.

` .google.cloud.commerce.consumer.procurement.v1.LineItemChangeType change_type = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemChangeType](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemChangeType)` | The changeType.  
  
### getChangeTypeValue()
    
    
    public abstract int getChangeTypeValue()

Required. Type of the change to make.

` .google.cloud.commerce.consumer.procurement.v1.LineItemChangeType change_type = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for changeType.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when change was initiated.

`.google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when change was initiated.

`.google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getNewLineItemInfo()
    
    
    public abstract LineItemInfo getNewLineItemInfo()

Line item info after the change.

`.google.cloud.commerce.consumer.procurement.v1.LineItemInfo new_line_item_info = 4; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemInfo)` | The newLineItemInfo.  
  
### getNewLineItemInfoOrBuilder()
    
    
    public abstract LineItemInfoOrBuilder getNewLineItemInfoOrBuilder()

Line item info after the change.

`.google.cloud.commerce.consumer.procurement.v1.LineItemInfo new_line_item_info = 4; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemInfoOrBuilder)` |   
  
### getOldLineItemInfo()
    
    
    public abstract LineItemInfo getOldLineItemInfo()

Output only. Line item info before the change.

` .google.cloud.commerce.consumer.procurement.v1.LineItemInfo old_line_item_info = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemInfo)` | The oldLineItemInfo.  
  
### getOldLineItemInfoOrBuilder()
    
    
    public abstract LineItemInfoOrBuilder getOldLineItemInfoOrBuilder()

Output only. Line item info before the change.

` .google.cloud.commerce.consumer.procurement.v1.LineItemInfo old_line_item_info = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LineItemInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudcommerceconsumerprocurement/latest/com.google.cloud.commerce.consumer.procurement.v1.LineItemInfoOrBuilder)` |   
  
### getStateReason()
    
    
    public abstract String getStateReason()

Output only. Provider-supplied message explaining the LineItemChange's state. Mainly used to communicate progress and ETA for provisioning in the case of `PENDING_APPROVAL`, and to explain why the change request was denied or canceled in the case of `REJECTED` and `CANCELED` states.

`string state_reason = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stateReason.  
  
### getStateReasonBytes()
    
    
    public abstract ByteString getStateReasonBytes()

Output only. Provider-supplied message explaining the LineItemChange's state. Mainly used to communicate progress and ETA for provisioning in the case of `PENDING_APPROVAL`, and to explain why the change request was denied or canceled in the case of `REJECTED` and `CANCELED` states.

`string state_reason = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stateReason.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time when change was updated, e.g. approved/rejected by partners or cancelled by the user.

`.google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time when change was updated, e.g. approved/rejected by partners or cancelled by the user.

`.google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasChangeEffectiveTime()
    
    
    public abstract boolean hasChangeEffectiveTime()

Output only. A time at which the change became or will become (in case of pending change) effective.

` .google.protobuf.Timestamp change_effective_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the changeEffectiveTime field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when change was initiated.

`.google.protobuf.Timestamp create_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasNewLineItemInfo()
    
    
    public abstract boolean hasNewLineItemInfo()

Line item info after the change.

`.google.cloud.commerce.consumer.procurement.v1.LineItemInfo new_line_item_info = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the newLineItemInfo field is set.  
  
### hasOldLineItemInfo()
    
    
    public abstract boolean hasOldLineItemInfo()

Output only. Line item info before the change.

` .google.cloud.commerce.consumer.procurement.v1.LineItemInfo old_line_item_info = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oldLineItemInfo field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time when change was updated, e.g. approved/rejected by partners or cancelled by the user.

`.google.protobuf.Timestamp update_time = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
