---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers
title: Module pagers (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:23.719391+00:00
---

# Module pagers (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 

API documentation for `developerconnect_v1.services.developer_connect.pagers` module.

## Classes 

### [FetchGitRefsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsAsyncPager)
    
    
    FetchGitRefsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse,
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

A pager for iterating through `fetch_git_refs` requests.

This class thinly wraps an initial [FetchGitRefsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsResponse) object, and provides an `__aiter__` method to iterate through its `ref_names` field.

If there are more pages, the `__aiter__` method will make additional `FetchGitRefs` requests and continue to iterate through the `ref_names` field on the corresponding responses.

All the usual [FetchGitRefsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchGitRefsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchGitRefsPager)
    
    
    FetchGitRefsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchGitRefsResponse,
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

A pager for iterating through `fetch_git_refs` requests.

This class thinly wraps an initial [FetchGitRefsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsResponse) object, and provides an `__iter__` method to iterate through its `ref_names` field.

If there are more pages, the `__iter__` method will make additional `FetchGitRefs` requests and continue to iterate through the `ref_names` field on the corresponding responses.

All the usual [FetchGitRefsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchGitRefsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchLinkableGitRepositoriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesAsyncPager)
    
    
    FetchLinkableGitRepositoriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse,
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

A pager for iterating through `fetch_linkable_git_repositories` requests.

This class thinly wraps an initial [FetchLinkableGitRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse) object, and provides an `__aiter__` method to iterate through its `linkable_git_repositories` field.

If there are more pages, the `__aiter__` method will make additional `FetchLinkableGitRepositories` requests and continue to iterate through the `linkable_git_repositories` field on the corresponding responses.

All the usual [FetchLinkableGitRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [FetchLinkableGitRepositoriesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.FetchLinkableGitRepositoriesPager)
    
    
    FetchLinkableGitRepositoriesPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.FetchLinkableGitRepositoriesResponse,
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

A pager for iterating through `fetch_linkable_git_repositories` requests.

This class thinly wraps an initial [FetchLinkableGitRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse) object, and provides an `__iter__` method to iterate through its `linkable_git_repositories` field.

If there are more pages, the `__iter__` method will make additional `FetchLinkableGitRepositories` requests and continue to iterate through the `linkable_git_repositories` field on the corresponding responses.

All the usual [FetchLinkableGitRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.FetchLinkableGitRepositoriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccountConnectorsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsAsyncPager)
    
    
    ListAccountConnectorsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse,
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

A pager for iterating through `list_account_connectors` requests.

This class thinly wraps an initial [ListAccountConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse) object, and provides an `__aiter__` method to iterate through its `account_connectors` field.

If there are more pages, the `__aiter__` method will make additional `ListAccountConnectors` requests and continue to iterate through the `account_connectors` field on the corresponding responses.

All the usual [ListAccountConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccountConnectorsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListAccountConnectorsPager)
    
    
    ListAccountConnectorsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListAccountConnectorsResponse,
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

A pager for iterating through `list_account_connectors` requests.

This class thinly wraps an initial [ListAccountConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse) object, and provides an `__iter__` method to iterate through its `account_connectors` field.

If there are more pages, the `__iter__` method will make additional `ListAccountConnectors` requests and continue to iterate through the `account_connectors` field on the corresponding responses.

All the usual [ListAccountConnectorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListAccountConnectorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsAsyncPager)
    
    
    ListConnectionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse,
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

A pager for iterating through `list_connections` requests.

This class thinly wraps an initial [ListConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsResponse) object, and provides an `__aiter__` method to iterate through its `connections` field.

If there are more pages, the `__aiter__` method will make additional `ListConnections` requests and continue to iterate through the `connections` field on the corresponding responses.

All the usual [ListConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListConnectionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListConnectionsPager)
    
    
    ListConnectionsPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListConnectionsResponse,
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

A pager for iterating through `list_connections` requests.

This class thinly wraps an initial [ListConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsResponse) object, and provides an `__iter__` method to iterate through its `connections` field.

If there are more pages, the `__iter__` method will make additional `ListConnections` requests and continue to iterate through the `connections` field on the corresponding responses.

All the usual [ListConnectionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListConnectionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListGitRepositoryLinksAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksAsyncPager)
    
    
    ListGitRepositoryLinksAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse,
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

A pager for iterating through `list_git_repository_links` requests.

This class thinly wraps an initial [ListGitRepositoryLinksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse) object, and provides an `__aiter__` method to iterate through its `git_repository_links` field.

If there are more pages, the `__aiter__` method will make additional `ListGitRepositoryLinks` requests and continue to iterate through the `git_repository_links` field on the corresponding responses.

All the usual [ListGitRepositoryLinksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListGitRepositoryLinksPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListGitRepositoryLinksPager)
    
    
    ListGitRepositoryLinksPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListGitRepositoryLinksResponse,
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

A pager for iterating through `list_git_repository_links` requests.

This class thinly wraps an initial [ListGitRepositoryLinksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse) object, and provides an `__iter__` method to iterate through its `git_repository_links` field.

If there are more pages, the `__iter__` method will make additional `ListGitRepositoryLinks` requests and continue to iterate through the `git_repository_links` field on the corresponding responses.

All the usual [ListGitRepositoryLinksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListGitRepositoryLinksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListUsersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersAsyncPager)
    
    
    ListUsersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse
            ],
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListUsersRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse,
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

A pager for iterating through `list_users` requests.

This class thinly wraps an initial [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersResponse) object, and provides an `__aiter__` method to iterate through its `users` field.

If there are more pages, the `__aiter__` method will make additional `ListUsers` requests and continue to iterate through the `users` field on the corresponding responses.

All the usual [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListUsersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.developer_connect.pagers.ListUsersPager)
    
    
    ListUsersPager(
        method: typing.Callable[
            [...],
            google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse,
        ],
        request: google.cloud.developerconnect_v1.types.developer_connect.ListUsersRequest,
        response: google.cloud.developerconnect_v1.types.developer_connect.ListUsersResponse,
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

A pager for iterating through `list_users` requests.

This class thinly wraps an initial [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersResponse) object, and provides an `__iter__` method to iterate through its `users` field.

If there are more pages, the `__iter__` method will make additional `ListUsers` requests and continue to iterate through the `users` field on the corresponding responses.

All the usual [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListUsersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
