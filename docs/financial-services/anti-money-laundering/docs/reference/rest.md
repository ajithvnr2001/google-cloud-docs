---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/
title: Financial Services API \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:08:46.427880+00:00
---

# Financial Services API  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Reference ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest)



Send feedback 

#  Financial Services API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.backtestResults
  * REST Resource: v1.projects.locations.instances.datasets
  * REST Resource: v1.projects.locations.instances.engineConfigs
  * REST Resource: v1.projects.locations.instances.engineVersions
  * REST Resource: v1.projects.locations.instances.models
  * REST Resource: v1.projects.locations.instances.predictionResults
  * REST Resource: v1.projects.locations.operations



## Service: financialservices.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://financialservices.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://financialservices.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates an instance.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes an instance.  
`[exportRegisteredParties](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/exportRegisteredParties)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:exportRegisteredParties`   
Exports the list of registered parties.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets an instance.  
`[importRegisteredParties](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:importRegisteredParties`   
Imports the list of registered parties.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists instances.  
`[patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the parameters of a single Instance.  
  
## REST Resource: [v1.projects.locations.instances.backtestResults](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults)

Methods  
---  
`[create](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/backtestResults`   
Create a BacktestResult.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/backtestResults/*}`   
Deletes a BacktestResult.  
`[exportMetadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/exportMetadata)` |  `POST /v1/{backtestResult=projects/*/locations/*/instances/*/backtestResults/*}:exportMetadata`   
Export governance information for a BacktestResult resource.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/backtestResults/*}`   
Gets a BacktestResult.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/backtestResults`   
List BacktestResults.  
`[patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/patch)` |  `PATCH /v1/{backtestResult.name=projects/*/locations/*/instances/*/backtestResults/*}`   
Updates the parameters of a single BacktestResult.  
  
## REST Resource: [v1.projects.locations.instances.datasets](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets)

Methods  
---  
`[create](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/datasets`   
Creates a dataset.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/datasets/*}`   
Deletes a dataset.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/datasets/*}`   
Gets a dataset.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/datasets`   
Lists datasets.  
`[patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets/patch)` |  `PATCH /v1/{dataset.name=projects/*/locations/*/instances/*/datasets/*}`   
Updates the parameters of a single Dataset.  
  
## REST Resource: [v1.projects.locations.instances.engineConfigs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/engineConfigs`   
Creates an engine config.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/engineConfigs/*}`   
Deletes an engine config.  
`[exportMetadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/exportMetadata)` |  `POST /v1/{engineConfig=projects/*/locations/*/instances/*/engineConfigs/*}:exportMetadata`   
Export governance information for an EngineConfig resource.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/engineConfigs/*}`   
Gets an engine config.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/engineConfigs`   
Lists engine configs.  
`[patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/patch)` |  `PATCH /v1/{engineConfig.name=projects/*/locations/*/instances/*/engineConfigs/*}`   
Updates the parameters of a single EngineConfig.  
  
## REST Resource: [v1.projects.locations.instances.engineVersions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineVersions)

Methods  
---  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineVersions/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/engineVersions/*}`   
Gets a single EngineVersion.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineVersions/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/engineVersions`   
Lists EngineVersions for given location.  
  
## REST Resource: [v1.projects.locations.instances.models](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models)

Methods  
---  
`[copy](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/copy)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/models:copy`   
Copies a model from one instance to another.  
`[create](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/models`   
Creates a model.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/models/*}`   
Deletes a model.  
`[exportMetadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/exportMetadata)` |  `POST /v1/{model=projects/*/locations/*/instances/*/models/*}:exportMetadata`   
Export governance information for a Model resource.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/models/*}`   
Gets a model.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/models`   
Lists models.  
`[patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/patch)` |  `PATCH /v1/{model.name=projects/*/locations/*/instances/*/models/*}`   
Updates the parameters of a single Model.  
  
## REST Resource: [v1.projects.locations.instances.predictionResults](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults)

Methods  
---  
`[create](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/predictionResults`   
Create a PredictionResult.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/predictionResults/*}`   
Deletes a PredictionResult.  
`[exportMetadata](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/exportMetadata)` |  `POST /v1/{predictionResult=projects/*/locations/*/instances/*/predictionResults/*}:exportMetadata`   
Export governance information for a PredictionResult resource.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/predictionResults/*}`   
Gets a PredictionResult.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/predictionResults`   
List PredictionResults.  
`[patch](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/patch)` |  `PATCH /v1/{predictionResult.name=projects/*/locations/*/instances/*/predictionResults/*}`   
Updates the parameters of a single PredictionResult.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-04 UTC."],[],[]] 
