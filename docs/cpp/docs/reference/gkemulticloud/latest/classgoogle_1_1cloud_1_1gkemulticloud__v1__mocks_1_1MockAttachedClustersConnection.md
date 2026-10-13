---
url: https://docs.cloud.google.com/cpp/docs/reference/gkemulticloud/latest/classgoogle_1_1cloud_1_1gkemulticloud__v1__mocks_1_1MockAttachedClustersConnection/
title: Class MockAttachedClustersConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:00.149152+00:00
---

# Class MockAttachedClustersConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/gkemulticloud/latest/classgoogle_1_1cloud_1_1gkemulticloud__v1__mocks_1_1MockAttachedClustersConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MockAttachedClustersConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

A class to mock `AttachedClustersConnection`. 

Application developers may want to test their code with simulated responses, including errors, from an object of type `AttachedClustersClient`. To do so, construct an object of type `AttachedClustersClient` with an instance of this class. Then use the Google Test framework functions to program the behavior of this mock.

###### See Also

[This example](https://cloud.google.com/cpp/docs/reference/bigquery/latest/bigquery-read-mock) for how to test your application with GoogleTest. While the example showcases types from the BigQuery library, the underlying principles apply for any pair of `*Client` and `*Connection`. 

## Functions 

### virtual options()

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateAttachedCluster(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkemulticloud::v1::AttachedCluster > >` |   
  
### virtual UpdateAttachedCluster(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkemulticloud::v1::AttachedCluster > >` |   
  
### virtual ImportAttachedCluster(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkemulticloud::v1::AttachedCluster > >` |   
  
### virtual GetAttachedCluster(google::cloud::gkemulticloud::v1::GetAttachedClusterRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkemulticloud::v1::GetAttachedClusterRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkemulticloud::v1::AttachedCluster >` |   
  
### virtual ListAttachedClusters(google::cloud::gkemulticloud::v1::ListAttachedClustersRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkemulticloud::v1::ListAttachedClustersRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkemulticloud::v1::AttachedCluster >` |   
  
### virtual DeleteAttachedCluster(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkemulticloud::v1::OperationMetadata > >` |   
  
### virtual GetAttachedServerConfig(google::cloud::gkemulticloud::v1::GetAttachedServerConfigRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkemulticloud::v1::GetAttachedServerConfigRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkemulticloud::v1::AttachedServerConfig >` |   
  
### virtual GenerateAttachedClusterInstallManifest(google::cloud::gkemulticloud::v1::GenerateAttachedClusterInstallManifestRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkemulticloud::v1::GenerateAttachedClusterInstallManifestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkemulticloud::v1::GenerateAttachedClusterInstallManifestResponse >` |   
  
### virtual GenerateAttachedClusterAgentToken(google::cloud::gkemulticloud::v1::GenerateAttachedClusterAgentTokenRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkemulticloud::v1::GenerateAttachedClusterAgentTokenRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkemulticloud::v1::GenerateAttachedClusterAgentTokenResponse >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

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
