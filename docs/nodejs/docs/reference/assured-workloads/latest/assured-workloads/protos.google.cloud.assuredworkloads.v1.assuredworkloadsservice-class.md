---
url: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.assuredworkloadsservice-class
title: Class protos.google.cloud.assuredworkloads.v1.AssuredWorkloadsService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:55:07.021545+00:00
---

# Class protos.google.cloud.assuredworkloads.v1.AssuredWorkloadsService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.assuredworkloadsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.assuredworkloads.v1.AssuredWorkloadsService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  3.6.2  3.5.0  3.4.1  3.2.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.6 

Represents an AssuredWorkloadsService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.assuredworkloads.v1.AssuredWorkloadsService

## Package

[@google-cloud/assured-workloads](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AssuredWorkloadsService service.

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

### acknowledgeViolation(request, callback)
    
    
    public acknowledgeViolation(request: google.cloud.assuredworkloads.v1.IAcknowledgeViolationRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.AcknowledgeViolationCallback): void;

Calls AcknowledgeViolation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeViolationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.iacknowledgeviolationrequest)`   
AcknowledgeViolationRequest message or plain object  
`callback` |  `[AcknowledgeViolationCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and AcknowledgeViolationResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### acknowledgeViolation(request)
    
    
    public acknowledgeViolation(request: google.cloud.assuredworkloads.v1.IAcknowledgeViolationRequest): Promise<google.cloud.assuredworkloads.v1.AcknowledgeViolationResponse>;

Calls AcknowledgeViolation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAcknowledgeViolationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.iacknowledgeviolationrequest)`   
AcknowledgeViolationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.AcknowledgeViolationResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.acknowledgeviolationresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AssuredWorkloadsService;

Creates new AssuredWorkloadsService service using the specified rpc implementation.

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
`[AssuredWorkloadsService](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.assuredworkloadsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createWorkload(request, callback)
    
    
    public createWorkload(request: google.cloud.assuredworkloads.v1.ICreateWorkloadRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.CreateWorkloadCallback): void;

Calls CreateWorkload.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.icreateworkloadrequest)`   
CreateWorkloadRequest message or plain object  
`callback` |  `[CreateWorkloadCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createWorkload(request)
    
    
    public createWorkload(request: google.cloud.assuredworkloads.v1.ICreateWorkloadRequest): Promise<google.longrunning.Operation>;

Calls CreateWorkload.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.icreateworkloadrequest)`   
CreateWorkloadRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.longrunning.operation)>` | Promise  
  
### deleteWorkload(request, callback)
    
    
    public deleteWorkload(request: google.cloud.assuredworkloads.v1.IDeleteWorkloadRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.DeleteWorkloadCallback): void;

Calls DeleteWorkload.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.ideleteworkloadrequest)`   
DeleteWorkloadRequest message or plain object  
`callback` |  `[DeleteWorkloadCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteWorkload(request)
    
    
    public deleteWorkload(request: google.cloud.assuredworkloads.v1.IDeleteWorkloadRequest): Promise<google.protobuf.Empty>;

Calls DeleteWorkload.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.ideleteworkloadrequest)`   
DeleteWorkloadRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.protobuf.empty)>` | Promise  
  
### getViolation(request, callback)
    
    
    public getViolation(request: google.cloud.assuredworkloads.v1.IGetViolationRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.GetViolationCallback): void;

Calls GetViolation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetViolationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.igetviolationrequest)`   
GetViolationRequest message or plain object  
`callback` |  `[GetViolationCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and Violation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getViolation(request)
    
    
    public getViolation(request: google.cloud.assuredworkloads.v1.IGetViolationRequest): Promise<google.cloud.assuredworkloads.v1.Violation>;

Calls GetViolation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetViolationRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.igetviolationrequest)`   
GetViolationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.Violation](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.violation-class)>` | Promise  
  
### getWorkload(request, callback)
    
    
    public getWorkload(request: google.cloud.assuredworkloads.v1.IGetWorkloadRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.GetWorkloadCallback): void;

