---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.AutoMlGrpc.AutoMlBlockingV2Stub
title: Class AutoMlGrpc.AutoMlBlockingV2Stub (2.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:29.372216+00:00
---

# Class AutoMlGrpc.AutoMlBlockingV2Stub (2.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.AutoMlGrpc.AutoMlBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AutoMlGrpc.AutoMlBlockingV2Stub (2.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.95.0 (latest)  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.18  2.2.3  2.1.23 
    
    
    public static final class AutoMlGrpc.AutoMlBlockingV2Stub extends AbstractBlockingStub<AutoMlGrpc.AutoMlBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service AutoMl.

AutoML Server API. The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted. An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`. Currently the only supported `location_id` is "us-central1". On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > AutoMlGrpc.AutoMlBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected AutoMlGrpc.AutoMlBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AutoMlGrpc.AutoMlBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.AutoMlGrpc.AutoMlBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createDataset(CreateDatasetRequest request)
    
    
    public Dataset createDataset(CreateDatasetRequest request)

Creates a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.CreateDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.Dataset)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createModel(CreateModelRequest request)
    
    
    public Operation createModel(CreateModelRequest request)

Creates a model. Returns a Model in the response field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.CreateModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteDataset(DeleteDatasetRequest request)
    
    
    public Operation deleteDataset(DeleteDatasetRequest request)

Deletes a dataset and all of its contents. Returns empty response in the response field when it completes, and `delete_details` in the metadata field.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.DeleteDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteModel(DeleteModelRequest request)
    
    
    public Operation deleteModel(DeleteModelRequest request)

Deletes a model. Returns `google.protobuf.Empty` in the response field when it completes, and `delete_details` in the metadata field.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.DeleteModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deployModel(DeployModelRequest request)
    
    
    public Operation deployModel(DeployModelRequest request)

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing node_number) will reset the deployment state without pausing the model's availability. Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically. Returns an empty response in the response field when it completes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.DeployModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### exportData(ExportDataRequest request)
    
    
    public Operation exportData(ExportDataRequest request)

Exports dataset's data to the provided output location. Returns an empty response in the response field when it completes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ExportDataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### exportEvaluatedExamples(ExportEvaluatedExamplesRequest request)
    
    
    public Operation exportEvaluatedExamples(ExportEvaluatedExamplesRequest request)

Exports examples on which the model was evaluated (i.e. which were in the TEST set of the dataset the model was created from), together with their ground truth annotations and the annotations created (predicted) by the model. The examples, ground truth and predictions are exported in the state they were at the moment the model was evaluated. This export is available only for 30 days since the model evaluation is created. Currently only available for Tables. Returns an empty response in the response field when it completes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportEvaluatedExamplesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ExportEvaluatedExamplesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### exportModel(ExportModelRequest request)
    
    
    public Operation exportModel(ExportModelRequest request)

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in ModelExportOutputConfig. Returns an empty response in the response field when it completes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ExportModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getAnnotationSpec(GetAnnotationSpecRequest request)
    
    
    public AnnotationSpec getAnnotationSpec(GetAnnotationSpecRequest request)

Gets an annotation spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAnnotationSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.GetAnnotationSpecRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnnotationSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.AnnotationSpec)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getColumnSpec(GetColumnSpecRequest request)
    
    
    public ColumnSpec getColumnSpec(GetColumnSpecRequest request)

Gets a column spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetColumnSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.GetColumnSpecRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ColumnSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ColumnSpec)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getDataset(GetDatasetRequest request)
    
    
    public Dataset getDataset(GetDatasetRequest request)

Gets a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.GetDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.Dataset)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getModel(GetModelRequest request)
    
    
    public Model getModel(GetModelRequest request)

Gets a model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.GetModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.Model)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getModelEvaluation(GetModelEvaluationRequest request)
    
    
    public ModelEvaluation getModelEvaluation(GetModelEvaluationRequest request)

Gets a model evaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.GetModelEvaluationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModelEvaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ModelEvaluation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getTableSpec(GetTableSpecRequest request)
    
    
    public TableSpec getTableSpec(GetTableSpecRequest request)

Gets a table spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetTableSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.GetTableSpecRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.TableSpec)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importData(ImportDataRequest request)
    
    
    public Operation importData(ImportDataRequest request)

Imports data into a dataset. For Tables this method can only be called on an empty Dataset. For Tables:

  * A schema_inference_version parameter must be explicitly set. Returns an empty response in the response field when it completes.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ImportDataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listColumnSpecs(ListColumnSpecsRequest request)
    
    
    public ListColumnSpecsResponse listColumnSpecs(ListColumnSpecsRequest request)

Lists column specs in a table spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListColumnSpecsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListColumnSpecsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListColumnSpecsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListColumnSpecsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listDatasets(ListDatasetsRequest request)
    
    
    public ListDatasetsResponse listDatasets(ListDatasetsRequest request)

Lists datasets in a project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListDatasetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListDatasetsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listModelEvaluations(ListModelEvaluationsRequest request)
    
    
    public ListModelEvaluationsResponse listModelEvaluations(ListModelEvaluationsRequest request)

Lists model evaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListModelEvaluationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListModelEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListModelEvaluationsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listModels(ListModelsRequest request)
    
    
    public ListModelsResponse listModels(ListModelsRequest request)

Lists models.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListModelsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListModelsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listTableSpecs(ListTableSpecsRequest request)
    
    
    public ListTableSpecsResponse listTableSpecs(ListTableSpecsRequest request)

Lists table specs in a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListTableSpecsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListTableSpecsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListTableSpecsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ListTableSpecsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### undeployModel(UndeployModelRequest request)
    
    
    public Operation undeployModel(UndeployModelRequest request)

Undeploys a model. If the model is not deployed this method has no effect. Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically. Returns an empty response in the response field when it completes.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UndeployModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.UndeployModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateColumnSpec(UpdateColumnSpecRequest request)
    
    
    public ColumnSpec updateColumnSpec(UpdateColumnSpecRequest request)

Updates a column spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateColumnSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.UpdateColumnSpecRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ColumnSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.ColumnSpec)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateDataset(UpdateDatasetRequest request)
    
    
    public Dataset updateDataset(UpdateDatasetRequest request)

Updates a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.UpdateDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.Dataset)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateTableSpec(UpdateTableSpecRequest request)
    
    
    public TableSpec updateTableSpec(UpdateTableSpecRequest request)

Updates a table spec.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateTableSpecRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.UpdateTableSpecRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TableSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-automl/latest/com.google.cloud.automl.v1beta1.TableSpec)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-06 UTC."],[],[]] 
