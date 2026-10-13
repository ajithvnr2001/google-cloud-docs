---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/
title: Network Services API \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:37.661527+00:00
---

# Network Services API  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/v1.29/docs/apis)



Send feedback 

#  Network Services API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.endpointPolicies
  * REST Resource: v1.projects.locations.gateways
  * REST Resource: v1.projects.locations.gateways.routeViews
  * REST Resource: v1.projects.locations.grpcRoutes
  * REST Resource: v1.projects.locations.httpRoutes
  * REST Resource: v1.projects.locations.meshes
  * REST Resource: v1.projects.locations.meshes.routeViews
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.routeViews
  * REST Resource: v1.projects.locations.serviceLbPolicies
  * REST Resource: v1.projects.locations.tcpRoutes
  * REST Resource: v1.projects.locations.tlsRoutes
  * REST Resource: v1alpha1.projects.locations
  * REST Resource: v1alpha1.projects.locations.agentGateways
  * REST Resource: v1alpha1.projects.locations.gateways
  * REST Resource: v1alpha1.projects.locations.gateways.routeViews
  * REST Resource: v1alpha1.projects.locations.grpcRoutes
  * REST Resource: v1alpha1.projects.locations.httpRoutes
  * REST Resource: v1alpha1.projects.locations.meshes
  * REST Resource: v1alpha1.projects.locations.meshes.routeViews
  * REST Resource: v1alpha1.projects.locations.operations
  * REST Resource: v1alpha1.projects.locations.routeViews
  * REST Resource: v1alpha1.projects.locations.serviceBindings
  * REST Resource: v1alpha1.projects.locations.serviceLbPolicies
  * REST Resource: v1alpha1.projects.locations.tcpRoutes
  * REST Resource: v1alpha1.projects.locations.tlsRoutes
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.endpointPolicies
  * REST Resource: v1beta1.projects.locations.gateways
  * REST Resource: v1beta1.projects.locations.gateways.routeViews
  * REST Resource: v1beta1.projects.locations.grpcRoutes
  * REST Resource: v1beta1.projects.locations.httpRoutes
  * REST Resource: v1beta1.projects.locations.meshes
  * REST Resource: v1beta1.projects.locations.meshes.routeViews
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta1.projects.locations.serviceLbPolicies
  * REST Resource: v1beta1.projects.locations.tcpRoutes
  * REST Resource: v1beta1.projects.locations.tlsRoutes



## Service: networkservices.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://networkservices.googleapis.com/$discovery/rest?version=v1>
  * <https://networkservices.googleapis.com/$discovery/rest?version=v1beta1>
  * <https://networkservices.googleapis.com/$discovery/rest?version=v1alpha1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networkservices.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.endpointPolicies](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/endpointPolicies`   
