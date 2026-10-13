---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListAutonomousDbVersionsAsyncPager
title: Class ListAutonomousDbVersionsAsyncPager (0.6.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:31.384293+00:00
---

# Class ListAutonomousDbVersionsAsyncPager (0.6.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.services.oracle_database.pagers.ListAutonomousDbVersionsAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListAutonomousDbVersionsAsyncPager (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    ListAutonomousDbVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.oracledatabase_v1.types.oracledatabase.ListAutonomousDbVersionsResponse
            ],
        ],
        request: google.cloud.oracledatabase_v1.types.oracledatabase.ListAutonomousDbVersionsRequest,
        response: google.cloud.oracledatabase_v1.types.oracledatabase.ListAutonomousDbVersionsResponse,
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

A pager for iterating through `list_autonomous_db_versions` requests.

This class thinly wraps an initial [ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse) object, and provides an `__aiter__` method to iterate through its `autonomous_db_versions` field.

If there are more pages, the `__aiter__` method will make additional `ListAutonomousDbVersions` requests and continue to iterate through the `autonomous_db_versions` field on the corresponding responses.

All the usual [ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListAutonomousDbVersionsAsyncPager
    
    
    ListAutonomousDbVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.oracledatabase_v1.types.oracledatabase.ListAutonomousDbVersionsResponse
            ],
        ],
        request: google.cloud.oracledatabase_v1.types.oracledatabase.ListAutonomousDbVersionsRequest,
        response: google.cloud.oracledatabase_v1.types.oracledatabase.ListAutonomousDbVersionsResponse,
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
`request` |  `[google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsRequest)`   
The initial request object.  
`response` |  `[google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-oracledatabase/latest/google.cloud.oracledatabase_v1.types.ListAutonomousDbVersionsResponse)`   
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
