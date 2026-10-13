---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers
title: Module pagers (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:02.352541+00:00
---

# Module pagers (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 

API documentation for `visionai_v1alpha1.services.streams_service.pagers` module.

## Classes 

### [ListClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListClustersAsyncPager)
    
    
    ListClustersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.visionai_v1alpha1.types.streams_service.ListClustersResponse
            ],
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListClustersRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListClustersResponse,
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

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListClustersResponse) object, and provides an `__aiter__` method to iterate through its `clusters` field.

If there are more pages, the `__aiter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListClustersPager)
    
    
    ListClustersPager(
        method: typing.Callable[
            [...], google.cloud.visionai_v1alpha1.types.streams_service.ListClustersResponse
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListClustersRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListClustersResponse,
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

A pager for iterating through `list_clusters` requests.

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListClustersResponse) object, and provides an `__iter__` method to iterate through its `clusters` field.

If there are more pages, the `__iter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEventsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListEventsAsyncPager)
    
    
    ListEventsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.visionai_v1alpha1.types.streams_service.ListEventsResponse
            ],
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListEventsRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListEventsResponse,
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

A pager for iterating through `list_events` requests.

This class thinly wraps an initial [ListEventsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListEventsResponse) object, and provides an `__aiter__` method to iterate through its `events` field.

If there are more pages, the `__aiter__` method will make additional `ListEvents` requests and continue to iterate through the `events` field on the corresponding responses.

All the usual [ListEventsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListEventsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListEventsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListEventsPager)
    
    
    ListEventsPager(
        method: typing.Callable[
            [...], google.cloud.visionai_v1alpha1.types.streams_service.ListEventsResponse
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListEventsRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListEventsResponse,
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

A pager for iterating through `list_events` requests.

This class thinly wraps an initial [ListEventsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListEventsResponse) object, and provides an `__iter__` method to iterate through its `events` field.

If there are more pages, the `__iter__` method will make additional `ListEvents` requests and continue to iterate through the `events` field on the corresponding responses.

All the usual [ListEventsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListEventsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSeriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListSeriesAsyncPager)
    
    
    ListSeriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.visionai_v1alpha1.types.streams_service.ListSeriesResponse
            ],
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListSeriesRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListSeriesResponse,
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

A pager for iterating through `list_series` requests.

This class thinly wraps an initial [ListSeriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListSeriesResponse) object, and provides an `__aiter__` method to iterate through its `series` field.

If there are more pages, the `__aiter__` method will make additional `ListSeries` requests and continue to iterate through the `series` field on the corresponding responses.

All the usual [ListSeriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListSeriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSeriesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListSeriesPager)
    
    
    ListSeriesPager(
        method: typing.Callable[
            [...], google.cloud.visionai_v1alpha1.types.streams_service.ListSeriesResponse
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListSeriesRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListSeriesResponse,
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

A pager for iterating through `list_series` requests.

This class thinly wraps an initial [ListSeriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListSeriesResponse) object, and provides an `__iter__` method to iterate through its `series` field.

If there are more pages, the `__iter__` method will make additional `ListSeries` requests and continue to iterate through the `series` field on the corresponding responses.

All the usual [ListSeriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListSeriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListStreamsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListStreamsAsyncPager)
    
    
    ListStreamsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.visionai_v1alpha1.types.streams_service.ListStreamsResponse
            ],
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListStreamsRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListStreamsResponse,
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

This class thinly wraps an initial [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListStreamsResponse) object, and provides an `__aiter__` method to iterate through its `streams` field.

If there are more pages, the `__aiter__` method will make additional `ListStreams` requests and continue to iterate through the `streams` field on the corresponding responses.

All the usual [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListStreamsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListStreamsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.services.streams_service.pagers.ListStreamsPager)
    
    
    ListStreamsPager(
        method: typing.Callable[
            [...], google.cloud.visionai_v1alpha1.types.streams_service.ListStreamsResponse
        ],
        request: google.cloud.visionai_v1alpha1.types.streams_service.ListStreamsRequest,
        response: google.cloud.visionai_v1alpha1.types.streams_service.ListStreamsResponse,
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

This class thinly wraps an initial [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListStreamsResponse) object, and provides an `__iter__` method to iterate through its `streams` field.

If there are more pages, the `__iter__` method will make additional `ListStreams` requests and continue to iterate through the `streams` field on the corresponding responses.

All the usual [ListStreamsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.ListStreamsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
