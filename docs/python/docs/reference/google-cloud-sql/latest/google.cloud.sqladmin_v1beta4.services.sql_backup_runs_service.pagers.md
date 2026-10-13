---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.services.sql_backup_runs_service.pagers
title: Module pagers (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:40.291880+00:00
---

# Module pagers (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.services.sql_backup_runs_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 

API documentation for `sqladmin_v1beta4.services.sql_backup_runs_service.pagers` module.

## Classes 

### [ListAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.services.sql_backup_runs_service.pagers.ListAsyncPager)
    
    
    ListAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.sqladmin_v1beta4.types.cloud_sql_resources.BackupRunsListResponse
            ],
        ],
        request: google.cloud.sqladmin_v1beta4.types.cloud_sql.SqlBackupRunsListRequest,
        response: google.cloud.sqladmin_v1beta4.types.cloud_sql_resources.BackupRunsListResponse,
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

A pager for iterating through `list` requests.

This class thinly wraps an initial [BackupRunsListResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.BackupRunsListResponse) object, and provides an `__aiter__` method to iterate through its `items` field.

If there are more pages, the `__aiter__` method will make additional `List` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [BackupRunsListResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.BackupRunsListResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.services.sql_backup_runs_service.pagers.ListPager)
    
    
    ListPager(
        method: typing.Callable[
            [...],
            google.cloud.sqladmin_v1beta4.types.cloud_sql_resources.BackupRunsListResponse,
        ],
        request: google.cloud.sqladmin_v1beta4.types.cloud_sql.SqlBackupRunsListRequest,
        response: google.cloud.sqladmin_v1beta4.types.cloud_sql_resources.BackupRunsListResponse,
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

A pager for iterating through `list` requests.

This class thinly wraps an initial [BackupRunsListResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.BackupRunsListResponse) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `List` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [BackupRunsListResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1beta4.types.BackupRunsListResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
