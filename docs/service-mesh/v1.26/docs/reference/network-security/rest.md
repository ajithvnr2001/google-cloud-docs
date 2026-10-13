---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/
title: Network Security API \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:36.345189+00:00
---

# Network Security API  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/

You are viewing archived v1.26 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback 

#  Network Security API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations.authorizationPolicies
  * REST Resource: v1.projects.locations.clientTlsPolicies
  * REST Resource: v1.projects.locations.serverTlsPolicies
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.authorizationPolicies
  * REST Resource: v1beta1.projects.locations.clientTlsPolicies
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta1.projects.locations.serverTlsPolicies



## Service: networksecurity.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1>
  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networksecurity.googleapis.com`



## REST Resource: [v1.projects.locations.authorizationPolicies](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/authorizationPolicies`   
Creates a new AuthorizationPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/authorizationPolicies/*}`   
Deletes a single AuthorizationPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/authorizationPolicies/*}`   
Gets details of a single AuthorizationPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/authorizationPolicies`   
Lists AuthorizationPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.authorizationPolicies/patch)` |  `PATCH /v1/{authorizationPolicy.name=projects/*/locations/*/authorizationPolicies/*}`   
Updates the parameters of a single AuthorizationPolicy.  
  
## REST Resource: [v1.projects.locations.clientTlsPolicies](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/clientTlsPolicies`   
Creates a new ClientTlsPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/clientTlsPolicies/*}`   
Deletes a single ClientTlsPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/clientTlsPolicies/*}`   
Gets details of a single ClientTlsPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/clientTlsPolicies`   
Lists ClientTlsPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.clientTlsPolicies/patch)` |  `PATCH /v1/{clientTlsPolicy.name=projects/*/locations/*/clientTlsPolicies/*}`   
Updates the parameters of a single ClientTlsPolicy.  
  
## REST Resource: [v1.projects.locations.serverTlsPolicies](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/serverTlsPolicies`   
Creates a new ServerTlsPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/serverTlsPolicies/*}`   
Deletes a single ServerTlsPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/serverTlsPolicies/*}`   
Gets details of a single ServerTlsPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/serverTlsPolicies`   
Lists ServerTlsPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1/projects.locations.serverTlsPolicies/patch)` |  `PATCH /v1/{serverTlsPolicy.name=projects/*/locations/*/serverTlsPolicies/*}`   
Updates the parameters of a single ServerTlsPolicy.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.authorizationPolicies](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/authorizationPolicies`   
Creates a new AuthorizationPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/authorizationPolicies/*}`   
Deletes a single AuthorizationPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/authorizationPolicies/*}`   
Gets details of a single AuthorizationPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/authorizationPolicies`   
Lists AuthorizationPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/patch)` |  `PATCH /v1beta1/{authorizationPolicy.name=projects/*/locations/*/authorizationPolicies/*}`   
Updates the parameters of a single AuthorizationPolicy.  
  
## REST Resource: [v1beta1.projects.locations.clientTlsPolicies](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/clientTlsPolicies`   
Creates a new ClientTlsPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/clientTlsPolicies/*}`   
Deletes a single ClientTlsPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/clientTlsPolicies/*}`   
Gets details of a single ClientTlsPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/clientTlsPolicies`   
Lists ClientTlsPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/patch)` |  `PATCH /v1beta1/{clientTlsPolicy.name=projects/*/locations/*/clientTlsPolicies/*}`   
Updates the parameters of a single ClientTlsPolicy.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.serverTlsPolicies](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/serverTlsPolicies`   
Creates a new ServerTlsPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/serverTlsPolicies/*}`   
Deletes a single ServerTlsPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/serverTlsPolicies/*}`   
Gets details of a single ServerTlsPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/serverTlsPolicies`   
Lists ServerTlsPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.26/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/patch)` |  `PATCH /v1beta1/{serverTlsPolicy.name=projects/*/locations/*/serverTlsPolicies/*}`   
Updates the parameters of a single ServerTlsPolicy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-20 UTC."],[],[]] 
