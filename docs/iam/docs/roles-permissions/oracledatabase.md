---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase/
title: Oracle Database@Google Cloud roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:42:01.764669+00:00
---

# Oracle Database@Google Cloud roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Oracle Database@Google Cloud roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Oracle Database@Google Cloud. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Oracle Database@Google Cloud roles

Role | Permissions  
---|---  
  
#### Oracle Database@Google Cloud admin 

(`roles/oracledatabase.admin`) Grants full access to manage all Oracle Database resources.  |  `oracledatabase.autonomousDatabaseBackups.*`

  * `oracledatabase.autonomousDatabaseBackups.clone`
  * `oracledatabase.autonomousDatabaseBackups.create`
  * `oracledatabase.autonomousDatabaseBackups.delete`
  * `oracledatabase.autonomousDatabaseBackups.get`
  * `oracledatabase.autonomousDatabaseBackups.list`

`oracledatabase.autonomousDatabaseCharacterSets.list` `oracledatabase.autonomousDatabases.*`

  * `oracledatabase.autonomousDatabases.clone`
  * `oracledatabase.autonomousDatabases.create`
  * `oracledatabase.autonomousDatabases.delete`
  * `oracledatabase.autonomousDatabases.failover`
  * `oracledatabase.autonomousDatabases.generateWallet`
  * `oracledatabase.autonomousDatabases.get`
  * `oracledatabase.autonomousDatabases.list`
  * `oracledatabase.autonomousDatabases.listRefreshableClones`
  * `oracledatabase.autonomousDatabases.refresh`
  * `oracledatabase.autonomousDatabases.restart`
  * `oracledatabase.autonomousDatabases.restore`
  * `oracledatabase.autonomousDatabases.start`
  * `oracledatabase.autonomousDatabases.stop`
  * `oracledatabase.autonomousDatabases.switchover`
  * `oracledatabase.autonomousDatabases.update`

`oracledatabase.autonomousDbVersions.list` `oracledatabase.cloudExadataInfrastructures.*`

  * `oracledatabase.cloudExadataInfrastructures.create`
  * `oracledatabase.cloudExadataInfrastructures.delete`
  * `oracledatabase.cloudExadataInfrastructures.get`
  * `oracledatabase.cloudExadataInfrastructures.list`
  * `oracledatabase.cloudExadataInfrastructures.update`
  * `oracledatabase.cloudExadataInfrastructures.use`

`oracledatabase.cloudVmClusters.*`

  * `oracledatabase.cloudVmClusters.create`
  * `oracledatabase.cloudVmClusters.delete`
  * `oracledatabase.cloudVmClusters.get`
  * `oracledatabase.cloudVmClusters.list`
  * `oracledatabase.cloudVmClusters.update`

`oracledatabase.databaseCharacterSets.list` `oracledatabase.databaseConnections.*`

  * `oracledatabase.databaseConnections.create`
  * `oracledatabase.databaseConnections.delete`
  * `oracledatabase.databaseConnections.executeSql`
  * `oracledatabase.databaseConnections.get`
  * `oracledatabase.databaseConnections.list`
  * `oracledatabase.databaseConnections.test`
  * `oracledatabase.databaseConnections.update`
  * `oracledatabase.databaseConnections.use`

`oracledatabase.databases.*`

  * `oracledatabase.databases.get`
  * `oracledatabase.databases.list`

`oracledatabase.dbNodes.list` `oracledatabase.dbServers.list` `oracledatabase.dbSystemComputePerformances.list` `oracledatabase.dbSystemInitialStorageSizes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.dbSystems.*`

  * `oracledatabase.dbSystems.create`
  * `oracledatabase.dbSystems.delete`
  * `oracledatabase.dbSystems.get`
  * `oracledatabase.dbSystems.list`
  * `oracledatabase.dbSystems.update`

`oracledatabase.dbVersions.list` `oracledatabase.entitlements.list` `oracledatabase.exadbVmClusters.*`

  * `oracledatabase.exadbVmClusters.create`
  * `oracledatabase.exadbVmClusters.delete`
  * `oracledatabase.exadbVmClusters.get`
  * `oracledatabase.exadbVmClusters.list`
  * `oracledatabase.exadbVmClusters.update`

`oracledatabase.exascaleDbStorageVaults.*`

  * `oracledatabase.exascaleDbStorageVaults.create`
  * `oracledatabase.exascaleDbStorageVaults.delete`
  * `oracledatabase.exascaleDbStorageVaults.get`
  * `oracledatabase.exascaleDbStorageVaults.list`
  * `oracledatabase.exascaleDbStorageVaults.update`
  * `oracledatabase.exascaleDbStorageVaults.use`

