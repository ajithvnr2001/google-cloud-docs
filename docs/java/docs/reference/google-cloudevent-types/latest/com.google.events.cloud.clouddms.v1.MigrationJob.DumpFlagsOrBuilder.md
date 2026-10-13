---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagsOrBuilder
title: Interface MigrationJob.DumpFlagsOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:19.897813+00:00
---

# Interface MigrationJob.DumpFlagsOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MigrationJob.DumpFlagsOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagsOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagsOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagsOrBuilder)


    
    
    public static interface MigrationJob.DumpFlagsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDumpFlags(int index)
    
    
    public abstract MigrationJob.DumpFlag getDumpFlags(int index)

The flags for the initial dump.

`repeated .google.events.cloud.clouddms.v1.MigrationJob.DumpFlag dump_flags = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MigrationJob.DumpFlag](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlag)` |   
  
### getDumpFlagsCount()
    
    
    public abstract int getDumpFlagsCount()

The flags for the initial dump.

`repeated .google.events.cloud.clouddms.v1.MigrationJob.DumpFlag dump_flags = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDumpFlagsList()
    
    
    public abstract List<MigrationJob.DumpFlag> getDumpFlagsList()

The flags for the initial dump.

`repeated .google.events.cloud.clouddms.v1.MigrationJob.DumpFlag dump_flags = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[DumpFlag](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlag)>` |   
  
### getDumpFlagsOrBuilder(int index)
    
    
    public abstract MigrationJob.DumpFlagOrBuilder getDumpFlagsOrBuilder(int index)

The flags for the initial dump.

`repeated .google.events.cloud.clouddms.v1.MigrationJob.DumpFlag dump_flags = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MigrationJob.DumpFlagOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagOrBuilder)` |   
  
### getDumpFlagsOrBuilderList()
    
    
    public abstract List<? extends MigrationJob.DumpFlagOrBuilder> getDumpFlagsOrBuilderList()

The flags for the initial dump.

`repeated .google.events.cloud.clouddms.v1.MigrationJob.DumpFlag dump_flags = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.events.cloud.clouddms.v1.MigrationJob.DumpFlagOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
