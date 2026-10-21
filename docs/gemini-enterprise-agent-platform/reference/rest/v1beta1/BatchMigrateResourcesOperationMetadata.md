---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesOperationMetadata/
title: BatchMigrateResourcesOperationMetadata \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:04:57.028522+00:00
---

# BatchMigrateResourcesOperationMetadata  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesOperationMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  BatchMigrateResourcesOperationMetadata Stay organized with collections  Save and categorize content based on your preferences. 

Runtime operation information for `[MigrationService.BatchMigrateResources](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#google.cloud.aiplatform.v1beta1.MigrationService.BatchMigrateResources)`.

Fields  
  
`genericMetadata` `object (`[GenericOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenericOperationMetadata)`)` The common part of the operation metadata. | `partialResults[]` `object (`[PartialResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesOperationMetadata#PartialResult)`)` Partial results that reflect the latest migration operation progress. | JSON representation  
---  
      
    
    {
      "genericMetadata": {
        object ([GenericOperationMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/GenericOperationMetadata))
      },
      "partialResults": [
        {
          object ([PartialResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/BatchMigrateResourcesOperationMetadata#PartialResult))
        }
      ]
    }  
  
## PartialResult

Represents a partial result in batch migration operation for one `[MigrateResourceRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateResourceRequest)`.

Fields  
  
`request` `object (`[MigrateResourceRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateResourceRequest)`)` It's the same as the value in `[BatchMigrateResourcesRequest.migrate_resource_requests](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#body.request_body.FIELDS.migrate_resource_requests)`. | `result` `Union type`  
  
If the resource's migration is ongoing, none of the result will be set. If the resource's migration is finished, either error or one of the migrated resource name will be filled. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`error` `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` The error result of the migration request in case of failure. | `model` `string` Migrated model resource name. | `dataset` `string` Migrated dataset resource name. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "request": {
        object ([MigrateResourceRequest](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.migratableResources/batchMigrate#MigrateResourceRequest))
      },
    
      // result
      "error": {
        object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "model": string,
      "dataset": string
      // Union type
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
