---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/
title: Google Cloud Memorystore for Redis API \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:33.025661+00:00
---

# Google Cloud Memorystore for Redis API  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  Google Cloud Memorystore for Redis API Stay organized with collections  Save and categorize content based on your preferences. 

Creates and manages Redis instances on the Google Cloud Platform.

  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.aclPolicies
  * REST Resource: v1beta1.projects.locations.aclPolicies.revisions
  * REST Resource: v1beta1.projects.locations.backupCollections
  * REST Resource: v1beta1.projects.locations.backupCollections.backups
  * REST Resource: v1beta1.projects.locations.clusters
  * REST Resource: v1beta1.projects.locations.clusters.tokenAuthUsers
  * REST Resource: v1beta1.projects.locations.clusters.tokenAuthUsers.authTokens
  * REST Resource: v1beta1.projects.locations.operations
  * REST Resource: v1alpha1.projects.locations
  * REST Resource: v1alpha1.projects.locations.aclPolicies
  * REST Resource: v1alpha1.projects.locations.aclPolicies.revisions
  * REST Resource: v1alpha1.projects.locations.backupCollections
  * REST Resource: v1alpha1.projects.locations.backupCollections.backups
  * REST Resource: v1alpha1.projects.locations.clusters
  * REST Resource: v1alpha1.projects.locations.clusters.tokenAuthUsers
  * REST Resource: v1alpha1.projects.locations.clusters.tokenAuthUsers.authTokens
  * REST Resource: v1alpha1.projects.locations.operations
  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.aclPolicies
  * REST Resource: v1.projects.locations.aclPolicies.revisions
  * REST Resource: v1.projects.locations.backupCollections
  * REST Resource: v1.projects.locations.backupCollections.backups
  * REST Resource: v1.projects.locations.clusters
  * REST Resource: v1.projects.locations.clusters.tokenAuthUsers
  * REST Resource: v1.projects.locations.clusters.tokenAuthUsers.authTokens
  * REST Resource: v1.projects.locations.operations



## Service: redis.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://redis.googleapis.com/$discovery/rest?version=v1>
  * <https://redis.googleapis.com/$discovery/rest?version=v1beta1>
  * <https://redis.googleapis.com/$discovery/rest?version=v1alpha1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://redis.googleapis.com`



## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations/get)` |  `GET /v1beta1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getSharedRegionalCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations/getSharedRegionalCertificateAuthority)` |  `GET /v1beta1/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`   
Gets the details of regional certificate authority information for Redis cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations/list)` |  `GET /v1beta1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1beta1.projects.locations.aclPolicies](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/aclPolicies`   
Creates an ACL policy.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/aclPolicies/*}`   
Deletes a specific ACL policy.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies/get)` |  `GET /v1beta1/{name=projects/*/locations/*/aclPolicies/*}`   
Gets the details of a specific Redis Cluster ACL policy.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/aclPolicies`   
Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies/patch)` |  `PATCH /v1beta1/{aclPolicy.name=projects/*/locations/*/aclPolicies/*}`   
Updates the ACL policy.  
  
## REST Resource: [v1beta1.projects.locations.aclPolicies.revisions](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions/get)` |  `GET /v1beta1/{name=projects/*/locations/*/aclPolicies/*/revisions/*}`   
Gets details of a specific ACL policy revision.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.aclPolicies.revisions/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/aclPolicies/*}/revisions`   
Lists all ACL policy revisions in a given ACL policy.  
  
## REST Resource: [v1beta1.projects.locations.backupCollections](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections/get)` |  `GET /v1beta1/{name=projects/*/locations/*/backupCollections/*}`   
Get a backup collection.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/backupCollections`   
Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
## REST Resource: [v1beta1.projects.locations.backupCollections.backups](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections.backups)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections.backups/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Deletes a specific backup.  
`[export](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections.backups/export)` |  `POST /v1beta1/{name=projects/*/locations/*/backupCollections/*/backups/*}:export`   
Exports a specific backup to a customer target Cloud Storage URI.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections.backups/get)` |  `GET /v1beta1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.backupCollections.backups/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/backupCollections/*}/backups`   
Lists all backups owned by a backup collection.  
  
## REST Resource: [v1beta1.projects.locations.clusters](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters)

Methods  
---  
`[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/addTokenAuthUser)` |  `POST /v1beta1/{cluster=projects/*/locations/*/clusters/*}:addTokenAuthUser`   
Adds a token auth user for a token based auth enabled cluster.  
`[backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/backup)` |  `POST /v1beta1/{name=projects/*/locations/*/clusters/*}:backup`   
Backup Redis Cluster.  
`[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/clusters`   
Creates a Redis cluster based on the specified properties.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/clusters/*}`   
Deletes a specific Redis cluster.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/get)` |  `GET /v1beta1/{name=projects/*/locations/*/clusters/*}`   
Gets the details of a specific Redis cluster.  
`[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/getCertificateAuthority)` |  `GET /v1beta1/{name=projects/*/locations/*/clusters/*/certificateAuthority}`   
Gets the details of certificate authority information for Redis cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/clusters`   
Lists all Redis clusters owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/patch)` |  `PATCH /v1beta1/{cluster.name=projects/*/locations/*/clusters/*}`   
Updates the metadata and configuration of a specific Redis cluster.  
`[rescheduleClusterMaintenance](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters/rescheduleClusterMaintenance)` |  `POST /v1beta1/{name=projects/*/locations/*/clusters/*}:rescheduleClusterMaintenance`   
Reschedules upcoming maintenance event.  
  
## REST Resource: [v1beta1.projects.locations.clusters.tokenAuthUsers](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers)

Methods  
---  
`[addAuthToken](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers/addAuthToken)` |  `POST /v1beta1/{tokenAuthUser=projects/*/locations/*/clusters/*/tokenAuthUsers/*}:addAuthToken`   
Adds a auth token for a user of a token based auth enabled cluster.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*}`   
Deletes a token auth user for a token based auth enabled cluster.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers/get)` |  `GET /v1beta1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*}`   
Gets a specific token auth user for a basic auth enabled cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/clusters/*}/tokenAuthUsers`   
Lists all the token auth users for a token based auth enabled cluster.  
  
## REST Resource: [v1beta1.projects.locations.clusters.tokenAuthUsers.authTokens](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers.authTokens)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers.authTokens/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*/authTokens/*}`   
Removes a auth token for a user of a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers.authTokens/get)` |  `GET /v1beta1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*/authTokens/*}`   
Gets a specific auth token for a specific token auth user.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.clusters.tokenAuthUsers.authTokens/list)` |  `GET /v1beta1/{parent=projects/*/locations/*/clusters/*/tokenAuthUsers/*}/authTokens`   
Lists all the auth tokens for a specific token auth user.  
  
## REST Resource: [v1beta1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.operations/cancel)` |  `POST /v1beta1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.operations/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.operations/get)` |  `GET /v1beta1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1beta1/projects.locations.operations/list)` |  `GET /v1beta1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1alpha1.projects.locations](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getSharedRegionalCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations/getSharedRegionalCertificateAuthority)` |  `GET /v1alpha1/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`   
Gets the details of regional certificate authority information for Redis cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations/list)` |  `GET /v1alpha1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1alpha1.projects.locations.aclPolicies](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/aclPolicies`   
Creates an ACL policy.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/aclPolicies/*}`   
Deletes a specific ACL policy.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/aclPolicies/*}`   
Gets the details of a specific Redis Cluster ACL policy.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/aclPolicies`   
Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies/patch)` |  `PATCH /v1alpha1/{aclPolicy.name=projects/*/locations/*/aclPolicies/*}`   
Updates the ACL policy.  
  
## REST Resource: [v1alpha1.projects.locations.aclPolicies.revisions](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies.revisions)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies.revisions/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/aclPolicies/*/revisions/*}`   
Gets details of a specific ACL policy revision.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.aclPolicies.revisions/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/aclPolicies/*}/revisions`   
Lists all ACL policy revisions in a given ACL policy.  
  
## REST Resource: [v1alpha1.projects.locations.backupCollections](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/backupCollections/*}`   
Get a backup collection.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/backupCollections`   
Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
## REST Resource: [v1alpha1.projects.locations.backupCollections.backups](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Deletes a specific backup.  
`[export](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/export)` |  `POST /v1alpha1/{name=projects/*/locations/*/backupCollections/*/backups/*}:export`   
Exports a specific backup to a customer target Cloud Storage URI.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/backupCollections/*}/backups`   
Lists all backups owned by a backup collection.  
  
## REST Resource: [v1alpha1.projects.locations.clusters](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters)

Methods  
---  
`[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/addTokenAuthUser)` |  `POST /v1alpha1/{cluster=projects/*/locations/*/clusters/*}:addTokenAuthUser`   
Adds a token auth user for a token based auth enabled cluster.  
`[backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/backup)` |  `POST /v1alpha1/{name=projects/*/locations/*/clusters/*}:backup`   
Backup Redis Cluster.  
`[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/create)` |  `POST /v1alpha1/{parent=projects/*/locations/*}/clusters`   
Creates a Redis cluster based on the specified properties.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/clusters/*}`   
Deletes a specific Redis cluster.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/clusters/*}`   
Gets the details of a specific Redis cluster.  
`[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/getCertificateAuthority)` |  `GET /v1alpha1/{name=projects/*/locations/*/clusters/*/certificateAuthority}`   
Gets the details of certificate authority information for Redis cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*}/clusters`   
Lists all Redis clusters owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/patch)` |  `PATCH /v1alpha1/{cluster.name=projects/*/locations/*/clusters/*}`   
Updates the metadata and configuration of a specific Redis cluster.  
`[rescheduleClusterMaintenance](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters/rescheduleClusterMaintenance)` |  `POST /v1alpha1/{name=projects/*/locations/*/clusters/*}:rescheduleClusterMaintenance`   
Reschedules upcoming maintenance event.  
  
## REST Resource: [v1alpha1.projects.locations.clusters.tokenAuthUsers](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers)

Methods  
---  
`[addAuthToken](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers/addAuthToken)` |  `POST /v1alpha1/{tokenAuthUser=projects/*/locations/*/clusters/*/tokenAuthUsers/*}:addAuthToken`   
Adds a auth token for a user of a token based auth enabled cluster.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*}`   
Deletes a token auth user for a token based auth enabled cluster.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*}`   
Gets a specific token auth user for a basic auth enabled cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/clusters/*}/tokenAuthUsers`   
Lists all the token auth users for a token based auth enabled cluster.  
  
## REST Resource: [v1alpha1.projects.locations.clusters.tokenAuthUsers.authTokens](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*/authTokens/*}`   
Removes a auth token for a user of a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*/authTokens/*}`   
Gets a specific auth token for a specific token auth user.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens/list)` |  `GET /v1alpha1/{parent=projects/*/locations/*/clusters/*/tokenAuthUsers/*}/authTokens`   
Lists all the auth tokens for a specific token auth user.  
  
## REST Resource: [v1alpha1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.operations/cancel)` |  `POST /v1alpha1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.operations/delete)` |  `DELETE /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.operations/get)` |  `GET /v1alpha1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.operations/list)` |  `GET /v1alpha1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[getSharedRegionalCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations/getSharedRegionalCertificateAuthority)` |  `GET /v1/{name=projects/*/locations/*/sharedRegionalCertificateAuthority}`   
Gets the details of regional certificate authority information for Redis cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.aclPolicies](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies/create)` |  `POST /v1/{parent=projects/*/locations/*}/aclPolicies`   
Creates an ACL policy.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies/delete)` |  `DELETE /v1/{name=projects/*/locations/*/aclPolicies/*}`   
Deletes a specific ACL policy.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies/get)` |  `GET /v1/{name=projects/*/locations/*/aclPolicies/*}`   
Gets the details of a specific Redis Cluster ACL policy.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies/list)` |  `GET /v1/{parent=projects/*/locations/*}/aclPolicies`   
Lists all ACL policies owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies/patch)` |  `PATCH /v1/{aclPolicy.name=projects/*/locations/*/aclPolicies/*}`   
Updates the ACL policy.  
  
## REST Resource: [v1.projects.locations.aclPolicies.revisions](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies.revisions)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies.revisions/get)` |  `GET /v1/{name=projects/*/locations/*/aclPolicies/*/revisions/*}`   
Gets details of a specific ACL policy revision.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.aclPolicies.revisions/list)` |  `GET /v1/{parent=projects/*/locations/*/aclPolicies/*}/revisions`   
Lists all ACL policy revisions in a given ACL policy.  
  
## REST Resource: [v1.projects.locations.backupCollections](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections/get)` |  `GET /v1/{name=projects/*/locations/*/backupCollections/*}`   
Get a backup collection.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections/list)` |  `GET /v1/{parent=projects/*/locations/*}/backupCollections`   
Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.  
  
## REST Resource: [v1.projects.locations.backupCollections.backups](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections.backups)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections.backups/delete)` |  `DELETE /v1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Deletes a specific backup.  
`[export](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections.backups/export)` |  `POST /v1/{name=projects/*/locations/*/backupCollections/*/backups/*}:export`   
Exports a specific backup to a customer target Cloud Storage URI.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections.backups/get)` |  `GET /v1/{name=projects/*/locations/*/backupCollections/*/backups/*}`   
Gets the details of a specific backup.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections.backups/list)` |  `GET /v1/{parent=projects/*/locations/*/backupCollections/*}/backups`   
Lists all backups owned by a backup collection.  
  
## REST Resource: [v1.projects.locations.clusters](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters)

Methods  
---  
`[addTokenAuthUser](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/addTokenAuthUser)` |  `POST /v1/{cluster=projects/*/locations/*/clusters/*}:addTokenAuthUser`   
Adds a token auth user for a token based auth enabled cluster.  
`[backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/backup)` |  `POST /v1/{name=projects/*/locations/*/clusters/*}:backup`   
Backup Redis Cluster.  
`[create](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/clusters`   
Creates a Redis cluster based on the specified properties.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/clusters/*}`   
Deletes a specific Redis cluster.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/get)` |  `GET /v1/{name=projects/*/locations/*/clusters/*}`   
Gets the details of a specific Redis cluster.  
`[getCertificateAuthority](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/getCertificateAuthority)` |  `GET /v1/{name=projects/*/locations/*/clusters/*/certificateAuthority}`   
Gets the details of certificate authority information for Redis cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/clusters`   
Lists all Redis clusters owned by a project in either the specified location (region) or all locations.  
`[patch](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/patch)` |  `PATCH /v1/{cluster.name=projects/*/locations/*/clusters/*}`   
Updates the metadata and configuration of a specific Redis cluster.  
`[rescheduleClusterMaintenance](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters/rescheduleClusterMaintenance)` |  `POST /v1/{name=projects/*/locations/*/clusters/*}:rescheduleClusterMaintenance`   
Reschedules upcoming maintenance event.  
  
