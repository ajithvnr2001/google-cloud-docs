---
url: https://docs.cloud.google.com/food-ai/reference/rest/
title: Food Ordering AI Agent API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:13:00.765896+00:00
---

# Food Ordering AI Agent API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)



Send feedback 

#  Food Ordering AI Agent API Stay organized with collections  Save and categorize content based on your preferences. 

foodorderingaiagent.googleapis.com API.

  * REST Resource: v1beta.projects.locations.brands
  * REST Resource: v1beta.projects.locations.brands.channelConfigs
  * REST Resource: v1beta.projects.locations.brands.channelConfigs.revisions
  * REST Resource: v1beta.projects.locations.brands.configApplicationRules
  * REST Resource: v1beta.projects.locations.brands.configApplicationRules.revisions
  * REST Resource: v1beta.projects.locations.brands.evaluationCaseResults
  * REST Resource: v1beta.projects.locations.brands.evaluationCases
  * REST Resource: v1beta.projects.locations.brands.evaluationContexts
  * REST Resource: v1beta.projects.locations.brands.evaluationDatasetResults
  * REST Resource: v1beta.projects.locations.brands.evaluationDatasets
  * REST Resource: v1beta.projects.locations.brands.evaluationMatchers
  * REST Resource: v1beta.projects.locations.brands.ingestionLogs
  * REST Resource: v1beta.projects.locations.brands.revisions
  * REST Resource: v1beta.projects.locations.brands.sessionRecords
  * REST Resource: v1beta.projects.locations.brands.stores
  * REST Resource: v1beta.projects.locations.brands.stores.discounts
  * REST Resource: v1beta.projects.locations.brands.stores.inventories
  * REST Resource: v1beta.projects.locations.brands.stores.revisions
  * REST Resource: v1beta.projects.locations.menus
  * REST Resource: v1beta.projects.locations.menus.entities
  * REST Resource: v1beta.projects.locations.operations
  * REST Resource: v1beta.projects.locations.sessions
  * REST Resource: v1.projects.locations.brands
  * REST Resource: v1.projects.locations.brands.channelConfigs
  * REST Resource: v1.projects.locations.brands.channelConfigs.revisions
  * REST Resource: v1.projects.locations.brands.configApplicationRules
  * REST Resource: v1.projects.locations.brands.configApplicationRules.revisions
  * REST Resource: v1.projects.locations.brands.evaluationCaseResults
  * REST Resource: v1.projects.locations.brands.evaluationCases
  * REST Resource: v1.projects.locations.brands.evaluationContexts
  * REST Resource: v1.projects.locations.brands.evaluationDatasetResults
  * REST Resource: v1.projects.locations.brands.evaluationDatasets
  * REST Resource: v1.projects.locations.brands.evaluationMatchers
  * REST Resource: v1.projects.locations.brands.ingestionLogs
  * REST Resource: v1.projects.locations.brands.revisions
  * REST Resource: v1.projects.locations.brands.sessionRecords
  * REST Resource: v1.projects.locations.brands.stores
  * REST Resource: v1.projects.locations.brands.stores.discounts
  * REST Resource: v1.projects.locations.brands.stores.inventories
  * REST Resource: v1.projects.locations.brands.stores.revisions
  * REST Resource: v1.projects.locations.menus
  * REST Resource: v1.projects.locations.menus.entities
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.sessions



## Service: foodorderingaiagent.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://foodorderingaiagent.googleapis.com/$discovery/rest?version=v1>
  * <https://foodorderingaiagent.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://foodorderingaiagent.googleapis.com`



## REST Resource: [v1beta.projects.locations.brands](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands)

