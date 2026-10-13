---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles
title: REST Resource: projects.locations.tableDataProfiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:41.057494+00:00
---

# REST Resource: projects.locations.tableDataProfiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.tableDataProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TableDataProfile
    * JSON representation
  * Methods



## Resource: TableDataProfile

The profile for a scanned table.

JSON representation  
---  
      
    
    {
      "name": string,
      "dataSourceType": {
        object ([DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType))
      },
      "projectDataProfile": string,
      "datasetProjectId": string,
      "datasetLocation": string,
      "datasetId": string,
      "tableId": string,
      "fullResource": string,
      "profileStatus": {
        object ([ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ProfileStatus))
      },
      "state": enum ([State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile.State)),
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      },
      "dataRiskLevel": {
        object ([DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel))
      },
      "predictedInfoTypes": [
        {
          object ([InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoTypeSummary))
        }
      ],
      "otherInfoTypes": [
        {
          object ([OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherInfoTypeSummary))
        }
      ],
      "configSnapshot": {
        object ([DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileConfigSnapshot))
      },
      "lastModifiedTime": string,
      "expirationTime": string,
      "scannedColumnCount": string,
      "failedColumnCount": string,
      "tableSizeBytes": string,
      "rowCount": string,
      "encryptionStatus": enum ([EncryptionStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile.EncryptionStatus)),
      "resourceVisibility": enum ([ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)),
      "profileLastGenerated": string,
      "resourceLabels": {
        string: string,
        ...
      },
      "createTime": string,
      "sampleFindingsTable": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      },
      "tags": [
        {
          object ([Tag](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Tag))
        }
      ],
      "relatedResources": [
        {
          object ([RelatedResource](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RelatedResource))
        }
      ],
      "domains": [
        {
          object ([Domain](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Domain))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The name of the profile.  
`dataSourceType` |  `object (`[DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType)`)` The resource type that was profiled.  
`projectDataProfile` |  `string` The resource name of the project data profile for this table.  
`datasetProjectId` |  `string` The Google Cloud project ID that owns the resource.  
`datasetLocation` |  `string` If supported, the location where the dataset's data is stored. See <https://docs.cloud.google.com/bigquery/docs/locations> for supported locations.  
`datasetId` |  `string` If the resource is BigQuery, the dataset ID.  
`tableId` |  `string` The table ID.  
`fullResource` |  `string` The Cloud Asset Inventory resource that was profiled in order to generate this TableDataProfile. <https://cloud.google.com/apis/design/resource_names#fullResourceName>  
`profileStatus` |  `object (`[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ProfileStatus)`)` Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile.State)`)` State of a profile. This will always be set to DONE when the table data profile is written to another service like BigQuery or Pub/Sub.  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` The sensitivity score of this table.  
`dataRiskLevel` |  `object (`[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel)`)` The data risk level of this table.  
`predictedInfoTypes[]` |  `object (`[InfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoTypeSummary)`)` The infoTypes predicted from this table's data.  
`otherInfoTypes[]` |  `object (`[OtherInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/OtherInfoTypeSummary)`)` Other infoTypes found in this table's data.  
`configSnapshot` |  `object (`[DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileConfigSnapshot)`)` The snapshot of the configurations used to generate the profile.  
`lastModifiedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when this table was last modifiedUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The time when this table expires.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`scannedColumnCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of columns profiled in the table.  
`failedColumnCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of columns skipped in the table because of an error.  
`tableSizeBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the table when the profile was generated.  
`rowCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of rows in the table when the profile was generated. This will not be populated for BigLake tables.  
`encryptionStatus` |  `enum (`[EncryptionStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles#TableDataProfile.EncryptionStatus)`)` How the table is encrypted.  
`resourceVisibility` |  `enum (`[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)`)` How broadly a resource has been shared.  
`profileLastGenerated` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time the profile was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resourceLabels` |  `map (key: string, value: string)` The labels applied to the resource at the time the profile was generated.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time at which the table was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sampleFindingsTable` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` The BigQuery table to which the sample findings are written.  
`tags[]` |  `object (`[Tag](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Tag)`)` The tags attached to the table, including any tags attached during profiling. Because tags are attached to Cloud SQL instances rather than Cloud SQL tables, this field is empty for Cloud SQL table profiles.  
`relatedResources[]` |  `object (`[RelatedResource](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RelatedResource)`)` Resources related to this profile.  
`domains[]` |  `object (`[Domain](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Domain)`)` Domains associated with the profile.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles/delete)`

|  Delete a TableDataProfile.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles/get)`

|  Gets a table data profile.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles/list)`

|  Lists table data profiles for an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
