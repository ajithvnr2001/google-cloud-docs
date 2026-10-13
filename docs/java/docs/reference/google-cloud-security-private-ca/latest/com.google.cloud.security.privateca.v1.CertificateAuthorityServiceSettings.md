---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings
title: Class CertificateAuthorityServiceSettings (2.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:44.685834+00:00
---

# Class CertificateAuthorityServiceSettings (2.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CertificateAuthorityServiceSettings (2.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.101.0 (latest)  2.97.0  2.96.0  2.95.0  2.93.0  2.90.0  2.89.0  2.87.0  2.85.0  2.84.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.74.0  2.72.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.4  2.4.0  2.3.0  2.2.5 
    
    
    public class CertificateAuthorityServiceSettings extends ClientSettings<CertificateAuthorityServiceSettings>

Settings class to configure an instance of [CertificateAuthorityServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1beta1.CertificateAuthorityServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (privateca.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createCertificate:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CertificateAuthorityServiceSettings.Builder certificateAuthorityServiceSettingsBuilder =
         CertificateAuthorityServiceSettings.newBuilder();
     certificateAuthorityServiceSettingsBuilder
         .createCertificateSettings()
         .setRetrySettings(
             certificateAuthorityServiceSettingsBuilder
                 .createCertificateSettings()
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
     CertificateAuthorityServiceSettings certificateAuthorityServiceSettings =
         certificateAuthorityServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for activateCertificateAuthority:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CertificateAuthorityServiceSettings.Builder certificateAuthorityServiceSettingsBuilder =
         CertificateAuthorityServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     certificateAuthorityServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > CertificateAuthorityServiceSettings

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

### create(CertificateAuthorityServiceStubSettings stub)
    
    
    public static final CertificateAuthorityServiceSettings create(CertificateAuthorityServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CertificateAuthorityServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.stub.CertificateAuthorityServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthorityServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings)` |   
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
    
    
    public static CertificateAuthorityServiceSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthorityServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static CertificateAuthorityServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthorityServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static CertificateAuthorityServiceSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthorityServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings.Builder)` |   
  
## Constructors 

### CertificateAuthorityServiceSettings(CertificateAuthorityServiceSettings.Builder settingsBuilder)
    
    
    protected CertificateAuthorityServiceSettings(CertificateAuthorityServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[CertificateAuthorityServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings.Builder)`  
  
  
## Methods 

### activateCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<ActivateCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> activateCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to activateCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ActivateCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### activateCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<ActivateCertificateAuthorityRequest,Operation> activateCertificateAuthoritySettings()

Returns the object with the settings used for calls to activateCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ActivateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ActivateCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCaPoolOperationSettings()
    
    
    public OperationCallSettings<CreateCaPoolRequest,CaPool,OperationMetadata> createCaPoolOperationSettings()

Returns the object with the settings used for calls to createCaPool.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCaPoolRequest),[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### createCaPoolSettings()
    
    
    public UnaryCallSettings<CreateCaPoolRequest,Operation> createCaPoolSettings()

Returns the object with the settings used for calls to createCaPool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCaPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<CreateCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> createCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to createCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### createCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<CreateCertificateAuthorityRequest,Operation> createCertificateAuthoritySettings()

Returns the object with the settings used for calls to createCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### createCertificateSettings()
    
    
    public UnaryCallSettings<CreateCertificateRequest,Certificate> createCertificateSettings()

Returns the object with the settings used for calls to createCertificate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateRequest),[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate)>` |   
  
### createCertificateTemplateOperationSettings()
    
    
    public OperationCallSettings<CreateCertificateTemplateRequest,CertificateTemplate,OperationMetadata> createCertificateTemplateOperationSettings()

Returns the object with the settings used for calls to createCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[CreateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateTemplateRequest),[CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### createCertificateTemplateSettings()
    
    
    public UnaryCallSettings<CreateCertificateTemplateRequest,Operation> createCertificateTemplateSettings()

Returns the object with the settings used for calls to createCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CreateCertificateTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCaPoolOperationSettings()
    
    
    public OperationCallSettings<DeleteCaPoolRequest,Empty,OperationMetadata> deleteCaPoolOperationSettings()

Returns the object with the settings used for calls to deleteCaPool.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCaPoolRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### deleteCaPoolSettings()
    
    
    public UnaryCallSettings<DeleteCaPoolRequest,Operation> deleteCaPoolSettings()

Returns the object with the settings used for calls to deleteCaPool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCaPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<DeleteCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> deleteCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to deleteCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### deleteCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<DeleteCertificateAuthorityRequest,Operation> deleteCertificateAuthoritySettings()

Returns the object with the settings used for calls to deleteCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### deleteCertificateTemplateOperationSettings()
    
    
    public OperationCallSettings<DeleteCertificateTemplateRequest,Empty,OperationMetadata> deleteCertificateTemplateOperationSettings()

Returns the object with the settings used for calls to deleteCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### deleteCertificateTemplateSettings()
    
    
    public UnaryCallSettings<DeleteCertificateTemplateRequest,Operation> deleteCertificateTemplateSettings()

Returns the object with the settings used for calls to deleteCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DeleteCertificateTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### disableCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<DisableCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> disableCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to disableCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DisableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DisableCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### disableCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<DisableCertificateAuthorityRequest,Operation> disableCertificateAuthoritySettings()

Returns the object with the settings used for calls to disableCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DisableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.DisableCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### enableCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<EnableCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> enableCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to enableCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### enableCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<EnableCertificateAuthorityRequest,Operation> enableCertificateAuthoritySettings()

Returns the object with the settings used for calls to enableCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[EnableCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.EnableCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### fetchCaCertsSettings()
    
    
    public UnaryCallSettings<FetchCaCertsRequest,FetchCaCertsResponse> fetchCaCertsSettings()

Returns the object with the settings used for calls to fetchCaCerts.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchCaCertsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.FetchCaCertsRequest),[FetchCaCertsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.FetchCaCertsResponse)>` |   
  
### fetchCertificateAuthorityCsrSettings()
    
    
    public UnaryCallSettings<FetchCertificateAuthorityCsrRequest,FetchCertificateAuthorityCsrResponse> fetchCertificateAuthorityCsrSettings()

Returns the object with the settings used for calls to fetchCertificateAuthorityCsr.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FetchCertificateAuthorityCsrRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.FetchCertificateAuthorityCsrRequest),[FetchCertificateAuthorityCsrResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.FetchCertificateAuthorityCsrResponse)>` |   
  
### getCaPoolSettings()
    
    
    public UnaryCallSettings<GetCaPoolRequest,CaPool> getCaPoolSettings()

Returns the object with the settings used for calls to getCaPool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.GetCaPoolRequest),[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool)>` |   
  
### getCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<GetCertificateAuthorityRequest,CertificateAuthority> getCertificateAuthoritySettings()

Returns the object with the settings used for calls to getCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.GetCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority)>` |   
  
### getCertificateRevocationListSettings()
    
    
    public UnaryCallSettings<GetCertificateRevocationListRequest,CertificateRevocationList> getCertificateRevocationListSettings()

Returns the object with the settings used for calls to getCertificateRevocationList.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCertificateRevocationListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.GetCertificateRevocationListRequest),[CertificateRevocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList)>` |   
  
### getCertificateSettings()
    
    
    public UnaryCallSettings<GetCertificateRequest,Certificate> getCertificateSettings()

Returns the object with the settings used for calls to getCertificate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.GetCertificateRequest),[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate)>` |   
  
### getCertificateTemplateSettings()
    
    
    public UnaryCallSettings<GetCertificateTemplateRequest,CertificateTemplate> getCertificateTemplateSettings()

Returns the object with the settings used for calls to getCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.GetCertificateTemplateRequest),[CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate)>` |   
  
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
  
### listCaPoolsSettings()
    
    
    public PagedCallSettings<ListCaPoolsRequest,ListCaPoolsResponse,CertificateAuthorityServiceClient.ListCaPoolsPagedResponse> listCaPoolsSettings()

Returns the object with the settings used for calls to listCaPools.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCaPoolsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCaPoolsRequest),[ListCaPoolsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCaPoolsResponse),[ListCaPoolsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.ListCaPoolsPagedResponse)>` |   
  
### listCertificateAuthoritiesSettings()
    
    
    public PagedCallSettings<ListCertificateAuthoritiesRequest,ListCertificateAuthoritiesResponse,CertificateAuthorityServiceClient.ListCertificateAuthoritiesPagedResponse> listCertificateAuthoritiesSettings()

Returns the object with the settings used for calls to listCertificateAuthorities.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCertificateAuthoritiesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificateAuthoritiesRequest),[ListCertificateAuthoritiesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificateAuthoritiesResponse),[ListCertificateAuthoritiesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.ListCertificateAuthoritiesPagedResponse)>` |   
  
### listCertificateRevocationListsSettings()
    
    
    public PagedCallSettings<ListCertificateRevocationListsRequest,ListCertificateRevocationListsResponse,CertificateAuthorityServiceClient.ListCertificateRevocationListsPagedResponse> listCertificateRevocationListsSettings()

Returns the object with the settings used for calls to listCertificateRevocationLists.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCertificateRevocationListsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificateRevocationListsRequest),[ListCertificateRevocationListsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificateRevocationListsResponse),[ListCertificateRevocationListsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.ListCertificateRevocationListsPagedResponse)>` |   
  
### listCertificateTemplatesSettings()
    
    
    public PagedCallSettings<ListCertificateTemplatesRequest,ListCertificateTemplatesResponse,CertificateAuthorityServiceClient.ListCertificateTemplatesPagedResponse> listCertificateTemplatesSettings()

Returns the object with the settings used for calls to listCertificateTemplates.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCertificateTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificateTemplatesRequest),[ListCertificateTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificateTemplatesResponse),[ListCertificateTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.ListCertificateTemplatesPagedResponse)>` |   
  
### listCertificatesSettings()
    
    
    public PagedCallSettings<ListCertificatesRequest,ListCertificatesResponse,CertificateAuthorityServiceClient.ListCertificatesPagedResponse> listCertificatesSettings()

Returns the object with the settings used for calls to listCertificates.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCertificatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificatesRequest),[ListCertificatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.ListCertificatesResponse),[ListCertificatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.ListCertificatesPagedResponse)>` |   
  
### listLocationsSettings()
    
    
    public PagedCallSettings<ListLocationsRequest,ListLocationsResponse,CertificateAuthorityServiceClient.ListLocationsPagedResponse> listLocationsSettings()

Returns the object with the settings used for calls to listLocations.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<com.google.cloud.location.ListLocationsRequest,com.google.cloud.location.ListLocationsResponse,[ListLocationsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceClient.ListLocationsPagedResponse)>` |   
  
### revokeCertificateSettings()
    
    
    public UnaryCallSettings<RevokeCertificateRequest,Certificate> revokeCertificateSettings()

Returns the object with the settings used for calls to revokeCertificate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RevokeCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.RevokeCertificateRequest),[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate)>` |   
  
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
    
    
    public CertificateAuthorityServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[CertificateAuthorityServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthorityServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### undeleteCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<UndeleteCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> undeleteCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to undeleteCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UndeleteCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### undeleteCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<UndeleteCertificateAuthorityRequest,Operation> undeleteCertificateAuthoritySettings()

Returns the object with the settings used for calls to undeleteCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UndeleteCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UndeleteCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCaPoolOperationSettings()
    
    
    public OperationCallSettings<UpdateCaPoolRequest,CaPool,OperationMetadata> updateCaPoolOperationSettings()

Returns the object with the settings used for calls to updateCaPool.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCaPoolRequest),[CaPool](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CaPool),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### updateCaPoolSettings()
    
    
    public UnaryCallSettings<UpdateCaPoolRequest,Operation> updateCaPoolSettings()

Returns the object with the settings used for calls to updateCaPool.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCaPoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCaPoolRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCertificateAuthorityOperationSettings()
    
    
    public OperationCallSettings<UpdateCertificateAuthorityRequest,CertificateAuthority,OperationMetadata> updateCertificateAuthorityOperationSettings()

Returns the object with the settings used for calls to updateCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateAuthorityRequest),[CertificateAuthority](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateAuthority),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### updateCertificateAuthoritySettings()
    
    
    public UnaryCallSettings<UpdateCertificateAuthorityRequest,Operation> updateCertificateAuthoritySettings()

