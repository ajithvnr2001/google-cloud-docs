---
url: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.documentprocessorservice-class
title: Class protos.google.cloud.documentai.v1.DocumentProcessorService (10.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:11.178911+00:00
---

# Class protos.google.cloud.documentai.v1.DocumentProcessorService (10.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.documentprocessorservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.documentai.v1.DocumentProcessorService (10.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

10.1.1 (latest)  9.6.0  9.2.0  8.12.0  8.10.0  8.8.0  8.6.0  8.5.0  8.4.0  8.2.0  8.1.2  8.0.0  7.3.1  7.1.0  7.0.1  6.3.0  6.1.0  6.0.0  3.3.0  3.2.1  3.1.0  3.0.2  2.10.0 

Represents a DocumentProcessorService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.documentai.v1.DocumentProcessorService

## Package

[@google-cloud/documentai](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DocumentProcessorService service.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
  
## Methods 

### batchProcessDocuments(request, callback)
    
    
    public batchProcessDocuments(request: google.cloud.documentai.v1.IBatchProcessRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.BatchProcessDocumentsCallback): void;

Calls BatchProcessDocuments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchProcessRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ibatchprocessrequest)`   
BatchProcessRequest message or plain object  
`callback` |  `[BatchProcessDocumentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchProcessDocuments(request)
    
    
    public batchProcessDocuments(request: google.cloud.documentai.v1.IBatchProcessRequest): Promise<google.longrunning.Operation>;

Calls BatchProcessDocuments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchProcessRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ibatchprocessrequest)`   
BatchProcessRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DocumentProcessorService;

Creates new DocumentProcessorService service using the specified rpc implementation.

**Parameters**  
---  
**Name** | **Description**  
`rpcImpl` |  `$protobuf.RPCImpl`   
RPC implementation  
`requestDelimited` |  `boolean`   
Whether requests are length-delimited  
`responseDelimited` |  `boolean`   
Whether responses are length-delimited  
**Returns**  
---  
**Type** | **Description**  
`[DocumentProcessorService](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.documentprocessorservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createProcessor(request, callback)
    
    
    public createProcessor(request: google.cloud.documentai.v1.ICreateProcessorRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.CreateProcessorCallback): void;

Calls CreateProcessor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.icreateprocessorrequest)`   
CreateProcessorRequest message or plain object  
`callback` |  `[CreateProcessorCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Processor  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createProcessor(request)
    
    
    public createProcessor(request: google.cloud.documentai.v1.ICreateProcessorRequest): Promise<google.cloud.documentai.v1.Processor>;

Calls CreateProcessor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.icreateprocessorrequest)`   
CreateProcessorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.Processor](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.processor-class)>` | Promise  
  
### deleteProcessor(request, callback)
    
    
    public deleteProcessor(request: google.cloud.documentai.v1.IDeleteProcessorRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorCallback): void;

Calls DeleteProcessor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ideleteprocessorrequest)`   
DeleteProcessorRequest message or plain object  
`callback` |  `[DeleteProcessorCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProcessor(request)
    
    
    public deleteProcessor(request: google.cloud.documentai.v1.IDeleteProcessorRequest): Promise<google.longrunning.Operation>;

Calls DeleteProcessor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ideleteprocessorrequest)`   
DeleteProcessorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### deleteProcessorVersion(request, callback)
    
    
    public deleteProcessorVersion(request: google.cloud.documentai.v1.IDeleteProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.DeleteProcessorVersionCallback): void;

Calls DeleteProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ideleteprocessorversionrequest)`   
DeleteProcessorVersionRequest message or plain object  
`callback` |  `[DeleteProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteProcessorVersion(request)
    
    
    public deleteProcessorVersion(request: google.cloud.documentai.v1.IDeleteProcessorVersionRequest): Promise<google.longrunning.Operation>;

Calls DeleteProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ideleteprocessorversionrequest)`   
DeleteProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### deployProcessorVersion(request, callback)
    
    
    public deployProcessorVersion(request: google.cloud.documentai.v1.IDeployProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.DeployProcessorVersionCallback): void;

