---
url: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorTypesPager
title: Class ListProcessorTypesPager (3.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:53.759943+00:00
---

# Class ListProcessorTypesPager (3.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.services.document_processor_service.pagers.ListProcessorTypesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListProcessorTypesPager (3.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.16.0 (latest)  3.15.0  3.14.0  3.13.0  3.12.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.1  2.35.0  2.34.0  2.33.0  2.32.0  2.30.0  2.29.3  2.28.0  2.27.1  2.26.0  2.25.0  2.24.2  2.23.0  2.22.0  2.21.1  2.20.2  2.19.0  2.18.0  2.17.0  2.16.1  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.3  1.5.1  1.4.2  1.3.0  1.2.1  1.1.0  1.0.0  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ListProcessorTypesPager(
        method: typing.Callable[
            [...],
            google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesResponse,
        ],
        request: google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesRequest,
        response: google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesResponse,
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

A pager for iterating through `list_processor_types` requests.

This class thinly wraps an initial [ListProcessorTypesResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse) object, and provides an `__iter__` method to iterate through its `processor_types` field.

If there are more pages, the `__iter__` method will make additional `ListProcessorTypes` requests and continue to iterate through the `processor_types` field on the corresponding responses.

All the usual [ListProcessorTypesResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListProcessorTypesPager
    
    
    ListProcessorTypesPager(
        method: typing.Callable[
            [...],
            google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesResponse,
        ],
        request: google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesRequest,
        response: google.cloud.documentai_v1beta3.types.document_processor_service.ListProcessorTypesResponse,
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
`request` |  `[google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorTypesRequest)`   
The initial request object.  
`response` |  `[google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1beta3.types.ListProcessorTypesResponse)`   
The initial response object.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
