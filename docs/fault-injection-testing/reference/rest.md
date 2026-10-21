---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/
title: Fault Testing API \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:41.296396+00:00
---

# Fault Testing API  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Fault Testing API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.exclusionWindows
  * REST Resource: v1alpha.projects.locations.experimentTemplates
  * REST Resource: v1alpha.projects.locations.experiments
  * REST Resource: v1alpha.projects.locations.experiments.affectedResources
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.validations
  * REST Resource: v1alpha.projects.locations.validations.validationResources



## Service: faulttesting.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://faulttesting.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://faulttesting.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.exclusionWindows](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows)

Methods  
---  
`[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/exclusionWindows`   
Creates a new exclusion window.  
`[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/exclusionWindows/*}`   
Deletes an exclusion window.  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/get)` |  `GET /v1alpha/{name=projects/*/locations/*/exclusionWindows/*}`   
Get the details of an exclusion window.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/exclusionWindows`   
Lists all exclusion windows in a project and region, or all exclusion windows in a project in all regions if the location is given as "-".  
`[patch](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/patch)` |  `PATCH /v1alpha/{exclusionWindow.name=projects/*/locations/*/exclusionWindows/*}`   
Updates an exclusion window.  
`[start](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/start)` |  `POST /v1alpha/{name=projects/*/locations/*/exclusionWindows/*}:start`   
Starts or restarts an existing exclusion window.  
`[stop](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/stop)` |  `POST /v1alpha/{name=projects/*/locations/*/exclusionWindows/*}:stop`   
Stops an active exclusion window.  
  
## REST Resource: [v1alpha.projects.locations.experimentTemplates](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates)

Methods  
---  
`[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/experimentTemplates`   
Creates a new experiment template.  
`[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/experimentTemplates/*}`   
Deletes an experiment template.  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/get)` |  `GET /v1alpha/{name=projects/*/locations/*/experimentTemplates/*}`   
Retrieves the details of a specific experiment template.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/experimentTemplates`   
Lists all experiment templates in a specified project and location.  
`[patch](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experimentTemplates/patch)` |  `PATCH /v1alpha/{experimentTemplate.name=projects/*/locations/*/experimentTemplates/*}`   
Updates an existing experiment template.  
  
## REST Resource: [v1alpha.projects.locations.experiments](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments)

Methods  
---  
`[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/experiments`   
Creates an `Experiment` and prepares it to run by identifying all cloud resources that will be affected.  
`[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/experiments/*}`   
Deletes an `Experiment` record.  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/get)` |  `GET /v1alpha/{name=projects/*/locations/*/experiments/*}`   
Returns a single `Experiment` resource, including its current state and configuration.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/experiments`   
Lists all experiments in a specified project and location.  
`[start](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/start)` |  `POST /v1alpha/{name=projects/*/locations/*/experiments/*}:start`   
Starts an existing `Experiment`.  
`[stop](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stop)` |  `POST /v1alpha/{name=projects/*/locations/*/experiments/*}:stop`   
Stops a running `Experiment`.  
`[stopAll](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments/stopAll)` |  `POST /v1alpha/{parent=projects/*/locations/*}/experiments:stopAll`   
Stops all running experiments in a given location for a given project.  
  
## REST Resource: [v1alpha.projects.locations.experiments.affectedResources](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources)

Methods  
---  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources/get)` |  `GET /v1alpha/{name=projects/*/locations/*/experiments/*/affectedResources/*}`   
Gets the details of a specific cloud resource that is being or was affected by a particular `Experiment`.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.experiments.affectedResources/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/experiments/*}/affectedResources`   
Lists all cloud resources that are being or were affected by a specific `Experiment`.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.validations](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations)

Methods  
---  
`[create](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/validations`   
Creates a new `Validation` dry run.  
`[delete](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/validations/*}`   
Deletes a record of a dry run.  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/validations/*}`   
Retrieves the details of a specific `Validation` dry run.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/validations`   
Lists all dry runs in a specified project and location.  
  
## REST Resource: [v1alpha.projects.locations.validations.validationResources](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources)

Methods  
---  
`[get](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources/get)` |  `GET /v1alpha/{name=projects/*/locations/*/validations/*/validationResources/*}`   
Gets the details of a specific `ValidationResource`.  
`[list](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.validations.validationResources/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/validations/*}/validationResources`   
Lists all cloud resources identified as potentially affected within a specific `Validation` dry run.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
