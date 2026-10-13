---
url: https://docs.cloud.google.com/cpp/docs/reference/chronicle/latest/classgoogle_1_1cloud_1_1chronicle__v1__mocks_1_1MockDataAccessControlServiceConnection/
title: Class MockDataAccessControlServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:31.575183+00:00
---

# Class MockDataAccessControlServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/chronicle/latest/classgoogle_1_1cloud_1_1chronicle__v1__mocks_1_1MockDataAccessControlServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MockDataAccessControlServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0 

A class to mock `DataAccessControlServiceConnection`. 

Application developers may want to test their code with simulated responses, including errors, from an object of type `DataAccessControlServiceClient`. To do so, construct an object of type `DataAccessControlServiceClient` with an instance of this class. Then use the Google Test framework functions to program the behavior of this mock.

###### See Also

[This example](https://cloud.google.com/cpp/docs/reference/bigquery/latest/bigquery-read-mock) for how to test your application with GoogleTest. While the example showcases types from the BigQuery library, the underlying principles apply for any pair of `*Client` and `*Connection`. 

## Functions 

### virtual options()

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateDataAccessLabel(google::cloud::chronicle::v1::CreateDataAccessLabelRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::CreateDataAccessLabelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::chronicle::v1::DataAccessLabel >` |   
  
### virtual GetDataAccessLabel(google::cloud::chronicle::v1::GetDataAccessLabelRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::GetDataAccessLabelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::chronicle::v1::DataAccessLabel >` |   
  
### virtual ListDataAccessLabels(google::cloud::chronicle::v1::ListDataAccessLabelsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::ListDataAccessLabelsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::chronicle::v1::DataAccessLabel >` |   
  
### virtual UpdateDataAccessLabel(google::cloud::chronicle::v1::UpdateDataAccessLabelRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::UpdateDataAccessLabelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::chronicle::v1::DataAccessLabel >` |   
  
### virtual DeleteDataAccessLabel(google::cloud::chronicle::v1::DeleteDataAccessLabelRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::DeleteDataAccessLabelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CreateDataAccessScope(google::cloud::chronicle::v1::CreateDataAccessScopeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::CreateDataAccessScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::chronicle::v1::DataAccessScope >` |   
  
### virtual GetDataAccessScope(google::cloud::chronicle::v1::GetDataAccessScopeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::GetDataAccessScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::chronicle::v1::DataAccessScope >` |   
  
### virtual ListDataAccessScopes(google::cloud::chronicle::v1::ListDataAccessScopesRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::ListDataAccessScopesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::chronicle::v1::DataAccessScope >` |   
  
### virtual UpdateDataAccessScope(google::cloud::chronicle::v1::UpdateDataAccessScopeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::UpdateDataAccessScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::chronicle::v1::DataAccessScope >` |   
  
### virtual DeleteDataAccessScope(google::cloud::chronicle::v1::DeleteDataAccessScopeRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::chronicle::v1::DeleteDataAccessScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
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