Calls DeployProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeployProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ideployprocessorversionrequest)`   
DeployProcessorVersionRequest message or plain object  
`callback` |  `[DeployProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deployProcessorVersion(request)
    
    
    public deployProcessorVersion(request: google.cloud.documentai.v1.IDeployProcessorVersionRequest): Promise<google.longrunning.Operation>;

Calls DeployProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeployProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ideployprocessorversionrequest)`   
DeployProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### disableProcessor(request, callback)
    
    
    public disableProcessor(request: google.cloud.documentai.v1.IDisableProcessorRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.DisableProcessorCallback): void;

Calls DisableProcessor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDisableProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.idisableprocessorrequest)`   
DisableProcessorRequest message or plain object  
`callback` |  `[DisableProcessorCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### disableProcessor(request)
    
    
    public disableProcessor(request: google.cloud.documentai.v1.IDisableProcessorRequest): Promise<google.longrunning.Operation>;

Calls DisableProcessor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDisableProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.idisableprocessorrequest)`   
DisableProcessorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### enableProcessor(request, callback)
    
    
    public enableProcessor(request: google.cloud.documentai.v1.IEnableProcessorRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.EnableProcessorCallback): void;

Calls EnableProcessor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnableProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ienableprocessorrequest)`   
EnableProcessorRequest message or plain object  
`callback` |  `[EnableProcessorCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enableProcessor(request)
    
    
    public enableProcessor(request: google.cloud.documentai.v1.IEnableProcessorRequest): Promise<google.longrunning.Operation>;

Calls EnableProcessor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnableProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ienableprocessorrequest)`   
EnableProcessorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### evaluateProcessorVersion(request, callback)
    
    
    public evaluateProcessorVersion(request: google.cloud.documentai.v1.IEvaluateProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.EvaluateProcessorVersionCallback): void;

Calls EvaluateProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEvaluateProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ievaluateprocessorversionrequest)`   
EvaluateProcessorVersionRequest message or plain object  
`callback` |  `[EvaluateProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### evaluateProcessorVersion(request)
    
    
    public evaluateProcessorVersion(request: google.cloud.documentai.v1.IEvaluateProcessorVersionRequest): Promise<google.longrunning.Operation>;

Calls EvaluateProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEvaluateProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ievaluateprocessorversionrequest)`   
EvaluateProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### fetchProcessorTypes(request, callback)
    
    
    public fetchProcessorTypes(request: google.cloud.documentai.v1.IFetchProcessorTypesRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.FetchProcessorTypesCallback): void;

Calls FetchProcessorTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchProcessorTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ifetchprocessortypesrequest)`   
FetchProcessorTypesRequest message or plain object  
`callback` |  `[FetchProcessorTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchProcessorTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchProcessorTypes(request)
    
    
    public fetchProcessorTypes(request: google.cloud.documentai.v1.IFetchProcessorTypesRequest): Promise<google.cloud.documentai.v1.FetchProcessorTypesResponse>;

Calls FetchProcessorTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchProcessorTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ifetchprocessortypesrequest)`   
FetchProcessorTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.FetchProcessorTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.fetchprocessortypesresponse)>` | Promise  
  
### getEvaluation(request, callback)
    
    
    public getEvaluation(request: google.cloud.documentai.v1.IGetEvaluationRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.GetEvaluationCallback): void;

Calls GetEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetevaluationrequest)`   
GetEvaluationRequest message or plain object  
`callback` |  `[GetEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Evaluation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request)
    
    
    public getEvaluation(request: google.cloud.documentai.v1.IGetEvaluationRequest): Promise<google.cloud.documentai.v1.Evaluation>;

Calls GetEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetevaluationrequest)`   
GetEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.evaluation-class)>` | Promise  
  
### getProcessor(request, callback)
    
    
    public getProcessor(request: google.cloud.documentai.v1.IGetProcessorRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.GetProcessorCallback): void;

