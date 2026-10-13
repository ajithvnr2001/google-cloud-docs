---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings
title: Class SecurityCenterManagementSettings (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:06.098433+00:00
---

# Class SecurityCenterManagementSettings (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SecurityCenterManagementSettings (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class SecurityCenterManagementSettings extends ClientSettings<SecurityCenterManagementSettings>

Settings class to configure an instance of [SecurityCenterManagementClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient).

The default instance has everything set to sensible defaults:

  * The default service address (securitycentermanagement.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getEffectiveSecurityHealthAnalyticsCustomModule:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     SecurityCenterManagementSettings.Builder securityCenterManagementSettingsBuilder =
         SecurityCenterManagementSettings.newBuilder();
     securityCenterManagementSettingsBuilder
         .getEffectiveSecurityHealthAnalyticsCustomModuleSettings()
         .setRetrySettings(
             securityCenterManagementSettingsBuilder
                 .getEffectiveSecurityHealthAnalyticsCustomModuleSettings()
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
     SecurityCenterManagementSettings securityCenterManagementSettings =
         securityCenterManagementSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > SecurityCenterManagementSettings

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

### create(SecurityCenterManagementStubSettings stub)
    
    
    public static final SecurityCenterManagementSettings create(SecurityCenterManagementStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[SecurityCenterManagementStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.stub.SecurityCenterManagementStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings)` |   
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
    
    
    public static SecurityCenterManagementSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static SecurityCenterManagementSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static SecurityCenterManagementSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings.Builder)` |   
  
## Constructors 

### SecurityCenterManagementSettings(SecurityCenterManagementSettings.Builder settingsBuilder)
    
    
    protected SecurityCenterManagementSettings(SecurityCenterManagementSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[SecurityCenterManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings.Builder)`  
  
  
## Methods 

### createEventThreatDetectionCustomModuleSettings()
    
    
    public UnaryCallSettings<CreateEventThreatDetectionCustomModuleRequest,EventThreatDetectionCustomModule> createEventThreatDetectionCustomModuleSettings()

Returns the object with the settings used for calls to createEventThreatDetectionCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateEventThreatDetectionCustomModuleRequest),[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)>` |   
  
### createSecurityHealthAnalyticsCustomModuleSettings()
    
    
    public UnaryCallSettings<CreateSecurityHealthAnalyticsCustomModuleRequest,SecurityHealthAnalyticsCustomModule> createSecurityHealthAnalyticsCustomModuleSettings()

Returns the object with the settings used for calls to createSecurityHealthAnalyticsCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CreateSecurityHealthAnalyticsCustomModuleRequest),[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)>` |   
  
### deleteEventThreatDetectionCustomModuleSettings()
    
    
    public UnaryCallSettings<DeleteEventThreatDetectionCustomModuleRequest,Empty> deleteEventThreatDetectionCustomModuleSettings()

Returns the object with the settings used for calls to deleteEventThreatDetectionCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteEventThreatDetectionCustomModuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSecurityHealthAnalyticsCustomModuleSettings()
    
    
    public UnaryCallSettings<DeleteSecurityHealthAnalyticsCustomModuleRequest,Empty> deleteSecurityHealthAnalyticsCustomModuleSettings()

Returns the object with the settings used for calls to deleteSecurityHealthAnalyticsCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.DeleteSecurityHealthAnalyticsCustomModuleRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getEffectiveEventThreatDetectionCustomModuleSettings()
    
    
    public UnaryCallSettings<GetEffectiveEventThreatDetectionCustomModuleRequest,EffectiveEventThreatDetectionCustomModule> getEffectiveEventThreatDetectionCustomModuleSettings()

Returns the object with the settings used for calls to getEffectiveEventThreatDetectionCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEffectiveEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEffectiveEventThreatDetectionCustomModuleRequest),[EffectiveEventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveEventThreatDetectionCustomModule)>` |   
  
### getEffectiveSecurityHealthAnalyticsCustomModuleSettings()
    
    
    public UnaryCallSettings<GetEffectiveSecurityHealthAnalyticsCustomModuleRequest,EffectiveSecurityHealthAnalyticsCustomModule> getEffectiveSecurityHealthAnalyticsCustomModuleSettings()

Returns the object with the settings used for calls to getEffectiveSecurityHealthAnalyticsCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEffectiveSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEffectiveSecurityHealthAnalyticsCustomModuleRequest),[EffectiveSecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EffectiveSecurityHealthAnalyticsCustomModule)>` |   
  
### getEventThreatDetectionCustomModuleSettings()
    
    
    public UnaryCallSettings<GetEventThreatDetectionCustomModuleRequest,EventThreatDetectionCustomModule> getEventThreatDetectionCustomModuleSettings()

Returns the object with the settings used for calls to getEventThreatDetectionCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetEventThreatDetectionCustomModuleRequest),[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)>` |   
  
### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getSecurityCenterServiceSettings()
    
    
    public UnaryCallSettings<GetSecurityCenterServiceRequest,SecurityCenterService> getSecurityCenterServiceSettings()

Returns the object with the settings used for calls to getSecurityCenterService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSecurityCenterServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetSecurityCenterServiceRequest),[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)>` |   
  
### getSecurityHealthAnalyticsCustomModuleSettings()
    
    
    public UnaryCallSettings<GetSecurityHealthAnalyticsCustomModuleRequest,SecurityHealthAnalyticsCustomModule> getSecurityHealthAnalyticsCustomModuleSettings()

Returns the object with the settings used for calls to getSecurityHealthAnalyticsCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.GetSecurityHealthAnalyticsCustomModuleRequest),[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)>` |   
  
### listDescendantEventThreatDetectionCustomModulesSettings()
    
    
    public PagedCallSettings<ListDescendantEventThreatDetectionCustomModulesRequest,ListDescendantEventThreatDetectionCustomModulesResponse,SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse> listDescendantEventThreatDetectionCustomModulesSettings()

Returns the object with the settings used for calls to listDescendantEventThreatDetectionCustomModules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDescendantEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantEventThreatDetectionCustomModulesRequest),[ListDescendantEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantEventThreatDetectionCustomModulesResponse),[ListDescendantEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantEventThreatDetectionCustomModulesPagedResponse)>` |   
  
### listDescendantSecurityHealthAnalyticsCustomModulesSettings()
    
    
    public PagedCallSettings<ListDescendantSecurityHealthAnalyticsCustomModulesRequest,ListDescendantSecurityHealthAnalyticsCustomModulesResponse,SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse> listDescendantSecurityHealthAnalyticsCustomModulesSettings()

Returns the object with the settings used for calls to listDescendantSecurityHealthAnalyticsCustomModules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDescendantSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantSecurityHealthAnalyticsCustomModulesRequest),[ListDescendantSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListDescendantSecurityHealthAnalyticsCustomModulesResponse),[ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListDescendantSecurityHealthAnalyticsCustomModulesPagedResponse)>` |   
  
### listEffectiveEventThreatDetectionCustomModulesSettings()
    
    
    public PagedCallSettings<ListEffectiveEventThreatDetectionCustomModulesRequest,ListEffectiveEventThreatDetectionCustomModulesResponse,SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse> listEffectiveEventThreatDetectionCustomModulesSettings()

Returns the object with the settings used for calls to listEffectiveEventThreatDetectionCustomModules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEffectiveEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveEventThreatDetectionCustomModulesRequest),[ListEffectiveEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveEventThreatDetectionCustomModulesResponse),[ListEffectiveEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveEventThreatDetectionCustomModulesPagedResponse)>` |   
  
### listEffectiveSecurityHealthAnalyticsCustomModulesSettings()
    
    
    public PagedCallSettings<ListEffectiveSecurityHealthAnalyticsCustomModulesRequest,ListEffectiveSecurityHealthAnalyticsCustomModulesResponse,SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse> listEffectiveSecurityHealthAnalyticsCustomModulesSettings()

Returns the object with the settings used for calls to listEffectiveSecurityHealthAnalyticsCustomModules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEffectiveSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveSecurityHealthAnalyticsCustomModulesRequest),[ListEffectiveSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEffectiveSecurityHealthAnalyticsCustomModulesResponse),[ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEffectiveSecurityHealthAnalyticsCustomModulesPagedResponse)>` |   
  
