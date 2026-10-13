---
url: https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.services.web_security_scanner.pagers.ListFindingsAsyncPager
title: Class ListFindingsAsyncPager (1.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:57.863457+00:00
---

# Class ListFindingsAsyncPager (1.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.services.web_security_scanner.pagers.ListFindingsAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListFindingsAsyncPager (1.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.22.0 (latest)  1.21.0  1.20.0  1.19.0  1.18.0  1.17.2  1.16.0  1.15.1  1.14.5  1.13.0  1.12.2  1.11.1  1.10.0  1.9.2  1.8.3  1.7.2  1.6.1  1.5.0  1.4.3  1.3.0  1.2.0  1.1.0  1.0.0  0.4.2  0.3.0 
    
    
    ListFindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.websecurityscanner_v1alpha.types.web_security_scanner.ListFindingsResponse
            ],
        ],
        request: google.cloud.websecurityscanner_v1alpha.types.web_security_scanner.ListFindingsRequest,
        response: google.cloud.websecurityscanner_v1alpha.types.web_security_scanner.ListFindingsResponse,
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

A pager for iterating through `list_findings` requests.

This class thinly wraps an initial [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ListFindingsResponse) object, and provides an `__aiter__` method to iterate through its `findings` field.

If there are more pages, the `__aiter__` method will make additional `ListFindings` requests and continue to iterate through the `findings` field on the corresponding responses.

All the usual [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ListFindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListFindingsAsyncPager
    
    
    ListFindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.websecurityscanner_v1alpha.types.web_security_scanner.ListFindingsResponse
            ],
        ],
        request: google.cloud.websecurityscanner_v1alpha.types.web_security_scanner.ListFindingsRequest,
        response: google.cloud.websecurityscanner_v1alpha.types.web_security_scanner.ListFindingsResponse,
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
`request` |  `[google.cloud.websecurityscanner_v1alpha.types.ListFindingsRequest](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ListFindingsRequest)`   
The initial request object.  
`response` |  `[google.cloud.websecurityscanner_v1alpha.types.ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/websecurityscanner/latest/google.cloud.websecurityscanner_v1alpha.types.ListFindingsResponse)`   
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
