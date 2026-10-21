---
url: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/
title: Cloud Memorystore for Memcached API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:10:47.505160+00:00
---

# Cloud Memorystore for Memcached API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/memcached/apis)



Send feedback 

#  Cloud Memorystore for Memcached API Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Memorystore for Memcached API is used for creating and managing Memcached instances in GCP.

  * REST Resource: v1beta2.projects.locations
  * REST Resource: v1beta2.projects.locations.instances
  * REST Resource: v1beta2.projects.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.operations



## Service: memcache.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://memcache.googleapis.com/$discovery/rest?version=v1>
  * <https://memcache.googleapis.com/$discovery/rest?version=v1beta2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://memcache.googleapis.com`



## REST Resource: [v1beta2.projects.locations](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations/get)` |  `GET /v1beta2/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations/list)` |  `GET /v1beta2/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta2.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances)

Methods  
---  
`[applyParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/applyParameters)` |  `POST /v1beta2/{name=projects/*/locations/*/instances/*}:applyParameters`   
`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.  
`[applySoftwareUpdate](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/applySoftwareUpdate)` |  `POST /v1beta2/{instance=projects/*/locations/*/instances/*}:applySoftwareUpdate`   
Updates software on the selected nodes of the Instance.  
`[create](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/create)` |  `POST /v1beta2/{parent=projects/*/locations/*}/instances`   
Creates a new Instance in a given location.  
`[delete](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/delete)` |  `DELETE /v1beta2/{name=projects/*/locations/*/instances/*}`   
Deletes a single Instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/get)` |  `GET /v1beta2/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/list)` |  `GET /v1beta2/{parent=projects/*/locations/*}/instances`   
Lists Instances in a given location.  
`[patch](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/patch)` |  `PATCH /v1beta2/{resource.name=projects/*/locations/*/instances/*}`   
Updates an existing Instance in a given project and location.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1beta2/{instance=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Performs the apply phase of the RescheduleMaintenance verb.  
`[updateParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/updateParameters)` |  `PATCH /v1beta2/{name=projects/*/locations/*/instances/*}:updateParameters`   
Updates the defined Memcached parameters for an existing instance.  
`[upgrade](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.instances/upgrade)` |  `POST /v1beta2/{name=projects/*/locations/*/instances/*}:upgrade`   
Upgrades the Memcache instance to a newer memcached engine version specified in the request.  
  
## REST Resource: [v1beta2.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.operations/cancel)` |  `POST /v1beta2/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.operations/delete)` |  `DELETE /v1beta2/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.operations/get)` |  `GET /v1beta2/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1beta2/projects.locations.operations/list)` |  `GET /v1beta2/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[applyParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/applyParameters)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:applyParameters`   
`ApplyParameters` restarts the set of specified nodes in order to update them to the current set of parameters for the Memcached Instance.  
`[create](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates a new Instance in a given location.  
`[delete](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes a single Instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists Instances in a given location.  
`[patch](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates an existing Instance in a given project and location.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1/{instance=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedules upcoming maintenance event.  
`[updateParameters](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/updateParameters)` |  `PATCH /v1/{name=projects/*/locations/*/instances/*}:updateParameters`   
Updates the defined Memcached parameters for an existing instance.  
`[upgrade](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.instances/upgrade)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:upgrade`   
Upgrades the Memcache instance to a newer memcached engine version specified in the request.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/memcached/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
