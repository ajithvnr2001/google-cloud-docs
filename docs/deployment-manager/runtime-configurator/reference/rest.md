---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/
title: Cloud Runtime Configuration API \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:32.792212+00:00
---

# Cloud Runtime Configuration API  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Cloud Runtime Configuration API Stay organized with collections  Save and categorize content based on your preferences. 

The Runtime Configurator allows you to dynamically configure and expose variables through Google Cloud Platform. In addition, you can also set Watchers and Waiters that will watch for changes to your data and return based on certain conditions.

  * REST Resource: v1beta1.projects.configs
  * REST Resource: v1beta1.projects.configs.operations
  * REST Resource: v1beta1.projects.configs.variables
  * REST Resource: v1beta1.projects.configs.waiters
  * REST Resource: v1.operations



## Service: runtimeconfig.googleapis.com

All URIs below are relative to `https://runtimeconfig.googleapis.com`

This service provides the following [discovery documents](https://developers.google.com/discovery/v1/reference/apis):

  * <https://runtimeconfig.googleapis.com/$discovery/rest?version=v1>
  * <https://runtimeconfig.googleapis.com/$discovery/rest?version=v1beta1>



## REST Resource: [v1beta1.projects.configs](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs)

Methods  
---  
`[create](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/create)` |  `POST /v1beta1/{parent=projects/*}/configs`   
Creates a new RuntimeConfig resource.  
`[delete](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/delete)` |  `DELETE /v1beta1/{name=projects/*/configs/*}`   
Deletes a RuntimeConfig resource.  
`[get](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/get)` |  `GET /v1beta1/{name=projects/*/configs/*}`   
Gets information about a RuntimeConfig resource.  
`[getIamPolicy](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/configs/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/list)` |  `GET /v1beta1/{parent=projects/*}/configs`   
Lists all the RuntimeConfig resources within project.  
`[setIamPolicy](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/configs/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/configs/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[update](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/update)` |  `PUT /v1beta1/{name=projects/*/configs/*}`   
Updates a RuntimeConfig resource.  
  
## REST Resource: [v1beta1.projects.configs.operations](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.operations/get)` |  `GET /v1beta1/{name=projects/*/configs/*/operations/**}`   
Gets the latest state of a long-running operation.  
`[testIamPermissions](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.operations/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/configs/*/operations/**}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.configs.variables](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables)

Methods  
---  
`[create](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/create)` |  `POST /v1beta1/{parent=projects/*/configs/*}/variables`   
Creates a variable within the given configuration.  
`[delete](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/delete)` |  `DELETE /v1beta1/{name=projects/*/configs/*/variables/**}`   
Deletes a variable or multiple variables.  
`[get](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/get)` |  `GET /v1beta1/{name=projects/*/configs/*/variables/**}`   
Gets information about a single variable.  
`[list](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list)` |  `GET /v1beta1/{parent=projects/*/configs/*}/variables`   
Lists variables within given a configuration, matching any provided filters.  
`[testIamPermissions](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/configs/*/variables/**}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[update](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/update)` |  `PUT /v1beta1/{name=projects/*/configs/*/variables/**}`   
Updates an existing variable with a new value.  
`[watch](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/watch)` |  `POST /v1beta1/{name=projects/*/configs/*/variables/**}:watch`   
Watches a specific variable and waits for a change in the variable's value.  
  
## REST Resource: [v1beta1.projects.configs.waiters](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters)

Methods  
---  
`[create](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/create)` |  `POST /v1beta1/{parent=projects/*/configs/*}/waiters`   
Creates a Waiter resource.  
`[delete](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/delete)` |  `DELETE /v1beta1/{name=projects/*/configs/*/waiters/*}`   
Deletes the waiter with the specified name.  
`[get](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/get)` |  `GET /v1beta1/{name=projects/*/configs/*/waiters/*}`   
Gets information about a single waiter.  
`[list](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/list)` |  `GET /v1beta1/{parent=projects/*/configs/*}/waiters`   
List waiters within the given configuration.  
`[testIamPermissions](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.waiters/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/configs/*/waiters/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## Service: runtimeconfig.googleapis.com

All URIs below are relative to `https://runtimeconfig.googleapis.com`

This service provides the following [discovery documents](https://developers.google.com/discovery/v1/reference/apis):

  * <https://runtimeconfig.googleapis.com/$discovery/rest?version=v1>
  * <https://runtimeconfig.googleapis.com/$discovery/rest?version=v1beta1>



## REST Resource: [v1.operations](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1/operations/cancel)` |  `POST /v1/{name=operations/**}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1/operations/delete)` |  `DELETE /v1/{name=operations/**}`   
Deletes a long-running operation.  
`[list](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1/operations/list)` |  `GET /v1/{name}`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
