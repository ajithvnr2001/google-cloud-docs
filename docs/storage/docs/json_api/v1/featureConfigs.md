---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/
title: FeatureConfigs \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:43:07.622385+00:00
---

# FeatureConfigs  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  FeatureConfigs Stay organized with collections  Save and categorize content based on your preferences. 

The `FeatureConfig` resource represents configuration for various Cloud Storage features, such as [Object enrichments](https://docs.cloud.google.com/storage/docs/object-enrichments/overview).

To try out the methods for this resource, see Methods.

## Resource representation
    
    
    {
      "name": string,
      "description": string,
      "createTime": datetime,
      "updateTime": datetime,
      "type": string,
      "filter": {
        "includedCloudStorageLocations": {
          "locations": [
            string
          ]
        },
        "excludedCloudStorageLocations": {
          "locations": [
            string
          ]
        },
        "includedCloudStorageBuckets": {
          "bucketIdRegexes": [
            string
          ]
        },
        "excludedCloudStorageBuckets": {
          "bucketIdRegexes": [
            string
          ]
        }
      },
      "autoAnnotateConfig": {
        "models": [
          {
            "name": string
          }
        ],
        "processingLocation": string
      }
    }

Property name | Value | Description | Notes  
---|---|---|---  
`name` | `string` | The name of the FeatureConfig resource. Format: `projects/PROJECT_NUMBER/locations/global/featureConfigs/FEATURE_CONFIG_ID`. |   
`description` | `string` | An optional, user-provided description of the feature configuration. | Writeable  
`createTime` | `datetime` | The creation time of the feature configuration in [RFC 3339](https://tools.ietf.org/html/rfc3339) format. |   
`updateTime` | `datetime` | The last update time of the feature configuration in [RFC 3339](https://tools.ietf.org/html/rfc3339) format. |   
`type` | `string` | The type of feature this configuration applies to. For Object enrichments, the value is `AUTO_ANNOTATE`. |   
`filter` | `object` | An optional filter to include or exclude specific locations or buckets from this configuration. If omitted, the configuration applies to all buckets in the project, subject to regional availability. | Writeable  
`filter.includedCloudStorageLocations` | `object` | Contains a list of locations to include. If present, only buckets in these locations are included in this configuration. You can specify either `includedCloudStorageLocations` or `excludedCloudStorageLocations`, but not both. | Writeable  
`filter.includedCloudStorageLocations.locations[]` | `list` | The list of locations to include, for example: `["us-east1", "us"]`. | Writeable  
`filter.excludedCloudStorageLocations` | `object` | Contains a list of locations to exclude. If present, buckets in these locations are excluded from this configuration. You can specify either `includedCloudStorageLocations` or `excludedCloudStorageLocations`, but not both. | Writeable  
`filter.excludedCloudStorageLocations.locations[]` | `list` | The list of locations to exclude, for example: `["us-west1"]`. | Writeable  
`filter.includedCloudStorageBuckets` | `object` | Contains a list of bucket name regexes to include. If present, only buckets with names matching one of these regexes are included in this configuration. You can specify either `includedCloudStorageBuckets` or `excludedCloudStorageBuckets`, but not both. | Writeable  
`filter.includedCloudStorageBuckets.bucketIdRegexes[]` | `list` | A list of RE2 regular expressions for matching bucket names to include. For example, `["^sample-bucket-"]`. | Writeable  
`filter.excludedCloudStorageBuckets` | `object` | Contains a list of bucket name regexes to exclude. If present, buckets with names matching one of these regexes are excluded from this configuration. You can specify either `includedCloudStorageBuckets` or `excludedCloudStorageBuckets`, but not both. | Writeable  
`filter.excludedCloudStorageBuckets.bucketIdRegexes[]` | `list` | A list of RE2 regular expressions for matching bucket names to exclude. | Writeable  
`autoAnnotateConfig` | `object` | If `type` is `AUTO_ANNOTATE`, this object contains the configuration for the Object enrichments feature. | Writeable  
`autoAnnotateConfig.models[]` | `list` | A list of machine learning models to use for object enrichments generation. | Writeable  
`autoAnnotateConfig.models[].name` | `string` |  The name of a model. Acceptable values are: 

  * `face-detector`
  * `object-detector`
  * `label-detector`
  * `content-safety`
  * `pdf-classification`

| Writeable  
`autoAnnotateConfig.processingLocation` | `string` | The multi-region where data processing occurs. Supported values are `us`, `eu`, and `asia`. | Writeable  
  
## Methods

[create](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/create)
    Creates a new feature configuration.
[delete](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/delete)
    Deletes the specified feature configuration.
[get](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/get)
    Returns metadata for the specified feature configuration.
[list](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/list)
    Retrieves a list of feature configurations in a given project.
[patch](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/patch)
    Updates metadata for the specified feature configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
