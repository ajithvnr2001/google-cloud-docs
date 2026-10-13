---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.internal.WrappingPublisher
title: Class WrappingPublisher (1.16.5) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:20.701152+00:00
---

# Class WrappingPublisher (1.16.5)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.internal.WrappingPublisher

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class WrappingPublisher (1.16.5) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.5 (latest)  1.16.2  1.15.21  1.14.8  1.13.8  1.12.22  1.11.2  1.10.0  1.9.4  1.8.0  1.7.1  1.6.3  1.5.5  1.4.12 
    
    
    public class WrappingPublisher extends ProxyService implements Publisher

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [AbstractApiService](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html) > [ProxyService](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService) > WrappingPublisher

## Implements

[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.cloudpubsub.Publisher)

## Inherited Members

[AbstractApiService.addListener(ApiService.Listener,Executor)](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_addListener_com_google_api_core_ApiService_Listener_java_util_concurrent_Executor_)

[AbstractApiService.awaitRunning()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_awaitRunning__)

[AbstractApiService.awaitRunning(long,TimeUnit)](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_awaitRunning_long_java_util_concurrent_TimeUnit_)

[AbstractApiService.awaitTerminated()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_awaitTerminated__)

[AbstractApiService.awaitTerminated(long,TimeUnit)](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_awaitTerminated_long_java_util_concurrent_TimeUnit_)

[AbstractApiService.failureCause()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_failureCause__)

[AbstractApiService.isRunning()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_isRunning__)

[AbstractApiService.notifyFailed(Throwable)](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_notifyFailed_java_lang_Throwable_)

[AbstractApiService.notifyStarted()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_notifyStarted__)

[AbstractApiService.notifyStopped()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_notifyStopped__)

[AbstractApiService.startAsync()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_startAsync__)

[AbstractApiService.state()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_state__)

[AbstractApiService.stopAsync()](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.AbstractApiService.html#com_google_api_core_AbstractApiService_stopAsync__)

[ProxyService.<T>addServices(Collection<T>)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService__T_addServices_java_util_Collection_T__)

[ProxyService.addServices(ApiService)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_addServices_com_google_api_core_ApiService____)

[ProxyService.doStart()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_doStart__)

[ProxyService.doStop()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_doStop__)

[ProxyService.handlePermanentError(CheckedApiException)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_handlePermanentError_com_google_cloud_pubsublite_internal_CheckedApiException_)

[ProxyService.onPermanentError(CheckedApiException)](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_onPermanentError_com_google_cloud_pubsublite_internal_CheckedApiException_)

[ProxyService.start()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_start__)

[ProxyService.stop()](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.ProxyService#com_google_cloud_pubsublite_internal_ProxyService_stop__)

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

### WrappingPublisher(Publisher<MessageMetadata> wirePublisher, MessageTransformer<PubsubMessage,Message> transformer)
    
    
    public WrappingPublisher(Publisher<MessageMetadata> wirePublisher, MessageTransformer<PubsubMessage,Message> transformer)

**Parameters**  
---  
**Name** | **Description**  
`wirePublisher` | `[Publisher](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.internal.Publisher)<[MessageMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageMetadata)>`  
  
`transformer` | `[MessageTransformer](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.MessageTransformer)<com.google.pubsub.v1.PubsubMessage,[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-pubsublite/latest/com.google.cloud.pubsublite.Message)>`  
  
  
## Methods 

### publish(PubsubMessage message)
    
    
    public ApiFuture<String> publish(PubsubMessage message)

**Parameter**  
---  
**Name** | **Description**  
`message` | `com.google.pubsub.v1.PubsubMessage`  
  
**Returns**  
---  
**Type** | **Description**  
`[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-26 UTC."],[],[]] 
