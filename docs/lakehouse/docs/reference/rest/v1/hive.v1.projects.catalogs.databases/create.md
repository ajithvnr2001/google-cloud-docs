---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/create/
title: Method: hive.v1.projects.catalogs.databases.create \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:28:02.919738+00:00
---

# Method: hive.v1.projects.catalogs.databases.create  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/create/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  Method: hive.v1.projects.catalogs.databases.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a new database.

### HTTP request

Choose an endpoint:

globalasia-south1asia-south2europe-west1europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central2northamerica-northeast1northamerica-northeast2us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://biglake.googleapis.com/hive/v1/{parent=projects/*/catalogs/*}/databases`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this database will be created. Format: projects/{project_id_or_number}/catalogs/{catalogId}  
  
### Query parameters

Parameters  
---  
`hiveDatabaseId` |  `string` Required. The ID to use for the Hive Database. The maximum length is 128 characters.  
  
### Request body

The request body contains an instance of `[HiveDatabase](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases#HiveDatabase)`.

### Response body

If successful, the response body contains a newly created instance of `[HiveDatabase](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases#HiveDatabase)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/bigquery`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
