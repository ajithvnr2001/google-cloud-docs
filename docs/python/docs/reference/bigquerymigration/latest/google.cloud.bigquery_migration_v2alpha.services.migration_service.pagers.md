---
url: https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.services.migration_service.pagers
title: Module pagers (0.15.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:35.243847+00:00
---

# Module pagers (0.15.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.services.migration_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.15.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.2 (latest)  0.15.1  0.14.0  0.13.0  0.12.0  0.11.15  0.10.0  0.9.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.3  0.3.1  0.2.1  0.1.0 

API documentation for `bigquery_migration_v2alpha.services.migration_service.pagers` module.

## Classes 

### [ListMigrationSubtasksAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.services.migration_service.pagers.ListMigrationSubtasksAsyncPager)
    
    
    ListMigrationSubtasksAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationSubtasksResponse
            ],
        ],
        request: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationSubtasksRequest,
        response: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationSubtasksResponse,
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

A pager for iterating through `list_migration_subtasks` requests.

This class thinly wraps an initial [ListMigrationSubtasksResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationSubtasksResponse) object, and provides an `__aiter__` method to iterate through its `migration_subtasks` field.

If there are more pages, the `__aiter__` method will make additional `ListMigrationSubtasks` requests and continue to iterate through the `migration_subtasks` field on the corresponding responses.

All the usual [ListMigrationSubtasksResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationSubtasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMigrationSubtasksPager](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.services.migration_service.pagers.ListMigrationSubtasksPager)
    
    
    ListMigrationSubtasksPager(
        method: typing.Callable[
            [...],
            google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationSubtasksResponse,
        ],
        request: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationSubtasksRequest,
        response: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationSubtasksResponse,
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

A pager for iterating through `list_migration_subtasks` requests.

This class thinly wraps an initial [ListMigrationSubtasksResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationSubtasksResponse) object, and provides an `__iter__` method to iterate through its `migration_subtasks` field.

If there are more pages, the `__iter__` method will make additional `ListMigrationSubtasks` requests and continue to iterate through the `migration_subtasks` field on the corresponding responses.

All the usual [ListMigrationSubtasksResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationSubtasksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMigrationWorkflowsAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.services.migration_service.pagers.ListMigrationWorkflowsAsyncPager)
    
    
    ListMigrationWorkflowsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationWorkflowsResponse
            ],
        ],
        request: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationWorkflowsRequest,
        response: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationWorkflowsResponse,
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

A pager for iterating through `list_migration_workflows` requests.

This class thinly wraps an initial [ListMigrationWorkflowsResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationWorkflowsResponse) object, and provides an `__aiter__` method to iterate through its `migration_workflows` field.

If there are more pages, the `__aiter__` method will make additional `ListMigrationWorkflows` requests and continue to iterate through the `migration_workflows` field on the corresponding responses.

All the usual [ListMigrationWorkflowsResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationWorkflowsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListMigrationWorkflowsPager](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.services.migration_service.pagers.ListMigrationWorkflowsPager)
    
    
    ListMigrationWorkflowsPager(
        method: typing.Callable[
            [...],
            google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationWorkflowsResponse,
        ],
        request: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationWorkflowsRequest,
        response: google.cloud.bigquery_migration_v2alpha.types.migration_service.ListMigrationWorkflowsResponse,
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

A pager for iterating through `list_migration_workflows` requests.

This class thinly wraps an initial [ListMigrationWorkflowsResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationWorkflowsResponse) object, and provides an `__iter__` method to iterate through its `migration_workflows` field.

If there are more pages, the `__iter__` method will make additional `ListMigrationWorkflows` requests and continue to iterate through the `migration_workflows` field on the corresponding responses.

All the usual [ListMigrationWorkflowsResponse](https://docs.cloud.google.com/python/docs/reference/bigquerymigration/latest/google.cloud.bigquery_migration_v2alpha.types.ListMigrationWorkflowsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
