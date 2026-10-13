---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceStateOrBuilder
title: Interface QueuedResourceStateOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:47.056901+00:00
---

# Interface QueuedResourceStateOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceStateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QueuedResourceStateOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.2.6 
    
    
    public interface QueuedResourceStateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAcceptedData()
    
    
    public abstract QueuedResourceState.AcceptedData getAcceptedData()

Further data for the accepted state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.AcceptedData accepted_data = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.AcceptedData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.AcceptedData)` | The acceptedData.  
  
### getAcceptedDataOrBuilder()
    
    
    public abstract QueuedResourceState.AcceptedDataOrBuilder getAcceptedDataOrBuilder()

Further data for the accepted state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.AcceptedData accepted_data = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.AcceptedDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.AcceptedDataOrBuilder)` |   
  
### getActiveData()
    
    
    public abstract QueuedResourceState.ActiveData getActiveData()

Further data for the active state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.ActiveData active_data = 7;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.ActiveData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.ActiveData)` | The activeData.  
  
### getActiveDataOrBuilder()
    
    
    public abstract QueuedResourceState.ActiveDataOrBuilder getActiveDataOrBuilder()

Further data for the active state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.ActiveData active_data = 7;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.ActiveDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.ActiveDataOrBuilder)` |   
  
### getCreatingData()
    
    
    public abstract QueuedResourceState.CreatingData getCreatingData()

Further data for the creating state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.CreatingData creating_data = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.CreatingData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.CreatingData)` | The creatingData.  
  
### getCreatingDataOrBuilder()
    
    
    public abstract QueuedResourceState.CreatingDataOrBuilder getCreatingDataOrBuilder()

Further data for the creating state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.CreatingData creating_data = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.CreatingDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.CreatingDataOrBuilder)` |   
  
### getDeletingData()
    
    
    public abstract QueuedResourceState.DeletingData getDeletingData()

Further data for the deleting state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.DeletingData deleting_data = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.DeletingData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.DeletingData)` | The deletingData.  
  
### getDeletingDataOrBuilder()
    
    
    public abstract QueuedResourceState.DeletingDataOrBuilder getDeletingDataOrBuilder()

Further data for the deleting state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.DeletingData deleting_data = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.DeletingDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.DeletingDataOrBuilder)` |   
  
### getFailedData()
    
    
    public abstract QueuedResourceState.FailedData getFailedData()

Further data for the failed state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.FailedData failed_data = 5;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.FailedData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.FailedData)` | The failedData.  
  
### getFailedDataOrBuilder()
    
    
    public abstract QueuedResourceState.FailedDataOrBuilder getFailedDataOrBuilder()

Further data for the failed state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.FailedData failed_data = 5;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.FailedDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.FailedDataOrBuilder)` |   
  
### getProvisioningData()
    
    
    public abstract QueuedResourceState.ProvisioningData getProvisioningData()

Further data for the provisioning state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.ProvisioningData provisioning_data = 4; `

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.ProvisioningData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.ProvisioningData)` | The provisioningData.  
  
### getProvisioningDataOrBuilder()
    
    
    public abstract QueuedResourceState.ProvisioningDataOrBuilder getProvisioningDataOrBuilder()

Further data for the provisioning state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.ProvisioningData provisioning_data = 4; `

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.ProvisioningDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.ProvisioningDataOrBuilder)` |   
  
### getState()
    
    
    public abstract QueuedResourceState.State getState()

State of the QueuedResource request.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.State state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.State)` | The state.  
  
### getStateDataCase()
    
    
    public abstract QueuedResourceState.StateDataCase getStateDataCase()

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.StateDataCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.StateDataCase)` |   
  
### getStateInitiator()
    
    
    public abstract QueuedResourceState.StateInitiator getStateInitiator()

Output only. The initiator of the QueuedResources's current state. Used to indicate whether the SUSPENDING/SUSPENDED state was initiated by the user or the service.

` .google.cloud.tpu.v2alpha1.QueuedResourceState.StateInitiator state_initiator = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.StateInitiator](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.StateInitiator)` | The stateInitiator.  
  
### getStateInitiatorValue()
    
    
    public abstract int getStateInitiatorValue()

Output only. The initiator of the QueuedResources's current state. Used to indicate whether the SUSPENDING/SUSPENDED state was initiated by the user or the service.

` .google.cloud.tpu.v2alpha1.QueuedResourceState.StateInitiator state_initiator = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for stateInitiator.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

State of the QueuedResource request.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.State state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getSuspendedData()
    
    
    public abstract QueuedResourceState.SuspendedData getSuspendedData()

Further data for the suspended state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendedData suspended_data = 9;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.SuspendedData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendedData)` | The suspendedData.  
  
### getSuspendedDataOrBuilder()
    
    
    public abstract QueuedResourceState.SuspendedDataOrBuilder getSuspendedDataOrBuilder()

Further data for the suspended state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendedData suspended_data = 9;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.SuspendedDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendedDataOrBuilder)` |   
  
### getSuspendingData()
    
    
    public abstract QueuedResourceState.SuspendingData getSuspendingData()

Further data for the suspending state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendingData suspending_data = 8;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.SuspendingData](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendingData)` | The suspendingData.  
  
### getSuspendingDataOrBuilder()
    
    
    public abstract QueuedResourceState.SuspendingDataOrBuilder getSuspendingDataOrBuilder()

Further data for the suspending state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendingData suspending_data = 8;`

**Returns**  
---  
**Type** | **Description**  
`[QueuedResourceState.SuspendingDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tpu/latest/com.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendingDataOrBuilder)` |   
  
### hasAcceptedData()
    
    
    public abstract boolean hasAcceptedData()

Further data for the accepted state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.AcceptedData accepted_data = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the acceptedData field is set.  
  
### hasActiveData()
    
    
    public abstract boolean hasActiveData()

Further data for the active state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.ActiveData active_data = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the activeData field is set.  
  
### hasCreatingData()
    
    
    public abstract boolean hasCreatingData()

Further data for the creating state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.CreatingData creating_data = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creatingData field is set.  
  
### hasDeletingData()
    
    
    public abstract boolean hasDeletingData()

Further data for the deleting state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.DeletingData deleting_data = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deletingData field is set.  
  
### hasFailedData()
    
    
    public abstract boolean hasFailedData()

Further data for the failed state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.FailedData failed_data = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the failedData field is set.  
  
### hasProvisioningData()
    
    
    public abstract boolean hasProvisioningData()

Further data for the provisioning state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.ProvisioningData provisioning_data = 4; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the provisioningData field is set.  
  
### hasSuspendedData()
    
    
    public abstract boolean hasSuspendedData()

Further data for the suspended state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendedData suspended_data = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the suspendedData field is set.  
  
### hasSuspendingData()
    
    
    public abstract boolean hasSuspendingData()

Further data for the suspending state.

`.google.cloud.tpu.v2alpha1.QueuedResourceState.SuspendingData suspending_data = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the suspendingData field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