## REST Resource: [v1.projects.locations.clusters.tokenAuthUsers](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers)

Methods  
---  
`[addAuthToken](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/addAuthToken)` |  `POST /v1/{tokenAuthUser=projects/*/locations/*/clusters/*/tokenAuthUsers/*}:addAuthToken`   
Adds a auth token for a user of a token based auth enabled cluster.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/delete)` |  `DELETE /v1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*}`   
Deletes a token auth user for a token based auth enabled cluster.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/get)` |  `GET /v1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*}`   
Gets a specific token auth user for a basic auth enabled cluster.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/list)` |  `GET /v1/{parent=projects/*/locations/*/clusters/*}/tokenAuthUsers`   
Lists all the token auth users for a token based auth enabled cluster.  
  
## REST Resource: [v1.projects.locations.clusters.tokenAuthUsers.authTokens](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers.authTokens)

Methods  
---  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers.authTokens/delete)` |  `DELETE /v1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*/authTokens/*}`   
Removes a auth token for a user of a token based auth enabled instance.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers.authTokens/get)` |  `GET /v1/{name=projects/*/locations/*/clusters/*/tokenAuthUsers/*/authTokens/*}`   
Gets a specific auth token for a specific token auth user.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers.authTokens/list)` |  `GET /v1/{parent=projects/*/locations/*/clusters/*/tokenAuthUsers/*}/authTokens`   
Lists all the auth tokens for a specific token auth user.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
