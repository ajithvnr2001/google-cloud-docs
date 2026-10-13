---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers
title: Module pagers (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:15.577661+00:00
---

# Module pagers (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 

API documentation for `asset_v1.services.asset_service.pagers` module.

## Classes 

### [AnalyzeOrgPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager)
    
    
    AnalyzeOrgPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse,
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

A pager for iterating through `analyze_org_policies` requests.

This class thinly wraps an initial [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `org_policy_results` field.

If there are more pages, the `__aiter__` method will make additional `AnalyzeOrgPolicies` requests and continue to iterate through the `org_policy_results` field on the corresponding responses.

All the usual [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPoliciesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesPager)
    
    
    AnalyzeOrgPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPoliciesResponse,
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

A pager for iterating through `analyze_org_policies` requests.

This class thinly wraps an initial [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) object, and provides an `__iter__` method to iterate through its `org_policy_results` field.

If there are more pages, the `__iter__` method will make additional `AnalyzeOrgPolicies` requests and continue to iterate through the `org_policy_results` field on the corresponding responses.

All the usual [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager)
    
    
    AnalyzeOrgPolicyGovernedAssetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
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

A pager for iterating through `analyze_org_policy_governed_assets` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) object, and provides an `__aiter__` method to iterate through its `governed_assets` field.

If there are more pages, the `__aiter__` method will make additional `AnalyzeOrgPolicyGovernedAssets` requests and continue to iterate through the `governed_assets` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedAssetsPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsPager)
    
    
    AnalyzeOrgPolicyGovernedAssetsPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedAssetsResponse,
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

A pager for iterating through `analyze_org_policy_governed_assets` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) object, and provides an `__iter__` method to iterate through its `governed_assets` field.

If there are more pages, the `__iter__` method will make additional `AnalyzeOrgPolicyGovernedAssets` requests and continue to iterate through the `governed_assets` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedContainersAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager)
    
    
    AnalyzeOrgPolicyGovernedContainersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
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

A pager for iterating through `analyze_org_policy_governed_containers` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) object, and provides an `__aiter__` method to iterate through its `governed_containers` field.

If there are more pages, the `__aiter__` method will make additional `AnalyzeOrgPolicyGovernedContainers` requests and continue to iterate through the `governed_containers` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedContainersPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersPager)
    
    
    AnalyzeOrgPolicyGovernedContainersPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
        ],
        request: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersRequest,
        response: google.cloud.asset_v1.types.asset_service.AnalyzeOrgPolicyGovernedContainersResponse,
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

A pager for iterating through `analyze_org_policy_governed_containers` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) object, and provides an `__iter__` method to iterate through its `governed_containers` field.

If there are more pages, the `__iter__` method will make additional `AnalyzeOrgPolicyGovernedContainers` requests and continue to iterate through the `governed_containers` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager)
    
    
    ListAssetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.asset_v1.types.asset_service.ListAssetsResponse],
        ],
        request: google.cloud.asset_v1.types.asset_service.ListAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.ListAssetsResponse,
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

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) object, and provides an `__aiter__` method to iterate through its `assets` field.

If there are more pages, the `__aiter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsPager)
    
    
    ListAssetsPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.ListAssetsResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.ListAssetsRequest,
        response: google.cloud.asset_v1.types.asset_service.ListAssetsResponse,
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

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) object, and provides an `__iter__` method to iterate through its `assets` field.

If there are more pages, the `__iter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSavedQueriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager)
    
    
    ListSavedQueriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.ListSavedQueriesRequest,
        response: google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse,
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

A pager for iterating through `list_saved_queries` requests.

This class thinly wraps an initial [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) object, and provides an `__aiter__` method to iterate through its `saved_queries` field.

If there are more pages, the `__aiter__` method will make additional `ListSavedQueries` requests and continue to iterate through the `saved_queries` field on the corresponding responses.

All the usual [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSavedQueriesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesPager)
    
    
    ListSavedQueriesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.ListSavedQueriesRequest,
        response: google.cloud.asset_v1.types.asset_service.ListSavedQueriesResponse,
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

A pager for iterating through `list_saved_queries` requests.

This class thinly wraps an initial [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) object, and provides an `__iter__` method to iterate through its `saved_queries` field.

If there are more pages, the `__iter__` method will make additional `ListSavedQueries` requests and continue to iterate through the `saved_queries` field on the corresponding responses.

All the usual [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllIamPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager)
    
    
    SearchAllIamPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse,
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

A pager for iterating through `search_all_iam_policies` requests.

This class thinly wraps an initial [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchAllIamPolicies` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllIamPoliciesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesPager)
    
    
    SearchAllIamPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllIamPoliciesResponse,
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

A pager for iterating through `search_all_iam_policies` requests.

This class thinly wraps an initial [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllIamPolicies` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager)
    
    
    SearchAllResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse
            ],
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse,
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

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllResourcesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesPager)
    
    
    SearchAllResourcesPager(
        method: typing.Callable[
            [...], google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse
        ],
        request: google.cloud.asset_v1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1.types.asset_service.SearchAllResourcesResponse,
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

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
