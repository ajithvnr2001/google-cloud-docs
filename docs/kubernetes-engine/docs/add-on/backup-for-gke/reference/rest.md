---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/
title: Backup for GKE API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:12:01.290742+00:00
---

# Backup for GKE API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ APIs & Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest)



Send feedback 

#  Backup for GKE API Stay organized with collections  Save and categorize content based on your preferences. 

Backup for GKE is a managed Kubernetes workload backup and restore service for GKE clusters.

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.backupChannels
  * REST Resource: v1.projects.locations.backupChannels.backupPlanBindings
  * REST Resource: v1.projects.locations.backupPlans
  * REST Resource: v1.projects.locations.backupPlans.backups
  * REST Resource: v1.projects.locations.backupPlans.backups.volumeBackups
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.restoreChannels
  * REST Resource: v1.projects.locations.restoreChannels.restorePlanBindings
  * REST Resource: v1.projects.locations.restorePlans
  * REST Resource: v1.projects.locations.restorePlans.restores
  * REST Resource: v1.projects.locations.restorePlans.restores.volumeRestores



## Service: gkebackup.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://gkebackup.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://gkebackup.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global me-central1 me-central2 me-west1 europe-west6 africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west8 europe-west9 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  

* `https://gkebackup.googleapis.com`

## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.backupChannels](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/create)` |  `POST /v1/{parent=projects/*/locations/*}/backupChannels`   
Creates a new BackupChannel in a given location.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/delete)` |  `DELETE /v1/{name=projects/*/locations/*/backupChannels/*}`   
Deletes an existing BackupChannel.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/get)` |  `GET /v1/{name=projects/*/locations/*/backupChannels/*}`   
Retrieve the details of a single BackupChannel.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/list)` |  `GET /v1/{parent=projects/*/locations/*}/backupChannels`   
Lists BackupChannels in a given location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels/patch)` |  `PATCH /v1/{backupChannel.name=projects/*/locations/*/backupChannels/*}`   
Update a BackupChannel.  
  
## REST Resource: [v1.projects.locations.backupChannels.backupPlanBindings](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings/get)` |  `GET /v1/{name=projects/*/locations/*/backupChannels/*/backupPlanBindings/*}`   
Retrieve the details of a single BackupPlanBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupChannels.backupPlanBindings/list)` |  `GET /v1/{parent=projects/*/locations/*/backupChannels/*}/backupPlanBindings`   
Lists BackupPlanBindings in a given location.  
  
## REST Resource: [v1.projects.locations.backupPlans](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/create)` |  `POST /v1/{parent=projects/*/locations/*}/backupPlans`   
Creates a new BackupPlan in a given location.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/delete)` |  `DELETE /v1/{name=projects/*/locations/*/backupPlans/*}`   
Deletes an existing BackupPlan.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/get)` |  `GET /v1/{name=projects/*/locations/*/backupPlans/*}`   
Retrieve the details of a single BackupPlan.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/backupPlans/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[getTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/getTags)` |  `GET /v1/{name=projects/*/locations/*/backupPlans/*}:getTags`   
Returns tags directly bound to a GCP resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/list)` |  `GET /v1/{parent=projects/*/locations/*}/backupPlans`   
Lists BackupPlans in a given location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/patch)` |  `PATCH /v1/{backupPlan.name=projects/*/locations/*/backupPlans/*}`   
Update a BackupPlan.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/backupPlans/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[setTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/setTags)` |  `POST /v1/{name=projects/*/locations/*/backupPlans/*}:setTags`   
Updates tags directly bound to a GCP resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/backupPlans/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.backupPlans.backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/create)` |  `POST /v1/{parent=projects/*/locations/*/backupPlans/*}/backups`   
Creates a Backup for the given BackupPlan.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/backupPlans/*/backups/*}`   
Deletes an existing Backup.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/get)` |  `GET /v1/{name=projects/*/locations/*/backupPlans/*/backups/*}`   
Retrieve the details of a single Backup.  
`[getBackupIndexDownloadUrl](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/getBackupIndexDownloadUrl)` |  `GET /v1/{backup=projects/*/locations/*/backupPlans/*/backups/*}:getBackupIndexDownloadUrl`   
Retrieve the link to the backupIndex.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/backupPlans/*/backups/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/list)` |  `GET /v1/{parent=projects/*/locations/*/backupPlans/*}/backups`   
Lists the Backups for a given BackupPlan.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/patch)` |  `PATCH /v1/{backup.name=projects/*/locations/*/backupPlans/*/backups/*}`   
Update a Backup.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/backupPlans/*/backups/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/backupPlans/*/backups/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.backupPlans.backups.volumeBackups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/get)` |  `GET /v1/{name=projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*}`   
Retrieve the details of a single VolumeBackup.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/list)` |  `GET /v1/{parent=projects/*/locations/*/backupPlans/*/backups/*}/volumeBackups`   
Lists the VolumeBackups for a given Backup.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.backupPlans.backups.volumeBackups/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.restoreChannels](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/create)` |  `POST /v1/{parent=projects/*/locations/*}/restoreChannels`   
Creates a new RestoreChannel in a given location.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/delete)` |  `DELETE /v1/{name=projects/*/locations/*/restoreChannels/*}`   
Deletes an existing RestoreChannel.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/get)` |  `GET /v1/{name=projects/*/locations/*/restoreChannels/*}`   
Retrieve the details of a single RestoreChannel.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/list)` |  `GET /v1/{parent=projects/*/locations/*}/restoreChannels`   
Lists RestoreChannels in a given location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels/patch)` |  `PATCH /v1/{restoreChannel.name=projects/*/locations/*/restoreChannels/*}`   
Update a RestoreChannel.  
  
## REST Resource: [v1.projects.locations.restoreChannels.restorePlanBindings](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings/get)` |  `GET /v1/{name=projects/*/locations/*/restoreChannels/*/restorePlanBindings/*}`   
Retrieve the details of a single RestorePlanBinding.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restoreChannels.restorePlanBindings/list)` |  `GET /v1/{parent=projects/*/locations/*/restoreChannels/*}/restorePlanBindings`   
Lists RestorePlanBindings in a given location.  
  
## REST Resource: [v1.projects.locations.restorePlans](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/create)` |  `POST /v1/{parent=projects/*/locations/*}/restorePlans`   
Creates a new RestorePlan in a given location.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/delete)` |  `DELETE /v1/{name=projects/*/locations/*/restorePlans/*}`   
Deletes an existing RestorePlan.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/get)` |  `GET /v1/{name=projects/*/locations/*/restorePlans/*}`   
Retrieve the details of a single RestorePlan.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/restorePlans/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[getTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/getTags)` |  `GET /v1/{name=projects/*/locations/*/restorePlans/*}:getTags`   
Returns tags directly bound to a GCP resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/list)` |  `GET /v1/{parent=projects/*/locations/*}/restorePlans`   
Lists RestorePlans in a given location.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/patch)` |  `PATCH /v1/{restorePlan.name=projects/*/locations/*/restorePlans/*}`   
Update a RestorePlan.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/restorePlans/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[setTags](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/setTags)` |  `POST /v1/{name=projects/*/locations/*/restorePlans/*}:setTags`   
Updates tags directly bound to a GCP resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/restorePlans/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.restorePlans.restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores)

Methods  
---  
`[create](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/create)` |  `POST /v1/{parent=projects/*/locations/*/restorePlans/*}/restores`   
Creates a new Restore for the given RestorePlan.  
`[delete](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/delete)` |  `DELETE /v1/{name=projects/*/locations/*/restorePlans/*/restores/*}`   
Deletes an existing Restore.  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/get)` |  `GET /v1/{name=projects/*/locations/*/restorePlans/*/restores/*}`   
Retrieves the details of a single Restore.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/restorePlans/*/restores/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/list)` |  `GET /v1/{parent=projects/*/locations/*/restorePlans/*}/restores`   
Lists the Restores for a given RestorePlan.  
`[patch](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/patch)` |  `PATCH /v1/{restore.name=projects/*/locations/*/restorePlans/*/restores/*}`   
Update a Restore.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/restorePlans/*/restores/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/restorePlans/*/restores/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
## REST Resource: [v1.projects.locations.restorePlans.restores.volumeRestores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores)

Methods  
---  
`[get](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores/get)` |  `GET /v1/{name=projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*}`   
Retrieve the details of a single VolumeRestore.  
`[getIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores/getIamPolicy)` |  `GET /v1/{resource=projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores/list)` |  `GET /v1/{parent=projects/*/locations/*/restorePlans/*/restores/*}/volumeRestores`   
Lists the VolumeRestores for a given Restore.  
`[setIamPolicy](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores/setIamPolicy)` |  `POST /v1/{resource=projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/reference/rest/v1/projects.locations.restorePlans.restores.volumeRestores/testIamPermissions)` |  `POST /v1/{resource=projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
