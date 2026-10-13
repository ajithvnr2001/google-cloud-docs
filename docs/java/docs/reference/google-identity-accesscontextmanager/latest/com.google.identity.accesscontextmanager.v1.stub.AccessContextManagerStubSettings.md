---
url: https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings
title: Class AccessContextManagerStubSettings (1.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:13.602324+00:00
---

# Class AccessContextManagerStubSettings (1.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AccessContextManagerStubSettings (1.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.100.0 (latest)  1.96.0  1.95.0  1.94.0  1.92.0  1.89.0  1.88.0  1.86.0  1.84.0  1.83.0  1.82.0  1.81.0  1.79.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.71.0  1.69.0  1.68.0  1.65.0  1.64.0  1.63.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.5  1.3.1  1.2.10 
    
    
    public class AccessContextManagerStubSettings extends StubSettings<AccessContextManagerStubSettings>

Settings class to configure an instance of [AccessContextManagerStub](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStub).

The default instance has everything set to sensible defaults:

  * The default service address (accesscontextmanager.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getAccessPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessContextManagerStubSettings.Builder accessContextManagerSettingsBuilder =
         AccessContextManagerStubSettings.newBuilder();
     accessContextManagerSettingsBuilder
         .getAccessPolicySettings()
         .setRetrySettings(
             accessContextManagerSettingsBuilder
                 .getAccessPolicySettings()
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
     AccessContextManagerStubSettings accessContextManagerSettings =
         accessContextManagerSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createAccessPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessContextManagerStubSettings.Builder accessContextManagerSettingsBuilder =
         AccessContextManagerStubSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     accessContextManagerSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > AccessContextManagerStubSettings

## Inherited Members

[StubSettings.getApiKey()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getApiKey__)

[StubSettings.getBackgroundExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getBackgroundExecutorProvider__)

[StubSettings.getClock()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getClock__)

[StubSettings.getCredentialsProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getCredentialsProvider__)

[StubSettings.getEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getEndpoint__)

[StubSettings.getExecutorProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getExecutorProvider__)

[StubSettings.getGdchApiAudience()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getGdchApiAudience__)

[StubSettings.getHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getHeaderProvider__)

[StubSettings.getInternalHeaderProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getInternalHeaderProvider__)

[StubSettings.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

[StubSettings.getMtlsEndpoint()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getMtlsEndpoint__)

[StubSettings.getQuotaProjectId()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getQuotaProjectId__)

[StubSettings.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

[StubSettings.getStreamWatchdogCheckInterval()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getStreamWatchdogCheckInterval__)

[StubSettings.getStreamWatchdogCheckIntervalDuration()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getStreamWatchdogCheckIntervalDuration__)

[StubSettings.getStreamWatchdogProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getStreamWatchdogProvider__)

[StubSettings.getTracerFactory()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getTracerFactory__)

[StubSettings.getTransportChannelProvider()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getTransportChannelProvider__)

[StubSettings.getUniverseDomain()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getUniverseDomain__)

[StubSettings.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

[StubSettings.toString()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toString__)

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
  
### defaultGrpcApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultGrpcApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultHttpJsonApiClientHeaderProviderBuilder()
    
    
    public static ApiClientHeaderProvider.Builder defaultHttpJsonApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
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

**Obsolete**

_Use getEndpoint() instead_

This feature is stable for usage in this major version, but may be deprecated in a future release.

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultMtlsEndpoint()
    
    
    public static String getDefaultMtlsEndpoint()

Returns the default mTLS service endpoint.

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
    
    
    public static AccessContextManagerStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AccessContextManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static AccessContextManagerStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessContextManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static AccessContextManagerStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AccessContextManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings.Builder)` |   
  
## Constructors 

### AccessContextManagerStubSettings(AccessContextManagerStubSettings.Builder settingsBuilder)
    
    
    protected AccessContextManagerStubSettings(AccessContextManagerStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[AccessContextManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings.Builder)`  
  
  
## Methods 

### commitServicePerimetersOperationSettings()
    
    
    public OperationCallSettings<CommitServicePerimetersRequest,CommitServicePerimetersResponse,AccessContextManagerOperationMetadata> commitServicePerimetersOperationSettings()

Returns the object with the settings used for calls to commitServicePerimeters.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CommitServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CommitServicePerimetersRequest),[CommitServicePerimetersResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CommitServicePerimetersResponse),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### commitServicePerimetersSettings()
    
    
    public UnaryCallSettings<CommitServicePerimetersRequest,Operation> commitServicePerimetersSettings()

Returns the object with the settings used for calls to commitServicePerimeters.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CommitServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CommitServicePerimetersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAccessLevelOperationSettings()
    
    
    public OperationCallSettings<CreateAccessLevelRequest,AccessLevel,AccessContextManagerOperationMetadata> createAccessLevelOperationSettings()

Returns the object with the settings used for calls to createAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateAccessLevelRequest),[AccessLevel](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessLevel),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### createAccessLevelSettings()
    
    
    public UnaryCallSettings<CreateAccessLevelRequest,Operation> createAccessLevelSettings()

Returns the object with the settings used for calls to createAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateAccessLevelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createAccessPolicyOperationSettings()
    
    
    public OperationCallSettings<AccessPolicy,AccessPolicy,AccessContextManagerOperationMetadata> createAccessPolicyOperationSettings()

Returns the object with the settings used for calls to createAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy),[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### createAccessPolicySettings()
    
    
    public UnaryCallSettings<AccessPolicy,Operation> createAccessPolicySettings()

Returns the object with the settings used for calls to createAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGcpUserAccessBindingOperationSettings()
    
    
    public OperationCallSettings<CreateGcpUserAccessBindingRequest,GcpUserAccessBinding,GcpUserAccessBindingOperationMetadata> createGcpUserAccessBindingOperationSettings()

Returns the object with the settings used for calls to createGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateGcpUserAccessBindingRequest),[GcpUserAccessBinding](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBinding),[GcpUserAccessBindingOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBindingOperationMetadata)>` |   
  
### createGcpUserAccessBindingSettings()
    
    
    public UnaryCallSettings<CreateGcpUserAccessBindingRequest,Operation> createGcpUserAccessBindingSettings()

Returns the object with the settings used for calls to createGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateGcpUserAccessBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServicePerimeterOperationSettings()
    
    
    public OperationCallSettings<CreateServicePerimeterRequest,ServicePerimeter,AccessContextManagerOperationMetadata> createServicePerimeterOperationSettings()

Returns the object with the settings used for calls to createServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateServicePerimeterRequest),[ServicePerimeter](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeter),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### createServicePerimeterSettings()
    
    
    public UnaryCallSettings<CreateServicePerimeterRequest,Operation> createServicePerimeterSettings()

Returns the object with the settings used for calls to createServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.CreateServicePerimeterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createStub()
    
    
    public AccessContextManagerStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[AccessContextManagerStub](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteAccessLevelOperationSettings()
    
    
    public OperationCallSettings<DeleteAccessLevelRequest,Empty,AccessContextManagerOperationMetadata> deleteAccessLevelOperationSettings()

Returns the object with the settings used for calls to deleteAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteAccessLevelRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### deleteAccessLevelSettings()
    
    
    public UnaryCallSettings<DeleteAccessLevelRequest,Operation> deleteAccessLevelSettings()

Returns the object with the settings used for calls to deleteAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteAccessLevelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAccessPolicyOperationSettings()
    
    
    public OperationCallSettings<DeleteAccessPolicyRequest,Empty,AccessContextManagerOperationMetadata> deleteAccessPolicyOperationSettings()

Returns the object with the settings used for calls to deleteAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteAccessPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### deleteAccessPolicySettings()
    
    
    public UnaryCallSettings<DeleteAccessPolicyRequest,Operation> deleteAccessPolicySettings()

Returns the object with the settings used for calls to deleteAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteAccessPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGcpUserAccessBindingOperationSettings()
    
    
    public OperationCallSettings<DeleteGcpUserAccessBindingRequest,Empty,GcpUserAccessBindingOperationMetadata> deleteGcpUserAccessBindingOperationSettings()

Returns the object with the settings used for calls to deleteGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteGcpUserAccessBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[GcpUserAccessBindingOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBindingOperationMetadata)>` |   
  
### deleteGcpUserAccessBindingSettings()
    
    
    public UnaryCallSettings<DeleteGcpUserAccessBindingRequest,Operation> deleteGcpUserAccessBindingSettings()

Returns the object with the settings used for calls to deleteGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteGcpUserAccessBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServicePerimeterOperationSettings()
    
    
    public OperationCallSettings<DeleteServicePerimeterRequest,Empty,AccessContextManagerOperationMetadata> deleteServicePerimeterOperationSettings()

Returns the object with the settings used for calls to deleteServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteServicePerimeterRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### deleteServicePerimeterSettings()
    
    
    public UnaryCallSettings<DeleteServicePerimeterRequest,Operation> deleteServicePerimeterSettings()

Returns the object with the settings used for calls to deleteServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.DeleteServicePerimeterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAccessLevelSettings()
    
    
    public UnaryCallSettings<GetAccessLevelRequest,AccessLevel> getAccessLevelSettings()

Returns the object with the settings used for calls to getAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetAccessLevelRequest),[AccessLevel](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessLevel)>` |   
  
### getAccessPolicySettings()
    
    
    public UnaryCallSettings<GetAccessPolicyRequest,AccessPolicy> getAccessPolicySettings()

Returns the object with the settings used for calls to getAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetAccessPolicyRequest),[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy)>` |   
  
### getGcpUserAccessBindingSettings()
    
    
    public UnaryCallSettings<GetGcpUserAccessBindingRequest,GcpUserAccessBinding> getGcpUserAccessBindingSettings()

Returns the object with the settings used for calls to getGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetGcpUserAccessBindingRequest),[GcpUserAccessBinding](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBinding)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getServicePerimeterSettings()
    
    
    public UnaryCallSettings<GetServicePerimeterRequest,ServicePerimeter> getServicePerimeterSettings()

