---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings
title: Class ChatServiceStubSettings (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:06.477030+00:00
---

# Class ChatServiceStubSettings (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ChatServiceStubSettings (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public class ChatServiceStubSettings extends StubSettings<ChatServiceStubSettings>

Settings class to configure an instance of [ChatServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStub).

The default instance has everything set to sensible defaults:

  * The default service address (chat.googleapis.com) and default port (443) are used. 
  * Credentials are acquired automatically through Application Default Credentials. 
  * Retries are configured for idempotent methods but not for non-idempotent methods. 



The builder of this class is recursive, so contained classes are themselves builders. When build() is called, the tree of builders is called to create the complete settings object.

For example, to set the [RetrySettings](https://cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) of createMessage:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ChatServiceStubSettings.Builder chatServiceSettingsBuilder =
         ChatServiceStubSettings.newBuilder();
     chatServiceSettingsBuilder
         .createMessageSettings()
         .setRetrySettings(
             chatServiceSettingsBuilder
                 .createMessageSettings()
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
     ChatServiceStubSettings chatServiceSettings = chatServiceSettingsBuilder.build();
     

Please refer to the [Client Side Retry Guide](https://docs.cloud.google.com/java/docs/client-retries) for additional support in setting retries.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [StubSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html) > ChatServiceStubSettings

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
    
    
    public static ChatServiceStubSettings.Builder newBuilder()

Returns a new gRPC builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings.Builder)` |   
  
### newBuilder(@Nullable ClientContext clientContext)
    
    
    public static ChatServiceStubSettings.Builder newBuilder(@Nullable ClientContext clientContext)

Returns a new builder for this class.

**Parameter**  
---  
**Name** | **Description**  
`clientContext` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ClientContext`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings.Builder)` |   
  
### newHttpJsonBuilder()
    
    
    public static ChatServiceStubSettings.Builder newHttpJsonBuilder()

Returns a new REST builder for this class.

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings.Builder)` |   
  
## Constructors 

### ChatServiceStubSettings(ChatServiceStubSettings.Builder settingsBuilder)
    
    
    protected ChatServiceStubSettings(ChatServiceStubSettings.Builder settingsBuilder)

**Parameter**  
---  
**Name** | **Description**  
`settingsBuilder` | `[ChatServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings.Builder)`  
  
  
## Methods 

### completeImportSpaceSettings()
    
    
    public UnaryCallSettings<CompleteImportSpaceRequest,CompleteImportSpaceResponse> completeImportSpaceSettings()

Returns the object with the settings used for calls to completeImportSpace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CompleteImportSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequest),[CompleteImportSpaceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponse)>` |   
  
### createCustomEmojiSettings()
    
    
    public UnaryCallSettings<CreateCustomEmojiRequest,CustomEmoji> createCustomEmojiSettings()

Returns the object with the settings used for calls to createCustomEmoji.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequest),[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)>` |   
  
### createMembershipSettings()
    
    
    public UnaryCallSettings<CreateMembershipRequest,Membership> createMembershipSettings()

Returns the object with the settings used for calls to createMembership.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### createMessagePinSettings()
    
    
    public UnaryCallSettings<CreateMessagePinRequest,MessagePin> createMessagePinSettings()

Returns the object with the settings used for calls to createMessagePin.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequest),[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)>` |   
  
### createMessageSettings()
    
    
    public UnaryCallSettings<CreateMessageRequest,Message> createMessageSettings()

Returns the object with the settings used for calls to createMessage.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest),[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>` |   
  
### createReactionSettings()
    
    
    public UnaryCallSettings<CreateReactionRequest,Reaction> createReactionSettings()

Returns the object with the settings used for calls to createReaction.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequest),[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)>` |   
  
### createSectionSettings()
    
    
    public UnaryCallSettings<CreateSectionRequest,Section> createSectionSettings()

Returns the object with the settings used for calls to createSection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequest),[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)>` |   
  
### createSpaceSettings()
    
    
    public UnaryCallSettings<CreateSpaceRequest,Space> createSpaceSettings()

