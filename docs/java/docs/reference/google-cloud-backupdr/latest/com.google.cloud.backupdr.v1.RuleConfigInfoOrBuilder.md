---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RuleConfigInfoOrBuilder
title: Interface RuleConfigInfoOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:17.963831+00:00
---

# Interface RuleConfigInfoOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RuleConfigInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RuleConfigInfoOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface RuleConfigInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLastBackupError()
    
    
    public abstract Status getLastBackupError()

Output only. google.rpc.Status object to store the last backup error.

`.google.rpc.Status last_backup_error = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The lastBackupError.  
  
### getLastBackupErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getLastBackupErrorOrBuilder()

Output only. google.rpc.Status object to store the last backup error.

`.google.rpc.Status last_backup_error = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getLastBackupState()
    
    
    public abstract RuleConfigInfo.LastBackupState getLastBackupState()

Output only. The last backup state for rule.

` .google.cloud.backupdr.v1.RuleConfigInfo.LastBackupState last_backup_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[RuleConfigInfo.LastBackupState](https://docs.cloud.google.com/java/docs/reference/google-cloud-backupdr/latest/com.google.cloud.backupdr.v1.RuleConfigInfo.LastBackupState)` | The lastBackupState.  
  
### getLastBackupStateValue()
    
    
    public abstract int getLastBackupStateValue()

Output only. The last backup state for rule.

` .google.cloud.backupdr.v1.RuleConfigInfo.LastBackupState last_backup_state = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for lastBackupState.  
  
### getLastSuccessfulBackupConsistencyTime()
    
    
    public abstract Timestamp getLastSuccessfulBackupConsistencyTime()

Output only. The point in time when the last successful backup was captured from the source.

` .google.protobuf.Timestamp last_successful_backup_consistency_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The lastSuccessfulBackupConsistencyTime.  
  
### getLastSuccessfulBackupConsistencyTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getLastSuccessfulBackupConsistencyTimeOrBuilder()

Output only. The point in time when the last successful backup was captured from the source.

` .google.protobuf.Timestamp last_successful_backup_consistency_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getRuleId()
    
    
    public abstract String getRuleId()

Output only. Backup Rule id fetched from backup plan.

`string rule_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ruleId.  
  
### getRuleIdBytes()
    
    
    public abstract ByteString getRuleIdBytes()

Output only. Backup Rule id fetched from backup plan.

`string rule_id = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ruleId.  
  
### hasLastBackupError()
    
    
    public abstract boolean hasLastBackupError()

Output only. google.rpc.Status object to store the last backup error.

`.google.rpc.Status last_backup_error = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastBackupError field is set.  
  
### hasLastSuccessfulBackupConsistencyTime()
    
    
    public abstract boolean hasLastSuccessfulBackupConsistencyTime()

Output only. The point in time when the last successful backup was captured from the source.

` .google.protobuf.Timestamp last_successful_backup_consistency_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the lastSuccessfulBackupConsistencyTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