`oracledatabase.flexComponents.list` `oracledatabase.giVersions.list` `oracledatabase.goldenGateConnectionAssignments.*`

  * `oracledatabase.goldenGateConnectionAssignments.create`
  * `oracledatabase.goldenGateConnectionAssignments.delete`
  * `oracledatabase.goldenGateConnectionAssignments.get`
  * `oracledatabase.goldenGateConnectionAssignments.list`
  * `oracledatabase.goldenGateConnectionAssignments.test`
  * `oracledatabase.goldenGateConnectionAssignments.update`

`oracledatabase.goldenGateConnectionTypes.list` `oracledatabase.goldenGateConnections.*`

  * `oracledatabase.goldenGateConnections.create`
  * `oracledatabase.goldenGateConnections.delete`
  * `oracledatabase.goldenGateConnections.get`
  * `oracledatabase.goldenGateConnections.list`
  * `oracledatabase.goldenGateConnections.update`
  * `oracledatabase.goldenGateConnections.use`

`oracledatabase.goldenGateDeploymentEnvironments.list` `oracledatabase.goldenGateDeploymentTypes.list` `oracledatabase.goldenGateDeploymentVersions.list` `oracledatabase.goldenGateDeployments.*`

  * `oracledatabase.goldenGateDeployments.create`
  * `oracledatabase.goldenGateDeployments.delete`
  * `oracledatabase.goldenGateDeployments.get`
  * `oracledatabase.goldenGateDeployments.list`
  * `oracledatabase.goldenGateDeployments.start`
  * `oracledatabase.goldenGateDeployments.stop`
  * `oracledatabase.goldenGateDeployments.update`
  * `oracledatabase.goldenGateDeployments.use`

`oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.odbDnsZones.*`

  * `oracledatabase.odbDnsZones.create`
  * `oracledatabase.odbDnsZones.delete`
  * `oracledatabase.odbDnsZones.get`
  * `oracledatabase.odbDnsZones.list`

`oracledatabase.odbNetworks.*`

  * `oracledatabase.odbNetworks.create`
  * `oracledatabase.odbNetworks.delete`
  * `oracledatabase.odbNetworks.get`
  * `oracledatabase.odbNetworks.list`
  * `oracledatabase.odbNetworks.update`
  * `oracledatabase.odbNetworks.use`

`oracledatabase.odbSubnets.*`

  * `oracledatabase.odbSubnets.create`
  * `oracledatabase.odbSubnets.delete`
  * `oracledatabase.odbSubnets.get`
  * `oracledatabase.odbSubnets.list`
  * `oracledatabase.odbSubnets.update`
  * `oracledatabase.odbSubnets.use`

`oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`oracledatabase.serviceIntegrations.*`

  * `oracledatabase.serviceIntegrations.create`
  * `oracledatabase.serviceIntegrations.delete`
  * `oracledatabase.serviceIntegrations.get`
  * `oracledatabase.serviceIntegrations.list`

`oracledatabase.systemVersions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud viewer 

(`roles/oracledatabase.viewer`) Grants view access to all Oracle Database resources.  |  `oracledatabase.autonomousDatabaseBackups.get` `oracledatabase.autonomousDatabaseBackups.list` `oracledatabase.autonomousDatabaseCharacterSets.list` `oracledatabase.autonomousDatabases.get` `oracledatabase.autonomousDatabases.list` `oracledatabase.autonomousDatabases.listRefreshableClones` `oracledatabase.autonomousDbVersions.list` `oracledatabase.cloudExadataInfrastructures.get` `oracledatabase.cloudExadataInfrastructures.list` `oracledatabase.cloudVmClusters.get` `oracledatabase.cloudVmClusters.list` `oracledatabase.databaseCharacterSets.list` `oracledatabase.databaseConnections.get` `oracledatabase.databaseConnections.list` `oracledatabase.databases.*`

  * `oracledatabase.databases.get`
  * `oracledatabase.databases.list`

