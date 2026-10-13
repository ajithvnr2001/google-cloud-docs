---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings
title: Class CloudChannelServiceSettings (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:52.003076+00:00
---

# Class CloudChannelServiceSettings (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudChannelServiceSettings (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 
    
    
    public class CloudChannelServiceSettings extends ClientSettings<CloudChannelServiceSettings>

Settings class to configure an instance of [CloudChannelServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (cloudchannel.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getCustomer:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelServiceSettings.Builder cloudChannelServiceSettingsBuilder =
         CloudChannelServiceSettings.newBuilder();
     cloudChannelServiceSettingsBuilder
         .getCustomerSettings()
         .setRetrySettings(
             cloudChannelServiceSettingsBuilder
                 .getCustomerSettings()
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
     CloudChannelServiceSettings cloudChannelServiceSettings =
         cloudChannelServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for provisionCloudIdentity:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelServiceSettings.Builder cloudChannelServiceSettingsBuilder =
         CloudChannelServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     cloudChannelServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > CloudChannelServiceSettings

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

### create(CloudChannelServiceStubSettings stub)
    
    
    public static final CloudChannelServiceSettings create(CloudChannelServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudChannelServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings)` |   
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
    
    
    public static CloudChannelServiceSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static CloudChannelServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static CloudChannelServiceSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings.Builder)` |   
  
## Constructors 

### CloudChannelServiceSettings(CloudChannelServiceSettings.Builder settingsBuilder)
    
    
    protected CloudChannelServiceSettings(CloudChannelServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[CloudChannelServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings.Builder)`  
  
  
## Methods 

### activateEntitlementOperationSettings()
    
    
    public OperationCallSettings<ActivateEntitlementRequest,Entitlement,OperationMetadata> activateEntitlementOperationSettings()

Returns the object with the settings used for calls to activateEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### activateEntitlementSettings()
    
    
    public UnaryCallSettings<ActivateEntitlementRequest,Operation> activateEntitlementSettings()

Returns the object with the settings used for calls to activateEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ActivateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ActivateEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### cancelEntitlementOperationSettings()
    
    
    public OperationCallSettings<CancelEntitlementRequest,Empty,OperationMetadata> cancelEntitlementOperationSettings()

Returns the object with the settings used for calls to cancelEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### cancelEntitlementSettings()
    
    
    public UnaryCallSettings<CancelEntitlementRequest,Operation> cancelEntitlementSettings()

Returns the object with the settings used for calls to cancelEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CancelEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CancelEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### changeOfferOperationSettings()
    
    
    public OperationCallSettings<ChangeOfferRequest,Entitlement,OperationMetadata> changeOfferOperationSettings()

Returns the object with the settings used for calls to changeOffer.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeOfferSettings()
    
    
    public UnaryCallSettings<ChangeOfferRequest,Operation> changeOfferSettings()

Returns the object with the settings used for calls to changeOffer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ChangeOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeOfferRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### changeParametersOperationSettings()
    
    
    public OperationCallSettings<ChangeParametersRequest,Entitlement,OperationMetadata> changeParametersOperationSettings()

Returns the object with the settings used for calls to changeParameters.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeParametersSettings()
    
    
    public UnaryCallSettings<ChangeParametersRequest,Operation> changeParametersSettings()

Returns the object with the settings used for calls to changeParameters.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ChangeParametersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeParametersRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### changeRenewalSettingsOperationSettings()
    
    
    public OperationCallSettings<ChangeRenewalSettingsRequest,Entitlement,OperationMetadata> changeRenewalSettingsOperationSettings()

Returns the object with the settings used for calls to changeRenewalSettings.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### changeRenewalSettingsSettings()
    
    
    public UnaryCallSettings<ChangeRenewalSettingsRequest,Operation> changeRenewalSettingsSettings()

Returns the object with the settings used for calls to changeRenewalSettings.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ChangeRenewalSettingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChangeRenewalSettingsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### checkCloudIdentityAccountsExistSettings()
    
    
    public UnaryCallSettings<CheckCloudIdentityAccountsExistRequest,CheckCloudIdentityAccountsExistResponse> checkCloudIdentityAccountsExistSettings()

Returns the object with the settings used for calls to checkCloudIdentityAccountsExist.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CheckCloudIdentityAccountsExistRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistRequest),[CheckCloudIdentityAccountsExistResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CheckCloudIdentityAccountsExistResponse)>` |   
  
### createChannelPartnerLinkSettings()
    
    
    public UnaryCallSettings<CreateChannelPartnerLinkRequest,ChannelPartnerLink> createChannelPartnerLinkSettings()

Returns the object with the settings used for calls to createChannelPartnerLink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### createChannelPartnerRepricingConfigSettings()
    
    
    public UnaryCallSettings<CreateChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> createChannelPartnerRepricingConfigSettings()

Returns the object with the settings used for calls to createChannelPartnerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### createCustomerRepricingConfigSettings()
    
    
    public UnaryCallSettings<CreateCustomerRepricingConfigRequest,CustomerRepricingConfig> createCustomerRepricingConfigSettings()

Returns the object with the settings used for calls to createCustomerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### createCustomerSettings()
    
    
    public UnaryCallSettings<CreateCustomerRequest,Customer> createCustomerSettings()

Returns the object with the settings used for calls to createCustomer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### createEntitlementOperationSettings()
    
    
    public OperationCallSettings<CreateEntitlementRequest,Entitlement,OperationMetadata> createEntitlementOperationSettings()

Returns the object with the settings used for calls to createEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### createEntitlementSettings()
    
    
    public UnaryCallSettings<CreateEntitlementRequest,Operation> createEntitlementSettings()

Returns the object with the settings used for calls to createEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CreateEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteChannelPartnerRepricingConfigSettings()
    
    
    public UnaryCallSettings<DeleteChannelPartnerRepricingConfigRequest,Empty> deleteChannelPartnerRepricingConfigSettings()

Returns the object with the settings used for calls to deleteChannelPartnerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteChannelPartnerRepricingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteCustomerRepricingConfigSettings()
    
    
    public UnaryCallSettings<DeleteCustomerRepricingConfigRequest,Empty> deleteCustomerRepricingConfigSettings()

Returns the object with the settings used for calls to deleteCustomerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRepricingConfigRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteCustomerSettings()
    
    
    public UnaryCallSettings<DeleteCustomerRequest,Empty> deleteCustomerSettings()

Returns the object with the settings used for calls to deleteCustomer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.DeleteCustomerRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getChannelPartnerLinkSettings()
    
    
    public UnaryCallSettings<GetChannelPartnerLinkRequest,ChannelPartnerLink> getChannelPartnerLinkSettings()

Returns the object with the settings used for calls to getChannelPartnerLink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### getChannelPartnerRepricingConfigSettings()
    
    
    public UnaryCallSettings<GetChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> getChannelPartnerRepricingConfigSettings()

Returns the object with the settings used for calls to getChannelPartnerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### getCustomerRepricingConfigSettings()
    
    
    public UnaryCallSettings<GetCustomerRepricingConfigRequest,CustomerRepricingConfig> getCustomerRepricingConfigSettings()

Returns the object with the settings used for calls to getCustomerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### getCustomerSettings()
    
    
    public UnaryCallSettings<GetCustomerRequest,Customer> getCustomerSettings()

Returns the object with the settings used for calls to getCustomer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### getEntitlementSettings()
    
    
    public UnaryCallSettings<GetEntitlementRequest,Entitlement> getEntitlementSettings()

Returns the object with the settings used for calls to getEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.GetEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement)>` |   
  
### importCustomerSettings()
    
    
    public UnaryCallSettings<ImportCustomerRequest,Customer> importCustomerSettings()

Returns the object with the settings used for calls to importCustomer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ImportCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ImportCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
### listChannelPartnerLinksSettings()
    
    
    public PagedCallSettings<ListChannelPartnerLinksRequest,ListChannelPartnerLinksResponse,CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse> listChannelPartnerLinksSettings()

Returns the object with the settings used for calls to listChannelPartnerLinks.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListChannelPartnerLinksRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksRequest),[ListChannelPartnerLinksResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerLinksResponse),[ListChannelPartnerLinksPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerLinksPagedResponse)>` |   
  
### listChannelPartnerRepricingConfigsSettings()
    
    
    public PagedCallSettings<ListChannelPartnerRepricingConfigsRequest,ListChannelPartnerRepricingConfigsResponse,CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse> listChannelPartnerRepricingConfigsSettings()

Returns the object with the settings used for calls to listChannelPartnerRepricingConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListChannelPartnerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsRequest),[ListChannelPartnerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListChannelPartnerRepricingConfigsResponse),[ListChannelPartnerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListChannelPartnerRepricingConfigsPagedResponse)>` |   
  
### listCustomerRepricingConfigsSettings()
    
    
    public PagedCallSettings<ListCustomerRepricingConfigsRequest,ListCustomerRepricingConfigsResponse,CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse> listCustomerRepricingConfigsSettings()

Returns the object with the settings used for calls to listCustomerRepricingConfigs.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCustomerRepricingConfigsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsRequest),[ListCustomerRepricingConfigsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomerRepricingConfigsResponse),[ListCustomerRepricingConfigsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomerRepricingConfigsPagedResponse)>` |   
  
### listCustomersSettings()
    
    
    public PagedCallSettings<ListCustomersRequest,ListCustomersResponse,CloudChannelServiceClient.ListCustomersPagedResponse> listCustomersSettings()

Returns the object with the settings used for calls to listCustomers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCustomersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersRequest),[ListCustomersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListCustomersResponse),[ListCustomersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListCustomersPagedResponse)>` |   
  
### listEntitlementChangesSettings()
    
    
    public PagedCallSettings<ListEntitlementChangesRequest,ListEntitlementChangesResponse,CloudChannelServiceClient.ListEntitlementChangesPagedResponse> listEntitlementChangesSettings()

Returns the object with the settings used for calls to listEntitlementChanges.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEntitlementChangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesRequest),[ListEntitlementChangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementChangesResponse),[ListEntitlementChangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementChangesPagedResponse)>` |   
  
### listEntitlementsSettings()
    
    
    public PagedCallSettings<ListEntitlementsRequest,ListEntitlementsResponse,CloudChannelServiceClient.ListEntitlementsPagedResponse> listEntitlementsSettings()

Returns the object with the settings used for calls to listEntitlements.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsRequest),[ListEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListEntitlementsResponse),[ListEntitlementsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListEntitlementsPagedResponse)>` |   
  
### listOffersSettings()
    
    
    public PagedCallSettings<ListOffersRequest,ListOffersResponse,CloudChannelServiceClient.ListOffersPagedResponse> listOffersSettings()

Returns the object with the settings used for calls to listOffers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersRequest),[ListOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListOffersResponse),[ListOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListOffersPagedResponse)>` |   
  
### listProductsSettings()
    
    
    public PagedCallSettings<ListProductsRequest,ListProductsResponse,CloudChannelServiceClient.ListProductsPagedResponse> listProductsSettings()

Returns the object with the settings used for calls to listProducts.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsRequest),[ListProductsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListProductsResponse),[ListProductsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListProductsPagedResponse)>` |   
  
### listPurchasableOffersSettings()
    
    
    public PagedCallSettings<ListPurchasableOffersRequest,ListPurchasableOffersResponse,CloudChannelServiceClient.ListPurchasableOffersPagedResponse> listPurchasableOffersSettings()

Returns the object with the settings used for calls to listPurchasableOffers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPurchasableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersRequest),[ListPurchasableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableOffersResponse),[ListPurchasableOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListPurchasableOffersPagedResponse)>` |   
  
