---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ParallelstoreGrpc.ParallelstoreBlockingV2Stub
title: Class ParallelstoreGrpc.ParallelstoreBlockingV2Stub (0.62.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:10:16.532356+00:00
---

# Class ParallelstoreGrpc.ParallelstoreBlockingV2Stub (0.62.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ParallelstoreGrpc.ParallelstoreBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ParallelstoreGrpc.ParallelstoreBlockingV2Stub (0.62.0) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static final class ParallelstoreGrpc.ParallelstoreBlockingV2Stub extends AbstractBlockingStub<ParallelstoreGrpc.ParallelstoreBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service Parallelstore.

Service describing handlers for resources Configures and manages parallelstore resources. Parallelstore service. The `parallelstore.googleapis.com` service implements the parallelstore API and defines the following resource model for managing instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of instances named `/instances/*`.
  * Parallelstore instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}` Note that location_id must be a Google Cloud `zone`; for example:
  * `projects/12345/locations/us-central1-c/instances/my-parallelstore-share`



## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ParallelstoreGrpc.ParallelstoreBlockingV2Stub

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
    
    
    protected ParallelstoreGrpc.ParallelstoreBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ParallelstoreGrpc.ParallelstoreBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ParallelstoreGrpc.ParallelstoreBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createInstance(CreateInstanceRequest request)
    
    
    public Operation createInstance(CreateInstanceRequest request)

Creates a Parallelstore instance in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.CreateInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteInstance(DeleteInstanceRequest request)
    
    
    public Operation deleteInstance(DeleteInstanceRequest request)

Deletes a single instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.DeleteInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### exportData(ExportDataRequest request)
    
    
    public Operation exportData(ExportDataRequest request)

Copies data from Parallelstore to Cloud Storage.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ExportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ExportDataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getInstance(GetInstanceRequest request)
    
    
    public Instance getInstance(GetInstanceRequest request)

Gets details of a single instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.GetInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.Instance)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### importData(ImportDataRequest request)
    
    
    public Operation importData(ImportDataRequest request)

Copies data from Cloud Storage to Parallelstore.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ImportDataRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ImportDataRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listInstances(ListInstancesRequest request)
    
    
    public ListInstancesResponse listInstances(ListInstancesRequest request)

Lists all instances in a given project and location.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ListInstancesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.ListInstancesResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateInstance(UpdateInstanceRequest request)
    
    
    public Operation updateInstance(UpdateInstanceRequest request)

Updates the parameters of a single instance.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-parallelstore/latest/com.google.cloud.parallelstore.v1beta.UpdateInstanceRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
