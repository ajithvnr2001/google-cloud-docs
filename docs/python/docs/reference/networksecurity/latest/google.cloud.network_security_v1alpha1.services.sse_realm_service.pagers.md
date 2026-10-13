---
url: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers
title: Module pagers (0.13.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:37.015510+00:00
---

# Module pagers (0.13.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.13.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.4 (latest)  0.13.3  0.12.0  0.11.0  0.10.0  0.9.21  0.8.0  0.7.2  0.6.1  0.5.0  0.4.2  0.3.2  0.2.0  0.1.5 

API documentation for `network_security_v1alpha1.services.sse_realm_service.pagers` module.

## Classes 

### [ListPartnerSSERealmsAsyncPager](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers.ListPartnerSSERealmsAsyncPager)
    
    
    ListPartnerSSERealmsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.network_security_v1alpha1.types.sse_realm.ListPartnerSSERealmsResponse
            ],
        ],
        request: google.cloud.network_security_v1alpha1.types.sse_realm.ListPartnerSSERealmsRequest,
        response: google.cloud.network_security_v1alpha1.types.sse_realm.ListPartnerSSERealmsResponse,
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

A pager for iterating through `list_partner_sse_realms` requests.

This class thinly wraps an initial [ListPartnerSSERealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListPartnerSSERealmsResponse) object, and provides an `__aiter__` method to iterate through its `partner_sse_realms` field.

If there are more pages, the `__aiter__` method will make additional `ListPartnerSSERealms` requests and continue to iterate through the `partner_sse_realms` field on the corresponding responses.

All the usual [ListPartnerSSERealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListPartnerSSERealmsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPartnerSSERealmsPager](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers.ListPartnerSSERealmsPager)
    
    
    ListPartnerSSERealmsPager(
        method: typing.Callable[
            [...],
            google.cloud.network_security_v1alpha1.types.sse_realm.ListPartnerSSERealmsResponse,
        ],
        request: google.cloud.network_security_v1alpha1.types.sse_realm.ListPartnerSSERealmsRequest,
        response: google.cloud.network_security_v1alpha1.types.sse_realm.ListPartnerSSERealmsResponse,
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

A pager for iterating through `list_partner_sse_realms` requests.

This class thinly wraps an initial [ListPartnerSSERealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListPartnerSSERealmsResponse) object, and provides an `__iter__` method to iterate through its `partner_sse_realms` field.

If there are more pages, the `__iter__` method will make additional `ListPartnerSSERealms` requests and continue to iterate through the `partner_sse_realms` field on the corresponding responses.

All the usual [ListPartnerSSERealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListPartnerSSERealmsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSACAttachmentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers.ListSACAttachmentsAsyncPager)
    
    
    ListSACAttachmentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.network_security_v1alpha1.types.sse_realm.ListSACAttachmentsResponse
            ],
        ],
        request: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACAttachmentsRequest,
        response: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACAttachmentsResponse,
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

A pager for iterating through `list_sac_attachments` requests.

This class thinly wraps an initial [ListSACAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACAttachmentsResponse) object, and provides an `__aiter__` method to iterate through its `sac_attachments` field.

If there are more pages, the `__aiter__` method will make additional `ListSACAttachments` requests and continue to iterate through the `sac_attachments` field on the corresponding responses.

All the usual [ListSACAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACAttachmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSACAttachmentsPager](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers.ListSACAttachmentsPager)
    
    
    ListSACAttachmentsPager(
        method: typing.Callable[
            [...],
            google.cloud.network_security_v1alpha1.types.sse_realm.ListSACAttachmentsResponse,
        ],
        request: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACAttachmentsRequest,
        response: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACAttachmentsResponse,
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

A pager for iterating through `list_sac_attachments` requests.

This class thinly wraps an initial [ListSACAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACAttachmentsResponse) object, and provides an `__iter__` method to iterate through its `sac_attachments` field.

If there are more pages, the `__iter__` method will make additional `ListSACAttachments` requests and continue to iterate through the `sac_attachments` field on the corresponding responses.

All the usual [ListSACAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACAttachmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSACRealmsAsyncPager](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers.ListSACRealmsAsyncPager)
    
    
    ListSACRealmsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.network_security_v1alpha1.types.sse_realm.ListSACRealmsResponse
            ],
        ],
        request: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACRealmsRequest,
        response: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACRealmsResponse,
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

A pager for iterating through `list_sac_realms` requests.

This class thinly wraps an initial [ListSACRealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACRealmsResponse) object, and provides an `__aiter__` method to iterate through its `sac_realms` field.

If there are more pages, the `__aiter__` method will make additional `ListSACRealms` requests and continue to iterate through the `sac_realms` field on the corresponding responses.

All the usual [ListSACRealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACRealmsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSACRealmsPager](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.services.sse_realm_service.pagers.ListSACRealmsPager)
    
    
    ListSACRealmsPager(
        method: typing.Callable[
            [...],
            google.cloud.network_security_v1alpha1.types.sse_realm.ListSACRealmsResponse,
        ],
        request: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACRealmsRequest,
        response: google.cloud.network_security_v1alpha1.types.sse_realm.ListSACRealmsResponse,
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

A pager for iterating through `list_sac_realms` requests.

This class thinly wraps an initial [ListSACRealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACRealmsResponse) object, and provides an `__iter__` method to iterate through its `sac_realms` field.

If there are more pages, the `__iter__` method will make additional `ListSACRealms` requests and continue to iterate through the `sac_realms` field on the corresponding responses.

All the usual [ListSACRealmsResponse](https://docs.cloud.google.com/python/docs/reference/networksecurity/latest/google.cloud.network_security_v1alpha1.types.ListSACRealmsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
