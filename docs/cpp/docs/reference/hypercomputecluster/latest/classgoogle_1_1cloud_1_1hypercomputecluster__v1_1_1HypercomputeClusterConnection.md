---
url: https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1_1_1HypercomputeClusterConnection/
title: Class HypercomputeClusterConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:59.003073+00:00
---

# Class HypercomputeClusterConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1_1_1HypercomputeClusterConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class HypercomputeClusterConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0 

The [`HypercomputeClusterConnection`](https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1_1_1HypercomputeClusterConnection) object for [`HypercomputeClusterClient`](https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1_1_1HypercomputeClusterClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`HypercomputeClusterClient`](https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1_1_1HypercomputeClusterClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`HypercomputeClusterClient`](https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1_1_1HypercomputeClusterClient).

To create a concrete instance, see [`MakeHypercomputeClusterConnection()`](https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/namespacegoogle_1_1cloud_1_1hypercomputecluster__v1).

For mocking, see [`hypercomputecluster_v1_mocks::MockHypercomputeClusterConnection`](https://docs.cloud.google.com/cpp/docs/reference/hypercomputecluster/latest/classgoogle_1_1cloud_1_1hypercomputecluster__v1__mocks_1_1MockHypercomputeClusterConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListClusters(google::cloud::hypercomputecluster::v1::ListClustersRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::hypercomputecluster::v1::ListClustersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::hypercomputecluster::v1::Cluster >` |   
  
### virtual GetCluster(google::cloud::hypercomputecluster::v1::GetClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::hypercomputecluster::v1::GetClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::hypercomputecluster::v1::Cluster >` |   
  
### virtual CreateCluster(google::cloud::hypercomputecluster::v1::CreateClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::hypercomputecluster::v1::CreateClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::hypercomputecluster::v1::Cluster > >` |   
  
### virtual CreateCluster(NoAwaitTag, google::cloud::hypercomputecluster::v1::CreateClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::hypercomputecluster::v1::CreateClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::hypercomputecluster::v1::Cluster > >` |   
  
### virtual UpdateCluster(google::cloud::hypercomputecluster::v1::UpdateClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::hypercomputecluster::v1::UpdateClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::hypercomputecluster::v1::Cluster > >` |   
  
### virtual UpdateCluster(NoAwaitTag, google::cloud::hypercomputecluster::v1::UpdateClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::hypercomputecluster::v1::UpdateClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::hypercomputecluster::v1::Cluster > >` |   
  
### virtual DeleteCluster(google::cloud::hypercomputecluster::v1::DeleteClusterRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::hypercomputecluster::v1::DeleteClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::hypercomputecluster::v1::OperationMetadata > >` |   
  
### virtual DeleteCluster(NoAwaitTag, google::cloud::hypercomputecluster::v1::DeleteClusterRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::hypercomputecluster::v1::DeleteClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteCluster(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::hypercomputecluster::v1::OperationMetadata > >` |   
  
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
