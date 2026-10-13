---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.CreateMetadataImportRequest
title: Google Cloud Dataproc Metastore V1alpha Client - Class CreateMetadataImportRequest (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:38.508006+00:00
---

# Google Cloud Dataproc Metastore V1alpha Client - Class CreateMetadataImportRequest (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.CreateMetadataImportRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1alpha Client - Class CreateMetadataImportRequest (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1alpha Client class CreateMetadataImportRequest.

Request message for [DataprocMetastore.CreateMetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.Client.DataprocMetastoreClient#_Google_Cloud_Metastore_V1alpha_Client_DataprocMetastoreClient__createMetadataImport__).

Generated from protobuf message `google.cloud.metastore.v1alpha.CreateMetadataImportRequest`

## Namespace

Google \ Cloud \ Metastore \ V1alpha

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`↳ metadata_import_id` |  `string`   
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
`↳ metadata_import` |  `[MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport)`   
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`↳ request_id` |  `string`   
Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request. For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.  
  
### getParent

Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetadataImportId

Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setMetadataImportId

Required. The ID of the metadata import, which is used as the final component of the metadata import's name.

This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetadataImport

Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.

**Returns**  
---  
**Type** | **Description**  
`[MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport)|null` |   
  
### hasMetadataImport

### clearMetadataImport

### setMetadataImport

Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRequestId

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setRequestId

Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments. The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The relative resource name of the service in which to create a metastore import, in the following form: `projects/{project_number}/locations/{location_id}/services/{service_id}`. Please see DataprocMetastoreClient::serviceName() for help formatting this field.  
`metadataImport` |  `[MetadataImport](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.MetadataImport)`   
Required. The metadata import to create. The `name` field is ignored. The ID of the created metadata import must be provided in the request's `metadata_import_id` field.  
`metadataImportId` |  `string`   
Required. The ID of the metadata import, which is used as the final component of the metadata import's name. This value must be between 1 and 64 characters long, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens.  
**Returns**  
---  
**Type** | **Description**  
`[CreateMetadataImportRequest](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1alpha.CreateMetadataImportRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
