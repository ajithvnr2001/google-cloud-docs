---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/
title: GKE Hub API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:05:54.139171+00:00
---

# GKE Hub API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  GKE Hub API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v2beta.projects.locations
  * REST Resource: v2beta.projects.locations.memberships.features
  * REST Resource: v2beta.projects.locations.operations
  * REST Resource: v2alpha.projects.locations
  * REST Resource: v2alpha.projects.locations.memberships.features
  * REST Resource: v2alpha.projects.locations.operations
  * REST Resource: v2.projects.locations
  * REST Resource: v2.projects.locations.memberships.features
  * REST Resource: v2.projects.locations.operations
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.memberships
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1beta.organizations.locations.fleets
  * REST Resource: v1beta.projects.locations
  * REST Resource: v1beta.projects.locations.features
  * REST Resource: v1beta.projects.locations.fleets
  * REST Resource: v1beta.projects.locations.memberships
  * REST Resource: v1beta.projects.locations.memberships.bindings
  * REST Resource: v1beta.projects.locations.memberships.rbacrolebindings
  * REST Resource: v1beta.projects.locations.operations
  * REST Resource: v1beta.projects.locations.rolloutSequences
  * REST Resource: v1beta.projects.locations.rollouts
  * REST Resource: v1beta.projects.locations.scopes
  * REST Resource: v1beta.projects.locations.scopes.namespaces
  * REST Resource: v1beta.projects.locations.scopes.rbacrolebindings
  * REST Resource: v1alpha.organizations.locations.fleets
  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.features
  * REST Resource: v1alpha.projects.locations.fleets
  * REST Resource: v1alpha.projects.locations.memberships
  * REST Resource: v1alpha.projects.locations.memberships.bindings
  * REST Resource: v1alpha.projects.locations.memberships.rbacrolebindings
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.rolloutSequences
  * REST Resource: v1alpha.projects.locations.rollouts
  * REST Resource: v1alpha.projects.locations.scopes
  * REST Resource: v1alpha.projects.locations.scopes.namespaces
  * REST Resource: v1alpha.projects.locations.scopes.rbacrolebindings
  * REST Resource: v1.organizations.locations.fleets
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.features
  * REST Resource: v1.projects.locations.fleets
  * REST Resource: v1.projects.locations.memberships
  * REST Resource: v1.projects.locations.memberships.bindings
  * REST Resource: v1.projects.locations.memberships.rbacrolebindings
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.scopes
  * REST Resource: v1.projects.locations.scopes.namespaces
  * REST Resource: v1.projects.locations.scopes.rbacrolebindings



## Service: gkehub.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://gkehub.googleapis.com/$discovery/rest?version=v2>
  * <https://gkehub.googleapis.com/$discovery/rest?version=v2beta>
  * <https://gkehub.googleapis.com/$discovery/rest?version=v2alpha>
  * <https://gkehub.googleapis.com/$discovery/rest?version=v1>
  * <https://gkehub.googleapis.com/$discovery/rest?version=v1beta1>
  * <https://gkehub.googleapis.com/$discovery/rest?version=v1beta>
  * <https://gkehub.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://gkehub.googleapis.com`



