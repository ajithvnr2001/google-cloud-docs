---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.reservations-class
title: Class protos.google.cloud.compute.v1.Reservations (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:43.521453+00:00
---

# Class protos.google.cloud.compute.v1.Reservations (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.reservations-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.compute.v1.Reservations (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Represents a Reservations

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.compute.v1.Reservations

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Reservations service.

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
    
    
    public aggregatedList(request: google.cloud.compute.v1.IAggregatedListReservationsRequest, callback: google.cloud.compute.v1.Reservations.AggregatedListCallback): void;

Calls AggregatedList.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iaggregatedlistreservationsrequest)`   
AggregatedListReservationsRequest message or plain object  
`callback` |  `[AggregatedListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and ReservationAggregatedList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### aggregatedList(request)
    
    
    public aggregatedList(request: google.cloud.compute.v1.IAggregatedListReservationsRequest): Promise<google.cloud.compute.v1.ReservationAggregatedList>;

Calls AggregatedList.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IAggregatedListReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iaggregatedlistreservationsrequest)`   
AggregatedListReservationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.ReservationAggregatedList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.reservationaggregatedlist)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Reservations;

Creates new Reservations service using the specified rpc implementation.

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
`[Reservations](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.reservations-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### delete(request, callback)
    
    
    public delete(request: google.cloud.compute.v1.IDeleteReservationRequest, callback: google.cloud.compute.v1.Reservations.DeleteCallback): void;

Calls Delete.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletereservationrequest)`   
DeleteReservationRequest message or plain object  
`callback` |  `[DeleteCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### delete(request)
    
    
    public delete(request: google.cloud.compute.v1.IDeleteReservationRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Delete.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ideletereservationrequest)`   
DeleteReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### get(request, callback)
    
    
    public get(request: google.cloud.compute.v1.IGetReservationRequest, callback: google.cloud.compute.v1.Reservations.GetCallback): void;

Calls Get.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetreservationrequest)`   
GetReservationRequest message or plain object  
`callback` |  `[GetCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Reservation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### get(request)
    
    
    public get(request: google.cloud.compute.v1.IGetReservationRequest): Promise<google.cloud.compute.v1.Reservation>;

Calls Get.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetreservationrequest)`   
GetReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Reservation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.reservation-class)>` | Promise  
  
### getIamPolicy(request, callback)
    
    
    public getIamPolicy(request: google.cloud.compute.v1.IGetIamPolicyReservationRequest, callback: google.cloud.compute.v1.Reservations.GetIamPolicyCallback): void;

Calls GetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetiampolicyreservationrequest)`   
GetIamPolicyReservationRequest message or plain object  
`callback` |  `[GetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIamPolicy(request)
    
    
    public getIamPolicy(request: google.cloud.compute.v1.IGetIamPolicyReservationRequest): Promise<google.cloud.compute.v1.Policy>;

Calls GetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIamPolicyReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.igetiampolicyreservationrequest)`   
GetIamPolicyReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.policy)>` | Promise  
  
### insert(request, callback)
    
    
    public insert(request: google.cloud.compute.v1.IInsertReservationRequest, callback: google.cloud.compute.v1.Reservations.InsertCallback): void;

Calls Insert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInsertReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinsertreservationrequest)`   
InsertReservationRequest message or plain object  
`callback` |  `[InsertCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### insert(request)
    
    
    public insert(request: google.cloud.compute.v1.IInsertReservationRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Insert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInsertReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinsertreservationrequest)`   
InsertReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### list(request, callback)
    
    
    public list(request: google.cloud.compute.v1.IListReservationsRequest, callback: google.cloud.compute.v1.Reservations.ListCallback): void;

Calls List.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ilistreservationsrequest)`   
ListReservationsRequest message or plain object  
`callback` |  `[ListCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and ReservationList  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### list(request)
    
    
    public list(request: google.cloud.compute.v1.IListReservationsRequest): Promise<google.cloud.compute.v1.ReservationList>;

Calls List.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReservationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ilistreservationsrequest)`   
ListReservationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.ReservationList](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.reservationlist)>` | Promise  
  
### performMaintenance(request, callback)
    
    
    public performMaintenance(request: google.cloud.compute.v1.IPerformMaintenanceReservationRequest, callback: google.cloud.compute.v1.Reservations.PerformMaintenanceCallback): void;

Calls PerformMaintenance.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IPerformMaintenanceReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iperformmaintenancereservationrequest)`   
PerformMaintenanceReservationRequest message or plain object  
`callback` |  `[PerformMaintenanceCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### performMaintenance(request)
    
    
    public performMaintenance(request: google.cloud.compute.v1.IPerformMaintenanceReservationRequest): Promise<google.cloud.compute.v1.Operation>;

Calls PerformMaintenance.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IPerformMaintenanceReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iperformmaintenancereservationrequest)`   
PerformMaintenanceReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### resize(request, callback)
    
    
    public resize(request: google.cloud.compute.v1.IResizeReservationRequest, callback: google.cloud.compute.v1.Reservations.ResizeCallback): void;

Calls Resize.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IResizeReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iresizereservationrequest)`   
ResizeReservationRequest message or plain object  
`callback` |  `[ResizeCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### resize(request)
    
    
    public resize(request: google.cloud.compute.v1.IResizeReservationRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Resize.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IResizeReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iresizereservationrequest)`   
ResizeReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
### setIamPolicy(request, callback)
    
    
    public setIamPolicy(request: google.cloud.compute.v1.ISetIamPolicyReservationRequest, callback: google.cloud.compute.v1.Reservations.SetIamPolicyCallback): void;

Calls SetIamPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isetiampolicyreservationrequest)`   
SetIamPolicyReservationRequest message or plain object  
`callback` |  `[SetIamPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Policy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### setIamPolicy(request)
    
    
    public setIamPolicy(request: google.cloud.compute.v1.ISetIamPolicyReservationRequest): Promise<google.cloud.compute.v1.Policy>;

Calls SetIamPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISetIamPolicyReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.isetiampolicyreservationrequest)`   
SetIamPolicyReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Policy](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.policy)>` | Promise  
  
### testIamPermissions(request, callback)
    
    
    public testIamPermissions(request: google.cloud.compute.v1.ITestIamPermissionsReservationRequest, callback: google.cloud.compute.v1.Reservations.TestIamPermissionsCallback): void;

Calls TestIamPermissions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.itestiampermissionsreservationrequest)`   
TestIamPermissionsReservationRequest message or plain object  
`callback` |  `[TestIamPermissionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and TestPermissionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### testIamPermissions(request)
    
    
    public testIamPermissions(request: google.cloud.compute.v1.ITestIamPermissionsReservationRequest): Promise<google.cloud.compute.v1.TestPermissionsResponse>;

Calls TestIamPermissions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ITestIamPermissionsReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.itestiampermissionsreservationrequest)`   
TestIamPermissionsReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.TestPermissionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.testpermissionsresponse)>` | Promise  
  
### update(request, callback)
    
    
    public update(request: google.cloud.compute.v1.IUpdateReservationRequest, callback: google.cloud.compute.v1.Reservations.UpdateCallback): void;

Calls Update.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iupdatereservationrequest)`   
UpdateReservationRequest message or plain object  
`callback` |  `[UpdateCallback](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### update(request)
    
    
    public update(request: google.cloud.compute.v1.IUpdateReservationRequest): Promise<google.cloud.compute.v1.Operation>;

Calls Update.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateReservationRequest](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iupdatereservationrequest)`   
UpdateReservationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.compute.v1.Operation](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.operation-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
