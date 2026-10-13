---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings
title: Class NetworkServicesSettings (0.55.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:36:04.589781+00:00
---

# Class NetworkServicesSettings (0.55.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class NetworkServicesSettings (0.55.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.55.0 (latest)  0.51.0  0.50.0  0.49.0  0.47.0  0.44.0  0.43.0  0.41.0  0.39.0  0.38.0  0.36.0  0.34.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class NetworkServicesSettings extends ClientSettings<NetworkServicesSettings>

Settings class to configure an instance of [NetworkServicesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1beta1.NetworkServicesClient).

The default instance has everything set to sensible defaults:

  * The default service address (networkservices.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getEndpointPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServicesSettings.Builder networkServicesSettingsBuilder =
         NetworkServicesSettings.newBuilder();
     networkServicesSettingsBuilder
         .getEndpointPolicySettings()
         .setRetrySettings(
             networkServicesSettingsBuilder
                 .getEndpointPolicySettings()
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
     NetworkServicesSettings networkServicesSettings = networkServicesSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createEndpointPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     NetworkServicesSettings.Builder networkServicesSettingsBuilder =
         NetworkServicesSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     networkServicesSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > NetworkServicesSettings

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

### create(NetworkServicesStubSettings stub)
    
    
    public static final NetworkServicesSettings create(NetworkServicesStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[NetworkServicesStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.stub.NetworkServicesStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings)` |   
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
    
    
    public static NetworkServicesSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static NetworkServicesSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static NetworkServicesSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings.Builder)` |   
  
## Constructors 

### NetworkServicesSettings(NetworkServicesSettings.Builder settingsBuilder)
    
    
    protected NetworkServicesSettings(NetworkServicesSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[NetworkServicesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings.Builder)`  
  
  
## Methods 

### createAgentGatewayOperationSettings()
    
    
    public OperationCallSettings<CreateAgentGatewayRequest,AgentGateway,OperationMetadata> createAgentGatewayOperationSettings()

Returns the object with the settings used for calls to createAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest),[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createAgentGatewaySettings()
    
    
    public UnaryCallSettings<CreateAgentGatewayRequest,Operation> createAgentGatewaySettings()

Returns the object with the settings used for calls to createAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateAgentGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createEndpointPolicyOperationSettings()
    
    
    public OperationCallSettings<CreateEndpointPolicyRequest,EndpointPolicy,OperationMetadata> createEndpointPolicyOperationSettings()

Returns the object with the settings used for calls to createEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest),[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createEndpointPolicySettings()
    
    
    public UnaryCallSettings<CreateEndpointPolicyRequest,Operation> createEndpointPolicySettings()

Returns the object with the settings used for calls to createEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateEndpointPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGatewayOperationSettings()
    
    
    public OperationCallSettings<CreateGatewayRequest,Gateway,OperationMetadata> createGatewayOperationSettings()

Returns the object with the settings used for calls to createGateway.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest),[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGatewaySettings()
    
    
    public UnaryCallSettings<CreateGatewayRequest,Operation> createGatewaySettings()

Returns the object with the settings used for calls to createGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createGrpcRouteOperationSettings()
    
    
    public OperationCallSettings<CreateGrpcRouteRequest,GrpcRoute,OperationMetadata> createGrpcRouteOperationSettings()

Returns the object with the settings used for calls to createGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest),[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createGrpcRouteSettings()
    
    
    public UnaryCallSettings<CreateGrpcRouteRequest,Operation> createGrpcRouteSettings()

Returns the object with the settings used for calls to createGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateGrpcRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createHttpRouteOperationSettings()
    
    
    public OperationCallSettings<CreateHttpRouteRequest,HttpRoute,OperationMetadata> createHttpRouteOperationSettings()

Returns the object with the settings used for calls to createHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest),[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createHttpRouteSettings()
    
    
    public UnaryCallSettings<CreateHttpRouteRequest,Operation> createHttpRouteSettings()

Returns the object with the settings used for calls to createHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateHttpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createMeshOperationSettings()
    
    
    public OperationCallSettings<CreateMeshRequest,Mesh,OperationMetadata> createMeshOperationSettings()

Returns the object with the settings used for calls to createMesh.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest),[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createMeshSettings()
    
    
    public UnaryCallSettings<CreateMeshRequest,Operation> createMeshSettings()

Returns the object with the settings used for calls to createMesh.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateMeshRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceBindingOperationSettings()
    
    
    public OperationCallSettings<CreateServiceBindingRequest,ServiceBinding,OperationMetadata> createServiceBindingOperationSettings()

Returns the object with the settings used for calls to createServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest),[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceBindingSettings()
    
    
    public UnaryCallSettings<CreateServiceBindingRequest,Operation> createServiceBindingSettings()

Returns the object with the settings used for calls to createServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createServiceLbPolicyOperationSettings()
    
    
    public OperationCallSettings<CreateServiceLbPolicyRequest,ServiceLbPolicy,OperationMetadata> createServiceLbPolicyOperationSettings()

Returns the object with the settings used for calls to createServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest),[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createServiceLbPolicySettings()
    
    
    public UnaryCallSettings<CreateServiceLbPolicyRequest,Operation> createServiceLbPolicySettings()

Returns the object with the settings used for calls to createServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateServiceLbPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTcpRouteOperationSettings()
    
    
    public OperationCallSettings<CreateTcpRouteRequest,TcpRoute,OperationMetadata> createTcpRouteOperationSettings()

Returns the object with the settings used for calls to createTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest),[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTcpRouteSettings()
    
    
    public UnaryCallSettings<CreateTcpRouteRequest,Operation> createTcpRouteSettings()

Returns the object with the settings used for calls to createTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTcpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createTlsRouteOperationSettings()
    
    
    public OperationCallSettings<CreateTlsRouteRequest,TlsRoute,OperationMetadata> createTlsRouteOperationSettings()

Returns the object with the settings used for calls to createTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest),[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createTlsRouteSettings()
    
    
    public UnaryCallSettings<CreateTlsRouteRequest,Operation> createTlsRouteSettings()

Returns the object with the settings used for calls to createTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateTlsRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWasmPluginOperationSettings()
    
    
    public OperationCallSettings<CreateWasmPluginRequest,WasmPlugin,OperationMetadata> createWasmPluginOperationSettings()

Returns the object with the settings used for calls to createWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest),[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginSettings()
    
    
    public UnaryCallSettings<CreateWasmPluginRequest,Operation> createWasmPluginSettings()

Returns the object with the settings used for calls to createWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createWasmPluginVersionOperationSettings()
    
    
    public OperationCallSettings<CreateWasmPluginVersionRequest,WasmPluginVersion,OperationMetadata> createWasmPluginVersionOperationSettings()

Returns the object with the settings used for calls to createWasmPluginVersion.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest),[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### createWasmPluginVersionSettings()
    
    
    public UnaryCallSettings<CreateWasmPluginVersionRequest,Operation> createWasmPluginVersionSettings()

Returns the object with the settings used for calls to createWasmPluginVersion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.CreateWasmPluginVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAgentGatewayOperationSettings()
    
    
    public OperationCallSettings<DeleteAgentGatewayRequest,Empty,OperationMetadata> deleteAgentGatewayOperationSettings()

Returns the object with the settings used for calls to deleteAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteAgentGatewaySettings()
    
    
    public UnaryCallSettings<DeleteAgentGatewayRequest,Operation> deleteAgentGatewaySettings()

Returns the object with the settings used for calls to deleteAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteAgentGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteEndpointPolicyOperationSettings()
    
    
    public OperationCallSettings<DeleteEndpointPolicyRequest,Empty,OperationMetadata> deleteEndpointPolicyOperationSettings()

Returns the object with the settings used for calls to deleteEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteEndpointPolicySettings()
    
    
    public UnaryCallSettings<DeleteEndpointPolicyRequest,Operation> deleteEndpointPolicySettings()

Returns the object with the settings used for calls to deleteEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteEndpointPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGatewayOperationSettings()
    
    
    public OperationCallSettings<DeleteGatewayRequest,Empty,OperationMetadata> deleteGatewayOperationSettings()

Returns the object with the settings used for calls to deleteGateway.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGatewaySettings()
    
    
    public UnaryCallSettings<DeleteGatewayRequest,Operation> deleteGatewaySettings()

Returns the object with the settings used for calls to deleteGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteGrpcRouteOperationSettings()
    
    
    public OperationCallSettings<DeleteGrpcRouteRequest,Empty,OperationMetadata> deleteGrpcRouteOperationSettings()

Returns the object with the settings used for calls to deleteGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteGrpcRouteSettings()
    
    
    public UnaryCallSettings<DeleteGrpcRouteRequest,Operation> deleteGrpcRouteSettings()

Returns the object with the settings used for calls to deleteGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteGrpcRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteHttpRouteOperationSettings()
    
    
    public OperationCallSettings<DeleteHttpRouteRequest,Empty,OperationMetadata> deleteHttpRouteOperationSettings()

Returns the object with the settings used for calls to deleteHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteHttpRouteSettings()
    
    
    public UnaryCallSettings<DeleteHttpRouteRequest,Operation> deleteHttpRouteSettings()

Returns the object with the settings used for calls to deleteHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteHttpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteMeshOperationSettings()
    
    
    public OperationCallSettings<DeleteMeshRequest,Empty,OperationMetadata> deleteMeshOperationSettings()

Returns the object with the settings used for calls to deleteMesh.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteMeshSettings()
    
    
    public UnaryCallSettings<DeleteMeshRequest,Operation> deleteMeshSettings()

Returns the object with the settings used for calls to deleteMesh.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteMeshRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceBindingOperationSettings()
    
    
    public OperationCallSettings<DeleteServiceBindingRequest,Empty,OperationMetadata> deleteServiceBindingOperationSettings()

Returns the object with the settings used for calls to deleteServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceBindingSettings()
    
    
    public UnaryCallSettings<DeleteServiceBindingRequest,Operation> deleteServiceBindingSettings()

Returns the object with the settings used for calls to deleteServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteServiceLbPolicyOperationSettings()
    
    
    public OperationCallSettings<DeleteServiceLbPolicyRequest,Empty,OperationMetadata> deleteServiceLbPolicyOperationSettings()

Returns the object with the settings used for calls to deleteServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteServiceLbPolicySettings()
    
    
    public UnaryCallSettings<DeleteServiceLbPolicyRequest,Operation> deleteServiceLbPolicySettings()

Returns the object with the settings used for calls to deleteServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteServiceLbPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTcpRouteOperationSettings()
    
    
    public OperationCallSettings<DeleteTcpRouteRequest,Empty,OperationMetadata> deleteTcpRouteOperationSettings()

Returns the object with the settings used for calls to deleteTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTcpRouteSettings()
    
    
    public UnaryCallSettings<DeleteTcpRouteRequest,Operation> deleteTcpRouteSettings()

Returns the object with the settings used for calls to deleteTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTcpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteTlsRouteOperationSettings()
    
    
    public OperationCallSettings<DeleteTlsRouteRequest,Empty,OperationMetadata> deleteTlsRouteOperationSettings()

Returns the object with the settings used for calls to deleteTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteTlsRouteSettings()
    
    
    public UnaryCallSettings<DeleteTlsRouteRequest,Operation> deleteTlsRouteSettings()

Returns the object with the settings used for calls to deleteTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteTlsRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWasmPluginOperationSettings()
    
    
    public OperationCallSettings<DeleteWasmPluginRequest,Empty,OperationMetadata> deleteWasmPluginOperationSettings()

Returns the object with the settings used for calls to deleteWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginSettings()
    
    
    public UnaryCallSettings<DeleteWasmPluginRequest,Operation> deleteWasmPluginSettings()

Returns the object with the settings used for calls to deleteWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteWasmPluginVersionOperationSettings()
    
    
    public OperationCallSettings<DeleteWasmPluginVersionRequest,Empty,OperationMetadata> deleteWasmPluginVersionOperationSettings()

Returns the object with the settings used for calls to deleteWasmPluginVersion.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### deleteWasmPluginVersionSettings()
    
    
    public UnaryCallSettings<DeleteWasmPluginVersionRequest,Operation> deleteWasmPluginVersionSettings()

Returns the object with the settings used for calls to deleteWasmPluginVersion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.DeleteWasmPluginVersionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAgentGatewaySettings()
    
    
    public UnaryCallSettings<GetAgentGatewayRequest,AgentGateway> getAgentGatewaySettings()

Returns the object with the settings used for calls to getAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetAgentGatewayRequest),[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway)>` |   
  
### getEndpointPolicySettings()
    
    
    public UnaryCallSettings<GetEndpointPolicyRequest,EndpointPolicy> getEndpointPolicySettings()

Returns the object with the settings used for calls to getEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetEndpointPolicyRequest),[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy)>` |   
  
### getGatewayRouteViewSettings()
    
    
    public UnaryCallSettings<GetGatewayRouteViewRequest,GatewayRouteView> getGatewayRouteViewSettings()

Returns the object with the settings used for calls to getGatewayRouteView.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGatewayRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRouteViewRequest),[GatewayRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GatewayRouteView)>` |   
  
### getGatewaySettings()
    
    
    public UnaryCallSettings<GetGatewayRequest,Gateway> getGatewaySettings()

Returns the object with the settings used for calls to getGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGatewayRequest),[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway)>` |   
  
### getGrpcRouteSettings()
    
    
    public UnaryCallSettings<GetGrpcRouteRequest,GrpcRoute> getGrpcRouteSettings()

Returns the object with the settings used for calls to getGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetGrpcRouteRequest),[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute)>` |   
  
### getHttpRouteSettings()
    
    
    public UnaryCallSettings<GetHttpRouteRequest,HttpRoute> getHttpRouteSettings()

Returns the object with the settings used for calls to getHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetHttpRouteRequest),[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getMeshRouteViewSettings()
    
    
    public UnaryCallSettings<GetMeshRouteViewRequest,MeshRouteView> getMeshRouteViewSettings()

Returns the object with the settings used for calls to getMeshRouteView.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetMeshRouteViewRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRouteViewRequest),[MeshRouteView](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.MeshRouteView)>` |   
  
### getMeshSettings()
    
    
    public UnaryCallSettings<GetMeshRequest,Mesh> getMeshSettings()

Returns the object with the settings used for calls to getMesh.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetMeshRequest),[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh)>` |   
  
### getServiceBindingSettings()
    
    
    public UnaryCallSettings<GetServiceBindingRequest,ServiceBinding> getServiceBindingSettings()

Returns the object with the settings used for calls to getServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceBindingRequest),[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding)>` |   
  
### getServiceLbPolicySettings()
    
    
    public UnaryCallSettings<GetServiceLbPolicyRequest,ServiceLbPolicy> getServiceLbPolicySettings()

Returns the object with the settings used for calls to getServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetServiceLbPolicyRequest),[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy)>` |   
  
### getTcpRouteSettings()
    
    
    public UnaryCallSettings<GetTcpRouteRequest,TcpRoute> getTcpRouteSettings()

Returns the object with the settings used for calls to getTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTcpRouteRequest),[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute)>` |   
  
### getTlsRouteSettings()
    
    
    public UnaryCallSettings<GetTlsRouteRequest,TlsRoute> getTlsRouteSettings()

Returns the object with the settings used for calls to getTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetTlsRouteRequest),[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute)>` |   
  
