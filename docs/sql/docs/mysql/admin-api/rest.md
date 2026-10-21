---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/
title: Cloud SQL Admin API \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:48.694081+00:00
---

# Cloud SQL Admin API  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL Admin API Stay organized with collections  Save and categorize content based on your preferences. 

API for Cloud SQL instance management.

  * REST Resource: v1beta4.backupRuns
  * REST Resource: v1beta4.backups
  * REST Resource: v1beta4.blueGreenDeployments
  * REST Resource: v1beta4.connect
  * REST Resource: v1beta4.databases
  * REST Resource: v1beta4.flags
  * REST Resource: v1beta4.instances
  * REST Resource: v1beta4.operations
  * REST Resource: v1beta4.projects.instances
  * REST Resource: v1beta4.sslCerts
  * REST Resource: v1beta4.tiers
  * REST Resource: v1beta4.users
  * REST Resource: v1.Backups
  * REST Resource: v1.backupRuns
  * REST Resource: v1.blueGreenDeployments
  * REST Resource: v1.connect
  * REST Resource: v1.databases
  * REST Resource: v1.flags
  * REST Resource: v1.instances
  * REST Resource: v1.operations
  * REST Resource: v1.projects.instances
  * REST Resource: v1.sslCerts
  * REST Resource: v1.tiers
  * REST Resource: v1.users



## Service: sqladmin.googleapis.com

### Service endpoint

A [service endpoint](https://google.aip.dev/9#api-service-endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints.

This service has the following global endpoint, to which all URIs below it are relative: 

  * `https://sqladmin.googleapis.com`



### Regional endpoints

Cloud SQL also supports _regional endpoints_. A regional endpoint is a base URL that specifies the network address of an API service hosted in a particular region. A regional endpoint takes the form,  
`sqladmin.{region}.rep.googleapis.com`, like this:

  * `https://sqladmin.us-central1.rep.googleapis.com`



For more information, see [Use Cloud SQL regional endpoints](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rep).

## REST Resource: [v1beta4.backupRuns](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns)

Methods  
---  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns/delete)` |  `DELETE /sql/v1beta4/projects/{project}/instances/{instance}/backupRuns/{id}`   
Deletes the backup taken by a backup run.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns/get)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/backupRuns/{id}`   
Retrieves a resource containing information about a backup run.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns/insert)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/backupRuns`   
Creates a new backup run on demand.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns/list)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/backupRuns`   
Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.  
  
## REST Resource: [v1beta4.backups](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups)

Methods  
---  
`[createBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/createBackup)` |  `POST /sql/v1beta4/{parent=projects/*}/backups`   
Creates a backup for a Cloud SQL instance.  
`[deleteBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/deleteBackup)` |  `DELETE /sql/v1beta4/{name=projects/*/backups/*}`   
Deletes the backup.  
`[getBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/getBackup)` |  `GET /sql/v1beta4/{name=projects/*/backups/*}`   
Retrieves a resource containing information about a backup.  
`[listBackups](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/listBackups)` |  `GET /sql/v1beta4/{parent=projects/*}/backups`   
Lists all backups associated with the project.  
`[updateBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backups/updateBackup)` |  `PATCH /sql/v1beta4/{backup.name=projects/*/backups/*}`   
Updates the retention period and the description of the backup.  
  
