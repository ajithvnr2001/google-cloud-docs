---
url: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.IAMPolicyGrpc.IAMPolicyBlockingV2Stub
title: Class IAMPolicyGrpc.IAMPolicyBlockingV2Stub (1.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:38.730344+00:00
---

# Class IAMPolicyGrpc.IAMPolicyBlockingV2Stub (1.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.IAMPolicyGrpc.IAMPolicyBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class IAMPolicyGrpc.IAMPolicyBlockingV2Stub (1.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.73.0 (latest)  1.69.0  1.68.0  1.67.0  1.65.0  1.62.0  1.61.0  1.60.1  1.59.1  1.58.2  1.57.0  1.56.3  1.55.0  1.54.2  1.53.0  1.52.0  1.51.0  1.49.1  1.48.0  1.47.0  1.46.0  1.45.1  1.44.0  1.43.0  1.41.0  1.40.1  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.0  1.29.0  1.28.0  1.27.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.0  1.18.1  1.17.1  1.16.1  1.10.0  1.9.3  1.8.0  1.7.0  1.6.23  1.5.1  1.4.1  1.3.4  1.2.12 
    
    
    public static final class IAMPolicyGrpc.IAMPolicyBlockingV2Stub extends AbstractBlockingStub<IAMPolicyGrpc.IAMPolicyBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service IAMPolicy.

API Overview Manages Identity and Access Management (IAM) policies. Any implementation of an API that offers access control features implements the google.iam.v1.IAMPolicy interface.

## Data model

Access control is applied when a principal (user or service account), takes some action on a resource exposed by a service. Resources, identified by URI-like names, are the unit of access control specification. Service implementations can choose the granularity of access control and the supported permissions for their resources. For example one database service may allow access control to be specified only at the Table level, whereas another might allow access control to also be specified at the Column level.

## Policy Structure

See google.iam.v1.Policy This is intentionally not a CRUD style API because access control policies are created and deleted implicitly with the resources to which they are attached.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > IAMPolicyGrpc.IAMPolicyBlockingV2Stub

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
    
    
    protected IAMPolicyGrpc.IAMPolicyBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[IAMPolicyGrpc.IAMPolicyBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.IAMPolicyGrpc.IAMPolicyBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### getIamPolicy(GetIamPolicyRequest request)
    
    
    public Policy getIamPolicy(GetIamPolicyRequest request)

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### setIamPolicy(SetIamPolicyRequest request)
    
    
    public Policy setIamPolicy(SetIamPolicyRequest request)

Sets the access control policy on the specified resource. Replaces any existing policy. Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### testIamPermissions(TestIamPermissionsRequest request)
    
    
    public TestIamPermissionsResponse testIamPermissions(TestIamPermissionsRequest request)

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error. Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[TestIamPermissionsRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TestIamPermissionsResponse](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.TestIamPermissionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
