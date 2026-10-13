---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.PolicyBindingsGrpc.PolicyBindingsStub
title: Class PolicyBindingsGrpc.PolicyBindingsStub (1.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:48.245811+00:00
---

# Class PolicyBindingsGrpc.PolicyBindingsStub (1.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.PolicyBindingsGrpc.PolicyBindingsStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class PolicyBindingsGrpc.PolicyBindingsStub (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.73.0 (latest)  1.69.0  1.68.0  1.67.0  1.65.0  1.62.0  1.61.0  1.60.1  1.59.1  1.58.2  1.57.0  1.56.3  1.55.0  1.54.2  1.53.0  1.52.0  1.51.0  1.49.1  1.48.0  1.47.0  1.46.0  1.45.1  1.44.0  1.43.0  1.41.0  1.40.1  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.0  1.29.0  1.28.0  1.27.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.1  1.17.1  1.16.1  1.10.0  1.9.3  1.8.0  1.7.0  1.6.23  1.5.1  1.4.1  1.3.4  1.2.12 
    
    
    public static final class PolicyBindingsGrpc.PolicyBindingsStub extends AbstractAsyncStub<PolicyBindingsGrpc.PolicyBindingsStub>

A stub to allow clients to do asynchronous rpc calls to service PolicyBindings.

An interface for managing Identity and Access Management (IAM) policy bindings.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > PolicyBindingsGrpc.PolicyBindingsStub

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
    
    
    protected PolicyBindingsGrpc.PolicyBindingsStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[PolicyBindingsGrpc.PolicyBindingsStub](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.PolicyBindingsGrpc.PolicyBindingsStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createPolicyBinding(CreatePolicyBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void createPolicyBinding(CreatePolicyBindingRequest request, StreamObserver<Operation> responseObserver)

Creates a policy binding and returns a long-running operation. Callers will need the IAM permissions on both the policy and target. After the binding is created, the policy is applied to the target.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreatePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.CreatePolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### deletePolicyBinding(DeletePolicyBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void deletePolicyBinding(DeletePolicyBindingRequest request, StreamObserver<Operation> responseObserver)

Deletes a policy binding and returns a long-running operation. Callers will need the IAM permissions on both the policy and target. After the binding is deleted, the policy no longer applies to the target.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeletePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.DeletePolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
### getPolicyBinding(GetPolicyBindingRequest request, StreamObserver<PolicyBinding> responseObserver)
    
    
    public void getPolicyBinding(GetPolicyBindingRequest request, StreamObserver<PolicyBinding> responseObserver)

Gets a policy binding.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetPolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.GetPolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PolicyBinding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.PolicyBinding)>`  
  
  
### listPolicyBindings(ListPolicyBindingsRequest request, StreamObserver<ListPolicyBindingsResponse> responseObserver)
    
    
    public void listPolicyBindings(ListPolicyBindingsRequest request, StreamObserver<ListPolicyBindingsResponse> responseObserver)

Lists policy bindings.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.ListPolicyBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.ListPolicyBindingsResponse)>`  
  
  
### searchTargetPolicyBindings(SearchTargetPolicyBindingsRequest request, StreamObserver<SearchTargetPolicyBindingsResponse> responseObserver)
    
    
    public void searchTargetPolicyBindings(SearchTargetPolicyBindingsRequest request, StreamObserver<SearchTargetPolicyBindingsResponse> responseObserver)

Search policy bindings by target. Returns all policy binding objects bound directly to target.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchTargetPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.SearchTargetPolicyBindingsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.SearchTargetPolicyBindingsResponse)>`  
  
  
### updatePolicyBinding(UpdatePolicyBindingRequest request, StreamObserver<Operation> responseObserver)
    
    
    public void updatePolicyBinding(UpdatePolicyBindingRequest request, StreamObserver<Operation> responseObserver)

Updates a policy binding and returns a long-running operation. Callers will need the IAM permissions on the policy and target in the binding to update. Target and policy are immutable and cannot be updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdatePolicyBindingRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v3beta.UpdatePolicyBindingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
