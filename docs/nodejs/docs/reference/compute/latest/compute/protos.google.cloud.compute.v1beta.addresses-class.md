---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.addresses-class
title: Class protos.google.cloud.compute.v1beta.Addresses (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:19.893651+00:00
---

# Class protos.google.cloud.compute.v1beta.Addresses (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.addresses-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1beta.Addresses (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents an Addresses

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1beta.Addresses

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Addresses service.

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

### aggregatedList(request, callback)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListAddressesRequest, callback: google.cloud.compute.v1beta.Addresses.AggregatedListCallback): void;

Calls AggregatedList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListAddressesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlistaddressesrequest)`   
AggregatedListAddressesRequest message or plain object  
`callback` |  `[AggregatedListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and AddressAggregatedList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregatedList(request)
    
    
    public aggregatedList(request: google.cloud.compute.v1beta.IAggregatedListAddressesRequest): Promise<google.cloud.compute.v1beta.AddressAggregatedList>;

Calls AggregatedList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListAddressesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iaggregatedlistaddressesrequest)`   
AggregatedListAddressesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.AddressAggregatedList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.addressaggregatedlist)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Addresses;

Creates new Addresses service using the specified rpc implementation.

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
`[Addresses](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.addresses-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteAddressRequest, callback: google.cloud.compute.v1beta.Addresses.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteaddressrequest)`   
DeleteAddressRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1beta.IDeleteAddressRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ideleteaddressrequest)`   
DeleteAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1beta.IGetAddressRequest, callback: google.cloud.compute.v1beta.Addresses.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetaddressrequest)`   
GetAddressRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Address  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1beta.IGetAddressRequest): Promise<google.cloud.compute.v1beta.Address>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.igetaddressrequest)`   
GetAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Address](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.address-class)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertAddressRequest, callback: google.cloud.compute.v1beta.Addresses.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertaddressrequest)`   
InsertAddressRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1beta.IInsertAddressRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinsertaddressrequest)`   
InsertAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1beta.IListAddressesRequest, callback: google.cloud.compute.v1beta.Addresses.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAddressesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistaddressesrequest)`   
ListAddressesRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and AddressList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1beta.IListAddressesRequest): Promise<google.cloud.compute.v1beta.AddressList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAddressesRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.ilistaddressesrequest)`   
ListAddressesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.AddressList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.addresslist)>` | Promise  
  
### move(request, callback)
    
    
    public move(request: google.cloud.compute.v1beta.IMoveAddressRequest, callback: google.cloud.compute.v1beta.Addresses.MoveCallback): void;

Calls Move.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IMoveAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imoveaddressrequest)`   
MoveAddressRequest message or plain object  
`callback` |  `[MoveCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### move(request)
    
    
    public move(request: google.cloud.compute.v1beta.IMoveAddressRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls Move.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IMoveAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.imoveaddressrequest)`   
MoveAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### setLabels(request, callback)
    
    
    public setLabels(request: google.cloud.compute.v1beta.ISetLabelsAddressRequest, callback: google.cloud.compute.v1beta.Addresses.SetLabelsCallback): void;

Calls SetLabels.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsaddressrequest)`   
SetLabelsAddressRequest message or plain object  
`callback` |  `[SetLabelsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setLabels(request)
    
    
    public setLabels(request: google.cloud.compute.v1beta.ISetLabelsAddressRequest): Promise<google.cloud.compute.v1beta.Operation>;

Calls SetLabels.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetLabelsAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.isetlabelsaddressrequest)`   
SetLabelsAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.operation-class)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsAddressRequest, callback: google.cloud.compute.v1beta.Addresses.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsaddressrequest)`   
TestIamPermissionsAddressRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TestPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.cloud.compute.v1beta.ITestIamPermissionsAddressRequest): Promise<google.cloud.compute.v1beta.TestPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsAddressRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.itestiampermissionsaddressrequest)`   
TestIamPermissionsAddressRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1beta.TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.testpermissionsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
