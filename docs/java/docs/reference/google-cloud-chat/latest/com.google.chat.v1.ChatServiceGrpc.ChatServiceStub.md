---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceGrpc.ChatServiceStub
title: Class ChatServiceGrpc.ChatServiceStub (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:14.428801+00:00
---

# Class ChatServiceGrpc.ChatServiceStub (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceGrpc.ChatServiceStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ChatServiceGrpc.ChatServiceStub (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public static final class ChatServiceGrpc.ChatServiceStub extends AbstractAsyncStub<ChatServiceGrpc.ChatServiceStub>

A stub to allow clients to do asynchronous rpc calls to service ChatService.

Enables developers to build Chat apps and integrations on Google Chat Platform.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractAsyncStub > ChatServiceGrpc.ChatServiceStub

## Inherited Members

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractAsyncStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected ChatServiceGrpc.ChatServiceStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceGrpc.ChatServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceGrpc.ChatServiceStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### completeImportSpace(CompleteImportSpaceRequest request, StreamObserver<CompleteImportSpaceResponse> responseObserver)
    
    
    public void completeImportSpace(CompleteImportSpaceRequest request, StreamObserver<CompleteImportSpaceResponse> responseObserver)

Completes the [import process](https://developers.google.com/workspace/chat/import-data) for the specified space and makes it visible to users. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and domain-wide delegation with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.import>` For more information, see [Authorize Google Chat apps to import data](https://developers.google.com/workspace/chat/authorize-import).



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteImportSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CompleteImportSpaceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponse)>`  
  
  
### createCustomEmoji(CreateCustomEmojiRequest request, StreamObserver<CustomEmoji> responseObserver)
    
    
    public void createCustomEmoji(CreateCustomEmojiRequest request, StreamObserver<CustomEmoji> responseObserver)

Creates a custom emoji. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.customemojis>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)>`  
  
  
### createMembership(CreateMembershipRequest request, StreamObserver<Membership> responseObserver)
    
    
    public void createMembership(CreateMembershipRequest request, StreamObserver<Membership> responseObserver)

Creates a membership for the calling Chat app, a user, or a Google Group. Creating memberships for other Chat apps isn't supported. When creating a membership, if the specified member has their auto-accept policy turned off, then they're invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope:
    * `<https://www.googleapis.com/auth/chat.app.memberships>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.memberships>`
    * `<https://www.googleapis.com/auth/chat.memberships.app>` (to add the calling app to the space)
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used:
      * `<https://www.googleapis.com/auth/chat.admin.memberships>` App authentication is not supported for the following use cases:
  * Inviting users external to the Workspace organization that owns the space.
  * Adding a Google Group to a space.
  * Adding a Chat app to a space. For example usage, see:
  * [Invite or add a user to a space](https://developers.google.com/workspace/chat/create-members#create-user-membership).
  * [Invite or add a Google Group to a space](https://developers.google.com/workspace/chat/create-members#create-group-membership).
  * [Add the Chat app to a space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>`  
  
  
### createMessage(CreateMessageRequest request, StreamObserver<Message> responseObserver)
    
    
    public void createMessage(CreateMessageRequest request, StreamObserver<Message> responseObserver)

Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope:
    * `<https://www.googleapis.com/auth/chat.bot>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.messages.create>`
    * `<https://www.googleapis.com/auth/chat.messages>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) Chat attributes the message sender differently depending on the type of authentication that you use in your request. The following image shows how Chat attributes a message when you use app authentication. Chat displays the Chat app as the message sender. The content of the message can contain text (`text`), cards (`cardsV2`), and accessory widgets (`accessoryWidgets`). ![Message sent with app authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg) The following image shows how Chat attributes a message when you use user authentication. Chat displays the user as the message sender and attributes the Chat app to the message by displaying its name. The content of message can only contain text (`text`). ![Message sent with user authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg) The maximum message size, including the message contents, is 32,000 bytes. For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>`  
  
  
### createMessagePin(CreateMessagePinRequest request, StreamObserver<MessagePin> responseObserver)
    
    
    public void createMessagePin(CreateMessagePinRequest request, StreamObserver<MessagePin> responseObserver)

Creates a message pin. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.spaces.pins>`
  * `<https://www.googleapis.com/auth/chat.spaces>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)>`  
  
  
### createReaction(CreateReactionRequest request, StreamObserver<Reaction> responseObserver)
    
    
    public void createReaction(CreateReactionRequest request, StreamObserver<Reaction> responseObserver)

Creates a reaction and adds it to a message. For an example, see [Add a reaction to a message](https://developers.google.com/workspace/chat/create-reactions). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.messages.reactions.create>`
  * `<https://www.googleapis.com/auth/chat.messages.reactions>`
  * `<https://www.googleapis.com/auth/chat.messages>`
  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)>`  
  
  
### createSection(CreateSectionRequest request, StreamObserver<Section> responseObserver)
    
    
    public void createSection(CreateSectionRequest request, StreamObserver<Section> responseObserver)

Creates a section in Google Chat. Sections help users group conversations and customize the list of spaces displayed in Chat navigation panel. Only sections of type `CUSTOM_SECTION` can be created. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)>`  
  
  
### createSpace(CreateSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public void createSpace(CreateSpaceRequest request, StreamObserver<Space> responseObserver)

Creates a space. Can be used to create a named space, or a group chat in `Import mode`. For an example, see [Create a space](https://developers.google.com/workspace/chat/create-spaces). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.app.spaces.create>`
    * `<https://www.googleapis.com/auth/chat.app.spaces>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.create>`
    * `<https://www.googleapis.com/auth/chat.spaces>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) When authenticating as an app, the `space.customer` field must be set in the request. When authenticating as an app, the Chat app is added as a member of the space. However, unlike human authentication, the Chat app is not added as a space manager. By default, the Chat app can be removed from the space by all space members. To allow only space managers to remove the app from a space, set `space.permission_settings.manage_apps` to `managers_allowed`. Space membership upon creation depends on whether the space is created in `Import mode`:
  * **Import mode:** No members are created.
  * **All other modes:** The calling user is added as a member. This is:
    * The app itself when using app authentication.
    * The human user when using user authentication. If you receive the error message `ALREADY_EXISTS` when creating a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>`  
  
  
### deleteCustomEmoji(DeleteCustomEmojiRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteCustomEmoji(DeleteCustomEmojiRequest request, StreamObserver<Empty> responseObserver)

Deletes a custom emoji. By default, users can only delete custom emoji they created. [Emoji managers](https://support.google.com/a/answer/12850085) assigned by the administrator can delete any custom emoji in the organization. See [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149). Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.customemojis>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteMembership(DeleteMembershipRequest request, StreamObserver<Membership> responseObserver)
    
    
    public void deleteMembership(DeleteMembershipRequest request, StreamObserver<Membership> responseObserver)

Deletes a membership. For an example, see [Remove a user or a Google Chat app from a space](https://developers.google.com/workspace/chat/delete-members). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope:
    * `<https://www.googleapis.com/auth/chat.app.memberships>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.memberships>`
    * `<https://www.googleapis.com/auth/chat.memberships.app>` (to remove the calling app from the space)
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used:
      * `<https://www.googleapis.com/auth/chat.admin.memberships>` App authentication is not supported for the following use cases:
  * Removing a Google Group from a space.
  * Removing a Chat app from a space. To delete memberships for space managers, the requester must be a space manager. If you're using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) the Chat app must be the space creator.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>`  
  
  
### deleteMessage(DeleteMessageRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteMessage(DeleteMessageRequest request, StreamObserver<Empty> responseObserver)

Deletes a message. For an example, see [Delete a message](https://developers.google.com/workspace/chat/delete-messages). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope:
    * `<https://www.googleapis.com/auth/chat.bot>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.messages>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) When using app authentication, requests can only delete messages created by the calling Chat app.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteMessagePin(DeleteMessagePinRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteMessagePin(DeleteMessagePinRequest request, StreamObserver<Empty> responseObserver)

Deletes a message pin. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.spaces.pins>`
  * `<https://www.googleapis.com/auth/chat.spaces>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteReaction(DeleteReactionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteReaction(DeleteReactionRequest request, StreamObserver<Empty> responseObserver)

Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/workspace/chat/delete-reactions). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.messages.reactions>`
  * `<https://www.googleapis.com/auth/chat.messages>`
  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteSection(DeleteSectionRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteSection(DeleteSectionRequest request, StreamObserver<Empty> responseObserver)

Deletes a section of type `CUSTOM_SECTION`. If the section contains items, such as spaces, the items are moved to Google Chat's default sections and are not deleted. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### deleteSpace(DeleteSpaceRequest request, StreamObserver<Empty> responseObserver)
    
    
    public void deleteSpace(DeleteSpaceRequest request, StreamObserver<Empty> responseObserver)

Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see [Delete a space](https://developers.google.com/workspace/chat/delete-spaces). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope:
    * `<https://www.googleapis.com/auth/chat.app.delete>` (only in spaces the app created)
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.delete>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used:
      * `<https://www.googleapis.com/auth/chat.admin.delete>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>`  
  
  
### findDirectMessage(FindDirectMessageRequest request, StreamObserver<Space> responseObserver)
    
    
    public void findDirectMessage(FindDirectMessageRequest request, StreamObserver<Space> responseObserver)

Returns the existing direct message with the specified user. If no direct message space is found, returns a `404 NOT_FOUND` error. For an example, see [Find a direct message](https://docs.cloud.google.com/chat/api/guides/v1/spaces/find-direct-message). With [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), returns the direct message space between the specified user and the calling Chat app. With [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), returns the direct message space between the specified user and the authenticated user. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope:
    * `<https://www.googleapis.com/auth/chat.bot>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.spaces>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[FindDirectMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>`  
  
  
### findGroupChats(FindGroupChatsRequest request, StreamObserver<FindGroupChatsResponse> responseObserver)
    
    
    public void findGroupChats(FindGroupChatsRequest request, StreamObserver<FindGroupChatsResponse> responseObserver)

Returns all spaces with `spaceType == GROUP_CHAT`, whose human memberships contain exactly the calling user, and the users specified in `FindGroupChatsRequest.users`. Only members that have joined the conversation are supported. For an example, see [Find group chats](https://developers.google.com/workspace/chat/find-group-chats). If the calling user blocks, or is blocked by, some users, and no spaces with the entire specified set of users are found, this method returns spaces that don't include the blocked or blocking users. The specified set of users must contain only human (non-app) memberships. A request that contains non-human users doesn't return any spaces. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.memberships.readonly>`
  * `<https://www.googleapis.com/auth/chat.memberships>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[FindGroupChatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[FindGroupChatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsResponse)>`  
  
  
### getAttachment(GetAttachmentRequest request, StreamObserver<Attachment> responseObserver)
    
    
    public void getAttachment(GetAttachmentRequest request, StreamObserver<Attachment> responseObserver)

Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download). For an example, see [Get metadata about a message attachment](https://developers.google.com/workspace/chat/get-media-attachments). Requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.bot>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)>`  
  
  
### getAvailability(GetAvailabilityRequest request, StreamObserver<Availability> responseObserver)
    
    
    public void getAvailability(GetAvailabilityRequest request, StreamObserver<Availability> responseObserver)

Returns availability information for a human user in Google Chat. For example, this can be used to check if a user is online or away, or to retrieve their custom status message. This method only retrieves the authenticated user's availability. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.availability.readonly>`
  * `<https://www.googleapis.com/auth/chat.users.availability>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>`  
  
  
### getCustomEmoji(GetCustomEmojiRequest request, StreamObserver<CustomEmoji> responseObserver)
    
    
    public void getCustomEmoji(GetCustomEmojiRequest request, StreamObserver<CustomEmoji> responseObserver)

Returns details about a custom emoji. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.customemojis.readonly>`
  * `<https://www.googleapis.com/auth/chat.customemojis>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)>`  
  
  
### getMembership(GetMembershipRequest request, StreamObserver<Membership> responseObserver)
    
    
    public void getMembership(GetMembershipRequest request, StreamObserver<Membership> responseObserver)

Returns details about a membership. For an example, see [Get details about a user's or Google Chat app's membership](https://developers.google.com/workspace/chat/get-members). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.bot>`
    * `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.memberships.readonly>`
    * `<https://www.googleapis.com/auth/chat.memberships>`
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used:
      * `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>`
      * `<https://www.googleapis.com/auth/chat.admin.memberships>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>`  
  
  
### getMessage(GetMessageRequest request, StreamObserver<Message> responseObserver)
    
    
    public void getMessage(GetMessageRequest request, StreamObserver<Message> responseObserver)

Returns details about a message. For an example, see [Get details about a message](https://developers.google.com/workspace/chat/get-messages). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.bot>`: When using this authorization scope, this method returns details about a message the Chat app has access to, like direct messages and [slash commands](https://developers.google.com/workspace/chat/slash-commands) that invoke the Chat app.
    * `<https://www.googleapis.com/auth/chat.app.messages.readonly>` with [administrator approval](https://support.google.com/a?p=chat-app-auth). When using this authentication scope, this method returns details about a public message in a space.
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages>` Note: Might return a message from a blocked member or space.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>`  
  
  
### getSpace(GetSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public void getSpace(GetSpaceRequest request, StreamObserver<Space> responseObserver)

Returns details about a space. For an example, see [Get details about a space](https://developers.google.com/workspace/chat/get-spaces). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.bot>`
    * `<https://www.googleapis.com/auth/chat.app.spaces>` with [administrator approval](https://support.google.com/a?p=chat-app-auth)
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.spaces>`
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used:
      * `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>`
      * `<https://www.googleapis.com/auth/chat.admin.spaces>` App authentication has the following limitations:
  * `space.access_settings` is only populated when using the `chat.app.spaces` scope.
  * `space.predefind_permission_settings` and `space.permission_settings` are only populated when using the `chat.app.spaces` scope, and only for spaces the app created.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>`  
  
  
### getSpaceEvent(GetSpaceEventRequest request, StreamObserver<SpaceEvent> responseObserver)
    
    
    public void getSpaceEvent(GetSpaceEventRequest request, StreamObserver<SpaceEvent> responseObserver)

Returns an event from a Google Chat space. The [event payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the resource that changed. For example, if you request an event about a new message but the message was later updated, the server returns the updated `Message` resource in the event payload. Note: The `permissionSettings` field is not returned in the Space object of the Space event data for this request. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.app.spaces>`
    * `<https://www.googleapis.com/auth/chat.app.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.app.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.app.memberships>`
    * `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.spaces>`
    * `<https://www.googleapis.com/auth/chat.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages>`
    * `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages.reactions>`
    * `<https://www.googleapis.com/auth/chat.memberships.readonly>`
    * `<https://www.googleapis.com/auth/chat.memberships>` To get an event, the authenticated caller must be a member of the space. For an example, see [Get details about an event from a Google Chat space](https://developers.google.com/workspace/chat/get-space-event).



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpaceEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SpaceEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent)>`  
  
  
### getSpaceNotificationSetting(GetSpaceNotificationSettingRequest request, StreamObserver<SpaceNotificationSetting> responseObserver)
    
    
    public void getSpaceNotificationSetting(GetSpaceNotificationSettingRequest request, StreamObserver<SpaceNotificationSetting> responseObserver)

Gets the space notification setting. For an example, see [Get the caller's space notification setting](https://developers.google.com/workspace/chat/get-space-notification-setting). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.spacesettings>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)>`  
  
  
### getSpaceReadState(GetSpaceReadStateRequest request, StreamObserver<SpaceReadState> responseObserver)
    
    
    public void getSpaceReadState(GetSpaceReadStateRequest request, StreamObserver<SpaceReadState> responseObserver)

Returns details about a user's read state within a space, used to identify read and unread messages. For an example, see [Get details about a user's space read state](https://developers.google.com/workspace/chat/get-space-read-state). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.readstate.readonly>`
  * `<https://www.googleapis.com/auth/chat.users.readstate>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)>`  
  
  
### getThreadReadState(GetThreadReadStateRequest request, StreamObserver<ThreadReadState> responseObserver)
    
    
    public void getThreadReadState(GetThreadReadStateRequest request, StreamObserver<ThreadReadState> responseObserver)

Returns details about a user's read state within a thread, used to identify read and unread messages. For an example, see [Get details about a user's thread read state](https://developers.google.com/workspace/chat/get-thread-read-state). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.readstate.readonly>`
  * `<https://www.googleapis.com/auth/chat.users.readstate>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetThreadReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ThreadReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState)>`  
  
  
### listCustomEmojis(ListCustomEmojisRequest request, StreamObserver<ListCustomEmojisResponse> responseObserver)
    
    
    public void listCustomEmojis(ListCustomEmojisRequest request, StreamObserver<ListCustomEmojisResponse> responseObserver)

Lists custom emojis visible to the authenticated user. Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.customemojis.readonly>`
  * `<https://www.googleapis.com/auth/chat.customemojis>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListCustomEmojisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListCustomEmojisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisResponse)>`  
  
  
### listMemberships(ListMembershipsRequest request, StreamObserver<ListMembershipsResponse> responseObserver)
    
    
    public void listMemberships(ListMembershipsRequest request, StreamObserver<ListMembershipsResponse> responseObserver)

Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.bot>`
    * `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.memberships.readonly>`
    * `<https://www.googleapis.com/auth/chat.memberships>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used:
      * `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>`
      * `<https://www.googleapis.com/auth/chat.admin.memberships>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsResponse)>`  
  
  
### listMessagePins(ListMessagePinsRequest request, StreamObserver<ListMessagePinsResponse> responseObserver)
    
    
    public void listMessagePins(ListMessagePinsRequest request, StreamObserver<ListMessagePinsResponse> responseObserver)

Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>`
  * `<https://www.googleapis.com/auth/chat.spaces.pins>`
  * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
  * `<https://www.googleapis.com/auth/chat.spaces>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMessagePinsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMessagePinsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsResponse)>`  
  
  
### listMessages(ListMessagesRequest request, StreamObserver<ListMessagesResponse> responseObserver)
    
    
    public void listMessages(ListMessagesRequest request, StreamObserver<ListMessagesResponse> responseObserver)

Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope:
    * `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesResponse)>`  
  
  
### listReactions(ListReactionsRequest request, StreamObserver<ListReactionsResponse> responseObserver)
    
    
    public void listReactions(ListReactionsRequest request, StreamObserver<ListReactionsResponse> responseObserver)

Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>`
  * `<https://www.googleapis.com/auth/chat.messages.reactions>`
  * `<https://www.googleapis.com/auth/chat.messages.readonly>`
  * `<https://www.googleapis.com/auth/chat.messages>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReactionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListReactionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsResponse)>`  
  
  
### listSectionItems(ListSectionItemsRequest request, StreamObserver<ListSectionItemsResponse> responseObserver)
    
    
    public void listSectionItems(ListSectionItemsRequest request, StreamObserver<ListSectionItemsResponse> responseObserver)

Lists items in a section. Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`
  * `<https://www.googleapis.com/auth/chat.users.sections.readonly>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSectionItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSectionItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsResponse)>`  
  
  
### listSections(ListSectionsRequest request, StreamObserver<ListSectionsResponse> responseObserver)
    
    
    public void listSections(ListSectionsRequest request, StreamObserver<ListSectionsResponse> responseObserver)

Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`
  * `<https://www.googleapis.com/auth/chat.users.sections.readonly>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsResponse)>`  
  
  
### listSpaceEvents(ListSpaceEventsRequest request, StreamObserver<ListSpaceEventsResponse> responseObserver)
    
    
    public void listSpaceEvents(ListSpaceEventsRequest request, StreamObserver<ListSpaceEventsResponse> responseObserver)

Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.app.spaces>`
    * `<https://www.googleapis.com/auth/chat.app.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.app.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.app.memberships>`
    * `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.spaces>`
    * `<https://www.googleapis.com/auth/chat.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages>`
    * `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages.reactions>`
    * `<https://www.googleapis.com/auth/chat.memberships.readonly>`
    * `<https://www.googleapis.com/auth/chat.memberships>` To list events, the authenticated caller must be a member of the space. For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events).



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpaceEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSpaceEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsResponse)>`  
  
  
### listSpaces(ListSpacesRequest request, StreamObserver<ListSpacesResponse> responseObserver)
    
    
    public void listSpaces(ListSpacesRequest request, StreamObserver<ListSpacesResponse> responseObserver)

Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/workspace/chat/list-spaces). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope:
    * `<https://www.googleapis.com/auth/chat.bot>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.spaces>` To list all named spaces by Google Workspace organization, use the [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search) method using Workspace administrator privileges instead.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[ListSpacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesResponse)>`  
  
  
### markAsActive(MarkAsActiveRequest request, StreamObserver<Availability> responseObserver)
    
    
    public void markAsActive(MarkAsActiveRequest request, StreamObserver<Availability> responseObserver)

Marks user as `ACTIVE` in Google Chat. Sets the user's availability state to `ACTIVE`. The `ACTIVE` state lasts until the specified expiration, at which point the user's state becomes `AWAY`. Note that if the user is actively using Chat, the `ACTIVE` state duration may extend beyond the provided expiration. This method only updates the authenticated user's availability. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.availability>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkAsActiveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>`  
  
  
### markAsAway(MarkAsAwayRequest request, StreamObserver<Availability> responseObserver)
    
    
    public void markAsAway(MarkAsAwayRequest request, StreamObserver<Availability> responseObserver)

Marks user as `AWAY` in Google Chat. Sets the user's state to away and is not affected by the user's activity. This method only updates the authenticated user's availability. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.availability>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkAsAwayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>`  
  
  
### markAsDoNotDisturb(MarkAsDoNotDisturbRequest request, StreamObserver<Availability> responseObserver)
    
    
    public void markAsDoNotDisturb(MarkAsDoNotDisturbRequest request, StreamObserver<Availability> responseObserver)

Marks user as `DO_NOT_DISTURB` in Google Chat. Sets a user's availability state to `DO_NOT_DISTURB` until a specified expiration time. When in `DO_NOT_DISTURB`, users typically won't receive notifications. This method only updates the authenticated user's availability. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.availability>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[MarkAsDoNotDisturbRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>`  
  
  
### moveSectionItem(MoveSectionItemRequest request, StreamObserver<MoveSectionItemResponse> responseObserver)
    
    
    public void moveSectionItem(MoveSectionItemRequest request, StreamObserver<MoveSectionItemResponse> responseObserver)

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[MoveSectionItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)>`  
  
  
### positionSection(PositionSectionRequest request, StreamObserver<PositionSectionResponse> responseObserver)
    
    
    public void positionSection(PositionSectionRequest request, StreamObserver<PositionSectionResponse> responseObserver)

Changes the sort order of a section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[PositionSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[PositionSectionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponse)>`  
  
  
### searchMessages(SearchMessagesRequest request, StreamObserver<SearchMessagesResponse> responseObserver)
    
    
    public void searchMessages(SearchMessagesRequest request, StreamObserver<SearchMessagesResponse> responseObserver)

Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria. To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides. This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.

  * Private Messages that are visible to the authenticated user.
  * Messages posted by Chat apps in spaces or group chats.
  * Messages in a Chat app DM.
  * Messages from blocked users.
  * Messages in spaces that the caller has muted. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    * `<https://www.googleapis.com/auth/chat.messages.readonly>`
    * `<https://www.googleapis.com/auth/chat.messages>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesResponse)>`  
  
  
### searchSpaces(SearchSpacesRequest request, StreamObserver<SearchSpacesResponse> responseObserver)
    
    
    public void searchSpaces(SearchSpacesRequest request, StreamObserver<SearchSpacesResponse> responseObserver)

Returns a list of spaces in a Google Workspace organization. For an example, see [Search for and manage spaces](https://developers.google.com/workspace/chat/search-manage-admin). When `use_admin_access` is set to `false`, the results are limited to spaces where the calling user is a joined member. To search with administrator privileges, set `use_admin_access` to `true`. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.spaces>`
  * [User authentication with administrator privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges) and one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):
    * `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>`
    * `<https://www.googleapis.com/auth/chat.admin.spaces>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SearchSpacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse)>`  
  
  
### setUpSpace(SetUpSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public void setUpSpace(SetUpSpaceRequest request, StreamObserver<Space> responseObserver)

Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn't be specified as a membership in the request. For an example, see [Set up a space with initial members](https://developers.google.com/workspace/chat/set-up-spaces). To specify the human members to add, add memberships with the appropriate `membership.member.name`. To add a human user, use `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` for the person from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`. To specify the Google groups to add, add memberships with the appropriate `membership.group_member.name`. To add or invite a Google group, use `groups/{group}`, where `{group}` is the `id` for the group from the Cloud Identity Groups API. For example, you can use [Cloud Identity Groups lookup API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) to retrieve the ID `123456789` for group email `group@example.com`, then you can add the group to the space by setting the `membership.group_member.name` to `groups/123456789`. Group email is not supported, and Google groups can only be added as members in named spaces. For a named space or group chat, if the caller blocks, or is blocked by some members, or doesn't have permission to add some members, then those members aren't added to the created space. To create a direct message (DM) between the calling user and another human user, specify exactly one membership to represent the human user. If one user blocks the other, the request fails and the DM isn't created. To create a DM between the calling user and the calling app, set `Space.singleUserBotDm` to `true` and don't specify any memberships. You can only use this method to set up a DM with the calling app. To add the calling app as a member of a space or an existing DM between two human users, see [Invite or add a user or app to a space](https://developers.google.com/workspace/chat/create-members). If a DM already exists between two users, even when one user blocks the other at the time a request is made, then the existing DM is returned. Spaces with threaded replies aren't supported. If you receive the error message `ALREADY_EXISTS` when setting up a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.spaces.create>`
  * `<https://www.googleapis.com/auth/chat.spaces>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[SetUpSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>`  
  
  
### updateAvailability(UpdateAvailabilityRequest request, StreamObserver<Availability> responseObserver)
    
    
    public void updateAvailability(UpdateAvailabilityRequest request, StreamObserver<Availability> responseObserver)

Updates availability information for a human user. Only the `custom_status` field can be updated through this method. This method only updates the authenticated user's availability. Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.availability>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>`  
  
  
### updateMembership(UpdateMembershipRequest request, StreamObserver<Membership> responseObserver)
    
    
    public void updateMembership(UpdateMembershipRequest request, StreamObserver<Membership> responseObserver)

Updates a membership. For an example, see [Update a user's membership in a space](https://developers.google.com/workspace/chat/update-members). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope:
    * `<https://www.googleapis.com/auth/chat.app.memberships>` (only in spaces the app created)
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.memberships>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used:
      * `<https://www.googleapis.com/auth/chat.admin.memberships>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>`  
  
  
### updateMessage(UpdateMessageRequest request, StreamObserver<Message> responseObserver)
    
    
    public void updateMessage(UpdateMessageRequest request, StreamObserver<Message> responseObserver)

Updates a message. There's a difference between the `patch` and `update` methods. The `patch` method uses a `patch` request while the `update` method uses a `put` request. We recommend using the `patch` method. For an example, see [Update a message](https://developers.google.com/workspace/chat/update-messages). Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope:
    * `<https://www.googleapis.com/auth/chat.bot>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.messages>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) When using app authentication, requests can only update messages created by the calling Chat app.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>`  
  
  
### updateSection(UpdateSectionRequest request, StreamObserver<Section> responseObserver)
    
    
    public void updateSection(UpdateSectionRequest request, StreamObserver<Section> responseObserver)

Updates a section. Only sections of type `CUSTOM_SECTION` can be updated. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.sections>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)>`  
  
  
### updateSpace(UpdateSpaceRequest request, StreamObserver<Space> responseObserver)
    
    
    public void updateSpace(UpdateSpaceRequest request, StreamObserver<Space> responseObserver)

Updates a space. For an example, see [Update a space](https://developers.google.com/workspace/chat/update-spaces). If you're updating the `displayName` field and receive the error message `ALREADY_EXISTS`, try a different display name.. An existing space within the Google Workspace organization might already use this display name. Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

  * [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.app.spaces>`
  * [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes:
    * `<https://www.googleapis.com/auth/chat.spaces>`
    * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)
    * User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scopes is used:
      * `<https://www.googleapis.com/auth/chat.admin.spaces>` App authentication has the following limitations:
  * To update either `space.predefined_permission_settings` or `space.permission_settings`, the app must be the space creator.
  * Updating the `space.access_settings.audience` is not supported for app authentication.



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>`  
  
  
### updateSpaceNotificationSetting(UpdateSpaceNotificationSettingRequest request, StreamObserver<SpaceNotificationSetting> responseObserver)
    
    
    public void updateSpaceNotificationSetting(UpdateSpaceNotificationSettingRequest request, StreamObserver<SpaceNotificationSetting> responseObserver)

Updates the space notification setting. For an example, see [Update the caller's space notification setting](https://developers.google.com/workspace/chat/update-space-notification-setting). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.spacesettings>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)>`  
  
  
### updateSpaceReadState(UpdateSpaceReadStateRequest request, StreamObserver<SpaceReadState> responseObserver)
    
    
    public void updateSpaceReadState(UpdateSpaceReadStateRequest request, StreamObserver<SpaceReadState> responseObserver)

Updates a user's read state within a space, used to identify read and unread messages. For an example, see [Update a user's space read state](https://developers.google.com/workspace/chat/update-space-read-state). Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.users.readstate>`



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)>`  
  
  
### uploadAttachment(UploadAttachmentRequest request, StreamObserver<UploadAttachmentResponse> responseObserver)
    
    
    public void uploadAttachment(UploadAttachmentRequest request, StreamObserver<UploadAttachmentResponse> responseObserver)

Uploads an attachment. For an example, see [Upload media as a file attachment](https://developers.google.com/workspace/chat/upload-media-attachments). Requires user [authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

  * `<https://www.googleapis.com/auth/chat.messages.create>`
  * `<https://www.googleapis.com/auth/chat.messages>`
  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) You can upload attachments up to 200 MB. Certain file types aren't supported. For details, see [File types blocked by Google Chat](https://support.google.com/chat/answer/7651457?&co=GENIE.Platform%3DDesktop#File%20types%20blocked%20in%20Google%20Chat).



**Parameters**  
---  
**Name** | **Description**  
`request` | `[UploadAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequest)`  
  
`responseObserver` | `io.grpc.stub.StreamObserver<[UploadAttachmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponse)>`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
