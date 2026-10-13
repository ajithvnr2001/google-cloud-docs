---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub
title: Class OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:23.416775+00:00
---

# Class OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub extends AbstractBlockingStub<OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service OnlineReturnPolicyService.

The service facilitates the management of a business's remorse return policy configuration, encompassing return policies for both ads and free listings

## programs. This API defines the following resource model:

OnlineReturnPolicy

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub

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
    
    
    protected OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicyServiceGrpc.OnlineReturnPolicyServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createOnlineReturnPolicy(CreateOnlineReturnPolicyRequest request)
    
    
    public OnlineReturnPolicy createOnlineReturnPolicy(CreateOnlineReturnPolicyRequest request)

Creates a new return policy for a given business.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateOnlineReturnPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.CreateOnlineReturnPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OnlineReturnPolicy](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicy)` |   
  
### deleteOnlineReturnPolicy(DeleteOnlineReturnPolicyRequest request)
    
    
    public Empty deleteOnlineReturnPolicy(DeleteOnlineReturnPolicyRequest request)

Deletes an existing return policy.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteOnlineReturnPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.DeleteOnlineReturnPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### getOnlineReturnPolicy(GetOnlineReturnPolicyRequest request)
    
    
    public OnlineReturnPolicy getOnlineReturnPolicy(GetOnlineReturnPolicyRequest request)

Gets an existing return policy for a given business.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetOnlineReturnPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.GetOnlineReturnPolicyRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OnlineReturnPolicy](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.OnlineReturnPolicy)` |   
  
### listOnlineReturnPolicies(ListOnlineReturnPoliciesRequest request)
    
    
    public ListOnlineReturnPoliciesResponse listOnlineReturnPolicies(ListOnlineReturnPoliciesRequest request)

Lists all existing return policies for a given business.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListOnlineReturnPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ListOnlineReturnPoliciesRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListOnlineReturnPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1.ListOnlineReturnPoliciesResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
