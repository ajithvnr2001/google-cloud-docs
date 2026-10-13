---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub
title: Class NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:45:10.234121+00:00
---

# Class NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static final class NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub extends AbstractBlockingStub<NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service NotificationsApiService.

Service to manage notification subscriptions for merchants

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub

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
    
    
    protected NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationsApiServiceGrpc.NotificationsApiServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### createNotificationSubscription(CreateNotificationSubscriptionRequest request)
    
    
    public NotificationSubscription createNotificationSubscription(CreateNotificationSubscriptionRequest request)

Creates a notification subscription for a business. For standalone or subaccounts accounts, the business can create a subscription for self. For MCAs, the business can create a subscription for all managed accounts or for a specific subaccount. We will allow the following types of notification subscriptions to exist together (per business as a subscriber per event type):

  1. Subscription for all managed accounts + subscription for self.
  2. Multiple "partial" subscriptions for managed accounts + subscription for self. we will not allow (per business as a subscriber per event type):
  3. Multiple self subscriptions.
  4. Multiple "all managed accounts" subscriptions.
  5. "All managed accounts" subscription and partial subscriptions at the same time.
  6. Multiple partial subscriptions for the same target account.



**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateNotificationSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.CreateNotificationSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotificationSubscription](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationSubscription)` |   
  
### deleteNotificationSubscription(DeleteNotificationSubscriptionRequest request)
    
    
    public Empty deleteNotificationSubscription(DeleteNotificationSubscriptionRequest request)

Deletes a notification subscription for a merchant.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteNotificationSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.DeleteNotificationSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)` |   
  
### getNotificationSubscription(GetNotificationSubscriptionRequest request)
    
    
    public NotificationSubscription getNotificationSubscription(GetNotificationSubscriptionRequest request)

Gets notification subscriptions for an account.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotificationSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.GetNotificationSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotificationSubscription](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationSubscription)` |   
  
### getNotificationSubscriptionHealthMetrics(GetNotificationSubscriptionHealthMetricsRequest request)
    
    
    public NotificationSubscriptionHealthMetrics getNotificationSubscriptionHealthMetrics(GetNotificationSubscriptionHealthMetricsRequest request)

Retrieves notification subscription health metrics for a merchant. We recommend calling this periodically (hourly or daily) to monitor health of your callback endpoint.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetNotificationSubscriptionHealthMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.GetNotificationSubscriptionHealthMetricsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotificationSubscriptionHealthMetrics](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationSubscriptionHealthMetrics)` |   
  
### listNotificationSubscriptions(ListNotificationSubscriptionsRequest request)
    
    
    public ListNotificationSubscriptionsResponse listNotificationSubscriptions(ListNotificationSubscriptionsRequest request)

Gets all the notification subscriptions for a merchant.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListNotificationSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.ListNotificationSubscriptionsRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListNotificationSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.ListNotificationSubscriptionsResponse)` |   
  
### updateNotificationSubscription(UpdateNotificationSubscriptionRequest request)
    
    
    public NotificationSubscription updateNotificationSubscription(UpdateNotificationSubscriptionRequest request)

Updates an existing notification subscription for a merchant.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateNotificationSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.UpdateNotificationSubscriptionRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NotificationSubscription](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-notifications/latest/com.google.shopping.merchant.notifications.v1.NotificationSubscription)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