### getWasmPluginSettings()
    
    
    public UnaryCallSettings<GetWasmPluginRequest,WasmPlugin> getWasmPluginSettings()

Returns the object with the settings used for calls to getWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginRequest),[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin)>` |   
  
### getWasmPluginVersionSettings()
    
    
    public UnaryCallSettings<GetWasmPluginVersionRequest,WasmPluginVersion> getWasmPluginVersionSettings()

Returns the object with the settings used for calls to getWasmPluginVersion.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetWasmPluginVersionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GetWasmPluginVersionRequest),[WasmPluginVersion](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPluginVersion)>` |   
  
### listAgentGatewaysSettings()
    
    
    public PagedCallSettings<ListAgentGatewaysRequest,ListAgentGatewaysResponse,NetworkServicesClient.ListAgentGatewaysPagedResponse> listAgentGatewaysSettings()

Returns the object with the settings used for calls to listAgentGateways.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAgentGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysRequest),[ListAgentGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListAgentGatewaysResponse),[ListAgentGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListAgentGatewaysPagedResponse)>` |   
  
### listEndpointPoliciesSettings()
    
    
    public PagedCallSettings<ListEndpointPoliciesRequest,ListEndpointPoliciesResponse,NetworkServicesClient.ListEndpointPoliciesPagedResponse> listEndpointPoliciesSettings()

Returns the object with the settings used for calls to listEndpointPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEndpointPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesRequest),[ListEndpointPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListEndpointPoliciesResponse),[ListEndpointPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListEndpointPoliciesPagedResponse)>` |   
  
