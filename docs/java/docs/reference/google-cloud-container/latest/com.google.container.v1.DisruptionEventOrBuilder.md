---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DisruptionEventOrBuilder
title: Interface DisruptionEventOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:18.766779+00:00
---

# Interface DisruptionEventOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DisruptionEventOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DisruptionEventOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface DisruptionEventOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDisruptionType()
    
    
    public abstract DisruptionEvent.DisruptionType getDisruptionType()

The type of the disruption event.

`.google.container.v1.DisruptionEvent.DisruptionType disruption_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[DisruptionEvent.DisruptionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DisruptionEvent.DisruptionType)` | The disruptionType.  
  
### getDisruptionTypeValue()
    
    
    public abstract int getDisruptionTypeValue()

The type of the disruption event.

`.google.container.v1.DisruptionEvent.DisruptionType disruption_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for disruptionType.  
  
### getPdbBlockedNode()
    
    
    public abstract String getPdbBlockedNode()

The node whose drain is blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`string pdb_blocked_node = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pdbBlockedNode.  
  
### getPdbBlockedNodeBytes()
    
    
    public abstract ByteString getPdbBlockedNodeBytes()

The node whose drain is blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`string pdb_blocked_node = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pdbBlockedNode.  
  
### getPdbBlockedPod(int index)
    
    
    public abstract DisruptionEvent.PdbBlockedPod getPdbBlockedPod(int index)

The pods whose evictions are blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`repeated .google.container.v1.DisruptionEvent.PdbBlockedPod pdb_blocked_pod = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DisruptionEvent.PdbBlockedPod](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DisruptionEvent.PdbBlockedPod)` |   
  
### getPdbBlockedPodCount()
    
    
    public abstract int getPdbBlockedPodCount()

The pods whose evictions are blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`repeated .google.container.v1.DisruptionEvent.PdbBlockedPod pdb_blocked_pod = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPdbBlockedPodList()
    
    
    public abstract List<DisruptionEvent.PdbBlockedPod> getPdbBlockedPodList()

The pods whose evictions are blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`repeated .google.container.v1.DisruptionEvent.PdbBlockedPod pdb_blocked_pod = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PdbBlockedPod](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DisruptionEvent.PdbBlockedPod)>` |   
  
### getPdbBlockedPodOrBuilder(int index)
    
    
    public abstract DisruptionEvent.PdbBlockedPodOrBuilder getPdbBlockedPodOrBuilder(int index)

The pods whose evictions are blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`repeated .google.container.v1.DisruptionEvent.PdbBlockedPod pdb_blocked_pod = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DisruptionEvent.PdbBlockedPodOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DisruptionEvent.PdbBlockedPodOrBuilder)` |   
  
### getPdbBlockedPodOrBuilderList()
    
    
    public abstract List<? extends DisruptionEvent.PdbBlockedPodOrBuilder> getPdbBlockedPodOrBuilderList()

The pods whose evictions are blocked by PDB. This field is set for both POD_PDB_VIOLATION and POD_NOT_ENOUGH_PDB event.

`repeated .google.container.v1.DisruptionEvent.PdbBlockedPod pdb_blocked_pod = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.container.v1.DisruptionEvent.PdbBlockedPodOrBuilder>` |   
  
### getPdbViolationTimeout()
    
    
    public abstract Duration getPdbViolationTimeout()

The timeout in seconds for which the node drain is blocked by PDB. After this timeout, pods are forcefully evicted. This field is only populated when event_type is POD_PDB_VIOLATION.

`optional .google.protobuf.Duration pdb_violation_timeout = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The pdbViolationTimeout.  
  
### getPdbViolationTimeoutOrBuilder()
    
    
    public abstract DurationOrBuilder getPdbViolationTimeoutOrBuilder()

The timeout in seconds for which the node drain is blocked by PDB. After this timeout, pods are forcefully evicted. This field is only populated when event_type is POD_PDB_VIOLATION.

`optional .google.protobuf.Duration pdb_violation_timeout = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasPdbViolationTimeout()
    
    
    public abstract boolean hasPdbViolationTimeout()

The timeout in seconds for which the node drain is blocked by PDB. After this timeout, pods are forcefully evicted. This field is only populated when event_type is POD_PDB_VIOLATION.

`optional .google.protobuf.Duration pdb_violation_timeout = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pdbViolationTimeout field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
