---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpcomingMaintenanceOrBuilder
title: Interface UpcomingMaintenanceOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:42.227362+00:00
---

# Interface UpcomingMaintenanceOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.UpcomingMaintenanceOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpcomingMaintenanceOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface UpcomingMaintenanceOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCanReschedule()
    
    
    public abstract boolean getCanReschedule()

Indicates if the maintenance can be customer triggered.

`optional bool can_reschedule = 95981977;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The canReschedule.  
  
### getLatestWindowStartTime()
    
    
    public abstract String getLatestWindowStartTime()

The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.

`optional string latest_window_start_time = 128032129;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The latestWindowStartTime.  
  
### getLatestWindowStartTimeBytes()
    
    
    public abstract ByteString getLatestWindowStartTimeBytes()

The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.

`optional string latest_window_start_time = 128032129;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for latestWindowStartTime.  
  
### getMaintenanceOnShutdown()
    
    
    public abstract boolean getMaintenanceOnShutdown()

Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.

`optional bool maintenance_on_shutdown = 231055754;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maintenanceOnShutdown.  
  
### getMaintenanceReasons(int index)
    
    
    public abstract String getMaintenanceReasons(int index)

The reasons for the maintenance. Only valid for vms. Check the MaintenanceReasons enum for the list of possible values.

`repeated string maintenance_reasons = 140283267;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The maintenanceReasons at the given index.  
  
### getMaintenanceReasonsBytes(int index)
    
    
    public abstract ByteString getMaintenanceReasonsBytes(int index)

The reasons for the maintenance. Only valid for vms. Check the MaintenanceReasons enum for the list of possible values.

`repeated string maintenance_reasons = 140283267;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the maintenanceReasons at the given index.  
  
### getMaintenanceReasonsCount()
    
    
    public abstract int getMaintenanceReasonsCount()

The reasons for the maintenance. Only valid for vms. Check the MaintenanceReasons enum for the list of possible values.

`repeated string maintenance_reasons = 140283267;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of maintenanceReasons.  
  
### getMaintenanceReasonsList()
    
    
    public abstract List<String> getMaintenanceReasonsList()

The reasons for the maintenance. Only valid for vms. Check the MaintenanceReasons enum for the list of possible values.

`repeated string maintenance_reasons = 140283267;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the maintenanceReasons.  
  
### getMaintenanceStatus()
    
    
    public abstract String getMaintenanceStatus()

Check the MaintenanceStatus enum for the list of possible values.

`optional string maintenance_status = 81645214;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The maintenanceStatus.  
  
### getMaintenanceStatusBytes()
    
    
    public abstract ByteString getMaintenanceStatusBytes()

Check the MaintenanceStatus enum for the list of possible values.

`optional string maintenance_status = 81645214;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for maintenanceStatus.  
  
### getType()
    
    
    public abstract String getType()

Defines the type of maintenance. Check the Type enum for the list of possible values.

`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

Defines the type of maintenance. Check the Type enum for the list of possible values.

`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### getWindowEndTime()
    
    
    public abstract String getWindowEndTime()

The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.

`optional string window_end_time = 271816480;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The windowEndTime.  
  
### getWindowEndTimeBytes()
    
    
    public abstract ByteString getWindowEndTimeBytes()

The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.

`optional string window_end_time = 271816480;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for windowEndTime.  
  
### getWindowStartTime()
    
    
    public abstract String getWindowStartTime()

The current start time of the maintenance window. This timestamp value is in RFC3339 text format.

`optional string window_start_time = 473061433;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The windowStartTime.  
  
### getWindowStartTimeBytes()
    
    
    public abstract ByteString getWindowStartTimeBytes()

The current start time of the maintenance window. This timestamp value is in RFC3339 text format.

`optional string window_start_time = 473061433;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for windowStartTime.  
  
### hasCanReschedule()
    
    
    public abstract boolean hasCanReschedule()

Indicates if the maintenance can be customer triggered.

`optional bool can_reschedule = 95981977;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the canReschedule field is set.  
  
### hasLatestWindowStartTime()
    
    
    public abstract boolean hasLatestWindowStartTime()

The latest time for the planned maintenance window to start. This timestamp value is in RFC3339 text format.

`optional string latest_window_start_time = 128032129;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the latestWindowStartTime field is set.  
  
### hasMaintenanceOnShutdown()
    
    
    public abstract boolean hasMaintenanceOnShutdown()

Indicates whether the UpcomingMaintenance will be triggered on VM shutdown.

`optional bool maintenance_on_shutdown = 231055754;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceOnShutdown field is set.  
  
### hasMaintenanceStatus()
    
    
    public abstract boolean hasMaintenanceStatus()

Check the MaintenanceStatus enum for the list of possible values.

`optional string maintenance_status = 81645214;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maintenanceStatus field is set.  
  
### hasType()
    
    
    public abstract boolean hasType()

Defines the type of maintenance. Check the Type enum for the list of possible values.

`optional string type = 3575610;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
### hasWindowEndTime()
    
    
    public abstract boolean hasWindowEndTime()

The time by which the maintenance disruption will be completed. This timestamp value is in RFC3339 text format.

`optional string window_end_time = 271816480;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowEndTime field is set.  
  
### hasWindowStartTime()
    
    
    public abstract boolean hasWindowStartTime()

The current start time of the maintenance window. This timestamp value is in RFC3339 text format.

`optional string window_start_time = 473061433;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the windowStartTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
