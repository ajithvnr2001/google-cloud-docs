---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/
title: Database Migration API \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:28.184969+00:00
---

# Database Migration API  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  Database Migration API Stay organized with collections  Save and categorize content based on your preferences. 

Manage Cloud Database Migration Service resources on Google Cloud Platform.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.connectionProfiles
  * REST Resource: v1beta1.projects.locations.migrationJobs
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1alpha2.projects.locations
  * REST Resource: v1alpha2.projects.locations.connectionProfiles
  * REST Resource: v1alpha2.projects.locations.migrationJobs
  * REST Resource: v1alpha2.projects.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.connectionProfiles
  * REST Resource: v1.projects.locations.conversionWorkspaces
  * REST Resource: v1.projects.locations.conversionWorkspaces.mappingRules
  * REST Resource: v1.projects.locations.migrationJobs
  * REST Resource: v1.projects.locations.migrationJobs.objects
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.privateConnections



## Service: datamigration.googleapis.com

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://datamigration.googleapis.com/$discovery/rest?version=v1>
  * <https://datamigration.googleapis.com/$discovery/rest?version=v1beta1>
  * <https://datamigration.googleapis.com/$discovery/rest?version=v1alpha2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://datamigration.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  

* `https://datamigration.googleapis.com`

## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.connectionProfiles](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/create)` |  `POST /v1beta1/{parent}/connectionProfiles`   
Creates a new connection profile in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/delete)` |  `DELETE /v1beta1/{name}`   
Deletes a single Database Migration Service connection profile.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/get)` |  `GET /v1beta1/{name}`   
Gets details of a single connection profile.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/getIamPolicy)` |  `GET /v1beta1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/list)` |  `GET /v1beta1/{parent}/connectionProfiles`   
Retrieve a list of all connection profiles in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/patch)` |  `PATCH /v1beta1/{connectionProfile.name}`   
Update the configuration of a single connection profile.  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/setIamPolicy)` |  `POST /v1beta1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.connectionProfiles/testIamPermissions)` |  `POST /v1beta1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1beta1.projects.locations.migrationJobs](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/create)` |  `POST /v1beta1/{parent}/migrationJobs`   
Creates a new migration job in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/delete)` |  `DELETE /v1beta1/{name}`   
Deletes a single migration job.  
`[generateSshScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/generateSshScript)` |  `POST /v1beta1/{migrationJob}:generateSshScript`   
Generate a SSH configuration script to configure the reverse SSH connectivity.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/get)` |  `GET /v1beta1/{name}`   
Gets details of a single migration job.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/getIamPolicy)` |  `GET /v1beta1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/list)` |  `GET /v1beta1/{parent}/migrationJobs`   
Lists migration jobs in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/patch)` |  `PATCH /v1beta1/{migrationJob.name}`   
Updates the parameters of a single migration job.  
`[promote](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/promote)` |  `POST /v1beta1/{name}:promote`   
Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.  
`[restart](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/restart)` |  `POST /v1beta1/{name}:restart`   
Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.  
`[resume](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/resume)` |  `POST /v1beta1/{name}:resume`   
Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/setIamPolicy)` |  `POST /v1beta1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[start](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/start)` |  `POST /v1beta1/{name}:start`   
Start an already created migration job.  
`[stop](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/stop)` |  `POST /v1beta1/{name}:stop`   
Stops a running migration job.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/testIamPermissions)` |  `POST /v1beta1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[verify](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.migrationJobs/verify)` |  `POST /v1beta1/{name}:verify`   
Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha2.projects.locations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations/get)` |  `GET /v1alpha2/{name}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations/list)` |  `GET /v1alpha2/{name}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha2.projects.locations.connectionProfiles](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/create)` |  `POST /v1alpha2/{parent}/connectionProfiles`   
Creates a new connection profile in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/delete)` |  `DELETE /v1alpha2/{name}`   
Deletes a single Database Migration Service connection profile.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/get)` |  `GET /v1alpha2/{name}`   
Gets details of a single connection profile.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/getIamPolicy)` |  `GET /v1alpha2/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/list)` |  `GET /v1alpha2/{parent}/connectionProfiles`   
Retrieve a list of all connection profiles in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/patch)` |  `PATCH /v1alpha2/{connectionProfile.name}`   
Update the configuration of a single connection profile.  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/setIamPolicy)` |  `POST /v1alpha2/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.connectionProfiles/testIamPermissions)` |  `POST /v1alpha2/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1alpha2.projects.locations.migrationJobs](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/create)` |  `POST /v1alpha2/{parent}/migrationJobs`   
Creates a new migration job in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/delete)` |  `DELETE /v1alpha2/{name}`   
Deletes a single migration job.  
`[generateSshScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript)` |  `POST /v1alpha2/{name}:generateSshScript`   
Generate a SSH configuration script to configure the reverse SSH connectivity.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/get)` |  `GET /v1alpha2/{name}`   
Gets details of a single migration job.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/getIamPolicy)` |  `GET /v1alpha2/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/list)` |  `GET /v1alpha2/{parent}/migrationJobs`   
Lists migration jobs in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/patch)` |  `PATCH /v1alpha2/{migrationJob.name}`   
Updates the parameters of a single migration job.  
`[promote](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/promote)` |  `POST /v1alpha2/{name}:promote`   
Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.  
`[restart](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/restart)` |  `POST /v1alpha2/{name}:restart`   
Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.  
`[resume](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/resume)` |  `POST /v1alpha2/{name}:resume`   
Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/setIamPolicy)` |  `POST /v1alpha2/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[start](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/start)` |  `POST /v1alpha2/{name}:start`   
Start an already created migration job.  
`[stop](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/stop)` |  `POST /v1alpha2/{name}:stop`   
Stops a running migration job.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/testIamPermissions)` |  `POST /v1alpha2/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[verify](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/verify)` |  `POST /v1alpha2/{name}:verify`   
Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.  
  
## REST Resource: [v1alpha2.projects.locations.operations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.operations/cancel)` |  `POST /v1alpha2/{name}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.operations/delete)` |  `DELETE /v1alpha2/{name}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.operations/get)` |  `GET /v1alpha2/{name}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.operations/list)` |  `GET /v1alpha2/{name}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[fetchStaticIps](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations/fetchStaticIps)` |  `GET /v1/{name}:fetchStaticIps`   
Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.connectionProfiles](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/create)` |  `POST /v1/{parent}/connectionProfiles`   
Creates a new connection profile in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/delete)` |  `DELETE /v1/{name}`   
Deletes a single Database Migration Service connection profile.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/get)` |  `GET /v1/{name}`   
Gets details of a single connection profile.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/getIamPolicy)` |  `GET /v1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/list)` |  `GET /v1/{parent}/connectionProfiles`   
Retrieves a list of all connection profiles in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/patch)` |  `PATCH /v1/{connectionProfile.name}`   
Update the configuration of a single connection profile.  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/setIamPolicy)` |  `POST /v1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.connectionProfiles/testIamPermissions)` |  `POST /v1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.conversionWorkspaces](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces)

Methods  
---  
`[apply](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/apply)` |  `POST /v1/{name}:apply`   
Applies draft tree onto a specific destination database.  
`[commit](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/commit)` |  `POST /v1/{name}:commit`   
Marks all the data in the conversion workspace as committed.  
`[convert](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/convert)` |  `POST /v1/{name}:convert`   
Creates a draft tree schema for the destination database.  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/create)` |  `POST /v1/{parent}/conversionWorkspaces`   
Creates a new conversion workspace in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/delete)` |  `DELETE /v1/{name}`   
Deletes a single conversion workspace.  
`[describeConversionWorkspaceRevisions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeConversionWorkspaceRevisions)` |  `GET /v1/{conversionWorkspace}:describeConversionWorkspaceRevisions`   
Retrieves a list of committed revisions of a specific conversion workspace.  
`[describeDatabaseEntities](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities)` |  `GET /v1/{conversionWorkspace}:describeDatabaseEntities`   
Describes the database entities tree for a specific conversion workspace and a specific tree type.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/get)` |  `GET /v1/{name}`   
Gets details of a single conversion workspace.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/getIamPolicy)` |  `GET /v1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/list)` |  `GET /v1/{parent}/conversionWorkspaces`   
Lists conversion workspaces in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/patch)` |  `PATCH /v1/{conversionWorkspace.name}`   
Updates the parameters of a single conversion workspace.  
`[rollback](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/rollback)` |  `POST /v1/{name}:rollback`   
Rolls back a conversion workspace to the last committed snapshot.  
`[searchBackgroundJobs](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs)` |  `GET /v1/{conversionWorkspace}:searchBackgroundJobs`   
Searches/lists the background jobs for a specific conversion workspace.  
`[seed](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/seed)` |  `POST /v1/{name}:seed`   
Imports a snapshot of the source database into the conversion workspace.  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/setIamPolicy)` |  `POST /v1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/testIamPermissions)` |  `POST /v1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.conversionWorkspaces.mappingRules](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/create)` |  `POST /v1/{parent}/mappingRules`   
Creates a new mapping rule for a given conversion workspace.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/delete)` |  `DELETE /v1/{name}`   
Deletes a single mapping rule.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/get)` |  `GET /v1/{name}`   
Gets the details of a mapping rule.  
`[import](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/import)` |  `POST /v1/{parent}/mappingRules:import`   
Imports the mapping rules for a given conversion workspace.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces.mappingRules/list)` |  `GET /v1/{parent}/mappingRules`   
Lists the mapping rules for a specific conversion workspace.  
  
