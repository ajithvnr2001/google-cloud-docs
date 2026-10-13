---
url: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.jobservice-class
title: Class protos.google.cloud.talent.v4.JobService (8.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:46.384857+00:00
---

# Class protos.google.cloud.talent.v4.JobService (8.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.jobservice-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.talent.v4.JobService (8.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

8.1.1 (latest)  7.2.0  6.4.0  6.3.1  6.0.2  5.1.3  5.0.1  4.1.1  3.5.1  3.4.1  3.3.0  3.2.7 

Represents a JobService

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.talent.v4.JobService

## Package

[@google-cloud/talent](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new JobService service.

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

### batchCreateJobs(request, callback)
    
    
    public batchCreateJobs(request: google.cloud.talent.v4.IBatchCreateJobsRequest, callback: google.cloud.talent.v4.JobService.BatchCreateJobsCallback): void;

Calls BatchCreateJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ibatchcreatejobsrequest)`   
BatchCreateJobsRequest message or plain object  
`callback` |  `[BatchCreateJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchCreateJobs(request)
    
    
    public batchCreateJobs(request: google.cloud.talent.v4.IBatchCreateJobsRequest): Promise<google.longrunning.Operation>;

Calls BatchCreateJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchCreateJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ibatchcreatejobsrequest)`   
BatchCreateJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.longrunning.operation)>` | Promise  
  
### batchDeleteJobs(request, callback)
    
    
    public batchDeleteJobs(request: google.cloud.talent.v4.IBatchDeleteJobsRequest, callback: google.cloud.talent.v4.JobService.BatchDeleteJobsCallback): void;

Calls BatchDeleteJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ibatchdeletejobsrequest)`   
BatchDeleteJobsRequest message or plain object  
`callback` |  `[BatchDeleteJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchDeleteJobs(request)
    
    
    public batchDeleteJobs(request: google.cloud.talent.v4.IBatchDeleteJobsRequest): Promise<google.longrunning.Operation>;

Calls BatchDeleteJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchDeleteJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ibatchdeletejobsrequest)`   
BatchDeleteJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.longrunning.operation)>` | Promise  
  
### batchUpdateJobs(request, callback)
    
    
    public batchUpdateJobs(request: google.cloud.talent.v4.IBatchUpdateJobsRequest, callback: google.cloud.talent.v4.JobService.BatchUpdateJobsCallback): void;

Calls BatchUpdateJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ibatchupdatejobsrequest)`   
BatchUpdateJobsRequest message or plain object  
`callback` |  `[BatchUpdateJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### batchUpdateJobs(request)
    
    
    public batchUpdateJobs(request: google.cloud.talent.v4.IBatchUpdateJobsRequest): Promise<google.longrunning.Operation>;

Calls BatchUpdateJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IBatchUpdateJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ibatchupdatejobsrequest)`   
BatchUpdateJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.longrunning.operation)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): JobService;

Creates new JobService service using the specified rpc implementation.

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
`[JobService](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.jobservice-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createJob(request, callback)
    
    
    public createJob(request: google.cloud.talent.v4.ICreateJobRequest, callback: google.cloud.talent.v4.JobService.CreateJobCallback): void;

Calls CreateJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.icreatejobrequest)`   
CreateJobRequest message or plain object  
`callback` |  `[CreateJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createJob(request)
    
    
    public createJob(request: google.cloud.talent.v4.ICreateJobRequest): Promise<google.cloud.talent.v4.Job>;

Calls CreateJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.icreatejobrequest)`   
CreateJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.talent.v4.Job](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.job-class)>` | Promise  
  
### deleteJob(request, callback)
    
    
    public deleteJob(request: google.cloud.talent.v4.IDeleteJobRequest, callback: google.cloud.talent.v4.JobService.DeleteJobCallback): void;

Calls DeleteJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ideletejobrequest)`   
DeleteJobRequest message or plain object  
`callback` |  `[DeleteJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteJob(request)
    
    
    public deleteJob(request: google.cloud.talent.v4.IDeleteJobRequest): Promise<google.protobuf.Empty>;

Calls DeleteJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ideletejobrequest)`   
DeleteJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.protobuf.empty)>` | Promise  
  
### getJob(request, callback)
    
    
    public getJob(request: google.cloud.talent.v4.IGetJobRequest, callback: google.cloud.talent.v4.JobService.GetJobCallback): void;

Calls GetJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.igetjobrequest)`   
GetJobRequest message or plain object  
`callback` |  `[GetJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJob(request)
    
    
    public getJob(request: google.cloud.talent.v4.IGetJobRequest): Promise<google.cloud.talent.v4.Job>;

Calls GetJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.igetjobrequest)`   
GetJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.talent.v4.Job](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.job-class)>` | Promise  
  
### listJobs(request, callback)
    
    
    public listJobs(request: google.cloud.talent.v4.IListJobsRequest, callback: google.cloud.talent.v4.JobService.ListJobsCallback): void;

Calls ListJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ilistjobsrequest)`   
ListJobsRequest message or plain object  
`callback` |  `[ListJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and ListJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listJobs(request)
    
    
    public listJobs(request: google.cloud.talent.v4.IListJobsRequest): Promise<google.cloud.talent.v4.ListJobsResponse>;

Calls ListJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.ilistjobsrequest)`   
ListJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.talent.v4.ListJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.listjobsresponse)>` | Promise  
  
### searchJobs(request, callback)
    
    
    public searchJobs(request: google.cloud.talent.v4.ISearchJobsRequest, callback: google.cloud.talent.v4.JobService.SearchJobsCallback): void;

Calls SearchJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.isearchjobsrequest)`   
SearchJobsRequest message or plain object  
`callback` |  `[SearchJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchJobs(request)
    
    
    public searchJobs(request: google.cloud.talent.v4.ISearchJobsRequest): Promise<google.cloud.talent.v4.SearchJobsResponse>;

Calls SearchJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.isearchjobsrequest)`   
SearchJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.talent.v4.SearchJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.searchjobsresponse-class)>` | Promise  
  
### searchJobsForAlert(request, callback)
    
    
    public searchJobsForAlert(request: google.cloud.talent.v4.ISearchJobsRequest, callback: google.cloud.talent.v4.JobService.SearchJobsForAlertCallback): void;

Calls SearchJobsForAlert.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISearchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.isearchjobsrequest)`   
SearchJobsRequest message or plain object  
`callback` |  `[SearchJobsForAlertCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and SearchJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### searchJobsForAlert(request)
    
    
    public searchJobsForAlert(request: google.cloud.talent.v4.ISearchJobsRequest): Promise<google.cloud.talent.v4.SearchJobsResponse>;

Calls SearchJobsForAlert.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISearchJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.isearchjobsrequest)`   
SearchJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.talent.v4.SearchJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.searchjobsresponse-class)>` | Promise  
  
### updateJob(request, callback)
    
    
    public updateJob(request: google.cloud.talent.v4.IUpdateJobRequest, callback: google.cloud.talent.v4.JobService.UpdateJobCallback): void;

Calls UpdateJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.iupdatejobrequest)`   
UpdateJobRequest message or plain object  
`callback` |  `[UpdateJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateJob(request)
    
    
    public updateJob(request: google.cloud.talent.v4.IUpdateJobRequest): Promise<google.cloud.talent.v4.Job>;

Calls UpdateJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.iupdatejobrequest)`   
UpdateJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.talent.v4.Job](https://docs.cloud.google.com/nodejs/docs/reference/talent/latest/talent/protos.google.cloud.talent.v4.job-class)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
