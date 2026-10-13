---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ClusterInfoOrBuilder
title: Interface ClusterInfoOrBuilder (0.33.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:52.494462+00:00
---

# Interface ClusterInfoOrBuilder (0.33.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ClusterInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ClusterInfoOrBuilder (0.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.0 (latest)  0.29.0  0.28.0  0.27.0  0.25.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface ClusterInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCurrent()
    
    
    public abstract ResourceBundleDeploymentInfo getCurrent()

Output only. Current state of the resource bundle.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo current = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleDeploymentInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo)` | The current.  
  
### getCurrentOrBuilder()
    
    
    public abstract ResourceBundleDeploymentInfoOrBuilder getCurrentOrBuilder()

Output only. Current state of the resource bundle.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo current = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleDeploymentInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfoOrBuilder)` |   
  
### getDesired()
    
    
    public abstract ResourceBundleDeploymentInfo getDesired()

Output only. Desired state for the resource bundle.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo desired = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleDeploymentInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo)` | The desired.  
  
### getDesiredOrBuilder()
    
    
    public abstract ResourceBundleDeploymentInfoOrBuilder getDesiredOrBuilder()

Output only. Desired state for the resource bundle.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo desired = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleDeploymentInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfoOrBuilder)` |   
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

Output only. Timestamp when reconciliation ends.

`.google.protobuf.Timestamp end_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

Output only. Timestamp when reconciliation ends.

`.google.protobuf.Timestamp end_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getInitial()
    
    
    public abstract ResourceBundleDeploymentInfo getInitial()

Output only. Initial state of the resource bundle prior to the deployment.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo initial = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleDeploymentInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo)` | The initial.  
  
### getInitialOrBuilder()
    
    
    public abstract ResourceBundleDeploymentInfoOrBuilder getInitialOrBuilder()

Output only. Initial state of the resource bundle prior to the deployment.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo initial = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ResourceBundleDeploymentInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfoOrBuilder)` |   
  
### getMembership()
    
    
    public abstract String getMembership()

Output only. gkehub membership of target cluster

` string membership = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The membership.  
  
### getMembershipBytes()
    
    
    public abstract ByteString getMembershipBytes()

Output only. gkehub membership of target cluster

` string membership = 1 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for membership.  
  
### getMessages(int index)
    
    
    public abstract String getMessages(int index)

Output only. Unordered list. Messages convey additional information related to the deployment.

` repeated string messages = 6 [(.google.api.field_behavior) = UNORDERED_LIST, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The messages at the given index.  
  
### getMessagesBytes(int index)
    
    
    public abstract ByteString getMessagesBytes(int index)

Output only. Unordered list. Messages convey additional information related to the deployment.

` repeated string messages = 6 [(.google.api.field_behavior) = UNORDERED_LIST, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the messages at the given index.  
  
### getMessagesCount()
    
    
    public abstract int getMessagesCount()

Output only. Unordered list. Messages convey additional information related to the deployment.

` repeated string messages = 6 [(.google.api.field_behavior) = UNORDERED_LIST, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of messages.  
  
### getMessagesList()
    
    
    public abstract List<String> getMessagesList()

Output only. Unordered list. Messages convey additional information related to the deployment.

` repeated string messages = 6 [(.google.api.field_behavior) = UNORDERED_LIST, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the messages.  
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. Timestamp when reconciliation starts.

`.google.protobuf.Timestamp start_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. Timestamp when reconciliation starts.

`.google.protobuf.Timestamp start_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getState()
    
    
    public abstract ClusterInfo.State getState()

Output only. State of the rollout for the cluster.

` .google.cloud.configdelivery.v1beta.ClusterInfo.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterInfo.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ClusterInfo.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. State of the rollout for the cluster.

` .google.cloud.configdelivery.v1beta.ClusterInfo.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasCurrent()
    
    
    public abstract boolean hasCurrent()

Output only. Current state of the resource bundle.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo current = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the current field is set.  
  
### hasDesired()
    
    
    public abstract boolean hasDesired()

Output only. Desired state for the resource bundle.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo desired = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the desired field is set.  
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

Output only. Timestamp when reconciliation ends.

`.google.protobuf.Timestamp end_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasInitial()
    
    
    public abstract boolean hasInitial()

Output only. Initial state of the resource bundle prior to the deployment.

` .google.cloud.configdelivery.v1beta.ResourceBundleDeploymentInfo initial = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the initial field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. Timestamp when reconciliation starts.

`.google.protobuf.Timestamp start_time = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
