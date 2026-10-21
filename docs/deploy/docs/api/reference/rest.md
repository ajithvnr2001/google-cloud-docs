---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/
title: Cloud Deploy API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:49.583845+00:00
---

# Cloud Deploy API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  Cloud Deploy API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.customTargetTypes
  * REST Resource: v1.projects.locations.deliveryPipelines
  * REST Resource: v1.projects.locations.deliveryPipelines.automationRuns
  * REST Resource: v1.projects.locations.deliveryPipelines.automations
  * REST Resource: v1.projects.locations.deliveryPipelines.releases
  * REST Resource: v1.projects.locations.deliveryPipelines.releases.rollouts
  * REST Resource: v1.projects.locations.deliveryPipelines.releases.rollouts.jobRuns
  * REST Resource: v1.projects.locations.deployPolicies
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.targets



## Service: clouddeploy.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://clouddeploy.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://clouddeploy.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global asia-south1 asia-south2 us-central1 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4

  

* `https://clouddeploy.googleapis.com`

## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getConfig](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/getConfig)` |  `GET /v1/{name=projects/*/locations/*/config}`   
Gets the configuration for a location.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.customTargetTypes](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/create)` |  `POST /v1/{parent=projects/*/locations/*}/customTargetTypes`   
Creates a new CustomTargetType in a given project and location.  
`[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/customTargetTypes/*}`   
Deletes a single CustomTargetType.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/get)` |  `GET /v1/{name=projects/*/locations/*/customTargetTypes/*}`   
Gets details of a single CustomTargetType.  
`[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/customTargetTypes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/list)` |  `GET /v1/{parent=projects/*/locations/*}/customTargetTypes`   
Lists CustomTargetTypes in a given project and location.  
`[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/patch)` |  `PATCH /v1/{customTargetType.name=projects/*/locations/*/customTargetTypes/*}`   
Updates a single CustomTargetType.  
`[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.customTargetTypes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/customTargetTypes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
  
## REST Resource: [v1.projects.locations.deliveryPipelines](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines)

Methods  
---  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/create)` |  `POST /v1/{parent=projects/*/locations/*}/deliveryPipelines`   
Creates a new DeliveryPipeline in a given project and location.  
`[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/delete)` |  `DELETE /v1/{name=projects/*/locations/*/deliveryPipelines/*}`   
Deletes a single DeliveryPipeline.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/get)` |  `GET /v1/{name=projects/*/locations/*/deliveryPipelines/*}`   
Gets details of a single DeliveryPipeline.  
`[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/deliveryPipelines/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/list)` |  `GET /v1/{parent=projects/*/locations/*}/deliveryPipelines`   
Lists DeliveryPipelines in a given project and location.  
`[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/patch)` |  `PATCH /v1/{deliveryPipeline.name=projects/*/locations/*/deliveryPipelines/*}`   
Updates the parameters of a single DeliveryPipeline.  
`[rollbackTarget](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/rollbackTarget)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*}:rollbackTarget`   
Creates a `Rollout` to roll back the specified target.  
`[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/deliveryPipelines/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/deliveryPipelines/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.deliveryPipelines.automationRuns](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns)

Methods  
---  
`[cancel](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns/cancel)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*/automationRuns/*}:cancel`   
Cancels an AutomationRun.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns/get)` |  `GET /v1/{name=projects/*/locations/*/deliveryPipelines/*/automationRuns/*}`   
Gets details of a single AutomationRun.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns/list)` |  `GET /v1/{parent=projects/*/locations/*/deliveryPipelines/*}/automationRuns`   
Lists AutomationRuns in a given project and location.  
  
## REST Resource: [v1.projects.locations.deliveryPipelines.automations](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations)

Methods  
---  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/create)` |  `POST /v1/{parent=projects/*/locations/*/deliveryPipelines/*}/automations`   
Creates a new Automation in a given project and location.  
`[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/deliveryPipelines/*/automations/*}`   
Deletes a single Automation resource.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/get)` |  `GET /v1/{name=projects/*/locations/*/deliveryPipelines/*/automations/*}`   
Gets details of a single Automation.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/list)` |  `GET /v1/{parent=projects/*/locations/*/deliveryPipelines/*}/automations`   
Lists Automations in a given project and location.  
`[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations/patch)` |  `PATCH /v1/{automation.name=projects/*/locations/*/deliveryPipelines/*/automations/*}`   
Updates the parameters of a single Automation resource.  
  
## REST Resource: [v1.projects.locations.deliveryPipelines.releases](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases)

Methods  
---  
`[abandon](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/abandon)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*}:abandon`   
Abandons a Release in the Delivery Pipeline.  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/create)` |  `POST /v1/{parent=projects/*/locations/*/deliveryPipelines/*}/releases`   
Creates a new Release in a given project and location.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/get)` |  `GET /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*}`   
Gets details of a single Release.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases/list)` |  `GET /v1/{parent=projects/*/locations/*/deliveryPipelines/*}/releases`   
Lists Releases in a given project and location.  
  
## REST Resource: [v1.projects.locations.deliveryPipelines.releases.rollouts](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts)

Methods  
---  
`[advance](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/advance)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}:advance`   
Advances a Rollout in a given project and location.  
`[approve](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/approve)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}:approve`   
Approves a Rollout.  
`[cancel](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/cancel)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}:cancel`   
Cancels a Rollout in a given project and location.  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/create)` |  `POST /v1/{parent=projects/*/locations/*/deliveryPipelines/*/releases/*}/rollouts`   
Creates a new Rollout in a given project and location.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/get)` |  `GET /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}`   
Gets details of a single Rollout.  
`[ignoreJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/ignoreJob)` |  `POST /v1/{rollout=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}:ignoreJob`   
Ignores the specified Job in a Rollout.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/list)` |  `GET /v1/{parent=projects/*/locations/*/deliveryPipelines/*/releases/*}/rollouts`   
Lists Rollouts in a given project and location.  
`[retryJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/retryJob)` |  `POST /v1/{rollout=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}:retryJob`   
Retries the specified Job in a Rollout.  
  
## REST Resource: [v1.projects.locations.deliveryPipelines.releases.rollouts.jobRuns](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns)

Methods  
---  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns/get)` |  `GET /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*/jobRuns/*}`   
Gets details of a single JobRun.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns/list)` |  `GET /v1/{parent=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*}/jobRuns`   
Lists JobRuns in a given project and location.  
`[terminate](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns/terminate)` |  `POST /v1/{name=projects/*/locations/*/deliveryPipelines/*/releases/*/rollouts/*/jobRuns/*}:terminate`   
Terminates a Job Run in a given project and location.  
  
## REST Resource: [v1.projects.locations.deployPolicies](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/deployPolicies`   
Creates a new DeployPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/deployPolicies/*}`   
Deletes a single DeployPolicy.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/deployPolicies/*}`   
Gets details of a single DeployPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/deployPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/deployPolicies`   
Lists DeployPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/patch)` |  `PATCH /v1/{deployPolicy.name=projects/*/locations/*/deployPolicies/*}`   
Updates the parameters of a single DeployPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deployPolicies/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/deployPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.targets](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets)

Methods  
---  
`[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/create)` |  `POST /v1/{parent=projects/*/locations/*}/targets`   
Creates a new Target in a given project and location.  
`[delete](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/targets/*}`   
Deletes a single Target.  
`[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/get)` |  `GET /v1/{name=projects/*/locations/*/targets/*}`   
Gets details of a single Target.  
`[getIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/targets/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/list)` |  `GET /v1/{parent=projects/*/locations/*}/targets`   
Lists Targets in a given project and location.  
`[patch](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/patch)` |  `PATCH /v1/{target.name=projects/*/locations/*/targets/*}`   
Updates the parameters of a single Target.  
`[setIamPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/targets/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.targets/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/targets/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
