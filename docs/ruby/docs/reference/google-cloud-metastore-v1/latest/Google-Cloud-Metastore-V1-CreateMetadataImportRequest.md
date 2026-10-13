---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-CreateMetadataImportRequest/
title: Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::CreateMetadataImportRequest (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:08:33.942835+00:00
---

# Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::CreateMetadataImportRequest (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-CreateMetadataImportRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1 API - Class Google::Cloud::Metastore::V1::CreateMetadataImportRequest (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Dataproc Metastore V1 API class Google::Cloud::Metastore::V1::CreateMetadataImportRequest.

Request message for [DataprocMetastore.CreateMetadataImport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-DataprocMetastore-Client#Google__Cloud__Metastore__V1__DataprocMetastore__Client_create_metadata_import_instance_ "Google::Cloud::Metastore::V1::DataprocMetastore::Client#create_metadata_import \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #metadata_import
    
    
    def metadata_import() -> ::Google::Cloud::Metastore::V1::MetadataImport

**Returns**

  * ([::Google::Cloud::Metastore::V1::MetadataImport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-MetadataImport)) — Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field. 



### #metadata_import=
    
    
    def metadata_import=(value) -> ::Google::Cloud::Metastore::V1::MetadataImport

**Parameter**

  * **value** ([::Google::Cloud::Metastore::V1::MetadataImport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-MetadataImport)) — Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field. 



**Returns**

  * ([::Google::Cloud::Metastore::V1::MetadataImport](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1/latest/Google-Cloud-Metastore-V1-MetadataImport)) — Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field. 



### #metadata_import_id
    
    
    def metadata_import_id() -> ::String

**Returns**

  * (::String) — Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. 




### #metadata_import_id=
    
    
    def metadata_import_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. 




**Returns**

  * (::String) — Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The relative resource name of the service in which to create a metastore import, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`. 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The relative resource name of the service in which to create a metastore import, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`. 




**Returns**

  * (::String) — Required. The relative resource name of the service in which to create a metastore import, in the following form:

`projects/{project_number}/locations/{location_id}/services/{service_id}`. 




### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported. 




### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported. 




**Returns**

  * (::String) — Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