### listPurchasableSkusSettings()
    
    
    public PagedCallSettings<ListPurchasableSkusRequest,ListPurchasableSkusResponse,CloudChannelServiceClient.ListPurchasableSkusPagedResponse> listPurchasableSkusSettings()

Returns the object with the settings used for calls to listPurchasableSkus.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPurchasableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusRequest),[ListPurchasableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListPurchasableSkusResponse),[ListPurchasableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListPurchasableSkusPagedResponse)>` |   
  
### listSkuGroupBillableSkusSettings()
    
    
    public PagedCallSettings<ListSkuGroupBillableSkusRequest,ListSkuGroupBillableSkusResponse,CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse> listSkuGroupBillableSkusSettings()

Returns the object with the settings used for calls to listSkuGroupBillableSkus.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSkuGroupBillableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusRequest),[ListSkuGroupBillableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupBillableSkusResponse),[ListSkuGroupBillableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupBillableSkusPagedResponse)>` |   
  
### listSkuGroupsSettings()
    
    
    public PagedCallSettings<ListSkuGroupsRequest,ListSkuGroupsResponse,CloudChannelServiceClient.ListSkuGroupsPagedResponse> listSkuGroupsSettings()

Returns the object with the settings used for calls to listSkuGroups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSkuGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsRequest),[ListSkuGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkuGroupsResponse),[ListSkuGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkuGroupsPagedResponse)>` |   
  
### listSkusSettings()
    
    
    public PagedCallSettings<ListSkusRequest,ListSkusResponse,CloudChannelServiceClient.ListSkusPagedResponse> listSkusSettings()

Returns the object with the settings used for calls to listSkus.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusRequest),[ListSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSkusResponse),[ListSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSkusPagedResponse)>` |   
  
