---
url: https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseConnection/
title: Class OracleDatabaseConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:47.352043+00:00
---

# Class OracleDatabaseConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class OracleDatabaseConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0 

The [`OracleDatabaseConnection`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseConnection) object for [`OracleDatabaseClient`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`OracleDatabaseClient`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`OracleDatabaseClient`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1_1_1OracleDatabaseClient).

To create a concrete instance, see [`MakeOracleDatabaseConnection()`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/namespacegoogle_1_1cloud_1_1oracledatabase__v1).

For mocking, see [`oracledatabase_v1_mocks::MockOracleDatabaseConnection`](https://docs.cloud.google.com/cpp/docs/reference/oracledatabase/latest/classgoogle_1_1cloud_1_1oracledatabase__v1__mocks_1_1MockOracleDatabaseConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListCloudExadataInfrastructures(google::cloud::oracledatabase::v1::ListCloudExadataInfrastructuresRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListCloudExadataInfrastructuresRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::CloudExadataInfrastructure >` |   
  
### virtual GetCloudExadataInfrastructure(google::cloud::oracledatabase::v1::GetCloudExadataInfrastructureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::CloudExadataInfrastructure >` |   
  
### virtual CreateCloudExadataInfrastructure(google::cloud::oracledatabase::v1::CreateCloudExadataInfrastructureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::CloudExadataInfrastructure > >` |   
  
### virtual CreateCloudExadataInfrastructure(NoAwaitTag, google::cloud::oracledatabase::v1::CreateCloudExadataInfrastructureRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateCloudExadataInfrastructure(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::CloudExadataInfrastructure > >` |   
  
### virtual DeleteCloudExadataInfrastructure(google::cloud::oracledatabase::v1::DeleteCloudExadataInfrastructureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteCloudExadataInfrastructure(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteCloudExadataInfrastructureRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteCloudExadataInfrastructure(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ConfigureExascaleCloudExadataInfrastructure(google::cloud::oracledatabase::v1::ConfigureExascaleCloudExadataInfrastructureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ConfigureExascaleCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::CloudExadataInfrastructure > >` |   
  
### virtual ConfigureExascaleCloudExadataInfrastructure(NoAwaitTag, google::cloud::oracledatabase::v1::ConfigureExascaleCloudExadataInfrastructureRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::ConfigureExascaleCloudExadataInfrastructureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ConfigureExascaleCloudExadataInfrastructure(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::CloudExadataInfrastructure > >` |   
  
### virtual ListCloudVmClusters(google::cloud::oracledatabase::v1::ListCloudVmClustersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListCloudVmClustersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::CloudVmCluster >` |   
  
### virtual GetCloudVmCluster(google::cloud::oracledatabase::v1::GetCloudVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetCloudVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::CloudVmCluster >` |   
  
### virtual CreateCloudVmCluster(google::cloud::oracledatabase::v1::CreateCloudVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateCloudVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::CloudVmCluster > >` |   
  
### virtual CreateCloudVmCluster(NoAwaitTag, google::cloud::oracledatabase::v1::CreateCloudVmClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateCloudVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateCloudVmCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::CloudVmCluster > >` |   
  
### virtual DeleteCloudVmCluster(google::cloud::oracledatabase::v1::DeleteCloudVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteCloudVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteCloudVmCluster(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteCloudVmClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteCloudVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteCloudVmCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ListEntitlements(google::cloud::oracledatabase::v1::ListEntitlementsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListEntitlementsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::Entitlement >` |   
  
### virtual ListDbServers(google::cloud::oracledatabase::v1::ListDbServersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDbServersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DbServer >` |   
  
### virtual ListDbNodes(google::cloud::oracledatabase::v1::ListDbNodesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDbNodesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DbNode >` |   
  
### virtual ListGiVersions(google::cloud::oracledatabase::v1::ListGiVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGiVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GiVersion >` |   
  
### virtual ListMinorVersions(google::cloud::oracledatabase::v1::ListMinorVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListMinorVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::MinorVersion >` |   
  
### virtual ListDbSystemShapes(google::cloud::oracledatabase::v1::ListDbSystemShapesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDbSystemShapesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DbSystemShape >` |   
  
### virtual ListAutonomousDatabases(google::cloud::oracledatabase::v1::ListAutonomousDatabasesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListAutonomousDatabasesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::AutonomousDatabase >` |   
  
### virtual GetAutonomousDatabase(google::cloud::oracledatabase::v1::GetAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase >` |   
  
### virtual CreateAutonomousDatabase(google::cloud::oracledatabase::v1::CreateAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual CreateAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::CreateAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual UpdateAutonomousDatabase(google::cloud::oracledatabase::v1::UpdateAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::UpdateAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual UpdateAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::UpdateAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::UpdateAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual DeleteAutonomousDatabase(google::cloud::oracledatabase::v1::DeleteAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual RestoreAutonomousDatabase(google::cloud::oracledatabase::v1::RestoreAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::RestoreAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual RestoreAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::RestoreAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::RestoreAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RestoreAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual GenerateAutonomousDatabaseWallet(google::cloud::oracledatabase::v1::GenerateAutonomousDatabaseWalletRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GenerateAutonomousDatabaseWalletRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::GenerateAutonomousDatabaseWalletResponse >` |   
  
### virtual ListAutonomousDbVersions(google::cloud::oracledatabase::v1::ListAutonomousDbVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListAutonomousDbVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::AutonomousDbVersion >` |   
  
### virtual ListAutonomousDatabaseCharacterSets(google::cloud::oracledatabase::v1::ListAutonomousDatabaseCharacterSetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListAutonomousDatabaseCharacterSetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::AutonomousDatabaseCharacterSet >` |   
  
### virtual ListAutonomousDatabaseBackups(google::cloud::oracledatabase::v1::ListAutonomousDatabaseBackupsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListAutonomousDatabaseBackupsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::AutonomousDatabaseBackup >` |   
  
### virtual StopAutonomousDatabase(google::cloud::oracledatabase::v1::StopAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::StopAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual StopAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::StopAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::StopAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual StopAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual StartAutonomousDatabase(google::cloud::oracledatabase::v1::StartAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::StartAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual StartAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::StartAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::StartAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual StartAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual RestartAutonomousDatabase(google::cloud::oracledatabase::v1::RestartAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::RestartAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual RestartAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::RestartAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::RestartAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RestartAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual SwitchoverAutonomousDatabase(google::cloud::oracledatabase::v1::SwitchoverAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::SwitchoverAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual SwitchoverAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::SwitchoverAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::SwitchoverAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual SwitchoverAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual FailoverAutonomousDatabase(google::cloud::oracledatabase::v1::FailoverAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::FailoverAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual FailoverAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::FailoverAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::FailoverAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual FailoverAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual RefreshAutonomousDatabase(google::cloud::oracledatabase::v1::RefreshAutonomousDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::RefreshAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual RefreshAutonomousDatabase(NoAwaitTag, google::cloud::oracledatabase::v1::RefreshAutonomousDatabaseRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::RefreshAutonomousDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RefreshAutonomousDatabase(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabase > >` |   
  
### virtual GetAutonomousDatabaseRefreshableClones(google::cloud::oracledatabase::v1::GetAutonomousDatabaseRefreshableClonesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetAutonomousDatabaseRefreshableClonesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::AutonomousDatabaseRefreshableClones >` |   
  
### virtual ListOdbNetworks(google::cloud::oracledatabase::v1::ListOdbNetworksRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListOdbNetworksRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::OdbNetwork >` |   
  
### virtual GetOdbNetwork(google::cloud::oracledatabase::v1::GetOdbNetworkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetOdbNetworkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::OdbNetwork >` |   
  
### virtual CreateOdbNetwork(google::cloud::oracledatabase::v1::CreateOdbNetworkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateOdbNetworkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OdbNetwork > >` |   
  
### virtual CreateOdbNetwork(NoAwaitTag, google::cloud::oracledatabase::v1::CreateOdbNetworkRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateOdbNetworkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateOdbNetwork(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OdbNetwork > >` |   
  
### virtual DeleteOdbNetwork(google::cloud::oracledatabase::v1::DeleteOdbNetworkRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteOdbNetworkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteOdbNetwork(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteOdbNetworkRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteOdbNetworkRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOdbNetwork(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ListOdbSubnets(google::cloud::oracledatabase::v1::ListOdbSubnetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListOdbSubnetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::OdbSubnet >` |   
  
### virtual GetOdbSubnet(google::cloud::oracledatabase::v1::GetOdbSubnetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetOdbSubnetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::OdbSubnet >` |   
  
### virtual CreateOdbSubnet(google::cloud::oracledatabase::v1::CreateOdbSubnetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateOdbSubnetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OdbSubnet > >` |   
  
### virtual CreateOdbSubnet(NoAwaitTag, google::cloud::oracledatabase::v1::CreateOdbSubnetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateOdbSubnetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateOdbSubnet(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OdbSubnet > >` |   
  
### virtual DeleteOdbSubnet(google::cloud::oracledatabase::v1::DeleteOdbSubnetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteOdbSubnetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteOdbSubnet(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteOdbSubnetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteOdbSubnetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOdbSubnet(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ListExadbVmClusters(google::cloud::oracledatabase::v1::ListExadbVmClustersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListExadbVmClustersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::ExadbVmCluster >` |   
  
### virtual GetExadbVmCluster(google::cloud::oracledatabase::v1::GetExadbVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster >` |   
  
### virtual CreateExadbVmCluster(google::cloud::oracledatabase::v1::CreateExadbVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster > >` |   
  
### virtual CreateExadbVmCluster(NoAwaitTag, google::cloud::oracledatabase::v1::CreateExadbVmClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateExadbVmCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster > >` |   
  
### virtual DeleteExadbVmCluster(google::cloud::oracledatabase::v1::DeleteExadbVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteExadbVmCluster(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteExadbVmClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteExadbVmCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual UpdateExadbVmCluster(google::cloud::oracledatabase::v1::UpdateExadbVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::UpdateExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster > >` |   
  
### virtual UpdateExadbVmCluster(NoAwaitTag, google::cloud::oracledatabase::v1::UpdateExadbVmClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::UpdateExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateExadbVmCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster > >` |   
  
### virtual RemoveVirtualMachineExadbVmCluster(google::cloud::oracledatabase::v1::RemoveVirtualMachineExadbVmClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::RemoveVirtualMachineExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster > >` |   
  
### virtual RemoveVirtualMachineExadbVmCluster(NoAwaitTag, google::cloud::oracledatabase::v1::RemoveVirtualMachineExadbVmClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::RemoveVirtualMachineExadbVmClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RemoveVirtualMachineExadbVmCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExadbVmCluster > >` |   
  
### virtual ListExascaleDbStorageVaults(google::cloud::oracledatabase::v1::ListExascaleDbStorageVaultsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListExascaleDbStorageVaultsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::ExascaleDbStorageVault >` |   
  
### virtual GetExascaleDbStorageVault(google::cloud::oracledatabase::v1::GetExascaleDbStorageVaultRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetExascaleDbStorageVaultRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::ExascaleDbStorageVault >` |   
  
### virtual CreateExascaleDbStorageVault(google::cloud::oracledatabase::v1::CreateExascaleDbStorageVaultRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateExascaleDbStorageVaultRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExascaleDbStorageVault > >` |   
  
### virtual CreateExascaleDbStorageVault(NoAwaitTag, google::cloud::oracledatabase::v1::CreateExascaleDbStorageVaultRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateExascaleDbStorageVaultRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateExascaleDbStorageVault(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::ExascaleDbStorageVault > >` |   
  
### virtual DeleteExascaleDbStorageVault(google::cloud::oracledatabase::v1::DeleteExascaleDbStorageVaultRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteExascaleDbStorageVaultRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteExascaleDbStorageVault(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteExascaleDbStorageVaultRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteExascaleDbStorageVaultRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteExascaleDbStorageVault(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ListDbSystemInitialStorageSizes(google::cloud::oracledatabase::v1::ListDbSystemInitialStorageSizesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDbSystemInitialStorageSizesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DbSystemInitialStorageSize >` |   
  
### virtual ListDatabases(google::cloud::oracledatabase::v1::ListDatabasesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDatabasesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::Database >` |   
  
### virtual GetDatabase(google::cloud::oracledatabase::v1::GetDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::Database >` |   
  
### virtual ListPluggableDatabases(google::cloud::oracledatabase::v1::ListPluggableDatabasesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListPluggableDatabasesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::PluggableDatabase >` |   
  
### virtual GetPluggableDatabase(google::cloud::oracledatabase::v1::GetPluggableDatabaseRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetPluggableDatabaseRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::PluggableDatabase >` |   
  
### virtual ListDbSystems(google::cloud::oracledatabase::v1::ListDbSystemsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDbSystemsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DbSystem >` |   
  
### virtual GetDbSystem(google::cloud::oracledatabase::v1::GetDbSystemRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetDbSystemRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::DbSystem >` |   
  
### virtual CreateDbSystem(google::cloud::oracledatabase::v1::CreateDbSystemRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateDbSystemRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::DbSystem > >` |   
  
### virtual CreateDbSystem(NoAwaitTag, google::cloud::oracledatabase::v1::CreateDbSystemRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateDbSystemRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateDbSystem(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::DbSystem > >` |   
  
### virtual DeleteDbSystem(google::cloud::oracledatabase::v1::DeleteDbSystemRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteDbSystemRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteDbSystem(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteDbSystemRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteDbSystemRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteDbSystem(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ListGoldengateDeployments(google::cloud::oracledatabase::v1::ListGoldengateDeploymentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateDeploymentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateDeployment >` |   
  
### virtual GetGoldengateDeployment(google::cloud::oracledatabase::v1::GetGoldengateDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment >` |   
  
### virtual CreateGoldengateDeployment(google::cloud::oracledatabase::v1::CreateGoldengateDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment > >` |   
  
### virtual CreateGoldengateDeployment(NoAwaitTag, google::cloud::oracledatabase::v1::CreateGoldengateDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateGoldengateDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment > >` |   
  
### virtual DeleteGoldengateDeployment(google::cloud::oracledatabase::v1::DeleteGoldengateDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteGoldengateDeployment(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteGoldengateDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteGoldengateDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual StopGoldengateDeployment(google::cloud::oracledatabase::v1::StopGoldengateDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::StopGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment > >` |   
  
### virtual StopGoldengateDeployment(NoAwaitTag, google::cloud::oracledatabase::v1::StopGoldengateDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::StopGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual StopGoldengateDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment > >` |   
  
### virtual StartGoldengateDeployment(google::cloud::oracledatabase::v1::StartGoldengateDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::StartGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment > >` |   
  
### virtual StartGoldengateDeployment(NoAwaitTag, google::cloud::oracledatabase::v1::StartGoldengateDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::StartGoldengateDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual StartGoldengateDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateDeployment > >` |   
  
### virtual ListGoldengateConnections(google::cloud::oracledatabase::v1::ListGoldengateConnectionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateConnectionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateConnection >` |   
  
### virtual GetGoldengateConnection(google::cloud::oracledatabase::v1::GetGoldengateConnectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetGoldengateConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::GoldengateConnection >` |   
  
### virtual CreateGoldengateConnection(google::cloud::oracledatabase::v1::CreateGoldengateConnectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateGoldengateConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateConnection > >` |   
  
### virtual CreateGoldengateConnection(NoAwaitTag, google::cloud::oracledatabase::v1::CreateGoldengateConnectionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateGoldengateConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateGoldengateConnection(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateConnection > >` |   
  
### virtual DeleteGoldengateConnection(google::cloud::oracledatabase::v1::DeleteGoldengateConnectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteGoldengateConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteGoldengateConnection(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteGoldengateConnectionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteGoldengateConnectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteGoldengateConnection(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual ListGoldengateDeploymentVersions(google::cloud::oracledatabase::v1::ListGoldengateDeploymentVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateDeploymentVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateDeploymentVersion >` |   
  
### virtual ListGoldengateDeploymentTypes(google::cloud::oracledatabase::v1::ListGoldengateDeploymentTypesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateDeploymentTypesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateDeploymentType >` |   
  
### virtual ListGoldengateDeploymentEnvironments(google::cloud::oracledatabase::v1::ListGoldengateDeploymentEnvironmentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateDeploymentEnvironmentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateDeploymentEnvironment >` |   
  
### virtual ListGoldengateConnectionTypes(google::cloud::oracledatabase::v1::ListGoldengateConnectionTypesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateConnectionTypesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateConnectionType >` |   
  
### virtual ListDbVersions(google::cloud::oracledatabase::v1::ListDbVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDbVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DbVersion >` |   
  
### virtual ListDatabaseCharacterSets(google::cloud::oracledatabase::v1::ListDatabaseCharacterSetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListDatabaseCharacterSetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::DatabaseCharacterSet >` |   
  
### virtual ListGoldengateConnectionAssignments(google::cloud::oracledatabase::v1::ListGoldengateConnectionAssignmentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::ListGoldengateConnectionAssignmentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::oracledatabase::v1::GoldengateConnectionAssignment >` |   
  
### virtual GetGoldengateConnectionAssignment(google::cloud::oracledatabase::v1::GetGoldengateConnectionAssignmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::GetGoldengateConnectionAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::GoldengateConnectionAssignment >` |   
  
### virtual CreateGoldengateConnectionAssignment(google::cloud::oracledatabase::v1::CreateGoldengateConnectionAssignmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::CreateGoldengateConnectionAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateConnectionAssignment > >` |   
  
### virtual CreateGoldengateConnectionAssignment(NoAwaitTag, google::cloud::oracledatabase::v1::CreateGoldengateConnectionAssignmentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::CreateGoldengateConnectionAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateGoldengateConnectionAssignment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::GoldengateConnectionAssignment > >` |   
  
### virtual DeleteGoldengateConnectionAssignment(google::cloud::oracledatabase::v1::DeleteGoldengateConnectionAssignmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::DeleteGoldengateConnectionAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual DeleteGoldengateConnectionAssignment(NoAwaitTag, google::cloud::oracledatabase::v1::DeleteGoldengateConnectionAssignmentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::oracledatabase::v1::DeleteGoldengateConnectionAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteGoldengateConnectionAssignment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::oracledatabase::v1::OperationMetadata > >` |   
  
### virtual TestGoldengateConnectionAssignment(google::cloud::oracledatabase::v1::TestGoldengateConnectionAssignmentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::oracledatabase::v1::TestGoldengateConnectionAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::oracledatabase::v1::TestGoldengateConnectionAssignmentResponse >` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
