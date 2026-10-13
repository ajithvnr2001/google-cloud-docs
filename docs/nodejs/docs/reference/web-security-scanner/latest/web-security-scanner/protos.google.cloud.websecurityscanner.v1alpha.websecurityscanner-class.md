---
url: https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.websecurityscanner-class
title: Class protos.google.cloud.websecurityscanner.v1alpha.WebSecurityScanner (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:39.527446+00:00
---

# Class protos.google.cloud.websecurityscanner.v1alpha.WebSecurityScanner (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.websecurityscanner-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.websecurityscanner.v1alpha.WebSecurityScanner (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.0  3.0.2  2.1.5  1.1.1  1.0.7 

Represents a WebSecurityScanner

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.websecurityscanner.v1alpha.WebSecurityScanner

## Package

[@google-cloud/web-security-scanner](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new WebSecurityScanner service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): WebSecurityScanner;

Creates new WebSecurityScanner service using the specified rpc implementation.

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
`[WebSecurityScanner](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.websecurityscanner-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createScanConfig(request, callback)
    
    
    public createScanConfig(request: google.cloud.websecurityscanner.v1alpha.ICreateScanConfigRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.CreateScanConfigCallback): void;

Calls CreateScanConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.icreatescanconfigrequest)`   
CreateScanConfigRequest message or plain object  
`callback` |  `[CreateScanConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ScanConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createScanConfig(request)
    
    
    public createScanConfig(request: google.cloud.websecurityscanner.v1alpha.ICreateScanConfigRequest): Promise<google.cloud.websecurityscanner.v1alpha.ScanConfig>;

Calls CreateScanConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.icreatescanconfigrequest)`   
CreateScanConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ScanConfig](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.scanconfig-class)>` | Promise  
  
### deleteScanConfig(request, callback)
    
    
    public deleteScanConfig(request: google.cloud.websecurityscanner.v1alpha.IDeleteScanConfigRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.DeleteScanConfigCallback): void;

Calls DeleteScanConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ideletescanconfigrequest)`   
DeleteScanConfigRequest message or plain object  
`callback` |  `[DeleteScanConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteScanConfig(request)
    
    
    public deleteScanConfig(request: google.cloud.websecurityscanner.v1alpha.IDeleteScanConfigRequest): Promise<google.protobuf.Empty>;

Calls DeleteScanConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ideletescanconfigrequest)`   
DeleteScanConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.protobuf.empty)>` | Promise  
  
### getFinding(request, callback)
    
    
    public getFinding(request: google.cloud.websecurityscanner.v1alpha.IGetFindingRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.GetFindingCallback): void;

Calls GetFinding.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetFindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.igetfindingrequest)`   
GetFindingRequest message or plain object  
`callback` |  `[GetFindingCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and Finding  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getFinding(request)
    
    
    public getFinding(request: google.cloud.websecurityscanner.v1alpha.IGetFindingRequest): Promise<google.cloud.websecurityscanner.v1alpha.Finding>;

Calls GetFinding.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetFindingRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.igetfindingrequest)`   
GetFindingRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.Finding](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.finding-class)>` | Promise  
  
### getScanConfig(request, callback)
    
    
    public getScanConfig(request: google.cloud.websecurityscanner.v1alpha.IGetScanConfigRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.GetScanConfigCallback): void;

Calls GetScanConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.igetscanconfigrequest)`   
GetScanConfigRequest message or plain object  
`callback` |  `[GetScanConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ScanConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getScanConfig(request)
    
    
    public getScanConfig(request: google.cloud.websecurityscanner.v1alpha.IGetScanConfigRequest): Promise<google.cloud.websecurityscanner.v1alpha.ScanConfig>;

Calls GetScanConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.igetscanconfigrequest)`   
GetScanConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ScanConfig](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.scanconfig-class)>` | Promise  
  
### getScanRun(request, callback)
    
    
    public getScanRun(request: google.cloud.websecurityscanner.v1alpha.IGetScanRunRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.GetScanRunCallback): void;

Calls GetScanRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetScanRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.igetscanrunrequest)`   
GetScanRunRequest message or plain object  
`callback` |  `[GetScanRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ScanRun  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getScanRun(request)
    
    
    public getScanRun(request: google.cloud.websecurityscanner.v1alpha.IGetScanRunRequest): Promise<google.cloud.websecurityscanner.v1alpha.ScanRun>;

Calls GetScanRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetScanRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.igetscanrunrequest)`   
GetScanRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.scanrun-class)>` | Promise  
  
### listCrawledUrls(request, callback)
    
    
    public listCrawledUrls(request: google.cloud.websecurityscanner.v1alpha.IListCrawledUrlsRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.ListCrawledUrlsCallback): void;

Calls ListCrawledUrls.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListCrawledUrlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistcrawledurlsrequest)`   
ListCrawledUrlsRequest message or plain object  
`callback` |  `[ListCrawledUrlsCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ListCrawledUrlsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listCrawledUrls(request)
    
    
    public listCrawledUrls(request: google.cloud.websecurityscanner.v1alpha.IListCrawledUrlsRequest): Promise<google.cloud.websecurityscanner.v1alpha.ListCrawledUrlsResponse>;

Calls ListCrawledUrls.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListCrawledUrlsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistcrawledurlsrequest)`   
ListCrawledUrlsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ListCrawledUrlsResponse](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.listcrawledurlsresponse)>` | Promise  
  
### listFindings(request, callback)
    
    
    public listFindings(request: google.cloud.websecurityscanner.v1alpha.IListFindingsRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.ListFindingsCallback): void;

Calls ListFindings.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistfindingsrequest)`   
ListFindingsRequest message or plain object  
`callback` |  `[ListFindingsCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFindingsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFindings(request)
    
    
    public listFindings(request: google.cloud.websecurityscanner.v1alpha.IListFindingsRequest): Promise<google.cloud.websecurityscanner.v1alpha.ListFindingsResponse>;

Calls ListFindings.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFindingsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistfindingsrequest)`   
ListFindingsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ListFindingsResponse](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.listfindingsresponse)>` | Promise  
  
### listFindingTypeStats(request, callback)
    
    
    public listFindingTypeStats(request: google.cloud.websecurityscanner.v1alpha.IListFindingTypeStatsRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.ListFindingTypeStatsCallback): void;

Calls ListFindingTypeStats.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListFindingTypeStatsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistfindingtypestatsrequest)`   
ListFindingTypeStatsRequest message or plain object  
`callback` |  `[ListFindingTypeStatsCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ListFindingTypeStatsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listFindingTypeStats(request)
    
    
    public listFindingTypeStats(request: google.cloud.websecurityscanner.v1alpha.IListFindingTypeStatsRequest): Promise<google.cloud.websecurityscanner.v1alpha.ListFindingTypeStatsResponse>;

Calls ListFindingTypeStats.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListFindingTypeStatsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistfindingtypestatsrequest)`   
ListFindingTypeStatsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ListFindingTypeStatsResponse](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.listfindingtypestatsresponse)>` | Promise  
  
### listScanConfigs(request, callback)
    
    
    public listScanConfigs(request: google.cloud.websecurityscanner.v1alpha.IListScanConfigsRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.ListScanConfigsCallback): void;

Calls ListScanConfigs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScanConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistscanconfigsrequest)`   
ListScanConfigsRequest message or plain object  
`callback` |  `[ListScanConfigsCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ListScanConfigsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listScanConfigs(request)
    
    
    public listScanConfigs(request: google.cloud.websecurityscanner.v1alpha.IListScanConfigsRequest): Promise<google.cloud.websecurityscanner.v1alpha.ListScanConfigsResponse>;

Calls ListScanConfigs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListScanConfigsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistscanconfigsrequest)`   
ListScanConfigsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ListScanConfigsResponse](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.listscanconfigsresponse)>` | Promise  
  
### listScanRuns(request, callback)
    
    
    public listScanRuns(request: google.cloud.websecurityscanner.v1alpha.IListScanRunsRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.ListScanRunsCallback): void;

Calls ListScanRuns.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListScanRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistscanrunsrequest)`   
ListScanRunsRequest message or plain object  
`callback` |  `[ListScanRunsCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ListScanRunsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listScanRuns(request)
    
    
    public listScanRuns(request: google.cloud.websecurityscanner.v1alpha.IListScanRunsRequest): Promise<google.cloud.websecurityscanner.v1alpha.ListScanRunsResponse>;

Calls ListScanRuns.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListScanRunsRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.ilistscanrunsrequest)`   
ListScanRunsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ListScanRunsResponse](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.listscanrunsresponse)>` | Promise  
  
### startScanRun(request, callback)
    
    
    public startScanRun(request: google.cloud.websecurityscanner.v1alpha.IStartScanRunRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.StartScanRunCallback): void;

Calls StartScanRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStartScanRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.istartscanrunrequest)`   
StartScanRunRequest message or plain object  
`callback` |  `[StartScanRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ScanRun  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### startScanRun(request)
    
    
    public startScanRun(request: google.cloud.websecurityscanner.v1alpha.IStartScanRunRequest): Promise<google.cloud.websecurityscanner.v1alpha.ScanRun>;

Calls StartScanRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStartScanRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.istartscanrunrequest)`   
StartScanRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.scanrun-class)>` | Promise  
  
### stopScanRun(request, callback)
    
    
    public stopScanRun(request: google.cloud.websecurityscanner.v1alpha.IStopScanRunRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.StopScanRunCallback): void;

Calls StopScanRun.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IStopScanRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.istopscanrunrequest)`   
StopScanRunRequest message or plain object  
`callback` |  `[StopScanRunCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ScanRun  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### stopScanRun(request)
    
    
    public stopScanRun(request: google.cloud.websecurityscanner.v1alpha.IStopScanRunRequest): Promise<google.cloud.websecurityscanner.v1alpha.ScanRun>;

Calls StopScanRun.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IStopScanRunRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.istopscanrunrequest)`   
StopScanRunRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ScanRun](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.scanrun-class)>` | Promise  
  
### updateScanConfig(request, callback)
    
    
    public updateScanConfig(request: google.cloud.websecurityscanner.v1alpha.IUpdateScanConfigRequest, callback: google.cloud.websecurityscanner.v1alpha.WebSecurityScanner.UpdateScanConfigCallback): void;

Calls UpdateScanConfig.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.iupdatescanconfigrequest)`   
UpdateScanConfigRequest message or plain object  
`callback` |  `[UpdateScanConfigCallback](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/overview.html)`   
Node-style callback called with the error, if any, and ScanConfig  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateScanConfig(request)
    
    
    public updateScanConfig(request: google.cloud.websecurityscanner.v1alpha.IUpdateScanConfigRequest): Promise<google.cloud.websecurityscanner.v1alpha.ScanConfig>;

Calls UpdateScanConfig.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateScanConfigRequest](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.iupdatescanconfigrequest)`   
UpdateScanConfigRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.websecurityscanner.v1alpha.ScanConfig](https://docs.cloud.google.com/nodejs/docs/reference/web-security-scanner/latest/web-security-scanner/protos.google.cloud.websecurityscanner.v1alpha.scanconfig-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
