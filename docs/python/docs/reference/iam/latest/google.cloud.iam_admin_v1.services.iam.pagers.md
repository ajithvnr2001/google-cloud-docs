---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers
title: Module pagers (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:25.901940+00:00
---

# Module pagers (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 

API documentation for `iam_admin_v1.services.iam.pagers` module.

## Classes 

### [ListRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager)
    
    
    ListRolesAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.iam_admin_v1.types.iam.ListRolesResponse]
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListRolesResponse,
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

A pager for iterating through `list_roles` requests.

This class thinly wraps an initial [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) object, and provides an `__aiter__` method to iterate through its `roles` field.

If there are more pages, the `__aiter__` method will make additional `ListRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRolesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager)
    
    
    ListRolesPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.ListRolesResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListRolesResponse,
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

A pager for iterating through `list_roles` requests.

This class thinly wraps an initial [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) object, and provides an `__iter__` method to iterate through its `roles` field.

If there are more pages, the `__iter__` method will make additional `ListRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListServiceAccountsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager)
    
    
    ListServiceAccountsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse
            ],
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse,
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

A pager for iterating through `list_service_accounts` requests.

This class thinly wraps an initial [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) object, and provides an `__aiter__` method to iterate through its `accounts` field.

If there are more pages, the `__aiter__` method will make additional `ListServiceAccounts` requests and continue to iterate through the `accounts` field on the corresponding responses.

All the usual [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListServiceAccountsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsPager)
    
    
    ListServiceAccountsPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse,
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

A pager for iterating through `list_service_accounts` requests.

This class thinly wraps an initial [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) object, and provides an `__iter__` method to iterate through its `accounts` field.

If there are more pages, the `__iter__` method will make additional `ListServiceAccounts` requests and continue to iterate through the `accounts` field on the corresponding responses.

All the usual [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryGrantableRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager)
    
    
    QueryGrantableRolesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse
            ],
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse,
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

A pager for iterating through `query_grantable_roles` requests.

This class thinly wraps an initial [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) object, and provides an `__aiter__` method to iterate through its `roles` field.

If there are more pages, the `__aiter__` method will make additional `QueryGrantableRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryGrantableRolesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesPager)
    
    
    QueryGrantableRolesPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse,
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

A pager for iterating through `query_grantable_roles` requests.

This class thinly wraps an initial [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) object, and provides an `__iter__` method to iterate through its `roles` field.

If there are more pages, the `__iter__` method will make additional `QueryGrantableRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryTestablePermissionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager)
    
    
    QueryTestablePermissionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse
            ],
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse,
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

A pager for iterating through `query_testable_permissions` requests.

This class thinly wraps an initial [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) object, and provides an `__aiter__` method to iterate through its `permissions` field.

If there are more pages, the `__aiter__` method will make additional `QueryTestablePermissions` requests and continue to iterate through the `permissions` field on the corresponding responses.

All the usual [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryTestablePermissionsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsPager)
    
    
    QueryTestablePermissionsPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse,
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

A pager for iterating through `query_testable_permissions` requests.

This class thinly wraps an initial [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) object, and provides an `__iter__` method to iterate through its `permissions` field.

If there are more pages, the `__iter__` method will make additional `QueryTestablePermissions` requests and continue to iterate through the `permissions` field on the corresponding responses.

All the usual [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
