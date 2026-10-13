---
url: https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager
title: Class ListProjectBillingInfoAsyncPager (1.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:08.630355+00:00
---

# Class ListProjectBillingInfoAsyncPager (1.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListProjectBillingInfoAsyncPager (1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.3  1.15.0  1.14.1  1.13.6  1.12.1  1.11.5  1.10.1  1.9.1  1.8.0  1.7.3  1.6.1  1.5.1  1.4.1  1.3.4  1.2.1  1.1.1  1.0.0  0.1.0 
    
    
    ListProjectBillingInfoAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse
            ],
        ],
        request: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoRequest,
        response: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse,
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

A pager for iterating through `list_project_billing_info` requests.

This class thinly wraps an initial [ListProjectBillingInfoResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListProjectBillingInfoResponse) object, and provides an `__aiter__` method to iterate through its `project_billing_info` field.

If there are more pages, the `__aiter__` method will make additional `ListProjectBillingInfo` requests and continue to iterate through the `project_billing_info` field on the corresponding responses.

All the usual [ListProjectBillingInfoResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListProjectBillingInfoResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListProjectBillingInfoAsyncPager
    
    
    ListProjectBillingInfoAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse
            ],
        ],
        request: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoRequest,
        response: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse,
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
`request` |  `[google.cloud.billing_v1.types.ListProjectBillingInfoRequest](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListProjectBillingInfoRequest)`   
The initial request object.  
`response` |  `[google.cloud.billing_v1.types.ListProjectBillingInfoResponse](https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.types.ListProjectBillingInfoResponse)`   
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