Calls GetProcessor.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetprocessorrequest)`   
GetProcessorRequest message or plain object  
`callback` |  `[GetProcessorCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Processor  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProcessor(request)
    
    
    public getProcessor(request: google.cloud.documentai.v1.IGetProcessorRequest): Promise<google.cloud.documentai.v1.Processor>;

Calls GetProcessor.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProcessorRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetprocessorrequest)`   
GetProcessorRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.Processor](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.processor-class)>` | Promise  
  
### getProcessorType(request, callback)
    
    
    public getProcessorType(request: google.cloud.documentai.v1.IGetProcessorTypeRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.GetProcessorTypeCallback): void;

Calls GetProcessorType.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProcessorTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetprocessortyperequest)`   
GetProcessorTypeRequest message or plain object  
`callback` |  `[GetProcessorTypeCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ProcessorType  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProcessorType(request)
    
    
    public getProcessorType(request: google.cloud.documentai.v1.IGetProcessorTypeRequest): Promise<google.cloud.documentai.v1.ProcessorType>;

Calls GetProcessorType.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProcessorTypeRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetprocessortyperequest)`   
GetProcessorTypeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ProcessorType](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.processortype-class)>` | Promise  
  
### getProcessorVersion(request, callback)
    
    
    public getProcessorVersion(request: google.cloud.documentai.v1.IGetProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.GetProcessorVersionCallback): void;

Calls GetProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetprocessorversionrequest)`   
GetProcessorVersionRequest message or plain object  
`callback` |  `[GetProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ProcessorVersion  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getProcessorVersion(request)
    
    
    public getProcessorVersion(request: google.cloud.documentai.v1.IGetProcessorVersionRequest): Promise<google.cloud.documentai.v1.ProcessorVersion>;

Calls GetProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.igetprocessorversionrequest)`   
GetProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ProcessorVersion](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.processorversion-class)>` | Promise  
  
### listEvaluations(request, callback)
    
    
    public listEvaluations(request: google.cloud.documentai.v1.IListEvaluationsRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.ListEvaluationsCallback): void;

Calls ListEvaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistevaluationsrequest)`   
ListEvaluationsRequest message or plain object  
`callback` |  `[ListEvaluationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEvaluationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluations(request)
    
    
    public listEvaluations(request: google.cloud.documentai.v1.IListEvaluationsRequest): Promise<google.cloud.documentai.v1.ListEvaluationsResponse>;

Calls ListEvaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistevaluationsrequest)`   
ListEvaluationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.listevaluationsresponse)>` | Promise  
  
### listProcessors(request, callback)
    
    
    public listProcessors(request: google.cloud.documentai.v1.IListProcessorsRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.ListProcessorsCallback): void;

Calls ListProcessors.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProcessorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistprocessorsrequest)`   
ListProcessorsRequest message or plain object  
`callback` |  `[ListProcessorsCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProcessorsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProcessors(request)
    
    
    public listProcessors(request: google.cloud.documentai.v1.IListProcessorsRequest): Promise<google.cloud.documentai.v1.ListProcessorsResponse>;

Calls ListProcessors.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProcessorsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistprocessorsrequest)`   
ListProcessorsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ListProcessorsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.listprocessorsresponse)>` | Promise  
  
### listProcessorTypes(request, callback)
    
    
    public listProcessorTypes(request: google.cloud.documentai.v1.IListProcessorTypesRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.ListProcessorTypesCallback): void;

Calls ListProcessorTypes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProcessorTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistprocessortypesrequest)`   
ListProcessorTypesRequest message or plain object  
`callback` |  `[ListProcessorTypesCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProcessorTypesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProcessorTypes(request)
    
    
    public listProcessorTypes(request: google.cloud.documentai.v1.IListProcessorTypesRequest): Promise<google.cloud.documentai.v1.ListProcessorTypesResponse>;

Calls ListProcessorTypes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProcessorTypesRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistprocessortypesrequest)`   
ListProcessorTypesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ListProcessorTypesResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.listprocessortypesresponse)>` | Promise  
  
### listProcessorVersions(request, callback)
    
    
    public listProcessorVersions(request: google.cloud.documentai.v1.IListProcessorVersionsRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.ListProcessorVersionsCallback): void;