## REST Resource: [v1.projects.locations.migrationJobs](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/create)` |  `POST /v1/{parent}/migrationJobs`   
Creates a new migration job in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/delete)` |  `DELETE /v1/{name}`   
Deletes a single migration job.  
`[demoteDestination](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/demoteDestination)` |  `POST /v1/{name}:demoteDestination`   
Demotes the destination database to become a read replica of the source.  
`[fetchSourceObjects](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/fetchSourceObjects)` |  `GET /v1/{name}:fetchSourceObjects`   
Retrieves objects from the source database that can be selected for data migration.  
`[generateSshScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateSshScript)` |  `POST /v1/{migrationJob}:generateSshScript`   
Generate a SSH configuration script to configure the reverse SSH connectivity.  
`[generateTcpProxyScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/generateTcpProxyScript)` |  `POST /v1/{migrationJob}:generateTcpProxyScript`   
Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/get)` |  `GET /v1/{name}`   
Gets details of a single migration job.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/getIamPolicy)` |  `GET /v1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/list)` |  `GET /v1/{parent}/migrationJobs`   
Lists migration jobs in a given project and location.  
`[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/patch)` |  `PATCH /v1/{migrationJob.name}`   
Updates the parameters of a single migration job.  
`[promote](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/promote)` |  `POST /v1/{name}:promote`   
Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.  
`[restart](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/restart)` |  `POST /v1/{name}:restart`   
Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.  
`[resume](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/resume)` |  `POST /v1/{name}:resume`   
Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/setIamPolicy)` |  `POST /v1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[start](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/start)` |  `POST /v1/{name}:start`   
Start an already created migration job.  
`[stop](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/stop)` |  `POST /v1/{name}:stop`   
Stops a running migration job.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/testIamPermissions)` |  `POST /v1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[verify](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs/verify)` |  `POST /v1/{name}:verify`   
Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.  
  
## REST Resource: [v1.projects.locations.migrationJobs.objects](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects)

Methods  
---  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/get)` |  `GET /v1/{name}`   
Use this method to get details about a migration job object.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/getIamPolicy)` |  `GET /v1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/list)` |  `GET /v1/{parent}/objects`   
Use this method to list the objects of a specific migration job.  
`[lookup](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/lookup)` |  `POST /v1/{parent}/objects:lookup`   
Use this method to look up a migration job object by its source object identifier.  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/setIamPolicy)` |  `POST /v1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/testIamPermissions)` |  `POST /v1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.privateConnections](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections)

Methods  
---  
`[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/create)` |  `POST /v1/{parent}/privateConnections`   
Creates a new private connection in a given project and location.  
`[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/delete)` |  `DELETE /v1/{name}`   
Deletes a single Database Migration Service private connection.  
`[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/get)` |  `GET /v1/{name}`   
Gets details of a single private connection.  
`[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/getIamPolicy)` |  `GET /v1/{resource}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/list)` |  `GET /v1/{parent}/privateConnections`   
Retrieves a list of private connections in a given project and location.  
`[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/setIamPolicy)` |  `POST /v1/{resource}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.privateConnections/testIamPermissions)` |  `POST /v1/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