Returns the object with the settings used for calls to getServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GetServicePerimeterRequest),[ServicePerimeter](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeter)>` |   
  
### listAccessLevelsSettings()
    
    
    public PagedCallSettings<ListAccessLevelsRequest,ListAccessLevelsResponse,AccessContextManagerClient.ListAccessLevelsPagedResponse> listAccessLevelsSettings()

Returns the object with the settings used for calls to listAccessLevels.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAccessLevelsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessLevelsRequest),[ListAccessLevelsResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessLevelsResponse),[ListAccessLevelsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerClient.ListAccessLevelsPagedResponse)>` |   
  
### listAccessPoliciesSettings()
    
    
    public PagedCallSettings<ListAccessPoliciesRequest,ListAccessPoliciesResponse,AccessContextManagerClient.ListAccessPoliciesPagedResponse> listAccessPoliciesSettings()

Returns the object with the settings used for calls to listAccessPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAccessPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessPoliciesRequest),[ListAccessPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListAccessPoliciesResponse),[ListAccessPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerClient.ListAccessPoliciesPagedResponse)>` |   
  
### listGcpUserAccessBindingsSettings()
    
    
    public PagedCallSettings<ListGcpUserAccessBindingsRequest,ListGcpUserAccessBindingsResponse,AccessContextManagerClient.ListGcpUserAccessBindingsPagedResponse> listGcpUserAccessBindingsSettings()

Returns the object with the settings used for calls to listGcpUserAccessBindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGcpUserAccessBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsRequest),[ListGcpUserAccessBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListGcpUserAccessBindingsResponse),[ListGcpUserAccessBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerClient.ListGcpUserAccessBindingsPagedResponse)>` |   
  
