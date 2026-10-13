---
url: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers
title: Module pagers (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:51.312461+00:00
---

# Module pagers (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.2  2.9.0  2.8.0  2.7.1  2.6.0  2.5.0  2.4.0  2.3.1  2.2.2  2.1.0  2.0.1  1.13.0  1.12.3  1.11.0  1.10.0  1.9.0  1.8.1  1.7.0  1.6.2  1.5.1  1.4.3  1.3.0  1.2.0  1.1.3  1.0.1  0.2.1  0.1.0 

API documentation for `dataplex_v1.services.dataplex_service.pagers` module.

## Classes 

### [ListAssetActionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListAssetActionsAsyncPager)
    
    
    ListAssetActionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListActionsResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListAssetActionsRequest,
        response: google.cloud.dataplex_v1.types.service.ListActionsResponse,
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

A pager for iterating through `list_asset_actions` requests.

This class thinly wraps an initial [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) object, and provides an `__aiter__` method to iterate through its `actions` field.

If there are more pages, the `__aiter__` method will make additional `ListAssetActions` requests and continue to iterate through the `actions` field on the corresponding responses.

All the usual [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetActionsPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListAssetActionsPager)
    
    
    ListAssetActionsPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListActionsResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListAssetActionsRequest,
        response: google.cloud.dataplex_v1.types.service.ListActionsResponse,
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

A pager for iterating through `list_asset_actions` requests.

This class thinly wraps an initial [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) object, and provides an `__iter__` method to iterate through its `actions` field.

If there are more pages, the `__iter__` method will make additional `ListAssetActions` requests and continue to iterate through the `actions` field on the corresponding responses.

All the usual [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListAssetsAsyncPager)
    
    
    ListAssetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListAssetsResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListAssetsRequest,
        response: google.cloud.dataplex_v1.types.service.ListAssetsResponse,
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

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListAssetsResponse) object, and provides an `__aiter__` method to iterate through its `assets` field.

If there are more pages, the `__aiter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListAssetsPager)
    
    
    ListAssetsPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListAssetsResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListAssetsRequest,
        response: google.cloud.dataplex_v1.types.service.ListAssetsResponse,
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

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListAssetsResponse) object, and provides an `__iter__` method to iterate through its `assets` field.

If there are more pages, the `__iter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListJobsAsyncPager)
    
    
    ListJobsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.dataplex_v1.types.service.ListJobsResponse]
        ],
        request: google.cloud.dataplex_v1.types.service.ListJobsRequest,
        response: google.cloud.dataplex_v1.types.service.ListJobsResponse,
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

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListJobsResponse) object, and provides an `__aiter__` method to iterate through its `jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListJobsPager)
    
    
    ListJobsPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListJobsResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListJobsRequest,
        response: google.cloud.dataplex_v1.types.service.ListJobsResponse,
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

A pager for iterating through `list_jobs` requests.

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListJobsResponse) object, and provides an `__iter__` method to iterate through its `jobs` field.

If there are more pages, the `__iter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLakeActionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListLakeActionsAsyncPager)
    
    
    ListLakeActionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListActionsResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListLakeActionsRequest,
        response: google.cloud.dataplex_v1.types.service.ListActionsResponse,
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

A pager for iterating through `list_lake_actions` requests.

This class thinly wraps an initial [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) object, and provides an `__aiter__` method to iterate through its `actions` field.

If there are more pages, the `__aiter__` method will make additional `ListLakeActions` requests and continue to iterate through the `actions` field on the corresponding responses.

All the usual [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLakeActionsPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListLakeActionsPager)
    
    
    ListLakeActionsPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListActionsResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListLakeActionsRequest,
        response: google.cloud.dataplex_v1.types.service.ListActionsResponse,
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

A pager for iterating through `list_lake_actions` requests.

This class thinly wraps an initial [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) object, and provides an `__iter__` method to iterate through its `actions` field.

If there are more pages, the `__iter__` method will make additional `ListLakeActions` requests and continue to iterate through the `actions` field on the corresponding responses.

