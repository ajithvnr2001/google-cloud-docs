---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceGrpc.NotebookServiceFutureStub
title: Class NotebookServiceGrpc.NotebookServiceFutureStub (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:42.485063+00:00
---

# Class NotebookServiceGrpc.NotebookServiceFutureStub (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceGrpc.NotebookServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NotebookServiceGrpc.NotebookServiceFutureStub (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static final class NotebookServiceGrpc.NotebookServiceFutureStub extends AbstractFutureStub<NotebookServiceGrpc.NotebookServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service NotebookService.

The interface for Vertex Notebook service (a.k.a. Colab on Workbench).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > NotebookServiceGrpc.NotebookServiceFutureStub

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

### assignNotebookRuntime(AssignNotebookRuntimeRequest request)
    
    
    public ListenableFuture<Operation> assignNotebookRuntime(AssignNotebookRuntimeRequest request)

Assigns a NotebookRuntime to a user for a particular Notebook file. This method will either returns an existing assignment or generates a new one.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AssignNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.AssignNotebookRuntimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected NotebookServiceGrpc.NotebookServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotebookServiceGrpc.NotebookServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookServiceGrpc.NotebookServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createNotebookExecutionJob(CreateNotebookExecutionJobRequest request)
    
    
    public ListenableFuture<Operation> createNotebookExecutionJob(CreateNotebookExecutionJobRequest request)

Creates a NotebookExecutionJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookExecutionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createNotebookRuntimeTemplate(CreateNotebookRuntimeTemplateRequest request)
    
    
    public ListenableFuture<Operation> createNotebookRuntimeTemplate(CreateNotebookRuntimeTemplateRequest request)

Creates a NotebookRuntimeTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CreateNotebookRuntimeTemplateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNotebookExecutionJob(DeleteNotebookExecutionJobRequest request)
    
    
    public ListenableFuture<Operation> deleteNotebookExecutionJob(DeleteNotebookExecutionJobRequest request)

Deletes a NotebookExecutionJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookExecutionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNotebookRuntime(DeleteNotebookRuntimeRequest request)
    
    
    public ListenableFuture<Operation> deleteNotebookRuntime(DeleteNotebookRuntimeRequest request)

Deletes a NotebookRuntime.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteNotebookRuntimeTemplate(DeleteNotebookRuntimeTemplateRequest request)
    
    
    public ListenableFuture<Operation> deleteNotebookRuntimeTemplate(DeleteNotebookRuntimeTemplateRequest request)

Deletes a NotebookRuntimeTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.DeleteNotebookRuntimeTemplateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getNotebookExecutionJob(GetNotebookExecutionJobRequest request)
    
    
    public ListenableFuture<NotebookExecutionJob> getNotebookExecutionJob(GetNotebookExecutionJobRequest request)

Gets a NotebookExecutionJob.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotebookExecutionJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookExecutionJobRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotebookExecutionJob](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookExecutionJob)>` |   
  
### getNotebookRuntime(GetNotebookRuntimeRequest request)
    
    
    public ListenableFuture<NotebookRuntime> getNotebookRuntime(GetNotebookRuntimeRequest request)

Gets a NotebookRuntime.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookRuntimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotebookRuntime](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntime)>` |   
  
### getNotebookRuntimeTemplate(GetNotebookRuntimeTemplateRequest request)
    
    
    public ListenableFuture<NotebookRuntimeTemplate> getNotebookRuntimeTemplate(GetNotebookRuntimeTemplateRequest request)

Gets a NotebookRuntimeTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.GetNotebookRuntimeTemplateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)>` |   
  
### listNotebookExecutionJobs(ListNotebookExecutionJobsRequest request)
    
    
    public ListenableFuture<ListNotebookExecutionJobsResponse> listNotebookExecutionJobs(ListNotebookExecutionJobsRequest request)

Lists NotebookExecutionJobs in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotebookExecutionJobsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookExecutionJobsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListNotebookExecutionJobsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookExecutionJobsResponse)>` |   
  
### listNotebookRuntimeTemplates(ListNotebookRuntimeTemplatesRequest request)
    
    
    public ListenableFuture<ListNotebookRuntimeTemplatesResponse> listNotebookRuntimeTemplates(ListNotebookRuntimeTemplatesRequest request)

Lists NotebookRuntimeTemplates in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotebookRuntimeTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimeTemplatesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListNotebookRuntimeTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimeTemplatesResponse)>` |   
  
### listNotebookRuntimes(ListNotebookRuntimesRequest request)
    
    
    public ListenableFuture<ListNotebookRuntimesResponse> listNotebookRuntimes(ListNotebookRuntimesRequest request)

Lists NotebookRuntimes in a Location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotebookRuntimesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListNotebookRuntimesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.ListNotebookRuntimesResponse)>` |   
  
### startNotebookRuntime(StartNotebookRuntimeRequest request)
    
    
    public ListenableFuture<Operation> startNotebookRuntime(StartNotebookRuntimeRequest request)

Starts a NotebookRuntime.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StartNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StartNotebookRuntimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### stopNotebookRuntime(StopNotebookRuntimeRequest request)
    
    
    public ListenableFuture<Operation> stopNotebookRuntime(StopNotebookRuntimeRequest request)

Stops a NotebookRuntime.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[StopNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StopNotebookRuntimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateNotebookRuntimeTemplate(UpdateNotebookRuntimeTemplateRequest request)
    
    
    public ListenableFuture<NotebookRuntimeTemplate> updateNotebookRuntimeTemplate(UpdateNotebookRuntimeTemplateRequest request)

Updates a NotebookRuntimeTemplate.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNotebookRuntimeTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpdateNotebookRuntimeTemplateRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[NotebookRuntimeTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.NotebookRuntimeTemplate)>` |   
  
### upgradeNotebookRuntime(UpgradeNotebookRuntimeRequest request)
    
    
    public ListenableFuture<Operation> upgradeNotebookRuntime(UpgradeNotebookRuntimeRequest request)

Upgrades a NotebookRuntime.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpgradeNotebookRuntimeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.UpgradeNotebookRuntimeRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
