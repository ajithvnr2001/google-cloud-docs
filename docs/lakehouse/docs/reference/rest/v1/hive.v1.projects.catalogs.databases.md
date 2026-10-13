---
url: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases
title: REST Resource: hive.v1.projects.catalogs.databases \u00a0|\u00a0 BigLake API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:20.428951+00:00
---

# REST Resource: hive.v1.projects.catalogs.databases  |  BigLake API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ BigLake API ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Reference ](https://docs.cloud.google.com/lakehouse/docs/quotas)



#  REST Resource: hive.v1.projects.catalogs.databases Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: HiveDatabase
    * JSON representation
  * Methods



## Resource: HiveDatabase

Stores the hive database information. It includes the database name, description, location and properties associated with the database.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "locationUri": string,
      "parameters": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name. Format: projects/{project_id_or_number}/catalogs/{catalogId}/databases/{databaseId}  
`description` |  `string` Optional. Stores the database description. The maximum length is 4000 characters.  
`locationUri` |  `string` Optional. The Cloud Storage location path where the database exists. Format: `gs://bucket/path/to/database` If unspecified, the database will be stored in the catalog location. The maximum length is 4000 characters.  
`parameters` |  `map (key: string, value: string)` Optional. Stores the properties associated with the database. The maximum size is 2 MiB.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update time of the database.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/create)`

|  Creates a new database.  
  
### `[delete](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/delete)`

|  Deletes an existing database specified by the database name.  
  
### `[get](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/get)`

|  Gets the database specified by the resource name.  
  
### `[list](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/list)`

|  List all databases in a specified catalog.  
  
### `[patch](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/hive.v1.projects.catalogs.databases/patch)`

|  Updates an existing database specified by the database name.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
