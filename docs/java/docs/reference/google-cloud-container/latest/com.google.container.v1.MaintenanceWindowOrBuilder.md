---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenanceWindowOrBuilder
title: Interface MaintenanceWindowOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:39.065701+00:00
---

# Interface MaintenanceWindowOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenanceWindowOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MaintenanceWindowOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface MaintenanceWindowOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMaintenanceExclusions(String key)
    
    
    public abstract boolean containsMaintenanceExclusions(String key)

Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.

`map<string, .google.container.v1.TimeWindow> maintenance_exclusions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDailyMaintenanceWindow()
    
    
    public abstract DailyMaintenanceWindow getDailyMaintenanceWindow()

DailyMaintenanceWindow specifies a daily maintenance operation window.

`.google.container.v1.DailyMaintenanceWindow daily_maintenance_window = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DailyMaintenanceWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DailyMaintenanceWindow)` | The dailyMaintenanceWindow.  
  
### getDailyMaintenanceWindowOrBuilder()
    
    
    public abstract DailyMaintenanceWindowOrBuilder getDailyMaintenanceWindowOrBuilder()

DailyMaintenanceWindow specifies a daily maintenance operation window.

`.google.container.v1.DailyMaintenanceWindow daily_maintenance_window = 2;`

**Returns**  
---  
**Type** | **Description**  
`[DailyMaintenanceWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DailyMaintenanceWindowOrBuilder)` |   
  
### getMaintenanceExclusions() (deprecated)
    
    
    public abstract Map<String,TimeWindow> getMaintenanceExclusions()

Use [#getMaintenanceExclusionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenanceWindowOrBuilder#com_google_container_v1_MaintenanceWindowOrBuilder_getMaintenanceExclusionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TimeWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.TimeWindow)>` |   
  
### getMaintenanceExclusionsCount()
    
    
    public abstract int getMaintenanceExclusionsCount()

Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.

`map<string, .google.container.v1.TimeWindow> maintenance_exclusions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMaintenanceExclusionsMap()
    
    
    public abstract Map<String,TimeWindow> getMaintenanceExclusionsMap()

Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.

`map<string, .google.container.v1.TimeWindow> maintenance_exclusions = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[TimeWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.TimeWindow)>` |   
  
### getMaintenanceExclusionsOrDefault(String key, TimeWindow defaultValue)
    
    
    public abstract TimeWindow getMaintenanceExclusionsOrDefault(String key, TimeWindow defaultValue)

Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.

`map<string, .google.container.v1.TimeWindow> maintenance_exclusions = 4;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[TimeWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.TimeWindow)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.TimeWindow)` |   
  
### getMaintenanceExclusionsOrThrow(String key)
    
    
    public abstract TimeWindow getMaintenanceExclusionsOrThrow(String key)

Exceptions to maintenance window. Non-emergency maintenance should not occur in these windows.

`map<string, .google.container.v1.TimeWindow> maintenance_exclusions = 4;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimeWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.TimeWindow)` |   
  
### getPolicyCase()
    
    
    public abstract MaintenanceWindow.PolicyCase getPolicyCase()

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceWindow.PolicyCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.MaintenanceWindow.PolicyCase)` |   
  
### getRecurringMaintenanceWindow()
    
    
    public abstract RecurringMaintenanceWindow getRecurringMaintenanceWindow()

RecurringMaintenanceWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time. Alternative to RecurringWindow, with renamed fields.

`.google.container.v1.RecurringMaintenanceWindow recurring_maintenance_window = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RecurringMaintenanceWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RecurringMaintenanceWindow)` | The recurringMaintenanceWindow.  
  
### getRecurringMaintenanceWindowOrBuilder()
    
    
    public abstract RecurringMaintenanceWindowOrBuilder getRecurringMaintenanceWindowOrBuilder()

RecurringMaintenanceWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time. Alternative to RecurringWindow, with renamed fields.

`.google.container.v1.RecurringMaintenanceWindow recurring_maintenance_window = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RecurringMaintenanceWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RecurringMaintenanceWindowOrBuilder)` |   
  
### getRecurringWindow()
    
    
    public abstract RecurringTimeWindow getRecurringWindow()

RecurringWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time.

`.google.container.v1.RecurringTimeWindow recurring_window = 3;`

**Returns**  
---  
**Type** | **Description**  
`[RecurringTimeWindow](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RecurringTimeWindow)` | The recurringWindow.  
  
### getRecurringWindowOrBuilder()
    
    
    public abstract RecurringTimeWindowOrBuilder getRecurringWindowOrBuilder()

RecurringWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time.

`.google.container.v1.RecurringTimeWindow recurring_window = 3;`

**Returns**  
---  
**Type** | **Description**  
`[RecurringTimeWindowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RecurringTimeWindowOrBuilder)` |   
  
### hasDailyMaintenanceWindow()
    
    
    public abstract boolean hasDailyMaintenanceWindow()

DailyMaintenanceWindow specifies a daily maintenance operation window.

`.google.container.v1.DailyMaintenanceWindow daily_maintenance_window = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dailyMaintenanceWindow field is set.  
  
### hasRecurringMaintenanceWindow()
    
    
    public abstract boolean hasRecurringMaintenanceWindow()

RecurringMaintenanceWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time. Alternative to RecurringWindow, with renamed fields.

`.google.container.v1.RecurringMaintenanceWindow recurring_maintenance_window = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recurringMaintenanceWindow field is set.  
  
### hasRecurringWindow()
    
    
    public abstract boolean hasRecurringWindow()

RecurringWindow specifies some number of recurring time periods for maintenance to occur. The time windows may be overlapping. If no maintenance windows are set, maintenance can occur at any time.

`.google.container.v1.RecurringTimeWindow recurring_window = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the recurringWindow field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
