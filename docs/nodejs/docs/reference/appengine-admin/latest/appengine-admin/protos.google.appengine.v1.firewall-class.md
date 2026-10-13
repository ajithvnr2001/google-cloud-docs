---
url: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.firewall-class
title: Class protos.google.appengine.v1.Firewall (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:41:35.152105+00:00
---

# Class protos.google.appengine.v1.Firewall (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.firewall-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.appengine.v1.Firewall (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  3.2.0  2.2.2  2.1.2  1.2.0  1.1.0  1.0.6 

Represents a Firewall

## Inheritance

$protobuf.rpc.Service > protos.google.appengine.v1.Firewall

## Package

[@google-cloud/appengine-admin](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Firewall service.

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

### batchUpdateIngressRules(request, callback)
    
    
    public batchUpdateIngressRules(request: google.appengine.v1.IBatchUpdateIngressRulesRequest, callback: google.appengine.v1.Firewall.BatchUpdateIngressRulesCallback): void;

Calls BatchUpdateIngressRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateIngressRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ibatchupdateingressrulesrequest)`   
BatchUpdateIngressRulesRequest message or plain object  
`callback` |  `[BatchUpdateIngressRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and BatchUpdateIngressRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateIngressRules(request)
    
    
    public batchUpdateIngressRules(request: google.appengine.v1.IBatchUpdateIngressRulesRequest): Promise<google.appengine.v1.BatchUpdateIngressRulesResponse>;

Calls BatchUpdateIngressRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateIngressRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ibatchupdateingressrulesrequest)`   
BatchUpdateIngressRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.BatchUpdateIngressRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.batchupdateingressrulesresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Firewall;

Creates new Firewall service using the specified rpc implementation.

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
`[Firewall](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.firewall-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createIngressRule(request, callback)
    
    
    public createIngressRule(request: google.appengine.v1.ICreateIngressRuleRequest, callback: google.appengine.v1.Firewall.CreateIngressRuleCallback): void;

Calls CreateIngressRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateingressrulerequest)`   
CreateIngressRuleRequest message or plain object  
`callback` |  `[CreateIngressRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and FirewallRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createIngressRule(request)
    
    
    public createIngressRule(request: google.appengine.v1.ICreateIngressRuleRequest): Promise<google.appengine.v1.FirewallRule>;

Calls CreateIngressRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.icreateingressrulerequest)`   
CreateIngressRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.FirewallRule](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.firewallrule-class)>` | Promise  
  
### deleteIngressRule(request, callback)
    
    
    public deleteIngressRule(request: google.appengine.v1.IDeleteIngressRuleRequest, callback: google.appengine.v1.Firewall.DeleteIngressRuleCallback): void;

Calls DeleteIngressRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteingressrulerequest)`   
DeleteIngressRuleRequest message or plain object  
`callback` |  `[DeleteIngressRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteIngressRule(request)
    
    
    public deleteIngressRule(request: google.appengine.v1.IDeleteIngressRuleRequest): Promise<google.protobuf.Empty>;

Calls DeleteIngressRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ideleteingressrulerequest)`   
DeleteIngressRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.protobuf.empty)>` | Promise  
  
### getIngressRule(request, callback)
    
    
    public getIngressRule(request: google.appengine.v1.IGetIngressRuleRequest, callback: google.appengine.v1.Firewall.GetIngressRuleCallback): void;

Calls GetIngressRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetingressrulerequest)`   
GetIngressRuleRequest message or plain object  
`callback` |  `[GetIngressRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and FirewallRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getIngressRule(request)
    
    
    public getIngressRule(request: google.appengine.v1.IGetIngressRuleRequest): Promise<google.appengine.v1.FirewallRule>;

Calls GetIngressRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.igetingressrulerequest)`   
GetIngressRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.FirewallRule](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.firewallrule-class)>` | Promise  
  
### listIngressRules(request, callback)
    
    
    public listIngressRules(request: google.appengine.v1.IListIngressRulesRequest, callback: google.appengine.v1.Firewall.ListIngressRulesCallback): void;

Calls ListIngressRules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListIngressRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistingressrulesrequest)`   
ListIngressRulesRequest message or plain object  
`callback` |  `[ListIngressRulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and ListIngressRulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listIngressRules(request)
    
    
    public listIngressRules(request: google.appengine.v1.IListIngressRulesRequest): Promise<google.appengine.v1.ListIngressRulesResponse>;

Calls ListIngressRules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListIngressRulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.ilistingressrulesrequest)`   
ListIngressRulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.ListIngressRulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.listingressrulesresponse)>` | Promise  
  
### updateIngressRule(request, callback)
    
    
    public updateIngressRule(request: google.appengine.v1.IUpdateIngressRuleRequest, callback: google.appengine.v1.Firewall.UpdateIngressRuleCallback): void;

Calls UpdateIngressRule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateingressrulerequest)`   
UpdateIngressRuleRequest message or plain object  
`callback` |  `[UpdateIngressRuleCallback](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/overview.html)`   
Node-style callback called with the error, if any, and FirewallRule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateIngressRule(request)
    
    
    public updateIngressRule(request: google.appengine.v1.IUpdateIngressRuleRequest): Promise<google.appengine.v1.FirewallRule>;

Calls UpdateIngressRule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateIngressRuleRequest](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.iupdateingressrulerequest)`   
UpdateIngressRuleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.appengine.v1.FirewallRule](https://docs.cloud.google.com/nodejs/docs/reference/appengine-admin/latest/appengine-admin/protos.google.appengine.v1.firewallrule-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
