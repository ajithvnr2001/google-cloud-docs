---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockOrBuilder
title: Interface ReservationBlockOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:04.203910+00:00
---

# Interface ReservationBlockOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReservationBlockOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface ReservationBlockOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCount()
    
    
    public abstract int getCount()

Output only. [Output Only] The number of resources that are allocated in this reservation block.

`optional int32 count = 94851343;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count.  
  
### getCreationTimestamp()
    
    
    public abstract String getCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The creationTimestamp.  
  
### getCreationTimestampBytes()
    
    
    public abstract ByteString getCreationTimestampBytes()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for creationTimestamp.  
  
### getHealthInfo()
    
    
    public abstract ReservationBlockHealthInfo getHealthInfo()

Output only. [Output Only] Health information for the reservation block.

`optional .google.cloud.compute.v1.ReservationBlockHealthInfo health_info = 235287729; `

**Returns**  
---  
**Type** | **Description**  
`[ReservationBlockHealthInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockHealthInfo)` | The healthInfo.  
  
### getHealthInfoOrBuilder()
    
    
    public abstract ReservationBlockHealthInfoOrBuilder getHealthInfoOrBuilder()

Output only. [Output Only] Health information for the reservation block.

`optional .google.cloud.compute.v1.ReservationBlockHealthInfo health_info = 235287729; `

**Returns**  
---  
**Type** | **Description**  
`[ReservationBlockHealthInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockHealthInfoOrBuilder)` |   
  
### getId()
    
    
    public abstract long getId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The id.  
  
### getInUseCount()
    
    
    public abstract int getInUseCount()

Output only. [Output Only] The number of instances that are currently in use on this reservation block.

`optional int32 in_use_count = 493458877;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The inUseCount.  
  
### getInUseHostCount()
    
    
    public abstract int getInUseHostCount()

Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use.

`optional int32 in_use_host_count = 364069834;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The inUseHostCount.  
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output Only] Type of the resource. Alwayscompute#reservationBlock for reservation blocks.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output Only] Type of the resource. Alwayscompute#reservationBlock for reservation blocks.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getName()
    
    
    public abstract String getName()

Output only. [Output Only] The name of this reservation block generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 @pattern [a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockOrBuilder?:\[-a-z0-9\]{0,61}\[a-z0-9\])?

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. [Output Only] The name of this reservation block generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 @pattern [a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockOrBuilder?:\[-a-z0-9\]{0,61}\[a-z0-9\])?

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPhysicalTopology()
    
    
    public abstract ReservationBlockPhysicalTopology getPhysicalTopology()

Output only. [Output Only] The physical topology of the reservation block.

` optional .google.cloud.compute.v1.ReservationBlockPhysicalTopology physical_topology = 279778519; `

**Returns**  
---  
**Type** | **Description**  
`[ReservationBlockPhysicalTopology](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockPhysicalTopology)` | The physicalTopology.  
  
### getPhysicalTopologyOrBuilder()
    
    
    public abstract ReservationBlockPhysicalTopologyOrBuilder getPhysicalTopologyOrBuilder()

Output only. [Output Only] The physical topology of the reservation block.

` optional .google.cloud.compute.v1.ReservationBlockPhysicalTopology physical_topology = 279778519; `

**Returns**  
---  
**Type** | **Description**  
`[ReservationBlockPhysicalTopologyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockPhysicalTopologyOrBuilder)` |   
  
### getReservationMaintenance()
    
    
    public abstract GroupMaintenanceInfo getReservationMaintenance()

Output only. [Output Only] Maintenance information for this reservation block.

` optional .google.cloud.compute.v1.GroupMaintenanceInfo reservation_maintenance = 340607776; `

**Returns**  
---  
**Type** | **Description**  
`[GroupMaintenanceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GroupMaintenanceInfo)` | The reservationMaintenance.  
  
### getReservationMaintenanceOrBuilder()
    
    
    public abstract GroupMaintenanceInfoOrBuilder getReservationMaintenanceOrBuilder()

Output only. [Output Only] Maintenance information for this reservation block.

` optional .google.cloud.compute.v1.GroupMaintenanceInfo reservation_maintenance = 340607776; `

**Returns**  
---  
**Type** | **Description**  
`[GroupMaintenanceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GroupMaintenanceInfoOrBuilder)` |   
  
### getReservationSubBlockCount()
    
    
    public abstract int getReservationSubBlockCount()

Output only. [Output Only] The number of reservation subBlocks associated with this reservation block.

`optional int32 reservation_sub_block_count = 330782955;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reservationSubBlockCount.  
  
### getReservationSubBlockInUseCount()
    
    
    public abstract int getReservationSubBlockInUseCount()

Output only. [Output Only] The number of in-use reservation subBlocks associated with this reservation block. If at least one VM is running on a subBlock, it is considered in-use.

