---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager
title: Class FetchBackupsForResourceTypeAsyncPager (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:33.692948+00:00
---

# Class FetchBackupsForResourceTypeAsyncPager (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.services.backup_dr.pagers.FetchBackupsForResourceTypeAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FetchBackupsForResourceTypeAsyncPager (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    FetchBackupsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
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

A pager for iterating through `fetch_backups_for_resource_type` requests.

This class thinly wraps an initial [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `FetchBackupsForResourceType` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### FetchBackupsForResourceTypeAsyncPager
    
    
    FetchBackupsForResourceTypeAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse
            ],
        ],
        request: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeRequest,
        response: google.cloud.backupdr_v1.types.backupvault.FetchBackupsForResourceTypeResponse,
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
`request` |  `[google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest)`   
The initial request object.  
`response` |  `[google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse)`   
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
