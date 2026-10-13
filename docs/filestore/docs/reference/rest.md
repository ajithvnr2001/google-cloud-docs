---
url: https://docs.cloud.google.com/filestore/docs/reference/rest/
title: Cloud Filestore API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:19.480299+00:00
---

# Cloud Filestore API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/filestore/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Filestore ](https://docs.cloud.google.com/filestore/docs)
  * [ Reference ](https://docs.cloud.google.com/filestore/docs/apis)



Send feedback 

#  Cloud Filestore API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Filestore API is used for creating and managing cloud file servers.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.backups
  * REST Resource: v1beta1.projects.locations.instances
  * REST Resource: v1beta1.projects.locations.instances.shares
  * REST Resource: v1beta1.projects.locations.instances.snapshots
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.backups
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.snapshots
  * REST Resource: v1.projects.locations.operations



## Service: file.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://file.googleapis.com/$discovery/rest?version=v1>
  * <https://file.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://file.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.backups](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.backups)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.backups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/backups`   
Creates a backup.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.backups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/backups/*}`   
Deletes a backup.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.backups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.backups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/backups`   
Lists all backups in a project for either a specified location or for all locations.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.backups/patch)` |  `PATCH /v1beta1/{backup.name=projects/*/locations/*/backups/*}`   
Updates the settings of a specific backup.  
  
## REST Resource: [v1beta1.projects.locations.instances](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/instances`   
Creates an instance.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/instances/*}`   
Deletes an instance.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/get)` |  `GET /v1beta1/{name=projects/*/locations/*/instances/*}`   
Gets the details of a specific instance.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/instances`   
Lists all instances in a project for either a specified location or for all locations.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/patch)` |  `PATCH /v1beta1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the settings of a specific instance.  
`[pauseReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/pauseReplica)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:pauseReplica`   
Pause the standby instance (replica).  
`[promoteReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/promoteReplica)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:promoteReplica`   
Promote the standby instance (replica).  
`[restore](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/restore)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:restore`   
Restores an existing instance's file share from a backup.  
`[resumeReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/resumeReplica)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:resumeReplica`   
Resume the standby instance (replica).  
`[revert](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances/revert)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:revert`   
Revert an existing instance's file system to a specified snapshot.  
  
## REST Resource: [v1beta1.projects.locations.instances.shares](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/instances/*}/shares`   
Creates a share.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/instances/*/shares/*}`   
Deletes a share.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/get)` |  `GET /v1beta1/{name=projects/*/locations/*/instances/*/shares/*}`   
Gets the details of a specific share.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/instances/*}/shares`   
Lists all shares for a specified instance.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.shares/patch)` |  `PATCH /v1beta1/{share.name=projects/*/locations/*/instances/*/shares/*}`   
Updates the settings of a specific share.  
  
## REST Resource: [v1beta1.projects.locations.instances.snapshots](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.snapshots)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.snapshots/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/instances/*}/snapshots`   
Creates a snapshot.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.snapshots/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/instances/*/snapshots/*}`   
Deletes a snapshot.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.snapshots/get)` |  `GET /v1beta1/{name=projects/*/locations/*/instances/*/snapshots/*}`   
Gets the details of a specific snapshot.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.snapshots/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/instances/*}/snapshots`   
Lists all snapshots in a project for either a specified location or for all locations.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.instances.snapshots/patch)` |  `PATCH /v1beta1/{snapshot.name=projects/*/locations/*/instances/*/snapshots/*}`   
Updates the settings of a specific snapshot.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.backups](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/create)` |  `POST /v1/{parent=projects/*/locations/*}/backups`   
Creates a backup.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/backups/*}`   
Deletes a backup.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/get)` |  `GET /v1/{name=projects/*/locations/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/list)` |  `GET /v1/{parent=projects/*/locations/*}/backups`   
Lists all backups in a project for either a specified location or for all locations.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.backups/patch)` |  `PATCH /v1/{backup.name=projects/*/locations/*/backups/*}`   
Updates the settings of a specific backup.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates an instance.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes an instance.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets the details of a specific instance.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists all instances in a project for either a specified location or for all locations.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the settings of a specific instance.  
`[promoteReplica](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/promoteReplica)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:promoteReplica`   
Promote the standby instance (replica).  
`[restore](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/restore)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:restore`   
Restores an existing instance's file share from a backup.  
`[revert](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances/revert)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:revert`   
Revert an existing instance's file system to a specified snapshot.  
  
## REST Resource: [v1.projects.locations.instances.snapshots](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots)

Methods  
---  
`[create](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/snapshots`   
Creates a snapshot.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/snapshots/*}`   
Deletes a snapshot.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/snapshots/*}`   
Gets the details of a specific snapshot.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/snapshots`   
Lists all snapshots in a project for either a specified location or for all locations.  
`[patch](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.instances.snapshots/patch)` |  `PATCH /v1/{snapshot.name=projects/*/locations/*/instances/*/snapshots/*}`   
Updates the settings of a specific snapshot.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/filestore/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-11 UTC."],[],[]] 
