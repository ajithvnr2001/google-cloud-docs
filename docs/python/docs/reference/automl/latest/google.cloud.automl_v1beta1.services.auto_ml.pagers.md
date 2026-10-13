---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers
title: Module pagers (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:37.937210+00:00
---

# Module pagers (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 

API documentation for `automl_v1beta1.services.auto_ml.pagers` module.

## Classes 

### [ListColumnSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager)
    
    
    ListColumnSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse,
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

A pager for iterating through `list_column_specs` requests.

This class thinly wraps an initial [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) object, and provides an `__aiter__` method to iterate through its `column_specs` field.

If there are more pages, the `__aiter__` method will make additional `ListColumnSpecs` requests and continue to iterate through the `column_specs` field on the corresponding responses.

All the usual [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListColumnSpecsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsPager)
    
    
    ListColumnSpecsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListColumnSpecsResponse,
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

A pager for iterating through `list_column_specs` requests.

This class thinly wraps an initial [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) object, and provides an `__iter__` method to iterate through its `column_specs` field.

If there are more pages, the `__iter__` method will make additional `ListColumnSpecs` requests and continue to iterate through the `column_specs` field on the corresponding responses.

All the usual [ListColumnSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatasetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager)
    
    
    ListDatasetsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListDatasetsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListDatasetsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListDatasetsResponse,
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

A pager for iterating through `list_datasets` requests.

This class thinly wraps an initial [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) object, and provides an `__aiter__` method to iterate through its `datasets` field.

If there are more pages, the `__aiter__` method will make additional `ListDatasets` requests and continue to iterate through the `datasets` field on the corresponding responses.

All the usual [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatasetsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsPager)
    
    
    ListDatasetsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListDatasetsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListDatasetsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListDatasetsResponse,
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

A pager for iterating through `list_datasets` requests.

This class thinly wraps an initial [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) object, and provides an `__iter__` method to iterate through its `datasets` field.

If there are more pages, the `__iter__` method will make additional `ListDatasets` requests and continue to iterate through the `datasets` field on the corresponding responses.

All the usual [ListDatasetsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager)
    
    
    ListModelEvaluationsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse,
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

A pager for iterating through `list_model_evaluations` requests.

This class thinly wraps an initial [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) object, and provides an `__aiter__` method to iterate through its `model_evaluation` field.

If there are more pages, the `__aiter__` method will make additional `ListModelEvaluations` requests and continue to iterate through the `model_evaluation` field on the corresponding responses.

All the usual [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelEvaluationsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsPager)
    
    
    ListModelEvaluationsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelEvaluationsResponse,
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

A pager for iterating through `list_model_evaluations` requests.

This class thinly wraps an initial [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) object, and provides an `__iter__` method to iterate through its `model_evaluation` field.

If there are more pages, the `__iter__` method will make additional `ListModelEvaluations` requests and continue to iterate through the `model_evaluation` field on the corresponding responses.

All the usual [ListModelEvaluationsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager)
    
    
    ListModelsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.automl_v1beta1.types.service.ListModelsResponse],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelsResponse,
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

A pager for iterating through `list_models` requests.

This class thinly wraps an initial [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) object, and provides an `__aiter__` method to iterate through its `model` field.

If there are more pages, the `__aiter__` method will make additional `ListModels` requests and continue to iterate through the `model` field on the corresponding responses.

All the usual [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListModelsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsPager)
    
    
    ListModelsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListModelsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListModelsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListModelsResponse,
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

A pager for iterating through `list_models` requests.

This class thinly wraps an initial [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) object, and provides an `__iter__` method to iterate through its `model` field.

If there are more pages, the `__iter__` method will make additional `ListModels` requests and continue to iterate through the `model` field on the corresponding responses.

All the usual [ListModelsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTableSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager)
    
    
    ListTableSpecsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse
            ],
        ],
        request: google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse,
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

A pager for iterating through `list_table_specs` requests.

This class thinly wraps an initial [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) object, and provides an `__aiter__` method to iterate through its `table_specs` field.

If there are more pages, the `__aiter__` method will make additional `ListTableSpecs` requests and continue to iterate through the `table_specs` field on the corresponding responses.

All the usual [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListTableSpecsPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsPager)
    
    
    ListTableSpecsPager(
        method: typing.Callable[
            [...], google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse
        ],
        request: google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest,
        response: google.cloud.automl_v1beta1.types.service.ListTableSpecsResponse,
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

A pager for iterating through `list_table_specs` requests.

This class thinly wraps an initial [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) object, and provides an `__iter__` method to iterate through its `table_specs` field.

If there are more pages, the `__iter__` method will make additional `ListTableSpecs` requests and continue to iterate through the `table_specs` field on the corresponding responses.

All the usual [ListTableSpecsResponse](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
