---
url: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceConnection/
title: Class DatasetServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:06:07.434700+00:00
---

# Class DatasetServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class DatasetServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0 

The [`DatasetServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceConnection) object for [`DatasetServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`DatasetServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`DatasetServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1DatasetServiceClient).

To create a concrete instance, see [`MakeDatasetServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/namespacegoogle_1_1cloud_1_1aiplatform__v1).

For mocking, see [`aiplatform_v1_mocks::MockDatasetServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1__mocks_1_1MockDatasetServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual CreateDataset(google::cloud::aiplatform::v1::CreateDatasetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::CreateDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::Dataset > >` |   
  
### virtual CreateDataset(NoAwaitTag, google::cloud::aiplatform::v1::CreateDatasetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::CreateDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateDataset(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::Dataset > >` |   
  
### virtual GetDataset(google::cloud::aiplatform::v1::GetDatasetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::GetDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::Dataset >` |   
  
### virtual UpdateDataset(google::cloud::aiplatform::v1::UpdateDatasetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::UpdateDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::Dataset >` |   
  
### virtual ListDatasets(google::cloud::aiplatform::v1::ListDatasetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListDatasetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::Dataset >` |   
  
### virtual DeleteDataset(google::cloud::aiplatform::v1::DeleteDatasetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::DeleteDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual DeleteDataset(NoAwaitTag, google::cloud::aiplatform::v1::DeleteDatasetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::DeleteDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteDataset(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual ImportData(google::cloud::aiplatform::v1::ImportDataRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ImportDataRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::ImportDataResponse > >` |   
  
### virtual ImportData(NoAwaitTag, google::cloud::aiplatform::v1::ImportDataRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::ImportDataRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ImportData(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::ImportDataResponse > >` |   
  
### virtual ExportData(google::cloud::aiplatform::v1::ExportDataRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ExportDataRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::ExportDataResponse > >` |   
  
### virtual ExportData(NoAwaitTag, google::cloud::aiplatform::v1::ExportDataRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::ExportDataRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ExportData(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::ExportDataResponse > >` |   
  
### virtual CreateDatasetVersion(google::cloud::aiplatform::v1::CreateDatasetVersionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::CreateDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DatasetVersion > >` |   
  
### virtual CreateDatasetVersion(NoAwaitTag, google::cloud::aiplatform::v1::CreateDatasetVersionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::CreateDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateDatasetVersion(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DatasetVersion > >` |   
  
### virtual UpdateDatasetVersion(google::cloud::aiplatform::v1::UpdateDatasetVersionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::UpdateDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::DatasetVersion >` |   
  
### virtual DeleteDatasetVersion(google::cloud::aiplatform::v1::DeleteDatasetVersionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::DeleteDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual DeleteDatasetVersion(NoAwaitTag, google::cloud::aiplatform::v1::DeleteDatasetVersionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::DeleteDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteDatasetVersion(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual GetDatasetVersion(google::cloud::aiplatform::v1::GetDatasetVersionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::GetDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::DatasetVersion >` |   
  
### virtual ListDatasetVersions(google::cloud::aiplatform::v1::ListDatasetVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListDatasetVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::DatasetVersion >` |   
  
### virtual RestoreDatasetVersion(google::cloud::aiplatform::v1::RestoreDatasetVersionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::RestoreDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DatasetVersion > >` |   
  
### virtual RestoreDatasetVersion(NoAwaitTag, google::cloud::aiplatform::v1::RestoreDatasetVersionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::RestoreDatasetVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual RestoreDatasetVersion(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DatasetVersion > >` |   
  
### virtual ListDataItems(google::cloud::aiplatform::v1::ListDataItemsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListDataItemsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::DataItem >` |   
  
### virtual SearchDataItems(google::cloud::aiplatform::v1::SearchDataItemsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::SearchDataItemsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::DataItemView >` |   
  
### virtual ListSavedQueries(google::cloud::aiplatform::v1::ListSavedQueriesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListSavedQueriesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::SavedQuery >` |   
  
### virtual DeleteSavedQuery(google::cloud::aiplatform::v1::DeleteSavedQueryRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::DeleteSavedQueryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual DeleteSavedQuery(NoAwaitTag, google::cloud::aiplatform::v1::DeleteSavedQueryRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::DeleteSavedQueryRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteSavedQuery(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual GetAnnotationSpec(google::cloud::aiplatform::v1::GetAnnotationSpecRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::GetAnnotationSpecRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::AnnotationSpec >` |   
  
### virtual ListAnnotations(google::cloud::aiplatform::v1::ListAnnotationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListAnnotationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::Annotation >` |   
  
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
  
### virtual WaitOperation(google::longrunning::WaitOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::WaitOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
