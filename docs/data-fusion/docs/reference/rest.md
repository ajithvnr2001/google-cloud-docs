---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/
title: Cloud Data Fusion API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:08.007681+00:00
---

# Cloud Data Fusion API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  Cloud Data Fusion API Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion is a fully-managed, cloud native, enterprise data integration service for quickly building and managing data pipelines. It provides a graphical interface to increase time efficiency and reduce complexity, and allows business users, developers, and data scientists to easily and reliably build scalable data integration solutions to cleanse, prepare, blend, transfer and transform data without having to wrestle with infrastructure.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.instances
  * REST Resource: v1beta1.projects.locations.instances.dnsPeerings
  * REST Resource: v1beta1.projects.locations.instances.namespaces
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta1.projects.locations.versions
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.dnsPeerings
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.versions



## Service: datafusion.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://datafusion.googleapis.com/$discovery/rest?version=v1>
  * <https://datafusion.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://datafusion.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
`[removeIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations/removeIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/**}:removeIamPolicy`   
Remove IAM policy that is currently set on the given resource.  
  
## REST Resource: [v1beta1.projects.locations.instances](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/instances`   
Creates a new Data Fusion instance in the specified project and location.  
`[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/instances/*}`   
Deletes a single Data Fusion instance.  
`[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/get)` |  `GET /v1beta1/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Data Fusion instance.  
`[getIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/instances/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/instances`   
Lists Data Fusion instances in the specified project and location.  
`[patch](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/patch)` |  `PATCH /v1beta1/{instance.name=projects/*/locations/*/instances/*}`   
Updates a single Data Fusion instance.  
`[restart](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/restart)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:restart`   
Restart a single Data Fusion instance.  
`[setIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/instances/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/instances/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[upgrade](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances/upgrade)` |  `POST /v1beta1/{name=projects/*/locations/*/instances/*}:upgrade`   
Upgrade a single Data Fusion instance.  
  
## REST Resource: [v1beta1.projects.locations.instances.dnsPeerings](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings)

Methods  
---  
`[create](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/instances/*}/dnsPeerings`   
Creates DNS peering on the given resource.  
`[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/instances/*/dnsPeerings/*}`   
Deletes DNS peering on the given resource.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.dnsPeerings/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/instances/*}/dnsPeerings`   
Lists DNS peerings for a given resource.  
  
## REST Resource: [v1beta1.projects.locations.instances.namespaces](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces)

Methods  
---  
`[getIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/instances/*/namespaces/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/instances/*}/namespaces`   
List namespaces in a given instance  
`[setIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/instances/*/namespaces/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.instances.namespaces/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/instances/*/namespaces/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.versions](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.versions)

Methods  
---  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1beta1/projects.locations.versions/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/versions`   
Lists possible versions for Data Fusion instances in the specified project and location.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[create](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates a new Data Fusion instance in the specified project and location.  
`[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes a single Date Fusion instance.  
`[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Data Fusion instance.  
`[getIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/instances/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists Data Fusion instances in the specified project and location.  
`[patch](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates a single Data Fusion instance.  
`[restart](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/restart)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:restart`   
Restart a single Data Fusion instance.  
`[setIamPolicy](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/instances/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/instances/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.instances.dnsPeerings](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings)

Methods  
---  
`[create](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings/create)` |  `POST /v1/{parent=projects/*/locations/*/instances/*}/dnsPeerings`   
Creates DNS peering on the given resource.  
`[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/dnsPeerings/*}`   
Deletes DNS peering on the given resource.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances.dnsPeerings/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/dnsPeerings`   
Lists DNS peerings for a given resource.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.versions](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.versions)

Methods  
---  
`[list](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.versions/list)` |  `GET /v1/{parent=projects/*/locations/*}/versions`   
Lists possible versions for Data Fusion instances in the specified project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-20 UTC."],[],[]] 
