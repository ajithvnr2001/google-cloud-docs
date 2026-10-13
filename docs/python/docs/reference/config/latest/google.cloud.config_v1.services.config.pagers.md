---
url: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers
title: Module pagers (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:12:33.422368+00:00
---

# Module pagers (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.21 

API documentation for `config_v1.services.config.pagers` module.

## Classes 

### [ListDeploymentGroupRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsAsyncPager)
    
    
    ListDeploymentGroupRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse,
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

A pager for iterating through `list_deployment_group_revisions` requests.

This class thinly wraps an initial [ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `deployment_group_revisions` field.

If there are more pages, the `__aiter__` method will make additional `ListDeploymentGroupRevisions` requests and continue to iterate through the `deployment_group_revisions` field on the corresponding responses.

All the usual [ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentGroupRevisionsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupRevisionsPager)
    
    
    ListDeploymentGroupRevisionsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupRevisionsResponse,
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

A pager for iterating through `list_deployment_group_revisions` requests.

This class thinly wraps an initial [ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsResponse) object, and provides an `__iter__` method to iterate through its `deployment_group_revisions` field.

If there are more pages, the `__iter__` method will make additional `ListDeploymentGroupRevisions` requests and continue to iterate through the `deployment_group_revisions` field on the corresponding responses.

All the usual [ListDeploymentGroupRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentGroupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsAsyncPager)
    
    
    ListDeploymentGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListDeploymentGroupsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupsResponse,
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

A pager for iterating through `list_deployment_groups` requests.

This class thinly wraps an initial [ListDeploymentGroupsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsResponse) object, and provides an `__aiter__` method to iterate through its `deployment_groups` field.

If there are more pages, the `__aiter__` method will make additional `ListDeploymentGroups` requests and continue to iterate through the `deployment_groups` field on the corresponding responses.

All the usual [ListDeploymentGroupsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentGroupsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentGroupsPager)
    
    
    ListDeploymentGroupsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListDeploymentGroupsResponse
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentGroupsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentGroupsResponse,
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

A pager for iterating through `list_deployment_groups` requests.

This class thinly wraps an initial [ListDeploymentGroupsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsResponse) object, and provides an `__iter__` method to iterate through its `deployment_groups` field.

If there are more pages, the `__iter__` method will make additional `ListDeploymentGroups` requests and continue to iterate through the `deployment_groups` field on the corresponding responses.

All the usual [ListDeploymentGroupsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentsAsyncPager)
    
    
    ListDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListDeploymentsResponse],
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentsResponse,
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

A pager for iterating through `list_deployments` requests.

This class thinly wraps an initial [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsResponse) object, and provides an `__aiter__` method to iterate through its `deployments` field.

If there are more pages, the `__aiter__` method will make additional `ListDeployments` requests and continue to iterate through the `deployments` field on the corresponding responses.

All the usual [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListDeploymentsPager)
    
    
    ListDeploymentsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListDeploymentsResponse
        ],
        request: google.cloud.config_v1.types.config.ListDeploymentsRequest,
        response: google.cloud.config_v1.types.config.ListDeploymentsResponse,
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

A pager for iterating through `list_deployments` requests.

This class thinly wraps an initial [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsResponse) object, and provides an `__iter__` method to iterate through its `deployments` field.

If there are more pages, the `__iter__` method will make additional `ListDeployments` requests and continue to iterate through the `deployments` field on the corresponding responses.

All the usual [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListDeploymentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPreviewsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListPreviewsAsyncPager)
    
    
    ListPreviewsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListPreviewsResponse],
        ],
        request: google.cloud.config_v1.types.config.ListPreviewsRequest,
        response: google.cloud.config_v1.types.config.ListPreviewsResponse,
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

A pager for iterating through `list_previews` requests.

This class thinly wraps an initial [ListPreviewsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsResponse) object, and provides an `__aiter__` method to iterate through its `previews` field.

If there are more pages, the `__aiter__` method will make additional `ListPreviews` requests and continue to iterate through the `previews` field on the corresponding responses.

All the usual [ListPreviewsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPreviewsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListPreviewsPager)
    
    
    ListPreviewsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListPreviewsResponse
        ],
        request: google.cloud.config_v1.types.config.ListPreviewsRequest,
        response: google.cloud.config_v1.types.config.ListPreviewsResponse,
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

A pager for iterating through `list_previews` requests.

This class thinly wraps an initial [ListPreviewsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsResponse) object, and provides an `__iter__` method to iterate through its `previews` field.

If there are more pages, the `__iter__` method will make additional `ListPreviews` requests and continue to iterate through the `previews` field on the corresponding responses.

All the usual [ListPreviewsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListPreviewsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceChangesAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceChangesAsyncPager)
    
    
    ListResourceChangesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListResourceChangesResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListResourceChangesRequest,
        response: google.cloud.config_v1.types.config.ListResourceChangesResponse,
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

A pager for iterating through `list_resource_changes` requests.

