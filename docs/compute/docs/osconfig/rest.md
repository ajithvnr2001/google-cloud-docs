---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/
title: OS Config API \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:25:00.671022+00:00
---

# OS Config API  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  OS Config API Stay organized with collections  Save and categorize content based on your preferences. 

OS management tools that can be used for patch management, patch compliance, and configuration management on VM instances.

  * REST Resource: v2beta.folders.locations.global.policyOrchestrators
  * REST Resource: v2beta.folders.locations.operations
  * REST Resource: v2beta.organizations.locations.global.policyOrchestrators
  * REST Resource: v2beta.organizations.locations.operations
  * REST Resource: v2beta.projects.locations.global.policyOrchestrators
  * REST Resource: v2beta.projects.locations.operations
  * REST Resource: v2.folders.locations.global.policyOrchestrators
  * REST Resource: v2.folders.locations.operations
  * REST Resource: v2.organizations.locations.global.policyOrchestrators
  * REST Resource: v2.organizations.locations.operations
  * REST Resource: v2.projects.locations.global.policyOrchestrators
  * REST Resource: v2.projects.locations.operations
  * REST Resource: v1beta.projects.guestPolicies
  * REST Resource: v1beta.projects.patchDeployments
  * REST Resource: v1beta.projects.patchJobs
  * REST Resource: v1beta.projects.patchJobs.instanceDetails
  * REST Resource: v1beta.projects.zones.instances
  * REST Resource: v1alpha.projects.locations.instanceOSPoliciesCompliances
  * REST Resource: v1alpha.projects.locations.instances.inventories
  * REST Resource: v1alpha.projects.locations.instances.osPolicyAssignments.reports
  * REST Resource: v1alpha.projects.locations.instances.vulnerabilityReports
  * REST Resource: v1alpha.projects.locations.osPolicyAssignments
  * REST Resource: v1alpha.projects.locations.osPolicyAssignments.operations
  * REST Resource: v1.projects.locations.global
  * REST Resource: v1.projects.locations.instances.inventories
  * REST Resource: v1.projects.locations.instances.osPolicyAssignments.reports
  * REST Resource: v1.projects.locations.instances.vulnerabilityReports
  * REST Resource: v1.projects.locations.osPolicyAssignments
  * REST Resource: v1.projects.locations.osPolicyAssignments.operations
  * REST Resource: v1.projects.patchDeployments
  * REST Resource: v1.projects.patchJobs
  * REST Resource: v1.projects.patchJobs.instanceDetails



## Service: osconfig.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://osconfig.googleapis.com/$discovery/rest?version=v2>
  * <https://osconfig.googleapis.com/$discovery/rest?version=v2beta>
  * <https://osconfig.googleapis.com/$discovery/rest?version=v1>
  * <https://osconfig.googleapis.com/$discovery/rest?version=v1beta>
  * <https://osconfig.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://osconfig.googleapis.com`



## REST Resource: [v2beta.folders.locations.global.policyOrchestrators](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/create)` |  `POST /v2beta/{parent=folders/*/locations/global}/policyOrchestrators`   
Creates a new policy orchestrator under the given folder resource.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/delete)` |  `DELETE /v2beta/{name=folders/*/locations/global/policyOrchestrators/*}`   
Deletes an existing policy orchestrator resource, parented by a folder.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/get)` |  `GET /v2beta/{name=folders/*/locations/global/policyOrchestrators/*}`   
Retrieves an existing policy orchestrator, parented by a folder.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/list)` |  `GET /v2beta/{parent=folders/*/locations/global}/policyOrchestrators`   
Lists the policy orchestrators under the given parent folder resource.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.global.policyOrchestrators/patch)` |  `PATCH /v2beta/{policyOrchestrator.name=folders/*/locations/global/policyOrchestrators/*}`   
Updates an existing policy orchestrator, parented by a folder.  
  
