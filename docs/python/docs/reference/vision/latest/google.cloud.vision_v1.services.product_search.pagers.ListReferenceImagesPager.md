---
url: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.pagers.ListReferenceImagesPager
title: Class ListReferenceImagesPager (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:51.114345+00:00
---

# Class ListReferenceImagesPager (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.pagers.ListReferenceImagesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListReferenceImagesPager (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.1  3.11.0  3.10.2  3.9.0  3.8.1  3.7.4  3.6.0  3.5.0  3.4.5  3.3.1  3.2.0  3.1.4  3.0.0  2.8.0  2.7.3  2.6.3  2.5.0  2.4.4  2.3.2  2.2.0  2.1.0  2.0.0  1.0.2  0.42.0  0.41.0  0.40.0  0.39.0  0.38.1 
    
    
    ListReferenceImagesPager(
        method: typing.Callable[
            [...],
            google.cloud.vision_v1.types.product_search_service.ListReferenceImagesResponse,
        ],
        request: google.cloud.vision_v1.types.product_search_service.ListReferenceImagesRequest,
        response: google.cloud.vision_v1.types.product_search_service.ListReferenceImagesResponse,
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

A pager for iterating through `list_reference_images` requests.

This class thinly wraps an initial [ListReferenceImagesResponse](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ListReferenceImagesResponse) object, and provides an `__iter__` method to iterate through its `reference_images` field.

If there are more pages, the `__iter__` method will make additional `ListReferenceImages` requests and continue to iterate through the `reference_images` field on the corresponding responses.

All the usual [ListReferenceImagesResponse](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ListReferenceImagesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListReferenceImagesPager
    
    
    ListReferenceImagesPager(
        method: typing.Callable[
            [...],
            google.cloud.vision_v1.types.product_search_service.ListReferenceImagesResponse,
        ],
        request: google.cloud.vision_v1.types.product_search_service.ListReferenceImagesRequest,
        response: google.cloud.vision_v1.types.product_search_service.ListReferenceImagesResponse,
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
`request` |  `[google.cloud.vision_v1.types.ListReferenceImagesRequest](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ListReferenceImagesRequest)`   
The initial request object.  
`response` |  `[google.cloud.vision_v1.types.ListReferenceImagesResponse](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ListReferenceImagesResponse)`   
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
