---
url: https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.accessapproval-class
title: Class protos.google.cloud.accessapproval.v1.AccessApproval (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:36.890774+00:00
---

# Class protos.google.cloud.accessapproval.v1.AccessApproval (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.accessapproval-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.accessapproval.v1.AccessApproval (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  3.2.0  2.2.2  2.1.2  1.1.0  1.0.8 

Represents an AccessApproval

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.accessapproval.v1.AccessApproval

## Package

[@google-cloud/access-approval](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AccessApproval service.

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

### approveApprovalRequest(request, callback)
    
    
    public approveApprovalRequest(request: google.cloud.accessapproval.v1.IApproveApprovalRequestMessage, callback: google.cloud.accessapproval.v1.AccessApproval.ApproveApprovalRequestCallback): void;

Calls ApproveApprovalRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IApproveApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.iapproveapprovalrequestmessage)`   
ApproveApprovalRequestMessage message or plain object  
`callback` |  `[ApproveApprovalRequestCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and ApprovalRequest  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### approveApprovalRequest(request)
    
    
    public approveApprovalRequest(request: google.cloud.accessapproval.v1.IApproveApprovalRequestMessage): Promise<google.cloud.accessapproval.v1.ApprovalRequest>;

Calls ApproveApprovalRequest.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IApproveApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.iapproveapprovalrequestmessage)`   
ApproveApprovalRequestMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.ApprovalRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.approvalrequest)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AccessApproval;

Creates new AccessApproval service using the specified rpc implementation.

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
`[AccessApproval](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.accessapproval-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteAccessApprovalSettings(request, callback)
    
    
    public deleteAccessApprovalSettings(request: google.cloud.accessapproval.v1.IDeleteAccessApprovalSettingsMessage, callback: google.cloud.accessapproval.v1.AccessApproval.DeleteAccessApprovalSettingsCallback): void;

Calls DeleteAccessApprovalSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.ideleteaccessapprovalsettingsmessage)`   
DeleteAccessApprovalSettingsMessage message or plain object  
`callback` |  `[DeleteAccessApprovalSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAccessApprovalSettings(request)
    
    
    public deleteAccessApprovalSettings(request: google.cloud.accessapproval.v1.IDeleteAccessApprovalSettingsMessage): Promise<google.protobuf.Empty>;

Calls DeleteAccessApprovalSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAccessApprovalSettingsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.ideleteaccessapprovalsettingsmessage)`   
DeleteAccessApprovalSettingsMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.protobuf.empty)>` | Promise  
  
### dismissApprovalRequest(request, callback)
    
    
    public dismissApprovalRequest(request: google.cloud.accessapproval.v1.IDismissApprovalRequestMessage, callback: google.cloud.accessapproval.v1.AccessApproval.DismissApprovalRequestCallback): void;

Calls DismissApprovalRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDismissApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.idismissapprovalrequestmessage)`   
DismissApprovalRequestMessage message or plain object  
`callback` |  `[DismissApprovalRequestCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and ApprovalRequest  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### dismissApprovalRequest(request)
    
    
    public dismissApprovalRequest(request: google.cloud.accessapproval.v1.IDismissApprovalRequestMessage): Promise<google.cloud.accessapproval.v1.ApprovalRequest>;

Calls DismissApprovalRequest.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDismissApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.idismissapprovalrequestmessage)`   
DismissApprovalRequestMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.ApprovalRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.approvalrequest)>` | Promise  
  
### getAccessApprovalServiceAccount(request, callback)
    
    
    public getAccessApprovalServiceAccount(request: google.cloud.accessapproval.v1.IGetAccessApprovalServiceAccountMessage, callback: google.cloud.accessapproval.v1.AccessApproval.GetAccessApprovalServiceAccountCallback): void;

Calls GetAccessApprovalServiceAccount.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.igetaccessapprovalserviceaccountmessage)`   
GetAccessApprovalServiceAccountMessage message or plain object  
`callback` |  `[GetAccessApprovalServiceAccountCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessApprovalServiceAccount  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccessApprovalServiceAccount(request)
    
    
    public getAccessApprovalServiceAccount(request: google.cloud.accessapproval.v1.IGetAccessApprovalServiceAccountMessage): Promise<google.cloud.accessapproval.v1.AccessApprovalServiceAccount>;

Calls GetAccessApprovalServiceAccount.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessApprovalServiceAccountMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.igetaccessapprovalserviceaccountmessage)`   
GetAccessApprovalServiceAccountMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.AccessApprovalServiceAccount](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.accessapprovalserviceaccount)>` | Promise  
  
### getAccessApprovalSettings(request, callback)
    
    
    public getAccessApprovalSettings(request: google.cloud.accessapproval.v1.IGetAccessApprovalSettingsMessage, callback: google.cloud.accessapproval.v1.AccessApproval.GetAccessApprovalSettingsCallback): void;

