---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesPager
title: Class ListTargetSitesPager (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:00:29.086753+00:00
---

# Class ListTargetSitesPager (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.site_search_engine_service.pagers.ListTargetSitesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListTargetSitesPager (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    ListTargetSitesPager(
        method: typing.Callable[
            [...],
            google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesResponse,
        ],
        request: google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesRequest,
        response: google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesResponse,
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

A pager for iterating through `list_target_sites` requests.

This class thinly wraps an initial [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse) object, and provides an `__iter__` method to iterate through its `target_sites` field.

If there are more pages, the `__iter__` method will make additional `ListTargetSites` requests and continue to iterate through the `target_sites` field on the corresponding responses.

All the usual [ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListTargetSitesPager
    
    
    ListTargetSitesPager(
        method: typing.Callable[
            [...],
            google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesResponse,
        ],
        request: google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesRequest,
        response: google.cloud.discoveryengine_v1.types.site_search_engine_service.ListTargetSitesResponse,
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
`request` |  `[google.cloud.discoveryengine_v1.types.ListTargetSitesRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesRequest)`   
The initial request object.  
`response` |  `[google.cloud.discoveryengine_v1.types.ListTargetSitesResponse](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ListTargetSitesResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
