---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingCallSettings
title: Class BatchingCallSettings<ElementT,ElementResultT,RequestT,ResponseT> (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:38:13.981515+00:00
---

# Class BatchingCallSettings<ElementT,ElementResultT,RequestT,ResponseT> (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingCallSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BatchingCallSettings<ElementT,ElementResultT,RequestT,ResponseT> (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public final class BatchingCallSettings<ElementT,ElementResultT,RequestT,ResponseT> extends UnaryCallSettings<RequestT,ResponseT>

This is an extension of [UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings) class to configure a [UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable) for calls to an API method that supports batching. The batching settings are provided using the instance of [BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings).

Retry configuration will be applied on each batching RPC request.

Sample settings configuration:
    
    
     BatchingCallSettings batchingCallSettings = // Default BatchingCallSettings from the client
     BatchingCallSettings customBatchingCallSettings =
         batchingCallSettings
             .toBuilder()
             .setRetryableCodes(StatusCode.Code.UNAVAILABLE, ...)
             .setRetrySettings(RetrySettings.newBuilder()...build())
             .setBatchingSettings(BatchingSettings.newBuilder()...build())
             .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings) > BatchingCallSettings<ElementT,ElementResultT,RequestT,ResponseT>

## Inherited Members

[UnaryCallSettings.<RequestT,ResponseT>newUnaryCallSettingsBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings__RequestT_ResponseT_newUnaryCallSettingsBuilder__)

[UnaryCallSettings.equals(@Nullable Object)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_equals__org_jspecify_annotations_Nullable_java_lang_Object_)

[UnaryCallSettings.getRetrySettings()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_getRetrySettings__)

[UnaryCallSettings.getRetryableCodes()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_getRetryableCodes__)

[UnaryCallSettings.hashCode()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_hashCode__)

[UnaryCallSettings.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_toBuilder__)

[UnaryCallSettings.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Type Parameters  
  
---  
**Name** | **Description**  
`ElementT` |   
`ElementResultT` |   
`RequestT` |   
`ResponseT` |   
  
## Static Methods 

### <ElementT,ElementResultT,RequestT,ResponseT>newBuilder(BatchingDescriptor<ElementT,ElementResultT,RequestT,ResponseT> batchingDescriptor)
    
    
    public static BatchingCallSettings.Builder<ElementT,ElementResultT,RequestT,ResponseT> <ElementT,ElementResultT,RequestT,ResponseT>newBuilder(BatchingDescriptor<ElementT,ElementResultT,RequestT,ResponseT> batchingDescriptor)

**Internal Only** : This feature is not stable for application use.

_For google-cloud-java client use only_

Please use [#toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingCallSettings#com_google_api_gax_batching_BatchingCallSettings_toBuilder__) to override settings values.

**Parameter**  
---  
**Name** | **Description**  
`batchingDescriptor` | `[BatchingDescriptor](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingDescriptor)<ElementT,ElementResultT,RequestT,ResponseT>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingCallSettings.Builder)<ElementT,ElementResultT,RequestT,ResponseT>` |   
  
## Methods 

### getBatchingDescriptor()
    
    
    public BatchingDescriptor<ElementT,ElementResultT,RequestT,ResponseT> getBatchingDescriptor()

**Internal Only** : This feature is not stable for application use.

_For google-cloud-java client use only_

**Returns**  
---  
**Type** | **Description**  
`[BatchingDescriptor](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingDescriptor)<ElementT,ElementResultT,RequestT,ResponseT>` |   
  
### getBatchingSettings()
    
    
    public BatchingSettings getBatchingSettings()

Returns batching settings which contains multiple batch threshold levels.

**Returns**  
---  
**Type** | **Description**  
`[BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings)` |   
  
### toBuilder()
    
    
    public final BatchingCallSettings.Builder<ElementT,ElementResultT,RequestT,ResponseT> toBuilder()

Get a builder with the same values as this object. See the class documentation of [BatchingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingCallSettings) for a sample settings configuration.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingCallSettings.Builder)<ElementT,ElementResultT,RequestT,ResponseT>` |   
**Overrides**

[UnaryCallSettings<RequestT,ResponseT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_toBuilder__)

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[UnaryCallSettings<RequestT,ResponseT>.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings#com_google_api_gax_rpc_UnaryCallSettings_toString__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
