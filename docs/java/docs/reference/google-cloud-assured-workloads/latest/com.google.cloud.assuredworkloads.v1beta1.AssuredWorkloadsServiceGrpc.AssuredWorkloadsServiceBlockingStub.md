---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub
title: Class AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:47.866003+00:00
---

# Class AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.1.0  2.0.0  1.1.0  1.0.4  0.9.0  0.8.2 
    
    
    public static final class AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub extends AbstractBlockingStub<AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service AssuredWorkloadsService.

Service to manage AssuredWorkloads.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub

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

### analyzeWorkloadMove(AnalyzeWorkloadMoveRequest request)
    
    
    public AnalyzeWorkloadMoveResponse analyzeWorkloadMove(AnalyzeWorkloadMoveRequest request)

Analyze if the source Assured Workloads can be moved to the target Assured Workload

**Parameter**  
---  
**Name** | **Description**  
`request` | `[AnalyzeWorkloadMoveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AnalyzeWorkloadMoveRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyzeWorkloadMoveResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AnalyzeWorkloadMoveResponse)` |   
  
### build(Channel channel, CallOptions callOptions)
    
    
    protected AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.AssuredWorkloadsServiceGrpc.AssuredWorkloadsServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createWorkload(CreateWorkloadRequest request)
    
    
    public Operation createWorkload(CreateWorkloadRequest request)

Creates Assured Workload.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.CreateWorkloadRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### deleteWorkload(DeleteWorkloadRequest request)
    
    
    public Empty deleteWorkload(DeleteWorkloadRequest request)

Deletes the workload. Make sure that workload's direct children are already in a deleted state, otherwise the request will fail with a FAILED_PRECONDITION error. In addition to assuredworkloads.workload.delete permission, the user should also have orgpolicy.policy.set permission on the deleted folder to remove Assured Workloads OrgPolicies.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.DeleteWorkloadRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### getWorkload(GetWorkloadRequest request)
    
    
    public Workload getWorkload(GetWorkloadRequest request)

Gets Assured Workload associated with a CRM Node

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.GetWorkloadRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload)` |   
  
### listWorkloads(ListWorkloadsRequest request)
    
    
    public ListWorkloadsResponse listWorkloads(ListWorkloadsRequest request)

Lists Assured Workloads under a CRM Node.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListWorkloadsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.ListWorkloadsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListWorkloadsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.ListWorkloadsResponse)` |   
  
### restrictAllowedResources(RestrictAllowedResourcesRequest request)
    
    
    public RestrictAllowedResourcesResponse restrictAllowedResources(RestrictAllowedResourcesRequest request)

Restrict the list of resources allowed in the Workload environment. The current list of allowed products can be found at <https://cloud.google.com/assured-workloads/docs/supported-products> In addition to assuredworkloads.workload.update permission, the user should also have orgpolicy.policy.set permission on the folder resource to use this functionality.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RestrictAllowedResourcesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RestrictAllowedResourcesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse)` |   
  
### updateWorkload(UpdateWorkloadRequest request)
    
    
    public Workload updateWorkload(UpdateWorkloadRequest request)

Updates an existing workload. Currently allows updating of workload display_name and labels. For force updates don't set etag field in the Workload. Only one update operation per workload can be in progress.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateWorkloadRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.UpdateWorkloadRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Workload](https://docs.cloud.google.com/java/docs/reference/google-cloud-assured-workloads/latest/com.google.cloud.assuredworkloads.v1beta1.Workload)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
