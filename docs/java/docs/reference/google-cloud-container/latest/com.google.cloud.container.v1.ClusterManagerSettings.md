---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings
title: Class ClusterManagerSettings (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:41:48.816265+00:00
---

# Class ClusterManagerSettings (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ClusterManagerSettings (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public class ClusterManagerSettings extends ClientSettings<ClusterManagerSettings>

Settings class to configure an instance of [ClusterManagerClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1beta1.ClusterManagerClient).

The default instance has everything set to sensible defaults:

  * The default service address (container.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of listClusters:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ClusterManagerSettings.Builder clusterManagerSettingsBuilder =
         ClusterManagerSettings.newBuilder();
     clusterManagerSettingsBuilder
         .listClustersSettings()
         .setRetrySettings(
             clusterManagerSettingsBuilder
                 .listClustersSettings()
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
     ClusterManagerSettings clusterManagerSettings = clusterManagerSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > ClusterManagerSettings

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

### create(ClusterManagerStubSettings stub)
    
    
    public static final ClusterManagerSettings create(ClusterManagerStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ClusterManagerStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.stub.ClusterManagerStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings)` |   
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
    
    
    public static ClusterManagerSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static ClusterManagerSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static ClusterManagerSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings.Builder)` |   
  
## Constructors 

### ClusterManagerSettings(ClusterManagerSettings.Builder settingsBuilder)
    
    
    protected ClusterManagerSettings(ClusterManagerSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[ClusterManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings.Builder)`  
  
  
## Methods 

### cancelOperationSettings()
    
    
    public UnaryCallSettings<CancelOperationRequest,Empty> cancelOperationSettings()

Returns the object with the settings used for calls to cancel.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CancelOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CancelOperationRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### checkAutopilotCompatibilitySettings()
    
    
    public UnaryCallSettings<CheckAutopilotCompatibilityRequest,CheckAutopilotCompatibilityResponse> checkAutopilotCompatibilitySettings()

Returns the object with the settings used for calls to checkAutopilotCompatibility.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CheckAutopilotCompatibilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityRequest),[CheckAutopilotCompatibilityResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CheckAutopilotCompatibilityResponse)>` |   
  
### completeControlPlaneUpgradeSettings()
    
    
    public UnaryCallSettings<CompleteControlPlaneUpgradeRequest,Operation> completeControlPlaneUpgradeSettings()

Returns the object with the settings used for calls to completeControlPlaneUpgrade.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CompleteControlPlaneUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteControlPlaneUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### completeIPRotationSettings()
    
    
    public UnaryCallSettings<CompleteIPRotationRequest,Operation> completeIPRotationSettings()

Returns the object with the settings used for calls to completeIPRotation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CompleteIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### completeNodePoolUpgradeSettings()
    
    
    public UnaryCallSettings<CompleteNodePoolUpgradeRequest,Empty> completeNodePoolUpgradeSettings()

Returns the object with the settings used for calls to completeNodePoolUpgrade.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CompleteNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CompleteNodePoolUpgradeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### createClusterSettings()
    
    
    public UnaryCallSettings<CreateClusterRequest,Operation> createClusterSettings()

Returns the object with the settings used for calls to createCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### createNodePoolSettings()
    
    
    public UnaryCallSettings<CreateNodePoolRequest,Operation> createNodePoolSettings()

Returns the object with the settings used for calls to createNodePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.CreateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### deleteClusterSettings()
    
    
    public UnaryCallSettings<DeleteClusterRequest,Operation> deleteClusterSettings()

Returns the object with the settings used for calls to deleteCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### deleteNodePoolSettings()
    
    
    public UnaryCallSettings<DeleteNodePoolRequest,Operation> deleteNodePoolSettings()

Returns the object with the settings used for calls to deleteNodePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### fetchClusterUpgradeInfoSettings()
    
    
    public UnaryCallSettings<FetchClusterUpgradeInfoRequest,ClusterUpgradeInfo> fetchClusterUpgradeInfoSettings()

Returns the object with the settings used for calls to fetchClusterUpgradeInfo.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchClusterUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchClusterUpgradeInfoRequest),[ClusterUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ClusterUpgradeInfo)>` |   
  
### fetchNodePoolUpgradeInfoSettings()
    
    
    public UnaryCallSettings<FetchNodePoolUpgradeInfoRequest,NodePoolUpgradeInfo> fetchNodePoolUpgradeInfoSettings()

Returns the object with the settings used for calls to fetchNodePoolUpgradeInfo.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchNodePoolUpgradeInfoRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.FetchNodePoolUpgradeInfoRequest),[NodePoolUpgradeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePoolUpgradeInfo)>` |   
  
### getClusterSettings()
    
    
    public UnaryCallSettings<GetClusterRequest,Cluster> getClusterSettings()

Returns the object with the settings used for calls to getCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetClusterRequest),[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Cluster)>` |   
  
### getJSONWebKeysSettings()
    
    
    public UnaryCallSettings<GetJSONWebKeysRequest,GetJSONWebKeysResponse> getJSONWebKeysSettings()

Returns the object with the settings used for calls to getJSONWebKeys.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetJSONWebKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysRequest),[GetJSONWebKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetJSONWebKeysResponse)>` |   
  
### getNodePoolSettings()
    
    
    public UnaryCallSettings<GetNodePoolRequest,NodePool> getNodePoolSettings()

Returns the object with the settings used for calls to getNodePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetNodePoolRequest),[NodePool](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.NodePool)>` |   
  
### getOperationSettings()
    
    
    public UnaryCallSettings<GetOperationRequest,Operation> getOperationSettings()

Returns the object with the settings used for calls to get.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetOperationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetOperationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### getServerConfigSettings()
    
    
    public UnaryCallSettings<GetServerConfigRequest,ServerConfig> getServerConfigSettings()

Returns the object with the settings used for calls to getServerConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetServerConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.GetServerConfigRequest),[ServerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ServerConfig)>` |   
  
### listClustersSettings()
    
    
    public UnaryCallSettings<ListClustersRequest,ListClustersResponse> listClustersSettings()

Returns the object with the settings used for calls to listClusters.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ListClustersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersRequest),[ListClustersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListClustersResponse)>` |   
  
### listNodePoolsSettings()
    
    
    public UnaryCallSettings<ListNodePoolsRequest,ListNodePoolsResponse> listNodePoolsSettings()

Returns the object with the settings used for calls to listNodePools.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ListNodePoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsRequest),[ListNodePoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListNodePoolsResponse)>` |   
  