`oracledatabase.dbNodes.list` `oracledatabase.dbServers.list` `oracledatabase.dbSystemComputePerformances.list` `oracledatabase.dbSystemInitialStorageSizes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.dbSystems.get` `oracledatabase.dbSystems.list` `oracledatabase.dbVersions.list` `oracledatabase.entitlements.list` `oracledatabase.exadbVmClusters.get` `oracledatabase.exadbVmClusters.list` `oracledatabase.exascaleDbStorageVaults.get` `oracledatabase.exascaleDbStorageVaults.list` `oracledatabase.flexComponents.list` `oracledatabase.giVersions.list` `oracledatabase.goldenGateConnectionAssignments.get` `oracledatabase.goldenGateConnectionAssignments.list` `oracledatabase.goldenGateConnections.get` `oracledatabase.goldenGateConnections.list` `oracledatabase.goldenGateDeployments.get` `oracledatabase.goldenGateDeployments.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.odbDnsZones.get` `oracledatabase.odbDnsZones.list` `oracledatabase.odbNetworks.get` `oracledatabase.odbNetworks.list` `oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.operations.get` `oracledatabase.operations.list` `oracledatabase.pluggableDatabases.*`

  * `oracledatabase.pluggableDatabases.get`
  * `oracledatabase.pluggableDatabases.list`

`oracledatabase.serviceIntegrations.get` `oracledatabase.serviceIntegrations.list` `oracledatabase.systemVersions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Autonomous Database Admin 

(`roles/oracledatabase.autonomousDatabaseAdmin`) Grants full access to manage all Autonomous Database resources.  |  `oracledatabase.autonomousDatabaseBackups.*`

  * `oracledatabase.autonomousDatabaseBackups.clone`
  * `oracledatabase.autonomousDatabaseBackups.create`
  * `oracledatabase.autonomousDatabaseBackups.delete`
  * `oracledatabase.autonomousDatabaseBackups.get`
  * `oracledatabase.autonomousDatabaseBackups.list`

`oracledatabase.autonomousDatabaseCharacterSets.list` `oracledatabase.autonomousDatabases.*`

  * `oracledatabase.autonomousDatabases.clone`
  * `oracledatabase.autonomousDatabases.create`
  * `oracledatabase.autonomousDatabases.delete`
  * `oracledatabase.autonomousDatabases.failover`
  * `oracledatabase.autonomousDatabases.generateWallet`
  * `oracledatabase.autonomousDatabases.get`
  * `oracledatabase.autonomousDatabases.list`
  * `oracledatabase.autonomousDatabases.listRefreshableClones`
  * `oracledatabase.autonomousDatabases.refresh`
  * `oracledatabase.autonomousDatabases.restart`
  * `oracledatabase.autonomousDatabases.restore`
  * `oracledatabase.autonomousDatabases.start`
  * `oracledatabase.autonomousDatabases.stop`
  * `oracledatabase.autonomousDatabases.switchover`
  * `oracledatabase.autonomousDatabases.update`

`oracledatabase.autonomousDbVersions.list` `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.odbSubnets.use` `oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Autonomous Database Viewer 

(`roles/oracledatabase.autonomousDatabaseViewer`) Grants read access to see all Autonomous Database resources.  |  `oracledatabase.autonomousDatabaseBackups.get` `oracledatabase.autonomousDatabaseBackups.list` `oracledatabase.autonomousDatabaseCharacterSets.list` `oracledatabase.autonomousDatabases.get` `oracledatabase.autonomousDatabases.list` `oracledatabase.autonomousDatabases.listRefreshableClones` `oracledatabase.autonomousDbVersions.list` `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Infrastructure Admin 

(`roles/oracledatabase.cloudExadataInfrastructureAdmin`) Grants full access to manage all Exadata Infrastructure resources.  |  `oracledatabase.cloudExadataInfrastructures.create` `oracledatabase.cloudExadataInfrastructures.delete` `oracledatabase.cloudExadataInfrastructures.get` `oracledatabase.cloudExadataInfrastructures.list` `oracledatabase.cloudExadataInfrastructures.update` `oracledatabase.dbServers.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.flexComponents.list` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Infrastructure User 

(`roles/oracledatabase.cloudExadataInfrastructureUser`) Grants user access to use all Exadata Infrastructure resources.  |  `oracledatabase.cloudExadataInfrastructures.get` `oracledatabase.cloudExadataInfrastructures.list` `oracledatabase.cloudExadataInfrastructures.use` `oracledatabase.dbServers.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.flexComponents.list` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Infrastructure Viewer 

(`roles/oracledatabase.cloudExadataInfrastructureViewer`) Grants read access to see all Exadata Infrastructure resources.  |  `oracledatabase.cloudExadataInfrastructures.get` `oracledatabase.cloudExadataInfrastructures.list` `oracledatabase.dbServers.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.flexComponents.list` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud VM Cluster Admin 

(`roles/oracledatabase.cloudVmClusterAdmin`) Grants full access to manage all VM Cluster resources.  |  `oracledatabase.cloudExadataInfrastructures.list` `oracledatabase.cloudExadataInfrastructures.use` `oracledatabase.cloudVmClusters.*`

  * `oracledatabase.cloudVmClusters.create`
  * `oracledatabase.cloudVmClusters.delete`
  * `oracledatabase.cloudVmClusters.get`
  * `oracledatabase.cloudVmClusters.list`
  * `oracledatabase.cloudVmClusters.update`

`oracledatabase.dbNodes.list` `oracledatabase.dbServers.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.exascaleDbStorageVaults.get` `oracledatabase.exascaleDbStorageVaults.list` `oracledatabase.exascaleDbStorageVaults.use` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.odbSubnets.use` `oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`oracledatabase.systemVersions.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud VM Cluster Viewer 

