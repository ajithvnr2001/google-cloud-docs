---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStubSettings
title: Class RecaptchaEnterpriseServiceStubSettings (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:32.215887+00:00
---

# Class RecaptchaEnterpriseServiceStubSettings (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RecaptchaEnterpriseServiceStubSettings (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public class RecaptchaEnterpriseServiceStubSettings extends StubSettings<RecaptchaEnterpriseServiceStubSettings>

Settings class to configure an instance of [RecaptchaEnterpriseServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (recaptchaenterprise.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createAssessment:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RecaptchaEnterpriseServiceStubSettings.Builder recaptchaEnterpriseServiceSettingsBuilder =
         RecaptchaEnterpriseServiceStubSettings.newBuilder();
     recaptchaEnterpriseServiceSettingsBuilder
         .createAssessmentSettings()
         .setRetrySettings(
             recaptchaEnterpriseServiceSettingsBuilder
                 .createAssessmentSettings()
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
     RecaptchaEnterpriseServiceStubSettings recaptchaEnterpriseServiceSettings =
         recaptchaEnterpriseServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > RecaptchaEnterpriseServiceStubSettings

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
  
### defaultGrpcTransportProviderBuilder()
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
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
    
    
    public static RecaptchaEnterpriseServiceStubSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[RecaptchaEnterpriseServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static RecaptchaEnterpriseServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[RecaptchaEnterpriseServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStubSettings.Builder)` |   
  
## Constructors 

### RecaptchaEnterpriseServiceStubSettings(RecaptchaEnterpriseServiceStubSettings.Builder settingsBuilder)
    
    
    protected RecaptchaEnterpriseServiceStubSettings(RecaptchaEnterpriseServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[RecaptchaEnterpriseServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStubSettings.Builder)`  
  
  
## Methods 

### addIpOverrideSettings()
    
    
    public UnaryCallSettings<AddIpOverrideRequest,AddIpOverrideResponse> addIpOverrideSettings()

Returns the object with the settings used for calls to addIpOverride.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AddIpOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AddIpOverrideRequest),[AddIpOverrideResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AddIpOverrideResponse)>` |   
  
### annotateAssessmentSettings()
    
    
    public UnaryCallSettings<AnnotateAssessmentRequest,AnnotateAssessmentResponse> annotateAssessmentSettings()

Returns the object with the settings used for calls to annotateAssessment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[AnnotateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest),[AnnotateAssessmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentResponse)>` |   
  
### createAssessmentSettings()
    
    
    public UnaryCallSettings<CreateAssessmentRequest,Assessment> createAssessmentSettings()

Returns the object with the settings used for calls to createAssessment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateAssessmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateAssessmentRequest),[Assessment](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Assessment)>` |   
  
### createFirewallPolicySettings()
    
    
    public UnaryCallSettings<CreateFirewallPolicyRequest,FirewallPolicy> createFirewallPolicySettings()

Returns the object with the settings used for calls to createFirewallPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateFirewallPolicyRequest),[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallPolicy)>` |   
  
### createKeySettings()
    
    
    public UnaryCallSettings<CreateKeyRequest,Key> createKeySettings()

Returns the object with the settings used for calls to createKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.CreateKeyRequest),[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key)>` |   
  
### createStub()
    
    
    public RecaptchaEnterpriseServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[RecaptchaEnterpriseServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteFirewallPolicySettings()
    
    
    public UnaryCallSettings<DeleteFirewallPolicyRequest,Empty> deleteFirewallPolicySettings()

Returns the object with the settings used for calls to deleteFirewallPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.DeleteFirewallPolicyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteKeySettings()
    
    
    public UnaryCallSettings<DeleteKeyRequest,Empty> deleteKeySettings()

Returns the object with the settings used for calls to deleteKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.DeleteKeyRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getFirewallPolicySettings()
    
    
    public UnaryCallSettings<GetFirewallPolicyRequest,FirewallPolicy> getFirewallPolicySettings()

Returns the object with the settings used for calls to getFirewallPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetFirewallPolicyRequest),[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallPolicy)>` |   
  
### getKeySettings()
    
    
    public UnaryCallSettings<GetKeyRequest,Key> getKeySettings()

Returns the object with the settings used for calls to getKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetKeyRequest),[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getMetricsSettings()
    
    
    public UnaryCallSettings<GetMetricsRequest,Metrics> getMetricsSettings()

Returns the object with the settings used for calls to getMetrics.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetMetricsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetMetricsRequest),[Metrics](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Metrics)>` |   
  
### getPolicySettings()
    
    
    public UnaryCallSettings<GetPolicyRequest,Policy> getPolicySettings()

Returns the object with the settings used for calls to getPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.GetPolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Policy)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listFirewallPoliciesSettings()
    
    
    public PagedCallSettings<ListFirewallPoliciesRequest,ListFirewallPoliciesResponse,RecaptchaEnterpriseServiceClient.ListFirewallPoliciesPagedResponse> listFirewallPoliciesSettings()

Returns the object with the settings used for calls to listFirewallPolicies.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListFirewallPoliciesRequest),[ListFirewallPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListFirewallPoliciesResponse),[ListFirewallPoliciesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListFirewallPoliciesPagedResponse)>` |   
  
### listIpOverridesSettings()
    
    
    public PagedCallSettings<ListIpOverridesRequest,ListIpOverridesResponse,RecaptchaEnterpriseServiceClient.ListIpOverridesPagedResponse> listIpOverridesSettings()

Returns the object with the settings used for calls to listIpOverrides.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListIpOverridesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListIpOverridesRequest),[ListIpOverridesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListIpOverridesResponse),[ListIpOverridesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListIpOverridesPagedResponse)>` |   
  
### listKeysSettings()
    
    
    public PagedCallSettings<ListKeysRequest,ListKeysResponse,RecaptchaEnterpriseServiceClient.ListKeysPagedResponse> listKeysSettings()

Returns the object with the settings used for calls to listKeys.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListKeysRequest),[ListKeysResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListKeysResponse),[ListKeysPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListKeysPagedResponse)>` |   
  
