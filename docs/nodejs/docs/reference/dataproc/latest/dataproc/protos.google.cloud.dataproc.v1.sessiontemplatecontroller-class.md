---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessiontemplatecontroller-class
title: Class protos.google.cloud.dataproc.v1.SessionTemplateController (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:04:00.642975+00:00
---

# Class protos.google.cloud.dataproc.v1.SessionTemplateController (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessiontemplatecontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.SessionTemplateController (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a SessionTemplateController

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.SessionTemplateController

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new SessionTemplateController service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): SessionTemplateController;

Creates new SessionTemplateController service using the specified rpc implementation.

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
`[SessionTemplateController](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessiontemplatecontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createSessionTemplate(request, callback)
    
    
    public createSessionTemplate(request: google.cloud.dataproc.v1.ICreateSessionTemplateRequest, callback: google.cloud.dataproc.v1.SessionTemplateController.CreateSessionTemplateCallback): void;

Calls CreateSessionTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatesessiontemplaterequest)`   
CreateSessionTemplateRequest message or plain object  
`callback` |  `[CreateSessionTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and SessionTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createSessionTemplate(request)
    
    
    public createSessionTemplate(request: google.cloud.dataproc.v1.ICreateSessionTemplateRequest): Promise<google.cloud.dataproc.v1.SessionTemplate>;

Calls CreateSessionTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icreatesessiontemplaterequest)`   
CreateSessionTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.SessionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessiontemplate)>` | Promise  
  
### deleteSessionTemplate(request, callback)
    
    
    public deleteSessionTemplate(request: google.cloud.dataproc.v1.IDeleteSessionTemplateRequest, callback: google.cloud.dataproc.v1.SessionTemplateController.DeleteSessionTemplateCallback): void;

Calls DeleteSessionTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletesessiontemplaterequest)`   
DeleteSessionTemplateRequest message or plain object  
`callback` |  `[DeleteSessionTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteSessionTemplate(request)
    
    
    public deleteSessionTemplate(request: google.cloud.dataproc.v1.IDeleteSessionTemplateRequest): Promise<google.protobuf.Empty>;

Calls DeleteSessionTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletesessiontemplaterequest)`   
DeleteSessionTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.protobuf.empty)>` | Promise  
  
### getSessionTemplate(request, callback)
    
    
    public getSessionTemplate(request: google.cloud.dataproc.v1.IGetSessionTemplateRequest, callback: google.cloud.dataproc.v1.SessionTemplateController.GetSessionTemplateCallback): void;

Calls GetSessionTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetsessiontemplaterequest)`   
GetSessionTemplateRequest message or plain object  
`callback` |  `[GetSessionTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and SessionTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getSessionTemplate(request)
    
    
    public getSessionTemplate(request: google.cloud.dataproc.v1.IGetSessionTemplateRequest): Promise<google.cloud.dataproc.v1.SessionTemplate>;

Calls GetSessionTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetsessiontemplaterequest)`   
GetSessionTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.SessionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessiontemplate)>` | Promise  
  
### listSessionTemplates(request, callback)
    
    
    public listSessionTemplates(request: google.cloud.dataproc.v1.IListSessionTemplatesRequest, callback: google.cloud.dataproc.v1.SessionTemplateController.ListSessionTemplatesCallback): void;

Calls ListSessionTemplates.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListSessionTemplatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistsessiontemplatesrequest)`   
ListSessionTemplatesRequest message or plain object  
`callback` |  `[ListSessionTemplatesCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListSessionTemplatesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listSessionTemplates(request)
    
    
    public listSessionTemplates(request: google.cloud.dataproc.v1.IListSessionTemplatesRequest): Promise<google.cloud.dataproc.v1.ListSessionTemplatesResponse>;

Calls ListSessionTemplates.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListSessionTemplatesRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistsessiontemplatesrequest)`   
ListSessionTemplatesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.ListSessionTemplatesResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.listsessiontemplatesresponse)>` | Promise  
  
### updateSessionTemplate(request, callback)
    
    
    public updateSessionTemplate(request: google.cloud.dataproc.v1.IUpdateSessionTemplateRequest, callback: google.cloud.dataproc.v1.SessionTemplateController.UpdateSessionTemplateCallback): void;

Calls UpdateSessionTemplate.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdatesessiontemplaterequest)`   
UpdateSessionTemplateRequest message or plain object  
`callback` |  `[UpdateSessionTemplateCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and SessionTemplate  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateSessionTemplate(request)
    
    
    public updateSessionTemplate(request: google.cloud.dataproc.v1.IUpdateSessionTemplateRequest): Promise<google.cloud.dataproc.v1.SessionTemplate>;

Calls UpdateSessionTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateSessionTemplateRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdatesessiontemplaterequest)`   
UpdateSessionTemplateRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.SessionTemplate](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.sessiontemplate)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
