---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings
title: Class CloudChannelReportsServiceSettings (3.103.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:26:52.154677+00:00
---

# Class CloudChannelReportsServiceSettings (3.103.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class CloudChannelReportsServiceSettings (3.103.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.103.0 (latest)  3.99.0  3.98.0  3.97.0  3.95.0  3.92.0  3.91.0  3.89.0  3.87.0  3.86.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.78.0  3.77.0  3.76.0  3.74.0  3.72.0  3.71.0  3.68.0  3.67.0  3.66.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.6  3.6.1  3.5.1  3.3.1 
    
    
    public class CloudChannelReportsServiceSettings extends ClientSettings<CloudChannelReportsServiceSettings>

**Deprecated.** _This class is deprecated and will be removed in the next major version update._

Settings class to configure an instance of [CloudChannelReportsServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient).

The default instance has everything set to sensible defaults:

  * The default service address (cloudchannel.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of runReportJob:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelReportsServiceSettings.Builder cloudChannelReportsServiceSettingsBuilder =
         CloudChannelReportsServiceSettings.newBuilder();
     cloudChannelReportsServiceSettingsBuilder
         .runReportJobSettings()
         .setRetrySettings(
             cloudChannelReportsServiceSettingsBuilder
                 .runReportJobSettings()
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
     CloudChannelReportsServiceSettings cloudChannelReportsServiceSettings =
         cloudChannelReportsServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

To configure the RetrySettings of a Long Running Operation method, create an OperationTimedPollAlgorithm object and update the RPC's polling algorithm. For example, to configure the RetrySettings for runReportJob:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     CloudChannelReportsServiceSettings.Builder cloudChannelReportsServiceSettingsBuilder =
         CloudChannelReportsServiceSettings.newBuilder();
     TimedRetryAlgorithm timedRetryAlgorithm =
         OperationalTimedPollAlgorithm.create(
             RetrySettings.newBuilder()
                 .setInitialRetryDelayDuration(Duration.ofMillis(500))
                 .setRetryDelayMultiplier(1.5)
                 .setMaxRetryDelayDuration(Duration.ofMillis(5000))
                 .setTotalTimeoutDuration(Duration.ofHours(24))
                 .build());
     cloudChannelReportsServiceSettingsBuilder
         .createClusterOperationSettings()
         .setPollingAlgorithm(timedRetryAlgorithm)
         .build();
     

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [ClientSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html) > CloudChannelReportsServiceSettings

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

### create(CloudChannelReportsServiceStubSettings stub) (deprecated)
    
    
    public static final CloudChannelReportsServiceSettings create(CloudChannelReportsServiceStubSettings stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[CloudChannelReportsServiceStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.stub.CloudChannelReportsServiceStubSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### defaultApiClientHeaderProviderBuilder() (deprecated)
    
    
    public static ApiClientHeaderProvider.Builder defaultApiClientHeaderProviderBuilder()

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiClientHeaderProvider.Builder.html)` |   
  
### defaultCredentialsProviderBuilder() (deprecated)
    
    
    public static GoogleCredentialsProvider.Builder defaultCredentialsProviderBuilder()

Returns a builder for the default credentials for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.GoogleCredentialsProvider.Builder.html)` |   
  
### defaultExecutorProviderBuilder() (deprecated)
    
    
    public static InstantiatingExecutorProvider.Builder defaultExecutorProviderBuilder()

Returns a builder for the default ExecutorProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.core.InstantiatingExecutorProvider.Builder.html)` |   
  
### defaultGrpcTransportProviderBuilder() (deprecated)
    
    
    public static InstantiatingGrpcChannelProvider.Builder defaultGrpcTransportProviderBuilder()

Returns a builder for the default gRPC ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html)` |   
  
### defaultHttpJsonTransportProviderBuilder() (deprecated)
    
    
    public static InstantiatingHttpJsonChannelProvider.Builder defaultHttpJsonTransportProviderBuilder()

**Beta**

This feature is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the launch stage descriptions.

Returns a builder for the default REST ChannelProvider for this service.

**Returns**  
---  
**Type** | **Description**  
`[Builder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.httpjson.InstantiatingHttpJsonChannelProvider.Builder.html)` |   
  
### defaultTransportChannelProvider() (deprecated)
    
    
    public static TransportChannelProvider defaultTransportChannelProvider()

**Returns**  
---  
**Type** | **Description**  
`[TransportChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.TransportChannelProvider.html)` |   
  
### getDefaultEndpoint() (deprecated)
    
    
    public static String getDefaultEndpoint()

Returns the default service endpoint.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDefaultServiceScopes() (deprecated)
    
    
    public static List<String> getDefaultServiceScopes()

Returns the default service scopes.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### newBuilder() (deprecated)
    
    
    public static CloudChannelReportsServiceSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext) (deprecated)
    
    
    public static CloudChannelReportsServiceSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings.Builder)` |   
  
### newHttpJsonBuilder() (deprecated)
    
    
    public static CloudChannelReportsServiceSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings.Builder)` |   
  
## Constructors 

### CloudChannelReportsServiceSettings(CloudChannelReportsServiceSettings.Builder settingsBuilder) (deprecated)
    
    
    protected CloudChannelReportsServiceSettings(CloudChannelReportsServiceSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[CloudChannelReportsServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings.Builder)`  
  
  
## Methods 

### fetchReportResultsSettings() (deprecated)
    
    
    public PagedCallSettings<FetchReportResultsRequest,FetchReportResultsResponse,CloudChannelReportsServiceClient.FetchReportResultsPagedResponse> fetchReportResultsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to fetchReportResults.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[FetchReportResultsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.FetchReportResultsRequest),[FetchReportResultsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.FetchReportResultsResponse),[FetchReportResultsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.FetchReportResultsPagedResponse)>` |   
  
### listReportsSettings() (deprecated)
    
    
    public PagedCallSettings<ListReportsRequest,ListReportsResponse,CloudChannelReportsServiceClient.ListReportsPagedResponse> listReportsSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to listReports.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListReportsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListReportsRequest),[ListReportsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.ListReportsResponse),[ListReportsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceClient.ListReportsPagedResponse)>` |   
  
### runReportJobOperationSettings() (deprecated)
    
    
    public OperationCallSettings<RunReportJobRequest,RunReportJobResponse,OperationMetadata> runReportJobOperationSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to runReportJob.

**Returns**  
---  
**Type** | **Description**  
`[OperationCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.OperationCallSettings.html)<[RunReportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobRequest),[RunReportJobResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobResponse),[OperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.OperationMetadata)>` |   
  
### runReportJobSettings() (deprecated)
    
    
    public UnaryCallSettings<RunReportJobRequest,Operation> runReportJobSettings()

**Deprecated.** _This method is deprecated and will be removed in the next major version update._

Returns the object with the settings used for calls to runReportJob.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RunReportJobRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.RunReportJobRequest),[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### toBuilder() (deprecated)
    
    
    public CloudChannelReportsServiceSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[CloudChannelReportsServiceSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-channel/latest/com.google.cloud.channel.v1.CloudChannelReportsServiceSettings.Builder)` |   
**Overrides**

[ClientSettings<SettingsT>.<B>toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ClientSettings.html#com_google_api_gax_rpc_ClientSettings__B_toBuilder__)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
