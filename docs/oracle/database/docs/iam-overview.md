---
url: https://docs.cloud.google.com/oracle/database/docs/iam-overview/
title: IAM overview \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:02.729378+00:00
---

# IAM overview  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/iam-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  IAM overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Oracle Database@Google Cloud Identity and Access Management (IAM) integration and how you can use IAM to manage access across your resources.

IAM lets you control user and group access to Oracle Database@Google Cloud resources for the Exadata Database and Autonomous AI Database services. Roles are defined at the Google Cloud project level. For example, giving a user `viewer` access in an Exadata Infrastructure instance would grant them `viewer` access to all Exadata Infrastructure instances and Exadata VM Clusters in that project.

Using access control with IAM, you can grant permissions to a user or a group without modifying each instance, cluster, or database individually. Oracle Database@Google Cloud provides a set of predefined roles to manage access. You can use predefined roles or specific permissions to grant access to users. For more information about how IAM works at Google Cloud, see [IAM documentation](https://docs.cloud.google.com/iam/docs).

## Oracle Database@Google Cloud predefined roles

Predefined roles contain permissions that allow Google Cloud project members to perform specific actions on Oracle Database@Google Cloud resources. The role you grant to a project member controls what actions they can take in that project. Project members can be individuals, groups, or service accounts. You can grant multiple roles to the same project member, and can change the roles granted at any time.

Broader roles include the more narrowly defined roles. For example, the **Cloud Exadata Infrastructure Admin** role includes all permissions of the **Cloud Exadata Infrastructure Viewer** role, along with additional permissions of the **Cloud Exadata Infrastructure Admin** role.

Each IAM role for Oracle Database@Google Cloud contains permissions that give the principal access to specific resources as shown in the following table.

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
  
## What's next

  * Learn more about how to [grant access using IAM](https://docs.cloud.google.com/oracle/database/docs/iam-roles).
  * [Learn more about Oracle Database@Google Cloud](https://docs.cloud.google.com/oracle/database/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
