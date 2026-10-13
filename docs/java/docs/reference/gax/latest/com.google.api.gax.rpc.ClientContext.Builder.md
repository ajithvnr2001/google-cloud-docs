---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder
title: Class ClientContext.Builder (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:20.956217+00:00
---

# Class ClientContext.Builder (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClientContext.Builder (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public abstract static class ClientContext.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ClientContext.Builder

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

### Builder()
    
    
    public Builder()

## Methods 

### build()
    
    
    public abstract ClientContext build()

**Returns**  
---  
**Type** | **Description**  
`[ClientContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext)` |   
  
### setBackgroundResources(List<BackgroundResource> backgroundResources)
    
    
    public abstract ClientContext.Builder setBackgroundResources(List<BackgroundResource> backgroundResources)

**Parameter**  
---  
**Name** | **Description**  
`backgroundResources` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackgroundResource](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.BackgroundResource)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setClock(ApiClock clock)
    
    
    public abstract ClientContext.Builder setClock(ApiClock clock)

**Parameter**  
---  
**Name** | **Description**  
`clock` | `[ApiClock](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiClock.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setCredentials(Credentials value)
    
    
    public abstract ClientContext.Builder setCredentials(Credentials value)

**Parameter**  
---  
**Name** | **Description**  
`value` | `com.google.auth.Credentials`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setDefaultCallContext(ApiCallContext defaultCallContext)
    
    
    public abstract ClientContext.Builder setDefaultCallContext(ApiCallContext defaultCallContext)

**Parameter**  
---  
**Name** | **Description**  
`defaultCallContext` | `[ApiCallContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiCallContext)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setEndpoint(String endpoint)
    
    
    public abstract ClientContext.Builder setEndpoint(String endpoint)

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setExecutor(ScheduledExecutorService value)
    
    
    public abstract ClientContext.Builder setExecutor(ScheduledExecutorService value)

Sets the executor to use for running scheduled API call logic (such as retries and long-running operations).

**Parameter**  
---  
**Name** | **Description**  
`value` | `[ScheduledExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ScheduledExecutorService.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setGdchApiAudience(@Nullable String gdchApiAudience)
    
    
    public abstract ClientContext.Builder setGdchApiAudience(@Nullable String gdchApiAudience)

Sets the API audience used by com.google.auth.oauth2.GdchCredentials It cannot be used if other type of com.google.auth.Credentials is used

If the provided credentials already contain an api audience, it will be overriden by this one

**Parameter**  
---  
**Name** | **Description**  
`gdchApiAudience` | `@org.jspecify.annotations.Nullable java.lang.String`  
the audience to be used - must be a valid URI string  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setHeaders(Map<String,String> headers)
    
    
    public abstract ClientContext.Builder setHeaders(Map<String,String> headers)

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setInternalHeaders(Map<String,String> headers)
    
    
    protected abstract ClientContext.Builder setInternalHeaders(Map<String,String> headers)

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setQuotaProjectId(@Nullable String QuotaProjectId)
    
    
    public abstract ClientContext.Builder setQuotaProjectId(@Nullable String QuotaProjectId)

**Parameter**  
---  
**Name** | **Description**  
`QuotaProjectId` | `@org.jspecify.annotations.Nullable java.lang.String`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setStreamWatchdog(@Nullable Watchdog watchdog)
    
    
    public abstract ClientContext.Builder setStreamWatchdog(@Nullable Watchdog watchdog)

**Parameter**  
---  
**Name** | **Description**  
`watchdog` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.Watchdog`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setStreamWatchdogCheckInterval(Duration duration)
    
    
    public final ClientContext.Builder setStreamWatchdogCheckInterval(Duration duration)

**Obsolete**

_Use setStreamWatchdogCheckIntervalDuration(java.time.Duration) instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#setStreamWatchdogCheckIntervalDuration(java.time.Duration)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder#com_google_api_gax_rpc_ClientContext_Builder_setStreamWatchdogCheckIntervalDuration_java_time_Duration_) instead.

**Parameter**  
---  
**Name** | **Description**  
`duration` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setStreamWatchdogCheckIntervalDuration(Duration duration)
    
    
    public abstract ClientContext.Builder setStreamWatchdogCheckIntervalDuration(Duration duration)

**Parameter**  
---  
**Name** | **Description**  
`duration` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setTracerFactory(ApiTracerFactory tracerFactory)
    
    
    public abstract ClientContext.Builder setTracerFactory(ApiTracerFactory tracerFactory)

**Beta**

_The surface for tracing is not stable yet and may change in the future._

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Set the [ApiTracerFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.tracing.ApiTracerFactory) that will be used to generate traces for operations.

**Parameter**  
---  
**Name** | **Description**  
`tracerFactory` | `[ApiTracerFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.tracing.ApiTracerFactory)`  
an instance [ApiTracerFactory](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.tracing.ApiTracerFactory).  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setTransportChannel(TransportChannel transportChannel)
    
    
    public abstract ClientContext.Builder setTransportChannel(TransportChannel transportChannel)

**Parameter**  
---  
**Name** | **Description**  
`transportChannel` | `[TransportChannel](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannel)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
### setUniverseDomain(String universeDomain)
    
    
    public abstract ClientContext.Builder setUniverseDomain(String universeDomain)

**Parameter**  
---  
**Name** | **Description**  
`universeDomain` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClientContext.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientContext.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
