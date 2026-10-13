---
url: https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1_1_1AppConnectorsServiceConnection/
title: Class AppConnectorsServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:31:07.392027+00:00
---

# Class AppConnectorsServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1_1_1AppConnectorsServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AppConnectorsServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`AppConnectorsServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1_1_1AppConnectorsServiceConnection) object for [`AppConnectorsServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1_1_1AppConnectorsServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`AppConnectorsServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1_1_1AppConnectorsServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`AppConnectorsServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1_1_1AppConnectorsServiceClient).

To create a concrete instance, see [`MakeAppConnectorsServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/namespacegoogle_1_1cloud_1_1beyondcorp__appconnectors__v1).

For mocking, see [`beyondcorp_appconnectors_v1_mocks::MockAppConnectorsServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/beyondcorp/latest/classgoogle_1_1cloud_1_1beyondcorp__appconnectors__v1__mocks_1_1MockAppConnectorsServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListAppConnectors(google::cloud::beyondcorp::appconnectors::v1::ListAppConnectorsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::ListAppConnectorsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::beyondcorp::appconnectors::v1::AppConnector >` |   
  
### virtual GetAppConnector(google::cloud::beyondcorp::appconnectors::v1::GetAppConnectorRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::GetAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector >` |   
  
### virtual CreateAppConnector(google::cloud::beyondcorp::appconnectors::v1::CreateAppConnectorRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::CreateAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector > >` |   
  
### virtual CreateAppConnector(NoAwaitTag, google::cloud::beyondcorp::appconnectors::v1::CreateAppConnectorRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::CreateAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateAppConnector(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector > >` |   
  
### virtual UpdateAppConnector(google::cloud::beyondcorp::appconnectors::v1::UpdateAppConnectorRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::UpdateAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector > >` |   
  
### virtual UpdateAppConnector(NoAwaitTag, google::cloud::beyondcorp::appconnectors::v1::UpdateAppConnectorRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::UpdateAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateAppConnector(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector > >` |   
  
### virtual DeleteAppConnector(google::cloud::beyondcorp::appconnectors::v1::DeleteAppConnectorRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::DeleteAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnectorOperationMetadata > >` |   
  
### virtual DeleteAppConnector(NoAwaitTag, google::cloud::beyondcorp::appconnectors::v1::DeleteAppConnectorRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::DeleteAppConnectorRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteAppConnector(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnectorOperationMetadata > >` |   
  
### virtual ReportStatus(google::cloud::beyondcorp::appconnectors::v1::ReportStatusRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::ReportStatusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector > >` |   
  
### virtual ReportStatus(NoAwaitTag, google::cloud::beyondcorp::appconnectors::v1::ReportStatusRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::beyondcorp::appconnectors::v1::ReportStatusRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ReportStatus(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::beyondcorp::appconnectors::v1::AppConnector > >` |   
  
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
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` |   
  
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
