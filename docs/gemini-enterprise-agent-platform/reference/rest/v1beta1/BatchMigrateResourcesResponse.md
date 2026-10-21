---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesResponse/
title: BatchMigrateResourcesResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:21:23.344425+00:00
---

# BatchMigrateResourcesResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  BatchMigrateResourcesResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response message for `[MigrationService.BatchMigrateResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#google.cloud.aiplatform.v1beta1.MigrationService.BatchMigrateResources)`.

Fields  
  
`migrateResourceResponses[]` `object (`[MigrateResourceResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesResponse#MigrateResourceResponse)`)` Successfully migrated resources. | JSON representation  
---  
      
    
    {
      "migrateResourceResponses": [
        {
          object ([MigrateResourceResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesResponse#MigrateResourceResponse))
        }
      ]
    }  
  
## MigrateResourceResponse

Describes a successfully migrated resource.

Fields  
  
`migratableResource` `object (`[MigratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MigratableResource)`)` Before migration, the identifier in ml.googleapis.com, automl.googleapis.com or datalabeling.googleapis.com. | `migrated_resource` `Union type`  
  
After migration, the resource name in Agent Platform. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`dataset` `string` Migrated Dataset's resource name. | `model` `string` Migrated Model's resource name. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "migratableResource": {
        object ([MigratableResource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/search#MigratableResource))
      },
    
      // migrated_resource
      "dataset": string,
      "model": string
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
