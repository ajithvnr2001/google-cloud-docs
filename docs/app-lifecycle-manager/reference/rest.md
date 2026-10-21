---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/
title: App Lifecycle Manager API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:32:13.450480+00:00
---

# App Lifecycle Manager API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  App Lifecycle Manager API Stay organized with collections  Save and categorize content based on your preferences. 

Model, deploy, and operate your SaaS at scale.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.flagAttributes
  * REST Resource: v1beta1.projects.locations.flagReleases
  * REST Resource: v1beta1.projects.locations.flagRevisions
  * REST Resource: v1beta1.projects.locations.flags
  * REST Resource: v1beta1.projects.locations.releases
  * REST Resource: v1beta1.projects.locations.rolloutKinds
  * REST Resource: v1beta1.projects.locations.rollouts
  * REST Resource: v1beta1.projects.locations.saas
  * REST Resource: v1beta1.projects.locations.tenants
  * REST Resource: v1beta1.projects.locations.unitKinds
  * REST Resource: v1beta1.projects.locations.unitOperations
  * REST Resource: v1beta1.projects.locations.units
  * REST Resource: v1.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.releases
  * REST Resource: v1.projects.locations.rolloutKinds
  * REST Resource: v1.projects.locations.rollouts
  * REST Resource: v1.projects.locations.saas
  * REST Resource: v1.projects.locations.tenants
  * REST Resource: v1.projects.locations.unitKinds
  * REST Resource: v1.projects.locations.unitOperations
  * REST Resource: v1.projects.locations.units



## Service: saasservicemgmt.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://saasservicemgmt.googleapis.com/$discovery/rest?version=v1>
  * <https://saasservicemgmt.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://saasservicemgmt.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.flagAttributes](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagAttributes)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagAttributes/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/flagAttributes`   