### listSubscribersSettings()
    
    
    public PagedCallSettings<ListSubscribersRequest,ListSubscribersResponse,CloudChannelServiceClient.ListSubscribersPagedResponse> listSubscribersSettings()

Returns the object with the settings used for calls to listSubscribers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSubscribersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersRequest),[ListSubscribersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListSubscribersResponse),[ListSubscribersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListSubscribersPagedResponse)>` |   
  
### listTransferableOffersSettings()
    
    
    public PagedCallSettings<ListTransferableOffersRequest,ListTransferableOffersResponse,CloudChannelServiceClient.ListTransferableOffersPagedResponse> listTransferableOffersSettings()

Returns the object with the settings used for calls to listTransferableOffers.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTransferableOffersRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersRequest),[ListTransferableOffersResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableOffersResponse),[ListTransferableOffersPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListTransferableOffersPagedResponse)>` |   
  
### listTransferableSkusSettings()
    
    
    public PagedCallSettings<ListTransferableSkusRequest,ListTransferableSkusResponse,CloudChannelServiceClient.ListTransferableSkusPagedResponse> listTransferableSkusSettings()

Returns the object with the settings used for calls to listTransferableSkus.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListTransferableSkusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusRequest),[ListTransferableSkusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListTransferableSkusResponse),[ListTransferableSkusPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceClient.ListTransferableSkusPagedResponse)>` |   
  
### lookupOfferSettings()
    
    
    public UnaryCallSettings<LookupOfferRequest,Offer> lookupOfferSettings()

Returns the object with the settings used for calls to lookupOffer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[LookupOfferRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.LookupOfferRequest),[Offer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Offer)>` |   
  
