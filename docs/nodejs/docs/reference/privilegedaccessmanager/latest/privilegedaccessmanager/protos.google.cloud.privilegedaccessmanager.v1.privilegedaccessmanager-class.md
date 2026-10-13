---
url: https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.privilegedaccessmanager-class
title: Class protos.google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager (0.8.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:13.529615+00:00
---

# Class protos.google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager (0.8.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.privilegedaccessmanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager (0.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.1 (latest)  0.4.0  0.3.1  0.2.0 

Represents a PrivilegedAccessManager

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager

## Package

[@google-cloud/privilegedaccessmanager](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new PrivilegedAccessManager service.

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

### approveGrant(request, callback)
    
    
    public approveGrant(request: google.cloud.privilegedaccessmanager.v1.IApproveGrantRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ApproveGrantCallback): void;

Calls ApproveGrant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApproveGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.iapprovegrantrequest)`   
ApproveGrantRequest message or plain object  
`callback` |  `[ApproveGrantCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Grant  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### approveGrant(request)
    
    
    public approveGrant(request: google.cloud.privilegedaccessmanager.v1.IApproveGrantRequest): Promise<google.cloud.privilegedaccessmanager.v1.Grant>;

Calls ApproveGrant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApproveGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.iapprovegrantrequest)`   
ApproveGrantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.Grant](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.grant-class)>` | Promise  
  
### checkOnboardingStatus(request, callback)
    
    
    public checkOnboardingStatus(request: google.cloud.privilegedaccessmanager.v1.ICheckOnboardingStatusRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CheckOnboardingStatusCallback): void;

Calls CheckOnboardingStatus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckOnboardingStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.icheckonboardingstatusrequest)`   
CheckOnboardingStatusRequest message or plain object  
`callback` |  `[CheckOnboardingStatusCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and CheckOnboardingStatusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### checkOnboardingStatus(request)
    
    
    public checkOnboardingStatus(request: google.cloud.privilegedaccessmanager.v1.ICheckOnboardingStatusRequest): Promise<google.cloud.privilegedaccessmanager.v1.CheckOnboardingStatusResponse>;

Calls CheckOnboardingStatus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICheckOnboardingStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.icheckonboardingstatusrequest)`   
CheckOnboardingStatusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.CheckOnboardingStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.checkonboardingstatusresponse-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): PrivilegedAccessManager;

Creates new PrivilegedAccessManager service using the specified rpc implementation.

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
`[PrivilegedAccessManager](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.privilegedaccessmanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createEntitlement(request, callback)
    
    
    public createEntitlement(request: google.cloud.privilegedaccessmanager.v1.ICreateEntitlementRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateEntitlementCallback): void;

Calls CreateEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.icreateentitlementrequest)`   
CreateEntitlementRequest message or plain object  
`callback` |  `[CreateEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEntitlement(request)
    
    
    public createEntitlement(request: google.cloud.privilegedaccessmanager.v1.ICreateEntitlementRequest): Promise<google.longrunning.Operation>;

Calls CreateEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.icreateentitlementrequest)`   
CreateEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.longrunning.operation)>` | Promise  
  
### createGrant(request, callback)
    
    
    public createGrant(request: google.cloud.privilegedaccessmanager.v1.ICreateGrantRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.CreateGrantCallback): void;

Calls CreateGrant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.icreategrantrequest)`   
CreateGrantRequest message or plain object  
`callback` |  `[CreateGrantCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Grant  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createGrant(request)
    
    
    public createGrant(request: google.cloud.privilegedaccessmanager.v1.ICreateGrantRequest): Promise<google.cloud.privilegedaccessmanager.v1.Grant>;

Calls CreateGrant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.icreategrantrequest)`   
CreateGrantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.Grant](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.grant-class)>` | Promise  
  
### deleteEntitlement(request, callback)
    
    
    public deleteEntitlement(request: google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DeleteEntitlementCallback): void;

Calls DeleteEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)`   
DeleteEntitlementRequest message or plain object  
`callback` |  `[DeleteEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEntitlement(request)
    
    
    public deleteEntitlement(request: google.cloud.privilegedaccessmanager.v1.IDeleteEntitlementRequest): Promise<google.longrunning.Operation>;

Calls DeleteEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ideleteentitlementrequest)`   
DeleteEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.longrunning.operation)>` | Promise  
  
### denyGrant(request, callback)
    
    
    public denyGrant(request: google.cloud.privilegedaccessmanager.v1.IDenyGrantRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.DenyGrantCallback): void;

Calls DenyGrant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDenyGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.idenygrantrequest)`   
DenyGrantRequest message or plain object  
`callback` |  `[DenyGrantCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Grant  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### denyGrant(request)
    
    
    public denyGrant(request: google.cloud.privilegedaccessmanager.v1.IDenyGrantRequest): Promise<google.cloud.privilegedaccessmanager.v1.Grant>;

Calls DenyGrant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDenyGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.idenygrantrequest)`   
DenyGrantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.Grant](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.grant-class)>` | Promise  
  
### getEntitlement(request, callback)
    
    
    public getEntitlement(request: google.cloud.privilegedaccessmanager.v1.IGetEntitlementRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetEntitlementCallback): void;

Calls GetEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.igetentitlementrequest)`   
GetEntitlementRequest message or plain object  
`callback` |  `[GetEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Entitlement  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEntitlement(request)
    
    
    public getEntitlement(request: google.cloud.privilegedaccessmanager.v1.IGetEntitlementRequest): Promise<google.cloud.privilegedaccessmanager.v1.Entitlement>;

Calls GetEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.igetentitlementrequest)`   
GetEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.Entitlement](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.entitlement-class)>` | Promise  
  
