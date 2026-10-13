---
url: https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.audit-class
title: Class protos.google.cloud.cloudsecuritycompliance.v1.Audit (0.4.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:57.158902+00:00
---

# Class protos.google.cloud.cloudsecuritycompliance.v1.Audit (0.4.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.audit-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.cloudsecuritycompliance.v1.Audit (0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an Audit

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.cloudsecuritycompliance.v1.Audit

## Package

[@google-cloud/cloudsecuritycompliance](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new Audit service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): Audit;

Creates new Audit service using the specified rpc implementation.

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
`[Audit](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.audit-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createFrameworkAudit(request, callback)
    
    
    public createFrameworkAudit(request: google.cloud.cloudsecuritycompliance.v1.ICreateFrameworkAuditRequest, callback: google.cloud.cloudsecuritycompliance.v1.Audit.CreateFrameworkAuditCallback): void;

Calls CreateFrameworkAudit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateFrameworkAuditRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.icreateframeworkauditrequest)`   
CreateFrameworkAuditRequest message or plain object  
`callback` |  `[CreateFrameworkAuditCallback](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createFrameworkAudit(request)
    
    
    public createFrameworkAudit(request: google.cloud.cloudsecuritycompliance.v1.ICreateFrameworkAuditRequest): Promise<google.longrunning.Operation>;

Calls CreateFrameworkAudit.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateFrameworkAuditRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.icreateframeworkauditrequest)`   
CreateFrameworkAuditRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.longrunning.operation)>` | Promise  
  
### generateFrameworkAuditScopeReport(request, callback)
    
    
    public generateFrameworkAuditScopeReport(request: google.cloud.cloudsecuritycompliance.v1.IGenerateFrameworkAuditScopeReportRequest, callback: google.cloud.cloudsecuritycompliance.v1.Audit.GenerateFrameworkAuditScopeReportCallback): void;

Calls GenerateFrameworkAuditScopeReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateFrameworkAuditScopeReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.igenerateframeworkauditscopereportrequest)`   
GenerateFrameworkAuditScopeReportRequest message or plain object  
`callback` |  `[GenerateFrameworkAuditScopeReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/overview.html)`   
Node-style callback called with the error, if any, and GenerateFrameworkAuditScopeReportResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateFrameworkAuditScopeReport(request)
    
    
    public generateFrameworkAuditScopeReport(request: google.cloud.cloudsecuritycompliance.v1.IGenerateFrameworkAuditScopeReportRequest): Promise<google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportResponse>;

Calls GenerateFrameworkAuditScopeReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateFrameworkAuditScopeReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.igenerateframeworkauditscopereportrequest)`   
GenerateFrameworkAuditScopeReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.cloudsecuritycompliance.v1.GenerateFrameworkAuditScopeReportResponse](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.generateframeworkauditscopereportresponse)>` | Promise  
  
### getFrameworkAudit(request, callback)
    
    
    public getFrameworkAudit(request: google.cloud.cloudsecuritycompliance.v1.IGetFrameworkAuditRequest, callback: google.cloud.cloudsecuritycompliance.v1.Audit.GetFrameworkAuditCallback): void;

Calls GetFrameworkAudit.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFrameworkAuditRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.igetframeworkauditrequest)`   
GetFrameworkAuditRequest message or plain object  
`callback` |  `[GetFrameworkAuditCallback](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/overview.html)`   
Node-style callback called with the error, if any, and FrameworkAudit  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFrameworkAudit(request)
    
    
    public getFrameworkAudit(request: google.cloud.cloudsecuritycompliance.v1.IGetFrameworkAuditRequest): Promise<google.cloud.cloudsecuritycompliance.v1.FrameworkAudit>;

Calls GetFrameworkAudit.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFrameworkAuditRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.igetframeworkauditrequest)`   
GetFrameworkAuditRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.cloudsecuritycompliance.v1.FrameworkAudit](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.frameworkaudit-class)>` | Promise  
  
### listFrameworkAudits(request, callback)
    
    
    public listFrameworkAudits(request: google.cloud.cloudsecuritycompliance.v1.IListFrameworkAuditsRequest, callback: google.cloud.cloudsecuritycompliance.v1.Audit.ListFrameworkAuditsCallback): void;

Calls ListFrameworkAudits.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFrameworkAuditsRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.ilistframeworkauditsrequest)`   
ListFrameworkAuditsRequest message or plain object  
`callback` |  `[ListFrameworkAuditsCallback](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFrameworkAuditsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFrameworkAudits(request)
    
    
    public listFrameworkAudits(request: google.cloud.cloudsecuritycompliance.v1.IListFrameworkAuditsRequest): Promise<google.cloud.cloudsecuritycompliance.v1.ListFrameworkAuditsResponse>;

Calls ListFrameworkAudits.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFrameworkAuditsRequest](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.ilistframeworkauditsrequest)`   
ListFrameworkAuditsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.cloudsecuritycompliance.v1.ListFrameworkAuditsResponse](https://docs.cloud.google.com/nodejs/docs/reference/cloudsecuritycompliance/latest/cloudsecuritycompliance/protos.google.cloud.cloudsecuritycompliance.v1.listframeworkauditsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
