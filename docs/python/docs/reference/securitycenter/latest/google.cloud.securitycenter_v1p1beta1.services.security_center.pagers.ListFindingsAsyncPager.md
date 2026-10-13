---
url: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1p1beta1.services.security_center.pagers.ListFindingsAsyncPager
title: Class ListFindingsAsyncPager (1.47.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:14.295701+00:00
---

# Class ListFindingsAsyncPager (1.47.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1p1beta1.services.security_center.pagers.ListFindingsAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListFindingsAsyncPager (1.47.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.47.0 (latest)  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.1  1.33.1  1.32.1  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.1  1.25.0  1.24.1  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.2  1.17.0  1.16.2  1.15.0  1.14.0  1.13.0  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.2  1.4.0  1.3.1  1.2.0  1.1.0  1.0.0  0.7.3  0.6.0  0.5.0  0.4.0  0.3.0 
    
    
    ListFindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v1p1beta1.types.securitycenter_service.ListFindingsResponse
            ],
        ],
        request: google.cloud.securitycenter_v1p1beta1.types.securitycenter_service.ListFindingsRequest,
        response: google.cloud.securitycenter_v1p1beta1.types.securitycenter_service.ListFindingsResponse,
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

This class thinly wraps an initial [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse) object, and provides an `__aiter__` method to iterate through its `list_findings_results` field.

If there are more pages, the `__aiter__` method will make additional `ListFindings` requests and continue to iterate through the `list_findings_results` field on the corresponding responses.

All the usual [ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListFindingsAsyncPager
    
    
    ListFindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.securitycenter_v1p1beta1.types.securitycenter_service.ListFindingsResponse
            ],
        ],
        request: google.cloud.securitycenter_v1p1beta1.types.securitycenter_service.ListFindingsRequest,
        response: google.cloud.securitycenter_v1p1beta1.types.securitycenter_service.ListFindingsResponse,
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
`request` |  `[google.cloud.securitycenter_v1p1beta1.types.ListFindingsRequest](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1p1beta1.types.ListFindingsRequest)`   
The initial request object.  
`response` |  `[google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse](https://docs.cloud.google.com/python/docs/reference/securitycenter/latest/google.cloud.securitycenter_v1p1beta1.types.ListFindingsResponse)`   
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
