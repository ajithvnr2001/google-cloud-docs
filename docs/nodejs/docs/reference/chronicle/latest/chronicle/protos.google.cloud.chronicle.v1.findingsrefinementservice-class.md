---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementservice-class
title: Class protos.google.cloud.chronicle.v1.FindingsRefinementService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:38.658151+00:00
---

# Class protos.google.cloud.chronicle.v1.FindingsRefinementService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.FindingsRefinementService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a FindingsRefinementService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.FindingsRefinementService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new FindingsRefinementService service.

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

### computeAllFindingsRefinementActivities(request, callback)
    
    
    public computeAllFindingsRefinementActivities(request: google.cloud.chronicle.v1.IComputeAllFindingsRefinementActivitiesRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.ComputeAllFindingsRefinementActivitiesCallback): void;

Calls ComputeAllFindingsRefinementActivities.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeAllFindingsRefinementActivitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icomputeallfindingsrefinementactivitiesrequest)`   
ComputeAllFindingsRefinementActivitiesRequest message or plain object  
`callback` |  `[ComputeAllFindingsRefinementActivitiesCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ComputeAllFindingsRefinementActivitiesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### computeAllFindingsRefinementActivities(request)
    
    
    public computeAllFindingsRefinementActivities(request: google.cloud.chronicle.v1.IComputeAllFindingsRefinementActivitiesRequest): Promise<google.cloud.chronicle.v1.ComputeAllFindingsRefinementActivitiesResponse>;

Calls ComputeAllFindingsRefinementActivities.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IComputeAllFindingsRefinementActivitiesRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icomputeallfindingsrefinementactivitiesrequest)`   
ComputeAllFindingsRefinementActivitiesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ComputeAllFindingsRefinementActivitiesResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.computeallfindingsrefinementactivitiesresponse)>` | Promise  
  
### computeFindingsRefinementActivity(request, callback)
    
    
    public computeFindingsRefinementActivity(request: google.cloud.chronicle.v1.IComputeFindingsRefinementActivityRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.ComputeFindingsRefinementActivityCallback): void;

Calls ComputeFindingsRefinementActivity.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IComputeFindingsRefinementActivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icomputefindingsrefinementactivityrequest)`   
ComputeFindingsRefinementActivityRequest message or plain object  
`callback` |  `[ComputeFindingsRefinementActivityCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ComputeFindingsRefinementActivityResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### computeFindingsRefinementActivity(request)
    
    
    public computeFindingsRefinementActivity(request: google.cloud.chronicle.v1.IComputeFindingsRefinementActivityRequest): Promise<google.cloud.chronicle.v1.ComputeFindingsRefinementActivityResponse>;

Calls ComputeFindingsRefinementActivity.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IComputeFindingsRefinementActivityRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icomputefindingsrefinementactivityrequest)`   
ComputeFindingsRefinementActivityRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ComputeFindingsRefinementActivityResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.computefindingsrefinementactivityresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): FindingsRefinementService;

Creates new FindingsRefinementService service using the specified rpc implementation.

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
`[FindingsRefinementService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFindingsRefinement(request, callback)
    
    
    public createFindingsRefinement(request: google.cloud.chronicle.v1.ICreateFindingsRefinementRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.CreateFindingsRefinementCallback): void;

Calls CreateFindingsRefinement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFindingsRefinementRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatefindingsrefinementrequest)`   
CreateFindingsRefinementRequest message or plain object  
`callback` |  `[CreateFindingsRefinementCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FindingsRefinement  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFindingsRefinement(request)
    
    
    public createFindingsRefinement(request: google.cloud.chronicle.v1.ICreateFindingsRefinementRequest): Promise<google.cloud.chronicle.v1.FindingsRefinement>;

Calls CreateFindingsRefinement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFindingsRefinementRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatefindingsrefinementrequest)`   
CreateFindingsRefinementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FindingsRefinement](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinement)>` | Promise  
  
### getFindingsRefinement(request, callback)
    
    
    public getFindingsRefinement(request: google.cloud.chronicle.v1.IGetFindingsRefinementRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.GetFindingsRefinementCallback): void;

Calls GetFindingsRefinement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFindingsRefinementRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfindingsrefinementrequest)`   
GetFindingsRefinementRequest message or plain object  
`callback` |  `[GetFindingsRefinementCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FindingsRefinement  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFindingsRefinement(request)
    
    
    public getFindingsRefinement(request: google.cloud.chronicle.v1.IGetFindingsRefinementRequest): Promise<google.cloud.chronicle.v1.FindingsRefinement>;

Calls GetFindingsRefinement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFindingsRefinementRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfindingsrefinementrequest)`   
GetFindingsRefinementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FindingsRefinement](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinement)>` | Promise  
  
### getFindingsRefinementDeployment(request, callback)
    
    
    public getFindingsRefinementDeployment(request: google.cloud.chronicle.v1.IGetFindingsRefinementDeploymentRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.GetFindingsRefinementDeploymentCallback): void;

