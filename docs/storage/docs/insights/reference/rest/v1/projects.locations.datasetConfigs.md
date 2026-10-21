---
url: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs
title: REST Resource: projects.locations.datasetConfigs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:36.480572+00:00
---

# REST Resource: projects.locations.datasetConfigs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  REST Resource: projects.locations.datasetConfigs Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: DatasetConfig

Message describing the dataset configuration properties. For more information, see [Dataset configuration properties](https://cloud.google.com/storage/docs/insights/datasets#dataset-config).

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "uid": string,
      "organizationNumber": string,
      "includeNewlyCreatedBuckets": boolean,
      "retentionPeriodDays": integer,
      "link": {
        object ([Link](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#Link))
      },
      "identity": {
        object ([Identity](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#Identity))
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status))
      },
      "datasetConfigState": enum ([ConfigState](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#ConfigState)),
      "description": string,
    
      // Union field source_options can be only one of the following:
      "sourceProjects": {
        object ([SourceProjects](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#SourceProjects))
      },
      "sourceFolders": {
        object ([SourceFolders](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#SourceFolders))
      },
      "organizationScope": boolean,
      "cloudStorageObjectPath": string
      // End of list of possible types for union field source_options.
    
      // Union field cloud_storage_locations can be only one of the following:
      "includeCloudStorageLocations": {
        object ([CloudStorageLocations](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageLocations))
      },
      "excludeCloudStorageLocations": {
        object ([CloudStorageLocations](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageLocations))
      }
      // End of list of possible types for union field cloud_storage_locations.
    
      // Union field cloud_storage_buckets can be only one of the following:
      "includeCloudStorageBuckets": {
        object ([CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageBuckets))
      },
      "excludeCloudStorageBuckets": {
        object ([CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageBuckets))
      }
      // End of list of possible types for union field cloud_storage_buckets.
      "activityDataRetentionPeriodDays": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. name of resource  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The UTC time at which the dataset configuration was created. This is auto-populated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The UTC time at which the dataset configuration was last updated. This is auto-populated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. System generated unique identifier for the resource.  
`organizationNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Organization resource ID that the source projects should belong to. Projects that do not belong to the provided organization are not considered when creating the dataset.  
`includeNewlyCreatedBuckets` |  `boolean` If set to `true`, the request includes all the newly created buckets in the dataset that meet the inclusion and exclusion rules.  
`retentionPeriodDays` |  `integer` Number of days of history that must be retained.  
`link` |  `object (`[Link](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#Link)`)` Details of the linked dataset.  
`identity` |  `object (`[Identity](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#Identity)`)` Identity used by this `datasetConfig`.  
`status` |  `object (`[Status](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/Status)`)` Output only. Status of the `datasetConfig`.  
`datasetConfigState` |  `enum (`[ConfigState](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#ConfigState)`)` Output only. State of the `datasetConfig`.  
`description` |  `string` Optional. A user-provided description for the dataset configuration.Maximum length: 256 characters.  
Union field `source_options`. Defines the options for providing source identifiers for the dataset. `source_options` can be only one of the following:  
`sourceProjects` |  `object (`[SourceProjects](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#SourceProjects)`)` Defines the options for providing source projects for the dataset.  
`sourceFolders` |  `object (`[SourceFolders](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#SourceFolders)`)` Defines the options for providing source folders for the dataset.  
`organizationScope` |  `boolean` Defines the options for providing a source organization for the dataset.  
`cloudStorageObjectPath` |  `string` Input only. Cloud Storage object path containing a list of project or folder numbers to include in the dataset; it cannot contain a mix of project and folders.The object must be a text file where each line has one of the following entries:

  * Project number, formatted as `projects/{projectNumber}`, for example, `projects/1234567890`.
  * Folder identifier, formatted as `folders/{folder_number}`, for example, `folders/9876543210`. Path must be in the format `gs://{bucketName}/{objectName}`.

  
Union field `cloud_storage_locations`. Cloud Storage locations to include or exclude. `cloud_storage_locations` can be only one of the following:  
`includeCloudStorageLocations` |  `object (`[CloudStorageLocations](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageLocations)`)`  
`excludeCloudStorageLocations` |  `object (`[CloudStorageLocations](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageLocations)`)`  
Union field `cloud_storage_buckets`. Cloud Storage buckets to include or exclude. `cloud_storage_buckets` can be only one of the following:  
`includeCloudStorageBuckets` |  `object (`[CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageBuckets)`)`  
`excludeCloudStorageBuckets` |  `object (`[CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageBuckets)`)`  
`activityDataRetentionPeriodDays` |  `integer` Optional. When set, overrides the retention period for activity data. If not set, activity data uses the value specified in `retentionPeriodDays`.  
  
## SourceProjects

Collection of project numbers

JSON representation  
---  
      
    
    {
      "projectNumbers": [
        string
      ]
    }  
  
Fields  
---  
`projectNumbers[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)`  
  
## SourceFolders

Specifies a set of folders to include in the dataset

JSON representation  
---  
      
    
    {
      "folderNumbers": [
        string
      ]
    }  
  
Fields  
---  
`folderNumbers[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The list of folder numbers to include in the dataset.  
  
## CloudStorageLocations

Collection of Cloud Storage locations.

JSON representation  
---  
      
    
    {
      "locations": [
        string
      ]
    }  
  
Fields  
---  
`locations[]` |  `string`  
  
## CloudStorageBuckets

Collection of Cloud Storage buckets.

JSON representation  
---  
      
    
    {
      "cloudStorageBuckets": [
        {
          object ([CloudStorageBucket](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageBucket))
        }
      ]
    }  
  
Fields  
---  
`cloudStorageBuckets[]` |  `object (`[CloudStorageBucket](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#CloudStorageBucket)`)`  
  
## CloudStorageBucket

Defines the bucket by its name or a regex pattern to match buckets.

JSON representation  
---  
      
    
    {
    
      // Union field cloud_storage_bucket can be only one of the following:
      "bucketName": string,
      "bucketPrefixRegex": string
      // End of list of possible types for union field cloud_storage_bucket.
    }  
  
Fields  
---  
Union field `cloud_storage_bucket`.`cloud_storage_bucket` can be only one of the following:  
`bucketName` |  `string` Cloud Storage bucket name.  
`bucketPrefixRegex` |  `string` A regex pattern for bucket names matching the regex. Regex should follow the syntax specified in `google/re2` on GitHub.  
  
## Link

Defines the details about the linked dataset.

JSON representation  
---  
      
    
    {
      "dataset": string,
      "linked": boolean
    }  
  
Fields  
---  
`dataset` |  `string` Output only. Dataset name for linked dataset.  
`linked` |  `boolean` Output only. State of the linked dataset.  
  
## Identity

Identity lets the user provide the type of identity to use, and outputs the identity string that can be used for IAM policy changes.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([IdentityType](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#IdentityType))
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the identity.  
`type` |  `enum (`[IdentityType](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs#IdentityType)`)` Type of identity to use for the datasetConfig.  
  
## IdentityType

Type of service account to use for the dataset configuration.

Enums  
---  
`IDENTITY_TYPE_UNSPECIFIED` | Default is unspecified and should not be used.  
`IDENTITY_TYPE_PER_CONFIG` | Google managed service account per resource.  
`IDENTITY_TYPE_PER_PROJECT` | Google managed service account per project.  
  
## ConfigState

State of the configuration.

Enums  
---  
`CONFIG_STATE_UNSPECIFIED` | Unspecified state.  
`CONFIG_STATE_ACTIVE` | Active configuration indicates that the configuration is actively ingesting data.  
`CONFIG_STATE_VERIFICATION_IN_PROGRESS` | In this state, the configuration is being verified for various permissions.  
`CONFIG_STATE_CREATED` | Configuration is created and further processing needs to happen.  
`CONFIG_STATE_PROCESSING` | Configuration is under processing  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/create)`

|  Creates a dataset configuration in a given project for a given location.  
  
### `[delete](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/delete)`

|  Deletes a dataset configuration in a given project for a given location.  
  
### `[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/get)`

|  Gets the dataset configuration in a given project for a given location.  
  
### `[linkDataset](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/linkDataset)`

|  Links a dataset to BigQuery in a given project for a given location.  
  
### `[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/list)`

|  Lists the dataset configurations in a given project for a given location.  
  
### `[patch](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/patch)`

|  Updates a dataset configuration in a given project for a given location.  
  
### `[unlinkDataset](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/unlinkDataset)`

|  Unlinks a dataset from BigQuery in a given project for a given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
