---
url: https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings
title: Class AccessPoliciesSettings (1.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:06.079937+00:00
---

# Class AccessPoliciesSettings (1.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AccessPoliciesSettings (1.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.96.0 (latest)  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.83.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.72.0  1.71.0  1.70.0  1.68.0  1.66.0  1.65.0  1.62.0  1.61.0  1.60.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.7.0 
    
    
    public class AccessPoliciesSettings extends ClientSettings<AccessPoliciesSettings>

Settings class to configure an instance of [AccessPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3beta.AccessPoliciesClient).

The default instance has everything set to sensible defaults:

  * The default service address (iam.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getAccessPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessPoliciesSettings.Builder accessPoliciesSettingsBuilder =
         AccessPoliciesSettings.newBuilder();
     accessPoliciesSettingsBuilder
         .getAccessPolicySettings()
         .setRetrySettings(
             accessPoliciesSettingsBuilder
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
     AccessPoliciesSettings accessPoliciesSettings = accessPoliciesSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for createAccessPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AccessPoliciesSettings.Builder accessPoliciesSettingsBuilder =
         AccessPoliciesSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     accessPoliciesSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > AccessPoliciesSettings

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

### create(AccessPoliciesStubSettings stub)
    
    
    public static final AccessPoliciesSettings create(AccessPoliciesStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AccessPoliciesStubSettings](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.stub.AccessPoliciesStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings)` |   
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
    
    
    public static AccessPoliciesSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AccessPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static AccessPoliciesSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static AccessPoliciesSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AccessPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings.Builder)` |   
  
## Constructors 

### AccessPoliciesSettings(AccessPoliciesSettings.Builder settingsBuilder)
    
    
    protected AccessPoliciesSettings(AccessPoliciesSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[AccessPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings.Builder)`  
  
  
## Methods 

### createAccessPolicyOperationSettings()
    
    
    public OperationCallSettings<CreateAccessPolicyRequest,AccessPolicy,OperationMetadata> createAccessPolicyOperationSettings()

Returns the object with the settings used for calls to createAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.CreateAccessPolicyRequest),[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.OperationMetadata)>` |   
  
### createAccessPolicySettings()
    
    
    public UnaryCallSettings<CreateAccessPolicyRequest,Operation> createAccessPolicySettings()

Returns the object with the settings used for calls to createAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.CreateAccessPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteAccessPolicyOperationSettings()
    
    
    public OperationCallSettings<DeleteAccessPolicyRequest,Empty,OperationMetadata> deleteAccessPolicyOperationSettings()

Returns the object with the settings used for calls to deleteAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.DeleteAccessPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.OperationMetadata)>` |   
  
### deleteAccessPolicySettings()
    
    
    public UnaryCallSettings<DeleteAccessPolicyRequest,Operation> deleteAccessPolicySettings()

Returns the object with the settings used for calls to deleteAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.DeleteAccessPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getAccessPolicySettings()
    
    
    public UnaryCallSettings<GetAccessPolicyRequest,AccessPolicy> getAccessPolicySettings()

Returns the object with the settings used for calls to getAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.GetAccessPolicyRequest),[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPolicy)>` |   
  
### listAccessPoliciesSettings()
    
    
    public PagedCallSettings<ListAccessPoliciesRequest,ListAccessPoliciesResponse,AccessPoliciesClient.ListAccessPoliciesPagedResponse> listAccessPoliciesSettings()

Returns the object with the settings used for calls to listAccessPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListAccessPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.ListAccessPoliciesRequest),[ListAccessPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.ListAccessPoliciesResponse),[ListAccessPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesClient.ListAccessPoliciesPagedResponse)>` |   
  
### searchAccessPolicyBindingsSettings()
    
    
    public PagedCallSettings<SearchAccessPolicyBindingsRequest,SearchAccessPolicyBindingsResponse,AccessPoliciesClient.SearchAccessPolicyBindingsPagedResponse> searchAccessPolicyBindingsSettings()

Returns the object with the settings used for calls to searchAccessPolicyBindings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.SearchAccessPolicyBindingsRequest),[SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.SearchAccessPolicyBindingsResponse),[SearchAccessPolicyBindingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesClient.SearchAccessPolicyBindingsPagedResponse)>` |   
  
### toBuilder()
    
    
    public AccessPoliciesSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[AccessPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPoliciesSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateAccessPolicyOperationSettings()
    
    
    public OperationCallSettings<UpdateAccessPolicyRequest,AccessPolicy,OperationMetadata> updateAccessPolicyOperationSettings()

Returns the object with the settings used for calls to updateAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.UpdateAccessPolicyRequest),[AccessPolicy](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.AccessPolicy),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.OperationMetadata)>` |   
  
### updateAccessPolicySettings()
    
    
    public UnaryCallSettings<UpdateAccessPolicyRequest,Operation> updateAccessPolicySettings()

Returns the object with the settings used for calls to updateAccessPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAccessPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-policy/latest/com.google.iam.v3.UpdateAccessPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
