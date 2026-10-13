---
url: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.jobcontroller-class
title: Class protos.google.cloud.dataproc.v1.JobController (7.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:03:48.119984+00:00
---

# Class protos.google.cloud.dataproc.v1.JobController (7.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.jobcontroller-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.dataproc.v1.JobController (7.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.1.1 (latest)  6.8.0  6.7.0  6.6.0  5.13.0  5.12.0  5.10.0  5.9.0  5.7.0  5.5.0  5.4.0  4.5.0  4.3.1  4.1.1  3.2.0  3.1.0  3.0.0  2.5.0  2.4.4 

Represents a JobController

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.dataproc.v1.JobController

## Package

[@google-cloud/dataproc](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new JobController service.

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

### cancelJob(request, callback)
    
    
    public cancelJob(request: google.cloud.dataproc.v1.ICancelJobRequest, callback: google.cloud.dataproc.v1.JobController.CancelJobCallback): void;

Calls CancelJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icanceljobrequest)`   
CancelJobRequest message or plain object  
`callback` |  `[CancelJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelJob(request)
    
    
    public cancelJob(request: google.cloud.dataproc.v1.ICancelJobRequest): Promise<google.cloud.dataproc.v1.Job>;

Calls CancelJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.icanceljobrequest)`   
CancelJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): JobController;

Creates new JobController service using the specified rpc implementation.

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
`[JobController](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.jobcontroller-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### deleteJob(request, callback)
    
    
    public deleteJob(request: google.cloud.dataproc.v1.IDeleteJobRequest, callback: google.cloud.dataproc.v1.JobController.DeleteJobCallback): void;

Calls DeleteJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletejobrequest)`   
DeleteJobRequest message or plain object  
`callback` |  `[DeleteJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteJob(request)
    
    
    public deleteJob(request: google.cloud.dataproc.v1.IDeleteJobRequest): Promise<google.protobuf.Empty>;

Calls DeleteJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ideletejobrequest)`   
DeleteJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.protobuf.empty)>` | Promise  
  
### getJob(request, callback)
    
    
    public getJob(request: google.cloud.dataproc.v1.IGetJobRequest, callback: google.cloud.dataproc.v1.JobController.GetJobCallback): void;

Calls GetJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)`   
GetJobRequest message or plain object  
`callback` |  `[GetJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJob(request)
    
    
    public getJob(request: google.cloud.dataproc.v1.IGetJobRequest): Promise<google.cloud.dataproc.v1.Job>;

Calls GetJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.igetjobrequest)`   
GetJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)>` | Promise  
  
### listJobs(request, callback)
    
    
    public listJobs(request: google.cloud.dataproc.v1.IListJobsRequest, callback: google.cloud.dataproc.v1.JobController.ListJobsCallback): void;

Calls ListJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistjobsrequest)`   
ListJobsRequest message or plain object  
`callback` |  `[ListJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and ListJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listJobs(request)
    
    
    public listJobs(request: google.cloud.dataproc.v1.IListJobsRequest): Promise<google.cloud.dataproc.v1.ListJobsResponse>;

Calls ListJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.ilistjobsrequest)`   
ListJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.ListJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.listjobsresponse)>` | Promise  
  
### submitJob(request, callback)
    
    
    public submitJob(request: google.cloud.dataproc.v1.ISubmitJobRequest, callback: google.cloud.dataproc.v1.JobController.SubmitJobCallback): void;

Calls SubmitJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isubmitjobrequest)`   
SubmitJobRequest message or plain object  
`callback` |  `[SubmitJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### submitJob(request)
    
    
    public submitJob(request: google.cloud.dataproc.v1.ISubmitJobRequest): Promise<google.cloud.dataproc.v1.Job>;

Calls SubmitJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubmitJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isubmitjobrequest)`   
SubmitJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)>` | Promise  
  
### submitJobAsOperation(request, callback)
    
    
    public submitJobAsOperation(request: google.cloud.dataproc.v1.ISubmitJobRequest, callback: google.cloud.dataproc.v1.JobController.SubmitJobAsOperationCallback): void;

Calls SubmitJobAsOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ISubmitJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isubmitjobrequest)`   
SubmitJobRequest message or plain object  
`callback` |  `[SubmitJobAsOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### submitJobAsOperation(request)
    
    
    public submitJobAsOperation(request: google.cloud.dataproc.v1.ISubmitJobRequest): Promise<google.longrunning.Operation>;

Calls SubmitJobAsOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ISubmitJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.isubmitjobrequest)`   
SubmitJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.longrunning.operation)>` | Promise  
  
### updateJob(request, callback)
    
    
    public updateJob(request: google.cloud.dataproc.v1.IUpdateJobRequest, callback: google.cloud.dataproc.v1.JobController.UpdateJobCallback): void;

Calls UpdateJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IUpdateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdatejobrequest)`   
UpdateJobRequest message or plain object  
`callback` |  `[UpdateJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### updateJob(request)
    
    
    public updateJob(request: google.cloud.dataproc.v1.IUpdateJobRequest): Promise<google.cloud.dataproc.v1.Job>;

Calls UpdateJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IUpdateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.iupdatejobrequest)`   
UpdateJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.dataproc.v1.Job](https://docs.cloud.google.com/nodejs/docs/reference/dataproc/latest/dataproc/protos.google.cloud.dataproc.v1.job)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