### listServicePerimetersSettings()
    
    
    public PagedCallSettings<ListServicePerimetersRequest,ListServicePerimetersResponse,AccessContextManagerClient.ListServicePerimetersPagedResponse> listServicePerimetersSettings()

Returns the object with the settings used for calls to listServicePerimeters.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListServicePerimetersRequest),[ListServicePerimetersResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ListServicePerimetersResponse),[ListServicePerimetersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerClient.ListServicePerimetersPagedResponse)>` |   
  
### replaceAccessLevelsOperationSettings()
    
    
    public OperationCallSettings<ReplaceAccessLevelsRequest,ReplaceAccessLevelsResponse,AccessContextManagerOperationMetadata> replaceAccessLevelsOperationSettings()

Returns the object with the settings used for calls to replaceAccessLevels.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReplaceAccessLevelsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceAccessLevelsRequest),[ReplaceAccessLevelsResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceAccessLevelsResponse),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### replaceAccessLevelsSettings()
    
    
    public UnaryCallSettings<ReplaceAccessLevelsRequest,Operation> replaceAccessLevelsSettings()

Returns the object with the settings used for calls to replaceAccessLevels.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReplaceAccessLevelsRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceAccessLevelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### replaceServicePerimetersOperationSettings()
    
    
    public OperationCallSettings<ReplaceServicePerimetersRequest,ReplaceServicePerimetersResponse,AccessContextManagerOperationMetadata> replaceServicePerimetersOperationSettings()

Returns the object with the settings used for calls to replaceServicePerimeters.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ReplaceServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersRequest),[ReplaceServicePerimetersResponse](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersResponse),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### replaceServicePerimetersSettings()
    
    
    public UnaryCallSettings<ReplaceServicePerimetersRequest,Operation> replaceServicePerimetersSettings()

Returns the object with the settings used for calls to replaceServicePerimeters.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReplaceServicePerimetersRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ReplaceServicePerimetersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public AccessContextManagerStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[AccessContextManagerStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.stub.AccessContextManagerStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateAccessLevelOperationSettings()
    
    
    public OperationCallSettings<UpdateAccessLevelRequest,AccessLevel,AccessContextManagerOperationMetadata> updateAccessLevelOperationSettings()

Returns the object with the settings used for calls to updateAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateAccessLevelRequest),[AccessLevel](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessLevel),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### updateAccessLevelSettings()
    
    
    public UnaryCallSettings<UpdateAccessLevelRequest,Operation> updateAccessLevelSettings()

Returns the object with the settings used for calls to updateAccessLevel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAccessLevelRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateAccessLevelRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateAccessPolicyOperationSettings()
    
    
    public OperationCallSettings<UpdateAccessPolicyRequest,AccessPolicy,AccessContextManagerOperationMetadata> updateAccessPolicyOperationSettings()

Returns the object with the settings used for calls to updateAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateAccessPolicyRequest),[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessPolicy),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### updateAccessPolicySettings()
    
    
    public UnaryCallSettings<UpdateAccessPolicyRequest,Operation> updateAccessPolicySettings()

Returns the object with the settings used for calls to updateAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateAccessPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGcpUserAccessBindingOperationSettings()
    
    
    public OperationCallSettings<UpdateGcpUserAccessBindingRequest,GcpUserAccessBinding,GcpUserAccessBindingOperationMetadata> updateGcpUserAccessBindingOperationSettings()

Returns the object with the settings used for calls to updateGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest),[GcpUserAccessBinding](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBinding),[GcpUserAccessBindingOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.GcpUserAccessBindingOperationMetadata)>` |   
  
### updateGcpUserAccessBindingSettings()
    
    
    public UnaryCallSettings<UpdateGcpUserAccessBindingRequest,Operation> updateGcpUserAccessBindingSettings()

Returns the object with the settings used for calls to updateGcpUserAccessBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateGcpUserAccessBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateGcpUserAccessBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServicePerimeterOperationSettings()
    
    
    public OperationCallSettings<UpdateServicePerimeterRequest,ServicePerimeter,AccessContextManagerOperationMetadata> updateServicePerimeterOperationSettings()

Returns the object with the settings used for calls to updateServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateServicePerimeterRequest),[ServicePerimeter](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.ServicePerimeter),[AccessContextManagerOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.AccessContextManagerOperationMetadata)>` |   
  
### updateServicePerimeterSettings()
    
    
    public UnaryCallSettings<UpdateServicePerimeterRequest,Operation> updateServicePerimeterSettings()

Returns the object with the settings used for calls to updateServicePerimeter.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateServicePerimeterRequest](https://docs.cloud.google.com/java/docs/reference/google-identity-accesscontextmanager/latest/com.google.identity.accesscontextmanager.v1.UpdateServicePerimeterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
