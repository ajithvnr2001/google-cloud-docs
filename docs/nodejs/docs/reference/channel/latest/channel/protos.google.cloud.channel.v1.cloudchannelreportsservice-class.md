---
url: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.cloudchannelreportsservice-class
title: Class protos.google.cloud.channel.v1.CloudChannelReportsService (5.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:15:15.984621+00:00
---

# Class protos.google.cloud.channel.v1.CloudChannelReportsService (5.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.cloudchannelreportsservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.channel.v1.CloudChannelReportsService (5.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.1.1 (latest)  4.1.2  3.6.0  3.2.1  3.0.0  2.5.1  2.4.1  2.2.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.6 

Represents a CloudChannelReportsService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.channel.v1.CloudChannelReportsService

## Package

[@google-cloud/channel](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new CloudChannelReportsService service.

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
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): CloudChannelReportsService;

Creates new CloudChannelReportsService service using the specified rpc implementation.

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
`[CloudChannelReportsService](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.cloudchannelreportsservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### fetchReportResults(request, callback)
    
    
    public fetchReportResults(request: google.cloud.channel.v1.IFetchReportResultsRequest, callback: google.cloud.channel.v1.CloudChannelReportsService.FetchReportResultsCallback): void;

Calls FetchReportResults.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IFetchReportResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ifetchreportresultsrequest)`   
FetchReportResultsRequest message or plain object  
`callback` |  `[FetchReportResultsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and FetchReportResultsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### fetchReportResults(request)
    
    
    public fetchReportResults(request: google.cloud.channel.v1.IFetchReportResultsRequest): Promise<google.cloud.channel.v1.FetchReportResultsResponse>;

Calls FetchReportResults.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IFetchReportResultsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ifetchreportresultsrequest)`   
FetchReportResultsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.FetchReportResultsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.fetchreportresultsresponse)>` | Promise  
  
### listReports(request, callback)
    
    
    public listReports(request: google.cloud.channel.v1.IListReportsRequest, callback: google.cloud.channel.v1.CloudChannelReportsService.ListReportsCallback): void;

Calls ListReports.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistreportsrequest)`   
ListReportsRequest message or plain object  
`callback` |  `[ListReportsCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and ListReportsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listReports(request)
    
    
    public listReports(request: google.cloud.channel.v1.IListReportsRequest): Promise<google.cloud.channel.v1.ListReportsResponse>;

Calls ListReports.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListReportsRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.ilistreportsrequest)`   
ListReportsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.channel.v1.ListReportsResponse](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.listreportsresponse)>` | Promise  
  
### runReportJob(request, callback)
    
    
    public runReportJob(request: google.cloud.channel.v1.IRunReportJobRequest, callback: google.cloud.channel.v1.CloudChannelReportsService.RunReportJobCallback): void;

Calls RunReportJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IRunReportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.irunreportjobrequest)`   
RunReportJobRequest message or plain object  
`callback` |  `[RunReportJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### runReportJob(request)
    
    
    public runReportJob(request: google.cloud.channel.v1.IRunReportJobRequest): Promise<google.longrunning.Operation>;

Calls RunReportJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IRunReportJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.cloud.channel.v1.irunreportjobrequest)`   
RunReportJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/channel/latest/channel/protos.google.longrunning.operation)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
