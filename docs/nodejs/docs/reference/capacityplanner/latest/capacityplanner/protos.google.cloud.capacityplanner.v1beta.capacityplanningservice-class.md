---
url: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplanningservice-class
title: Class protos.google.cloud.capacityplanner.v1beta.CapacityPlanningService (0.1.2) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:21.549530+00:00
---

# Class protos.google.cloud.capacityplanner.v1beta.CapacityPlanningService (0.1.2)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplanningservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.capacityplanner.v1beta.CapacityPlanningService (0.1.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.2.0  0.1.2 

Represents a CapacityPlanningService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.capacityplanner.v1beta.CapacityPlanningService

## Package

[@google-cloud/capacityplanner](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CapacityPlanningService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CapacityPlanningService;

Creates new CapacityPlanningService service using the specified rpc implementation.

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
`[CapacityPlanningService](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplanningservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### getCapacityPlan(request, callback)
    
    
    public getCapacityPlan(request: google.cloud.capacityplanner.v1beta.IGetCapacityPlanRequest, callback: google.cloud.capacityplanner.v1beta.CapacityPlanningService.GetCapacityPlanCallback): void;

Calls GetCapacityPlan.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetCapacityPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.igetcapacityplanrequest)`   
GetCapacityPlanRequest message or plain object  
`callback` |  `[GetCapacityPlanCallback](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)`   
Node-style callback called with the error, if any, and CapacityPlan  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getCapacityPlan(request)
    
    
    public getCapacityPlan(request: google.cloud.capacityplanner.v1beta.IGetCapacityPlanRequest): Promise<google.cloud.capacityplanner.v1beta.CapacityPlan>;

Calls GetCapacityPlan.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetCapacityPlanRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.igetcapacityplanrequest)`   
GetCapacityPlanRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.capacityplanner.v1beta.CapacityPlan](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.capacityplan)>` | Promise  
  
### queryCapacityPlanInsights(request, callback)
    
    
    public queryCapacityPlanInsights(request: google.cloud.capacityplanner.v1beta.IQueryCapacityPlanInsightsRequest, callback: google.cloud.capacityplanner.v1beta.CapacityPlanningService.QueryCapacityPlanInsightsCallback): void;

Calls QueryCapacityPlanInsights.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCapacityPlanInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iquerycapacityplaninsightsrequest)`   
QueryCapacityPlanInsightsRequest message or plain object  
`callback` |  `[QueryCapacityPlanInsightsCallback](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryCapacityPlanInsightsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCapacityPlanInsights(request)
    
    
    public queryCapacityPlanInsights(request: google.cloud.capacityplanner.v1beta.IQueryCapacityPlanInsightsRequest): Promise<google.cloud.capacityplanner.v1beta.QueryCapacityPlanInsightsResponse>;

Calls QueryCapacityPlanInsights.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryCapacityPlanInsightsRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iquerycapacityplaninsightsrequest)`   
QueryCapacityPlanInsightsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.capacityplanner.v1beta.QueryCapacityPlanInsightsResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.querycapacityplaninsightsresponse)>` | Promise  
  
### queryCapacityPlans(request, callback)
    
    
    public queryCapacityPlans(request: google.cloud.capacityplanner.v1beta.IQueryCapacityPlansRequest, callback: google.cloud.capacityplanner.v1beta.CapacityPlanningService.QueryCapacityPlansCallback): void;

Calls QueryCapacityPlans.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IQueryCapacityPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iquerycapacityplansrequest)`   
QueryCapacityPlansRequest message or plain object  
`callback` |  `[QueryCapacityPlansCallback](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/overview.html)`   
Node-style callback called with the error, if any, and QueryCapacityPlansResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### queryCapacityPlans(request)
    
    
    public queryCapacityPlans(request: google.cloud.capacityplanner.v1beta.IQueryCapacityPlansRequest): Promise<google.cloud.capacityplanner.v1beta.QueryCapacityPlansResponse>;

Calls QueryCapacityPlans.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IQueryCapacityPlansRequest](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.iquerycapacityplansrequest)`   
QueryCapacityPlansRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.capacityplanner.v1beta.QueryCapacityPlansResponse](https://docs.cloud.google.com/nodejs/docs/reference/capacityplanner/latest/capacityplanner/protos.google.cloud.capacityplanner.v1beta.querycapacityplansresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
