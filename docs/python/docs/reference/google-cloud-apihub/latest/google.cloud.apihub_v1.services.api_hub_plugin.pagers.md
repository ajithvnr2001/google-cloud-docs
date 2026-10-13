---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers
title: Module pagers (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:20.861837+00:00
---

# Module pagers (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 

API documentation for `apihub_v1.services.api_hub_plugin.pagers` module.

## Classes 

### [ListPluginInstancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesAsyncPager)
    
    
    ListPluginInstancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse,
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

A pager for iterating through `list_plugin_instances` requests.

This class thinly wraps an initial [ListPluginInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesResponse) object, and provides an `__aiter__` method to iterate through its `plugin_instances` field.

If there are more pages, the `__aiter__` method will make additional `ListPluginInstances` requests and continue to iterate through the `plugin_instances` field on the corresponding responses.

All the usual [ListPluginInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPluginInstancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginInstancesPager)
    
    
    ListPluginInstancesPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginInstancesResponse,
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

A pager for iterating through `list_plugin_instances` requests.

This class thinly wraps an initial [ListPluginInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesResponse) object, and provides an `__iter__` method to iterate through its `plugin_instances` field.

If there are more pages, the `__iter__` method will make additional `ListPluginInstances` requests and continue to iterate through the `plugin_instances` field on the corresponding responses.

All the usual [ListPluginInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginInstancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPluginsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsAsyncPager)
    
    
    ListPluginsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse
            ],
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse,
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

A pager for iterating through `list_plugins` requests.

This class thinly wraps an initial [ListPluginsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsResponse) object, and provides an `__aiter__` method to iterate through its `plugins` field.

If there are more pages, the `__aiter__` method will make additional `ListPlugins` requests and continue to iterate through the `plugins` field on the corresponding responses.

All the usual [ListPluginsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPluginsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.services.api_hub_plugin.pagers.ListPluginsPager)
    
    
    ListPluginsPager(
        method: typing.Callable[
            [...], google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse
        ],
        request: google.cloud.apihub_v1.types.plugin_service.ListPluginsRequest,
        response: google.cloud.apihub_v1.types.plugin_service.ListPluginsResponse,
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

A pager for iterating through `list_plugins` requests.

This class thinly wraps an initial [ListPluginsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsResponse) object, and provides an `__iter__` method to iterate through its `plugins` field.

If there are more pages, the `__iter__` method will make additional `ListPlugins` requests and continue to iterate through the `plugins` field on the corresponding responses.

All the usual [ListPluginsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.ListPluginsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
