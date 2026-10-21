---
url: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/
title: Memorystore API \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:04:25.313573+00:00
---

# Memorystore API  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/valkey/apis)



Send feedback 

#  Memorystore API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1beta.projects.locations
  * REST Resource: v1beta.projects.locations.aclPolicies
  * REST Resource: v1beta.projects.locations.aclPolicies.revisions
  * REST Resource: v1beta.projects.locations.backupCollections
  * REST Resource: v1beta.projects.locations.backupCollections.backups
  * REST Resource: v1beta.projects.locations.instances
  * REST Resource: v1beta.projects.locations.instances.tokenAuthUsers
  * REST Resource: v1beta.projects.locations.instances.tokenAuthUsers.authTokens
  * REST Resource: v1beta.projects.locations.operations
  * REST Resource: v1alpha.projects.locations
  * REST Resource: v1alpha.projects.locations.aclPolicies
  * REST Resource: v1alpha.projects.locations.aclPolicies.revisions
  * REST Resource: v1alpha.projects.locations.backupCollections
  * REST Resource: v1alpha.projects.locations.backupCollections.backups
  * REST Resource: v1alpha.projects.locations.instances
  * REST Resource: v1alpha.projects.locations.instances.tokenAuthUsers
  * REST Resource: v1alpha.projects.locations.instances.tokenAuthUsers.authTokens
  * REST Resource: v1alpha.projects.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.aclPolicies
  * REST Resource: v1.projects.locations.aclPolicies.revisions
  * REST Resource: v1.projects.locations.backupCollections
  * REST Resource: v1.projects.locations.backupCollections.backups
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.instances.tokenAuthUsers
  * REST Resource: v1.projects.locations.instances.tokenAuthUsers.authTokens
  * REST Resource: v1.projects.locations.operations



## Service: memorystore.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://memorystore.googleapis.com/$discovery/rest?version=v1>
  * <https://memorystore.googleapis.com/$discovery/rest?version=v1beta>
  * <https://memorystore.googleapis.com/$discovery/rest?version=v1alpha>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://memorystore.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west15 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-central2 us-east1 us-east4 us-east5 us-east7 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8

  

* `https://memorystore.googleapis.com`

