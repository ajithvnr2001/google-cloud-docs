---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.AMLGrpc.AMLBlockingStub
title: Class AMLGrpc.AMLBlockingStub (0.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:36.345132+00:00
---

# Class AMLGrpc.AMLBlockingStub (0.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.AMLGrpc.AMLBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AMLGrpc.AMLBlockingStub (0.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.40.0 (latest)  0.36.0  0.35.0  0.34.0  0.32.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class AMLGrpc.AMLBlockingStub extends AbstractBlockingStub<AMLGrpc.AMLBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service AML.

The AML (Anti Money Laundering) service allows users to perform REST operations on aml.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > AMLGrpc.AMLBlockingStub

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
    
    
    protected AMLGrpc.AMLBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AMLGrpc.AMLBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.AMLGrpc.AMLBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createBacktestResult(CreateBacktestResultRequest request)
    
    
    public Operation createBacktestResult(CreateBacktestResultRequest request)

Create a BacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateBacktestResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.CreateBacktestResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createDataset(CreateDatasetRequest request)
    
    
    public Operation createDataset(CreateDatasetRequest request)

Creates a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.CreateDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createEngineConfig(CreateEngineConfigRequest request)
    
    
    public Operation createEngineConfig(CreateEngineConfigRequest request)

Creates an engine config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.CreateEngineConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createInstance(CreateInstanceRequest request)
    
    
    public Operation createInstance(CreateInstanceRequest request)

Creates an instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.CreateInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createModel(CreateModelRequest request)
    
    
    public Operation createModel(CreateModelRequest request)

Creates a model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.CreateModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### createPredictionResult(CreatePredictionResultRequest request)
    
    
    public Operation createPredictionResult(CreatePredictionResultRequest request)

Create a PredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreatePredictionResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.CreatePredictionResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteBacktestResult(DeleteBacktestResultRequest request)
    
    
    public Operation deleteBacktestResult(DeleteBacktestResultRequest request)

Deletes a BacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteBacktestResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.DeleteBacktestResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteDataset(DeleteDatasetRequest request)
    
    
    public Operation deleteDataset(DeleteDatasetRequest request)

Deletes a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.DeleteDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteEngineConfig(DeleteEngineConfigRequest request)
    
    
    public Operation deleteEngineConfig(DeleteEngineConfigRequest request)

Deletes an engine config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.DeleteEngineConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteInstance(DeleteInstanceRequest request)
    
    
    public Operation deleteInstance(DeleteInstanceRequest request)

Deletes an instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.DeleteInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteModel(DeleteModelRequest request)
    
    
    public Operation deleteModel(DeleteModelRequest request)

Deletes a model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.DeleteModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deletePredictionResult(DeletePredictionResultRequest request)
    
    
    public Operation deletePredictionResult(DeletePredictionResultRequest request)

Deletes a PredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeletePredictionResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.DeletePredictionResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### exportBacktestResultMetadata(ExportBacktestResultMetadataRequest request)
    
    
    public Operation exportBacktestResultMetadata(ExportBacktestResultMetadataRequest request)

Export governance information for a BacktestResult resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#backtest-results).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportBacktestResultMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ExportBacktestResultMetadataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### exportEngineConfigMetadata(ExportEngineConfigMetadataRequest request)
    
    
    public Operation exportEngineConfigMetadata(ExportEngineConfigMetadataRequest request)

Export governance information for an EngineConfig resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#engine-config).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportEngineConfigMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ExportEngineConfigMetadataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### exportModelMetadata(ExportModelMetadataRequest request)
    
    
    public Operation exportModelMetadata(ExportModelMetadataRequest request)

Export governance information for a Model resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#model).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportModelMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ExportModelMetadataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### exportPredictionResultMetadata(ExportPredictionResultMetadataRequest request)
    
    
    public Operation exportPredictionResultMetadata(ExportPredictionResultMetadataRequest request)

Export governance information for a PredictionResult resource. For information on the exported fields, see [AML output data model](https://cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#prediction-results).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportPredictionResultMetadataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ExportPredictionResultMetadataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### exportRegisteredParties(ExportRegisteredPartiesRequest request)
    
    
    public Operation exportRegisteredParties(ExportRegisteredPartiesRequest request)

Exports the list of registered parties. See [Create and manage instances](https://cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#export-registered-parties) for information on the output schema for this method.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportRegisteredPartiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ExportRegisteredPartiesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getBacktestResult(GetBacktestResultRequest request)
    
    
    public BacktestResult getBacktestResult(GetBacktestResultRequest request)

Gets a BacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBacktestResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetBacktestResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BacktestResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.BacktestResult)` |   
  
### getDataset(GetDatasetRequest request)
    
    
    public Dataset getDataset(GetDatasetRequest request)

Gets a dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Dataset](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.Dataset)` |   
  
### getEngineConfig(GetEngineConfigRequest request)
    
    
    public EngineConfig getEngineConfig(GetEngineConfigRequest request)

Gets an engine config.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetEngineConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EngineConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.EngineConfig)` |   
  
### getEngineVersion(GetEngineVersionRequest request)
    
    
    public EngineVersion getEngineVersion(GetEngineVersionRequest request)

Gets a single EngineVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetEngineVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetEngineVersionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EngineVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.EngineVersion)` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public Instance getInstance(GetInstanceRequest request)

Gets an instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.Instance)` |   
  
### getModel(GetModelRequest request)
    
    
    public Model getModel(GetModelRequest request)

Gets a model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Model](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.Model)` |   
  
