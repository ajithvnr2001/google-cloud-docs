---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers
title: Module pagers (0.4.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:07.541149+00:00
---

# Module pagers (0.4.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.4.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.3 (latest)  0.4.2  0.3.0  0.2.0  0.1.5 

API documentation for `parametermanager_v1.services.parameter_manager.pagers` module.

## Classes 

### [ListParameterVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListParameterVersionsAsyncPager)
    
    
    ListParameterVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.parametermanager_v1.types.service.ListParameterVersionsResponse
            ],
        ],
        request: google.cloud.parametermanager_v1.types.service.ListParameterVersionsRequest,
        response: google.cloud.parametermanager_v1.types.service.ListParameterVersionsResponse,
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

A pager for iterating through `list_parameter_versions` requests.

This class thinly wraps an initial [ListParameterVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParameterVersionsResponse) object, and provides an `__aiter__` method to iterate through its `parameter_versions` field.

If there are more pages, the `__aiter__` method will make additional `ListParameterVersions` requests and continue to iterate through the `parameter_versions` field on the corresponding responses.

All the usual [ListParameterVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParameterVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListParameterVersionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListParameterVersionsPager)
    
    
    ListParameterVersionsPager(
        method: typing.Callable[
            [...],
            google.cloud.parametermanager_v1.types.service.ListParameterVersionsResponse,
        ],
        request: google.cloud.parametermanager_v1.types.service.ListParameterVersionsRequest,
        response: google.cloud.parametermanager_v1.types.service.ListParameterVersionsResponse,
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

A pager for iterating through `list_parameter_versions` requests.

This class thinly wraps an initial [ListParameterVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParameterVersionsResponse) object, and provides an `__iter__` method to iterate through its `parameter_versions` field.

If there are more pages, the `__iter__` method will make additional `ListParameterVersions` requests and continue to iterate through the `parameter_versions` field on the corresponding responses.

All the usual [ListParameterVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParameterVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListParametersAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListParametersAsyncPager)
    
    
    ListParametersAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.parametermanager_v1.types.service.ListParametersResponse
            ],
        ],
        request: google.cloud.parametermanager_v1.types.service.ListParametersRequest,
        response: google.cloud.parametermanager_v1.types.service.ListParametersResponse,
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

A pager for iterating through `list_parameters` requests.

This class thinly wraps an initial [ListParametersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParametersResponse) object, and provides an `__aiter__` method to iterate through its `parameters` field.

If there are more pages, the `__aiter__` method will make additional `ListParameters` requests and continue to iterate through the `parameters` field on the corresponding responses.

All the usual [ListParametersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParametersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListParametersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListParametersPager)
    
    
    ListParametersPager(
        method: typing.Callable[
            [...], google.cloud.parametermanager_v1.types.service.ListParametersResponse
        ],
        request: google.cloud.parametermanager_v1.types.service.ListParametersRequest,
        response: google.cloud.parametermanager_v1.types.service.ListParametersResponse,
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

A pager for iterating through `list_parameters` requests.

This class thinly wraps an initial [ListParametersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParametersResponse) object, and provides an `__iter__` method to iterate through its `parameters` field.

If there are more pages, the `__iter__` method will make additional `ListParameters` requests and continue to iterate through the `parameters` field on the corresponding responses.

All the usual [ListParametersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListParametersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplateVersionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListTemplateVersionsAsyncPager)
    
    
    ListTemplateVersionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.parametermanager_v1.types.service.ListTemplateVersionsResponse
            ],
        ],
        request: google.cloud.parametermanager_v1.types.service.ListTemplateVersionsRequest,
        response: google.cloud.parametermanager_v1.types.service.ListTemplateVersionsResponse,
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

A pager for iterating through `list_template_versions` requests.

This class thinly wraps an initial [ListTemplateVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplateVersionsResponse) object, and provides an `__aiter__` method to iterate through its `template_versions` field.

If there are more pages, the `__aiter__` method will make additional `ListTemplateVersions` requests and continue to iterate through the `template_versions` field on the corresponding responses.

All the usual [ListTemplateVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplateVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplateVersionsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListTemplateVersionsPager)
    
    
    ListTemplateVersionsPager(
        method: typing.Callable[
            [...],
            google.cloud.parametermanager_v1.types.service.ListTemplateVersionsResponse,
        ],
        request: google.cloud.parametermanager_v1.types.service.ListTemplateVersionsRequest,
        response: google.cloud.parametermanager_v1.types.service.ListTemplateVersionsResponse,
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

A pager for iterating through `list_template_versions` requests.

This class thinly wraps an initial [ListTemplateVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplateVersionsResponse) object, and provides an `__iter__` method to iterate through its `template_versions` field.

If there are more pages, the `__iter__` method will make additional `ListTemplateVersions` requests and continue to iterate through the `template_versions` field on the corresponding responses.

All the usual [ListTemplateVersionsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplateVersionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplatesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListTemplatesAsyncPager)
    
    
    ListTemplatesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.parametermanager_v1.types.service.ListTemplatesResponse
            ],
        ],
        request: google.cloud.parametermanager_v1.types.service.ListTemplatesRequest,
        response: google.cloud.parametermanager_v1.types.service.ListTemplatesResponse,
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

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplatesResponse) object, and provides an `__aiter__` method to iterate through its `templates` field.

If there are more pages, the `__aiter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTemplatesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.services.parameter_manager.pagers.ListTemplatesPager)
    
    
    ListTemplatesPager(
        method: typing.Callable[
            [...], google.cloud.parametermanager_v1.types.service.ListTemplatesResponse
        ],
        request: google.cloud.parametermanager_v1.types.service.ListTemplatesRequest,
        response: google.cloud.parametermanager_v1.types.service.ListTemplatesResponse,
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

This class thinly wraps an initial [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplatesResponse) object, and provides an `__iter__` method to iterate through its `templates` field.

If there are more pages, the `__iter__` method will make additional `ListTemplates` requests and continue to iterate through the `templates` field on the corresponding responses.

All the usual [ListTemplatesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-parametermanager/latest/google.cloud.parametermanager_v1.types.ListTemplatesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