(`roles/oracledatabase.cloudVmClusterViewer`) Grants read access to see all VM Cluster resources.  |  `oracledatabase.cloudVmClusters.get` `oracledatabase.cloudVmClusters.list` `oracledatabase.dbNodes.list` `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Container Database Viewer 

(`roles/oracledatabase.databaseViewer`) Grants read access to see all Container Database resources.  |  `oracledatabase.databases.*`

  * `oracledatabase.databases.get`
  * `oracledatabase.databases.list`

`oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `oracledatabase.pluggableDatabases.*`

  * `oracledatabase.pluggableDatabases.get`
  * `oracledatabase.pluggableDatabases.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud DB System Admin 

(`roles/oracledatabase.dbSystemAdmin`) Grants full access to manage all DB System resources.  |  `oracledatabase.databaseCharacterSets.list` `oracledatabase.databases.*`

  * `oracledatabase.databases.get`
  * `oracledatabase.databases.list`

`oracledatabase.dbSystemComputePerformances.list` `oracledatabase.dbSystemInitialStorageSizes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.dbSystems.*`

  * `oracledatabase.dbSystems.create`
  * `oracledatabase.dbSystems.delete`
  * `oracledatabase.dbSystems.get`
  * `oracledatabase.dbSystems.list`
  * `oracledatabase.dbSystems.update`

`oracledatabase.dbVersions.list` `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud DB System Viewer 

(`roles/oracledatabase.dbSystemViewer`) Grants read access to see all DB System resources.  |  `oracledatabase.databaseCharacterSets.list` `oracledatabase.databases.*`

  * `oracledatabase.databases.get`
  * `oracledatabase.databases.list`

`oracledatabase.dbSystemComputePerformances.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.dbSystems.get` `oracledatabase.dbSystems.list` `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin 

(`roles/oracledatabase.exadbVmClusterAdmin`) Grants full access to manage all Exadata Database Service on Exascale Infrastructure VM Cluster resources.  |  `oracledatabase.dbNodes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.exadbVmClusters.*`

  * `oracledatabase.exadbVmClusters.create`
  * `oracledatabase.exadbVmClusters.delete`
  * `oracledatabase.exadbVmClusters.get`
  * `oracledatabase.exadbVmClusters.list`
  * `oracledatabase.exadbVmClusters.update`

`oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer 

(`roles/oracledatabase.exadbVmClusterViewer`) Grants read access to see all Exadata Database Service on Exascale Infrastructure VM Cluster resources.  |  `oracledatabase.dbNodes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.exadbVmClusters.get` `oracledatabase.exadbVmClusters.list` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin 

(`roles/oracledatabase.exascaleDbStorageVaultAdmin`) Grants full access to manage all Exadata Database Service on Exascale Infrastructure Storage Vault resources.  |  `oracledatabase.dbNodes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.exascaleDbStorageVaults.create` `oracledatabase.exascaleDbStorageVaults.delete` `oracledatabase.exascaleDbStorageVaults.get` `oracledatabase.exascaleDbStorageVaults.list` `oracledatabase.exascaleDbStorageVaults.update` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User 

(`roles/oracledatabase.exascaleDbStorageVaultUser`) Grants permissions to use Exadata Database Service on Exascale Infrastructure Storage Vault resources.  |  `oracledatabase.dbNodes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.exascaleDbStorageVaults.get` `oracledatabase.exascaleDbStorageVaults.list` `oracledatabase.exascaleDbStorageVaults.use` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer 

(`roles/oracledatabase.exascaleDbStorageVaultViewer`) Grants read access to see all Exadata Database Service on Exascale Infrastructure Storage Vault resources.  |  `oracledatabase.dbNodes.list` `oracledatabase.dbSystemShapes.list` `oracledatabase.entitlements.list` `oracledatabase.exascaleDbStorageVaults.get` `oracledatabase.exascaleDbStorageVaults.list` `oracledatabase.giVersions.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.minorVersions.list` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud GoldenGate Connection Admin 

