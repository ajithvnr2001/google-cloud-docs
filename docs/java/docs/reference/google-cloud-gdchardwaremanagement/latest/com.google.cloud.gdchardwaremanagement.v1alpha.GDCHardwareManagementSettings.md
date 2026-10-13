---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings
title: Class GDCHardwareManagementSettings (0.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:59.234489+00:00
---

# Class GDCHardwareManagementSettings (0.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class GDCHardwareManagementSettings (0.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.54.0 (latest)  0.50.0  0.49.0  0.48.0  0.46.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class GDCHardwareManagementSettings extends ClientSettings<GDCHardwareManagementSettings>

Settings class to configure an instance of [GDCHardwareManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient).

The default instance has everything set to sensible defaults:

  * The default service address (gdchardwaremanagement.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getOrder:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GDCHardwareManagementSettings.Builder gDCHardwareManagementSettingsBuilder =
         GDCHardwareManagementSettings.newBuilder();
     gDCHardwareManagementSettingsBuilder
         .getOrderSettings()
         .setRetrySettings(
             gDCHardwareManagementSettingsBuilder
                 .getOrderSettings()
                 .getRetrySettings()
                 .toBuilder()
                 .setInitialRetryDelayDuration(Duration.ofSeconds(1))
                 .setInitialRpcTimeoutDuration(Duration.ofSeconds(5))
                 .setMaxAttempts(5)
                 .setMaxRetryDelayDuration(Duration.ofSeconds(30))
                 .setMaxRpcTimeoutDuration(Duration.ofSeconds(60))
                 .setRetryDelayMultiplier(1.3)
                 .setRpcTimeoutMultiplier(1.5)
                 .setTotalTimeoutDuration(Duration.ofSeconds(300))
                 .build());
     GDCHardwareManagementSettings gDCHardwareManagementSettings =
         gDCHardwareManagementSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createOrder:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     GDCHardwareManagementSettings.Builder gDCHardwareManagementSettingsBuilder =
         GDCHardwareManagementSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     gDCHardwareManagementSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > GDCHardwareManagementSettings

## Inherited Members

[ClientSettings.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

[ClientSettings.getApiKey()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getApiKey__)

[ClientSettings.getBackgroundExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getBackgroundExecutorProvider__)

[ClientSettings.getClock()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getClock__)

[ClientSettings.getCredentialsProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getCredentialsProvider__)

[ClientSettings.getEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getEndpoint__)

[ClientSettings.getExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getExecutorProvider__)

[ClientSettings.getGdchApiAudience()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getGdchApiAudience__)

[ClientSettings.getHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getHeaderProvider__)

[ClientSettings.getInternalHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getInternalHeaderProvider__)

[ClientSettings.getQuotaProjectId()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getQuotaProjectId__)

[ClientSettings.getStubSettings()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getStubSettings__)

[ClientSettings.getTransportChannelProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getTransportChannelProvider__)

[ClientSettings.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getUniverseDomain__)

[ClientSettings.getWatchdogCheckInterval()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogCheckInterval__)

[ClientSettings.getWatchdogCheckIntervalDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogCheckIntervalDuration__)

[ClientSettings.getWatchdogProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_getWatchdogProvider__)

[ClientSettings.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings_toString__)

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### create(GDCHardwareManagementStubSettings stub)
    
    
    public static final GDCHardwareManagementSettings create(GDCHardwareManagementStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[GDCHardwareManagementStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.stub.GDCHardwareManagementStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### defaultApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultCredentialsProviderBuilder()
    
    
    public static GoogleCredentialsProvider.Builder defaultCredentialsProviderBuilder()

Returns a builder for the default credentials for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.GoogleCredentialsProvider.Builder.html)` |   
  
### defaultExecutorProviderBuilder()
    
    
    public static InstantiatingExecutorProvider.Builder defaultExecutorProviderBuilder()

Returns a builder for the default ExecutorProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultHttpJsonTransportProviderBuilder()
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a builder for the default REST ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.InstantiatingHttpJsonChannelProvider.Builder.html)` |   
  
### defaultTransportChannelProvider()
    
    
    public static TransportChannelProvider defaultTransportChannelProvider()

**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)` |   
  
### getDefaultEndpoint()
    
    
    public static String getDefaultEndpoint()

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultServiceScopes()
    
    
    public static List<String> getDefaultServiceScopes()

Returns the default service scopes.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### newBuilder()
    
    
    public static GDCHardwareManagementSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static GDCHardwareManagementSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static GDCHardwareManagementSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings.Builder)` |   
  
## Constructors 

### GDCHardwareManagementSettings(GDCHardwareManagementSettings.Builder settingsBuilder)
    
    
    protected GDCHardwareManagementSettings(GDCHardwareManagementSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[GDCHardwareManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings.Builder)`  
  
  
## Methods 

### cancelOrderOperationSettings()
    
    
    public OperationCallSettings<CancelOrderRequest,Order,OperationMetadata> cancelOrderOperationSettings()

Returns the object with the settings used for calls to cancelOrder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### cancelOrderSettings()
    
    
    public UnaryCallSettings<CancelOrderRequest,Operation> cancelOrderSettings()

Returns the object with the settings used for calls to cancelOrder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CancelOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CancelOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCommentOperationSettings()
    
    
    public OperationCallSettings<CreateCommentRequest,Comment,OperationMetadata> createCommentOperationSettings()

Returns the object with the settings used for calls to createComment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createCommentSettings()
    
    
    public UnaryCallSettings<CreateCommentRequest,Operation> createCommentSettings()

Returns the object with the settings used for calls to createComment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateCommentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHardwareGroupOperationSettings()
    
    
    public OperationCallSettings<CreateHardwareGroupRequest,HardwareGroup,OperationMetadata> createHardwareGroupOperationSettings()

Returns the object with the settings used for calls to createHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest),[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareGroupSettings()
    
    
    public UnaryCallSettings<CreateHardwareGroupRequest,Operation> createHardwareGroupSettings()

Returns the object with the settings used for calls to createHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHardwareOperationSettings()
    
    
    public OperationCallSettings<CreateHardwareRequest,Hardware,OperationMetadata> createHardwareOperationSettings()

Returns the object with the settings used for calls to createHardware.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest),[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createHardwareSettings()
    
    
    public UnaryCallSettings<CreateHardwareRequest,Operation> createHardwareSettings()

Returns the object with the settings used for calls to createHardware.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateHardwareRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createOrderOperationSettings()
    
    
    public OperationCallSettings<CreateOrderRequest,Order,OperationMetadata> createOrderOperationSettings()

Returns the object with the settings used for calls to createOrder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createOrderSettings()
    
    
    public UnaryCallSettings<CreateOrderRequest,Operation> createOrderSettings()

Returns the object with the settings used for calls to createOrder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSiteOperationSettings()
    
    
    public OperationCallSettings<CreateSiteRequest,Site,OperationMetadata> createSiteOperationSettings()

Returns the object with the settings used for calls to createSite.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createSiteSettings()
    
    
    public UnaryCallSettings<CreateSiteRequest,Operation> createSiteSettings()

Returns the object with the settings used for calls to createSite.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createZoneOperationSettings()
    
    
    public OperationCallSettings<CreateZoneRequest,Zone,OperationMetadata> createZoneOperationSettings()

Returns the object with the settings used for calls to createZone.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### createZoneSettings()
    
    
    public UnaryCallSettings<CreateZoneRequest,Operation> createZoneSettings()

Returns the object with the settings used for calls to createZone.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CreateZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHardwareGroupOperationSettings()
    
    
    public OperationCallSettings<DeleteHardwareGroupRequest,Empty,OperationMetadata> deleteHardwareGroupOperationSettings()

Returns the object with the settings used for calls to deleteHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareGroupSettings()
    
    
    public UnaryCallSettings<DeleteHardwareGroupRequest,Operation> deleteHardwareGroupSettings()

Returns the object with the settings used for calls to deleteHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHardwareOperationSettings()
    
    
    public OperationCallSettings<DeleteHardwareRequest,Empty,OperationMetadata> deleteHardwareOperationSettings()

Returns the object with the settings used for calls to deleteHardware.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteHardwareSettings()
    
    
    public UnaryCallSettings<DeleteHardwareRequest,Operation> deleteHardwareSettings()

Returns the object with the settings used for calls to deleteHardware.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteHardwareRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteOrderOperationSettings()
    
    
    public OperationCallSettings<DeleteOrderRequest,Empty,OperationMetadata> deleteOrderOperationSettings()

Returns the object with the settings used for calls to deleteOrder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteOrderSettings()
    
    
    public UnaryCallSettings<DeleteOrderRequest,Operation> deleteOrderSettings()

Returns the object with the settings used for calls to deleteOrder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSiteOperationSettings()
    
    
    public OperationCallSettings<DeleteSiteRequest,Empty,OperationMetadata> deleteSiteOperationSettings()

Returns the object with the settings used for calls to deleteSite.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteSiteSettings()
    
    
    public UnaryCallSettings<DeleteSiteRequest,Operation> deleteSiteSettings()

Returns the object with the settings used for calls to deleteSite.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteZoneOperationSettings()
    
    
    public OperationCallSettings<DeleteZoneRequest,Empty,OperationMetadata> deleteZoneOperationSettings()

Returns the object with the settings used for calls to deleteZone.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### deleteZoneSettings()
    
    
    public UnaryCallSettings<DeleteZoneRequest,Operation> deleteZoneSettings()

Returns the object with the settings used for calls to deleteZone.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.DeleteZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getChangeLogEntrySettings()
    
    
    public UnaryCallSettings<GetChangeLogEntryRequest,ChangeLogEntry> getChangeLogEntrySettings()

Returns the object with the settings used for calls to getChangeLogEntry.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetChangeLogEntryRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetChangeLogEntryRequest),[ChangeLogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ChangeLogEntry)>` |   
  
### getCommentSettings()
    
    
    public UnaryCallSettings<GetCommentRequest,Comment> getCommentSettings()

Returns the object with the settings used for calls to getComment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)>` |   
  
### getHardwareGroupSettings()
    
    
    public UnaryCallSettings<GetHardwareGroupRequest,HardwareGroup> getHardwareGroupSettings()

Returns the object with the settings used for calls to getHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareGroupRequest),[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup)>` |   
  
### getHardwareSettings()
    
    
    public UnaryCallSettings<GetHardwareRequest,Hardware> getHardwareSettings()

Returns the object with the settings used for calls to getHardware.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetHardwareRequest),[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getOrderSettings()
    
    
    public UnaryCallSettings<GetOrderRequest,Order> getOrderSettings()

Returns the object with the settings used for calls to getOrder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order)>` |   
  
### getSiteSettings()
    
    
    public UnaryCallSettings<GetSiteRequest,Site> getSiteSettings()

Returns the object with the settings used for calls to getSite.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site)>` |   
  
### getSkuSettings()
    
    
    public UnaryCallSettings<GetSkuRequest,Sku> getSkuSettings()

Returns the object with the settings used for calls to getSku.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSkuRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetSkuRequest),[Sku](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Sku)>` |   
  
### getZoneSettings()
    
    
    public UnaryCallSettings<GetZoneRequest,Zone> getZoneSettings()

Returns the object with the settings used for calls to getZone.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GetZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone)>` |   
  
### listChangeLogEntriesSettings()
    
    
    public PagedCallSettings<ListChangeLogEntriesRequest,ListChangeLogEntriesResponse,GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse> listChangeLogEntriesSettings()

Returns the object with the settings used for calls to listChangeLogEntries.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListChangeLogEntriesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesRequest),[ListChangeLogEntriesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListChangeLogEntriesResponse),[ListChangeLogEntriesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListChangeLogEntriesPagedResponse)>` |   
  
### listCommentsSettings()
    
    
    public PagedCallSettings<ListCommentsRequest,ListCommentsResponse,GDCHardwareManagementClient.ListCommentsPagedResponse> listCommentsSettings()

Returns the object with the settings used for calls to listComments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCommentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsRequest),[ListCommentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListCommentsResponse),[ListCommentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListCommentsPagedResponse)>` |   
  
