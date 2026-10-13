---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.regioninstancegroupmanagerresizerequests-class
title: Class protos.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:49.573222+00:00
---

# Class protos.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.regioninstancegroupmanagerresizerequests-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a RegionInstanceGroupManagerResizeRequests

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new RegionInstanceGroupManagerResizeRequests service.

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

### cancel(request, callback)
    
    
    public cancel(request: google.cloud.compute.v1.ICancelRegionInstanceGroupManagerResizeRequestRequest, callback: google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests.CancelCallback): void;

Calls Cancel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.icancelregioninstancegroupmanagerresizerequestrequest)`   
CancelRegionInstanceGroupManagerResizeRequestRequest message or plain object  
`callback` |  `[CancelCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancel(request)
    
    
    public cancel(request: google.cloud.compute.v1.ICancelRegionInstanceGroupManagerResizeRequestRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Cancel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.icancelregioninstancegroupmanagerresizerequestrequest)`   
CancelRegionInstanceGroupManagerResizeRequestRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): RegionInstanceGroupManagerResizeRequests;

Creates new RegionInstanceGroupManagerResizeRequests service using the specified rpc implementation.

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
`[RegionInstanceGroupManagerResizeRequests](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.regioninstancegroupmanagerresizerequests-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1.IDeleteRegionInstanceGroupManagerResizeRequestRequest, callback: google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideleteregioninstancegroupmanagerresizerequestrequest)`   
DeleteRegionInstanceGroupManagerResizeRequestRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1.IDeleteRegionInstanceGroupManagerResizeRequestRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideleteregioninstancegroupmanagerresizerequestrequest)`   
DeleteRegionInstanceGroupManagerResizeRequestRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1.IGetRegionInstanceGroupManagerResizeRequestRequest, callback: google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetregioninstancegroupmanagerresizerequestrequest)`   
GetRegionInstanceGroupManagerResizeRequestRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and InstanceGroupManagerResizeRequest  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1.IGetRegionInstanceGroupManagerResizeRequestRequest): Promise<google.cloud.compute.v1.InstanceGroupManagerResizeRequest>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetregioninstancegroupmanagerresizerequestrequest)`   
GetRegionInstanceGroupManagerResizeRequestRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.InstanceGroupManagerResizeRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.instancegroupmanagerresizerequest-class)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1.IInsertRegionInstanceGroupManagerResizeRequestRequest, callback: google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinsertregioninstancegroupmanagerresizerequestrequest)`   
InsertRegionInstanceGroupManagerResizeRequestRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1.IInsertRegionInstanceGroupManagerResizeRequestRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertRegionInstanceGroupManagerResizeRequestRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinsertregioninstancegroupmanagerresizerequestrequest)`   
InsertRegionInstanceGroupManagerResizeRequestRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1.IListRegionInstanceGroupManagerResizeRequestsRequest, callback: google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequests.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstanceGroupManagerResizeRequestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ilistregioninstancegroupmanagerresizerequestsrequest)`   
ListRegionInstanceGroupManagerResizeRequestsRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and RegionInstanceGroupManagerResizeRequestsListResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1.IListRegionInstanceGroupManagerResizeRequestsRequest): Promise<google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsListResponse>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRegionInstanceGroupManagerResizeRequestsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ilistregioninstancegroupmanagerresizerequestsrequest)`   
ListRegionInstanceGroupManagerResizeRequestsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.RegionInstanceGroupManagerResizeRequestsListResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.regioninstancegroupmanagerresizerequestslistresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