Returns the object with the settings used for calls to createSpace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[CreateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### createStub()
    
    
    public ChatServiceStub createStub()

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStub)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### deleteCustomEmojiSettings()
    
    
    public UnaryCallSettings<DeleteCustomEmojiRequest,Empty> deleteCustomEmojiSettings()

Returns the object with the settings used for calls to deleteCustomEmoji.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteMembershipSettings()
    
    
    public UnaryCallSettings<DeleteMembershipRequest,Membership> deleteMembershipSettings()

Returns the object with the settings used for calls to deleteMembership.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### deleteMessagePinSettings()
    
    
    public UnaryCallSettings<DeleteMessagePinRequest,Empty> deleteMessagePinSettings()

Returns the object with the settings used for calls to deleteMessagePin.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteMessageSettings()
    
    
    public UnaryCallSettings<DeleteMessageRequest,Empty> deleteMessageSettings()

Returns the object with the settings used for calls to deleteMessage.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteReactionSettings()
    
    
    public UnaryCallSettings<DeleteReactionRequest,Empty> deleteReactionSettings()

Returns the object with the settings used for calls to deleteReaction.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSectionSettings()
    
    
    public UnaryCallSettings<DeleteSectionRequest,Empty> deleteSectionSettings()

Returns the object with the settings used for calls to deleteSection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSpaceSettings()
    
    
    public UnaryCallSettings<DeleteSpaceRequest,Empty> deleteSpaceSettings()

Returns the object with the settings used for calls to deleteSpace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[DeleteSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### findDirectMessageSettings()
    
    
    public UnaryCallSettings<FindDirectMessageRequest,Space> findDirectMessageSettings()

Returns the object with the settings used for calls to findDirectMessage.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[FindDirectMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### findGroupChatsSettings()
    
    
    public PagedCallSettings<FindGroupChatsRequest,FindGroupChatsResponse,ChatServiceClient.FindGroupChatsPagedResponse> findGroupChatsSettings()

Returns the object with the settings used for calls to findGroupChats.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[FindGroupChatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest),[FindGroupChatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsResponse),[FindGroupChatsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.FindGroupChatsPagedResponse)>` |   
  
### getAttachmentSettings()
    
    
    public UnaryCallSettings<GetAttachmentRequest,Attachment> getAttachmentSettings()

Returns the object with the settings used for calls to getAttachment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequest),[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)>` |   
  
### getAvailabilitySettings()
    
    
    public UnaryCallSettings<GetAvailabilityRequest,Availability> getAvailabilitySettings()

Returns the object with the settings used for calls to getAvailability.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### getCustomEmojiSettings()
    
    
    public UnaryCallSettings<GetCustomEmojiRequest,CustomEmoji> getCustomEmojiSettings()

Returns the object with the settings used for calls to getCustomEmoji.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequest),[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)>` |   
  
### getLibraryMetadata()
    
    
    protected LibraryMetadata getLibraryMetadata()

**Returns**  
---  
**Type** | **Description**  
`[LibraryMetadata](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.LibraryMetadata.html)` |   
**Overrides**

[StubSettings<SettingsT>.getLibraryMetadata()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getLibraryMetadata__)

### getMembershipSettings()
    
    
    public UnaryCallSettings<GetMembershipRequest,Membership> getMembershipSettings()

Returns the object with the settings used for calls to getMembership.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### getMessageSettings()
    
    
    public UnaryCallSettings<GetMessageRequest,Message> getMessageSettings()

Returns the object with the settings used for calls to getMessage.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequest),[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>` |   
  
### getServiceName()
    
    
    public String getServiceName()

Returns the default service name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[StubSettings<SettingsT>.getServiceName()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_getServiceName__)

### getSpaceEventSettings()
    
    
    public UnaryCallSettings<GetSpaceEventRequest,SpaceEvent> getSpaceEventSettings()

Returns the object with the settings used for calls to getSpaceEvent.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSpaceEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequest),[SpaceEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent)>` |   
  
### getSpaceNotificationSettingSettings()
    
    
    public UnaryCallSettings<GetSpaceNotificationSettingRequest,SpaceNotificationSetting> getSpaceNotificationSettingSettings()

Returns the object with the settings used for calls to getSpaceNotificationSetting.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequest),[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)>` |   
  
