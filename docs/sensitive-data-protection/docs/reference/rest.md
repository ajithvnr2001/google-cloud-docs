---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/
title: Sensitive Data Protection (DLP API) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:21.992394+00:00
---

# Sensitive Data Protection (DLP API)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  Sensitive Data Protection (DLP API) Stay organized with collections  Save and categorize content based on your preferences. 

Provides methods for detection of privacy-sensitive fragments in text, images, and Google Cloud Platform storage repositories. The Cloud Data Loss Prevention API (DLP API) is part of [Sensitive Data Protection](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview).

  * REST Resource: v2.infoTypes
  * REST Resource: v2.locations.infoTypes
  * REST Resource: v2.organizations.locations.columnDataProfiles
  * REST Resource: v2.organizations.locations.connections
  * REST Resource: v2.organizations.locations.discoveryConfigs
  * REST Resource: v2.organizations.locations.fileStoreDataProfiles
  * REST Resource: v2.organizations.locations.projectDataProfiles
  * REST Resource: v2.organizations.locations.tableDataProfiles
  * REST Resource: v2.projects.content
  * REST Resource: v2.projects.deidentifyTemplates
  * REST Resource: v2.projects.dlpJobs
  * REST Resource: v2.projects.image
  * REST Resource: v2.projects.inspectTemplates
  * REST Resource: v2.projects.jobTriggers
  * REST Resource: v2.projects.locations.columnDataProfiles
  * REST Resource: v2.projects.locations.connections
  * REST Resource: v2.projects.locations.content
  * REST Resource: v2.projects.locations.contentPolicies
  * REST Resource: v2.projects.locations.deidentifyTemplates
  * REST Resource: v2.projects.locations.discoveryConfigs
  * REST Resource: v2.projects.locations.dlpJobs
  * REST Resource: v2.projects.locations.fileStoreDataProfiles
  * REST Resource: v2.projects.locations.image
  * REST Resource: v2.projects.locations.inspectTemplates
  * REST Resource: v2.projects.locations.jobTriggers
  * REST Resource: v2.projects.locations.projectDataProfiles
  * REST Resource: v2.projects.locations.storedInfoTypes
  * REST Resource: v2.projects.locations.tableDataProfiles
  * REST Resource: v2.projects.storedInfoTypes



## Service: dlp.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://dlp.googleapis.com/$discovery/rest?version=v2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://dlp.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us eu in

  

* `https://dlp.googleapis.com`

## REST Resource: [v2.infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/infoTypes)

Methods  
---  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/infoTypes/list)` |  `GET /v2/infoTypes`   
Returns a list of the sensitive information types that the DLP API supports.  
  
## REST Resource: [v2.locations.infoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/locations.infoTypes)

Methods  
---  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/locations.infoTypes/list)` |  `GET /v2/{parent=locations/*}/infoTypes`   
Returns a list of the sensitive information types that the DLP API supports.  
  
## REST Resource: [v2.organizations.locations.columnDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles)

