---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub
title: Class SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:52.765839+00:00
---

# Class SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub extends AbstractBlockingStub<SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub>

A stub to allow clients to do synchronous rpc calls to service SubscriptionsService.

A service that manages subscriptions to Google Workspace events.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub

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
    
    
    protected SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.SubscriptionsServiceGrpc.SubscriptionsServiceBlockingV2Stub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createSubscription(CreateSubscriptionRequest request)
    
    
    public Operation createSubscription(CreateSubscriptionRequest request)

Creates a Google Workspace subscription. To learn how to use this method, see [Create a Google Workspace subscription](https://developers.google.com/workspace/events/guides/create-subscription).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.CreateSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### deleteSubscription(DeleteSubscriptionRequest request)
    
    
    public Operation deleteSubscription(DeleteSubscriptionRequest request)

Deletes a Google Workspace subscription. To learn how to use this method, see [Delete a Google Workspace subscription](https://developers.google.com/workspace/events/guides/delete-subscription).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.DeleteSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### getSubscription(GetSubscriptionRequest request)
    
    
    public Subscription getSubscription(GetSubscriptionRequest request)

Gets details about a Google Workspace subscription. To learn how to use this method, see [Get details about a Google Workspace subscription](https://developers.google.com/workspace/events/guides/get-subscription).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.GetSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.Subscription)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### listSubscriptions(ListSubscriptionsRequest request)
    
    
    public ListSubscriptionsResponse listSubscriptions(ListSubscriptionsRequest request)

Lists Google Workspace subscriptions. To learn how to use this method, see [List Google Workspace subscriptions](https://developers.google.com/workspace/events/guides/list-subscriptions).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.ListSubscriptionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.ListSubscriptionsResponse)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### reactivateSubscription(ReactivateSubscriptionRequest request)
    
    
    public Operation reactivateSubscription(ReactivateSubscriptionRequest request)

Reactivates a suspended Google Workspace subscription. This method resets your subscription's `State` field to `ACTIVE`. Before you use this method, you must fix the error that suspended the subscription. This method will ignore or reject any subscription that isn't currently in a suspended state. To learn how to use this method, see [Reactivate a Google Workspace subscription](https://developers.google.com/workspace/events/guides/reactivate-subscription).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ReactivateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.ReactivateSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`io.grpc.StatusException` |   
  
### updateSubscription(UpdateSubscriptionRequest request)
    
    
    public Operation updateSubscription(UpdateSubscriptionRequest request)

Updates or renews a Google Workspace subscription. To learn how to use this method, see [Update or renew a Google Workspace subscription](https://developers.google.com/workspace/events/guides/update-subscription).

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-workspaceevents/latest/com.google.apps.events.subscriptions.v1beta.UpdateSubscriptionRequest)`  
  
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

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
