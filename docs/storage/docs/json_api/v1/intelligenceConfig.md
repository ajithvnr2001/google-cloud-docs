---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/
title: IntelligenceConfigs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:20.469524+00:00
---

# IntelligenceConfigs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  IntelligenceConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EditionConfig
  * Filter
    * JSON representation
  * CloudStorageLocations
    * JSON representation
  * CloudStorageBuckets
    * JSON representation
  * EffectiveIntelligenceConfig
    * JSON representation
  * EffectiveEdition
  * Stats
    * JSON representation
  * ProcessingState
  * TrialConfig
    * JSON representation



The `IntelligenceConfig` resource associated with your organization, folder, or project.

JSON representation  
---  
      
    
    {
      "name": string,
      "editionConfig": enum ([EditionConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#EditionConfig)),
      "updateTime": string,
      "filter": {
        object ([Filter](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#Filter))
      },
      "effectiveIntelligenceConfig": {
        object ([EffectiveIntelligenceConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#EffectiveIntelligenceConfig))
      },
      "trialConfig": {
        object ([TrialConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#TrialConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the `IntelligenceConfig` resource associated with your organization, folder, or project.The name format varies based on the GCP resource hierarchy as follows:

  * For project: `projects/{projectNumber}/locations/global/intelligenceConfig`
  * For organization: `organizations/{org_id}/locations/global/intelligenceConfig`
  * For folder: `folders/{folderId}/locations/global/intelligenceConfig`

  
`editionConfig` |  `enum (`[EditionConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#EditionConfig)`)` Optional. The edition configuration of the `IntelligenceConfig` resource.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the `IntelligenceConfig` resource is last updated.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filter` |  `object (`[Filter](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#Filter)`)` Optional. Filter over location and bucket.  
`effectiveIntelligenceConfig` |  `object (`[EffectiveIntelligenceConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#EffectiveIntelligenceConfig)`)` Output only. The `IntelligenceConfig` resource that is applicable for the resource.  
`trialConfig` |  `object (`[TrialConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#TrialConfig)`)` The [30-day introductory trial configuration](https://docs.cloud.google.com/storage/docs/storage-intelligence/30-day-introductory-trial/overview) of the `IntelligenceConfig` resource.  
  
## EditionConfig

The edition configuration of the `IntelligenceConfig` resource. This signifies the edition used for configuring the `IntelligenceConfig` resource and can only take the following values: `EDITION_CONFIG_UNSPECIFIED`, `INHERIT`, `DISABLED`, `STANDARD` and `EVALUATE`.

Enums  
---  
`EDITION_CONFIG_UNSPECIFIED` | This is an unknown edition of the resource.  
`INHERIT` | The edition configuration of the parent resource. This is the default edition when there is no `IntelligenceConfig` setup for a GCP resource.  
`DISABLED` | The edition configuration is disabled for the `IntelligenceConfig` resource and its children. Filters are not applicable.  
`STANDARD` | The `IntelligenceConfig` resource is of STANDARD edition.  
`TRIAL` | The `IntelligenceConfig` resource is available in `TRIAL` edition.  
  
## Filter

Filter over location and bucket using include or exclude semantics. Resources that match the include or exclude filter are exclusively included or excluded from the Storage Intelligence plan.

JSON representation  
---  
      
    
    {
    
      // Union field cloud_storage_locations can be only one of the following:
      "includedCloudStorageLocations": {
        object ([CloudStorageLocations](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageLocations))
      },
      "excludedCloudStorageLocations": {
        object ([CloudStorageLocations](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageLocations))
      }
      // End of list of possible types for union field cloud_storage_locations.
    
      // Union field cloud_storage_buckets can be only one of the following:
      "includedCloudStorageBuckets": {
        object ([CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageBuckets))
      },
      "excludedCloudStorageBuckets": {
        object ([CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageBuckets))
      }
      // End of list of possible types for union field cloud_storage_buckets.
    }  
  
Fields  
---  
Union field `cloud_storage_locations`. Bucket locations to include or exclude. `cloud_storage_locations` can be only one of the following:  
`includedCloudStorageLocations` |  `object (`[CloudStorageLocations](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageLocations)`)` Bucket locations to include.  
`excludedCloudStorageLocations` |  `object (`[CloudStorageLocations](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageLocations)`)` Bucket locations to exclude.  
Union field `cloud_storage_buckets`. Buckets to include or exclude. `cloud_storage_buckets` can be only one of the following:  
`includedCloudStorageBuckets` |  `object (`[CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageBuckets)`)` Buckets to include.  
`excludedCloudStorageBuckets` |  `object (`[CloudStorageBuckets](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#CloudStorageBuckets)`)` Buckets to exclude.  
  
## CloudStorageLocations

Collection of bucket locations.

JSON representation  
---  
      
    
    {
      "locations": [
        string
      ]
    }  
  
Fields  
---  
`locations[]` |  `string` Optional. Bucket locations. Location can be any of the Cloud Storage regions specified in lower case format. For example, `us-east1`, `us-west1`.  
  
## CloudStorageBuckets

Collection of buckets.

JSON representation  
---  
      
    
    {
      "bucketIdRegexes": [
        string
      ]
    }  
  
Fields  
---  
`bucketIdRegexes[]` |  `string` Optional. A regex pattern for matching bucket names. Regex should follow the syntax specified in [google/re2](https://github.com/google/re2). For example, `^sample_.*` matches all buckets of the form `gs://sample_bucket-1`, `gs://sample_bucket-2`, `gs://sample_bucket-n` but not `gs://test_sample_bucket`. If you want to match a single bucket, say `gs://sample_bucket`, use `sample_bucket`.  
  
## EffectiveIntelligenceConfig

The effective `IntelligenceConfig` for the resource.

JSON representation  
---  
      
    
    {
      "effectiveEdition": enum ([EffectiveEdition](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#EffectiveEdition)),
      "intelligenceConfig": string
    }  
  
Fields  
---  
`effectiveEdition` |  `enum (`[EffectiveEdition](https://docs.cloud.google.com/storage/docs/json_api/v1/intelligenceConfig#EffectiveEdition)`)` Output only. The `IntelligenceConfig` edition that is applicable for the resource.  
`intelligenceConfig` |  `string` Output only. The `IntelligenceConfig` resource that is applied for the target resource. Format: `{organizations|folders|projects}/{id}/locations/{location}/intelligenceConfig`  
  
## EffectiveEdition

The effective edition of the `IntelligenceConfig` resource.

Enums  
---  
`EFFECTIVE_EDITION_UNSPECIFIED` | This is an unknown edition of the resource.  
`NONE` | No edition.  
`STANDARD` | The `IntelligenceConfig` resource is of STANDARD edition.  
  
## TrialConfig

The trial configuration of the `IntelligenceConfig` resource.

JSON representation  
---  
      
    
    {
      "expireTime": string,
    }  
  
Fields  
---  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the trial ends in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format.Example: `"2014-10-02T15:01:23Z"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
