---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.cmekservice-class
title: Class protos.google.cloud.dataplex.v1.CmekService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:33:26.042319+00:00
---

# Class protos.google.cloud.dataplex.v1.CmekService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.cmekservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataplex.v1.CmekService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.5.0  5.4.0  5.3.0  3.13.0  3.12.0  3.11.0  3.10.0  3.8.0  3.7.0  3.5.1  3.2.0  3.1.0  2.4.0  2.3.2  2.2.2  2.1.1  1.2.0  1.1.0  1.0.0 

Represents a CmekService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataplex.v1.CmekService

## Package

[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CmekService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CmekService;

Creates new CmekService service using the specified rpc implementation.

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
`[CmekService](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.cmekservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createEncryptionConfig(request, callback)
    
    
    public createEncryptionConfig(request: google.cloud.dataplex.v1.ICreateEncryptionConfigRequest, callback: google.cloud.dataplex.v1.CmekService.CreateEncryptionConfigCallback): void;

Calls CreateEncryptionConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateencryptionconfigrequest)`   
CreateEncryptionConfigRequest message or plain object  
`callback` |  `[CreateEncryptionConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createEncryptionConfig(request)
    
    
    public createEncryptionConfig(request: google.cloud.dataplex.v1.ICreateEncryptionConfigRequest): Promise<google.longrunning.Operation>;

Calls CreateEncryptionConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.icreateencryptionconfigrequest)`   
CreateEncryptionConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### deleteEncryptionConfig(request, callback)
    
    
    public deleteEncryptionConfig(request: google.cloud.dataplex.v1.IDeleteEncryptionConfigRequest, callback: google.cloud.dataplex.v1.CmekService.DeleteEncryptionConfigCallback): void;

Calls DeleteEncryptionConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteencryptionconfigrequest)`   
DeleteEncryptionConfigRequest message or plain object  
`callback` |  `[DeleteEncryptionConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteEncryptionConfig(request)
    
    
    public deleteEncryptionConfig(request: google.cloud.dataplex.v1.IDeleteEncryptionConfigRequest): Promise<google.longrunning.Operation>;

Calls DeleteEncryptionConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ideleteencryptionconfigrequest)`   
DeleteEncryptionConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
### getEncryptionConfig(request, callback)
    
    
    public getEncryptionConfig(request: google.cloud.dataplex.v1.IGetEncryptionConfigRequest, callback: google.cloud.dataplex.v1.CmekService.GetEncryptionConfigCallback): void;

Calls GetEncryptionConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetencryptionconfigrequest)`   
GetEncryptionConfigRequest message or plain object  
`callback` |  `[GetEncryptionConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and EncryptionConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getEncryptionConfig(request)
    
    
    public getEncryptionConfig(request: google.cloud.dataplex.v1.IGetEncryptionConfigRequest): Promise<google.cloud.dataplex.v1.EncryptionConfig>;

Calls GetEncryptionConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.igetencryptionconfigrequest)`   
GetEncryptionConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.EncryptionConfig](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.encryptionconfig-class)>` | Promise  
  
### listEncryptionConfigs(request, callback)
    
    
    public listEncryptionConfigs(request: google.cloud.dataplex.v1.IListEncryptionConfigsRequest, callback: google.cloud.dataplex.v1.CmekService.ListEncryptionConfigsCallback): void;

Calls ListEncryptionConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListEncryptionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistencryptionconfigsrequest)`   
ListEncryptionConfigsRequest message or plain object  
`callback` |  `[ListEncryptionConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and ListEncryptionConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listEncryptionConfigs(request)
    
    
    public listEncryptionConfigs(request: google.cloud.dataplex.v1.IListEncryptionConfigsRequest): Promise<google.cloud.dataplex.v1.ListEncryptionConfigsResponse>;

Calls ListEncryptionConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListEncryptionConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.ilistencryptionconfigsrequest)`   
ListEncryptionConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataplex.v1.ListEncryptionConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.listencryptionconfigsresponse)>` | Promise  
  
### updateEncryptionConfig(request, callback)
    
    
    public updateEncryptionConfig(request: google.cloud.dataplex.v1.IUpdateEncryptionConfigRequest, callback: google.cloud.dataplex.v1.CmekService.UpdateEncryptionConfigCallback): void;

Calls UpdateEncryptionConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateencryptionconfigrequest)`   
UpdateEncryptionConfigRequest message or plain object  
`callback` |  `[UpdateEncryptionConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateEncryptionConfig(request)
    
    
    public updateEncryptionConfig(request: google.cloud.dataplex.v1.IUpdateEncryptionConfigRequest): Promise<google.longrunning.Operation>;

Calls UpdateEncryptionConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateEncryptionConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.cloud.dataplex.v1.iupdateencryptionconfigrequest)`   
UpdateEncryptionConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/dataplex/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