## REST Resource: [v2beta.folders.locations.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations/cancel)` |  `POST /v2beta/{name=folders/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations/delete)` |  `DELETE /v2beta/{name=folders/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations/get)` |  `GET /v2beta/{name=folders/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/folders.locations.operations/list)` |  `GET /v2beta/{name=folders/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2beta.organizations.locations.global.policyOrchestrators](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.global.policyOrchestrators)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.global.policyOrchestrators/create)` |  `POST /v2beta/{parent=organizations/*/locations/global}/policyOrchestrators`   
Creates a new policy orchestrator under the given organizations resource.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.global.policyOrchestrators/delete)` |  `DELETE /v2beta/{name=organizations/*/locations/global/policyOrchestrators/*}`   
Deletes an existing policy orchestrator resource, parented by an organization.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.global.policyOrchestrators/get)` |  `GET /v2beta/{name=organizations/*/locations/global/policyOrchestrators/*}`   
Retrieves an existing policy orchestrator, parented by an organization.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.global.policyOrchestrators/list)` |  `GET /v2beta/{parent=organizations/*/locations/global}/policyOrchestrators`   
Lists the policy orchestrators under the given parent organization resource.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.global.policyOrchestrators/patch)` |  `PATCH /v2beta/{policyOrchestrator.name=organizations/*/locations/global/policyOrchestrators/*}`   
Updates an existing policy orchestrator, parented by an organization.  
  
## REST Resource: [v2beta.organizations.locations.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.operations/cancel)` |  `POST /v2beta/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.operations/delete)` |  `DELETE /v2beta/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.operations/get)` |  `GET /v2beta/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/organizations.locations.operations/list)` |  `GET /v2beta/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2beta.projects.locations.global.policyOrchestrators](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/create)` |  `POST /v2beta/{parent=projects/*/locations/global}/policyOrchestrators`   
Creates a new policy orchestrator under the given project resource.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/delete)` |  `DELETE /v2beta/{name=projects/*/locations/global/policyOrchestrators/*}`   
Deletes an existing policy orchestrator resource, parented by a project.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/get)` |  `GET /v2beta/{name=projects/*/locations/global/policyOrchestrators/*}`   
Retrieves an existing policy orchestrator, parented by a project.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/list)` |  `GET /v2beta/{parent=projects/*/locations/global}/policyOrchestrators`   
Lists the policy orchestrators under the given parent project resource.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.global.policyOrchestrators/patch)` |  `PATCH /v2beta/{policyOrchestrator.name=projects/*/locations/global/policyOrchestrators/*}`   
Updates an existing policy orchestrator, parented by a project.  
  
## REST Resource: [v2beta.projects.locations.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.operations/cancel)` |  `POST /v2beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.operations/delete)` |  `DELETE /v2beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.operations/get)` |  `GET /v2beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2beta/projects.locations.operations/list)` |  `GET /v2beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.folders.locations.global.policyOrchestrators](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/create)` |  `POST /v2/{parent=folders/*/locations/global}/policyOrchestrators`   
Creates a new policy orchestrator under the given folder resource.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/delete)` |  `DELETE /v2/{name=folders/*/locations/global/policyOrchestrators/*}`   
Deletes an existing policy orchestrator resource, parented by a folder.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/get)` |  `GET /v2/{name=folders/*/locations/global/policyOrchestrators/*}`   
Retrieves an existing policy orchestrator, parented by a folder.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/list)` |  `GET /v2/{parent=folders/*/locations/global}/policyOrchestrators`   
Lists the policy orchestrators under the given parent folder resource.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.global.policyOrchestrators/patch)` |  `PATCH /v2/{policyOrchestrator.name=folders/*/locations/global/policyOrchestrators/*}`   
Updates an existing policy orchestrator, parented by a folder.  
  
