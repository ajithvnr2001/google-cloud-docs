---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers
title: Module pagers (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:32.920457+00:00
---

# Module pagers (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 

API documentation for `backupdr_v1.services.backup_dr.pagers` module.

## Classes 

### [FetchBackupPlanAssociationsForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypeAsyncPager)
    
    
    FetchBackupPlanAssociationsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
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

A pager for iterating through `fetch_backup_plan_associations_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupPlanAssociationsForResourceType` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupPlanAssociationsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupPlanAssociationsForResourceTypePager)
    
    
    FetchBackupPlanAssociationsForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.FetchBackupPlanAssociationsForResourceTypeResponse,
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

A pager for iterating through `fetch_backup_plan_associations_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__iter__` method will make additional `FetchBackupPlanAssociationsForResourceType` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupsForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager)
    
    
    FetchBackupsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
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

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchBackupsForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypePager)
    
    
    FetchBackupsForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
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

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDataSourceReferencesForResourceTypeAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypeAsyncPager)
    
    
    FetchDataSourceReferencesForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
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

A pager for iterating through `fetch_data_source_references_for_resource_type` requests.

This class thinly wraps an initial [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__aiter__` method will make additional `FetchDataSourceReferencesForResourceType` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchDataSourceReferencesForResourceTypePager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchDataSourceReferencesForResourceTypePager)
    
    
    FetchDataSourceReferencesForResourceTypePager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.FetchDataSourceReferencesForResourceTypeResponse,
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

A pager for iterating through `fetch_data_source_references_for_resource_type` requests.

This class thinly wraps an initial [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) object, and provides an `__iter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__iter__` method will make additional `FetchDataSourceReferencesForResourceType` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchUsableBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsAsyncPager)
    
    
    FetchUsableBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse,
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

A pager for iterating through `fetch_usable_backup_vaults` requests.

This class thinly wraps an initial [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `FetchUsableBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchUsableBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchUsableBackupVaultsPager)
    
    
    FetchUsableBackupVaultsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchUsableBackupVaultsResponse,
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

A pager for iterating through `fetch_usable_backup_vaults` requests.

This class thinly wraps an initial [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `FetchUsableBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanAssociationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsAsyncPager)
    
    
    ListBackupPlanAssociationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse,
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

A pager for iterating through `list_backup_plan_associations` requests.

This class thinly wraps an initial [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlanAssociations` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanAssociationsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanAssociationsPager)
    
    
    ListBackupPlanAssociationsPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse,
        ],
        request: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsRequest,
        response: google.cloud.backupdr_v1.types.backupplanassociation.ListBackupPlanAssociationsResponse,
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

A pager for iterating through `list_backup_plan_associations` requests.

This class thinly wraps an initial [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_associations` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlanAssociations` requests and continue to iterate through the `backup_plan_associations` field on the corresponding responses.

All the usual [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsAsyncPager)
    
    
    ListBackupPlanRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse,
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

A pager for iterating through `list_backup_plan_revisions` requests.

This class thinly wraps an initial [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `backup_plan_revisions` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlanRevisions` requests and continue to iterate through the `backup_plan_revisions` field on the corresponding responses.

All the usual [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlanRevisionsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlanRevisionsPager)
    
    
    ListBackupPlanRevisionsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlanRevisionsResponse,
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

A pager for iterating through `list_backup_plan_revisions` requests.

This class thinly wraps an initial [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) object, and provides an `__iter__` method to iterate through its `backup_plan_revisions` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlanRevisions` requests and continue to iterate through the `backup_plan_revisions` field on the corresponding responses.

All the usual [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlansAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansAsyncPager)
    
    
    ListBackupPlansAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse,
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

A pager for iterating through `list_backup_plans` requests.

This class thinly wraps an initial [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) object, and provides an `__aiter__` method to iterate through its `backup_plans` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPlans` requests and continue to iterate through the `backup_plans` field on the corresponding responses.

All the usual [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPlansPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupPlansPager)
    
    
    ListBackupPlansPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse
        ],
        request: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansRequest,
        response: google.cloud.backupdr_v1.types.backupplan.ListBackupPlansResponse,
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

A pager for iterating through `list_backup_plans` requests.

This class thinly wraps an initial [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) object, and provides an `__iter__` method to iterate through its `backup_plans` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPlans` requests and continue to iterate through the `backup_plans` field on the corresponding responses.

All the usual [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsAsyncPager)
    
    
    ListBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse,
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

A pager for iterating through `list_backup_vaults` requests.

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupVaultsPager)
    
    
    ListBackupVaultsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupVaultsResponse,
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

A pager for iterating through `list_backup_vaults` requests.

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsAsyncPager)
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse,
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

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListBackupsPager)
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListBackupsRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListBackupsResponse,
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

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourceReferencesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesAsyncPager)
    
    
    ListDataSourceReferencesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse,
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

A pager for iterating through `list_data_source_references` requests.

This class thinly wraps an initial [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) object, and provides an `__aiter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__aiter__` method will make additional `ListDataSourceReferences` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourceReferencesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourceReferencesPager)
    
    
    ListDataSourceReferencesPager(
        method: typing.Callable[
            [...],
            google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse,
        ],
        request: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesRequest,
        response: google.cloud.backupdr_v1.types.datasourcereference.ListDataSourceReferencesResponse,
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

A pager for iterating through `list_data_source_references` requests.

This class thinly wraps an initial [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) object, and provides an `__iter__` method to iterate through its `data_source_references` field.

If there are more pages, the `__iter__` method will make additional `ListDataSourceReferences` requests and continue to iterate through the `data_source_references` field on the corresponding responses.

All the usual [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesAsyncPager)
    
    
    ListDataSourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse,
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

A pager for iterating through `list_data_sources` requests.

This class thinly wraps an initial [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) object, and provides an `__aiter__` method to iterate through its `data_sources` field.

If there are more pages, the `__aiter__` method will make additional `ListDataSources` requests and continue to iterate through the `data_sources` field on the corresponding responses.

All the usual [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataSourcesPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListDataSourcesPager)
    
    
    ListDataSourcesPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse
        ],
        request: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesRequest,
        response: google.cloud.backupdr_v1.types.backupvault.ListDataSourcesResponse,
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

A pager for iterating through `list_data_sources` requests.

This class thinly wraps an initial [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) object, and provides an `__iter__` method to iterate through its `data_sources` field.

If there are more pages, the `__iter__` method will make additional `ListDataSources` requests and continue to iterate through the `data_sources` field on the corresponding responses.

All the usual [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagementServersAsyncPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersAsyncPager)
    
    
    ListManagementServersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest,
        response: google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse,
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

A pager for iterating through `list_management_servers` requests.

This class thinly wraps an initial [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) object, and provides an `__aiter__` method to iterate through its `management_servers` field.

If there are more pages, the `__aiter__` method will make additional `ListManagementServers` requests and continue to iterate through the `management_servers` field on the corresponding responses.

All the usual [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagementServersPager](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.ListManagementServersPager)
    
    
    ListManagementServersPager(
        method: typing.Callable[
            [...], google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse
        ],
        request: google.cloud.backupdr_v1.types.backupdr.ListManagementServersRequest,
        response: google.cloud.backupdr_v1.types.backupdr.ListManagementServersResponse,
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

A pager for iterating through `list_management_servers` requests.

This class thinly wraps an initial [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) object, and provides an `__iter__` method to iterate through its `management_servers` field.

If there are more pages, the `__iter__` method will make additional `ListManagementServers` requests and continue to iterate through the `management_servers` field on the corresponding responses.

All the usual [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
