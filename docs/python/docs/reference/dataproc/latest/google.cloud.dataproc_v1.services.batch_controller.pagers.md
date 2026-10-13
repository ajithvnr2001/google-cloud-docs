---
url: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.batch_controller.pagers
title: Module pagers (5.31.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:40.062061+00:00
---

# Module pagers (5.31.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.batch_controller.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (5.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

5.31.0 (latest)  5.30.0  5.29.0  5.28.0  5.27.0  5.26.0  5.25.0  5.24.0  5.23.0  5.22.0  5.21.0  5.20.0  5.18.1  5.17.1  5.16.0  5.15.1  5.14.0  5.13.0  5.12.0  5.10.2  5.9.3  5.8.0  5.7.0  5.6.0  5.5.1  5.4.3  5.3.0  5.2.0  5.1.0  5.0.3  4.0.3  3.3.2  3.2.0  3.1.1  3.0.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.0.2  1.1.3  1.0.1  0.8.2  0.7.0  0.6.1  0.5.0 

API documentation for `dataproc_v1.services.batch_controller.pagers` module.

## Classes 

### [ListBatchesAsyncPager](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.batch_controller.pagers.ListBatchesAsyncPager)
    
    
    ListBatchesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.dataproc_v1.types.batches.ListBatchesResponse],
        ],
        request: google.cloud.dataproc_v1.types.batches.ListBatchesRequest,
        response: google.cloud.dataproc_v1.types.batches.ListBatchesResponse,
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

A pager for iterating through `list_batches` requests.

This class thinly wraps an initial [ListBatchesResponse](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.ListBatchesResponse) object, and provides an `__aiter__` method to iterate through its `batches` field.

If there are more pages, the `__aiter__` method will make additional `ListBatches` requests and continue to iterate through the `batches` field on the corresponding responses.

All the usual [ListBatchesResponse](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.ListBatchesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBatchesPager](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.services.batch_controller.pagers.ListBatchesPager)
    
    
    ListBatchesPager(
        method: typing.Callable[
            [...], google.cloud.dataproc_v1.types.batches.ListBatchesResponse
        ],
        request: google.cloud.dataproc_v1.types.batches.ListBatchesRequest,
        response: google.cloud.dataproc_v1.types.batches.ListBatchesResponse,
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

A pager for iterating through `list_batches` requests.

This class thinly wraps an initial [ListBatchesResponse](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.ListBatchesResponse) object, and provides an `__iter__` method to iterate through its `batches` field.

If there are more pages, the `__iter__` method will make additional `ListBatches` requests and continue to iterate through the `batches` field on the corresponding responses.

All the usual [ListBatchesResponse](https://docs.cloud.google.com/python/docs/reference/dataproc/latest/google.cloud.dataproc_v1.types.ListBatchesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
