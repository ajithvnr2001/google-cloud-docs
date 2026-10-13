---
url: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.services.tpu.pagers.ListAcceleratorTypesPager
title: Class ListAcceleratorTypesPager (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:24.791779+00:00
---

# Class ListAcceleratorTypesPager (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.services.tpu.pagers.ListAcceleratorTypesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListAcceleratorTypesPager (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.2  1.22.0  1.21.0  1.20.0  1.19.1  1.18.5  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.2  1.10.1  1.9.0  1.8.0  1.7.2  1.6.0  1.5.2  1.4.1  1.3.4  1.2.1  1.1.0  1.0.2  0.2.2  0.1.0 
    
    
    ListAcceleratorTypesPager(
        method: typing.Callable[
            [...], google.cloud.tpu_v2.types.cloud_tpu.ListAcceleratorTypesResponse
        ],
        request: google.cloud.tpu_v2.types.cloud_tpu.ListAcceleratorTypesRequest,
        response: google.cloud.tpu_v2.types.cloud_tpu.ListAcceleratorTypesResponse,
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

A pager for iterating through `list_accelerator_types` requests.

This class thinly wraps an initial [ListAcceleratorTypesResponse](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.types.ListAcceleratorTypesResponse) object, and provides an `__iter__` method to iterate through its `accelerator_types` field.

If there are more pages, the `__iter__` method will make additional `ListAcceleratorTypes` requests and continue to iterate through the `accelerator_types` field on the corresponding responses.

All the usual [ListAcceleratorTypesResponse](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.types.ListAcceleratorTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListAcceleratorTypesPager
    
    
    ListAcceleratorTypesPager(
        method: typing.Callable[
            [...], google.cloud.tpu_v2.types.cloud_tpu.ListAcceleratorTypesResponse
        ],
        request: google.cloud.tpu_v2.types.cloud_tpu.ListAcceleratorTypesRequest,
        response: google.cloud.tpu_v2.types.cloud_tpu.ListAcceleratorTypesResponse,
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

Instantiate the pager.

**Parameters**  
---  
**Name** | **Description**  
`method` |  `Callable`   
The method that was originally called, and which instantiated this pager.  
`request` |  `[google.cloud.tpu_v2.types.ListAcceleratorTypesRequest](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.types.ListAcceleratorTypesRequest)`   
The initial request object.  
`response` |  `[google.cloud.tpu_v2.types.ListAcceleratorTypesResponse](https://docs.cloud.google.com/python/docs/reference/tpu/latest/google.cloud.tpu_v2.types.ListAcceleratorTypesResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