### listHardwareGroupsSettings()
    
    
    public PagedCallSettings<ListHardwareGroupsRequest,ListHardwareGroupsResponse,GDCHardwareManagementClient.ListHardwareGroupsPagedResponse> listHardwareGroupsSettings()

Returns the object with the settings used for calls to listHardwareGroups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHardwareGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsRequest),[ListHardwareGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareGroupsResponse),[ListHardwareGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwareGroupsPagedResponse)>` |   
  
### listHardwareSettings()
    
    
    public PagedCallSettings<ListHardwareRequest,ListHardwareResponse,GDCHardwareManagementClient.ListHardwarePagedResponse> listHardwareSettings()

Returns the object with the settings used for calls to listHardware.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareRequest),[ListHardwareResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListHardwareResponse),[ListHardwarePagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListHardwarePagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,GDCHardwareManagementClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListLocationsPagedResponse)>` |   
  
### listOrdersSettings()
    
    
    public PagedCallSettings<ListOrdersRequest,ListOrdersResponse,GDCHardwareManagementClient.ListOrdersPagedResponse> listOrdersSettings()

Returns the object with the settings used for calls to listOrders.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListOrdersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersRequest),[ListOrdersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListOrdersResponse),[ListOrdersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListOrdersPagedResponse)>` |   
  
### listSitesSettings()
    
    
    public PagedCallSettings<ListSitesRequest,ListSitesResponse,GDCHardwareManagementClient.ListSitesPagedResponse> listSitesSettings()

Returns the object with the settings used for calls to listSites.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSitesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesRequest),[ListSitesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSitesResponse),[ListSitesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSitesPagedResponse)>` |   
  
