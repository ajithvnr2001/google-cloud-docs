---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRetentionSettingsOrBuilder
title: Interface BackupRetentionSettingsOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:39.337876+00:00
---

# Interface BackupRetentionSettingsOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRetentionSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackupRetentionSettingsOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface BackupRetentionSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getRetainedBackups()
    
    
    public abstract Int32Value getRetainedBackups()

Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is 'COUNT', we will retain this many backups.

`.google.protobuf.Int32Value retained_backups = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Int32Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32Value.html)` | The retainedBackups.  
  
### getRetainedBackupsOrBuilder()
    
    
    public abstract Int32ValueOrBuilder getRetainedBackupsOrBuilder()

Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is 'COUNT', we will retain this many backups.

`.google.protobuf.Int32Value retained_backups = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Int32ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Int32ValueOrBuilder.html)` |   
  
### getRetentionUnit()
    
    
    public abstract BackupRetentionSettings.RetentionUnit getRetentionUnit()

The unit that 'retained_backups' represents.

`.google.cloud.sql.v1.BackupRetentionSettings.RetentionUnit retention_unit = 1;`

**Returns**  
---  
**Type** | **Description**  
`[BackupRetentionSettings.RetentionUnit](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1.BackupRetentionSettings.RetentionUnit)` | The retentionUnit.  
  
### getRetentionUnitValue()
    
    
    public abstract int getRetentionUnitValue()

The unit that 'retained_backups' represents.

`.google.cloud.sql.v1.BackupRetentionSettings.RetentionUnit retention_unit = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for retentionUnit.  
  
### hasRetainedBackups()
    
    
    public abstract boolean hasRetainedBackups()

Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is 'COUNT', we will retain this many backups.

`.google.protobuf.Int32Value retained_backups = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the retainedBackups field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
