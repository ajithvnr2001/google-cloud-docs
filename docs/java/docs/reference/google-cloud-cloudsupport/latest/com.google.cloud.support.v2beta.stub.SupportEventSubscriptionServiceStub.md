---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.stub.SupportEventSubscriptionServiceStub
title: Class SupportEventSubscriptionServiceStub (0.83.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:35.963335+00:00
---

# Class SupportEventSubscriptionServiceStub (0.83.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.stub.SupportEventSubscriptionServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SupportEventSubscriptionServiceStub (0.83.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.83.0 (latest)  0.79.0  0.78.0  0.77.0  0.75.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.54.0  0.52.0  0.51.0  0.48.0  0.47.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public abstract class SupportEventSubscriptionServiceStub implements BackgroundResource

Base stub class for the SupportEventSubscriptionService service API.

This class is for advanced usage and reflects the underlying API directly.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SupportEventSubscriptionServiceStub

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

### SupportEventSubscriptionServiceStub()
    
    
    public SupportEventSubscriptionServiceStub()

## Methods 

### close()
    
    
    public abstract void close()

### createSupportEventSubscriptionCallable()
    
    
    public UnaryCallable<CreateSupportEventSubscriptionRequest,SupportEventSubscription> createSupportEventSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSupportEventSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.CreateSupportEventSubscriptionRequest),[SupportEventSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.SupportEventSubscription)>` |   
  
### deleteSupportEventSubscriptionCallable()
    
    
    public UnaryCallable<DeleteSupportEventSubscriptionRequest,SupportEventSubscription> deleteSupportEventSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.DeleteSupportEventSubscriptionRequest),[SupportEventSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.SupportEventSubscription)>` |   
  
### expungeSupportEventSubscriptionCallable()
    
    
    public UnaryCallable<ExpungeSupportEventSubscriptionRequest,Empty> expungeSupportEventSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ExpungeSupportEventSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ExpungeSupportEventSubscriptionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getSupportEventSubscriptionCallable()
    
    
    public UnaryCallable<GetSupportEventSubscriptionRequest,SupportEventSubscription> getSupportEventSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSupportEventSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.GetSupportEventSubscriptionRequest),[SupportEventSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.SupportEventSubscription)>` |   
  
### listSupportEventSubscriptionsCallable()
    
    
    public UnaryCallable<ListSupportEventSubscriptionsRequest,ListSupportEventSubscriptionsResponse> listSupportEventSubscriptionsCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ListSupportEventSubscriptionsRequest),[ListSupportEventSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ListSupportEventSubscriptionsResponse)>` |   
  
### listSupportEventSubscriptionsPagedCallable()
    
    
    public UnaryCallable<ListSupportEventSubscriptionsRequest,SupportEventSubscriptionServiceClient.ListSupportEventSubscriptionsPagedResponse> listSupportEventSubscriptionsPagedCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSupportEventSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.ListSupportEventSubscriptionsRequest),[ListSupportEventSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.SupportEventSubscriptionServiceClient.ListSupportEventSubscriptionsPagedResponse)>` |   
  
### undeleteSupportEventSubscriptionCallable()
    
    
    public UnaryCallable<UndeleteSupportEventSubscriptionRequest,SupportEventSubscription> undeleteSupportEventSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UndeleteSupportEventSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.UndeleteSupportEventSubscriptionRequest),[SupportEventSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.SupportEventSubscription)>` |   
  
### updateSupportEventSubscriptionCallable()
    
    
    public UnaryCallable<UpdateSupportEventSubscriptionRequest,SupportEventSubscription> updateSupportEventSubscriptionCallable()

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSupportEventSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.UpdateSupportEventSubscriptionRequest),[SupportEventSubscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsupport/latest/com.google.cloud.support.v2beta.SupportEventSubscription)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
