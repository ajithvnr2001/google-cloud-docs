---
url: https://docs.cloud.google.com/cpp/docs/reference/redis/latest/classgoogle_1_1cloud_1_1redis__cluster__v1_1_1CloudRedisClusterConnectionIdempotencyPolicy/
title: Class CloudRedisClusterConnectionIdempotencyPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:31.126527+00:00
---

# Class CloudRedisClusterConnectionIdempotencyPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/redis/latest/classgoogle_1_1cloud_1_1redis__cluster__v1_1_1CloudRedisClusterConnectionIdempotencyPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class CloudRedisClusterConnectionIdempotencyPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

## Functions 

### virtual clone() const

Create a new copy of this object. 

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< CloudRedisClusterConnectionIdempotencyPolicy >` |   
  
### virtual ListClusters(google::cloud::redis::cluster::v1::ListClustersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::ListClustersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetCluster(google::cloud::redis::cluster::v1::GetClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::GetClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual UpdateCluster(google::cloud::redis::cluster::v1::UpdateClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::UpdateClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteCluster(google::cloud::redis::cluster::v1::DeleteClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::DeleteClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CreateCluster(google::cloud::redis::cluster::v1::CreateClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::CreateClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetClusterCertificateAuthority(google::cloud::redis::cluster::v1::GetClusterCertificateAuthorityRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::GetClusterCertificateAuthorityRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetSharedRegionalCertificateAuthority(google::cloud::redis::cluster::v1::GetSharedRegionalCertificateAuthorityRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::GetSharedRegionalCertificateAuthorityRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual RescheduleClusterMaintenance(google::cloud::redis::cluster::v1::RescheduleClusterMaintenanceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::RescheduleClusterMaintenanceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListBackupCollections(google::cloud::redis::cluster::v1::ListBackupCollectionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::ListBackupCollectionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetBackupCollection(google::cloud::redis::cluster::v1::GetBackupCollectionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::GetBackupCollectionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListBackups(google::cloud::redis::cluster::v1::ListBackupsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::ListBackupsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetBackup(google::cloud::redis::cluster::v1::GetBackupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::GetBackupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteBackup(google::cloud::redis::cluster::v1::DeleteBackupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::DeleteBackupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ExportBackup(google::cloud::redis::cluster::v1::ExportBackupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::ExportBackupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual BackupCluster(google::cloud::redis::cluster::v1::BackupClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::redis::cluster::v1::BackupClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`google::cloud::Idempotency` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
