---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search/
title: Method: migratableResources.search \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:57:21.839028+00:00
---

# Method: migratableResources.search  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: migratableResources.search Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.migratableResources.search

Searches all of the resources in automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com that can be migrated to Agent Platform's given location.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/migratableResources:search`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The location that the migratable resources should be searched from. It's the Agent Platform location that the resources can be migrated to, not the resources' original location. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`pageSize` `integer` The standard page size. The default and maximum value is 100. | `pageToken` `string` The standard page token. | `filter` `string` A filter for your search. You can use the following types of filters:

  * Resource type filters. The following strings filter for a specific type of `[MigratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MigratableResource)`: 
    * `mlEngineModelVersion:*`
    * `automlModel:*`
    * `automlDataset:*`
    * `dataLabelingDataset:*`
  * "Migrated or not" filters. The following strings filter for resources that either have or have not already been migrated: 
    * `lastMigrateTime:*` filters for migrated resources.
    * `NOT lastMigrateTime:*` filters for not yet migrated resources.



### Response body

Response message for `[MigrationService.SearchMigratableResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#google.cloud.aiplatform.v1beta1.MigrationService.SearchMigratableResources)`. If successful, the response body contains data with the following structure: | Fields  
  
`migratableResources[]` `object (`[MigratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MigratableResource)`)` All migratable resources that can be migrated to the location specified in the request. | `nextPageToken` `string` The standard next-page token. The migratableResources may not fill pageSize in SearchMigratableResourcesRequest even when there are subsequent pages. | JSON representation  
---  
      
    
    {
      "migratableResources": [
        {
          object ([MigratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MigratableResource))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.migratableResources.search`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## MigratableResource

Represents one resource that exists in automl.googleapis.com, datalabeling.googleapis.com or ml.googleapis.com.

Fields  
  
`lastMigrateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when the last migration attempt on this MigratableResource started. Will not be set if there's no migration attempt on this MigratableResource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `lastUpdateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this MigratableResource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `resource` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`mlEngineModelVersion` `object (`[MlEngineModelVersion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MlEngineModelVersion)`)` Output only. Represents one version in ml.googleapis.com. | `automlModel` `object (`[AutomlModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#AutomlModel)`)` Output only. Represents one Model in automl.googleapis.com. | `automlDataset` `object (`[AutomlDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#AutomlDataset)`)` Output only. Represents one Dataset in automl.googleapis.com. | `dataLabelingDataset  
**(deprecated)**` `object (`[DataLabelingDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#DataLabelingDataset)`)` This item is deprecated!Output only. Deprecated: data Labeling Dataset migration is no longer supported. Represents one Dataset in datalabeling.googleapis.com. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "lastMigrateTime": string,
      "lastUpdateTime": string,
    
      // resource
      "mlEngineModelVersion": {
        object ([MlEngineModelVersion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MlEngineModelVersion))
      },
      "automlModel": {
        object ([AutomlModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#AutomlModel))
      },
      "automlDataset": {
        object ([AutomlDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#AutomlDataset))
      },
      "dataLabelingDataset": {
        object ([DataLabelingDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#DataLabelingDataset))
      }
      // Union type
    }  
  
## MlEngineModelVersion

Represents one model version in ml.googleapis.com.

Fields  
  
`endpoint` `string` The ml.googleapis.com endpoint that this model version currently lives in. Example values:

  * ml.googleapis.com
  * us-centrall-ml.googleapis.com
  * europe-west4-ml.googleapis.com
  * asia-east1-ml.googleapis.com

| `version` `string` Full resource name of ml engine model version. Format: `projects/{project}/models/{model}/versions/{version}`. | JSON representation  
---  
      
    
    {
      "endpoint": string,
      "version": string
    }  
  
## AutomlModel

Represents one Model in automl.googleapis.com.

Fields  
  
`model` `string` Full resource name of automl Model. Format: `projects/{project}/locations/{location}/models/{model}`. | `modelDisplayName` `string` The Model's display name in automl.googleapis.com. | JSON representation  
---  
      
    
    {
      "model": string,
      "modelDisplayName": string
    }  
  
## AutomlDataset

Represents one Dataset in automl.googleapis.com.

Fields  
  
`dataset` `string` Full resource name of automl Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`. | `datasetDisplayName` `string` The Dataset's display name in automl.googleapis.com. | JSON representation  
---  
      
    
    {
      "dataset": string,
      "datasetDisplayName": string
    }  
  
## DataLabelingDataset

Represents one Dataset in datalabeling.googleapis.com.

Fields  
  
`dataset` `string` Full resource name of data labeling Dataset. Format: `projects/{project}/datasets/{dataset}`. | `datasetDisplayName` `string` The Dataset's display name in datalabeling.googleapis.com. | `dataLabelingAnnotatedDatasets[]` `object (`[DataLabelingAnnotatedDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#DataLabelingAnnotatedDataset)`)` The migratable AnnotatedDataset in datalabeling.googleapis.com belongs to the data labeling Dataset. | JSON representation  
---  
      
    
    {
      "dataset": string,
      "datasetDisplayName": string,
      "dataLabelingAnnotatedDatasets": [
        {
          object ([DataLabelingAnnotatedDataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#DataLabelingAnnotatedDataset))
        }
      ]
    }  
  
## DataLabelingAnnotatedDataset

Represents one AnnotatedDataset in datalabeling.googleapis.com.

Fields  
  
`annotatedDataset` `string` Full resource name of data labeling AnnotatedDataset. Format: `projects/{project}/datasets/{dataset}/annotatedDatasets/{annotatedDataset}`. | `annotatedDatasetDisplayName` `string` The AnnotatedDataset's display name in datalabeling.googleapis.com. | JSON representation  
---  
      
    
    {
      "annotatedDataset": string,
      "annotatedDatasetDisplayName": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