### getGrant(request, callback)
    
    
    public getGrant(request: google.cloud.privilegedaccessmanager.v1.IGetGrantRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.GetGrantCallback): void;

Calls GetGrant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.igetgrantrequest)`   
GetGrantRequest message or plain object  
`callback` |  `[GetGrantCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Grant  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getGrant(request)
    
    
    public getGrant(request: google.cloud.privilegedaccessmanager.v1.IGetGrantRequest): Promise<google.cloud.privilegedaccessmanager.v1.Grant>;

Calls GetGrant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.igetgrantrequest)`   
GetGrantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.Grant](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.grant-class)>` | Promise  
  
### listEntitlements(request, callback)
    
    
    public listEntitlements(request: google.cloud.privilegedaccessmanager.v1.IListEntitlementsRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListEntitlementsCallback): void;

Calls ListEntitlements.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ilistentitlementsrequest)`   
ListEntitlementsRequest message or plain object  
`callback` |  `[ListEntitlementsCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEntitlementsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEntitlements(request)
    
    
    public listEntitlements(request: google.cloud.privilegedaccessmanager.v1.IListEntitlementsRequest): Promise<google.cloud.privilegedaccessmanager.v1.ListEntitlementsResponse>;

Calls ListEntitlements.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ilistentitlementsrequest)`   
ListEntitlementsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.ListEntitlementsResponse](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.listentitlementsresponse)>` | Promise  
  
### listGrants(request, callback)
    
    
    public listGrants(request: google.cloud.privilegedaccessmanager.v1.IListGrantsRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.ListGrantsCallback): void;

Calls ListGrants.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListGrantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ilistgrantsrequest)`   
ListGrantsRequest message or plain object  
`callback` |  `[ListGrantsCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListGrantsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listGrants(request)
    
    
    public listGrants(request: google.cloud.privilegedaccessmanager.v1.IListGrantsRequest): Promise<google.cloud.privilegedaccessmanager.v1.ListGrantsResponse>;

Calls ListGrants.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListGrantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.ilistgrantsrequest)`   
ListGrantsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.ListGrantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.listgrantsresponse)>` | Promise  
  
### revokeGrant(request, callback)
    
    
    public revokeGrant(request: google.cloud.privilegedaccessmanager.v1.IRevokeGrantRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.RevokeGrantCallback): void;

Calls RevokeGrant.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRevokeGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.irevokegrantrequest)`   
RevokeGrantRequest message or plain object  
`callback` |  `[RevokeGrantCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### revokeGrant(request)
    
    
    public revokeGrant(request: google.cloud.privilegedaccessmanager.v1.IRevokeGrantRequest): Promise<google.longrunning.Operation>;

Calls RevokeGrant.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRevokeGrantRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.irevokegrantrequest)`   
RevokeGrantRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.longrunning.operation)>` | Promise  
  
### searchEntitlements(request, callback)
    
    
    public searchEntitlements(request: google.cloud.privilegedaccessmanager.v1.ISearchEntitlementsRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.SearchEntitlementsCallback): void;

Calls SearchEntitlements.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.isearchentitlementsrequest)`   
SearchEntitlementsRequest message or plain object  
`callback` |  `[SearchEntitlementsCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchEntitlementsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchEntitlements(request)
    
    
    public searchEntitlements(request: google.cloud.privilegedaccessmanager.v1.ISearchEntitlementsRequest): Promise<google.cloud.privilegedaccessmanager.v1.SearchEntitlementsResponse>;

Calls SearchEntitlements.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchEntitlementsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.isearchentitlementsrequest)`   
SearchEntitlementsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.SearchEntitlementsResponse](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.searchentitlementsresponse)>` | Promise  
  
### searchGrants(request, callback)
    
    
    public searchGrants(request: google.cloud.privilegedaccessmanager.v1.ISearchGrantsRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.SearchGrantsCallback): void;

Calls SearchGrants.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchGrantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.isearchgrantsrequest)`   
SearchGrantsRequest message or plain object  
`callback` |  `[SearchGrantsCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchGrantsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchGrants(request)
    
    
    public searchGrants(request: google.cloud.privilegedaccessmanager.v1.ISearchGrantsRequest): Promise<google.cloud.privilegedaccessmanager.v1.SearchGrantsResponse>;

Calls SearchGrants.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchGrantsRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.isearchgrantsrequest)`   
SearchGrantsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.privilegedaccessmanager.v1.SearchGrantsResponse](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.searchgrantsresponse)>` | Promise  
  
### updateEntitlement(request, callback)
    
    
    public updateEntitlement(request: google.cloud.privilegedaccessmanager.v1.IUpdateEntitlementRequest, callback: google.cloud.privilegedaccessmanager.v1.PrivilegedAccessManager.UpdateEntitlementCallback): void;

Calls UpdateEntitlement.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.iupdateentitlementrequest)`   
UpdateEntitlementRequest message or plain object  
`callback` |  `[UpdateEntitlementCallback](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEntitlement(request)
    
    
    public updateEntitlement(request: google.cloud.privilegedaccessmanager.v1.IUpdateEntitlementRequest): Promise<google.longrunning.Operation>;

Calls UpdateEntitlement.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEntitlementRequest](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.cloud.privilegedaccessmanager.v1.iupdateentitlementrequest)`   
UpdateEntitlementRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/privilegedaccessmanager/latest/privilegedaccessmanager/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
