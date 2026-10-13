---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-CreateMembershipRequest/
title: Google Chat V1 API - Class Google::Apps::Chat::V1::CreateMembershipRequest (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:00:23.193081+00:00
---

# Google Chat V1 API - Class Google::Apps::Chat::V1::CreateMembershipRequest (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-CreateMembershipRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Chat::V1::CreateMembershipRequest (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Chat::V1::CreateMembershipRequest.

Request message for creating a membership.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #membership
    
    
    def membership() -> ::Google::Apps::Chat::V1::Membership

**Returns**

  * ([::Google::Apps::Chat::V1::Membership](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Membership)) — Required. The membership relation to create.

The `memberType` field must contain a user with the `user.name` and `user.type` fields populated. The server will assign a resource name and overwrite anything specified.

When a Chat app creates a membership relation for a human user, it must use certain authorization scopes and set specific values for certain fields:

    * When [authenticating as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the `chat.memberships` authorization scope is required.

    * When [authenticating as an app](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), the `chat.app.memberships` authorization scope is required.

    * Set `user.type` to `HUMAN`, and set `user.name` with format `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` of the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`.

Inviting users external to the Workspace organization that owns the space requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).

When a Chat app creates a membership relation for itself, it must [authenticate as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and use the `chat.memberships.app` scope, set `user.type` to `BOT`, and set `user.name` to `users/app`. 




### #membership=
    
    
    def membership=(value) -> ::Google::Apps::Chat::V1::Membership

**Parameter**

  * **value** ([::Google::Apps::Chat::V1::Membership](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Membership)) — Required. The membership relation to create.

The `memberType` field must contain a user with the `user.name` and `user.type` fields populated. The server will assign a resource name and overwrite anything specified.

When a Chat app creates a membership relation for a human user, it must use certain authorization scopes and set specific values for certain fields:

    * When [authenticating as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the `chat.memberships` authorization scope is required.

    * When [authenticating as an app](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), the `chat.app.memberships` authorization scope is required.

    * Set `user.type` to `HUMAN`, and set `user.name` with format `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` of the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`.

Inviting users external to the Workspace organization that owns the space requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).

When a Chat app creates a membership relation for itself, it must [authenticate as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and use the `chat.memberships.app` scope, set `user.type` to `BOT`, and set `user.name` to `users/app`. 




**Returns**

  * ([::Google::Apps::Chat::V1::Membership](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Membership)) — Required. The membership relation to create.

The `memberType` field must contain a user with the `user.name` and `user.type` fields populated. The server will assign a resource name and overwrite anything specified.

When a Chat app creates a membership relation for a human user, it must use certain authorization scopes and set specific values for certain fields:

    * When [authenticating as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user), the `chat.memberships` authorization scope is required.

    * When [authenticating as an app](https://developers.google.com/workspace/chat/authenticate-authorize-chat-app), the `chat.app.memberships` authorization scope is required.

    * Set `user.type` to `HUMAN`, and set `user.name` with format `users/{user}`, where `{user}` can be the email address for the user. For users in the same Workspace organization `{user}` can also be the `id` of the [person](https://developers.google.com/people/api/rest/v1/people) from the People API, or the `id` for the user in the Directory API. For example, if the People API Person profile ID for `user@example.com` is `123456789`, you can add the user to the space by setting the `membership.member.name` to `users/user@example.com` or `users/123456789`.

Inviting users external to the Workspace organization that owns the space requires [user authentication](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user).

When a Chat app creates a membership relation for itself, it must [authenticate as a user](https://developers.google.com/workspace/chat/authenticate-authorize-chat-user) and use the `chat.memberships.app` scope, set `user.type` to `BOT`, and set `user.name` to `users/app`. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the space for which to create the membership.

Format: spaces/{space} 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the space for which to create the membership.

Format: spaces/{space} 




**Returns**

  * (::String) — Required. The resource name of the space for which to create the membership.

Format: spaces/{space} 




### #use_admin_access
    
    
    def use_admin_access() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires the `chat.admin.memberships` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).

Creating app memberships or creating memberships for users outside the administrator's Google Workspace organization isn't supported using admin access. 




### #use_admin_access=
    
    
    def use_admin_access=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires the `chat.admin.memberships` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).

Creating app memberships or creating memberships for users outside the administrator's Google Workspace organization isn't supported using admin access. 




**Returns**

  * (::Boolean) — Optional. When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires the `chat.admin.memberships` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).

Creating app memberships or creating memberships for users outside the administrator's Google Workspace organization isn't supported using admin access. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
