---
url: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.evaluationservice-class
title: Class protos.google.cloud.discoveryengine.v1beta.EvaluationService (3.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:51.447598+00:00
---

# Class protos.google.cloud.discoveryengine.v1beta.EvaluationService (3.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.evaluationservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.discoveryengine.v1beta.EvaluationService (3.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.3.1 (latest)  3.3.0  3.1.0  2.9.0  2.8.0  2.6.0  2.2.0  2.0.1  1.14.0  1.10.0  1.9.0  1.7.0  1.6.0  1.4.1  1.3.1  1.2.0  1.0.0  0.6.0  0.5.0  0.3.1  0.2.0 

Represents an EvaluationService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.discoveryengine.v1beta.EvaluationService

## Package

[@google-cloud/discoveryengine](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new EvaluationService service.

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

### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): EvaluationService;

Creates new EvaluationService service using the specified rpc implementation.

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
`[EvaluationService](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.evaluationservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createEvaluation(request, callback)
    
    
    public createEvaluation(request: google.cloud.discoveryengine.v1beta.ICreateEvaluationRequest, callback: google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluationCallback): void;

Calls CreateEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateevaluationrequest)`   
CreateEvaluationRequest message or plain object  
`callback` |  `[CreateEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEvaluation(request)
    
    
    public createEvaluation(request: google.cloud.discoveryengine.v1beta.ICreateEvaluationRequest): Promise<google.longrunning.Operation>;

Calls CreateEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.icreateevaluationrequest)`   
CreateEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.longrunning.operation)>` | Promise  
  
### getEvaluation(request, callback)
    
    
    public getEvaluation(request: google.cloud.discoveryengine.v1beta.IGetEvaluationRequest, callback: google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluationCallback): void;

Calls GetEvaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetevaluationrequest)`   
GetEvaluationRequest message or plain object  
`callback` |  `[GetEvaluationCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and Evaluation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEvaluation(request)
    
    
    public getEvaluation(request: google.cloud.discoveryengine.v1beta.IGetEvaluationRequest): Promise<google.cloud.discoveryengine.v1beta.Evaluation>;

Calls GetEvaluation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEvaluationRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.igetevaluationrequest)`   
GetEvaluationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.Evaluation](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.evaluation-class)>` | Promise  
  
### listEvaluationResults(request, callback)
    
    
    public listEvaluationResults(request: google.cloud.discoveryengine.v1beta.IListEvaluationResultsRequest, callback: google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResultsCallback): void;

Calls ListEvaluationResults.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistevaluationresultsrequest)`   
ListEvaluationResultsRequest message or plain object  
`callback` |  `[ListEvaluationResultsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEvaluationResultsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluationResults(request)
    
    
    public listEvaluationResults(request: google.cloud.discoveryengine.v1beta.IListEvaluationResultsRequest): Promise<google.cloud.discoveryengine.v1beta.ListEvaluationResultsResponse>;

Calls ListEvaluationResults.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistevaluationresultsrequest)`   
ListEvaluationResultsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.ListEvaluationResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.listevaluationresultsresponse-class)>` | Promise  
  
### listEvaluations(request, callback)
    
    
    public listEvaluations(request: google.cloud.discoveryengine.v1beta.IListEvaluationsRequest, callback: google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationsCallback): void;

Calls ListEvaluations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistevaluationsrequest)`   
ListEvaluationsRequest message or plain object  
`callback` |  `[ListEvaluationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEvaluationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEvaluations(request)
    
    
    public listEvaluations(request: google.cloud.discoveryengine.v1beta.IListEvaluationsRequest): Promise<google.cloud.discoveryengine.v1beta.ListEvaluationsResponse>;

Calls ListEvaluations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEvaluationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.ilistevaluationsrequest)`   
ListEvaluationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.discoveryengine.v1beta.ListEvaluationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/discoveryengine/latest/discoveryengine/protos.google.cloud.discoveryengine.v1beta.listevaluationsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
