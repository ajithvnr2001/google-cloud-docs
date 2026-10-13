---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers
title: Module pagers (0.7.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:06.108488+00:00
---

# Module pagers (0.7.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.2 (latest)  0.7.1  0.6.0  0.5.0  0.4.0  0.3.0  0.2.8  0.1.1 

API documentation for `modelarmor_v1beta.services.model_armor.pagers` module.

## Classes 

### [ListTemplatesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesAsyncPager)
    
    
    ListTemplatesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse
            ],
        ],
        request: google.cloud.modelarmor_v1beta.types.service.ListTemplatesRequest,
        response: google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse,
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

A pager for iterating through `list_templates` requests.

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) object, and provides an `__aiter__` method to iterate through its `templates` field.

If there are more pages, the `__aiter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplatesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.services.model_armor.pagers.ListTemplatesPager)
    
    
    ListTemplatesPager(
        method: typing.Callable[
            [...], google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse
        ],
        request: google.cloud.modelarmor_v1beta.types.service.ListTemplatesRequest,
        response: google.cloud.modelarmor_v1beta.types.service.ListTemplatesResponse,
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

A pager for iterating through `list_templates` requests.

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) object, and provides an `__iter__` method to iterate through its `templates` field.

If there are more pages, the `__iter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-modelarmor/latest/google.cloud.modelarmor_v1beta.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