## REST Resource: [v2.folders.locations.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.operations/cancel)` |  `POST /v2/{name=folders/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.operations/delete)` |  `DELETE /v2/{name=folders/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.operations/get)` |  `GET /v2/{name=folders/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/folders.locations.operations/list)` |  `GET /v2/{name=folders/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.organizations.locations.global.policyOrchestrators](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/create)` |  `POST /v2/{parent=organizations/*/locations/global}/policyOrchestrators`   
Creates a new policy orchestrator under the given organizations resource.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/delete)` |  `DELETE /v2/{name=organizations/*/locations/global/policyOrchestrators/*}`   
Deletes an existing policy orchestrator resource, parented by an organization.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/get)` |  `GET /v2/{name=organizations/*/locations/global/policyOrchestrators/*}`   
Retrieves an existing policy orchestrator, parented by an organization.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/list)` |  `GET /v2/{parent=organizations/*/locations/global}/policyOrchestrators`   
Lists the policy orchestrators under the given parent organization resource.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.global.policyOrchestrators/patch)` |  `PATCH /v2/{policyOrchestrator.name=organizations/*/locations/global/policyOrchestrators/*}`   
Updates an existing policy orchestrator, parented by an organization.  
  
## REST Resource: [v2.organizations.locations.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.operations/cancel)` |  `POST /v2/{name=organizations/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.operations/delete)` |  `DELETE /v2/{name=organizations/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.operations/get)` |  `GET /v2/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/organizations.locations.operations/list)` |  `GET /v2/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v2.projects.locations.global.policyOrchestrators](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/create)` |  `POST /v2/{parent=projects/*/locations/global}/policyOrchestrators`   
Creates a new policy orchestrator under the given project resource.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/delete)` |  `DELETE /v2/{name=projects/*/locations/global/policyOrchestrators/*}`   
Deletes an existing policy orchestrator resource, parented by a project.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/get)` |  `GET /v2/{name=projects/*/locations/global/policyOrchestrators/*}`   
Retrieves an existing policy orchestrator, parented by a project.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/list)` |  `GET /v2/{parent=projects/*/locations/global}/policyOrchestrators`   
Lists the policy orchestrators under the given parent project resource.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.global.policyOrchestrators/patch)` |  `PATCH /v2/{policyOrchestrator.name=projects/*/locations/global/policyOrchestrators/*}`   
Updates an existing policy orchestrator, parented by a project.  
  
## REST Resource: [v2.projects.locations.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.operations/cancel)` |  `POST /v2/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.operations/delete)` |  `DELETE /v2/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.operations/get)` |  `GET /v2/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v2/projects.locations.operations/list)` |  `GET /v2/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta.projects.guestPolicies](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/create)` |  `POST /v1beta/{parent=projects/*}/guestPolicies`   
Create an OS Config guest policy.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/delete)` |  `DELETE /v1beta/{name=projects/*/guestPolicies/*}`   
Delete an OS Config guest policy.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/get)` |  `GET /v1beta/{name=projects/*/guestPolicies/*}`   
Get an OS Config guest policy.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/list)` |  `GET /v1beta/{parent=projects/*}/guestPolicies`   
Get a page of OS Config guest policies.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.guestPolicies/patch)` |  `PATCH /v1beta/{guestPolicy.name=projects/*/guestPolicies/*}`   
Update an OS Config guest policy.  
  
## REST Resource: [v1beta.projects.patchDeployments](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/create)` |  `POST /v1beta/{parent=projects/*}/patchDeployments`   
Create an OS Config patch deployment.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/delete)` |  `DELETE /v1beta/{name=projects/*/patchDeployments/*}`   
Delete an OS Config patch deployment.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/get)` |  `GET /v1beta/{name=projects/*/patchDeployments/*}`   
Get an OS Config patch deployment.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/list)` |  `GET /v1beta/{parent=projects/*}/patchDeployments`   
Get a page of OS Config patch deployments.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/patch)` |  `PATCH /v1beta/{patchDeployment.name=projects/*/patchDeployments/*}`   
Update an OS Config patch deployment.  
`[pause](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/pause)` |  `POST /v1beta/{name=projects/*/patchDeployments/*}:pause`   
Change state of patch deployment to "PAUSED".  
`[resume](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchDeployments/resume)` |  `POST /v1beta/{name=projects/*/patchDeployments/*}:resume`   
Change state of patch deployment back to "ACTIVE".  
  
## REST Resource: [v1beta.projects.patchJobs](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs/cancel)` |  `POST /v1beta/{name=projects/*/patchJobs/*}:cancel`   
Cancel a patch job.  
`[execute](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs/execute)` |  `POST /v1beta/{parent=projects/*}/patchJobs:execute`   
Patch VM instances by creating and running a patch job.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs/get)` |  `GET /v1beta/{name=projects/*/patchJobs/*}`   
Get the patch job.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs/list)` |  `GET /v1beta/{parent=projects/*}/patchJobs`   
Get a list of patch jobs.  
  
## REST Resource: [v1beta.projects.patchJobs.instanceDetails](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails)

Methods  
---  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.patchJobs.instanceDetails/list)` |  `GET /v1beta/{parent=projects/*/patchJobs/*}/instanceDetails`   
Get a list of instance details for a given patch job.  
  
## REST Resource: [v1beta.projects.zones.instances](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances)

Methods  
---  
`[lookupEffectiveGuestPolicy](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1beta/projects.zones.instances/lookupEffectiveGuestPolicy)` |  `POST /v1beta/{instance=projects/*/zones/*/instances/*}:lookupEffectiveGuestPolicy`   
Lookup the effective guest policy that applies to a VM instance.  
  
## REST Resource: [v1alpha.projects.locations.instanceOSPoliciesCompliances](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/get)   
**(deprecated)**` |  `GET /v1alpha/{name=projects/*/locations/*/instanceOSPoliciesCompliances/*}`   
Get OS policies compliance data for the specified Compute Engine VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instanceOSPoliciesCompliances/list)   
**(deprecated)**` |  `GET /v1alpha/{parent=projects/*/locations/*}/instanceOSPoliciesCompliances`   
List OS policies compliance data for all Compute Engine VM instances in the specified zone.  
  
## REST Resource: [v1alpha.projects.locations.instances.inventories](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories/get)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*/inventory}`   
Get inventory data for the specified VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.inventories/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/instances/*}/inventories`   
List inventory data for all VM instances in the specified zone.  
  
