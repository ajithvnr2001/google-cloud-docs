---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataSubscriptionServiceStub
title: Class DataSubscriptionServiceStub (0.8.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:55.462802+00:00
---

# Class DataSubscriptionServiceStub (0.8.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.stub.DataSubscriptionServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class DataSubscriptionServiceStub (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.8.0 (latest)  0.4.0  0.3.0  0.2.0 
    
    
    public abstract class DataSubscriptionServiceStub implements BackgroundResource

Base stub class for the DataSubscriptionService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DataSubscriptionServiceStub

## Implements

[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource.html)

## Inherited Members

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

## Constructors 

### DataSubscriptionServiceStub()
    
    
    public DataSubscriptionServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createSubscriberCallable()
    
    
    public UnaryCallable<CreateSubscriberRequest,Operation> createSubscriberCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSubscriberOperationCallable()
    
    
    public OperationCallable<CreateSubscriberRequest,Subscriber,CreateSubscriberMetadata> createSubscriberOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[CreateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberRequest),[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[CreateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriberMetadata)>` |   
  
### createSubscriptionCallable()
    
    
    public UnaryCallable<CreateSubscriptionRequest,Subscription> createSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.CreateSubscriptionRequest),[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)>` |   
  
### deleteSubscriberCallable()
    
    
    public UnaryCallable<DeleteSubscriberRequest,Operation> deleteSubscriberCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSubscriberOperationCallable()
    
    
    public OperationCallable<DeleteSubscriberRequest,Empty,DeleteSubscriberMetadata> deleteSubscriberOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[DeleteSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[DeleteSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriberMetadata)>` |   
  
### deleteSubscriptionCallable()
    
    
    public UnaryCallable<DeleteSubscriptionRequest,Empty> deleteSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DeleteSubscriptionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getHttpJsonOperationsStub()
    
    
    public @Nullable OperationsStub getHttpJsonOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.gax.httpjson.longrunning.stub.OperationsStub` |   
  
### getOperationsStub()
    
    
    public @Nullable OperationsStub getOperationsStub()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.longrunning.stub.OperationsStub` |   
  
### listSubscribersCallable()
    
    
    public UnaryCallable<ListSubscribersRequest,ListSubscribersResponse> listSubscribersCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersRequest),[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersResponse)>` |   
  
### listSubscribersPagedCallable()
    
    
    public UnaryCallable<ListSubscribersRequest,DataSubscriptionServiceClient.ListSubscribersPagedResponse> listSubscribersPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscribersRequest),[ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscribersPagedResponse)>` |   
  
### listSubscriptionsCallable()
    
    
    public UnaryCallable<ListSubscriptionsRequest,ListSubscriptionsResponse> listSubscriptionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsRequest),[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsResponse)>` |   
  
### listSubscriptionsPagedCallable()
    
    
    public UnaryCallable<ListSubscriptionsRequest,DataSubscriptionServiceClient.ListSubscriptionsPagedResponse> listSubscriptionsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.ListSubscriptionsRequest),[ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.DataSubscriptionServiceClient.ListSubscriptionsPagedResponse)>` |   
  
### updateSubscriberCallable()
    
    
    public UnaryCallable<UpdateSubscriberRequest,Operation> updateSubscriberCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSubscriberOperationCallable()
    
    
    public OperationCallable<UpdateSubscriberRequest,Subscriber,UpdateSubscriberMetadata> updateSubscriberOperationCallable()

**Returns**  
---  
**Type** | **Description**  
`[OperationCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallable.html)<[UpdateSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberRequest),[Subscriber](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscriber),[UpdateSubscriberMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriberMetadata)>` |   
  
### updateSubscriptionCallable()
    
    
    public UnaryCallable<UpdateSubscriptionRequest,Subscription> updateSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.UpdateSubscriptionRequest),[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-health/latest/com.google.devicesandservices.health.v4.Subscription)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
