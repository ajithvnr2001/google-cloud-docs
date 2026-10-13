---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlInstancesPointInTimeRestoreRequestOrBuilder
title: Interface SqlInstancesPointInTimeRestoreRequestOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:15.461945+00:00
---

# Interface SqlInstancesPointInTimeRestoreRequestOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.SqlInstancesPointInTimeRestoreRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SqlInstancesPointInTimeRestoreRequestOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface SqlInstancesPointInTimeRestoreRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContext()
    
    
    public abstract PointInTimeRestoreContext getContext()

Required. The context for request to perform a PITR on a Google Cloud Backup and Disaster Recovery managed instance.

` .google.cloud.sql.v1beta4.PointInTimeRestoreContext context = 100 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PointInTimeRestoreContext](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.PointInTimeRestoreContext)` | The context.  
  
### getContextOrBuilder()
    
    
    public abstract PointInTimeRestoreContextOrBuilder getContextOrBuilder()

Required. The context for request to perform a PITR on a Google Cloud Backup and Disaster Recovery managed instance.

` .google.cloud.sql.v1beta4.PointInTimeRestoreContext context = 100 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[PointInTimeRestoreContextOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-sql/latest/com.google.cloud.sql.v1beta4.PointInTimeRestoreContextOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent resource where you created this instance. Format: projects/{project}

`string parent = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource where you created this instance. Format: projects/{project}

`string parent = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasContext()
    
    
    public abstract boolean hasContext()

Required. The context for request to perform a PITR on a Google Cloud Backup and Disaster Recovery managed instance.

` .google.cloud.sql.v1beta4.PointInTimeRestoreContext context = 100 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the context field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
