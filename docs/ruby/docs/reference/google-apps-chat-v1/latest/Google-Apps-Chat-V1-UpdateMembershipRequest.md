---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-UpdateMembershipRequest/
title: Google Chat V1 API - Class Google::Apps::Chat::V1::UpdateMembershipRequest (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:31.828733+00:00
---

# Google Chat V1 API - Class Google::Apps::Chat::V1::UpdateMembershipRequest (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-UpdateMembershipRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Chat::V1::UpdateMembershipRequest (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Chat::V1::UpdateMembershipRequest.

Request message for updating a membership.

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

  * ([::Google::Apps::Chat::V1::Membership](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Membership)) — Required. The membership to update. Only fields specified by `update_mask` are updated. 



### #membership=
    
    
    def membership=(value) -> ::Google::Apps::Chat::V1::Membership

**Parameter**

  * **value** ([::Google::Apps::Chat::V1::Membership](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Membership)) — Required. The membership to update. Only fields specified by `update_mask` are updated. 



**Returns**

  * ([::Google::Apps::Chat::V1::Membership](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-Membership)) — Required. The membership to update. Only fields specified by `update_mask` are updated. 



### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Protobuf-FieldMask)) — 

Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths.

Currently supported field paths:

    * `role`



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Protobuf-FieldMask)) — 

Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths.

Currently supported field paths:

    * `role`



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Protobuf-FieldMask)) — 

Required. The field paths to update. Separate multiple values with commas or use `*` to update all field paths.

Currently supported field paths:

    * `role`



### #use_admin_access
    
    
    def use_admin_access() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires the `chat.admin.memberships` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes). 




### #use_admin_access=
    
    
    def use_admin_access=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires the `chat.admin.memberships` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes). 




**Returns**

  * (::Boolean) — Optional. When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245).

Requires the `chat.admin.memberships` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
