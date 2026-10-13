---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles
title: REST Resource: projects.locations.fileStoreDataProfiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:35.627723+00:00
---

# REST Resource: projects.locations.fileStoreDataProfiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.fileStoreDataProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FileStoreDataProfile
    * JSON representation
  * Methods



## Resource: FileStoreDataProfile

The profile for a file store.

  * Cloud Storage: maps 1:1 with a bucket.
  * Amazon S3: maps 1:1 with a bucket.

JSON representation  
---  
      
    
    {
      "name": string,
      "dataSourceType": {
        object ([DataSourceType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataSourceType))
      },
      "projectDataProfile": string,
      "projectId": string,
      "fileStoreLocation": string,
      "dataStorageLocations": [
        string
      ],
      "locationType": string,
      "fileStorePath": string,
      "fullResource": string,
      "configSnapshot": {
        object ([DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileConfigSnapshot))
      },
      "profileStatus": {
        object ([ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ProfileStatus))
      },
      "state": enum ([State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.State)),
      "profileLastGenerated": string,
      "resourceVisibility": enum ([ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)),
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      },
      "dataRiskLevel": {
        object ([DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel))
      },
      "createTime": string,
      "lastModifiedTime": string,
      "fileClusterSummaries": [
        {
          object ([FileClusterSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileClusterSummary))
        }
      ],
      "resourceAttributes": {
        string: {
          object ([Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value))
        },
        ...
      },
      "resourceLabels": {
        string: string,
        ...
      },
      "fileStoreInfoTypeSummaries": [
        {
          object ([FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileStoreInfoTypeSummary))
        }
      ],
      "sampleFindingsTable": {
        object ([BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable))
      },
      "fileStoreIsEmpty": boolean,
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
`projectDataProfile` |  `string` The resource name of the project data profile for this file store.  
`projectId` |  `string` The Google Cloud project ID that owns the resource. For Amazon S3 buckets, this is the AWS Account Id.  
`fileStoreLocation` |  `string` The location of the file store.

  * Cloud Storage: <https://docs.cloud.google.com/storage/docs/locations#available-locations>
  * Amazon S3: <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>

  
`dataStorageLocations[]` |  `string` For resources that have multiple storage locations, these are those regions. For Cloud Storage this is the list of regions chosen for dual-region storage. `fileStoreLocation` will normally be the corresponding multi-region for the list of individual locations. The first region is always picked as the processing and storage location for the data profile.  
`locationType` |  `string` The location type of the file store (region, dual-region, multi-region, etc). If dual-region, expect dataStorageLocations to be populated.  
`fileStorePath` |  `string` The file store path.

  * Cloud Storage: `gs://{bucket}`
  * Amazon S3: `s3://{bucket}`
  * Vertex AI dataset: `projects/{project_number}/locations/{location}/datasets/{datasetId}`

  
`fullResource` |  `string` The resource name of the resource profiled. <https://cloud.google.com/apis/design/resource_names#fullResourceName>Example format of an S3 bucket full resource name: `//cloudasset.googleapis.com/organizations/{org_id}/otherCloudConnections/aws/arn:aws:s3:::{bucketName}`  
`configSnapshot` |  `object (`[DataProfileConfigSnapshot](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataProfileConfigSnapshot)`)` The snapshot of the configurations used to generate the profile.  
`profileStatus` |  `object (`[ProfileStatus](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ProfileStatus)`)` Success or error status from the most recent profile generation attempt. May be empty if the profile is still being generated.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.State)`)` State of a profile.  
`profileLastGenerated` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The last time the profile was generated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`resourceVisibility` |  `enum (`[ResourceVisibility](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/ResourceVisibility)`)` How broadly a resource has been shared.  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` The sensitivity score of this resource.  
`dataRiskLevel` |  `object (`[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel)`)` The data risk level of this resource.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the file store was first created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastModifiedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the file store was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`fileClusterSummaries[]` |  `object (`[FileClusterSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileClusterSummary)`)` FileClusterSummary per each cluster.  
`resourceAttributes` |  `map (key: string, value: object (`[Value](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Value)`))` Attributes of the resource being profiled. Currently used attributes:

  * customer_managed_encryption: boolean 
    * true: the resource is encrypted with a customer-managed key.
    * false: the resource is encrypted with a provider-managed key.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`resourceLabels` |  `map (key: string, value: string)` The labels applied to the resource at the time the profile was generated.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`fileStoreInfoTypeSummaries[]` |  `object (`[FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileStoreInfoTypeSummary)`)` InfoTypes detected in this file store.  
`sampleFindingsTable` |  `object (`[BigQueryTable](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/BigQueryTable)`)` The BigQuery table to which the sample findings are written.  
`fileStoreIsEmpty` |  `boolean` The file store does not have any files. If the profiling operation failed, this is false.  
`tags[]` |  `object (`[Tag](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Tag)`)` The tags attached to the resource, including any tags attached during profiling.  
`relatedResources[]` |  `object (`[RelatedResource](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/RelatedResource)`)` Resources related to this profile.  
`domains[]` |  `object (`[Domain](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Domain)`)` Domains associated with the profile.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles/delete)`

|  Delete a FileStoreDataProfile.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles/get)`

|  Gets a file store data profile.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles/list)`

|  Lists file store data profiles for an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