### listEventThreatDetectionCustomModulesSettings()
    
    
    public PagedCallSettings<ListEventThreatDetectionCustomModulesRequest,ListEventThreatDetectionCustomModulesResponse,SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse> listEventThreatDetectionCustomModulesSettings()

Returns the object with the settings used for calls to listEventThreatDetectionCustomModules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEventThreatDetectionCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesRequest),[ListEventThreatDetectionCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListEventThreatDetectionCustomModulesResponse),[ListEventThreatDetectionCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListEventThreatDetectionCustomModulesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,SecurityCenterManagementClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListLocationsPagedResponse)>` |   
  
### listSecurityCenterServicesSettings()
    
    
    public PagedCallSettings<ListSecurityCenterServicesRequest,ListSecurityCenterServicesResponse,SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse> listSecurityCenterServicesSettings()

Returns the object with the settings used for calls to listSecurityCenterServices.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSecurityCenterServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityCenterServicesRequest),[ListSecurityCenterServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityCenterServicesResponse),[ListSecurityCenterServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityCenterServicesPagedResponse)>` |   
  
### listSecurityHealthAnalyticsCustomModulesSettings()
    
    
    public PagedCallSettings<ListSecurityHealthAnalyticsCustomModulesRequest,ListSecurityHealthAnalyticsCustomModulesResponse,SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse> listSecurityHealthAnalyticsCustomModulesSettings()

