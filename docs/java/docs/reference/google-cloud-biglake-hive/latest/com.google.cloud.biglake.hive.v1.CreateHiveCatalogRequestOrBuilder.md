---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveCatalogRequestOrBuilder
title: Interface CreateHiveCatalogRequestOrBuilder (0.4.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:35.368788+00:00
---

# Interface CreateHiveCatalogRequestOrBuilder (0.4.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.CreateHiveCatalogRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateHiveCatalogRequestOrBuilder (0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface CreateHiveCatalogRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getHiveCatalog()
    
    
    public abstract HiveCatalog getHiveCatalog()

Required. The catalog to create. The `name` field does not need to be provided. Gets copied over from catalog_id.

` .google.cloud.biglake.hive.v1.HiveCatalog hive_catalog = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[HiveCatalog](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveCatalog)` | The hiveCatalog.  
  
### getHiveCatalogId()
    
    
    public abstract String getHiveCatalogId()

Required. The Hive Catalog ID to use for the catalog that will become the final component of the catalog's resource name. The maximum length is 256 characters.

`string hive_catalog_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hiveCatalogId.  
  
### getHiveCatalogIdBytes()
    
    
    public abstract ByteString getHiveCatalogIdBytes()

Required. The Hive Catalog ID to use for the catalog that will become the final component of the catalog's resource name. The maximum length is 256 characters.

`string hive_catalog_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hiveCatalogId.  
  
### getHiveCatalogOrBuilder()
    
    
    public abstract HiveCatalogOrBuilder getHiveCatalogOrBuilder()

Required. The catalog to create. The `name` field does not need to be provided. Gets copied over from catalog_id.

` .google.cloud.biglake.hive.v1.HiveCatalog hive_catalog = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[HiveCatalogOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-biglake-hive/latest/com.google.cloud.biglake.hive.v1.HiveCatalogOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The parent resource where this catalog will be created. Format: projects/{project_id_or_number}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The parent resource where this catalog will be created. Format: projects/{project_id_or_number}

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getPrimaryLocation()
    
    
    public abstract String getPrimaryLocation()

Required. The GCP region that specifies where the catalog metadata is stored, e.g. us-central1, EU, etc.

` string primary_location = 4 [json_name = "primary_location", (.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The primaryLocation.  
  
### getPrimaryLocationBytes()
    
    
    public abstract ByteString getPrimaryLocationBytes()

Required. The GCP region that specifies where the catalog metadata is stored, e.g. us-central1, EU, etc.

` string primary_location = 4 [json_name = "primary_location", (.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for primaryLocation.  
  
### hasHiveCatalog()
    
    
    public abstract boolean hasHiveCatalog()

Required. The catalog to create. The `name` field does not need to be provided. Gets copied over from catalog_id.

` .google.cloud.biglake.hive.v1.HiveCatalog hive_catalog = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the hiveCatalog field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