All the usual [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLakesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListLakesAsyncPager)
    
    
    ListLakesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListLakesResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListLakesRequest,
        response: google.cloud.dataplex_v1.types.service.ListLakesResponse,
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

A pager for iterating through `list_lakes` requests.

This class thinly wraps an initial [ListLakesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListLakesResponse) object, and provides an `__aiter__` method to iterate through its `lakes` field.

If there are more pages, the `__aiter__` method will make additional `ListLakes` requests and continue to iterate through the `lakes` field on the corresponding responses.

All the usual [ListLakesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListLakesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLakesPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListLakesPager)
    
    
    ListLakesPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListLakesResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListLakesRequest,
        response: google.cloud.dataplex_v1.types.service.ListLakesResponse,
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

A pager for iterating through `list_lakes` requests.

This class thinly wraps an initial [ListLakesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListLakesResponse) object, and provides an `__iter__` method to iterate through its `lakes` field.

If there are more pages, the `__iter__` method will make additional `ListLakes` requests and continue to iterate through the `lakes` field on the corresponding responses.

All the usual [ListLakesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListLakesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListTasksAsyncPager)
    
    
    ListTasksAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListTasksResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListTasksRequest,
        response: google.cloud.dataplex_v1.types.service.ListTasksResponse,
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

A pager for iterating through `list_tasks` requests.

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListTasksResponse) object, and provides an `__aiter__` method to iterate through its `tasks` field.

If there are more pages, the `__aiter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListTasksPager)
    
    
    ListTasksPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListTasksResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListTasksRequest,
        response: google.cloud.dataplex_v1.types.service.ListTasksResponse,
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

A pager for iterating through `list_tasks` requests.

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListTasksResponse) object, and provides an `__iter__` method to iterate through its `tasks` field.

If there are more pages, the `__iter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListZoneActionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListZoneActionsAsyncPager)
    
    
    ListZoneActionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListActionsResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListZoneActionsRequest,
        response: google.cloud.dataplex_v1.types.service.ListActionsResponse,
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

A pager for iterating through `list_zone_actions` requests.

This class thinly wraps an initial [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) object, and provides an `__aiter__` method to iterate through its `actions` field.

If there are more pages, the `__aiter__` method will make additional `ListZoneActions` requests and continue to iterate through the `actions` field on the corresponding responses.

All the usual [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListZoneActionsPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListZoneActionsPager)
    
    
    ListZoneActionsPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListActionsResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListZoneActionsRequest,
        response: google.cloud.dataplex_v1.types.service.ListActionsResponse,
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

A pager for iterating through `list_zone_actions` requests.

This class thinly wraps an initial [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) object, and provides an `__iter__` method to iterate through its `actions` field.

If there are more pages, the `__iter__` method will make additional `ListZoneActions` requests and continue to iterate through the `actions` field on the corresponding responses.

All the usual [ListActionsResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListActionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListZonesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListZonesAsyncPager)
    
    
    ListZonesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataplex_v1.types.service.ListZonesResponse],
        ],
        request: google.cloud.dataplex_v1.types.service.ListZonesRequest,
        response: google.cloud.dataplex_v1.types.service.ListZonesResponse,
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

A pager for iterating through `list_zones` requests.

This class thinly wraps an initial [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListZonesResponse) object, and provides an `__aiter__` method to iterate through its `zones` field.

If there are more pages, the `__aiter__` method will make additional `ListZones` requests and continue to iterate through the `zones` field on the corresponding responses.

All the usual [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListZonesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListZonesPager](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.dataplex_service.pagers.ListZonesPager)
    
    
    ListZonesPager(
        method: typing.Callable[
            [...], google.cloud.dataplex_v1.types.service.ListZonesResponse
        ],
        request: google.cloud.dataplex_v1.types.service.ListZonesRequest,
        response: google.cloud.dataplex_v1.types.service.ListZonesResponse,
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

A pager for iterating through `list_zones` requests.

This class thinly wraps an initial [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListZonesResponse) object, and provides an `__iter__` method to iterate through its `zones` field.

If there are more pages, the `__iter__` method will make additional `ListZones` requests and continue to iterate through the `zones` field on the corresponding responses.

All the usual [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.ListZonesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