Creates a new EndpointPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/endpointPolicies/*}`   
Deletes a single EndpointPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/endpointPolicies/*}`   
Gets details of a single EndpointPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/endpointPolicies`   
Lists EndpointPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/patch)` |  `PATCH /v1/{endpointPolicy.name=projects/*/locations/*/endpointPolicies/*}`   
Updates the parameters of a single EndpointPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/endpointPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.endpointPolicies/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/endpointPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.gateways](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/create)` |  `POST /v1/{parent=projects/*/locations/*}/gateways`   
Creates a new Gateway in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/delete)` |  `DELETE /v1/{name=projects/*/locations/*/gateways/*}`   
Deletes a single Gateway.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/get)` |  `GET /v1/{name=projects/*/locations/*/gateways/*}`   
Gets details of a single Gateway.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/list)` |  `GET /v1/{parent=projects/*/locations/*}/gateways`   
Lists Gateways in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/patch)` |  `PATCH /v1/{gateway.name=projects/*/locations/*/gateways/*}`   
Updates the parameters of a single Gateway.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/gateways/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/gateways/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.gateways.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews/get)` |  `GET /v1/{name=projects/*/locations/*/gateways/*/routeViews/*}`   
Get a single RouteView of a Gateway.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways.routeViews/list)` |  `GET /v1/{parent=projects/*/locations/*/gateways/*}/routeViews`   
Lists RouteViews  
  
## REST Resource: [v1.projects.locations.grpcRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/create)` |  `POST /v1/{parent=projects/*/locations/*}/grpcRoutes`   
Creates a new GrpcRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/grpcRoutes/*}`   
Deletes a single GrpcRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/get)` |  `GET /v1/{name=projects/*/locations/*/grpcRoutes/*}`   
Gets details of a single GrpcRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/list)` |  `GET /v1/{parent=projects/*/locations/*}/grpcRoutes`   
Lists GrpcRoutes in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/patch)` |  `PATCH /v1/{grpcRoute.name=projects/*/locations/*/grpcRoutes/*}`   
Updates the parameters of a single GrpcRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/grpcRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/grpcRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.httpRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/create)` |  `POST /v1/{parent=projects/*/locations/*}/httpRoutes`   
Creates a new HttpRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/httpRoutes/*}`   
Deletes a single HttpRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/get)` |  `GET /v1/{name=projects/*/locations/*/httpRoutes/*}`   
Gets details of a single HttpRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/list)` |  `GET /v1/{parent=projects/*/locations/*}/httpRoutes`   
Lists HttpRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/patch)` |  `PATCH /v1/{httpRoute.name=projects/*/locations/*/httpRoutes/*}`   
Updates the parameters of a single HttpRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/httpRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/httpRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.meshes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/create)` |  `POST /v1/{parent=projects/*/locations/*}/meshes`   
Creates a new Mesh in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/meshes/*}`   
Deletes a single Mesh.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/get)` |  `GET /v1/{name=projects/*/locations/*/meshes/*}`   
Gets details of a single Mesh.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/list)` |  `GET /v1/{parent=projects/*/locations/*}/meshes`   
Lists Meshes in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/patch)` |  `PATCH /v1/{mesh.name=projects/*/locations/*/meshes/*}`   
Updates the parameters of a single Mesh.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/meshes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/meshes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.meshes.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes.routeViews)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes.routeViews/get)` |  `GET /v1/{name=projects/*/locations/*/meshes/*/routeViews/*}`   
Get a single RouteView of a Mesh.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes.routeViews/list)` |  `GET /v1/{parent=projects/*/locations/*/meshes/*}/routeViews`   
Lists RouteViews  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.routeViews)

Methods  
---  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.routeViews/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/routeViews/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.routeViews/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/routeViews/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.serviceLbPolicies](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/serviceLbPolicies`   
Creates a new ServiceLbPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/serviceLbPolicies/*}`   
Deletes a single ServiceLbPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/serviceLbPolicies/*}`   
Gets details of a single ServiceLbPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/serviceLbPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/serviceLbPolicies`   
Lists ServiceLbPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/patch)` |  `PATCH /v1/{serviceLbPolicy.name=projects/*/locations/*/serviceLbPolicies/*}`   
Updates the parameters of a single ServiceLbPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/serviceLbPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/serviceLbPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.tcpRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/create)` |  `POST /v1/{parent=projects/*/locations/*}/tcpRoutes`   
Creates a new TcpRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/tcpRoutes/*}`   
Deletes a single TcpRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/get)` |  `GET /v1/{name=projects/*/locations/*/tcpRoutes/*}`   
Gets details of a single TcpRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/list)` |  `GET /v1/{parent=projects/*/locations/*}/tcpRoutes`   
Lists TcpRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/patch)` |  `PATCH /v1/{tcpRoute.name=projects/*/locations/*/tcpRoutes/*}`   
Updates the parameters of a single TcpRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/tcpRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/tcpRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.tlsRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/create)` |  `POST /v1/{parent=projects/*/locations/*}/tlsRoutes`   
Creates a new TlsRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/tlsRoutes/*}`   
Deletes a single TlsRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/get)` |  `GET /v1/{name=projects/*/locations/*/tlsRoutes/*}`   
Gets details of a single TlsRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/list)` |  `GET /v1/{parent=projects/*/locations/*}/tlsRoutes`   
Lists TlsRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/patch)` |  `PATCH /v1/{tlsRoute.name=projects/*/locations/*/tlsRoutes/*}`   
Updates the parameters of a single TlsRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/tlsRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/tlsRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations/list)` |  `GET /v1alpha1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha1.projects.locations.agentGateways](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/agentGateways`   
Creates a new AgentGateway in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/agentGateways/*}`   
Deletes a single AgentGateway.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/agentGateways/*}`   
Gets details of a single AgentGateway.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/agentGateways`   
Lists AgentGateways in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/patch)` |  `PATCH /v1alpha1/{agentGateway.name=projects/*/locations/*/agentGateways/*}`   
Updates the parameters of a single AgentGateway.  
  
## REST Resource: [v1alpha1.projects.locations.gateways](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/gateways`   
Creates a new Gateway in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/gateways/*}`   
Deletes a single Gateway.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/gateways/*}`   
Gets details of a single Gateway.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/gateways/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/gateways`   
Lists Gateways in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/patch)` |  `PATCH /v1alpha1/{gateway.name=projects/*/locations/*/gateways/*}`   
Updates the parameters of a single Gateway.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/gateways/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/gateways/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.gateways.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways.routeViews)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways.routeViews/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/gateways/*/routeViews/*}`   
Get a single RouteView of a Gateway.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.gateways.routeViews/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/gateways/*}/routeViews`   
Lists RouteViews  
  
## REST Resource: [v1alpha1.projects.locations.grpcRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/grpcRoutes`   
Creates a new GrpcRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/grpcRoutes/*}`   
Deletes a single GrpcRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/grpcRoutes/*}`   
Gets details of a single GrpcRoute.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/grpcRoutes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/grpcRoutes`   
Lists GrpcRoutes in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/patch)` |  `PATCH /v1alpha1/{grpcRoute.name=projects/*/locations/*/grpcRoutes/*}`   
Updates the parameters of a single GrpcRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/grpcRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.grpcRoutes/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/grpcRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.httpRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/httpRoutes`   
Creates a new HttpRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/httpRoutes/*}`   
Deletes a single HttpRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/httpRoutes/*}`   
Gets details of a single HttpRoute.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/httpRoutes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/httpRoutes`   
Lists HttpRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/patch)` |  `PATCH /v1alpha1/{httpRoute.name=projects/*/locations/*/httpRoutes/*}`   
Updates the parameters of a single HttpRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/httpRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.httpRoutes/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/httpRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.meshes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/meshes`   
Creates a new Mesh in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/meshes/*}`   
Deletes a single Mesh.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/meshes/*}`   
Gets details of a single Mesh.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/meshes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/meshes`   
Lists Meshes in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/patch)` |  `PATCH /v1alpha1/{mesh.name=projects/*/locations/*/meshes/*}`   
Updates the parameters of a single Mesh.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/meshes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/meshes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.meshes.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes.routeViews)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes.routeViews/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/meshes/*/routeViews/*}`   
Get a single RouteView of a Mesh.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.meshes.routeViews/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/meshes/*}/routeViews`   
Lists RouteViews  
  
## REST Resource: [v1alpha1.projects.locations.operations](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.operations/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.operations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.operations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.operations/list)` |  `GET /v1alpha1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha1.projects.locations.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.routeViews)

Methods  
---  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.routeViews/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/routeViews/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.routeViews/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/routeViews/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.routeViews/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/routeViews/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.serviceBindings](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/serviceBindings`   
Creates a new ServiceBinding in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/serviceBindings/*}`   
Deletes a single ServiceBinding.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/serviceBindings/*}`   
Gets details of a single ServiceBinding.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceBindings/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/serviceBindings`   
Lists ServiceBinding in a given project and location.  
  
## REST Resource: [v1alpha1.projects.locations.serviceLbPolicies](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/serviceLbPolicies`   
Creates a new ServiceLbPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/serviceLbPolicies/*}`   
Deletes a single ServiceLbPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/serviceLbPolicies/*}`   
Gets details of a single ServiceLbPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/serviceLbPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/serviceLbPolicies`   
Lists ServiceLbPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/patch)` |  `PATCH /v1alpha1/{serviceLbPolicy.name=projects/*/locations/*/serviceLbPolicies/*}`   
Updates the parameters of a single ServiceLbPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/serviceLbPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.serviceLbPolicies/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/serviceLbPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.tcpRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/tcpRoutes`   
Creates a new TcpRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/tcpRoutes/*}`   
Deletes a single TcpRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/tcpRoutes/*}`   
Gets details of a single TcpRoute.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/tcpRoutes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/tcpRoutes`   
Lists TcpRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/patch)` |  `PATCH /v1alpha1/{tcpRoute.name=projects/*/locations/*/tcpRoutes/*}`   
Updates the parameters of a single TcpRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/tcpRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tcpRoutes/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/tcpRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha1.projects.locations.tlsRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/tlsRoutes`   
Creates a new TlsRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/tlsRoutes/*}`   
Deletes a single TlsRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/tlsRoutes/*}`   
Gets details of a single TlsRoute.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/getIamPolicy)` |  `GET /v1alpha1/{resource=projects/*/locations/*/tlsRoutes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/tlsRoutes`   
Lists TlsRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/patch)` |  `PATCH /v1alpha1/{tlsRoute.name=projects/*/locations/*/tlsRoutes/*}`   
Updates the parameters of a single TlsRoute.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/setIamPolicy)` |  `POST /v1alpha1/{resource=projects/*/locations/*/tlsRoutes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1alpha1/projects.locations.tlsRoutes/testIamPermissions)` |  `POST /v1alpha1/{resource=projects/*/locations/*/tlsRoutes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.endpointPolicies](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/endpointPolicies`   
Creates a new EndpointPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/endpointPolicies/*}`   
Deletes a single EndpointPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/endpointPolicies/*}`   
Gets details of a single EndpointPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/endpointPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/endpointPolicies`   
Lists EndpointPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/patch)` |  `PATCH /v1beta1/{endpointPolicy.name=projects/*/locations/*/endpointPolicies/*}`   
Updates the parameters of a single EndpointPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/endpointPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.endpointPolicies/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/endpointPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.gateways](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/gateways`   
Creates a new Gateway in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/gateways/*}`   
Deletes a single Gateway.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways/get)` |  `GET /v1beta1/{name=projects/*/locations/*/gateways/*}`   
Gets details of a single Gateway.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/gateways`   
Lists Gateways in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways/patch)` |  `PATCH /v1beta1/{gateway.name=projects/*/locations/*/gateways/*}`   
Updates the parameters of a single Gateway.  
  
## REST Resource: [v1beta1.projects.locations.gateways.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways.routeViews)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways.routeViews/get)` |  `GET /v1beta1/{name=projects/*/locations/*/gateways/*/routeViews/*}`   
Get a single RouteView of a Gateway.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.gateways.routeViews/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/gateways/*}/routeViews`   
Lists RouteViews  
  
## REST Resource: [v1beta1.projects.locations.grpcRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/grpcRoutes`   
Creates a new GrpcRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/grpcRoutes/*}`   
Deletes a single GrpcRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes/get)` |  `GET /v1beta1/{name=projects/*/locations/*/grpcRoutes/*}`   
Gets details of a single GrpcRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/grpcRoutes`   
Lists GrpcRoutes in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.grpcRoutes/patch)` |  `PATCH /v1beta1/{grpcRoute.name=projects/*/locations/*/grpcRoutes/*}`   
Updates the parameters of a single GrpcRoute.  
  
## REST Resource: [v1beta1.projects.locations.httpRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/httpRoutes`   
Creates a new HttpRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/httpRoutes/*}`   
Deletes a single HttpRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/get)` |  `GET /v1beta1/{name=projects/*/locations/*/httpRoutes/*}`   
Gets details of a single HttpRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/httpRoutes`   
Lists HttpRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.httpRoutes/patch)` |  `PATCH /v1beta1/{httpRoute.name=projects/*/locations/*/httpRoutes/*}`   
Updates the parameters of a single HttpRoute.  
  
## REST Resource: [v1beta1.projects.locations.meshes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/meshes`   
Creates a new Mesh in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/meshes/*}`   
Deletes a single Mesh.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes/get)` |  `GET /v1beta1/{name=projects/*/locations/*/meshes/*}`   
Gets details of a single Mesh.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/meshes`   
Lists Meshes in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes/patch)` |  `PATCH /v1beta1/{mesh.name=projects/*/locations/*/meshes/*}`   
Updates the parameters of a single Mesh.  
  
## REST Resource: [v1beta1.projects.locations.meshes.routeViews](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes.routeViews)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes.routeViews/get)` |  `GET /v1beta1/{name=projects/*/locations/*/meshes/*/routeViews/*}`   
Get a single RouteView of a Mesh.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.meshes.routeViews/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/meshes/*}/routeViews`   
Lists RouteViews  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.serviceLbPolicies](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/serviceLbPolicies`   
Creates a new ServiceLbPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/serviceLbPolicies/*}`   
Deletes a single ServiceLbPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/serviceLbPolicies/*}`   
Gets details of a single ServiceLbPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/serviceLbPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/serviceLbPolicies`   
Lists ServiceLbPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/patch)` |  `PATCH /v1beta1/{serviceLbPolicy.name=projects/*/locations/*/serviceLbPolicies/*}`   
Updates the parameters of a single ServiceLbPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/serviceLbPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.serviceLbPolicies/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/serviceLbPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.tcpRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/tcpRoutes`   
Creates a new TcpRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/tcpRoutes/*}`   
Deletes a single TcpRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes/get)` |  `GET /v1beta1/{name=projects/*/locations/*/tcpRoutes/*}`   
Gets details of a single TcpRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/tcpRoutes`   
Lists TcpRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tcpRoutes/patch)` |  `PATCH /v1beta1/{tcpRoute.name=projects/*/locations/*/tcpRoutes/*}`   
Updates the parameters of a single TcpRoute.  
  
## REST Resource: [v1beta1.projects.locations.tlsRoutes](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/tlsRoutes`   
Creates a new TlsRoute in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/tlsRoutes/*}`   
Deletes a single TlsRoute.  
`[get](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes/get)` |  `GET /v1beta1/{name=projects/*/locations/*/tlsRoutes/*}`   
Gets details of a single TlsRoute.  
`[list](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/tlsRoutes`   
Lists TlsRoute in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1beta1/projects.locations.tlsRoutes/patch)` |  `PATCH /v1beta1/{tlsRoute.name=projects/*/locations/*/tlsRoutes/*}`   
Updates the parameters of a single TlsRoute.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
