---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/
title: VM Migration API \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:40.668150+00:00
---

# VM Migration API  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  VM Migration API Stay organized with collections  Save and categorize content based on your preferences. 

Use the Migrate to Virtual Machines API to programmatically migrate workloads.

  * REST Resource: v1alpha1.projects.locations
  * REST Resource: v1alpha1.projects.locations.groups
  * REST Resource: v1alpha1.projects.locations.imageImports
  * REST Resource: v1alpha1.projects.locations.imageImports.imageImportJobs
  * REST Resource: v1alpha1.projects.locations.operations
  * REST Resource: v1alpha1.projects.locations.sources
  * REST Resource: v1alpha1.projects.locations.sources.datacenterConnectors
  * REST Resource: v1alpha1.projects.locations.sources.migratingVms
  * REST Resource: v1alpha1.projects.locations.sources.migratingVms.cloneJobs
  * REST Resource: v1alpha1.projects.locations.sources.migratingVms.cutoverJobs
  * REST Resource: v1alpha1.projects.locations.sources.migratingVms.replicationCycles
  * REST Resource: v1alpha1.projects.locations.sources.utilizationReports
  * REST Resource: v1alpha1.projects.locations.targetProjects



## Service: vmmigration.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://vmmigration.googleapis.com`



## REST Resource: [v1alpha1.projects.locations](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations/list)` |  `GET /v1alpha1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha1.projects.locations.groups](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups)

