---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient
title: Class ChatServiceClient (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:58.513659+00:00
---

# Class ChatServiceClient (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ChatServiceClient (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 

[GitHub Repository](https://github.com/googleapis/google-cloud-java/tree/main/java-chat/google-cloud-chat/src/main/java/com/google/chat/v1/ChatServiceClient.java)| [Product Reference](https://developers.google.com/chat/concepts)| [REST Documentation](https://developers.google.com/chat/api/reference/rest)  
---|---|---  
  
Service Description: Enables developers to build Chat apps and integrations on Google Chat Platform.

This class provides the ability to make remote calls to the backing service through method calls that map to API methods. Sample code to get started:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       Message message = Message.newBuilder().build();
       String messageId = "messageId-1440013438";
       Message response = chatServiceClient.createMessage(parent, message, messageId);
     }
     

Note: close() needs to be called on the ChatServiceClient object to clean up resources such as threads. In the example above, try-with-resources is used, which automatically calls close().

Methods Method | Description | Method Variants  
---|---|---  
CreateMessage |  Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)  Chat attributes the message sender differently depending on the type of authentication that you use in your request.  The following image shows how Chat attributes a message when you use app authentication. Chat displays the Chat app as the message sender. The content of the message can contain text (`text`), cards (`cardsV2`), and accessory widgets (`accessoryWidgets`).  ![Message sent with app authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg) The following image shows how Chat attributes a message when you use user authentication. Chat displays the user as the message sender and attributes the Chat app to the message by displaying its name. The content of message can only contain text (`text`).  ![Message sent with user authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg) The maximum message size, including the message contents, is 32,000 bytes.  For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMessage(CreateMessageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createMessage(SpaceName parent, Message message, String messageId) 
  * createMessage(String parent, Message message, String messageId) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMessageCallable() 

  
ListMessages |  Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope: - `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMessages(ListMessagesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMessages(SpaceName parent) 
  * listMessages(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMessagesPagedCallable() 
  * listMessagesCallable() 

  
ListMemberships |  Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMemberships(ListMembershipsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMemberships(SpaceName parent) 
  * listMemberships(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMembershipsPagedCallable() 
  * listMembershipsCallable() 

  
GetMembership |  Returns details about a membership. For an example, see [Get details about a user's or Google Chat app's membership](https://developers.google.com/workspace/chat/get-members).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMembership(GetMembershipRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMembership(MembershipName name) 
  * getMembership(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMembershipCallable() 

  
GetMessage |  Returns details about a message. For an example, see [Get details about a message](https://developers.google.com/workspace/chat/get-messages).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>`: When using this authorization scope, this method returns details about a message the Chat app has access to, like direct messages and [slash commands](https://developers.google.com/workspace/chat/slash-commands) that invoke the Chat app. - `<https://www.googleapis.com/auth/chat.app.messages.readonly>` with [administrator approval](https://support.google.com/a?p=chat-app-auth). When using this authentication scope, this method returns details about a public message in a space.  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` Note: Might return a message from a blocked member or space. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getMessage(GetMessageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getMessage(MessageName name) 
  * getMessage(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getMessageCallable() 

  
UpdateMessage |  Updates a message. There's a difference between the `patch` and `update` methods. The `patch` method uses a `patch` request while the `update` method uses a `put` request. We recommend using the `patch` method. For an example, see [Update a message](https://developers.google.com/workspace/chat/update-messages).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)  When using app authentication, requests can only update messages created by the calling Chat app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMessage(UpdateMessageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateMessage(Message message, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMessageCallable() 

  
DeleteMessage |  Deletes a message. For an example, see [Delete a message](https://developers.google.com/workspace/chat/delete-messages).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)  When using app authentication, requests can only delete messages created by the calling Chat app. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMessage(DeleteMessageRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteMessage(MessageName name) 
  * deleteMessage(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMessageCallable() 

  
SearchMessages |  Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria.  To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides.  This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.  \- Private Messages that are visible to the authenticated user. - Messages posted by Chat apps in spaces or group chats. - Messages in a Chat app DM. - Messages from blocked users. - Messages in spaces that the caller has muted.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchMessages(SearchMessagesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchMessages(SpaceName parent, String filter) 
  * searchMessages(String parent, String filter) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchMessagesPagedCallable() 
  * searchMessagesCallable() 

  
GetAttachment |  Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download). For an example, see [Get metadata about a message attachment](https://developers.google.com/workspace/chat/get-media-attachments).  Requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.bot>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAttachment(GetAttachmentRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAttachment(AttachmentName name) 
  * getAttachment(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAttachmentCallable() 

  
UploadAttachment |  Uploads an attachment. For an example, see [Upload media as a file attachment](https://developers.google.com/workspace/chat/upload-media-attachments).  Requires user [authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)  You can upload attachments up to 200 MB. Certain file types aren't supported. For details, see [File types blocked by Google Chat](https://support.google.com/chat/answer/7651457?&co=GENIE.Platform%3DDesktop#File%20types%20blocked%20in%20Google%20Chat). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * uploadAttachment(UploadAttachmentRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * uploadAttachmentCallable() 

  
ListSpaces |  Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/workspace/chat/list-spaces).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` To list all named spaces by Google Workspace organization, use the [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search) method using Workspace administrator privileges instead. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSpaces(ListSpacesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSpaces() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSpacesPagedCallable() 
  * listSpacesCallable() 

  
SearchSpaces |  Returns a list of spaces in a Google Workspace organization. For an example, see [Search for and manage spaces](https://developers.google.com/workspace/chat/search-manage-admin).  When `use_admin_access` is set to `false`, the results are limited to spaces where the calling user is a joined member. To search with administrator privileges, set `use_admin_access` to `true`.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- [User authentication with administrator privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges) and one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * searchSpaces(SearchSpacesRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * searchSpaces() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * searchSpacesPagedCallable() 
  * searchSpacesCallable() 

  
GetSpace |  Returns details about a space. For an example, see [Get details about a space](https://developers.google.com/workspace/chat/get-spaces).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.spaces>` with [administrator approval](https://support.google.com/a?p=chat-app-auth) \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>` App authentication has the following limitations:  \- `space.access_settings` is only populated when using the `chat.app.spaces` scope. - `space.predefind_permission_settings` and `space.permission_settings` are only populated when using the `chat.app.spaces` scope, and only for spaces the app created. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSpace(GetSpaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSpace(SpaceName name) 
  * getSpace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSpaceCallable() 

  
CreateSpace |  Creates a space. Can be used to create a named space, or a group chat in `Import mode`. For an example, see [Create a space](https://developers.google.com/workspace/chat/create-spaces).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces.create>` \- `<https://www.googleapis.com/auth/chat.app.spaces>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)  When authenticating as an app, the `space.customer` field must be set in the request.  When authenticating as an app, the Chat app is added as a member of the space. However, unlike human authentication, the Chat app is not added as a space manager. By default, the Chat app can be removed from the space by all space members. To allow only space managers to remove the app from a space, set `space.permission_settings.manage_apps` to `managers_allowed`.  Space membership upon creation depends on whether the space is created in `Import mode`: 

  * **Import mode:** No members are created. 
  * **All other modes:** The calling user is added as a member. This is: * The app itself when using app authentication. * The human user when using user authentication. 

If you receive the error message `ALREADY_EXISTS` when creating a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSpace(CreateSpaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSpace(Space space) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSpaceCallable() 

  
SetUpSpace |  Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn't be specified as a membership in the request. For an example, see [Set up a space with initial members](https://developers.google.com/workspace/chat/set-up-spaces).  To specify the human members to add, add memberships with the appropriate `membership.member.name`. To add a human user, use `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` for the person from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`.  To specify the Google groups to add, add memberships with the appropriate `membership.group_member.name`. To add or invite a Google group, use `groups/{group}`, where `{group}` is the `id` for the group from the Cloud Identity Groups API. For example, you can use [Cloud Identity Groups lookup API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) to retrieve the ID `123456789` for group email `group@example.com`, then you can add the group to the space by setting the `membership.group_member.name` to `groups/123456789`. Group email is not supported, and Google groups can only be added as members in named spaces.  For a named space or group chat, if the caller blocks, or is blocked by some members, or doesn't have permission to add some members, then those members aren't added to the created space.  To create a direct message (DM) between the calling user and another human user, specify exactly one membership to represent the human user. If one user blocks the other, the request fails and the DM isn't created.  To create a DM between the calling user and the calling app, set `Space.singleUserBotDm` to `true` and don't specify any memberships. You can only use this method to set up a DM with the calling app. To add the calling app as a member of a space or an existing DM between two human users, see [Invite or add a user or app to a space](https://developers.google.com/workspace/chat/create-members).  If a DM already exists between two users, even when one user blocks the other at the time a request is made, then the existing DM is returned.  Spaces with threaded replies aren't supported. If you receive the error message `ALREADY_EXISTS` when setting up a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * setUpSpace(SetUpSpaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * setUpSpaceCallable() 

  
UpdateSpace |  Updates a space. For an example, see [Update a space](https://developers.google.com/workspace/chat/update-spaces).  If you're updating the `displayName` field and receive the error message `ALREADY_EXISTS`, try a different display name.. An existing space within the Google Workspace organization might already use this display name.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces>` App authentication has the following limitations:  \- To update either `space.predefined_permission_settings` or `space.permission_settings`, the app must be the space creator. - Updating the `space.access_settings.audience` is not supported for app authentication. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSpace(UpdateSpaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSpace(Space space, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSpaceCallable() 

  
DeleteSpace |  Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see [Delete a space](https://developers.google.com/workspace/chat/delete-spaces).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.delete>` (only in spaces the app created)  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.delete>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.delete>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSpace(DeleteSpaceRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSpace(SpaceName name) 
  * deleteSpace(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSpaceCallable() 

  
CompleteImportSpace |  Completes the [import process](https://developers.google.com/workspace/chat/import-data) for the specified space and makes it visible to users.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and domain-wide delegation with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.import>` For more information, see [Authorize Google Chat apps to import data](https://developers.google.com/workspace/chat/authorize-import). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * completeImportSpace(CompleteImportSpaceRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * completeImportSpaceCallable() 

  
FindDirectMessage |  Returns the existing direct message with the specified user. If no direct message space is found, returns a `404 NOT_FOUND` error. For an example, see [Find a direct message](https://docs.cloud.google.com/chat/api/guides/v1/spaces/find-direct-message).  With [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), returns the direct message space between the specified user and the calling Chat app.  With [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), returns the direct message space between the specified user and the authenticated user.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * findDirectMessage(FindDirectMessageRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * findDirectMessageCallable() 

  
FindGroupChats |  Returns all spaces with `spaceType == GROUP_CHAT`, whose human memberships contain exactly the calling user, and the users specified in `FindGroupChatsRequest.users`. Only members that have joined the conversation are supported. For an example, see [Find group chats](https://developers.google.com/workspace/chat/find-group-chats).  If the calling user blocks, or is blocked by, some users, and no spaces with the entire specified set of users are found, this method returns spaces that don't include the blocked or blocking users.  The specified set of users must contain only human (non-app) memberships. A request that contains non-human users doesn't return any spaces.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * findGroupChats(FindGroupChatsRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * findGroupChatsPagedCallable() 
  * findGroupChatsCallable() 

  
CreateMembership |  Creates a membership for the calling Chat app, a user, or a Google Group. Creating memberships for other Chat apps isn't supported. When creating a membership, if the specified member has their auto-accept policy turned off, then they're invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to add the calling app to the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>` App authentication is not supported for the following use cases:  \- Inviting users external to the Workspace organization that owns the space. - Adding a Google Group to a space. - Adding a Chat app to a space.  For example usage, see:  \- [Invite or add a user to a space](https://developers.google.com/workspace/chat/create-members#create-user-membership). - [Invite or add a Google Group to a space](https://developers.google.com/workspace/chat/create-members#create-group-membership). - [Add the Chat app to a space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMembership(CreateMembershipRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createMembership(SpaceName parent, Membership membership) 
  * createMembership(String parent, Membership membership) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMembershipCallable() 

  
UpdateMembership |  Updates a membership. For an example, see [Update a user's membership in a space](https://developers.google.com/workspace/chat/update-members).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>` (only in spaces the app created)  \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateMembership(UpdateMembershipRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateMembership(Membership membership, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateMembershipCallable() 

  
DeleteMembership |  Deletes a membership. For an example, see [Remove a user or a Google Chat app from a space](https://developers.google.com/workspace/chat/delete-members).  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to remove the calling app from the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>` App authentication is not supported for the following use cases:  \- Removing a Google Group from a space. - Removing a Chat app from a space.  To delete memberships for space managers, the requester must be a space manager. If you're using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) the Chat app must be the space creator. |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMembership(DeleteMembershipRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteMembership(MembershipName name) 
  * deleteMembership(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMembershipCallable() 

  
CreateReaction |  Creates a reaction and adds it to a message. For an example, see [Add a reaction to a message](https://developers.google.com/workspace/chat/create-reactions).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.messages.reactions.create>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createReaction(CreateReactionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createReaction(MessageName parent, Reaction reaction) 
  * createReaction(String parent, Reaction reaction) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createReactionCallable() 

  
ListReactions |  Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listReactions(ListReactionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listReactions(MessageName parent) 
  * listReactions(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listReactionsPagedCallable() 
  * listReactionsCallable() 

  
DeleteReaction |  Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/workspace/chat/delete-reactions).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteReaction(DeleteReactionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteReaction(ReactionName name) 
  * deleteReaction(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteReactionCallable() 

  
ListMessagePins |  Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listMessagePins(ListMessagePinsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listMessagePins(SpaceName parent) 
  * listMessagePins(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listMessagePinsPagedCallable() 
  * listMessagePinsCallable() 

  
CreateMessagePin |  Creates a message pin.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createMessagePin(CreateMessagePinRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createMessagePin(SpaceName parent, MessagePin messagePin) 
  * createMessagePin(String parent, MessagePin messagePin) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createMessagePinCallable() 

  
DeleteMessagePin |  Deletes a message pin.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteMessagePin(DeleteMessagePinRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteMessagePin(MessagePinName name) 
  * deleteMessagePin(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteMessagePinCallable() 

  
CreateCustomEmoji |  Creates a custom emoji.  Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.customemojis>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createCustomEmoji(CreateCustomEmojiRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createCustomEmoji(CustomEmoji customEmoji) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createCustomEmojiCallable() 

  
GetCustomEmoji |  Returns details about a custom emoji.  Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getCustomEmoji(GetCustomEmojiRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getCustomEmoji(CustomEmojiName name) 
  * getCustomEmoji(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getCustomEmojiCallable() 

  
ListCustomEmojis |  Lists custom emojis visible to the authenticated user.  Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listCustomEmojis(ListCustomEmojisRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listCustomEmojis() 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listCustomEmojisPagedCallable() 
  * listCustomEmojisCallable() 

  
DeleteCustomEmoji |  Deletes a custom emoji. By default, users can only delete custom emoji they created. [Emoji managers](https://support.google.com/a/answer/12850085) assigned by the administrator can delete any custom emoji in the organization. See [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149).  Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.customemojis>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteCustomEmoji(DeleteCustomEmojiRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteCustomEmoji(CustomEmojiName name) 
  * deleteCustomEmoji(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteCustomEmojiCallable() 

  
GetSpaceReadState |  Returns details about a user's read state within a space, used to identify read and unread messages. For an example, see [Get details about a user's space read state](https://developers.google.com/workspace/chat/get-space-read-state).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSpaceReadState(GetSpaceReadStateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSpaceReadState(SpaceReadStateName name) 
  * getSpaceReadState(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSpaceReadStateCallable() 

  
UpdateSpaceReadState |  Updates a user's read state within a space, used to identify read and unread messages. For an example, see [Update a user's space read state](https://developers.google.com/workspace/chat/update-space-read-state).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.readstate>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSpaceReadState(UpdateSpaceReadStateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSpaceReadState(SpaceReadState spaceReadState, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSpaceReadStateCallable() 

  
GetThreadReadState |  Returns details about a user's read state within a thread, used to identify read and unread messages. For an example, see [Get details about a user's thread read state](https://developers.google.com/workspace/chat/get-thread-read-state).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getThreadReadState(GetThreadReadStateRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getThreadReadState(ThreadReadStateName name) 
  * getThreadReadState(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getThreadReadStateCallable() 

  
GetAvailability |  Returns availability information for a human user in Google Chat. For example, this can be used to check if a user is online or away, or to retrieve their custom status message.  This method only retrieves the authenticated user's availability.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.availability.readonly>` \- `<https://www.googleapis.com/auth/chat.users.availability>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getAvailability(GetAvailabilityRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getAvailability(AvailabilityName name) 
  * getAvailability(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getAvailabilityCallable() 

  
MarkAsActive |  Marks user as `ACTIVE` in Google Chat.  Sets the user's availability state to `ACTIVE`. The `ACTIVE` state lasts until the specified expiration, at which point the user's state becomes `AWAY`. Note that if the user is actively using Chat, the `ACTIVE` state duration may extend beyond the provided expiration.  This method only updates the authenticated user's availability.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.availability>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markAsActive(MarkAsActiveRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markAsActiveCallable() 

  
MarkAsAway |  Marks user as `AWAY` in Google Chat.  Sets the user's state to away and is not affected by the user's activity.  This method only updates the authenticated user's availability.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.availability>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markAsAway(MarkAsAwayRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markAsAwayCallable() 

  
MarkAsDoNotDisturb |  Marks user as `DO_NOT_DISTURB` in Google Chat.  Sets a user's availability state to `DO_NOT_DISTURB` until a specified expiration time. When in `DO_NOT_DISTURB`, users typically won't receive notifications.  This method only updates the authenticated user's availability.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.availability>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * markAsDoNotDisturb(MarkAsDoNotDisturbRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * markAsDoNotDisturbCallable() 

  
UpdateAvailability |  Updates availability information for a human user. Only the `custom_status` field can be updated through this method.  This method only updates the authenticated user's availability.  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.availability>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateAvailability(UpdateAvailabilityRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateAvailability(Availability availability, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateAvailabilityCallable() 

  
GetSpaceEvent |  Returns an event from a Google Chat space. The [event payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the resource that changed. For example, if you request an event about a new message but the message was later updated, the server returns the updated `Message` resource in the event payload.  Note: The `permissionSettings` field is not returned in the Space object of the Space event data for this request.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` To get an event, the authenticated caller must be a member of the space.  For an example, see [Get details about an event from a Google Chat space](https://developers.google.com/workspace/chat/get-space-event). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSpaceEvent(GetSpaceEventRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSpaceEvent(SpaceEventName name) 
  * getSpaceEvent(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSpaceEventCallable() 

  
ListSpaceEvents |  Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource.  Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:  \- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` To list events, the authenticated caller must be a member of the space.  For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events). |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSpaceEvents(ListSpaceEventsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSpaceEvents(SpaceName parent, String filter) 
  * listSpaceEvents(String parent, String filter) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSpaceEventsPagedCallable() 
  * listSpaceEventsCallable() 

  
GetSpaceNotificationSetting |  Gets the space notification setting. For an example, see [Get the caller's space notification setting](https://developers.google.com/workspace/chat/get-space-notification-setting).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.spacesettings>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * getSpaceNotificationSetting(GetSpaceNotificationSettingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * getSpaceNotificationSetting(SpaceNotificationSettingName name) 
  * getSpaceNotificationSetting(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * getSpaceNotificationSettingCallable() 

  
UpdateSpaceNotificationSetting |  Updates the space notification setting. For an example, see [Update the caller's space notification setting](https://developers.google.com/workspace/chat/update-space-notification-setting).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.spacesettings>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSpaceNotificationSetting(UpdateSpaceNotificationSettingRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSpaceNotificationSetting(SpaceNotificationSetting spaceNotificationSetting, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSpaceNotificationSettingCallable() 

  
CreateSection |  Creates a section in Google Chat. Sections help users group conversations and customize the list of spaces displayed in Chat navigation panel. Only sections of type `CUSTOM_SECTION` can be created. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * createSection(CreateSectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * createSection(UserName parent, Section section) 
  * createSection(String parent, Section section) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * createSectionCallable() 

  
DeleteSection |  Deletes a section of type `CUSTOM_SECTION`.  If the section contains items, such as spaces, the items are moved to Google Chat's default sections and are not deleted.  For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * deleteSection(DeleteSectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * deleteSection(SectionName name) 
  * deleteSection(String name) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * deleteSectionCallable() 

  
UpdateSection |  Updates a section. Only sections of type `CUSTOM_SECTION` can be updated. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * updateSection(UpdateSectionRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * updateSection(Section section, FieldMask updateMask) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * updateSectionCallable() 

  
ListSections |  Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSections(ListSectionsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSections(UserName parent) 
  * listSections(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSectionsPagedCallable() 
  * listSectionsCallable() 

  
PositionSection |  Changes the sort order of a section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * positionSection(PositionSectionRequest request) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * positionSectionCallable() 

  
ListSectionItems |  Lists items in a section.  Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * listSectionItems(ListSectionItemsRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * listSectionItems(SectionName parent) 
  * listSectionItems(String parent) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * listSectionItemsPagedCallable() 
  * listSectionItemsCallable() 

  
MoveSectionItem |  Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).  Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):  \- `<https://www.googleapis.com/auth/chat.users.sections>` |  Request object method variants only take one parameter, a request object, which must be constructed before the call.

  * moveSectionItem(MoveSectionItemRequest request) 

"Flattened" method variants have converted the fields of the request object into function parameters to enable multiple ways to call the same method.

  * moveSectionItem(SectionItemName name, SectionName targetSection) 
  * moveSectionItem(SectionItemName name, String targetSection) 
  * moveSectionItem(String name, SectionName targetSection) 
  * moveSectionItem(String name, String targetSection) 

Callable method variants take no parameters and return an immutable API callable object, which can be used to initiate calls to the service.

  * moveSectionItemCallable() 

  
  
See the individual methods for example code.

Many parameters require resource names to be formatted in a particular way. To assist with these names, this class includes a format method for each type of name, and additionally a parse method to extract the individual identifiers contained within names that are returned.

This class can be customized by passing in a custom instance of ChatServiceSettings to create(). For example:

To customize credentials:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ChatServiceSettings chatServiceSettings =
         ChatServiceSettings.newBuilder()
             .setCredentialsProvider(FixedCredentialsProvider.create(myCredentials))
             .build();
     ChatServiceClient chatServiceClient = ChatServiceClient.create(chatServiceSettings);
     

To customize the endpoint:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ChatServiceSettings chatServiceSettings =
         ChatServiceSettings.newBuilder().setEndpoint(myEndpoint).build();
     ChatServiceClient chatServiceClient = ChatServiceClient.create(chatServiceSettings);
     

To use REST (HTTP1.1/JSON) transport (instead of gRPC) for sending and receiving requests over the wire:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     ChatServiceSettings chatServiceSettings = ChatServiceSettings.newHttpJsonBuilder().build();
     ChatServiceClient chatServiceClient = ChatServiceClient.create(chatServiceSettings);
     

Please refer to the GitHub repository's samples for more quickstart code snippets.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ChatServiceClient

## Static Methods 

### create()
    
    
    public static final ChatServiceClient create()

Constructs an instance of ChatServiceClient with default settings.

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ChatServiceSettings settings)
    
    
    public static final ChatServiceClient create(ChatServiceSettings settings)

Constructs an instance of ChatServiceClient, using the given settings. The channels are created based on the settings passed in, or defaults for any settings that are not set.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ChatServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceSettings)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
### create(ChatServiceStub stub)
    
    
    public static final ChatServiceClient create(ChatServiceStub stub)

Constructs an instance of ChatServiceClient, using the given stub for making calls. This is for advanced usage - prefer using create(ChatServiceSettings).

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ChatServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStub)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient)` |   
  
## Constructors 

### ChatServiceClient(ChatServiceSettings settings)
    
    
    protected ChatServiceClient(ChatServiceSettings settings)

Constructs an instance of ChatServiceClient, using the given settings. This is protected so that it is easy to make a subclass, but otherwise, the static factory methods should be preferred.

**Parameter**  
---  
**Name** | **Description**  
`settings` | `[ChatServiceSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceSettings)`  
  
  
### ChatServiceClient(ChatServiceStub stub)
    
    
    protected ChatServiceClient(ChatServiceStub stub)

**Parameter**  
---  
**Name** | **Description**  
`stub` | `[ChatServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStub)`  
  
  
## Methods 

### awaitTermination(long duration, TimeUnit unit)
    
    
    public boolean awaitTermination(long duration, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`duration` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### close()
    
    
    public final void close()

### completeImportSpace(CompleteImportSpaceRequest request)
    
    
    public final CompleteImportSpaceResponse completeImportSpace(CompleteImportSpaceRequest request)

Completes the [import process](https://developers.google.com/workspace/chat/import-data) for the specified space and makes it visible to users.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and domain-wide delegation with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.import>`

For more information, see [Authorize Google Chat apps to import data](https://developers.google.com/workspace/chat/authorize-import).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CompleteImportSpaceRequest request =
           CompleteImportSpaceRequest.newBuilder()
               .setName(SpaceName.of("[SPACE]").toString())
               .build();
       CompleteImportSpaceResponse response = chatServiceClient.completeImportSpace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CompleteImportSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CompleteImportSpaceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponse)` |   
  
### completeImportSpaceCallable()
    
    
    public final UnaryCallable<CompleteImportSpaceRequest,CompleteImportSpaceResponse> completeImportSpaceCallable()

Completes the [import process](https://developers.google.com/workspace/chat/import-data) for the specified space and makes it visible to users.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and domain-wide delegation with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.import>`

For more information, see [Authorize Google Chat apps to import data](https://developers.google.com/workspace/chat/authorize-import).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CompleteImportSpaceRequest request =
           CompleteImportSpaceRequest.newBuilder()
               .setName(SpaceName.of("[SPACE]").toString())
               .build();
       ApiFuture<CompleteImportSpaceResponse> future =
           chatServiceClient.completeImportSpaceCallable().futureCall(request);
       // Do something.
       CompleteImportSpaceResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CompleteImportSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceRequest),[CompleteImportSpaceResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CompleteImportSpaceResponse)>` |   
  
### createCustomEmoji(CreateCustomEmojiRequest request)
    
    
    public final CustomEmoji createCustomEmoji(CreateCustomEmojiRequest request)

Creates a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateCustomEmojiRequest request =
           CreateCustomEmojiRequest.newBuilder()
               .setCustomEmoji(CustomEmoji.newBuilder().build())
               .build();
       CustomEmoji response = chatServiceClient.createCustomEmoji(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)` |   
  
### createCustomEmoji(CustomEmoji customEmoji)
    
    
    public final CustomEmoji createCustomEmoji(CustomEmoji customEmoji)

Creates a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CustomEmoji customEmoji = CustomEmoji.newBuilder().build();
       CustomEmoji response = chatServiceClient.createCustomEmoji(customEmoji);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`customEmoji` | `[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)`  
Required. The custom emoji to create.  
**Returns**  
---  
**Type** | **Description**  
`[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)` |   
  
### createCustomEmojiCallable()
    
    
    public final UnaryCallable<CreateCustomEmojiRequest,CustomEmoji> createCustomEmojiCallable()

Creates a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateCustomEmojiRequest request =
           CreateCustomEmojiRequest.newBuilder()
               .setCustomEmoji(CustomEmoji.newBuilder().build())
               .build();
       ApiFuture<CustomEmoji> future =
           chatServiceClient.createCustomEmojiCallable().futureCall(request);
       // Do something.
       CustomEmoji response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateCustomEmojiRequest),[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)>` |   
  
### createMembership(@Nullable SpaceName parent, Membership membership)
    
    
    public final Membership createMembership(@Nullable SpaceName parent, Membership membership)

Creates a membership for the calling Chat app, a user, or a Google Group. Creating memberships for other Chat apps isn't supported. When creating a membership, if the specified member has their auto-accept policy turned off, then they're invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to add the calling app to the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Inviting users external to the Workspace organization that owns the space. - Adding a Google Group to a space. - Adding a Chat app to a space.

For example usage, see:

\- [Invite or add a user to a space](https://developers.google.com/workspace/chat/create-members#create-user-membership). - [Invite or add a Google Group to a space](https://developers.google.com/workspace/chat/create-members#create-group-membership). - [Add the Chat app to a space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       Membership membership = Membership.newBuilder().build();
       Membership response = chatServiceClient.createMembership(parent, membership);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The resource name of the space for which to create the membership. Format: spaces/{space}  
`membership` | `[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)`  
Required. The membership relation to create. The `memberType` field must contain a user with the `user.name` and `user.type` fields populated. The server will assign a resource name and overwrite anything specified. When a Chat app creates a membership relation for a human user, it must use certain authorization scopes and set specific values for certain fields: \- When [authenticating as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the `chat.memberships` authorization scope is required. \- When [authenticating as an app](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), the `chat.app.memberships` authorization scope is required. \- Set `user.type` to `HUMAN`, and set `user.name` with format `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` of the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`. Inviting users external to the Workspace organization that owns the space requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user). When a Chat app creates a membership relation for itself, it must [authenticate as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and use the `chat.memberships.app` scope, set `user.type` to `BOT`, and set `user.name` to `users/app`.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### createMembership(CreateMembershipRequest request)
    
    
    public final Membership createMembership(CreateMembershipRequest request)

Creates a membership for the calling Chat app, a user, or a Google Group. Creating memberships for other Chat apps isn't supported. When creating a membership, if the specified member has their auto-accept policy turned off, then they're invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to add the calling app to the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Inviting users external to the Workspace organization that owns the space. - Adding a Google Group to a space. - Adding a Chat app to a space.

For example usage, see:

\- [Invite or add a user to a space](https://developers.google.com/workspace/chat/create-members#create-user-membership). - [Invite or add a Google Group to a space](https://developers.google.com/workspace/chat/create-members#create-group-membership). - [Add the Chat app to a space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateMembershipRequest request =
           CreateMembershipRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setMembership(Membership.newBuilder().build())
               .setUseAdminAccess(true)
               .build();
       Membership response = chatServiceClient.createMembership(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### createMembership(String parent, Membership membership)
    
    
    public final Membership createMembership(String parent, Membership membership)

Creates a membership for the calling Chat app, a user, or a Google Group. Creating memberships for other Chat apps isn't supported. When creating a membership, if the specified member has their auto-accept policy turned off, then they're invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to add the calling app to the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Inviting users external to the Workspace organization that owns the space. - Adding a Google Group to a space. - Adding a Chat app to a space.

For example usage, see:

\- [Invite or add a user to a space](https://developers.google.com/workspace/chat/create-members#create-user-membership). - [Invite or add a Google Group to a space](https://developers.google.com/workspace/chat/create-members#create-group-membership). - [Add the Chat app to a space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       Membership membership = Membership.newBuilder().build();
       Membership response = chatServiceClient.createMembership(parent, membership);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the space for which to create the membership. Format: spaces/{space}  
`membership` | `[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)`  
Required. The membership relation to create. The `memberType` field must contain a user with the `user.name` and `user.type` fields populated. The server will assign a resource name and overwrite anything specified. When a Chat app creates a membership relation for a human user, it must use certain authorization scopes and set specific values for certain fields: \- When [authenticating as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the `chat.memberships` authorization scope is required. \- When [authenticating as an app](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), the `chat.app.memberships` authorization scope is required. \- Set `user.type` to `HUMAN`, and set `user.name` with format `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` of the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`. Inviting users external to the Workspace organization that owns the space requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user). When a Chat app creates a membership relation for itself, it must [authenticate as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and use the `chat.memberships.app` scope, set `user.type` to `BOT`, and set `user.name` to `users/app`.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### createMembershipCallable()
    
    
    public final UnaryCallable<CreateMembershipRequest,Membership> createMembershipCallable()

Creates a membership for the calling Chat app, a user, or a Google Group. Creating memberships for other Chat apps isn't supported. When creating a membership, if the specified member has their auto-accept policy turned off, then they're invited, and must accept the space invitation before joining. Otherwise, creating a membership adds the member directly to the specified space.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to add the calling app to the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Inviting users external to the Workspace organization that owns the space. - Adding a Google Group to a space. - Adding a Chat app to a space.

For example usage, see:

\- [Invite or add a user to a space](https://developers.google.com/workspace/chat/create-members#create-user-membership). - [Invite or add a Google Group to a space](https://developers.google.com/workspace/chat/create-members#create-group-membership). - [Add the Chat app to a space](https://developers.google.com/workspace/chat/create-members#create-membership-calling-api).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateMembershipRequest request =
           CreateMembershipRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setMembership(Membership.newBuilder().build())
               .setUseAdminAccess(true)
               .build();
       ApiFuture<Membership> future =
           chatServiceClient.createMembershipCallable().futureCall(request);
       // Do something.
       Membership response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### createMessage(@Nullable SpaceName parent, Message message, String messageId)
    
    
    public final Message createMessage(@Nullable SpaceName parent, Message message, String messageId)

Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Chat attributes the message sender differently depending on the type of authentication that you use in your request.

The following image shows how Chat attributes a message when you use app authentication. Chat displays the Chat app as the message sender. The content of the message can contain text (`text`), cards (`cardsV2`), and accessory widgets (`accessoryWidgets`).

![Message sent with app authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg)

The following image shows how Chat attributes a message when you use user authentication. Chat displays the user as the message sender and attributes the Chat app to the message by displaying its name. The content of message can only contain text (`text`).

![Message sent with user authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg)

The maximum message size, including the message contents, is 32,000 bytes.

For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       Message message = Message.newBuilder().build();
       String messageId = "messageId-1440013438";
       Message response = chatServiceClient.createMessage(parent, message, messageId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The resource name of the space in which to create a message. Format: `spaces/{space}`  
`message` | `[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)`  
Required. Message body.  
`messageId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. A custom ID for a message. Lets Chat apps get, update, or delete a message without needing to store the system-assigned ID in the message's resource name (represented in the message `name` field). The value for this field must meet the following requirements: 

  * Begins with `client-`. For example, `client-custom-name` is a valid custom ID, but `custom-name` is not. 
  * Contains up to 63 characters and only lowercase letters, numbers, and hyphens. 
  * Is unique within a space. A Chat app can't use the same custom ID for different messages. 

For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### createMessage(CreateMessageRequest request)
    
    
    public final Message createMessage(CreateMessageRequest request)

Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Chat attributes the message sender differently depending on the type of authentication that you use in your request.

The following image shows how Chat attributes a message when you use app authentication. Chat displays the Chat app as the message sender. The content of the message can contain text (`text`), cards (`cardsV2`), and accessory widgets (`accessoryWidgets`).

![Message sent with app authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg)

The following image shows how Chat attributes a message when you use user authentication. Chat displays the user as the message sender and attributes the Chat app to the message by displaying its name. The content of message can only contain text (`text`).

![Message sent with user authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg)

The maximum message size, including the message contents, is 32,000 bytes.

For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateMessageRequest request =
           CreateMessageRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setMessage(Message.newBuilder().build())
               .setThreadKey("threadKey-1562254347")
               .setRequestId("requestId693933066")
               .setMessageId("messageId-1440013438")
               .setCreateMessageNotificationOptions(
                   CreateMessageNotificationOptions.newBuilder().build())
               .build();
       Message response = chatServiceClient.createMessage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### createMessage(String parent, Message message, String messageId)
    
    
    public final Message createMessage(String parent, Message message, String messageId)

Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Chat attributes the message sender differently depending on the type of authentication that you use in your request.

The following image shows how Chat attributes a message when you use app authentication. Chat displays the Chat app as the message sender. The content of the message can contain text (`text`), cards (`cardsV2`), and accessory widgets (`accessoryWidgets`).

![Message sent with app authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg)

The following image shows how Chat attributes a message when you use user authentication. Chat displays the user as the message sender and attributes the Chat app to the message by displaying its name. The content of message can only contain text (`text`).

![Message sent with user authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg)

The maximum message size, including the message contents, is 32,000 bytes.

For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       Message message = Message.newBuilder().build();
       String messageId = "messageId-1440013438";
       Message response = chatServiceClient.createMessage(parent, message, messageId);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the space in which to create a message. Format: `spaces/{space}`  
`message` | `[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)`  
Required. Message body.  
`messageId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Optional. A custom ID for a message. Lets Chat apps get, update, or delete a message without needing to store the system-assigned ID in the message's resource name (represented in the message `name` field). The value for this field must meet the following requirements: 

  * Begins with `client-`. For example, `client-custom-name` is a valid custom ID, but `custom-name` is not. 
  * Contains up to 63 characters and only lowercase letters, numbers, and hyphens. 
  * Is unique within a space. A Chat app can't use the same custom ID for different messages. 

For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### createMessageCallable()
    
    
    public final UnaryCallable<CreateMessageRequest,Message> createMessageCallable()

Creates a message in a Google Chat space. For an example, see [Send a message](https://developers.google.com/workspace/chat/create-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>` \- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Chat attributes the message sender differently depending on the type of authentication that you use in your request.

The following image shows how Chat attributes a message when you use app authentication. Chat displays the Chat app as the message sender. The content of the message can contain text (`text`), cards (`cardsV2`), and accessory widgets (`accessoryWidgets`).

![Message sent with app authentication](https://developers.google.com/workspace/chat/images/message-app-auth.svg)

The following image shows how Chat attributes a message when you use user authentication. Chat displays the user as the message sender and attributes the Chat app to the message by displaying its name. The content of message can only contain text (`text`).

![Message sent with user authentication](https://developers.google.com/workspace/chat/images/message-user-auth.svg)

The maximum message size, including the message contents, is 32,000 bytes.

For [webhook](https://developers.google.com/workspace/chat/quickstart/webhooks) requests, the response doesn't contain the full message. The response only populates the `name` and `thread.name` fields in addition to the information that was in the request.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateMessageRequest request =
           CreateMessageRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setMessage(Message.newBuilder().build())
               .setThreadKey("threadKey-1562254347")
               .setRequestId("requestId693933066")
               .setMessageId("messageId-1440013438")
               .setCreateMessageNotificationOptions(
                   CreateMessageNotificationOptions.newBuilder().build())
               .build();
       ApiFuture<Message> future = chatServiceClient.createMessageCallable().futureCall(request);
       // Do something.
       Message response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessageRequest),[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>` |   
  
### createMessagePin(@Nullable SpaceName parent, MessagePin messagePin)
    
    
    public final MessagePin createMessagePin(@Nullable SpaceName parent, MessagePin messagePin)

Creates a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       MessagePin messagePin = MessagePin.newBuilder().build();
       MessagePin response = chatServiceClient.createMessagePin(parent, messagePin);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The parent space in which to create the message pin. Format: spaces/{space}  
`messagePin` | `[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)`  
Required. The MessagePin to create.  
**Returns**  
---  
**Type** | **Description**  
`[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)` |   
  
### createMessagePin(CreateMessagePinRequest request)
    
    
    public final MessagePin createMessagePin(CreateMessagePinRequest request)

Creates a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateMessagePinRequest request =
           CreateMessagePinRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setMessagePin(MessagePin.newBuilder().build())
               .build();
       MessagePin response = chatServiceClient.createMessagePin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)` |   
  
### createMessagePin(String parent, MessagePin messagePin)
    
    
    public final MessagePin createMessagePin(String parent, MessagePin messagePin)

Creates a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       MessagePin messagePin = MessagePin.newBuilder().build();
       MessagePin response = chatServiceClient.createMessagePin(parent, messagePin);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent space in which to create the message pin. Format: spaces/{space}  
`messagePin` | `[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)`  
Required. The MessagePin to create.  
**Returns**  
---  
**Type** | **Description**  
`[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)` |   
  
### createMessagePinCallable()
    
    
    public final UnaryCallable<CreateMessagePinRequest,MessagePin> createMessagePinCallable()

Creates a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateMessagePinRequest request =
           CreateMessagePinRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setMessagePin(MessagePin.newBuilder().build())
               .build();
       ApiFuture<MessagePin> future =
           chatServiceClient.createMessagePinCallable().futureCall(request);
       // Do something.
       MessagePin response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateMessagePinRequest),[MessagePin](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MessagePin)>` |   
  
### createReaction(@Nullable MessageName parent, Reaction reaction)
    
    
    public final Reaction createReaction(@Nullable MessageName parent, Reaction reaction)

Creates a reaction and adds it to a message. For an example, see [Add a reaction to a message](https://developers.google.com/workspace/chat/create-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.create>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MessageName parent = MessageName.of("[SPACE]", "[MESSAGE]");
       Reaction reaction = Reaction.newBuilder().build();
       Reaction response = chatServiceClient.createReaction(parent, reaction);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MessageName`  
Required. The message where the reaction is created. Format: `spaces/{space}/messages/{message}`  
`reaction` | `[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)`  
Required. The reaction to create.  
**Returns**  
---  
**Type** | **Description**  
`[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)` |   
  
### createReaction(CreateReactionRequest request)
    
    
    public final Reaction createReaction(CreateReactionRequest request)

Creates a reaction and adds it to a message. For an example, see [Add a reaction to a message](https://developers.google.com/workspace/chat/create-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.create>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateReactionRequest request =
           CreateReactionRequest.newBuilder()
               .setParent(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setReaction(Reaction.newBuilder().build())
               .build();
       Reaction response = chatServiceClient.createReaction(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)` |   
  
### createReaction(String parent, Reaction reaction)
    
    
    public final Reaction createReaction(String parent, Reaction reaction)

Creates a reaction and adds it to a message. For an example, see [Add a reaction to a message](https://developers.google.com/workspace/chat/create-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.create>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = MessageName.of("[SPACE]", "[MESSAGE]").toString();
       Reaction reaction = Reaction.newBuilder().build();
       Reaction response = chatServiceClient.createReaction(parent, reaction);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The message where the reaction is created. Format: `spaces/{space}/messages/{message}`  
`reaction` | `[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)`  
Required. The reaction to create.  
**Returns**  
---  
**Type** | **Description**  
`[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)` |   
  
### createReactionCallable()
    
    
    public final UnaryCallable<CreateReactionRequest,Reaction> createReactionCallable()

Creates a reaction and adds it to a message. For an example, see [Add a reaction to a message](https://developers.google.com/workspace/chat/create-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.create>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateReactionRequest request =
           CreateReactionRequest.newBuilder()
               .setParent(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setReaction(Reaction.newBuilder().build())
               .build();
       ApiFuture<Reaction> future = chatServiceClient.createReactionCallable().futureCall(request);
       // Do something.
       Reaction response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateReactionRequest),[Reaction](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Reaction)>` |   
  
### createSection(@Nullable UserName parent, Section section)
    
    
    public final Section createSection(@Nullable UserName parent, Section section)

Creates a section in Google Chat. Sections help users group conversations and customize the list of spaces displayed in Chat navigation panel. Only sections of type `CUSTOM_SECTION` can be created. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UserName parent = UserName.of("[USER]");
       Section section = Section.newBuilder().build();
       Section response = chatServiceClient.createSection(parent, section);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.UserName`  
Required. The parent resource name where the section is created. Format: `users/{user}`  
`section` | `[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)`  
Required. The section to create.  
**Returns**  
---  
**Type** | **Description**  
`[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)` |   
  
### createSection(CreateSectionRequest request)
    
    
    public final Section createSection(CreateSectionRequest request)

Creates a section in Google Chat. Sections help users group conversations and customize the list of spaces displayed in Chat navigation panel. Only sections of type `CUSTOM_SECTION` can be created. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateSectionRequest request =
           CreateSectionRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setSection(Section.newBuilder().build())
               .build();
       Section response = chatServiceClient.createSection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)` |   
  
### createSection(String parent, Section section)
    
    
    public final Section createSection(String parent, Section section)

Creates a section in Google Chat. Sections help users group conversations and customize the list of spaces displayed in Chat navigation panel. Only sections of type `CUSTOM_SECTION` can be created. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = UserName.of("[USER]").toString();
       Section section = Section.newBuilder().build();
       Section response = chatServiceClient.createSection(parent, section);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent resource name where the section is created. Format: `users/{user}`  
`section` | `[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)`  
Required. The section to create.  
**Returns**  
---  
**Type** | **Description**  
`[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)` |   
  
### createSectionCallable()
    
    
    public final UnaryCallable<CreateSectionRequest,Section> createSectionCallable()

Creates a section in Google Chat. Sections help users group conversations and customize the list of spaces displayed in Chat navigation panel. Only sections of type `CUSTOM_SECTION` can be created. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateSectionRequest request =
           CreateSectionRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setSection(Section.newBuilder().build())
               .build();
       ApiFuture<Section> future = chatServiceClient.createSectionCallable().futureCall(request);
       // Do something.
       Section response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSectionRequest),[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)>` |   
  
### createSpace(CreateSpaceRequest request)
    
    
    public final Space createSpace(CreateSpaceRequest request)

Creates a space. Can be used to create a named space, or a group chat in `Import mode`. For an example, see [Create a space](https://developers.google.com/workspace/chat/create-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces.create>` \- `<https://www.googleapis.com/auth/chat.app.spaces>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When authenticating as an app, the `space.customer` field must be set in the request.

When authenticating as an app, the Chat app is added as a member of the space. However, unlike human authentication, the Chat app is not added as a space manager. By default, the Chat app can be removed from the space by all space members. To allow only space managers to remove the app from a space, set `space.permission_settings.manage_apps` to `managers_allowed`.

Space membership upon creation depends on whether the space is created in `Import mode`:

  * **Import mode:** No members are created. 
  * **All other modes:** The calling user is added as a member. This is: * The app itself when using app authentication. * The human user when using user authentication. 



If you receive the error message `ALREADY_EXISTS` when creating a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateSpaceRequest request =
           CreateSpaceRequest.newBuilder()
               .setSpace(Space.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       Space response = chatServiceClient.createSpace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[CreateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### createSpace(Space space)
    
    
    public final Space createSpace(Space space)

Creates a space. Can be used to create a named space, or a group chat in `Import mode`. For an example, see [Create a space](https://developers.google.com/workspace/chat/create-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces.create>` \- `<https://www.googleapis.com/auth/chat.app.spaces>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When authenticating as an app, the `space.customer` field must be set in the request.

When authenticating as an app, the Chat app is added as a member of the space. However, unlike human authentication, the Chat app is not added as a space manager. By default, the Chat app can be removed from the space by all space members. To allow only space managers to remove the app from a space, set `space.permission_settings.manage_apps` to `managers_allowed`.

Space membership upon creation depends on whether the space is created in `Import mode`:

  * **Import mode:** No members are created. 
  * **All other modes:** The calling user is added as a member. This is: * The app itself when using app authentication. * The human user when using user authentication. 



If you receive the error message `ALREADY_EXISTS` when creating a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       Space space = Space.newBuilder().build();
       Space response = chatServiceClient.createSpace(space);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`space` | `[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)`  
Required. The `displayName` and `spaceType` fields must be populated. Only `SpaceType.SPACE` and `SpaceType.GROUP_CHAT` are supported. `SpaceType.GROUP_CHAT` can only be used if `importMode` is set to true. If you receive the error message `ALREADY_EXISTS`, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name. The space `name` is assigned on the server so anything specified in this field will be ignored.  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### createSpaceCallable()
    
    
    public final UnaryCallable<CreateSpaceRequest,Space> createSpaceCallable()

Creates a space. Can be used to create a named space, or a group chat in `Import mode`. For an example, see [Create a space](https://developers.google.com/workspace/chat/create-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces.create>` \- `<https://www.googleapis.com/auth/chat.app.spaces>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When authenticating as an app, the `space.customer` field must be set in the request.

When authenticating as an app, the Chat app is added as a member of the space. However, unlike human authentication, the Chat app is not added as a space manager. By default, the Chat app can be removed from the space by all space members. To allow only space managers to remove the app from a space, set `space.permission_settings.manage_apps` to `managers_allowed`.

Space membership upon creation depends on whether the space is created in `Import mode`:

  * **Import mode:** No members are created. 
  * **All other modes:** The calling user is added as a member. This is: * The app itself when using app authentication. * The human user when using user authentication. 



If you receive the error message `ALREADY_EXISTS` when creating a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CreateSpaceRequest request =
           CreateSpaceRequest.newBuilder()
               .setSpace(Space.newBuilder().build())
               .setRequestId("requestId693933066")
               .build();
       ApiFuture<Space> future = chatServiceClient.createSpaceCallable().futureCall(request);
       // Do something.
       Space response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[CreateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CreateSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### deleteCustomEmoji(@Nullable CustomEmojiName name)
    
    
    public final void deleteCustomEmoji(@Nullable CustomEmojiName name)

Deletes a custom emoji. By default, users can only delete custom emoji they created. [Emoji managers](https://support.google.com/a/answer/12850085) assigned by the administrator can delete any custom emoji in the organization. See [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149).

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CustomEmojiName name = CustomEmojiName.of("[CUSTOM_EMOJI]");
       chatServiceClient.deleteCustomEmoji(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.CustomEmojiName`  
Required. Resource name of the custom emoji to delete. Format: `customEmojis/{customEmoji}` You can use the emoji name as an alias for `{customEmoji}`. For example, `customEmojis/:example-emoji:` where `:example-emoji:` is the emoji name for a custom emoji.  
  
### deleteCustomEmoji(DeleteCustomEmojiRequest request)
    
    
    public final void deleteCustomEmoji(DeleteCustomEmojiRequest request)

Deletes a custom emoji. By default, users can only delete custom emoji they created. [Emoji managers](https://support.google.com/a/answer/12850085) assigned by the administrator can delete any custom emoji in the organization. See [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149).

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteCustomEmojiRequest request =
           DeleteCustomEmojiRequest.newBuilder()
               .setName(CustomEmojiName.of("[CUSTOM_EMOJI]").toString())
               .build();
       chatServiceClient.deleteCustomEmoji(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteCustomEmoji(String name)
    
    
    public final void deleteCustomEmoji(String name)

Deletes a custom emoji. By default, users can only delete custom emoji they created. [Emoji managers](https://support.google.com/a/answer/12850085) assigned by the administrator can delete any custom emoji in the organization. See [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149).

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = CustomEmojiName.of("[CUSTOM_EMOJI]").toString();
       chatServiceClient.deleteCustomEmoji(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the custom emoji to delete. Format: `customEmojis/{customEmoji}` You can use the emoji name as an alias for `{customEmoji}`. For example, `customEmojis/:example-emoji:` where `:example-emoji:` is the emoji name for a custom emoji.  
  
### deleteCustomEmojiCallable()
    
    
    public final UnaryCallable<DeleteCustomEmojiRequest,Empty> deleteCustomEmojiCallable()

Deletes a custom emoji. By default, users can only delete custom emoji they created. [Emoji managers](https://support.google.com/a/answer/12850085) assigned by the administrator can delete any custom emoji in the organization. See [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149).

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteCustomEmojiRequest request =
           DeleteCustomEmojiRequest.newBuilder()
               .setName(CustomEmojiName.of("[CUSTOM_EMOJI]").toString())
               .build();
       ApiFuture<Empty> future = chatServiceClient.deleteCustomEmojiCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteCustomEmojiRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteMembership(@Nullable MembershipName name)
    
    
    public final Membership deleteMembership(@Nullable MembershipName name)

Deletes a membership. For an example, see [Remove a user or a Google Chat app from a space](https://developers.google.com/workspace/chat/delete-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to remove the calling app from the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Removing a Google Group from a space. - Removing a Chat app from a space.

To delete memberships for space managers, the requester must be a space manager. If you're using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) the Chat app must be the space creator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MembershipName name = MembershipName.of("[SPACE]", "[MEMBER]");
       Membership response = chatServiceClient.deleteMembership(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MembershipName`  
Required. Resource name of the membership to delete. Chat apps can delete human users' or their own memberships. Chat apps can't delete other apps' memberships. When deleting a human membership, requires the `chat.memberships` scope with [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) or the `chat.memberships.app` scope with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) and the `spaces/{space}/members/{member}` format. You can use the email as an alias for `{member}`. For example, `spaces/{space}/members/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user. When deleting an app membership, requires the `chat.memberships.app` scope and `spaces/{space}/members/app` format. Format: `spaces/{space}/members/{member}` or `spaces/{space}/members/app`.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### deleteMembership(DeleteMembershipRequest request)
    
    
    public final Membership deleteMembership(DeleteMembershipRequest request)

Deletes a membership. For an example, see [Remove a user or a Google Chat app from a space](https://developers.google.com/workspace/chat/delete-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to remove the calling app from the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Removing a Google Group from a space. - Removing a Chat app from a space.

To delete memberships for space managers, the requester must be a space manager. If you're using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) the Chat app must be the space creator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteMembershipRequest request =
           DeleteMembershipRequest.newBuilder()
               .setName(MembershipName.of("[SPACE]", "[MEMBER]").toString())
               .setUseAdminAccess(true)
               .build();
       Membership response = chatServiceClient.deleteMembership(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### deleteMembership(String name)
    
    
    public final Membership deleteMembership(String name)

Deletes a membership. For an example, see [Remove a user or a Google Chat app from a space](https://developers.google.com/workspace/chat/delete-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to remove the calling app from the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Removing a Google Group from a space. - Removing a Chat app from a space.

To delete memberships for space managers, the requester must be a space manager. If you're using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) the Chat app must be the space creator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = MembershipName.of("[SPACE]", "[MEMBER]").toString();
       Membership response = chatServiceClient.deleteMembership(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the membership to delete. Chat apps can delete human users' or their own memberships. Chat apps can't delete other apps' memberships. When deleting a human membership, requires the `chat.memberships` scope with [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) or the `chat.memberships.app` scope with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) and the `spaces/{space}/members/{member}` format. You can use the email as an alias for `{member}`. For example, `spaces/{space}/members/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user. When deleting an app membership, requires the `chat.memberships.app` scope and `spaces/{space}/members/app` format. Format: `spaces/{space}/members/{member}` or `spaces/{space}/members/app`.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### deleteMembershipCallable()
    
    
    public final UnaryCallable<DeleteMembershipRequest,Membership> deleteMembershipCallable()

Deletes a membership. For an example, see [Remove a user or a Google Chat app from a space](https://developers.google.com/workspace/chat/delete-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.memberships.app>` (to remove the calling app from the space) - `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

App authentication is not supported for the following use cases:

\- Removing a Google Group from a space. - Removing a Chat app from a space.

To delete memberships for space managers, the requester must be a space manager. If you're using [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) the Chat app must be the space creator.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteMembershipRequest request =
           DeleteMembershipRequest.newBuilder()
               .setName(MembershipName.of("[SPACE]", "[MEMBER]").toString())
               .setUseAdminAccess(true)
               .build();
       ApiFuture<Membership> future =
           chatServiceClient.deleteMembershipCallable().futureCall(request);
       // Do something.
       Membership response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### deleteMessage(@Nullable MessageName name)
    
    
    public final void deleteMessage(@Nullable MessageName name)

Deletes a message. For an example, see [Delete a message](https://developers.google.com/workspace/chat/delete-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only delete messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MessageName name = MessageName.of("[SPACE]", "[MESSAGE]");
       chatServiceClient.deleteMessage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MessageName`  
Required. Resource name of the message. Format: `spaces/{space}/messages/{message}` If you've set a custom ID for your message, you can use the value from the `clientAssignedMessageId` field for `{message}`. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).  
  
### deleteMessage(DeleteMessageRequest request)
    
    
    public final void deleteMessage(DeleteMessageRequest request)

Deletes a message. For an example, see [Delete a message](https://developers.google.com/workspace/chat/delete-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only delete messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteMessageRequest request =
           DeleteMessageRequest.newBuilder()
               .setName(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setForce(true)
               .build();
       chatServiceClient.deleteMessage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteMessage(String name)
    
    
    public final void deleteMessage(String name)

Deletes a message. For an example, see [Delete a message](https://developers.google.com/workspace/chat/delete-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only delete messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = MessageName.of("[SPACE]", "[MESSAGE]").toString();
       chatServiceClient.deleteMessage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the message. Format: `spaces/{space}/messages/{message}` If you've set a custom ID for your message, you can use the value from the `clientAssignedMessageId` field for `{message}`. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).  
  
### deleteMessageCallable()
    
    
    public final UnaryCallable<DeleteMessageRequest,Empty> deleteMessageCallable()

Deletes a message. For an example, see [Delete a message](https://developers.google.com/workspace/chat/delete-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only delete messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteMessageRequest request =
           DeleteMessageRequest.newBuilder()
               .setName(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setForce(true)
               .build();
       ApiFuture<Empty> future = chatServiceClient.deleteMessageCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessageRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteMessagePin(@Nullable MessagePinName name)
    
    
    public final void deleteMessagePin(@Nullable MessagePinName name)

Deletes a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MessagePinName name = MessagePinName.of("[SPACE]", "[MESSAGE_PIN]");
       chatServiceClient.deleteMessagePin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MessagePinName`  
Required. The resource name of the message pin to remove. Format: spaces/{space}/messagePins/{message_pin}  
  
### deleteMessagePin(DeleteMessagePinRequest request)
    
    
    public final void deleteMessagePin(DeleteMessagePinRequest request)

Deletes a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteMessagePinRequest request =
           DeleteMessagePinRequest.newBuilder()
               .setName(MessagePinName.of("[SPACE]", "[MESSAGE_PIN]").toString())
               .build();
       chatServiceClient.deleteMessagePin(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteMessagePin(String name)
    
    
    public final void deleteMessagePin(String name)

Deletes a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = MessagePinName.of("[SPACE]", "[MESSAGE_PIN]").toString();
       chatServiceClient.deleteMessagePin(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the message pin to remove. Format: spaces/{space}/messagePins/{message_pin}  
  
### deleteMessagePinCallable()
    
    
    public final UnaryCallable<DeleteMessagePinRequest,Empty> deleteMessagePinCallable()

Deletes a message pin.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteMessagePinRequest request =
           DeleteMessagePinRequest.newBuilder()
               .setName(MessagePinName.of("[SPACE]", "[MESSAGE_PIN]").toString())
               .build();
       ApiFuture<Empty> future = chatServiceClient.deleteMessagePinCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteMessagePinRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteMessagePinRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteReaction(@Nullable ReactionName name)
    
    
    public final void deleteReaction(@Nullable ReactionName name)

Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/workspace/chat/delete-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ReactionName name = ReactionName.of("[SPACE]", "[MESSAGE]", "[REACTION]");
       chatServiceClient.deleteReaction(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.ReactionName`  
Required. Name of the reaction to delete. Format: `spaces/{space}/messages/{message}/reactions/{reaction}`  
  
### deleteReaction(DeleteReactionRequest request)
    
    
    public final void deleteReaction(DeleteReactionRequest request)

Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/workspace/chat/delete-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteReactionRequest request =
           DeleteReactionRequest.newBuilder()
               .setName(ReactionName.of("[SPACE]", "[MESSAGE]", "[REACTION]").toString())
               .build();
       chatServiceClient.deleteReaction(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteReaction(String name)
    
    
    public final void deleteReaction(String name)

Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/workspace/chat/delete-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = ReactionName.of("[SPACE]", "[MESSAGE]", "[REACTION]").toString();
       chatServiceClient.deleteReaction(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Name of the reaction to delete. Format: `spaces/{space}/messages/{message}/reactions/{reaction}`  
  
### deleteReactionCallable()
    
    
    public final UnaryCallable<DeleteReactionRequest,Empty> deleteReactionCallable()

Deletes a reaction to a message. For an example, see [Delete a reaction](https://developers.google.com/workspace/chat/delete-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteReactionRequest request =
           DeleteReactionRequest.newBuilder()
               .setName(ReactionName.of("[SPACE]", "[MESSAGE]", "[REACTION]").toString())
               .build();
       ApiFuture<Empty> future = chatServiceClient.deleteReactionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteReactionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteReactionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSection(@Nullable SectionName name)
    
    
    public final void deleteSection(@Nullable SectionName name)

Deletes a section of type `CUSTOM_SECTION`.

If the section contains items, such as spaces, the items are moved to Google Chat's default sections and are not deleted.

For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SectionName name = SectionName.of("[USER]", "[SECTION]");
       chatServiceClient.deleteSection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SectionName`  
Required. The name of the section to delete. Format: `users/{user}/sections/{section}`  
  
### deleteSection(DeleteSectionRequest request)
    
    
    public final void deleteSection(DeleteSectionRequest request)

Deletes a section of type `CUSTOM_SECTION`.

If the section contains items, such as spaces, the items are moved to Google Chat's default sections and are not deleted.

For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteSectionRequest request =
           DeleteSectionRequest.newBuilder()
               .setName(SectionName.of("[USER]", "[SECTION]").toString())
               .build();
       chatServiceClient.deleteSection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSection(String name)
    
    
    public final void deleteSection(String name)

Deletes a section of type `CUSTOM_SECTION`.

If the section contains items, such as spaces, the items are moved to Google Chat's default sections and are not deleted.

For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SectionName.of("[USER]", "[SECTION]").toString();
       chatServiceClient.deleteSection(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The name of the section to delete. Format: `users/{user}/sections/{section}`  
  
### deleteSectionCallable()
    
    
    public final UnaryCallable<DeleteSectionRequest,Empty> deleteSectionCallable()

Deletes a section of type `CUSTOM_SECTION`.

If the section contains items, such as spaces, the items are moved to Google Chat's default sections and are not deleted.

For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       DeleteSectionRequest request =
           DeleteSectionRequest.newBuilder()
               .setName(SectionName.of("[USER]", "[SECTION]").toString())
               .build();
       ApiFuture<Empty> future = chatServiceClient.deleteSectionCallable().futureCall(request);
       // Do something.
       future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSectionRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### deleteSpace(@Nullable SpaceName name)
    
    
    public final void deleteSpace(@Nullable SpaceName name)

Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see [Delete a space](https://developers.google.com/workspace/chat/delete-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.delete>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.delete>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.delete>`

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        SpaceName name = SpaceName.of("[SPACE]");
        chatServiceClient.deleteSpace(name);
        }
        




**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. Resource name of the space to delete. Format: `spaces/{space}`  
  
### deleteSpace(DeleteSpaceRequest request)
    
    
    public final void deleteSpace(DeleteSpaceRequest request)

Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see [Delete a space](https://developers.google.com/workspace/chat/delete-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.delete>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.delete>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.delete>`

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        DeleteSpaceRequest request =
            DeleteSpaceRequest.newBuilder()
                .setName(SpaceName.of("[SPACE]").toString())
                .setUseAdminAccess(true)
                .build();
        chatServiceClient.deleteSpace(request);
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[DeleteSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequest)`  
The request object containing all of the parameters for the API call.  
  
### deleteSpace(String name)
    
    
    public final void deleteSpace(String name)

Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see [Delete a space](https://developers.google.com/workspace/chat/delete-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.delete>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.delete>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.delete>`

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        String name = SpaceName.of("[SPACE]").toString();
        chatServiceClient.deleteSpace(name);
        }
        




**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the space to delete. Format: `spaces/{space}`  
  
### deleteSpaceCallable()
    
    
    public final UnaryCallable<DeleteSpaceRequest,Empty> deleteSpaceCallable()

Deletes a named space. Always performs a cascading delete, which means that the space's child resources—like messages posted in the space and memberships in the space—are also deleted. For an example, see [Delete a space](https://developers.google.com/workspace/chat/delete-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.delete>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.delete>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.delete>`

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        DeleteSpaceRequest request =
            DeleteSpaceRequest.newBuilder()
                .setName(SpaceName.of("[SPACE]").toString())
                .setUseAdminAccess(true)
                .build();
        ApiFuture<Empty> future = chatServiceClient.deleteSpaceCallable().futureCall(request);
        // Do something.
        future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[DeleteSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.DeleteSpaceRequest),[Empty](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html)>` |   
  
### findDirectMessage(FindDirectMessageRequest request)
    
    
    public final Space findDirectMessage(FindDirectMessageRequest request)

Returns the existing direct message with the specified user. If no direct message space is found, returns a `404 NOT_FOUND` error. For an example, see [Find a direct message](https://docs.cloud.google.com/chat/api/guides/v1/spaces/find-direct-message).

With [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), returns the direct message space between the specified user and the calling Chat app.

With [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), returns the direct message space between the specified user and the authenticated user.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       FindDirectMessageRequest request =
           FindDirectMessageRequest.newBuilder().setName("name3373707").build();
       Space response = chatServiceClient.findDirectMessage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FindDirectMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### findDirectMessageCallable()
    
    
    public final UnaryCallable<FindDirectMessageRequest,Space> findDirectMessageCallable()

Returns the existing direct message with the specified user. If no direct message space is found, returns a `404 NOT_FOUND` error. For an example, see [Find a direct message](https://docs.cloud.google.com/chat/api/guides/v1/spaces/find-direct-message).

With [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), returns the direct message space between the specified user and the calling Chat app.

With [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), returns the direct message space between the specified user and the authenticated user.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       FindDirectMessageRequest request =
           FindDirectMessageRequest.newBuilder().setName("name3373707").build();
       ApiFuture<Space> future = chatServiceClient.findDirectMessageCallable().futureCall(request);
       // Do something.
       Space response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FindDirectMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindDirectMessageRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### findGroupChats(FindGroupChatsRequest request)
    
    
    public final ChatServiceClient.FindGroupChatsPagedResponse findGroupChats(FindGroupChatsRequest request)

Returns all spaces with `spaceType == GROUP_CHAT`, whose human memberships contain exactly the calling user, and the users specified in `FindGroupChatsRequest.users`. Only members that have joined the conversation are supported. For an example, see [Find group chats](https://developers.google.com/workspace/chat/find-group-chats).

If the calling user blocks, or is blocked by, some users, and no spaces with the entire specified set of users are found, this method returns spaces that don't include the blocked or blocking users.

The specified set of users must contain only human (non-app) memberships. A request that contains non-human users doesn't return any spaces.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       FindGroupChatsRequest request =
           FindGroupChatsRequest.newBuilder()
               .addAllUsers(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSpaceView(SpaceView.forNumber(0))
               .build();
       for (Space element : chatServiceClient.findGroupChats(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[FindGroupChatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.FindGroupChatsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.FindGroupChatsPagedResponse)` |   
  
### findGroupChatsCallable()
    
    
    public final UnaryCallable<FindGroupChatsRequest,FindGroupChatsResponse> findGroupChatsCallable()

Returns all spaces with `spaceType == GROUP_CHAT`, whose human memberships contain exactly the calling user, and the users specified in `FindGroupChatsRequest.users`. Only members that have joined the conversation are supported. For an example, see [Find group chats](https://developers.google.com/workspace/chat/find-group-chats).

If the calling user blocks, or is blocked by, some users, and no spaces with the entire specified set of users are found, this method returns spaces that don't include the blocked or blocking users.

The specified set of users must contain only human (non-app) memberships. A request that contains non-human users doesn't return any spaces.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       FindGroupChatsRequest request =
           FindGroupChatsRequest.newBuilder()
               .addAllUsers(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSpaceView(SpaceView.forNumber(0))
               .build();
       while (true) {
         FindGroupChatsResponse response = chatServiceClient.findGroupChatsCallable().call(request);
         for (Space element : response.getSpacesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FindGroupChatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest),[FindGroupChatsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsResponse)>` |   
  
### findGroupChatsPagedCallable()
    
    
    public final UnaryCallable<FindGroupChatsRequest,ChatServiceClient.FindGroupChatsPagedResponse> findGroupChatsPagedCallable()

Returns all spaces with `spaceType == GROUP_CHAT`, whose human memberships contain exactly the calling user, and the users specified in `FindGroupChatsRequest.users`. Only members that have joined the conversation are supported. For an example, see [Find group chats](https://developers.google.com/workspace/chat/find-group-chats).

If the calling user blocks, or is blocked by, some users, and no spaces with the entire specified set of users are found, this method returns spaces that don't include the blocked or blocking users.

The specified set of users must contain only human (non-app) memberships. A request that contains non-human users doesn't return any spaces.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       FindGroupChatsRequest request =
           FindGroupChatsRequest.newBuilder()
               .addAllUsers(new ArrayList<String>())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setSpaceView(SpaceView.forNumber(0))
               .build();
       ApiFuture<Space> future = chatServiceClient.findGroupChatsPagedCallable().futureCall(request);
       // Do something.
       for (Space element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[FindGroupChatsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequest),[FindGroupChatsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.FindGroupChatsPagedResponse)>` |   
  
### getAttachment(@Nullable AttachmentName name)
    
    
    public final Attachment getAttachment(@Nullable AttachmentName name)

Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download). For an example, see [Get metadata about a message attachment](https://developers.google.com/workspace/chat/get-media-attachments).

Requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.bot>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       AttachmentName name = AttachmentName.of("[SPACE]", "[MESSAGE]", "[ATTACHMENT]");
       Attachment response = chatServiceClient.getAttachment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.AttachmentName`  
Required. Resource name of the attachment, in the form `spaces/{space}/messages/{message}/attachments/{attachment}`.  
**Returns**  
---  
**Type** | **Description**  
`[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)` |   
  
### getAttachment(GetAttachmentRequest request)
    
    
    public final Attachment getAttachment(GetAttachmentRequest request)

Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download). For an example, see [Get metadata about a message attachment](https://developers.google.com/workspace/chat/get-media-attachments).

Requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.bot>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetAttachmentRequest request =
           GetAttachmentRequest.newBuilder()
               .setName(AttachmentName.of("[SPACE]", "[MESSAGE]", "[ATTACHMENT]").toString())
               .build();
       Attachment response = chatServiceClient.getAttachment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)` |   
  
### getAttachment(String name)
    
    
    public final Attachment getAttachment(String name)

Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download). For an example, see [Get metadata about a message attachment](https://developers.google.com/workspace/chat/get-media-attachments).

Requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.bot>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = AttachmentName.of("[SPACE]", "[MESSAGE]", "[ATTACHMENT]").toString();
       Attachment response = chatServiceClient.getAttachment(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the attachment, in the form `spaces/{space}/messages/{message}/attachments/{attachment}`.  
**Returns**  
---  
**Type** | **Description**  
`[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)` |   
  
### getAttachmentCallable()
    
    
    public final UnaryCallable<GetAttachmentRequest,Attachment> getAttachmentCallable()

Gets the metadata of a message attachment. The attachment data is fetched using the [media API](https://developers.google.com/workspace/chat/api/reference/rest/v1/media/download). For an example, see [Get metadata about a message attachment](https://developers.google.com/workspace/chat/get-media-attachments).

Requires [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.bot>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetAttachmentRequest request =
           GetAttachmentRequest.newBuilder()
               .setName(AttachmentName.of("[SPACE]", "[MESSAGE]", "[ATTACHMENT]").toString())
               .build();
       ApiFuture<Attachment> future = chatServiceClient.getAttachmentCallable().futureCall(request);
       // Do something.
       Attachment response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAttachmentRequest),[Attachment](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Attachment)>` |   
  
### getAvailability(@Nullable AvailabilityName name)
    
    
    public final Availability getAvailability(@Nullable AvailabilityName name)

Returns availability information for a human user in Google Chat. For example, this can be used to check if a user is online or away, or to retrieve their custom status message.

This method only retrieves the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability.readonly>` \- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       AvailabilityName name = AvailabilityName.of("[USER]");
       Availability response = chatServiceClient.getAvailability(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.AvailabilityName`  
Required. The resource name of the availability to retrieve. Format: users/{user}/availability `{user}` is the id for the Person in the People API or Admin SDK directory API. For example, `users/123456789`. The user's email address or `me` can also be used as an alias to refer to the caller. For example, `users/user@example.com` or `users/me`.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### getAvailability(GetAvailabilityRequest request)
    
    
    public final Availability getAvailability(GetAvailabilityRequest request)

Returns availability information for a human user in Google Chat. For example, this can be used to check if a user is online or away, or to retrieve their custom status message.

This method only retrieves the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability.readonly>` \- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetAvailabilityRequest request =
           GetAvailabilityRequest.newBuilder()
               .setName(AvailabilityName.of("[USER]").toString())
               .build();
       Availability response = chatServiceClient.getAvailability(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### getAvailability(String name)
    
    
    public final Availability getAvailability(String name)

Returns availability information for a human user in Google Chat. For example, this can be used to check if a user is online or away, or to retrieve their custom status message.

This method only retrieves the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability.readonly>` \- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = AvailabilityName.of("[USER]").toString();
       Availability response = chatServiceClient.getAvailability(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the availability to retrieve. Format: users/{user}/availability `{user}` is the id for the Person in the People API or Admin SDK directory API. For example, `users/123456789`. The user's email address or `me` can also be used as an alias to refer to the caller. For example, `users/user@example.com` or `users/me`.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### getAvailabilityCallable()
    
    
    public final UnaryCallable<GetAvailabilityRequest,Availability> getAvailabilityCallable()

Returns availability information for a human user in Google Chat. For example, this can be used to check if a user is online or away, or to retrieve their custom status message.

This method only retrieves the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability.readonly>` \- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetAvailabilityRequest request =
           GetAvailabilityRequest.newBuilder()
               .setName(AvailabilityName.of("[USER]").toString())
               .build();
       ApiFuture<Availability> future =
           chatServiceClient.getAvailabilityCallable().futureCall(request);
       // Do something.
       Availability response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetAvailabilityRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### getCustomEmoji(@Nullable CustomEmojiName name)
    
    
    public final CustomEmoji getCustomEmoji(@Nullable CustomEmojiName name)

Returns details about a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       CustomEmojiName name = CustomEmojiName.of("[CUSTOM_EMOJI]");
       CustomEmoji response = chatServiceClient.getCustomEmoji(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.CustomEmojiName`  
Required. Resource name of the custom emoji. Format: `customEmojis/{customEmoji}` You can use the emoji name as an alias for `{customEmoji}`. For example, `customEmojis/:example-emoji:` where `:example-emoji:` is the emoji name for a custom emoji.  
**Returns**  
---  
**Type** | **Description**  
`[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)` |   
  
### getCustomEmoji(GetCustomEmojiRequest request)
    
    
    public final CustomEmoji getCustomEmoji(GetCustomEmojiRequest request)

Returns details about a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetCustomEmojiRequest request =
           GetCustomEmojiRequest.newBuilder()
               .setName(CustomEmojiName.of("[CUSTOM_EMOJI]").toString())
               .build();
       CustomEmoji response = chatServiceClient.getCustomEmoji(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)` |   
  
### getCustomEmoji(String name)
    
    
    public final CustomEmoji getCustomEmoji(String name)

Returns details about a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = CustomEmojiName.of("[CUSTOM_EMOJI]").toString();
       CustomEmoji response = chatServiceClient.getCustomEmoji(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the custom emoji. Format: `customEmojis/{customEmoji}` You can use the emoji name as an alias for `{customEmoji}`. For example, `customEmojis/:example-emoji:` where `:example-emoji:` is the emoji name for a custom emoji.  
**Returns**  
---  
**Type** | **Description**  
`[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)` |   
  
### getCustomEmojiCallable()
    
    
    public final UnaryCallable<GetCustomEmojiRequest,CustomEmoji> getCustomEmojiCallable()

Returns details about a custom emoji.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetCustomEmojiRequest request =
           GetCustomEmojiRequest.newBuilder()
               .setName(CustomEmojiName.of("[CUSTOM_EMOJI]").toString())
               .build();
       ApiFuture<CustomEmoji> future =
           chatServiceClient.getCustomEmojiCallable().futureCall(request);
       // Do something.
       CustomEmoji response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetCustomEmojiRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetCustomEmojiRequest),[CustomEmoji](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.CustomEmoji)>` |   
  
### getMembership(@Nullable MembershipName name)
    
    
    public final Membership getMembership(@Nullable MembershipName name)

Returns details about a membership. For an example, see [Get details about a user's or Google Chat app's membership](https://developers.google.com/workspace/chat/get-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MembershipName name = MembershipName.of("[SPACE]", "[MEMBER]");
       Membership response = chatServiceClient.getMembership(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MembershipName`  
Required. Resource name of the membership to retrieve. To get the app's own membership [by using user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), you can optionally use `spaces/{space}/members/app`. Format: `spaces/{space}/members/{member}` or `spaces/{space}/members/app` You can use the user's email as an alias for `{member}`. For example, `spaces/{space}/members/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### getMembership(GetMembershipRequest request)
    
    
    public final Membership getMembership(GetMembershipRequest request)

Returns details about a membership. For an example, see [Get details about a user's or Google Chat app's membership](https://developers.google.com/workspace/chat/get-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetMembershipRequest request =
           GetMembershipRequest.newBuilder()
               .setName(MembershipName.of("[SPACE]", "[MEMBER]").toString())
               .setUseAdminAccess(true)
               .build();
       Membership response = chatServiceClient.getMembership(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### getMembership(String name)
    
    
    public final Membership getMembership(String name)

Returns details about a membership. For an example, see [Get details about a user's or Google Chat app's membership](https://developers.google.com/workspace/chat/get-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = MembershipName.of("[SPACE]", "[MEMBER]").toString();
       Membership response = chatServiceClient.getMembership(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the membership to retrieve. To get the app's own membership [by using user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), you can optionally use `spaces/{space}/members/app`. Format: `spaces/{space}/members/{member}` or `spaces/{space}/members/app` You can use the user's email as an alias for `{member}`. For example, `spaces/{space}/members/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### getMembershipCallable()
    
    
    public final UnaryCallable<GetMembershipRequest,Membership> getMembershipCallable()

Returns details about a membership. For an example, see [Get details about a user's or Google Chat app's membership](https://developers.google.com/workspace/chat/get-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetMembershipRequest request =
           GetMembershipRequest.newBuilder()
               .setName(MembershipName.of("[SPACE]", "[MEMBER]").toString())
               .setUseAdminAccess(true)
               .build();
       ApiFuture<Membership> future = chatServiceClient.getMembershipCallable().futureCall(request);
       // Do something.
       Membership response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### getMessage(@Nullable MessageName name)
    
    
    public final Message getMessage(@Nullable MessageName name)

Returns details about a message. For an example, see [Get details about a message](https://developers.google.com/workspace/chat/get-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>`: When using this authorization scope, this method returns details about a message the Chat app has access to, like direct messages and [slash commands](https://developers.google.com/workspace/chat/slash-commands) that invoke the Chat app. - `<https://www.googleapis.com/auth/chat.app.messages.readonly>` with [administrator approval](https://support.google.com/a?p=chat-app-auth). When using this authentication scope, this method returns details about a public message in a space.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Note: Might return a message from a blocked member or space.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MessageName name = MessageName.of("[SPACE]", "[MESSAGE]");
       Message response = chatServiceClient.getMessage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MessageName`  
Required. Resource name of the message. Format: `spaces/{space}/messages/{message}` If you've set a custom ID for your message, you can use the value from the `clientAssignedMessageId` field for `{message}`. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### getMessage(GetMessageRequest request)
    
    
    public final Message getMessage(GetMessageRequest request)

Returns details about a message. For an example, see [Get details about a message](https://developers.google.com/workspace/chat/get-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>`: When using this authorization scope, this method returns details about a message the Chat app has access to, like direct messages and [slash commands](https://developers.google.com/workspace/chat/slash-commands) that invoke the Chat app. - `<https://www.googleapis.com/auth/chat.app.messages.readonly>` with [administrator approval](https://support.google.com/a?p=chat-app-auth). When using this authentication scope, this method returns details about a public message in a space.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Note: Might return a message from a blocked member or space.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetMessageRequest request =
           GetMessageRequest.newBuilder()
               .setName(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       Message response = chatServiceClient.getMessage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### getMessage(String name)
    
    
    public final Message getMessage(String name)

Returns details about a message. For an example, see [Get details about a message](https://developers.google.com/workspace/chat/get-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>`: When using this authorization scope, this method returns details about a message the Chat app has access to, like direct messages and [slash commands](https://developers.google.com/workspace/chat/slash-commands) that invoke the Chat app. - `<https://www.googleapis.com/auth/chat.app.messages.readonly>` with [administrator approval](https://support.google.com/a?p=chat-app-auth). When using this authentication scope, this method returns details about a public message in a space.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Note: Might return a message from a blocked member or space.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = MessageName.of("[SPACE]", "[MESSAGE]").toString();
       Message response = chatServiceClient.getMessage(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the message. Format: `spaces/{space}/messages/{message}` If you've set a custom ID for your message, you can use the value from the `clientAssignedMessageId` field for `{message}`. For details, see [Name a message](https://developers.google.com/workspace/chat/create-messages#name_a_created_message).  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### getMessageCallable()
    
    
    public final UnaryCallable<GetMessageRequest,Message> getMessageCallable()

Returns details about a message. For an example, see [Get details about a message](https://developers.google.com/workspace/chat/get-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>`: When using this authorization scope, this method returns details about a message the Chat app has access to, like direct messages and [slash commands](https://developers.google.com/workspace/chat/slash-commands) that invoke the Chat app. - `<https://www.googleapis.com/auth/chat.app.messages.readonly>` with [administrator approval](https://support.google.com/a?p=chat-app-auth). When using this authentication scope, this method returns details about a public message in a space.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Note: Might return a message from a blocked member or space.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetMessageRequest request =
           GetMessageRequest.newBuilder()
               .setName(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       ApiFuture<Message> future = chatServiceClient.getMessageCallable().futureCall(request);
       // Do something.
       Message response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetMessageRequest),[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>` |   
  
### getSettings()
    
    
    public final @Nullable ChatServiceSettings getSettings()

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable com.google.chat.v1.ChatServiceSettings` |   
  
### getSpace(@Nullable SpaceName name)
    
    
    public final Space getSpace(@Nullable SpaceName name)

Returns details about a space. For an example, see [Get details about a space](https://developers.google.com/workspace/chat/get-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.spaces>` with [administrator approval](https://support.google.com/a?p=chat-app-auth)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- `space.access_settings` is only populated when using the `chat.app.spaces` scope. - `space.predefind_permission_settings` and `space.permission_settings` are only populated when using the `chat.app.spaces` scope, and only for spaces the app created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName name = SpaceName.of("[SPACE]");
       Space response = chatServiceClient.getSpace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. Resource name of the space, in the form `spaces/{space}`. Format: `spaces/{space}`  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### getSpace(GetSpaceRequest request)
    
    
    public final Space getSpace(GetSpaceRequest request)

Returns details about a space. For an example, see [Get details about a space](https://developers.google.com/workspace/chat/get-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.spaces>` with [administrator approval](https://support.google.com/a?p=chat-app-auth)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- `space.access_settings` is only populated when using the `chat.app.spaces` scope. - `space.predefind_permission_settings` and `space.permission_settings` are only populated when using the `chat.app.spaces` scope, and only for spaces the app created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceRequest request =
           GetSpaceRequest.newBuilder()
               .setName(SpaceName.of("[SPACE]").toString())
               .setUseAdminAccess(true)
               .build();
       Space response = chatServiceClient.getSpace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### getSpace(String name)
    
    
    public final Space getSpace(String name)

Returns details about a space. For an example, see [Get details about a space](https://developers.google.com/workspace/chat/get-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.spaces>` with [administrator approval](https://support.google.com/a?p=chat-app-auth)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- `space.access_settings` is only populated when using the `chat.app.spaces` scope. - `space.predefind_permission_settings` and `space.permission_settings` are only populated when using the `chat.app.spaces` scope, and only for spaces the app created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SpaceName.of("[SPACE]").toString();
       Space response = chatServiceClient.getSpace(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the space, in the form `spaces/{space}`. Format: `spaces/{space}`  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### getSpaceCallable()
    
    
    public final UnaryCallable<GetSpaceRequest,Space> getSpaceCallable()

Returns details about a space. For an example, see [Get details about a space](https://developers.google.com/workspace/chat/get-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.spaces>` with [administrator approval](https://support.google.com/a?p=chat-app-auth)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- `space.access_settings` is only populated when using the `chat.app.spaces` scope. - `space.predefind_permission_settings` and `space.permission_settings` are only populated when using the `chat.app.spaces` scope, and only for spaces the app created.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceRequest request =
           GetSpaceRequest.newBuilder()
               .setName(SpaceName.of("[SPACE]").toString())
               .setUseAdminAccess(true)
               .build();
       ApiFuture<Space> future = chatServiceClient.getSpaceCallable().futureCall(request);
       // Do something.
       Space response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### getSpaceEvent(@Nullable SpaceEventName name)
    
    
    public final SpaceEvent getSpaceEvent(@Nullable SpaceEventName name)

Returns an event from a Google Chat space. The [event payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the resource that changed. For example, if you request an event about a new message but the message was later updated, the server returns the updated `Message` resource in the event payload.

Note: The `permissionSettings` field is not returned in the Space object of the Space event data for this request.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To get an event, the authenticated caller must be a member of the space.

For an example, see [Get details about an event from a Google Chat space](https://developers.google.com/workspace/chat/get-space-event).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceEventName name = SpaceEventName.of("[SPACE]", "[SPACE_EVENT]");
       SpaceEvent response = chatServiceClient.getSpaceEvent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceEventName`  
Required. The resource name of the space event. Format: `spaces/{space}/spaceEvents/{spaceEvent}`  
**Returns**  
---  
**Type** | **Description**  
`[SpaceEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent)` |   
  
### getSpaceEvent(GetSpaceEventRequest request)
    
    
    public final SpaceEvent getSpaceEvent(GetSpaceEventRequest request)

Returns an event from a Google Chat space. The [event payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the resource that changed. For example, if you request an event about a new message but the message was later updated, the server returns the updated `Message` resource in the event payload.

Note: The `permissionSettings` field is not returned in the Space object of the Space event data for this request.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To get an event, the authenticated caller must be a member of the space.

For an example, see [Get details about an event from a Google Chat space](https://developers.google.com/workspace/chat/get-space-event).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceEventRequest request =
           GetSpaceEventRequest.newBuilder()
               .setName(SpaceEventName.of("[SPACE]", "[SPACE_EVENT]").toString())
               .build();
       SpaceEvent response = chatServiceClient.getSpaceEvent(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSpaceEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent)` |   
  
### getSpaceEvent(String name)
    
    
    public final SpaceEvent getSpaceEvent(String name)

Returns an event from a Google Chat space. The [event payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the resource that changed. For example, if you request an event about a new message but the message was later updated, the server returns the updated `Message` resource in the event payload.

Note: The `permissionSettings` field is not returned in the Space object of the Space event data for this request.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To get an event, the authenticated caller must be a member of the space.

For an example, see [Get details about an event from a Google Chat space](https://developers.google.com/workspace/chat/get-space-event).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SpaceEventName.of("[SPACE]", "[SPACE_EVENT]").toString();
       SpaceEvent response = chatServiceClient.getSpaceEvent(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the space event. Format: `spaces/{space}/spaceEvents/{spaceEvent}`  
**Returns**  
---  
**Type** | **Description**  
`[SpaceEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent)` |   
  
### getSpaceEventCallable()
    
    
    public final UnaryCallable<GetSpaceEventRequest,SpaceEvent> getSpaceEventCallable()

Returns an event from a Google Chat space. The [event payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the resource that changed. For example, if you request an event about a new message but the message was later updated, the server returns the updated `Message` resource in the event payload.

Note: The `permissionSettings` field is not returned in the Space object of the Space event data for this request.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To get an event, the authenticated caller must be a member of the space.

For an example, see [Get details about an event from a Google Chat space](https://developers.google.com/workspace/chat/get-space-event).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceEventRequest request =
           GetSpaceEventRequest.newBuilder()
               .setName(SpaceEventName.of("[SPACE]", "[SPACE_EVENT]").toString())
               .build();
       ApiFuture<SpaceEvent> future = chatServiceClient.getSpaceEventCallable().futureCall(request);
       // Do something.
       SpaceEvent response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpaceEventRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceEventRequest),[SpaceEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceEvent)>` |   
  
### getSpaceNotificationSetting(@Nullable SpaceNotificationSettingName name)
    
    
    public final SpaceNotificationSetting getSpaceNotificationSetting(@Nullable SpaceNotificationSettingName name)

Gets the space notification setting. For an example, see [Get the caller's space notification setting](https://developers.google.com/workspace/chat/get-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceNotificationSettingName name = SpaceNotificationSettingName.of("[USER]", "[SPACE]");
       SpaceNotificationSetting response = chatServiceClient.getSpaceNotificationSetting(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceNotificationSettingName`  
Required. Format: users/{user}/spaces/{space}/spaceNotificationSetting \- `users/me/spaces/{space}/spaceNotificationSetting`, OR - `users/user@example.com/spaces/{space}/spaceNotificationSetting`, OR - `users/123456789/spaces/{space}/spaceNotificationSetting`. Note: Only the caller's user id or email is allowed in the path.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)` |   
  
### getSpaceNotificationSetting(GetSpaceNotificationSettingRequest request)
    
    
    public final SpaceNotificationSetting getSpaceNotificationSetting(GetSpaceNotificationSettingRequest request)

Gets the space notification setting. For an example, see [Get the caller's space notification setting](https://developers.google.com/workspace/chat/get-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceNotificationSettingRequest request =
           GetSpaceNotificationSettingRequest.newBuilder()
               .setName(SpaceNotificationSettingName.of("[USER]", "[SPACE]").toString())
               .build();
       SpaceNotificationSetting response = chatServiceClient.getSpaceNotificationSetting(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)` |   
  
### getSpaceNotificationSetting(String name)
    
    
    public final SpaceNotificationSetting getSpaceNotificationSetting(String name)

Gets the space notification setting. For an example, see [Get the caller's space notification setting](https://developers.google.com/workspace/chat/get-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SpaceNotificationSettingName.of("[USER]", "[SPACE]").toString();
       SpaceNotificationSetting response = chatServiceClient.getSpaceNotificationSetting(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Format: users/{user}/spaces/{space}/spaceNotificationSetting \- `users/me/spaces/{space}/spaceNotificationSetting`, OR - `users/user@example.com/spaces/{space}/spaceNotificationSetting`, OR - `users/123456789/spaces/{space}/spaceNotificationSetting`. Note: Only the caller's user id or email is allowed in the path.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)` |   
  
### getSpaceNotificationSettingCallable()
    
    
    public final UnaryCallable<GetSpaceNotificationSettingRequest,SpaceNotificationSetting> getSpaceNotificationSettingCallable()

Gets the space notification setting. For an example, see [Get the caller's space notification setting](https://developers.google.com/workspace/chat/get-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceNotificationSettingRequest request =
           GetSpaceNotificationSettingRequest.newBuilder()
               .setName(SpaceNotificationSettingName.of("[USER]", "[SPACE]").toString())
               .build();
       ApiFuture<SpaceNotificationSetting> future =
           chatServiceClient.getSpaceNotificationSettingCallable().futureCall(request);
       // Do something.
       SpaceNotificationSetting response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceNotificationSettingRequest),[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)>` |   
  
### getSpaceReadState(@Nullable SpaceReadStateName name)
    
    
    public final SpaceReadState getSpaceReadState(@Nullable SpaceReadStateName name)

Returns details about a user's read state within a space, used to identify read and unread messages. For an example, see [Get details about a user's space read state](https://developers.google.com/workspace/chat/get-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceReadStateName name = SpaceReadStateName.of("[USER]", "[SPACE]");
       SpaceReadState response = chatServiceClient.getSpaceReadState(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceReadStateName`  
Required. Resource name of the space read state to retrieve. Only supports getting read state for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me/spaces/{space}/spaceReadState`. \- Their Workspace email address. For example, `users/user@example.com/spaces/{space}/spaceReadState`. \- Their user id. For example, `users/123456789/spaces/{space}/spaceReadState`. Format: users/{user}/spaces/{space}/spaceReadState  
**Returns**  
---  
**Type** | **Description**  
`[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)` |   
  
### getSpaceReadState(GetSpaceReadStateRequest request)
    
    
    public final SpaceReadState getSpaceReadState(GetSpaceReadStateRequest request)

Returns details about a user's read state within a space, used to identify read and unread messages. For an example, see [Get details about a user's space read state](https://developers.google.com/workspace/chat/get-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceReadStateRequest request =
           GetSpaceReadStateRequest.newBuilder()
               .setName(SpaceReadStateName.of("[USER]", "[SPACE]").toString())
               .build();
       SpaceReadState response = chatServiceClient.getSpaceReadState(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)` |   
  
### getSpaceReadState(String name)
    
    
    public final SpaceReadState getSpaceReadState(String name)

Returns details about a user's read state within a space, used to identify read and unread messages. For an example, see [Get details about a user's space read state](https://developers.google.com/workspace/chat/get-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SpaceReadStateName.of("[USER]", "[SPACE]").toString();
       SpaceReadState response = chatServiceClient.getSpaceReadState(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the space read state to retrieve. Only supports getting read state for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me/spaces/{space}/spaceReadState`. \- Their Workspace email address. For example, `users/user@example.com/spaces/{space}/spaceReadState`. \- Their user id. For example, `users/123456789/spaces/{space}/spaceReadState`. Format: users/{user}/spaces/{space}/spaceReadState  
**Returns**  
---  
**Type** | **Description**  
`[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)` |   
  
### getSpaceReadStateCallable()
    
    
    public final UnaryCallable<GetSpaceReadStateRequest,SpaceReadState> getSpaceReadStateCallable()

Returns details about a user's read state within a space, used to identify read and unread messages. For an example, see [Get details about a user's space read state](https://developers.google.com/workspace/chat/get-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetSpaceReadStateRequest request =
           GetSpaceReadStateRequest.newBuilder()
               .setName(SpaceReadStateName.of("[USER]", "[SPACE]").toString())
               .build();
       ApiFuture<SpaceReadState> future =
           chatServiceClient.getSpaceReadStateCallable().futureCall(request);
       // Do something.
       SpaceReadState response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetSpaceReadStateRequest),[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)>` |   
  
### getStub()
    
    
    public ChatServiceStub getStub()

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceStub](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.stub.ChatServiceStub)` |   
  
### getThreadReadState(@Nullable ThreadReadStateName name)
    
    
    public final ThreadReadState getThreadReadState(@Nullable ThreadReadStateName name)

Returns details about a user's read state within a thread, used to identify read and unread messages. For an example, see [Get details about a user's thread read state](https://developers.google.com/workspace/chat/get-thread-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ThreadReadStateName name = ThreadReadStateName.of("[USER]", "[SPACE]", "[THREAD]");
       ThreadReadState response = chatServiceClient.getThreadReadState(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.ThreadReadStateName`  
Required. Resource name of the thread read state to retrieve. Only supports getting read state for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me/spaces/{space}/threads/{thread}/threadReadState`. \- Their Workspace email address. For example, `users/user@example.com/spaces/{space}/threads/{thread}/threadReadState`. \- Their user id. For example, `users/123456789/spaces/{space}/threads/{thread}/threadReadState`. Format: users/{user}/spaces/{space}/threads/{thread}/threadReadState  
**Returns**  
---  
**Type** | **Description**  
`[ThreadReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState)` |   
  
### getThreadReadState(GetThreadReadStateRequest request)
    
    
    public final ThreadReadState getThreadReadState(GetThreadReadStateRequest request)

Returns details about a user's read state within a thread, used to identify read and unread messages. For an example, see [Get details about a user's thread read state](https://developers.google.com/workspace/chat/get-thread-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetThreadReadStateRequest request =
           GetThreadReadStateRequest.newBuilder()
               .setName(ThreadReadStateName.of("[USER]", "[SPACE]", "[THREAD]").toString())
               .build();
       ThreadReadState response = chatServiceClient.getThreadReadState(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GetThreadReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ThreadReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState)` |   
  
### getThreadReadState(String name)
    
    
    public final ThreadReadState getThreadReadState(String name)

Returns details about a user's read state within a thread, used to identify read and unread messages. For an example, see [Get details about a user's thread read state](https://developers.google.com/workspace/chat/get-thread-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = ThreadReadStateName.of("[USER]", "[SPACE]", "[THREAD]").toString();
       ThreadReadState response = chatServiceClient.getThreadReadState(name);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the thread read state to retrieve. Only supports getting read state for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me/spaces/{space}/threads/{thread}/threadReadState`. \- Their Workspace email address. For example, `users/user@example.com/spaces/{space}/threads/{thread}/threadReadState`. \- Their user id. For example, `users/123456789/spaces/{space}/threads/{thread}/threadReadState`. Format: users/{user}/spaces/{space}/threads/{thread}/threadReadState  
**Returns**  
---  
**Type** | **Description**  
`[ThreadReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState)` |   
  
### getThreadReadStateCallable()
    
    
    public final UnaryCallable<GetThreadReadStateRequest,ThreadReadState> getThreadReadStateCallable()

Returns details about a user's read state within a thread, used to identify read and unread messages. For an example, see [Get details about a user's thread read state](https://developers.google.com/workspace/chat/get-thread-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       GetThreadReadStateRequest request =
           GetThreadReadStateRequest.newBuilder()
               .setName(ThreadReadStateName.of("[USER]", "[SPACE]", "[THREAD]").toString())
               .build();
       ApiFuture<ThreadReadState> future =
           chatServiceClient.getThreadReadStateCallable().futureCall(request);
       // Do something.
       ThreadReadState response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[GetThreadReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.GetThreadReadStateRequest),[ThreadReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ThreadReadState)>` |   
  
### isShutdown()
    
    
    public boolean isShutdown()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isTerminated()
    
    
    public boolean isTerminated()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### listCustomEmojis()
    
    
    public final ChatServiceClient.ListCustomEmojisPagedResponse listCustomEmojis()

Lists custom emojis visible to the authenticated user.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       for (CustomEmoji element : chatServiceClient.listCustomEmojis().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListCustomEmojisPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisPagedResponse)` |   
  
### listCustomEmojis(ListCustomEmojisRequest request)
    
    
    public final ChatServiceClient.ListCustomEmojisPagedResponse listCustomEmojis(ListCustomEmojisRequest request)

Lists custom emojis visible to the authenticated user.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListCustomEmojisRequest request =
           ListCustomEmojisRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (CustomEmoji element : chatServiceClient.listCustomEmojis(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListCustomEmojisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListCustomEmojisPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisPagedResponse)` |   
  
### listCustomEmojisCallable()
    
    
    public final UnaryCallable<ListCustomEmojisRequest,ListCustomEmojisResponse> listCustomEmojisCallable()

Lists custom emojis visible to the authenticated user.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListCustomEmojisRequest request =
           ListCustomEmojisRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListCustomEmojisResponse response =
             chatServiceClient.listCustomEmojisCallable().call(request);
         for (CustomEmoji element : response.getCustomEmojisList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomEmojisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest),[ListCustomEmojisResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisResponse)>` |   
  
### listCustomEmojisPagedCallable()
    
    
    public final UnaryCallable<ListCustomEmojisRequest,ChatServiceClient.ListCustomEmojisPagedResponse> listCustomEmojisPagedCallable()

Lists custom emojis visible to the authenticated user.

Custom emojis are only available for Google Workspace accounts, and the administrator must turn custom emojis on for the organization. For more information, see [Learn about custom emojis in Google Chat](https://support.google.com/chat/answer/12800149) and [Manage custom emoji permissions](https://support.google.com/a/answer/12850085).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.customemojis.readonly>` \- `<https://www.googleapis.com/auth/chat.customemojis>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListCustomEmojisRequest request =
           ListCustomEmojisRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<CustomEmoji> future =
           chatServiceClient.listCustomEmojisPagedCallable().futureCall(request);
       // Do something.
       for (CustomEmoji element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListCustomEmojisRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListCustomEmojisRequest),[ListCustomEmojisPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListCustomEmojisPagedResponse)>` |   
  
### listMemberships(@Nullable SpaceName parent)
    
    
    public final ChatServiceClient.ListMembershipsPagedResponse listMemberships(@Nullable SpaceName parent)

Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       for (Membership element : chatServiceClient.listMemberships(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The resource name of the space for which to fetch a membership list. Format: spaces/{space}  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse)` |   
  
### listMemberships(ListMembershipsRequest request)
    
    
    public final ChatServiceClient.ListMembershipsPagedResponse listMemberships(ListMembershipsRequest request)

Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMembershipsRequest request =
           ListMembershipsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setShowGroups(true)
               .setShowInvited(true)
               .setUseAdminAccess(true)
               .build();
       for (Membership element : chatServiceClient.listMemberships(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse)` |   
  
### listMemberships(String parent)
    
    
    public final ChatServiceClient.ListMembershipsPagedResponse listMemberships(String parent)

Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       for (Membership element : chatServiceClient.listMemberships(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the space for which to fetch a membership list. Format: spaces/{space}  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse)` |   
  
### listMembershipsCallable()
    
    
    public final UnaryCallable<ListMembershipsRequest,ListMembershipsResponse> listMembershipsCallable()

Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMembershipsRequest request =
           ListMembershipsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setShowGroups(true)
               .setShowInvited(true)
               .setUseAdminAccess(true)
               .build();
       while (true) {
         ListMembershipsResponse response =
             chatServiceClient.listMembershipsCallable().call(request);
         for (Membership element : response.getMembershipsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest),[ListMembershipsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsResponse)>` |   
  
### listMembershipsPagedCallable()
    
    
    public final UnaryCallable<ListMembershipsRequest,ChatServiceClient.ListMembershipsPagedResponse> listMembershipsPagedCallable()

Lists memberships in a space. For an example, see [List users and Google Chat apps in a space](https://developers.google.com/workspace/chat/list-members). Listing memberships with [app authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) lists memberships in spaces that the Chat app has access to, but excludes Chat app memberships, including its own. Listing memberships with [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) lists memberships in spaces that the authenticated user has access to.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.bot>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` (requires [administrator approval](https://support.google.com/a?p=chat-app-auth))

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and one of the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMembershipsRequest request =
           ListMembershipsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setShowGroups(true)
               .setShowInvited(true)
               .setUseAdminAccess(true)
               .build();
       ApiFuture<Membership> future =
           chatServiceClient.listMembershipsPagedCallable().futureCall(request);
       // Do something.
       for (Membership element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMembershipsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMembershipsRequest),[ListMembershipsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMembershipsPagedResponse)>` |   
  
### listMessagePins(@Nullable SpaceName parent)
    
    
    public final ChatServiceClient.ListMessagePinsPagedResponse listMessagePins(@Nullable SpaceName parent)

Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       for (MessagePin element : chatServiceClient.listMessagePins(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The parent space which owns the collection of pinned items Format: `spaces/{space}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMessagePinsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse)` |   
  
### listMessagePins(ListMessagePinsRequest request)
    
    
    public final ChatServiceClient.ListMessagePinsPagedResponse listMessagePins(ListMessagePinsRequest request)

Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMessagePinsRequest request =
           ListMessagePinsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (MessagePin element : chatServiceClient.listMessagePins(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMessagePinsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMessagePinsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse)` |   
  
### listMessagePins(String parent)
    
    
    public final ChatServiceClient.ListMessagePinsPagedResponse listMessagePins(String parent)

Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       for (MessagePin element : chatServiceClient.listMessagePins(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent space which owns the collection of pinned items Format: `spaces/{space}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMessagePinsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse)` |   
  
### listMessagePinsCallable()
    
    
    public final UnaryCallable<ListMessagePinsRequest,ListMessagePinsResponse> listMessagePinsCallable()

Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMessagePinsRequest request =
           ListMessagePinsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListMessagePinsResponse response =
             chatServiceClient.listMessagePinsCallable().call(request);
         for (MessagePin element : response.getMessagePinsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessagePinsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest),[ListMessagePinsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsResponse)>` |   
  
### listMessagePinsPagedCallable()
    
    
    public final UnaryCallable<ListMessagePinsRequest,ChatServiceClient.ListMessagePinsPagedResponse> listMessagePinsPagedCallable()

Lists message pins in a space. Users can pin important messages in spaces for easy access. For more information, see [Pin or unpin a conversation in Google Chat](https://support.google.com/chat/answer/15622437).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.pins.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces.pins>` \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMessagePinsRequest request =
           ListMessagePinsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<MessagePin> future =
           chatServiceClient.listMessagePinsPagedCallable().futureCall(request);
       // Do something.
       for (MessagePin element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessagePinsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagePinsRequest),[ListMessagePinsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagePinsPagedResponse)>` |   
  
### listMessages(@Nullable SpaceName parent)
    
    
    public final ChatServiceClient.ListMessagesPagedResponse listMessages(@Nullable SpaceName parent)

Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope: - `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       for (Message element : chatServiceClient.listMessages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The resource name of the space to list messages from. Format: `spaces/{space}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse)` |   
  
### listMessages(ListMessagesRequest request)
    
    
    public final ChatServiceClient.ListMessagesPagedResponse listMessages(ListMessagesRequest request)

Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope: - `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMessagesRequest request =
           ListMessagesRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setShowDeleted(true)
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       for (Message element : chatServiceClient.listMessages(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse)` |   
  
### listMessages(String parent)
    
    
    public final ChatServiceClient.ListMessagesPagedResponse listMessages(String parent)

Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope: - `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       for (Message element : chatServiceClient.listMessages(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the space to list messages from. Format: `spaces/{space}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse)` |   
  
### listMessagesCallable()
    
    
    public final UnaryCallable<ListMessagesRequest,ListMessagesResponse> listMessagesCallable()

Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope: - `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMessagesRequest request =
           ListMessagesRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setShowDeleted(true)
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       while (true) {
         ListMessagesResponse response = chatServiceClient.listMessagesCallable().call(request);
         for (Message element : response.getMessagesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest),[ListMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesResponse)>` |   
  
### listMessagesPagedCallable()
    
    
    public final UnaryCallable<ListMessagesRequest,ChatServiceClient.ListMessagesPagedResponse> listMessagesPagedCallable()

Lists messages in a space that the caller is a member of, including messages from blocked members and spaces. System messages, like those announcing new space members, aren't included. If you list messages from a space with no messages, the response is an empty object. When using a REST/HTTP interface, the response contains an empty JSON object, `{}`. For an example, see [List messages](https://developers.google.com/workspace/chat/api/guides/v1/messages/list).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with the authorization scope: - `<https://www.googleapis.com/auth/chat.app.messages.readonly>`. When using this authentication scope, this method only returns public messages in a space. It doesn't include private messages.

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListMessagesRequest request =
           ListMessagesRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .setOrderBy("orderBy-1207110587")
               .setShowDeleted(true)
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       ApiFuture<Message> future = chatServiceClient.listMessagesPagedCallable().futureCall(request);
       // Do something.
       for (Message element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListMessagesRequest),[ListMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListMessagesPagedResponse)>` |   
  
### listReactions(@Nullable MessageName parent)
    
    
    public final ChatServiceClient.ListReactionsPagedResponse listReactions(@Nullable MessageName parent)

Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MessageName parent = MessageName.of("[SPACE]", "[MESSAGE]");
       for (Reaction element : chatServiceClient.listReactions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.MessageName`  
Required. The message users reacted to. Format: `spaces/{space}/messages/{message}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListReactionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse)` |   
  
### listReactions(ListReactionsRequest request)
    
    
    public final ChatServiceClient.ListReactionsPagedResponse listReactions(ListReactionsRequest request)

Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListReactionsRequest request =
           ListReactionsRequest.newBuilder()
               .setParent(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Reaction element : chatServiceClient.listReactions(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListReactionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListReactionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse)` |   
  
### listReactions(String parent)
    
    
    public final ChatServiceClient.ListReactionsPagedResponse listReactions(String parent)

Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = MessageName.of("[SPACE]", "[MESSAGE]").toString();
       for (Reaction element : chatServiceClient.listReactions(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The message users reacted to. Format: `spaces/{space}/messages/{message}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListReactionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse)` |   
  
### listReactionsCallable()
    
    
    public final UnaryCallable<ListReactionsRequest,ListReactionsResponse> listReactionsCallable()

Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListReactionsRequest request =
           ListReactionsRequest.newBuilder()
               .setParent(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListReactionsResponse response = chatServiceClient.listReactionsCallable().call(request);
         for (Reaction element : response.getReactionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReactionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest),[ListReactionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsResponse)>` |   
  
### listReactionsPagedCallable()
    
    
    public final UnaryCallable<ListReactionsRequest,ChatServiceClient.ListReactionsPagedResponse> listReactionsPagedCallable()

Lists reactions to a message. For an example, see [List reactions for a message](https://developers.google.com/workspace/chat/list-reactions).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListReactionsRequest request =
           ListReactionsRequest.newBuilder()
               .setParent(MessageName.of("[SPACE]", "[MESSAGE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Reaction> future =
           chatServiceClient.listReactionsPagedCallable().futureCall(request);
       // Do something.
       for (Reaction element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListReactionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListReactionsRequest),[ListReactionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListReactionsPagedResponse)>` |   
  
### listSectionItems(@Nullable SectionName parent)
    
    
    public final ChatServiceClient.ListSectionItemsPagedResponse listSectionItems(@Nullable SectionName parent)

Lists items in a section.

Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SectionName parent = SectionName.of("[USER]", "[SECTION]");
       for (SectionItem element : chatServiceClient.listSectionItems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SectionName`  
Required. The parent, which is the section resource name that owns this collection of section items. Only supports listing section items for the calling user. When you're filtering by space, use the wildcard `-` to search across all sections. For example, `users/{user}/sections/-`. Format: `users/{user}/sections/{section}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSectionItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse)` |   
  
### listSectionItems(ListSectionItemsRequest request)
    
    
    public final ChatServiceClient.ListSectionItemsPagedResponse listSectionItems(ListSectionItemsRequest request)

Lists items in a section.

Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSectionItemsRequest request =
           ListSectionItemsRequest.newBuilder()
               .setParent(SectionName.of("[USER]", "[SECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (SectionItem element : chatServiceClient.listSectionItems(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSectionItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSectionItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse)` |   
  
### listSectionItems(String parent)
    
    
    public final ChatServiceClient.ListSectionItemsPagedResponse listSectionItems(String parent)

Lists items in a section.

Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SectionName.of("[USER]", "[SECTION]").toString();
       for (SectionItem element : chatServiceClient.listSectionItems(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which is the section resource name that owns this collection of section items. Only supports listing section items for the calling user. When you're filtering by space, use the wildcard `-` to search across all sections. For example, `users/{user}/sections/-`. Format: `users/{user}/sections/{section}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSectionItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse)` |   
  
### listSectionItemsCallable()
    
    
    public final UnaryCallable<ListSectionItemsRequest,ListSectionItemsResponse> listSectionItemsCallable()

Lists items in a section.

Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSectionItemsRequest request =
           ListSectionItemsRequest.newBuilder()
               .setParent(SectionName.of("[USER]", "[SECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListSectionItemsResponse response =
             chatServiceClient.listSectionItemsCallable().call(request);
         for (SectionItem element : response.getSectionItemsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSectionItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest),[ListSectionItemsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsResponse)>` |   
  
### listSectionItemsPagedCallable()
    
    
    public final UnaryCallable<ListSectionItemsRequest,ChatServiceClient.ListSectionItemsPagedResponse> listSectionItemsPagedCallable()

Lists items in a section.

Only spaces can be section items. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSectionItemsRequest request =
           ListSectionItemsRequest.newBuilder()
               .setParent(SectionName.of("[USER]", "[SECTION]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<SectionItem> future =
           chatServiceClient.listSectionItemsPagedCallable().futureCall(request);
       // Do something.
       for (SectionItem element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSectionItemsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionItemsRequest),[ListSectionItemsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionItemsPagedResponse)>` |   
  
### listSections(@Nullable UserName parent)
    
    
    public final ChatServiceClient.ListSectionsPagedResponse listSections(@Nullable UserName parent)

Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UserName parent = UserName.of("[USER]");
       for (Section element : chatServiceClient.listSections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.UserName`  
Required. The parent, which is the user resource name that owns this collection of sections. Only supports listing sections for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me`. \- Their Workspace email address. For example, `users/user@example.com`. \- Their user id. For example, `users/123456789`. Format: `users/{user}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse)` |   
  
### listSections(ListSectionsRequest request)
    
    
    public final ChatServiceClient.ListSectionsPagedResponse listSections(ListSectionsRequest request)

Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSectionsRequest request =
           ListSectionsRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       for (Section element : chatServiceClient.listSections(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse)` |   
  
### listSections(String parent)
    
    
    public final ChatServiceClient.ListSectionsPagedResponse listSections(String parent)

Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = UserName.of("[USER]").toString();
       for (Section element : chatServiceClient.listSections(parent).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The parent, which is the user resource name that owns this collection of sections. Only supports listing sections for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me`. \- Their Workspace email address. For example, `users/user@example.com`. \- Their user id. For example, `users/123456789`. Format: `users/{user}`  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse)` |   
  
### listSectionsCallable()
    
    
    public final UnaryCallable<ListSectionsRequest,ListSectionsResponse> listSectionsCallable()

Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSectionsRequest request =
           ListSectionsRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       while (true) {
         ListSectionsResponse response = chatServiceClient.listSectionsCallable().call(request);
         for (Section element : response.getSectionsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest),[ListSectionsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsResponse)>` |   
  
### listSectionsPagedCallable()
    
    
    public final UnaryCallable<ListSectionsRequest,ChatServiceClient.ListSectionsPagedResponse> listSectionsPagedCallable()

Lists sections available to the Chat user. Sections help users group their conversations and customize the list of spaces displayed in Chat navigation panel. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>` \- `<https://www.googleapis.com/auth/chat.users.sections.readonly>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSectionsRequest request =
           ListSectionsRequest.newBuilder()
               .setParent(UserName.of("[USER]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .build();
       ApiFuture<Section> future = chatServiceClient.listSectionsPagedCallable().futureCall(request);
       // Do something.
       for (Section element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSectionsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSectionsRequest),[ListSectionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSectionsPagedResponse)>` |   
  
### listSpaceEvents(@Nullable SpaceName parent, String filter)
    
    
    public final ChatServiceClient.ListSpaceEventsPagedResponse listSpaceEvents(@Nullable SpaceName parent, String filter)

Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To list events, the authenticated caller must be a member of the space.

For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       String filter = "filter-1274492040";
       for (SpaceEvent element : chatServiceClient.listSpaceEvents(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. Resource name of the [Google Chat space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) where the events occurred. Format: `spaces/{space}`.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A query filter. You must specify at least one event type (`event_type`) using the has `:` operator. To filter by multiple event types, use the `OR` operator. Omit batch event types in your filter. The request automatically returns any related batch events. For example, if you filter by new reactions (`google.workspace.chat.reaction.v1.created`), the server also returns batch new reactions events (`google.workspace.chat.reaction.v1.batchCreated`). For a list of supported event types, see the [`SpaceEvents` reference documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.event_type). Optionally, you can also filter by start time (`start_time`) and end time (`end_time`): 

  * `start_time`: Exclusive timestamp from which to start listing space events. You can list events that occurred up to 28 days ago. If unspecified, lists space events from the past 28 days. 
  * `end_time`: Inclusive timestamp until which space events are listed. If unspecified, lists events up to the time of the request. 

To specify a start or end time, use the equals `=` operator and format in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339). To filter by both `start_time` and `end_time`, use the `AND` operator. For example, the following queries are valid: ``<code> start_time="2023-08-23T19:20:33+00:00" AND end_time="2023-08-23T19:21:54+00:00" </code>`` ``<code> start_time="2023-08-23T19:20:33+00:00" AND (event_types:"google.workspace.chat.space.v1.updated" OR event_types:"google.workspace.chat.message.v1.created") </code>`` ``The following queries are invalid: ``<code> start_time="2023-08-23T19:20:33+00:00" OR end_time="2023-08-23T19:21:54+00:00" </code>`` ``<code> event_types:"google.workspace.chat.space.v1.updated" AND event_types:"google.workspace.chat.message.v1.created" </code>`` ``Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSpaceEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse)` |   
  
### listSpaceEvents(ListSpaceEventsRequest request)
    
    
    public final ChatServiceClient.ListSpaceEventsPagedResponse listSpaceEvents(ListSpaceEventsRequest request)

Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To list events, the authenticated caller must be a member of the space.

For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSpaceEventsRequest request =
           ListSpaceEventsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (SpaceEvent element : chatServiceClient.listSpaceEvents(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSpaceEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSpaceEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse)` |   
  
### listSpaceEvents(String parent, String filter)
    
    
    public final ChatServiceClient.ListSpaceEventsPagedResponse listSpaceEvents(String parent, String filter)

Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To list events, the authenticated caller must be a member of the space.

For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       String filter = "filter-1274492040";
       for (SpaceEvent element : chatServiceClient.listSpaceEvents(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. Resource name of the [Google Chat space](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces) where the events occurred. Format: `spaces/{space}`.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A query filter. You must specify at least one event type (`event_type`) using the has `:` operator. To filter by multiple event types, use the `OR` operator. Omit batch event types in your filter. The request automatically returns any related batch events. For example, if you filter by new reactions (`google.workspace.chat.reaction.v1.created`), the server also returns batch new reactions events (`google.workspace.chat.reaction.v1.batchCreated`). For a list of supported event types, see the [`SpaceEvents` reference documentation](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.event_type). Optionally, you can also filter by start time (`start_time`) and end time (`end_time`): 

  * `start_time`: Exclusive timestamp from which to start listing space events. You can list events that occurred up to 28 days ago. If unspecified, lists space events from the past 28 days. 
  * `end_time`: Inclusive timestamp until which space events are listed. If unspecified, lists events up to the time of the request. 

To specify a start or end time, use the equals `=` operator and format in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339). To filter by both `start_time` and `end_time`, use the `AND` operator. For example, the following queries are valid: ``<code> start_time="2023-08-23T19:20:33+00:00" AND end_time="2023-08-23T19:21:54+00:00" </code>`` ``<code> start_time="2023-08-23T19:20:33+00:00" AND (event_types:"google.workspace.chat.space.v1.updated" OR event_types:"google.workspace.chat.message.v1.created") </code>`` ``The following queries are invalid: ``<code> start_time="2023-08-23T19:20:33+00:00" OR end_time="2023-08-23T19:21:54+00:00" </code>`` ``<code> event_types:"google.workspace.chat.space.v1.updated" AND event_types:"google.workspace.chat.message.v1.created" </code>`` ``Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSpaceEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse)` |   
  
### listSpaceEventsCallable()
    
    
    public final UnaryCallable<ListSpaceEventsRequest,ListSpaceEventsResponse> listSpaceEventsCallable()

Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To list events, the authenticated caller must be a member of the space.

For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSpaceEventsRequest request =
           ListSpaceEventsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListSpaceEventsResponse response =
             chatServiceClient.listSpaceEventsCallable().call(request);
         for (SpaceEvent element : response.getSpaceEventsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpaceEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest),[ListSpaceEventsResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsResponse)>` |   
  
### listSpaceEventsPagedCallable()
    
    
    public final UnaryCallable<ListSpaceEventsRequest,ChatServiceClient.ListSpaceEventsPagedResponse> listSpaceEventsPagedCallable()

Lists events from a Google Chat space. For each event, the [payload](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces.spaceEvents#SpaceEvent.FIELDS.oneof_payload) contains the most recent version of the Chat resource. For example, if you list events about new space members, the server returns `Membership` resources that contain the latest membership details. If new members were removed during the requested period, the event payload contains an empty `Membership` resource.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize) with an [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes) appropriate for reading the requested data:

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>` \- `<https://www.googleapis.com/auth/chat.app.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.app.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.app.memberships>` \- `<https://www.googleapis.com/auth/chat.app.memberships.readonly>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` \- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.messages.reactions.readonly>` \- `<https://www.googleapis.com/auth/chat.messages.reactions>` \- `<https://www.googleapis.com/auth/chat.memberships.readonly>` \- `<https://www.googleapis.com/auth/chat.memberships>`

To list events, the authenticated caller must be a member of the space.

For an example, see [List events from a Google Chat space](https://developers.google.com/workspace/chat/list-space-events).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSpaceEventsRequest request =
           ListSpaceEventsRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<SpaceEvent> future =
           chatServiceClient.listSpaceEventsPagedCallable().futureCall(request);
       // Do something.
       for (SpaceEvent element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpaceEventsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpaceEventsRequest),[ListSpaceEventsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpaceEventsPagedResponse)>` |   
  
### listSpaces()
    
    
    public final ChatServiceClient.ListSpacesPagedResponse listSpaces()

Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/workspace/chat/list-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

To list all named spaces by Google Workspace organization, use the [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search) method using Workspace administrator privileges instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       for (Space element : chatServiceClient.listSpaces().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesPagedResponse)` |   
  
### listSpaces(ListSpacesRequest request)
    
    
    public final ChatServiceClient.ListSpacesPagedResponse listSpaces(ListSpacesRequest request)

Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/workspace/chat/list-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

To list all named spaces by Google Workspace organization, use the [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search) method using Workspace administrator privileges instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSpacesRequest request =
           ListSpacesRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       for (Space element : chatServiceClient.listSpaces(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[ListSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.ListSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesPagedResponse)` |   
  
### listSpacesCallable()
    
    
    public final UnaryCallable<ListSpacesRequest,ListSpacesResponse> listSpacesCallable()

Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/workspace/chat/list-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

To list all named spaces by Google Workspace organization, use the [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search) method using Workspace administrator privileges instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSpacesRequest request =
           ListSpacesRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       while (true) {
         ListSpacesResponse response = chatServiceClient.listSpacesCallable().call(request);
         for (Space element : response.getSpacesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest),[ListSpacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesResponse)>` |   
  
### listSpacesPagedCallable()
    
    
    public final UnaryCallable<ListSpacesRequest,ChatServiceClient.ListSpacesPagedResponse> listSpacesPagedCallable()

Lists spaces the caller is a member of. Group chats and DMs aren't listed until the first message is sent. For an example, see [List spaces](https://developers.google.com/workspace/chat/list-spaces).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

To list all named spaces by Google Workspace organization, use the [`spaces.search()`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces/search) method using Workspace administrator privileges instead.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       ListSpacesRequest request =
           ListSpacesRequest.newBuilder()
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setFilter("filter-1274492040")
               .build();
       ApiFuture<Space> future = chatServiceClient.listSpacesPagedCallable().futureCall(request);
       // Do something.
       for (Space element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[ListSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ListSpacesRequest),[ListSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.ListSpacesPagedResponse)>` |   
  
### markAsActive(MarkAsActiveRequest request)
    
    
    public final Availability markAsActive(MarkAsActiveRequest request)

Marks user as `ACTIVE` in Google Chat.

Sets the user's availability state to `ACTIVE`. The `ACTIVE` state lasts until the specified expiration, at which point the user's state becomes `AWAY`. Note that if the user is actively using Chat, the `ACTIVE` state duration may extend beyond the provided expiration.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MarkAsActiveRequest request =
           MarkAsActiveRequest.newBuilder()
               .setName(AvailabilityName.of("[USER]").toString())
               .build();
       Availability response = chatServiceClient.markAsActive(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkAsActiveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### markAsActiveCallable()
    
    
    public final UnaryCallable<MarkAsActiveRequest,Availability> markAsActiveCallable()

Marks user as `ACTIVE` in Google Chat.

Sets the user's availability state to `ACTIVE`. The `ACTIVE` state lasts until the specified expiration, at which point the user's state becomes `AWAY`. Note that if the user is actively using Chat, the `ACTIVE` state duration may extend beyond the provided expiration.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MarkAsActiveRequest request =
           MarkAsActiveRequest.newBuilder()
               .setName(AvailabilityName.of("[USER]").toString())
               .build();
       ApiFuture<Availability> future = chatServiceClient.markAsActiveCallable().futureCall(request);
       // Do something.
       Availability response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkAsActiveRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsActiveRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### markAsAway(MarkAsAwayRequest request)
    
    
    public final Availability markAsAway(MarkAsAwayRequest request)

Marks user as `AWAY` in Google Chat.

Sets the user's state to away and is not affected by the user's activity.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MarkAsAwayRequest request =
           MarkAsAwayRequest.newBuilder().setName(AvailabilityName.of("[USER]").toString()).build();
       Availability response = chatServiceClient.markAsAway(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkAsAwayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### markAsAwayCallable()
    
    
    public final UnaryCallable<MarkAsAwayRequest,Availability> markAsAwayCallable()

Marks user as `AWAY` in Google Chat.

Sets the user's state to away and is not affected by the user's activity.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MarkAsAwayRequest request =
           MarkAsAwayRequest.newBuilder().setName(AvailabilityName.of("[USER]").toString()).build();
       ApiFuture<Availability> future = chatServiceClient.markAsAwayCallable().futureCall(request);
       // Do something.
       Availability response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkAsAwayRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsAwayRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### markAsDoNotDisturb(MarkAsDoNotDisturbRequest request)
    
    
    public final Availability markAsDoNotDisturb(MarkAsDoNotDisturbRequest request)

Marks user as `DO_NOT_DISTURB` in Google Chat.

Sets a user's availability state to `DO_NOT_DISTURB` until a specified expiration time. When in `DO_NOT_DISTURB`, users typically won't receive notifications.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MarkAsDoNotDisturbRequest request =
           MarkAsDoNotDisturbRequest.newBuilder()
               .setName(AvailabilityName.of("[USER]").toString())
               .build();
       Availability response = chatServiceClient.markAsDoNotDisturb(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MarkAsDoNotDisturbRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### markAsDoNotDisturbCallable()
    
    
    public final UnaryCallable<MarkAsDoNotDisturbRequest,Availability> markAsDoNotDisturbCallable()

Marks user as `DO_NOT_DISTURB` in Google Chat.

Sets a user's availability state to `DO_NOT_DISTURB` until a specified expiration time. When in `DO_NOT_DISTURB`, users typically won't receive notifications.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MarkAsDoNotDisturbRequest request =
           MarkAsDoNotDisturbRequest.newBuilder()
               .setName(AvailabilityName.of("[USER]").toString())
               .build();
       ApiFuture<Availability> future =
           chatServiceClient.markAsDoNotDisturbCallable().futureCall(request);
       // Do something.
       Availability response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MarkAsDoNotDisturbRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MarkAsDoNotDisturbRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### moveSectionItem(@Nullable SectionItemName name, @Nullable SectionName targetSection)
    
    
    public final MoveSectionItemResponse moveSectionItem(@Nullable SectionItemName name, @Nullable SectionName targetSection)

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SectionItemName name = SectionItemName.of("[USER]", "[SECTION]", "[ITEM]");
       SectionName targetSection = SectionName.of("[USER]", "[SECTION]");
       MoveSectionItemResponse response = chatServiceClient.moveSectionItem(name, targetSection);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SectionItemName`  
Required. The resource name of the section item to move. Format: `users/{user}/sections/{section}/items/{item}`  
`targetSection` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SectionName`  
Required. The resource name of the section to move the section item to. Format: `users/{user}/sections/{section}`  
**Returns**  
---  
**Type** | **Description**  
`[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)` |   
  
### moveSectionItem(@Nullable SectionItemName name, String targetSection)
    
    
    public final MoveSectionItemResponse moveSectionItem(@Nullable SectionItemName name, String targetSection)

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SectionItemName name = SectionItemName.of("[USER]", "[SECTION]", "[ITEM]");
       String targetSection = SectionName.of("[USER]", "[SECTION]").toString();
       MoveSectionItemResponse response = chatServiceClient.moveSectionItem(name, targetSection);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SectionItemName`  
Required. The resource name of the section item to move. Format: `users/{user}/sections/{section}/items/{item}`  
`targetSection` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the section to move the section item to. Format: `users/{user}/sections/{section}`  
**Returns**  
---  
**Type** | **Description**  
`[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)` |   
  
### moveSectionItem(MoveSectionItemRequest request)
    
    
    public final MoveSectionItemResponse moveSectionItem(MoveSectionItemRequest request)

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MoveSectionItemRequest request =
           MoveSectionItemRequest.newBuilder()
               .setName(SectionItemName.of("[USER]", "[SECTION]", "[ITEM]").toString())
               .setTargetSection(SectionName.of("[USER]", "[SECTION]").toString())
               .build();
       MoveSectionItemResponse response = chatServiceClient.moveSectionItem(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[MoveSectionItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)` |   
  
### moveSectionItem(String name, @Nullable SectionName targetSection)
    
    
    public final MoveSectionItemResponse moveSectionItem(String name, @Nullable SectionName targetSection)

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SectionItemName.of("[USER]", "[SECTION]", "[ITEM]").toString();
       SectionName targetSection = SectionName.of("[USER]", "[SECTION]");
       MoveSectionItemResponse response = chatServiceClient.moveSectionItem(name, targetSection);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the section item to move. Format: `users/{user}/sections/{section}/items/{item}`  
`targetSection` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SectionName`  
Required. The resource name of the section to move the section item to. Format: `users/{user}/sections/{section}`  
**Returns**  
---  
**Type** | **Description**  
`[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)` |   
  
### moveSectionItem(String name, String targetSection)
    
    
    public final MoveSectionItemResponse moveSectionItem(String name, String targetSection)

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String name = SectionItemName.of("[USER]", "[SECTION]", "[ITEM]").toString();
       String targetSection = SectionName.of("[USER]", "[SECTION]").toString();
       MoveSectionItemResponse response = chatServiceClient.moveSectionItem(name, targetSection);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the section item to move. Format: `users/{user}/sections/{section}/items/{item}`  
`targetSection` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the section to move the section item to. Format: `users/{user}/sections/{section}`  
**Returns**  
---  
**Type** | **Description**  
`[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)` |   
  
### moveSectionItemCallable()
    
    
    public final UnaryCallable<MoveSectionItemRequest,MoveSectionItemResponse> moveSectionItemCallable()

Moves an item from one section to another. For example, if a section contains spaces, this method can be used to move a space to a different section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       MoveSectionItemRequest request =
           MoveSectionItemRequest.newBuilder()
               .setName(SectionItemName.of("[USER]", "[SECTION]", "[ITEM]").toString())
               .setTargetSection(SectionName.of("[USER]", "[SECTION]").toString())
               .build();
       ApiFuture<MoveSectionItemResponse> future =
           chatServiceClient.moveSectionItemCallable().futureCall(request);
       // Do something.
       MoveSectionItemResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[MoveSectionItemRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemRequest),[MoveSectionItemResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.MoveSectionItemResponse)>` |   
  
### positionSection(PositionSectionRequest request)
    
    
    public final PositionSectionResponse positionSection(PositionSectionRequest request)

Changes the sort order of a section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       PositionSectionRequest request =
           PositionSectionRequest.newBuilder()
               .setName(SectionName.of("[USER]", "[SECTION]").toString())
               .build();
       PositionSectionResponse response = chatServiceClient.positionSection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[PositionSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[PositionSectionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponse)` |   
  
### positionSectionCallable()
    
    
    public final UnaryCallable<PositionSectionRequest,PositionSectionResponse> positionSectionCallable()

Changes the sort order of a section. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       PositionSectionRequest request =
           PositionSectionRequest.newBuilder()
               .setName(SectionName.of("[USER]", "[SECTION]").toString())
               .build();
       ApiFuture<PositionSectionResponse> future =
           chatServiceClient.positionSectionCallable().futureCall(request);
       // Do something.
       PositionSectionResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[PositionSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionRequest),[PositionSectionResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.PositionSectionResponse)>` |   
  
### searchMessages(@Nullable SpaceName parent, String filter)
    
    
    public final ChatServiceClient.SearchMessagesPagedResponse searchMessages(@Nullable SpaceName parent, String filter)

Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria.

To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides.

This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.

\- Private Messages that are visible to the authenticated user. - Messages posted by Chat apps in spaces or group chats. - Messages in a Chat app DM. - Messages from blocked users. - Messages in spaces that the caller has muted.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceName parent = SpaceName.of("[SPACE]");
       String filter = "filter-1274492040";
       for (SearchMessageResult element :
           chatServiceClient.searchMessages(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `@org.jspecify.annotations.Nullable com.google.chat.v1.SpaceName`  
Required. The resource name of the space to search within. To search across all spaces the user has access to, set this field to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. To limit the search to one or more spaces, use `space.name` or `space.display_name` in the `filter`.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A search query. The query can specify one or more search keywords, which are used to filter the results, You can also filter the results using the following message fields: \- `create_time`: Accepts a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `<` and `>=`. - `sender.name`: The resource name of the sender (`users/{user}`). Only supports `=`. You can use the e-mail as an alias for `{user}`. For example, `users/example@gmail.com`, where `example@gmail.com` is the e-mail of the Google Chat user. - `space.name`: The resource name of the space where the message is posted. (`spaces/{space}`). Only supports `=`. If this filter is not set, the search is performed across all direct messages and spaces the user has access to as a space member. - `space.display_name`: Supports the operator `:` (has) and filters spaces based on a partial match of their display name. Results are limited to the top five space matches. For example, `space.display_name:Project` searches for messages in the top five spaces that contain the word "Project" in their display names. - `space.space_type`: The type of the space. Only supports `=`. For example, `space.space_type="DIRECT_MESSAGE"` returns only messages from direct messages. The possible values are `DIRECT_MESSAGE`, `GROUP_CHAT`, and `SPACE`. - `attachment`: Supports the operator `:*` (has any) to check for the presence of attachments. If `attachment:*` is specified, only messages that have at least one attachment are returned. - `annotations.user_mentions.user.name`: The resource name of the mentioned user (`users/{user}`). Only supports `:` (has). For example: `annotations.user_mentions.user.name:"users/1234567890"` returns only messages that contain a mention to the specified user. Alternatively, the alias `me` can be used to filter for messages that mention the caller user, for example: `annotations.user_mentions.user.name:users/me`. You can also use the e-mail as an alias for `{user}`, for example, `users/example@gmail.com`. For advanced filtering, the following functions are also available: \- `has_link()`: Returns only messages that have at least one hyperlink in the message text. - `is_unread()`: Filters out messages that have been read by the calling user. Using the `space.display_name` or the `space.space_type` filters requires that the calling credentials include one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` Using the `is_unread()` filter requires that the calling credentials include one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): \- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>` Across different fields, only `AND` operators are supported. A valid example is `sender.name = "users/1234567890" AND is_unread()`. The word `AND` is optional and is implied if omitted. For example, `sender.name = "users/1234567890" is_unread()` is valid and is equivalent to the previous example. An invalid example is `sender.name = "users/1234567890" OR is_unread()` because `OR` is not supported between different fields. Among the same field: \- `create_time` supports only `AND`, and can only be used to represent an interval, such as `create_time >= "2022-01-01T00:00:00+00:00" AND create_time < "2023-01-01T00:00:00+00:00"`. - `sender.name` supports only the `OR` operator, for example: `sender.name = "users/1234567890" OR sender.name = "users/0987654321"`. - `space.name` supports only the `OR` operator, for example: `space.name = "spaces/ABCDEFGH" OR space.name = "spaces/QWERTYUI"`. - `space.display_name` supports the operators `AND` and `OR`, but not a mix of both. For example: `space.display_name:Project AND space.display_name:Tasks` returns messages that are in spaces with display names containing both `Project` and `Tasks`, whereas `space.display_name:Project OR space.display_name:Tasks` returns messages that are in spaces with display names containing either `Project` or `Tasks` or both. - `space.space_type` supports only the `OR` operator, for example: `space.space_type = "DIRECT_MESSAGE" OR space.space_type = "GROUP_CHAT"`. - `annotations.user_mentions.user.name` supports the operators `AND` and `OR`, but not a mix of both. For example: `annotations.user_mentions.user.name:"users/1234567890" AND annotations.user_mentions.user.name:"users/0987654321"` returns only messages that mentions both users, whereas `annotations.user_mentions.user.name:"users/1234567890" OR annotations.user_mentions.user.name:"users/0987654321"` returns messages that mention either user or both. Parentheses are required to disambiguate operator precedence when combining `AND` and `OR` operators in the same query. For example: `(sender.name="users/me" OR sender.name="users/123456") AND is_unread()`. Otherwise, parentheses are optional. The following example queries are valid: ``<code> "Pending reports" AND create_time &gt;= "2023-01-01T00:00:00Z" <p>sender.name = "users/example@gmail.com" <p>annotations.user_mentions.user.name:"users/0987654321" <p>attachment:&#42; AND space.name = "spaces/ABCDEFGH" <p>tasks AND is_unread() AND sender.name = "users/1234567890" <p>"things to do" "urgent" <p>(sender.name = "users/1234567890") AND (create_time &lt; "2023-05-01T00:00:00Z") <p>tasks AND space.name = "spaces/ABCDEFGH" AND has_link() <p>"project one" is_unread() <p>space.display_name:Project tasks </code>`` ``The maximum query length is 1,000 characters. ``Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.SearchMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse)` |   
  
### searchMessages(SearchMessagesRequest request)
    
    
    public final ChatServiceClient.SearchMessagesPagedResponse searchMessages(SearchMessagesRequest request)

Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria.

To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides.

This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.

\- Private Messages that are visible to the authenticated user. - Messages posted by Chat apps in spaces or group chats. - Messages in a Chat app DM. - Messages from blocked users. - Messages in spaces that the caller has muted.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SearchMessagesRequest request =
           SearchMessagesRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       for (SearchMessageResult element : chatServiceClient.searchMessages(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.SearchMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse)` |   
  
### searchMessages(String parent, String filter)
    
    
    public final ChatServiceClient.SearchMessagesPagedResponse searchMessages(String parent, String filter)

Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria.

To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides.

This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.

\- Private Messages that are visible to the authenticated user. - Messages posted by Chat apps in spaces or group chats. - Messages in a Chat app DM. - Messages from blocked users. - Messages in spaces that the caller has muted.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       String parent = SpaceName.of("[SPACE]").toString();
       String filter = "filter-1274492040";
       for (SearchMessageResult element :
           chatServiceClient.searchMessages(parent, filter).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. The resource name of the space to search within. To search across all spaces the user has access to, set this field to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. To limit the search to one or more spaces, use `space.name` or `space.display_name` in the `filter`.  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Required. A search query. The query can specify one or more search keywords, which are used to filter the results, You can also filter the results using the following message fields: \- `create_time`: Accepts a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `<` and `>=`. - `sender.name`: The resource name of the sender (`users/{user}`). Only supports `=`. You can use the e-mail as an alias for `{user}`. For example, `users/example@gmail.com`, where `example@gmail.com` is the e-mail of the Google Chat user. - `space.name`: The resource name of the space where the message is posted. (`spaces/{space}`). Only supports `=`. If this filter is not set, the search is performed across all direct messages and spaces the user has access to as a space member. - `space.display_name`: Supports the operator `:` (has) and filters spaces based on a partial match of their display name. Results are limited to the top five space matches. For example, `space.display_name:Project` searches for messages in the top five spaces that contain the word "Project" in their display names. - `space.space_type`: The type of the space. Only supports `=`. For example, `space.space_type="DIRECT_MESSAGE"` returns only messages from direct messages. The possible values are `DIRECT_MESSAGE`, `GROUP_CHAT`, and `SPACE`. - `attachment`: Supports the operator `:*` (has any) to check for the presence of attachments. If `attachment:*` is specified, only messages that have at least one attachment are returned. - `annotations.user_mentions.user.name`: The resource name of the mentioned user (`users/{user}`). Only supports `:` (has). For example: `annotations.user_mentions.user.name:"users/1234567890"` returns only messages that contain a mention to the specified user. Alternatively, the alias `me` can be used to filter for messages that mention the caller user, for example: `annotations.user_mentions.user.name:users/me`. You can also use the e-mail as an alias for `{user}`, for example, `users/example@gmail.com`. For advanced filtering, the following functions are also available: \- `has_link()`: Returns only messages that have at least one hyperlink in the message text. - `is_unread()`: Filters out messages that have been read by the calling user. Using the `space.display_name` or the `space.space_type` filters requires that the calling credentials include one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): \- `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>` Using the `is_unread()` filter requires that the calling credentials include one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): \- `<https://www.googleapis.com/auth/chat.users.readstate.readonly>` \- `<https://www.googleapis.com/auth/chat.users.readstate>` Across different fields, only `AND` operators are supported. A valid example is `sender.name = "users/1234567890" AND is_unread()`. The word `AND` is optional and is implied if omitted. For example, `sender.name = "users/1234567890" is_unread()` is valid and is equivalent to the previous example. An invalid example is `sender.name = "users/1234567890" OR is_unread()` because `OR` is not supported between different fields. Among the same field: \- `create_time` supports only `AND`, and can only be used to represent an interval, such as `create_time >= "2022-01-01T00:00:00+00:00" AND create_time < "2023-01-01T00:00:00+00:00"`. - `sender.name` supports only the `OR` operator, for example: `sender.name = "users/1234567890" OR sender.name = "users/0987654321"`. - `space.name` supports only the `OR` operator, for example: `space.name = "spaces/ABCDEFGH" OR space.name = "spaces/QWERTYUI"`. - `space.display_name` supports the operators `AND` and `OR`, but not a mix of both. For example: `space.display_name:Project AND space.display_name:Tasks` returns messages that are in spaces with display names containing both `Project` and `Tasks`, whereas `space.display_name:Project OR space.display_name:Tasks` returns messages that are in spaces with display names containing either `Project` or `Tasks` or both. - `space.space_type` supports only the `OR` operator, for example: `space.space_type = "DIRECT_MESSAGE" OR space.space_type = "GROUP_CHAT"`. - `annotations.user_mentions.user.name` supports the operators `AND` and `OR`, but not a mix of both. For example: `annotations.user_mentions.user.name:"users/1234567890" AND annotations.user_mentions.user.name:"users/0987654321"` returns only messages that mentions both users, whereas `annotations.user_mentions.user.name:"users/1234567890" OR annotations.user_mentions.user.name:"users/0987654321"` returns messages that mention either user or both. Parentheses are required to disambiguate operator precedence when combining `AND` and `OR` operators in the same query. For example: `(sender.name="users/me" OR sender.name="users/123456") AND is_unread()`. Otherwise, parentheses are optional. The following example queries are valid: ``<code> "Pending reports" AND create_time &gt;= "2023-01-01T00:00:00Z" <p>sender.name = "users/example@gmail.com" <p>annotations.user_mentions.user.name:"users/0987654321" <p>attachment:&#42; AND space.name = "spaces/ABCDEFGH" <p>tasks AND is_unread() AND sender.name = "users/1234567890" <p>"things to do" "urgent" <p>(sender.name = "users/1234567890") AND (create_time &lt; "2023-05-01T00:00:00Z") <p>tasks AND space.name = "spaces/ABCDEFGH" AND has_link() <p>"project one" is_unread() <p>space.display_name:Project tasks </code>`` ``The maximum query length is 1,000 characters. ``Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.SearchMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse)` |   
  
### searchMessagesCallable()
    
    
    public final UnaryCallable<SearchMessagesRequest,SearchMessagesResponse> searchMessagesCallable()

Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria.

To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides.

This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.

\- Private Messages that are visible to the authenticated user. - Messages posted by Chat apps in spaces or group chats. - Messages in a Chat app DM. - Messages from blocked users. - Messages in spaces that the caller has muted.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SearchMessagesRequest request =
           SearchMessagesRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       while (true) {
         SearchMessagesResponse response = chatServiceClient.searchMessagesCallable().call(request);
         for (SearchMessageResult element : response.getResultsList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest),[SearchMessagesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesResponse)>` |   
  
### searchMessagesPagedCallable()
    
    
    public final UnaryCallable<SearchMessagesRequest,ChatServiceClient.SearchMessagesPagedResponse> searchMessagesPagedCallable()

Searches for messages in Google Chat that the calling user has access to. Returns a list of messages matching the search criteria.

To search across all spaces the user has access to, set `parent` to `spaces/-`. Using any other value for `parent` results in an `INVALID_ARGUMENT` error. The returned messages have their `name` field populated with the full resource name, which includes the specific `space` in which the message resides.

This API doesn't return all message types. The types of messages listed below aren't included in the response. Use ListMessages to list all messages.

\- Private Messages that are visible to the authenticated user. - Messages posted by Chat apps in spaces or group chats. - Messages in a Chat app DM. - Messages from blocked users. - Messages in spaces that the caller has muted.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.readonly>` \- `<https://www.googleapis.com/auth/chat.messages>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SearchMessagesRequest request =
           SearchMessagesRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setFilter("filter-1274492040")
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setOrderBy("orderBy-1207110587")
               .setMarkupSyntax(MarkupSyntax.forNumber(0))
               .build();
       ApiFuture<SearchMessageResult> future =
           chatServiceClient.searchMessagesPagedCallable().futureCall(request);
       // Do something.
       for (SearchMessageResult element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchMessagesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchMessagesRequest),[SearchMessagesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchMessagesPagedResponse)>` |   
  
### searchSpaces()
    
    
    public final ChatServiceClient.SearchSpacesPagedResponse searchSpaces()

Returns a list of spaces in a Google Workspace organization. For an example, see [Search for and manage spaces](https://developers.google.com/workspace/chat/search-manage-admin).

When `use_admin_access` is set to `false`, the results are limited to spaces where the calling user is a joined member. To search with administrator privileges, set `use_admin_access` to `true`.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

\- [User authentication with administrator privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges) and one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       for (Space element : chatServiceClient.searchSpaces().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.SearchSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesPagedResponse)` |   
  
### searchSpaces(SearchSpacesRequest request)
    
    
    public final ChatServiceClient.SearchSpacesPagedResponse searchSpaces(SearchSpacesRequest request)

Returns a list of spaces in a Google Workspace organization. For an example, see [Search for and manage spaces](https://developers.google.com/workspace/chat/search-manage-admin).

When `use_admin_access` is set to `false`, the results are limited to spaces where the calling user is a joined member. To search with administrator privileges, set `use_admin_access` to `true`.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

\- [User authentication with administrator privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges) and one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SearchSpacesRequest request =
           SearchSpacesRequest.newBuilder()
               .setUseAdminAccess(true)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setQuery("query107944136")
               .setOrderBy("orderBy-1207110587")
               .build();
       for (Space element : chatServiceClient.searchSpaces(request).iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[ChatServiceClient.SearchSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesPagedResponse)` |   
  
### searchSpacesCallable()
    
    
    public final UnaryCallable<SearchSpacesRequest,SearchSpacesResponse> searchSpacesCallable()

Returns a list of spaces in a Google Workspace organization. For an example, see [Search for and manage spaces](https://developers.google.com/workspace/chat/search-manage-admin).

When `use_admin_access` is set to `false`, the results are limited to spaces where the calling user is a joined member. To search with administrator privileges, set `use_admin_access` to `true`.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

\- [User authentication with administrator privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges) and one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SearchSpacesRequest request =
           SearchSpacesRequest.newBuilder()
               .setUseAdminAccess(true)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setQuery("query107944136")
               .setOrderBy("orderBy-1207110587")
               .build();
       while (true) {
         SearchSpacesResponse response = chatServiceClient.searchSpacesCallable().call(request);
         for (Space element : response.getSpacesList()) {
           // doThingsWith(element);
         }
         String nextPageToken = response.getNextPageToken();
         if (!Strings.isNullOrEmpty(nextPageToken)) {
           request = request.toBuilder().setPageToken(nextPageToken).build();
         } else {
           break;
         }
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest),[SearchSpacesResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesResponse)>` |   
  
### searchSpacesPagedCallable()
    
    
    public final UnaryCallable<SearchSpacesRequest,ChatServiceClient.SearchSpacesPagedResponse> searchSpacesPagedCallable()

Returns a list of spaces in a Google Workspace organization. For an example, see [Search for and manage spaces](https://developers.google.com/workspace/chat/search-manage-admin).

When `use_admin_access` is set to `false`, the results are limited to spaces where the calling user is a joined member. To search with administrator privileges, set `use_admin_access` to `true`.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.spaces>`

\- [User authentication with administrator privileges](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user#admin-privileges) and one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes): - `<https://www.googleapis.com/auth/chat.admin.spaces.readonly>` \- `<https://www.googleapis.com/auth/chat.admin.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SearchSpacesRequest request =
           SearchSpacesRequest.newBuilder()
               .setUseAdminAccess(true)
               .setPageSize(883849137)
               .setPageToken("pageToken873572522")
               .setQuery("query107944136")
               .setOrderBy("orderBy-1207110587")
               .build();
       ApiFuture<Space> future = chatServiceClient.searchSpacesPagedCallable().futureCall(request);
       // Do something.
       for (Space element : future.get().iterateAll()) {
         // doThingsWith(element);
       }
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SearchSpacesRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SearchSpacesRequest),[SearchSpacesPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.ChatServiceClient.SearchSpacesPagedResponse)>` |   
  
### setUpSpace(SetUpSpaceRequest request)
    
    
    public final Space setUpSpace(SetUpSpaceRequest request)

Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn't be specified as a membership in the request. For an example, see [Set up a space with initial members](https://developers.google.com/workspace/chat/set-up-spaces).

To specify the human members to add, add memberships with the appropriate `membership.member.name`. To add a human user, use `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` for the person from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`.

To specify the Google groups to add, add memberships with the appropriate `membership.group_member.name`. To add or invite a Google group, use `groups/{group}`, where `{group}` is the `id` for the group from the Cloud Identity Groups API. For example, you can use [Cloud Identity Groups lookup API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) to retrieve the ID `123456789` for group email `group@example.com`, then you can add the group to the space by setting the `membership.group_member.name` to `groups/123456789`. Group email is not supported, and Google groups can only be added as members in named spaces.

For a named space or group chat, if the caller blocks, or is blocked by some members, or doesn't have permission to add some members, then those members aren't added to the created space.

To create a direct message (DM) between the calling user and another human user, specify exactly one membership to represent the human user. If one user blocks the other, the request fails and the DM isn't created.

To create a DM between the calling user and the calling app, set `Space.singleUserBotDm` to `true` and don't specify any memberships. You can only use this method to set up a DM with the calling app. To add the calling app as a member of a space or an existing DM between two human users, see [Invite or add a user or app to a space](https://developers.google.com/workspace/chat/create-members).

If a DM already exists between two users, even when one user blocks the other at the time a request is made, then the existing DM is returned.

Spaces with threaded replies aren't supported. If you receive the error message `ALREADY_EXISTS` when setting up a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SetUpSpaceRequest request =
           SetUpSpaceRequest.newBuilder()
               .setSpace(Space.newBuilder().build())
               .setRequestId("requestId693933066")
               .addAllMemberships(new ArrayList<Membership>())
               .build();
       Space response = chatServiceClient.setUpSpace(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[SetUpSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### setUpSpaceCallable()
    
    
    public final UnaryCallable<SetUpSpaceRequest,Space> setUpSpaceCallable()

Creates a space and adds specified users to it. The calling user is automatically added to the space, and shouldn't be specified as a membership in the request. For an example, see [Set up a space with initial members](https://developers.google.com/workspace/chat/set-up-spaces).

To specify the human members to add, add memberships with the appropriate `membership.member.name`. To add a human user, use `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` for the person from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`.

To specify the Google groups to add, add memberships with the appropriate `membership.group_member.name`. To add or invite a Google group, use `groups/{group}`, where `{group}` is the `id` for the group from the Cloud Identity Groups API. For example, you can use [Cloud Identity Groups lookup API](https://cloud.google.com/identity/docs/reference/rest/v1/groups/lookup) to retrieve the ID `123456789` for group email `group@example.com`, then you can add the group to the space by setting the `membership.group_member.name` to `groups/123456789`. Group email is not supported, and Google groups can only be added as members in named spaces.

For a named space or group chat, if the caller blocks, or is blocked by some members, or doesn't have permission to add some members, then those members aren't added to the created space.

To create a direct message (DM) between the calling user and another human user, specify exactly one membership to represent the human user. If one user blocks the other, the request fails and the DM isn't created.

To create a DM between the calling user and the calling app, set `Space.singleUserBotDm` to `true` and don't specify any memberships. You can only use this method to set up a DM with the calling app. To add the calling app as a member of a space or an existing DM between two human users, see [Invite or add a user or app to a space](https://developers.google.com/workspace/chat/create-members).

If a DM already exists between two users, even when one user blocks the other at the time a request is made, then the existing DM is returned.

Spaces with threaded replies aren't supported. If you receive the error message `ALREADY_EXISTS` when setting up a space, try a different `displayName`. An existing space within the Google Workspace organization might already use this display name.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.spaces.create>` \- `<https://www.googleapis.com/auth/chat.spaces>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SetUpSpaceRequest request =
           SetUpSpaceRequest.newBuilder()
               .setSpace(Space.newBuilder().build())
               .setRequestId("requestId693933066")
               .addAllMemberships(new ArrayList<Membership>())
               .build();
       ApiFuture<Space> future = chatServiceClient.setUpSpaceCallable().futureCall(request);
       // Do something.
       Space response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[SetUpSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SetUpSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### shutdown()
    
    
    public void shutdown()

### shutdownNow()
    
    
    public void shutdownNow()

### updateAvailability(Availability availability, FieldMask updateMask)
    
    
    public final Availability updateAvailability(Availability availability, FieldMask updateMask)

Updates availability information for a human user. Only the `custom_status` field can be updated through this method.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       Availability availability = Availability.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Availability response = chatServiceClient.updateAvailability(availability, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`availability` | `[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)`  
Required. The availability to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The list of fields to update. The only field that can be updated is `custom_status`.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### updateAvailability(UpdateAvailabilityRequest request)
    
    
    public final Availability updateAvailability(UpdateAvailabilityRequest request)

Updates availability information for a human user. Only the `custom_status` field can be updated through this method.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateAvailabilityRequest request =
           UpdateAvailabilityRequest.newBuilder()
               .setAvailability(Availability.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Availability response = chatServiceClient.updateAvailability(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)` |   
  
### updateAvailabilityCallable()
    
    
    public final UnaryCallable<UpdateAvailabilityRequest,Availability> updateAvailabilityCallable()

Updates availability information for a human user. Only the `custom_status` field can be updated through this method.

This method only updates the authenticated user's availability.

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.availability>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateAvailabilityRequest request =
           UpdateAvailabilityRequest.newBuilder()
               .setAvailability(Availability.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Availability> future =
           chatServiceClient.updateAvailabilityCallable().futureCall(request);
       // Do something.
       Availability response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateAvailabilityRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateAvailabilityRequest),[Availability](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Availability)>` |   
  
### updateMembership(Membership membership, FieldMask updateMask)
    
    
    public final Membership updateMembership(Membership membership, FieldMask updateMask)

Updates a membership. For an example, see [Update a user's membership in a space](https://developers.google.com/workspace/chat/update-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       Membership membership = Membership.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Membership response = chatServiceClient.updateMembership(membership, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`membership` | `[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)`  
Required. The membership to update. Only fields specified by `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths. Currently supported field paths: \- `role`  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### updateMembership(UpdateMembershipRequest request)
    
    
    public final Membership updateMembership(UpdateMembershipRequest request)

Updates a membership. For an example, see [Update a user's membership in a space](https://developers.google.com/workspace/chat/update-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateMembershipRequest request =
           UpdateMembershipRequest.newBuilder()
               .setMembership(Membership.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUseAdminAccess(true)
               .build();
       Membership response = chatServiceClient.updateMembership(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)` |   
  
### updateMembershipCallable()
    
    
    public final UnaryCallable<UpdateMembershipRequest,Membership> updateMembershipCallable()

Updates a membership. For an example, see [Update a user's membership in a space](https://developers.google.com/workspace/chat/update-members).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and the authorization scope: - `<https://www.googleapis.com/auth/chat.app.memberships>` (only in spaces the app created)

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.memberships>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scope is used: - `<https://www.googleapis.com/auth/chat.admin.memberships>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateMembershipRequest request =
           UpdateMembershipRequest.newBuilder()
               .setMembership(Membership.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setUseAdminAccess(true)
               .build();
       ApiFuture<Membership> future =
           chatServiceClient.updateMembershipCallable().futureCall(request);
       // Do something.
       Membership response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMembershipRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMembershipRequest),[Membership](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Membership)>` |   
  
### updateMessage(Message message, FieldMask updateMask)
    
    
    public final Message updateMessage(Message message, FieldMask updateMask)

Updates a message. There's a difference between the `patch` and `update` methods. The `patch` method uses a `patch` request while the `update` method uses a `put` request. We recommend using the `patch` method. For an example, see [Update a message](https://developers.google.com/workspace/chat/update-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only update messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       Message message = Message.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Message response = chatServiceClient.updateMessage(message, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`message` | `[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)`  
Required. Message with fields updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths. Currently supported field paths: \- `text` \- `attachment` \- `cards` (Requires [app authentication](https://docs.cloud.google.com/chat/api/guides/auth/service-accounts).) \- `cards_v2` (Requires [app authentication](https://docs.cloud.google.com/chat/api/guides/auth/service-accounts).) \- `accessory_widgets` (Requires [app authentication](https://docs.cloud.google.com/chat/api/guides/auth/service-accounts).) \- `quoted_message_metadata` (Only allows removal of the quoted message.)  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### updateMessage(UpdateMessageRequest request)
    
    
    public final Message updateMessage(UpdateMessageRequest request)

Updates a message. There's a difference between the `patch` and `update` methods. The `patch` method uses a `patch` request while the `update` method uses a `put` request. We recommend using the `patch` method. For an example, see [Update a message](https://developers.google.com/workspace/chat/update-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only update messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateMessageRequest request =
           UpdateMessageRequest.newBuilder()
               .setMessage(Message.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       Message response = chatServiceClient.updateMessage(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)` |   
  
### updateMessageCallable()
    
    
    public final UnaryCallable<UpdateMessageRequest,Message> updateMessageCallable()

Updates a message. There's a difference between the `patch` and `update` methods. The `patch` method uses a `patch` request while the `update` method uses a `put` request. We recommend using the `patch` method. For an example, see [Update a message](https://developers.google.com/workspace/chat/update-messages).

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with the authorization scope: - `<https://www.googleapis.com/auth/chat.bot>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

When using app authentication, requests can only update messages created by the calling Chat app.

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateMessageRequest request =
           UpdateMessageRequest.newBuilder()
               .setMessage(Message.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .setAllowMissing(true)
               .build();
       ApiFuture<Message> future = chatServiceClient.updateMessageCallable().futureCall(request);
       // Do something.
       Message response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateMessageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateMessageRequest),[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Message)>` |   
  
### updateSection(Section section, FieldMask updateMask)
    
    
    public final Section updateSection(Section section, FieldMask updateMask)

Updates a section. Only sections of type `CUSTOM_SECTION` can be updated. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       Section section = Section.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       Section response = chatServiceClient.updateSection(section, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`section` | `[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)`  
Required. The section to update.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The mask to specify which fields to update. Currently supported field paths: \- `display_name`  
**Returns**  
---  
**Type** | **Description**  
`[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)` |   
  
### updateSection(UpdateSectionRequest request)
    
    
    public final Section updateSection(UpdateSectionRequest request)

Updates a section. Only sections of type `CUSTOM_SECTION` can be updated. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateSectionRequest request =
           UpdateSectionRequest.newBuilder()
               .setSection(Section.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       Section response = chatServiceClient.updateSection(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)` |   
  
### updateSectionCallable()
    
    
    public final UnaryCallable<UpdateSectionRequest,Section> updateSectionCallable()

Updates a section. Only sections of type `CUSTOM_SECTION` can be updated. For details, see [Create and organize sections in Google Chat](https://support.google.com/chat/answer/16059854).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.sections>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateSectionRequest request =
           UpdateSectionRequest.newBuilder()
               .setSection(Section.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<Section> future = chatServiceClient.updateSectionCallable().futureCall(request);
       // Do something.
       Section response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSectionRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSectionRequest),[Section](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Section)>` |   
  
### updateSpace(Space space, FieldMask updateMask)
    
    
    public final Space updateSpace(Space space, FieldMask updateMask)

Updates a space. For an example, see [Update a space](https://developers.google.com/workspace/chat/update-spaces).

If you're updating the `displayName` field and receive the error message `ALREADY_EXISTS`, try a different display name.. An existing space within the Google Workspace organization might already use this display name.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- To update either `space.predefined_permission_settings` or `space.permission_settings`, the app must be the space creator. - Updating the `space.access_settings.audience` is not supported for app authentication.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        Space space = Space.newBuilder().build();
        FieldMask updateMask = FieldMask.newBuilder().build();
        Space response = chatServiceClient.updateSpace(space, updateMask);
        }
        




**Parameters**  
---  
**Name** | **Description**  
`space` | `[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)`  
Required. Space with fields to be updated. `Space.name` must be populated in the form of `spaces/{space}`. Only fields specified by `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The updated field paths, comma separated if there are multiple. You can update the following fields for a space: `space_details`: Updates the space's description and guidelines. You must pass both description and guidelines in the update request as `SpaceDetails`. If you only want to update one of the fields, pass the existing value for the other field. `display_name`: Only supports updating the display name for spaces where `spaceType` field is `SPACE`. If you receive the error message `ALREADY_EXISTS`, try a different value. An existing space within the Google Workspace organization might already use this display name. `space_type`: Only supports changing a `GROUP_CHAT` space type to `SPACE`. Include `display_name` together with `space_type` in the update mask and ensure that the specified space has a non-empty display name and the `SPACE` space type. Including the `space_type` mask and the `SPACE` type in the specified space when updating the display name is optional if the existing space already has the `SPACE` type. Trying to update the space type in other ways results in an invalid argument error. `space_type` is not supported with `useAdminAccess`. `space_history_state`: Updates [space history settings](https://support.google.com/chat/answer/7664687) by turning history on or off for the space. Only supported if history settings are enabled for the Google Workspace organization. To update the space history state, you must omit all other field masks in your request. `space_history_state` is not supported with `useAdminAccess`. `access_settings.audience`: Updates the [access setting](https://support.google.com/chat/answer/11971020) of who can discover the space, join the space, and preview the messages in named space where `spaceType` field is `SPACE`. If the existing space has a target audience, you can remove the audience and restrict space access by omitting a value for this field mask. To update access settings for a space, the authenticating user must be a space manager and omit all other field masks in your request. You can't update this field if the space is in [import mode](https://developers.google.com/workspace/chat/import-data-overview). To learn more, see [Make a space discoverable to specific users](https://developers.google.com/workspace/chat/space-target-audience). `access_settings.audience` is not supported with `useAdminAccess`. `access_settings.access_permission_settings`: Updates the [access permission settings](https://support.google.com/chat/answer/11971020) of who can discover and join the space where `spaceType` field is `SPACE`. Principals allowed to join the space must also be allowed to discover it. To update access permission settings for a space, the authenticating user must be a space manager or assistant manager and omit all other field masks in the request. You can't update this field if the space is in [import mode](https://developers.google.com/workspace/chat/import-data-overview). To learn more, see [Make a space discoverable to specific users](https://developers.google.com/workspace/chat/space-target-audience). `access_settings.access_permission_settings` is not supported with `useAdminAccess`. The supported field masks include: \- `access_settings.access_permission_settings.discoverSpaceSetting` \- `access_settings.access_permission_settings.joinSpaceSetting` \- `access_settings.access_permission_settings.viewSpaceMembershipSetting` `permission_settings`: Supports changing the [permission settings](https://support.google.com/chat/answer/13340792) of a space. When updating permission settings, you can only specify `permissionSettings` field masks; you cannot update other field masks at the same time. The supported field masks include: \- `permission_settings.manageMembersAndGroups` \- `permission_settings.modifySpaceDetails` \- `permission_settings.toggleHistory` \- `permission_settings.useAtMentionAll` \- `permission_settings.manageApps` \- `permission_settings.manageWebhooks` \- `permission_settings.replyMessages` \- `permission_settings.viewSpaceMembership`  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### updateSpace(UpdateSpaceRequest request)
    
    
    public final Space updateSpace(UpdateSpaceRequest request)

Updates a space. For an example, see [Update a space](https://developers.google.com/workspace/chat/update-spaces).

If you're updating the `displayName` field and receive the error message `ALREADY_EXISTS`, try a different display name.. An existing space within the Google Workspace organization might already use this display name.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- To update either `space.predefined_permission_settings` or `space.permission_settings`, the app must be the space creator. - Updating the `space.access_settings.audience` is not supported for app authentication.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        UpdateSpaceRequest request =
            UpdateSpaceRequest.newBuilder()
                .setSpace(Space.newBuilder().build())
                .setUpdateMask(FieldMask.newBuilder().build())
                .setUseAdminAccess(true)
                .build();
        Space response = chatServiceClient.updateSpace(request);
        }
        




**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)` |   
  
### updateSpaceCallable()
    
    
    public final UnaryCallable<UpdateSpaceRequest,Space> updateSpaceCallable()

Updates a space. For an example, see [Update a space](https://developers.google.com/workspace/chat/update-spaces).

If you're updating the `displayName` field and receive the error message `ALREADY_EXISTS`, try a different display name.. An existing space within the Google Workspace organization might already use this display name.

Supports the following types of [authentication](https://developers.google.com/workspace/chat/authenticate-authorize):

\- [App authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app) with [administrator approval](https://support.google.com/a?p=chat-app-auth) and one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.app.spaces>`

\- [User authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following authorization scopes: - `<https://www.googleapis.com/auth/chat.spaces>`

  * `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only) - User authentication grants administrator privileges when an administrator account authenticates, `use_admin_access` is `true`, and the following authorization scopes is used: - `<https://www.googleapis.com/auth/chat.admin.spaces>`

App authentication has the following limitations:

\- To update either `space.predefined_permission_settings` or `space.permission_settings`, the app must be the space creator. - Updating the `space.access_settings.audience` is not supported for app authentication.

Sample code:
        
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
        UpdateSpaceRequest request =
            UpdateSpaceRequest.newBuilder()
                .setSpace(Space.newBuilder().build())
                .setUpdateMask(FieldMask.newBuilder().build())
                .setUseAdminAccess(true)
                .build();
        ApiFuture<Space> future = chatServiceClient.updateSpaceCallable().futureCall(request);
        // Do something.
        Space response = future.get();
        }
        




**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSpaceRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceRequest),[Space](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.Space)>` |   
  
### updateSpaceNotificationSetting(SpaceNotificationSetting spaceNotificationSetting, FieldMask updateMask)
    
    
    public final SpaceNotificationSetting updateSpaceNotificationSetting(SpaceNotificationSetting spaceNotificationSetting, FieldMask updateMask)

Updates the space notification setting. For an example, see [Update the caller's space notification setting](https://developers.google.com/workspace/chat/update-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceNotificationSetting spaceNotificationSetting =
           SpaceNotificationSetting.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SpaceNotificationSetting response =
           chatServiceClient.updateSpaceNotificationSetting(spaceNotificationSetting, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`spaceNotificationSetting` | `[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)`  
Required. The resource name for the space notification settings must be populated in the form of `users/{user}/spaces/{space}/spaceNotificationSetting`. Only fields specified by `update_mask` are updated.  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. Supported field paths: \- `notification_setting` \- `mute_setting`  
**Returns**  
---  
**Type** | **Description**  
`[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)` |   
  
### updateSpaceNotificationSetting(UpdateSpaceNotificationSettingRequest request)
    
    
    public final SpaceNotificationSetting updateSpaceNotificationSetting(UpdateSpaceNotificationSettingRequest request)

Updates the space notification setting. For an example, see [Update the caller's space notification setting](https://developers.google.com/workspace/chat/update-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateSpaceNotificationSettingRequest request =
           UpdateSpaceNotificationSettingRequest.newBuilder()
               .setSpaceNotificationSetting(SpaceNotificationSetting.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SpaceNotificationSetting response = chatServiceClient.updateSpaceNotificationSetting(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)` |   
  
### updateSpaceNotificationSettingCallable()
    
    
    public final UnaryCallable<UpdateSpaceNotificationSettingRequest,SpaceNotificationSetting> updateSpaceNotificationSettingCallable()

Updates the space notification setting. For an example, see [Update the caller's space notification setting](https://developers.google.com/workspace/chat/update-space-notification-setting).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.spacesettings>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateSpaceNotificationSettingRequest request =
           UpdateSpaceNotificationSettingRequest.newBuilder()
               .setSpaceNotificationSetting(SpaceNotificationSetting.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SpaceNotificationSetting> future =
           chatServiceClient.updateSpaceNotificationSettingCallable().futureCall(request);
       // Do something.
       SpaceNotificationSetting response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSpaceNotificationSettingRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceNotificationSettingRequest),[SpaceNotificationSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceNotificationSetting)>` |   
  
### updateSpaceReadState(SpaceReadState spaceReadState, FieldMask updateMask)
    
    
    public final SpaceReadState updateSpaceReadState(SpaceReadState spaceReadState, FieldMask updateMask)

Updates a user's read state within a space, used to identify read and unread messages. For an example, see [Update a user's space read state](https://developers.google.com/workspace/chat/update-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       SpaceReadState spaceReadState = SpaceReadState.newBuilder().build();
       FieldMask updateMask = FieldMask.newBuilder().build();
       SpaceReadState response = chatServiceClient.updateSpaceReadState(spaceReadState, updateMask);
     }
     

**Parameters**  
---  
**Name** | **Description**  
`spaceReadState` | `[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)`  
Required. The space read state and fields to update. Only supports updating read state for the calling user. To refer to the calling user, set one of the following: \- The `me` alias. For example, `users/me/spaces/{space}/spaceReadState`. \- Their Workspace email address. For example, `users/user@example.com/spaces/{space}/spaceReadState`. \- Their user id. For example, `users/123456789/spaces/{space}/spaceReadState`. Format: users/{user}/spaces/{space}/spaceReadState  
`updateMask` | `[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)`  
Required. The field paths to update. Currently supported field paths: \- `last_read_time` When the `last_read_time` is before the latest message create time, the space appears as unread in the UI. To mark the space as read, set `last_read_time` to any value later (larger) than the latest message create time. The `last_read_time` is coerced to match the latest message create time. Note that the space read state only affects the read state of messages that are visible in the space's top-level conversation. Replies in threads are unaffected by this timestamp, and instead rely on the thread read state.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)` |   
  
### updateSpaceReadState(UpdateSpaceReadStateRequest request)
    
    
    public final SpaceReadState updateSpaceReadState(UpdateSpaceReadStateRequest request)

Updates a user's read state within a space, used to identify read and unread messages. For an example, see [Update a user's space read state](https://developers.google.com/workspace/chat/update-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateSpaceReadStateRequest request =
           UpdateSpaceReadStateRequest.newBuilder()
               .setSpaceReadState(SpaceReadState.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       SpaceReadState response = chatServiceClient.updateSpaceReadState(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpdateSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)` |   
  
### updateSpaceReadStateCallable()
    
    
    public final UnaryCallable<UpdateSpaceReadStateRequest,SpaceReadState> updateSpaceReadStateCallable()

Updates a user's read state within a space, used to identify read and unread messages. For an example, see [Update a user's space read state](https://developers.google.com/workspace/chat/update-space-read-state).

Requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with the [authorization scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.users.readstate>`

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UpdateSpaceReadStateRequest request =
           UpdateSpaceReadStateRequest.newBuilder()
               .setSpaceReadState(SpaceReadState.newBuilder().build())
               .setUpdateMask(FieldMask.newBuilder().build())
               .build();
       ApiFuture<SpaceReadState> future =
           chatServiceClient.updateSpaceReadStateCallable().futureCall(request);
       // Do something.
       SpaceReadState response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UpdateSpaceReadStateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UpdateSpaceReadStateRequest),[SpaceReadState](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceReadState)>` |   
  
### uploadAttachment(UploadAttachmentRequest request)
    
    
    public final UploadAttachmentResponse uploadAttachment(UploadAttachmentRequest request)

Uploads an attachment. For an example, see [Upload media as a file attachment](https://developers.google.com/workspace/chat/upload-media-attachments).

Requires user [authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

You can upload attachments up to 200 MB. Certain file types aren't supported. For details, see [File types blocked by Google Chat](https://support.google.com/chat/answer/7651457?&co=GENIE.Platform%3DDesktop#File%20types%20blocked%20in%20Google%20Chat).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UploadAttachmentRequest request =
           UploadAttachmentRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setFilename("filename-734768633")
               .build();
       UploadAttachmentResponse response = chatServiceClient.uploadAttachment(request);
     }
     

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UploadAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequest)`  
The request object containing all of the parameters for the API call.  
**Returns**  
---  
**Type** | **Description**  
`[UploadAttachmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponse)` |   
  
### uploadAttachmentCallable()
    
    
    public final UnaryCallable<UploadAttachmentRequest,UploadAttachmentResponse> uploadAttachmentCallable()

Uploads an attachment. For an example, see [Upload media as a file attachment](https://developers.google.com/workspace/chat/upload-media-attachments).

Requires user [authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) with one of the following [authorization scopes](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes):

\- `<https://www.googleapis.com/auth/chat.messages.create>` \- `<https://www.googleapis.com/auth/chat.messages>` \- `<https://www.googleapis.com/auth/chat.import>` (import mode spaces only)

You can upload attachments up to 200 MB. Certain file types aren't supported. For details, see [File types blocked by Google Chat](https://support.google.com/chat/answer/7651457?&co=GENIE.Platform%3DDesktop#File%20types%20blocked%20in%20Google%20Chat).

Sample code:
    
    
     // This snippet has been automatically generated and should be regarded as a code template only.
     // It will require modifications to work:
     // - It may require correct/in-range values for request initialization.
     // - It may require specifying regional endpoints when creating the service client as shown in
     // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
     try (ChatServiceClient chatServiceClient = ChatServiceClient.create()) {
       UploadAttachmentRequest request =
           UploadAttachmentRequest.newBuilder()
               .setParent(SpaceName.of("[SPACE]").toString())
               .setFilename("filename-734768633")
               .build();
       ApiFuture<UploadAttachmentResponse> future =
           chatServiceClient.uploadAttachmentCallable().futureCall(request);
       // Do something.
       UploadAttachmentResponse response = future.get();
     }
     

**Returns**  
---  
**Type** | **Description**  
`[UnaryCallable](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.UnaryCallable.html)<[UploadAttachmentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentRequest),[UploadAttachmentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.UploadAttachmentResponse)>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
