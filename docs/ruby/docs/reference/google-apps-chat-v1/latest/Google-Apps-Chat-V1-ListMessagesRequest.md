---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-ListMessagesRequest/
title: Google Chat V1 API - Class Google::Apps::Chat::V1::ListMessagesRequest (v0.31.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:37.415891+00:00
---

# Google Chat V1 API - Class Google::Apps::Chat::V1::ListMessagesRequest (v0.31.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-ListMessagesRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Chat V1 API - Class Google::Apps::Chat::V1::ListMessagesRequest (v0.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.0 (latest)  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.2 

Reference documentation and code samples for the Google Chat V1 API class Google::Apps::Chat::V1::ListMessagesRequest.

Lists messages in the specified space, that the user is a member of.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #filter
    
    
    def filter() -> ::String

**Returns**

  * (::String) — Optional. A query filter.

You can filter messages by date (`create_time`) and thread (`thread.name`).

To filter messages by the date they were created, specify the `create_time` with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and double quotation marks. For example, `"2023-04-21T11:30:00-04:00"`. You can use the greater than operator `>` to list messages that were created after a timestamp, or the less than operator `<` to list messages that were created before a timestamp. To filter messages within a time interval, use the `AND` operator between two timestamps.

To filter by thread, specify the `thread.name`, formatted as `spaces/{space}/threads/{thread}`. You can only specify one `thread.name` per query.

To filter by both thread and date, use the `AND` operator in your query.

For example, the following queries are valid:

``` create_time > "2012-04-21T11:30:00-04:00"

create_time > "2012-04-21T11:30:00-04:00" AND thread.name = spaces/AAAAAAAAAAA/threads/123

create_time > "2012-04-21T11:30:00+00:00" AND

create_time < "2013-01-01T00:00:00+00:00" AND thread.name = spaces/AAAAAAAAAAA/threads/123

thread.name = spaces/AAAAAAAAAAA/threads/123 ```

Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error. 




### #filter=
    
    
    def filter=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A query filter.

You can filter messages by date (`create_time`) and thread (`thread.name`).

To filter messages by the date they were created, specify the `create_time` with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and double quotation marks. For example, `"2023-04-21T11:30:00-04:00"`. You can use the greater than operator `>` to list messages that were created after a timestamp, or the less than operator `<` to list messages that were created before a timestamp. To filter messages within a time interval, use the `AND` operator between two timestamps.

To filter by thread, specify the `thread.name`, formatted as `spaces/{space}/threads/{thread}`. You can only specify one `thread.name` per query.

To filter by both thread and date, use the `AND` operator in your query.

For example, the following queries are valid:

``` create_time > "2012-04-21T11:30:00-04:00"

create_time > "2012-04-21T11:30:00-04:00" AND thread.name = spaces/AAAAAAAAAAA/threads/123

create_time > "2012-04-21T11:30:00+00:00" AND

create_time < "2013-01-01T00:00:00+00:00" AND thread.name = spaces/AAAAAAAAAAA/threads/123

thread.name = spaces/AAAAAAAAAAA/threads/123 ```

Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error. 




**Returns**

  * (::String) — Optional. A query filter.

You can filter messages by date (`create_time`) and thread (`thread.name`).

To filter messages by the date they were created, specify the `create_time` with a timestamp in [RFC-3339](https://www.rfc-editor.org/rfc/rfc3339) format and double quotation marks. For example, `"2023-04-21T11:30:00-04:00"`. You can use the greater than operator `>` to list messages that were created after a timestamp, or the less than operator `<` to list messages that were created before a timestamp. To filter messages within a time interval, use the `AND` operator between two timestamps.

To filter by thread, specify the `thread.name`, formatted as `spaces/{space}/threads/{thread}`. You can only specify one `thread.name` per query.

To filter by both thread and date, use the `AND` operator in your query.

For example, the following queries are valid:

``` create_time > "2012-04-21T11:30:00-04:00"

create_time > "2012-04-21T11:30:00-04:00" AND thread.name = spaces/AAAAAAAAAAA/threads/123

create_time > "2012-04-21T11:30:00+00:00" AND

create_time < "2013-01-01T00:00:00+00:00" AND thread.name = spaces/AAAAAAAAAAA/threads/123

thread.name = spaces/AAAAAAAAAAA/threads/123 ```

Invalid queries are rejected by the server with an `INVALID_ARGUMENT` error. 




### #markup_syntax
    
    
    def markup_syntax() -> ::Google::Apps::Chat::V1::MarkupSyntax

**Returns**

  * ([::Google::Apps::Chat::V1::MarkupSyntax](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-MarkupSyntax)) — Optional. Specifies the desired output syntax for the Chat message `formatted_text` field. 



### #markup_syntax=
    
    
    def markup_syntax=(value) -> ::Google::Apps::Chat::V1::MarkupSyntax

**Parameter**

  * **value** ([::Google::Apps::Chat::V1::MarkupSyntax](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-MarkupSyntax)) — Optional. Specifies the desired output syntax for the Chat message `formatted_text` field. 



**Returns**

  * ([::Google::Apps::Chat::V1::MarkupSyntax](https://docs.cloud.google.com/ruby/docs/reference/google-apps-chat-v1/latest/Google-Apps-Chat-V1-MarkupSyntax)) — Optional. Specifies the desired output syntax for the Chat message `formatted_text` field. 



### #order_by
    
    
    def order_by() -> ::String

**Returns**

  * (::String) — Optional. How the list of messages is ordered. Specify a value to order by an ordering operation. Valid ordering operation values are as follows:

    * `ASC` for ascending.

    * `DESC` for descending.

The default ordering is `create_time ASC`. 




### #order_by=
    
    
    def order_by=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. How the list of messages is ordered. Specify a value to order by an ordering operation. Valid ordering operation values are as follows:

    * `ASC` for ascending.

    * `DESC` for descending.

The default ordering is `create_time ASC`. 




**Returns**

  * (::String) — Optional. How the list of messages is ordered. Specify a value to order by an ordering operation. Valid ordering operation values are as follows:

    * `ASC` for ascending.

    * `DESC` for descending.

The default ordering is `create_time ASC`. 




### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — Optional. The maximum number of messages returned. The service might return fewer messages than this value.

If unspecified, at most 25 are returned.

The maximum value is 1000. If you use a value more than 1000, it's automatically changed to 1000.

Negative values return an `INVALID_ARGUMENT` error. 




### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Optional. The maximum number of messages returned. The service might return fewer messages than this value.

If unspecified, at most 25 are returned.

The maximum value is 1000. If you use a value more than 1000, it's automatically changed to 1000.

Negative values return an `INVALID_ARGUMENT` error. 




**Returns**

  * (::Integer) — Optional. The maximum number of messages returned. The service might return fewer messages than this value.

If unspecified, at most 25 are returned.

The maximum value is 1000. If you use a value more than 1000, it's automatically changed to 1000.

Negative values return an `INVALID_ARGUMENT` error. 




### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — Optional. A page token received from a previous list messages call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. A page token received from a previous list messages call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results. 




**Returns**

  * (::String) — Optional. A page token received from a previous list messages call. Provide this parameter to retrieve the subsequent page.

When paginating, all other parameters provided should match the call that provided the page token. Passing different values to the other parameters might lead to unexpected results. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The resource name of the space to list messages from.

Format: `spaces/{space}`




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource name of the space to list messages from.

Format: `spaces/{space}`




**Returns**

  * (::String) — Required. The resource name of the space to list messages from.

Format: `spaces/{space}`




### #show_deleted
    
    
    def show_deleted() -> ::Boolean

**Returns**

  * (::Boolean) — Optional. Whether to include deleted messages. Deleted messages include deleted time and metadata about their deletion, but message content is unavailable. 



### #show_deleted=
    
    
    def show_deleted=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Optional. Whether to include deleted messages. Deleted messages include deleted time and metadata about their deletion, but message content is unavailable. 



**Returns**

  * (::Boolean) — Optional. Whether to include deleted messages. Deleted messages include deleted time and metadata about their deletion, but message content is unavailable. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
