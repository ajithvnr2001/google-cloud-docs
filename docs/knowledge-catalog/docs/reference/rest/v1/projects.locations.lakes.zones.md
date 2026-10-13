---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones
title: REST Resource: projects.locations.lakes.zones \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:05.505415+00:00
---

# REST Resource: projects.locations.lakes.zones  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  REST Resource: projects.locations.lakes.zones Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Zone
    * JSON representation
  * Type
  * DiscoverySpec
    * JSON representation
  * CsvOptions
    * JSON representation
  * JsonOptions
    * JSON representation
  * ResourceSpec
    * JSON representation
  * LocationType
  * Methods



## Resource: Zone

A zone represents a logical group of related assets within a lake. A zone can be used to map to organizational structure or represent stages of data readiness from raw to curated. It provides managing behavior that is shared or inherited by all contained assets.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uid": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "state": enum ([State](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/State)),
      "type": enum ([Type](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#Type)),
      "discoverySpec": {
        object ([DiscoverySpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#DiscoverySpec))
      },
      "resourceSpec": {
        object ([ResourceSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#ResourceSpec))
      },
      "assetStatus": {
        object ([AssetStatus](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/AssetStatus))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The relative resource name of the zone, of the form: `projects/{projectNumber}/locations/{locationId}/lakes/{lakeId}/zones/{zoneId}`.  
`displayName` |  `string` Optional. User friendly display name.  
`uid` |  `string` Output only. System generated globally unique ID for the zone. This ID will be different if the zone is deleted and re-created with the same name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the zone was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the zone was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User defined labels for the zone.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. Description of the zone.  
`state` |  `enum (`[State](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/State)`)` Output only. Current state of the zone.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#Type)`)` Required. Immutable. The type of the zone.  
`discoverySpec` |  `object (`[DiscoverySpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#DiscoverySpec)`)` Optional. Specification of the discovery feature applied to data in this zone.  
`resourceSpec` |  `object (`[ResourceSpec](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#ResourceSpec)`)` Required. Specification of the resources that are referenced by the assets within this zone.  
`assetStatus` |  `object (`[AssetStatus](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/AssetStatus)`)` Output only. Aggregated status of the underlying assets of the zone.  
  
## Type

Type of zone.

Enums  
---  
`TYPE_UNSPECIFIED` | Zone type not specified.  
`RAW` | A zone that contains data that needs further processing before it is considered generally ready for consumption and analytics workloads.  
`CURATED` | A zone that contains data that is considered to be ready for broader consumption and analytics workloads. Curated structured data stored in Cloud Storage must conform to certain file formats (parquet, avro and orc) and organized in a hive-compatible directory layout.  
  
## DiscoverySpec

Settings to manage the metadata discovery and publishing in a zone.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "includePatterns": [
        string
      ],
      "excludePatterns": [
        string
      ],
      "csvOptions": {
        object ([CsvOptions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#CsvOptions))
      },
      "jsonOptions": {
        object ([JsonOptions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#JsonOptions))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "schedule": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`enabled` |  `boolean` Required. Whether discovery is enabled.  
`includePatterns[]` |  `string` Optional. The list of patterns to apply for selecting data to include during discovery if only a subset of the data should considered. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names.  
`excludePatterns[]` |  `string` Optional. The list of patterns to apply for selecting data to exclude during discovery. For Cloud Storage bucket assets, these are interpreted as glob patterns used to match object names. For BigQuery dataset assets, these are interpreted as patterns to match table names.  
`csvOptions` |  `object (`[CsvOptions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#CsvOptions)`)` Optional. Configuration for CSV data.  
`jsonOptions` |  `object (`[JsonOptions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#JsonOptions)`)` Optional. Configuration for Json data.  
Determines when discovery is triggered. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`schedule` |  `string` Optional. Cron schedule (<https://en.wikipedia.org/wiki/Cron>) for running discovery periodically. Successive discovery runs must be scheduled at least 60 minutes apart. The default value is to run discovery every 60 minutes.To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, `CRON_TZ=America/New_York 1 * * * *`, or `TZ=America/New_York 1 * * * *`.  
End of mutually exclusive fields.  
  
## CsvOptions

Describe CSV and similar semi-structured data formats.

JSON representation  
---  
      
    
    {
      "headerRows": integer,
      "delimiter": string,
      "encoding": string,
      "disableTypeInference": boolean
    }  
  
Fields  
---  
`headerRows` |  `integer` Optional. The number of rows to interpret as header rows that should be skipped when reading data rows.  
`delimiter` |  `string` Optional. The delimiter being used to separate values. This defaults to ','.  
`encoding` |  `string` Optional. The character encoding of the data. The default is UTF-8.  
`disableTypeInference` |  `boolean` Optional. Whether to disable the inference of data type for CSV data. If true, all columns will be registered as strings.  
  
## JsonOptions

Describe JSON data format.

JSON representation  
---  
      
    
    {
      "encoding": string,
      "disableTypeInference": boolean
    }  
  
Fields  
---  
`encoding` |  `string` Optional. The character encoding of the data. The default is UTF-8.  
`disableTypeInference` |  `boolean` Optional. Whether to disable the inference of data type for Json data. If true, all columns will be registered as their primitive types (strings, number or boolean).  
  
## ResourceSpec

Settings for resources attached as assets within a zone.

JSON representation  
---  
      
    
    {
      "locationType": enum ([LocationType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#LocationType))
    }  
  
Fields  
---  
`locationType` |  `enum (`[LocationType](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones#LocationType)`)` Required. Immutable. The location type of the resources that are allowed to be attached to the assets within this zone.  
  
## LocationType

Location type of the resources attached to a zone.

Enums  
---  
`LOCATION_TYPE_UNSPECIFIED` | Unspecified location type.  
`SINGLE_REGION` | Resources that are associated with a single region.  
`MULTI_REGION` | Resources that are associated with a multi-region location.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/create)`

|  Creates a zone resource within a lake.  
  
### `[delete](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/delete)`

|  Deletes a zone resource.  
  
### `[get](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/get)`

|  Retrieves a zone resource.  
  
### `[getIamPolicy](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/list)`

|  Lists zone resources in a lake.  
  
### `[patch](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/patch)`

|  Updates a zone resource.  
  
### `[setIamPolicy](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.lakes.zones/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
