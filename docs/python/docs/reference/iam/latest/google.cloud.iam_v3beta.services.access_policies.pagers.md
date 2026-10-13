---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers
title: Module pagers (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:59.076210+00:00
---

# Module pagers (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 

API documentation for `iam_v3beta.services.access_policies.pagers` module.

## Classes 

### [ListAccessPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesAsyncPager)
    
    
    ListAccessPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse,
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

A pager for iterating through `list_access_policies` requests.

This class thinly wraps an initial [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `access_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListAccessPolicies` requests and continue to iterate through the `access_policies` field on the corresponding responses.

All the usual [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccessPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesPager)
    
    
    ListAccessPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse,
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse,
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

A pager for iterating through `list_access_policies` requests.

This class thinly wraps an initial [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) object, and provides an `__iter__` method to iterate through its `access_policies` field.

If there are more pages, the `__iter__` method will make additional `ListAccessPolicies` requests and continue to iterate through the `access_policies` field on the corresponding responses.

All the usual [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAccessPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager)
    
    
    SearchAccessPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse,
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

A pager for iterating through `search_access_policy_bindings` requests.

This class thinly wraps an initial [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchAccessPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAccessPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsPager)
    
    
    SearchAccessPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse,
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

A pager for iterating through `search_access_policy_bindings` requests.

This class thinly wraps an initial [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchAccessPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