Create a new flag attribute.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagAttributes/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/flagAttributes/*}`   
Delete a single flag attribute.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagAttributes/get)` |  `GET /v1beta1/{name=projects/*/locations/*/flagAttributes/*}`   
Retrieve a single flag attribute.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagAttributes/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/flagAttributes`   
Retrieve a collection of flag attributes.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagAttributes/patch)` |  `PATCH /v1beta1/{flagAttribute.name=projects/*/locations/*/flagAttributes/*}`   
Update a single flag attribute.  
  
## REST Resource: [v1beta1.projects.locations.flagReleases](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/flagReleases`   
Create a new flag release.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/flagReleases/*}`   
Delete a single flag release.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/get)` |  `GET /v1beta1/{name=projects/*/locations/*/flagReleases/*}`   
Retrieve a single flag release.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/flagReleases`   
Retrieve a collection of flag releases.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagReleases/patch)` |  `PATCH /v1beta1/{flagRelease.name=projects/*/locations/*/flagReleases/*}`   
Update a single flag release.  
  
## REST Resource: [v1beta1.projects.locations.flagRevisions](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/flagRevisions`   
Create a new flag revision.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/flagRevisions/*}`   
Delete a single flag revision.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions/get)` |  `GET /v1beta1/{name=projects/*/locations/*/flagRevisions/*}`   
Retrieve a single flag revision.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/flagRevisions`   
Retrieve a collection of flag revisions.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flagRevisions/patch)` |  `PATCH /v1beta1/{flagRevision.name=projects/*/locations/*/flagRevisions/*}`   
Update a single flag revision.  
  
## REST Resource: [v1beta1.projects.locations.flags](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/flags`   
Create a new flag.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/flags/*}`   
Delete a single flag.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/get)` |  `GET /v1beta1/{name=projects/*/locations/*/flags/*}`   
Retrieve a single flag.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/flags`   
Retrieve a collection of flags.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.flags/patch)` |  `PATCH /v1beta1/{flag.name=projects/*/locations/*/flags/*}`   
Update a single flag.  
  
## REST Resource: [v1beta1.projects.locations.releases](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.releases)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.releases/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/releases`   
Create a new release.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.releases/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/releases/*}`   
Delete a single release.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.releases/get)` |  `GET /v1beta1/{name=projects/*/locations/*/releases/*}`   
Retrieve a single release.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.releases/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/releases`   
Retrieve a collection of releases.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.releases/patch)` |  `PATCH /v1beta1/{release.name=projects/*/locations/*/releases/*}`   
Update a single release.  
  
## REST Resource: [v1beta1.projects.locations.rolloutKinds](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/rolloutKinds`   
Create a new rollout kind.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/rolloutKinds/*}`   
Delete a single rollout kind.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/get)` |  `GET /v1beta1/{name=projects/*/locations/*/rolloutKinds/*}`   
Retrieve a single rollout kind.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/rolloutKinds`   
Retrieve a collection of rollout kinds.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/patch)` |  `PATCH /v1beta1/{rolloutKind.name=projects/*/locations/*/rolloutKinds/*}`   
Update a single rollout kind.  
  
## REST Resource: [v1beta1.projects.locations.rollouts](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/rollouts`   
Create a new rollout.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/rollouts/*}`   
Delete a single rollout.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/get)` |  `GET /v1beta1/{name=projects/*/locations/*/rollouts/*}`   
Retrieve a single rollout.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/rollouts`   
Retrieve a collection of rollouts.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/patch)` |  `PATCH /v1beta1/{rollout.name=projects/*/locations/*/rollouts/*}`   
Update a single rollout.  
  
## REST Resource: [v1beta1.projects.locations.saas](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.saas)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.saas/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/saas`   
Create a new saas.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.saas/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/saas/*}`   
Delete a single saas.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.saas/get)` |  `GET /v1beta1/{name=projects/*/locations/*/saas/*}`   
Retrieve a single saas.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.saas/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/saas`   
Retrieve a collection of saas.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.saas/patch)` |  `PATCH /v1beta1/{saas.name=projects/*/locations/*/saas/*}`   
Update a single saas.  
  
## REST Resource: [v1beta1.projects.locations.tenants](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.tenants)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.tenants/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/tenants`   
Create a new tenant.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.tenants/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/tenants/*}`   
Delete a single tenant.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.tenants/get)` |  `GET /v1beta1/{name=projects/*/locations/*/tenants/*}`   
Retrieve a single tenant.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.tenants/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/tenants`   
Retrieve a collection of tenants.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.tenants/patch)` |  `PATCH /v1beta1/{tenant.name=projects/*/locations/*/tenants/*}`   
Update a single tenant.  
  
## REST Resource: [v1beta1.projects.locations.unitKinds](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/unitKinds`   
Create a new unit kind.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/unitKinds/*}`   
Delete a single unit kind.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/get)` |  `GET /v1beta1/{name=projects/*/locations/*/unitKinds/*}`   
Retrieve a single unit kind.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/unitKinds`   
Retrieve a collection of unit kinds.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitKinds/patch)` |  `PATCH /v1beta1/{unitKind.name=projects/*/locations/*/unitKinds/*}`   
Update a single unit kind.  
  
## REST Resource: [v1beta1.projects.locations.unitOperations](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/unitOperations`   
Create a new unit operation.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/unitOperations/*}`   
Delete a single unit operation.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/unitOperations/*}`   
Retrieve a single unit operation.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/unitOperations`   
Retrieve a collection of unit operations.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.unitOperations/patch)` |  `PATCH /v1beta1/{unitOperation.name=projects/*/locations/*/unitOperations/*}`   
Update a single unit operation.  
  
## REST Resource: [v1beta1.projects.locations.units](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.units)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.units/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/units`   
Create a new unit.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.units/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/units/*}`   
Delete a single unit.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.units/get)` |  `GET /v1beta1/{name=projects/*/locations/*/units/*}`   
Retrieve a single unit.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.units/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/units`   
Retrieve a collection of units.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.units/patch)` |  `PATCH /v1beta1/{unit.name=projects/*/locations/*/units/*}`   
Update a single unit.  
  
## REST Resource: [v1.operations](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/operations/cancel)` |  `POST /v1/{name=operations/**}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/operations/delete)` |  `DELETE /v1/{name=operations/**}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/operations/get)` |  `GET /v1/{name=operations/**}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/operations/list)` |  `GET /v1/{name=operations}`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.releases](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.releases)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.releases/create)` |  `POST /v1/{parent=projects/*/locations/*}/releases`   
Create a new release.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.releases/delete)` |  `DELETE /v1/{name=projects/*/locations/*/releases/*}`   
Delete a single release.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.releases/get)` |  `GET /v1/{name=projects/*/locations/*/releases/*}`   
Retrieve a single release.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.releases/list)` |  `GET /v1/{parent=projects/*/locations/*}/releases`   
Retrieve a collection of releases.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.releases/patch)` |  `PATCH /v1/{release.name=projects/*/locations/*/releases/*}`   
Update a single release.  
  
## REST Resource: [v1.projects.locations.rolloutKinds](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rolloutKinds)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rolloutKinds/create)` |  `POST /v1/{parent=projects/*/locations/*}/rolloutKinds`   
Create a new rollout kind.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rolloutKinds/delete)` |  `DELETE /v1/{name=projects/*/locations/*/rolloutKinds/*}`   
Delete a single rollout kind.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rolloutKinds/get)` |  `GET /v1/{name=projects/*/locations/*/rolloutKinds/*}`   
Retrieve a single rollout kind.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rolloutKinds/list)` |  `GET /v1/{parent=projects/*/locations/*}/rolloutKinds`   
Retrieve a collection of rollout kinds.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rolloutKinds/patch)` |  `PATCH /v1/{rolloutKind.name=projects/*/locations/*/rolloutKinds/*}`   
Update a single rollout kind.  
  
## REST Resource: [v1.projects.locations.rollouts](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rollouts)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rollouts/create)` |  `POST /v1/{parent=projects/*/locations/*}/rollouts`   
Create a new rollout.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rollouts/delete)` |  `DELETE /v1/{name=projects/*/locations/*/rollouts/*}`   
Delete a single rollout.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rollouts/get)` |  `GET /v1/{name=projects/*/locations/*/rollouts/*}`   
Retrieve a single rollout.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rollouts/list)` |  `GET /v1/{parent=projects/*/locations/*}/rollouts`   
Retrieve a collection of rollouts.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.rollouts/patch)` |  `PATCH /v1/{rollout.name=projects/*/locations/*/rollouts/*}`   
Update a single rollout.  
  
## REST Resource: [v1.projects.locations.saas](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.saas)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.saas/create)` |  `POST /v1/{parent=projects/*/locations/*}/saas`   
Create a new saas.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.saas/delete)` |  `DELETE /v1/{name=projects/*/locations/*/saas/*}`   
Delete a single saas.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.saas/get)` |  `GET /v1/{name=projects/*/locations/*/saas/*}`   
Retrieve a single saas.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.saas/list)` |  `GET /v1/{parent=projects/*/locations/*}/saas`   
Retrieve a collection of saas.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.saas/patch)` |  `PATCH /v1/{saas.name=projects/*/locations/*/saas/*}`   
Update a single saas.  
  
## REST Resource: [v1.projects.locations.tenants](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.tenants)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.tenants/create)` |  `POST /v1/{parent=projects/*/locations/*}/tenants`   
Create a new tenant.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.tenants/delete)` |  `DELETE /v1/{name=projects/*/locations/*/tenants/*}`   
Delete a single tenant.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.tenants/get)` |  `GET /v1/{name=projects/*/locations/*/tenants/*}`   
Retrieve a single tenant.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.tenants/list)` |  `GET /v1/{parent=projects/*/locations/*}/tenants`   
Retrieve a collection of tenants.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.tenants/patch)` |  `PATCH /v1/{tenant.name=projects/*/locations/*/tenants/*}`   
Update a single tenant.  
  
## REST Resource: [v1.projects.locations.unitKinds](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitKinds)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitKinds/create)` |  `POST /v1/{parent=projects/*/locations/*}/unitKinds`   
Create a new unit kind.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitKinds/delete)` |  `DELETE /v1/{name=projects/*/locations/*/unitKinds/*}`   
Delete a single unit kind.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitKinds/get)` |  `GET /v1/{name=projects/*/locations/*/unitKinds/*}`   
Retrieve a single unit kind.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitKinds/list)` |  `GET /v1/{parent=projects/*/locations/*}/unitKinds`   
Retrieve a collection of unit kinds.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitKinds/patch)` |  `PATCH /v1/{unitKind.name=projects/*/locations/*/unitKinds/*}`   
Update a single unit kind.  
  
## REST Resource: [v1.projects.locations.unitOperations](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/create)` |  `POST /v1/{parent=projects/*/locations/*}/unitOperations`   
Create a new unit operation.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/unitOperations/*}`   
Delete a single unit operation.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/get)` |  `GET /v1/{name=projects/*/locations/*/unitOperations/*}`   
Retrieve a single unit operation.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/list)` |  `GET /v1/{parent=projects/*/locations/*}/unitOperations`   
Retrieve a collection of unit operations.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.unitOperations/patch)` |  `PATCH /v1/{unitOperation.name=projects/*/locations/*/unitOperations/*}`   
Update a single unit operation.  
  
## REST Resource: [v1.projects.locations.units](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units)

Methods  
---  
`[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/create)` |  `POST /v1/{parent=projects/*/locations/*}/units`   
Create a new unit.  
`[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/delete)` |  `DELETE /v1/{name=projects/*/locations/*/units/*}`   
Delete a single unit.  
`[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/get)` |  `GET /v1/{name=projects/*/locations/*/units/*}`   
Retrieve a single unit.  
`[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/list)` |  `GET /v1/{parent=projects/*/locations/*}/units`   
Retrieve a collection of units.  
`[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1/projects.locations.units/patch)` |  `PATCH /v1/{unit.name=projects/*/locations/*/units/*}`   
Update a single unit.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
