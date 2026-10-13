---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.controlservice-class
title: Class protos.google.cloud.retail.v2alpha.ControlService (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:22:08.769470+00:00
---

# Class protos.google.cloud.retail.v2alpha.ControlService (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.controlservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2alpha.ControlService (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a ControlService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.retail.v2alpha.ControlService

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ControlService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ControlService;

Creates new ControlService service using the specified rpc implementation.

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
`[ControlService](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.controlservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createControl(request, callback)
    
    
    public createControl(request: google.cloud.retail.v2alpha.ICreateControlRequest, callback: google.cloud.retail.v2alpha.ControlService.CreateControlCallback): void;

Calls CreateControl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest)`   
CreateControlRequest message or plain object  
`callback` |  `[CreateControlCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Control  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createControl(request)
    
    
    public createControl(request: google.cloud.retail.v2alpha.ICreateControlRequest): Promise<google.cloud.retail.v2alpha.Control>;

Calls CreateControl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.icreatecontrolrequest)`   
CreateControlRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control)>` | Promise  
  
### deleteControl(request, callback)
    
    
    public deleteControl(request: google.cloud.retail.v2alpha.IDeleteControlRequest, callback: google.cloud.retail.v2alpha.ControlService.DeleteControlCallback): void;

Calls DeleteControl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest)`   
DeleteControlRequest message or plain object  
`callback` |  `[DeleteControlCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteControl(request)
    
    
    public deleteControl(request: google.cloud.retail.v2alpha.IDeleteControlRequest): Promise<google.protobuf.Empty>;

Calls DeleteControl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ideletecontrolrequest)`   
DeleteControlRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.protobuf.empty)>` | Promise  
  
### getControl(request, callback)
    
    
    public getControl(request: google.cloud.retail.v2alpha.IGetControlRequest, callback: google.cloud.retail.v2alpha.ControlService.GetControlCallback): void;

Calls GetControl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest)`   
GetControlRequest message or plain object  
`callback` |  `[GetControlCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Control  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getControl(request)
    
    
    public getControl(request: google.cloud.retail.v2alpha.IGetControlRequest): Promise<google.cloud.retail.v2alpha.Control>;

Calls GetControl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.igetcontrolrequest)`   
GetControlRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control)>` | Promise  
  
### listControls(request, callback)
    
    
    public listControls(request: google.cloud.retail.v2alpha.IListControlsRequest, callback: google.cloud.retail.v2alpha.ControlService.ListControlsCallback): void;

Calls ListControls.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
ListControlsRequest message or plain object  
`callback` |  `[ListControlsCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and ListControlsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listControls(request)
    
    
    public listControls(request: google.cloud.retail.v2alpha.IListControlsRequest): Promise<google.cloud.retail.v2alpha.ListControlsResponse>;

Calls ListControls.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.ilistcontrolsrequest)`   
ListControlsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.ListControlsResponse](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.listcontrolsresponse)>` | Promise  
  
### updateControl(request, callback)
    
    
    public updateControl(request: google.cloud.retail.v2alpha.IUpdateControlRequest, callback: google.cloud.retail.v2alpha.ControlService.UpdateControlCallback): void;

Calls UpdateControl.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest)`   
UpdateControlRequest message or plain object  
`callback` |  `[UpdateControlCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and Control  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateControl(request)
    
    
    public updateControl(request: google.cloud.retail.v2alpha.IUpdateControlRequest): Promise<google.cloud.retail.v2alpha.Control>;

Calls UpdateControl.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateControlRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.iupdatecontrolrequest)`   
UpdateControlRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2alpha.Control](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2alpha.control)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