(`roles/oracledatabase.goldenGateConnectionAdmin`) Grants full access to manage all GoldenGate Connection resources.  |  `oracledatabase.entitlements.list` `oracledatabase.goldenGateConnectionTypes.list` `oracledatabase.goldenGateConnections.create` `oracledatabase.goldenGateConnections.delete` `oracledatabase.goldenGateConnections.get` `oracledatabase.goldenGateConnections.list` `oracledatabase.goldenGateConnections.update` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.odbSubnets.use` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud GoldenGate Connection Assignment Admin 

(`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`) Grants full access to manage all GoldenGate Connection Assignment resources.  |  `oracledatabase.goldenGateConnectionAssignments.*`

  * `oracledatabase.goldenGateConnectionAssignments.create`
  * `oracledatabase.goldenGateConnectionAssignments.delete`
  * `oracledatabase.goldenGateConnectionAssignments.get`
  * `oracledatabase.goldenGateConnectionAssignments.list`
  * `oracledatabase.goldenGateConnectionAssignments.test`
  * `oracledatabase.goldenGateConnectionAssignments.update`

`oracledatabase.goldenGateConnections.get` `oracledatabase.goldenGateConnections.list` `oracledatabase.goldenGateConnections.use` `oracledatabase.goldenGateDeployments.get` `oracledatabase.goldenGateDeployments.list` `oracledatabase.goldenGateDeployments.use` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer 

(`roles/oracledatabase.goldenGateConnectionAssignmentViewer`) Grants read access to see all GoldenGate Connection Assignment resources.  |  `oracledatabase.goldenGateConnectionAssignments.get` `oracledatabase.goldenGateConnectionAssignments.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud GoldenGate Connection Viewer 

(`roles/oracledatabase.goldenGateConnectionViewer`) Grants read access to see all GoldenGate Connection resources.  |  `oracledatabase.goldenGateConnections.get` `oracledatabase.goldenGateConnections.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google GoldenGate Connections User 

(`roles/oracledatabase.goldenGateConnectionsUser`) Grants use access to GoldenGate Connections resources.  |  `oracledatabase.goldenGateConnections.get` `oracledatabase.goldenGateConnections.list` `oracledatabase.goldenGateConnections.use` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud GoldenGate Deployment Admin 

(`roles/oracledatabase.goldenGateDeploymentAdmin`) Grants full access to manage all GoldenGate Deployment resources.  |  `oracledatabase.entitlements.list` `oracledatabase.goldenGateDeploymentEnvironments.list` `oracledatabase.goldenGateDeploymentTypes.list` `oracledatabase.goldenGateDeploymentVersions.list` `oracledatabase.goldenGateDeployments.create` `oracledatabase.goldenGateDeployments.delete` `oracledatabase.goldenGateDeployments.get` `oracledatabase.goldenGateDeployments.list` `oracledatabase.goldenGateDeployments.start` `oracledatabase.goldenGateDeployments.stop` `oracledatabase.goldenGateDeployments.update` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.odbSubnets.use` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud GoldenGate Deployment Viewer 

(`roles/oracledatabase.goldenGateDeploymentViewer`) Grants read access to see all GoldenGate Deployment resources.  |  `oracledatabase.goldenGateDeployments.get` `oracledatabase.goldenGateDeployments.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google GoldenGate Deployments User 

(`roles/oracledatabase.goldenGateDeploymentsUser`) Grants use access to GoldenGate Deployments resources.  |  `oracledatabase.goldenGateDeployments.get` `oracledatabase.goldenGateDeployments.list` `oracledatabase.goldenGateDeployments.use` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Network Admin 

(`roles/oracledatabase.networkAdmin`) Grants full access to manage all ODB Network and ODB Subnet resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbDnsZones.*`

  * `oracledatabase.odbDnsZones.create`
  * `oracledatabase.odbDnsZones.delete`
  * `oracledatabase.odbDnsZones.get`
  * `oracledatabase.odbDnsZones.list`

`oracledatabase.odbNetworks.*`

  * `oracledatabase.odbNetworks.create`
  * `oracledatabase.odbNetworks.delete`
  * `oracledatabase.odbNetworks.get`
  * `oracledatabase.odbNetworks.list`
  * `oracledatabase.odbNetworks.update`
  * `oracledatabase.odbNetworks.use`

`oracledatabase.odbSubnets.*`

  * `oracledatabase.odbSubnets.create`
  * `oracledatabase.odbSubnets.delete`
  * `oracledatabase.odbSubnets.get`
  * `oracledatabase.odbSubnets.list`
  * `oracledatabase.odbSubnets.update`
  * `oracledatabase.odbSubnets.use`

`oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google ODB Network Admin 

(`roles/oracledatabase.odbNetworkAdmin`) Grants full access to manage all ODB Network resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbNetworks.*`

  * `oracledatabase.odbNetworks.create`
  * `oracledatabase.odbNetworks.delete`
  * `oracledatabase.odbNetworks.get`
  * `oracledatabase.odbNetworks.list`
  * `oracledatabase.odbNetworks.update`
  * `oracledatabase.odbNetworks.use`

`oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google ODB Network Viewer 

(`roles/oracledatabase.odbNetworkViewer`) Grants read access to see all ODB Network resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbNetworks.get` `oracledatabase.odbNetworks.list` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google ODB Subnet Admin 

(`roles/oracledatabase.odbSubnetAdmin`) Grants full access to manage all ODB Subnet resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbSubnets.*`

  * `oracledatabase.odbSubnets.create`
  * `oracledatabase.odbSubnets.delete`
  * `oracledatabase.odbSubnets.get`
  * `oracledatabase.odbSubnets.list`
  * `oracledatabase.odbSubnets.update`
  * `oracledatabase.odbSubnets.use`

`oracledatabase.operations.*`

  * `oracledatabase.operations.cancel`
  * `oracledatabase.operations.delete`
  * `oracledatabase.operations.get`
  * `oracledatabase.operations.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google ODB Subnet User 

(`roles/oracledatabase.odbSubnetUser`) Grants use access to ODB Subnet resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.odbSubnets.use` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google ODB Subnet Viewer 

(`roles/oracledatabase.odbSubnetViewer`) Grants read access to see all ODB Subnet resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.odbSubnets.get` `oracledatabase.odbSubnets.list` `oracledatabase.operations.get` `oracledatabase.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Oracle Database@Google Cloud Pluggable Database Viewer 

(`roles/oracledatabase.pluggableDatabaseViewer`) Grants read access to see all Pluggable Database resources.  |  `oracledatabase.entitlements.list` `oracledatabase.locations.*`

  * `oracledatabase.locations.get`
  * `oracledatabase.locations.list`

`oracledatabase.operations.get` `oracledatabase.operations.list` `oracledatabase.pluggableDatabases.*`

  * `oracledatabase.pluggableDatabases.get`
  * `oracledatabase.pluggableDatabases.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Oracle Database@Google Cloud permissions

Permission | Included in roles  
---|---  
  
#### `oracledatabase.autonomousDatabaseBackups.clone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabaseBackups.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabaseBackups.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabaseBackups.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.autonomousDatabaseBackups.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.autonomousDatabaseCharacterSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.autonomousDatabases.clone`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.failover`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.generateWallet`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.autonomousDatabases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.autonomousDatabases.listRefreshableClones`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.autonomousDatabases.refresh`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.restart`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.restore`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.switchover`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDatabases.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)   
  
#### `oracledatabase.autonomousDbVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)   
  
#### `oracledatabase.cloudExadataInfrastructures.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)   
  
#### `oracledatabase.cloudExadataInfrastructures.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)   
  
#### `oracledatabase.cloudExadataInfrastructures.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)   
  
#### `oracledatabase.cloudExadataInfrastructures.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
#### `oracledatabase.cloudExadataInfrastructures.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)   
  
#### `oracledatabase.cloudExadataInfrastructures.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
#### `oracledatabase.cloudVmClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
#### `oracledatabase.cloudVmClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
#### `oracledatabase.cloudVmClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)   
  
#### `oracledatabase.cloudVmClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)   
  
#### `oracledatabase.cloudVmClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
#### `oracledatabase.databaseCharacterSets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)   
  
#### `oracledatabase.databaseConnections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.databaseConnections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.databaseConnections.executeSql`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.databaseConnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `oracledatabase.databaseConnections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `oracledatabase.databaseConnections.test`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.databaseConnections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.databaseConnections.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.databases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)   
  
#### `oracledatabase.databases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)   
  
#### `oracledatabase.dbNodes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)   
  
#### `oracledatabase.dbServers.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
#### `oracledatabase.dbSystemComputePerformances.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)   
  
#### `oracledatabase.dbSystemInitialStorageSizes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)   
  
#### `oracledatabase.dbSystemShapes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)   
  
#### `oracledatabase.dbSystems.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)   
  
#### `oracledatabase.dbSystems.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)   
  
#### `oracledatabase.dbSystems.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)   
  
