---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceGrpc.AsyncService
title: Interface ModelServiceGrpc.AsyncService (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:48.305860+00:00
---

# Interface ModelServiceGrpc.AsyncService (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelServiceGrpc.AsyncService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ModelServiceGrpc.AsyncService (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface ModelServiceGrpc.AsyncService

A service for managing Vertex AI's machine learning Models.

## Methods 

### batchImportEvaluatedAnnotations(BatchImportEvaluatedAnnotationsRequest request, StreamObserver<BatchImportEvaluatedAnnotationsResponse> responseObserver)
    
    
    public default void batchImportEvaluatedAnnotations(BatchImportEvaluatedAnnotationsRequest request, StreamObserver<BatchImportEvaluatedAnnotationsResponse> responseObserver)

Imports a list of externally generated EvaluatedAnnotations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchImportEvaluatedAnnotationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchImportEvaluatedAnnotationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportEvaluatedAnnotationsResponse)>`  
  
  
### batchImportModelEvaluationSlices(BatchImportModelEvaluationSlicesRequest request, StreamObserver<BatchImportModelEvaluationSlicesResponse> responseObserver)
    
    
    public default void batchImportModelEvaluationSlices(BatchImportModelEvaluationSlicesRequest request, StreamObserver<BatchImportModelEvaluationSlicesResponse> responseObserver)

Imports a list of externally generated ModelEvaluationSlice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchImportModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[BatchImportModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.BatchImportModelEvaluationSlicesResponse)>`  
  
  
### copyModel(CopyModelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void copyModel(CopyModelRequest request, StreamObserver<Operation> responseObserver)

Copies an already existing Vertex AI Model into the specified Location. The source Model must exist in the same Project. When copying custom Models, the users themselves are responsible for Model.metadata content to be region-agnostic, as well as making sure that any resources (e.g. files) it depends on remain accessible.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CopyModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CopyModelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteModel(DeleteModelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteModel(DeleteModelRequest request, StreamObserver<Operation> responseObserver)

Deletes a Model. A model cannot be deleted if any Endpoint resource has a DeployedModel based on the model in its deployed_models field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteModelVersion(DeleteModelVersionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void deleteModelVersion(DeleteModelVersionRequest request, StreamObserver<Operation> responseObserver)

Deletes a Model version. Model version can only be deleted if there are no DeployedModels created from it. Deleting the only version in the Model is not allowed. Use DeleteModel for deleting the Model instead.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteModelVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteModelVersionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### exportModel(ExportModelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void exportModel(ExportModelRequest request, StreamObserver<Operation> responseObserver)

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one supported export format.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ExportModelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getModel(GetModelRequest request, StreamObserver<Model> responseObserver)
    
    
    public default void getModel(GetModelRequest request, StreamObserver<Model> responseObserver)

Gets a Model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)>`  
  
  
### getModelEvaluation(GetModelEvaluationRequest request, StreamObserver<ModelEvaluation> responseObserver)
    
    
    public default void getModelEvaluation(GetModelEvaluationRequest request, StreamObserver<ModelEvaluation> responseObserver)

Gets a ModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)>`  
  
  
### getModelEvaluationSlice(GetModelEvaluationSliceRequest request, StreamObserver<ModelEvaluationSlice> responseObserver)
    
    
    public default void getModelEvaluationSlice(GetModelEvaluationSliceRequest request, StreamObserver<ModelEvaluationSlice> responseObserver)

Gets a ModelEvaluationSlice.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationSliceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetModelEvaluationSliceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ModelEvaluationSlice](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluationSlice)>`  
  
  
### importModelEvaluation(ImportModelEvaluationRequest request, StreamObserver<ModelEvaluation> responseObserver)
    
    
    public default void importModelEvaluation(ImportModelEvaluationRequest request, StreamObserver<ModelEvaluation> responseObserver)

Imports an externally generated ModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ImportModelEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ModelEvaluation)>`  
  
  
### listModelEvaluationSlices(ListModelEvaluationSlicesRequest request, StreamObserver<ListModelEvaluationSlicesResponse> responseObserver)
    
    
    public default void listModelEvaluationSlices(ListModelEvaluationSlicesRequest request, StreamObserver<ListModelEvaluationSlicesResponse> responseObserver)

Lists ModelEvaluationSlices in a ModelEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationSlicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationSlicesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListModelEvaluationSlicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationSlicesResponse)>`  
  
  
### listModelEvaluations(ListModelEvaluationsRequest request, StreamObserver<ListModelEvaluationsResponse> responseObserver)
    
    
    public default void listModelEvaluations(ListModelEvaluationsRequest request, StreamObserver<ListModelEvaluationsResponse> responseObserver)

Lists ModelEvaluations in a Model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListModelEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelEvaluationsResponse)>`  
  
  
### listModelVersionCheckpoints(ListModelVersionCheckpointsRequest request, StreamObserver<ListModelVersionCheckpointsResponse> responseObserver)
    
    
    public default void listModelVersionCheckpoints(ListModelVersionCheckpointsRequest request, StreamObserver<ListModelVersionCheckpointsResponse> responseObserver)

Lists checkpoints of the specified model version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelVersionCheckpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionCheckpointsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListModelVersionCheckpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionCheckpointsResponse)>`  
  
  
### listModelVersions(ListModelVersionsRequest request, StreamObserver<ListModelVersionsResponse> responseObserver)
    
    
    public default void listModelVersions(ListModelVersionsRequest request, StreamObserver<ListModelVersionsResponse> responseObserver)

Lists versions of the specified model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListModelVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelVersionsResponse)>`  
  
  
### listModels(ListModelsRequest request, StreamObserver<ListModelsResponse> responseObserver)
    
    
    public default void listModels(ListModelsRequest request, StreamObserver<ListModelsResponse> responseObserver)

Lists Models in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListModelsResponse)>`  
  
  
### mergeVersionAliases(MergeVersionAliasesRequest request, StreamObserver<Model> responseObserver)
    
    
    public default void mergeVersionAliases(MergeVersionAliasesRequest request, StreamObserver<Model> responseObserver)

Merges a set of aliases for a Model version.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[MergeVersionAliasesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.MergeVersionAliasesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)>`  
  
  
### updateExplanationDataset(UpdateExplanationDatasetRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void updateExplanationDataset(UpdateExplanationDatasetRequest request, StreamObserver<Operation> responseObserver)

Incrementally update the dataset used for an examples model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateExplanationDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateExplanationDatasetRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateModel(UpdateModelRequest request, StreamObserver<Model> responseObserver)
    
    
    public default void updateModel(UpdateModelRequest request, StreamObserver<Model> responseObserver)

Updates a Model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateModelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Model)>`  
  
  
### uploadModel(UploadModelRequest request, StreamObserver<Operation> responseObserver)
    
    
    public default void uploadModel(UploadModelRequest request, StreamObserver<Operation> responseObserver)

Uploads a Model artifact into Vertex AI.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UploadModelRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
