---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers
title: Module pagers (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:08.848968+00:00
---

# Module pagers (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 

API documentation for `talent_v4.services.company_service.pagers` module.

## Classes 

### [ListCompaniesAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager)
    
    
    ListCompaniesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4.types.company_service.ListCompaniesResponse
            ],
        ],
        request: google.cloud.talent_v4.types.company_service.ListCompaniesRequest,
        response: google.cloud.talent_v4.types.company_service.ListCompaniesResponse,
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

A pager for iterating through `list_companies` requests.

This class thinly wraps an initial [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) object, and provides an `__aiter__` method to iterate through its `companies` field.

If there are more pages, the `__aiter__` method will make additional `ListCompanies` requests and continue to iterate through the `companies` field on the corresponding responses.

All the usual [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListCompaniesPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesPager)
    
    
    ListCompaniesPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4.types.company_service.ListCompaniesResponse
        ],
        request: google.cloud.talent_v4.types.company_service.ListCompaniesRequest,
        response: google.cloud.talent_v4.types.company_service.ListCompaniesResponse,
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

A pager for iterating through `list_companies` requests.

This class thinly wraps an initial [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) object, and provides an `__iter__` method to iterate through its `companies` field.

If there are more pages, the `__iter__` method will make additional `ListCompanies` requests and continue to iterate through the `companies` field on the corresponding responses.

All the usual [ListCompaniesResponse](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