### getSpaceReadStateSettings()
    
    
    public UnaryCallSettings<GetSpaceReadStateRequest,SpaceReadState> getSpaceReadStateSettings()

Returns the object with the settings used for calls to getSpaceReadState.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequest),[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)>` |   
  
### getSpaceSettings()
    
    
    public UnaryCallSettings<GetSpaceRequest,Space> getSpaceSettings()

Returns the object with the settings used for calls to getSpace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### getThreadReadStateSettings()
    
    
    public UnaryCallSettings<GetThreadReadStateRequest,ThreadReadState> getThreadReadStateSettings()

Returns the object with the settings used for calls to getThreadReadState.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[GetThreadReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequest),[ThreadReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState)>` |   
  
### listCustomEmojisSettings()
    
    
    public PagedCallSettings<ListCustomEmojisRequest,ListCustomEmojisResponse,ChatServiceClient.ListCustomEmojisPagedResponse> listCustomEmojisSettings()

Returns the object with the settings used for calls to listCustomEmojis.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListCustomEmojisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest),[ListCustomEmojisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisResponse),[ListCustomEmojisPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisPagedResponse)>` |   
  
### listMembershipsSettings()
    
    
    public PagedCallSettings<ListMembershipsRequest,ListMembershipsResponse,ChatServiceClient.ListMembershipsPagedResponse> listMembershipsSettings()

Returns the object with the settings used for calls to listMemberships.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest),[ListMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsResponse),[ListMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse)>` |   
  
### listMessagePinsSettings()
    
    
    public PagedCallSettings<ListMessagePinsRequest,ListMessagePinsResponse,ChatServiceClient.ListMessagePinsPagedResponse> listMessagePinsSettings()

Returns the object with the settings used for calls to listMessagePins.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListMessagePinsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest),[ListMessagePinsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsResponse),[ListMessagePinsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse)>` |   
  
### listMessagesSettings()
    
    
    public PagedCallSettings<ListMessagesRequest,ListMessagesResponse,ChatServiceClient.ListMessagesPagedResponse> listMessagesSettings()

Returns the object with the settings used for calls to listMessages.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest),[ListMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesResponse),[ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse)>` |   
  
### listReactionsSettings()
    
    
    public PagedCallSettings<ListReactionsRequest,ListReactionsResponse,ChatServiceClient.ListReactionsPagedResponse> listReactionsSettings()

Returns the object with the settings used for calls to listReactions.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListReactionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest),[ListReactionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsResponse),[ListReactionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse)>` |   
  
### listSectionItemsSettings()
    
    
    public PagedCallSettings<ListSectionItemsRequest,ListSectionItemsResponse,ChatServiceClient.ListSectionItemsPagedResponse> listSectionItemsSettings()

Returns the object with the settings used for calls to listSectionItems.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSectionItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest),[ListSectionItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsResponse),[ListSectionItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse)>` |   
  
### listSectionsSettings()
    
    
    public PagedCallSettings<ListSectionsRequest,ListSectionsResponse,ChatServiceClient.ListSectionsPagedResponse> listSectionsSettings()

Returns the object with the settings used for calls to listSections.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest),[ListSectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsResponse),[ListSectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse)>` |   
  
### listSpaceEventsSettings()
    
    
    public PagedCallSettings<ListSpaceEventsRequest,ListSpaceEventsResponse,ChatServiceClient.ListSpaceEventsPagedResponse> listSpaceEventsSettings()

Returns the object with the settings used for calls to listSpaceEvents.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSpaceEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest),[ListSpaceEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsResponse),[ListSpaceEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse)>` |   
  
### listSpacesSettings()
    
    
    public PagedCallSettings<ListSpacesRequest,ListSpacesResponse,ChatServiceClient.ListSpacesPagedResponse> listSpacesSettings()