Returns the object with the settings used for calls to listSecurityHealthAnalyticsCustomModules.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSecurityHealthAnalyticsCustomModulesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesRequest),[ListSecurityHealthAnalyticsCustomModulesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ListSecurityHealthAnalyticsCustomModulesResponse),[ListSecurityHealthAnalyticsCustomModulesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementClient.ListSecurityHealthAnalyticsCustomModulesPagedResponse)>` |   
  
### simulateSecurityHealthAnalyticsCustomModuleSettings()
    
    
    public UnaryCallSettings<SimulateSecurityHealthAnalyticsCustomModuleRequest,SimulateSecurityHealthAnalyticsCustomModuleResponse> simulateSecurityHealthAnalyticsCustomModuleSettings()

Returns the object with the settings used for calls to simulateSecurityHealthAnalyticsCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SimulateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleRequest),[SimulateSecurityHealthAnalyticsCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SimulateSecurityHealthAnalyticsCustomModuleResponse)>` |   
  
### toBuilder()
    
    
    public SecurityCenterManagementSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[SecurityCenterManagementSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterManagementSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateEventThreatDetectionCustomModuleSettings()
    
    
    public UnaryCallSettings<UpdateEventThreatDetectionCustomModuleRequest,EventThreatDetectionCustomModule> updateEventThreatDetectionCustomModuleSettings()

Returns the object with the settings used for calls to updateEventThreatDetectionCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateEventThreatDetectionCustomModuleRequest),[EventThreatDetectionCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.EventThreatDetectionCustomModule)>` |   
  
### updateSecurityCenterServiceSettings()
    
    
    public UnaryCallSettings<UpdateSecurityCenterServiceRequest,SecurityCenterService> updateSecurityCenterServiceSettings()

Returns the object with the settings used for calls to updateSecurityCenterService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSecurityCenterServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateSecurityCenterServiceRequest),[SecurityCenterService](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityCenterService)>` |   
  
### updateSecurityHealthAnalyticsCustomModuleSettings()
    
    
    public UnaryCallSettings<UpdateSecurityHealthAnalyticsCustomModuleRequest,SecurityHealthAnalyticsCustomModule> updateSecurityHealthAnalyticsCustomModuleSettings()

Returns the object with the settings used for calls to updateSecurityHealthAnalyticsCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSecurityHealthAnalyticsCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.UpdateSecurityHealthAnalyticsCustomModuleRequest),[SecurityHealthAnalyticsCustomModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.SecurityHealthAnalyticsCustomModule)>` |   
  
### validateEventThreatDetectionCustomModuleSettings()
    
    
    public UnaryCallSettings<ValidateEventThreatDetectionCustomModuleRequest,ValidateEventThreatDetectionCustomModuleResponse> validateEventThreatDetectionCustomModuleSettings()

Returns the object with the settings used for calls to validateEventThreatDetectionCustomModule.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ValidateEventThreatDetectionCustomModuleRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ValidateEventThreatDetectionCustomModuleRequest),[ValidateEventThreatDetectionCustomModuleResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.ValidateEventThreatDetectionCustomModuleResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