Calls GetWorkload.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.igetworkloadrequest)`   
GetWorkloadRequest message or plain object  
`callback` |  `[GetWorkloadCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and Workload  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getWorkload(request)
    
    
    public getWorkload(request: google.cloud.assuredworkloads.v1.IGetWorkloadRequest): Promise<google.cloud.assuredworkloads.v1.Workload>;

Calls GetWorkload.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.igetworkloadrequest)`   
GetWorkloadRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.workload-class)>` | Promise  
  
### listViolations(request, callback)
    
    
    public listViolations(request: google.cloud.assuredworkloads.v1.IListViolationsRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.ListViolationsCallback): void;

Calls ListViolations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListViolationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.ilistviolationsrequest)`   
ListViolationsRequest message or plain object  
`callback` |  `[ListViolationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and ListViolationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listViolations(request)
    
    
    public listViolations(request: google.cloud.assuredworkloads.v1.IListViolationsRequest): Promise<google.cloud.assuredworkloads.v1.ListViolationsResponse>;

Calls ListViolations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListViolationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.ilistviolationsrequest)`   
ListViolationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.ListViolationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.listviolationsresponse)>` | Promise  
  
### listWorkloads(request, callback)
    
    
    public listWorkloads(request: google.cloud.assuredworkloads.v1.IListWorkloadsRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.ListWorkloadsCallback): void;

Calls ListWorkloads.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.ilistworkloadsrequest)`   
ListWorkloadsRequest message or plain object  
`callback` |  `[ListWorkloadsCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and ListWorkloadsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listWorkloads(request)
    
    
    public listWorkloads(request: google.cloud.assuredworkloads.v1.IListWorkloadsRequest): Promise<google.cloud.assuredworkloads.v1.ListWorkloadsResponse>;

Calls ListWorkloads.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListWorkloadsRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.ilistworkloadsrequest)`   
ListWorkloadsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.ListWorkloadsResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.listworkloadsresponse)>` | Promise  
  
### restrictAllowedResources(request, callback)
    
    
    public restrictAllowedResources(request: google.cloud.assuredworkloads.v1.IRestrictAllowedResourcesRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.RestrictAllowedResourcesCallback): void;

Calls RestrictAllowedResources.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.irestrictallowedresourcesrequest)`   
RestrictAllowedResourcesRequest message or plain object  
`callback` |  `[RestrictAllowedResourcesCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and RestrictAllowedResourcesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### restrictAllowedResources(request)
    
    
    public restrictAllowedResources(request: google.cloud.assuredworkloads.v1.IRestrictAllowedResourcesRequest): Promise<google.cloud.assuredworkloads.v1.RestrictAllowedResourcesResponse>;

Calls RestrictAllowedResources.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRestrictAllowedResourcesRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.irestrictallowedresourcesrequest)`   
RestrictAllowedResourcesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.RestrictAllowedResourcesResponse](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.restrictallowedresourcesresponse)>` | Promise  
  
### updateWorkload(request, callback)
    
    
    public updateWorkload(request: google.cloud.assuredworkloads.v1.IUpdateWorkloadRequest, callback: google.cloud.assuredworkloads.v1.AssuredWorkloadsService.UpdateWorkloadCallback): void;

Calls UpdateWorkload.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.iupdateworkloadrequest)`   
UpdateWorkloadRequest message or plain object  
`callback` |  `[UpdateWorkloadCallback](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/overview.html)`   
Node-style callback called with the error, if any, and Workload  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateWorkload(request)
    
    
    public updateWorkload(request: google.cloud.assuredworkloads.v1.IUpdateWorkloadRequest): Promise<google.cloud.assuredworkloads.v1.Workload>;

Calls UpdateWorkload.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateWorkloadRequest](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.iupdateworkloadrequest)`   
UpdateWorkloadRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.assuredworkloads.v1.Workload](https://docs.cloud.google.com/nodejs/docs/reference/assured-workloads/latest/assured-workloads/protos.google.cloud.assuredworkloads.v1.workload-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