### listGatewayRouteViewsSettings()
    
    
    public PagedCallSettings<ListGatewayRouteViewsRequest,ListGatewayRouteViewsResponse,NetworkServicesClient.ListGatewayRouteViewsPagedResponse> listGatewayRouteViewsSettings()

Returns the object with the settings used for calls to listGatewayRouteViews.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGatewayRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsRequest),[ListGatewayRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewayRouteViewsResponse),[ListGatewayRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewayRouteViewsPagedResponse)>` |   
  
### listGatewaysSettings()
    
    
    public PagedCallSettings<ListGatewaysRequest,ListGatewaysResponse,NetworkServicesClient.ListGatewaysPagedResponse> listGatewaysSettings()

Returns the object with the settings used for calls to listGateways.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGatewaysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysRequest),[ListGatewaysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGatewaysResponse),[ListGatewaysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGatewaysPagedResponse)>` |   
  
### listGrpcRoutesSettings()
    
    
    public PagedCallSettings<ListGrpcRoutesRequest,ListGrpcRoutesResponse,NetworkServicesClient.ListGrpcRoutesPagedResponse> listGrpcRoutesSettings()

Returns the object with the settings used for calls to listGrpcRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListGrpcRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesRequest),[ListGrpcRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListGrpcRoutesResponse),[ListGrpcRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListGrpcRoutesPagedResponse)>` |   
  
### listHttpRoutesSettings()
    
    
    public PagedCallSettings<ListHttpRoutesRequest,ListHttpRoutesResponse,NetworkServicesClient.ListHttpRoutesPagedResponse> listHttpRoutesSettings()

Returns the object with the settings used for calls to listHttpRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListHttpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesRequest),[ListHttpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListHttpRoutesResponse),[ListHttpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListHttpRoutesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,NetworkServicesClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListLocationsPagedResponse)>` |   
  
