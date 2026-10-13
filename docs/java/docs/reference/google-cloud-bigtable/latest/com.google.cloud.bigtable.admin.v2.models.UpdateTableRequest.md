---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest
title: Class UpdateTableRequest (2.85.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:20.122546+00:00
---

# Class UpdateTableRequest (2.85.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class UpdateTableRequest (2.85.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.85.0 (latest)  2.81.0  2.80.0  2.79.0  2.78.1  2.77.0  2.74.0  2.73.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.1  2.66.0  2.65.1  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.2  2.56.0  2.54.0  2.52.0  2.51.2  2.49.0  2.46.0  2.45.1  2.44.1  2.43.0  2.42.0  2.40.0  2.39.5  2.37.0  2.35.1  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.1  2.28.0 
    
    
    public class UpdateTableRequest

Wrapper for com.google.bigtable.admin.v2.UpdateTableRequest

Allows for updating table:

  * Change stream retention period. 



## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > UpdateTableRequest

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### of(String tableId)
    
    
    public static UpdateTableRequest of(String tableId)

**Parameter**  
---  
**Name** | **Description**  
`tableId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
## Methods 

### addChangeStreamRetention(Duration retention)
    
    
    public UpdateTableRequest addChangeStreamRetention(Duration retention)

Update change stream retention period between 1 day and 7 days.

**Parameter**  
---  
**Name** | **Description**  
`retention` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### disableAutomatedBackup()
    
    
    public UpdateTableRequest disableAutomatedBackup()

Disables table automated backup policy.

**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### disableChangeStreamRetention()
    
    
    public UpdateTableRequest disableChangeStreamRetention()

Disable change stream for table.

**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### equals(Object o)
    
    
    public boolean equals(Object o)

**Parameter**  
---  
**Name** | **Description**  
`o` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### setAutomatedBackup(Duration retentionPeriod, Duration frequency)
    
    
    public UpdateTableRequest setAutomatedBackup(Duration retentionPeriod, Duration frequency)

Set an automated backup policy for the table.

**Parameters**  
---  
**Name** | **Description**  
`retentionPeriod` | `org.threeten.bp.Duration`  
  
`frequency` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### setAutomatedBackupFrequency(Duration frequency)
    
    
    public UpdateTableRequest setAutomatedBackupFrequency(Duration frequency)

Updates table automated backup policy frequency.

**Parameter**  
---  
**Name** | **Description**  
`frequency` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### setAutomatedBackupRetentionPeriod(Duration retention)
    
    
    public UpdateTableRequest setAutomatedBackupRetentionPeriod(Duration retention)

Updates table automated backup policy retention period.

**Parameter**  
---  
**Name** | **Description**  
`retention` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### setDeletionProtection(boolean deletionProtection)
    
    
    public UpdateTableRequest setDeletionProtection(boolean deletionProtection)

Changes the deletion protection of an existing table.

**Parameter**  
---  
**Name** | **Description**  
`deletionProtection` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpdateTableRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.admin.v2.models.UpdateTableRequest)` |   
  
### toProto(String projectId, String instanceId)
    
    
    public UpdateTableRequest toProto(String projectId, String instanceId)

**Internal Only** : This feature is not stable for application use.

**Parameters**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`instanceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.bigtable.admin.v2.UpdateTableRequest` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