`optional int32 reservation_sub_block_in_use_count = 186007137;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The reservationSubBlockInUseCount.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. [Output Only] Server-defined fully-qualified URL for this resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. [Output Only] Server-defined fully-qualified URL for this resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getSelfLinkWithId()
    
    
    public abstract String getSelfLinkWithId()

Output only. [Output Only] Server-defined URL for this resource with the resource id.

`optional string self_link_with_id = 44520962;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLinkWithId.  
  
### getSelfLinkWithIdBytes()
    
    
    public abstract ByteString getSelfLinkWithIdBytes()

Output only. [Output Only] Server-defined URL for this resource with the resource id.

`optional string self_link_with_id = 44520962;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLinkWithId.  
  
### getStatus()
    
    
    public abstract String getStatus()

Output only. [Output Only] Status of the reservation block. Check the Status enum for the list of possible values.

`optional string status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The status.  
  
### getStatusBytes()
    
    
    public abstract ByteString getStatusBytes()

Output only. [Output Only] Status of the reservation block. Check the Status enum for the list of possible values.

`optional string status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for status.  
  
### getZone()
    
    
    public abstract String getZone()

Output only. [Output Only] Zone in which the reservation block resides.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes()
    
    
    public abstract ByteString getZoneBytes()

Output only. [Output Only] Zone in which the reservation block resides.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
### hasCount()
    
    
    public abstract boolean hasCount()

Output only. [Output Only] The number of resources that are allocated in this reservation block.

`optional int32 count = 94851343;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the count field is set.  
  
### hasCreationTimestamp()
    
    
    public abstract boolean hasCreationTimestamp()

Output only. [Output Only] Creation timestamp inRFC3339 text format.

`optional string creation_timestamp = 30525366;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the creationTimestamp field is set.  
  
### hasHealthInfo()
    
    
    public abstract boolean hasHealthInfo()

Output only. [Output Only] Health information for the reservation block.

`optional .google.cloud.compute.v1.ReservationBlockHealthInfo health_info = 235287729; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the healthInfo field is set.  
  
### hasId()
    
    
    public abstract boolean hasId()

Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.

`optional uint64 id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasInUseCount()
    
    
    public abstract boolean hasInUseCount()

Output only. [Output Only] The number of instances that are currently in use on this reservation block.

`optional int32 in_use_count = 493458877;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inUseCount field is set.  
  
### hasInUseHostCount()
    
    
    public abstract boolean hasInUseHostCount()

Output only. Number of hosts currently in use. If there is one or more Instances running on the host, it is considered in use.

`optional int32 in_use_host_count = 364069834;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the inUseHostCount field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output Only] Type of the resource. Alwayscompute#reservationBlock for reservation blocks.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

Output only. [Output Only] The name of this reservation block generated by Google Compute Engine. The name must be 1-63 characters long, and comply with RFC1035 @pattern [a-z](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ReservationBlockOrBuilder?:\[-a-z0-9\]{0,61}\[a-z0-9\])?

`optional string name = 3373707;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasPhysicalTopology()
    
    
    public abstract boolean hasPhysicalTopology()

Output only. [Output Only] The physical topology of the reservation block.

` optional .google.cloud.compute.v1.ReservationBlockPhysicalTopology physical_topology = 279778519; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the physicalTopology field is set.  
  
### hasReservationMaintenance()
    
    
    public abstract boolean hasReservationMaintenance()

Output only. [Output Only] Maintenance information for this reservation block.

` optional .google.cloud.compute.v1.GroupMaintenanceInfo reservation_maintenance = 340607776; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reservationMaintenance field is set.  
  
### hasReservationSubBlockCount()
    
    
    public abstract boolean hasReservationSubBlockCount()

Output only. [Output Only] The number of reservation subBlocks associated with this reservation block.

`optional int32 reservation_sub_block_count = 330782955;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reservationSubBlockCount field is set.  
  
### hasReservationSubBlockInUseCount()
    
    
    public abstract boolean hasReservationSubBlockInUseCount()

Output only. [Output Only] The number of in-use reservation subBlocks associated with this reservation block. If at least one VM is running on a subBlock, it is considered in-use.

`optional int32 reservation_sub_block_in_use_count = 186007137;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the reservationSubBlockInUseCount field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined fully-qualified URL for this resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasSelfLinkWithId()
    
    
    public abstract boolean hasSelfLinkWithId()

Output only. [Output Only] Server-defined URL for this resource with the resource id.

`optional string self_link_with_id = 44520962;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLinkWithId field is set.  
  
### hasStatus()
    
    
    public abstract boolean hasStatus()

Output only. [Output Only] Status of the reservation block. Check the Status enum for the list of possible values.

`optional string status = 181260274;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the status field is set.  
  
### hasZone()
    
    
    public abstract boolean hasZone()

Output only. [Output Only] Zone in which the reservation block resides.

`optional string zone = 3744684;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the zone field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