### listMeshRouteViewsSettings()
    
    
    public PagedCallSettings<ListMeshRouteViewsRequest,ListMeshRouteViewsResponse,NetworkServicesClient.ListMeshRouteViewsPagedResponse> listMeshRouteViewsSettings()

Returns the object with the settings used for calls to listMeshRouteViews.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListMeshRouteViewsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsRequest),[ListMeshRouteViewsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshRouteViewsResponse),[ListMeshRouteViewsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshRouteViewsPagedResponse)>` |   
  
### listMeshesSettings()
    
    
    public PagedCallSettings<ListMeshesRequest,ListMeshesResponse,NetworkServicesClient.ListMeshesPagedResponse> listMeshesSettings()

Returns the object with the settings used for calls to listMeshes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListMeshesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesRequest),[ListMeshesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListMeshesResponse),[ListMeshesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListMeshesPagedResponse)>` |   
  
### listServiceBindingsSettings()
    
    
    public PagedCallSettings<ListServiceBindingsRequest,ListServiceBindingsResponse,NetworkServicesClient.ListServiceBindingsPagedResponse> listServiceBindingsSettings()

Returns the object with the settings used for calls to listServiceBindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListServiceBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsRequest),[ListServiceBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceBindingsResponse),[ListServiceBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceBindingsPagedResponse)>` |   
  
### listServiceLbPoliciesSettings()
    
    
    public PagedCallSettings<ListServiceLbPoliciesRequest,ListServiceLbPoliciesResponse,NetworkServicesClient.ListServiceLbPoliciesPagedResponse> listServiceLbPoliciesSettings()

Returns the object with the settings used for calls to listServiceLbPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListServiceLbPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesRequest),[ListServiceLbPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListServiceLbPoliciesResponse),[ListServiceLbPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListServiceLbPoliciesPagedResponse)>` |   
  
