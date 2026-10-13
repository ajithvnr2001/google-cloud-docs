---
url: https://docs.cloud.google.com/python/docs/reference/iap/latest/google.cloud.iap_v1.services.identity_aware_proxy_admin_service.pagers.ListTunnelDestGroupsAsyncPager
title: Class ListTunnelDestGroupsAsyncPager (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:02.149575+00:00
---

# Class ListTunnelDestGroupsAsyncPager (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iap/latest/google.cloud.iap_v1.services.identity_aware_proxy_admin_service.pagers.ListTunnelDestGroupsAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListTunnelDestGroupsAsyncPager (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.1  1.16.1  1.15.0  1.14.1  1.13.5  1.12.0  1.10.3  1.9.0  1.8.1  1.7.0  1.6.0  1.5.4  1.4.1  1.3.1  1.2.1  1.1.0  1.0.2  0.1.2 
    
    
    ListTunnelDestGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iap_v1.types.service.ListTunnelDestGroupsResponse
            ],
        ],
        request: google.cloud.iap_v1.types.service.ListTunnelDestGroupsRequest,
        response: google.cloud.iap_v1.types.service.ListTunnelDestGroupsResponse,
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

A pager for iterating through `list_tunnel_dest_groups` requests.

This class thinly wraps an initial [ListTunnelDestGroupsResponse](https://docs.cloud.google.com/python/docs/reference/iap/latest/google.cloud.iap_v1.types.ListTunnelDestGroupsResponse) object, and provides an `__aiter__` method to iterate through its `tunnel_dest_groups` field.

If there are more pages, the `__aiter__` method will make additional `ListTunnelDestGroups` requests and continue to iterate through the `tunnel_dest_groups` field on the corresponding responses.

All the usual [ListTunnelDestGroupsResponse](https://docs.cloud.google.com/python/docs/reference/iap/latest/google.cloud.iap_v1.types.ListTunnelDestGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListTunnelDestGroupsAsyncPager
    
    
    ListTunnelDestGroupsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iap_v1.types.service.ListTunnelDestGroupsResponse
            ],
        ],
        request: google.cloud.iap_v1.types.service.ListTunnelDestGroupsRequest,
        response: google.cloud.iap_v1.types.service.ListTunnelDestGroupsResponse,
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

Instantiates the pager.

**Parameters**  
---  
**Name** | **Description**  
`method` |  `Callable`   
The method that was originally called, and which instantiated this pager.  
`request` |  `[google.cloud.iap_v1.types.ListTunnelDestGroupsRequest](https://docs.cloud.google.com/python/docs/reference/iap/latest/google.cloud.iap_v1.types.ListTunnelDestGroupsRequest)`   
The initial request object.  
`response` |  `[google.cloud.iap_v1.types.ListTunnelDestGroupsResponse](https://docs.cloud.google.com/python/docs/reference/iap/latest/google.cloud.iap_v1.types.ListTunnelDestGroupsResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
