---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.ImportEntitiesMetadataOrBuilder
title: Interface ImportEntitiesMetadataOrBuilder (3.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:20.117129+00:00
---

# Interface ImportEntitiesMetadataOrBuilder (3.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.ImportEntitiesMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ImportEntitiesMetadataOrBuilder (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.3.0  3.2.0  3.1.0  2.40.0  2.37.0  2.36.0  2.34.0  2.33.3  2.32.3  2.31.4  2.30.0  2.29.1  2.28.2  2.27.1  2.26.4  2.25.2  2.24.3  2.23.0  2.22.0  2.21.3  2.20.2  2.19.2  2.18.5  2.17.6 
    
    
    public interface ImportEntitiesMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCommon()
    
    
    public abstract CommonMetadata getCommon()

Metadata common to all Datastore Admin operations.

`.google.datastore.admin.v1.CommonMetadata common = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CommonMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.CommonMetadata)` | The common.  
  
### getCommonOrBuilder()
    
    
    public abstract CommonMetadataOrBuilder getCommonOrBuilder()

Metadata common to all Datastore Admin operations.

`.google.datastore.admin.v1.CommonMetadata common = 1;`

**Returns**  
---  
**Type** | **Description**  
`[CommonMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.CommonMetadataOrBuilder)` |   
  
### getEntityFilter()
    
    
    public abstract EntityFilter getEntityFilter()

Description of which entities are being imported.

`.google.datastore.admin.v1.EntityFilter entity_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[EntityFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.EntityFilter)` | The entityFilter.  
  
### getEntityFilterOrBuilder()
    
    
    public abstract EntityFilterOrBuilder getEntityFilterOrBuilder()

Description of which entities are being imported.

`.google.datastore.admin.v1.EntityFilter entity_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[EntityFilterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.EntityFilterOrBuilder)` |   
  
### getInputUrl()
    
    
    public abstract String getInputUrl()

The location of the import metadata file. This will be the same value as the google.datastore.admin.v1.ExportEntitiesResponse.output_url field.

`string input_url = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inputUrl.  
  
### getInputUrlBytes()
    
    
    public abstract ByteString getInputUrlBytes()

The location of the import metadata file. This will be the same value as the google.datastore.admin.v1.ExportEntitiesResponse.output_url field.

`string input_url = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for inputUrl.  
  
### getProgressBytes()
    
    
    public abstract Progress getProgressBytes()

An estimate of the number of bytes processed.

`.google.datastore.admin.v1.Progress progress_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Progress](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.Progress)` | The progressBytes.  
  
### getProgressBytesOrBuilder()
    
    
    public abstract ProgressOrBuilder getProgressBytesOrBuilder()

An estimate of the number of bytes processed.

`.google.datastore.admin.v1.Progress progress_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ProgressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.ProgressOrBuilder)` |   
  
### getProgressEntities()
    
    
    public abstract Progress getProgressEntities()

An estimate of the number of entities processed.

`.google.datastore.admin.v1.Progress progress_entities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Progress](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.Progress)` | The progressEntities.  
  
### getProgressEntitiesOrBuilder()
    
    
    public abstract ProgressOrBuilder getProgressEntitiesOrBuilder()

An estimate of the number of entities processed.

`.google.datastore.admin.v1.Progress progress_entities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ProgressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datastore/latest/com.google.datastore.admin.v1.ProgressOrBuilder)` |   
  
### hasCommon()
    
    
    public abstract boolean hasCommon()

Metadata common to all Datastore Admin operations.

`.google.datastore.admin.v1.CommonMetadata common = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the common field is set.  
  
### hasEntityFilter()
    
    
    public abstract boolean hasEntityFilter()

Description of which entities are being imported.

`.google.datastore.admin.v1.EntityFilter entity_filter = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the entityFilter field is set.  
  
### hasProgressBytes()
    
    
    public abstract boolean hasProgressBytes()

An estimate of the number of bytes processed.

`.google.datastore.admin.v1.Progress progress_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the progressBytes field is set.  
  
### hasProgressEntities()
    
    
    public abstract boolean hasProgressEntities()

An estimate of the number of entities processed.

`.google.datastore.admin.v1.Progress progress_entities = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the progressEntities field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
