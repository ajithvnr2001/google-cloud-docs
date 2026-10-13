---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/
title: Design Center API \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:04.524304+00:00
---

# Design Center API  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Design Center API Stay organized with collections  Save and categorize content based on your preferences. 

Design and share deployable application architectures.

  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1alpha.projects.locations.spaces
  * REST Resource: v1alpha.projects.locations.spaces.applicationTemplates
  * REST Resource: v1alpha.projects.locations.spaces.applicationTemplates.components
  * REST Resource: v1alpha.projects.locations.spaces.applicationTemplates.components.connections
  * REST Resource: v1alpha.projects.locations.spaces.applicationTemplates.policies
  * REST Resource: v1alpha.projects.locations.spaces.applicationTemplates.revisions
  * REST Resource: v1alpha.projects.locations.spaces.applicationTemplates.systemRevisions
  * REST Resource: v1alpha.projects.locations.spaces.applications
  * REST Resource: v1alpha.projects.locations.spaces.catalogs
  * REST Resource: v1alpha.projects.locations.spaces.catalogs.shares
  * REST Resource: v1alpha.projects.locations.spaces.catalogs.templates
  * REST Resource: v1alpha.projects.locations.spaces.catalogs.templates.revisions
  * REST Resource: v1alpha.projects.locations.spaces.sharedTemplates
  * REST Resource: v1alpha.projects.locations.spaces.sharedTemplates.revisions
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.spaces
  * REST Resource: v1.projects.locations.spaces.applicationTemplates
  * REST Resource: v1.projects.locations.spaces.applicationTemplates.components
  * REST Resource: v1.projects.locations.spaces.applicationTemplates.components.connections
  * REST Resource: v1.projects.locations.spaces.applicationTemplates.policies
  * REST Resource: v1.projects.locations.spaces.applicationTemplates.revisions
  * REST Resource: v1.projects.locations.spaces.applicationTemplates.systemRevisions
  * REST Resource: v1.projects.locations.spaces.applications
  * REST Resource: v1.projects.locations.spaces.catalogs
  * REST Resource: v1.projects.locations.spaces.catalogs.shares
  * REST Resource: v1.projects.locations.spaces.catalogs.templates
  * REST Resource: v1.projects.locations.spaces.catalogs.templates.revisions
  * REST Resource: v1.projects.locations.spaces.sharedTemplates
  * REST Resource: v1.projects.locations.spaces.sharedTemplates.revisions



## Service: designcenter.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://designcenter.googleapis.com/$discovery/rest?version=v1>
  * <https://designcenter.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://designcenter.googleapis.com`



## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[fetchFrameworks](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations/fetchFrameworks)` |  `GET /v1alpha/{parent=projects/*/locations/*}:fetchFrameworks`   
Fetches all frameworks for assessment report.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations.spaces](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/spaces`   
Creates a space.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*}`   
Deletes a space.  
`[generateTerraformPlanAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/generateTerraformPlanAssessmentReport)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*}:generateTerraformPlanAssessmentReport`   
Generate a Terraform plan assessment report for a given Terraform plan.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*}`   
Gets details about a space.  
`[getIamPolicy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/getIamPolicy)` |  `GET /v1alpha/{resource=projects/*/locations/*/spaces/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[inferConnections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/inferConnections)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*}:inferConnections`   
Infers and suggests connections between components within a space.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/spaces`   
Lists spaces in a given project and location.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/patch)` |  `PATCH /v1alpha/{space.name=projects/*/locations/*/spaces/*}`   
Updates a space.  
`[registerAppHubApplicationResources](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/registerAppHubApplicationResources)` |  `POST /v1alpha/{parent=projects/*/locations/*}/spaces:registerAppHubApplicationResources`   
Register deployed resources from terraform state file with App Hub without needing a space.  
`[registerApphubResources](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/registerApphubResources)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*}:registerApphubResources`   
Registers a list of deployed GCP resources with App Hub.  
`[registerDeployedResources](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/registerDeployedResources)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*}:registerDeployedResources`   
Register deployed resources from terraform state file with App Hub.  
`[setIamPolicy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/setIamPolicy)` |  `POST /v1alpha/{resource=projects/*/locations/*/spaces/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces/testIamPermissions)` |  `POST /v1alpha/{resource=projects/*/locations/*/spaces/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applicationTemplates](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates)

Methods  
---  
`[commit](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/commit)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:commit`   
Commits an application template to create a new revision.  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*}/applicationTemplates`   
Creates an application template.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}`   
Deletes an application template.  
`[export](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/export)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:export`   
Exports Terraform files for an application template.  
`[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/generate)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:generate`   
Generates Terraform files for an application template.  
`[generateAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/generateAssessmentReport)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:generateAssessmentReport`   
Generate assessment reports of an application template.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}`   
Gets details about an application template.  
`[import](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/import)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:import`   
Imports to an existing application template from a given shared template.  
`[importIaC](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/importIaC)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:importIaC`   
Imports IaC for an application template.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*}/applicationTemplates`   
Lists application templates in a given space.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates/patch)` |  `PATCH /v1alpha/{applicationTemplate.name=projects/*/locations/*/spaces/*/applicationTemplates/*}`   
Updates an application template.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applicationTemplates.components](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/components`   
Creates a component.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}`   
Deletes a component.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}`   
Gets details about a Component.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/components`   
Lists components in an application template.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components/patch)` |  `PATCH /v1alpha/{component.name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}`   
Updates a component.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applicationTemplates.components.connections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}/connections`   
Creates a connection.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*/connections/*}`   
Deletes a connection.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*/connections/*}`   
Gets details about a connection.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}/connections`   
Lists connections in an application template.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.components.connections/patch)` |  `PATCH /v1alpha/{connection.name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*/connections/*}`   
Updates a connection.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applicationTemplates.policies](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.policies)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.policies/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/policies`   
Creates a policy for an application template.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.policies/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/policies/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.policies/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/policies/*}`   
Policy related APIs.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.policies/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/policies`   
Lists policies for an application template.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.policies/patch)` |  `PATCH /v1alpha/{policy.name=projects/*/locations/*/spaces/*/applicationTemplates/*/policies/*}`   
Updates a policy.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applicationTemplates.revisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}`   
Deletes an application template revision.  
`[export](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/export)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}:export`   
Exports Terraform files for an application template revision.  
`[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/generate)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}:generate`   
Generates Terraform files for an application template revision.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}`   
Gets details about an application template revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.revisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/revisions`   
Lists application template revisions in a given application template.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applicationTemplates.systemRevisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions)

Methods  
---  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/systemRevisions/*}`   
Gets the given application template system revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/systemRevisions`   
Lists application template system revisions in a given application template.  
  
## REST Resource: [v1alpha.projects.locations.spaces.applications](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*}/applications`   
Creates an application.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}`   
Deletes an application.  
`[deploy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/deploy)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:deploy`   
Deploys an application.  
`[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/fetchAssessmentReport)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:fetchAssessmentReport`   
Fetches the assessment report of a deployed application if present.  
`[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/generate)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:generate`   
Generates Terraform files for an application.  
`[generateAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/generateAssessmentReport)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:generateAssessmentReport`   
Generate assessment reports of an application.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}`   
Gets details about an application.  
`[importIaC](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/importIaC)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:importIaC`   
Imports IaC for an application resource.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*}/applications`   
Lists applications in a given space.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/patch)` |  `PATCH /v1alpha/{application.name=projects/*/locations/*/spaces/*/applications/*}`   
Updates an application.  
`[preview](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/preview)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:preview`   
Previews deployment of an application.  
`[register](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applications/register)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/applications/*}:register`   
Register deployed application from terraform state file with App Hub.  
  
## REST Resource: [v1alpha.projects.locations.spaces.catalogs](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*}/catalogs`   
Creates a catalog.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*}`   
Deletes a catalog.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*}`   
Gets details about a catalog.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*}/catalogs`   
Lists catalogs in a given space.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs/patch)` |  `PATCH /v1alpha/{catalog.name=projects/*/locations/*/spaces/*/catalogs/*}`   
Updates a catalog.  
  
## REST Resource: [v1alpha.projects.locations.spaces.catalogs.shares](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*/catalogs/*}/shares`   
Shares a catalog from one space to another space.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/shares/*}`   
Deletes a catalog share.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/shares/*}`   
Get catalog share object for the space.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/catalogs/*}/shares`   
Lists catalog share objects for the space.  
`[sync](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.shares/sync)` |  `POST /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/shares/*}:sync`   
Synchronizes a share and updates the destination workspace to reflect.  
  
## REST Resource: [v1alpha.projects.locations.spaces.catalogs.templates](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*/catalogs/*}/templates`   
Adds a template to a catalog.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*}`   
Deletes a catalog template.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*}`   
Gets a catalog template.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/catalogs/*}/templates`   
Lists catalog templates.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates/patch)` |  `PATCH /v1alpha/{catalogTemplate.name=projects/*/locations/*/spaces/*/catalogs/*/templates/*}`   
Updates a catalog template resource.  
  
## REST Resource: [v1alpha.projects.locations.spaces.catalogs.templates.revisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions/create)` |  `POST /v1alpha/{parent=projects/*/locations/*/spaces/*/catalogs/*/templates/*}/revisions`   
Creates a template revision.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*/revisions/*}`   
Deletes a template revision.  
`[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions/fetchAssessmentReport)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*/revisions/*}:fetchAssessmentReport`   
Fetches the assessment report of a catalog template revision if present.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*/revisions/*}`   
Gets details about a template revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.catalogs.templates.revisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/catalogs/*/templates/*}/revisions`   
Lists template revisions.  
  
## REST Resource: [v1alpha.projects.locations.spaces.sharedTemplates](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates)

Methods  
---  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/sharedTemplates/*}`   
Gets details about a shared template.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*}/sharedTemplates`   
Lists shared templates in a given space.  
  
## REST Resource: [v1alpha.projects.locations.spaces.sharedTemplates.revisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates.revisions)

Methods  
---  
`[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates.revisions/fetchAssessmentReport)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/sharedTemplates/*/revisions/*}:fetchAssessmentReport`   
Fetches the assessment report of a shared template revision if present.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates.revisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/spaces/*/sharedTemplates/*/revisions/*}`   
Gets details about a shared template revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.sharedTemplates.revisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/spaces/*/sharedTemplates/*}/revisions`   
Lists shared template revisions in a given space.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[fetchFrameworks](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations/fetchFrameworks)` |  `GET /v1/{parent=projects/*/locations/*}:fetchFrameworks`   
Fetches all frameworks for assessment report.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.spaces](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/create)` |  `POST /v1/{parent=projects/*/locations/*}/spaces`   
Creates a space.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*}`   
Deletes a space.  
`[generateTerraformPlanAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/generateTerraformPlanAssessmentReport)` |  `POST /v1/{name=projects/*/locations/*/spaces/*}:generateTerraformPlanAssessmentReport`   
Generate a Terraform plan assessment report for a given Terraform plan.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*}`   
Gets details about a space.  
`[getIamPolicy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/spaces/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/list)` |  `GET /v1/{parent=projects/*/locations/*}/spaces`   
Lists spaces in a given project and location.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/patch)` |  `PATCH /v1/{space.name=projects/*/locations/*/spaces/*}`   
Updates a space.  
`[registerAppHubApplicationResources](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/registerAppHubApplicationResources)` |  `POST /v1/{parent=projects/*/locations/*}/spaces:registerAppHubApplicationResources`   
Register deployed resources from terraform state file with App Hub without needing a space.  
`[setIamPolicy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/spaces/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/spaces/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.spaces.applicationTemplates](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates)

Methods  
---  
`[commit](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/commit)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:commit`   
Commits an application template to create a new revision.  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*}/applicationTemplates`   
Creates an application template.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}`   
Deletes an application template.  
`[export](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/export)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:export`   
Exports Terraform files for an application template.  
`[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/generate)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:generate`   
Generates Terraform files for an application template.  
`[generateAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/generateAssessmentReport)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:generateAssessmentReport`   
Generate assessment reports of an application template.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}`   
Gets details about an application template.  
`[import](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/import)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:import`   
Imports to an existing application template from a given shared template.  
`[importIaC](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/importIaC)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*}:importIaC`   
Imports IaC for an application template.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*}/applicationTemplates`   
Lists application templates in a given space.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates/patch)` |  `PATCH /v1/{applicationTemplate.name=projects/*/locations/*/spaces/*/applicationTemplates/*}`   
Updates an application template.  
  
## REST Resource: [v1.projects.locations.spaces.applicationTemplates.components](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/components`   
Creates a component.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}`   
Deletes a component.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}`   
Gets details about a Component.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/components`   
Lists components in an application template.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components/patch)` |  `PATCH /v1/{component.name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}`   
Updates a component.  
  
## REST Resource: [v1.projects.locations.spaces.applicationTemplates.components.connections](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}/connections`   
Creates a connection.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*/connections/*}`   
Deletes a connection.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*/connections/*}`   
Gets details about a connection.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*}/connections`   
Lists connections in an application template.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.components.connections/patch)` |  `PATCH /v1/{connection.name=projects/*/locations/*/spaces/*/applicationTemplates/*/components/*/connections/*}`   
Updates a connection.  
  
## REST Resource: [v1.projects.locations.spaces.applicationTemplates.policies](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/policies`   
Creates a policy for an application template.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/policies/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/policies/*}`   
Policy related APIs.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/policies`   
Lists policies for an application template.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.policies/patch)` |  `PATCH /v1/{policy.name=projects/*/locations/*/spaces/*/applicationTemplates/*/policies/*}`   
Updates a policy.  
  
## REST Resource: [v1.projects.locations.spaces.applicationTemplates.revisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions)

Methods  
---  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}`   
Deletes an application template revision.  
`[export](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/export)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}:export`   
Exports Terraform files for an application template revision.  
`[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/generate)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}:generate`   
Generates Terraform files for an application template revision.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/revisions/*}`   
Gets details about an application template revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/revisions`   
Lists application template revisions in a given application template.  
  
## REST Resource: [v1.projects.locations.spaces.applicationTemplates.systemRevisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.systemRevisions)

Methods  
---  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.systemRevisions/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applicationTemplates/*/systemRevisions/*}`   
Gets the given application template system revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applicationTemplates.systemRevisions/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/applicationTemplates/*}/systemRevisions`   
Lists application template system revisions in a given application template.  
  
## REST Resource: [v1.projects.locations.spaces.applications](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*}/applications`   
Creates an application.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/applications/*}`   
Deletes an application.  
`[deploy](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/deploy)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applications/*}:deploy`   
Deploys an application.  
`[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/fetchAssessmentReport)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applications/*}:fetchAssessmentReport`   
Fetches the assessment report of a deployed application if present.  
`[generate](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/generate)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applications/*}:generate`   
Generates Terraform files for an application.  
`[generateAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/generateAssessmentReport)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applications/*}:generateAssessmentReport`   
Generate assessment reports of an application.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/applications/*}`   
Gets details about an application.  
`[importIaC](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/importIaC)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applications/*}:importIaC`   
Imports IaC for an application resource.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*}/applications`   
Lists applications in a given space.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/patch)` |  `PATCH /v1/{application.name=projects/*/locations/*/spaces/*/applications/*}`   
Updates an application.  
`[preview](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.applications/preview)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/applications/*}:preview`   
Previews deployment of an application.  
  
## REST Resource: [v1.projects.locations.spaces.catalogs](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*}/catalogs`   
Creates a catalog.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/catalogs/*}`   
Deletes a catalog.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/catalogs/*}`   
Gets details about a catalog.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*}/catalogs`   
Lists catalogs in a given space.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs/patch)` |  `PATCH /v1/{catalog.name=projects/*/locations/*/spaces/*/catalogs/*}`   
Updates a catalog.  
  
## REST Resource: [v1.projects.locations.spaces.catalogs.shares](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.shares)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.shares/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*/catalogs/*}/shares`   
Shares a catalog from one space to another space.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.shares/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/shares/*}`   
Deletes a catalog share.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.shares/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/shares/*}`   
Get catalog share object for the space.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.shares/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/catalogs/*}/shares`   
Lists catalog share objects for the space.  
`[sync](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.shares/sync)` |  `POST /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/shares/*}:sync`   
Synchronizes a share and updates the destination workspace to reflect.  
  
## REST Resource: [v1.projects.locations.spaces.catalogs.templates](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*/catalogs/*}/templates`   
Adds a template to a catalog.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*}`   
Deletes a catalog template.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*}`   
Gets a catalog template.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/catalogs/*}/templates`   
Lists catalog templates.  
`[patch](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates/patch)` |  `PATCH /v1/{catalogTemplate.name=projects/*/locations/*/spaces/*/catalogs/*/templates/*}`   
Updates a catalog template resource.  
  
## REST Resource: [v1.projects.locations.spaces.catalogs.templates.revisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions)

Methods  
---  
`[create](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/create)` |  `POST /v1/{parent=projects/*/locations/*/spaces/*/catalogs/*/templates/*}/revisions`   
Creates a template revision.  
`[delete](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/delete)` |  `DELETE /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*/revisions/*}`   
Deletes a template revision.  
`[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/fetchAssessmentReport)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*/revisions/*}:fetchAssessmentReport`   
Fetches the assessment report of a catalog template revision if present.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/catalogs/*/templates/*/revisions/*}`   
Gets details about a template revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.catalogs.templates.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/catalogs/*/templates/*}/revisions`   
Lists template revisions.  
  
## REST Resource: [v1.projects.locations.spaces.sharedTemplates](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates)

Methods  
---  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/sharedTemplates/*}`   
Gets details about a shared template.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*}/sharedTemplates`   
Lists shared templates in a given space.  
  
## REST Resource: [v1.projects.locations.spaces.sharedTemplates.revisions](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions)

Methods  
---  
`[fetchAssessmentReport](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/fetchAssessmentReport)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/sharedTemplates/*/revisions/*}:fetchAssessmentReport`   
Fetches the assessment report of a shared template revision if present.  
`[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/spaces/*/sharedTemplates/*/revisions/*}`   
Gets details about a shared template revision.  
`[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/spaces/*/sharedTemplates/*}/revisions`   
Lists shared template revisions in a given space.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