Calls GetAccessApprovalSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessApprovalSettingsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.igetaccessapprovalsettingsmessage)`   
GetAccessApprovalSettingsMessage message or plain object  
`callback` |  `[GetAccessApprovalSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessApprovalSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAccessApprovalSettings(request)
    
    
    public getAccessApprovalSettings(request: google.cloud.accessapproval.v1.IGetAccessApprovalSettingsMessage): Promise<google.cloud.accessapproval.v1.AccessApprovalSettings>;

Calls GetAccessApprovalSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAccessApprovalSettingsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.igetaccessapprovalsettingsmessage)`   
GetAccessApprovalSettingsMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.AccessApprovalSettings](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.accessapprovalsettings)>` | Promise  
  
### getApprovalRequest(request, callback)
    
    
    public getApprovalRequest(request: google.cloud.accessapproval.v1.IGetApprovalRequestMessage, callback: google.cloud.accessapproval.v1.AccessApproval.GetApprovalRequestCallback): void;

Calls GetApprovalRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.igetapprovalrequestmessage)`   
GetApprovalRequestMessage message or plain object  
`callback` |  `[GetApprovalRequestCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and ApprovalRequest  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApprovalRequest(request)
    
    
    public getApprovalRequest(request: google.cloud.accessapproval.v1.IGetApprovalRequestMessage): Promise<google.cloud.accessapproval.v1.ApprovalRequest>;

Calls GetApprovalRequest.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.igetapprovalrequestmessage)`   
GetApprovalRequestMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.ApprovalRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.approvalrequest)>` | Promise  
  
### invalidateApprovalRequest(request, callback)
    
    
    public invalidateApprovalRequest(request: google.cloud.accessapproval.v1.IInvalidateApprovalRequestMessage, callback: google.cloud.accessapproval.v1.AccessApproval.InvalidateApprovalRequestCallback): void;

Calls InvalidateApprovalRequest.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IInvalidateApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.iinvalidateapprovalrequestmessage)`   
InvalidateApprovalRequestMessage message or plain object  
`callback` |  `[InvalidateApprovalRequestCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and ApprovalRequest  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### invalidateApprovalRequest(request)
    
    
    public invalidateApprovalRequest(request: google.cloud.accessapproval.v1.IInvalidateApprovalRequestMessage): Promise<google.cloud.accessapproval.v1.ApprovalRequest>;

Calls InvalidateApprovalRequest.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IInvalidateApprovalRequestMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.iinvalidateapprovalrequestmessage)`   
InvalidateApprovalRequestMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.ApprovalRequest](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.approvalrequest)>` | Promise  
  
### listApprovalRequests(request, callback)
    
    
    public listApprovalRequests(request: google.cloud.accessapproval.v1.IListApprovalRequestsMessage, callback: google.cloud.accessapproval.v1.AccessApproval.ListApprovalRequestsCallback): void;

Calls ListApprovalRequests.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListApprovalRequestsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.ilistapprovalrequestsmessage)`   
ListApprovalRequestsMessage message or plain object  
`callback` |  `[ListApprovalRequestsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and ListApprovalRequestsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listApprovalRequests(request)
    
    
    public listApprovalRequests(request: google.cloud.accessapproval.v1.IListApprovalRequestsMessage): Promise<google.cloud.accessapproval.v1.ListApprovalRequestsResponse>;

Calls ListApprovalRequests.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListApprovalRequestsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.ilistapprovalrequestsmessage)`   
ListApprovalRequestsMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.ListApprovalRequestsResponse](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.listapprovalrequestsresponse)>` | Promise  
  
### updateAccessApprovalSettings(request, callback)
    
    
    public updateAccessApprovalSettings(request: google.cloud.accessapproval.v1.IUpdateAccessApprovalSettingsMessage, callback: google.cloud.accessapproval.v1.AccessApproval.UpdateAccessApprovalSettingsCallback): void;

Calls UpdateAccessApprovalSettings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.iupdateaccessapprovalsettingsmessage)`   
UpdateAccessApprovalSettingsMessage message or plain object  
`callback` |  `[UpdateAccessApprovalSettingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/overview.html)`   
Node-style callback called with the error, if any, and AccessApprovalSettings  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAccessApprovalSettings(request)
    
    
    public updateAccessApprovalSettings(request: google.cloud.accessapproval.v1.IUpdateAccessApprovalSettingsMessage): Promise<google.cloud.accessapproval.v1.AccessApprovalSettings>;

Calls UpdateAccessApprovalSettings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAccessApprovalSettingsMessage](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.iupdateaccessapprovalsettingsmessage)`   
UpdateAccessApprovalSettingsMessage message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.accessapproval.v1.AccessApprovalSettings](https://docs.cloud.google.com/nodejs/docs/reference/access-approval/latest/access-approval/protos.google.cloud.accessapproval.v1.accessapprovalsettings)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
