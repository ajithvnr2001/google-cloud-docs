---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder
title: Class InstantiatingGrpcChannelProvider.Builder (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:38.639537+00:00
---

# Class InstantiatingGrpcChannelProvider.Builder (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class InstantiatingGrpcChannelProvider.Builder (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public static final class InstantiatingGrpcChannelProvider.Builder

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > InstantiatingGrpcChannelProvider.Builder

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

## Methods 

### build()
    
    
    public InstantiatingGrpcChannelProvider build()

**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider)` |   
  
### getChannelConfigurator()
    
    
    public @Nullable ApiFunction<ManagedChannelBuilder,ManagedChannelBuilder> getChannelConfigurator()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.api.core.ApiFunction<io.grpc.ManagedChannelBuilder,io.grpc.ManagedChannelBuilder>` |   
  
### getEndpoint()
    
    
    public String getEndpoint()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getKeepAliveTime()
    
    
    public Duration getKeepAliveTime()

**Obsolete**

_Use getKeepAliveTimeDuration() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#getKeepAliveTimeDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_getKeepAliveTimeDuration__) instead.

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

This method is obsolete. Use [#getKeepAliveTimeoutDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_getKeepAliveTimeoutDuration__) instead

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
  
### getMaxInboundMessageSize()
    
    
    public Integer getMaxInboundMessageSize()

The maximum message size allowed to be received on the channel.

**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` |   
  
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
  
### getPoolSize() (deprecated)
    
    
    public int getPoolSize()

**Deprecated.** _Please use[#setChannelPoolSettings(ChannelPoolSettings)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setChannelPoolSettings_com_google_api_gax_grpc_ChannelPoolSettings_)_

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### setAllowHardBoundTokenTypes(List<InstantiatingGrpcChannelProvider.HardBoundTokenTypes> allowedValues)
    
    
    public InstantiatingGrpcChannelProvider.Builder setAllowHardBoundTokenTypes(List<InstantiatingGrpcChannelProvider.HardBoundTokenTypes> allowedValues)

**Internal Only** : This feature is not stable for application use.

**Parameter**  
---  
**Name** | **Description**  
`allowedValues` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[HardBoundTokenTypes](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.HardBoundTokenTypes)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setAllowNonDefaultServiceAccount(boolean allowNonDefaultServiceAccount)
    
    
    public InstantiatingGrpcChannelProvider.Builder setAllowNonDefaultServiceAccount(boolean allowNonDefaultServiceAccount)

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

Whether allow non-default service account for DirectPath.

**Parameter**  
---  
**Name** | **Description**  
`allowNonDefaultServiceAccount` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setAttemptDirectPath(boolean attemptDirectPath)
    
    
    public InstantiatingGrpcChannelProvider.Builder setAttemptDirectPath(boolean attemptDirectPath)

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

Whether attempt DirectPath.

**Parameter**  
---  
**Name** | **Description**  
`attemptDirectPath` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setAttemptDirectPathXds()
    
    
    public InstantiatingGrpcChannelProvider.Builder setAttemptDirectPathXds()

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

Use DirectPath xDS. Only valid if DirectPath is attempted.

**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setBackgroundExecutor(ScheduledExecutorService executor)
    
    
    public InstantiatingGrpcChannelProvider.Builder setBackgroundExecutor(ScheduledExecutorService executor)

Sets the background executor for this TransportChannelProvider. The life cycle of the executor should be managed by the caller.

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[ScheduledExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ScheduledExecutorService.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setChannelConfigurator(@Nullable ApiFunction<ManagedChannelBuilder,ManagedChannelBuilder> channelConfigurator)
    
    
    public InstantiatingGrpcChannelProvider.Builder setChannelConfigurator(@Nullable ApiFunction<ManagedChannelBuilder,ManagedChannelBuilder> channelConfigurator)

**Beta**

_Surface for advanced channel configuration is not yet stable_

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Add a callback that can intercept channel creation.

This can be used for advanced configuration like setting the netty event loop. The callback will be invoked with a fully configured channel builder, which the callback can augment or replace.

**Parameter**  
---  
**Name** | **Description**  
`channelConfigurator` | `@org.jspecify.annotations.Nullable com.google.api.core.ApiFunction<io.grpc.ManagedChannelBuilder,io.grpc.ManagedChannelBuilder>`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setChannelPoolSettings(ChannelPoolSettings settings)
    
    
    public InstantiatingGrpcChannelProvider.Builder setChannelPoolSettings(ChannelPoolSettings settings)

**Beta**

_Channel pool sizing api is not yet stable_

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ChannelPoolSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.ChannelPoolSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setChannelPrimer(ChannelPrimer channelPrimer)
    
    
    public InstantiatingGrpcChannelProvider.Builder setChannelPrimer(ChannelPrimer channelPrimer)

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

By setting a channelPrimer, the ChannelPool created by the provider will be refreshing ChannelPool. channelPrimer will be invoked periodically when the channels are refreshed

This is public only for technical reasons, for advanced usage.

**Parameter**  
---  
**Name** | **Description**  
`channelPrimer` | `[ChannelPrimer](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.ChannelPrimer)`  
invoked when the channels are refreshed  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` | builder for the provider  
  
### setChannelsPerCpu(double multiplier) (deprecated)
    
    
    public InstantiatingGrpcChannelProvider.Builder setChannelsPerCpu(double multiplier)

**Deprecated.** _Please use[#setChannelPoolSettings(ChannelPoolSettings)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setChannelPoolSettings_com_google_api_gax_grpc_ChannelPoolSettings_)_

**Parameter**  
---  
**Name** | **Description**  
`multiplier` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setChannelsPerCpu(double multiplier, int maxChannels) (deprecated)
    
    
    public InstantiatingGrpcChannelProvider.Builder setChannelsPerCpu(double multiplier, int maxChannels)

**Deprecated.** _Please use[#setChannelPoolSettings(ChannelPoolSettings)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setChannelPoolSettings_com_google_api_gax_grpc_ChannelPoolSettings_)_

**Parameters**  
---  
**Name** | **Description**  
`multiplier` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`maxChannels` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setCredentials(Credentials credentials)
    
    
    public InstantiatingGrpcChannelProvider.Builder setCredentials(Credentials credentials)

**Parameter**  
---  
**Name** | **Description**  
`credentials` | `com.google.auth.Credentials`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setDirectPathServiceConfig(Map<String,?> serviceConfig)
    
    
    public InstantiatingGrpcChannelProvider.Builder setDirectPathServiceConfig(Map<String,?> serviceConfig)

**Internal Only** : This feature is not stable for application use.

_For internal use by google-cloud-java clients only_

Sets a service config for direct path. If direct path is not enabled, the provided service config will be ignored.

See [ the service config proto definition](https://github.com/grpc/grpc-proto/blob/master/grpc/service_config/service_config.proto) for more details.

**Parameter**  
---  
**Name** | **Description**  
`serviceConfig` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setEndpoint(String endpoint)
    
    
    public InstantiatingGrpcChannelProvider.Builder setEndpoint(String endpoint)

Sets the endpoint used to reach the service, eg "localhost:8080".

**Parameter**  
---  
**Name** | **Description**  
`endpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setExecutor(Executor executor)
    
    
    public InstantiatingGrpcChannelProvider.Builder setExecutor(Executor executor)

Sets the Executor for this TransportChannelProvider.

This is optional; if it is not provided, needsExecutor() will return true, meaning that an Executor must be provided when getChannel is called on the constructed TransportChannelProvider instance. Note: GrpcTransportProvider will automatically provide its own Executor in this circumstance when it calls getChannel.

**Parameter**  
---  
**Name** | **Description**  
`executor` | `[Executor](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Executor.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setExecutorProvider(ExecutorProvider executorProvider) (deprecated)
    
    
    public InstantiatingGrpcChannelProvider.Builder setExecutorProvider(ExecutorProvider executorProvider)

**Deprecated.** _Please use[#setExecutor(Executor)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setExecutor_java_util_concurrent_Executor_)._

**Parameter**  
---  
**Name** | **Description**  
`executorProvider` | `[ExecutorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.ExecutorProvider)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setHeaderProvider(HeaderProvider headerProvider)
    
    
    public InstantiatingGrpcChannelProvider.Builder setHeaderProvider(HeaderProvider headerProvider)

Sets the HeaderProvider for this TransportChannelProvider.

This is optional; if it is not provided, needsHeaders() will return true, meaning that headers must be provided when getChannel is called on the constructed TransportChannelProvider instance.

**Parameter**  
---  
**Name** | **Description**  
`headerProvider` | `[HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setInterceptorProvider(GrpcInterceptorProvider interceptorProvider)
    
    
    public InstantiatingGrpcChannelProvider.Builder setInterceptorProvider(GrpcInterceptorProvider interceptorProvider)

Sets the GrpcInterceptorProvider for this TransportChannelProvider.

The provider will be called once for each underlying gRPC ManagedChannel that is created. It is recommended to return a new list of new interceptors on each call so that interceptors are not shared among channels, but this is not required.

**Parameter**  
---  
**Name** | **Description**  
`interceptorProvider` | `[GrpcInterceptorProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.GrpcInterceptorProvider)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setKeepAliveTime(Duration duration)
    
    
    public InstantiatingGrpcChannelProvider.Builder setKeepAliveTime(Duration duration)

**Obsolete**

_Use setKeepAliveTimeDuration(java.time.Duration) instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#setKeepAliveTimeDuration(java.time.Duration)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setKeepAliveTimeDuration_java_time_Duration_) instead.

**Parameter**  
---  
**Name** | **Description**  
`duration` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setKeepAliveTimeDuration(Duration duration)
    
    
    public InstantiatingGrpcChannelProvider.Builder setKeepAliveTimeDuration(Duration duration)

The time without read activity before sending a keepalive ping.

**Parameter**  
---  
**Name** | **Description**  
`duration` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setKeepAliveTimeout(Duration duration)
    
    
    public InstantiatingGrpcChannelProvider.Builder setKeepAliveTimeout(Duration duration)

**Obsolete**

_Use setKeepAliveTimeoutDuration(java.time.Duration) instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

This method is obsolete. Use [#setKeepAliveTimeoutDuration(java.time.Duration)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setKeepAliveTimeoutDuration_java_time_Duration_) instead.

**Parameter**  
---  
**Name** | **Description**  
`duration` | `org.threeten.bp.Duration`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setKeepAliveTimeoutDuration(Duration duration)
    
    
    public InstantiatingGrpcChannelProvider.Builder setKeepAliveTimeoutDuration(Duration duration)

The time without read activity after sending a keepalive ping.

**Parameter**  
---  
**Name** | **Description**  
`duration` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setKeepAliveWithoutCalls(Boolean keepalive)
    
    
    public InstantiatingGrpcChannelProvider.Builder setKeepAliveWithoutCalls(Boolean keepalive)

Whether keepalive will be performed when there are no outstanding RPCs.

**Parameter**  
---  
**Name** | **Description**  
`keepalive` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setMaxInboundMessageSize(Integer max)
    
    
    public InstantiatingGrpcChannelProvider.Builder setMaxInboundMessageSize(Integer max)

The maximum message size allowed to be received on the channel.

**Parameter**  
---  
**Name** | **Description**  
`max` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setMaxInboundMetadataSize(Integer max)
    
    
    public InstantiatingGrpcChannelProvider.Builder setMaxInboundMetadataSize(Integer max)

**Beta**

_The surface for maximum metadata size is not stable yet and may change in the future._

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

The maximum metadata size allowed to be received on the channel.

**Parameter**  
---  
**Name** | **Description**  
`max` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setMtlsEndpoint(String mtlsEndpoint)
    
    
    public InstantiatingGrpcChannelProvider.Builder setMtlsEndpoint(String mtlsEndpoint)

**Internal Only** : This feature is not stable for application use.

_This public method is used by Gax to help configure the MTLS endpoint for S2A_

Sets the mTLS Endpoint used to reach the service, eg "localhost:8080".

**Parameter**  
---  
**Name** | **Description**  
`mtlsEndpoint` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
### setPoolSize(int poolSize) (deprecated)
    
    
    public InstantiatingGrpcChannelProvider.Builder setPoolSize(int poolSize)

**Deprecated.** _Please use[#setChannelPoolSettings(ChannelPoolSettings)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setChannelPoolSettings_com_google_api_gax_grpc_ChannelPoolSettings_)_

**Parameter**  
---  
**Name** | **Description**  
`poolSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InstantiatingGrpcChannelProvider.Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
