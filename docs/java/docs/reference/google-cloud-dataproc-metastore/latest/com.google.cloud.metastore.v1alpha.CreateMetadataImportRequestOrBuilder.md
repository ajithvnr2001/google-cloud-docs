---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1alpha.CreateMetadataImportRequestOrBuilder
title: Interface CreateMetadataImportRequestOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:35.118566+00:00
---

# Interface CreateMetadataImportRequestOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1alpha.CreateMetadataImportRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateMetadataImportRequestOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.4  2.3.0  2.2.0  2.1.9 
    
    
    public interface CreateMetadataImportRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMetadataImport()
    
    
    public abstract MetadataImport getMetadataImport()

Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.

` .google.cloud.metastore.v1alpha.MetadataImport metadata_import = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1alpha.MetadataImport)` | The metadataImport.  
  
### getMetadataImportId()
    
    
    public abstract String getMetadataImportId()

Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.

`string metadata_import_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The metadataImportId.  
  
### getMetadataImportIdBytes()
    
    
    public abstract ByteString getMetadataImportIdBytes()

Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.

`string metadata_import_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for metadataImportId.  
  
### getMetadataImportOrBuilder()
    
    
    public abstract MetadataImportOrBuilder getMetadataImportOrBuilder()

Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.

` .google.cloud.metastore.v1alpha.MetadataImport metadata_import = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[MetadataImportOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataproc-metastore/latest/com.google.cloud.metastore.v1alpha.MetadataImportOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The relative resource name of the service in which to create a metastore import, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The relative resource name of the service in which to create a metastore import, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

`string request_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

`string request_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### hasMetadataImport()
    
    
    public abstract boolean hasMetadataImport()

Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.

` .google.cloud.metastore.v1alpha.MetadataImport metadata_import = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the metadataImport field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
