---
url: https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.pagers.ListImportJobsAsyncPager
title: Class ListImportJobsAsyncPager (3.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:16:01.848861+00:00
---

# Class ListImportJobsAsyncPager (3.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.services.key_management_service.pagers.ListImportJobsAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListImportJobsAsyncPager (3.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.18.0 (latest)  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.1  3.4.0  3.3.1  3.2.2  3.1.1  3.0.0  2.24.2  2.23.0  2.22.0  2.21.4  2.20.0  2.19.2  2.18.0  2.17.0  2.16.1  2.15.0  2.14.1  2.13.0  2.12.3  2.11.2  2.10.1  2.9.0  2.8.0  2.7.0  2.6.1  2.5.0  2.4.3  2.3.0  2.2.0  2.1.0  2.0.1  1.4.2  1.3.0  1.2.1  1.1.0 
    
    
    ListImportJobsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.kms_v1.types.service.ListImportJobsResponse],
        ],
        request: google.cloud.kms_v1.types.service.ListImportJobsRequest,
        response: google.cloud.kms_v1.types.service.ListImportJobsResponse,
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

A pager for iterating through `list_import_jobs` requests.

This class thinly wraps an initial [ListImportJobsResponse](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ListImportJobsResponse) object, and provides an `__aiter__` method to iterate through its `import_jobs` field.

If there are more pages, the `__aiter__` method will make additional `ListImportJobs` requests and continue to iterate through the `import_jobs` field on the corresponding responses.

All the usual [ListImportJobsResponse](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ListImportJobsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListImportJobsAsyncPager
    
    
    ListImportJobsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.kms_v1.types.service.ListImportJobsResponse],
        ],
        request: google.cloud.kms_v1.types.service.ListImportJobsRequest,
        response: google.cloud.kms_v1.types.service.ListImportJobsResponse,
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
`request` |  `[google.cloud.kms_v1.types.ListImportJobsRequest](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ListImportJobsRequest)`   
The initial request object.  
`response` |  `[google.cloud.kms_v1.types.ListImportJobsResponse](https://docs.cloud.google.com/python/docs/reference/cloudkms/latest/google.cloud.kms_v1.types.ListImportJobsResponse)`   
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