#### `oracledatabase.dbSystems.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)   
  
#### `oracledatabase.dbSystems.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)   
  
#### `oracledatabase.dbVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)   
  
#### `oracledatabase.entitlements.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)   
  
#### `oracledatabase.exadbVmClusters.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)   
  
#### `oracledatabase.exadbVmClusters.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)   
  
#### `oracledatabase.exadbVmClusters.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)   
  
#### `oracledatabase.exadbVmClusters.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)   
  
#### `oracledatabase.exadbVmClusters.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)   
  
#### `oracledatabase.exascaleDbStorageVaults.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)   
  
#### `oracledatabase.exascaleDbStorageVaults.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)   
  
#### `oracledatabase.exascaleDbStorageVaults.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)   
  
#### `oracledatabase.exascaleDbStorageVaults.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)   
  
#### `oracledatabase.exascaleDbStorageVaults.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)   
  
#### `oracledatabase.exascaleDbStorageVaults.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)   
  
#### `oracledatabase.flexComponents.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)   
  
#### `oracledatabase.giVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)   
  
#### `oracledatabase.goldenGateConnectionAssignments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)   
  
#### `oracledatabase.goldenGateConnectionAssignments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)   
  
#### `oracledatabase.goldenGateConnectionAssignments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentViewer) (`roles/oracledatabase.goldenGateConnectionAssignmentViewer`)   
  
#### `oracledatabase.goldenGateConnectionAssignments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentViewer) (`roles/oracledatabase.goldenGateConnectionAssignmentViewer`)   
  
#### `oracledatabase.goldenGateConnectionAssignments.test`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)   
  
#### `oracledatabase.goldenGateConnectionAssignments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)   
  
#### `oracledatabase.goldenGateConnectionTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)   
  
#### `oracledatabase.goldenGateConnections.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)   
  
#### `oracledatabase.goldenGateConnections.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)   
  
#### `oracledatabase.goldenGateConnections.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionViewer) (`roles/oracledatabase.goldenGateConnectionViewer`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)   
  
#### `oracledatabase.goldenGateConnections.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionViewer) (`roles/oracledatabase.goldenGateConnectionViewer`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)   
  
#### `oracledatabase.goldenGateConnections.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)   
  
#### `oracledatabase.goldenGateConnections.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)   
  
#### `oracledatabase.goldenGateDeploymentEnvironments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeploymentTypes.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeploymentVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeployments.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeployments.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeployments.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentViewer) (`roles/oracledatabase.goldenGateDeploymentViewer`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)   
  
#### `oracledatabase.goldenGateDeployments.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentViewer) (`roles/oracledatabase.goldenGateDeploymentViewer`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)   
  
#### `oracledatabase.goldenGateDeployments.start`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeployments.stop`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeployments.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)   
  
#### `oracledatabase.goldenGateDeployments.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)   
  
#### `oracledatabase.locations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentViewer) (`roles/oracledatabase.goldenGateConnectionAssignmentViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionViewer) (`roles/oracledatabase.goldenGateConnectionViewer`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentViewer) (`roles/oracledatabase.goldenGateDeploymentViewer`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)   
  
#### `oracledatabase.locations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentViewer) (`roles/oracledatabase.goldenGateConnectionAssignmentViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionViewer) (`roles/oracledatabase.goldenGateConnectionViewer`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentViewer) (`roles/oracledatabase.goldenGateDeploymentViewer`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)   
  
#### `oracledatabase.minorVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)   
  
#### `oracledatabase.odbDnsZones.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)   
  
#### `oracledatabase.odbDnsZones.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)   
  
#### `oracledatabase.odbDnsZones.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)   
  
#### `oracledatabase.odbDnsZones.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)   
  
#### `oracledatabase.odbNetworks.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.odbNetworks.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)   
  
#### `oracledatabase.odbNetworks.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.odbNetworks.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.odbNetworks.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)   
  
#### `oracledatabase.odbNetworks.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)   
  
#### `oracledatabase.odbSubnets.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.odbSubnets.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)   
  
#### `oracledatabase.odbSubnets.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.odbSubnets.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.odbSubnets.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)   
  
#### `oracledatabase.odbSubnets.use`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)   
  
#### `oracledatabase.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)   
  