### getPredictionResult(GetPredictionResultRequest request)
    
    
    public PredictionResult getPredictionResult(GetPredictionResultRequest request)

Gets a PredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetPredictionResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.GetPredictionResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[PredictionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.PredictionResult)` |   
  
### importRegisteredParties(ImportRegisteredPartiesRequest request)
    
    
    public Operation importRegisteredParties(ImportRegisteredPartiesRequest request)

Imports the list of registered parties. See [Create and manage instances](https://cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#import-registered-parties) for information on the input schema and response for this method.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportRegisteredPartiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ImportRegisteredPartiesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### listBacktestResults(ListBacktestResultsRequest request)
    
    
    public ListBacktestResultsResponse listBacktestResults(ListBacktestResultsRequest request)

List BacktestResults.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBacktestResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListBacktestResultsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBacktestResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListBacktestResultsResponse)` |   
  
### listDatasets(ListDatasetsRequest request)
    
    
    public ListDatasetsResponse listDatasets(ListDatasetsRequest request)

Lists datasets.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDatasetsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListDatasetsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListDatasetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListDatasetsResponse)` |   
  
### listEngineConfigs(ListEngineConfigsRequest request)
    
    
    public ListEngineConfigsResponse listEngineConfigs(ListEngineConfigsRequest request)

Lists engine configs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEngineConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListEngineConfigsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListEngineConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListEngineConfigsResponse)` |   
  
### listEngineVersions(ListEngineVersionsRequest request)
    
    
    public ListEngineVersionsResponse listEngineVersions(ListEngineVersionsRequest request)

Lists EngineVersions for given location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListEngineVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListEngineVersionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListEngineVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListEngineVersionsResponse)` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public ListInstancesResponse listInstances(ListInstancesRequest request)

Lists instances.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListInstancesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListInstancesResponse)` |   
  
### listModels(ListModelsRequest request)
    
    
    public ListModelsResponse listModels(ListModelsRequest request)

Lists models.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListModelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListModelsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListModelsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListModelsResponse)` |   
  
### listPredictionResults(ListPredictionResultsRequest request)
    
    
    public ListPredictionResultsResponse listPredictionResults(ListPredictionResultsRequest request)

List PredictionResults.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListPredictionResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListPredictionResultsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListPredictionResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.ListPredictionResultsResponse)` |   
  
### updateBacktestResult(UpdateBacktestResultRequest request)
    
    
    public Operation updateBacktestResult(UpdateBacktestResultRequest request)

Updates the parameters of a single BacktestResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateBacktestResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.UpdateBacktestResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateDataset(UpdateDatasetRequest request)
    
    
    public Operation updateDataset(UpdateDatasetRequest request)

Updates the parameters of a single Dataset.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDatasetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.UpdateDatasetRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateEngineConfig(UpdateEngineConfigRequest request)
    
    
    public Operation updateEngineConfig(UpdateEngineConfigRequest request)

Updates the parameters of a single EngineConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateEngineConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.UpdateEngineConfigRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateInstance(UpdateInstanceRequest request)
    
    
    public Operation updateInstance(UpdateInstanceRequest request)

Updates the parameters of a single Instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.UpdateInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updateModel(UpdateModelRequest request)
    
    
    public Operation updateModel(UpdateModelRequest request)

Updates the parameters of a single Model.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateModelRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.UpdateModelRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### updatePredictionResult(UpdatePredictionResultRequest request)
    
    
    public Operation updatePredictionResult(UpdatePredictionResultRequest request)

Updates the parameters of a single PredictionResult.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdatePredictionResultRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-financialservices/latest/com.google.cloud.financialservices.v1.UpdatePredictionResultRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