### listSkusSettings()
    
    
    public PagedCallSettings<ListSkusRequest,ListSkusResponse,GDCHardwareManagementClient.ListSkusPagedResponse> listSkusSettings()

Returns the object with the settings used for calls to listSkus.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListSkusResponse),[ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListSkusPagedResponse)>` |   
  
### listZonesSettings()
    
    
    public PagedCallSettings<ListZonesRequest,ListZonesResponse,GDCHardwareManagementClient.ListZonesPagedResponse> listZonesSettings()

Returns the object with the settings used for calls to listZones.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListZonesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesRequest),[ListZonesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.ListZonesResponse),[ListZonesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementClient.ListZonesPagedResponse)>` |   
  
### recordActionOnCommentSettings()
    
    
    public UnaryCallSettings<RecordActionOnCommentRequest,Comment> recordActionOnCommentSettings()

Returns the object with the settings used for calls to recordActionOnComment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RecordActionOnCommentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RecordActionOnCommentRequest),[Comment](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Comment)>` |   
  
### requestOrderDateChangeOperationSettings()
    
    
    public OperationCallSettings<RequestOrderDateChangeRequest,Order,OperationMetadata> requestOrderDateChangeOperationSettings()

Returns the object with the settings used for calls to requestOrderDateChange.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### requestOrderDateChangeSettings()
    
    
    public UnaryCallSettings<RequestOrderDateChangeRequest,Operation> requestOrderDateChangeSettings()

Returns the object with the settings used for calls to requestOrderDateChange.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RequestOrderDateChangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.RequestOrderDateChangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### signalZoneStateOperationSettings()
    
    
    public OperationCallSettings<SignalZoneStateRequest,Zone,OperationMetadata> signalZoneStateOperationSettings()

Returns the object with the settings used for calls to signalZoneState.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### signalZoneStateSettings()
    
    
    public UnaryCallSettings<SignalZoneStateRequest,Operation> signalZoneStateSettings()

Returns the object with the settings used for calls to signalZoneState.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SignalZoneStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SignalZoneStateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### submitOrderOperationSettings()
    
    
    public OperationCallSettings<SubmitOrderRequest,Order,OperationMetadata> submitOrderOperationSettings()

Returns the object with the settings used for calls to submitOrder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### submitOrderSettings()
    
    
    public UnaryCallSettings<SubmitOrderRequest,Operation> submitOrderSettings()

Returns the object with the settings used for calls to submitOrder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SubmitOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.SubmitOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### toBuilder()
    
    
    public GDCHardwareManagementSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[GDCHardwareManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.GDCHardwareManagementSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateHardwareGroupOperationSettings()
    
    
    public OperationCallSettings<UpdateHardwareGroupRequest,HardwareGroup,OperationMetadata> updateHardwareGroupOperationSettings()

Returns the object with the settings used for calls to updateHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest),[HardwareGroup](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.HardwareGroup),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareGroupSettings()
    
    
    public UnaryCallSettings<UpdateHardwareGroupRequest,Operation> updateHardwareGroupSettings()

Returns the object with the settings used for calls to updateHardwareGroup.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHardwareGroupRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareGroupRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHardwareOperationSettings()
    
    
    public OperationCallSettings<UpdateHardwareRequest,Hardware,OperationMetadata> updateHardwareOperationSettings()

Returns the object with the settings used for calls to updateHardware.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest),[Hardware](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Hardware),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateHardwareSettings()
    
    
    public UnaryCallSettings<UpdateHardwareRequest,Operation> updateHardwareSettings()

Returns the object with the settings used for calls to updateHardware.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHardwareRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateHardwareRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateOrderOperationSettings()
    
    
    public OperationCallSettings<UpdateOrderRequest,Order,OperationMetadata> updateOrderOperationSettings()

Returns the object with the settings used for calls to updateOrder.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest),[Order](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Order),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateOrderSettings()
    
    
    public UnaryCallSettings<UpdateOrderRequest,Operation> updateOrderSettings()

Returns the object with the settings used for calls to updateOrder.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateOrderRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateOrderRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateSiteOperationSettings()
    
    
    public OperationCallSettings<UpdateSiteRequest,Site,OperationMetadata> updateSiteOperationSettings()

Returns the object with the settings used for calls to updateSite.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest),[Site](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Site),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateSiteSettings()
    
    
    public UnaryCallSettings<UpdateSiteRequest,Operation> updateSiteSettings()

Returns the object with the settings used for calls to updateSite.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSiteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateSiteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateZoneOperationSettings()
    
    
    public OperationCallSettings<UpdateZoneRequest,Zone,OperationMetadata> updateZoneOperationSettings()

Returns the object with the settings used for calls to updateZone.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest),[Zone](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Zone),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.OperationMetadata)>` |   
  
### updateZoneSettings()
    
    
    public UnaryCallSettings<UpdateZoneRequest,Operation> updateZoneSettings()

Returns the object with the settings used for calls to updateZone.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateZoneRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.UpdateZoneRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
