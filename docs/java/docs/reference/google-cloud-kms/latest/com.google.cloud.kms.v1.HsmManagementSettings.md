---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings
title: Class HsmManagementSettings (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:03.838674+00:00
---

# Class HsmManagementSettings (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class HsmManagementSettings (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.8  2.5.3  2.4.4  2.3.1 
    
    
    public class HsmManagementSettings extends ClientSettings<HsmManagementSettings>

Settings class to configure an instance of [HsmManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementClient).

The default instance has everything set to sensible defaults:

  * The default service address (cloudkms.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getSingleTenantHsmInstance:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HsmManagementSettings.Builder hsmManagementSettingsBuilder = HsmManagementSettings.newBuilder();
     hsmManagementSettingsBuilder
         .getSingleTenantHsmInstanceSettings()
         .setRetrySettings(
             hsmManagementSettingsBuilder
                 .getSingleTenantHsmInstanceSettings()
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
     HsmManagementSettings hsmManagementSettings = hsmManagementSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createSingleTenantHsmInstance:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     HsmManagementSettings.Builder hsmManagementSettingsBuilder = HsmManagementSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     hsmManagementSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > HsmManagementSettings

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

### create(HsmManagementStubSettings stub)
    
    
    public static final HsmManagementSettings create(HsmManagementStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[HsmManagementStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.stub.HsmManagementStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[HsmManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings)` |   
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
    
    
    public static HsmManagementSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[HsmManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static HsmManagementSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[HsmManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static HsmManagementSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[HsmManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings.Builder)` |   
  
## Constructors 

### HsmManagementSettings(HsmManagementSettings.Builder settingsBuilder)
    
    
    protected HsmManagementSettings(HsmManagementSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[HsmManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings.Builder)`  
  
  
## Methods 

### approveSingleTenantHsmInstanceProposalSettings()
    
    
    public UnaryCallSettings<ApproveSingleTenantHsmInstanceProposalRequest,ApproveSingleTenantHsmInstanceProposalResponse> approveSingleTenantHsmInstanceProposalSettings()

Returns the object with the settings used for calls to approveSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ApproveSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ApproveSingleTenantHsmInstanceProposalRequest),[ApproveSingleTenantHsmInstanceProposalResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ApproveSingleTenantHsmInstanceProposalResponse)>` |   
  
### createSingleTenantHsmInstanceOperationSettings()
    
    
    public OperationCallSettings<CreateSingleTenantHsmInstanceRequest,SingleTenantHsmInstance,CreateSingleTenantHsmInstanceMetadata> createSingleTenantHsmInstanceOperationSettings()

Returns the object with the settings used for calls to createSingleTenantHsmInstance.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceRequest),[SingleTenantHsmInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.SingleTenantHsmInstance),[CreateSingleTenantHsmInstanceMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceMetadata)>` |   
  
### createSingleTenantHsmInstanceProposalOperationSettings()
    
    
    public OperationCallSettings<CreateSingleTenantHsmInstanceProposalRequest,SingleTenantHsmInstanceProposal,CreateSingleTenantHsmInstanceProposalMetadata> createSingleTenantHsmInstanceProposalOperationSettings()

Returns the object with the settings used for calls to createSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceProposalRequest),[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.SingleTenantHsmInstanceProposal),[CreateSingleTenantHsmInstanceProposalMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceProposalMetadata)>` |   
  
### createSingleTenantHsmInstanceProposalSettings()
    
    
    public UnaryCallSettings<CreateSingleTenantHsmInstanceProposalRequest,Operation> createSingleTenantHsmInstanceProposalSettings()

Returns the object with the settings used for calls to createSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceProposalRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createSingleTenantHsmInstanceSettings()
    
    
    public UnaryCallSettings<CreateSingleTenantHsmInstanceRequest,Operation> createSingleTenantHsmInstanceSettings()

Returns the object with the settings used for calls to createSingleTenantHsmInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.CreateSingleTenantHsmInstanceRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteSingleTenantHsmInstanceProposalSettings()
    
    
    public UnaryCallSettings<DeleteSingleTenantHsmInstanceProposalRequest,Empty> deleteSingleTenantHsmInstanceProposalSettings()

Returns the object with the settings used for calls to deleteSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.DeleteSingleTenantHsmInstanceProposalRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### executeSingleTenantHsmInstanceProposalOperationSettings()
    
    
    public OperationCallSettings<ExecuteSingleTenantHsmInstanceProposalRequest,ExecuteSingleTenantHsmInstanceProposalResponse,ExecuteSingleTenantHsmInstanceProposalMetadata> executeSingleTenantHsmInstanceProposalOperationSettings()

Returns the object with the settings used for calls to executeSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ExecuteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExecuteSingleTenantHsmInstanceProposalRequest),[ExecuteSingleTenantHsmInstanceProposalResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExecuteSingleTenantHsmInstanceProposalResponse),[ExecuteSingleTenantHsmInstanceProposalMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExecuteSingleTenantHsmInstanceProposalMetadata)>` |   
  
### executeSingleTenantHsmInstanceProposalSettings()
    
    
    public UnaryCallSettings<ExecuteSingleTenantHsmInstanceProposalRequest,Operation> executeSingleTenantHsmInstanceProposalSettings()

Returns the object with the settings used for calls to executeSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ExecuteSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ExecuteSingleTenantHsmInstanceProposalRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
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
  
### getSingleTenantHsmInstanceProposalSettings()
    
    
    public UnaryCallSettings<GetSingleTenantHsmInstanceProposalRequest,SingleTenantHsmInstanceProposal> getSingleTenantHsmInstanceProposalSettings()

Returns the object with the settings used for calls to getSingleTenantHsmInstanceProposal.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSingleTenantHsmInstanceProposalRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetSingleTenantHsmInstanceProposalRequest),[SingleTenantHsmInstanceProposal](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.SingleTenantHsmInstanceProposal)>` |   
  
### getSingleTenantHsmInstanceSettings()
    
    
    public UnaryCallSettings<GetSingleTenantHsmInstanceRequest,SingleTenantHsmInstance> getSingleTenantHsmInstanceSettings()

Returns the object with the settings used for calls to getSingleTenantHsmInstance.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSingleTenantHsmInstanceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.GetSingleTenantHsmInstanceRequest),[SingleTenantHsmInstance](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.SingleTenantHsmInstance)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,HsmManagementClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementClient.ListLocationsPagedResponse)>` |   
  
### listSingleTenantHsmInstanceProposalsSettings()
    
    
    public PagedCallSettings<ListSingleTenantHsmInstanceProposalsRequest,ListSingleTenantHsmInstanceProposalsResponse,HsmManagementClient.ListSingleTenantHsmInstanceProposalsPagedResponse> listSingleTenantHsmInstanceProposalsSettings()

Returns the object with the settings used for calls to listSingleTenantHsmInstanceProposals.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSingleTenantHsmInstanceProposalsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsRequest),[ListSingleTenantHsmInstanceProposalsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstanceProposalsResponse),[ListSingleTenantHsmInstanceProposalsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementClient.ListSingleTenantHsmInstanceProposalsPagedResponse)>` |   
  
### listSingleTenantHsmInstancesSettings()
    
    
    public PagedCallSettings<ListSingleTenantHsmInstancesRequest,ListSingleTenantHsmInstancesResponse,HsmManagementClient.ListSingleTenantHsmInstancesPagedResponse> listSingleTenantHsmInstancesSettings()

Returns the object with the settings used for calls to listSingleTenantHsmInstances.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSingleTenantHsmInstancesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstancesRequest),[ListSingleTenantHsmInstancesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.ListSingleTenantHsmInstancesResponse),[ListSingleTenantHsmInstancesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementClient.ListSingleTenantHsmInstancesPagedResponse)>` |   
  
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
    
    
    public HsmManagementSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[HsmManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-kms/latest/com.google.cloud.kms.v1.HsmManagementSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
