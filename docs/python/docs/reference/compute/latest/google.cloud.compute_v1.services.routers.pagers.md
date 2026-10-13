---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers
title: Module pagers (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:38.801187+00:00
---

# Module pagers (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 

API documentation for `compute_v1.services.routers.pagers` module.

## Classes 

### [AggregatedListPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers.AggregatedListPager)
    
    
    AggregatedListPager(
        method: typing.Callable[
            [...], google.cloud.compute_v1.types.compute.RouterAggregatedList
        ],
        request: google.cloud.compute_v1.types.compute.AggregatedListRoutersRequest,
        response: google.cloud.compute_v1.types.compute.RouterAggregatedList,
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

A pager for iterating through `aggregated_list` requests.

This class thinly wraps an initial [RouterAggregatedList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RouterAggregatedList) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `AggregatedList` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [RouterAggregatedList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RouterAggregatedList) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GetNatMappingInfoPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers.GetNatMappingInfoPager)
    
    
    GetNatMappingInfoPager(
        method: typing.Callable[
            [...], google.cloud.compute_v1.types.compute.VmEndpointNatMappingsList
        ],
        request: google.cloud.compute_v1.types.compute.GetNatMappingInfoRoutersRequest,
        response: google.cloud.compute_v1.types.compute.VmEndpointNatMappingsList,
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

A pager for iterating through `get_nat_mapping_info` requests.

This class thinly wraps an initial [VmEndpointNatMappingsList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.VmEndpointNatMappingsList) object, and provides an `__iter__` method to iterate through its `result` field.

If there are more pages, the `__iter__` method will make additional `GetNatMappingInfo` requests and continue to iterate through the `result` field on the corresponding responses.

All the usual [VmEndpointNatMappingsList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.VmEndpointNatMappingsList) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBgpRoutesPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers.ListBgpRoutesPager)
    
    
    ListBgpRoutesPager(
        method: typing.Callable[
            [...], google.cloud.compute_v1.types.compute.RoutersListBgpRoutes
        ],
        request: google.cloud.compute_v1.types.compute.ListBgpRoutesRoutersRequest,
        response: google.cloud.compute_v1.types.compute.RoutersListBgpRoutes,
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

A pager for iterating through `list_bgp_routes` requests.

This class thinly wraps an initial [RoutersListBgpRoutes](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RoutersListBgpRoutes) object, and provides an `__iter__` method to iterate through its `result` field.

If there are more pages, the `__iter__` method will make additional `ListBgpRoutes` requests and continue to iterate through the `result` field on the corresponding responses.

All the usual [RoutersListBgpRoutes](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RoutersListBgpRoutes) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListNamedSetsPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers.ListNamedSetsPager)
    
    
    ListNamedSetsPager(
        method: typing.Callable[
            [...], google.cloud.compute_v1.types.compute.RoutersListNamedSets
        ],
        request: google.cloud.compute_v1.types.compute.ListNamedSetsRoutersRequest,
        response: google.cloud.compute_v1.types.compute.RoutersListNamedSets,
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

A pager for iterating through `list_named_sets` requests.

This class thinly wraps an initial [RoutersListNamedSets](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RoutersListNamedSets) object, and provides an `__iter__` method to iterate through its `result` field.

If there are more pages, the `__iter__` method will make additional `ListNamedSets` requests and continue to iterate through the `result` field on the corresponding responses.

All the usual [RoutersListNamedSets](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RoutersListNamedSets) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers.ListPager)
    
    
    ListPager(
        method: typing.Callable[[...], google.cloud.compute_v1.types.compute.RouterList],
        request: google.cloud.compute_v1.types.compute.ListRoutersRequest,
        response: google.cloud.compute_v1.types.compute.RouterList,
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

A pager for iterating through `list` requests.

This class thinly wraps an initial [RouterList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RouterList) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `List` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [RouterList](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RouterList) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRoutePoliciesPager](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.services.routers.pagers.ListRoutePoliciesPager)
    
    
    ListRoutePoliciesPager(
        method: typing.Callable[
            [...], google.cloud.compute_v1.types.compute.RoutersListRoutePolicies
        ],
        request: google.cloud.compute_v1.types.compute.ListRoutePoliciesRoutersRequest,
        response: google.cloud.compute_v1.types.compute.RoutersListRoutePolicies,
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

A pager for iterating through `list_route_policies` requests.

This class thinly wraps an initial [RoutersListRoutePolicies](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RoutersListRoutePolicies) object, and provides an `__iter__` method to iterate through its `result` field.

If there are more pages, the `__iter__` method will make additional `ListRoutePolicies` requests and continue to iterate through the `result` field on the corresponding responses.

All the usual [RoutersListRoutePolicies](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.RoutersListRoutePolicies) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
