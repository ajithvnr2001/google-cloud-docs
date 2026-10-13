---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers
title: Module pagers (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:57.339551+00:00
---

# Module pagers (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.14 

API documentation for `redis_cluster_v1beta1.services.cloud_redis_cluster.pagers` module.

## Classes 

### [ListBackupCollectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsAsyncPager)
    
    
    ListBackupCollectionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsResponse
            ],
        ],
        request: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsRequest,
        response: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsResponse,
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

A pager for iterating through `list_backup_collections` requests.

This class thinly wraps an initial [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) object, and provides an `__aiter__` method to iterate through its `backup_collections` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupCollections` requests and continue to iterate through the `backup_collections` field on the corresponding responses.

All the usual [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupCollectionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupCollectionsPager)
    
    
    ListBackupCollectionsPager(
        method: typing.Callable[
            [...],
            google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsResponse,
        ],
        request: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsRequest,
        response: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupCollectionsResponse,
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

A pager for iterating through `list_backup_collections` requests.

This class thinly wraps an initial [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) object, and provides an `__iter__` method to iterate through its `backup_collections` field.

If there are more pages, the `__iter__` method will make additional `ListBackupCollections` requests and continue to iterate through the `backup_collections` field on the corresponding responses.

All the usual [ListBackupCollectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupCollectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsAsyncPager)
    
    
    ListBackupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsResponse
            ],
        ],
        request: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsRequest,
        response: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsResponse,
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

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListBackupsPager)
    
    
    ListBackupsPager(
        method: typing.Callable[
            [...],
            google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsResponse,
        ],
        request: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsRequest,
        response: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListBackupsResponse,
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

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersAsyncPager)
    
    
    ListClustersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersResponse
            ],
        ],
        request: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersRequest,
        response: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersResponse,
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

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) object, and provides an `__aiter__` method to iterate through its `clusters` field.

If there are more pages, the `__aiter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListClustersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.services.cloud_redis_cluster.pagers.ListClustersPager)
    
    
    ListClustersPager(
        method: typing.Callable[
            [...],
            google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersResponse,
        ],
        request: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersRequest,
        response: google.cloud.redis_cluster_v1beta1.types.cloud_redis_cluster.ListClustersResponse,
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

This class thinly wraps an initial [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) object, and provides an `__iter__` method to iterate through its `clusters` field.

If there are more pages, the `__iter__` method will make additional `ListClusters` requests and continue to iterate through the `clusters` field on the corresponding responses.

All the usual [ListClustersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-redis-cluster/latest/google.cloud.redis_cluster_v1beta1.types.ListClustersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