### listTcpRoutesSettings()
    
    
    public PagedCallSettings<ListTcpRoutesRequest,ListTcpRoutesResponse,NetworkServicesClient.ListTcpRoutesPagedResponse> listTcpRoutesSettings()

Returns the object with the settings used for calls to listTcpRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTcpRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesRequest),[ListTcpRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTcpRoutesResponse),[ListTcpRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTcpRoutesPagedResponse)>` |   
  
### listTlsRoutesSettings()
    
    
    public PagedCallSettings<ListTlsRoutesRequest,ListTlsRoutesResponse,NetworkServicesClient.ListTlsRoutesPagedResponse> listTlsRoutesSettings()

Returns the object with the settings used for calls to listTlsRoutes.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTlsRoutesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesRequest),[ListTlsRoutesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListTlsRoutesResponse),[ListTlsRoutesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListTlsRoutesPagedResponse)>` |   
  
### listWasmPluginVersionsSettings()
    
    
    public PagedCallSettings<ListWasmPluginVersionsRequest,ListWasmPluginVersionsResponse,NetworkServicesClient.ListWasmPluginVersionsPagedResponse> listWasmPluginVersionsSettings()

Returns the object with the settings used for calls to listWasmPluginVersions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWasmPluginVersionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsRequest),[ListWasmPluginVersionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginVersionsResponse),[ListWasmPluginVersionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginVersionsPagedResponse)>` |   
  
### listWasmPluginsSettings()
    
    
    public PagedCallSettings<ListWasmPluginsRequest,ListWasmPluginsResponse,NetworkServicesClient.ListWasmPluginsPagedResponse> listWasmPluginsSettings()

Returns the object with the settings used for calls to listWasmPlugins.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListWasmPluginsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsRequest),[ListWasmPluginsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ListWasmPluginsResponse),[ListWasmPluginsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesClient.ListWasmPluginsPagedResponse)>` |   
  
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
    
    
    public NetworkServicesSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[NetworkServicesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.NetworkServicesSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateAgentGatewayOperationSettings()
    
    
    public OperationCallSettings<UpdateAgentGatewayRequest,AgentGateway,OperationMetadata> updateAgentGatewayOperationSettings()

Returns the object with the settings used for calls to updateAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest),[AgentGateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.AgentGateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateAgentGatewaySettings()
    
    
    public UnaryCallSettings<UpdateAgentGatewayRequest,Operation> updateAgentGatewaySettings()

Returns the object with the settings used for calls to updateAgentGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAgentGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateAgentGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateEndpointPolicyOperationSettings()
    
    
    public OperationCallSettings<UpdateEndpointPolicyRequest,EndpointPolicy,OperationMetadata> updateEndpointPolicyOperationSettings()

Returns the object with the settings used for calls to updateEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest),[EndpointPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.EndpointPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateEndpointPolicySettings()
    
    
    public UnaryCallSettings<UpdateEndpointPolicyRequest,Operation> updateEndpointPolicySettings()

Returns the object with the settings used for calls to updateEndpointPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEndpointPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateEndpointPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGatewayOperationSettings()
    
    
    public OperationCallSettings<UpdateGatewayRequest,Gateway,OperationMetadata> updateGatewayOperationSettings()

Returns the object with the settings used for calls to updateGateway.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest),[Gateway](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Gateway),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGatewaySettings()
    
    
    public UnaryCallSettings<UpdateGatewayRequest,Operation> updateGatewaySettings()

