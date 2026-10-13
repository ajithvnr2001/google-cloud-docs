---
url: https://docs.cloud.google.com/cpp/docs/reference/osconfig/latest/classgoogle_1_1cloud_1_1osconfig__v1__mocks_1_1MockOsConfigZonalServiceConnection/
title: Class MockOsConfigZonalServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:19.119111+00:00
---

# Class MockOsConfigZonalServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/osconfig/latest/classgoogle_1_1cloud_1_1osconfig__v1__mocks_1_1MockOsConfigZonalServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class MockOsConfigZonalServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

A class to mock `OsConfigZonalServiceConnection`. 

Application developers may want to test their code with simulated responses, including errors, from an object of type `OsConfigZonalServiceClient`. To do so, construct an object of type `OsConfigZonalServiceClient` with an instance of this class. Then use the Google Test framework functions to program the behavior of this mock.

###### See Also

[This example](https://cloud.google.com/cpp/docs/reference/bigquery/latest/bigquery-read-mock) for how to test your application with GoogleTest. While the example showcases types from the BigQuery library, the underlying principles apply for any pair of `*Client` and `*Connection`. 

## Functions 

### virtual options()

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateOSPolicyAssignment(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::osconfig::v1::OSPolicyAssignment > >` |   
  
### virtual UpdateOSPolicyAssignment(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::osconfig::v1::OSPolicyAssignment > >` |   
  
### virtual GetOSPolicyAssignment(google::cloud::osconfig::v1::GetOSPolicyAssignmentRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::GetOSPolicyAssignmentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::osconfig::v1::OSPolicyAssignment >` |   
  
### virtual ListOSPolicyAssignments(google::cloud::osconfig::v1::ListOSPolicyAssignmentsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::ListOSPolicyAssignmentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::osconfig::v1::OSPolicyAssignment >` |   
  
### virtual ListOSPolicyAssignmentRevisions(google::cloud::osconfig::v1::ListOSPolicyAssignmentRevisionsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::ListOSPolicyAssignmentRevisionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::osconfig::v1::OSPolicyAssignment >` |   
  
### virtual DeleteOSPolicyAssignment(google::longrunning::Operation const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::osconfig::v1::OSPolicyAssignmentOperationMetadata > >` |   
  
### virtual GetOSPolicyAssignmentReport(google::cloud::osconfig::v1::GetOSPolicyAssignmentReportRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::GetOSPolicyAssignmentReportRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::osconfig::v1::OSPolicyAssignmentReport >` |   
  
### virtual ListOSPolicyAssignmentReports(google::cloud::osconfig::v1::ListOSPolicyAssignmentReportsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::ListOSPolicyAssignmentReportsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::osconfig::v1::OSPolicyAssignmentReport >` |   
  
### virtual GetInventory(google::cloud::osconfig::v1::GetInventoryRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::GetInventoryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::osconfig::v1::Inventory >` |   
  
### virtual ListInventories(google::cloud::osconfig::v1::ListInventoriesRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::ListInventoriesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::osconfig::v1::Inventory >` |   
  
### virtual GetVulnerabilityReport(google::cloud::osconfig::v1::GetVulnerabilityReportRequest const &)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::GetVulnerabilityReportRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::osconfig::v1::VulnerabilityReport >` |   
  
### virtual ListVulnerabilityReports(google::cloud::osconfig::v1::ListVulnerabilityReportsRequest)

This function is implemented using [gMock](https://google.github.io/googletest)'s `MOCK_METHOD()`. Consult the gMock documentation to use this mock in your tests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::osconfig::v1::ListVulnerabilityReportsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::osconfig::v1::VulnerabilityReport >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