### provisionCloudIdentityOperationSettings()
    
    
    public OperationCallSettings<ProvisionCloudIdentityRequest,Customer,OperationMetadata> provisionCloudIdentityOperationSettings()

Returns the object with the settings used for calls to provisionCloudIdentity.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### provisionCloudIdentitySettings()
    
    
    public UnaryCallSettings<ProvisionCloudIdentityRequest,Operation> provisionCloudIdentitySettings()

Returns the object with the settings used for calls to provisionCloudIdentity.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ProvisionCloudIdentityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ProvisionCloudIdentityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### queryEligibleBillingAccountsSettings()
    
    
    public UnaryCallSettings<QueryEligibleBillingAccountsRequest,QueryEligibleBillingAccountsResponse> queryEligibleBillingAccountsSettings()

Returns the object with the settings used for calls to queryEligibleBillingAccounts.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[QueryEligibleBillingAccountsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsRequest),[QueryEligibleBillingAccountsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.QueryEligibleBillingAccountsResponse)>` |   
  
### registerSubscriberSettings()
    
    
    public UnaryCallSettings<RegisterSubscriberRequest,RegisterSubscriberResponse> registerSubscriberSettings()

Returns the object with the settings used for calls to registerSubscriber.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RegisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberRequest),[RegisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RegisterSubscriberResponse)>` |   
  
