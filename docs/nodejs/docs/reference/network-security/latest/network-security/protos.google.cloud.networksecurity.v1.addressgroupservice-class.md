---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.addressgroupservice-class
title: Class protos.google.cloud.networksecurity.v1.AddressGroupService (4.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:30:56.671287+00:00
---

# Class protos.google.cloud.networksecurity.v1.AddressGroupService (4.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.addressgroupservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networksecurity.v1.AddressGroupService (4.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

4.1.1 (latest)  3.6.0  3.1.0  1.1.2  1.0.2  0.5.0  0.3.0  0.2.0 

Represents an AddressGroupService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.networksecurity.v1.AddressGroupService

## Package

[@google-cloud/network-security](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AddressGroupService service.

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

### addAddressGroupItems(request, callback)
    
    
    public addAddressGroupItems(request: google.cloud.networksecurity.v1.IAddAddressGroupItemsRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.AddAddressGroupItemsCallback): void;

Calls AddAddressGroupItems.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAddAddressGroupItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.iaddaddressgroupitemsrequest)`   
AddAddressGroupItemsRequest message or plain object  
`callback` |  `[AddAddressGroupItemsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### addAddressGroupItems(request)
    
    
    public addAddressGroupItems(request: google.cloud.networksecurity.v1.IAddAddressGroupItemsRequest): Promise<google.longrunning.Operation>;

Calls AddAddressGroupItems.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAddAddressGroupItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.iaddaddressgroupitemsrequest)`   
AddAddressGroupItemsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)>` | Promise  
  
### cloneAddressGroupItems(request, callback)
    
    
    public cloneAddressGroupItems(request: google.cloud.networksecurity.v1.ICloneAddressGroupItemsRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.CloneAddressGroupItemsCallback): void;

Calls CloneAddressGroupItems.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICloneAddressGroupItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.icloneaddressgroupitemsrequest)`   
CloneAddressGroupItemsRequest message or plain object  
`callback` |  `[CloneAddressGroupItemsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cloneAddressGroupItems(request)
    
    
    public cloneAddressGroupItems(request: google.cloud.networksecurity.v1.ICloneAddressGroupItemsRequest): Promise<google.longrunning.Operation>;

Calls CloneAddressGroupItems.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICloneAddressGroupItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.icloneaddressgroupitemsrequest)`   
CloneAddressGroupItemsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AddressGroupService;

Creates new AddressGroupService service using the specified rpc implementation.

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
`[AddressGroupService](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.addressgroupservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAddressGroup(request, callback)
    
    
    public createAddressGroup(request: google.cloud.networksecurity.v1.ICreateAddressGroupRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.CreateAddressGroupCallback): void;

Calls CreateAddressGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.icreateaddressgrouprequest)`   
CreateAddressGroupRequest message or plain object  
`callback` |  `[CreateAddressGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAddressGroup(request)
    
    
    public createAddressGroup(request: google.cloud.networksecurity.v1.ICreateAddressGroupRequest): Promise<google.longrunning.Operation>;

Calls CreateAddressGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.icreateaddressgrouprequest)`   
CreateAddressGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)>` | Promise  
  
### deleteAddressGroup(request, callback)
    
    
    public deleteAddressGroup(request: google.cloud.networksecurity.v1.IDeleteAddressGroupRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.DeleteAddressGroupCallback): void;

Calls DeleteAddressGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ideleteaddressgrouprequest)`   
DeleteAddressGroupRequest message or plain object  
`callback` |  `[DeleteAddressGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAddressGroup(request)
    
    
    public deleteAddressGroup(request: google.cloud.networksecurity.v1.IDeleteAddressGroupRequest): Promise<google.longrunning.Operation>;

Calls DeleteAddressGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ideleteaddressgrouprequest)`   
DeleteAddressGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)>` | Promise  
  
### getAddressGroup(request, callback)
    
    
    public getAddressGroup(request: google.cloud.networksecurity.v1.IGetAddressGroupRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.GetAddressGroupCallback): void;

