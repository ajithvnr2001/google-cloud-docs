---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub
title: Class StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:48.776970+00:00
---

# Class StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static final class StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub extends AbstractBlockingStub<StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service StorageBatchOperations.

Storage Batch Operations offers a managed experience to perform batch operations on millions of Cloud Storage objects in a serverless fashion. With this service, you can automate and simplify large scale API operations performed on Cloud Storage objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.StorageBatchOperationsGrpc.StorageBatchOperationsBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### cancelJob(CancelJobRequest request)
    
    
    public CancelJobResponse cancelJob(CancelJobRequest request)

Cancels a batch job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CancelJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.CancelJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CancelJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.CancelJobResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### createJob(CreateJobRequest request)
    
    
    public Operation createJob(CreateJobRequest request)

Creates a batch job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.CreateJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteJob(DeleteJobRequest request)
    
    
    public Empty deleteJob(DeleteJobRequest request)

Deletes a batch job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.DeleteJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getBucketOperation(GetBucketOperationRequest request)
    
    
    public BucketOperation getBucketOperation(GetBucketOperationRequest request)

Gets a BucketOperation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetBucketOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.GetBucketOperationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BucketOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.BucketOperation)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getJob(GetJobRequest request)
    
    
    public Job getJob(GetJobRequest request)

Gets a batch job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.GetJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.Job)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listBucketOperations(ListBucketOperationsRequest request)
    
    
    public ListBucketOperationsResponse listBucketOperations(ListBucketOperationsRequest request)

Lists BucketOperations in a given project and job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListBucketOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ListBucketOperationsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListBucketOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ListBucketOperationsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listJobs(ListJobsRequest request)
    
    
    public ListJobsResponse listJobs(ListJobsRequest request)

Lists Jobs in a given project.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ListJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storagebatchoperations/latest/com.google.cloud.storagebatchoperations.v1.ListJobsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