## REST Resource: [v1alpha.projects.locations.instances.osPolicyAssignments.reports](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.osPolicyAssignments.reports)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.osPolicyAssignments.reports/get)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*/osPolicyAssignments/*/report}`   
Get the OS policy assignment report for the specified Compute Engine VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.osPolicyAssignments.reports/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/instances/*/osPolicyAssignments/*}/reports`   
List OS policy assignment reports for all Compute Engine VM instances in the specified zone.  
  
## REST Resource: [v1alpha.projects.locations.instances.vulnerabilityReports](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.vulnerabilityReports)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.vulnerabilityReports/get)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*/vulnerabilityReport}`   
Gets the vulnerability report for the specified VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.instances.vulnerabilityReports/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/instances/*}/vulnerabilityReports`   
List vulnerability reports for all VM instances in the specified zone.  
  
## REST Resource: [v1alpha.projects.locations.osPolicyAssignments](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments`   
Create an OS policy assignment.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}`   
Delete the OS policy assignment.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments/get)` |  `GET /v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}`   
Retrieve an existing OS policy assignment.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/osPolicyAssignments`   
List the OS policy assignments under the parent resource.  
`[listRevisions](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments/listRevisions)` |  `GET /v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*}:listRevisions`   
List the OS policy assignment revisions for a given OS policy assignment.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments/patch)` |  `PATCH /v1alpha/{osPolicyAssignment.name=projects/*/locations/*/osPolicyAssignments/*}`   
Update an existing OS policy assignment.  
  
## REST Resource: [v1alpha.projects.locations.osPolicyAssignments.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1alpha/projects.locations.osPolicyAssignments.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/osPolicyAssignments/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.locations.global](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.global)

Methods  
---  
`[getProjectFeatureSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.global/getProjectFeatureSettings)` |  `GET /v1/{name=projects/*/locations/global/projectFeatureSettings}`   
GetProjectFeatureSettings returns the VM Manager feature settings for a project.  
`[updateProjectFeatureSettings](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.global/updateProjectFeatureSettings)` |  `PATCH /v1/{projectFeatureSettings.name=projects/*/locations/global/projectFeatureSettings}`   
UpdateProjectFeatureSettings sets the VM Manager features for a project.  
  
