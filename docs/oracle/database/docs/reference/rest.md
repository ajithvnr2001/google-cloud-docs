---
url: https://docs.cloud.google.com/oracle/database/docs/reference/rest/
title: Oracle Database@Google Cloud API \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:08:35.740951+00:00
---

# Oracle Database@Google Cloud API  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Reference ](https://docs.cloud.google.com/oracle/database/docs/apis)



Send feedback 

#  Oracle Database@Google Cloud API Stay organized with collections  Save and categorize content based on your preferences. 

The Oracle [Database@Google](mailto:Database@Google) Cloud API provides a set of APIs to manage Oracle database services, such as Exadata and Autonomous Databases.

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.autonomousDatabaseBackups
  * REST Resource: v1.projects.locations.autonomousDatabaseCharacterSets
  * REST Resource: v1.projects.locations.autonomousDatabases
  * REST Resource: v1.projects.locations.autonomousDbVersions
  * REST Resource: v1.projects.locations.cloudExadataInfrastructures
  * REST Resource: v1.projects.locations.cloudExadataInfrastructures.dbServers
  * REST Resource: v1.projects.locations.cloudVmClusters
  * REST Resource: v1.projects.locations.cloudVmClusters.dbNodes
  * REST Resource: v1.projects.locations.databaseCharacterSets
  * REST Resource: v1.projects.locations.databases
  * REST Resource: v1.projects.locations.dbSystemInitialStorageSizes
  * REST Resource: v1.projects.locations.dbSystemShapes
  * REST Resource: v1.projects.locations.dbSystems
  * REST Resource: v1.projects.locations.dbVersions
  * REST Resource: v1.projects.locations.entitlements
  * REST Resource: v1.projects.locations.exadbVmClusters
  * REST Resource: v1.projects.locations.exadbVmClusters.dbNodes
  * REST Resource: v1.projects.locations.exascaleDbStorageVaults
  * REST Resource: v1.projects.locations.giVersions
  * REST Resource: v1.projects.locations.giVersions.minorVersions
  * REST Resource: v1.projects.locations.goldengateConnectionAssignments
  * REST Resource: v1.projects.locations.goldengateConnectionTypes
  * REST Resource: v1.projects.locations.goldengateConnections
  * REST Resource: v1.projects.locations.goldengateDeploymentEnvironments
  * REST Resource: v1.projects.locations.goldengateDeploymentTypes
  * REST Resource: v1.projects.locations.goldengateDeploymentVersions
  * REST Resource: v1.projects.locations.goldengateDeployments
  * REST Resource: v1.projects.locations.odbNetworks
  * REST Resource: v1.projects.locations.odbNetworks.odbSubnets
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.pluggableDatabases



## Service: oracledatabase.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://oracledatabase.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://oracledatabase.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global asia-northeast2 asia-south2 asia-south1 australia-southeast2 europe-west8 northamerica-northeast2

  

* `https://oracledatabase.googleapis.com`

## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.autonomousDatabaseBackups](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseBackups/list)` |  `GET /v1/{parent=projects/*/locations/*}/autonomousDatabaseBackups`   
Lists the long-term and automatic backups of an Autonomous Database.  
  
## REST Resource: [v1.projects.locations.autonomousDatabaseCharacterSets](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabaseCharacterSets/list)` |  `GET /v1/{parent=projects/*/locations/*}/autonomousDatabaseCharacterSets`   
Lists Autonomous Database Character Sets in a given project and location.  
  
