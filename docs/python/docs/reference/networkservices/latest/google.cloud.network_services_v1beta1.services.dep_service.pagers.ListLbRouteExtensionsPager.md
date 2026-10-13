---
url: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListLbRouteExtensionsPager
title: Class ListLbRouteExtensionsPager (0.10.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:15.968782+00:00
---

# Class ListLbRouteExtensionsPager (0.10.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.services.dep_service.pagers.ListLbRouteExtensionsPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListLbRouteExtensionsPager (0.10.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.4 (latest)  0.10.3  0.9.0  0.8.0  0.7.0  0.6.0  0.5.24  0.4.1  0.3.0  0.2.2  0.1.1 
    
    
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

## Methods 

### ListLbRouteExtensionsPager
    
    
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

Instantiate the pager.

**Parameters**  
---  
**Name** | **Description**  
`method` |  `Callable`   
The method that was originally called, and which instantiated this pager.  
`request` |  `[google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsRequest](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsRequest)`   
The initial request object.  
`response` |  `[google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsResponse](https://docs.cloud.google.com/python/docs/reference/networkservices/latest/google.cloud.network_services_v1beta1.types.ListLbRouteExtensionsResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
