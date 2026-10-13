---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/get/
title: Method: iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables.get \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:26.533804+00:00
---

# Method: iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables.get  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables/get/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  Method: iceberg.v1.restcatalog.v1.projects.catalogs.namespaces.tables.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Gets a table in the namespace.

### HTTP request

Choose an endpoint:

globalasia-south1asia-south2europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central2northamerica-northeast1northamerica-northeast2us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://biglake.googleapis.com/iceberg/v1/restcatalog/v1/{name=projects/*/catalogs/*/namespaces/*/tables/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Table to get in the format:  
  
### Query parameters

Parameters  
---  
`snapshots` |  `string` Optional. What snapshot to get. Valid only for tables.get.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigquery`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
