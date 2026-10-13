---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager
title: Class SearchAllResourcesPager (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:39.723928+00:00
---

# Class SearchAllResourcesPager (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SearchAllResourcesPager (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 
    
    
    SearchAllResourcesPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
        ],
        request: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
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

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### SearchAllResourcesPager
    
    
    SearchAllResourcesPager(
        method: typing.Callable[
            [...],
            google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
        ],
        request: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesRequest,
        response: google.cloud.asset_v1p1beta1.types.asset_service.SearchAllResourcesResponse,
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
`request` |  `[google.cloud.asset_v1p1beta1.types.SearchAllResourcesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesRequest)`   
The initial request object.  
`response` |  `[google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
