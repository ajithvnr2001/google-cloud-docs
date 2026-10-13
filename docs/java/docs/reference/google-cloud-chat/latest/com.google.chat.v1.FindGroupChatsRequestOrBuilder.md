---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequestOrBuilder
title: Interface FindGroupChatsRequestOrBuilder (0.63.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:08.449246+00:00
---

# Interface FindGroupChatsRequestOrBuilder (0.63.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.FindGroupChatsRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FindGroupChatsRequestOrBuilder (0.63.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.63.0 (latest)  0.59.0  0.58.0  0.57.0  0.55.0  0.52.0  0.51.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.42.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.34.0  0.32.0  0.31.0  0.28.0  0.27.0  0.26.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface FindGroupChatsRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPageSize()
    
    
    public abstract int getPageSize()

Optional. The maximum number of spaces to return. The service might return fewer than this value.

If unspecified, at most 10 spaces are returned.

The maximum value is 30. If you use a value more than 30, it's automatically changed to 30.

Negative values return an `INVALID_ARGUMENT` error.

`int32 page_size = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The pageSize.  
  
### getPageToken()
    
    
    public abstract String getPageToken()

Optional. A page token, received from a previous call to find group chats. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the token. Passing different values may lead to unexpected results.

`string page_token = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The pageToken.  
  
### getPageTokenBytes()
    
    
    public abstract ByteString getPageTokenBytes()

Optional. A page token, received from a previous call to find group chats. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the token. Passing different values may lead to unexpected results.

`string page_token = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for pageToken.  
  
### getSpaceView()
    
    
    public abstract SpaceView getSpaceView()

Requested space view type. If unset, defaults to `SPACE_VIEW_RESOURCE_NAME_ONLY`. Requests that specify `SPACE_VIEW_EXPANDED` must include scopes that allow reading space data, for example, <https://www.googleapis.com/auth/chat.spaces> or <https://www.googleapis.com/auth/chat.spaces.readonly>.

`.google.chat.v1.SpaceView space_view = 4;`

**Returns**  
---  
**Type** | **Description**  
`[SpaceView](https://docs.cloud.google.com/java/docs/reference/google-cloud-chat/latest/com.google.chat.v1.SpaceView)` | The spaceView.  
  
### getSpaceViewValue()
    
    
    public abstract int getSpaceViewValue()

Requested space view type. If unset, defaults to `SPACE_VIEW_RESOURCE_NAME_ONLY`. Requests that specify `SPACE_VIEW_EXPANDED` must include scopes that allow reading space data, for example, <https://www.googleapis.com/auth/chat.spaces> or <https://www.googleapis.com/auth/chat.spaces.readonly>.

`.google.chat.v1.SpaceView space_view = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for spaceView.  
  
### getUsers(int index)
    
    
    public abstract String getUsers(int index)

Optional. Resource names of all human users in group chat with the calling user. Chat apps can't be included in the request.

The maximum number of users that can be specified in a single request is `49`.

Format: `users/{user}`, where `{user}` is either the `id` for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, to find all group chats with the calling user and two other users, with People API profile IDs `123456789` and `987654321`, you can use `users/123456789` and `users/987654321`. You can also use the email as an alias for `{user}`. For example, `users/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.

`repeated string users = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The users at the given index.  
  
### getUsersBytes(int index)
    
    
    public abstract ByteString getUsersBytes(int index)

Optional. Resource names of all human users in group chat with the calling user. Chat apps can't be included in the request.

The maximum number of users that can be specified in a single request is `49`.

Format: `users/{user}`, where `{user}` is either the `id` for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, to find all group chats with the calling user and two other users, with People API profile IDs `123456789` and `987654321`, you can use `users/123456789` and `users/987654321`. You can also use the email as an alias for `{user}`. For example, `users/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.

`repeated string users = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the users at the given index.  
  
### getUsersCount()
    
    
    public abstract int getUsersCount()

Optional. Resource names of all human users in group chat with the calling user. Chat apps can't be included in the request.

The maximum number of users that can be specified in a single request is `49`.

Format: `users/{user}`, where `{user}` is either the `id` for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, to find all group chats with the calling user and two other users, with People API profile IDs `123456789` and `987654321`, you can use `users/123456789` and `users/987654321`. You can also use the email as an alias for `{user}`. For example, `users/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.

`repeated string users = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of users.  
  
### getUsersList()
    
    
    public abstract List<String> getUsersList()

Optional. Resource names of all human users in group chat with the calling user. Chat apps can't be included in the request.

The maximum number of users that can be specified in a single request is `49`.

Format: `users/{user}`, where `{user}` is either the `id` for the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the [user](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users) in the Directory API. For example, to find all group chats with the calling user and two other users, with People API profile IDs `123456789` and `987654321`, you can use `users/123456789` and `users/987654321`. You can also use the email as an alias for `{user}`. For example, `users/example@gmail.com` where `example@gmail.com` is the email of the Google Chat user.

`repeated string users = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the users.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
