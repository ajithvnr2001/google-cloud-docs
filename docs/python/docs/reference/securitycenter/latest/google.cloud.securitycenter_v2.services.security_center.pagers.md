---
url: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers
title: Module pagers (1.47.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:19.615387+00:00
---

# Module pagers (1.47.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (1.47.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.47.0 (latest)  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.1  1.33.1  1.32.1  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.1  1.25.0  1.24.1  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.2  1.17.0  1.16.2  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0 

API documentation for `securitycenter_v2.services.security_center.pagers` module.

## Classes 

### [GroupFindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.GroupFindingsAsyncPager)
    
    
    GroupFindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.GroupFindingsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.GroupFindingsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.GroupFindingsResponse,
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

A pager for iterating through `group_findings` requests.

This class thinly wraps an initial [GroupFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.GroupFindingsResponse) object, and provides an `__aiter__` method to iterate through its `group_by_results` field.

If there are more pages, the `__aiter__` method will make additional `GroupFindings` requests and continue to iterate through the `group_by_results` field on the corresponding responses.

All the usual [GroupFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.GroupFindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GroupFindingsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.GroupFindingsPager)
    
    
    GroupFindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.GroupFindingsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.GroupFindingsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.GroupFindingsResponse,
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

A pager for iterating through `group_findings` requests.

This class thinly wraps an initial [GroupFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.GroupFindingsResponse) object, and provides an `__iter__` method to iterate through its `group_by_results` field.

If there are more pages, the `__iter__` method will make additional `GroupFindings` requests and continue to iterate through the `group_by_results` field on the corresponding responses.

All the usual [GroupFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.GroupFindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAttackPathsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListAttackPathsAsyncPager)
    
    
    ListAttackPathsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListAttackPathsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListAttackPathsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListAttackPathsResponse,
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

A pager for iterating through `list_attack_paths` requests.

This class thinly wraps an initial [ListAttackPathsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListAttackPathsResponse) object, and provides an `__aiter__` method to iterate through its `attack_paths` field.

If there are more pages, the `__aiter__` method will make additional `ListAttackPaths` requests and continue to iterate through the `attack_paths` field on the corresponding responses.

All the usual [ListAttackPathsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListAttackPathsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAttackPathsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListAttackPathsPager)
    
    
    ListAttackPathsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListAttackPathsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListAttackPathsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListAttackPathsResponse,
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

A pager for iterating through `list_attack_paths` requests.

This class thinly wraps an initial [ListAttackPathsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListAttackPathsResponse) object, and provides an `__iter__` method to iterate through its `attack_paths` field.

If there are more pages, the `__iter__` method will make additional `ListAttackPaths` requests and continue to iterate through the `attack_paths` field on the corresponding responses.

All the usual [ListAttackPathsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListAttackPathsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBigQueryExportsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListBigQueryExportsAsyncPager)
    
    
    ListBigQueryExportsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListBigQueryExportsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListBigQueryExportsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListBigQueryExportsResponse,
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

A pager for iterating through `list_big_query_exports` requests.

This class thinly wraps an initial [ListBigQueryExportsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse) object, and provides an `__aiter__` method to iterate through its `big_query_exports` field.

If there are more pages, the `__aiter__` method will make additional `ListBigQueryExports` requests and continue to iterate through the `big_query_exports` field on the corresponding responses.

All the usual [ListBigQueryExportsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBigQueryExportsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListBigQueryExportsPager)
    
    
    ListBigQueryExportsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListBigQueryExportsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListBigQueryExportsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListBigQueryExportsResponse,
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

A pager for iterating through `list_big_query_exports` requests.

This class thinly wraps an initial [ListBigQueryExportsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse) object, and provides an `__iter__` method to iterate through its `big_query_exports` field.

If there are more pages, the `__iter__` method will make additional `ListBigQueryExports` requests and continue to iterate through the `big_query_exports` field on the corresponding responses.

All the usual [ListBigQueryExportsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListBigQueryExportsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListFindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListFindingsAsyncPager)
    
    
    ListFindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListFindingsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListFindingsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListFindingsResponse,
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

A pager for iterating through `list_findings` requests.

This class thinly wraps an initial [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListFindingsResponse) object, and provides an `__aiter__` method to iterate through its `list_findings_results` field.

If there are more pages, the `__aiter__` method will make additional `ListFindings` requests and continue to iterate through the `list_findings_results` field on the corresponding responses.

All the usual [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListFindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListFindingsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListFindingsPager)
    
    
    ListFindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListFindingsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListFindingsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListFindingsResponse,
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

A pager for iterating through `list_findings` requests.

This class thinly wraps an initial [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListFindingsResponse) object, and provides an `__iter__` method to iterate through its `list_findings_results` field.

If there are more pages, the `__iter__` method will make additional `ListFindings` requests and continue to iterate through the `list_findings_results` field on the corresponding responses.

All the usual [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListFindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMuteConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListMuteConfigsAsyncPager)
    
    
    ListMuteConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListMuteConfigsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListMuteConfigsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListMuteConfigsResponse,
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

A pager for iterating through `list_mute_configs` requests.

This class thinly wraps an initial [ListMuteConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListMuteConfigsResponse) object, and provides an `__aiter__` method to iterate through its `mute_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListMuteConfigs` requests and continue to iterate through the `mute_configs` field on the corresponding responses.

All the usual [ListMuteConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListMuteConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMuteConfigsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListMuteConfigsPager)
    
    
    ListMuteConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListMuteConfigsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListMuteConfigsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListMuteConfigsResponse,
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

A pager for iterating through `list_mute_configs` requests.

This class thinly wraps an initial [ListMuteConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListMuteConfigsResponse) object, and provides an `__iter__` method to iterate through its `mute_configs` field.

If there are more pages, the `__iter__` method will make additional `ListMuteConfigs` requests and continue to iterate through the `mute_configs` field on the corresponding responses.

All the usual [ListMuteConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListMuteConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListNotificationConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListNotificationConfigsAsyncPager)
    
    
    ListNotificationConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListNotificationConfigsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListNotificationConfigsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListNotificationConfigsResponse,
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

A pager for iterating through `list_notification_configs` requests.

This class thinly wraps an initial [ListNotificationConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse) object, and provides an `__aiter__` method to iterate through its `notification_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListNotificationConfigs` requests and continue to iterate through the `notification_configs` field on the corresponding responses.

All the usual [ListNotificationConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListNotificationConfigsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListNotificationConfigsPager)
    
    
    ListNotificationConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListNotificationConfigsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListNotificationConfigsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListNotificationConfigsResponse,
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

A pager for iterating through `list_notification_configs` requests.

This class thinly wraps an initial [ListNotificationConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse) object, and provides an `__iter__` method to iterate through its `notification_configs` field.

If there are more pages, the `__iter__` method will make additional `ListNotificationConfigs` requests and continue to iterate through the `notification_configs` field on the corresponding responses.

All the usual [ListNotificationConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListNotificationConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceValueConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListResourceValueConfigsAsyncPager)
    
    
    ListResourceValueConfigsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListResourceValueConfigsResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListResourceValueConfigsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListResourceValueConfigsResponse,
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

A pager for iterating through `list_resource_value_configs` requests.

This class thinly wraps an initial [ListResourceValueConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse) object, and provides an `__aiter__` method to iterate through its `resource_value_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceValueConfigs` requests and continue to iterate through the `resource_value_configs` field on the corresponding responses.

All the usual [ListResourceValueConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceValueConfigsPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListResourceValueConfigsPager)
    
    
    ListResourceValueConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListResourceValueConfigsResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListResourceValueConfigsRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListResourceValueConfigsResponse,
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

A pager for iterating through `list_resource_value_configs` requests.

This class thinly wraps an initial [ListResourceValueConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse) object, and provides an `__iter__` method to iterate through its `resource_value_configs` field.

If there are more pages, the `__iter__` method will make additional `ListResourceValueConfigs` requests and continue to iterate through the `resource_value_configs` field on the corresponding responses.

All the usual [ListResourceValueConfigsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListResourceValueConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListSourcesAsyncPager)
    
    
    ListSourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListSourcesResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListSourcesRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListSourcesResponse,
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

A pager for iterating through `list_sources` requests.

This class thinly wraps an initial [ListSourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListSourcesResponse) object, and provides an `__aiter__` method to iterate through its `sources` field.

If there are more pages, the `__aiter__` method will make additional `ListSources` requests and continue to iterate through the `sources` field on the corresponding responses.

All the usual [ListSourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSourcesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListSourcesPager)
    
    
    ListSourcesPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListSourcesResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListSourcesRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListSourcesResponse,
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

A pager for iterating through `list_sources` requests.

This class thinly wraps an initial [ListSourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListSourcesResponse) object, and provides an `__iter__` method to iterate through its `sources` field.

If there are more pages, the `__iter__` method will make additional `ListSources` requests and continue to iterate through the `sources` field on the corresponding responses.

All the usual [ListSourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListValuedResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListValuedResourcesAsyncPager)
    
    
    ListValuedResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v2.types.securitycenter_service.ListValuedResourcesResponse
            ],
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListValuedResourcesRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListValuedResourcesResponse,
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