## REST Resource: [v1beta4.blueGreenDeployments](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/create)` |  `POST /sql/v1beta4/{parent=projects/*/locations/*}/blueGreenDeployments`   
Creates a blue-green deployment under a given project and location.  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/delete)` |  `DELETE /sql/v1beta4/{name=projects/*/locations/*/blueGreenDeployments/*}`   
Deletes a blue-green deployment, including metadata and underlying resources based on the deployment state.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/get)` |  `GET /sql/v1beta4/{name=projects/*/locations/*/blueGreenDeployments/*}`   
Retrieves a blue-green deployment resource under a given project and location.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/list)` |  `GET /sql/v1beta4/{parent=projects/*/locations/*}/blueGreenDeployments`   
Lists blue-green deployments under a given project.  
`[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/blueGreenDeployments/switchover)` |  `POST /sql/v1beta4/{name=projects/*/locations/*/blueGreenDeployments/*}:switchover`   
Switches over to green instance for a blue-green deployment.  
  
## REST Resource: [v1beta4.connect](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect)

Methods  
---  
`[generateEphemeralCert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/generateEphemeralCert)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}:generateEphemeralCert`   
Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/get)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/connectSettings`   
Retrieves connect settings about a Cloud SQL instance.  
`[resolve](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/connect/resolve)` |  `GET /sql/v1beta4/locations/{location}/dns/{dnsName}:resolveConnectSettings`   
Retrieves connect settings about a Cloud SQL instance using the instance DNS name.  
  
## REST Resource: [v1beta4.databases](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases)

Methods  
---  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/delete)` |  `DELETE /sql/v1beta4/projects/{project}/instances/{instance}/databases/{database}`   
Deletes a database from a Cloud SQL instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/get)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/databases/{database}`   
Retrieves a resource containing information about a database inside a Cloud SQL instance.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/insert)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/databases`   
Inserts a resource containing information about a database inside a Cloud SQL instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/list)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/databases`   
Lists databases in the specified Cloud SQL instance.  
`[patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/patch)` |  `PATCH /sql/v1beta4/projects/{project}/instances/{instance}/databases/{database}`   
Partially updates a resource containing information about a database inside a Cloud SQL instance.  
`[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/databases/update)` |  `PUT /sql/v1beta4/projects/{project}/instances/{instance}/databases/{database}`   
Updates a resource containing information about a database inside a Cloud SQL instance.  
  
## REST Resource: [v1beta4.flags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/flags)

Methods  
---  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/flags/list)` |  `GET /sql/v1beta4/flags`   
Lists all available database flags for Cloud SQL instances.  
  
## REST Resource: [v1beta4.instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)

Methods  
---  
`[ListServerCertificates](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/ListServerCertificates)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/listServerCertificates`   
Lists all versions of server certificates and certificate authorities (CAs) for the specified instance.  
`[RotateServerCertificate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/RotateServerCertificate)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/rotateServerCertificate`   
Rotates the server certificate version to one previously added with the addServerCertificate method.  
`[addServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/addServerCa)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/addServerCa`   
Add a new trusted Certificate Authority (CA) version for the specified instance.  
`[addServerCertificate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/addServerCertificate)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/addServerCertificate`   
Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA.  
`[clone](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/clone)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/clone`   
Creates a Cloud SQL instance as a clone of the source instance.  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/delete)` |  `DELETE /sql/v1beta4/projects/{project}/instances/{instance}`   
Deletes a Cloud SQL instance.  
`[demote](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demote)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/demote`   
Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.  
`[demoteMaster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demoteMaster)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/demoteMaster`   
Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.  
`[executeSql](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/executeSql)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/executeSql`   
Execute SQL statements.  
`[export](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/export)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/export`   
Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file.  
`[failover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/failover`   
Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}`   
Retrieves a resource containing information about a Cloud SQL instance.  
`[import](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/import)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/import`   
Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert)` |  `POST /sql/v1beta4/projects/{project}/instances`   
Creates a new Cloud SQL instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/list)` |  `GET /sql/v1beta4/projects/{project}/instances`   
Lists instances under a given project.  
`[listServerCas](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/listServerCas)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/listServerCas`   
Lists all of the trusted Certificate Authorities (CAs) for the specified instance.  
`[patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch)` |  `PATCH /sql/v1beta4/projects/{project}/instances/{instance}`   
Partially updates settings of a Cloud SQL instance by merging the request with the current configuration.  
`[pointInTimeRestore](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/pointInTimeRestore)` |  `POST /sql/v1beta4/{parent=projects/*}:pointInTimeRestore`   
Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.  
`[preCheckMajorVersionUpgrade](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/preCheckMajorVersionUpgrade)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/preCheckMajorVersionUpgrade`   
Execute MVU Pre-checks  
`[promoteReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/promoteReplica)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/promoteReplica`   
Promotes the read replica instance to be an independent Cloud SQL primary instance.  
`[reencrypt](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/reencrypt)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/reencrypt`   
Reencrypt CMEK instance with latest key version.  
`[resetSslConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/resetSslConfig)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/resetSslConfig`   
Deletes all client certificates and generates a new server SSL certificate for the instance.  
`[restart](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/restart)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/restart`   
Restarts a Cloud SQL instance.  
`[restoreBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/restoreBackup)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/restoreBackup`   
Restores a backup of a Cloud SQL instance.  
`[rotateServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/rotateServerCa`   
Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method.  
`[startReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/startReplica)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/startReplica`   
Starts the replication in the read replica instance.  
`[stopReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/stopReplica)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/stopReplica`   
Stops the replication in the read replica instance.  
`[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/switchover)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/switchover`   
Switches over from the primary instance to the DR replica instance.  
`[truncateLog](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/truncateLog)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/truncateLog`   
Truncate MySQL general and slow query log tables MySQL only.  
`[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/update)` |  `PUT /sql/v1beta4/projects/{project}/instances/{instance}`   
Updates settings of a Cloud SQL instance.  
  
## REST Resource: [v1beta4.operations](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/cancel)` |  `POST /sql/v1beta4/projects/{project}/operations/{operation}/cancel`   
Cancels an instance operation that has been performed on an instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/get)` |  `GET /sql/v1beta4/projects/{project}/operations/{operation}`   
Retrieves an instance operation that has been performed on an instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations/list)` |  `GET /sql/v1beta4/projects/{project}/operations`   
Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.  
  
## REST Resource: [v1beta4.projects.instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances)

Methods  
---  
`[getDiskShrinkConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances/getDiskShrinkConfig)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/getDiskShrinkConfig`   
Get Disk Shrink Config for a given instance.  
`[getLatestRecoveryTime](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances/getLatestRecoveryTime)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/getLatestRecoveryTime`   
Get Latest Recovery Time for a given instance.  
`[performDiskShrink](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances/performDiskShrink)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/performDiskShrink`   
Perform Disk Shrink on primary instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances/rescheduleMaintenance)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/rescheduleMaintenance`   
Reschedules the maintenance on the given instance.  
`[startExternalSync](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances/startExternalSync)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/startExternalSync`   
Start External primary instance migration.  
`[verifyExternalSyncSettings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/projects.instances/verifyExternalSyncSettings)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/verifyExternalSyncSettings`   
Verify External primary instance external sync settings.  
  
## REST Resource: [v1beta4.sslCerts](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts)

Methods  
---  
`[createEphemeral](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts/createEphemeral)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/createEphemeral`   
Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance.  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts/delete)` |  `DELETE /sql/v1beta4/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}`   
Deletes the SSL certificate.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts/get)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}`   
Retrieves a particular SSL certificate.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts/insert)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/sslCerts`   
Creates an SSL certificate and returns it along with the private key and server certificate authority.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts/list)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/sslCerts`   
Lists all of the current SSL certificates for the instance.  
  
## REST Resource: [v1beta4.tiers](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/tiers)

Methods  
---  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/tiers/list)` |  `GET /sql/v1beta4/projects/{project}/tiers`   
Lists all available machine types (tiers) for Cloud SQL, for example, `db-custom-1-3840`.  
  
## REST Resource: [v1beta4.users](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users)

Methods  
---  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/delete)` |  `DELETE /sql/v1beta4/projects/{project}/instances/{instance}/users`   
Deletes a user from a Cloud SQL instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/get)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/users/{name}`   
Retrieves a resource containing information about a user.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/insert)` |  `POST /sql/v1beta4/projects/{project}/instances/{instance}/users`   
Creates a new user in a Cloud SQL instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/list)` |  `GET /sql/v1beta4/projects/{project}/instances/{instance}/users`   
Lists users in the specified Cloud SQL instance.  
`[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/users/update)` |  `PUT /sql/v1beta4/projects/{project}/instances/{instance}/users`   
Updates an existing user in a Cloud SQL instance.  
  
## REST Resource: [v1.Backups](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups)

Methods  
---  
`[CreateBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/CreateBackup)` |  `POST /v1/{parent=projects/*}/backups`   
Creates a backup for a Cloud SQL instance.  
`[DeleteBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/DeleteBackup)` |  `DELETE /v1/{name=projects/*/backups/*}`   
Deletes the backup.  
`[GetBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/GetBackup)` |  `GET /v1/{name=projects/*/backups/*}`   
Retrieves a resource containing information about a backup.  
`[ListBackups](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/ListBackups)` |  `GET /v1/{parent=projects/*}/backups`   
Lists all backups associated with the project.  
`[UpdateBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/Backups/UpdateBackup)` |  `PATCH /v1/{backup.name=projects/*/backups/*}`   
Updates the retention period and description of the backup.  
  
## REST Resource: [v1.backupRuns](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns)

Methods  
---  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/delete)` |  `DELETE /v1/projects/{project}/instances/{instance}/backupRuns/{id}`   
Deletes the backup taken by a backup run.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/get)` |  `GET /v1/projects/{project}/instances/{instance}/backupRuns/{id}`   
Retrieves a resource containing information about a backup run.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/insert)` |  `POST /v1/projects/{project}/instances/{instance}/backupRuns`   
Creates a new backup run on demand.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/list)` |  `GET /v1/projects/{project}/instances/{instance}/backupRuns`   
Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.  
  
## REST Resource: [v1.blueGreenDeployments](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/create)` |  `POST /v1/{parent=projects/*/locations/*}/blueGreenDeployments`   
Creates a blue-green deployment under a given project and location.  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/blueGreenDeployments/*}`   
Deletes a blue-green deployment.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/get)` |  `GET /v1/{name=projects/*/locations/*/blueGreenDeployments/*}`   
Retrieves a blue-green deployment resource under a given project and location.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/list)` |  `GET /v1/{parent=projects/*/locations/*}/blueGreenDeployments`   
Lists blue-green deployments under a given project.  
`[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/blueGreenDeployments/switchover)` |  `POST /v1/{name=projects/*/locations/*/blueGreenDeployments/*}:switchover`   
Switches over to green instance for a blue-green deployment.  
  
## REST Resource: [v1.connect](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/connect)

Methods  
---  
`[generateEphemeralCert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/connect/generateEphemeralCert)` |  `POST /v1/projects/{project}/instances/{instance}:generateEphemeralCert`   
Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/connect/get)` |  `GET /v1/projects/{project}/instances/{instance}/connectSettings`   
Retrieves connect settings about a Cloud SQL instance.  
`[resolve](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/connect/resolve)` |  `GET /v1/locations/{location}/dns/{dnsName}:resolveConnectSettings`   
Retrieves connect settings about a Cloud SQL instance using the instance DNS name.  
  
## REST Resource: [v1.databases](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases)

Methods  
---  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/delete)` |  `DELETE /v1/projects/{project}/instances/{instance}/databases/{database}`   
Deletes a database from a Cloud SQL instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/get)` |  `GET /v1/projects/{project}/instances/{instance}/databases/{database}`   
Retrieves a resource containing information about a database inside a Cloud SQL instance.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/insert)` |  `POST /v1/projects/{project}/instances/{instance}/databases`   
Inserts a resource containing information about a database inside a Cloud SQL instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/list)` |  `GET /v1/projects/{project}/instances/{instance}/databases`   
Lists databases in the specified Cloud SQL instance.  
`[patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/patch)` |  `PATCH /v1/projects/{project}/instances/{instance}/databases/{database}`   
Partially updates a resource containing information about a database inside a Cloud SQL instance.  
`[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases/update)` |  `PUT /v1/projects/{project}/instances/{instance}/databases/{database}`   
Updates a resource containing information about a database inside a Cloud SQL instance.  
  
## REST Resource: [v1.flags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/flags)

Methods  
---  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/flags/list)` |  `GET /v1/flags`   
Lists all available database flags for Cloud SQL instances.  
  
## REST Resource: [v1.instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances)

Methods  
---  
`[ListServerCertificates](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/ListServerCertificates)` |  `GET /v1/projects/{project}/instances/{instance}/listServerCertificates`   
Lists all versions of server certificates and certificate authorities (CAs) for the specified instance.  
`[RotateServerCertificate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/RotateServerCertificate)` |  `POST /v1/projects/{project}/instances/{instance}/rotateServerCertificate`   
Rotates the server certificate version to one previously added with the addServerCertificate method.  
`[addServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/addServerCa)` |  `POST /v1/projects/{project}/instances/{instance}/addServerCa`   
Adds a new trusted Certificate Authority (CA) version for the specified instance.  
`[addServerCertificate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/addServerCertificate)` |  `POST /v1/projects/{project}/instances/{instance}/addServerCertificate`   
Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA.  
`[clone](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/clone)` |  `POST /v1/projects/{project}/instances/{instance}/clone`   
Creates a Cloud SQL instance as a clone of the source instance.  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/delete)` |  `DELETE /v1/projects/{project}/instances/{instance}`   
Deletes a Cloud SQL instance.  
`[demote](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/demote)` |  `POST /v1/projects/{project}/instances/{instance}/demote`   
Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.  
`[demoteMaster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/demoteMaster)` |  `POST /v1/projects/{project}/instances/{instance}/demoteMaster`   
Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.  
`[executeSql](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/executeSql)` |  `POST /v1/projects/{project}/instances/{instance}/executeSql`   
Execute SQL statements.  
`[export](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/export)` |  `POST /v1/projects/{project}/instances/{instance}/export`   
Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file.  
`[failover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/failover)` |  `POST /v1/projects/{project}/instances/{instance}/failover`   
Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/get)` |  `GET /v1/projects/{project}/instances/{instance}`   
Retrieves a resource containing information about a Cloud SQL instance.  
`[import](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/import)` |  `POST /v1/projects/{project}/instances/{instance}/import`   
Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert)` |  `POST /v1/projects/{project}/instances`   
Creates a new Cloud SQL instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/list)` |  `GET /v1/projects/{project}/instances`   
Lists instances under a given project.  
`[listServerCas](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/listServerCas)` |  `GET /v1/projects/{project}/instances/{instance}/listServerCas`   
Lists all of the trusted Certificate Authorities (CAs) for the specified instance.  
`[patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/patch)` |  `PATCH /v1/projects/{project}/instances/{instance}`   
Partially updates settings of a Cloud SQL instance by merging the request with the current configuration.  
`[pointInTimeRestore](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/pointInTimeRestore)` |  `POST /v1/{parent=projects/*}:pointInTimeRestore`   
Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.  
`[promoteReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/promoteReplica)` |  `POST /v1/projects/{project}/instances/{instance}/promoteReplica`   
Promotes the read replica instance to be an independent Cloud SQL primary instance.  
`[reencrypt](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/reencrypt)` |  `POST /v1/projects/{project}/instances/{instance}/reencrypt`   
Reencrypt CMEK instance with latest key version.  
`[resetSslConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/resetSslConfig)` |  `POST /v1/projects/{project}/instances/{instance}/resetSslConfig`   
Deletes all client certificates and generates a new server SSL certificate for the instance.  
`[restart](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restart)` |  `POST /v1/projects/{project}/instances/{instance}/restart`   
Restarts a Cloud SQL instance.  
`[restoreBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/restoreBackup)` |  `POST /v1/projects/{project}/instances/{instance}/restoreBackup`   
Restores a backup of a Cloud SQL instance.  
`[rotateServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/rotateServerCa)` |  `POST /v1/projects/{project}/instances/{instance}/rotateServerCa`   
Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method.  
`[startReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/startReplica)` |  `POST /v1/projects/{project}/instances/{instance}/startReplica`   
Starts the replication in the read replica instance.  
`[stopReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/stopReplica)` |  `POST /v1/projects/{project}/instances/{instance}/stopReplica`   
Stops the replication in the read replica instance.  
`[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/switchover)` |  `POST /v1/projects/{project}/instances/{instance}/switchover`   
Switches over from the primary instance to the DR replica instance.  
`[truncateLog](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/truncateLog)` |  `POST /v1/projects/{project}/instances/{instance}/truncateLog`   
Truncate MySQL general and slow query log tables MySQL only.  
`[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/update)` |  `PUT /v1/projects/{project}/instances/{instance}`   
Updates settings of a Cloud SQL instance.  
  
## REST Resource: [v1.operations](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/cancel)` |  `POST /v1/projects/{project}/operations/{operation}/cancel`   
Cancels an instance operation that has been performed on an instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/get)` |  `GET /v1/projects/{project}/operations/{operation}`   
Retrieves an instance operation that has been performed on an instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations/list)` |  `GET /v1/projects/{project}/operations`   
Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.  
  
## REST Resource: [v1.projects.instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances)

Methods  
---  
`[getDiskShrinkConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/getDiskShrinkConfig)` |  `GET /v1/projects/{project}/instances/{instance}/getDiskShrinkConfig`   
Get Disk Shrink Config for a given instance.  
`[getLatestRecoveryTime](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/getLatestRecoveryTime)` |  `GET /v1/projects/{project}/instances/{instance}/getLatestRecoveryTime`   
Get Latest Recovery Time for a given instance.  
`[performDiskShrink](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/performDiskShrink)` |  `POST /v1/projects/{project}/instances/{instance}/performDiskShrink`   
Perform Disk Shrink on primary instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/rescheduleMaintenance)` |  `POST /v1/projects/{project}/instances/{instance}/rescheduleMaintenance`   
Reschedules the maintenance on the given instance.  
`[startExternalSync](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/startExternalSync)` |  `POST /v1/projects/{project}/instances/{instance}/startExternalSync`   
Start External primary instance migration.  
`[verifyExternalSyncSettings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/projects.instances/verifyExternalSyncSettings)` |  `POST /v1/projects/{project}/instances/{instance}/verifyExternalSyncSettings`   
Verify External primary instance external sync settings.  
  
## REST Resource: [v1.sslCerts](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts)

Methods  
---  
`[createEphemeral](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/createEphemeral)` |  `POST /v1/projects/{project}/instances/{instance}/createEphemeral`   
Generates a short-lived X509 certificate containing the provided public key and signed by a private key specific to the target instance.  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/delete)` |  `DELETE /v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}`   
Deletes the SSL certificate.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/get)` |  `GET /v1/projects/{project}/instances/{instance}/sslCerts/{sha1Fingerprint}`   
Retrieves a particular SSL certificate.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/insert)` |  `POST /v1/projects/{project}/instances/{instance}/sslCerts`   
Creates an SSL certificate and returns it along with the private key and server certificate authority.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/sslCerts/list)` |  `GET /v1/projects/{project}/instances/{instance}/sslCerts`   
Lists all of the current SSL certificates for the instance.  
  
## REST Resource: [v1.tiers](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/tiers)

Methods  
---  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/tiers/list)` |  `GET /v1/projects/{project}/tiers`   
Lists all available machine types (tiers) for Cloud SQL, for example, `db-custom-1-3840`.  
  
## REST Resource: [v1.users](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users)

Methods  
---  
`[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/delete)` |  `DELETE /v1/projects/{project}/instances/{instance}/users`   
Deletes a user from a Cloud SQL instance.  
`[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/get)` |  `GET /v1/projects/{project}/instances/{instance}/users/{name}`   
Retrieves a resource containing information about a user.  
`[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/insert)` |  `POST /v1/projects/{project}/instances/{instance}/users`   
Creates a new user in a Cloud SQL instance.  
`[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/list)` |  `GET /v1/projects/{project}/instances/{instance}/users`   
Lists users in the specified Cloud SQL instance.  
`[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users/update)` |  `PUT /v1/projects/{project}/instances/{instance}/users`   
Updates an existing user in a Cloud SQL instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
