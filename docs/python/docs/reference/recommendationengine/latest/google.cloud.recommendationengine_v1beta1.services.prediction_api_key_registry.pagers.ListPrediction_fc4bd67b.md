---
url: https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.pagers.ListPredictionApiKeyRegistrationsPager
title: Class ListPredictionApiKeyRegistrationsPager (0.13.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:11:56.552261+00:00
---

# Class ListPredictionApiKeyRegistrationsPager (0.13.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.services.prediction_api_key_registry.pagers.ListPredictionApiKeyRegistrationsPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListPredictionApiKeyRegistrationsPager (0.13.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.2 (latest)  0.13.1  0.12.0  0.11.0  0.10.18  0.9.0  0.8.2  0.7.1  0.6.2  0.5.1  0.4.0  0.3.3  0.2.2  0.1.0 
    
    
    ListPredictionApiKeyRegistrationsPager(
        method: typing.Callable[
            [...],
            google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse,
        ],
        request: google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest,
        response: google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse,
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

A pager for iterating through `list_prediction_api_key_registrations` requests.

This class thinly wraps an initial [ListPredictionApiKeyRegistrationsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsResponse) object, and provides an `__iter__` method to iterate through its `prediction_api_key_registrations` field.

If there are more pages, the `__iter__` method will make additional `ListPredictionApiKeyRegistrations` requests and continue to iterate through the `prediction_api_key_registrations` field on the corresponding responses.

All the usual [ListPredictionApiKeyRegistrationsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListPredictionApiKeyRegistrationsPager
    
    
    ListPredictionApiKeyRegistrationsPager(
        method: typing.Callable[
            [...],
            google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse,
        ],
        request: google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsRequest,
        response: google.cloud.recommendationengine_v1beta1.types.prediction_apikey_registry_service.ListPredictionApiKeyRegistrationsResponse,
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
`request` |  `[google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsRequest](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsRequest)`   
The initial request object.  
`response` |  `[google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsResponse](https://docs.cloud.google.com/python/docs/reference/recommendationengine/latest/google.cloud.recommendationengine_v1beta1.types.ListPredictionApiKeyRegistrationsResponse)`   
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
