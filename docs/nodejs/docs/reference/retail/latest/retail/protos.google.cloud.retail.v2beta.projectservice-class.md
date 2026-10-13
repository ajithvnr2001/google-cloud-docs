---
url: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.projectservice-class
title: Class protos.google.cloud.retail.v2beta.ProjectService (5.4.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:52.418179+00:00
---

# Class protos.google.cloud.retail.v2beta.ProjectService (5.4.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.projectservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.retail.v2beta.ProjectService (5.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.4.0 (latest)  5.3.1  5.0.1  4.4.0  4.3.0  3.6.0  3.5.0  3.1.0  2.4.1  2.3.1  2.1.1  2.0.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.2  1.1.6 

Represents a ProjectService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.retail.v2beta.ProjectService

## Package

[@google-cloud/retail](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ProjectService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ProjectService;

Creates new ProjectService service using the specified rpc implementation.

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
`[ProjectService](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.projectservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getAlertConfig(request, callback)
    
    
    public getAlertConfig(request: google.cloud.retail.v2beta.IGetAlertConfigRequest, callback: google.cloud.retail.v2beta.ProjectService.GetAlertConfigCallback): void;

Calls GetAlertConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAlertConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetalertconfigrequest)`   
GetAlertConfigRequest message or plain object  
`callback` |  `[GetAlertConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and AlertConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAlertConfig(request)
    
    
    public getAlertConfig(request: google.cloud.retail.v2beta.IGetAlertConfigRequest): Promise<google.cloud.retail.v2beta.AlertConfig>;

Calls GetAlertConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAlertConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.igetalertconfigrequest)`   
GetAlertConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.AlertConfig](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.alertconfig-class)>` | Promise  
  
### updateAlertConfig(request, callback)
    
    
    public updateAlertConfig(request: google.cloud.retail.v2beta.IUpdateAlertConfigRequest, callback: google.cloud.retail.v2beta.ProjectService.UpdateAlertConfigCallback): void;

Calls UpdateAlertConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAlertConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatealertconfigrequest)`   
UpdateAlertConfigRequest message or plain object  
`callback` |  `[UpdateAlertConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/overview.html)`   
Node-style callback called with the error, if any, and AlertConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAlertConfig(request)
    
    
    public updateAlertConfig(request: google.cloud.retail.v2beta.IUpdateAlertConfigRequest): Promise<google.cloud.retail.v2beta.AlertConfig>;

Calls UpdateAlertConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAlertConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.iupdatealertconfigrequest)`   
UpdateAlertConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.retail.v2beta.AlertConfig](https://docs.cloud.google.com/nodejs/docs/reference/retail/latest/retail/protos.google.cloud.retail.v2beta.alertconfig-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
