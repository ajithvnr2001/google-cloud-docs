---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/
title: Network Security API \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:27.513722+00:00
---

# Network Security API  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  Network Security API Stay organized with collections  Save and categorize content based on your preferences. 

## Service: networksecurity.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1>
  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networksecurity.googleapis.com`



## REST Resource: [v1beta1.organizations.locations.operations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/organizations.locations.operations/cancel)` |  `POST /v1beta1/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/organizations.locations.operations/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/organizations.locations.operations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/organizations.locations.operations/list)` |  `GET /v1beta1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.interceptDeploymentGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeploymentGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeploymentGroups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/interceptDeploymentGroups`   
Creates a deployment group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeploymentGroups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/interceptDeploymentGroups/*}`   
Deletes a deployment group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeploymentGroups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/interceptDeploymentGroups/*}`   
Gets a specific deployment group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeploymentGroups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/interceptDeploymentGroups`   
Lists deployment groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeploymentGroups/patch)` |  `PATCH /v1beta1/{interceptDeploymentGroup.name=projects/*/locations/*/interceptDeploymentGroups/*}`   
Updates a deployment group.  
  
## REST Resource: [v1beta1.projects.locations.interceptDeployments](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/interceptDeployments`   
Creates a deployment in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/interceptDeployments/*}`   
Deletes a deployment.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/get)` |  `GET /v1beta1/{name=projects/*/locations/*/interceptDeployments/*}`   
Gets a specific deployment.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/interceptDeployments`   
Lists deployments in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/patch)` |  `PATCH /v1beta1/{interceptDeployment.name=projects/*/locations/*/interceptDeployments/*}`   
Updates a deployment.  
  
## REST Resource: [v1beta1.projects.locations.interceptEndpointGroupAssociations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroupAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroupAssociations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/interceptEndpointGroupAssociations`   
Creates an association in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroupAssociations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/interceptEndpointGroupAssociations/*}`   
Deletes an association.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroupAssociations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/interceptEndpointGroupAssociations/*}`   
Gets a specific association.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroupAssociations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/interceptEndpointGroupAssociations`   
Lists associations in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroupAssociations/patch)` |  `PATCH /v1beta1/{interceptEndpointGroupAssociation.name=projects/*/locations/*/interceptEndpointGroupAssociations/*}`   
Updates an association.  
  
## REST Resource: [v1beta1.projects.locations.interceptEndpointGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/interceptEndpointGroups`   
Creates an endpoint group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/interceptEndpointGroups/*}`   
Deletes an endpoint group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/interceptEndpointGroups/*}`   
Gets a specific endpoint group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/interceptEndpointGroups`   
Lists endpoint groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptEndpointGroups/patch)` |  `PATCH /v1beta1/{interceptEndpointGroup.name=projects/*/locations/*/interceptEndpointGroups/*}`   
Updates an endpoint group.  
  
## REST Resource: [v1beta1.projects.locations.mirroringDeploymentGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/mirroringDeploymentGroups`   
Creates a deployment group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/mirroringDeploymentGroups/*}`   
Deletes a deployment group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/mirroringDeploymentGroups/*}`   
Gets a specific deployment group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/mirroringDeploymentGroups`   
Lists deployment groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/patch)` |  `PATCH /v1beta1/{mirroringDeploymentGroup.name=projects/*/locations/*/mirroringDeploymentGroups/*}`   
Updates a deployment group.  
  
## REST Resource: [v1beta1.projects.locations.mirroringDeployments](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeployments/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/mirroringDeployments`   
Creates a deployment in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeployments/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/mirroringDeployments/*}`   
Deletes a deployment.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeployments/get)` |  `GET /v1beta1/{name=projects/*/locations/*/mirroringDeployments/*}`   
Gets a specific deployment.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeployments/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/mirroringDeployments`   
Lists deployments in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeployments/patch)` |  `PATCH /v1beta1/{mirroringDeployment.name=projects/*/locations/*/mirroringDeployments/*}`   
Updates a deployment.  
  
## REST Resource: [v1beta1.projects.locations.mirroringEndpointGroupAssociations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroupAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroupAssociations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/mirroringEndpointGroupAssociations`   
Creates an association in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroupAssociations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/mirroringEndpointGroupAssociations/*}`   
Deletes an association.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroupAssociations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/mirroringEndpointGroupAssociations/*}`   
Gets a specific association.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroupAssociations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/mirroringEndpointGroupAssociations`   
Lists associations in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroupAssociations/patch)` |  `PATCH /v1beta1/{mirroringEndpointGroupAssociation.name=projects/*/locations/*/mirroringEndpointGroupAssociations/*}`   
Updates an association.  
  
## REST Resource: [v1beta1.projects.locations.mirroringEndpointGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/mirroringEndpointGroups`   
Creates an endpoint group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/mirroringEndpointGroups/*}`   
Deletes an endpoint group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/mirroringEndpointGroups/*}`   
Gets a specific endpoint group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/mirroringEndpointGroups`   
Lists endpoint groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringEndpointGroups/patch)` |  `PATCH /v1beta1/{mirroringEndpointGroup.name=projects/*/locations/*/mirroringEndpointGroups/*}`   
Updates an endpoint group.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.organizations.locations.operations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/organizations.locations.operations/cancel)` |  `POST /v1/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/organizations.locations.operations/delete)` |  `DELETE /v1/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/organizations.locations.operations/get)` |  `GET /v1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/organizations.locations.operations/list)` |  `GET /v1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.interceptDeploymentGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups/create)` |  `POST /v1/{parent=projects/*/locations/*}/interceptDeploymentGroups`   
Creates a deployment group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/interceptDeploymentGroups/*}`   
Deletes a deployment group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups/get)` |  `GET /v1/{name=projects/*/locations/*/interceptDeploymentGroups/*}`   
Gets a specific deployment group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups/list)` |  `GET /v1/{parent=projects/*/locations/*}/interceptDeploymentGroups`   
Lists deployment groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeploymentGroups/patch)` |  `PATCH /v1/{interceptDeploymentGroup.name=projects/*/locations/*/interceptDeploymentGroups/*}`   
Updates a deployment group.  
  
## REST Resource: [v1.projects.locations.interceptDeployments](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/create)` |  `POST /v1/{parent=projects/*/locations/*}/interceptDeployments`   
Creates a deployment in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/interceptDeployments/*}`   
Deletes a deployment.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/get)` |  `GET /v1/{name=projects/*/locations/*/interceptDeployments/*}`   
Gets a specific deployment.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/list)` |  `GET /v1/{parent=projects/*/locations/*}/interceptDeployments`   
Lists deployments in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptDeployments/patch)` |  `PATCH /v1/{interceptDeployment.name=projects/*/locations/*/interceptDeployments/*}`   
Updates a deployment.  
  
## REST Resource: [v1.projects.locations.interceptEndpointGroupAssociations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/create)` |  `POST /v1/{parent=projects/*/locations/*}/interceptEndpointGroupAssociations`   
Creates an association in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/interceptEndpointGroupAssociations/*}`   
Deletes an association.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/get)` |  `GET /v1/{name=projects/*/locations/*/interceptEndpointGroupAssociations/*}`   
Gets a specific association.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/list)` |  `GET /v1/{parent=projects/*/locations/*}/interceptEndpointGroupAssociations`   
Lists associations in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroupAssociations/patch)` |  `PATCH /v1/{interceptEndpointGroupAssociation.name=projects/*/locations/*/interceptEndpointGroupAssociations/*}`   
Updates an association.  
  
## REST Resource: [v1.projects.locations.interceptEndpointGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/create)` |  `POST /v1/{parent=projects/*/locations/*}/interceptEndpointGroups`   
Creates an endpoint group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/interceptEndpointGroups/*}`   
Deletes an endpoint group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/get)` |  `GET /v1/{name=projects/*/locations/*/interceptEndpointGroups/*}`   
Gets a specific endpoint group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/list)` |  `GET /v1/{parent=projects/*/locations/*}/interceptEndpointGroups`   
Lists endpoint groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.interceptEndpointGroups/patch)` |  `PATCH /v1/{interceptEndpointGroup.name=projects/*/locations/*/interceptEndpointGroups/*}`   
Updates an endpoint group.  
  
## REST Resource: [v1.projects.locations.mirroringDeploymentGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups/create)` |  `POST /v1/{parent=projects/*/locations/*}/mirroringDeploymentGroups`   
Creates a deployment group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/mirroringDeploymentGroups/*}`   
Deletes a deployment group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups/get)` |  `GET /v1/{name=projects/*/locations/*/mirroringDeploymentGroups/*}`   
Gets a specific deployment group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups/list)` |  `GET /v1/{parent=projects/*/locations/*}/mirroringDeploymentGroups`   
Lists deployment groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeploymentGroups/patch)` |  `PATCH /v1/{mirroringDeploymentGroup.name=projects/*/locations/*/mirroringDeploymentGroups/*}`   
Updates a deployment group.  
  
## REST Resource: [v1.projects.locations.mirroringDeployments](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/create)` |  `POST /v1/{parent=projects/*/locations/*}/mirroringDeployments`   
Creates a deployment in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/mirroringDeployments/*}`   
Deletes a deployment.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/get)` |  `GET /v1/{name=projects/*/locations/*/mirroringDeployments/*}`   
Gets a specific deployment.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/list)` |  `GET /v1/{parent=projects/*/locations/*}/mirroringDeployments`   
Lists deployments in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/patch)` |  `PATCH /v1/{mirroringDeployment.name=projects/*/locations/*/mirroringDeployments/*}`   
Updates a deployment.  
  
## REST Resource: [v1.projects.locations.mirroringEndpointGroupAssociations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations/create)` |  `POST /v1/{parent=projects/*/locations/*}/mirroringEndpointGroupAssociations`   
Creates an association in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/mirroringEndpointGroupAssociations/*}`   
Deletes an association.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations/get)` |  `GET /v1/{name=projects/*/locations/*/mirroringEndpointGroupAssociations/*}`   
Gets a specific association.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations/list)` |  `GET /v1/{parent=projects/*/locations/*}/mirroringEndpointGroupAssociations`   
Lists associations in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroupAssociations/patch)` |  `PATCH /v1/{mirroringEndpointGroupAssociation.name=projects/*/locations/*/mirroringEndpointGroupAssociations/*}`   
Updates an association.  
  
## REST Resource: [v1.projects.locations.mirroringEndpointGroups](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups/create)` |  `POST /v1/{parent=projects/*/locations/*}/mirroringEndpointGroups`   
Creates an endpoint group in a given project and location.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/mirroringEndpointGroups/*}`   
Deletes an endpoint group.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups/get)` |  `GET /v1/{name=projects/*/locations/*/mirroringEndpointGroups/*}`   
Gets a specific endpoint group.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups/list)` |  `GET /v1/{parent=projects/*/locations/*}/mirroringEndpointGroups`   
Lists endpoint groups in a given project and location.  
`[patch](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringEndpointGroups/patch)` |  `PATCH /v1/{mirroringEndpointGroup.name=projects/*/locations/*/mirroringEndpointGroups/*}`   
Updates an endpoint group.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