### listRelatedAccountGroupMembershipsSettings()
    
    
    public PagedCallSettings<ListRelatedAccountGroupMembershipsRequest,ListRelatedAccountGroupMembershipsResponse,RecaptchaEnterpriseServiceClient.ListRelatedAccountGroupMembershipsPagedResponse> listRelatedAccountGroupMembershipsSettings()

Returns the object with the settings used for calls to listRelatedAccountGroupMemberships.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupMembershipsRequest),[ListRelatedAccountGroupMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupMembershipsResponse),[ListRelatedAccountGroupMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListRelatedAccountGroupMembershipsPagedResponse)>` |   
  
### listRelatedAccountGroupsSettings()
    
    
    public PagedCallSettings<ListRelatedAccountGroupsRequest,ListRelatedAccountGroupsResponse,RecaptchaEnterpriseServiceClient.ListRelatedAccountGroupsPagedResponse> listRelatedAccountGroupsSettings()

Returns the object with the settings used for calls to listRelatedAccountGroups.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListRelatedAccountGroupsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupsRequest),[ListRelatedAccountGroupsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ListRelatedAccountGroupsResponse),[ListRelatedAccountGroupsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.ListRelatedAccountGroupsPagedResponse)>` |   
  
### migrateKeySettings()
    
    
    public UnaryCallSettings<MigrateKeyRequest,Key> migrateKeySettings()

Returns the object with the settings used for calls to migrateKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MigrateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.MigrateKeyRequest),[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key)>` |   
  
### removeIpOverrideSettings()
    
    
    public UnaryCallSettings<RemoveIpOverrideRequest,RemoveIpOverrideResponse> removeIpOverrideSettings()

Returns the object with the settings used for calls to removeIpOverride.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RemoveIpOverrideRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RemoveIpOverrideRequest),[RemoveIpOverrideResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RemoveIpOverrideResponse)>` |   
  
### reorderFirewallPoliciesSettings()
    
    
    public UnaryCallSettings<ReorderFirewallPoliciesRequest,ReorderFirewallPoliciesResponse> reorderFirewallPoliciesSettings()

Returns the object with the settings used for calls to reorderFirewallPolicies.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ReorderFirewallPoliciesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ReorderFirewallPoliciesRequest),[ReorderFirewallPoliciesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.ReorderFirewallPoliciesResponse)>` |   
  
### retrieveLegacySecretKeySettings()
    
    
    public UnaryCallSettings<RetrieveLegacySecretKeyRequest,RetrieveLegacySecretKeyResponse> retrieveLegacySecretKeySettings()

Returns the object with the settings used for calls to retrieveLegacySecretKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RetrieveLegacySecretKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RetrieveLegacySecretKeyRequest),[RetrieveLegacySecretKeyResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.RetrieveLegacySecretKeyResponse)>` |   
  
### searchRelatedAccountGroupMembershipsSettings()
    
    
    public PagedCallSettings<SearchRelatedAccountGroupMembershipsRequest,SearchRelatedAccountGroupMembershipsResponse,RecaptchaEnterpriseServiceClient.SearchRelatedAccountGroupMembershipsPagedResponse> searchRelatedAccountGroupMembershipsSettings()

Returns the object with the settings used for calls to searchRelatedAccountGroupMemberships.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchRelatedAccountGroupMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.SearchRelatedAccountGroupMembershipsRequest),[SearchRelatedAccountGroupMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.SearchRelatedAccountGroupMembershipsResponse),[SearchRelatedAccountGroupMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.RecaptchaEnterpriseServiceClient.SearchRelatedAccountGroupMembershipsPagedResponse)>` |   
  
### toBuilder()
    
    
    public RecaptchaEnterpriseServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[RecaptchaEnterpriseServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.cloud.recaptchaenterprise.v1.stub.RecaptchaEnterpriseServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateFirewallPolicySettings()
    
    
    public UnaryCallSettings<UpdateFirewallPolicyRequest,FirewallPolicy> updateFirewallPolicySettings()

Returns the object with the settings used for calls to updateFirewallPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateFirewallPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UpdateFirewallPolicyRequest),[FirewallPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.FirewallPolicy)>` |   
  
### updateKeySettings()
    
    
    public UnaryCallSettings<UpdateKeyRequest,Key> updateKeySettings()

Returns the object with the settings used for calls to updateKey.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UpdateKeyRequest),[Key](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Key)>` |   
  
### updatePolicySettings()
    
    
    public UnaryCallSettings<UpdatePolicyRequest,Policy> updatePolicySettings()

Returns the object with the settings used for calls to updatePolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdatePolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.UpdatePolicyRequest),[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.Policy)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
