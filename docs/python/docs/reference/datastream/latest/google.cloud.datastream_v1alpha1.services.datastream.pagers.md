---
url: https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers
title: Module pagers (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:00:54.167071+00:00
---

# Module pagers (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.2  1.12.0  1.11.0  1.10.1  1.9.5  1.8.0  1.7.0  1.6.1  1.5.1  1.4.1  1.3.0  1.2.2  1.1.1  1.0.2  0.4.3  0.3.1  0.2.0  0.1.3 

API documentation for `datastream_v1alpha1.services.datastream.pagers` module.

## Classes 

### [FetchStaticIpsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.FetchStaticIpsAsyncPager)
    
    
    FetchStaticIpsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.datastream_v1alpha1.types.datastream.FetchStaticIpsResponse
            ],
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.FetchStaticIpsRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.FetchStaticIpsResponse,
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

A pager for iterating through `fetch_static_ips` requests.

This class thinly wraps an initial [FetchStaticIpsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse) object, and provides an `__aiter__` method to iterate through its `static_ips` field.

If there are more pages, the `__aiter__` method will make additional `FetchStaticIps` requests and continue to iterate through the `static_ips` field on the corresponding responses.

All the usual [FetchStaticIpsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchStaticIpsPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.FetchStaticIpsPager)
    
    
    FetchStaticIpsPager(
        method: typing.Callable[
            [...], google.cloud.datastream_v1alpha1.types.datastream.FetchStaticIpsResponse
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.FetchStaticIpsRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.FetchStaticIpsResponse,
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

A pager for iterating through `fetch_static_ips` requests.

This class thinly wraps an initial [FetchStaticIpsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse) object, and provides an `__iter__` method to iterate through its `static_ips` field.

If there are more pages, the `__iter__` method will make additional `FetchStaticIps` requests and continue to iterate through the `static_ips` field on the corresponding responses.

All the usual [FetchStaticIpsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.FetchStaticIpsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectionProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListConnectionProfilesAsyncPager)
    
    
    ListConnectionProfilesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.datastream_v1alpha1.types.datastream.ListConnectionProfilesResponse
            ],
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListConnectionProfilesRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListConnectionProfilesResponse,
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

A pager for iterating through `list_connection_profiles` requests.

This class thinly wraps an initial [ListConnectionProfilesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse) object, and provides an `__aiter__` method to iterate through its `connection_profiles` field.

If there are more pages, the `__aiter__` method will make additional `ListConnectionProfiles` requests and continue to iterate through the `connection_profiles` field on the corresponding responses.

All the usual [ListConnectionProfilesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectionProfilesPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListConnectionProfilesPager)
    
    
    ListConnectionProfilesPager(
        method: typing.Callable[
            [...],
            google.cloud.datastream_v1alpha1.types.datastream.ListConnectionProfilesResponse,
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListConnectionProfilesRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListConnectionProfilesResponse,
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

A pager for iterating through `list_connection_profiles` requests.

This class thinly wraps an initial [ListConnectionProfilesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse) object, and provides an `__iter__` method to iterate through its `connection_profiles` field.

If there are more pages, the `__iter__` method will make additional `ListConnectionProfiles` requests and continue to iterate through the `connection_profiles` field on the corresponding responses.

All the usual [ListConnectionProfilesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListConnectionProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPrivateConnectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListPrivateConnectionsAsyncPager)
    
    
    ListPrivateConnectionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.datastream_v1alpha1.types.datastream.ListPrivateConnectionsResponse
            ],
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListPrivateConnectionsRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListPrivateConnectionsResponse,
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

A pager for iterating through `list_private_connections` requests.

This class thinly wraps an initial [ListPrivateConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse) object, and provides an `__aiter__` method to iterate through its `private_connections` field.

If there are more pages, the `__aiter__` method will make additional `ListPrivateConnections` requests and continue to iterate through the `private_connections` field on the corresponding responses.

All the usual [ListPrivateConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPrivateConnectionsPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListPrivateConnectionsPager)
    
    
    ListPrivateConnectionsPager(
        method: typing.Callable[
            [...],
            google.cloud.datastream_v1alpha1.types.datastream.ListPrivateConnectionsResponse,
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListPrivateConnectionsRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListPrivateConnectionsResponse,
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

A pager for iterating through `list_private_connections` requests.

This class thinly wraps an initial [ListPrivateConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse) object, and provides an `__iter__` method to iterate through its `private_connections` field.

If there are more pages, the `__iter__` method will make additional `ListPrivateConnections` requests and continue to iterate through the `private_connections` field on the corresponding responses.

All the usual [ListPrivateConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListPrivateConnectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRoutesAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListRoutesAsyncPager)
    
    
    ListRoutesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.datastream_v1alpha1.types.datastream.ListRoutesResponse
            ],
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListRoutesRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListRoutesResponse,
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

A pager for iterating through `list_routes` requests.

This class thinly wraps an initial [ListRoutesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListRoutesResponse) object, and provides an `__aiter__` method to iterate through its `routes` field.

If there are more pages, the `__aiter__` method will make additional `ListRoutes` requests and continue to iterate through the `routes` field on the corresponding responses.

All the usual [ListRoutesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListRoutesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRoutesPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListRoutesPager)
    
    
    ListRoutesPager(
        method: typing.Callable[
            [...], google.cloud.datastream_v1alpha1.types.datastream.ListRoutesResponse
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListRoutesRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListRoutesResponse,
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

A pager for iterating through `list_routes` requests.

This class thinly wraps an initial [ListRoutesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListRoutesResponse) object, and provides an `__iter__` method to iterate through its `routes` field.

If there are more pages, the `__iter__` method will make additional `ListRoutes` requests and continue to iterate through the `routes` field on the corresponding responses.

All the usual [ListRoutesResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListRoutesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListStreamsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListStreamsAsyncPager)
    
    
    ListStreamsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.datastream_v1alpha1.types.datastream.ListStreamsResponse
            ],
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListStreamsRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListStreamsResponse,
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

A pager for iterating through `list_streams` requests.

This class thinly wraps an initial [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListStreamsResponse) object, and provides an `__aiter__` method to iterate through its `streams` field.

If there are more pages, the `__aiter__` method will make additional `ListStreams` requests and continue to iterate through the `streams` field on the corresponding responses.

All the usual [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListStreamsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListStreamsPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.services.datastream.pagers.ListStreamsPager)
    
    
    ListStreamsPager(
        method: typing.Callable[
            [...], google.cloud.datastream_v1alpha1.types.datastream.ListStreamsResponse
        ],
        request: google.cloud.datastream_v1alpha1.types.datastream.ListStreamsRequest,
        response: google.cloud.datastream_v1alpha1.types.datastream.ListStreamsResponse,
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

A pager for iterating through `list_streams` requests.

This class thinly wraps an initial [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListStreamsResponse) object, and provides an `__iter__` method to iterate through its `streams` field.

If there are more pages, the `__iter__` method will make additional `ListStreams` requests and continue to iterate through the `streams` field on the corresponding responses.

All the usual [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1alpha1.types.ListStreamsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
