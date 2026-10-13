---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles
title: REST Resource: organizations.locations.fileStoreDataProfiles \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:23.918028+00:00
---

# REST Resource: organizations.locations.fileStoreDataProfiles  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: organizations.locations.fileStoreDataProfiles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: FileStoreDataProfile
    * JSON representation
    * State
    * FileClusterSummary
      * JSON representation
    * FileClusterType
      * JSON representation
    * Cluster
    * FileStoreInfoTypeSummary
      * JSON representation
    * FileExtensionInfo
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
  
### State

Possible states of a profile. New items may be added.

Enums  
---  
`STATE_UNSPECIFIED` | Unused.  
`RUNNING` | The profile is currently running. Once a profile has finished it will transition to DONE.  
`DONE` | The profile is no longer generating. If profileStatus.status.code is 0, the profile succeeded, otherwise, it failed.  
  
### FileClusterSummary

The file cluster summary.

JSON representation  
---  
      
    
    {
      "fileClusterType": {
        object ([FileClusterType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileClusterType))
      },
      "fileStoreInfoTypeSummaries": [
        {
          object ([FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileStoreInfoTypeSummary))
        }
      ],
      "sensitivityScore": {
        object ([SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore))
      },
      "dataRiskLevel": {
        object ([DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel))
      },
      "errors": [
        {
          object ([Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error))
        }
      ],
      "fileExtensionsScanned": [
        {
          object ([FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileExtensionInfo))
        }
      ],
      "fileExtensionsSeen": [
        {
          object ([FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileExtensionInfo))
        }
      ],
      "noFilesExist": boolean
    }  
  
Fields  
---  
`fileClusterType` |  `object (`[FileClusterType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileClusterType)`)` The file cluster type.  
`fileStoreInfoTypeSummaries[]` |  `object (`[FileStoreInfoTypeSummary](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileStoreInfoTypeSummary)`)` InfoTypes detected in this cluster.  
`sensitivityScore` |  `object (`[SensitivityScore](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/SensitivityScore)`)` The sensitivity score of this cluster. The score will be SENSITIVITY_LOW if nothing has been scanned.  
`dataRiskLevel` |  `object (`[DataRiskLevel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/DataRiskLevel)`)` The data risk level of this cluster. RISK_LOW if nothing has been scanned.  
`errors[]` |  `object (`[Error](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error)`)` A list of errors detected while scanning this cluster. The list is truncated to 10 per cluster.  
`fileExtensionsScanned[]` |  `object (`[FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileExtensionInfo)`)` A sample of file types scanned in this cluster. Empty if no files were scanned. File extensions can be derived from the file name or the file content.  
`fileExtensionsSeen[]` |  `object (`[FileExtensionInfo](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.FileExtensionInfo)`)` A sample of file types seen in this cluster. Empty if no files were seen. File extensions can be derived from the file name or the file content.  
`noFilesExist` |  `boolean` True if no files exist in this cluster. If the file store had more files than could be listed, this will be false even if no files for this cluster were seen and fileExtensionsSeen is empty.  
  
### FileClusterType

Message used to identify file cluster type being profiled.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cluster": enum ([Cluster](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.Cluster))
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
File cluster type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cluster` |  `enum (`[Cluster](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles#FileStoreDataProfile.Cluster)`)` Cluster type.  
End of mutually exclusive fields.  
  
### Cluster

Cluster type. Each cluster corresponds to a set of file types. Over time, new types may be added and files may move between clusters.

Enums  
---  
`CLUSTER_UNSPECIFIED` | Unused.  
`CLUSTER_UNKNOWN` | Unsupported files.  
`CLUSTER_TEXT` | Plain text.  
`CLUSTER_STRUCTURED_DATA` | Structured data like CSV, TSV etc.  
`CLUSTER_SOURCE_CODE` | Source code.  
`CLUSTER_RICH_DOCUMENT` | Rich document like docx, xlsx etc.  
`CLUSTER_IMAGE` | Images like jpeg, bmp.  
`CLUSTER_ARCHIVE` | Archives and containers like .zip, .tar etc.  
`CLUSTER_MULTIMEDIA` | Multimedia like .mp4, .avi etc.  
`CLUSTER_EXECUTABLE` | Executable files like .exe, .class, .apk etc.  
`CLUSTER_AI_MODEL` | AI models like .tflite etc.  
  
### FileStoreInfoTypeSummary

Information regarding the discovered InfoType.

JSON representation  
---  
      
    
    {
      "infoType": {
        object ([InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType))
      }
    }  
  
Fields  
---  
`infoType` |  `object (`[InfoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType)`)` The InfoType seen.  
  
### FileExtensionInfo

Information regarding the discovered file extension.

JSON representation  
---  
      
    
    {
      "fileExtension": string
    }  
  
Fields  
---  
`fileExtension` |  `string` The file extension if set. (aka .pdf, .jpg, .txt)  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles/delete)`

|  Delete a FileStoreDataProfile.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles/get)`

|  Gets a file store data profile.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles/list)`

|  Lists file store data profiles for an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-05 UTC."],[],[]] 
