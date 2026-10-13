---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.WorkloadManagerGrpc.WorkloadManagerStub
title: Class WorkloadManagerGrpc.WorkloadManagerStub (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:22.563103+00:00
---

# Class WorkloadManagerGrpc.WorkloadManagerStub (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.WorkloadManagerGrpc.WorkloadManagerStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WorkloadManagerGrpc.WorkloadManagerStub (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class WorkloadManagerGrpc.WorkloadManagerStub extends AbstractAsyncStub<WorkloadManagerGrpc.WorkloadManagerStub>

A stub to allow clients to do asynchronous rpc calls to service WorkloadManager.

The Workload Manager provides various tools to deploy, validate and observe your workloads running on Google Cloud.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > WorkloadManagerGrpc.WorkloadManagerStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

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
    
    
    protected WorkloadManagerGrpc.WorkloadManagerStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[WorkloadManagerGrpc.WorkloadManagerStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.WorkloadManagerGrpc.WorkloadManagerStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createEvaluation(CreateEvaluationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createEvaluation(CreateEvaluationRequest request, StreamObserver<Operation> responseObserver)

Creates a new Evaluation in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.CreateEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteEvaluation(DeleteEvaluationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteEvaluation(DeleteEvaluationRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.DeleteEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deleteExecution(DeleteExecutionRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deleteExecution(DeleteExecutionRequest request, StreamObserver<Operation> responseObserver)

Deletes a single Execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.DeleteExecutionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getEvaluation(GetEvaluationRequest request, StreamObserver<Evaluation> responseObserver)
    
    
    public void getEvaluation(GetEvaluationRequest request, StreamObserver<Evaluation> responseObserver)

Gets details of a single Evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.GetEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Evaluation](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.Evaluation)>`  
  
  
### getExecution(GetExecutionRequest request, StreamObserver<Execution> responseObserver)
    
    
    public void getExecution(GetExecutionRequest request, StreamObserver<Execution> responseObserver)

Gets details of a single Execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetExecutionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.GetExecutionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Execution](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.Execution)>`  
  
  
### listEvaluations(ListEvaluationsRequest request, StreamObserver<ListEvaluationsResponse> responseObserver)
    
    
    public void listEvaluations(ListEvaluationsRequest request, StreamObserver<ListEvaluationsResponse> responseObserver)

Lists Evaluations in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListEvaluationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListEvaluationsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListEvaluationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListEvaluationsResponse)>`  
  
  
### listExecutionResults(ListExecutionResultsRequest request, StreamObserver<ListExecutionResultsResponse> responseObserver)
    
    
    public void listExecutionResults(ListExecutionResultsRequest request, StreamObserver<ListExecutionResultsResponse> responseObserver)

Lists the result of a single evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListExecutionResultsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListExecutionResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListExecutionResultsResponse)>`  
  
  
### listExecutions(ListExecutionsRequest request, StreamObserver<ListExecutionsResponse> responseObserver)
    
    
    public void listExecutions(ListExecutionsRequest request, StreamObserver<ListExecutionsResponse> responseObserver)

Lists Executions in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListExecutionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListExecutionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListExecutionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListExecutionsResponse)>`  
  
  
### listRules(ListRulesRequest request, StreamObserver<ListRulesResponse> responseObserver)
    
    
    public void listRules(ListRulesRequest request, StreamObserver<ListRulesResponse> responseObserver)

Lists rules in a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListRulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListRulesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListRulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListRulesResponse)>`  
  
  
### listScannedResources(ListScannedResourcesRequest request, StreamObserver<ListScannedResourcesResponse> responseObserver)
    
    
    public void listScannedResources(ListScannedResourcesRequest request, StreamObserver<ListScannedResourcesResponse> responseObserver)

List all scanned resources for a single Execution.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListScannedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListScannedResourcesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListScannedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.ListScannedResourcesResponse)>`  
  
  
### runEvaluation(RunEvaluationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void runEvaluation(RunEvaluationRequest request, StreamObserver<Operation> responseObserver)

Creates a new Execution in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RunEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.RunEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### updateEvaluation(UpdateEvaluationRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updateEvaluation(UpdateEvaluationRequest request, StreamObserver<Operation> responseObserver)

Updates the parameters of a single Evaluation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateEvaluationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workloadmanager/latest/com.google.cloud.workloadmanager.v1.UpdateEvaluationRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