## REST Resource: [v1beta.projects.locations](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/get)` |  `GET /v1beta/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getSharedRegionalCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/getSharedRegionalCertificateAuthority)` |  `GET /v1beta/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`   
Gets the details of shared regional certificate authority information for Memorystore instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations/list)` |  `GET /v1beta/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta.projects.locations.aclPolicies](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/aclPolicies`   
Creates an ACL policy.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/aclPolicies/*}`   
Deletes a specific ACL policy.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies/get)` |  `GET /v1beta/{name=projects/*/locations/*/aclPolicies/*}`   
Gets the details of a specific Memorystore ACL policy.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/aclPolicies`   
Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies/patch)` |  `PATCH /v1beta/{aclPolicy.name=projects/*/locations/*/aclPolicies/*}`   
Updates the ACL policy.  
  
## REST Resource: [v1beta.projects.locations.aclPolicies.revisions](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies.revisions)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies.revisions/get)` |  `GET /v1beta/{name=projects/*/locations/*/aclPolicies/*/revisions/*}`   
Gets details of a specific ACL policy revision.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.aclPolicies.revisions/list)` |  `GET /v1beta/{parent=projects/*/locations/*/aclPolicies/*}/revisions`   
Lists all ACL policy revisions in a given ACL policy.  
  
## REST Resource: [v1beta.projects.locations.backupCollections](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections/get)` |  `GET /v1beta/{name=projects/*/locations/*/backupCollections/*}`   
Get a backup collection.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/backupCollections`   
Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
## REST Resource: [v1beta.projects.locations.backupCollections.backups](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections.backups)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections.backups/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Deletes a specific backup.  
`[export](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections.backups/export)` |  `POST /v1beta/{name=projects/*/locations/*/backupCollections/*/backups/*}:export`   
Exports a specific backup to a customer target Cloud Storage URI.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections.backups/get)` |  `GET /v1beta/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.backupCollections.backups/list)` |  `GET /v1beta/{parent=projects/*/locations/*/backupCollections/*}/backups`   
Lists all backups owned by a backup collection.  
  
## REST Resource: [v1beta.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances)

Methods  
---  
`[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/addTokenAuthUser)` |  `POST /v1beta/{instance=projects/*/locations/*/instances/*}:addTokenAuthUser`   
Adds a token auth user for a token based auth enabled instance.  
`[backup](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/backup)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*}:backup`   
Backup Instance.  
`[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/create)` |  `POST /v1beta/{parent=projects/*/locations/*}/instances`   
Creates a new Instance in a given project and location.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/instances/*}`   
Deletes a single Instance.  
`[finishMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/finishMigration)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*}:finishMigration`   
Finalizes the migration process.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Instance.  
`[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/getCertificateAuthority)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*}/certificateAuthority`   
Gets details about the certificate authority for an Instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/list)` |  `GET /v1beta/{parent=projects/*/locations/*}/instances`   
Lists Instances in a given project and location.  
`[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/patch)` |  `PATCH /v1beta/{instance.name=projects/*/locations/*/instances/*}`   
Updates the parameters of a single Instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedules upcoming maintenance event.  
`[startMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances/startMigration)` |  `POST /v1beta/{name=projects/*/locations/*/instances/*}:startMigration`   
Initiates the migration of a source instance to the target Memorystore instance.  
  
## REST Resource: [v1beta.projects.locations.instances.tokenAuthUsers](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers)

Methods  
---  
`[addAuthToken](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers/addAuthToken)` |  `POST /v1beta/{tokenAuthUser=projects/*/locations/*/instances/*/tokenAuthUsers/*}:addAuthToken`   
Adds a token for a user of a token based auth enabled instance.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*}`   
Deletes a token auth user for a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*}`   
Gets a specific token auth user for a token based auth enabled instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*}/tokenAuthUsers`   
Lists all the token auth users for a token based auth enabled instance.  
  
## REST Resource: [v1beta.projects.locations.instances.tokenAuthUsers.authTokens](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers.authTokens)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers.authTokens/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*/authTokens/*}`   
Deletes a token for a user of a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers.authTokens/get)` |  `GET /v1beta/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*/authTokens/*}`   
Gets a token based auth enabled instance's auth token for a given user.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.instances.tokenAuthUsers.authTokens/list)` |  `GET /v1beta/{parent=projects/*/locations/*/instances/*/tokenAuthUsers/*}/authTokens`   
Lists all the auth tokens for a specific token auth user.  
  
## REST Resource: [v1beta.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.operations/cancel)` |  `POST /v1beta/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.operations/delete)` |  `DELETE /v1beta/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.operations/get)` |  `GET /v1beta/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1beta/projects.locations.operations/list)` |  `GET /v1beta/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha.projects.locations](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations/get)` |  `GET /v1alpha/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getSharedRegionalCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations/getSharedRegionalCertificateAuthority)` |  `GET /v1alpha/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`   
Gets the details of shared regional certificate authority information for Memorystore instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations/list)` |  `GET /v1alpha/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha.projects.locations.aclPolicies](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/aclPolicies`   
Creates an ACL policy.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/aclPolicies/*}`   
Deletes a specific ACL policy.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/get)` |  `GET /v1alpha/{name=projects/*/locations/*/aclPolicies/*}`   
Gets the details of a specific Memorystore ACL policy.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/aclPolicies`   
Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies/patch)` |  `PATCH /v1alpha/{aclPolicy.name=projects/*/locations/*/aclPolicies/*}`   
Updates the ACL policy.  
  
## REST Resource: [v1alpha.projects.locations.aclPolicies.revisions](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies.revisions)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies.revisions/get)` |  `GET /v1alpha/{name=projects/*/locations/*/aclPolicies/*/revisions/*}`   
Gets details of a specific ACL policy revision.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.aclPolicies.revisions/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/aclPolicies/*}/revisions`   
Lists all ACL policy revisions in a given ACL policy.  
  
## REST Resource: [v1alpha.projects.locations.backupCollections](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections/get)` |  `GET /v1alpha/{name=projects/*/locations/*/backupCollections/*}`   
Get a backup collection.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/backupCollections`   
Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
## REST Resource: [v1alpha.projects.locations.backupCollections.backups](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Deletes a specific backup.  
`[export](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/export)` |  `POST /v1alpha/{name=projects/*/locations/*/backupCollections/*/backups/*}:export`   
Exports a specific backup to a customer target Cloud Storage URI.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/get)` |  `GET /v1alpha/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.backupCollections.backups/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/backupCollections/*}/backups`   
Lists all backups owned by a backup collection.  
  
## REST Resource: [v1alpha.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances)

Methods  
---  
`[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/addTokenAuthUser)` |  `POST /v1alpha/{instance=projects/*/locations/*/instances/*}:addTokenAuthUser`   
Adds a token auth user for a token based auth enabled instance.  
`[backup](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/backup)` |  `POST /v1alpha/{name=projects/*/locations/*/instances/*}:backup`   
Backup Instance.  
`[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/create)` |  `POST /v1alpha/{parent=projects/*/locations/*}/instances`   
Creates a new Instance in a given project and location.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/instances/*}`   
Deletes a single Instance.  
`[finishMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/finishMigration)` |  `POST /v1alpha/{name=projects/*/locations/*/instances/*}:finishMigration`   
Finalizes the migration process.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/get)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Instance.  
`[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/getCertificateAuthority)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*}/certificateAuthority`   
Gets details about the certificate authority for an Instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/list)` |  `GET /v1alpha/{parent=projects/*/locations/*}/instances`   
Lists Instances in a given project and location.  
`[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/patch)` |  `PATCH /v1alpha/{instance.name=projects/*/locations/*/instances/*}`   
Updates the parameters of a single Instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1alpha/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedules upcoming maintenance event.  
`[startMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances/startMigration)` |  `POST /v1alpha/{name=projects/*/locations/*/instances/*}:startMigration`   
Initiates the migration of a source instance to the target Memorystore instance.  
  
## REST Resource: [v1alpha.projects.locations.instances.tokenAuthUsers](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers)

Methods  
---  
`[addAuthToken](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers/addAuthToken)` |  `POST /v1alpha/{tokenAuthUser=projects/*/locations/*/instances/*/tokenAuthUsers/*}:addAuthToken`   
Adds a token for a user of a token based auth enabled instance.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*}`   
Deletes a token auth user for a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers/get)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*}`   
Gets a specific token auth user for a token based auth enabled instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/instances/*}/tokenAuthUsers`   
Lists all the token auth users for a token based auth enabled instance.  
  
## REST Resource: [v1alpha.projects.locations.instances.tokenAuthUsers.authTokens](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers.authTokens)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers.authTokens/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*/authTokens/*}`   
Deletes a token for a user of a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers.authTokens/get)` |  `GET /v1alpha/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*/authTokens/*}`   
Gets a token based auth enabled instance's auth token for a given user.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.instances.tokenAuthUsers.authTokens/list)` |  `GET /v1alpha/{parent=projects/*/locations/*/instances/*/tokenAuthUsers/*}/authTokens`   
Lists all the auth tokens for a specific token auth user.  
  
## REST Resource: [v1alpha.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.operations/cancel)` |  `POST /v1alpha/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.operations/delete)` |  `DELETE /v1alpha/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.operations/get)` |  `GET /v1alpha/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1alpha/projects.locations.operations/list)` |  `GET /v1alpha/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getSharedRegionalCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations/getSharedRegionalCertificateAuthority)` |  `GET /v1/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`   
Gets the details of shared regional certificate authority information for Memorystore instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.aclPolicies](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/aclPolicies`   
Creates an ACL policy.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/aclPolicies/*}`   
Deletes a specific ACL policy.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/aclPolicies/*}`   
Gets the details of a specific Memorystore ACL policy.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/aclPolicies`   
Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies/patch)` |  `PATCH /v1/{aclPolicy.name=projects/*/locations/*/aclPolicies/*}`   
Updates the ACL policy.  
  
## REST Resource: [v1.projects.locations.aclPolicies.revisions](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies.revisions)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/aclPolicies/*/revisions/*}`   
Gets details of a specific ACL policy revision.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.aclPolicies.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/aclPolicies/*}/revisions`   
Lists all ACL policy revisions in a given ACL policy.  
  
## REST Resource: [v1.projects.locations.backupCollections](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections/get)` |  `GET /v1/{name=projects/*/locations/*/backupCollections/*}`   
Get a backup collection.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections/list)` |  `GET /v1/{parent=projects/*/locations/*}/backupCollections`   
Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
## REST Resource: [v1.projects.locations.backupCollections.backups](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections.backups)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections.backups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Deletes a specific backup.  
`[export](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections.backups/export)` |  `POST /v1/{name=projects/*/locations/*/backupCollections/*/backups/*}:export`   
Exports a specific backup to a customer target Cloud Storage URI.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections.backups/get)` |  `GET /v1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.backupCollections.backups/list)` |  `GET /v1/{parent=projects/*/locations/*/backupCollections/*}/backups`   
Lists all backups owned by a backup collection.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances)

Methods  
---  
`[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/addTokenAuthUser)` |  `POST /v1/{instance=projects/*/locations/*/instances/*}:addTokenAuthUser`   
Adds a token auth user for a token based auth enabled instance.  
`[backup](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/backup)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:backup`   
Backup Instance.  
`[create](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/create)` |  `POST /v1/{parent=projects/*/locations/*}/instances`   
Creates a new Instance in a given project and location.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*}`   
Deletes a single Instance.  
`[finishMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/finishMigration)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:finishMigration`   
Finalizes the migration process.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Instance.  
`[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/getCertificateAuthority)` |  `GET /v1/{name=projects/*/locations/*/instances/*}/certificateAuthority`   
Gets details about the certificate authority for an Instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists Instances in a given project and location.  
`[patch](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/patch)` |  `PATCH /v1/{instance.name=projects/*/locations/*/instances/*}`   
Updates the parameters of a single Instance.  
`[rescheduleMaintenance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/rescheduleMaintenance)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:rescheduleMaintenance`   
Reschedules upcoming maintenance event.  
`[startMigration](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances/startMigration)` |  `POST /v1/{name=projects/*/locations/*/instances/*}:startMigration`   
Initiates the migration of a source instance to the target Memorystore instance.  
  
## REST Resource: [v1.projects.locations.instances.tokenAuthUsers](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers)

Methods  
---  
`[addAuthToken](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers/addAuthToken)` |  `POST /v1/{tokenAuthUser=projects/*/locations/*/instances/*/tokenAuthUsers/*}:addAuthToken`   
Adds a token for a user of a token based auth enabled instance.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*}`   
Deletes a token auth user for a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*}`   
Gets a specific token auth user for a token based auth enabled instance.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*}/tokenAuthUsers`   
Lists all the token auth users for a token based auth enabled instance.  
  
## REST Resource: [v1.projects.locations.instances.tokenAuthUsers.authTokens](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers.authTokens)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers.authTokens/delete)` |  `DELETE /v1/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*/authTokens/*}`   
Deletes a token for a user of a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers.authTokens/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*/tokenAuthUsers/*/authTokens/*}`   
Gets a token based auth enabled instance's auth token for a given user.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances.tokenAuthUsers.authTokens/list)` |  `GET /v1/{parent=projects/*/locations/*/instances/*/tokenAuthUsers/*}/authTokens`   
Lists all the auth tokens for a specific token auth user.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
