---
url: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.dashboardsservice-class
title: Class protos.google.monitoring.dashboard.v1.DashboardsService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:43:19.061846+00:00
---

# Class protos.google.monitoring.dashboard.v1.DashboardsService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.dashboardsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.monitoring.dashboard.v1.DashboardsService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  5.1.0  4.2.0  2.9.2  2.8.0  2.6.1  2.5.1  2.4.2  2.3.4 

Represents a DashboardsService

## Inheritance

$protobuf.rpc.Service > protos.google.monitoring.dashboard.v1.DashboardsService

## Package

[@google-cloud/monitoring-dashboards](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new DashboardsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): DashboardsService;

Creates new DashboardsService service using the specified rpc implementation.

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
`[DashboardsService](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.dashboardsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createDashboard(request, callback)
    
    
    public createDashboard(request: google.monitoring.dashboard.v1.ICreateDashboardRequest, callback: google.monitoring.dashboard.v1.DashboardsService.CreateDashboardCallback): void;

Calls CreateDashboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.icreatedashboardrequest)`   
CreateDashboardRequest message or plain object  
`callback` |  `[CreateDashboardCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)`   
Node-style callback called with the error, if any, and Dashboard  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createDashboard(request)
    
    
    public createDashboard(request: google.monitoring.dashboard.v1.ICreateDashboardRequest): Promise<google.monitoring.dashboard.v1.Dashboard>;

Calls CreateDashboard.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.icreatedashboardrequest)`   
CreateDashboardRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.dashboard.v1.Dashboard](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.dashboard)>` | Promise  
  
### deleteDashboard(request, callback)
    
    
    public deleteDashboard(request: google.monitoring.dashboard.v1.IDeleteDashboardRequest, callback: google.monitoring.dashboard.v1.DashboardsService.DeleteDashboardCallback): void;

Calls DeleteDashboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.ideletedashboardrequest)`   
DeleteDashboardRequest message or plain object  
`callback` |  `[DeleteDashboardCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteDashboard(request)
    
    
    public deleteDashboard(request: google.monitoring.dashboard.v1.IDeleteDashboardRequest): Promise<google.protobuf.Empty>;

Calls DeleteDashboard.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.ideletedashboardrequest)`   
DeleteDashboardRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.protobuf.empty)>` | Promise  
  
### getDashboard(request, callback)
    
    
    public getDashboard(request: google.monitoring.dashboard.v1.IGetDashboardRequest, callback: google.monitoring.dashboard.v1.DashboardsService.GetDashboardCallback): void;

Calls GetDashboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.igetdashboardrequest)`   
GetDashboardRequest message or plain object  
`callback` |  `[GetDashboardCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)`   
Node-style callback called with the error, if any, and Dashboard  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getDashboard(request)
    
    
    public getDashboard(request: google.monitoring.dashboard.v1.IGetDashboardRequest): Promise<google.monitoring.dashboard.v1.Dashboard>;

Calls GetDashboard.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.igetdashboardrequest)`   
GetDashboardRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.dashboard.v1.Dashboard](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.dashboard)>` | Promise  
  
### listDashboards(request, callback)
    
    
    public listDashboards(request: google.monitoring.dashboard.v1.IListDashboardsRequest, callback: google.monitoring.dashboard.v1.DashboardsService.ListDashboardsCallback): void;

Calls ListDashboards.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListDashboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.ilistdashboardsrequest)`   
ListDashboardsRequest message or plain object  
`callback` |  `[ListDashboardsCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)`   
Node-style callback called with the error, if any, and ListDashboardsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listDashboards(request)
    
    
    public listDashboards(request: google.monitoring.dashboard.v1.IListDashboardsRequest): Promise<google.monitoring.dashboard.v1.ListDashboardsResponse>;

Calls ListDashboards.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListDashboardsRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.ilistdashboardsrequest)`   
ListDashboardsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.dashboard.v1.ListDashboardsResponse](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.listdashboardsresponse)>` | Promise  
  
### updateDashboard(request, callback)
    
    
    public updateDashboard(request: google.monitoring.dashboard.v1.IUpdateDashboardRequest, callback: google.monitoring.dashboard.v1.DashboardsService.UpdateDashboardCallback): void;

Calls UpdateDashboard.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.iupdatedashboardrequest)`   
UpdateDashboardRequest message or plain object  
`callback` |  `[UpdateDashboardCallback](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/overview.html)`   
Node-style callback called with the error, if any, and Dashboard  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateDashboard(request)
    
    
    public updateDashboard(request: google.monitoring.dashboard.v1.IUpdateDashboardRequest): Promise<google.monitoring.dashboard.v1.Dashboard>;

Calls UpdateDashboard.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateDashboardRequest](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.iupdatedashboardrequest)`   
UpdateDashboardRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.monitoring.dashboard.v1.Dashboard](https://docs.cloud.google.com/nodejs/docs/reference/monitoring-dashboards/latest/monitoring-dashboards/protos.google.monitoring.dashboard.v1.dashboard)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
