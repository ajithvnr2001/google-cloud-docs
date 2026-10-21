---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate/
title: Method: migratableResources.batchMigrate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:10:02.451999+00:00
---

# Method: migratableResources.batchMigrate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: migratableResources.batchMigrate Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.migratableResources.batchMigrate

Batch migrates resources from ml.googleapis.com, automl.googleapis.com, and datalabeling.googleapis.com to Agent Platform.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{parent}/migratableResources:batchMigrate`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The location of the migrated resource will live in. Format: `projects/{project}/locations/{location}`

### Request body

The request body contains data with the following structure: | Fields  
  
`migrateResourceRequests[]` `object (`[MigrateResourceRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateResourceRequest)`)` Required. The request messages specifying the resources to migrate. They must be in the same location as the destination. Up to 50 resources can be migrated in one batch.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

## MigrateResourceRequest

Config of migrating one resource from automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com to Agent Platform. | Fields  
  
`request` `Union type`  
  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`migrateMlEngineModelVersionConfig` `object (`[MigrateMlEngineModelVersionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateMlEngineModelVersionConfig)`)` Config for migrating version in ml.googleapis.com to Agent Platform's Model. | `migrateAutomlModelConfig` `object (`[MigrateAutomlModelConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateAutomlModelConfig)`)` Config for migrating Model in automl.googleapis.com to Agent Platform's Model. | `migrateAutomlDatasetConfig` `object (`[MigrateAutomlDatasetConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateAutomlDatasetConfig)`)` Config for migrating Dataset in automl.googleapis.com to Agent Platform's Dataset. | `migrateDataLabelingDatasetConfig  
**(deprecated)**` `object (`[MigrateDataLabelingDatasetConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateDataLabelingDatasetConfig)`)` This item is deprecated!Deprecated: data labeling service is shut down. Config for migrating Dataset in datalabeling.googleapis.com to Agent Platform's Dataset. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
    
      // request
      "migrateMlEngineModelVersionConfig": {
        object ([MigrateMlEngineModelVersionConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateMlEngineModelVersionConfig))
      },
      "migrateAutomlModelConfig": {
        object ([MigrateAutomlModelConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateAutomlModelConfig))
      },
      "migrateAutomlDatasetConfig": {
        object ([MigrateAutomlDatasetConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateAutomlDatasetConfig))
      },
      "migrateDataLabelingDatasetConfig": {
        object ([MigrateDataLabelingDatasetConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateDataLabelingDatasetConfig))
      }
      // Union type
    }  
  
## MigrateMlEngineModelVersionConfig

Config for migrating version in ml.googleapis.com to Agent Platform's Model.

Fields  
  
`endpoint` `string` Required. The ml.googleapis.com endpoint that this model version should be migrated from. Example values:

  * ml.googleapis.com
  * us-centrall-ml.googleapis.com
  * europe-west4-ml.googleapis.com
  * asia-east1-ml.googleapis.com

| `modelVersion` `string` Required. Full resource name of ml engine model version. Format: `projects/{project}/models/{model}/versions/{version}`. | `modelDisplayName` `string` Required. Display name of the model in Agent Platform. System will pick a display name if unspecified. | JSON representation  
---  
      
    
    {
      "endpoint": string,
      "modelVersion": string,
      "modelDisplayName": string
    }  
  
## MigrateAutomlModelConfig

Config for migrating Model in automl.googleapis.com to Agent Platform's Model.

Fields  
  
`model` `string` Required. Full resource name of automl Model. Format: `projects/{project}/locations/{location}/models/{model}`. | `modelDisplayName` `string` Optional. Display name of the model in Agent Platform. System will pick a display name if unspecified. | JSON representation  
---  
      
    
    {
      "model": string,
      "modelDisplayName": string
    }  
  
## MigrateAutomlDatasetConfig

Config for migrating Dataset in automl.googleapis.com to Agent Platform's Dataset.

Fields  
  
`dataset` `string` Required. Full resource name of automl Dataset. Format: `projects/{project}/locations/{location}/datasets/{dataset}`. | `datasetDisplayName` `string` Required. Display name of the Dataset in Agent Platform. System will pick a display name if unspecified. | JSON representation  
---  
      
    
    {
      "dataset": string,
      "datasetDisplayName": string
    }  
  
## MigrateDataLabelingDatasetConfig

Config for migrating Dataset in datalabeling.googleapis.com to Agent Platform's Dataset.

Fields  
  
`dataset` `string` Required. Full resource name of data labeling Dataset. Format: `projects/{project}/datasets/{dataset}`. | `datasetDisplayName` `string` Optional. Display name of the Dataset in Agent Platform. System will pick a display name if unspecified. | `migrateDataLabelingAnnotatedDatasetConfigs[]` `object (`[MigrateDataLabelingAnnotatedDatasetConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateDataLabelingAnnotatedDatasetConfig)`)` Optional. Configs for migrating AnnotatedDataset in datalabeling.googleapis.com to Agent Platform's SavedQuery. The specified AnnotatedDatasets have to belong to the datalabeling Dataset. | JSON representation  
---  
      
    
    {
      "dataset": string,
      "datasetDisplayName": string,
      "migrateDataLabelingAnnotatedDatasetConfigs": [
        {
          object ([MigrateDataLabelingAnnotatedDatasetConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateDataLabelingAnnotatedDatasetConfig))
        }
      ]
    }  
  
## MigrateDataLabelingAnnotatedDatasetConfig

Config for migrating AnnotatedDataset in datalabeling.googleapis.com to Agent Platform's SavedQuery.

Fields  
  
`annotatedDataset` `string` Required. Full resource name of data labeling AnnotatedDataset. Format: `projects/{project}/datasets/{dataset}/annotatedDatasets/{annotatedDataset}`. | JSON representation  
---  
      
    
    {
      "annotatedDataset": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
