---
url: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.SearchSpacesRequest
title: Google Apps Chat V1 Client - Class SearchSpacesRequest (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:56.647766+00:00
---

# Google Apps Chat V1 Client - Class SearchSpacesRequest (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/apps-chat/latest/Chat.V1.SearchSpacesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Apps Chat V1 Client - Class SearchSpacesRequest (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.27.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.0  0.13.1  0.12.1  0.11.2  0.10.0  0.9.0  0.8.1  0.7.2  0.6.1  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Google Apps Chat V1 Client class SearchSpacesRequest.

Request to search for a list of spaces based on a query.

Generated from protobuf message `google.chat.v1.SearchSpacesRequest`

## Namespace

Google \ Apps \ Chat \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ use_admin_access` |  `bool`   
When `true`, the method runs using the user's Google Workspace administrator privileges. The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245). Requires either the `chat.admin.spaces.readonly` or `chat.admin.spaces` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).  
`↳ page_size` |  `int`   
The maximum number of spaces to return. The service may return fewer than this value. If unspecified, at most 100 spaces are returned. The maximum value is 1000 when `useAdminAccess` is set to `true`. Otherwise, the maximum value is 100. If you use a value more than the maximum value, it's automatically changed to the maximum value.  
`↳ page_token` |  `string`   
A token, received from the previous search spaces call. Provide this parameter to retrieve the subsequent page. When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.  
`↳ query` |  `string`   
Required. A search query. You can search by using the following parameters when `useAdminAccess` is set to `true`: - `create_time` \- `customer` \- `display_name` \- `external_user_allowed` \- `last_active_time` \- `space_history_state` \- `space_type` When `useAdminAccess` is set to `false`: - `display_name` \- `external_user_allowed` \- `space_type` `create_time` and `last_active_time` accept a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `=`, `<`, `>`, `<=`, `>=`. `customer` is required when `useAdminAccess` is set to `true`, and is used to indicate which customer to fetch spaces from. `customers/my_customer` is the only supported value. `display_name` only accepts the `HAS` (`:`) operator. The text to match is first tokenized into tokens and each token is prefix-matched case-insensitively and independently as a substring anywhere in the space's `display_name`. For example, `Fun Eve` matches `Fun event` or `The evening was fun`, but not `notFun event` or `even`. When `useAdminAccess` is set to `false`, `display_name` is required to retrieve meaningful results. Otherwise, the default behavior is to return an empty response. `external_user_allowed` accepts either `true` or `false`. `space_history_state` only accepts values from the [`historyState`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#Space.HistoryState) field of a `space` resource. `space_type` is required and the only valid value is `SPACE`. Across different fields, only `AND` operators are supported. A valid example is `space_type = "SPACE" AND display_name:"Hello"` and an invalid example is `space_type = "SPACE" OR display_name:"Hello"`. Among the same field, `space_type` doesn't support `AND` or `OR` operators. `display_name`, 'space_history_state', and 'external_user_allowed' only support `OR` operators. `last_active_time` and `create_time` support both `AND` and `OR` operators. `AND` can only be used to represent an interval, such as `last_active_time < "2022-01-01T00:00:00+00:00" AND last_active_time > "2023-01-01T00:00:00+00:00"`. The following example queries are valid when `useAdminAccess` is set to `true`: `customer = "customers/my_customer" AND space_type = "SPACE" customer = "customers/my_customer" AND space_type = "SPACE" AND display_name:"Hello World" customer = "customers/my_customer" AND space_type = "SPACE" AND (last_active_time < "2020-01-01T00:00:00+00:00" OR last_active_time > "2022-01-01T00:00:00+00:00") customer = "customers/my_customer" AND space_type = "SPACE" AND (display_name:"Hello World" OR display_name:"Fun event") AND (last_active_time > "2020-01-01T00:00:00+00:00" AND last_active_time < "2022-01-01T00:00:00+00:00") customer = "customers/my_customer" AND space_type = "SPACE" AND (create_time > "2019-01-01T00:00:00+00:00" AND create_time < "2020-01-01T00:00:00+00:00") AND (external_user_allowed = "true") AND (space_history_state = "HISTORY_ON" OR space_history_state = "HISTORY_OFF")` The following example queries are valid when `useAdminAccess` is set to `false`: `display_name:"Hello World" AND space_type = "SPACE" (display_name:"Hello" OR display_name:"Fun") AND space_type = "SPACE" (external_user_allowed = "true" AND space_type = "SPACE") // Returns an empty response. (external_user_allowed = "true" AND display_name:"Hello" AND space_type = "SPACE")` The maximum query length is 1,000 characters. Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.  
`↳ order_by` |  `string`   
Optional. How the list of spaces is ordered. Supported attributes to order by are: - `membership_count.joined_direct_human_user_count` — Denotes the count of human users that have directly joined a space. - `last_active_time` — Denotes the time when last eligible item is added to any topic of this space. - `create_time` — Denotes the time of the space creation. When `useAdminAccess` is `false`, only `create_time` and `relevance` are supported for ordering. Only `DESC` is supported for these fields in non-admin searches. Valid ordering operation values are: - `ASC` for ascending. Default value. - `DESC` for descending. The supported syntax are when `useAdminAccess` is set to `true`: - `membership_count.joined_direct_human_user_count DESC` \- `membership_count.joined_direct_human_user_count ASC` \- `last_active_time DESC` \- `last_active_time ASC` \- `create_time DESC` \- `create_time ASC` When `useAdminAccess` is set to `false`: - `create_time DESC` \- `relevance DESC` [Developer Preview](https://developers.google.com/workspace/preview).  
  
### getUseAdminAccess

When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245). Requires either the `chat.admin.spaces.readonly` or `chat.admin.spaces` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setUseAdminAccess

When `true`, the method runs using the user's Google Workspace administrator privileges.

The calling user must be a Google Workspace administrator with the [manage chat and spaces conversations privilege](https://support.google.com/a/answer/13369245). Requires either the `chat.admin.spaces.readonly` or `chat.admin.spaces` [OAuth 2.0 scope](https://developers.google.com/workspace/chat/authenticate-authorize#chat-api-scopes).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

The maximum number of spaces to return. The service may return fewer than this value.

If unspecified, at most 100 spaces are returned. The maximum value is 1000 when `useAdminAccess` is set to `true`. Otherwise, the maximum value is 100. If you use a value more than the maximum value, it's automatically changed to the maximum value.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

The maximum number of spaces to return. The service may return fewer than this value.

If unspecified, at most 100 spaces are returned. The maximum value is 1000 when `useAdminAccess` is set to `true`. Otherwise, the maximum value is 100. If you use a value more than the maximum value, it's automatically changed to the maximum value.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

A token, received from the previous search spaces call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

A token, received from the previous search spaces call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getQuery

Required. A search query.

You can search by using the following parameters when `useAdminAccess` is set to `true`:

  * `create_time`
  * `customer`
  * `display_name`
  * `external_user_allowed`
  * `last_active_time`
  * `space_history_state`
  * `space_type` When `useAdminAccess` is set to `false`:
  * `display_name`
  * `external_user_allowed`
  * `space_type` `create_time` and `last_active_time` accept a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `=`, `<`, `>`, `<=`, `>=`. `customer` is required when `useAdminAccess` is set to `true`, and is used to indicate which customer to fetch spaces from. `customers/my_customer` is the only supported value. `display_name` only accepts the `HAS` (`:`) operator. The text to match is first tokenized into tokens and each token is prefix-matched case-insensitively and independently as a substring anywhere in the space's `display_name`. For example, `Fun Eve` matches `Fun event` or `The evening was fun`, but not `notFun event` or `even`. When `useAdminAccess` is set to `false`, `display_name` is required to retrieve meaningful results. Otherwise, the default behavior is to return an empty response. `external_user_allowed` accepts either `true` or `false`. `space_history_state` only accepts values from the [`historyState`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#Space.HistoryState) field of a `space` resource. `space_type` is required and the only valid value is `SPACE`. Across different fields, only `AND` operators are supported. A valid example is `space_type = "SPACE" AND display_name:"Hello"` and an invalid example is `space_type = "SPACE" OR display_name:"Hello"`. Among the same field, `space_type` doesn't support `AND` or `OR` operators. `display_name`, 'space_history_state', and 'external_user_allowed' only support `OR` operators. `last_active_time` and `create_time` support both `AND` and `OR` operators. `AND` can only be used to represent an interval, such as `last_active_time < "2022-01-01T00:00:00+00:00" AND last_active_time > "2023-01-01T00:00:00+00:00"`. The following example queries are valid when `useAdminAccess` is set to `true`: `php customer = "customers/my_customer" AND space_type = "SPACE" customer = "customers/my_customer" AND space_type = "SPACE" AND display_name:"Hello World" customer = "customers/my_customer" AND space_type = "SPACE" AND (last_active_time < "2020-01-01T00:00:00+00:00" OR last_active_time > "2022-01-01T00:00:00+00:00") customer = "customers/my_customer" AND space_type = "SPACE" AND (display_name:"Hello World" OR display_name:"Fun event") AND (last_active_time > "2020-01-01T00:00:00+00:00" AND last_active_time < "2022-01-01T00:00:00+00:00") customer = "customers/my_customer" AND space_type = "SPACE" AND (create_time > "2019-01-01T00:00:00+00:00" AND create_time < "2020-01-01T00:00:00+00:00") AND (external_user_allowed = "true") AND (space_history_state = "HISTORY_ON" OR space_history_state = "HISTORY_OFF")` The following example queries are valid when `useAdminAccess` is set to `false`: `php display_name:"Hello World" AND space_type = "SPACE" (display_name:"Hello" OR display_name:"Fun") AND space_type = "SPACE" (external_user_allowed = "true" AND space_type = "SPACE") // Returns an empty response. (external_user_allowed = "true" AND display_name:"Hello" AND space_type = "SPACE")` The maximum query length is 1,000 characters. Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setQuery

Required. A search query.

You can search by using the following parameters when `useAdminAccess` is set to `true`:

  * `create_time`
  * `customer`
  * `display_name`
  * `external_user_allowed`
  * `last_active_time`
  * `space_history_state`
  * `space_type` When `useAdminAccess` is set to `false`:
  * `display_name`
  * `external_user_allowed`
  * `space_type` `create_time` and `last_active_time` accept a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and the supported comparison operators are: `=`, `<`, `>`, `<=`, `>=`. `customer` is required when `useAdminAccess` is set to `true`, and is used to indicate which customer to fetch spaces from. `customers/my_customer` is the only supported value. `display_name` only accepts the `HAS` (`:`) operator. The text to match is first tokenized into tokens and each token is prefix-matched case-insensitively and independently as a substring anywhere in the space's `display_name`. For example, `Fun Eve` matches `Fun event` or `The evening was fun`, but not `notFun event` or `even`. When `useAdminAccess` is set to `false`, `display_name` is required to retrieve meaningful results. Otherwise, the default behavior is to return an empty response. `external_user_allowed` accepts either `true` or `false`. `space_history_state` only accepts values from the [`historyState`](https://developers.google.com/workspace/chat/api/reference/rest/v1/spaces#Space.HistoryState) field of a `space` resource. `space_type` is required and the only valid value is `SPACE`. Across different fields, only `AND` operators are supported. A valid example is `space_type = "SPACE" AND display_name:"Hello"` and an invalid example is `space_type = "SPACE" OR display_name:"Hello"`. Among the same field, `space_type` doesn't support `AND` or `OR` operators. `display_name`, 'space_history_state', and 'external_user_allowed' only support `OR` operators. `last_active_time` and `create_time` support both `AND` and `OR` operators. `AND` can only be used to represent an interval, such as `last_active_time < "2022-01-01T00:00:00+00:00" AND last_active_time > "2023-01-01T00:00:00+00:00"`. The following example queries are valid when `useAdminAccess` is set to `true`: `php customer = "customers/my_customer" AND space_type = "SPACE" customer = "customers/my_customer" AND space_type = "SPACE" AND display_name:"Hello World" customer = "customers/my_customer" AND space_type = "SPACE" AND (last_active_time < "2020-01-01T00:00:00+00:00" OR last_active_time > "2022-01-01T00:00:00+00:00") customer = "customers/my_customer" AND space_type = "SPACE" AND (display_name:"Hello World" OR display_name:"Fun event") AND (last_active_time > "2020-01-01T00:00:00+00:00" AND last_active_time < "2022-01-01T00:00:00+00:00") customer = "customers/my_customer" AND space_type = "SPACE" AND (create_time > "2019-01-01T00:00:00+00:00" AND create_time < "2020-01-01T00:00:00+00:00") AND (external_user_allowed = "true") AND (space_history_state = "HISTORY_ON" OR space_history_state = "HISTORY_OFF")` The following example queries are valid when `useAdminAccess` is set to `false`: `php display_name:"Hello World" AND space_type = "SPACE" (display_name:"Hello" OR display_name:"Fun") AND space_type = "SPACE" (external_user_allowed = "true" AND space_type = "SPACE") // Returns an empty response. (external_user_allowed = "true" AND display_name:"Hello" AND space_type = "SPACE")` The maximum query length is 1,000 characters. Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. How the list of spaces is ordered.

Supported attributes to order by are:

  * `membership_count.joined_direct_human_user_count` — Denotes the count of human users that have directly joined a space.
  * `last_active_time` — Denotes the time when last eligible item is added to any topic of this space.
  * `create_time` — Denotes the time of the space creation. When `useAdminAccess` is `false`, only `create_time` and `relevance` are supported for ordering. Only `DESC` is supported for these fields in non-admin searches. Valid ordering operation values are:
  * `ASC` for ascending. Default value.
  * `DESC` for descending. The supported syntax are when `useAdminAccess` is set to `true`:
  * `membership_count.joined_direct_human_user_count DESC`
  * `membership_count.joined_direct_human_user_count ASC`
  * `last_active_time DESC`
  * `last_active_time ASC`
  * `create_time DESC`
  * `create_time ASC` When `useAdminAccess` is set to `false`:
  * `create_time DESC`
  * `relevance DESC` [Developer Preview](https://developers.google.com/workspace/preview).



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. How the list of spaces is ordered.

Supported attributes to order by are:

  * `membership_count.joined_direct_human_user_count` — Denotes the count of human users that have directly joined a space.
  * `last_active_time` — Denotes the time when last eligible item is added to any topic of this space.
  * `create_time` — Denotes the time of the space creation. When `useAdminAccess` is `false`, only `create_time` and `relevance` are supported for ordering. Only `DESC` is supported for these fields in non-admin searches. Valid ordering operation values are:
  * `ASC` for ascending. Default value.
  * `DESC` for descending. The supported syntax are when `useAdminAccess` is set to `true`:
  * `membership_count.joined_direct_human_user_count DESC`
  * `membership_count.joined_direct_human_user_count ASC`
  * `last_active_time DESC`
  * `last_active_time ASC`
  * `create_time DESC`
  * `create_time ASC` When `useAdminAccess` is set to `false`:
  * `create_time DESC`
  * `relevance DESC` [Developer Preview](https://developers.google.com/workspace/preview).



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
