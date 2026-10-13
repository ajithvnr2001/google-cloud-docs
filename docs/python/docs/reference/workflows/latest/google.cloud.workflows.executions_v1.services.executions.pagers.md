---
url: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.services.executions.pagers
title: Module pagers (1.24.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:56:13.214569+00:00
---

# Module pagers (1.24.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.services.executions.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (1.24.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.24.0 (latest)  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.1  1.17.0  1.16.0  1.15.1  1.14.5  1.13.0  1.12.0  1.11.0  1.10.2  1.9.1  1.8.0  1.7.4  1.6.3  1.5.0  1.4.1  1.3.0  1.2.3  1.1.0  1.0.0  0.3.2  0.2.0  0.1.0 

API documentation for `workflows.executions_v1.services.executions.pagers` module.

## Classes 

### [ListExecutionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.services.executions.pagers.ListExecutionsAsyncPager)
    
    
    ListExecutionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.workflows.executions_v1.types.executions.ListExecutionsResponse
            ],
        ],
        request: google.cloud.workflows.executions_v1.types.executions.ListExecutionsRequest,
        response: google.cloud.workflows.executions_v1.types.executions.ListExecutionsResponse,
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

A pager for iterating through `list_executions` requests.

This class thinly wraps an initial [ListExecutionsResponse](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ListExecutionsResponse) object, and provides an `__aiter__` method to iterate through its `executions` field.

If there are more pages, the `__aiter__` method will make additional `ListExecutions` requests and continue to iterate through the `executions` field on the corresponding responses.

All the usual [ListExecutionsResponse](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ListExecutionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListExecutionsPager](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.services.executions.pagers.ListExecutionsPager)
    
    
    ListExecutionsPager(
        method: typing.Callable[
            [...],
            google.cloud.workflows.executions_v1.types.executions.ListExecutionsResponse,
        ],
        request: google.cloud.workflows.executions_v1.types.executions.ListExecutionsRequest,
        response: google.cloud.workflows.executions_v1.types.executions.ListExecutionsResponse,
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

A pager for iterating through `list_executions` requests.

This class thinly wraps an initial [ListExecutionsResponse](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ListExecutionsResponse) object, and provides an `__iter__` method to iterate through its `executions` field.

If there are more pages, the `__iter__` method will make additional `ListExecutions` requests and continue to iterate through the `executions` field on the corresponding responses.

All the usual [ListExecutionsResponse](https://docs.cloud.google.com/python/docs/reference/workflows/latest/google.cloud.workflows.executions_v1.types.ListExecutionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
