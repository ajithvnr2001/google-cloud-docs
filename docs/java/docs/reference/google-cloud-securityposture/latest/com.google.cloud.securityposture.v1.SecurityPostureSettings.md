---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings
title: Class SecurityPostureSettings (0.64.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:05.944355+00:00
---

# Class SecurityPostureSettings (0.64.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityPostureSettings (0.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.64.0 (latest)  0.60.0  0.59.0  0.58.0  0.56.0  0.53.0  0.52.0  0.50.0  0.48.0  0.47.0  0.45.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.33.0  0.32.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 
    
    
    public class SecurityPostureSettings extends ClientSettings<SecurityPostureSettings>

Settings class to configure an instance of [SecurityPostureClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient).

The default instance has everything set to sensible defaults:

  * The default service address (securityposture.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getPosture:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityPostureSettings.Builder securityPostureSettingsBuilder =
         SecurityPostureSettings.newBuilder();
     securityPostureSettingsBuilder
         .getPostureSettings()
         .setRetrySettings(
             securityPostureSettingsBuilder
                 .getPostureSettings()
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
     SecurityPostureSettings securityPostureSettings = securityPostureSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createPosture:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityPostureSettings.Builder securityPostureSettingsBuilder =
         SecurityPostureSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     securityPostureSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > SecurityPostureSettings

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

### create(SecurityPostureStubSettings stub)
    
    
    public static final SecurityPostureSettings create(SecurityPostureStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityPostureStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.stub.SecurityPostureStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings)` |   
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
    
    
    public static SecurityPostureSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static SecurityPostureSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static SecurityPostureSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings.Builder)` |   
  
## Constructors 

### SecurityPostureSettings(SecurityPostureSettings.Builder settingsBuilder)
    
    
    protected SecurityPostureSettings(SecurityPostureSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[SecurityPostureSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings.Builder)`  
  
  
## Methods 

### createPostureDeploymentOperationSettings()
    
    
    public OperationCallSettings<CreatePostureDeploymentRequest,PostureDeployment,OperationMetadata> createPostureDeploymentOperationSettings()

Returns the object with the settings used for calls to createPostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureDeploymentRequest),[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureDeploymentSettings()
    
    
    public UnaryCallSettings<CreatePostureDeploymentRequest,Operation> createPostureDeploymentSettings()

Returns the object with the settings used for calls to createPostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createPostureOperationSettings()
    
    
    public OperationCallSettings<CreatePostureRequest,Posture,OperationMetadata> createPostureOperationSettings()

Returns the object with the settings used for calls to createPosture.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### createPostureSettings()
    
    
    public UnaryCallSettings<CreatePostureRequest,Operation> createPostureSettings()

Returns the object with the settings used for calls to createPosture.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.CreatePostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePostureDeploymentOperationSettings()
    
    
    public OperationCallSettings<DeletePostureDeploymentRequest,Empty,OperationMetadata> deletePostureDeploymentOperationSettings()

Returns the object with the settings used for calls to deletePostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeletePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureDeploymentRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureDeploymentSettings()
    
    
    public UnaryCallSettings<DeletePostureDeploymentRequest,Operation> deletePostureDeploymentSettings()

Returns the object with the settings used for calls to deletePostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeletePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deletePostureOperationSettings()
    
    
    public OperationCallSettings<DeletePostureRequest,Empty,OperationMetadata> deletePostureOperationSettings()

Returns the object with the settings used for calls to deletePosture.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeletePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### deletePostureSettings()
    
    
    public UnaryCallSettings<DeletePostureRequest,Operation> deletePostureSettings()

Returns the object with the settings used for calls to deletePosture.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeletePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.DeletePostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### extractPostureOperationSettings()
    
    
    public OperationCallSettings<ExtractPostureRequest,Posture,OperationMetadata> extractPostureOperationSettings()

Returns the object with the settings used for calls to extractPosture.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ExtractPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ExtractPostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### extractPostureSettings()
    
    
    public UnaryCallSettings<ExtractPostureRequest,Operation> extractPostureSettings()

Returns the object with the settings used for calls to extractPosture.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExtractPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ExtractPostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getPostureDeploymentSettings()
    
    
    public UnaryCallSettings<GetPostureDeploymentRequest,PostureDeployment> getPostureDeploymentSettings()

Returns the object with the settings used for calls to getPostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureDeploymentRequest),[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment)>` |   
  
### getPostureSettings()
    
    
    public UnaryCallSettings<GetPostureRequest,Posture> getPostureSettings()

Returns the object with the settings used for calls to getPosture.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture)>` |   
  
### getPostureTemplateSettings()
    
    
    public UnaryCallSettings<GetPostureTemplateRequest,PostureTemplate> getPostureTemplateSettings()

Returns the object with the settings used for calls to getPostureTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPostureTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.GetPostureTemplateRequest),[PostureTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureTemplate)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,SecurityPostureClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListLocationsPagedResponse)>` |   
  
### listPostureDeploymentsSettings()
    
    
    public PagedCallSettings<ListPostureDeploymentsRequest,ListPostureDeploymentsResponse,SecurityPostureClient.ListPostureDeploymentsPagedResponse> listPostureDeploymentsSettings()

Returns the object with the settings used for calls to listPostureDeployments.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPostureDeploymentsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureDeploymentsRequest),[ListPostureDeploymentsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureDeploymentsResponse),[ListPostureDeploymentsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureDeploymentsPagedResponse)>` |   
  
### listPostureRevisionsSettings()
    
    
    public PagedCallSettings<ListPostureRevisionsRequest,ListPostureRevisionsResponse,SecurityPostureClient.ListPostureRevisionsPagedResponse> listPostureRevisionsSettings()

Returns the object with the settings used for calls to listPostureRevisions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPostureRevisionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureRevisionsRequest),[ListPostureRevisionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureRevisionsResponse),[ListPostureRevisionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureRevisionsPagedResponse)>` |   
  
### listPostureTemplatesSettings()
    
    
    public PagedCallSettings<ListPostureTemplatesRequest,ListPostureTemplatesResponse,SecurityPostureClient.ListPostureTemplatesPagedResponse> listPostureTemplatesSettings()

Returns the object with the settings used for calls to listPostureTemplates.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPostureTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureTemplatesRequest),[ListPostureTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPostureTemplatesResponse),[ListPostureTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPostureTemplatesPagedResponse)>` |   
  
### listPosturesSettings()
    
    
    public PagedCallSettings<ListPosturesRequest,ListPosturesResponse,SecurityPostureClient.ListPosturesPagedResponse> listPosturesSettings()

Returns the object with the settings used for calls to listPostures.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPosturesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPosturesRequest),[ListPosturesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ListPosturesResponse),[ListPosturesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureClient.ListPosturesPagedResponse)>` |   
  
### toBuilder()
    
    
    public SecurityPostureSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[SecurityPostureSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.SecurityPostureSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updatePostureDeploymentOperationSettings()
    
    
    public OperationCallSettings<UpdatePostureDeploymentRequest,PostureDeployment,OperationMetadata> updatePostureDeploymentOperationSettings()

Returns the object with the settings used for calls to updatePostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureDeploymentRequest),[PostureDeployment](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PostureDeployment),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureDeploymentSettings()
    
    
    public UnaryCallSettings<UpdatePostureDeploymentRequest,Operation> updatePostureDeploymentSettings()

Returns the object with the settings used for calls to updatePostureDeployment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePostureDeploymentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureDeploymentRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updatePostureOperationSettings()
    
    
    public OperationCallSettings<UpdatePostureRequest,Posture,OperationMetadata> updatePostureOperationSettings()

Returns the object with the settings used for calls to updatePosture.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureRequest),[Posture](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Posture),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.OperationMetadata)>` |   
  
### updatePostureSettings()
    
    
    public UnaryCallSettings<UpdatePostureRequest,Operation> updatePostureSettings()

Returns the object with the settings used for calls to updatePosture.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePostureRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.UpdatePostureRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
