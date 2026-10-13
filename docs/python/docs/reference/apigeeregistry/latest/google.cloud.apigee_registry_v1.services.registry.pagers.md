---
url: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers
title: Module pagers (0.10.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:24:04.144782+00:00
---

# Module pagers (0.10.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.0 (latest)  0.9.0  0.8.0  0.7.0  0.6.18  0.5.1  0.4.0  0.3.2  0.2.1  0.1.2 

API documentation for `apigee_registry_v1.services.registry.pagers` module.

## Classes 

### [ListApiDeploymentRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsAsyncPager)
    
    
    ListApiDeploymentRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse,
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

A pager for iterating through `list_api_deployment_revisions` requests.

This class thinly wraps an initial [ListApiDeploymentRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `api_deployments` field.

If there are more pages, the `__aiter__` method will make additional `ListApiDeploymentRevisions` requests and continue to iterate through the `api_deployments` field on the corresponding responses.

All the usual [ListApiDeploymentRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiDeploymentRevisionsPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentRevisionsPager)
    
    
    ListApiDeploymentRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentRevisionsResponse,
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

A pager for iterating through `list_api_deployment_revisions` requests.

This class thinly wraps an initial [ListApiDeploymentRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsResponse) object, and provides an `__iter__` method to iterate through its `api_deployments` field.

If there are more pages, the `__iter__` method will make additional `ListApiDeploymentRevisions` requests and continue to iterate through the `api_deployments` field on the corresponding responses.

All the usual [ListApiDeploymentRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiDeploymentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsAsyncPager)
    
    
    ListApiDeploymentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse,
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

A pager for iterating through `list_api_deployments` requests.

This class thinly wraps an initial [ListApiDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsResponse) object, and provides an `__aiter__` method to iterate through its `api_deployments` field.

If there are more pages, the `__aiter__` method will make additional `ListApiDeployments` requests and continue to iterate through the `api_deployments` field on the corresponding responses.

All the usual [ListApiDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiDeploymentsPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiDeploymentsPager)
    
    
    ListApiDeploymentsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiDeploymentsResponse,
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

A pager for iterating through `list_api_deployments` requests.

This class thinly wraps an initial [ListApiDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsResponse) object, and provides an `__iter__` method to iterate through its `api_deployments` field.

If there are more pages, the `__iter__` method will make additional `ListApiDeployments` requests and continue to iterate through the `api_deployments` field on the corresponding responses.

All the usual [ListApiDeploymentsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiDeploymentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiSpecRevisionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsAsyncPager)
    
    
    ListApiSpecRevisionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse,
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

A pager for iterating through `list_api_spec_revisions` requests.

This class thinly wraps an initial [ListApiSpecRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsResponse) object, and provides an `__aiter__` method to iterate through its `api_specs` field.

If there are more pages, the `__aiter__` method will make additional `ListApiSpecRevisions` requests and continue to iterate through the `api_specs` field on the corresponding responses.

All the usual [ListApiSpecRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiSpecRevisionsPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecRevisionsPager)
    
    
    ListApiSpecRevisionsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecRevisionsResponse,
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

A pager for iterating through `list_api_spec_revisions` requests.

This class thinly wraps an initial [ListApiSpecRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsResponse) object, and provides an `__iter__` method to iterate through its `api_specs` field.

If there are more pages, the `__iter__` method will make additional `ListApiSpecRevisions` requests and continue to iterate through the `api_specs` field on the corresponding responses.

All the usual [ListApiSpecRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecRevisionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsAsyncPager)
    
    
    ListApiSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse,
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

A pager for iterating through `list_api_specs` requests.

This class thinly wraps an initial [ListApiSpecsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsResponse) object, and provides an `__aiter__` method to iterate through its `api_specs` field.

If there are more pages, the `__aiter__` method will make additional `ListApiSpecs` requests and continue to iterate through the `api_specs` field on the corresponding responses.

All the usual [ListApiSpecsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiSpecsPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiSpecsPager)
    
    
    ListApiSpecsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiSpecsResponse,
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

A pager for iterating through `list_api_specs` requests.

This class thinly wraps an initial [ListApiSpecsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsResponse) object, and provides an `__iter__` method to iterate through its `api_specs` field.

If there are more pages, the `__iter__` method will make additional `ListApiSpecs` requests and continue to iterate through the `api_specs` field on the corresponding responses.

All the usual [ListApiSpecsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsAsyncPager)
    
    
    ListApiVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse,
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

A pager for iterating through `list_api_versions` requests.

This class thinly wraps an initial [ListApiVersionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsResponse) object, and provides an `__aiter__` method to iterate through its `api_versions` field.

If there are more pages, the `__aiter__` method will make additional `ListApiVersions` requests and continue to iterate through the `api_versions` field on the corresponding responses.

All the usual [ListApiVersionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApiVersionsPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApiVersionsPager)
    
    
    ListApiVersionsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApiVersionsResponse,
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

A pager for iterating through `list_api_versions` requests.

This class thinly wraps an initial [ListApiVersionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsResponse) object, and provides an `__iter__` method to iterate through its `api_versions` field.

If there are more pages, the `__iter__` method will make additional `ListApiVersions` requests and continue to iterate through the `api_versions` field on the corresponding responses.

All the usual [ListApiVersionsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApiVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApisAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApisAsyncPager)
    
    
    ListApisAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse,
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

This class thinly wraps an initial [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisResponse) object, and provides an `__aiter__` method to iterate through its `apis` field.

If there are more pages, the `__aiter__` method will make additional `ListApis` requests and continue to iterate through the `apis` field on the corresponding responses.

All the usual [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListApisPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListApisPager)
    
    
    ListApisPager(
        method: typing.Callable[
            [...], google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListApisRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListApisResponse,
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

This class thinly wraps an initial [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisResponse) object, and provides an `__iter__` method to iterate through its `apis` field.

If there are more pages, the `__iter__` method will make additional `ListApis` requests and continue to iterate through the `apis` field on the corresponding responses.

All the usual [ListApisResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListApisResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListArtifactsAsyncPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsAsyncPager)
    
    
    ListArtifactsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse
            ],
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse,
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

A pager for iterating through `list_artifacts` requests.

This class thinly wraps an initial [ListArtifactsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsResponse) object, and provides an `__aiter__` method to iterate through its `artifacts` field.

If there are more pages, the `__aiter__` method will make additional `ListArtifacts` requests and continue to iterate through the `artifacts` field on the corresponding responses.

All the usual [ListArtifactsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListArtifactsPager](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.services.registry.pagers.ListArtifactsPager)
    
    
    ListArtifactsPager(
        method: typing.Callable[
            [...],
            google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse,
        ],
        request: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsRequest,
        response: google.cloud.apigee_registry_v1.types.registry_service.ListArtifactsResponse,
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

A pager for iterating through `list_artifacts` requests.

This class thinly wraps an initial [ListArtifactsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsResponse) object, and provides an `__iter__` method to iterate through its `artifacts` field.

If there are more pages, the `__iter__` method will make additional `ListArtifacts` requests and continue to iterate through the `artifacts` field on the corresponding responses.

All the usual [ListArtifactsResponse](https://docs.cloud.google.com/python/docs/reference/apigeeregistry/latest/google.cloud.apigee_registry_v1.types.ListArtifactsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
