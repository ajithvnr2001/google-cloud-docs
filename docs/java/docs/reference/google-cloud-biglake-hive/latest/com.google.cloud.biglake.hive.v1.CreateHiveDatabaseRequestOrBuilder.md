---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveDatabaseRequestOrBuilder
title: Interface CreateHiveDatabaseRequestOrBuilder (0.4.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:44.659435+00:00
---

# Interface CreateHiveDatabaseRequestOrBuilder (0.4.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveDatabaseRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateHiveDatabaseRequestOrBuilder (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface CreateHiveDatabaseRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getHiveDatabase()
    
    
    public abstract HiveDatabase getHiveDatabase()

Required. The database to create. The `name` field does not need to be provided.

` .google.cloud.biglake.hive.v1.HiveDatabase hive_database = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[HiveDatabase](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveDatabase)` | The hiveDatabase.  
  
### getHiveDatabaseId()
    
    
    public abstract String getHiveDatabaseId()

Required. The ID to use for the Hive Database. The maximum length is 128 characters.

`string hive_database_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hiveDatabaseId.  
  
### getHiveDatabaseIdBytes()
    
    
    public abstract ByteString getHiveDatabaseIdBytes()

Required. The ID to use for the Hive Database. The maximum length is 128 characters.

`string hive_database_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hiveDatabaseId.  
  
### getHiveDatabaseOrBuilder()
    
    
    public abstract HiveDatabaseOrBuilder getHiveDatabaseOrBuilder()

Required. The database to create. The `name` field does not need to be provided.

` .google.cloud.biglake.hive.v1.HiveDatabase hive_database = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[HiveDatabaseOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveDatabaseOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent resource where this database will be created. Format: projects/{project_id_or_number}/catalogs/{catalog_id}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource where this database will be created. Format: projects/{project_id_or_number}/catalogs/{catalog_id}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### hasHiveDatabase()
    
    
    public abstract boolean hasHiveDatabase()

Required. The database to create. The `name` field does not need to be provided.

` .google.cloud.biglake.hive.v1.HiveDatabase hive_database = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hiveDatabase field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