Returns the object with the settings used for calls to updateGateway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateGatewayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGatewayRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateGrpcRouteOperationSettings()
    
    
    public OperationCallSettings<UpdateGrpcRouteRequest,GrpcRoute,OperationMetadata> updateGrpcRouteOperationSettings()

Returns the object with the settings used for calls to updateGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest),[GrpcRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.GrpcRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateGrpcRouteSettings()
    
    
    public UnaryCallSettings<UpdateGrpcRouteRequest,Operation> updateGrpcRouteSettings()

Returns the object with the settings used for calls to updateGrpcRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateGrpcRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateGrpcRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateHttpRouteOperationSettings()
    
    
    public OperationCallSettings<UpdateHttpRouteRequest,HttpRoute,OperationMetadata> updateHttpRouteOperationSettings()

Returns the object with the settings used for calls to updateHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest),[HttpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.HttpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateHttpRouteSettings()
    
    
    public UnaryCallSettings<UpdateHttpRouteRequest,Operation> updateHttpRouteSettings()

Returns the object with the settings used for calls to updateHttpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateHttpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateHttpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateMeshOperationSettings()
    
    
    public OperationCallSettings<UpdateMeshRequest,Mesh,OperationMetadata> updateMeshOperationSettings()

Returns the object with the settings used for calls to updateMesh.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest),[Mesh](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.Mesh),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateMeshSettings()
    
    
    public UnaryCallSettings<UpdateMeshRequest,Operation> updateMeshSettings()

