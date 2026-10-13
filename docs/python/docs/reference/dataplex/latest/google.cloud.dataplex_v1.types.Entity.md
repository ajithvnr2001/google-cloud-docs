---
url: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entity
title: Class Entity (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:38.709707+00:00
---

# Class Entity (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entity

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Entity (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.2  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.2  2.1.0  2.0.1  1.13.0  1.12.3  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.2  1.5.1  1.4.3  1.3.0  1.2.0  1.1.3  1.0.1  0.2.1  0.1.0 
    
    
    Entity(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents tables and fileset metadata contained within a zone.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The resource name of the entity, of the form: `projects/{project_number}/locations/{location_id}/lakes/{lake_id}/zones/{zone_id}/entities/{id}`.   
`display_name` |  `str`   
Optional. Display name must be shorter than or equal to 256 characters.   
`description` |  `str`   
Optional. User friendly longer description text. Must be shorter than or equal to 1024 characters.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the entity was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the entity was last updated.   
`id` |  `str`   
Required. A user-provided entity ID. It is mutable, and will be used as the published table name. Specifying a new ID in an update entity request will override the existing value. The ID must contain only letters (a-z, A-Z), numbers (0-9), and underscores, and consist of 256 or fewer characters.   
`etag` |  `str`   
Optional. The etag associated with the entity, which can be retrieved with a [GetEntity][] request. Required for update and delete requests.   
`type_` |  `[google.cloud.dataplex_v1.types.Entity.Type](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entity.Type)`   
Required. Immutable. The type of entity.   
`asset` |  `str`   
Required. Immutable. The ID of the asset associated with the storage location containing the entity data. The entity must be with in the same zone with the asset.   
`data_path` |  `str`   
Required. Immutable. The storage path of the entity data. For Cloud Storage data, this is the fully-qualified path to the entity, such as `gs://bucket/path/to/data`. For BigQuery data, this is the name of the table resource, such as `projects/project_id/datasets/dataset_id/tables/table_id`.   
`data_path_pattern` |  `str`   
Optional. The set of items within the data path constituting the data in the entity, represented as a glob path. Example: `gs://bucket/path/to/data/**/*.csv`.   
`catalog_entry` |  `str`   
Output only. The name of the associated Data Catalog entry.   
`system` |  `[google.cloud.dataplex_v1.types.StorageSystem](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.StorageSystem)`   
Required. Immutable. Identifies the storage system of the entity data.   
`format_` |  `[google.cloud.dataplex_v1.types.StorageFormat](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.StorageFormat)`   
Required. Identifies the storage format of the entity data. It does not apply to entities with data stored in BigQuery.   
`compatibility` |  `[google.cloud.dataplex_v1.types.Entity.CompatibilityStatus](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Entity.CompatibilityStatus)`   
Output only. Metadata stores that the entity is compatible with.   
`access` |  `[google.cloud.dataplex_v1.types.StorageAccess](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.StorageAccess)`   
Output only. Identifies the access mechanism to the entity. Not user settable.   
`uid` |  `str`   
Output only. System generated unique ID for the Entity. This ID will be different if the Entity is deleted and re-created with the same name.   
`schema` |  `[google.cloud.dataplex_v1.types.Schema](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.Schema)`   
Required. The description of the data structure and layout. The schema is not included in list responses. It is only included in `SCHEMA` and `FULL` entity views of a `GetEntity` response.   
  
## Classes 

### CompatibilityStatus
    
    
    CompatibilityStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Provides compatibility information for various metadata stores.

### Type
    
    
    Type(value)

The type of entity.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