## REST Resource: [v2beta.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations/get)` |  `GET /v2beta/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations/list)` |  `GET /v2beta/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v2beta.projects.locations.memberships.features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.memberships.features)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.memberships.features/create)` |  `POST /v2beta/{parent=projects/*/locations/*/memberships/*}/features`   
Creates membershipFeature under a given parent.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.memberships.features/delete)` |  `DELETE /v2beta/{name=projects/*/locations/*/memberships/*/features/*}`   
Removes a membershipFeature.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.memberships.features/get)` |  `GET /v2beta/{name=projects/*/locations/*/memberships/*/features/*}`   
========= MembershipFeature Services ========= Gets details of a membershipFeature.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.memberships.features/list)` |  `GET /v2beta/{parent=projects/*/locations/*/memberships/*}/features`   
Lists MembershipFeatures in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.memberships.features/patch)` |  `PATCH /v2beta/{membershipFeature.name=projects/*/locations/*/memberships/*/features/*}`   
Updates an existing MembershipFeature.  
  
## REST Resource: [v2beta.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.operations/cancel)` |  `POST /v2beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.operations/get)` |  `GET /v2beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2beta/projects.locations.operations/list)` |  `GET /v2beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2alpha.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations/get)` |  `GET /v2alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations/list)` |  `GET /v2alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v2alpha.projects.locations.memberships.features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.memberships.features)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.memberships.features/create)` |  `POST /v2alpha/{parent=projects/*/locations/*/memberships/*}/features`   
Creates membershipFeature under a given parent.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.memberships.features/delete)` |  `DELETE /v2alpha/{name=projects/*/locations/*/memberships/*/features/*}`   
Removes a membershipFeature.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.memberships.features/get)` |  `GET /v2alpha/{name=projects/*/locations/*/memberships/*/features/*}`   
========= MembershipFeature Services ========= Gets details of a membershipFeature.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.memberships.features/list)` |  `GET /v2alpha/{parent=projects/*/locations/*/memberships/*}/features`   
Lists MembershipFeatures in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.memberships.features/patch)` |  `PATCH /v2alpha/{membershipFeature.name=projects/*/locations/*/memberships/*/features/*}`   
Updates an existing MembershipFeature.  
  
## REST Resource: [v2alpha.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.operations/cancel)` |  `POST /v2alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.operations/get)` |  `GET /v2alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2alpha/projects.locations.operations/list)` |  `GET /v2alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations/get)` |  `GET /v2/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations/list)` |  `GET /v2/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v2.projects.locations.memberships.features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features/create)` |  `POST /v2/{parent=projects/*/locations/*/memberships/*}/features`   
Creates membershipFeature under a given parent.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features/delete)` |  `DELETE /v2/{name=projects/*/locations/*/memberships/*/features/*}`   
Removes a membershipFeature.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features/get)` |  `GET /v2/{name=projects/*/locations/*/memberships/*/features/*}`   
========= MembershipFeature Services ========= Gets details of a membershipFeature.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features/list)` |  `GET /v2/{parent=projects/*/locations/*/memberships/*}/features`   
Lists MembershipFeatures in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.memberships.features/patch)` |  `PATCH /v2/{membershipFeature.name=projects/*/locations/*/memberships/*/features/*}`   
Updates an existing MembershipFeature.  
  
## REST Resource: [v2.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.operations/cancel)` |  `POST /v2/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.operations/get)` |  `GET /v2/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v2/projects.locations.operations/list)` |  `GET /v2/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.memberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/memberships`   
Creates a new Membership.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/memberships/*}`   
Removes a Membership.  
`[generateConnectManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/generateConnectManifest)` |  `GET /v1beta1/{name=projects/*/locations/*/memberships/*}:generateConnectManifest`   
Generates the manifest for deployment of the GKE connect agent.  
`[generateExclusivityManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/generateExclusivityManifest)` |  `GET /v1beta1/{name=projects/*/locations/*/memberships/*}:generateExclusivityManifest`   
GenerateExclusivityManifest generates the manifests to update the exclusivity artifacts in the cluster if needed.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/get)` |  `GET /v1beta1/{name=projects/*/locations/*/memberships/*}`   
Gets the details of a Membership.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/getIamPolicy)` |  `GET /v1beta1/{resource=projects/*/locations/*/memberships/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/memberships`   
Lists Memberships in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/patch)` |  `PATCH /v1beta1/{name=projects/*/locations/*/memberships/*}`   
Updates an existing Membership.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/setIamPolicy)` |  `POST /v1beta1/{resource=projects/*/locations/*/memberships/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/testIamPermissions)` |  `POST /v1beta1/{resource=projects/*/locations/*/memberships/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[validateExclusivity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.memberships/validateExclusivity)` |  `GET /v1beta1/{parent=projects/*/locations/*}/memberships:validateExclusivity`   
ValidateExclusivity validates the state of exclusivity in the cluster.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.organizations.locations.fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/organizations.locations.fleets)

Methods  
---  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/organizations.locations.fleets/list)` |  `GET /v1beta/{parent=organizations/*/locations/*}/fleets`   
Returns all fleets within an organization or a project that the caller has access to.  
  
## REST Resource: [v1beta.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations/get)` |  `GET /v1beta/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations/list)` |  `GET /v1beta/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta.projects.locations.features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/features`   
Adds a new Feature.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/features/*}`   
Removes a Feature.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/get)` |  `GET /v1beta/{name=projects/*/locations/*/features/*}`   
Gets details of a single Feature.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/getIamPolicy)` |  `GET /v1beta/{resource=projects/*/locations/*/features/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/features`   
Lists Features in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/patch)` |  `PATCH /v1beta/{name=projects/*/locations/*/features/*}`   
Updates an existing Feature.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/setIamPolicy)` |  `POST /v1beta/{resource=projects/*/locations/*/features/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/testIamPermissions)` |  `POST /v1beta/{resource=projects/*/locations/*/features/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta.projects.locations.fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.fleets)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.fleets/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/fleets`   
Creates a fleet.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.fleets/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/fleets/*}`   
Removes a Fleet.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.fleets/get)` |  `GET /v1beta/{name=projects/*/locations/*/fleets/*}`   
Returns the details of a fleet.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.fleets/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/fleets`   
Returns all fleets within an organization or a project that the caller has access to.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.fleets/patch)` |  `PATCH /v1beta/{fleet.name=projects/*/locations/*/fleets/*}`   
Updates a fleet.  
  
## REST Resource: [v1beta.projects.locations.memberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/memberships`   
Creates a new Membership.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/memberships/*}`   
Removes a Membership.  
`[generateConnectManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/generateConnectManifest)` |  `GET /v1beta/{name=projects/*/locations/*/memberships/*}:generateConnectManifest`   
Generates the manifest for deployment of the GKE connect agent.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/get)` |  `GET /v1beta/{name=projects/*/locations/*/memberships/*}`   
Gets the details of a Membership.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/getIamPolicy)` |  `GET /v1beta/{resource=projects/*/locations/*/memberships/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/memberships`   
Lists Memberships in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/patch)` |  `PATCH /v1beta/{name=projects/*/locations/*/memberships/*}`   
Updates an existing Membership.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/setIamPolicy)` |  `POST /v1beta/{resource=projects/*/locations/*/memberships/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships/testIamPermissions)` |  `POST /v1beta/{resource=projects/*/locations/*/memberships/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta.projects.locations.memberships.bindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.bindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.bindings/create)` |  `POST /v1beta/{parent=projects/*/locations/*/memberships/*}/bindings`   
Creates a MembershipBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.bindings/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/memberships/*/bindings/*}`   
Deletes a MembershipBinding.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.bindings/get)` |  `GET /v1beta/{name=projects/*/locations/*/memberships/*/bindings/*}`   
Returns the details of a MembershipBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.bindings/list)` |  `GET /v1beta/{parent=projects/*/locations/*/memberships/*}/bindings`   
Lists MembershipBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.bindings/patch)` |  `PATCH /v1beta/{membershipBinding.name=projects/*/locations/*/memberships/*/bindings/*}`   
Updates a MembershipBinding.  
  
## REST Resource: [v1beta.projects.locations.memberships.rbacrolebindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings/create)` |  `POST /v1beta/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`   
Creates a Membership RBACRoleBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Deletes a Membership RBACRoleBinding.  
`[generateMembershipRBACRoleBindingYAML](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings/generateMembershipRBACRoleBindingYAML)` |  `POST /v1beta/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings:generateMembershipRBACRoleBindingYAML`   
Generates a YAML of the RBAC policies for the specified RoleBinding and its associated impersonation resources.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings/get)` |  `GET /v1beta/{name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Returns the details of a Membership RBACRoleBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings/list)` |  `GET /v1beta/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`   
Lists all Membership RBACRoleBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.memberships.rbacrolebindings/patch)` |  `PATCH /v1beta/{rbacrolebinding.name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Updates a Membership RBACRoleBinding.  
  
## REST Resource: [v1beta.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.operations/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.operations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.operations/list)` |  `GET /v1beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.projects.locations.rolloutSequences](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/rolloutSequences`   
Create a new rollout sequence resource.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/rolloutSequences/*}`   
Remove a RolloutSequence.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/get)` |  `GET /v1beta/{name=projects/*/locations/*/rolloutSequences/*}`   
Retrieve a single rollout sequence.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/rolloutSequences`   
Retrieve the list of all rollout sequences.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/patch)` |  `PATCH /v1beta/{rolloutSequence.name=projects/*/locations/*/rolloutSequences/*}`   
Update a rollout sequence.  
  
## REST Resource: [v1beta.projects.locations.rollouts](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rollouts)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rollouts/get)` |  `GET /v1beta/{name=projects/*/locations/*/rollouts/*}`   
Retrieve a single rollout.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rollouts/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/rollouts`   
Retrieve the list of all rollouts.  
  
## REST Resource: [v1beta.projects.locations.scopes](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/scopes`   
Creates a Scope.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/scopes/*}`   
Deletes a Scope.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/get)` |  `GET /v1beta/{name=projects/*/locations/*/scopes/*}`   
Returns the details of a Scope.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/getIamPolicy)` |  `GET /v1beta/{resource=projects/*/locations/*/scopes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/scopes`   
Lists Scopes.  
`[listMemberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/listMemberships)` |  `GET /v1beta/{scopeName=projects/*/locations/*/scopes/*}:listMemberships`   
Lists Memberships bound to a Scope.  
`[listPermitted](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/listPermitted)` |  `GET /v1beta/{parent=projects/*/locations/*}/scopes:listPermitted`   
Lists permitted Scopes.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/patch)` |  `PATCH /v1beta/{scope.name=projects/*/locations/*/scopes/*}`   
Updates a scopes.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/setIamPolicy)` |  `POST /v1beta/{resource=projects/*/locations/*/scopes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes/testIamPermissions)` |  `POST /v1beta/{resource=projects/*/locations/*/scopes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta.projects.locations.scopes.namespaces](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.namespaces)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.namespaces/create)` |  `POST /v1beta/{parent=projects/*/locations/*/scopes/*}/namespaces`   
Creates a fleet namespace.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.namespaces/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/scopes/*/namespaces/*}`   
Deletes a fleet namespace.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.namespaces/get)` |  `GET /v1beta/{name=projects/*/locations/*/scopes/*/namespaces/*}`   
Returns the details of a fleet namespace.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.namespaces/list)` |  `GET /v1beta/{parent=projects/*/locations/*/scopes/*}/namespaces`   
Lists fleet namespaces.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.namespaces/patch)` |  `PATCH /v1beta/{scopeNamespace.name=projects/*/locations/*/scopes/*/namespaces/*}`   
Updates a fleet namespace.  
  
## REST Resource: [v1beta.projects.locations.scopes.rbacrolebindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.rbacrolebindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.rbacrolebindings/create)` |  `POST /v1beta/{parent=projects/*/locations/*/scopes/*}/rbacrolebindings`   
Creates a Scope RBACRoleBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.rbacrolebindings/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Deletes a Scope RBACRoleBinding.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.rbacrolebindings/get)` |  `GET /v1beta/{name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Returns the details of a Scope RBACRoleBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.rbacrolebindings/list)` |  `GET /v1beta/{parent=projects/*/locations/*/scopes/*}/rbacrolebindings`   
Lists all Scope RBACRoleBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.scopes.rbacrolebindings/patch)` |  `PATCH /v1beta/{rbacrolebinding.name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Updates a Scope RBACRoleBinding.  
  
## REST Resource: [v1alpha.organizations.locations.fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/organizations.locations.fleets)

Methods  
---  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/organizations.locations.fleets/list)` |  `GET /v1alpha/{parent=organizations/*/locations/*}/fleets`   
Returns all fleets within an organization or a project that the caller has access to.  
  
## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/features`   
Adds a new Feature.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/features/*}`   
Removes a Feature.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/get)` |  `GET /v1alpha/{name=projects/*/locations/*/features/*}`   
Gets details of a single Feature.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/features/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/features`   
Lists Features in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/patch)` |  `PATCH /v1alpha/{name=projects/*/locations/*/features/*}`   
Updates an existing Feature.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/features/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.features/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/features/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha.projects.locations.fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/fleets`   
Creates a fleet.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/fleets/*}`   
Removes a Fleet.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/get)` |  `GET /v1alpha/{name=projects/*/locations/*/fleets/*}`   
Returns the details of a fleet.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/fleets`   
Returns all fleets within an organization or a project that the caller has access to.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/patch)` |  `PATCH /v1alpha/{fleet.name=projects/*/locations/*/fleets/*}`   
Updates a fleet.  
  
## REST Resource: [v1alpha.projects.locations.memberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/memberships`   
Creates a new Membership.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/memberships/*}`   
Removes a Membership.  
`[generateConnectManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/generateConnectManifest)` |  `GET /v1alpha/{name=projects/*/locations/*/memberships/*}:generateConnectManifest`   
Generates the manifest for deployment of the GKE connect agent.  
`[generateExclusivityManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/generateExclusivityManifest)` |  `GET /v1alpha/{name=projects/*/locations/*/memberships/*}:generateExclusivityManifest`   
GenerateExclusivityManifest generates the manifests to update the exclusivity artifacts in the cluster if needed.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/get)` |  `GET /v1alpha/{name=projects/*/locations/*/memberships/*}`   
Gets the details of a Membership.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/memberships/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/memberships`   
Lists Memberships in a given project and location.  
`[listAdmin](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/listAdmin)` |  `GET /v1alpha/{parent=projects/*/locations/*}/memberships:listAdmin`   
Lists Memberships of admin clusters in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/patch)` |  `PATCH /v1alpha/{name=projects/*/locations/*/memberships/*}`   
Updates an existing Membership.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/memberships/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/memberships/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[validateCreate](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateCreate)` |  `POST /v1alpha/{parent=projects/*/locations/*}/memberships:validateCreate`   
ValidateCreateMembership is a preflight check for CreateMembership.  
`[validateExclusivity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships/validateExclusivity)` |  `GET /v1alpha/{parent=projects/*/locations/*}/memberships:validateExclusivity`   
ValidateExclusivity validates the state of exclusivity in the cluster.  
  
## REST Resource: [v1alpha.projects.locations.memberships.bindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/memberships/*}/bindings`   
Creates a MembershipBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/memberships/*/bindings/*}`   
Deletes a MembershipBinding.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/get)` |  `GET /v1alpha/{name=projects/*/locations/*/memberships/*/bindings/*}`   
Returns the details of a MembershipBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/memberships/*}/bindings`   
Lists MembershipBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.bindings/patch)` |  `PATCH /v1alpha/{membershipBinding.name=projects/*/locations/*/memberships/*/bindings/*}`   
Updates a MembershipBinding.  
  
## REST Resource: [v1alpha.projects.locations.memberships.rbacrolebindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`   
Creates a Membership RBACRoleBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Deletes a Membership RBACRoleBinding.  
`[generateMembershipRBACRoleBindingYAML](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/generateMembershipRBACRoleBindingYAML)` |  `POST /v1alpha/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings:generateMembershipRBACRoleBindingYAML`   
Generates a YAML of the RBAC policies for the specified RoleBinding and its associated impersonation resources.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/get)` |  `GET /v1alpha/{name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Returns the details of a Membership RBACRoleBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`   
Lists all Membership RBACRoleBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships.rbacrolebindings/patch)` |  `PATCH /v1alpha/{rbacrolebinding.name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Updates a Membership RBACRoleBinding.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.rolloutSequences](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/rolloutSequences`   
Create a new rollout sequence resource.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/rolloutSequences/*}`   
Remove a RolloutSequence.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/get)` |  `GET /v1alpha/{name=projects/*/locations/*/rolloutSequences/*}`   
Retrieve a single rollout sequence.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/rolloutSequences`   
Retrieve the list of all rollout sequences.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/patch)` |  `PATCH /v1alpha/{rolloutSequence.name=projects/*/locations/*/rolloutSequences/*}`   
Update a rollout sequence.  
  
## REST Resource: [v1alpha.projects.locations.rollouts](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts/get)` |  `GET /v1alpha/{name=projects/*/locations/*/rollouts/*}`   
Retrieve a single rollout.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/rollouts`   
Retrieve the list of all rollouts.  
  
## REST Resource: [v1alpha.projects.locations.scopes](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/scopes`   
Creates a Scope.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/scopes/*}`   
Deletes a Scope.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/get)` |  `GET /v1alpha/{name=projects/*/locations/*/scopes/*}`   
Returns the details of a Scope.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/scopes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/scopes`   
Lists Scopes.  
`[listMemberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/listMemberships)` |  `GET /v1alpha/{scopeName=projects/*/locations/*/scopes/*}:listMemberships`   
Lists Memberships bound to a Scope.  
`[listPermitted](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/listPermitted)` |  `GET /v1alpha/{parent=projects/*/locations/*}/scopes:listPermitted`   
Lists permitted Scopes.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/patch)` |  `PATCH /v1alpha/{scope.name=projects/*/locations/*/scopes/*}`   
Updates a scopes.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/scopes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/scopes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha.projects.locations.scopes.namespaces](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/scopes/*}/namespaces`   
Creates a fleet namespace.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/scopes/*/namespaces/*}`   
Deletes a fleet namespace.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/get)` |  `GET /v1alpha/{name=projects/*/locations/*/scopes/*/namespaces/*}`   
Returns the details of a fleet namespace.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/scopes/*}/namespaces`   
Lists fleet namespaces.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.namespaces/patch)` |  `PATCH /v1alpha/{scopeNamespace.name=projects/*/locations/*/scopes/*/namespaces/*}`   
Updates a fleet namespace.  
  
## REST Resource: [v1alpha.projects.locations.scopes.rbacrolebindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.rbacrolebindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.rbacrolebindings/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/scopes/*}/rbacrolebindings`   
Creates a Scope RBACRoleBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.rbacrolebindings/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Deletes a Scope RBACRoleBinding.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.rbacrolebindings/get)` |  `GET /v1alpha/{name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Returns the details of a Scope RBACRoleBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.rbacrolebindings/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/scopes/*}/rbacrolebindings`   
Lists all Scope RBACRoleBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes.rbacrolebindings/patch)` |  `PATCH /v1alpha/{rbacrolebinding.name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Updates a Scope RBACRoleBinding.  
  
## REST Resource: [v1.organizations.locations.fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/organizations.locations.fleets)

Methods  
---  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/organizations.locations.fleets/list)` |  `GET /v1/{parent=organizations/*/locations/*}/fleets`   
Returns all fleets within an organization or a project that the caller has access to.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/create)` |  `POST /v1/{parent=projects/*/locations/*}/features`   
Adds a new Feature.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/delete)` |  `DELETE /v1/{name=projects/*/locations/*/features/*}`   
Removes a Feature.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/get)` |  `GET /v1/{name=projects/*/locations/*/features/*}`   
Gets details of a single Feature.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/features/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/list)` |  `GET /v1/{parent=projects/*/locations/*}/features`   
Lists Features in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/patch)` |  `PATCH /v1/{name=projects/*/locations/*/features/*}`   
Updates an existing Feature.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/features/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.features/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/features/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.fleets](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/create)` |  `POST /v1/{parent=projects/*/locations/*}/fleets`   
Creates a fleet.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/fleets/*}`   
Removes a Fleet.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/get)` |  `GET /v1/{name=projects/*/locations/*/fleets/*}`   
Returns the details of a fleet.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/list)` |  `GET /v1/{parent=projects/*/locations/*}/fleets`   
Returns all fleets within an organization or a project that the caller has access to.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.fleets/patch)` |  `PATCH /v1/{fleet.name=projects/*/locations/*/fleets/*}`   
Updates a fleet.  
  
## REST Resource: [v1.projects.locations.memberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/create)` |  `POST /v1/{parent=projects/*/locations/*}/memberships`   
Creates a new Membership.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/delete)` |  `DELETE /v1/{name=projects/*/locations/*/memberships/*}`   
Removes a Membership.  
`[generateConnectManifest](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/generateConnectManifest)` |  `GET /v1/{name=projects/*/locations/*/memberships/*}:generateConnectManifest`   
Generates the manifest for deployment of the GKE connect agent.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/get)` |  `GET /v1/{name=projects/*/locations/*/memberships/*}`   
Gets the details of a Membership.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/memberships/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/list)` |  `GET /v1/{parent=projects/*/locations/*}/memberships`   
Lists Memberships in a given project and location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/patch)` |  `PATCH /v1/{name=projects/*/locations/*/memberships/*}`   
Updates an existing Membership.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/memberships/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/memberships/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.memberships.bindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings/create)` |  `POST /v1/{parent=projects/*/locations/*/memberships/*}/bindings`   
Creates a MembershipBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/memberships/*/bindings/*}`   
Deletes a MembershipBinding.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings/get)` |  `GET /v1/{name=projects/*/locations/*/memberships/*/bindings/*}`   
Returns the details of a MembershipBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings/list)` |  `GET /v1/{parent=projects/*/locations/*/memberships/*}/bindings`   
Lists MembershipBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.bindings/patch)` |  `PATCH /v1/{membershipBinding.name=projects/*/locations/*/memberships/*/bindings/*}`   
Updates a MembershipBinding.  
  
## REST Resource: [v1.projects.locations.memberships.rbacrolebindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/create)` |  `POST /v1/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`   
Creates a Membership RBACRoleBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Deletes a Membership RBACRoleBinding.  
`[generateMembershipRBACRoleBindingYAML](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/generateMembershipRBACRoleBindingYAML)` |  `POST /v1/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings:generateMembershipRBACRoleBindingYAML`   
Generates a YAML of the RBAC policies for the specified RoleBinding and its associated impersonation resources.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/get)` |  `GET /v1/{name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Returns the details of a Membership RBACRoleBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/list)` |  `GET /v1/{parent=projects/*/locations/*/memberships/*}/rbacrolebindings`   
Lists all Membership RBACRoleBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.memberships.rbacrolebindings/patch)` |  `PATCH /v1/{rbacrolebinding.name=projects/*/locations/*/memberships/*/rbacrolebindings/*}`   
Updates a Membership RBACRoleBinding.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.scopes](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/create)` |  `POST /v1/{parent=projects/*/locations/*}/scopes`   
Creates a Scope.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/delete)` |  `DELETE /v1/{name=projects/*/locations/*/scopes/*}`   
Deletes a Scope.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/get)` |  `GET /v1/{name=projects/*/locations/*/scopes/*}`   
Returns the details of a Scope.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/scopes/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/list)` |  `GET /v1/{parent=projects/*/locations/*}/scopes`   
Lists Scopes.  
`[listMemberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/listMemberships)` |  `GET /v1/{scopeName=projects/*/locations/*/scopes/*}:listMemberships`   
Lists Memberships bound to a Scope.  
`[listPermitted](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/listPermitted)` |  `GET /v1/{parent=projects/*/locations/*}/scopes:listPermitted`   
Lists permitted Scopes.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/patch)` |  `PATCH /v1/{scope.name=projects/*/locations/*/scopes/*}`   
Updates a scopes.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/scopes/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/scopes/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.scopes.namespaces](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces/create)` |  `POST /v1/{parent=projects/*/locations/*/scopes/*}/namespaces`   
Creates a fleet namespace.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces/delete)` |  `DELETE /v1/{name=projects/*/locations/*/scopes/*/namespaces/*}`   
Deletes a fleet namespace.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces/get)` |  `GET /v1/{name=projects/*/locations/*/scopes/*/namespaces/*}`   
Returns the details of a fleet namespace.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces/list)` |  `GET /v1/{parent=projects/*/locations/*/scopes/*}/namespaces`   
Lists fleet namespaces.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.namespaces/patch)` |  `PATCH /v1/{scopeNamespace.name=projects/*/locations/*/scopes/*/namespaces/*}`   
Updates a fleet namespace.  
  
## REST Resource: [v1.projects.locations.scopes.rbacrolebindings](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings/create)` |  `POST /v1/{parent=projects/*/locations/*/scopes/*}/rbacrolebindings`   
Creates a Scope RBACRoleBinding.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings/delete)` |  `DELETE /v1/{name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Deletes a Scope RBACRoleBinding.  
`[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings/get)` |  `GET /v1/{name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Returns the details of a Scope RBACRoleBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings/list)` |  `GET /v1/{parent=projects/*/locations/*/scopes/*}/rbacrolebindings`   
Lists all Scope RBACRoleBindings.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1/projects.locations.scopes.rbacrolebindings/patch)` |  `PATCH /v1/{rbacrolebinding.name=projects/*/locations/*/scopes/*/rbacrolebindings/*}`   
Updates a Scope RBACRoleBinding.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
