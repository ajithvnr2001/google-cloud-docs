---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers
title: Module pagers (0.5.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:35.439053+00:00
---

# Module pagers (0.5.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.5.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.2 (latest)  0.5.1  0.4.0  0.3.0  0.2.0  0.1.18 

API documentation for `edgenetwork_v1.services.edge_network.pagers` module.

## Classes 

### [ListInterconnectAttachmentsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListInterconnectAttachmentsAsyncPager)
    
    
    ListInterconnectAttachmentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgenetwork_v1.types.service.ListInterconnectAttachmentsResponse
            ],
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListInterconnectAttachmentsRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListInterconnectAttachmentsResponse,
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

A pager for iterating through `list_interconnect_attachments` requests.

This class thinly wraps an initial [ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse) object, and provides an `__aiter__` method to iterate through its `interconnect_attachments` field.

If there are more pages, the `__aiter__` method will make additional `ListInterconnectAttachments` requests and continue to iterate through the `interconnect_attachments` field on the corresponding responses.

All the usual [ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInterconnectAttachmentsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListInterconnectAttachmentsPager)
    
    
    ListInterconnectAttachmentsPager(
        method: typing.Callable[
            [...],
            google.cloud.edgenetwork_v1.types.service.ListInterconnectAttachmentsResponse,
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListInterconnectAttachmentsRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListInterconnectAttachmentsResponse,
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

A pager for iterating through `list_interconnect_attachments` requests.

This class thinly wraps an initial [ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse) object, and provides an `__iter__` method to iterate through its `interconnect_attachments` field.

If there are more pages, the `__iter__` method will make additional `ListInterconnectAttachments` requests and continue to iterate through the `interconnect_attachments` field on the corresponding responses.

All the usual [ListInterconnectAttachmentsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectAttachmentsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInterconnectsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListInterconnectsAsyncPager)
    
    
    ListInterconnectsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgenetwork_v1.types.service.ListInterconnectsResponse
            ],
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListInterconnectsRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListInterconnectsResponse,
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

A pager for iterating through `list_interconnects` requests.

This class thinly wraps an initial [ListInterconnectsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectsResponse) object, and provides an `__aiter__` method to iterate through its `interconnects` field.

If there are more pages, the `__aiter__` method will make additional `ListInterconnects` requests and continue to iterate through the `interconnects` field on the corresponding responses.

All the usual [ListInterconnectsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInterconnectsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListInterconnectsPager)
    
    
    ListInterconnectsPager(
        method: typing.Callable[
            [...], google.cloud.edgenetwork_v1.types.service.ListInterconnectsResponse
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListInterconnectsRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListInterconnectsResponse,
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

A pager for iterating through `list_interconnects` requests.

This class thinly wraps an initial [ListInterconnectsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectsResponse) object, and provides an `__iter__` method to iterate through its `interconnects` field.

If there are more pages, the `__iter__` method will make additional `ListInterconnects` requests and continue to iterate through the `interconnects` field on the corresponding responses.

All the usual [ListInterconnectsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListInterconnectsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListNetworksAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListNetworksAsyncPager)
    
    
    ListNetworksAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.edgenetwork_v1.types.service.ListNetworksResponse
            ],
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListNetworksRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListNetworksResponse,
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

A pager for iterating through `list_networks` requests.

This class thinly wraps an initial [ListNetworksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListNetworksResponse) object, and provides an `__aiter__` method to iterate through its `networks` field.

If there are more pages, the `__aiter__` method will make additional `ListNetworks` requests and continue to iterate through the `networks` field on the corresponding responses.

All the usual [ListNetworksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListNetworksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListNetworksPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListNetworksPager)
    
    
    ListNetworksPager(
        method: typing.Callable[
            [...], google.cloud.edgenetwork_v1.types.service.ListNetworksResponse
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListNetworksRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListNetworksResponse,
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

A pager for iterating through `list_networks` requests.

This class thinly wraps an initial [ListNetworksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListNetworksResponse) object, and provides an `__iter__` method to iterate through its `networks` field.

If there are more pages, the `__iter__` method will make additional `ListNetworks` requests and continue to iterate through the `networks` field on the corresponding responses.

All the usual [ListNetworksResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListNetworksResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRoutersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListRoutersAsyncPager)
    
    
    ListRoutersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.edgenetwork_v1.types.service.ListRoutersResponse],
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListRoutersRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListRoutersResponse,
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

A pager for iterating through `list_routers` requests.

This class thinly wraps an initial [ListRoutersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListRoutersResponse) object, and provides an `__aiter__` method to iterate through its `routers` field.

If there are more pages, the `__aiter__` method will make additional `ListRouters` requests and continue to iterate through the `routers` field on the corresponding responses.

All the usual [ListRoutersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListRoutersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRoutersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListRoutersPager)
    
    
    ListRoutersPager(
        method: typing.Callable[
            [...], google.cloud.edgenetwork_v1.types.service.ListRoutersResponse
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListRoutersRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListRoutersResponse,
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

A pager for iterating through `list_routers` requests.

This class thinly wraps an initial [ListRoutersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListRoutersResponse) object, and provides an `__iter__` method to iterate through its `routers` field.

If there are more pages, the `__iter__` method will make additional `ListRouters` requests and continue to iterate through the `routers` field on the corresponding responses.

All the usual [ListRoutersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListRoutersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSubnetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListSubnetsAsyncPager)
    
    
    ListSubnetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.edgenetwork_v1.types.service.ListSubnetsResponse],
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListSubnetsRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListSubnetsResponse,
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

A pager for iterating through `list_subnets` requests.

This class thinly wraps an initial [ListSubnetsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListSubnetsResponse) object, and provides an `__aiter__` method to iterate through its `subnets` field.

If there are more pages, the `__aiter__` method will make additional `ListSubnets` requests and continue to iterate through the `subnets` field on the corresponding responses.

All the usual [ListSubnetsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListSubnetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSubnetsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListSubnetsPager)
    
    
    ListSubnetsPager(
        method: typing.Callable[
            [...], google.cloud.edgenetwork_v1.types.service.ListSubnetsResponse
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListSubnetsRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListSubnetsResponse,
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

A pager for iterating through `list_subnets` requests.

This class thinly wraps an initial [ListSubnetsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListSubnetsResponse) object, and provides an `__iter__` method to iterate through its `subnets` field.

If there are more pages, the `__iter__` method will make additional `ListSubnets` requests and continue to iterate through the `subnets` field on the corresponding responses.

All the usual [ListSubnetsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListSubnetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListZonesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListZonesAsyncPager)
    
    
    ListZonesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.edgenetwork_v1.types.service.ListZonesResponse],
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListZonesRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListZonesResponse,
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

A pager for iterating through `list_zones` requests.

This class thinly wraps an initial [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListZonesResponse) object, and provides an `__aiter__` method to iterate through its `zones` field.

If there are more pages, the `__aiter__` method will make additional `ListZones` requests and continue to iterate through the `zones` field on the corresponding responses.

All the usual [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListZonesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListZonesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.services.edge_network.pagers.ListZonesPager)
    
    
    ListZonesPager(
        method: typing.Callable[
            [...], google.cloud.edgenetwork_v1.types.service.ListZonesResponse
        ],
        request: google.cloud.edgenetwork_v1.types.service.ListZonesRequest,
        response: google.cloud.edgenetwork_v1.types.service.ListZonesResponse,
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

A pager for iterating through `list_zones` requests.

This class thinly wraps an initial [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListZonesResponse) object, and provides an `__iter__` method to iterate through its `zones` field.

If there are more pages, the `__iter__` method will make additional `ListZones` requests and continue to iterate through the `zones` field on the corresponding responses.

All the usual [ListZonesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-edgenetwork/latest/google.cloud.edgenetwork_v1.types.ListZonesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