Returns the object with the settings used for calls to updateMesh.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateMeshRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateMeshRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceBindingOperationSettings()
    
    
    public OperationCallSettings<UpdateServiceBindingRequest,ServiceBinding,OperationMetadata> updateServiceBindingOperationSettings()

Returns the object with the settings used for calls to updateServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest),[ServiceBinding](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceBinding),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceBindingSettings()
    
    
    public UnaryCallSettings<UpdateServiceBindingRequest,Operation> updateServiceBindingSettings()

Returns the object with the settings used for calls to updateServiceBinding.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateServiceBindingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceBindingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateServiceLbPolicyOperationSettings()
    
    
    public OperationCallSettings<UpdateServiceLbPolicyRequest,ServiceLbPolicy,OperationMetadata> updateServiceLbPolicyOperationSettings()

Returns the object with the settings used for calls to updateServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest),[ServiceLbPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.ServiceLbPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateServiceLbPolicySettings()
    
    
    public UnaryCallSettings<UpdateServiceLbPolicyRequest,Operation> updateServiceLbPolicySettings()

Returns the object with the settings used for calls to updateServiceLbPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateServiceLbPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateServiceLbPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTcpRouteOperationSettings()
    
    
    public OperationCallSettings<UpdateTcpRouteRequest,TcpRoute,OperationMetadata> updateTcpRouteOperationSettings()

Returns the object with the settings used for calls to updateTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest),[TcpRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TcpRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTcpRouteSettings()
    
    
    public UnaryCallSettings<UpdateTcpRouteRequest,Operation> updateTcpRouteSettings()

Returns the object with the settings used for calls to updateTcpRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTcpRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTcpRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateTlsRouteOperationSettings()
    
    
    public OperationCallSettings<UpdateTlsRouteRequest,TlsRoute,OperationMetadata> updateTlsRouteOperationSettings()

Returns the object with the settings used for calls to updateTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest),[TlsRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.TlsRoute),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateTlsRouteSettings()
    
    
    public UnaryCallSettings<UpdateTlsRouteRequest,Operation> updateTlsRouteSettings()

Returns the object with the settings used for calls to updateTlsRoute.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateTlsRouteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateTlsRouteRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateWasmPluginOperationSettings()
    
    
    public OperationCallSettings<UpdateWasmPluginRequest,WasmPlugin,OperationMetadata> updateWasmPluginOperationSettings()

Returns the object with the settings used for calls to updateWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest),[WasmPlugin](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.WasmPlugin),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.OperationMetadata)>` |   
  
### updateWasmPluginSettings()
    
    
    public UnaryCallSettings<UpdateWasmPluginRequest,Operation> updateWasmPluginSettings()

Returns the object with the settings used for calls to updateWasmPlugin.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateWasmPluginRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-networkservices/latest/com.google.cloud.networkservices.v1.UpdateWasmPluginRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
