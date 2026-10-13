---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers
title: Module pagers (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:08.386559+00:00
---

# Module pagers (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 

API documentation for `agentidentity_v1.services.auth_provider_service.pagers` module.

## Classes 

### [ListAccessSummariesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.ListAccessSummariesAsyncPager)
    
    
    ListAccessSummariesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.agentidentity_v1.types.auth_provider_service.ListAccessSummariesResponse
            ],
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.ListAccessSummariesRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.ListAccessSummariesResponse,
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

A pager for iterating through `list_access_summaries` requests.

This class thinly wraps an initial [ListAccessSummariesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAccessSummariesResponse) object, and provides an `__aiter__` method to iterate through its `access_summaries` field.

If there are more pages, the `__aiter__` method will make additional `ListAccessSummaries` requests and continue to iterate through the `access_summaries` field on the corresponding responses.

All the usual [ListAccessSummariesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAccessSummariesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccessSummariesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.ListAccessSummariesPager)
    
    
    ListAccessSummariesPager(
        method: typing.Callable[
            [...],
            google.cloud.agentidentity_v1.types.auth_provider_service.ListAccessSummariesResponse,
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.ListAccessSummariesRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.ListAccessSummariesResponse,
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

A pager for iterating through `list_access_summaries` requests.

This class thinly wraps an initial [ListAccessSummariesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAccessSummariesResponse) object, and provides an `__iter__` method to iterate through its `access_summaries` field.

If there are more pages, the `__iter__` method will make additional `ListAccessSummaries` requests and continue to iterate through the `access_summaries` field on the corresponding responses.

All the usual [ListAccessSummariesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAccessSummariesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAuthProvidersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.ListAuthProvidersAsyncPager)
    
    
    ListAuthProvidersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthProvidersResponse
            ],
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthProvidersRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthProvidersResponse,
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

A pager for iterating through `list_auth_providers` requests.

This class thinly wraps an initial [ListAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthProvidersResponse) object, and provides an `__aiter__` method to iterate through its `auth_providers` field.

If there are more pages, the `__aiter__` method will make additional `ListAuthProviders` requests and continue to iterate through the `auth_providers` field on the corresponding responses.

All the usual [ListAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthProvidersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAuthProvidersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.ListAuthProvidersPager)
    
    
    ListAuthProvidersPager(
        method: typing.Callable[
            [...],
            google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthProvidersResponse,
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthProvidersRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthProvidersResponse,
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

A pager for iterating through `list_auth_providers` requests.

This class thinly wraps an initial [ListAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthProvidersResponse) object, and provides an `__iter__` method to iterate through its `auth_providers` field.

If there are more pages, the `__iter__` method will make additional `ListAuthProviders` requests and continue to iterate through the `auth_providers` field on the corresponding responses.

All the usual [ListAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthProvidersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAuthorizationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.ListAuthorizationsAsyncPager)
    
    
    ListAuthorizationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthorizationsResponse
            ],
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthorizationsRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthorizationsResponse,
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

A pager for iterating through `list_authorizations` requests.

This class thinly wraps an initial [ListAuthorizationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthorizationsResponse) object, and provides an `__aiter__` method to iterate through its `authorizations` field.

If there are more pages, the `__aiter__` method will make additional `ListAuthorizations` requests and continue to iterate through the `authorizations` field on the corresponding responses.

All the usual [ListAuthorizationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthorizationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAuthorizationsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.ListAuthorizationsPager)
    
    
    ListAuthorizationsPager(
        method: typing.Callable[
            [...],
            google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthorizationsResponse,
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthorizationsRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.ListAuthorizationsResponse,
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

A pager for iterating through `list_authorizations` requests.

This class thinly wraps an initial [ListAuthorizationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthorizationsResponse) object, and provides an `__iter__` method to iterate through its `authorizations` field.

If there are more pages, the `__iter__` method will make additional `ListAuthorizations` requests and continue to iterate through the `authorizations` field on the corresponding responses.

All the usual [ListAuthorizationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.ListAuthorizationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryAuthProvidersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.QueryAuthProvidersAsyncPager)
    
    
    QueryAuthProvidersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.agentidentity_v1.types.auth_provider_service.QueryAuthProvidersResponse
            ],
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.QueryAuthProvidersRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.QueryAuthProvidersResponse,
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

A pager for iterating through `query_auth_providers` requests.

This class thinly wraps an initial [QueryAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse) object, and provides an `__aiter__` method to iterate through its `auth_provider_names` field.

If there are more pages, the `__aiter__` method will make additional `QueryAuthProviders` requests and continue to iterate through the `auth_provider_names` field on the corresponding responses.

All the usual [QueryAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryAuthProvidersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.QueryAuthProvidersPager)
    
    
    QueryAuthProvidersPager(
        method: typing.Callable[
            [...],
            google.cloud.agentidentity_v1.types.auth_provider_service.QueryAuthProvidersResponse,
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.QueryAuthProvidersRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.QueryAuthProvidersResponse,
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

A pager for iterating through `query_auth_providers` requests.

This class thinly wraps an initial [QueryAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse) object, and provides an `__iter__` method to iterate through its `auth_provider_names` field.

If there are more pages, the `__iter__` method will make additional `QueryAuthProviders` requests and continue to iterate through the `auth_provider_names` field on the corresponding responses.

All the usual [QueryAuthProvidersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryAuthProvidersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryWorkloadsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.QueryWorkloadsAsyncPager)
    
    
    QueryWorkloadsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.agentidentity_v1.types.auth_provider_service.QueryWorkloadsResponse
            ],
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.QueryWorkloadsRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.QueryWorkloadsResponse,
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

A pager for iterating through `query_workloads` requests.

This class thinly wraps an initial [QueryWorkloadsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryWorkloadsResponse) object, and provides an `__aiter__` method to iterate through its `workload_ids` field.

If there are more pages, the `__aiter__` method will make additional `QueryWorkloads` requests and continue to iterate through the `workload_ids` field on the corresponding responses.

All the usual [QueryWorkloadsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryWorkloadsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryWorkloadsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.services.auth_provider_service.pagers.QueryWorkloadsPager)
    
    
    QueryWorkloadsPager(
        method: typing.Callable[
            [...],
            google.cloud.agentidentity_v1.types.auth_provider_service.QueryWorkloadsResponse,
        ],
        request: google.cloud.agentidentity_v1.types.auth_provider_service.QueryWorkloadsRequest,
        response: google.cloud.agentidentity_v1.types.auth_provider_service.QueryWorkloadsResponse,
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

A pager for iterating through `query_workloads` requests.

This class thinly wraps an initial [QueryWorkloadsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryWorkloadsResponse) object, and provides an `__iter__` method to iterate through its `workload_ids` field.

If there are more pages, the `__iter__` method will make additional `QueryWorkloads` requests and continue to iterate through the `workload_ids` field on the corresponding responses.

All the usual [QueryWorkloadsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-agentidentity/latest/google.cloud.agentidentity_v1.types.QueryWorkloadsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
