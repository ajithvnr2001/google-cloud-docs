---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.dataplex.v1.DataScan.ExecutionSpecOrBuilder
title: Interface DataScan.ExecutionSpecOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:26.137609+00:00
---

# Interface DataScan.ExecutionSpecOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.dataplex.v1.DataScan.ExecutionSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DataScan.ExecutionSpecOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.dataplex.v1.DataScan.ExecutionSpecOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.dataplex.v1.DataScan.ExecutionSpecOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.dataplex.v1.DataScan.ExecutionSpecOrBuilder)


    
    
    public static interface DataScan.ExecutionSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getField()
    
    
    public abstract String getField()

Immutable. The unnested field (of type _Date_ or _Timestamp_) that contains values which monotonically increase over time. If not specified, a data scan will run for all data in the table.

`string field = 100;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The field.  
  
### getFieldBytes()
    
    
    public abstract ByteString getFieldBytes()

Immutable. The unnested field (of type _Date_ or _Timestamp_) that contains values which monotonically increase over time. If not specified, a data scan will run for all data in the table.

`string field = 100;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for field.  
  
### getIncrementalCase()
    
    
    public abstract DataScan.ExecutionSpec.IncrementalCase getIncrementalCase()

**Returns**  
---  
**Type** | **Description**  
`[DataScan.ExecutionSpec.IncrementalCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.dataplex.v1.DataScan.ExecutionSpec.IncrementalCase)` |   
  
### getTrigger()
    
    
    public abstract Trigger getTrigger()

Optional. Spec related to how often and when a scan should be triggered. If not specified, the default is `OnDemand`, which means the scan will not run until the user calls `RunDataScan` API.

`.google.events.cloud.dataplex.v1.Trigger trigger = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Trigger](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.dataplex.v1.Trigger)` | The trigger.  
  
### getTriggerOrBuilder()
    
    
    public abstract TriggerOrBuilder getTriggerOrBuilder()

Optional. Spec related to how often and when a scan should be triggered. If not specified, the default is `OnDemand`, which means the scan will not run until the user calls `RunDataScan` API.

`.google.events.cloud.dataplex.v1.Trigger trigger = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TriggerOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.dataplex.v1.TriggerOrBuilder)` |   
  
### hasField()
    
    
    public abstract boolean hasField()

Immutable. The unnested field (of type _Date_ or _Timestamp_) that contains values which monotonically increase over time. If not specified, a data scan will run for all data in the table.

`string field = 100;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the field field is set.  
  
### hasTrigger()
    
    
    public abstract boolean hasTrigger()

Optional. Spec related to how often and when a scan should be triggered. If not specified, the default is `OnDemand`, which means the scan will not run until the user calls `RunDataScan` API.

`.google.events.cloud.dataplex.v1.Trigger trigger = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trigger field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