A pager for iterating through `list_valued_resources` requests.

This class thinly wraps an initial [ListValuedResourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListValuedResourcesResponse) object, and provides an `__aiter__` method to iterate through its `valued_resources` field.

If there are more pages, the `__aiter__` method will make additional `ListValuedResources` requests and continue to iterate through the `valued_resources` field on the corresponding responses.

All the usual [ListValuedResourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListValuedResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListValuedResourcesPager](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.services.security_center.pagers.ListValuedResourcesPager)
    
    
    ListValuedResourcesPager(
        method: typing.Callable[
            [...],
            google.cloud.securitycenter_v2.types.securitycenter_service.ListValuedResourcesResponse,
        ],
        request: google.cloud.securitycenter_v2.types.securitycenter_service.ListValuedResourcesRequest,
        response: google.cloud.securitycenter_v2.types.securitycenter_service.ListValuedResourcesResponse,
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

A pager for iterating through `list_valued_resources` requests.

This class thinly wraps an initial [ListValuedResourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListValuedResourcesResponse) object, and provides an `__iter__` method to iterate through its `valued_resources` field.

If there are more pages, the `__iter__` method will make additional `ListValuedResources` requests and continue to iterate through the `valued_resources` field on the corresponding responses.

All the usual [ListValuedResourcesResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v2.types.ListValuedResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