### listOperationsSettings()
    
    
    public UnaryCallSettings<ListOperationsRequest,ListOperationsResponse> listOperationsSettings()

Returns the object with the settings used for calls to listOperations.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ListOperationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsRequest),[ListOperationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListOperationsResponse)>` |   
  
### listUsableSubnetworksSettings()
    
    
    public PagedCallSettings<ListUsableSubnetworksRequest,ListUsableSubnetworksResponse,ClusterManagerClient.ListUsableSubnetworksPagedResponse> listUsableSubnetworksSettings()

Returns the object with the settings used for calls to listUsableSubnetworks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListUsableSubnetworksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksRequest),[ListUsableSubnetworksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.ListUsableSubnetworksResponse),[ListUsableSubnetworksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerClient.ListUsableSubnetworksPagedResponse)>` |   
  
### rollbackNodePoolUpgradeSettings()
    
    
    public UnaryCallSettings<RollbackNodePoolUpgradeRequest,Operation> rollbackNodePoolUpgradeSettings()

Returns the object with the settings used for calls to rollbackNodePoolUpgrade.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RollbackNodePoolUpgradeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.RollbackNodePoolUpgradeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setAddonsConfigSettings()
    
    
    public UnaryCallSettings<SetAddonsConfigRequest,Operation> setAddonsConfigSettings()