Returns the object with the settings used for calls to updateCertificateAuthority.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCertificateAuthorityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateAuthorityRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCertificateRevocationListOperationSettings()
    
    
    public OperationCallSettings<UpdateCertificateRevocationListRequest,CertificateRevocationList,OperationMetadata> updateCertificateRevocationListOperationSettings()

Returns the object with the settings used for calls to updateCertificateRevocationList.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateCertificateRevocationListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateRevocationListRequest),[CertificateRevocationList](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateRevocationList),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### updateCertificateRevocationListSettings()
    
    
    public UnaryCallSettings<UpdateCertificateRevocationListRequest,Operation> updateCertificateRevocationListSettings()

Returns the object with the settings used for calls to updateCertificateRevocationList.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCertificateRevocationListRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateRevocationListRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### updateCertificateSettings()
    
    
    public UnaryCallSettings<UpdateCertificateRequest,Certificate> updateCertificateSettings()

Returns the object with the settings used for calls to updateCertificate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCertificateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateRequest),[Certificate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.Certificate)>` |   
  
### updateCertificateTemplateOperationSettings()
    
    
    public OperationCallSettings<UpdateCertificateTemplateRequest,CertificateTemplate,OperationMetadata> updateCertificateTemplateOperationSettings()

Returns the object with the settings used for calls to updateCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest),[CertificateTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.CertificateTemplate),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.OperationMetadata)>` |   
  
### updateCertificateTemplateSettings()
    
    
    public UnaryCallSettings<UpdateCertificateTemplateRequest,Operation> updateCertificateTemplateSettings()

Returns the object with the settings used for calls to updateCertificateTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateCertificateTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-security-private-ca/latest/com.google.cloud.security.privateca.v1.UpdateCertificateTemplateRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
