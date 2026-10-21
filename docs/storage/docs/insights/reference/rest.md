---
url: https://docs.cloud.google.com/storage/docs/insights/reference/rest/
title: Storage Insights API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:36.317975+00:00
---

# Storage Insights API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Storage Insights API Stay organized with collections  Save and categorize content based on your preferences. 

Provides insights capability on Google Cloud Storage

## Service: storageinsights.googleapis.com

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://storageinsights.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.datasetConfigs](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*}/datasetConfigs`   
Creates a dataset configuration in a given project for a given location.  
`[delete](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/datasetConfigs/*}`   
Deletes a dataset configuration in a given project for a given location.  
`[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/datasetConfigs/*}`   
Gets the dataset configuration in a given project for a given location.  
`[linkDataset](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/linkDataset)` |  `POST /v1/{name=projects/*/locations/*/datasetConfigs/*}:linkDataset`   
Links a dataset to BigQuery in a given project for a given location.  
`[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*}/datasetConfigs`   
Lists the dataset configurations in a given project for a given location.  
`[patch](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/patch)` |  `PATCH /v1/{datasetConfig.name=projects/*/locations/*/datasetConfigs/*}`   
Updates a dataset configuration in a given project for a given location.  
`[unlinkDataset](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.datasetConfigs/unlinkDataset)` |  `POST /v1/{name=projects/*/locations/*/datasetConfigs/*}:unlinkDataset`   
Unlinks a dataset from BigQuery in a given project for a given location.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.reportConfigs](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*}/reportConfigs`   
Creates a new inventory report configuration in a given project for a given location.  
`[delete](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/reportConfigs/*}`   
Deletes an existing inventory report configuration in a given project for a given location.  
`[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/reportConfigs/*}`   
Gets the inventory report configuration in a given project for a given location.  
`[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*}/reportConfigs`   
Lists the inventory report configurations in a given project for a given location.  
`[patch](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/patch)` |  `PATCH /v1/{reportConfig.name=projects/*/locations/*/reportConfigs/*}`   
Updates an existing inventory report configuration in a given project for a given location.  
  
## REST Resource: [v1.projects.locations.reportConfigs.reportDetails](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails)

Methods  
---  
`[get](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails/get)` |  `GET /v1/{name=projects/*/locations/*/reportConfigs/*/reportDetails/*}`   
Gets an existing inventory report in a given project for a given location.  
`[list](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs.reportDetails/list)` |  `GET /v1/{parent=projects/*/locations/*/reportConfigs/*}/reportDetails`   
Lists the inventory reports in a given project for a given location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
