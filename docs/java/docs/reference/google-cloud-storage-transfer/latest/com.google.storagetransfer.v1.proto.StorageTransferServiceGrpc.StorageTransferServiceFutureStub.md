---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceGrpc.StorageTransferServiceFutureStub
title: Class StorageTransferServiceGrpc.StorageTransferServiceFutureStub (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:45.476654+00:00
---

# Class StorageTransferServiceGrpc.StorageTransferServiceFutureStub (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceGrpc.StorageTransferServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StorageTransferServiceGrpc.StorageTransferServiceFutureStub (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.0.4 
    
    
    public static final class StorageTransferServiceGrpc.StorageTransferServiceFutureStub extends AbstractFutureStub<StorageTransferServiceGrpc.StorageTransferServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service StorageTransferService.

Storage Transfer Service and its protos. Transfers data between between Google Cloud Storage buckets or from a data source external to Google to a Cloud Storage bucket.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > StorageTransferServiceGrpc.StorageTransferServiceFutureStub

## Inherited Members

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractFutureStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected StorageTransferServiceGrpc.StorageTransferServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageTransferServiceGrpc.StorageTransferServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.StorageTransferServiceGrpc.StorageTransferServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createAgentPool(TransferProto.CreateAgentPoolRequest request)
    
    
    public ListenableFuture<TransferTypes.AgentPool> createAgentPool(TransferProto.CreateAgentPoolRequest request)

Creates an agent pool resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.CreateAgentPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.CreateAgentPoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AgentPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AgentPool)>` |   
  
### createTransferJob(TransferProto.CreateTransferJobRequest request)
    
    
    public ListenableFuture<TransferTypes.TransferJob> createTransferJob(TransferProto.CreateTransferJobRequest request)

Creates a transfer job that runs periodically.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.CreateTransferJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.CreateTransferJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob)>` |   
  
### deleteAgentPool(TransferProto.DeleteAgentPoolRequest request)
    
    
    public ListenableFuture<Empty> deleteAgentPool(TransferProto.DeleteAgentPoolRequest request)

Deletes an agent pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.DeleteAgentPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.DeleteAgentPoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteTransferJob(TransferProto.DeleteTransferJobRequest request)
    
    
    public ListenableFuture<Empty> deleteTransferJob(TransferProto.DeleteTransferJobRequest request)

Deletes a transfer job. Deleting a transfer job sets its status to DELETED.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.DeleteTransferJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.DeleteTransferJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getAgentPool(TransferProto.GetAgentPoolRequest request)
    
    
    public ListenableFuture<TransferTypes.AgentPool> getAgentPool(TransferProto.GetAgentPoolRequest request)

Gets an agent pool.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.GetAgentPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.GetAgentPoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AgentPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AgentPool)>` |   
  
### getGoogleServiceAccount(TransferProto.GetGoogleServiceAccountRequest request)
    
    
    public ListenableFuture<TransferTypes.GoogleServiceAccount> getGoogleServiceAccount(TransferProto.GetGoogleServiceAccountRequest request)

Returns the Google service account that is used by Storage Transfer Service to access buckets in the project where transfers run or in other projects. Each Google service account is associated with one Google Cloud project. Users should add this service account to the Google Cloud Storage bucket ACLs to grant access to Storage Transfer Service. This service account is created and owned by Storage Transfer Service and can only be used by Storage Transfer Service.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.GetGoogleServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.GetGoogleServiceAccountRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[GoogleServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.GoogleServiceAccount)>` |   
  
### getTransferJob(TransferProto.GetTransferJobRequest request)
    
    
    public ListenableFuture<TransferTypes.TransferJob> getTransferJob(TransferProto.GetTransferJobRequest request)

Gets a transfer job.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.GetTransferJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.GetTransferJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob)>` |   
  
### listAgentPools(TransferProto.ListAgentPoolsRequest request)
    
    
    public ListenableFuture<TransferProto.ListAgentPoolsResponse> listAgentPools(TransferProto.ListAgentPoolsRequest request)

Lists agent pools.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.ListAgentPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.ListAgentPoolsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAgentPoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.ListAgentPoolsResponse)>` |   
  
### listTransferJobs(TransferProto.ListTransferJobsRequest request)
    
    
    public ListenableFuture<TransferProto.ListTransferJobsResponse> listTransferJobs(TransferProto.ListTransferJobsRequest request)

Lists transfer jobs.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.ListTransferJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.ListTransferJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListTransferJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.ListTransferJobsResponse)>` |   
  
### pauseTransferOperation(TransferProto.PauseTransferOperationRequest request)
    
    
    public ListenableFuture<Empty> pauseTransferOperation(TransferProto.PauseTransferOperationRequest request)

Pauses a transfer operation.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.PauseTransferOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.PauseTransferOperationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### resumeTransferOperation(TransferProto.ResumeTransferOperationRequest request)
    
    
    public ListenableFuture<Empty> resumeTransferOperation(TransferProto.ResumeTransferOperationRequest request)

Resumes a transfer operation that is paused.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.ResumeTransferOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.ResumeTransferOperationRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### runTransferJob(TransferProto.RunTransferJobRequest request)
    
    
    public ListenableFuture<Operation> runTransferJob(TransferProto.RunTransferJobRequest request)

Starts a new operation for the specified transfer job. A `TransferJob` has a maximum of one active `TransferOperation`. If this method is called while a `TransferOperation` is active, an error is returned.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.RunTransferJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.RunTransferJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAgentPool(TransferProto.UpdateAgentPoolRequest request)
    
    
    public ListenableFuture<TransferTypes.AgentPool> updateAgentPool(TransferProto.UpdateAgentPoolRequest request)

Updates an existing agent pool resource.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.UpdateAgentPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.UpdateAgentPoolRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[AgentPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.AgentPool)>` |   
  
### updateTransferJob(TransferProto.UpdateTransferJobRequest request)
    
    
    public ListenableFuture<TransferTypes.TransferJob> updateTransferJob(TransferProto.UpdateTransferJobRequest request)

Updates a transfer job. Updating a job's transfer spec does not affect transfer operations that are running already. **Note:** The job's status field can be modified using this RPC (for example, to set a job's status to DELETED, DISABLED, or ENABLED).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TransferProto.UpdateTransferJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferProto.UpdateTransferJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[TransferJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferJob)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
