---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/
title: Distributed Cloud Edge Container API \u00a0|\u00a0 Google Distributed Cloud connected, version 1.10.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:22.087945+00:00
---

# Distributed Cloud Edge Container API  |  Google Distributed Cloud connected, version 1.10.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/apis)



Send feedback 

#  Distributed Cloud Edge Container API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.clusters
  * REST Resource: v1.projects.locations.clusters.nodePools
  * REST Resource: v1.projects.locations.machines
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.vpnConnections



## Service: edgecontainer.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://edgecontainer.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://edgecontainer.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getServerConfig](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations/getServerConfig)` |  `GET /v1/{name=projects/*/locations/*}/serverConfig`   
Gets the server config.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.clusters](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/clusters`   
Creates a new Cluster in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/clusters/*}`   
Deletes a single Cluster.  
`[generateAccessToken](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/generateAccessToken)` |  `GET /v1/{cluster=projects/*/locations/*/clusters/*}:generateAccessToken`   
Generates an access token for a Cluster.  
`[generateOfflineCredential](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/generateOfflineCredential)` |  `GET /v1/{cluster=projects/*/locations/*/clusters/*}:generateOfflineCredential`   
Generates an offline credential for a Cluster.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/get)` |  `GET /v1/{name=projects/*/locations/*/clusters/*}`   
Gets details of a single Cluster.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/clusters`   
Lists Clusters in a given project and location.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/patch)` |  `PATCH /v1/{cluster.name=projects/*/locations/*/clusters/*}`   
Updates the parameters of a single Cluster.  
`[upgrade](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters/upgrade)` |  `POST /v1/{name=projects/*/locations/*/clusters/*}:upgrade`   
Upgrades a single cluster.  
  
## REST Resource: [v1.projects.locations.clusters.nodePools](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters.nodePools)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/create)` |  `POST /v1/{parent=projects/*/locations/*/clusters/*}/nodePools`   
Creates a new NodePool in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/delete)` |  `DELETE /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}`   
Deletes a single NodePool.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/get)` |  `GET /v1/{name=projects/*/locations/*/clusters/*/nodePools/*}`   
Gets details of a single NodePool.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/list)` |  `GET /v1/{parent=projects/*/locations/*/clusters/*}/nodePools`   
Lists NodePools in a given project and location.  
`[patch](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.clusters.nodePools/patch)` |  `PATCH /v1/{nodePool.name=projects/*/locations/*/clusters/*/nodePools/*}`   
Updates the parameters of a single NodePool.  
  
## REST Resource: [v1.projects.locations.machines](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.machines)

Methods  
---  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.machines/get)` |  `GET /v1/{name=projects/*/locations/*/machines/*}`   
Gets details of a single Machine.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.machines/list)` |  `GET /v1/{parent=projects/*/locations/*}/machines`   
Lists Machines in a given project and location.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.vpnConnections](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.vpnConnections)

Methods  
---  
`[create](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/create)` |  `POST /v1/{parent=projects/*/locations/*}/vpnConnections`   
Creates a new VPN connection in a given project and location.  
`[delete](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/delete)` |  `DELETE /v1/{name=projects/*/locations/*/vpnConnections/*}`   
Deletes a single VPN connection.  
`[get](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/get)` |  `GET /v1/{name=projects/*/locations/*/vpnConnections/*}`   
Gets details of a single VPN connection.  
`[list](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/list)` |  `GET /v1/{parent=projects/*/locations/*}/vpnConnections`   
Lists VPN connections in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
