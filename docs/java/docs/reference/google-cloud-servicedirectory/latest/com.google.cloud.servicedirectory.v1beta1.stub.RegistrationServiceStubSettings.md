---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings
title: Class RegistrationServiceStubSettings (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:26.239709+00:00
---

# Class RegistrationServiceStubSettings (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class RegistrationServiceStubSettings (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.5  2.2.7 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 
    
    
    public class RegistrationServiceStubSettings extends StubSettings<RegistrationServiceStubSettings>

Settings class to configure an instance of [RegistrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (servicedirectory.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createNamespace:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     RegistrationServiceStubSettings.Builder registrationServiceSettingsBuilder =
         RegistrationServiceStubSettings.newBuilder();
     registrationServiceSettingsBuilder
         .createNamespaceSettings()
         .setRetrySettings(
             registrationServiceSettingsBuilder
                 .createNamespaceSettings()
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
     RegistrationServiceStubSettings registrationServiceSettings =
         registrationServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > RegistrationServiceStubSettings

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
    
    
    public static RegistrationServiceStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static RegistrationServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static RegistrationServiceStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings.Builder)` |   
  
## Constructors 

### RegistrationServiceStubSettings(RegistrationServiceStubSettings.Builder settingsBuilder)
    
    
    protected RegistrationServiceStubSettings(RegistrationServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[RegistrationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings.Builder)`  
  
  
## Methods 

### createEndpointSettings()
    
    
    public UnaryCallSettings<CreateEndpointRequest,Endpoint> createEndpointSettings()

Returns the object with the settings used for calls to createEndpoint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.CreateEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Endpoint)>` |   
  
### createNamespaceSettings()
    
    
    public UnaryCallSettings<CreateNamespaceRequest,Namespace> createNamespaceSettings()

Returns the object with the settings used for calls to createNamespace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.CreateNamespaceRequest),[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Namespace)>` |   
  
### createServiceSettings()
    
    
    public UnaryCallSettings<CreateServiceRequest,Service> createServiceSettings()

Returns the object with the settings used for calls to createService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.CreateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Service)>` |   
  
### createStub()
    
    
    public RegistrationServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteEndpointSettings()
    
    
    public UnaryCallSettings<DeleteEndpointRequest,Empty> deleteEndpointSettings()

Returns the object with the settings used for calls to deleteEndpoint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.DeleteEndpointRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteNamespaceSettings()
    
    
    public UnaryCallSettings<DeleteNamespaceRequest,Empty> deleteNamespaceSettings()

Returns the object with the settings used for calls to deleteNamespace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.DeleteNamespaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteServiceSettings()
    
    
    public UnaryCallSettings<DeleteServiceRequest,Empty> deleteServiceSettings()

Returns the object with the settings used for calls to deleteService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.DeleteServiceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getEndpointSettings()
    
    
    public UnaryCallSettings<GetEndpointRequest,Endpoint> getEndpointSettings()

Returns the object with the settings used for calls to getEndpoint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.GetEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Endpoint)>` |   
  
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

### getLocationSettings()
    
    
    public UnaryCallSettings<GetLocationRequest,Location> getLocationSettings()

Returns the object with the settings used for calls to getLocation.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.cloud.location.GetLocationRequest,com.google.cloud.location.Location>` |   
  
### getNamespaceSettings()
    
    
    public UnaryCallSettings<GetNamespaceRequest,Namespace> getNamespaceSettings()

Returns the object with the settings used for calls to getNamespace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.GetNamespaceRequest),[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Namespace)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getServiceSettings()
    
    
    public UnaryCallSettings<GetServiceRequest,Service> getServiceSettings()

Returns the object with the settings used for calls to getService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.GetServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Service)>` |   
  
### listEndpointsSettings()
    
    
    public PagedCallSettings<ListEndpointsRequest,ListEndpointsResponse,RegistrationServiceClient.ListEndpointsPagedResponse> listEndpointsSettings()

Returns the object with the settings used for calls to listEndpoints.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListEndpointsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.ListEndpointsRequest),[ListEndpointsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.ListEndpointsResponse),[ListEndpointsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.RegistrationServiceClient.ListEndpointsPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,RegistrationServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.RegistrationServiceClient.ListLocationsPagedResponse)>` |   
  
### listNamespacesSettings()
    
    
    public PagedCallSettings<ListNamespacesRequest,ListNamespacesResponse,RegistrationServiceClient.ListNamespacesPagedResponse> listNamespacesSettings()

Returns the object with the settings used for calls to listNamespaces.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListNamespacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.ListNamespacesRequest),[ListNamespacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.ListNamespacesResponse),[ListNamespacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.RegistrationServiceClient.ListNamespacesPagedResponse)>` |   
  
### listServicesSettings()
    
    
    public PagedCallSettings<ListServicesRequest,ListServicesResponse,RegistrationServiceClient.ListServicesPagedResponse> listServicesSettings()

Returns the object with the settings used for calls to listServices.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListServicesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.ListServicesRequest),[ListServicesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.ListServicesResponse),[ListServicesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.RegistrationServiceClient.ListServicesPagedResponse)>` |   
  
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
    
    
    public RegistrationServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[RegistrationServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.stub.RegistrationServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateEndpointSettings()
    
    
    public UnaryCallSettings<UpdateEndpointRequest,Endpoint> updateEndpointSettings()

Returns the object with the settings used for calls to updateEndpoint.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateEndpointRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.UpdateEndpointRequest),[Endpoint](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Endpoint)>` |   
  
### updateNamespaceSettings()
    
    
    public UnaryCallSettings<UpdateNamespaceRequest,Namespace> updateNamespaceSettings()

Returns the object with the settings used for calls to updateNamespace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateNamespaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.UpdateNamespaceRequest),[Namespace](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Namespace)>` |   
  
### updateServiceSettings()
    
    
    public UnaryCallSettings<UpdateServiceRequest,Service> updateServiceSettings()

Returns the object with the settings used for calls to updateService.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateServiceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.UpdateServiceRequest),[Service](https://docs.cloud.google.com/java/docs/reference/google-cloud-servicedirectory/latest/com.google.cloud.servicedirectory.v1beta1.Service)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
