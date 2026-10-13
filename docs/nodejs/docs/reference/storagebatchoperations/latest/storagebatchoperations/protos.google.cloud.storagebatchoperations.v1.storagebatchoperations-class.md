---
url: https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.storagebatchoperations-class
title: Class protos.google.cloud.storagebatchoperations.v1.StorageBatchOperations (0.7.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:56.727391+00:00
---

# Class protos.google.cloud.storagebatchoperations.v1.StorageBatchOperations (0.7.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.storagebatchoperations-class

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Class protos.google.cloud.storagebatchoperations.v1.StorageBatchOperations (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.5.0 

Represents a StorageBatchOperations

## Inheritance

$protobuf.rpc.Service > protos.google.cloud.storagebatchoperations.v1.StorageBatchOperations

## Package

[@google-cloud/storagebatchoperations](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)

## Constructors 

### (constructor)(rpcImpl, requestDelimited, responseDelimited)
    
    
    constructor(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean);

Constructs a new StorageBatchOperations service.

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
    
    
    public cancelJob(request: google.cloud.storagebatchoperations.v1.ICancelJobRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.CancelJobCallback): void;

Calls CancelJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICancelJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.icanceljobrequest)`   
CancelJobRequest message or plain object  
`callback` |  `[CancelJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and CancelJobResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### cancelJob(request)
    
    
    public cancelJob(request: google.cloud.storagebatchoperations.v1.ICancelJobRequest): Promise<google.cloud.storagebatchoperations.v1.CancelJobResponse>;

Calls CancelJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICancelJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.icanceljobrequest)`   
CancelJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.storagebatchoperations.v1.CancelJobResponse](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.canceljobresponse)>` | Promise  
  
### create(rpcImpl, requestDelimited, responseDelimited)
    
    
    public static create(rpcImpl: $protobuf.RPCImpl, requestDelimited?: boolean, responseDelimited?: boolean): StorageBatchOperations;

Creates new StorageBatchOperations service using the specified rpc implementation.

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
`[StorageBatchOperations](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.storagebatchoperations-class)` | RPC service. Useful where requests and/or responses are streamed.  
  
### createJob(request, callback)
    
    
    public createJob(request: google.cloud.storagebatchoperations.v1.ICreateJobRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.CreateJobCallback): void;

Calls CreateJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.icreatejobrequest)`   
CreateJobRequest message or plain object  
`callback` |  `[CreateJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and Operation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### createJob(request)
    
    
    public createJob(request: google.cloud.storagebatchoperations.v1.ICreateJobRequest): Promise<google.longrunning.Operation>;

Calls CreateJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[ICreateJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.icreatejobrequest)`   
CreateJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.longrunning.Operation](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.longrunning.operation)>` | Promise  
  
### deleteJob(request, callback)
    
    
    public deleteJob(request: google.cloud.storagebatchoperations.v1.IDeleteJobRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.DeleteJobCallback): void;

Calls DeleteJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IDeleteJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ideletejobrequest)`   
DeleteJobRequest message or plain object  
`callback` |  `[DeleteJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and Empty  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### deleteJob(request)
    
    
    public deleteJob(request: google.cloud.storagebatchoperations.v1.IDeleteJobRequest): Promise<google.protobuf.Empty>;

Calls DeleteJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IDeleteJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ideletejobrequest)`   
DeleteJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.protobuf.Empty](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.protobuf.empty)>` | Promise  
  
### getBucketOperation(request, callback)
    
    
    public getBucketOperation(request: google.cloud.storagebatchoperations.v1.IGetBucketOperationRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.GetBucketOperationCallback): void;

Calls GetBucketOperation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetBucketOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.igetbucketoperationrequest)`   
GetBucketOperationRequest message or plain object  
`callback` |  `[GetBucketOperationCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and BucketOperation  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getBucketOperation(request)
    
    
    public getBucketOperation(request: google.cloud.storagebatchoperations.v1.IGetBucketOperationRequest): Promise<google.cloud.storagebatchoperations.v1.BucketOperation>;

Calls GetBucketOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetBucketOperationRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.igetbucketoperationrequest)`   
GetBucketOperationRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.storagebatchoperations.v1.BucketOperation](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.bucketoperation-class)>` | Promise  
  
### getJob(request, callback)
    
    
    public getJob(request: google.cloud.storagebatchoperations.v1.IGetJobRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.GetJobCallback): void;

Calls GetJob.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.igetjobrequest)`   
GetJobRequest message or plain object  
`callback` |  `[GetJobCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and Job  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### getJob(request)
    
    
    public getJob(request: google.cloud.storagebatchoperations.v1.IGetJobRequest): Promise<google.cloud.storagebatchoperations.v1.Job>;

Calls GetJob.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IGetJobRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.igetjobrequest)`   
GetJobRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.storagebatchoperations.v1.Job](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.job-class)>` | Promise  
  
### listBucketOperations(request, callback)
    
    
    public listBucketOperations(request: google.cloud.storagebatchoperations.v1.IListBucketOperationsRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.ListBucketOperationsCallback): void;

Calls ListBucketOperations.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListBucketOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ilistbucketoperationsrequest)`   
ListBucketOperationsRequest message or plain object  
`callback` |  `[ListBucketOperationsCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and ListBucketOperationsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listBucketOperations(request)
    
    
    public listBucketOperations(request: google.cloud.storagebatchoperations.v1.IListBucketOperationsRequest): Promise<google.cloud.storagebatchoperations.v1.ListBucketOperationsResponse>;

Calls ListBucketOperations.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListBucketOperationsRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ilistbucketoperationsrequest)`   
ListBucketOperationsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.storagebatchoperations.v1.ListBucketOperationsResponse](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.listbucketoperationsresponse)>` | Promise  
  
### listJobs(request, callback)
    
    
    public listJobs(request: google.cloud.storagebatchoperations.v1.IListJobsRequest, callback: google.cloud.storagebatchoperations.v1.StorageBatchOperations.ListJobsCallback): void;

Calls ListJobs.

**Parameters**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ilistjobsrequest)`   
ListJobsRequest message or plain object  
`callback` |  `[ListJobsCallback](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/overview.html)`   
Node-style callback called with the error, if any, and ListJobsResponse  
**Returns**  
---  
**Type** | **Description**  
`void` |   
  
### listJobs(request)
    
    
    public listJobs(request: google.cloud.storagebatchoperations.v1.IListJobsRequest): Promise<google.cloud.storagebatchoperations.v1.ListJobsResponse>;

Calls ListJobs.

**Parameter**  
---  
**Name** | **Description**  
`request` |  `[IListJobsRequest](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.ilistjobsrequest)`   
ListJobsRequest message or plain object  
**Returns**  
---  
**Type** | **Description**  
`Promise<[google.cloud.storagebatchoperations.v1.ListJobsResponse](https://docs.cloud.google.com/nodejs/docs/reference/storagebatchoperations/latest/storagebatchoperations/protos.google.cloud.storagebatchoperations.v1.listjobsresponse)>` | Promise  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
