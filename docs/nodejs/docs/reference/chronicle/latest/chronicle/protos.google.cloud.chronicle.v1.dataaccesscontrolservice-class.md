---
url: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccesscontrolservice-class
title: Class protos.google.cloud.chronicle.v1.DataAccessControlService (0.10.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:17.309760+00:00
---

# Class protos.google.cloud.chronicle.v1.DataAccessControlService (0.10.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccesscontrolservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.chronicle.v1.DataAccessControlService (0.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.1 (latest)  0.8.0  0.6.0  0.5.0 

Represents a DataAccessControlService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.chronicle.v1.DataAccessControlService

## Package

[@google-cloud/chronicle](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DataAccessControlService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DataAccessControlService;

Creates new DataAccessControlService service using the specified rpc implementation.

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
`[DataAccessControlService](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccesscontrolservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDataAccessLabel(request, callback)
    
    
    public createDataAccessLabel(request: google.cloud.chronicle.v1.ICreateDataAccessLabelRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.CreateDataAccessLabelCallback): void;

Calls CreateDataAccessLabel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedataaccesslabelrequest)`   
CreateDataAccessLabelRequest message or plain object  
`callback` |  `[CreateDataAccessLabelCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAccessLabel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAccessLabel(request)
    
    
    public createDataAccessLabel(request: google.cloud.chronicle.v1.ICreateDataAccessLabelRequest): Promise<google.cloud.chronicle.v1.DataAccessLabel>;

Calls CreateDataAccessLabel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedataaccesslabelrequest)`   
CreateDataAccessLabelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataAccessLabel](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccesslabel)>` | Promise  
  
### createDataAccessScope(request, callback)
    
    
    public createDataAccessScope(request: google.cloud.chronicle.v1.ICreateDataAccessScopeRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.CreateDataAccessScopeCallback): void;

Calls CreateDataAccessScope.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedataaccessscoperequest)`   
CreateDataAccessScopeRequest message or plain object  
`callback` |  `[CreateDataAccessScopeCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAccessScope  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDataAccessScope(request)
    
    
    public createDataAccessScope(request: google.cloud.chronicle.v1.ICreateDataAccessScopeRequest): Promise<google.cloud.chronicle.v1.DataAccessScope>;

Calls CreateDataAccessScope.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.icreatedataaccessscoperequest)`   
CreateDataAccessScopeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataAccessScope](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccessscope)>` | Promise  
  
### deleteDataAccessLabel(request, callback)
    
    
    public deleteDataAccessLabel(request: google.cloud.chronicle.v1.IDeleteDataAccessLabelRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.DeleteDataAccessLabelCallback): void;

Calls DeleteDataAccessLabel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedataaccesslabelrequest)`   
DeleteDataAccessLabelRequest message or plain object  
`callback` |  `[DeleteDataAccessLabelCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAccessLabel(request)
    
    
    public deleteDataAccessLabel(request: google.cloud.chronicle.v1.IDeleteDataAccessLabelRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataAccessLabel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedataaccesslabelrequest)`   
DeleteDataAccessLabelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.protobuf.empty)>` | Promise  
  
### deleteDataAccessScope(request, callback)
    
    
    public deleteDataAccessScope(request: google.cloud.chronicle.v1.IDeleteDataAccessScopeRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.DeleteDataAccessScopeCallback): void;

Calls DeleteDataAccessScope.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedataaccessscoperequest)`   
DeleteDataAccessScopeRequest message or plain object  
`callback` |  `[DeleteDataAccessScopeCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDataAccessScope(request)
    
    
    public deleteDataAccessScope(request: google.cloud.chronicle.v1.IDeleteDataAccessScopeRequest): Promise<google.protobuf.Empty>;

Calls DeleteDataAccessScope.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ideletedataaccessscoperequest)`   
DeleteDataAccessScopeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.protobuf.empty)>` | Promise  
  
### getDataAccessLabel(request, callback)
    
    
    public getDataAccessLabel(request: google.cloud.chronicle.v1.IGetDataAccessLabelRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.GetDataAccessLabelCallback): void;

Calls GetDataAccessLabel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdataaccesslabelrequest)`   
GetDataAccessLabelRequest message or plain object  
`callback` |  `[GetDataAccessLabelCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAccessLabel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAccessLabel(request)
    
    
    public getDataAccessLabel(request: google.cloud.chronicle.v1.IGetDataAccessLabelRequest): Promise<google.cloud.chronicle.v1.DataAccessLabel>;

Calls GetDataAccessLabel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdataaccesslabelrequest)`   
GetDataAccessLabelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataAccessLabel](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccesslabel)>` | Promise  
  
### getDataAccessScope(request, callback)
    
    
    public getDataAccessScope(request: google.cloud.chronicle.v1.IGetDataAccessScopeRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.GetDataAccessScopeCallback): void;

Calls GetDataAccessScope.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdataaccessscoperequest)`   
GetDataAccessScopeRequest message or plain object  
`callback` |  `[GetDataAccessScopeCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAccessScope  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDataAccessScope(request)
    
    
    public getDataAccessScope(request: google.cloud.chronicle.v1.IGetDataAccessScopeRequest): Promise<google.cloud.chronicle.v1.DataAccessScope>;

Calls GetDataAccessScope.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.igetdataaccessscoperequest)`   
GetDataAccessScopeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataAccessScope](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccessscope)>` | Promise  
  
### listDataAccessLabels(request, callback)
    
    
    public listDataAccessLabels(request: google.cloud.chronicle.v1.IListDataAccessLabelsRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.ListDataAccessLabelsCallback): void;

Calls ListDataAccessLabels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAccessLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdataaccesslabelsrequest)`   
ListDataAccessLabelsRequest message or plain object  
`callback` |  `[ListDataAccessLabelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataAccessLabelsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAccessLabels(request)
    
    
    public listDataAccessLabels(request: google.cloud.chronicle.v1.IListDataAccessLabelsRequest): Promise<google.cloud.chronicle.v1.ListDataAccessLabelsResponse>;

Calls ListDataAccessLabels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataAccessLabelsRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdataaccesslabelsrequest)`   
ListDataAccessLabelsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListDataAccessLabelsResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listdataaccesslabelsresponse)>` | Promise  
  
### listDataAccessScopes(request, callback)
    
    
    public listDataAccessScopes(request: google.cloud.chronicle.v1.IListDataAccessScopesRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.ListDataAccessScopesCallback): void;

Calls ListDataAccessScopes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDataAccessScopesRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdataaccessscopesrequest)`   
ListDataAccessScopesRequest message or plain object  
`callback` |  `[ListDataAccessScopesCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDataAccessScopesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDataAccessScopes(request)
    
    
    public listDataAccessScopes(request: google.cloud.chronicle.v1.IListDataAccessScopesRequest): Promise<google.cloud.chronicle.v1.ListDataAccessScopesResponse>;

Calls ListDataAccessScopes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDataAccessScopesRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.ilistdataaccessscopesrequest)`   
ListDataAccessScopesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.ListDataAccessScopesResponse](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.listdataaccessscopesresponse)>` | Promise  
  
### updateDataAccessLabel(request, callback)
    
    
    public updateDataAccessLabel(request: google.cloud.chronicle.v1.IUpdateDataAccessLabelRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.UpdateDataAccessLabelCallback): void;

Calls UpdateDataAccessLabel.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedataaccesslabelrequest)`   
UpdateDataAccessLabelRequest message or plain object  
`callback` |  `[UpdateDataAccessLabelCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAccessLabel  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAccessLabel(request)
    
    
    public updateDataAccessLabel(request: google.cloud.chronicle.v1.IUpdateDataAccessLabelRequest): Promise<google.cloud.chronicle.v1.DataAccessLabel>;

Calls UpdateDataAccessLabel.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAccessLabelRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedataaccesslabelrequest)`   
UpdateDataAccessLabelRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataAccessLabel](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccesslabel)>` | Promise  
  
### updateDataAccessScope(request, callback)
    
    
    public updateDataAccessScope(request: google.cloud.chronicle.v1.IUpdateDataAccessScopeRequest, callback: google.cloud.chronicle.v1.DataAccessControlService.UpdateDataAccessScopeCallback): void;

Calls UpdateDataAccessScope.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedataaccessscoperequest)`   
UpdateDataAccessScopeRequest message or plain object  
`callback` |  `[UpdateDataAccessScopeCallback](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/overview.html)`   
Node-style callback called with the error, if any, and DataAccessScope  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDataAccessScope(request)
    
    
    public updateDataAccessScope(request: google.cloud.chronicle.v1.IUpdateDataAccessScopeRequest): Promise<google.cloud.chronicle.v1.DataAccessScope>;

Calls UpdateDataAccessScope.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDataAccessScopeRequest](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.iupdatedataaccessscoperequest)`   
UpdateDataAccessScopeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.chronicle.v1.DataAccessScope](https://docs.cloud.google.com/nodejs/docs/reference/chronicle/latest/chronicle/protos.google.cloud.chronicle.v1.dataaccessscope)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
