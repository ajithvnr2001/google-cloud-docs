---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.applications-class
title: Class protos.google.appengine.v1.Applications (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:29.079206+00:00
---

# Class protos.google.appengine.v1.Applications (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.applications-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.Applications (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents an Applications

## Inheritance

$protobuf.rpc.Service > protos.google.appengine.v1.Applications

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Applications service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Applications;

Creates new Applications service using the specified rpc implementation.

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
`[Applications](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.applications-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createApplication(request, callback)
    
    
    public createApplication(request: google.appengine.v1.ICreateApplicationRequest, callback: google.appengine.v1.Applications.CreateApplicationCallback): void;

Calls CreateApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateapplicationrequest)`   
CreateApplicationRequest message or plain object  
`callback` |  `[CreateApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createApplication(request)
    
    
    public createApplication(request: google.appengine.v1.ICreateApplicationRequest): Promise<google.longrunning.Operation>;

Calls CreateApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateapplicationrequest)`   
CreateApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### getApplication(request, callback)
    
    
    public getApplication(request: google.appengine.v1.IGetApplicationRequest, callback: google.appengine.v1.Applications.GetApplicationCallback): void;

Calls GetApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetapplicationrequest)`   
GetApplicationRequest message or plain object  
`callback` |  `[GetApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Application  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getApplication(request)
    
    
    public getApplication(request: google.appengine.v1.IGetApplicationRequest): Promise<google.appengine.v1.Application>;

Calls GetApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetapplicationrequest)`   
GetApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.Application](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.application-class)>` | Promise  
  
### repairApplication(request, callback)
    
    
    public repairApplication(request: google.appengine.v1.IRepairApplicationRequest, callback: google.appengine.v1.Applications.RepairApplicationCallback): void;

Calls RepairApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRepairApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.irepairapplicationrequest)`   
RepairApplicationRequest message or plain object  
`callback` |  `[RepairApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### repairApplication(request)
    
    
    public repairApplication(request: google.appengine.v1.IRepairApplicationRequest): Promise<google.longrunning.Operation>;

Calls RepairApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRepairApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.irepairapplicationrequest)`   
RepairApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### updateApplication(request, callback)
    
    
    public updateApplication(request: google.appengine.v1.IUpdateApplicationRequest, callback: google.appengine.v1.Applications.UpdateApplicationCallback): void;

Calls UpdateApplication.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateapplicationrequest)`   
UpdateApplicationRequest message or plain object  
`callback` |  `[UpdateApplicationCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateApplication(request)
    
    
    public updateApplication(request: google.appengine.v1.IUpdateApplicationRequest): Promise<google.longrunning.Operation>;

Calls UpdateApplication.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateApplicationRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateapplicationrequest)`   
UpdateApplicationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
