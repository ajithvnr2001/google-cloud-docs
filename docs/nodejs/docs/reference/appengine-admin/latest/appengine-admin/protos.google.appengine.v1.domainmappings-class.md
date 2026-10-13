---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.domainmappings-class
title: Class protos.google.appengine.v1.DomainMappings (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:33.788696+00:00
---

# Class protos.google.appengine.v1.DomainMappings (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.domainmappings-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.DomainMappings (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents a DomainMappings

## Inheritance

$protobuf.rpc.Service > protos.google.appengine.v1.DomainMappings

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DomainMappings service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DomainMappings;

Creates new DomainMappings service using the specified rpc implementation.

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
`[DomainMappings](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.domainmappings-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDomainMapping(request, callback)
    
    
    public createDomainMapping(request: google.appengine.v1.ICreateDomainMappingRequest, callback: google.appengine.v1.DomainMappings.CreateDomainMappingCallback): void;

Calls CreateDomainMapping.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreatedomainmappingrequest)`   
CreateDomainMappingRequest message or plain object  
`callback` |  `[CreateDomainMappingCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDomainMapping(request)
    
    
    public createDomainMapping(request: google.appengine.v1.ICreateDomainMappingRequest): Promise<google.longrunning.Operation>;

Calls CreateDomainMapping.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreatedomainmappingrequest)`   
CreateDomainMappingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### deleteDomainMapping(request, callback)
    
    
    public deleteDomainMapping(request: google.appengine.v1.IDeleteDomainMappingRequest, callback: google.appengine.v1.DomainMappings.DeleteDomainMappingCallback): void;

Calls DeleteDomainMapping.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideletedomainmappingrequest)`   
DeleteDomainMappingRequest message or plain object  
`callback` |  `[DeleteDomainMappingCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDomainMapping(request)
    
    
    public deleteDomainMapping(request: google.appengine.v1.IDeleteDomainMappingRequest): Promise<google.longrunning.Operation>;

Calls DeleteDomainMapping.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideletedomainmappingrequest)`   
DeleteDomainMappingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
### getDomainMapping(request, callback)
    
    
    public getDomainMapping(request: google.appengine.v1.IGetDomainMappingRequest, callback: google.appengine.v1.DomainMappings.GetDomainMappingCallback): void;

Calls GetDomainMapping.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetdomainmappingrequest)`   
GetDomainMappingRequest message or plain object  
`callback` |  `[GetDomainMappingCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and DomainMapping  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDomainMapping(request)
    
    
    public getDomainMapping(request: google.appengine.v1.IGetDomainMappingRequest): Promise<google.appengine.v1.DomainMapping>;

Calls GetDomainMapping.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetdomainmappingrequest)`   
GetDomainMappingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.DomainMapping](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.domainmapping)>` | Promise  
  
### listDomainMappings(request, callback)
    
    
    public listDomainMappings(request: google.appengine.v1.IListDomainMappingsRequest, callback: google.appengine.v1.DomainMappings.ListDomainMappingsCallback): void;

Calls ListDomainMappings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDomainMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistdomainmappingsrequest)`   
ListDomainMappingsRequest message or plain object  
`callback` |  `[ListDomainMappingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDomainMappingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDomainMappings(request)
    
    
    public listDomainMappings(request: google.appengine.v1.IListDomainMappingsRequest): Promise<google.appengine.v1.ListDomainMappingsResponse>;

Calls ListDomainMappings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDomainMappingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistdomainmappingsrequest)`   
ListDomainMappingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.ListDomainMappingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.listdomainmappingsresponse)>` | Promise  
  
### updateDomainMapping(request, callback)
    
    
    public updateDomainMapping(request: google.appengine.v1.IUpdateDomainMappingRequest, callback: google.appengine.v1.DomainMappings.UpdateDomainMappingCallback): void;

Calls UpdateDomainMapping.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdatedomainmappingrequest)`   
UpdateDomainMappingRequest message or plain object  
`callback` |  `[UpdateDomainMappingCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDomainMapping(request)
    
    
    public updateDomainMapping(request: google.appengine.v1.IUpdateDomainMappingRequest): Promise<google.longrunning.Operation>;

Calls UpdateDomainMapping.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDomainMappingRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdatedomainmappingrequest)`   
UpdateDomainMappingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
