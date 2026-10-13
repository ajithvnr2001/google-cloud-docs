---
url: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.services.translation_service.pagers.ListGlossariesPager
title: Class ListGlossariesPager (3.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:23.160985+00:00
---

# Class ListGlossariesPager (3.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.services.translation_service.pagers.ListGlossariesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListGlossariesPager (3.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.28.0 (latest)  3.27.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.1  3.20.3  3.19.0  3.18.0  3.17.0  3.15.5  3.14.0  3.13.0  3.12.1  3.11.3  3.10.1  3.9.0  3.8.4  3.7.4  3.6.1  3.5.0  3.4.1  3.3.2  3.2.1  3.1.0  3.0.2  2.0.4  1.7.2  1.6.0 
    
    
    ListGlossariesPager(
        method: typing.Callable[
            [...],
            google.cloud.translate_v3beta1.types.translation_service.ListGlossariesResponse,
        ],
        request: google.cloud.translate_v3beta1.types.translation_service.ListGlossariesRequest,
        response: google.cloud.translate_v3beta1.types.translation_service.ListGlossariesResponse,
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

A pager for iterating through `list_glossaries` requests.

This class thinly wraps an initial [ListGlossariesResponse](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.ListGlossariesResponse) object, and provides an `__iter__` method to iterate through its `glossaries` field.

If there are more pages, the `__iter__` method will make additional `ListGlossaries` requests and continue to iterate through the `glossaries` field on the corresponding responses.

All the usual [ListGlossariesResponse](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.ListGlossariesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListGlossariesPager
    
    
    ListGlossariesPager(
        method: typing.Callable[
            [...],
            google.cloud.translate_v3beta1.types.translation_service.ListGlossariesResponse,
        ],
        request: google.cloud.translate_v3beta1.types.translation_service.ListGlossariesRequest,
        response: google.cloud.translate_v3beta1.types.translation_service.ListGlossariesResponse,
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
`request` |  `[google.cloud.translate_v3beta1.types.ListGlossariesRequest](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.ListGlossariesRequest)`   
The initial request object.  
`response` |  `[google.cloud.translate_v3beta1.types.ListGlossariesResponse](https://docs.cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v3beta1.types.ListGlossariesResponse)`   
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
