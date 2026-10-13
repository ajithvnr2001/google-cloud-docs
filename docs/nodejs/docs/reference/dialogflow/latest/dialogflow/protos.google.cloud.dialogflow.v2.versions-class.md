---
url: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.versions-class
title: Class protos.google.cloud.dialogflow.v2.Versions (8.2.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:45.823403+00:00
---

# Class protos.google.cloud.dialogflow.v2.Versions (8.2.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.versions-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dialogflow.v2.Versions (8.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

8.2.0 (latest)  8.1.1  7.9.0  7.8.0  7.7.0  7.5.0  7.4.0  7.1.0  7.0.1  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.8.0  6.6.0  6.4.0  6.3.1  6.2.0  6.0.0  5.7.1  5.6.0  5.5.1  5.3.0  5.2.1  4.7.0  4.6.0  4.5.0  4.4.0  4.3.1  4.2.0  4.1.4  3.5.0  3.3.0 

Represents a Versions

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dialogflow.v2.Versions

## Package

[@google-cloud/dialogflow](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)

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
`[Versions](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.versions-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createVersion(request, callback)
    
    
    public createVersion(request: google.cloud.dialogflow.v2.ICreateVersionRequest, callback: google.cloud.dialogflow.v2.Versions.CreateVersionCallback): void;

Calls CreateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateversionrequest)`   
CreateVersionRequest message or plain object  
`callback` |  `[CreateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createVersion(request)
    
    
    public createVersion(request: google.cloud.dialogflow.v2.ICreateVersionRequest): Promise<google.cloud.dialogflow.v2.Version>;

Calls CreateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.icreateversionrequest)`   
CreateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Version](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.version-class)>` | Promise  
  
### deleteVersion(request, callback)
    
    
    public deleteVersion(request: google.cloud.dialogflow.v2.IDeleteVersionRequest, callback: google.cloud.dialogflow.v2.Versions.DeleteVersionCallback): void;

Calls DeleteVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
`callback` |  `[DeleteVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteVersion(request)
    
    
    public deleteVersion(request: google.cloud.dialogflow.v2.IDeleteVersionRequest): Promise<google.protobuf.Empty>;

Calls DeleteVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ideleteversionrequest)`   
DeleteVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.protobuf.empty)>` | Promise  
  
### getVersion(request, callback)
    
    
    public getVersion(request: google.cloud.dialogflow.v2.IGetVersionRequest, callback: google.cloud.dialogflow.v2.Versions.GetVersionCallback): void;

Calls GetVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetversionrequest)`   
GetVersionRequest message or plain object  
`callback` |  `[GetVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getVersion(request)
    
    
    public getVersion(request: google.cloud.dialogflow.v2.IGetVersionRequest): Promise<google.cloud.dialogflow.v2.Version>;

Calls GetVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.igetversionrequest)`   
GetVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Version](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.version-class)>` | Promise  
  
### listVersions(request, callback)
    
    
    public listVersions(request: google.cloud.dialogflow.v2.IListVersionsRequest, callback: google.cloud.dialogflow.v2.Versions.ListVersionsCallback): void;

Calls ListVersions.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
`callback` |  `[ListVersionsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and ListVersionsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listVersions(request)
    
    
    public listVersions(request: google.cloud.dialogflow.v2.IListVersionsRequest): Promise<google.cloud.dialogflow.v2.ListVersionsResponse>;

Calls ListVersions.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListVersionsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.ilistversionsrequest)`   
ListVersionsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.ListVersionsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.listversionsresponse)>` | Promise  
  
### updateVersion(request, callback)
    
    
    public updateVersion(request: google.cloud.dialogflow.v2.IUpdateVersionRequest, callback: google.cloud.dialogflow.v2.Versions.UpdateVersionCallback): void;

Calls UpdateVersion.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdateversionrequest)`   
UpdateVersionRequest message or plain object  
`callback` |  `[UpdateVersionCallback](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/overview.html)`   
Node-style callback called with the error, if any, and Version  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateVersion(request)
    
    
    public updateVersion(request: google.cloud.dialogflow.v2.IUpdateVersionRequest): Promise<google.cloud.dialogflow.v2.Version>;

Calls UpdateVersion.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateVersionRequest](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.iupdateversionrequest)`   
UpdateVersionRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dialogflow.v2.Version](https://docs.cloud.google.com/nodejs/docs/reference/dialogflow/latest/dialogflow/protos.google.cloud.dialogflow.v2.version-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
