---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStubSettings
title: Class StorageStubSettings (2.75.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:36.207624+00:00
---

# Class StorageStubSettings (2.75.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class StorageStubSettings (2.75.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.75.0 (latest)  2.71.0  2.70.0  2.69.0  2.67.0  2.64.0  2.63.0  2.62.1  2.60.0  2.59.0  2.58.1  2.57.0  2.56.0  2.55.0  2.54.0  2.53.3  2.52.3  2.50.0  2.49.0  2.48.2  2.47.0  2.46.0  2.45.0  2.44.1  2.43.2  2.42.0  2.41.0  2.40.1  2.39.0  2.38.0  2.37.0  2.36.1  2.34.0  2.33.0  2.32.1  2.30.1  2.29.1  2.28.0  2.27.1  2.24.0  2.23.0  2.22.6  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.0  2.15.1  2.14.0  2.13.1  2.12.0  2.11.3  2.10.0  2.9.3  2.8.1  2.7.1  2.6.1  2.5.1  2.4.5  2.3.0  2.2.3  2.1.10 
    
    
    public class StorageStubSettings extends StubSettings<StorageStubSettings>

Settings class to configure an instance of [StorageStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStub).

The default instance has everything set to sensible defaults:

  * The default service address (storage.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of deleteBucket:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     StorageStubSettings.Builder storageSettingsBuilder = StorageStubSettings.newBuilder();
     storageSettingsBuilder
         .deleteBucketSettings()
         .setRetrySettings(
             storageSettingsBuilder
                 .deleteBucketSettings()
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
     StorageStubSettings storageSettings = storageSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > StorageStubSettings

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
    
    
    public static StorageStubSettings.Builder newBuilder()

Returns a new builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[StorageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static StorageStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStubSettings.Builder)` |   
  
## Constructors 

### StorageStubSettings(StorageStubSettings.Builder settingsBuilder)
    
    
    protected StorageStubSettings(StorageStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[StorageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStubSettings.Builder)`  
  
  
## Methods 

### bidiReadObjectSettings()
    
    
    public StreamingCallSettings<BidiReadObjectRequest,BidiReadObjectResponse> bidiReadObjectSettings()

Returns the object with the settings used for calls to bidiReadObject.

**Returns**  
---  
**Type** | **Description**  
`[StreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings.html)<[BidiReadObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.BidiReadObjectRequest),[BidiReadObjectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.BidiReadObjectResponse)>` |   
  
### bidiWriteObjectSettings()
    
    
    public StreamingCallSettings<BidiWriteObjectRequest,BidiWriteObjectResponse> bidiWriteObjectSettings()

Returns the object with the settings used for calls to bidiWriteObject.

**Returns**  
---  
**Type** | **Description**  
`[StreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings.html)<[BidiWriteObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.BidiWriteObjectRequest),[BidiWriteObjectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.BidiWriteObjectResponse)>` |   
  
### cancelResumableWriteSettings()
    
    
    public UnaryCallSettings<CancelResumableWriteRequest,CancelResumableWriteResponse> cancelResumableWriteSettings()

Returns the object with the settings used for calls to cancelResumableWrite.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CancelResumableWriteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.CancelResumableWriteRequest),[CancelResumableWriteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.CancelResumableWriteResponse)>` |   
  
### composeObjectSettings()
    
    
    public UnaryCallSettings<ComposeObjectRequest,Object> composeObjectSettings()

Returns the object with the settings used for calls to composeObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[ComposeObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ComposeObjectRequest),[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)>` |   
  
### createBucketSettings()
    
    
    public UnaryCallSettings<CreateBucketRequest,Bucket> createBucketSettings()

Returns the object with the settings used for calls to createBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.CreateBucketRequest),[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Bucket)>` |   
  
### createStub()
    
    
    public StorageStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[StorageStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteBucketSettings()
    
    
    public UnaryCallSettings<DeleteBucketRequest,Empty> deleteBucketSettings()

Returns the object with the settings used for calls to deleteBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.DeleteBucketRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteObjectSettings()
    
    
    public UnaryCallSettings<DeleteObjectRequest,Empty> deleteObjectSettings()

Returns the object with the settings used for calls to deleteObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.DeleteObjectRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### getBucketSettings()
    
    
    public UnaryCallSettings<GetBucketRequest,Bucket> getBucketSettings()

Returns the object with the settings used for calls to getBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.GetBucketRequest),[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Bucket)>` |   
  
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

### getObjectSettings()
    
    
    public UnaryCallSettings<GetObjectRequest,Object> getObjectSettings()

Returns the object with the settings used for calls to getObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.GetObjectRequest),[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### listBucketsSettings()
    
    
    public PagedCallSettings<ListBucketsRequest,ListBucketsResponse,StorageClient.ListBucketsPagedResponse> listBucketsSettings()

Returns the object with the settings used for calls to listBuckets.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListBucketsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ListBucketsRequest),[ListBucketsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ListBucketsResponse),[ListBucketsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.StorageClient.ListBucketsPagedResponse)>` |   
  
### listObjectsSettings()
    
    
    public PagedCallSettings<ListObjectsRequest,ListObjectsResponse,StorageClient.ListObjectsPagedResponse> listObjectsSettings()

Returns the object with the settings used for calls to listObjects.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListObjectsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ListObjectsRequest),[ListObjectsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ListObjectsResponse),[ListObjectsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.StorageClient.ListObjectsPagedResponse)>` |   
  
