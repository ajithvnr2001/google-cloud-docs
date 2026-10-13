---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerActionsSummaryOrBuilder
title: Interface InstanceGroupManagerActionsSummaryOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:06.888559+00:00
---

# Interface InstanceGroupManagerActionsSummaryOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InstanceGroupManagerActionsSummaryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InstanceGroupManagerActionsSummaryOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface InstanceGroupManagerActionsSummaryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAbandoning()
    
    
    public abstract int getAbandoning()

Output only. The total number of instances in the managed instance group that are scheduled to be abandoned. Abandoning an instance removes it from the managed instance group without deleting it.

`optional int32 abandoning = 440023373;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The abandoning.  
  
### getCreating()
    
    
    public abstract int getCreating()

Output only. The number of instances in the managed instance group that are scheduled to be created or are currently being created. If the group fails to create any of these instances, it tries again until it creates the instance successfully.

If you have disabled creation retries, this field will not be populated; instead, the creatingWithoutRetries field will be populated.

`optional int32 creating = 209809081;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The creating.  
  
### getCreatingWithoutRetries()
    
    
    public abstract int getCreatingWithoutRetries()

Output only. The number of instances that the managed instance group will attempt to create. The group attempts to create each instance only once. If the group fails to create any of these instances, it decreases the group's targetSize value accordingly.

`optional int32 creating_without_retries = 369916745;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The creatingWithoutRetries.  
  
### getDeleting()
    
    
    public abstract int getDeleting()

Output only. The number of instances in the managed instance group that are scheduled to be deleted or are currently being deleted.

`optional int32 deleting = 282846120;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deleting.  
  
### getNone()
    
    
    public abstract int getNone()

Output only. The number of instances in the managed instance group that are running and have no scheduled actions.

`optional int32 none = 3387192;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The none.  
  
### getRecreating()
    
    
    public abstract int getRecreating()

Output only. The number of instances in the managed instance group that are scheduled to be recreated or are currently being being recreated. Recreating an instance deletes the existing root persistent disk and creates a new disk from the image that is defined in the instance template.

`optional int32 recreating = 339057132;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The recreating.  
  
### getRefreshing()
    
    
    public abstract int getRefreshing()

Output only. The number of instances in the managed instance group that are being reconfigured with properties that do not require a restart or a recreate action. For example, setting or removing target pools for the instance.

`optional int32 refreshing = 215044903;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The refreshing.  
  
### getRestarting()
    
    
    public abstract int getRestarting()

Output only. The number of instances in the managed instance group that are scheduled to be restarted or are currently being restarted.

`optional int32 restarting = 372312947;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The restarting.  
  
### getResuming()
    
    
    public abstract int getResuming()

Output only. The number of instances in the managed instance group that are scheduled to be resumed or are currently being resumed.

`optional int32 resuming = 201100714;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The resuming.  
  
### getStarting()
    
    
    public abstract int getStarting()

Output only. The number of instances in the managed instance group that are scheduled to be started or are currently being started.

`optional int32 starting = 243064896;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The starting.  
  
### getStopping()
    
    
    public abstract int getStopping()

Output only. The number of instances in the managed instance group that are scheduled to be stopped or are currently being stopped.

`optional int32 stopping = 105035892;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The stopping.  
  
### getSuspending()
    
    
    public abstract int getSuspending()

Output only. The number of instances in the managed instance group that are scheduled to be suspended or are currently being suspended.

`optional int32 suspending = 29113894;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The suspending.  
  
### getVerifying()
    
    
    public abstract int getVerifying()

Output only. The number of instances in the managed instance group that are being verified. See the managedInstances[].currentAction property in the listManagedInstances method documentation.

`optional int32 verifying = 451612873;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The verifying.  
  
### hasAbandoning()
    
    
    public abstract boolean hasAbandoning()

Output only. The total number of instances in the managed instance group that are scheduled to be abandoned. Abandoning an instance removes it from the managed instance group without deleting it.

`optional int32 abandoning = 440023373;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the abandoning field is set.  
  
### hasCreating()
    
    
    public abstract boolean hasCreating()

Output only. The number of instances in the managed instance group that are scheduled to be created or are currently being created. If the group fails to create any of these instances, it tries again until it creates the instance successfully.

If you have disabled creation retries, this field will not be populated; instead, the creatingWithoutRetries field will be populated.

`optional int32 creating = 209809081;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creating field is set.  
  
### hasCreatingWithoutRetries()
    
    
    public abstract boolean hasCreatingWithoutRetries()

Output only. The number of instances that the managed instance group will attempt to create. The group attempts to create each instance only once. If the group fails to create any of these instances, it decreases the group's targetSize value accordingly.

`optional int32 creating_without_retries = 369916745;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creatingWithoutRetries field is set.  
  
### hasDeleting()
    
    
    public abstract boolean hasDeleting()

Output only. The number of instances in the managed instance group that are scheduled to be deleted or are currently being deleted.

`optional int32 deleting = 282846120;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the deleting field is set.  
  
### hasNone()
    
    
    public abstract boolean hasNone()

Output only. The number of instances in the managed instance group that are running and have no scheduled actions.

`optional int32 none = 3387192;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the none field is set.  
  
### hasRecreating()
    
    
    public abstract boolean hasRecreating()

Output only. The number of instances in the managed instance group that are scheduled to be recreated or are currently being being recreated. Recreating an instance deletes the existing root persistent disk and creates a new disk from the image that is defined in the instance template.

`optional int32 recreating = 339057132;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recreating field is set.  
  
### hasRefreshing()
    
    
    public abstract boolean hasRefreshing()

Output only. The number of instances in the managed instance group that are being reconfigured with properties that do not require a restart or a recreate action. For example, setting or removing target pools for the instance.

`optional int32 refreshing = 215044903;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the refreshing field is set.  
  
### hasRestarting()
    
    
    public abstract boolean hasRestarting()

Output only. The number of instances in the managed instance group that are scheduled to be restarted or are currently being restarted.

`optional int32 restarting = 372312947;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the restarting field is set.  
  
### hasResuming()
    
    
    public abstract boolean hasResuming()

Output only. The number of instances in the managed instance group that are scheduled to be resumed or are currently being resumed.

`optional int32 resuming = 201100714;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resuming field is set.  
  
### hasStarting()
    
    
    public abstract boolean hasStarting()

Output only. The number of instances in the managed instance group that are scheduled to be started or are currently being started.

`optional int32 starting = 243064896;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the starting field is set.  
  
### hasStopping()
    
    
    public abstract boolean hasStopping()

Output only. The number of instances in the managed instance group that are scheduled to be stopped or are currently being stopped.

`optional int32 stopping = 105035892;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stopping field is set.  
  
### hasSuspending()
    
    
    public abstract boolean hasSuspending()

Output only. The number of instances in the managed instance group that are scheduled to be suspended or are currently being suspended.

`optional int32 suspending = 29113894;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the suspending field is set.  
  
### hasVerifying()
    
    
    public abstract boolean hasVerifying()

Output only. The number of instances in the managed instance group that are being verified. See the managedInstances[].currentAction property in the listManagedInstances method documentation.

`optional int32 verifying = 451612873;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the verifying field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