Returns the object with the settings used for calls to setAddonsConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetAddonsConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetAddonsConfigRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLabelsSettings()
    
    
    public UnaryCallSettings<SetLabelsRequest,Operation> setLabelsSettings()

Returns the object with the settings used for calls to setLabels.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetLabelsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLabelsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLegacyAbacSettings()
    
    
    public UnaryCallSettings<SetLegacyAbacRequest,Operation> setLegacyAbacSettings()

Returns the object with the settings used for calls to setLegacyAbac.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetLegacyAbacRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLegacyAbacRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLocationsSettings() (deprecated)
    
    
    public UnaryCallSettings<SetLocationsRequest,Operation> setLocationsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to setLocations.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetLocationsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLocationsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setLoggingServiceSettings()
    
    
    public UnaryCallSettings<SetLoggingServiceRequest,Operation> setLoggingServiceSettings()

Returns the object with the settings used for calls to setLoggingService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetLoggingServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetLoggingServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMaintenancePolicySettings()
    
    
    public UnaryCallSettings<SetMaintenancePolicyRequest,Operation> setMaintenancePolicySettings()

Returns the object with the settings used for calls to setMaintenancePolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMaintenancePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMaintenancePolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMasterAuthSettings()
    
    
    public UnaryCallSettings<SetMasterAuthRequest,Operation> setMasterAuthSettings()

Returns the object with the settings used for calls to setMasterAuth.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMasterAuthRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMasterAuthRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setMonitoringServiceSettings()
    
    
    public UnaryCallSettings<SetMonitoringServiceRequest,Operation> setMonitoringServiceSettings()

Returns the object with the settings used for calls to setMonitoringService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetMonitoringServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetMonitoringServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNetworkPolicySettings()
    
    
    public UnaryCallSettings<SetNetworkPolicyRequest,Operation> setNetworkPolicySettings()

Returns the object with the settings used for calls to setNetworkPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetNetworkPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNetworkPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolAutoscalingSettings()
    
    
    public UnaryCallSettings<SetNodePoolAutoscalingRequest,Operation> setNodePoolAutoscalingSettings()

Returns the object with the settings used for calls to setNodePoolAutoscaling.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetNodePoolAutoscalingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolAutoscalingRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolManagementSettings()
    
    
    public UnaryCallSettings<SetNodePoolManagementRequest,Operation> setNodePoolManagementSettings()

Returns the object with the settings used for calls to setNodePoolManagement.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetNodePoolManagementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolManagementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### setNodePoolSizeSettings()
    
    
    public UnaryCallSettings<SetNodePoolSizeRequest,Operation> setNodePoolSizeSettings()

Returns the object with the settings used for calls to setNodePoolSize.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetNodePoolSizeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.SetNodePoolSizeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### startIPRotationSettings()
    
    
    public UnaryCallSettings<StartIPRotationRequest,Operation> startIPRotationSettings()

Returns the object with the settings used for calls to startIPRotation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartIPRotationRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.StartIPRotationRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### toBuilder()
    
    
    public ClusterManagerSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[ClusterManagerSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.cloud.container.v1.ClusterManagerSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateClusterSettings()
    
    
    public UnaryCallSettings<UpdateClusterRequest,Operation> updateClusterSettings()

Returns the object with the settings used for calls to updateCluster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateClusterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateClusterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateMasterSettings()
    
    
    public UnaryCallSettings<UpdateMasterRequest,Operation> updateMasterSettings()

Returns the object with the settings used for calls to updateMaster.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateMasterRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateMasterRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
### updateNodePoolSettings()
    
    
    public UnaryCallSettings<UpdateNodePoolRequest,Operation> updateNodePoolSettings()

Returns the object with the settings used for calls to updateNodePool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateNodePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.UpdateNodePoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.Operation)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