### lockBucketRetentionPolicySettings()
    
    
    public UnaryCallSettings<LockBucketRetentionPolicyRequest,Bucket> lockBucketRetentionPolicySettings()

Returns the object with the settings used for calls to lockBucketRetentionPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[LockBucketRetentionPolicyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.LockBucketRetentionPolicyRequest),[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Bucket)>` |   
  
### moveObjectSettings()
    
    
    public UnaryCallSettings<MoveObjectRequest,Object> moveObjectSettings()

Returns the object with the settings used for calls to moveObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.MoveObjectRequest),[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)>` |   
  
### queryWriteStatusSettings()
    
    
    public UnaryCallSettings<QueryWriteStatusRequest,QueryWriteStatusResponse> queryWriteStatusSettings()

Returns the object with the settings used for calls to queryWriteStatus.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[QueryWriteStatusRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.QueryWriteStatusRequest),[QueryWriteStatusResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.QueryWriteStatusResponse)>` |   
  
### readObjectSettings()
    
    
    public ServerStreamingCallSettings<ReadObjectRequest,ReadObjectResponse> readObjectSettings()

Returns the object with the settings used for calls to readObject.

**Returns**  
---  
**Type** | **Description**  
`[ServerStreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ServerStreamingCallSettings.html)<[ReadObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ReadObjectRequest),[ReadObjectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.ReadObjectResponse)>` |   
  
### restoreObjectSettings()
    
    
    public UnaryCallSettings<RestoreObjectRequest,Object> restoreObjectSettings()

Returns the object with the settings used for calls to restoreObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RestoreObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.RestoreObjectRequest),[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)>` |   
  
### rewriteObjectSettings()
    
    
    public UnaryCallSettings<RewriteObjectRequest,RewriteResponse> rewriteObjectSettings()

Returns the object with the settings used for calls to rewriteObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[RewriteObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.RewriteObjectRequest),[RewriteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.RewriteResponse)>` |   
  
### setIamPolicySettings()
    
    
    public UnaryCallSettings<SetIamPolicyRequest,Policy> setIamPolicySettings()

Returns the object with the settings used for calls to setIamPolicy.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.SetIamPolicyRequest,com.google.iam.v1.Policy>` |   
  
### startResumableWriteSettings()
    
    
    public UnaryCallSettings<StartResumableWriteRequest,StartResumableWriteResponse> startResumableWriteSettings()

Returns the object with the settings used for calls to startResumableWrite.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[StartResumableWriteRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.StartResumableWriteRequest),[StartResumableWriteResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.StartResumableWriteResponse)>` |   
  
### testIamPermissionsSettings()
    
    
    public UnaryCallSettings<TestIamPermissionsRequest,TestIamPermissionsResponse> testIamPermissionsSettings()

Returns the object with the settings used for calls to testIamPermissions.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<com.google.iam.v1.TestIamPermissionsRequest,com.google.iam.v1.TestIamPermissionsResponse>` |   
  
### toBuilder()
    
    
    public StorageStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[StorageStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.stub.StorageStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateBucketSettings()
    
    
    public UnaryCallSettings<UpdateBucketRequest,Bucket> updateBucketSettings()

Returns the object with the settings used for calls to updateBucket.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateBucketRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.UpdateBucketRequest),[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Bucket)>` |   
  
### updateObjectSettings()
    
    
    public UnaryCallSettings<UpdateObjectRequest,Object> updateObjectSettings()

Returns the object with the settings used for calls to updateObject.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.UpdateObjectRequest),[Object](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.Object)>` |   
  
### writeObjectSettings()
    
    
    public StreamingCallSettings<WriteObjectRequest,WriteObjectResponse> writeObjectSettings()

Returns the object with the settings used for calls to writeObject.

**Returns**  
---  
**Type** | **Description**  
`[StreamingCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StreamingCallSettings.html)<[WriteObjectRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.WriteObjectRequest),[WriteObjectResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.v2.WriteObjectResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