Calls ListProcessorVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListProcessorVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistprocessorversionsrequest)`   
ListProcessorVersionsRequest message or plain object  
`callback` |  `[ListProcessorVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ListProcessorVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listProcessorVersions(request)
    
    
    public listProcessorVersions(request: google.cloud.documentai.v1.IListProcessorVersionsRequest): Promise<google.cloud.documentai.v1.ListProcessorVersionsResponse>;

Calls ListProcessorVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListProcessorVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ilistprocessorversionsrequest)`   
ListProcessorVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ListProcessorVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.listprocessorversionsresponse)>` | Promise  
  
### processDocument(request, callback)
    
    
    public processDocument(request: google.cloud.documentai.v1.IProcessRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.ProcessDocumentCallback): void;

Calls ProcessDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IProcessRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.iprocessrequest)`   
ProcessRequest message or plain object  
`callback` |  `[ProcessDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and ProcessResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### processDocument(request)
    
    
    public processDocument(request: google.cloud.documentai.v1.IProcessRequest): Promise<google.cloud.documentai.v1.ProcessResponse>;

Calls ProcessDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IProcessRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.iprocessrequest)`   
ProcessRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.documentai.v1.ProcessResponse](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.processresponse)>` | Promise  
  
### reviewDocument(request, callback)
    
    
    public reviewDocument(request: google.cloud.documentai.v1.IReviewDocumentRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.ReviewDocumentCallback): void;

Calls ReviewDocument.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReviewDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ireviewdocumentrequest)`   
ReviewDocumentRequest message or plain object  
`callback` |  `[ReviewDocumentCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### reviewDocument(request)
    
    
    public reviewDocument(request: google.cloud.documentai.v1.IReviewDocumentRequest): Promise<google.longrunning.Operation>;

Calls ReviewDocument.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReviewDocumentRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.ireviewdocumentrequest)`   
ReviewDocumentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### setDefaultProcessorVersion(request, callback)
    
    
    public setDefaultProcessorVersion(request: google.cloud.documentai.v1.ISetDefaultProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.SetDefaultProcessorVersionCallback): void;

Calls SetDefaultProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetDefaultProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.isetdefaultprocessorversionrequest)`   
SetDefaultProcessorVersionRequest message or plain object  
`callback` |  `[SetDefaultProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setDefaultProcessorVersion(request)
    
    
    public setDefaultProcessorVersion(request: google.cloud.documentai.v1.ISetDefaultProcessorVersionRequest): Promise<google.longrunning.Operation>;

Calls SetDefaultProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetDefaultProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.isetdefaultprocessorversionrequest)`   
SetDefaultProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### trainProcessorVersion(request, callback)
    
    
    public trainProcessorVersion(request: google.cloud.documentai.v1.ITrainProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.TrainProcessorVersionCallback): void;

Calls TrainProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITrainProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.itrainprocessorversionrequest)`   
TrainProcessorVersionRequest message or plain object  
`callback` |  `[TrainProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### trainProcessorVersion(request)
    
    
    public trainProcessorVersion(request: google.cloud.documentai.v1.ITrainProcessorVersionRequest): Promise<google.longrunning.Operation>;

Calls TrainProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITrainProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.itrainprocessorversionrequest)`   
TrainProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
### undeployProcessorVersion(request, callback)
    
    
    public undeployProcessorVersion(request: google.cloud.documentai.v1.IUndeployProcessorVersionRequest, callback: google.cloud.documentai.v1.DocumentProcessorService.UndeployProcessorVersionCallback): void;

Calls UndeployProcessorVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUndeployProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.iundeployprocessorversionrequest)`   
UndeployProcessorVersionRequest message or plain object  
`callback` |  `[UndeployProcessorVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### undeployProcessorVersion(request)
    
    
    public undeployProcessorVersion(request: google.cloud.documentai.v1.IUndeployProcessorVersionRequest): Promise<google.longrunning.Operation>;

Calls UndeployProcessorVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUndeployProcessorVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.cloud.documentai.v1.iundeployprocessorversionrequest)`   
UndeployProcessorVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/documentai/latest/documentai/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