Calls GetAddressGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.igetaddressgrouprequest)`   
GetAddressGroupRequest message or plain object  
`callback` |  `[GetAddressGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and AddressGroup  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAddressGroup(request)
    
    
    public getAddressGroup(request: google.cloud.networksecurity.v1.IGetAddressGroupRequest): Promise<google.cloud.networksecurity.v1.AddressGroup>;

Calls GetAddressGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.igetaddressgrouprequest)`   
GetAddressGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networksecurity.v1.AddressGroup](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.addressgroup-class)>` | Promise  
  
### listAddressGroupReferences(request, callback)
    
    
    public listAddressGroupReferences(request: google.cloud.networksecurity.v1.IListAddressGroupReferencesRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroupReferencesCallback): void;

Calls ListAddressGroupReferences.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAddressGroupReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ilistaddressgroupreferencesrequest)`   
ListAddressGroupReferencesRequest message or plain object  
`callback` |  `[ListAddressGroupReferencesCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAddressGroupReferencesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAddressGroupReferences(request)
    
    
    public listAddressGroupReferences(request: google.cloud.networksecurity.v1.IListAddressGroupReferencesRequest): Promise<google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse>;

Calls ListAddressGroupReferences.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAddressGroupReferencesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ilistaddressgroupreferencesrequest)`   
ListAddressGroupReferencesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.listaddressgroupreferencesresponse-class)>` | Promise  
  
### listAddressGroups(request, callback)
    
    
    public listAddressGroups(request: google.cloud.networksecurity.v1.IListAddressGroupsRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.ListAddressGroupsCallback): void;

Calls ListAddressGroups.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAddressGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ilistaddressgroupsrequest)`   
ListAddressGroupsRequest message or plain object  
`callback` |  `[ListAddressGroupsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAddressGroupsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAddressGroups(request)
    
    
    public listAddressGroups(request: google.cloud.networksecurity.v1.IListAddressGroupsRequest): Promise<google.cloud.networksecurity.v1.ListAddressGroupsResponse>;

Calls ListAddressGroups.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAddressGroupsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.ilistaddressgroupsrequest)`   
ListAddressGroupsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networksecurity.v1.ListAddressGroupsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.listaddressgroupsresponse)>` | Promise  
  
### removeAddressGroupItems(request, callback)
    
    
    public removeAddressGroupItems(request: google.cloud.networksecurity.v1.IRemoveAddressGroupItemsRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.RemoveAddressGroupItemsCallback): void;

Calls RemoveAddressGroupItems.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAddressGroupItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.iremoveaddressgroupitemsrequest)`   
RemoveAddressGroupItemsRequest message or plain object  
`callback` |  `[RemoveAddressGroupItemsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### removeAddressGroupItems(request)
    
    
    public removeAddressGroupItems(request: google.cloud.networksecurity.v1.IRemoveAddressGroupItemsRequest): Promise<google.longrunning.Operation>;

Calls RemoveAddressGroupItems.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRemoveAddressGroupItemsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.iremoveaddressgroupitemsrequest)`   
RemoveAddressGroupItemsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)>` | Promise  
  
### updateAddressGroup(request, callback)
    
    
    public updateAddressGroup(request: google.cloud.networksecurity.v1.IUpdateAddressGroupRequest, callback: google.cloud.networksecurity.v1.AddressGroupService.UpdateAddressGroupCallback): void;

Calls UpdateAddressGroup.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.iupdateaddressgrouprequest)`   
UpdateAddressGroupRequest message or plain object  
`callback` |  `[UpdateAddressGroupCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAddressGroup(request)
    
    
    public updateAddressGroup(request: google.cloud.networksecurity.v1.IUpdateAddressGroupRequest): Promise<google.longrunning.Operation>;

Calls UpdateAddressGroup.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAddressGroupRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.cloud.networksecurity.v1.iupdateaddressgrouprequest)`   
UpdateAddressGroupRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-security/latest/network-security/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
