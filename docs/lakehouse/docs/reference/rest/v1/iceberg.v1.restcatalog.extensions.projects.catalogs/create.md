---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs/create/
title: Method: iceberg.v1.restcatalog.extensions.projects.catalogs.create \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:56.296888+00:00
---

# Method: iceberg.v1.restcatalog.extensions.projects.catalogs.create  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs/create/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  Method: iceberg.v1.restcatalog.extensions.projects.catalogs.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates the Iceberg REST Catalog. Google Cloud Storage Bucket catalog id is the bucket for which the catalog is created (e.g. `my-catalog` for `gs://my-catalog`).

If the bucket does not exist, of the caller does not have bucket metadata permissions, the catalog will not be created.

### HTTP request

Choose an endpoint:

globalasia-south1asia-south2europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central2northamerica-northeast1northamerica-northeast2us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://biglake.googleapis.com/iceberg/v1/restcatalog/extensions/{parent=projects/*}/catalogs`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this catalog will be created. Format: projects/{projectId}  
  
### Query parameters

Parameters  
---  
`iceberg-catalog-id` |  `string` Required. The name of the catalog.  
`primary_location` |  `string` Optional. The primary location where the catalog metadata will be stored.For Google Cloud Storage bucket catalogs and BigLake catalogs, if this is not specified, then the region is inferred from the bucket's region (`defaultLocation` bucket for BigLake catalogs). If specified, the region must be in jurisdiction (near the `defaultLocation` bucket's region and the `restrictedLocations` buckets' regions for BigLake catalogs).For federated catalogs, this must be specified and be a Lakehouse-supported location (<https://docs.cloud.google.com/lakehouse/docs/locations)>. It should be close to the remote catalog's location for the best performance and cost.  
  
### Request body

The request body contains an instance of `[IcebergCatalog](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs#IcebergCatalog)`.

### Response body

If successful, the response body contains a newly created instance of `[IcebergCatalog](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs#IcebergCatalog)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigquery`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
