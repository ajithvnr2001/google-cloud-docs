---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicyservice-class
title: Class protos.google.monitoring.v3.AlertPolicyService (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:48.296485+00:00
---

# Class protos.google.monitoring.v3.AlertPolicyService (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicyservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.v3.AlertPolicyService (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  4.0.0  3.0.4  2.3.5 

Represents an AlertPolicyService

## Inheritance

$protobuf.rpc.Service > protos.google.monitoring.v3.AlertPolicyService

## Package

[@google-cloud/monitoring](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AlertPolicyService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AlertPolicyService;

Creates new AlertPolicyService service using the specified rpc implementation.

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
`[AlertPolicyService](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicyservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAlertPolicy(request, callback)
    
    
    public createAlertPolicy(request: google.monitoring.v3.ICreateAlertPolicyRequest, callback: google.monitoring.v3.AlertPolicyService.CreateAlertPolicyCallback): void;

Calls CreateAlertPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreatealertpolicyrequest)`   
CreateAlertPolicyRequest message or plain object  
`callback` |  `[CreateAlertPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and AlertPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAlertPolicy(request)
    
    
    public createAlertPolicy(request: google.monitoring.v3.ICreateAlertPolicyRequest): Promise<google.monitoring.v3.AlertPolicy>;

Calls CreateAlertPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.icreatealertpolicyrequest)`   
CreateAlertPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.AlertPolicy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy-class)>` | Promise  
  
### deleteAlertPolicy(request, callback)
    
    
    public deleteAlertPolicy(request: google.monitoring.v3.IDeleteAlertPolicyRequest, callback: google.monitoring.v3.AlertPolicyService.DeleteAlertPolicyCallback): void;

Calls DeleteAlertPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ideletealertpolicyrequest)`   
DeleteAlertPolicyRequest message or plain object  
`callback` |  `[DeleteAlertPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteAlertPolicy(request)
    
    
    public deleteAlertPolicy(request: google.monitoring.v3.IDeleteAlertPolicyRequest): Promise<google.protobuf.Empty>;

Calls DeleteAlertPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ideletealertpolicyrequest)`   
DeleteAlertPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.protobuf.empty)>` | Promise  
  
### getAlertPolicy(request, callback)
    
    
    public getAlertPolicy(request: google.monitoring.v3.IGetAlertPolicyRequest, callback: google.monitoring.v3.AlertPolicyService.GetAlertPolicyCallback): void;

Calls GetAlertPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetalertpolicyrequest)`   
GetAlertPolicyRequest message or plain object  
`callback` |  `[GetAlertPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and AlertPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAlertPolicy(request)
    
    
    public getAlertPolicy(request: google.monitoring.v3.IGetAlertPolicyRequest): Promise<google.monitoring.v3.AlertPolicy>;

Calls GetAlertPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.igetalertpolicyrequest)`   
GetAlertPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.AlertPolicy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy-class)>` | Promise  
  
### listAlertPolicies(request, callback)
    
    
    public listAlertPolicies(request: google.monitoring.v3.IListAlertPoliciesRequest, callback: google.monitoring.v3.AlertPolicyService.ListAlertPoliciesCallback): void;

Calls ListAlertPolicies.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAlertPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ilistalertpoliciesrequest)`   
ListAlertPoliciesRequest message or plain object  
`callback` |  `[ListAlertPoliciesCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAlertPoliciesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAlertPolicies(request)
    
    
    public listAlertPolicies(request: google.monitoring.v3.IListAlertPoliciesRequest): Promise<google.monitoring.v3.ListAlertPoliciesResponse>;

Calls ListAlertPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAlertPoliciesRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.ilistalertpoliciesrequest)`   
ListAlertPoliciesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.ListAlertPoliciesResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.listalertpoliciesresponse)>` | Promise  
  
### updateAlertPolicy(request, callback)
    
    
    public updateAlertPolicy(request: google.monitoring.v3.IUpdateAlertPolicyRequest, callback: google.monitoring.v3.AlertPolicyService.UpdateAlertPolicyCallback): void;

Calls UpdateAlertPolicy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.iupdatealertpolicyrequest)`   
UpdateAlertPolicyRequest message or plain object  
`callback` |  `[UpdateAlertPolicyCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/overview.html)`   
Node-style callback called with the error, if any, and AlertPolicy  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAlertPolicy(request)
    
    
    public updateAlertPolicy(request: google.monitoring.v3.IUpdateAlertPolicyRequest): Promise<google.monitoring.v3.AlertPolicy>;

Calls UpdateAlertPolicy.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAlertPolicyRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.iupdatealertpolicyrequest)`   
UpdateAlertPolicyRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.v3.AlertPolicy](https://docs.cloud.google.com/nodejs/docs/reference/monitoring/latest/monitoring/protos.google.monitoring.v3.alertpolicy-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
