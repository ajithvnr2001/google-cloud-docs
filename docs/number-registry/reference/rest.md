---
url: https://docs.cloud.google.com/number-registry/reference/rest/
title: Cloud Number Registry API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:18:45.571779+00:00
---

# Cloud Number Registry API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  Cloud Number Registry API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.customRanges
  * REST Resource: v1alpha.projects.locations.discoveredRanges
  * REST Resource: v1alpha.projects.locations.ipamAdminScopes
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.realms
  * REST Resource: v1alpha.projects.locations.registryBooks



## Service: cloudnumberregistry.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://cloudnumberregistry.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudnumberregistry.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.customRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges)

Methods  
---  
`[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/customRanges`   
Creates a new CustomRange in a given project and location.  
`[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/customRanges/*}`   
Deletes a single CustomRange.  
`[findFreeIpRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/findFreeIpRanges)` |  `GET /v1alpha/{name=projects/*/locations/*/customRanges/*}:findFreeIpRanges`   
Finds free IP ranges in a single CustomRange.  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/get)` |  `GET /v1alpha/{name=projects/*/locations/*/customRanges/*}`   
Gets details of a single CustomRange.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/customRanges`   
Lists CustomRanges in a given project and location.  
`[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/patch)` |  `PATCH /v1alpha/{customRange.name=projects/*/locations/*/customRanges/*}`   
Updates the parameters of a single CustomRange.  
`[showUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/showUtilization)` |  `GET /v1alpha/{name=projects/*/locations/*/customRanges/*}:showUtilization`   
Gets the details of a single CustomRange and its utilization.  
  
## REST Resource: [v1alpha.projects.locations.discoveredRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges)

Methods  
---  
`[findFreeIpRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/findFreeIpRanges)` |  `GET /v1alpha/{name=projects/*/locations/*/discoveredRanges/*}:findFreeIpRanges`   
Finds free IP ranges in a single DiscoveredRange.  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/get)` |  `GET /v1alpha/{name=projects/*/locations/*/discoveredRanges/*}`   
Gets details of a single DiscoveredRange.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/discoveredRanges`   
Lists DiscoveredRanges in a given project and location.  
`[showUtilization](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.discoveredRanges/showUtilization)` |  `GET /v1alpha/{name=projects/*/locations/*/discoveredRanges/*}:showUtilization`   
Gets the details of a single DiscoveredRange and its utilization.  
  
## REST Resource: [v1alpha.projects.locations.ipamAdminScopes](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes)

Methods  
---  
`[checkAvailability](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/checkAvailability)` |  `GET /v1alpha/{parent=projects/*/locations/*}/ipamAdminScopes:checkAvailability`   
Checks the availability of IpamAdminScopes in a given project and location.  
`[cleanup](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/cleanup)` |  `POST /v1alpha/{name=projects/*/locations/*/ipamAdminScopes/*}:cleanup`   
Cleans up a single IpamAdminScope.  
`[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/ipamAdminScopes`   
Creates a new IpamAdminScope in a given project and location.  
`[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/ipamAdminScopes/*}`   
Deletes a single IpamAdminScope.  
`[disable](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/disable)` |  `POST /v1alpha/{name=projects/*/locations/*/ipamAdminScopes/*}:disable`   
Disables a single IpamAdminScope.  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/get)` |  `GET /v1alpha/{name=projects/*/locations/*/ipamAdminScopes/*}`   
Gets details of a single IpamAdminScope.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/ipamAdminScopes`   
Lists IpamAdminScopes in a given project and location.  
`[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.ipamAdminScopes/patch)` |  `PATCH /v1alpha/{ipamAdminScope.name=projects/*/locations/*/ipamAdminScopes/*}`   
Updates the parameters of a single IpamAdminScope.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.realms](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms)

Methods  
---  
`[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/realms`   
Creates a new Realm in a given project and location.  
`[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/realms/*}`   
Deletes a single Realm.  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/get)` |  `GET /v1alpha/{name=projects/*/locations/*/realms/*}`   
Gets details of a single Realm.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/realms`   
Lists Realms in a given project and location.  
`[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.realms/patch)` |  `PATCH /v1alpha/{realm.name=projects/*/locations/*/realms/*}`   
Updates the parameters of a single Realm.  
  
## REST Resource: [v1alpha.projects.locations.registryBooks](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks)

Methods  
---  
`[create](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/registryBooks`   
Creates a new RegistryBook in a given project and location.  
`[delete](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/registryBooks/*}`   
Deletes a single RegistryBook.  
`[get](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/get)` |  `GET /v1alpha/{name=projects/*/locations/*/registryBooks/*}`   
Gets details of a single RegistryBook.  
`[list](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/registryBooks`   
Lists RegistryBooks in a given project and location.  
`[patch](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/patch)` |  `PATCH /v1alpha/{registryBook.name=projects/*/locations/*/registryBooks/*}`   
Updates the parameters of a single RegistryBook.  
`[searchIpResources](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.registryBooks/searchIpResources)` |  `POST /v1alpha/{name=projects/*/locations/*/registryBooks/*}:searchIpResources`   
Searches IP resources in a given RegistryBook.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
