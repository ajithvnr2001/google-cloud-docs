---
url: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers
title: Module pagers (0.22.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:22.868649+00:00
---

# Module pagers (0.22.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.22.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.4 (latest)  0.22.3  0.21.0  0.20.0  0.19.0  0.18.0  0.17.37  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.2  0.2.0  0.1.2 

API documentation for `batch_v1.services.batch_service.pagers` module.

## Classes 

### [ListJobsAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListJobsAsyncPager)
    
    
    ListJobsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.batch_v1.types.batch.ListJobsResponse]
        ],
        request: google.cloud.batch_v1.types.batch.ListJobsRequest,
        response: google.cloud.batch_v1.types.batch.ListJobsResponse,
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

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) object, and provides an `__aiter__` method to iterate through its `jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobsPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListJobsPager)
    
    
    ListJobsPager(
        method: typing.Callable[[...], google.cloud.batch_v1.types.batch.ListJobsResponse],
        request: google.cloud.batch_v1.types.batch.ListJobsRequest,
        response: google.cloud.batch_v1.types.batch.ListJobsResponse,
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

This class thinly wraps an initial [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) object, and provides an `__iter__` method to iterate through its `jobs` field.

If there are more pages, the `__iter__` method will make additional `ListJobs` requests and continue to iterate through the `jobs` field on the corresponding responses.

All the usual [ListJobsResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksAsyncPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListTasksAsyncPager)
    
    
    ListTasksAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.batch_v1.types.batch.ListTasksResponse]
        ],
        request: google.cloud.batch_v1.types.batch.ListTasksRequest,
        response: google.cloud.batch_v1.types.batch.ListTasksResponse,
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

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) object, and provides an `__aiter__` method to iterate through its `tasks` field.

If there are more pages, the `__aiter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTasksPager](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.services.batch_service.pagers.ListTasksPager)
    
    
    ListTasksPager(
        method: typing.Callable[[...], google.cloud.batch_v1.types.batch.ListTasksResponse],
        request: google.cloud.batch_v1.types.batch.ListTasksRequest,
        response: google.cloud.batch_v1.types.batch.ListTasksResponse,
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

This class thinly wraps an initial [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) object, and provides an `__iter__` method to iterate through its `tasks` field.

If there are more pages, the `__iter__` method will make additional `ListTasks` requests and continue to iterate through the `tasks` field on the corresponding responses.

All the usual [ListTasksResponse](https://docs.cloud.google.com/python/docs/reference/batch/latest/google.cloud.batch_v1.types.ListTasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