Methods  
---  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles/get)` |  `GET /v2/{name=organizations/*/locations/*/columnDataProfiles/*}`   
Gets a column data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.columnDataProfiles/list)` |  `GET /v2/{parent=organizations/*/locations/*}/columnDataProfiles`   
Lists column data profiles for an organization.  
  
## REST Resource: [v2.organizations.locations.connections](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/create)` |  `POST /v2/{parent=organizations/*/locations/*}/connections`   
Create a Connection to an external data source.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/delete)` |  `DELETE /v2/{name=organizations/*/locations/*/connections/*}`   
Delete a Connection.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/get)` |  `GET /v2/{name=organizations/*/locations/*/connections/*}`   
Get a Connection by name.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/list)` |  `GET /v2/{parent=organizations/*/locations/*}/connections`   
Lists Connections in a parent.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/patch)` |  `PATCH /v2/{name=organizations/*/locations/*/connections/*}`   
Update a Connection.  
`[search](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.connections/search)` |  `GET /v2/{parent=organizations/*/locations/*}/connections:search`   
Searches for Connections in a parent.  
  
## REST Resource: [v2.organizations.locations.discoveryConfigs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/create)` |  `POST /v2/{parent=organizations/*/locations/*}/discoveryConfigs`   
Creates a config for discovery to scan and profile storage.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/delete)` |  `DELETE /v2/{name=organizations/*/locations/*/discoveryConfigs/*}`   
Deletes a discovery configuration.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/get)` |  `GET /v2/{name=organizations/*/locations/*/discoveryConfigs/*}`   
Gets a discovery configuration.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/list)` |  `GET /v2/{parent=organizations/*/locations/*}/discoveryConfigs`   
Lists discovery configurations.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.discoveryConfigs/patch)` |  `PATCH /v2/{name=organizations/*/locations/*/discoveryConfigs/*}`   
Updates a discovery configuration.  
  
## REST Resource: [v2.organizations.locations.fileStoreDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles)

Methods  
---  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles/delete)` |  `DELETE /v2/{name=organizations/*/locations/*/fileStoreDataProfiles/*}`   
Delete a FileStoreDataProfile.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles/get)` |  `GET /v2/{name=organizations/*/locations/*/fileStoreDataProfiles/*}`   
Gets a file store data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.fileStoreDataProfiles/list)` |  `GET /v2/{parent=organizations/*/locations/*}/fileStoreDataProfiles`   
Lists file store data profiles for an organization.  
  
## REST Resource: [v2.organizations.locations.projectDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.projectDataProfiles)

Methods  
---  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.projectDataProfiles/get)` |  `GET /v2/{name=organizations/*/locations/*/projectDataProfiles/*}`   
Gets a project data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.projectDataProfiles/list)` |  `GET /v2/{parent=organizations/*/locations/*}/projectDataProfiles`   
Lists project data profiles for an organization.  
  
## REST Resource: [v2.organizations.locations.tableDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles)

Methods  
---  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles/delete)` |  `DELETE /v2/{name=organizations/*/locations/*/tableDataProfiles/*}`   
Delete a TableDataProfile.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles/get)` |  `GET /v2/{name=organizations/*/locations/*/tableDataProfiles/*}`   
Gets a table data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.locations.tableDataProfiles/list)` |  `GET /v2/{parent=organizations/*/locations/*}/tableDataProfiles`   
Lists table data profiles for an organization.  
  
## REST Resource: [v2.projects.content](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content)

Methods  
---  
`[deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify)` |  `POST /v2/{parent=projects/*}/content:deidentify`   
De-identifies potentially sensitive info from a ContentItem.  
`[inspect](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect)` |  `POST /v2/{parent=projects/*}/content:inspect`   
Finds potentially sensitive info in content.  
`[reidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify)` |  `POST /v2/{parent=projects/*}/content:reidentify`   
Re-identifies content that has been de-identified.  
  
## REST Resource: [v2.projects.deidentifyTemplates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/create)` |  `POST /v2/{parent=projects/*}/deidentifyTemplates`   
Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/delete)` |  `DELETE /v2/{name=projects/*/deidentifyTemplates/*}`   
Deletes a DeidentifyTemplate.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/get)` |  `GET /v2/{name=projects/*/deidentifyTemplates/*}`   
Gets a DeidentifyTemplate.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/list)` |  `GET /v2/{parent=projects/*}/deidentifyTemplates`   
Lists DeidentifyTemplates.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates/patch)` |  `PATCH /v2/{name=projects/*/deidentifyTemplates/*}`   
Updates the DeidentifyTemplate.  
  
## REST Resource: [v2.projects.dlpJobs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/cancel)` |  `POST /v2/{name=projects/*/dlpJobs/*}:cancel`   
Starts asynchronous cancellation on a long-running DlpJob.  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/create)` |  `POST /v2/{parent=projects/*}/dlpJobs`   
Creates a new job to inspect storage or calculate risk metrics.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/delete)` |  `DELETE /v2/{name=projects/*/dlpJobs/*}`   
Deletes a long-running DlpJob.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/get)` |  `GET /v2/{name=projects/*/dlpJobs/*}`   
Gets the latest state of a long-running DlpJob.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.dlpJobs/list)` |  `GET /v2/{parent=projects/*}/dlpJobs`   
Lists DlpJobs that match the specified filter in the request.  
  
## REST Resource: [v2.projects.image](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image)

Methods  
---  
`[redact](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.image/redact)` |  `POST /v2/{parent=projects/*}/image:redact`   
Redacts potentially sensitive info from an image.  
  
## REST Resource: [v2.projects.inspectTemplates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/create)` |  `POST /v2/{parent=projects/*}/inspectTemplates`   
Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/delete)` |  `DELETE /v2/{name=projects/*/inspectTemplates/*}`   
Deletes an InspectTemplate.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/get)` |  `GET /v2/{name=projects/*/inspectTemplates/*}`   
Gets an InspectTemplate.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/list)` |  `GET /v2/{parent=projects/*}/inspectTemplates`   
Lists InspectTemplates.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.inspectTemplates/patch)` |  `PATCH /v2/{name=projects/*/inspectTemplates/*}`   
Updates the InspectTemplate.  
  
## REST Resource: [v2.projects.jobTriggers](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers)

Methods  
---  
`[activate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/activate)` |  `POST /v2/{name=projects/*/jobTriggers/*}:activate`   
Activate a job trigger.  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/create)` |  `POST /v2/{parent=projects/*}/jobTriggers`   
Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/delete)` |  `DELETE /v2/{name=projects/*/jobTriggers/*}`   
Deletes a job trigger.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/get)` |  `GET /v2/{name=projects/*/jobTriggers/*}`   
Gets a job trigger.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/list)` |  `GET /v2/{parent=projects/*}/jobTriggers`   
Lists job triggers.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/patch)` |  `PATCH /v2/{name=projects/*/jobTriggers/*}`   
Updates a job trigger.  
  
## REST Resource: [v2.projects.locations.columnDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.columnDataProfiles)

Methods  
---  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.columnDataProfiles/get)` |  `GET /v2/{name=projects/*/locations/*/columnDataProfiles/*}`   
Gets a column data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.columnDataProfiles/list)` |  `GET /v2/{parent=projects/*/locations/*}/columnDataProfiles`   
Lists column data profiles for an organization.  
  
## REST Resource: [v2.projects.locations.connections](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/create)` |  `POST /v2/{parent=projects/*/locations/*}/connections`   
Create a Connection to an external data source.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/delete)` |  `DELETE /v2/{name=projects/*/locations/*/connections/*}`   
Delete a Connection.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/get)` |  `GET /v2/{name=projects/*/locations/*/connections/*}`   
Get a Connection by name.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/list)` |  `GET /v2/{parent=projects/*/locations/*}/connections`   
Lists Connections in a parent.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/patch)` |  `PATCH /v2/{name=projects/*/locations/*/connections/*}`   
Update a Connection.  
`[search](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.connections/search)` |  `GET /v2/{parent=projects/*/locations/*}/connections:search`   
Searches for Connections in a parent.  
  
## REST Resource: [v2.projects.locations.content](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content)

Methods  
---  
`[deidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/deidentify)` |  `POST /v2/{parent=projects/*/locations/*}/content:deidentify`   
De-identifies potentially sensitive info from a ContentItem.  
`[inspect](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/inspect)` |  `POST /v2/{parent=projects/*/locations/*}/content:inspect`   
Finds potentially sensitive info in content.  
`[reidentify](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.content/reidentify)` |  `POST /v2/{parent=projects/*/locations/*}/content:reidentify`   
Re-identifies content that has been de-identified.  
  
## REST Resource: [v2.projects.locations.contentPolicies](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/create)` |  `POST /v2/{parent=projects/*/locations/*}/contentPolicies`   
Create a ContentPolicy.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/delete)` |  `DELETE /v2/{name=projects/*/locations/*/contentPolicies/*}`   
Delete a ContentPolicy.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/get)` |  `GET /v2/{name=projects/*/locations/*/contentPolicies/*}`   
Get a ContentPolicy.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/list)` |  `GET /v2/{parent=projects/*/locations/*}/contentPolicies`   
Lists ContentPolicies in a parent.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.contentPolicies/patch)` |  `PATCH /v2/{name=projects/*/locations/*/contentPolicies/*}`   
Update a ContentPolicy.  
  
## REST Resource: [v2.projects.locations.deidentifyTemplates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/create)` |  `POST /v2/{parent=projects/*/locations/*}/deidentifyTemplates`   
Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/delete)` |  `DELETE /v2/{name=projects/*/locations/*/deidentifyTemplates/*}`   
Deletes a DeidentifyTemplate.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/get)` |  `GET /v2/{name=projects/*/locations/*/deidentifyTemplates/*}`   
Gets a DeidentifyTemplate.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/list)` |  `GET /v2/{parent=projects/*/locations/*}/deidentifyTemplates`   
Lists DeidentifyTemplates.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/patch)` |  `PATCH /v2/{name=projects/*/locations/*/deidentifyTemplates/*}`   
Updates the DeidentifyTemplate.  
  
## REST Resource: [v2.projects.locations.discoveryConfigs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/create)` |  `POST /v2/{parent=projects/*/locations/*}/discoveryConfigs`   
Creates a config for discovery to scan and profile storage.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/delete)` |  `DELETE /v2/{name=projects/*/locations/*/discoveryConfigs/*}`   
Deletes a discovery configuration.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/get)` |  `GET /v2/{name=projects/*/locations/*/discoveryConfigs/*}`   
Gets a discovery configuration.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/list)` |  `GET /v2/{parent=projects/*/locations/*}/discoveryConfigs`   
Lists discovery configurations.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.discoveryConfigs/patch)` |  `PATCH /v2/{name=projects/*/locations/*/discoveryConfigs/*}`   
Updates a discovery configuration.  
  
## REST Resource: [v2.projects.locations.dlpJobs](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/cancel)` |  `POST /v2/{name=projects/*/locations/*/dlpJobs/*}:cancel`   
Starts asynchronous cancellation on a long-running DlpJob.  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/create)` |  `POST /v2/{parent=projects/*/locations/*}/dlpJobs`   
Creates a new job to inspect storage or calculate risk metrics.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/delete)` |  `DELETE /v2/{name=projects/*/locations/*/dlpJobs/*}`   
Deletes a long-running DlpJob.  
`[finish](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/finish)` |  `POST /v2/{name=projects/*/locations/*/dlpJobs/*}:finish`   
Finish a running hybrid DlpJob.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/get)` |  `GET /v2/{name=projects/*/locations/*/dlpJobs/*}`   
Gets the latest state of a long-running DlpJob.  
`[hybridInspect](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/hybridInspect)` |  `POST /v2/{name=projects/*/locations/*/dlpJobs/*}:hybridInspect`   
Inspect hybrid content and store findings to a job.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.dlpJobs/list)` |  `GET /v2/{parent=projects/*/locations/*}/dlpJobs`   
Lists DlpJobs that match the specified filter in the request.  
  
## REST Resource: [v2.projects.locations.fileStoreDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles)

Methods  
---  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles/delete)` |  `DELETE /v2/{name=projects/*/locations/*/fileStoreDataProfiles/*}`   
Delete a FileStoreDataProfile.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles/get)` |  `GET /v2/{name=projects/*/locations/*/fileStoreDataProfiles/*}`   
Gets a file store data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.fileStoreDataProfiles/list)` |  `GET /v2/{parent=projects/*/locations/*}/fileStoreDataProfiles`   
Lists file store data profiles for an organization.  
  
## REST Resource: [v2.projects.locations.image](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image)

Methods  
---  
`[redact](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.image/redact)` |  `POST /v2/{parent=projects/*/locations/*}/image:redact`   
Redacts potentially sensitive info from an image.  
  
## REST Resource: [v2.projects.locations.inspectTemplates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates/create)` |  `POST /v2/{parent=projects/*/locations/*}/inspectTemplates`   
Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates/delete)` |  `DELETE /v2/{name=projects/*/locations/*/inspectTemplates/*}`   
Deletes an InspectTemplate.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates/get)` |  `GET /v2/{name=projects/*/locations/*/inspectTemplates/*}`   
Gets an InspectTemplate.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates/list)` |  `GET /v2/{parent=projects/*/locations/*}/inspectTemplates`   
Lists InspectTemplates.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.inspectTemplates/patch)` |  `PATCH /v2/{name=projects/*/locations/*/inspectTemplates/*}`   
Updates the InspectTemplate.  
  
## REST Resource: [v2.projects.locations.jobTriggers](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers)

Methods  
---  
`[activate](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/activate)` |  `POST /v2/{name=projects/*/locations/*/jobTriggers/*}:activate`   
Activate a job trigger.  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/create)` |  `POST /v2/{parent=projects/*/locations/*}/jobTriggers`   
Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/delete)` |  `DELETE /v2/{name=projects/*/locations/*/jobTriggers/*}`   
Deletes a job trigger.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/get)` |  `GET /v2/{name=projects/*/locations/*/jobTriggers/*}`   
Gets a job trigger.  
`[hybridInspect](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/hybridInspect)` |  `POST /v2/{name=projects/*/locations/*/jobTriggers/*}:hybridInspect`   
Inspect hybrid content and store findings to a trigger.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/list)` |  `GET /v2/{parent=projects/*/locations/*}/jobTriggers`   
Lists job triggers.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.jobTriggers/patch)` |  `PATCH /v2/{name=projects/*/locations/*/jobTriggers/*}`   
Updates a job trigger.  
  
## REST Resource: [v2.projects.locations.projectDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.projectDataProfiles)

Methods  
---  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.projectDataProfiles/get)` |  `GET /v2/{name=projects/*/locations/*/projectDataProfiles/*}`   
Gets a project data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.projectDataProfiles/list)` |  `GET /v2/{parent=projects/*/locations/*}/projectDataProfiles`   
Lists project data profiles for an organization.  
  
## REST Resource: [v2.projects.locations.storedInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/create)` |  `POST /v2/{parent=projects/*/locations/*}/storedInfoTypes`   
Creates a pre-built stored infoType to be used for inspection.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/delete)` |  `DELETE /v2/{name=projects/*/locations/*/storedInfoTypes/*}`   
Deletes a stored infoType.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/get)` |  `GET /v2/{name=projects/*/locations/*/storedInfoTypes/*}`   
Gets a stored infoType.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/list)` |  `GET /v2/{parent=projects/*/locations/*}/storedInfoTypes`   
Lists stored infoTypes.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.storedInfoTypes/patch)` |  `PATCH /v2/{name=projects/*/locations/*/storedInfoTypes/*}`   
Updates the stored infoType by creating a new version.  
  
## REST Resource: [v2.projects.locations.tableDataProfiles](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles)

Methods  
---  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles/delete)` |  `DELETE /v2/{name=projects/*/locations/*/tableDataProfiles/*}`   
Delete a TableDataProfile.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles/get)` |  `GET /v2/{name=projects/*/locations/*/tableDataProfiles/*}`   
Gets a table data profile.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.tableDataProfiles/list)` |  `GET /v2/{parent=projects/*/locations/*}/tableDataProfiles`   
Lists table data profiles for an organization.  
  
## REST Resource: [v2.projects.storedInfoTypes](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes)

Methods  
---  
`[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/create)` |  `POST /v2/{parent=projects/*}/storedInfoTypes`   
Creates a pre-built stored infoType to be used for inspection.  
`[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/delete)` |  `DELETE /v2/{name=projects/*/storedInfoTypes/*}`   
Deletes a stored infoType.  
`[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/get)` |  `GET /v2/{name=projects/*/storedInfoTypes/*}`   
Gets a stored infoType.  
`[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/list)` |  `GET /v2/{parent=projects/*}/storedInfoTypes`   
Lists stored infoTypes.  
`[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes/patch)` |  `PATCH /v2/{name=projects/*/storedInfoTypes/*}`   
Updates the stored infoType by creating a new version.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
