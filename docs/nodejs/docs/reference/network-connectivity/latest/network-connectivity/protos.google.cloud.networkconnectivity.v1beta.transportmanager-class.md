---
url: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.transportmanager-class
title: Class protos.google.cloud.networkconnectivity.v1beta.TransportManager (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:05.473400+00:00
---

# Class protos.google.cloud.networkconnectivity.v1beta.TransportManager (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.transportmanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.networkconnectivity.v1beta.TransportManager (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.6.0  4.2.0  3.6.0  3.2.0  2.3.3  2.2.0  2.1.2  1.5.0  1.4.2  1.3.0  1.2.1  1.1.6 

Represents a TransportManager

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.networkconnectivity.v1beta.TransportManager

## Package

[@google-cloud/network-connectivity](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new TransportManager service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): TransportManager;

Creates new TransportManager service using the specified rpc implementation.

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
`[TransportManager](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.transportmanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createTransport(request, callback)
    
    
    public createTransport(request: google.cloud.networkconnectivity.v1beta.ICreateTransportRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.CreateTransportCallback): void;

Calls CreateTransport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatetransportrequest)`   
CreateTransportRequest message or plain object  
`callback` |  `[CreateTransportCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createTransport(request)
    
    
    public createTransport(request: google.cloud.networkconnectivity.v1beta.ICreateTransportRequest): Promise<google.longrunning.Operation>;

Calls CreateTransport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.icreatetransportrequest)`   
CreateTransportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### deleteTransport(request, callback)
    
    
    public deleteTransport(request: google.cloud.networkconnectivity.v1beta.IDeleteTransportRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.DeleteTransportCallback): void;

Calls DeleteTransport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletetransportrequest)`   
DeleteTransportRequest message or plain object  
`callback` |  `[DeleteTransportCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteTransport(request)
    
    
    public deleteTransport(request: google.cloud.networkconnectivity.v1beta.IDeleteTransportRequest): Promise<google.longrunning.Operation>;

Calls DeleteTransport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ideletetransportrequest)`   
DeleteTransportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
### getRemoteTransportProfile(request, callback)
    
    
    public getRemoteTransportProfile(request: google.cloud.networkconnectivity.v1beta.IGetRemoteTransportProfileRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.GetRemoteTransportProfileCallback): void;

Calls GetRemoteTransportProfile.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetRemoteTransportProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetremotetransportprofilerequest)`   
GetRemoteTransportProfileRequest message or plain object  
`callback` |  `[GetRemoteTransportProfileCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and RemoteTransportProfile  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getRemoteTransportProfile(request)
    
    
    public getRemoteTransportProfile(request: google.cloud.networkconnectivity.v1beta.IGetRemoteTransportProfileRequest): Promise<google.cloud.networkconnectivity.v1beta.RemoteTransportProfile>;

Calls GetRemoteTransportProfile.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetRemoteTransportProfileRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetremotetransportprofilerequest)`   
GetRemoteTransportProfileRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1beta.RemoteTransportProfile](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.remotetransportprofile-class)>` | Promise  
  
### getStatus(request, callback)
    
    
    public getStatus(request: google.cloud.networkconnectivity.v1beta.IGetStatusRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.GetStatusCallback): void;

Calls GetStatus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetstatusrequest)`   
GetStatusRequest message or plain object  
`callback` |  `[GetStatusCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and GetStatusResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getStatus(request)
    
    
    public getStatus(request: google.cloud.networkconnectivity.v1beta.IGetStatusRequest): Promise<google.cloud.networkconnectivity.v1beta.GetStatusResponse>;

Calls GetStatus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igetstatusrequest)`   
GetStatusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1beta.GetStatusResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.getstatusresponse-class)>` | Promise  
  
### getTransport(request, callback)
    
    
    public getTransport(request: google.cloud.networkconnectivity.v1beta.IGetTransportRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.GetTransportCallback): void;

Calls GetTransport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igettransportrequest)`   
GetTransportRequest message or plain object  
`callback` |  `[GetTransportCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Transport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getTransport(request)
    
    
    public getTransport(request: google.cloud.networkconnectivity.v1beta.IGetTransportRequest): Promise<google.cloud.networkconnectivity.v1beta.Transport>;

Calls GetTransport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.igettransportrequest)`   
GetTransportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1beta.Transport](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.transport-class)>` | Promise  
  
### listRemoteTransportProfiles(request, callback)
    
    
    public listRemoteTransportProfiles(request: google.cloud.networkconnectivity.v1beta.IListRemoteTransportProfilesRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.ListRemoteTransportProfilesCallback): void;

Calls ListRemoteTransportProfiles.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListRemoteTransportProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistremotetransportprofilesrequest)`   
ListRemoteTransportProfilesRequest message or plain object  
`callback` |  `[ListRemoteTransportProfilesCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListRemoteTransportProfilesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listRemoteTransportProfiles(request)
    
    
    public listRemoteTransportProfiles(request: google.cloud.networkconnectivity.v1beta.IListRemoteTransportProfilesRequest): Promise<google.cloud.networkconnectivity.v1beta.ListRemoteTransportProfilesResponse>;

Calls ListRemoteTransportProfiles.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListRemoteTransportProfilesRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilistremotetransportprofilesrequest)`   
ListRemoteTransportProfilesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1beta.ListRemoteTransportProfilesResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.listremotetransportprofilesresponse)>` | Promise  
  
### listTransports(request, callback)
    
    
    public listTransports(request: google.cloud.networkconnectivity.v1beta.IListTransportsRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.ListTransportsCallback): void;

Calls ListTransports.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListTransportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilisttransportsrequest)`   
ListTransportsRequest message or plain object  
`callback` |  `[ListTransportsCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ListTransportsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listTransports(request)
    
    
    public listTransports(request: google.cloud.networkconnectivity.v1beta.IListTransportsRequest): Promise<google.cloud.networkconnectivity.v1beta.ListTransportsResponse>;

Calls ListTransports.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListTransportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.ilisttransportsrequest)`   
ListTransportsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1beta.ListTransportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.listtransportsresponse)>` | Promise  
  
### parseFromActivationKey(request, callback)
    
    
    public parseFromActivationKey(request: google.cloud.networkconnectivity.v1beta.IParseFromActivationKeyRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.ParseFromActivationKeyCallback): void;

Calls ParseFromActivationKey.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IParseFromActivationKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iparsefromactivationkeyrequest)`   
ParseFromActivationKeyRequest message or plain object  
`callback` |  `[ParseFromActivationKeyCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and ParseFromActivationKeyResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### parseFromActivationKey(request)
    
    
    public parseFromActivationKey(request: google.cloud.networkconnectivity.v1beta.IParseFromActivationKeyRequest): Promise<google.cloud.networkconnectivity.v1beta.ParseFromActivationKeyResponse>;

Calls ParseFromActivationKey.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IParseFromActivationKeyRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iparsefromactivationkeyrequest)`   
ParseFromActivationKeyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.networkconnectivity.v1beta.ParseFromActivationKeyResponse](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.parsefromactivationkeyresponse)>` | Promise  
  
### updateTransport(request, callback)
    
    
    public updateTransport(request: google.cloud.networkconnectivity.v1beta.IUpdateTransportRequest, callback: google.cloud.networkconnectivity.v1beta.TransportManager.UpdateTransportCallback): void;

Calls UpdateTransport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatetransportrequest)`   
UpdateTransportRequest message or plain object  
`callback` |  `[UpdateTransportCallback](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateTransport(request)
    
    
    public updateTransport(request: google.cloud.networkconnectivity.v1beta.IUpdateTransportRequest): Promise<google.longrunning.Operation>;

Calls UpdateTransport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateTransportRequest](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.cloud.networkconnectivity.v1beta.iupdatetransportrequest)`   
UpdateTransportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/network-connectivity/latest/network-connectivity/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
