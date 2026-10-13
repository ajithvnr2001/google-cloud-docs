---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager
title: Class ListPoliciesAsyncPager (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:42.555930+00:00
---

# Class ListPoliciesAsyncPager (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListPoliciesAsyncPager (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 
    
    
    ListPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.iam_v2beta.types.policy.ListPoliciesResponse],
        ],
        request: google.cloud.iam_v2beta.types.policy.ListPoliciesRequest,
        response: google.cloud.iam_v2beta.types.policy.ListPoliciesResponse,
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

A pager for iterating through `list_policies` requests.

This class thinly wraps an initial [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `policies` field.

If there are more pages, the `__aiter__` method will make additional `ListPolicies` requests and continue to iterate through the `policies` field on the corresponding responses.

All the usual [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListPoliciesAsyncPager
    
    
    ListPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.iam_v2beta.types.policy.ListPoliciesResponse],
        ],
        request: google.cloud.iam_v2beta.types.policy.ListPoliciesRequest,
        response: google.cloud.iam_v2beta.types.policy.ListPoliciesResponse,
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
`request` |  `[google.cloud.iam_v2beta.types.ListPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesRequest)`   
The initial request object.  
`response` |  `[google.cloud.iam_v2beta.types.ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse)`   
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