## REST Resource: [v1.projects.locations.autonomousDatabases](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/create)` |  `POST /v1/{parent=projects/*/locations/*}/autonomousDatabases`   
Creates a new Autonomous Database in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/delete)` |  `DELETE /v1/{name=projects/*/locations/*/autonomousDatabases/*}`   
Deletes a single Autonomous Database.  
`[failover](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/failover)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:failover`   
Initiates a failover to target autonomous database from the associated primary database.  
`[generateWallet](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/generateWallet)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:generateWallet`   
Generates a wallet for an Autonomous Database.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/get)` |  `GET /v1/{name=projects/*/locations/*/autonomousDatabases/*}`   
Gets the details of a single Autonomous Database.  
`[getRefreshableClones](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/getRefreshableClones)` |  `GET /v1/{name=projects/*/locations/*/autonomousDatabases/*}:getRefreshableClones`   
Gets the refreshable clones for a given Autonomous Database.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/list)` |  `GET /v1/{parent=projects/*/locations/*}/autonomousDatabases`   
Lists the Autonomous Databases in a given project and location.  
`[patch](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/patch)` |  `PATCH /v1/{autonomousDatabase.name=projects/*/locations/*/autonomousDatabases/*}`   
Updates the parameters of a single Autonomous Database.  
`[refresh](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/refresh)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:refresh`   
Refreshes the refreshable clone of an Autonomous Database.  
`[restart](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/restart)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:restart`   
Restarts an Autonomous Database.  
`[restore](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/restore)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:restore`   
Restores a single Autonomous Database.  
`[start](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/start)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:start`   
Starts an Autonomous Database.  
`[stop](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/stop)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:stop`   
Stops an Autonomous Database.  
`[switchover](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDatabases/switchover)` |  `POST /v1/{name=projects/*/locations/*/autonomousDatabases/*}:switchover`   
Initiates a switchover of specified autonomous database to the associated peer database.  
  
## REST Resource: [v1.projects.locations.autonomousDbVersions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDbVersions)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.autonomousDbVersions/list)` |  `GET /v1/{parent=projects/*/locations/*}/autonomousDbVersions`   
Lists all the available Autonomous Database versions for a project and location.  
  
## REST Resource: [v1.projects.locations.cloudExadataInfrastructures](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures)

Methods  
---  
`[configureExascale](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/configureExascale)` |  `POST /v1/{name=projects/*/locations/*/cloudExadataInfrastructures/*}:configureExascale`   
Configures Exascale for a single Exadata Infrastructure.  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/create)` |  `POST /v1/{parent=projects/*/locations/*}/cloudExadataInfrastructures`   
Creates a new Exadata Infrastructure in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/delete)` |  `DELETE /v1/{name=projects/*/locations/*/cloudExadataInfrastructures/*}`   
Deletes a single Exadata Infrastructure.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/get)` |  `GET /v1/{name=projects/*/locations/*/cloudExadataInfrastructures/*}`   
Gets details of a single Exadata Infrastructure.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures/list)` |  `GET /v1/{parent=projects/*/locations/*}/cloudExadataInfrastructures`   
Lists Exadata Infrastructures in a given project and location.  
  
## REST Resource: [v1.projects.locations.cloudExadataInfrastructures.dbServers](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudExadataInfrastructures.dbServers/list)` |  `GET /v1/{parent=projects/*/locations/*/cloudExadataInfrastructures/*}/dbServers`   
Lists the database servers of an Exadata Infrastructure instance.  
  
## REST Resource: [v1.projects.locations.cloudVmClusters](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/cloudVmClusters`   
Creates a new VM Cluster in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/cloudVmClusters/*}`   
Deletes a single VM Cluster.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/get)` |  `GET /v1/{name=projects/*/locations/*/cloudVmClusters/*}`   
Gets details of a single VM Cluster.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/cloudVmClusters`   
Lists the VM Clusters in a given project and location.  
  
## REST Resource: [v1.projects.locations.cloudVmClusters.dbNodes](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.cloudVmClusters.dbNodes/list)` |  `GET /v1/{parent=projects/*/locations/*/cloudVmClusters/*}/dbNodes`   
Lists the database nodes of a VM Cluster.  
  
## REST Resource: [v1.projects.locations.databaseCharacterSets](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databaseCharacterSets)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databaseCharacterSets/list)` |  `GET /v1/{parent=projects/*/locations/*}/databaseCharacterSets`   
List DatabaseCharacterSets for the given project and location.  
  
## REST Resource: [v1.projects.locations.databases](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases)

Methods  
---  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases/get)` |  `GET /v1/{name=projects/*/locations/*/databases/*}`   
Gets details of a single Database.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.databases/list)` |  `GET /v1/{parent=projects/*/locations/*}/databases`   
Lists all the Databases for the given project, location and DbSystem.  
  
## REST Resource: [v1.projects.locations.dbSystemInitialStorageSizes](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemInitialStorageSizes/list)` |  `GET /v1/{parent=projects/*/locations/*}/dbSystemInitialStorageSizes`   
Lists all the DbSystemInitialStorageSizes for the given project and location.  
  
## REST Resource: [v1.projects.locations.dbSystemShapes](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemShapes)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystemShapes/list)` |  `GET /v1/{parent=projects/*/locations/*}/dbSystemShapes`   
Lists the database system shapes available for the project and location.  
  
## REST Resource: [v1.projects.locations.dbSystems](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/create)` |  `POST /v1/{parent=projects/*/locations/*}/dbSystems`   
Creates a new DbSystem in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/delete)` |  `DELETE /v1/{name=projects/*/locations/*/dbSystems/*}`   
Deletes a single DbSystem.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/get)` |  `GET /v1/{name=projects/*/locations/*/dbSystems/*}`   
Gets details of a single DbSystem.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbSystems/list)` |  `GET /v1/{parent=projects/*/locations/*}/dbSystems`   
Lists all the DbSystems for the given project and location.  
  
## REST Resource: [v1.projects.locations.dbVersions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.dbVersions/list)` |  `GET /v1/{parent=projects/*/locations/*}/dbVersions`   
List DbVersions for the given project and location.  
  
## REST Resource: [v1.projects.locations.entitlements](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.entitlements/list)` |  `GET /v1/{parent=projects/*/locations/*}/entitlements`   
Lists the entitlements in a given project.  
  
## REST Resource: [v1.projects.locations.exadbVmClusters](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/create)` |  `POST /v1/{parent=projects/*/locations/*}/exadbVmClusters`   
Creates a new Exadb (Exascale) VM Cluster resource.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/delete)` |  `DELETE /v1/{name=projects/*/locations/*/exadbVmClusters/*}`   
Deletes a single Exadb (Exascale) VM Cluster.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/get)` |  `GET /v1/{name=projects/*/locations/*/exadbVmClusters/*}`   
Gets details of a single Exadb (Exascale) VM Cluster.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/list)` |  `GET /v1/{parent=projects/*/locations/*}/exadbVmClusters`   
Lists all the Exadb (Exascale) VM Clusters for the given project and location.  
`[patch](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/patch)` |  `PATCH /v1/{exadbVmCluster.name=projects/*/locations/*/exadbVmClusters/*}`   
Updates a single Exadb (Exascale) VM Cluster.  
`[removeVirtualMachine](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters/removeVirtualMachine)` |  `POST /v1/{name=projects/*/locations/*/exadbVmClusters/*}:removeVirtualMachine`   
Removes virtual machines from an existing exadb vm cluster.  
  
## REST Resource: [v1.projects.locations.exadbVmClusters.dbNodes](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters.dbNodes)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exadbVmClusters.dbNodes/list)` |  `GET /v1/{parent=projects/*/locations/*/exadbVmClusters/*}/dbNodes`   
Lists the database nodes of a VM Cluster.  
  
## REST Resource: [v1.projects.locations.exascaleDbStorageVaults](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/create)` |  `POST /v1/{parent=projects/*/locations/*}/exascaleDbStorageVaults`   
Creates a new ExascaleDB Storage Vault resource.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/delete)` |  `DELETE /v1/{name=projects/*/locations/*/exascaleDbStorageVaults/*}`   
Deletes a single ExascaleDB Storage Vault.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/get)` |  `GET /v1/{name=projects/*/locations/*/exascaleDbStorageVaults/*}`   
Gets details of a single ExascaleDB Storage Vault.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.exascaleDbStorageVaults/list)` |  `GET /v1/{parent=projects/*/locations/*}/exascaleDbStorageVaults`   
Lists all the ExascaleDB Storage Vaults for the given project and location.  
  
## REST Resource: [v1.projects.locations.giVersions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions/list)` |  `GET /v1/{parent=projects/*/locations/*}/giVersions`   
Lists all the valid Oracle Grid Infrastructure (GI) versions for the given project and location.  
  
## REST Resource: [v1.projects.locations.giVersions.minorVersions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions.minorVersions)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.giVersions.minorVersions/list)` |  `GET /v1/{parent=projects/*/locations/*/giVersions/*}/minorVersions`   
Lists all the valid minor versions for the given project, location, gi version and shape family.  
  
## REST Resource: [v1.projects.locations.goldengateConnectionAssignments](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/create)` |  `POST /v1/{parent=projects/*/locations/*}/goldengateConnectionAssignments`   
Creates a new GoldengateConnectionAssignment in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/goldengateConnectionAssignments/*}`   
Deletes a single GoldengateConnectionAssignment.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/get)` |  `GET /v1/{name=projects/*/locations/*/goldengateConnectionAssignments/*}`   
Gets details of a single GoldengateConnectionAssignment.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateConnectionAssignments`   
Lists GoldengateConnectionAssignments in a given project and location.  
`[test](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionAssignments/test)` |  `POST /v1/{name=projects/*/locations/*/goldengateConnectionAssignments/*}:test`   
Tests a single GoldengateConnectionAssignment.  
  
## REST Resource: [v1.projects.locations.goldengateConnectionTypes](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnectionTypes/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateConnectionTypes`   
Lists GoldengateConnectionTypes in a given project and location.  
  
## REST Resource: [v1.projects.locations.goldengateConnections](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/create)` |  `POST /v1/{parent=projects/*/locations/*}/goldengateConnections`   
Creates a new GoldengateConnection in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/delete)` |  `DELETE /v1/{name=projects/*/locations/*/goldengateConnections/*}`   
Deletes a single GoldengateConnection.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/get)` |  `GET /v1/{name=projects/*/locations/*/goldengateConnections/*}`   
Gets details of a single GoldengateConnection.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateConnections/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateConnections`   
Lists all the GoldengateConnections for the given project and location.  
  
## REST Resource: [v1.projects.locations.goldengateDeploymentEnvironments](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentEnvironments/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateDeploymentEnvironments`   
Lists GoldengateDeploymentEnvironments in a given project and location.  
  
## REST Resource: [v1.projects.locations.goldengateDeploymentTypes](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentTypes/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateDeploymentTypes`   
Lists GoldenGateDeploymentTypes in a given project and location.  
  
## REST Resource: [v1.projects.locations.goldengateDeploymentVersions](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions)

Methods  
---  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeploymentVersions/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateDeploymentVersions`   
Lists GoldengateDeploymentVersions in a given project and location.  
  
## REST Resource: [v1.projects.locations.goldengateDeployments](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/create)` |  `POST /v1/{parent=projects/*/locations/*}/goldengateDeployments`   
Creates a new GoldengateDeployment in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/delete)` |  `DELETE /v1/{name=projects/*/locations/*/goldengateDeployments/*}`   
Deletes a single GoldengateDeployment.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/get)` |  `GET /v1/{name=projects/*/locations/*/goldengateDeployments/*}`   
Gets details of a single GoldengateDeployment.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/list)` |  `GET /v1/{parent=projects/*/locations/*}/goldengateDeployments`   
Lists all the GoldengateDeployments for the given project and location.  
`[start](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/start)` |  `POST /v1/{name=projects/*/locations/*/goldengateDeployments/*}:start`   
Starts a single GoldengateDeployment.  
`[stop](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.goldengateDeployments/stop)` |  `POST /v1/{name=projects/*/locations/*/goldengateDeployments/*}:stop`   
Stops a single GoldengateDeployment.  
  
## REST Resource: [v1.projects.locations.odbNetworks](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/create)` |  `POST /v1/{parent=projects/*/locations/*}/odbNetworks`   
Creates a new ODB Network in a given project and location.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/delete)` |  `DELETE /v1/{name=projects/*/locations/*/odbNetworks/*}`   
Deletes a single ODB Network.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/get)` |  `GET /v1/{name=projects/*/locations/*/odbNetworks/*}`   
Gets details of a single ODB Network.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks/list)` |  `GET /v1/{parent=projects/*/locations/*}/odbNetworks`   
Lists the ODB Networks in a given project and location.  
  
## REST Resource: [v1.projects.locations.odbNetworks.odbSubnets](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets)

Methods  
---  
`[create](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/create)` |  `POST /v1/{parent=projects/*/locations/*/odbNetworks/*}/odbSubnets`   
Creates a new ODB Subnet in a given ODB Network.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/delete)` |  `DELETE /v1/{name=projects/*/locations/*/odbNetworks/*/odbSubnets/*}`   
Deletes a single ODB Subnet.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/get)` |  `GET /v1/{name=projects/*/locations/*/odbNetworks/*/odbSubnets/*}`   
Gets details of a single ODB Subnet.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.odbNetworks.odbSubnets/list)` |  `GET /v1/{parent=projects/*/locations/*/odbNetworks/*}/odbSubnets`   
Lists all the ODB Subnets in a given ODB Network.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.pluggableDatabases](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases)

Methods  
---  
`[get](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases/get)` |  `GET /v1/{name=projects/*/locations/*/pluggableDatabases/*}`   
Gets details of a single PluggableDatabase.  
`[list](https://docs.cloud.google.com/oracle/database/docs/reference/rest/v1/projects.locations.pluggableDatabases/list)` |  `GET /v1/{parent=projects/*/locations/*}/pluggableDatabases`   
Lists all the PluggableDatabases for the given project, location and Container Database.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
