---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers
title: Module pagers (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:12.030999+00:00
---

# Module pagers (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 

API documentation for `apihub_v1.services.api_hub.pagers` module.

## Classes 

### [ListApiOperationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsAsyncPager)
    
    
    ListApiOperationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse,
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

A pager for iterating through `list_api_operations` requests.

This class thinly wraps an initial [ListApiOperationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsResponse) object, and provides an `__aiter__` method to iterate through its `api_operations` field.

If there are more pages, the `__aiter__` method will make additional `ListApiOperations` requests and continue to iterate through the `api_operations` field on the corresponding responses.

All the usual [ListApiOperationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiOperationsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApiOperationsPager)
    
    
    ListApiOperationsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApiOperationsResponse,
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

A pager for iterating through `list_api_operations` requests.

This class thinly wraps an initial [ListApiOperationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsResponse) object, and provides an `__iter__` method to iterate through its `api_operations` field.

If there are more pages, the `__iter__` method will make additional `ListApiOperations` requests and continue to iterate through the `api_operations` field on the corresponding responses.

All the usual [ListApiOperationsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApiOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApisAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApisAsyncPager)
    
    
    ListApisAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.apihub_v1.types.apihub_service.ListApisResponse],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApisResponse,
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

A pager for iterating through `list_apis` requests.

This class thinly wraps an initial [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisResponse) object, and provides an `__aiter__` method to iterate through its `apis` field.

If there are more pages, the `__aiter__` method will make additional `ListApis` requests and continue to iterate through the `apis` field on the corresponding responses.

All the usual [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApisPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListApisPager)
    
    
    ListApisPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListApisResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListApisResponse,
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

A pager for iterating through `list_apis` requests.

This class thinly wraps an initial [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisResponse) object, and provides an `__iter__` method to iterate through its `apis` field.

If there are more pages, the `__iter__` method will make additional `ListApis` requests and continue to iterate through the `apis` field on the corresponding responses.

All the usual [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListApisResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAttributesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesAsyncPager)
    
    
    ListAttributesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse,
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

A pager for iterating through `list_attributes` requests.

This class thinly wraps an initial [ListAttributesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesResponse) object, and provides an `__aiter__` method to iterate through its `attributes` field.

If there are more pages, the `__aiter__` method will make additional `ListAttributes` requests and continue to iterate through the `attributes` field on the corresponding responses.

All the usual [ListAttributesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAttributesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListAttributesPager)
    
    
    ListAttributesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListAttributesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListAttributesResponse,
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

A pager for iterating through `list_attributes` requests.

This class thinly wraps an initial [ListAttributesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesResponse) object, and provides an `__iter__` method to iterate through its `attributes` field.

If there are more pages, the `__iter__` method will make additional `ListAttributes` requests and continue to iterate through the `attributes` field on the corresponding responses.

All the usual [ListAttributesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListAttributesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsAsyncPager)
    
    
    ListDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse,
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

This class thinly wraps an initial [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsResponse) object, and provides an `__aiter__` method to iterate through its `deployments` field.

If there are more pages, the `__aiter__` method will make additional `ListDeployments` requests and continue to iterate through the `deployments` field on the corresponding responses.

All the usual [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeploymentsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListDeploymentsPager)
    
    
    ListDeploymentsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListDeploymentsResponse,
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

This class thinly wraps an initial [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsResponse) object, and provides an `__iter__` method to iterate through its `deployments` field.

If there are more pages, the `__iter__` method will make additional `ListDeployments` requests and continue to iterate through the `deployments` field on the corresponding responses.

All the usual [ListDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListDeploymentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListExternalApisAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisAsyncPager)
    
    
    ListExternalApisAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse,
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

A pager for iterating through `list_external_apis` requests.

This class thinly wraps an initial [ListExternalApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisResponse) object, and provides an `__aiter__` method to iterate through its `external_apis` field.

If there are more pages, the `__aiter__` method will make additional `ListExternalApis` requests and continue to iterate through the `external_apis` field on the corresponding responses.

All the usual [ListExternalApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListExternalApisPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListExternalApisPager)
    
    
    ListExternalApisPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListExternalApisRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListExternalApisResponse,
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

A pager for iterating through `list_external_apis` requests.

This class thinly wraps an initial [ListExternalApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisResponse) object, and provides an `__iter__` method to iterate through its `external_apis` field.

If there are more pages, the `__iter__` method will make additional `ListExternalApis` requests and continue to iterate through the `external_apis` field on the corresponding responses.

All the usual [ListExternalApisResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListExternalApisResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsAsyncPager)
    
    
    ListSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse,
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

A pager for iterating through `list_specs` requests.

This class thinly wraps an initial [ListSpecsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsResponse) object, and provides an `__aiter__` method to iterate through its `specs` field.

If there are more pages, the `__aiter__` method will make additional `ListSpecs` requests and continue to iterate through the `specs` field on the corresponding responses.

All the usual [ListSpecsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSpecsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListSpecsPager)
    
    
    ListSpecsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListSpecsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListSpecsResponse,
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

A pager for iterating through `list_specs` requests.

This class thinly wraps an initial [ListSpecsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsResponse) object, and provides an `__iter__` method to iterate through its `specs` field.

If there are more pages, the `__iter__` method will make additional `ListSpecs` requests and continue to iterate through the `specs` field on the corresponding responses.

All the usual [ListSpecsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsAsyncPager)
    
    
    ListVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse,
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

A pager for iterating through `list_versions` requests.

This class thinly wraps an initial [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsResponse) object, and provides an `__aiter__` method to iterate through its `versions` field.

If there are more pages, the `__aiter__` method will make additional `ListVersions` requests and continue to iterate through the `versions` field on the corresponding responses.

All the usual [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListVersionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.ListVersionsPager)
    
    
    ListVersionsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.ListVersionsRequest,
        response: google.cloud.apihub_v1.types.apihub_service.ListVersionsResponse,
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

A pager for iterating through `list_versions` requests.

This class thinly wraps an initial [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsResponse) object, and provides an `__iter__` method to iterate through its `versions` field.

If there are more pages, the `__iter__` method will make additional `ListVersions` requests and continue to iterate through the `versions` field on the corresponding responses.

All the usual [ListVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesAsyncPager)
    
    
    SearchResourcesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse,
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

A pager for iterating through `search_resources` requests.

This class thinly wraps an initial [SearchResourcesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesResponse) object, and provides an `__aiter__` method to iterate through its `search_results` field.

If there are more pages, the `__aiter__` method will make additional `SearchResources` requests and continue to iterate through the `search_results` field on the corresponding responses.

All the usual [SearchResourcesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchResourcesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub.pagers.SearchResourcesPager)
    
    
    SearchResourcesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse
        ],
        request: google.cloud.apihub_v1.types.apihub_service.SearchResourcesRequest,
        response: google.cloud.apihub_v1.types.apihub_service.SearchResourcesResponse,
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

A pager for iterating through `search_resources` requests.

This class thinly wraps an initial [SearchResourcesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesResponse) object, and provides an `__iter__` method to iterate through its `search_results` field.

If there are more pages, the `__iter__` method will make additional `SearchResources` requests and continue to iterate through the `search_results` field on the corresponding responses.

All the usual [SearchResourcesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.SearchResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
