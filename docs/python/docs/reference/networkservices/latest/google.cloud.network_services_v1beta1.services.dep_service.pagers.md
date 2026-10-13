---
url: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers
title: Module pagers (0.10.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:27.699265+00:00
---

# Module pagers (0.10.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.10.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.4 (latest)  0.10.3  0.9.0  0.8.0  0.7.0  0.6.0  0.5.24  0.4.1  0.3.0  0.2.2  0.1.1 

API documentation for `network_services_v1beta1.services.dep_service.pagers` module.

## Classes 

### [ListExtensionBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListExtensionBindingsAsyncPager)
    
    
    ListExtensionBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.network_services_v1beta1.types.dep.ListExtensionBindingsResponse
            ],
        ],
        request: google.cloud.network_services_v1beta1.types.dep.ListExtensionBindingsRequest,
        response: google.cloud.network_services_v1beta1.types.dep.ListExtensionBindingsResponse,
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

A pager for iterating through `list_extension_bindings` requests.

This class thinly wraps an initial [ListExtensionBindingsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListExtensionBindingsResponse) object, and provides an `__aiter__` method to iterate through its `extension_bindings` field.

If there are more pages, the `__aiter__` method will make additional `ListExtensionBindings` requests and continue to iterate through the `extension_bindings` field on the corresponding responses.

All the usual [ListExtensionBindingsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListExtensionBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListExtensionBindingsPager](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListExtensionBindingsPager)
    
    
    ListExtensionBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.network_services_v1beta1.types.dep.ListExtensionBindingsResponse,
        ],
        request: google.cloud.network_services_v1beta1.types.dep.ListExtensionBindingsRequest,
        response: google.cloud.network_services_v1beta1.types.dep.ListExtensionBindingsResponse,
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

A pager for iterating through `list_extension_bindings` requests.

This class thinly wraps an initial [ListExtensionBindingsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListExtensionBindingsResponse) object, and provides an `__iter__` method to iterate through its `extension_bindings` field.

If there are more pages, the `__iter__` method will make additional `ListExtensionBindings` requests and continue to iterate through the `extension_bindings` field on the corresponding responses.

All the usual [ListExtensionBindingsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListExtensionBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLbRouteExtensionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListLbRouteExtensionsAsyncPager)
    
    
    ListLbRouteExtensionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.network_services_v1beta1.types.dep.ListLbRouteExtensionsResponse
            ],
        ],
        request: google.cloud.network_services_v1beta1.types.dep.ListLbRouteExtensionsRequest,
        response: google.cloud.network_services_v1beta1.types.dep.ListLbRouteExtensionsResponse,
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

A pager for iterating through `list_lb_route_extensions` requests.

This class thinly wraps an initial [ListLbRouteExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsResponse) object, and provides an `__aiter__` method to iterate through its `lb_route_extensions` field.

If there are more pages, the `__aiter__` method will make additional `ListLbRouteExtensions` requests and continue to iterate through the `lb_route_extensions` field on the corresponding responses.

All the usual [ListLbRouteExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLbRouteExtensionsPager](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListLbRouteExtensionsPager)
    
    
    ListLbRouteExtensionsPager(
        method: typing.Callable[
            [...],
            google.cloud.network_services_v1beta1.types.dep.ListLbRouteExtensionsResponse,
        ],
        request: google.cloud.network_services_v1beta1.types.dep.ListLbRouteExtensionsRequest,
        response: google.cloud.network_services_v1beta1.types.dep.ListLbRouteExtensionsResponse,
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

A pager for iterating through `list_lb_route_extensions` requests.

This class thinly wraps an initial [ListLbRouteExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsResponse) object, and provides an `__iter__` method to iterate through its `lb_route_extensions` field.

If there are more pages, the `__iter__` method will make additional `ListLbRouteExtensions` requests and continue to iterate through the `lb_route_extensions` field on the corresponding responses.

All the usual [ListLbRouteExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLbTrafficExtensionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListLbTrafficExtensionsAsyncPager)
    
    
    ListLbTrafficExtensionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.network_services_v1beta1.types.dep.ListLbTrafficExtensionsResponse
            ],
        ],
        request: google.cloud.network_services_v1beta1.types.dep.ListLbTrafficExtensionsRequest,
        response: google.cloud.network_services_v1beta1.types.dep.ListLbTrafficExtensionsResponse,
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

A pager for iterating through `list_lb_traffic_extensions` requests.

This class thinly wraps an initial [ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbTrafficExtensionsResponse) object, and provides an `__aiter__` method to iterate through its `lb_traffic_extensions` field.

If there are more pages, the `__aiter__` method will make additional `ListLbTrafficExtensions` requests and continue to iterate through the `lb_traffic_extensions` field on the corresponding responses.

All the usual [ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbTrafficExtensionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListLbTrafficExtensionsPager](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListLbTrafficExtensionsPager)
    
    
    ListLbTrafficExtensionsPager(
        method: typing.Callable[
            [...],
            google.cloud.network_services_v1beta1.types.dep.ListLbTrafficExtensionsResponse,
        ],
        request: google.cloud.network_services_v1beta1.types.dep.ListLbTrafficExtensionsRequest,
        response: google.cloud.network_services_v1beta1.types.dep.ListLbTrafficExtensionsResponse,
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

A pager for iterating through `list_lb_traffic_extensions` requests.

This class thinly wraps an initial [ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbTrafficExtensionsResponse) object, and provides an `__iter__` method to iterate through its `lb_traffic_extensions` field.

If there are more pages, the `__iter__` method will make additional `ListLbTrafficExtensions` requests and continue to iterate through the `lb_traffic_extensions` field on the corresponding responses.

All the usual [ListLbTrafficExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbTrafficExtensionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