Returns the object with the settings used for calls to listSpaces.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[ListSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest),[ListSpacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesResponse),[ListSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesPagedResponse)>` |   
  
### markAsActiveSettings()
    
    
    public UnaryCallSettings<MarkAsActiveRequest,Availability> markAsActiveSettings()

Returns the object with the settings used for calls to markAsActive.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MarkAsActiveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### markAsAwaySettings()
    
    
    public UnaryCallSettings<MarkAsAwayRequest,Availability> markAsAwaySettings()

Returns the object with the settings used for calls to markAsAway.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MarkAsAwayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### markAsDoNotDisturbSettings()
    
    
    public UnaryCallSettings<MarkAsDoNotDisturbRequest,Availability> markAsDoNotDisturbSettings()

Returns the object with the settings used for calls to markAsDoNotDisturb.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MarkAsDoNotDisturbRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### moveSectionItemSettings()
    
    
    public UnaryCallSettings<MoveSectionItemRequest,MoveSectionItemResponse> moveSectionItemSettings()

Returns the object with the settings used for calls to moveSectionItem.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[MoveSectionItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequest),[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)>` |   
  
### positionSectionSettings()
    
    
    public UnaryCallSettings<PositionSectionRequest,PositionSectionResponse> positionSectionSettings()

Returns the object with the settings used for calls to positionSection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[PositionSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest),[PositionSectionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponse)>` |   
  
### searchMessagesSettings()
    
    
    public PagedCallSettings<SearchMessagesRequest,SearchMessagesResponse,ChatServiceClient.SearchMessagesPagedResponse> searchMessagesSettings()

Returns the object with the settings used for calls to searchMessages.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest),[SearchMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesResponse),[SearchMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse)>` |   
  
### searchSpacesSettings()
    
    
    public PagedCallSettings<SearchSpacesRequest,SearchSpacesResponse,ChatServiceClient.SearchSpacesPagedResponse> searchSpacesSettings()

Returns the object with the settings used for calls to searchSpaces.

**Returns**  
---  
**Type** | **Description**  
`[PagedCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.PagedCallSettings.html)<[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest),[SearchSpacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse),[SearchSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesPagedResponse)>` |   
  
### setUpSpaceSettings()
    
    
    public UnaryCallSettings<SetUpSpaceRequest,Space> setUpSpaceSettings()

Returns the object with the settings used for calls to setUpSpace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[SetUpSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### toBuilder()
    
    
    public ChatServiceStubSettings.Builder toBuilder()

Returns a builder containing all the values of this settings class.

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceStubSettings.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStubSettings.Builder)` |   
**Overrides**

[StubSettings<SettingsT>.toBuilder()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StubSettings.html#com_google_api_gax_rpc_StubSettings_toBuilder__)

### updateAvailabilitySettings()
    
    
    public UnaryCallSettings<UpdateAvailabilityRequest,Availability> updateAvailabilitySettings()

Returns the object with the settings used for calls to updateAvailability.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### updateMembershipSettings()
    
    
    public UnaryCallSettings<UpdateMembershipRequest,Membership> updateMembershipSettings()

Returns the object with the settings used for calls to updateMembership.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### updateMessageSettings()
    
    
    public UnaryCallSettings<UpdateMessageRequest,Message> updateMessageSettings()

Returns the object with the settings used for calls to updateMessage.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequest),[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>` |   
  
### updateSectionSettings()
    
    
    public UnaryCallSettings<UpdateSectionRequest,Section> updateSectionSettings()

Returns the object with the settings used for calls to updateSection.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequest),[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)>` |   
  
### updateSpaceNotificationSettingSettings()
    
    
    public UnaryCallSettings<UpdateSpaceNotificationSettingRequest,SpaceNotificationSetting> updateSpaceNotificationSettingSettings()

Returns the object with the settings used for calls to updateSpaceNotificationSetting.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequest),[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)>` |   
  
### updateSpaceReadStateSettings()
    
    
    public UnaryCallSettings<UpdateSpaceReadStateRequest,SpaceReadState> updateSpaceReadStateSettings()

Returns the object with the settings used for calls to updateSpaceReadState.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequest),[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)>` |   
  
### updateSpaceSettings()
    
    
    public UnaryCallSettings<UpdateSpaceRequest,Space> updateSpaceSettings()

Returns the object with the settings used for calls to updateSpace.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UpdateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### uploadAttachmentSettings()
    
    
    public UnaryCallSettings<UploadAttachmentRequest,UploadAttachmentResponse> uploadAttachmentSettings()

Returns the object with the settings used for calls to uploadAttachment.

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallSettings.html)<[UploadAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequest),[UploadAttachmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
