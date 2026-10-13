---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/
title: Network Security API \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:20.899239+00:00
---

# Network Security API  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview)



Send feedback 

#  Network Security API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1beta1.organizations.locations.addressGroups
  * REST Resource: v1beta1.organizations.locations.firewallEndpoints
  * REST Resource: v1beta1.organizations.locations.operations
  * REST Resource: v1beta1.organizations.locations.securityProfileGroups
  * REST Resource: v1beta1.organizations.locations.securityProfiles
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.addressGroups
  * REST Resource: v1beta1.projects.locations.authorizationPolicies
  * REST Resource: v1beta1.projects.locations.clientTlsPolicies
  * REST Resource: v1beta1.projects.locations.firewallEndpointAssociations
  * REST Resource: v1beta1.projects.locations.gatewaySecurityPolicies
  * REST Resource: v1beta1.projects.locations.gatewaySecurityPolicies.rules
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta1.projects.locations.serverTlsPolicies
  * REST Resource: v1beta1.projects.locations.tlsInspectionPolicies
  * REST Resource: v1beta1.projects.locations.urlLists



## Service: networksecurity.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networksecurity.googleapis.com`



## REST Resource: [v1beta1.organizations.locations.addressGroups](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups)

Methods  
---  
`[addItems](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/addItems)` |  `POST /v1beta1/{addressGroup=organizations/*/locations/*/addressGroups/*}:addItems`   
Adds items to an address group.  
`[cloneItems](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/cloneItems)` |  `POST /v1beta1/{addressGroup=organizations/*/locations/*/addressGroups/*}:cloneItems`   
Clones items from one address group to another.  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/create)` |  `POST /v1beta1/{parent=organizations/*/locations/*}/addressGroups`   
Creates a new address group in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/addressGroups/*}`   
Deletes an address group.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/addressGroups/*}`   
Gets details of a single address group.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*}/addressGroups`   
Lists address groups in a given project and location.  
`[listReferences](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/listReferences)` |  `GET /v1beta1/{addressGroup=organizations/*/locations/*/addressGroups/*}:listReferences`   
Lists references of an address group.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/patch)` |  `PATCH /v1beta1/{addressGroup.name=organizations/*/locations/*/addressGroups/*}`   
Updates parameters of an address group.  
`[removeItems](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.addressGroups/removeItems)` |  `POST /v1beta1/{addressGroup=organizations/*/locations/*/addressGroups/*}:removeItems`   
Removes items from an address group.  
  
## REST Resource: [v1beta1.organizations.locations.firewallEndpoints](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.firewallEndpoints)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.firewallEndpoints/create)` |  `POST /v1beta1/{parent=organizations/*/locations/*}/firewallEndpoints`   
Creates a new FirewallEndpoint in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.firewallEndpoints/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/firewallEndpoints/*}`   
Deletes a single Endpoint.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.firewallEndpoints/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/firewallEndpoints/*}`   
Gets details of a single Endpoint.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.firewallEndpoints/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*}/firewallEndpoints`   
Lists FirewallEndpoints in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.firewallEndpoints/patch)` |  `PATCH /v1beta1/{firewallEndpoint.name=organizations/*/locations/*/firewallEndpoints/*}`   
Update a single Endpoint.  
  
## REST Resource: [v1beta1.organizations.locations.operations](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.operations/cancel)` |  `POST /v1beta1/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.operations/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.operations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.operations/list)` |  `GET /v1beta1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.organizations.locations.securityProfileGroups](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfileGroups)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfileGroups/create)` |  `POST /v1beta1/{parent=organizations/*/locations/*}/securityProfileGroups`   
Creates a new SecurityProfileGroup in a given organization and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfileGroups/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/securityProfileGroups/*}`   
Deletes a single SecurityProfileGroup.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfileGroups/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/securityProfileGroups/*}`   
Gets details of a single SecurityProfileGroup.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfileGroups/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*}/securityProfileGroups`   
Lists SecurityProfileGroups in a given organization and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfileGroups/patch)` |  `PATCH /v1beta1/{securityProfileGroup.name=organizations/*/locations/*/securityProfileGroups/*}`   
Updates the parameters of a single SecurityProfileGroup.  
  
## REST Resource: [v1beta1.organizations.locations.securityProfiles](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/create)` |  `POST /v1beta1/{parent=organizations/*/locations/*}/securityProfiles`   
Creates a new SecurityProfile in a given organization and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/securityProfiles/*}`   
Deletes a single SecurityProfile.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/securityProfiles/*}`   
Gets details of a single SecurityProfile.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*}/securityProfiles`   
Lists SecurityProfiles in a given organization and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/organizations.locations.securityProfiles/patch)` |  `PATCH /v1beta1/{securityProfile.name=organizations/*/locations/*/securityProfiles/*}`   
Updates the parameters of a single SecurityProfile.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.addressGroups](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups)

Methods  
---  
`[addItems](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/addItems)` |  `POST /v1beta1/{addressGroup=projects/*/locations/*/addressGroups/*}:addItems`   
Adds items to an address group.  
`[cloneItems](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/cloneItems)` |  `POST /v1beta1/{addressGroup=projects/*/locations/*/addressGroups/*}:cloneItems`   
Clones items from one address group to another.  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/addressGroups`   
Creates a new address group in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/addressGroups/*}`   
Deletes a single address group.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/addressGroups/*}`   
Gets details of a single address group.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/addressGroups/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/addressGroups`   
Lists address groups in a given project and location.  
`[listReferences](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/listReferences)` |  `GET /v1beta1/{addressGroup=projects/*/locations/*/addressGroups/*}:listReferences`   
Lists references of an address group.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/patch)` |  `PATCH /v1beta1/{addressGroup.name=projects/*/locations/*/addressGroups/*}`   
Updates the parameters of a single address group.  
`[removeItems](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/removeItems)` |  `POST /v1beta1/{addressGroup=projects/*/locations/*/addressGroups/*}:removeItems`   
Removes items from an address group.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/addressGroups/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.addressGroups/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/addressGroups/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.authorizationPolicies](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/authorizationPolicies`   
Creates a new AuthorizationPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/authorizationPolicies/*}`   
Deletes a single AuthorizationPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/authorizationPolicies/*}`   
Gets details of a single AuthorizationPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/authorizationPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/authorizationPolicies`   
Lists AuthorizationPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/patch)` |  `PATCH /v1beta1/{authorizationPolicy.name=projects/*/locations/*/authorizationPolicies/*}`   
Updates the parameters of a single AuthorizationPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/authorizationPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.authorizationPolicies/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/authorizationPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.clientTlsPolicies](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/clientTlsPolicies`   
Creates a new ClientTlsPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/clientTlsPolicies/*}`   
Deletes a single ClientTlsPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/clientTlsPolicies/*}`   
Gets details of a single ClientTlsPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/clientTlsPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/clientTlsPolicies`   
Lists ClientTlsPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/patch)` |  `PATCH /v1beta1/{clientTlsPolicy.name=projects/*/locations/*/clientTlsPolicies/*}`   
Updates the parameters of a single ClientTlsPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/clientTlsPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.clientTlsPolicies/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/clientTlsPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.firewallEndpointAssociations](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.firewallEndpointAssociations)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.firewallEndpointAssociations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/firewallEndpointAssociations`   
Creates a new FirewallEndpointAssociation in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.firewallEndpointAssociations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/firewallEndpointAssociations/*}`   
Deletes a single FirewallEndpointAssociation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.firewallEndpointAssociations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/firewallEndpointAssociations/*}`   
Gets details of a single FirewallEndpointAssociation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.firewallEndpointAssociations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/firewallEndpointAssociations`   
Lists Associations in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.firewallEndpointAssociations/patch)` |  `PATCH /v1beta1/{firewallEndpointAssociation.name=projects/*/locations/*/firewallEndpointAssociations/*}`   
Update a single FirewallEndpointAssociation.  
  
## REST Resource: [v1beta1.projects.locations.gatewaySecurityPolicies](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/gatewaySecurityPolicies`   
Creates a new GatewaySecurityPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/gatewaySecurityPolicies/*}`   
Deletes a single GatewaySecurityPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/gatewaySecurityPolicies/*}`   
Gets details of a single GatewaySecurityPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/gatewaySecurityPolicies`   
Lists GatewaySecurityPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies/patch)` |  `PATCH /v1beta1/{gatewaySecurityPolicy.name=projects/*/locations/*/gatewaySecurityPolicies/*}`   
Updates the parameters of a single GatewaySecurityPolicy.  
  
## REST Resource: [v1beta1.projects.locations.gatewaySecurityPolicies.rules](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/create)` |  `POST /v1beta1/{parent=projects/*/locations/*/gatewaySecurityPolicies/*}/rules`   
Creates a new GatewaySecurityPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/gatewaySecurityPolicies/*/rules/*}`   
Deletes a single GatewaySecurityPolicyRule.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/get)` |  `GET /v1beta1/{name=projects/*/locations/*/gatewaySecurityPolicies/*/rules/*}`   
Gets details of a single GatewaySecurityPolicyRule.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/gatewaySecurityPolicies/*}/rules`   
Lists GatewaySecurityPolicyRules in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.gatewaySecurityPolicies.rules/patch)` |  `PATCH /v1beta1/{gatewaySecurityPolicyRule.name=projects/*/locations/*/gatewaySecurityPolicies/*/rules/*}`   
Updates the parameters of a single GatewaySecurityPolicyRule.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations.serverTlsPolicies](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/serverTlsPolicies`   
Creates a new ServerTlsPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/serverTlsPolicies/*}`   
Deletes a single ServerTlsPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/serverTlsPolicies/*}`   
Gets details of a single ServerTlsPolicy.  
`[getIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/serverTlsPolicies/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/serverTlsPolicies`   
Lists ServerTlsPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/patch)` |  `PATCH /v1beta1/{serverTlsPolicy.name=projects/*/locations/*/serverTlsPolicies/*}`   
Updates the parameters of a single ServerTlsPolicy.  
`[setIamPolicy](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/serverTlsPolicies/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.serverTlsPolicies/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/serverTlsPolicies/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.tlsInspectionPolicies](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/tlsInspectionPolicies`   
Creates a new TlsInspectionPolicy in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/tlsInspectionPolicies/*}`   
Deletes a single TlsInspectionPolicy.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/tlsInspectionPolicies/*}`   
Gets details of a single TlsInspectionPolicy.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/tlsInspectionPolicies`   
Lists TlsInspectionPolicies in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.tlsInspectionPolicies/patch)` |  `PATCH /v1beta1/{tlsInspectionPolicy.name=projects/*/locations/*/tlsInspectionPolicies/*}`   
Updates the parameters of a single TlsInspectionPolicy.  
  
## REST Resource: [v1beta1.projects.locations.urlLists](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.urlLists)

Methods  
---  
`[create](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.urlLists/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/urlLists`   
Creates a new UrlList in a given project and location.  
`[delete](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.urlLists/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/urlLists/*}`   
Deletes a single UrlList.  
`[get](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.urlLists/get)` |  `GET /v1beta1/{name=projects/*/locations/*/urlLists/*}`   
Gets details of a single UrlList.  
`[list](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.urlLists/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/urlLists`   
Lists UrlLists in a given project and location.  
`[patch](https://docs.cloud.google.com/service-mesh/v1.21/docs/reference/network-security/rest/v1beta1/projects.locations.urlLists/patch)` |  `PATCH /v1beta1/{urlList.name=projects/*/locations/*/urlLists/*}`   
Updates the parameters of a single UrlList.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-20 UTC."],[],[]] 