Methods  
---  
`[addGroupMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/addGroupMigration)` |  `POST /v1alpha1/{group=projects/*/locations/*/groups/*}:addGroupMigration`   
Adds a MigratingVm to a Group.  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/groups`   
Creates a new Group in a given project and location.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/groups/*}`   
Deletes a single Group.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/groups/*}`   
Gets details of a single Group.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/groups`   
Lists Groups in a given project and location.  
`[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/patch)` |  `PATCH /v1alpha1/{group.name=projects/*/locations/*/groups/*}`   
Updates the parameters of a single Group.  
`[removeGroupMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.groups/removeGroupMigration)` |  `POST /v1alpha1/{group=projects/*/locations/*/groups/*}:removeGroupMigration`   
Removes a MigratingVm from a Group.  
  
## REST Resource: [v1alpha1.projects.locations.imageImports](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports)

Methods  
---  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/imageImports`   
Creates a new ImageImport in a given project.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/imageImports/*}`   
Deletes a single ImageImport.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/imageImports/*}`   
Gets details of a single ImageImport.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/imageImports`   
Lists ImageImports in a given project.  
  
## REST Resource: [v1alpha1.projects.locations.imageImports.imageImportJobs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports.imageImportJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports.imageImportJobs/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/imageImports/*/imageImportJobs/*}:cancel`   
Initiates the cancellation of a running clone job.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports.imageImportJobs/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/imageImports/*/imageImportJobs/*}`   
Gets details of a single ImageImportJob.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.imageImports.imageImportJobs/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/imageImports/*}/imageImportJobs`   
Lists ImageImportJobs in a given project.  
  
## REST Resource: [v1alpha1.projects.locations.operations](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.operations/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.operations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.operations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.operations/list)` |  `GET /v1alpha1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha1.projects.locations.sources](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources)

Methods  
---  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/sources`   
Creates a new Source in a given project and location.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/sources/*}`   
Deletes a single Source.  
`[fetchInventory](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/fetchInventory)` |  `GET /v1alpha1/{source=projects/*/locations/*/sources/*}:fetchInventory`   
List remote source's inventory of VMs.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*}`   
Gets details of a single Source.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/sources`   
Lists Sources in a given project and location.  
`[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources/patch)` |  `PATCH /v1alpha1/{source.name=projects/*/locations/*/sources/*}`   
Updates the parameters of a single Source.  
  
## REST Resource: [v1alpha1.projects.locations.sources.datacenterConnectors](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.datacenterConnectors)

Methods  
---  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.datacenterConnectors/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/sources/*}/datacenterConnectors`   
Creates a new DatacenterConnector in a given Source.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.datacenterConnectors/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/sources/*/datacenterConnectors/*}`   
Deletes a single DatacenterConnector.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.datacenterConnectors/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*/datacenterConnectors/*}`   
Gets details of a single DatacenterConnector.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.datacenterConnectors/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/sources/*}/datacenterConnectors`   
Lists DatacenterConnectors in a given Source.  
`[upgradeAppliance](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.datacenterConnectors/upgradeAppliance)` |  `POST /v1alpha1/{datacenterConnector=projects/*/locations/*/sources/*/datacenterConnectors/*}:upgradeAppliance`   
Upgrades the appliance relate to this DatacenterConnector to the in-place updateable version.  
  
## REST Resource: [v1alpha1.projects.locations.sources.migratingVms](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms)

Methods  
---  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/sources/*}/migratingVms`   
Creates a new MigratingVm in a given Source.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*}`   
Deletes a single MigratingVm.  
`[finalizeMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/finalizeMigration)` |  `POST /v1alpha1/{migratingVm=projects/*/locations/*/sources/*/migratingVms/*}:finalizeMigration`   
Marks a migration as completed, deleting migration resources that are no longer being used.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*}`   
Gets details of a single MigratingVm.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/sources/*}/migratingVms`   
Lists MigratingVms in a given Source.  
`[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/patch)` |  `PATCH /v1alpha1/{migratingVm.name=projects/*/locations/*/sources/*/migratingVms/*}`   
Updates the parameters of a single MigratingVm.  
`[pauseMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/pauseMigration)` |  `POST /v1alpha1/{migratingVm=projects/*/locations/*/sources/*/migratingVms/*}:pauseMigration`   
Pauses a migration for a VM.  
`[resumeMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/resumeMigration)` |  `POST /v1alpha1/{migratingVm=projects/*/locations/*/sources/*/migratingVms/*}:resumeMigration`   
Resumes a migration for a VM.  
`[startMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms/startMigration)` |  `POST /v1alpha1/{migratingVm=projects/*/locations/*/sources/*/migratingVms/*}:startMigration`   
Starts migration for a VM.  
  
## REST Resource: [v1alpha1.projects.locations.sources.migratingVms.cloneJobs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*/cloneJobs/*}:cancel`   
Initiates the cancellation of a running clone job.  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/sources/*/migratingVms/*}/cloneJobs`   
Initiates a Clone of a specific migrating VM.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*/cloneJobs/*}`   
Gets details of a single CloneJob.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cloneJobs/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/sources/*/migratingVms/*}/cloneJobs`   
Lists the CloneJobs of a migrating VM.  
  
## REST Resource: [v1alpha1.projects.locations.sources.migratingVms.cutoverJobs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs)

Methods  
---  
`[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*/cutoverJobs/*}:cancel`   
Initiates the cancellation of a running cutover job.  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/sources/*/migratingVms/*}/cutoverJobs`   
Initiates a Cutover of a specific migrating VM.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*/cutoverJobs/*}`   
Gets details of a single CutoverJob.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.cutoverJobs/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/sources/*/migratingVms/*}/cutoverJobs`   
Lists the CutoverJobs of a migrating VM.  
  
## REST Resource: [v1alpha1.projects.locations.sources.migratingVms.replicationCycles](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles)

Methods  
---  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*/migratingVms/*/replicationCycles/*}`   
Gets details of a single ReplicationCycle.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.migratingVms.replicationCycles/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/sources/*/migratingVms/*}/replicationCycles`   
Lists ReplicationCycles in a given MigratingVM.  
  
## REST Resource: [v1alpha1.projects.locations.sources.utilizationReports](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports)

Methods  
---  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*/sources/*}/utilizationReports`   
Creates a new UtilizationReport.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/sources/*/utilizationReports/*}`   
Deletes a single Utilization Report.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/sources/*/utilizationReports/*}`   
Gets a single Utilization Report.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.sources.utilizationReports/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/sources/*}/utilizationReports`   
Lists Utilization Reports of the given Source.  
  
## REST Resource: [v1alpha1.projects.locations.targetProjects](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects)

Methods  
---  
`[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/targetProjects`   
Creates a new TargetProject in a given project.  
`[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/targetProjects/*}`   
Deletes a single TargetProject.  
`[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/targetProjects/*}`   
Gets details of a single TargetProject.  
`[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/targetProjects`   
Lists TargetProjects in a given project.  
`[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1alpha1/projects.locations.targetProjects/patch)` |  `PATCH /v1alpha1/{targetProject.name=projects/*/locations/*/targetProjects/*}`   
Updates the parameters of a single TargetProject.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
