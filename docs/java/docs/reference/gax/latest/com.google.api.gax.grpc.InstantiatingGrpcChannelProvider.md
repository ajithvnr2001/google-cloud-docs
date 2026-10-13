---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider
title: Class InstantiatingGrpcChannelProvider (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:23:26.563769+00:00
---

# Class InstantiatingGrpcChannelProvider (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstantiatingGrpcChannelProvider (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public final class InstantiatingGrpcChannelProvider implements TransportChannelProvider

InstantiatingGrpcChannelProvider is a TransportChannelProvider which constructs a gRPC ManagedChannel with a number of configured inputs every time getChannel(...) is called. These inputs include a port, a service address, and credentials.

The credentials can either be supplied directly (by providing a FixedCredentialsProvider to Builder.setCredentialsProvider()) or acquired implicitly from Application Default Credentials (by providing a GoogleCredentialsProvider to Builder.setCredentialsProvider()).

The client lib header and generator header values are used to form a value that goes into the http header of requests to the service.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstantiatingGrpcChannelProvider

## Implements

[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)

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

## Static Methods 

### newBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder newBuilder()

**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
## Methods 

### acceptsPoolSize() (deprecated)
    
    
    public boolean acceptsPoolSize()

**Deprecated.** _Please modify pool settings via[#toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_toBuilder__)_

Reports whether this provider allows pool size customization.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### canUseDirectPath()
    
    
    public boolean canUseDirectPath()

**Internal Only** : This feature is not stable for application use.

Marked as Internal Api and intended for internal use. DirectPath must be enabled via the settings and a few other configurations/settings must also be valid for the request to go through DirectPath.

Checks: 1. Credentials are compatible 2.Running on Compute Engine 3. Universe Domain is configured to for the Google Default Universe

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | if DirectPath is enabled for the client AND if the configurations are valid  
  
### createChannelBuilder()
    
    
    public ManagedChannelBuilder<?> createChannelBuilder()

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ManagedChannelBuilder<?>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### createDecoratedChannelBuilder()
    
    
    public ManagedChannelBuilder<?> createDecoratedChannelBuilder()

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

**Returns**  
---  
**Type** | **Description**  
`io.grpc.ManagedChannelBuilder<?>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getChannelPoolSettings()
    
    
    public ChannelPoolSettings getChannelPoolSettings()

**Beta**

_Channel pool sizing api is not yet stable_

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

The configured channel pool settings used for gRPC's ChannelProvider

**Returns**  
---  
**Type** | **Description**  
`[ChannelPoolSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.ChannelPoolSettings)` |   
  
### getEndpoint()
    
    
    public String getEndpoint()

The endpoint to be used for the channel.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getExecutor()
    
    
    public @Nullable Executor getExecutor()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable java.util.concurrent.Executor` |   
  
### getKeepAliveTime()
    
    
    public Duration getKeepAliveTime()

**Obsolete**

_Use getKeepAliveTimeDuration() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#getKeepAliveTimeDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_getKeepAliveTimeDuration__) instead.

**Returns**  
---  
**Type** | **Description**  
`org.threeten.bp.Duration` |   
  
### getKeepAliveTimeDuration()
    
    
    public Duration getKeepAliveTimeDuration()

The time without read activity before sending a keepalive ping.

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)` |   
  
### getKeepAliveTimeout()
    
    
    public Duration getKeepAliveTimeout()

**Obsolete**

_Use getKeepAliveTimeoutDuration() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#getKeepAliveTimeoutDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_getKeepAliveTimeoutDuration__) instead

**Returns**  
---  
**Type** | **Description**  
`org.threeten.bp.Duration` |   
  
### getKeepAliveTimeoutDuration()
    
    
    public Duration getKeepAliveTimeoutDuration()

The time without read activity after sending a keepalive ping.

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)` |   
  
### getKeepAliveWithoutCalls()
    
    
    public Boolean getKeepAliveWithoutCalls()

Whether keepalive will be performed when there are no outstanding RPCs.

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` |   
  
### getMaxInboundMetadataSize()
    
    
    public Integer getMaxInboundMetadataSize()

**Beta**

_The surface for maximum metadata size is not stable yet and may change in the future._

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

The maximum metadata size allowed to be received on the channel.

**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` |   
  
### getTransportChannel()
    
    
    public TransportChannel getTransportChannel()

Provides a Transport, which could either be a new instance for every call, or the same instance, depending on the implementation.

If [#needsExecutor()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_needsExecutor__) is true, then [#withExecutor(Executor)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_withExecutor_java_util_concurrent_Executor_) needs to be called first to provide an executor.

If [#needsHeaders()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_needsHeaders__) is true, then [#withHeaders(Map)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_withHeaders_java_util_Map_java_lang_String_java_lang_String__) needs to be called first to provide headers.

if [#needsEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_needsEndpoint__) is true, then [#withEndpoint(String)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_withEndpoint_java_lang_String_) needs to be called first to provide an endpoint.

**Returns**  
---  
**Type** | **Description**  
`[TransportChannel](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannel)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### getTransportName()
    
    
    public String getTransportName()

The name of the transport.

This string can be used for identifying transports for switching logic.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### isDirectPathXdsEnabled()
    
    
    public boolean isDirectPathXdsEnabled()

**Internal Only** : This feature is not stable for application use.

This method tells if Direct Path xDS was enabled. There are two ways of enabling it: via environment variable (by setting GOOGLE_CLOUD_ENABLE_DIRECT_PATH_XDS=true) or when building this channel provider (via the Builder#setAttemptDirectPathXds() method).

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | true if Direct Path xDS was either enabled via env var or via builder option  
  
### needsBackgroundExecutor()
    
    
    public boolean needsBackgroundExecutor()

True if the TransportProvider needs a background executor. The background executor can be used for refreshing channels, resizing the channel pool etc.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### needsCredentials()
    
    
    public boolean needsCredentials()

True if credentials are needed before channel creation.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### needsEndpoint()
    
    
    public boolean needsEndpoint()

True if the TransportProvider has no endpoint set.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### needsExecutor() (deprecated)
    
    
    public boolean needsExecutor()

**Deprecated.** _If executor is not set, this channel provider will create channels with default grpc executor._

True if the TransportProvider needs an executor.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### needsHeaders()
    
    
    public boolean needsHeaders()

True if the TransportProvider has no headers provided.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### needsMtlsEndpoint()
    
    
    public boolean needsMtlsEndpoint()

**Internal Only** : This feature is not stable for application use.

_This public method is used by Gax to help configure the MTLS endpoint for S2A_

True for gRPC transport provider which has no mtlsEndpoint set.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### shouldAutoClose()
    
    
    public boolean shouldAutoClose()

Indicates whether the TransportChannel should be closed by the containing client class.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### toBuilder()
    
    
    public InstantiatingGrpcChannelProvider.Builder toBuilder()

**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### withBackgroundExecutor(ScheduledExecutorService executor)
    
    
    public TransportChannelProvider withBackgroundExecutor(ScheduledExecutorService executor)

Sets the background executor when constructing a new [TransportChannel](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannel).

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[ScheduledExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ScheduledExecutorService.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` |   
  
### withCredentials(Credentials credentials)
    
    
    public TransportChannelProvider withCredentials(Credentials credentials)

Sets the credentials that will be applied before channel creation.

**Parameter**  
---  
**Name** | **Description**  
`credentials` | `com.google.auth.Credentials`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` |   
  
### withEndpoint(String endpoint)
    
    
    public TransportChannelProvider withEndpoint(String endpoint)

Specify the endpoint the channel should connect to.

The value of `endpoint` must be of the form `host:port`.

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The endpoint to connect to  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` | A new [InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider) with the specified endpoint configured  
  
### withExecutor(Executor executor)
    
    
    public TransportChannelProvider withExecutor(Executor executor)

Sets the executor to use when constructing a new [TransportChannel](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannel).

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` |   
  
### withExecutor(ScheduledExecutorService executor) (deprecated)
    
    
    public TransportChannelProvider withExecutor(ScheduledExecutorService executor)

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[ScheduledExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ScheduledExecutorService.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` |   
  
### withHeaders(Map<String,String> headers)
    
    
    public TransportChannelProvider withHeaders(Map<String,String> headers)

Sets the headers to use when constructing a new [TransportChannel](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannel).

This method should only be called if [#needsHeaders()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_needsHeaders__) returns true.

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` |   
  
### withMtlsEndpoint(String mtlsEndpoint)
    
    
    public TransportChannelProvider withMtlsEndpoint(String mtlsEndpoint)

**Internal Only** : This feature is not stable for application use.

_This public method is used by Gax to help configure the MTLS endpoint for S2A_

Specify the mTLS endpoint the channel should connect to when using S2A.

The value of `mtlsEndpoint` must be of the form `host:port`.

**Parameter**  
---  
**Name** | **Description**  
`mtlsEndpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The mtTLS endpoint to connect to  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` | A new [InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider) with the specified mTLS endpoint configured  
  
### withPoolSize(int size) (deprecated)
    
    
    public TransportChannelProvider withPoolSize(int size)

**Deprecated.** _Please modify pool settings via[#toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_toBuilder__)_

Number of underlying transport channels to open. Calls will be load balanced across them.

**Parameter**  
---  
**Name** | **Description**  
`size` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` |   
  
### withUseS2A(boolean useS2A)
    
    
    public TransportChannelProvider withUseS2A(boolean useS2A)

Specify whether or not to use S2A.

**Parameter**  
---  
**Name** | **Description**  
`useS2A` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider)` | A new [InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider) with useS2A set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
