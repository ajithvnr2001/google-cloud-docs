---
url: https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.servicecontroller-class
title: Class protos.google.api.servicecontrol.v1.ServiceController (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:44.473795+00:00
---

# Class protos.google.api.servicecontrol.v1.ServiceController (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.servicecontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.api.servicecontrol.v1.ServiceController (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.4.0  3.3.0  3.2.0  2.3.0  2.2.0  2.1.2  2.0.3  1.4.0  1.3.0  1.2.1  1.1.4 

Represents a ServiceController

## Inheritance

$protobuf.rpc.Service > protos.google.api.servicecontrol.v1.ServiceController

## Package

[@google-cloud/service-control](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new ServiceController service.

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

### check(request, callback)
    
    
    public check(request: google.api.servicecontrol.v1.ICheckRequest, callback: google.api.servicecontrol.v1.ServiceController.CheckCallback): void;

Calls Check.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICheckRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.icheckrequest)`   
CheckRequest message or plain object  
`callback` |  `[CheckCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/overview.html)`   
Node-style callback called with the error, if any, and CheckResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### check(request)
    
    
    public check(request: google.api.servicecontrol.v1.ICheckRequest): Promise<google.api.servicecontrol.v1.CheckResponse>;

Calls Check.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICheckRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.icheckrequest)`   
CheckRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.servicecontrol.v1.CheckResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.checkresponse-class)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): ServiceController;

Creates new ServiceController service using the specified rpc implementation.

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
`[ServiceController](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.servicecontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### report(request, callback)
    
    
    public report(request: google.api.servicecontrol.v1.IReportRequest, callback: google.api.servicecontrol.v1.ServiceController.ReportCallback): void;

Calls Report.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ireportrequest)`   
ReportRequest message or plain object  
`callback` |  `[ReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/overview.html)`   
Node-style callback called with the error, if any, and ReportResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### report(request)
    
    
    public report(request: google.api.servicecontrol.v1.IReportRequest): Promise<google.api.servicecontrol.v1.ReportResponse>;

Calls Report.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.ireportrequest)`   
ReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.api.servicecontrol.v1.ReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/service-control/latest/service-control/protos.google.api.servicecontrol.v1.reportresponse-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