### startPaidServiceOperationSettings()
    
    
    public OperationCallSettings<StartPaidServiceRequest,Entitlement,OperationMetadata> startPaidServiceOperationSettings()

Returns the object with the settings used for calls to startPaidService.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### startPaidServiceSettings()
    
    
    public UnaryCallSettings<StartPaidServiceRequest,Operation> startPaidServiceSettings()

Returns the object with the settings used for calls to startPaidService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartPaidServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.StartPaidServiceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### suspendEntitlementOperationSettings()
    
    
    public OperationCallSettings<SuspendEntitlementRequest,Entitlement,OperationMetadata> suspendEntitlementOperationSettings()

Returns the object with the settings used for calls to suspendEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest),[Entitlement](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Entitlement),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### suspendEntitlementSettings()
    
    
    public UnaryCallSettings<SuspendEntitlementRequest,Operation> suspendEntitlementSettings()

Returns the object with the settings used for calls to suspendEntitlement.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SuspendEntitlementRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.SuspendEntitlementRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### toBuilder()
    
    
    public CloudChannelServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### transferEntitlementsOperationSettings()
    
    
    public OperationCallSettings<TransferEntitlementsRequest,TransferEntitlementsResponse,OperationMetadata> transferEntitlementsOperationSettings()

Returns the object with the settings used for calls to transferEntitlements.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest),[TransferEntitlementsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### transferEntitlementsSettings()
    
    
    public UnaryCallSettings<TransferEntitlementsRequest,Operation> transferEntitlementsSettings()

Returns the object with the settings used for calls to transferEntitlements.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[TransferEntitlementsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### transferEntitlementsToGoogleOperationSettings()
    
    
    public OperationCallSettings<TransferEntitlementsToGoogleRequest,Empty,OperationMetadata> transferEntitlementsToGoogleOperationSettings()

Returns the object with the settings used for calls to transferEntitlementsToGoogle.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### transferEntitlementsToGoogleSettings()
    
    
    public UnaryCallSettings<TransferEntitlementsToGoogleRequest,Operation> transferEntitlementsToGoogleSettings()

Returns the object with the settings used for calls to transferEntitlementsToGoogle.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[TransferEntitlementsToGoogleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.TransferEntitlementsToGoogleRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### unregisterSubscriberSettings()
    
    
    public UnaryCallSettings<UnregisterSubscriberRequest,UnregisterSubscriberResponse> unregisterSubscriberSettings()

Returns the object with the settings used for calls to unregisterSubscriber.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UnregisterSubscriberRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberRequest),[UnregisterSubscriberResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UnregisterSubscriberResponse)>` |   
  
### updateChannelPartnerLinkSettings()
    
    
    public UnaryCallSettings<UpdateChannelPartnerLinkRequest,ChannelPartnerLink> updateChannelPartnerLinkSettings()

Returns the object with the settings used for calls to updateChannelPartnerLink.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateChannelPartnerLinkRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerLinkRequest),[ChannelPartnerLink](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerLink)>` |   
  
### updateChannelPartnerRepricingConfigSettings()
    
    
    public UnaryCallSettings<UpdateChannelPartnerRepricingConfigRequest,ChannelPartnerRepricingConfig> updateChannelPartnerRepricingConfigSettings()

Returns the object with the settings used for calls to updateChannelPartnerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateChannelPartnerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateChannelPartnerRepricingConfigRequest),[ChannelPartnerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ChannelPartnerRepricingConfig)>` |   
  
### updateCustomerRepricingConfigSettings()
    
    
    public UnaryCallSettings<UpdateCustomerRepricingConfigRequest,CustomerRepricingConfig> updateCustomerRepricingConfigSettings()

Returns the object with the settings used for calls to updateCustomerRepricingConfig.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCustomerRepricingConfigRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRepricingConfigRequest),[CustomerRepricingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CustomerRepricingConfig)>` |   
  
### updateCustomerSettings()
    
    
    public UnaryCallSettings<UpdateCustomerRequest,Customer> updateCustomerSettings()

Returns the object with the settings used for calls to updateCustomer.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCustomerRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.UpdateCustomerRequest),[Customer](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.Customer)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
