---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/
title: Google Cloud Memorystore for Redis API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:45.972019+00:00
---

# Google Cloud Memorystore for Redis API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Google Cloud Memorystore for Redis API Stay organized with collections  Save and categorize content based on your preferences. 

Creates and manages Redis instances on the Google Cloud Platform.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.instances
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.operations



## Service: redis.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://redis.googleapis.com/$discovery/rest?version=v1>
  * <https://redis.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://redis.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/instances`   
Creates a Redis instance based on the specified tier and memory size.  
`[delete](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/instances/*}`   
Deletes a specific Redis instance.  
`[export](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/export)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:export`   
Export Redis instance data into a Redis RDB format file in Cloud Storage.  
`[failover](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/failover)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:failover`   
Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/get)` |  `GET /v1beta1/{name=projects/*/locations/*/instances/*}`   
Gets the details of a specific Redis instance.  
`[getAuthString](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/getAuthString)` |  `GET /v1beta1/{name=projects/*/locations/*/instances/*}/authString`   
Gets the AUTH string for a Redis instance.  
`[import](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/import)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:import`   
Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/instances`   
Lists all Redis instances owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/patch)` |  `PATCH /v1beta1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the metadata and configuration of a specific Redis instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedule maintenance for a given instance in a given project and location.  
`[upgrade](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.instances/upgrade)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:upgrade`   
Upgrades Redis instance to the newer Redis version specified in the request.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates a Redis instance based on the specified tier and memory size.  
`[delete](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes a specific Redis instance.  
`[export](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/export)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:export`   
Export Redis instance data into a Redis RDB format file in Cloud Storage.  
`[failover](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/failover)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:failover`   
Initiates a failover of the primary node to current replica node for a specific STANDARD tier Cloud Memorystore for Redis instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets the details of a specific Redis instance.  
`[getAuthString](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/getAuthString)` |  `GET /v1/{name=projects/*/locations/*/instances/*}/authString`   
Gets the AUTH string for a Redis instance.  
`[import](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/import)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:import`   
Import a Redis RDB snapshot file from Cloud Storage into a Redis instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists all Redis instances owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the metadata and configuration of a specific Redis instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedule maintenance for a given instance in a given project and location.  
`[upgrade](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/upgrade)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:upgrade`   
Upgrades Redis instance to the newer Redis version specified in the request.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
