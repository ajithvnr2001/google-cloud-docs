---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.versions-class
title: Class protos.google.appengine.v1.Versions (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:45.047059+00:00
---

# Class protos.google.appengine.v1.Versions (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.versions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.Versions (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents a Versions

## Inheritance

$protobuf.rpc.Service > protos.google.appengine.v1.Versions

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Versions service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Versions;

Creates new Versions service using the specified rpc implementation.

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
`[Versions](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.versions-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createVersion(request, callback)
    
    
    public createVersion(request: google.appengine.v1.ICreateVersionRequest, callback: google.appengine.v1.Versions.CreateVersionCallback): void;

Calls CreateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateversionrequest)`   
CreateVersionRequest message or plain object  
`callback` |  `[CreateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createVersion(request)
    
    
    public createVersion(request: google.appengine.v1.ICreateVersionRequest): Promise<google.longrunning.Operation>;

Calls CreateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateversionrequest)`   
CreateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### deleteVersion(request, callback)
    
    
    public deleteVersion(request: google.appengine.v1.IDeleteVersionRequest, callback: google.appengine.v1.Versions.DeleteVersionCallback): void;

Calls DeleteVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
`callback` |  `[DeleteVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteVersion(request)
    
    
    public deleteVersion(request: google.appengine.v1.IDeleteVersionRequest): Promise<google.longrunning.Operation>;

Calls DeleteVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### getVersion(request, callback)
    
    
    public getVersion(request: google.appengine.v1.IGetVersionRequest, callback: google.appengine.v1.Versions.GetVersionCallback): void;

Calls GetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
`callback` |  `[GetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVersion(request)
    
    
    public getVersion(request: google.appengine.v1.IGetVersionRequest): Promise<google.appengine.v1.Version>;

Calls GetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetversionrequest)`   
GetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.Version](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.version)>` | Promise  
  
### listVersions(request, callback)
    
    
    public listVersions(request: google.appengine.v1.IListVersionsRequest, callback: google.appengine.v1.Versions.ListVersionsCallback): void;

Calls ListVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
`callback` |  `[ListVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVersions(request)
    
    
    public listVersions(request: google.appengine.v1.IListVersionsRequest): Promise<google.appengine.v1.ListVersionsResponse>;

Calls ListVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.ListVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.listversionsresponse)>` | Promise  
  
### updateVersion(request, callback)
    
    
    public updateVersion(request: google.appengine.v1.IUpdateVersionRequest, callback: google.appengine.v1.Versions.UpdateVersionCallback): void;

Calls UpdateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateversionrequest)`   
UpdateVersionRequest message or plain object  
`callback` |  `[UpdateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateVersion(request)
    
    
    public updateVersion(request: google.appengine.v1.IUpdateVersionRequest): Promise<google.longrunning.Operation>;

Calls UpdateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateversionrequest)`   
UpdateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
