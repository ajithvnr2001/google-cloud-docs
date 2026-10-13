---
url: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers
title: Module pagers (2.12.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:42:36.851973+00:00
---

# Module pagers (2.12.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.0  2.10.0  2.9.0  2.8.0  2.7.1  2.6.3  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.0  1.19.1  1.18.1  1.17.3  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1  1.2.1  1.1.1  1.0.0  0.3.2  0.2.0  0.1.1 

API documentation for `deploy_v1.services.cloud_deploy.pagers` module.

## Classes 

### [ListAutomationRunsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsAsyncPager)
    
    
    ListAutomationRunsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse,
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

A pager for iterating through `list_automation_runs` requests.

This class thinly wraps an initial [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) object, and provides an `__aiter__` method to iterate through its `automation_runs` field.

If there are more pages, the `__aiter__` method will make additional `ListAutomationRuns` requests and continue to iterate through the `automation_runs` field on the corresponding responses.

All the usual [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutomationRunsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationRunsPager)
    
    
    ListAutomationRunsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationRunsResponse,
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

A pager for iterating through `list_automation_runs` requests.

This class thinly wraps an initial [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) object, and provides an `__iter__` method to iterate through its `automation_runs` field.

If there are more pages, the `__iter__` method will make additional `ListAutomationRuns` requests and continue to iterate through the `automation_runs` field on the corresponding responses.

All the usual [ListAutomationRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutomationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsAsyncPager)
    
    
    ListAutomationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse,
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

A pager for iterating through `list_automations` requests.

This class thinly wraps an initial [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) object, and provides an `__aiter__` method to iterate through its `automations` field.

If there are more pages, the `__aiter__` method will make additional `ListAutomations` requests and continue to iterate through the `automations` field on the corresponding responses.

All the usual [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAutomationsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListAutomationsPager)
    
    
    ListAutomationsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListAutomationsResponse,
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

A pager for iterating through `list_automations` requests.

This class thinly wraps an initial [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) object, and provides an `__iter__` method to iterate through its `automations` field.

If there are more pages, the `__iter__` method will make additional `ListAutomations` requests and continue to iterate through the `automations` field on the corresponding responses.

All the usual [ListAutomationsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListAutomationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCustomTargetTypesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesAsyncPager)
    
    
    ListCustomTargetTypesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse,
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

A pager for iterating through `list_custom_target_types` requests.

This class thinly wraps an initial [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) object, and provides an `__aiter__` method to iterate through its `custom_target_types` field.

If there are more pages, the `__aiter__` method will make additional `ListCustomTargetTypes` requests and continue to iterate through the `custom_target_types` field on the corresponding responses.

All the usual [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCustomTargetTypesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListCustomTargetTypesPager)
    
    
    ListCustomTargetTypesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListCustomTargetTypesResponse,
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

A pager for iterating through `list_custom_target_types` requests.

This class thinly wraps an initial [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) object, and provides an `__iter__` method to iterate through its `custom_target_types` field.

If there are more pages, the `__iter__` method will make additional `ListCustomTargetTypes` requests and continue to iterate through the `custom_target_types` field on the corresponding responses.

All the usual [ListCustomTargetTypesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListCustomTargetTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeliveryPipelinesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesAsyncPager)
    
    
    ListDeliveryPipelinesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse,
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

A pager for iterating through `list_delivery_pipelines` requests.

This class thinly wraps an initial [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) object, and provides an `__aiter__` method to iterate through its `delivery_pipelines` field.

If there are more pages, the `__aiter__` method will make additional `ListDeliveryPipelines` requests and continue to iterate through the `delivery_pipelines` field on the corresponding responses.

All the usual [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeliveryPipelinesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeliveryPipelinesPager)
    
    
    ListDeliveryPipelinesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeliveryPipelinesResponse,
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

A pager for iterating through `list_delivery_pipelines` requests.

This class thinly wraps an initial [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) object, and provides an `__iter__` method to iterate through its `delivery_pipelines` field.

If there are more pages, the `__iter__` method will make additional `ListDeliveryPipelines` requests and continue to iterate through the `delivery_pipelines` field on the corresponding responses.

All the usual [ListDeliveryPipelinesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeliveryPipelinesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeployPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesAsyncPager)
    
    
    ListDeployPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse,
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

A pager for iterating through `list_deploy_policies` requests.

This class thinly wraps an initial [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `deploy_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListDeployPolicies` requests and continue to iterate through the `deploy_policies` field on the corresponding responses.

All the usual [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDeployPoliciesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListDeployPoliciesPager)
    
    
    ListDeployPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListDeployPoliciesResponse,
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

A pager for iterating through `list_deploy_policies` requests.

This class thinly wraps an initial [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) object, and provides an `__iter__` method to iterate through its `deploy_policies` field.

If there are more pages, the `__iter__` method will make additional `ListDeployPolicies` requests and continue to iterate through the `deploy_policies` field on the corresponding responses.

All the usual [ListDeployPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListDeployPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobRunsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsAsyncPager)
    
    
    ListJobRunsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse,
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

A pager for iterating through `list_job_runs` requests.

This class thinly wraps an initial [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) object, and provides an `__aiter__` method to iterate through its `job_runs` field.

If there are more pages, the `__aiter__` method will make additional `ListJobRuns` requests and continue to iterate through the `job_runs` field on the corresponding responses.

All the usual [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListJobRunsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListJobRunsPager)
    
    
    ListJobRunsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListJobRunsResponse,
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

A pager for iterating through `list_job_runs` requests.

This class thinly wraps an initial [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) object, and provides an `__iter__` method to iterate through its `job_runs` field.

If there are more pages, the `__iter__` method will make additional `ListJobRuns` requests and continue to iterate through the `job_runs` field on the corresponding responses.

All the usual [ListJobRunsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListJobRunsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListReleasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesAsyncPager)
    
    
    ListReleasesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse,
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

A pager for iterating through `list_releases` requests.

This class thinly wraps an initial [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) object, and provides an `__aiter__` method to iterate through its `releases` field.

If there are more pages, the `__aiter__` method will make additional `ListReleases` requests and continue to iterate through the `releases` field on the corresponding responses.

All the usual [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListReleasesPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListReleasesPager)
    
    
    ListReleasesPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListReleasesResponse,
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

A pager for iterating through `list_releases` requests.

This class thinly wraps an initial [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) object, and provides an `__iter__` method to iterate through its `releases` field.

If there are more pages, the `__iter__` method will make additional `ListReleases` requests and continue to iterate through the `releases` field on the corresponding responses.

All the usual [ListReleasesResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListReleasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRolloutsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsAsyncPager)
    
    
    ListRolloutsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse
            ],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse,
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

A pager for iterating through `list_rollouts` requests.

This class thinly wraps an initial [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) object, and provides an `__aiter__` method to iterate through its `rollouts` field.

If there are more pages, the `__aiter__` method will make additional `ListRollouts` requests and continue to iterate through the `rollouts` field on the corresponding responses.

All the usual [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRolloutsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListRolloutsPager)
    
    
    ListRolloutsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListRolloutsResponse,
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

A pager for iterating through `list_rollouts` requests.

This class thinly wraps an initial [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) object, and provides an `__iter__` method to iterate through its `rollouts` field.

If there are more pages, the `__iter__` method will make additional `ListRollouts` requests and continue to iterate through the `rollouts` field on the corresponding responses.

All the usual [ListRolloutsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListRolloutsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsAsyncPager)
    
    
    ListTargetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse],
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse,
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

A pager for iterating through `list_targets` requests.

This class thinly wraps an initial [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) object, and provides an `__aiter__` method to iterate through its `targets` field.

If there are more pages, the `__aiter__` method will make additional `ListTargets` requests and continue to iterate through the `targets` field on the corresponding responses.

All the usual [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTargetsPager](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.services.cloud_deploy.pagers.ListTargetsPager)
    
    
    ListTargetsPager(
        method: typing.Callable[
            [...], google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse
        ],
        request: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsRequest,
        response: google.cloud.deploy_v1.types.cloud_deploy.ListTargetsResponse,
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

A pager for iterating through `list_targets` requests.

This class thinly wraps an initial [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) object, and provides an `__iter__` method to iterate through its `targets` field.

If there are more pages, the `__iter__` method will make additional `ListTargets` requests and continue to iterate through the `targets` field on the corresponding responses.

All the usual [ListTargetsResponse](https://docs.cloud.google.com/python/docs/reference/clouddeploy/latest/google.cloud.deploy_v1.types.ListTargetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
