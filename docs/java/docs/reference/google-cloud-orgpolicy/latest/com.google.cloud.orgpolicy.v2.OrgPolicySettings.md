---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings
title: Class OrgPolicySettings (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:48.214699+00:00
---

# Class OrgPolicySettings (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrgPolicySettings (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.7-SNAPSHOT  2.2.1  2.1.2  2.0.10 
    
    
    public class OrgPolicySettings extends ClientSettings<OrgPolicySettings>

Settings class to configure an instance of [OrgPolicyClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyClient).

The default instance has everything set to sensible defaults:

  * The default service address (orgpolicy.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getPolicy:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrgPolicySettings.Builder orgPolicySettingsBuilder = OrgPolicySettings.newBuilder();
     orgPolicySettingsBuilder
         .getPolicySettings()
         .setRetrySettings(
             orgPolicySettingsBuilder
                 .getPolicySettings()
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
     OrgPolicySettings orgPolicySettings = orgPolicySettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > OrgPolicySettings

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

### create(OrgPolicyStubSettings stub)
    
    
    public static final OrgPolicySettings create(OrgPolicyStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrgPolicyStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.stub.OrgPolicyStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicySettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings)` |   
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
    
    
    public static OrgPolicySettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[OrgPolicySettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static OrgPolicySettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrgPolicySettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static OrgPolicySettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[OrgPolicySettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings.Builder)` |   
  
## Constructors 

### OrgPolicySettings(OrgPolicySettings.Builder settingsBuilder)
    
    
    protected OrgPolicySettings(OrgPolicySettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[OrgPolicySettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings.Builder)`  
  
  
## Methods 

### createCustomConstraintSettings()
    
    
    public UnaryCallSettings<CreateCustomConstraintRequest,CustomConstraint> createCustomConstraintSettings()

Returns the object with the settings used for calls to createCustomConstraint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CreateCustomConstraintRequest),[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CustomConstraint)>` |   
  
### createPolicySettings()
    
    
    public UnaryCallSettings<CreatePolicyRequest,Policy> createPolicySettings()

Returns the object with the settings used for calls to createPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CreatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### deleteCustomConstraintSettings()
    
    
    public UnaryCallSettings<DeleteCustomConstraintRequest,Empty> deleteCustomConstraintSettings()

Returns the object with the settings used for calls to deleteCustomConstraint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.DeleteCustomConstraintRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deletePolicySettings()
    
    
    public UnaryCallSettings<DeletePolicyRequest,Empty> deletePolicySettings()

Returns the object with the settings used for calls to deletePolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeletePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.DeletePolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getCustomConstraintSettings()
    
    
    public UnaryCallSettings<GetCustomConstraintRequest,CustomConstraint> getCustomConstraintSettings()

Returns the object with the settings used for calls to getCustomConstraint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.GetCustomConstraintRequest),[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CustomConstraint)>` |   
  
### getEffectivePolicySettings()
    
    
    public UnaryCallSettings<GetEffectivePolicyRequest,Policy> getEffectivePolicySettings()

Returns the object with the settings used for calls to getEffectivePolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEffectivePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.GetEffectivePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### getPolicySettings()
    
    
    public UnaryCallSettings<GetPolicyRequest,Policy> getPolicySettings()

Returns the object with the settings used for calls to getPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.GetPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
### listConstraintsSettings()
    
    
    public PagedCallSettings<ListConstraintsRequest,ListConstraintsResponse,OrgPolicyClient.ListConstraintsPagedResponse> listConstraintsSettings()

Returns the object with the settings used for calls to listConstraints.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListConstraintsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListConstraintsRequest),[ListConstraintsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListConstraintsResponse),[ListConstraintsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyClient.ListConstraintsPagedResponse)>` |   
  
### listCustomConstraintsSettings()
    
    
    public PagedCallSettings<ListCustomConstraintsRequest,ListCustomConstraintsResponse,OrgPolicyClient.ListCustomConstraintsPagedResponse> listCustomConstraintsSettings()

Returns the object with the settings used for calls to listCustomConstraints.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCustomConstraintsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListCustomConstraintsRequest),[ListCustomConstraintsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListCustomConstraintsResponse),[ListCustomConstraintsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyClient.ListCustomConstraintsPagedResponse)>` |   
  
### listPoliciesSettings()
    
    
    public PagedCallSettings<ListPoliciesRequest,ListPoliciesResponse,OrgPolicyClient.ListPoliciesPagedResponse> listPoliciesSettings()

Returns the object with the settings used for calls to listPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListPoliciesRequest),[ListPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.ListPoliciesResponse),[ListPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicyClient.ListPoliciesPagedResponse)>` |   
  
### toBuilder()
    
    
    public OrgPolicySettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[OrgPolicySettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.OrgPolicySettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateCustomConstraintSettings()
    
    
    public UnaryCallSettings<UpdateCustomConstraintRequest,CustomConstraint> updateCustomConstraintSettings()

Returns the object with the settings used for calls to updateCustomConstraint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCustomConstraintRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.UpdateCustomConstraintRequest),[CustomConstraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.CustomConstraint)>` |   
  
### updatePolicySettings()
    
    
    public UnaryCallSettings<UpdatePolicyRequest,Policy> updatePolicySettings()

Returns the object with the settings used for calls to updatePolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.UpdatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-orgpolicy/latest/com.google.cloud.orgpolicy.v2.Policy)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
