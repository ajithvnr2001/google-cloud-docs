---
url: https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.services.cloud_channel_service.pagers.ListSkuGroupsPager
title: Class ListSkuGroupsPager (1.29.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:57.742513+00:00
---

# Class ListSkuGroupsPager (1.29.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.services.cloud_channel_service.pagers.ListSkuGroupsPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListSkuGroupsPager (1.29.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.29.0 (latest)  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.2  1.21.0  1.20.1  1.19.0  1.18.5  1.17.1  1.15.1  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.3  1.8.1  1.7.1  1.6.3  1.5.0  1.4.0  1.3.2  1.2.3  1.1.1  1.0.0  0.3.0  0.2.1  0.1.0 
    
    
    ListSkuGroupsPager(
        method: typing.Callable[
            [...], google.cloud.channel_v1.types.service.ListSkuGroupsResponse
        ],
        request: google.cloud.channel_v1.types.service.ListSkuGroupsRequest,
        response: google.cloud.channel_v1.types.service.ListSkuGroupsResponse,
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

A pager for iterating through `list_sku_groups` requests.

This class thinly wraps an initial [ListSkuGroupsResponse](https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.types.ListSkuGroupsResponse) object, and provides an `__iter__` method to iterate through its `sku_groups` field.

If there are more pages, the `__iter__` method will make additional `ListSkuGroups` requests and continue to iterate through the `sku_groups` field on the corresponding responses.

All the usual [ListSkuGroupsResponse](https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.types.ListSkuGroupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListSkuGroupsPager
    
    
    ListSkuGroupsPager(
        method: typing.Callable[
            [...], google.cloud.channel_v1.types.service.ListSkuGroupsResponse
        ],
        request: google.cloud.channel_v1.types.service.ListSkuGroupsRequest,
        response: google.cloud.channel_v1.types.service.ListSkuGroupsResponse,
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
`request` |  `[google.cloud.channel_v1.types.ListSkuGroupsRequest](https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.types.ListSkuGroupsRequest)`   
The initial request object.  
`response` |  `[google.cloud.channel_v1.types.ListSkuGroupsResponse](https://docs.cloud.google.com/python/docs/reference/cloudchannel/latest/google.cloud.channel_v1.types.ListSkuGroupsResponse)`   
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
