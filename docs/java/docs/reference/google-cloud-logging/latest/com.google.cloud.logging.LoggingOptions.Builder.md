---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder
title: Class LoggingOptions.Builder (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:01.816941+00:00
---

# Class LoggingOptions.Builder (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LoggingOptions.Builder (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static class LoggingOptions.Builder extends ServiceOptions.Builder<Logging,LoggingOptions,LoggingOptions.Builder>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.ServiceOptions.Builder > LoggingOptions.Builder

## Inherited Members

com.google.cloud.ServiceOptions.Builder.build()

com.google.cloud.ServiceOptions.Builder.getAllowedClientLibTokens()

com.google.cloud.ServiceOptions.Builder.self()

com.google.cloud.ServiceOptions.Builder.setApiTracerFactory(com.google.api.gax.tracing.ApiTracerFactory)

com.google.cloud.ServiceOptions.Builder.setClientLibToken(java.lang.String)

com.google.cloud.ServiceOptions.Builder.setClock(com.google.api.core.ApiClock)

com.google.cloud.ServiceOptions.Builder.setCredentials(com.google.auth.Credentials)

com.google.cloud.ServiceOptions.Builder.setHeaderProvider(com.google.api.gax.rpc.HeaderProvider)

com.google.cloud.ServiceOptions.Builder.setHost(java.lang.String)

com.google.cloud.ServiceOptions.Builder.setProjectId(java.lang.String)

com.google.cloud.ServiceOptions.Builder.setQuotaProjectId(java.lang.String)

com.google.cloud.ServiceOptions.Builder.setRetrySettings(com.google.api.gax.retrying.RetrySettings)

com.google.cloud.ServiceOptions.Builder.setServiceFactory(com.google.cloud.ServiceFactory<ServiceT,OptionsT>)

com.google.cloud.ServiceOptions.Builder.setServiceRpcFactory(com.google.cloud.spi.ServiceRpcFactory<OptionsT>)

com.google.cloud.ServiceOptions.Builder.setTransportOptions(com.google.cloud.TransportOptions)

com.google.cloud.ServiceOptions.Builder.setUniverseDomain(java.lang.String)

com.google.cloud.ServiceOptions.Builder.setUseJwtAccessWithScope(boolean)

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

### build()
    
    
    public LoggingOptions build()

**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions)` |   
**Overrides**

com.google.cloud.ServiceOptions.Builder.build()

### setAutoPopulateMetadata(boolean autoPopulateMetadataOnWrite)
    
    
    public LoggingOptions.Builder setAutoPopulateMetadata(boolean autoPopulateMetadataOnWrite)

**Parameter**  
---  
**Name** | **Description**  
`autoPopulateMetadataOnWrite` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder)` |   
  
### setBatchingSettings(BatchingSettings batchingSettings)
    
    
    public LoggingOptions.Builder setBatchingSettings(BatchingSettings batchingSettings)

**Parameter**  
---  
**Name** | **Description**  
`batchingSettings` | `[BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder)` |   
  
### setTransportOptions(TransportOptions transportOptions)
    
    
    public LoggingOptions.Builder setTransportOptions(TransportOptions transportOptions)

**Parameter**  
---  
**Name** | **Description**  
`transportOptions` | `com.google.cloud.TransportOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder)` |   
**Overrides**

com.google.cloud.ServiceOptions.Builder.setTransportOptions(com.google.cloud.TransportOptions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