Methods  
---  
`[computeAnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/computeAnalyticsMetrics)` |  `GET /v1beta/{brand=projects/*/locations/*/brands/*}:computeAnalyticsMetrics`   
Computes analytics metrics for a given brand for specified time period with optional store filter.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/brands`   
Creates a brand.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*}`   
Deletes the specified brand.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*}`   
Gets a brand.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/brands`   
Lists brands.  
`[listHistory](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/listHistory)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}:listHistory`   
Lists history entries for a brand.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands/patch)` |  `PATCH /v1beta/{brand.name=projects/*/locations/*/brands/*}`   
Updates the specified brand.  
  
## REST Resource: [v1beta.projects.locations.brands.channelConfigs](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/channelConfigs`   
Creates a ChannelConfig.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/channelConfigs/*}`   
Deletes the specified ChannelConfig.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/channelConfigs/*}`   
Gets a ChannelConfig.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/channelConfigs`   
Lists ChannelConfigs.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/patch)` |  `PATCH /v1beta/{channelConfig.name=projects/*/locations/*/brands/*/channelConfigs/*}`   
Updates the specified ChannelConfig.  
`[promote](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs/promote)` |  `POST /v1beta/{name=projects/*/locations/*/brands/*/channelConfigs/*}:promote`   
Promotes the specified channel config.  
  
## REST Resource: [v1beta.projects.locations.brands.channelConfigs.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/channelConfigs/*/revisions/*}`   
Deletes the specified ChannelConfigRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/channelConfigs/*/revisions/*}`   
Gets a ChannelConfigRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.channelConfigs.revisions/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*/channelConfigs/*}/revisions`   
Lists ChannelConfigRevisions.  
  
## REST Resource: [v1beta.projects.locations.brands.configApplicationRules](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/configApplicationRules`   
Creates a ConfigApplicationRule.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/configApplicationRules/*}`   
Deletes the specified ConfigApplicationRule.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/configApplicationRules/*}`   
Gets a ConfigApplicationRule.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/configApplicationRules`   
Lists ConfigApplicationRules.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules/patch)` |  `PATCH /v1beta/{configApplicationRule.name=projects/*/locations/*/brands/*/configApplicationRules/*}`   
Updates the specified ConfigApplicationRule.  
  
## REST Resource: [v1beta.projects.locations.brands.configApplicationRules.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules.revisions/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/configApplicationRules/*/revisions/*}`   
Deletes the specified ConfigApplicationRuleRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules.revisions/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/configApplicationRules/*/revisions/*}`   
Gets a ConfigApplicationRuleRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.configApplicationRules.revisions/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*/configApplicationRules/*}/revisions`   
Lists ConfigApplicationRuleRevisions.  
  
## REST Resource: [v1beta.projects.locations.brands.evaluationCaseResults](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/evaluationCaseResults/*}`   
Deletes the specified EvaluationCaseResult.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/evaluationCaseResults/*}`   
Gets an EvaluationCaseResult.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCaseResults/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCaseResults`   
Lists EvaluationCaseResults.  
  
## REST Resource: [v1beta.projects.locations.brands.evaluationCases](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchCreate)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCases:batchCreate`   
Batch creates EvaluationCases.  
`[batchUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/batchUpdate)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCases:batchUpdate`   
Batch updates EvaluationCases.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCases`   
Creates an EvaluationCase.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/evaluationCases/*}`   
Deletes the specified EvaluationCase.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/evaluationCases/*}`   
Gets an EvaluationCase.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationCases`   
Lists EvaluationCases.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/patch)` |  `PATCH /v1beta/{evaluationCase.name=projects/*/locations/*/brands/*/evaluationCases/*}`   
Updates the specified EvaluationCase.  
`[run](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationCases/run)` |  `POST /v1beta/{name=projects/*/locations/*/brands/*/evaluationCases/*}:run`   
Runs an evaluation case.  
  
## REST Resource: [v1beta.projects.locations.brands.evaluationContexts](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationContexts`   
Creates an EvaluationContext.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/evaluationContexts/*}`   
Deletes the specified EvaluationContext.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/evaluationContexts/*}`   
Gets an EvaluationContext.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationContexts`   
Lists EvaluationContexts.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationContexts/patch)` |  `PATCH /v1beta/{evaluationContext.name=projects/*/locations/*/brands/*/evaluationContexts/*}`   
Updates the specified EvaluationContext.  
  
## REST Resource: [v1beta.projects.locations.brands.evaluationDatasetResults](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/evaluationDatasetResults/*}`   
Deletes the specified EvaluationDatasetResult.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/evaluationDatasetResults/*}`   
Gets an EvaluationDatasetResult.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasetResults/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationDatasetResults`   
Lists EvaluationDatasetResults.  
  
## REST Resource: [v1beta.projects.locations.brands.evaluationDatasets](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationDatasets`   
Creates an EvaluationDataset.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/evaluationDatasets/*}`   
Deletes the specified EvaluationDataset.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/evaluationDatasets/*}`   
Gets an EvaluationDataset.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationDatasets`   
Lists EvaluationDatasets.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/patch)` |  `PATCH /v1beta/{evaluationDataset.name=projects/*/locations/*/brands/*/evaluationDatasets/*}`   
Updates the specified EvaluationDataset.  
`[run](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationDatasets/run)` |  `POST /v1beta/{name=projects/*/locations/*/brands/*/evaluationDatasets/*}:run`   
Runs an evaluation dataset.  
  
## REST Resource: [v1beta.projects.locations.brands.evaluationMatchers](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationMatchers`   
Creates an EvaluationMatcher.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/evaluationMatchers/*}`   
Deletes the specified EvaluationMatcher.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/evaluationMatchers/*}`   
Gets an EvaluationMatcher.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/evaluationMatchers`   
Lists EvaluationMatchers.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.evaluationMatchers/patch)` |  `PATCH /v1beta/{evaluationMatcher.name=projects/*/locations/*/brands/*/evaluationMatchers/*}`   
Updates the specified EvaluationMatcher.  
  
## REST Resource: [v1beta.projects.locations.brands.ingestionLogs](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs)

Methods  
---  
`[appendIngestionPhase](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/appendIngestionPhase)` |  `POST /v1beta/{name=projects/*/locations/*/brands/*/ingestionLogs/*}:appendIngestionPhase`   
Appends an ingestion phase to an ingestion log.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/ingestionLogs`   
Creates an ingestion log.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/ingestionLogs/*}`   
Deletes the specified ingestion log.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/ingestionLogs/*}`   
Gets an ingestion log.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.ingestionLogs/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/ingestionLogs`   
Lists ingestion logs.  
  
## REST Resource: [v1beta.projects.locations.brands.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.revisions/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/revisions/*}`   
Deletes the specified BrandRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.revisions/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/revisions/*}`   
Gets a BrandRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.revisions/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/revisions`   
Lists BrandRevisions.  
  
## REST Resource: [v1beta.projects.locations.brands.sessionRecords](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.sessionRecords)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.sessionRecords/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/sessionRecords/*}`   
Deletes an SessionRecord.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.sessionRecords/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/sessionRecords/*}`   
Gets a specific SessionRecord.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.sessionRecords/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/sessionRecords`   
Lists SessionRecords for a given brand.  
  
## REST Resource: [v1beta.projects.locations.brands.stores](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/batchDelete)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/stores:batchDelete`   
Batch deletes stores.  
`[batchUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/batchUpdate)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/stores:batchUpdate`   
Batch updates stores.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*}/stores`   
Creates a store.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/stores/*}`   
Deletes the specified store.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/stores/*}`   
Gets a store.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*}/stores`   
Lists stores.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores/patch)` |  `PATCH /v1beta/{store.name=projects/*/locations/*/brands/*/stores/*}`   
Update the specified store.  
  
## REST Resource: [v1beta.projects.locations.brands.stores.discounts](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*/stores/*}/discounts`   
Creates a discount.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/stores/*/discounts/*}`   
Deletes the specified discount.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/stores/*/discounts/*}`   
Gets a discount.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*/stores/*}/discounts`   
Lists discounts.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.discounts/patch)` |  `PATCH /v1beta/{discount.name=projects/*/locations/*/brands/*/stores/*/discounts/*}`   
Updates the specified discount.  
  
## REST Resource: [v1beta.projects.locations.brands.stores.inventories](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/create)` |  `POST /v1beta/{parent=projects/*/locations/*/brands/*/stores/*}/inventories`   
Creates an inventory.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/stores/*/inventories/*}`   
Deletes the specified inventory.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/stores/*/inventories/*}`   
Gets an inventory.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*/stores/*}/inventories`   
Lists inventories.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.inventories/patch)` |  `PATCH /v1beta/{inventory.name=projects/*/locations/*/brands/*/stores/*/inventories/*}`   
Updates the specified inventory.  
  
## REST Resource: [v1beta.projects.locations.brands.stores.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.revisions/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/brands/*/stores/*/revisions/*}`   
Deletes the specified StoreRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.revisions/get)` |  `GET /v1beta/{name=projects/*/locations/*/brands/*/stores/*/revisions/*}`   
Gets a StoreRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.brands.stores.revisions/list)` |  `GET /v1beta/{parent=projects/*/locations/*/brands/*/stores/*}/revisions`   
Lists StoreRevisions.  
  
## REST Resource: [v1beta.projects.locations.menus](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/menus`   
Creates a menu.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/menus/*}`   
Deletes the specified menu.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/get)` |  `GET /v1beta/{name=projects/*/locations/*/menus/*}`   
Gets a menu.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/menus`   
Lists menus.  
  
## REST Resource: [v1beta.projects.locations.menus.entities](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus.entities)

Methods  
---  
`[batchGet](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.menus.entities/batchGet)` |  `GET /v1beta/{parent=projects/*/locations/*/menus/*}/entities:batchGet`   
Batch gets entities for a menu.  
  
## REST Resource: [v1beta.projects.locations.operations](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.operations/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.operations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.operations/list)` |  `GET /v1beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.projects.locations.sessions](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.sessions)

Methods  
---  
`[processOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1beta/projects.locations.sessions/processOrder)` |  `POST /v1beta/{config.session=projects/*/locations/*/sessions/*}:processOrder`   
Performs a single turn logic to process user input and return the result.  
  
## REST Resource: [v1.projects.locations.brands](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands)

Methods  
---  
`[computeAnalyticsMetrics](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/computeAnalyticsMetrics)` |  `GET /v1/{brand=projects/*/locations/*/brands/*}:computeAnalyticsMetrics`   
Computes analytics metrics for a given brand for specified time period with optional store filter.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/create)` |  `POST /v1/{parent=projects/*/locations/*}/brands`   
Creates a brand.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*}`   
Deletes the specified brand.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*}`   
Gets a brand.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/list)` |  `GET /v1/{parent=projects/*/locations/*}/brands`   
Lists brands.  
`[listHistory](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/listHistory)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}:listHistory`   
Lists history entries for a brand.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands/patch)` |  `PATCH /v1/{brand.name=projects/*/locations/*/brands/*}`   
Updates the specified brand.  
  
## REST Resource: [v1.projects.locations.brands.channelConfigs](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/channelConfigs`   
Creates a ChannelConfig.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/channelConfigs/*}`   
Deletes the specified ChannelConfig.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/channelConfigs/*}`   
Gets a ChannelConfig.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/channelConfigs`   
Lists ChannelConfigs.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs/patch)` |  `PATCH /v1/{channelConfig.name=projects/*/locations/*/brands/*/channelConfigs/*}`   
Updates the specified ChannelConfig.  
`[promote](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs/promote)` |  `POST /v1/{name=projects/*/locations/*/brands/*/channelConfigs/*}:promote`   
Promotes the specified channel config.  
  
## REST Resource: [v1.projects.locations.brands.channelConfigs.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/channelConfigs/*/revisions/*}`   
Deletes the specified ChannelConfigRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/channelConfigs/*/revisions/*}`   
Gets a ChannelConfigRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.channelConfigs.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*/channelConfigs/*}/revisions`   
Lists ChannelConfigRevisions.  
  
## REST Resource: [v1.projects.locations.brands.configApplicationRules](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/configApplicationRules`   
Creates a ConfigApplicationRule.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/configApplicationRules/*}`   
Deletes the specified ConfigApplicationRule.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/configApplicationRules/*}`   
Gets a ConfigApplicationRule.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/configApplicationRules`   
Lists ConfigApplicationRules.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules/patch)` |  `PATCH /v1/{configApplicationRule.name=projects/*/locations/*/brands/*/configApplicationRules/*}`   
Updates the specified ConfigApplicationRule.  
  
## REST Resource: [v1.projects.locations.brands.configApplicationRules.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/configApplicationRules/*/revisions/*}`   
Deletes the specified ConfigApplicationRuleRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/configApplicationRules/*/revisions/*}`   
Gets a ConfigApplicationRuleRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.configApplicationRules.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*/configApplicationRules/*}/revisions`   
Lists ConfigApplicationRuleRevisions.  
  
## REST Resource: [v1.projects.locations.brands.evaluationCaseResults](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/evaluationCaseResults/*}`   
Deletes the specified EvaluationCaseResult.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/evaluationCaseResults/*}`   
Gets an EvaluationCaseResult.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCaseResults/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/evaluationCaseResults`   
Lists EvaluationCaseResults.  
  
## REST Resource: [v1.projects.locations.brands.evaluationCases](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases)

Methods  
---  
`[batchCreate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchCreate)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/evaluationCases:batchCreate`   
Batch creates EvaluationCases.  
`[batchUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/batchUpdate)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/evaluationCases:batchUpdate`   
Batch updates EvaluationCases.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/evaluationCases`   
Creates an EvaluationCase.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/evaluationCases/*}`   
Deletes the specified EvaluationCase.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/evaluationCases/*}`   
Gets an EvaluationCase.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/evaluationCases`   
Lists EvaluationCases.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/patch)` |  `PATCH /v1/{evaluationCase.name=projects/*/locations/*/brands/*/evaluationCases/*}`   
Updates the specified EvaluationCase.  
`[run](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationCases/run)` |  `POST /v1/{name=projects/*/locations/*/brands/*/evaluationCases/*}:run`   
Runs an evaluation case.  
  
## REST Resource: [v1.projects.locations.brands.evaluationContexts](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationContexts)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationContexts/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/evaluationContexts`   
Creates an EvaluationContext.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationContexts/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/evaluationContexts/*}`   
Deletes the specified EvaluationContext.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationContexts/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/evaluationContexts/*}`   
Gets an EvaluationContext.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationContexts/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/evaluationContexts`   
Lists EvaluationContexts.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationContexts/patch)` |  `PATCH /v1/{evaluationContext.name=projects/*/locations/*/brands/*/evaluationContexts/*}`   
Updates the specified EvaluationContext.  
  
## REST Resource: [v1.projects.locations.brands.evaluationDatasetResults](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasetResults)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasetResults/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/evaluationDatasetResults/*}`   
Deletes the specified EvaluationDatasetResult.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasetResults/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/evaluationDatasetResults/*}`   
Gets an EvaluationDatasetResult.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasetResults/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/evaluationDatasetResults`   
Lists EvaluationDatasetResults.  
  
## REST Resource: [v1.projects.locations.brands.evaluationDatasets](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/evaluationDatasets`   
Creates an EvaluationDataset.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/evaluationDatasets/*}`   
Deletes the specified EvaluationDataset.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/evaluationDatasets/*}`   
Gets an EvaluationDataset.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/evaluationDatasets`   
Lists EvaluationDatasets.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets/patch)` |  `PATCH /v1/{evaluationDataset.name=projects/*/locations/*/brands/*/evaluationDatasets/*}`   
Updates the specified EvaluationDataset.  
`[run](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationDatasets/run)` |  `POST /v1/{name=projects/*/locations/*/brands/*/evaluationDatasets/*}:run`   
Runs an evaluation dataset.  
  
## REST Resource: [v1.projects.locations.brands.evaluationMatchers](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationMatchers)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationMatchers/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/evaluationMatchers`   
Creates an EvaluationMatcher.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationMatchers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/evaluationMatchers/*}`   
Deletes the specified EvaluationMatcher.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationMatchers/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/evaluationMatchers/*}`   
Gets an EvaluationMatcher.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationMatchers/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/evaluationMatchers`   
Lists EvaluationMatchers.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.evaluationMatchers/patch)` |  `PATCH /v1/{evaluationMatcher.name=projects/*/locations/*/brands/*/evaluationMatchers/*}`   
Updates the specified EvaluationMatcher.  
  
## REST Resource: [v1.projects.locations.brands.ingestionLogs](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.ingestionLogs)

Methods  
---  
`[appendIngestionPhase](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.ingestionLogs/appendIngestionPhase)` |  `POST /v1/{name=projects/*/locations/*/brands/*/ingestionLogs/*}:appendIngestionPhase`   
Appends an ingestion phase to an ingestion log.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.ingestionLogs/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/ingestionLogs`   
Creates an ingestion log.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.ingestionLogs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/ingestionLogs/*}`   
Deletes the specified ingestion log.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.ingestionLogs/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/ingestionLogs/*}`   
Gets an ingestion log.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.ingestionLogs/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/ingestionLogs`   
Lists ingestion logs.  
  
## REST Resource: [v1.projects.locations.brands.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/revisions/*}`   
Deletes the specified BrandRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/revisions/*}`   
Gets a BrandRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/revisions`   
Lists BrandRevisions.  
  
## REST Resource: [v1.projects.locations.brands.sessionRecords](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/sessionRecords/*}`   
Deletes an SessionRecord.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/sessionRecords/*}`   
Gets a specific SessionRecord.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/sessionRecords`   
Lists SessionRecords for a given brand.  
  
## REST Resource: [v1.projects.locations.brands.stores](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores)

Methods  
---  
`[batchDelete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchDelete)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/stores:batchDelete`   
Batch deletes stores.  
`[batchUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/batchUpdate)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/stores:batchUpdate`   
Batch updates stores.  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*}/stores`   
Creates a store.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/stores/*}`   
Deletes the specified store.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/stores/*}`   
Gets a store.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*}/stores`   
Lists stores.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores/patch)` |  `PATCH /v1/{store.name=projects/*/locations/*/brands/*/stores/*}`   
Update the specified store.  
  
## REST Resource: [v1.projects.locations.brands.stores.discounts](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*/stores/*}/discounts`   
Creates a discount.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/stores/*/discounts/*}`   
Deletes the specified discount.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/stores/*/discounts/*}`   
Gets a discount.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*/stores/*}/discounts`   
Lists discounts.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.discounts/patch)` |  `PATCH /v1/{discount.name=projects/*/locations/*/brands/*/stores/*/discounts/*}`   
Updates the specified discount.  
  
## REST Resource: [v1.projects.locations.brands.stores.inventories](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/create)` |  `POST /v1/{parent=projects/*/locations/*/brands/*/stores/*}/inventories`   
Creates an inventory.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/stores/*/inventories/*}`   
Deletes the specified inventory.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/stores/*/inventories/*}`   
Gets an inventory.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*/stores/*}/inventories`   
Lists inventories.  
`[patch](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.inventories/patch)` |  `PATCH /v1/{inventory.name=projects/*/locations/*/brands/*/stores/*/inventories/*}`   
Updates the specified inventory.  
  
## REST Resource: [v1.projects.locations.brands.stores.revisions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/brands/*/stores/*/revisions/*}`   
Deletes the specified StoreRevision.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/brands/*/stores/*/revisions/*}`   
Gets a StoreRevision.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.stores.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/brands/*/stores/*}/revisions`   
Lists StoreRevisions.  
  
## REST Resource: [v1.projects.locations.menus](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus)

Methods  
---  
`[create](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus/create)` |  `POST /v1/{parent=projects/*/locations/*}/menus`   
Creates a menu.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus/delete)` |  `DELETE /v1/{name=projects/*/locations/*/menus/*}`   
Deletes the specified menu.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus/get)` |  `GET /v1/{name=projects/*/locations/*/menus/*}`   
Gets a menu.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus/list)` |  `GET /v1/{parent=projects/*/locations/*}/menus`   
Lists menus.  
  
## REST Resource: [v1.projects.locations.menus.entities](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus.entities)

Methods  
---  
`[batchGet](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.menus.entities/batchGet)` |  `GET /v1/{parent=projects/*/locations/*/menus/*}/entities:batchGet`   
Batch gets entities for a menu.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.sessions](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions)

Methods  
---  
`[processOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.sessions/processOrder)` |  `POST /v1/{config.session=projects/*/locations/*/sessions/*}:processOrder`   
Performs a single turn logic to process user input and return the result.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
