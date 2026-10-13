---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans
title: REST Resource: projects.locations.dataScans \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:54.256567+00:00
---

# REST Resource: projects.locations.dataScans  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  REST Resource: projects.locations.dataScans Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DataScan
    * JSON representation
  * DataSource
    * JSON representation
  * ExecutionSpec
    * JSON representation
  * Trigger
    * JSON representation
  * OnDemand
  * Schedule
    * JSON representation
  * OneTime
    * JSON representation
  * ExecutionStatus
    * JSON representation
  * ExecutionIdentity
    * JSON representation
  * DataplexServiceAgent
  * UserCredential
  * ServiceAccount
    * JSON representation
  * Methods



## Resource: DataScan

Represents a user-visible job which provides the insights for the related data source.

For example:

  * Data quality: generates queries based on the rules and runs against the data to get data quality check results. For more information, see [Auto data quality overview](https://cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).
  * Data profile: analyzes the data in tables and generates insights about the structure, content and relationships (such as null percent, cardinality, min/max/mean, etc). For more information, see [About data profiling](https://cloud.google.com/knowledge-catalog/docs/data-profiling-overview).
  * Data discovery: scans data in Cloud Storage buckets to extract and then catalog metadata. For more information, see [Discover and catalog Cloud Storage data](https://cloud.google.com/bigquery/docs/automatic-discovery).
  * Data documentation: analyzes the table or dataset metadata and generates insights. For tables, insights include descriptions and sample SQL queries. For datasets, insights include descriptions, schema relationships and sample SQL queries. For more information, see [Generate data insights in BigQuery](https://cloud.google.com/bigquery/docs/data-insights).

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "description": string,
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/State)),
      "createTime": string,
      "updateTime": string,
      "data": {
        object ([DataSource](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#DataSource))
      },
      "executionSpec": {
        object ([ExecutionSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ExecutionSpec))
      },
      "executionStatus": {
        object ([ExecutionStatus](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ExecutionStatus))
      },
      "type": enum ([DataScanType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataScanType)),
      "executionIdentity": {
        object ([ExecutionIdentity](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ExecutionIdentity))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dataQualitySpec": {
        object ([DataQualitySpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec))
      },
      "dataProfileSpec": {
        object ([DataProfileSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataProfileSpec))
      },
      "dataDiscoverySpec": {
        object ([DataDiscoverySpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDiscoverySpec))
      },
      "dataDocumentationSpec": {
        object ([DataDocumentationSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDocumentationSpec))
      },
      "unstructuredDataProfileSpec": {
        object ([UnstructuredDataProfileSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/UnstructuredDataProfileSpec))
      }
      // End of mutually exclusive fields.
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dataQualityResult": {
        object ([DataQualityResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityResult))
      },
      "dataProfileResult": {
        object ([DataProfileResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataProfileResult))
      },
      "dataDiscoveryResult": {
        object ([DataDiscoveryResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDiscoveryResult))
      },
      "dataDocumentationResult": {
        object ([DataDocumentationResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDocumentationResult))
      },
      "unstructuredDataProfileResult": {
        object ([UnstructuredDataProfileResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/UnstructuredDataProfileResult))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The relative resource name of the scan, of the form: `projects/{project}/locations/{locationId}/dataScans/{datascanId}`, where `project` refers to a _projectId_ or _projectNumber_ and `locationId` refers to a Google Cloud region.  
`uid` |  `string` Output only. System generated globally unique ID for the scan. This ID will be different if the scan is deleted and re-created with the same name.  
`description` |  `string` Optional. Description of the scan.

  * Must be between 1-1024 characters.

  
`displayName` |  `string` Optional. User friendly display name.

  * Must be between 1-256 characters.

  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels for the scan.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/State)`)` Output only. Current state of the DataScan.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the scan was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the scan was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`data` |  `object (`[DataSource](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#DataSource)`)` Required. The data source for DataScan.  
`executionSpec` |  `object (`[ExecutionSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ExecutionSpec)`)` Optional. DataScan execution settings.If not specified, the fields in it will use their default values.  
`executionStatus` |  `object (`[ExecutionStatus](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ExecutionStatus)`)` Output only. Status of the data scan execution.  
`type` |  `enum (`[DataScanType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataScanType)`)` Output only. The type of DataScan.  
`executionIdentity` |  `object (`[ExecutionIdentity](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ExecutionIdentity)`)` Optional. Immutable. The identity to run the datascan. If not specified, defaults to the Dataplex Service Agent.  
Data scan related setting. The settings are required and immutable. After you configure the settings for one type of data scan, you can't change the data scan to a different type of data scan. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dataQualitySpec` |  `object (`[DataQualitySpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualitySpec)`)` Settings for a data quality scan.  
`dataProfileSpec` |  `object (`[DataProfileSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataProfileSpec)`)` Settings for a data profile scan.  
`dataDiscoverySpec` |  `object (`[DataDiscoverySpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDiscoverySpec)`)` Settings for a data discovery scan.  
`dataDocumentationSpec` |  `object (`[DataDocumentationSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDocumentationSpec)`)` Settings for a data documentation scan.  
`unstructuredDataProfileSpec` |  `object (`[UnstructuredDataProfileSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/UnstructuredDataProfileSpec)`)` Optional. Settings for an unstructured data profile scan.  
End of mutually exclusive fields.  
The result of the data scan. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dataQualityResult` |  `object (`[DataQualityResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataQualityResult)`)` Output only. The result of a data quality scan.  
`dataProfileResult` |  `object (`[DataProfileResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataProfileResult)`)` Output only. The result of a data profile scan.  
`dataDiscoveryResult` |  `object (`[DataDiscoveryResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDiscoveryResult)`)` Output only. The result of a data discovery scan.  
`dataDocumentationResult` |  `object (`[DataDocumentationResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/DataDocumentationResult)`)` Output only. The result of a data documentation scan.  
`unstructuredDataProfileResult` |  `object (`[UnstructuredDataProfileResult](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/UnstructuredDataProfileResult)`)` Output only. The result of an unstructured data profile scan.  
End of mutually exclusive fields.  
  
## DataSource

The data source for DataScan.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "entity": string,
      "resource": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The source is required and immutable. Once it is set, it cannot be change to others. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`entity` |  `string` Immutable. The Dataplex Universal Catalog entity that represents the data source (e.g. BigQuery table) for DataScan, of the form: `projects/{projectNumber}/locations/{locationId}/lakes/{lakeId}/zones/{zoneId}/entities/{entityId}`.  
`resource` |  `string` Immutable. The service-qualified full resource name of the cloud resource for a DataScan job to scan against. The field could either be: Cloud Storage bucket for DataDiscoveryScan Format: //storage.googleapis.com/projects/PROJECT_ID/buckets/BUCKET_ID or BigQuery table of type "TABLE" for DataProfileScan/DataQualityScan/DataDocumentationScan Format: //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID or BigQuery dataset for DataDocumentationScan only Format: //bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID  
End of mutually exclusive fields.  
  
## ExecutionSpec

DataScan execution settings.

JSON representation  
---  
      
    
    {
      "trigger": {
        object ([Trigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#Trigger))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "field": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`trigger` |  `object (`[Trigger](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#Trigger)`)` Optional. Spec related to how often and when a scan should be triggered.If not specified, the default is `OnDemand`, which means the scan will not run until the user calls `dataScans.run` API.  
Spec related to incremental scan of the dataWhen an option is selected for incremental scan, it cannot be unset or changed. If not specified, a data scan will run for all data in the table. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`field` |  `string` Immutable. The unnested field (of type _Date_ or _Timestamp_) that contains values which monotonically increase over time.If not specified, a data scan will run for all data in the table.  
End of mutually exclusive fields.  
  
## Trigger

DataScan scheduling and trigger settings.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "onDemand": {
        object ([OnDemand](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#OnDemand))
      },
      "schedule": {
        object ([Schedule](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#Schedule))
      },
      "oneTime": {
        object ([OneTime](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#OneTime))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
DataScan scheduling and trigger settings.If not specified, the default is `onDemand`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`onDemand` |  `object (`[OnDemand](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#OnDemand)`)` The scan runs once via `dataScans.run` API.  
`schedule` |  `object (`[Schedule](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#Schedule)`)` The scan is scheduled to run periodically.  
`oneTime` |  `object (`[OneTime](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#OneTime)`)` The scan runs once, and does not create an associated ScanJob child resource.  
End of mutually exclusive fields.  
  
## OnDemand

This type has no fields.

The scan runs once via `dataScans.run` API.

## Schedule

The scan is scheduled to run periodically.

JSON representation  
---  
      
    
    {
      "cron": string
    }  
  
Fields  
---  
`cron` |  `string` Required. [Cron](https://en.wikipedia.org/wiki/Cron) schedule for running scans periodically.To explicitly set a timezone in the cron tab, apply a prefix in the cron tab: **"CRON_TZ=${IANA_TIME_ZONE}"** or **"TZ=${IANA_TIME_ZONE}"**. The **${IANA_TIME_ZONE}** may only be a valid string from IANA time zone database ([wikipedia](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List)). For example, `CRON_TZ=America/New_York 1 * * * *`, or `TZ=America/New_York 1 * * * *`.This field is required for Schedule scans.  
  
## OneTime

The scan runs once using create API.

JSON representation  
---  
      
    
    {
      "ttlAfterScanCompletion": string
    }  
  
Fields  
---  
`ttlAfterScanCompletion` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Time to live for OneTime scans. default value is 24 hours, minimum value is 0 seconds, and maximum value is 365 days. The time is calculated from the data scan job completion time. If value is set as 0 seconds, the scan will be immediately deleted upon job completion, regardless of whether the job succeeded or failed.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ExecutionStatus

Status of the data scan execution.

JSON representation  
---  
      
    
    {
      "latestJobStartTime": string,
      "latestJobEndTime": string,
      "latestJobCreateTime": string
    }  
  
Fields  
---  
`latestJobStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time when the latest DataScanJob started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`latestJobEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time when the latest DataScanJob ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`latestJobCreateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time when the DataScanJob execution was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ExecutionIdentity

The identity to run the datascan.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "dataplexServiceAgent": {
        object ([DataplexServiceAgent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#DataplexServiceAgent))
      },
      "userCredential": {
        object ([UserCredential](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#UserCredential))
      },
      "serviceAccount": {
        object ([ServiceAccount](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ServiceAccount))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The identity to run the datascan. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`dataplexServiceAgent` |  `object (`[DataplexServiceAgent](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#DataplexServiceAgent)`)` Optional. The Dataplex service agent associated with the user's project.  
`userCredential` |  `object (`[UserCredential](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#UserCredential)`)` Optional. The credential of the calling user. Supports only ONE_TIME trigger type.  
`serviceAccount` |  `object (`[ServiceAccount](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans#ServiceAccount)`)` Optional. The provided service account.  
End of mutually exclusive fields.  
  
## DataplexServiceAgent

This type has no fields.

The Dataplex service agent associated with the user's project.

## UserCredential

This type has no fields.

The credential of the calling user.

## ServiceAccount

The service account

JSON representation  
---  
      
    
    {
      "email": string
    }  
  
Fields  
---  
`email` |  `string` Required. Service account email. The datascan will execute with this service account's credentials. The user calling this API must have permissions to act as this service account. Dataplex service agent must be granted iam.serviceAccounts.getAccessToken permission on this service account, for example, through the iam.serviceAccountTokenCreator role .  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/create)`

|  Creates a DataScan resource.  
  
### `[delete](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/delete)`

|  Deletes a DataScan resource.  
  
### `[generateDataQualityRules](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/generateDataQualityRules)`

|  Generates recommended data quality rules based on the results of a data profiling scan.  
  
### `[get](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/get)`

|  Gets a DataScan resource.  
  
### `[getIamPolicy](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/list)`

|  Lists DataScans.  
  
### `[patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/patch)`

|  Updates a DataScan resource.  
  
### `[run](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/run)`

|  Runs an on-demand execution of a DataScan  
  
### `[setIamPolicy](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataScans/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