## REST Resource: [v1.projects.locations.instances.inventories](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.inventories)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.inventories/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/inventory}`   
Get inventory data for the specified VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.inventories/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/inventories`   
List inventory data for all VM instances in the specified zone.  
  
## REST Resource: [v1.projects.locations.instances.osPolicyAssignments.reports](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.osPolicyAssignments.reports)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.osPolicyAssignments.reports/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/osPolicyAssignments/*/report}`   
Get the OS policy assignment report for the specified Compute Engine VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.osPolicyAssignments.reports/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*/osPolicyAssignments/*}/reports`   
List OS policy assignment reports for all Compute Engine VM instances in the specified zone.  
  
## REST Resource: [v1.projects.locations.instances.vulnerabilityReports](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.vulnerabilityReports)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.vulnerabilityReports/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/vulnerabilityReport}`   
Gets the vulnerability report for the specified VM instance.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.instances.vulnerabilityReports/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/vulnerabilityReports`   
List vulnerability reports for all VM instances in the specified zone.  
  
## REST Resource: [v1.projects.locations.osPolicyAssignments](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/create)` |  `POST /v1/{parent=projects/*/locations/*}/osPolicyAssignments`   
Create an OS policy assignment.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/osPolicyAssignments/*}`   
Delete the OS policy assignment.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/get)` |  `GET /v1/{name=projects/*/locations/*/osPolicyAssignments/*}`   
Retrieve an existing OS policy assignment.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/list)` |  `GET /v1/{parent=projects/*/locations/*}/osPolicyAssignments`   
List the OS policy assignments under the parent resource.  
`[listRevisions](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/listRevisions)` |  `GET /v1/{name=projects/*/locations/*/osPolicyAssignments/*}:listRevisions`   
List the OS policy assignment revisions for a given OS policy assignment.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments/patch)` |  `PATCH /v1/{osPolicyAssignment.name=projects/*/locations/*/osPolicyAssignments/*}`   
Update an existing OS policy assignment.  
  
## REST Resource: [v1.projects.locations.osPolicyAssignments.operations](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/osPolicyAssignments/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments.operations/get)` |  `GET /v1/{name=projects/*/locations/*/osPolicyAssignments/*/operations/*}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.projects.patchDeployments](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/create)` |  `POST /v1/{parent=projects/*}/patchDeployments`   
Create an OS Config patch deployment.  
`[delete](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/delete)` |  `DELETE /v1/{name=projects/*/patchDeployments/*}`   
Delete an OS Config patch deployment.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/get)` |  `GET /v1/{name=projects/*/patchDeployments/*}`   
Get an OS Config patch deployment.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/list)` |  `GET /v1/{parent=projects/*}/patchDeployments`   
Get a page of OS Config patch deployments.  
`[patch](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/patch)` |  `PATCH /v1/{patchDeployment.name=projects/*/patchDeployments/*}`   
Update an OS Config patch deployment.  
`[pause](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/pause)` |  `POST /v1/{name=projects/*/patchDeployments/*}:pause`   
Change state of patch deployment to "PAUSED".  
`[resume](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchDeployments/resume)` |  `POST /v1/{name=projects/*/patchDeployments/*}:resume`   
Change state of patch deployment back to "ACTIVE".  
  
## REST Resource: [v1.projects.patchJobs](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/cancel)` |  `POST /v1/{name=projects/*/patchJobs/*}:cancel`   
Cancel a patch job.  
`[execute](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/execute)` |  `POST /v1/{parent=projects/*}/patchJobs:execute`   
Patch VM instances by creating and running a patch job.  
`[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/get)` |  `GET /v1/{name=projects/*/patchJobs/*}`   
Get the patch job.  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/list)` |  `GET /v1/{parent=projects/*}/patchJobs`   
Get a list of patch jobs.  
  
## REST Resource: [v1.projects.patchJobs.instanceDetails](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails)

Methods  
---  
`[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs.instanceDetails/list)` |  `GET /v1/{parent=projects/*/patchJobs/*}/instanceDetails`   
Get a list of instance details for a given patch job.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
