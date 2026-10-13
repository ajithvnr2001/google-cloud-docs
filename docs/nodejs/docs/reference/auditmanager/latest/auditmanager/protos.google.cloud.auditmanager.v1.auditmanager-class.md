---
url: https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditmanager-class
title: Class protos.google.cloud.auditmanager.v1.AuditManager (0.5.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:28.999724+00:00
---

# Class protos.google.cloud.auditmanager.v1.AuditManager (0.5.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditmanager-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.auditmanager.v1.AuditManager (0.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

Represents an AuditManager

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.auditmanager.v1.AuditManager

## Package

[@google-cloud/auditmanager](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new AuditManager service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): AuditManager;

Creates new AuditManager service using the specified rpc implementation.

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
`[AuditManager](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditmanager-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createAuditSchedule(request, callback)
    
    
    public createAuditSchedule(request: google.cloud.auditmanager.v1.ICreateAuditScheduleRequest, callback: google.cloud.auditmanager.v1.AuditManager.CreateAuditScheduleCallback): void;

Calls CreateAuditSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuditScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.icreateauditschedulerequest)`   
CreateAuditScheduleRequest message or plain object  
`callback` |  `[CreateAuditScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AuditSchedule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createAuditSchedule(request)
    
    
    public createAuditSchedule(request: google.cloud.auditmanager.v1.ICreateAuditScheduleRequest): Promise<google.cloud.auditmanager.v1.AuditSchedule>;

Calls CreateAuditSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateAuditScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.icreateauditschedulerequest)`   
CreateAuditScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.AuditSchedule](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditschedule-class)>` | Promise  
  
### enrollResource(request, callback)
    
    
    public enrollResource(request: google.cloud.auditmanager.v1.IEnrollResourceRequest, callback: google.cloud.auditmanager.v1.AuditManager.EnrollResourceCallback): void;

Calls EnrollResource.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IEnrollResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ienrollresourcerequest)`   
EnrollResourceRequest message or plain object  
`callback` |  `[EnrollResourceCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Enrollment  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### enrollResource(request)
    
    
    public enrollResource(request: google.cloud.auditmanager.v1.IEnrollResourceRequest): Promise<google.cloud.auditmanager.v1.Enrollment>;

Calls EnrollResource.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IEnrollResourceRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ienrollresourcerequest)`   
EnrollResourceRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.Enrollment](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.enrollment)>` | Promise  
  
### generateAuditReport(request, callback)
    
    
    public generateAuditReport(request: google.cloud.auditmanager.v1.IGenerateAuditReportRequest, callback: google.cloud.auditmanager.v1.AuditManager.GenerateAuditReportCallback): void;

Calls GenerateAuditReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAuditReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igenerateauditreportrequest)`   
GenerateAuditReportRequest message or plain object  
`callback` |  `[GenerateAuditReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAuditReport(request)
    
    
    public generateAuditReport(request: google.cloud.auditmanager.v1.IGenerateAuditReportRequest): Promise<google.longrunning.Operation>;

Calls GenerateAuditReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAuditReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igenerateauditreportrequest)`   
GenerateAuditReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.longrunning.operation)>` | Promise  
  
### generateAuditScopeReport(request, callback)
    
    
    public generateAuditScopeReport(request: google.cloud.auditmanager.v1.IGenerateAuditScopeReportRequest, callback: google.cloud.auditmanager.v1.AuditManager.GenerateAuditScopeReportCallback): void;

Calls GenerateAuditScopeReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAuditScopeReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igenerateauditscopereportrequest)`   
GenerateAuditScopeReportRequest message or plain object  
`callback` |  `[GenerateAuditScopeReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AuditScopeReport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### generateAuditScopeReport(request)
    
    
    public generateAuditScopeReport(request: google.cloud.auditmanager.v1.IGenerateAuditScopeReportRequest): Promise<google.cloud.auditmanager.v1.AuditScopeReport>;

Calls GenerateAuditScopeReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGenerateAuditScopeReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igenerateauditscopereportrequest)`   
GenerateAuditScopeReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.AuditScopeReport](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditscopereport)>` | Promise  
  
### getAuditReport(request, callback)
    
    
    public getAuditReport(request: google.cloud.auditmanager.v1.IGetAuditReportRequest, callback: google.cloud.auditmanager.v1.AuditManager.GetAuditReportCallback): void;

Calls GetAuditReport.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuditReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igetauditreportrequest)`   
GetAuditReportRequest message or plain object  
`callback` |  `[GetAuditReportCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AuditReport  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuditReport(request)
    
    
    public getAuditReport(request: google.cloud.auditmanager.v1.IGetAuditReportRequest): Promise<google.cloud.auditmanager.v1.AuditReport>;

Calls GetAuditReport.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAuditReportRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igetauditreportrequest)`   
GetAuditReportRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.AuditReport](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditreport-class)>` | Promise  
  
### getAuditSchedule(request, callback)
    
    
    public getAuditSchedule(request: google.cloud.auditmanager.v1.IGetAuditScheduleRequest, callback: google.cloud.auditmanager.v1.AuditManager.GetAuditScheduleCallback): void;

Calls GetAuditSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetAuditScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igetauditschedulerequest)`   
GetAuditScheduleRequest message or plain object  
`callback` |  `[GetAuditScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AuditSchedule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getAuditSchedule(request)
    
    
    public getAuditSchedule(request: google.cloud.auditmanager.v1.IGetAuditScheduleRequest): Promise<google.cloud.auditmanager.v1.AuditSchedule>;

Calls GetAuditSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetAuditScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igetauditschedulerequest)`   
GetAuditScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.AuditSchedule](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditschedule-class)>` | Promise  
  
### getResourceEnrollmentStatus(request, callback)
    
    
    public getResourceEnrollmentStatus(request: google.cloud.auditmanager.v1.IGetResourceEnrollmentStatusRequest, callback: google.cloud.auditmanager.v1.AuditManager.GetResourceEnrollmentStatusCallback): void;

Calls GetResourceEnrollmentStatus.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceEnrollmentStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igetresourceenrollmentstatusrequest)`   
GetResourceEnrollmentStatusRequest message or plain object  
`callback` |  `[GetResourceEnrollmentStatusCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ResourceEnrollmentStatus  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getResourceEnrollmentStatus(request)
    
    
    public getResourceEnrollmentStatus(request: google.cloud.auditmanager.v1.IGetResourceEnrollmentStatusRequest): Promise<google.cloud.auditmanager.v1.ResourceEnrollmentStatus>;

Calls GetResourceEnrollmentStatus.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetResourceEnrollmentStatusRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.igetresourceenrollmentstatusrequest)`   
GetResourceEnrollmentStatusRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.ResourceEnrollmentStatus](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.resourceenrollmentstatus-class)>` | Promise  
  
### listAuditReports(request, callback)
    
    
    public listAuditReports(request: google.cloud.auditmanager.v1.IListAuditReportsRequest, callback: google.cloud.auditmanager.v1.AuditManager.ListAuditReportsCallback): void;

Calls ListAuditReports.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuditReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistauditreportsrequest)`   
ListAuditReportsRequest message or plain object  
`callback` |  `[ListAuditReportsCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAuditReportsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuditReports(request)
    
    
    public listAuditReports(request: google.cloud.auditmanager.v1.IListAuditReportsRequest): Promise<google.cloud.auditmanager.v1.ListAuditReportsResponse>;

Calls ListAuditReports.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAuditReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistauditreportsrequest)`   
ListAuditReportsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.ListAuditReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.listauditreportsresponse)>` | Promise  
  
### listAuditSchedules(request, callback)
    
    
    public listAuditSchedules(request: google.cloud.auditmanager.v1.IListAuditSchedulesRequest, callback: google.cloud.auditmanager.v1.AuditManager.ListAuditSchedulesCallback): void;

Calls ListAuditSchedules.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListAuditSchedulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistauditschedulesrequest)`   
ListAuditSchedulesRequest message or plain object  
`callback` |  `[ListAuditSchedulesCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListAuditSchedulesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listAuditSchedules(request)
    
    
    public listAuditSchedules(request: google.cloud.auditmanager.v1.IListAuditSchedulesRequest): Promise<google.cloud.auditmanager.v1.ListAuditSchedulesResponse>;

Calls ListAuditSchedules.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListAuditSchedulesRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistauditschedulesrequest)`   
ListAuditSchedulesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.ListAuditSchedulesResponse](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.listauditschedulesresponse)>` | Promise  
  
### listControls(request, callback)
    
    
    public listControls(request: google.cloud.auditmanager.v1.IListControlsRequest, callback: google.cloud.auditmanager.v1.AuditManager.ListControlsCallback): void;

Calls ListControls.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistcontrolsrequest)`   
ListControlsRequest message or plain object  
`callback` |  `[ListControlsCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListControlsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listControls(request)
    
    
    public listControls(request: google.cloud.auditmanager.v1.IListControlsRequest): Promise<google.cloud.auditmanager.v1.ListControlsResponse>;

Calls ListControls.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListControlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistcontrolsrequest)`   
ListControlsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.ListControlsResponse](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.listcontrolsresponse)>` | Promise  
  
### listResourceEnrollmentStatuses(request, callback)
    
    
    public listResourceEnrollmentStatuses(request: google.cloud.auditmanager.v1.IListResourceEnrollmentStatusesRequest, callback: google.cloud.auditmanager.v1.AuditManager.ListResourceEnrollmentStatusesCallback): void;

Calls ListResourceEnrollmentStatuses.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistresourceenrollmentstatusesrequest)`   
ListResourceEnrollmentStatusesRequest message or plain object  
`callback` |  `[ListResourceEnrollmentStatusesCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and ListResourceEnrollmentStatusesResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listResourceEnrollmentStatuses(request)
    
    
    public listResourceEnrollmentStatuses(request: google.cloud.auditmanager.v1.IListResourceEnrollmentStatusesRequest): Promise<google.cloud.auditmanager.v1.ListResourceEnrollmentStatusesResponse>;

Calls ListResourceEnrollmentStatuses.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListResourceEnrollmentStatusesRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.ilistresourceenrollmentstatusesrequest)`   
ListResourceEnrollmentStatusesRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.ListResourceEnrollmentStatusesResponse](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.listresourceenrollmentstatusesresponse)>` | Promise  
  
### updateAuditSchedule(request, callback)
    
    
    public updateAuditSchedule(request: google.cloud.auditmanager.v1.IUpdateAuditScheduleRequest, callback: google.cloud.auditmanager.v1.AuditManager.UpdateAuditScheduleCallback): void;

Calls UpdateAuditSchedule.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuditScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.iupdateauditschedulerequest)`   
UpdateAuditScheduleRequest message or plain object  
`callback` |  `[UpdateAuditScheduleCallback](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/overview.html)`   
Node-style callback called with the error, if any, and AuditSchedule  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateAuditSchedule(request)
    
    
    public updateAuditSchedule(request: google.cloud.auditmanager.v1.IUpdateAuditScheduleRequest): Promise<google.cloud.auditmanager.v1.AuditSchedule>;

Calls UpdateAuditSchedule.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateAuditScheduleRequest](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.iupdateauditschedulerequest)`   
UpdateAuditScheduleRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.auditmanager.v1.AuditSchedule](https://docs.cloud.google.com/nodejs/docs/reference/auditmanager/latest/auditmanager/protos.google.cloud.auditmanager.v1.auditschedule-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