This class thinly wraps an initial [ListResourceChangesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesResponse) object, and provides an `__aiter__` method to iterate through its `resource_changes` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceChanges` requests and continue to iterate through the `resource_changes` field on the corresponding responses.

All the usual [ListResourceChangesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceChangesPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceChangesPager)
    
    
    ListResourceChangesPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListResourceChangesResponse
        ],
        request: google.cloud.config_v1.types.config.ListResourceChangesRequest,
        response: google.cloud.config_v1.types.config.ListResourceChangesResponse,
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

A pager for iterating through `list_resource_changes` requests.

This class thinly wraps an initial [ListResourceChangesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesResponse) object, and provides an `__iter__` method to iterate through its `resource_changes` field.

If there are more pages, the `__iter__` method will make additional `ListResourceChanges` requests and continue to iterate through the `resource_changes` field on the corresponding responses.

All the usual [ListResourceChangesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceChangesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceDriftsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceDriftsAsyncPager)
    
    
    ListResourceDriftsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListResourceDriftsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListResourceDriftsRequest,
        response: google.cloud.config_v1.types.config.ListResourceDriftsResponse,
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

A pager for iterating through `list_resource_drifts` requests.

This class thinly wraps an initial [ListResourceDriftsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsResponse) object, and provides an `__aiter__` method to iterate through its `resource_drifts` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceDrifts` requests and continue to iterate through the `resource_drifts` field on the corresponding responses.

All the usual [ListResourceDriftsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceDriftsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourceDriftsPager)
    
    
    ListResourceDriftsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListResourceDriftsResponse
        ],
        request: google.cloud.config_v1.types.config.ListResourceDriftsRequest,
        response: google.cloud.config_v1.types.config.ListResourceDriftsResponse,
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

A pager for iterating through `list_resource_drifts` requests.

This class thinly wraps an initial [ListResourceDriftsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsResponse) object, and provides an `__iter__` method to iterate through its `resource_drifts` field.

If there are more pages, the `__iter__` method will make additional `ListResourceDrifts` requests and continue to iterate through the `resource_drifts` field on the corresponding responses.

All the usual [ListResourceDriftsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourceDriftsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourcesAsyncPager)
    
    
    ListResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListResourcesResponse],
        ],
        request: google.cloud.config_v1.types.config.ListResourcesRequest,
        response: google.cloud.config_v1.types.config.ListResourcesResponse,
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

A pager for iterating through `list_resources` requests.

This class thinly wraps an initial [ListResourcesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesResponse) object, and provides an `__aiter__` method to iterate through its `resources` field.

If there are more pages, the `__aiter__` method will make additional `ListResources` requests and continue to iterate through the `resources` field on the corresponding responses.

All the usual [ListResourcesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourcesPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListResourcesPager)
    
    
    ListResourcesPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListResourcesResponse
        ],
        request: google.cloud.config_v1.types.config.ListResourcesRequest,
        response: google.cloud.config_v1.types.config.ListResourcesResponse,
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

A pager for iterating through `list_resources` requests.

This class thinly wraps an initial [ListResourcesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesResponse) object, and provides an `__iter__` method to iterate through its `resources` field.

If there are more pages, the `__iter__` method will make additional `ListResources` requests and continue to iterate through the `resources` field on the corresponding responses.

All the usual [ListResourcesResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListRevisionsAsyncPager)
    
    
    ListRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.config_v1.types.config.ListRevisionsResponse],
        ],
        request: google.cloud.config_v1.types.config.ListRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListRevisionsResponse,
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

A pager for iterating through `list_revisions` requests.

This class thinly wraps an initial [ListRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `revisions` field.

If there are more pages, the `__aiter__` method will make additional `ListRevisions` requests and continue to iterate through the `revisions` field on the corresponding responses.

All the usual [ListRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRevisionsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListRevisionsPager)
    
    
    ListRevisionsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListRevisionsResponse
        ],
        request: google.cloud.config_v1.types.config.ListRevisionsRequest,
        response: google.cloud.config_v1.types.config.ListRevisionsResponse,
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

A pager for iterating through `list_revisions` requests.

This class thinly wraps an initial [ListRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsResponse) object, and provides an `__iter__` method to iterate through its `revisions` field.

If there are more pages, the `__iter__` method will make additional `ListRevisions` requests and continue to iterate through the `revisions` field on the corresponding responses.

All the usual [ListRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTerraformVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListTerraformVersionsAsyncPager)
    
    
    ListTerraformVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.config_v1.types.config.ListTerraformVersionsResponse
            ],
        ],
        request: google.cloud.config_v1.types.config.ListTerraformVersionsRequest,
        response: google.cloud.config_v1.types.config.ListTerraformVersionsResponse,
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

A pager for iterating through `list_terraform_versions` requests.

This class thinly wraps an initial [ListTerraformVersionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsResponse) object, and provides an `__aiter__` method to iterate through its `terraform_versions` field.

If there are more pages, the `__aiter__` method will make additional `ListTerraformVersions` requests and continue to iterate through the `terraform_versions` field on the corresponding responses.

All the usual [ListTerraformVersionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTerraformVersionsPager](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.services.config.pagers.ListTerraformVersionsPager)
    
    
    ListTerraformVersionsPager(
        method: typing.Callable[
            [...], google.cloud.config_v1.types.config.ListTerraformVersionsResponse
        ],
        request: google.cloud.config_v1.types.config.ListTerraformVersionsRequest,
        response: google.cloud.config_v1.types.config.ListTerraformVersionsResponse,
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

A pager for iterating through `list_terraform_versions` requests.

This class thinly wraps an initial [ListTerraformVersionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsResponse) object, and provides an `__iter__` method to iterate through its `terraform_versions` field.

If there are more pages, the `__iter__` method will make additional `ListTerraformVersions` requests and continue to iterate through the `terraform_versions` field on the corresponding responses.

All the usual [ListTerraformVersionsResponse](https://docs.cloud.google.com/python/docs/reference/config/latest/google.cloud.config_v1.types.ListTerraformVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