Calls GetFindingsRefinementDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFindingsRefinementDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfindingsrefinementdeploymentrequest)`   
GetFindingsRefinementDeploymentRequest message or plain object  
`callback` |  `[GetFindingsRefinementDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FindingsRefinementDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFindingsRefinementDeployment(request)
    
    
    public getFindingsRefinementDeployment(request: google.cloud.chronicle.v1.IGetFindingsRefinementDeploymentRequest): Promise<google.cloud.chronicle.v1.FindingsRefinementDeployment>;

Calls GetFindingsRefinementDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFindingsRefinementDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetfindingsrefinementdeploymentrequest)`   
GetFindingsRefinementDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FindingsRefinementDeployment](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementdeployment)>` | Promise  
  
### listAllFindingsRefinementDeployments(request, callback)
    
    
    public listAllFindingsRefinementDeployments(request: google.cloud.chronicle.v1.IListAllFindingsRefinementDeploymentsRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.ListAllFindingsRefinementDeploymentsCallback): void;

Calls ListAllFindingsRefinementDeployments.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAllFindingsRefinementDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistallfindingsrefinementdeploymentsrequest)`   
ListAllFindingsRefinementDeploymentsRequest message or plain object  
`callback` |  `[ListAllFindingsRefinementDeploymentsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAllFindingsRefinementDeploymentsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAllFindingsRefinementDeployments(request)
    
    
    public listAllFindingsRefinementDeployments(request: google.cloud.chronicle.v1.IListAllFindingsRefinementDeploymentsRequest): Promise<google.cloud.chronicle.v1.ListAllFindingsRefinementDeploymentsResponse>;

Calls ListAllFindingsRefinementDeployments.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAllFindingsRefinementDeploymentsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistallfindingsrefinementdeploymentsrequest)`   
ListAllFindingsRefinementDeploymentsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListAllFindingsRefinementDeploymentsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listallfindingsrefinementdeploymentsresponse)>` | Promise  
  
### listFindingsRefinements(request, callback)
    
    
    public listFindingsRefinements(request: google.cloud.chronicle.v1.IListFindingsRefinementsRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.ListFindingsRefinementsCallback): void;

Calls ListFindingsRefinements.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFindingsRefinementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfindingsrefinementsrequest)`   
ListFindingsRefinementsRequest message or plain object  
`callback` |  `[ListFindingsRefinementsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFindingsRefinementsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFindingsRefinements(request)
    
    
    public listFindingsRefinements(request: google.cloud.chronicle.v1.IListFindingsRefinementsRequest): Promise<google.cloud.chronicle.v1.ListFindingsRefinementsResponse>;

Calls ListFindingsRefinements.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFindingsRefinementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistfindingsrefinementsrequest)`   
ListFindingsRefinementsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListFindingsRefinementsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listfindingsrefinementsresponse)>` | Promise  
  
### updateFindingsRefinement(request, callback)
    
    
    public updateFindingsRefinement(request: google.cloud.chronicle.v1.IUpdateFindingsRefinementRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.UpdateFindingsRefinementCallback): void;

Calls UpdateFindingsRefinement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFindingsRefinementRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatefindingsrefinementrequest)`   
UpdateFindingsRefinementRequest message or plain object  
`callback` |  `[UpdateFindingsRefinementCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FindingsRefinement  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFindingsRefinement(request)
    
    
    public updateFindingsRefinement(request: google.cloud.chronicle.v1.IUpdateFindingsRefinementRequest): Promise<google.cloud.chronicle.v1.FindingsRefinement>;

Calls UpdateFindingsRefinement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFindingsRefinementRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatefindingsrefinementrequest)`   
UpdateFindingsRefinementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FindingsRefinement](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinement)>` | Promise  
  
### updateFindingsRefinementDeployment(request, callback)
    
    
    public updateFindingsRefinementDeployment(request: google.cloud.chronicle.v1.IUpdateFindingsRefinementDeploymentRequest, callback: google.cloud.chronicle.v1.FindingsRefinementService.UpdateFindingsRefinementDeploymentCallback): void;

Calls UpdateFindingsRefinementDeployment.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFindingsRefinementDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatefindingsrefinementdeploymentrequest)`   
UpdateFindingsRefinementDeploymentRequest message or plain object  
`callback` |  `[UpdateFindingsRefinementDeploymentCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and FindingsRefinementDeployment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateFindingsRefinementDeployment(request)
    
    
    public updateFindingsRefinementDeployment(request: google.cloud.chronicle.v1.IUpdateFindingsRefinementDeploymentRequest): Promise<google.cloud.chronicle.v1.FindingsRefinementDeployment>;

Calls UpdateFindingsRefinementDeployment.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateFindingsRefinementDeploymentRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatefindingsrefinementdeploymentrequest)`   
UpdateFindingsRefinementDeploymentRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.FindingsRefinementDeployment](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.findingsrefinementdeployment)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
