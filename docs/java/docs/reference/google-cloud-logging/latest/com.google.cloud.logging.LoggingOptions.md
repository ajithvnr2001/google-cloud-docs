---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions
title: Class LoggingOptions (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:00.952684+00:00
---

# Class LoggingOptions (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LoggingOptions (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class LoggingOptions extends ServiceOptions<Logging,LoggingOptions>

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.ServiceOptions > LoggingOptions

## Inherited Members

com.google.cloud.ServiceOptions.<B>toBuilder()

com.google.cloud.ServiceOptions.<T>getFromServiceLoader(java.lang.Class<? extends T>,T)

com.google.cloud.ServiceOptions.<T>newInstance(java.lang.String)

com.google.cloud.ServiceOptions.baseEquals(com.google.cloud.ServiceOptions<?,?>)

com.google.cloud.ServiceOptions.baseHashCode()

com.google.cloud.ServiceOptions.defaultRetrySettings()

com.google.cloud.ServiceOptions.getApiTracerFactory()

com.google.cloud.ServiceOptions.getAppEngineAppId()

com.google.cloud.ServiceOptions.getAppEngineProjectId()

com.google.cloud.ServiceOptions.getAppEngineProjectIdFromAppId()

com.google.cloud.ServiceOptions.getApplicationName()

com.google.cloud.ServiceOptions.getClientLibToken()

com.google.cloud.ServiceOptions.getClock()

com.google.cloud.ServiceOptions.getCredentials()

com.google.cloud.ServiceOptions.getDefaultHost()

com.google.cloud.ServiceOptions.getDefaultProject()

com.google.cloud.ServiceOptions.getDefaultProjectId()

com.google.cloud.ServiceOptions.getDefaultRetrySettings()

com.google.cloud.ServiceOptions.getGoogApiClientLibName()

com.google.cloud.ServiceOptions.getGoogleCloudProjectId()

com.google.cloud.ServiceOptions.getHost()

com.google.cloud.ServiceOptions.getLibraryName()

com.google.cloud.ServiceOptions.getLibraryVersion()

com.google.cloud.ServiceOptions.getMergedHeaderProvider(com.google.api.gax.rpc.HeaderProvider)

com.google.cloud.ServiceOptions.getNoRetrySettings()

com.google.cloud.ServiceOptions.getProjectId()

com.google.cloud.ServiceOptions.getQuotaProjectId()

com.google.cloud.ServiceOptions.getResolvedApiaryHost(java.lang.String)

com.google.cloud.ServiceOptions.getResolvedHost(java.lang.String)

com.google.cloud.ServiceOptions.getRetrySettings()

com.google.cloud.ServiceOptions.getRpc()

com.google.cloud.ServiceOptions.getScopedCredentials()

com.google.cloud.ServiceOptions.getScopes()

com.google.cloud.ServiceOptions.getService()

com.google.cloud.ServiceOptions.getServiceAccountProjectId()

com.google.cloud.ServiceOptions.getTransportOptions()

com.google.cloud.ServiceOptions.getUniverseDomain()

com.google.cloud.ServiceOptions.getUseJwtAccessWithScope()

com.google.cloud.ServiceOptions.getUserAgent()

com.google.cloud.ServiceOptions.hasValidUniverseDomain()

com.google.cloud.ServiceOptions.projectIdRequired()

com.google.cloud.ServiceOptions.shouldRefreshRpc(com.google.cloud.ServiceRpc)

com.google.cloud.ServiceOptions.shouldRefreshService(ServiceT)

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

## Static Methods 

### getDefaultGrpcTransportOptions()
    
    
    public static GrpcTransportOptions getDefaultGrpcTransportOptions()

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.grpc.GrpcTransportOptions` |   
  
### getDefaultInstance()
    
    
    public static LoggingOptions getDefaultInstance()

Returns a default `LoggingOptions` instance.

**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions)` |   
  
### newBuilder()
    
    
    public static LoggingOptions.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder)` |   
  
## Constructors 

### LoggingOptions(LoggingOptions.Builder builder)
    
    
    protected LoggingOptions(LoggingOptions.Builder builder)

**Internal Only** : This feature is not stable for application use.

_This class should only be extended within google-cloud-java_

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[LoggingOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder)`  
  
  
## Methods 

### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### getAutoPopulateMetadata()
    
    
    public Boolean getAutoPopulateMetadata()

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getBatchingSettings()
    
    
    public BatchingSettings getBatchingSettings()

**Returns**  
---  
**Type** | **Description**  
`[BatchingSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.batching.BatchingSettings.html)` |   
  
### getDefaultHost()
    
    
    protected String getDefaultHost()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

com.google.cloud.ServiceOptions.getDefaultHost()

### getLoggingRpcV2()
    
    
    protected LoggingRpc getLoggingRpcV2()

**Returns**  
---  
**Type** | **Description**  
`[LoggingRpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.spi.v2.LoggingRpc)` |   
  
### getScopes()
    
    
    protected Set<String> getScopes()

**Returns**  
---  
**Type** | **Description**  
`[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
**Overrides**

com.google.cloud.ServiceOptions.getScopes()

### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toBuilder()
    
    
    public LoggingOptions.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[LoggingOptions.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingOptions.Builder)` |   
**Overrides**

com.google.cloud.ServiceOptions.<B>toBuilder()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
