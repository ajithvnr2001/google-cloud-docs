---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers
title: Module pagers (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:45.056782+00:00
---

# Module pagers (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

API documentation for `geminidataanalytics_v1.services.data_chat_service.pagers` module.

## Classes 

### [ListConversationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsAsyncPager)
    
    
    ListConversationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListConversationsResponse) object, and provides an `__aiter__` method to iterate through its `conversations` field.

If there are more pages, the `__aiter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConversationsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListConversationsPager)
    
    
    ListConversationsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsRequest,
        response: google.cloud.geminidataanalytics_v1.types.conversation.ListConversationsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

A pager for iterating through `list_conversations` requests.

This class thinly wraps an initial [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListConversationsResponse) object, and provides an `__iter__` method to iterate through its `conversations` field.

If there are more pages, the `__iter__` method will make additional `ListConversations` requests and continue to iterate through the `conversations` field on the corresponding responses.

All the usual [ListConversationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListConversationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMessagesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesAsyncPager)
    
    
    ListMessagesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

A pager for iterating through `list_messages` requests.

This class thinly wraps an initial [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListMessagesResponse) object, and provides an `__aiter__` method to iterate through its `messages` field.

If there are more pages, the `__aiter__` method will make additional `ListMessages` requests and continue to iterate through the `messages` field on the corresponding responses.

All the usual [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListMessagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMessagesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.pagers.ListMessagesPager)
    
    
    ListMessagesPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse,
        ],
        request: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesRequest,
        response: google.cloud.geminidataanalytics_v1.types.data_chat_service.ListMessagesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

A pager for iterating through `list_messages` requests.

This class thinly wraps an initial [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListMessagesResponse) object, and provides an `__iter__` method to iterate through its `messages` field.

If there are more pages, the `__iter__` method will make additional `ListMessages` requests and continue to iterate through the `messages` field on the corresponding responses.

All the usual [ListMessagesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ListMessagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
