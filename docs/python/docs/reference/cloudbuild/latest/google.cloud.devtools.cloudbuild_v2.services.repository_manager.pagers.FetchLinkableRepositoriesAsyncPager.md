---
url: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesAsyncPager
title: Class FetchLinkableRepositoriesAsyncPager (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:08.284739+00:00
---

# Class FetchLinkableRepositoriesAsyncPager (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.services.repository_manager.pagers.FetchLinkableRepositoriesAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FetchLinkableRepositoriesAsyncPager (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.1  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.3  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.2  3.23.3  3.22.0  3.21.0  3.20.1  3.19.0  3.18.0  3.17.1  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.1  3.10.0  3.9.3  3.8.3  3.7.1  3.6.0  3.5.2  3.4.0  3.3.2  3.2.1  3.1.1  3.0.2  2.0.2  1.1.2  1.0.0  0.1.0 
    
    
    FetchLinkableRepositoriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.devtools.cloudbuild_v2.types.repositories.FetchLinkableRepositoriesResponse
            ],
        ],
        request: google.cloud.devtools.cloudbuild_v2.types.repositories.FetchLinkableRepositoriesRequest,
        response: google.cloud.devtools.cloudbuild_v2.types.repositories.FetchLinkableRepositoriesResponse,
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

A pager for iterating through `fetch_linkable_repositories` requests.

This class thinly wraps an initial [FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse) object, and provides an `__aiter__` method to iterate through its `repositories` field.

If there are more pages, the `__aiter__` method will make additional `FetchLinkableRepositories` requests and continue to iterate through the `repositories` field on the corresponding responses.

All the usual [FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### FetchLinkableRepositoriesAsyncPager
    
    
    FetchLinkableRepositoriesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.devtools.cloudbuild_v2.types.repositories.FetchLinkableRepositoriesResponse
            ],
        ],
        request: google.cloud.devtools.cloudbuild_v2.types.repositories.FetchLinkableRepositoriesRequest,
        response: google.cloud.devtools.cloudbuild_v2.types.repositories.FetchLinkableRepositoriesResponse,
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
`request` |  `[google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesRequest](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesRequest)`   
The initial request object.  
`response` |  `[google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudbuild/latest/google.cloud.devtools.cloudbuild_v2.types.FetchLinkableRepositoriesResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
