---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/
title: GKE On-Prem API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:12:15.529723+00:00
---

# GKE On-Prem API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem-api/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ GKE On-Prem API ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api-overview)



Send feedback 

#  GKE On-Prem API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.bareMetalAdminClusters
  * REST Resource: v1.projects.locations.bareMetalClusters
  * REST Resource: v1.projects.locations.bareMetalClusters.bareMetalNodePools
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.vmwareAdminClusters
  * REST Resource: v1.projects.locations.vmwareClusters
  * REST Resource: v1.projects.locations.vmwareClusters.vmwareNodePools



## Service: gkeonprem.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://gkeonprem.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://gkeonprem.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.bareMetalAdminClusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/bareMetalAdminClusters`   
Creates a new bare metal admin cluster in a given project and location.  
`[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/enroll)` |  `POST /v1/{parent=projects/*/locations/*}/bareMetalAdminClusters:enroll`   
Enrolls an existing bare metal admin cluster to the Anthos On-Prem API within a given project and location.  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/get)` |  `GET /v1/{name=projects/*/locations/*/bareMetalAdminClusters/*}`   
Gets details of a single bare metal admin cluster.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/bareMetalAdminClusters`   
Lists bare metal admin clusters in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/patch)` |  `PATCH /v1/{bareMetalAdminCluster.name=projects/*/locations/*/bareMetalAdminClusters/*}`   
Updates the parameters of a single bare metal admin cluster.  
`[queryVersionConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters/queryVersionConfig)` |  `POST /v1/{parent=projects/*/locations/*}/bareMetalAdminClusters:queryVersionConfig`   
Queries the bare metal admin cluster version config.  
  
## REST Resource: [v1.projects.locations.bareMetalClusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/bareMetalClusters`   
Creates a new bare metal cluster in a given project and location.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/bareMetalClusters/*}`   
Deletes a single bare metal Cluster.  
`[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/enroll)` |  `POST /v1/{parent=projects/*/locations/*}/bareMetalClusters:enroll`   
Enrolls an existing bare metal user cluster and its node pools to the Anthos On-Prem API within a given project and location.  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/get)` |  `GET /v1/{name=projects/*/locations/*/bareMetalClusters/*}`   
Gets details of a single bare metal Cluster.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/bareMetalClusters`   
Lists bare metal clusters in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/patch)` |  `PATCH /v1/{bareMetalCluster.name=projects/*/locations/*/bareMetalClusters/*}`   
Updates the parameters of a single bare metal Cluster.  
`[queryVersionConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters/queryVersionConfig)` |  `POST /v1/{parent=projects/*/locations/*}/bareMetalClusters:queryVersionConfig`   
Queries the bare metal user cluster version config.  
  
## REST Resource: [v1.projects.locations.bareMetalClusters.bareMetalNodePools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/create)` |  `POST /v1/{parent=projects/*/locations/*/bareMetalClusters/*}/bareMetalNodePools`   
Creates a new bare metal node pool in a given project, location and Bare Metal cluster.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/delete)` |  `DELETE /v1/{name=projects/*/locations/*/bareMetalClusters/*/bareMetalNodePools/*}`   
Deletes a single bare metal node pool.  
`[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/enroll)` |  `POST /v1/{parent=projects/*/locations/*/bareMetalClusters/*}/bareMetalNodePools:enroll`   
Enrolls an existing bare metal node pool to the Anthos On-Prem API within a given project and location.  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/get)` |  `GET /v1/{name=projects/*/locations/*/bareMetalClusters/*/bareMetalNodePools/*}`   
Gets details of a single bare metal node pool.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/list)` |  `GET /v1/{parent=projects/*/locations/*/bareMetalClusters/*}/bareMetalNodePools`   
Lists bare metal node pools in a given project, location and bare metal cluster.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters.bareMetalNodePools/patch)` |  `PATCH /v1/{bareMetalNodePool.name=projects/*/locations/*/bareMetalClusters/*/bareMetalNodePools/*}`   
Updates the parameters of a single bare metal node pool.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.vmwareAdminClusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/vmwareAdminClusters`   
Creates a new VMware admin cluster in a given project and location.  
`[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/enroll)` |  `POST /v1/{parent=projects/*/locations/*}/vmwareAdminClusters:enroll`   
Enrolls an existing VMware admin cluster to the Anthos On-Prem API within a given project and location.  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/get)` |  `GET /v1/{name=projects/*/locations/*/vmwareAdminClusters/*}`   
Gets details of a single VMware admin cluster.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/vmwareAdminClusters`   
Lists VMware admin clusters in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareAdminClusters/patch)` |  `PATCH /v1/{vmwareAdminCluster.name=projects/*/locations/*/vmwareAdminClusters/*}`   
Updates the parameters of a single VMware admin cluster.  
  
## REST Resource: [v1.projects.locations.vmwareClusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/vmwareClusters`   
Creates a new VMware user cluster in a given project and location.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/vmwareClusters/*}`   
Deletes a single VMware Cluster.  
`[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/enroll)` |  `POST /v1/{parent=projects/*/locations/*}/vmwareClusters:enroll`   
Enrolls an existing VMware user cluster and its node pools to the Anthos On-Prem API within a given project and location.  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/get)` |  `GET /v1/{name=projects/*/locations/*/vmwareClusters/*}`   
Gets details of a single VMware Cluster.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/vmwareClusters`   
Lists VMware Clusters in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/patch)` |  `PATCH /v1/{vmwareCluster.name=projects/*/locations/*/vmwareClusters/*}`   
Updates the parameters of a single VMware cluster.  
`[queryVersionConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters/queryVersionConfig)` |  `POST /v1/{parent=projects/*/locations/*}/vmwareClusters:queryVersionConfig`   
Queries the VMware user cluster version config.  
  
## REST Resource: [v1.projects.locations.vmwareClusters.vmwareNodePools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/create)` |  `POST /v1/{parent=projects/*/locations/*/vmwareClusters/*}/vmwareNodePools`   
Creates a new VMware node pool in a given project, location and VMWare cluster.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/delete)` |  `DELETE /v1/{name=projects/*/locations/*/vmwareClusters/*/vmwareNodePools/*}`   
Deletes a single VMware node pool.  
`[enroll](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/enroll)` |  `POST /v1/{parent=projects/*/locations/*/vmwareClusters/*}/vmwareNodePools:enroll`   
Enrolls a VMware node pool to Anthos On-Prem API  
`[get](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/get)` |  `GET /v1/{name=projects/*/locations/*/vmwareClusters/*/vmwareNodePools/*}`   
Gets details of a single VMware node pool.  
`[list](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/list)` |  `GET /v1/{parent=projects/*/locations/*/vmwareClusters/*}/vmwareNodePools`   
Lists VMware node pools in a given project, location and VMWare cluster.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.vmwareClusters.vmwareNodePools/patch)` |  `PATCH /v1/{vmwareNodePool.name=projects/*/locations/*/vmwareClusters/*/vmwareNodePools/*}`   
Updates the parameters of a single VMware node pool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
