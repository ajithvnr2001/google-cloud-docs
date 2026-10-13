---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceFutureStub
title: Class DataAgentServiceGrpc.DataAgentServiceFutureStub (0.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:49.450215+00:00
---

# Class DataAgentServiceGrpc.DataAgentServiceFutureStub (0.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceFutureStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataAgentServiceGrpc.DataAgentServiceFutureStub (0.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.27.0 (latest)  0.23.0  0.22.0  0.21.0  0.19.0  0.16.0  0.15.0  0.13.0  0.11.0  0.10.0  0.9.0  0.8.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class DataAgentServiceGrpc.DataAgentServiceFutureStub extends AbstractFutureStub<DataAgentServiceGrpc.DataAgentServiceFutureStub>

A stub to allow clients to do ListenableFuture-style rpc calls to service DataAgentService.

Service describing handlers for resources.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractFutureStub > DataAgentServiceGrpc.DataAgentServiceFutureStub

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
    
    
    protected DataAgentServiceGrpc.DataAgentServiceFutureStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[DataAgentServiceGrpc.DataAgentServiceFutureStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgentServiceGrpc.DataAgentServiceFutureStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createDataAgent(CreateDataAgentRequest request)
    
    
    public ListenableFuture<Operation> createDataAgent(CreateDataAgentRequest request)

Creates a new DataAgent in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.CreateDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createDataAgentSync(CreateDataAgentRequest request)
    
    
    public ListenableFuture<DataAgent> createDataAgentSync(CreateDataAgentRequest request)

Creates a new DataAgent in a given project and location synchronously.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.CreateDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DataAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent)>` |   
  
### deleteDataAgent(DeleteDataAgentRequest request)
    
    
    public ListenableFuture<Operation> deleteDataAgent(DeleteDataAgentRequest request)

Deletes a single DataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DeleteDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteDataAgentSync(DeleteDataAgentRequest request)
    
    
    public ListenableFuture<Empty> deleteDataAgentSync(DeleteDataAgentRequest request)

Deletes a single DataAgent synchronously.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DeleteDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getDataAgent(GetDataAgentRequest request)
    
    
    public ListenableFuture<DataAgent> getDataAgent(GetDataAgentRequest request)

Gets details of a single DataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.GetDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DataAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent)>` |   
  
### getIamPolicy(GetIamPolicyRequest request)
    
    
    public ListenableFuture<Policy> getIamPolicy(GetIamPolicyRequest request)

Gets the IAM policy for DataAgent

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.GetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.Policy>` |   
  
### listAccessibleDataAgents(ListAccessibleDataAgentsRequest request)
    
    
    public ListenableFuture<ListAccessibleDataAgentsResponse> listAccessibleDataAgents(ListAccessibleDataAgentsRequest request)

Lists DataAgents that are accessible to the caller in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListAccessibleDataAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListAccessibleDataAgentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListAccessibleDataAgentsResponse)>` |   
  
### listDataAgents(ListDataAgentsRequest request)
    
    
    public ListenableFuture<ListDataAgentsResponse> listDataAgents(ListDataAgentsRequest request)

Lists DataAgents in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListDataAgentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListDataAgentsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[ListDataAgentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.ListDataAgentsResponse)>` |   
  
### retrieveAgentOpsObservability(RetrieveAgentOpsObservabilityRequest request)
    
    
    public ListenableFuture<RetrieveAgentOpsObservabilityResponse> retrieveAgentOpsObservability(RetrieveAgentOpsObservabilityRequest request)

Gets AgentOps observability settings and status of required services.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.RetrieveAgentOpsObservabilityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[RetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.RetrieveAgentOpsObservabilityResponse)>` |   
  
### setAgentOpsObservability(SetAgentOpsObservabilityRequest request)
    
    
    public ListenableFuture<Operation> setAgentOpsObservability(SetAgentOpsObservabilityRequest request)

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetAgentOpsObservabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.SetAgentOpsObservabilityRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public ListenableFuture<Policy> setIamPolicy(SetIamPolicyRequest request)

Sets the IAM policy for a DataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `com.google.iam.v1.SetIamPolicyRequest`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<com.google.iam.v1.Policy>` |   
  
### updateDataAgent(UpdateDataAgentRequest request)
    
    
    public ListenableFuture<Operation> updateDataAgent(UpdateDataAgentRequest request)

Updates the parameters of a single DataAgent.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.UpdateDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateDataAgentSync(UpdateDataAgentRequest request)
    
    
    public ListenableFuture<DataAgent> updateDataAgentSync(UpdateDataAgentRequest request)

Updates the parameters of a single DataAgent synchronously.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateDataAgentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.UpdateDataAgentRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.util.concurrent.ListenableFuture<[DataAgent](https://docs.cloud.google.com/java/docs/reference/google-cloud-geminidataanalytics/latest/com.google.cloud.geminidataanalytics.v1.DataAgent)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
