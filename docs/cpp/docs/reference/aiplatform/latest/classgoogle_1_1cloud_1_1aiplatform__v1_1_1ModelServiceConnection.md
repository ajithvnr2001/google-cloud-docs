---
url: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceConnection/
title: Class ModelServiceConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:38.259689+00:00
---

# Class ModelServiceConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ModelServiceConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0 

The [`ModelServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceConnection) object for [`ModelServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`ModelServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`ModelServiceClient`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1_1_1ModelServiceClient).

To create a concrete instance, see [`MakeModelServiceConnection()`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/namespacegoogle_1_1cloud_1_1aiplatform__v1).

For mocking, see [`aiplatform_v1_mocks::MockModelServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/aiplatform/latest/classgoogle_1_1cloud_1_1aiplatform__v1__mocks_1_1MockModelServiceConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual UploadModel(google::cloud::aiplatform::v1::UploadModelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::UploadModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::UploadModelResponse > >` |   
  
### virtual UploadModel(NoAwaitTag, google::cloud::aiplatform::v1::UploadModelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::UploadModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UploadModel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::UploadModelResponse > >` |   
  
### virtual GetModel(google::cloud::aiplatform::v1::GetModelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::GetModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::Model >` |   
  
### virtual ListModels(google::cloud::aiplatform::v1::ListModelsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListModelsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::Model >` |   
  
### virtual ListModelVersions(google::cloud::aiplatform::v1::ListModelVersionsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListModelVersionsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::Model >` |   
  
### virtual ListModelVersionCheckpoints(google::cloud::aiplatform::v1::ListModelVersionCheckpointsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListModelVersionCheckpointsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::ModelVersionCheckpoint >` |   
  
### virtual UpdateModel(google::cloud::aiplatform::v1::UpdateModelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::UpdateModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::Model >` |   
  
### virtual UpdateExplanationDataset(google::cloud::aiplatform::v1::UpdateExplanationDatasetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::UpdateExplanationDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::UpdateExplanationDatasetResponse > >` |   
  
### virtual UpdateExplanationDataset(NoAwaitTag, google::cloud::aiplatform::v1::UpdateExplanationDatasetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::UpdateExplanationDatasetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateExplanationDataset(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::UpdateExplanationDatasetResponse > >` |   
  
### virtual DeleteModel(google::cloud::aiplatform::v1::DeleteModelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::DeleteModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual DeleteModel(NoAwaitTag, google::cloud::aiplatform::v1::DeleteModelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::DeleteModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteModel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual DeleteModelVersion(google::cloud::aiplatform::v1::DeleteModelVersionRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::DeleteModelVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual DeleteModelVersion(NoAwaitTag, google::cloud::aiplatform::v1::DeleteModelVersionRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::DeleteModelVersionRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteModelVersion(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::DeleteOperationMetadata > >` |   
  
### virtual MergeVersionAliases(google::cloud::aiplatform::v1::MergeVersionAliasesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::MergeVersionAliasesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::Model >` |   
  
### virtual ExportModel(google::cloud::aiplatform::v1::ExportModelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ExportModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::ExportModelResponse > >` |   
  
### virtual ExportModel(NoAwaitTag, google::cloud::aiplatform::v1::ExportModelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::ExportModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual ExportModel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::ExportModelResponse > >` |   
  
### virtual CopyModel(google::cloud::aiplatform::v1::CopyModelRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::CopyModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::CopyModelResponse > >` |   
  
### virtual CopyModel(NoAwaitTag, google::cloud::aiplatform::v1::CopyModelRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::aiplatform::v1::CopyModelRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CopyModel(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::aiplatform::v1::CopyModelResponse > >` |   
  
### virtual ImportModelEvaluation(google::cloud::aiplatform::v1::ImportModelEvaluationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ImportModelEvaluationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::ModelEvaluation >` |   
  
### virtual BatchImportModelEvaluationSlices(google::cloud::aiplatform::v1::BatchImportModelEvaluationSlicesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::BatchImportModelEvaluationSlicesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::BatchImportModelEvaluationSlicesResponse >` |   
  
### virtual BatchImportEvaluatedAnnotations(google::cloud::aiplatform::v1::BatchImportEvaluatedAnnotationsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::BatchImportEvaluatedAnnotationsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::BatchImportEvaluatedAnnotationsResponse >` |   
  
### virtual GetModelEvaluation(google::cloud::aiplatform::v1::GetModelEvaluationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::GetModelEvaluationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::ModelEvaluation >` |   
  
### virtual ListModelEvaluations(google::cloud::aiplatform::v1::ListModelEvaluationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListModelEvaluationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::ModelEvaluation >` |   
  
### virtual GetModelEvaluationSlice(google::cloud::aiplatform::v1::GetModelEvaluationSliceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::GetModelEvaluationSliceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::aiplatform::v1::ModelEvaluationSlice >` |   
  
### virtual ListModelEvaluationSlices(google::cloud::aiplatform::v1::ListModelEvaluationSlicesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::aiplatform::v1::ListModelEvaluationSlicesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::aiplatform::v1::ModelEvaluationSlice >` |   
  
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
