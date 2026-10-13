---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.services-class
title: Class protos.google.appengine.v1.Services (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:42.069044+00:00
---

# Class protos.google.appengine.v1.Services (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.services-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.Services (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents a Services

## Inheritance

$protobuf.rpc.Service > protos.google.appengine.v1.Services

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Services service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Services;

Creates new Services service using the specified rpc implementation.

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
`[Services](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.services-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteService(request, callback)
    
    
    public deleteService(request: google.appengine.v1.IDeleteServiceRequest, callback: google.appengine.v1.Services.DeleteServiceCallback): void;

Calls DeleteService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteservicerequest)`   
DeleteServiceRequest message or plain object  
`callback` |  `[DeleteServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteService(request)
    
    
    public deleteService(request: google.appengine.v1.IDeleteServiceRequest): Promise<google.longrunning.Operation>;

Calls DeleteService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteservicerequest)`   
DeleteServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### getService(request, callback)
    
    
    public getService(request: google.appengine.v1.IGetServiceRequest, callback: google.appengine.v1.Services.GetServiceCallback): void;

Calls GetService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetservicerequest)`   
GetServiceRequest message or plain object  
`callback` |  `[GetServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Service  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getService(request)
    
    
    public getService(request: google.appengine.v1.IGetServiceRequest): Promise<google.appengine.v1.Service>;

Calls GetService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetservicerequest)`   
GetServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.Service](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.service)>` | Promise  
  
### listServices(request, callback)
    
    
    public listServices(request: google.appengine.v1.IListServicesRequest, callback: google.appengine.v1.Services.ListServicesCallback): void;

Calls ListServices.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistservicesrequest)`   
ListServicesRequest message or plain object  
`callback` |  `[ListServicesCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListServicesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listServices(request)
    
    
    public listServices(request: google.appengine.v1.IListServicesRequest): Promise<google.appengine.v1.ListServicesResponse>;

Calls ListServices.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListServicesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistservicesrequest)`   
ListServicesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.ListServicesResponse](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.listservicesresponse)>` | Promise  
  
### updateService(request, callback)
    
    
    public updateService(request: google.appengine.v1.IUpdateServiceRequest, callback: google.appengine.v1.Services.UpdateServiceCallback): void;

Calls UpdateService.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateservicerequest)`   
UpdateServiceRequest message or plain object  
`callback` |  `[UpdateServiceCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateService(request)
    
    
    public updateService(request: google.appengine.v1.IUpdateServiceRequest): Promise<google.longrunning.Operation>;

Calls UpdateService.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateServiceRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateservicerequest)`   
UpdateServiceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
