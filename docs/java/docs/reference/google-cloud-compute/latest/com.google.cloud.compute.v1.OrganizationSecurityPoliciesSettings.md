---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings
title: Class OrganizationSecurityPoliciesSettings (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:27.577258+00:00
---

# Class OrganizationSecurityPoliciesSettings (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class OrganizationSecurityPoliciesSettings (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public class OrganizationSecurityPoliciesSettings extends ClientSettings<OrganizationSecurityPoliciesSettings>

Settings class to configure an instance of [OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient).

The default instance has everything set to sensible defaults:

  * The default service address (compute.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of get:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationSecurityPoliciesSettings.Builder organizationSecurityPoliciesSettingsBuilder =
         OrganizationSecurityPoliciesSettings.newBuilder();
     organizationSecurityPoliciesSettingsBuilder
         .getSettings()
         .setRetrySettings(
             organizationSecurityPoliciesSettingsBuilder
                 .getSettings()
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
     OrganizationSecurityPoliciesSettings organizationSecurityPoliciesSettings =
         organizationSecurityPoliciesSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for addAssociation:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     OrganizationSecurityPoliciesSettings.Builder organizationSecurityPoliciesSettingsBuilder =
         OrganizationSecurityPoliciesSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     organizationSecurityPoliciesSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > OrganizationSecurityPoliciesSettings

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

### create(OrganizationSecurityPoliciesStubSettings stub)
    
    
    public static final OrganizationSecurityPoliciesSettings create(OrganizationSecurityPoliciesStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[OrganizationSecurityPoliciesStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.stub.OrganizationSecurityPoliciesStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings)` |   
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
  
### defaultHttpJsonTransportProviderBuilder()
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

Returns a builder for the default ChannelProvider for this service.

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
    
    
    public static OrganizationSecurityPoliciesSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static OrganizationSecurityPoliciesSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings.Builder)` |   
  
## Constructors 

### OrganizationSecurityPoliciesSettings(OrganizationSecurityPoliciesSettings.Builder settingsBuilder)
    
    
    protected OrganizationSecurityPoliciesSettings(OrganizationSecurityPoliciesSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[OrganizationSecurityPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings.Builder)`  
  
  
## Methods 

### addAssociationOperationSettings()
    
    
    public OperationCallSettings<AddAssociationOrganizationSecurityPolicyRequest,Operation,Operation> addAssociationOperationSettings()

Returns the object with the settings used for calls to addAssociation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AddAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addAssociationSettings()
    
    
    public UnaryCallSettings<AddAssociationOrganizationSecurityPolicyRequest,Operation> addAssociationSettings()

Returns the object with the settings used for calls to addAssociation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AddAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleOperationSettings()
    
    
    public OperationCallSettings<AddRuleOrganizationSecurityPolicyRequest,Operation,Operation> addRuleOperationSettings()

Returns the object with the settings used for calls to addRule.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[AddRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### addRuleSettings()
    
    
    public UnaryCallSettings<AddRuleOrganizationSecurityPolicyRequest,Operation> addRuleSettings()

Returns the object with the settings used for calls to addRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AddRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.AddRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### copyRulesOperationSettings()
    
    
    public OperationCallSettings<CopyRulesOrganizationSecurityPolicyRequest,Operation,Operation> copyRulesOperationSettings()

Returns the object with the settings used for calls to copyRules.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CopyRulesOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CopyRulesOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### copyRulesSettings()
    
    
    public UnaryCallSettings<CopyRulesOrganizationSecurityPolicyRequest,Operation> copyRulesSettings()

Returns the object with the settings used for calls to copyRules.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CopyRulesOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.CopyRulesOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteOperationSettings()
    
    
    public OperationCallSettings<DeleteOrganizationSecurityPolicyRequest,Operation,Operation> deleteOperationSettings()

Returns the object with the settings used for calls to delete.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### deleteSettings()
    
    
    public UnaryCallSettings<DeleteOrganizationSecurityPolicyRequest,Operation> deleteSettings()

Returns the object with the settings used for calls to delete.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DeleteOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### getAssociationSettings()
    
    
    public UnaryCallSettings<GetAssociationOrganizationSecurityPolicyRequest,SecurityPolicyAssociation> getAssociationSettings()

Returns the object with the settings used for calls to getAssociation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetAssociationOrganizationSecurityPolicyRequest),[SecurityPolicyAssociation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyAssociation)>` |   
  
### getRuleSettings()
    
    
    public UnaryCallSettings<GetRuleOrganizationSecurityPolicyRequest,SecurityPolicyRule> getRuleSettings()

Returns the object with the settings used for calls to getRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetRuleOrganizationSecurityPolicyRequest),[SecurityPolicyRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyRule)>` |   
  
### getSettings()
    
    
    public UnaryCallSettings<GetOrganizationSecurityPolicyRequest,SecurityPolicy> getSettings()

Returns the object with the settings used for calls to get.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.GetOrganizationSecurityPolicyRequest),[SecurityPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicy)>` |   
  
### insertOperationSettings()
    
    
    public OperationCallSettings<InsertOrganizationSecurityPolicyRequest,Operation,Operation> insertOperationSettings()

Returns the object with the settings used for calls to insert.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[InsertOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### insertSettings()
    
    
    public UnaryCallSettings<InsertOrganizationSecurityPolicyRequest,Operation> insertSettings()

Returns the object with the settings used for calls to insert.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[InsertOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.InsertOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### listAssociationsSettings()
    
    
    public UnaryCallSettings<ListAssociationsOrganizationSecurityPolicyRequest,OrganizationSecurityPoliciesListAssociationsResponse> listAssociationsSettings()

Returns the object with the settings used for calls to listAssociations.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ListAssociationsOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListAssociationsOrganizationSecurityPolicyRequest),[OrganizationSecurityPoliciesListAssociationsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesListAssociationsResponse)>` |   
  
### listPreconfiguredExpressionSetsSettings()
    
    
    public UnaryCallSettings<ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest,SecurityPoliciesListPreconfiguredExpressionSetsResponse> listPreconfiguredExpressionSetsSettings()

Returns the object with the settings used for calls to listPreconfiguredExpressionSets.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListPreconfiguredExpressionSetsOrganizationSecurityPoliciesRequest),[SecurityPoliciesListPreconfiguredExpressionSetsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPoliciesListPreconfiguredExpressionSetsResponse)>` |   
  
### listSettings()
    
    
    public PagedCallSettings<ListOrganizationSecurityPoliciesRequest,SecurityPolicyList,OrganizationSecurityPoliciesClient.ListPagedResponse> listSettings()

Returns the object with the settings used for calls to list.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListOrganizationSecurityPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ListOrganizationSecurityPoliciesRequest),[SecurityPolicyList](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.SecurityPolicyList),[ListPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesClient.ListPagedResponse)>` |   
  
### moveOperationSettings()
    
    
    public OperationCallSettings<MoveOrganizationSecurityPolicyRequest,Operation,Operation> moveOperationSettings()

Returns the object with the settings used for calls to move.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[MoveOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### moveSettings()
    
    
    public UnaryCallSettings<MoveOrganizationSecurityPolicyRequest,Operation> moveSettings()

Returns the object with the settings used for calls to move.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.MoveOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchOperationSettings()
    
    
    public OperationCallSettings<PatchOrganizationSecurityPolicyRequest,Operation,Operation> patchOperationSettings()

Returns the object with the settings used for calls to patch.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[PatchOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleOperationSettings()
    
    
    public OperationCallSettings<PatchRuleOrganizationSecurityPolicyRequest,Operation,Operation> patchRuleOperationSettings()

Returns the object with the settings used for calls to patchRule.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[PatchRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchRuleSettings()
    
    
    public UnaryCallSettings<PatchRuleOrganizationSecurityPolicyRequest,Operation> patchRuleSettings()

Returns the object with the settings used for calls to patchRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PatchRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### patchSettings()
    
    
    public UnaryCallSettings<PatchOrganizationSecurityPolicyRequest,Operation> patchSettings()

Returns the object with the settings used for calls to patch.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PatchOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.PatchOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationOperationSettings()
    
    
    public OperationCallSettings<RemoveAssociationOrganizationSecurityPolicyRequest,Operation,Operation> removeAssociationOperationSettings()

Returns the object with the settings used for calls to removeAssociation.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RemoveAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeAssociationSettings()
    
    
    public UnaryCallSettings<RemoveAssociationOrganizationSecurityPolicyRequest,Operation> removeAssociationSettings()

Returns the object with the settings used for calls to removeAssociation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveAssociationOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveAssociationOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleOperationSettings()
    
    
    public OperationCallSettings<RemoveRuleOrganizationSecurityPolicyRequest,Operation,Operation> removeRuleOperationSettings()

Returns the object with the settings used for calls to removeRule.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RemoveRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### removeRuleSettings()
    
    
    public UnaryCallSettings<RemoveRuleOrganizationSecurityPolicyRequest,Operation> removeRuleSettings()

Returns the object with the settings used for calls to removeRule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveRuleOrganizationSecurityPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.RemoveRuleOrganizationSecurityPolicyRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Operation)>` |   
  
### toBuilder()
    
    
    public OrganizationSecurityPoliciesSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[OrganizationSecurityPoliciesSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.OrganizationSecurityPoliciesSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
