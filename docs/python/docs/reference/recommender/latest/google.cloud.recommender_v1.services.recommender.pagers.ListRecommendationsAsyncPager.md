---
url: https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.services.recommender.pagers.ListRecommendationsAsyncPager
title: Class ListRecommendationsAsyncPager (2.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:14.931082+00:00
---

# Class ListRecommendationsAsyncPager (2.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.services.recommender.pagers.ListRecommendationsAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListRecommendationsAsyncPager (2.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.23.0 (latest)  2.22.0  2.21.0  2.20.0  2.19.0  2.18.2  2.17.0  2.16.1  2.15.5  2.14.0  2.13.0  2.12.0  2.11.2  2.10.1  2.9.0  2.8.3  2.7.4  2.6.0  2.5.1  2.4.0  2.3.4  2.2.0  2.1.0  2.0.0  1.1.3  1.0.0  0.3.0  0.2.0  0.1.0 
    
    
    ListRecommendationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recommender_v1.types.recommender_service.ListRecommendationsResponse
            ],
        ],
        request: google.cloud.recommender_v1.types.recommender_service.ListRecommendationsRequest,
        response: google.cloud.recommender_v1.types.recommender_service.ListRecommendationsResponse,
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

A pager for iterating through `list_recommendations` requests.

This class thinly wraps an initial [ListRecommendationsResponse](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.ListRecommendationsResponse) object, and provides an `__aiter__` method to iterate through its `recommendations` field.

If there are more pages, the `__aiter__` method will make additional `ListRecommendations` requests and continue to iterate through the `recommendations` field on the corresponding responses.

All the usual [ListRecommendationsResponse](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.ListRecommendationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListRecommendationsAsyncPager
    
    
    ListRecommendationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.recommender_v1.types.recommender_service.ListRecommendationsResponse
            ],
        ],
        request: google.cloud.recommender_v1.types.recommender_service.ListRecommendationsRequest,
        response: google.cloud.recommender_v1.types.recommender_service.ListRecommendationsResponse,
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
`request` |  `[google.cloud.recommender_v1.types.ListRecommendationsRequest](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.ListRecommendationsRequest)`   
The initial request object.  
`response` |  `[google.cloud.recommender_v1.types.ListRecommendationsResponse](https://docs.cloud.google.com/python/docs/reference/recommender/latest/google.cloud.recommender_v1.types.ListRecommendationsResponse)`   
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
