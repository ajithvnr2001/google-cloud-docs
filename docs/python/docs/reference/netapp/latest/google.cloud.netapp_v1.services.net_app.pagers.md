---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers
title: Module pagers (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:07.797957+00:00
---

# Module pagers (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 

API documentation for `netapp_v1.services.net_app.pagers` module.

## Classes 

### [ListActiveDirectoriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesAsyncPager)
    
    
    ListActiveDirectoriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
        response: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse,
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

A pager for iterating through `list_active_directories` requests.

This class thinly wraps an initial [ListActiveDirectoriesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesResponse) object, and provides an `__aiter__` method to iterate through its `active_directories` field.

If there are more pages, the `__aiter__` method will make additional `ListActiveDirectories` requests and continue to iterate through the `active_directories` field on the corresponding responses.

All the usual [ListActiveDirectoriesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListActiveDirectoriesPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListActiveDirectoriesPager)
    
    
    ListActiveDirectoriesPager(
        method: typing.Callable[
            [...],
            google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse,
        ],
        request: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesRequest,
        response: google.cloud.netapp_v1.types.active_directory.ListActiveDirectoriesResponse,
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

A pager for iterating through `list_active_directories` requests.

This class thinly wraps an initial [ListActiveDirectoriesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesResponse) object, and provides an `__iter__` method to iterate through its `active_directories` field.

If there are more pages, the `__iter__` method will make additional `ListActiveDirectories` requests and continue to iterate through the `active_directories` field on the corresponding responses.

All the usual [ListActiveDirectoriesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListActiveDirectoriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesAsyncPager)
    
    
    ListBackupPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest,
        response: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse,
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

A pager for iterating through `list_backup_policies` requests.

This class thinly wraps an initial [ListBackupPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `backup_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupPolicies` requests and continue to iterate through the `backup_policies` field on the corresponding responses.

All the usual [ListBackupPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupPoliciesPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupPoliciesPager)
    
    
    ListBackupPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse
        ],
        request: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesRequest,
        response: google.cloud.netapp_v1.types.backup_policy.ListBackupPoliciesResponse,
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

A pager for iterating through `list_backup_policies` requests.

This class thinly wraps an initial [ListBackupPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesResponse) object, and provides an `__iter__` method to iterate through its `backup_policies` field.

If there are more pages, the `__iter__` method will make additional `ListBackupPolicies` requests and continue to iterate through the `backup_policies` field on the corresponding responses.

All the usual [ListBackupPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsAsyncPager)
    
    
    ListBackupVaultsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest,
        response: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse,
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

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsResponse) object, and provides an `__aiter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupVaultsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupVaultsPager)
    
    
    ListBackupVaultsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse
        ],
        request: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsRequest,
        response: google.cloud.netapp_v1.types.backup_vault.ListBackupVaultsResponse,
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

This class thinly wraps an initial [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsResponse) object, and provides an `__iter__` method to iterate through its `backup_vaults` field.

If there are more pages, the `__iter__` method will make additional `ListBackupVaults` requests and continue to iterate through the `backup_vaults` field on the corresponding responses.

All the usual [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupVaultsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupsAsyncPager)
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.netapp_v1.types.backup.ListBackupsResponse]
        ],
        request: google.cloud.netapp_v1.types.backup.ListBackupsRequest,
        response: google.cloud.netapp_v1.types.backup.ListBackupsResponse,
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

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListBackupsPager)
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.backup.ListBackupsResponse
        ],
        request: google.cloud.netapp_v1.types.backup.ListBackupsRequest,
        response: google.cloud.netapp_v1.types.backup.ListBackupsResponse,
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

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListHostGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsAsyncPager)
    
    
    ListHostGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest,
        response: google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse,
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

A pager for iterating through `list_host_groups` requests.

This class thinly wraps an initial [ListHostGroupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsResponse) object, and provides an `__aiter__` method to iterate through its `host_groups` field.

If there are more pages, the `__aiter__` method will make additional `ListHostGroups` requests and continue to iterate through the `host_groups` field on the corresponding responses.

All the usual [ListHostGroupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListHostGroupsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListHostGroupsPager)
    
    
    ListHostGroupsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse
        ],
        request: google.cloud.netapp_v1.types.host_group.ListHostGroupsRequest,
        response: google.cloud.netapp_v1.types.host_group.ListHostGroupsResponse,
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

A pager for iterating through `list_host_groups` requests.

This class thinly wraps an initial [ListHostGroupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsResponse) object, and provides an `__iter__` method to iterate through its `host_groups` field.

If there are more pages, the `__iter__` method will make additional `ListHostGroups` requests and continue to iterate through the `host_groups` field on the corresponding responses.

All the usual [ListHostGroupsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListHostGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListKmsConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsAsyncPager)
    
    
    ListKmsConfigsAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse]
        ],
        request: google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest,
        response: google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse,
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

A pager for iterating through `list_kms_configs` requests.

This class thinly wraps an initial [ListKmsConfigsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsResponse) object, and provides an `__aiter__` method to iterate through its `kms_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListKmsConfigs` requests and continue to iterate through the `kms_configs` field on the corresponding responses.

All the usual [ListKmsConfigsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListKmsConfigsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListKmsConfigsPager)
    
    
    ListKmsConfigsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse
        ],
        request: google.cloud.netapp_v1.types.kms.ListKmsConfigsRequest,
        response: google.cloud.netapp_v1.types.kms.ListKmsConfigsResponse,
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

A pager for iterating through `list_kms_configs` requests.

This class thinly wraps an initial [ListKmsConfigsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsResponse) object, and provides an `__iter__` method to iterate through its `kms_configs` field.

If there are more pages, the `__iter__` method will make additional `ListKmsConfigs` requests and continue to iterate through the `kms_configs` field on the corresponding responses.

All the usual [ListKmsConfigsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListKmsConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListQuotaRulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesAsyncPager)
    
    
    ListQuotaRulesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest,
        response: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse,
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

A pager for iterating through `list_quota_rules` requests.

This class thinly wraps an initial [ListQuotaRulesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesResponse) object, and provides an `__aiter__` method to iterate through its `quota_rules` field.

If there are more pages, the `__aiter__` method will make additional `ListQuotaRules` requests and continue to iterate through the `quota_rules` field on the corresponding responses.

All the usual [ListQuotaRulesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListQuotaRulesPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListQuotaRulesPager)
    
    
    ListQuotaRulesPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse
        ],
        request: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesRequest,
        response: google.cloud.netapp_v1.types.quota_rule.ListQuotaRulesResponse,
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

A pager for iterating through `list_quota_rules` requests.

This class thinly wraps an initial [ListQuotaRulesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesResponse) object, and provides an `__iter__` method to iterate through its `quota_rules` field.

If there are more pages, the `__iter__` method will make additional `ListQuotaRules` requests and continue to iterate through the `quota_rules` field on the corresponding responses.

All the usual [ListQuotaRulesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListQuotaRulesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListReplicationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsAsyncPager)
    
    
    ListReplicationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.replication.ListReplicationsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.replication.ListReplicationsRequest,
        response: google.cloud.netapp_v1.types.replication.ListReplicationsResponse,
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

A pager for iterating through `list_replications` requests.

This class thinly wraps an initial [ListReplicationsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsResponse) object, and provides an `__aiter__` method to iterate through its `replications` field.

If there are more pages, the `__aiter__` method will make additional `ListReplications` requests and continue to iterate through the `replications` field on the corresponding responses.

All the usual [ListReplicationsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListReplicationsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListReplicationsPager)
    
    
    ListReplicationsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.replication.ListReplicationsResponse
        ],
        request: google.cloud.netapp_v1.types.replication.ListReplicationsRequest,
        response: google.cloud.netapp_v1.types.replication.ListReplicationsResponse,
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

A pager for iterating through `list_replications` requests.

This class thinly wraps an initial [ListReplicationsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsResponse) object, and provides an `__iter__` method to iterate through its `replications` field.

If there are more pages, the `__iter__` method will make additional `ListReplications` requests and continue to iterate through the `replications` field on the corresponding responses.

All the usual [ListReplicationsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListReplicationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSnapshotsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsAsyncPager)
    
    
    ListSnapshotsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse],
        ],
        request: google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest,
        response: google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse,
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

A pager for iterating through `list_snapshots` requests.

This class thinly wraps an initial [ListSnapshotsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsResponse) object, and provides an `__aiter__` method to iterate through its `snapshots` field.

If there are more pages, the `__aiter__` method will make additional `ListSnapshots` requests and continue to iterate through the `snapshots` field on the corresponding responses.

All the usual [ListSnapshotsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSnapshotsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListSnapshotsPager)
    
    
    ListSnapshotsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse
        ],
        request: google.cloud.netapp_v1.types.snapshot.ListSnapshotsRequest,
        response: google.cloud.netapp_v1.types.snapshot.ListSnapshotsResponse,
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

A pager for iterating through `list_snapshots` requests.

This class thinly wraps an initial [ListSnapshotsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsResponse) object, and provides an `__iter__` method to iterate through its `snapshots` field.

If there are more pages, the `__iter__` method will make additional `ListSnapshots` requests and continue to iterate through the `snapshots` field on the corresponding responses.

All the usual [ListSnapshotsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListSnapshotsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListStoragePoolsAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsAsyncPager)
    
    
    ListStoragePoolsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse
            ],
        ],
        request: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest,
        response: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse,
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

A pager for iterating through `list_storage_pools` requests.

This class thinly wraps an initial [ListStoragePoolsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsResponse) object, and provides an `__aiter__` method to iterate through its `storage_pools` field.

If there are more pages, the `__aiter__` method will make additional `ListStoragePools` requests and continue to iterate through the `storage_pools` field on the corresponding responses.

All the usual [ListStoragePoolsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListStoragePoolsPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListStoragePoolsPager)
    
    
    ListStoragePoolsPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse
        ],
        request: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsRequest,
        response: google.cloud.netapp_v1.types.storage_pool.ListStoragePoolsResponse,
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

A pager for iterating through `list_storage_pools` requests.

This class thinly wraps an initial [ListStoragePoolsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsResponse) object, and provides an `__iter__` method to iterate through its `storage_pools` field.

If there are more pages, the `__iter__` method will make additional `ListStoragePools` requests and continue to iterate through the `storage_pools` field on the corresponding responses.

All the usual [ListStoragePoolsResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListStoragePoolsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListVolumesAsyncPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListVolumesAsyncPager)
    
    
    ListVolumesAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.netapp_v1.types.volume.ListVolumesResponse]
        ],
        request: google.cloud.netapp_v1.types.volume.ListVolumesRequest,
        response: google.cloud.netapp_v1.types.volume.ListVolumesResponse,
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

A pager for iterating through `list_volumes` requests.

This class thinly wraps an initial [ListVolumesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesResponse) object, and provides an `__aiter__` method to iterate through its `volumes` field.

If there are more pages, the `__aiter__` method will make additional `ListVolumes` requests and continue to iterate through the `volumes` field on the corresponding responses.

All the usual [ListVolumesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListVolumesPager](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.services.net_app.pagers.ListVolumesPager)
    
    
    ListVolumesPager(
        method: typing.Callable[
            [...], google.cloud.netapp_v1.types.volume.ListVolumesResponse
        ],
        request: google.cloud.netapp_v1.types.volume.ListVolumesRequest,
        response: google.cloud.netapp_v1.types.volume.ListVolumesResponse,
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

A pager for iterating through `list_volumes` requests.

This class thinly wraps an initial [ListVolumesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesResponse) object, and provides an `__iter__` method to iterate through its `volumes` field.

If there are more pages, the `__iter__` method will make additional `ListVolumes` requests and continue to iterate through the `volumes` field on the corresponding responses.

All the usual [ListVolumesResponse](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.ListVolumesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
