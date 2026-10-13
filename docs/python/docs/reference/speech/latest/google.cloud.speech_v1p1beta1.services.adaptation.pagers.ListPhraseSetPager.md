---
url: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.adaptation.pagers.ListPhraseSetPager
title: Class ListPhraseSetPager (2.41.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:44.211758+00:00
---

# Class ListPhraseSetPager (2.41.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.services.adaptation.pagers.ListPhraseSetPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListPhraseSetPager (2.41.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.41.0 (latest)  2.40.0  2.39.0  2.38.0  2.37.0  2.36.1  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.1  2.25.1  2.24.1  2.23.0  2.22.0  2.21.1  2.20.1  2.19.0  2.18.0  2.17.3  2.16.2  2.15.1  2.14.1  2.13.1  2.12.0  2.11.1  2.10.0  2.9.3  2.8.0  2.7.0  2.6.0  2.5.1  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.4  1.2.0  1.1.0 
    
    
    ListPhraseSetPager(
        method: typing.Callable[
            [...],
            google.cloud.speech_v1p1beta1.types.cloud_speech_adaptation.ListPhraseSetResponse,
        ],
        request: google.cloud.speech_v1p1beta1.types.cloud_speech_adaptation.ListPhraseSetRequest,
        response: google.cloud.speech_v1p1beta1.types.cloud_speech_adaptation.ListPhraseSetResponse,
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

A pager for iterating through `list_phrase_set` requests.

This class thinly wraps an initial [ListPhraseSetResponse](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse) object, and provides an `__iter__` method to iterate through its `phrase_sets` field.

If there are more pages, the `__iter__` method will make additional `ListPhraseSet` requests and continue to iterate through the `phrase_sets` field on the corresponding responses.

All the usual [ListPhraseSetResponse](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListPhraseSetPager
    
    
    ListPhraseSetPager(
        method: typing.Callable[
            [...],
            google.cloud.speech_v1p1beta1.types.cloud_speech_adaptation.ListPhraseSetResponse,
        ],
        request: google.cloud.speech_v1p1beta1.types.cloud_speech_adaptation.ListPhraseSetRequest,
        response: google.cloud.speech_v1p1beta1.types.cloud_speech_adaptation.ListPhraseSetResponse,
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
`request` |  `[google.cloud.speech_v1p1beta1.types.ListPhraseSetRequest](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.ListPhraseSetRequest)`   
The initial request object.  
`response` |  `[google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1p1beta1.types.ListPhraseSetResponse)`   
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