#### `oracledatabase.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentViewer) (`roles/oracledatabase.goldenGateConnectionAssignmentViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionViewer) (`roles/oracledatabase.goldenGateConnectionViewer`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentViewer) (`roles/oracledatabase.goldenGateDeploymentViewer`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Autonomous Database Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseAdmin) (`roles/oracledatabase.autonomousDatabaseAdmin`)  [Oracle Database@Google Cloud Autonomous Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.autonomousDatabaseViewer) (`roles/oracledatabase.autonomousDatabaseViewer`)  [Oracle Database@Google Cloud Exadata Infrastructure Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureAdmin) (`roles/oracledatabase.cloudExadataInfrastructureAdmin`)  [Oracle Database@Google Cloud Exadata Infrastructure User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureUser) (`roles/oracledatabase.cloudExadataInfrastructureUser`)  [Oracle Database@Google Cloud Exadata Infrastructure Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudExadataInfrastructureViewer) (`roles/oracledatabase.cloudExadataInfrastructureViewer`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)  [Oracle Database@Google Cloud VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterViewer) (`roles/oracledatabase.cloudVmClusterViewer`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud DB System Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemAdmin) (`roles/oracledatabase.dbSystemAdmin`)  [Oracle Database@Google Cloud DB System Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.dbSystemViewer) (`roles/oracledatabase.dbSystemViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterAdmin) (`roles/oracledatabase.exadbVmClusterAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure VM Cluster Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exadbVmClusterViewer) (`roles/oracledatabase.exadbVmClusterViewer`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultAdmin) (`roles/oracledatabase.exascaleDbStorageVaultAdmin`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultUser) (`roles/oracledatabase.exascaleDbStorageVaultUser`)  [Oracle Database@Google Cloud Exadata Database Service on Exascale Infrastructure Storage Vault Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.exascaleDbStorageVaultViewer) (`roles/oracledatabase.exascaleDbStorageVaultViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAdmin) (`roles/oracledatabase.goldenGateConnectionAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentAdmin) (`roles/oracledatabase.goldenGateConnectionAssignmentAdmin`)  [Oracle Database@Google Cloud GoldenGate Connection Assignment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionAssignmentViewer) (`roles/oracledatabase.goldenGateConnectionAssignmentViewer`)  [Oracle Database@Google Cloud GoldenGate Connection Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionViewer) (`roles/oracledatabase.goldenGateConnectionViewer`)  [Oracle Database@Google GoldenGate Connections User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateConnectionsUser) (`roles/oracledatabase.goldenGateConnectionsUser`)  [Oracle Database@Google Cloud GoldenGate Deployment Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentAdmin) (`roles/oracledatabase.goldenGateDeploymentAdmin`)  [Oracle Database@Google Cloud GoldenGate Deployment Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentViewer) (`roles/oracledatabase.goldenGateDeploymentViewer`)  [Oracle Database@Google GoldenGate Deployments User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.goldenGateDeploymentsUser) (`roles/oracledatabase.goldenGateDeploymentsUser`)  [Oracle Database@Google Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.networkAdmin) (`roles/oracledatabase.networkAdmin`)  [Oracle Database@Google ODB Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkAdmin) (`roles/oracledatabase.odbNetworkAdmin`)  [Oracle Database@Google ODB Network Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbNetworkViewer) (`roles/oracledatabase.odbNetworkViewer`)  [Oracle Database@Google ODB Subnet Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetAdmin) (`roles/oracledatabase.odbSubnetAdmin`)  [Oracle Database@Google ODB Subnet User](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetUser) (`roles/oracledatabase.odbSubnetUser`)  [Oracle Database@Google ODB Subnet Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.odbSubnetViewer) (`roles/oracledatabase.odbSubnetViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)  Service agent roles **Warning:** Don't grant service agent roles to any principals except [service agents](https://docs.cloud.google.com/iam/docs/service-agents). 

  * [Oracle Database@Google Cloud Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/oci#oci.serviceAgent) (`roles/oci.serviceAgent`) 

  
  
#### `oracledatabase.pluggableDatabases.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)   
  
#### `oracledatabase.pluggableDatabases.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud Container Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.databaseViewer) (`roles/oracledatabase.databaseViewer`)  [Oracle Database@Google Cloud Pluggable Database Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.pluggableDatabaseViewer) (`roles/oracledatabase.pluggableDatabaseViewer`)   
  
#### `oracledatabase.serviceIntegrations.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.serviceIntegrations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)   
  
#### `oracledatabase.serviceIntegrations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `oracledatabase.serviceIntegrations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `oracledatabase.systemVersions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Oracle Database@Google Cloud admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.admin) (`roles/oracledatabase.admin`)  [Oracle Database@Google Cloud viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.viewer) (`roles/oracledatabase.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Oracle Database@Google Cloud VM Cluster Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/oracledatabase#oracledatabase.cloudVmClusterAdmin) (`roles/oracledatabase.cloudVmClusterAdmin`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
