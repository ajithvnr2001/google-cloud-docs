---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers
title: Module pagers (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:06.385443+00:00
---

# Module pagers (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

API documentation for `geminidataanalytics_v1alpha.services.data_agent_service.pagers` module.

## Classes 

### [ListAccessibleDataAgentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsAsyncPager)
    
    
    ListAccessibleDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

A pager for iterating through `list_accessible_data_agents` requests.

This class thinly wraps an initial [ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsResponse) object, and provides an `__aiter__` method to iterate through its `data_agents` field.

If there are more pages, the `__aiter__` method will make additional `ListAccessibleDataAgents` requests and continue to iterate through the `data_agents` field on the corresponding responses.

All the usual [ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccessibleDataAgentsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager)
    
    
    ListAccessibleDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsResponse,
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

A pager for iterating through `list_accessible_data_agents` requests.

This class thinly wraps an initial [ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsResponse) object, and provides an `__iter__` method to iterate through its `data_agents` field.

If there are more pages, the `__iter__` method will make additional `ListAccessibleDataAgents` requests and continue to iterate through the `data_agents` field on the corresponding responses.

All the usual [ListAccessibleDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataAgentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsAsyncPager)
    
    
    ListDataAgentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse
            ],
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse,
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

A pager for iterating through `list_data_agents` requests.

This class thinly wraps an initial [ListDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsResponse) object, and provides an `__aiter__` method to iterate through its `data_agents` field.

If there are more pages, the `__aiter__` method will make additional `ListDataAgents` requests and continue to iterate through the `data_agents` field on the corresponding responses.

All the usual [ListDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDataAgentsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager)
    
    
    ListDataAgentsPager(
        method: typing.Callable[
            [...],
            google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse,
        ],
        request: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
        response: google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsResponse,
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

A pager for iterating through `list_data_agents` requests.

This class thinly wraps an initial [ListDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsResponse) object, and provides an `__iter__` method to iterate through its `data_agents` field.

If there are more pages, the `__iter__` method will make additional `ListDataAgents` requests and continue to iterate through the `data_agents` field on the corresponding responses.

All the usual [ListDataAgentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
