---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.AutoMl.AutoMlBase
title: Google AutoML v1 API - Class AutoMl.AutoMlBase (3.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:24.654995+00:00
---

# Google AutoML v1 API - Class AutoMl.AutoMlBase (3.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.AutoMl.AutoMlBase

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google AutoML v1 API - Class AutoMl.AutoMlBase (3.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.6.0 (latest)  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    [BindServiceMethod(typeof(AutoMl), "BindService")]
    public abstract class AutoMl.AutoMlBase

Reference documentation and code samples for the Google AutoML v1 API class AutoMl.AutoMlBase.

Base class for server-side implementations of AutoMl

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AutoMl.AutoMlBase

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AutoML.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1)

## Assembly

Google.Cloud.AutoML.V1.dll

## Methods 

### CreateDataset(CreateDatasetRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateDataset(CreateDatasetRequest request, ServerCallContext context)

Creates a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.CreateDatasetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### CreateModel(CreateModelRequest, ServerCallContext)
    
    
    public virtual Task<Operation> CreateModel(CreateModelRequest request, ServerCallContext context)

Creates a model. Returns a Model in the [response][google.longrunning.Operation.response] field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.CreateModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteDataset(DeleteDatasetRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteDataset(DeleteDatasetRequest request, ServerCallContext context)

Deletes a dataset and all of its contents. Returns empty response in the [response][google.longrunning.Operation.response] field when it completes, and `delete_details` in the [metadata][google.longrunning.Operation.metadata] field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.DeleteDatasetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeleteModel(DeleteModelRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeleteModel(DeleteModelRequest request, ServerCallContext context)

Deletes a model. Returns `google.protobuf.Empty` in the [response][google.longrunning.Operation.response] field when it completes, and `delete_details` in the [metadata][google.longrunning.Operation.metadata] field.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.DeleteModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### DeployModel(DeployModelRequest, ServerCallContext)
    
    
    public virtual Task<Operation> DeployModel(DeployModelRequest request, ServerCallContext context)

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing [node_number][google.cloud.automl.v1p1beta.ImageObjectDetectionModelDeploymentMetadata.node_number]) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the [response][google.longrunning.Operation.response] field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeployModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.DeployModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportData(ExportDataRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportData(ExportDataRequest request, ServerCallContext context)

Exports dataset's data to the provided output location. Returns an empty response in the [response][google.longrunning.Operation.response] field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ExportDataRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ExportModel(ExportModelRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ExportModel(ExportModelRequest request, ServerCallContext context)

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in [ModelExportOutputConfig][google.cloud.automl.v1.ModelExportOutputConfig].

Returns an empty response in the [response][google.longrunning.Operation.response] field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ExportModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ExportModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### GetAnnotationSpec(GetAnnotationSpecRequest, ServerCallContext)
    
    
    public virtual Task<AnnotationSpec> GetAnnotationSpec(GetAnnotationSpecRequest request, ServerCallContext context)

Gets an annotation spec.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationSpecRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.GetAnnotationSpecRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnnotationSpec](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.AnnotationSpec)` | The response to send back to the client (wrapped by a task).  
  
### GetDataset(GetDatasetRequest, ServerCallContext)
    
    
    public virtual Task<Dataset> GetDataset(GetDatasetRequest request, ServerCallContext context)

Gets a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.GetDatasetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Dataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Dataset)` | The response to send back to the client (wrapped by a task).  
  
### GetModel(GetModelRequest, ServerCallContext)
    
    
    public virtual Task<Model> GetModel(GetModelRequest request, ServerCallContext context)

Gets a model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.GetModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Model](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Model)` | The response to send back to the client (wrapped by a task).  
  
### GetModelEvaluation(GetModelEvaluationRequest, ServerCallContext)
    
    
    public virtual Task<ModelEvaluation> GetModelEvaluation(GetModelEvaluationRequest request, ServerCallContext context)

Gets a model evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.GetModelEvaluationRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ModelEvaluation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ModelEvaluation)` | The response to send back to the client (wrapped by a task).  
  
### ImportData(ImportDataRequest, ServerCallContext)
    
    
    public virtual Task<Operation> ImportData(ImportDataRequest request, ServerCallContext context)

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A [schema_inference_version][google.cloud.automl.v1.InputConfig.params] parameter must be explicitly set. Returns an empty response in the [response][google.longrunning.Operation.response] field when it completes.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ImportDataRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### ListDatasets(ListDatasetsRequest, ServerCallContext)
    
    
    public virtual Task<ListDatasetsResponse> ListDatasets(ListDatasetsRequest request, ServerCallContext context)

Lists datasets in a project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ListDatasetsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListDatasetsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ListDatasetsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListModelEvaluations(ListModelEvaluationsRequest, ServerCallContext)
    
    
    public virtual Task<ListModelEvaluationsResponse> ListModelEvaluations(ListModelEvaluationsRequest request, ServerCallContext context)

Lists model evaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ListModelEvaluationsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListModelEvaluationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ListModelEvaluationsResponse)` | The response to send back to the client (wrapped by a task).  
  
### ListModels(ListModelsRequest, ServerCallContext)
    
    
    public virtual Task<ListModelsResponse> ListModels(ListModelsRequest request, ServerCallContext context)

Lists models.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ListModelsRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ListModelsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.ListModelsResponse)` | The response to send back to the client (wrapped by a task).  
  
### UndeployModel(UndeployModelRequest, ServerCallContext)
    
    
    public virtual Task<Operation> UndeployModel(UndeployModelRequest request, ServerCallContext context)

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the [response][google.longrunning.Operation.response] field when it completes.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UndeployModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.UndeployModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation.html)` | The response to send back to the client (wrapped by a task).  
  
### UpdateDataset(UpdateDatasetRequest, ServerCallContext)
    
    
    public virtual Task<Dataset> UpdateDataset(UpdateDatasetRequest request, ServerCallContext context)

Updates a dataset.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.UpdateDatasetRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Dataset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Dataset)` | The response to send back to the client (wrapped by a task).  
  
### UpdateModel(UpdateModelRequest, ServerCallContext)
    
    
    public virtual Task<Model> UpdateModel(UpdateModelRequest request, ServerCallContext context)

Updates a model.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.UpdateModelRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Model](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AutoML.V1/latest/Google.Cloud.AutoML.V1.Model)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
