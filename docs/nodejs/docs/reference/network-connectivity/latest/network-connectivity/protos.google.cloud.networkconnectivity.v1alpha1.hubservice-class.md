---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hubservice-class
title: Class protos.google.cloud.networkconnectivity.v1alpha1.HubService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:28.619440+00:00
---

# Class protos.google.cloud.networkconnectivity.v1alpha1.HubService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hubservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1alpha1.HubService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a HubService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.networkconnectivity.v1alpha1.HubService

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new HubService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): HubService;

Creates new HubService service using the specified rpc implementation.

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
`[HubService](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hubservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createHub(request, callback)
    
    
    public createHub(request: google.cloud.networkconnectivity.v1alpha1.ICreateHubRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.CreateHubCallback): void;

Calls CreateHub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatehubrequest)`   
CreateHubRequest message or plain object  
`callback` |  `[CreateHubCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createHub(request)
    
    
    public createHub(request: google.cloud.networkconnectivity.v1alpha1.ICreateHubRequest): Promise<google.longrunning.Operation>;

Calls CreateHub.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatehubrequest)`   
CreateHubRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### createSpoke(request, callback)
    
    
    public createSpoke(request: google.cloud.networkconnectivity.v1alpha1.ICreateSpokeRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.CreateSpokeCallback): void;

Calls CreateSpoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatespokerequest)`   
CreateSpokeRequest message or plain object  
`callback` |  `[CreateSpokeCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSpoke(request)
    
    
    public createSpoke(request: google.cloud.networkconnectivity.v1alpha1.ICreateSpokeRequest): Promise<google.longrunning.Operation>;

Calls CreateSpoke.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.icreatespokerequest)`   
CreateSpokeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteHub(request, callback)
    
    
    public deleteHub(request: google.cloud.networkconnectivity.v1alpha1.IDeleteHubRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.DeleteHubCallback): void;

Calls DeleteHub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletehubrequest)`   
DeleteHubRequest message or plain object  
`callback` |  `[DeleteHubCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteHub(request)
    
    
    public deleteHub(request: google.cloud.networkconnectivity.v1alpha1.IDeleteHubRequest): Promise<google.longrunning.Operation>;

Calls DeleteHub.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletehubrequest)`   
DeleteHubRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteSpoke(request, callback)
    
    
    public deleteSpoke(request: google.cloud.networkconnectivity.v1alpha1.IDeleteSpokeRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.DeleteSpokeCallback): void;

Calls DeleteSpoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletespokerequest)`   
DeleteSpokeRequest message or plain object  
`callback` |  `[DeleteSpokeCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSpoke(request)
    
    
    public deleteSpoke(request: google.cloud.networkconnectivity.v1alpha1.IDeleteSpokeRequest): Promise<google.longrunning.Operation>;

Calls DeleteSpoke.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ideletespokerequest)`   
DeleteSpokeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### getHub(request, callback)
    
    
    public getHub(request: google.cloud.networkconnectivity.v1alpha1.IGetHubRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.GetHubCallback): void;

Calls GetHub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest)`   
GetHubRequest message or plain object  
`callback` |  `[GetHubCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Hub  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getHub(request)
    
    
    public getHub(request: google.cloud.networkconnectivity.v1alpha1.IGetHubRequest): Promise<google.cloud.networkconnectivity.v1alpha1.Hub>;

Calls GetHub.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igethubrequest)`   
GetHubRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1alpha1.Hub](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.hub)>` | Promise  
  
### getSpoke(request, callback)
    
    
    public getSpoke(request: google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.GetSpokeCallback): void;

Calls GetSpoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest)`   
GetSpokeRequest message or plain object  
`callback` |  `[GetSpokeCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Spoke  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSpoke(request)
    
    
    public getSpoke(request: google.cloud.networkconnectivity.v1alpha1.IGetSpokeRequest): Promise<google.cloud.networkconnectivity.v1alpha1.Spoke>;

Calls GetSpoke.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.igetspokerequest)`   
GetSpokeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1alpha1.Spoke](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.spoke)>` | Promise  
  
### listHubs(request, callback)
    
    
    public listHubs(request: google.cloud.networkconnectivity.v1alpha1.IListHubsRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.ListHubsCallback): void;

Calls ListHubs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
ListHubsRequest message or plain object  
`callback` |  `[ListHubsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListHubsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listHubs(request)
    
    
    public listHubs(request: google.cloud.networkconnectivity.v1alpha1.IListHubsRequest): Promise<google.cloud.networkconnectivity.v1alpha1.ListHubsResponse>;

Calls ListHubs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListHubsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilisthubsrequest)`   
ListHubsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1alpha1.ListHubsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.listhubsresponse)>` | Promise  
  
### listSpokes(request, callback)
    
    
    public listSpokes(request: google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.ListSpokesCallback): void;

Calls ListSpokes.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
ListSpokesRequest message or plain object  
`callback` |  `[ListSpokesCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSpokesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSpokes(request)
    
    
    public listSpokes(request: google.cloud.networkconnectivity.v1alpha1.IListSpokesRequest): Promise<google.cloud.networkconnectivity.v1alpha1.ListSpokesResponse>;

Calls ListSpokes.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSpokesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.ilistspokesrequest)`   
ListSpokesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1alpha1.ListSpokesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.listspokesresponse)>` | Promise  
  
### updateHub(request, callback)
    
    
    public updateHub(request: google.cloud.networkconnectivity.v1alpha1.IUpdateHubRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.UpdateHubCallback): void;

Calls UpdateHub.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatehubrequest)`   
UpdateHubRequest message or plain object  
`callback` |  `[UpdateHubCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateHub(request)
    
    
    public updateHub(request: google.cloud.networkconnectivity.v1alpha1.IUpdateHubRequest): Promise<google.longrunning.Operation>;

Calls UpdateHub.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateHubRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatehubrequest)`   
UpdateHubRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### updateSpoke(request, callback)
    
    
    public updateSpoke(request: google.cloud.networkconnectivity.v1alpha1.IUpdateSpokeRequest, callback: google.cloud.networkconnectivity.v1alpha1.HubService.UpdateSpokeCallback): void;

Calls UpdateSpoke.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatespokerequest)`   
UpdateSpokeRequest message or plain object  
`callback` |  `[UpdateSpokeCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSpoke(request)
    
    
    public updateSpoke(request: google.cloud.networkconnectivity.v1alpha1.IUpdateSpokeRequest): Promise<google.longrunning.Operation>;

Calls UpdateSpoke.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSpokeRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1alpha1.iupdatespokerequest)`   
UpdateSpokeRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
