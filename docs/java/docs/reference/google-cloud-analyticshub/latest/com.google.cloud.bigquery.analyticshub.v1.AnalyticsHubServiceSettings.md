---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings
title: Class AnalyticsHubServiceSettings (0.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:37:40.515568+00:00
---

# Class AnalyticsHubServiceSettings (0.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class AnalyticsHubServiceSettings (0.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.96.0 (latest)  0.92.0  0.91.0  0.90.0  0.88.0  0.85.0  0.84.0  0.82.0  0.80.0  0.79.0  0.78.0  0.77.0  0.75.0  0.73.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.61.0  0.60.0  0.59.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public class AnalyticsHubServiceSettings extends ClientSettings<AnalyticsHubServiceSettings>

Settings class to configure an instance of [AnalyticsHubServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (analyticshub.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of getDataExchange:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AnalyticsHubServiceSettings.Builder analyticsHubServiceSettingsBuilder =
         AnalyticsHubServiceSettings.newBuilder();
     analyticsHubServiceSettingsBuilder
         .getDataExchangeSettings()
         .setRetrySettings(
             analyticsHubServiceSettingsBuilder
                 .getDataExchangeSettings()
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
     AnalyticsHubServiceSettings analyticsHubServiceSettings =
         analyticsHubServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for subscribeDataExchange:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     AnalyticsHubServiceSettings.Builder analyticsHubServiceSettingsBuilder =
         AnalyticsHubServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     analyticsHubServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > AnalyticsHubServiceSettings

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

### create(AnalyticsHubServiceStubSettings stub)
    
    
    public static final AnalyticsHubServiceSettings create(AnalyticsHubServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[AnalyticsHubServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.stub.AnalyticsHubServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings)` |   
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
    
    
    public static AnalyticsHubServiceSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static AnalyticsHubServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static AnalyticsHubServiceSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings.Builder)` |   
  
## Constructors 

### AnalyticsHubServiceSettings(AnalyticsHubServiceSettings.Builder settingsBuilder)
    
    
    protected AnalyticsHubServiceSettings(AnalyticsHubServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[AnalyticsHubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings.Builder)`  
  
  
## Methods 

### approveQueryTemplateSettings()
    
    
    public UnaryCallSettings<ApproveQueryTemplateRequest,QueryTemplate> approveQueryTemplateSettings()

Returns the object with the settings used for calls to approveQueryTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ApproveQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ApproveQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### createDataExchangeSettings()
    
    
    public UnaryCallSettings<CreateDataExchangeRequest,DataExchange> createDataExchangeSettings()

Returns the object with the settings used for calls to createDataExchange.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateDataExchangeRequest),[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>` |   
  
### createListingSettings()
    
    
    public UnaryCallSettings<CreateListingRequest,Listing> createListingSettings()

Returns the object with the settings used for calls to createListing.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateListingRequest),[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>` |   
  
### createQueryTemplateSettings()
    
    
    public UnaryCallSettings<CreateQueryTemplateRequest,QueryTemplate> createQueryTemplateSettings()

Returns the object with the settings used for calls to createQueryTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.CreateQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### deleteDataExchangeSettings()
    
    
    public UnaryCallSettings<DeleteDataExchangeRequest,Empty> deleteDataExchangeSettings()

Returns the object with the settings used for calls to deleteDataExchange.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteDataExchangeRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteListingSettings()
    
    
    public UnaryCallSettings<DeleteListingRequest,Empty> deleteListingSettings()

Returns the object with the settings used for calls to deleteListing.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteListingRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteQueryTemplateSettings()
    
    
    public UnaryCallSettings<DeleteQueryTemplateRequest,Empty> deleteQueryTemplateSettings()

Returns the object with the settings used for calls to deleteQueryTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteQueryTemplateRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSubscriptionOperationSettings()
    
    
    public OperationCallSettings<DeleteSubscriptionRequest,Empty,OperationMetadata> deleteSubscriptionOperationSettings()

Returns the object with the settings used for calls to deleteSubscription.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteSubscriptionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### deleteSubscriptionSettings()
    
    
    public UnaryCallSettings<DeleteSubscriptionRequest,Operation> deleteSubscriptionSettings()

Returns the object with the settings used for calls to deleteSubscription.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DeleteSubscriptionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getDataExchangeSettings()
    
    
    public UnaryCallSettings<GetDataExchangeRequest,DataExchange> getDataExchangeSettings()

Returns the object with the settings used for calls to getDataExchange.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetDataExchangeRequest),[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>` |   
  
### getIamPolicySettings()
    
    
    public UnaryCallSettings<GetIamPolicyRequest,Policy> getIamPolicySettings()

Returns the object with the settings used for calls to getIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.GetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### getListingSettings()
    
    
    public UnaryCallSettings<GetListingRequest,Listing> getListingSettings()

Returns the object with the settings used for calls to getListing.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetListingRequest),[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>` |   
  
### getQueryTemplateSettings()
    
    
    public UnaryCallSettings<GetQueryTemplateRequest,QueryTemplate> getQueryTemplateSettings()

Returns the object with the settings used for calls to getQueryTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### getSubscriptionSettings()
    
    
    public UnaryCallSettings<GetSubscriptionRequest,Subscription> getSubscriptionSettings()

Returns the object with the settings used for calls to getSubscription.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.GetSubscriptionRequest),[Subscription](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Subscription)>` |   
  
### listDataExchangesSettings()
    
    
    public PagedCallSettings<ListDataExchangesRequest,ListDataExchangesResponse,AnalyticsHubServiceClient.ListDataExchangesPagedResponse> listDataExchangesSettings()

Returns the object with the settings used for calls to listDataExchanges.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesRequest),[ListDataExchangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListDataExchangesResponse),[ListDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListDataExchangesPagedResponse)>` |   
  
### listListingsSettings()
    
    
    public PagedCallSettings<ListListingsRequest,ListListingsResponse,AnalyticsHubServiceClient.ListListingsPagedResponse> listListingsSettings()

Returns the object with the settings used for calls to listListings.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListListingsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsRequest),[ListListingsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListListingsResponse),[ListListingsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListListingsPagedResponse)>` |   
  
### listOrgDataExchangesSettings()
    
    
    public PagedCallSettings<ListOrgDataExchangesRequest,ListOrgDataExchangesResponse,AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse> listOrgDataExchangesSettings()

Returns the object with the settings used for calls to listOrgDataExchanges.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListOrgDataExchangesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesRequest),[ListOrgDataExchangesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListOrgDataExchangesResponse),[ListOrgDataExchangesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListOrgDataExchangesPagedResponse)>` |   
  
### listQueryTemplatesSettings()
    
    
    public PagedCallSettings<ListQueryTemplatesRequest,ListQueryTemplatesResponse,AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse> listQueryTemplatesSettings()

Returns the object with the settings used for calls to listQueryTemplates.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListQueryTemplatesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesRequest),[ListQueryTemplatesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListQueryTemplatesResponse),[ListQueryTemplatesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListQueryTemplatesPagedResponse)>` |   
  
### listSharedResourceSubscriptionsSettings()
    
    
    public PagedCallSettings<ListSharedResourceSubscriptionsRequest,ListSharedResourceSubscriptionsResponse,AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse> listSharedResourceSubscriptionsSettings()

Returns the object with the settings used for calls to listSharedResourceSubscriptions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsRequest),[ListSharedResourceSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSharedResourceSubscriptionsResponse),[ListSharedResourceSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSharedResourceSubscriptionsPagedResponse)>` |   
  
### listSubscriptionsSettings()
    
    
    public PagedCallSettings<ListSubscriptionsRequest,ListSubscriptionsResponse,AnalyticsHubServiceClient.ListSubscriptionsPagedResponse> listSubscriptionsSettings()

Returns the object with the settings used for calls to listSubscriptions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSubscriptionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsRequest),[ListSubscriptionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.ListSubscriptionsResponse),[ListSubscriptionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceClient.ListSubscriptionsPagedResponse)>` |   
  
### refreshSubscriptionOperationSettings()
    
    
    public OperationCallSettings<RefreshSubscriptionRequest,RefreshSubscriptionResponse,OperationMetadata> refreshSubscriptionOperationSettings()

Returns the object with the settings used for calls to refreshSubscription.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RefreshSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionRequest),[RefreshSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### refreshSubscriptionSettings()
    
    
    public UnaryCallSettings<RefreshSubscriptionRequest,Operation> refreshSubscriptionSettings()

Returns the object with the settings used for calls to refreshSubscription.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RefreshSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RefreshSubscriptionRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### revokeSubscriptionSettings()
    
    
    public UnaryCallSettings<RevokeSubscriptionRequest,RevokeSubscriptionResponse> revokeSubscriptionSettings()

Returns the object with the settings used for calls to revokeSubscription.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RevokeSubscriptionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionRequest),[RevokeSubscriptionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.RevokeSubscriptionResponse)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### submitQueryTemplateSettings()
    
    
    public UnaryCallSettings<SubmitQueryTemplateRequest,QueryTemplate> submitQueryTemplateSettings()

Returns the object with the settings used for calls to submitQueryTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SubmitQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubmitQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
### subscribeDataExchangeOperationSettings()
    
    
    public OperationCallSettings<SubscribeDataExchangeRequest,SubscribeDataExchangeResponse,OperationMetadata> subscribeDataExchangeOperationSettings()

Returns the object with the settings used for calls to subscribeDataExchange.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[SubscribeDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeRequest),[SubscribeDataExchangeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.OperationMetadata)>` |   
  
### subscribeDataExchangeSettings()
    
    
    public UnaryCallSettings<SubscribeDataExchangeRequest,Operation> subscribeDataExchangeSettings()

Returns the object with the settings used for calls to subscribeDataExchange.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SubscribeDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeDataExchangeRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### subscribeListingSettings()
    
    
    public UnaryCallSettings<SubscribeListingRequest,SubscribeListingResponse> subscribeListingSettings()

Returns the object with the settings used for calls to subscribeListing.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SubscribeListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingRequest),[SubscribeListingResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.SubscribeListingResponse)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public AnalyticsHubServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsHubServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.AnalyticsHubServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

### updateDataExchangeSettings()
    
    
    public UnaryCallSettings<UpdateDataExchangeRequest,DataExchange> updateDataExchangeSettings()

Returns the object with the settings used for calls to updateDataExchange.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateDataExchangeRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateDataExchangeRequest),[DataExchange](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.DataExchange)>` |   
  
### updateListingSettings()
    
    
    public UnaryCallSettings<UpdateListingRequest,Listing> updateListingSettings()

Returns the object with the settings used for calls to updateListing.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateListingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateListingRequest),[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.Listing)>` |   
  
### updateQueryTemplateSettings()
    
    
    public UnaryCallSettings<UpdateQueryTemplateRequest,QueryTemplate> updateQueryTemplateSettings()

Returns the object with the settings used for calls to updateQueryTemplate.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateQueryTemplateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.UpdateQueryTemplateRequest),[QueryTemplate](https://docs.cloud.google.com/java/docs/reference/google-cloud-analyticshub/latest/com.google.cloud.bigquery.analyticshub.v1.QueryTemplate)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
