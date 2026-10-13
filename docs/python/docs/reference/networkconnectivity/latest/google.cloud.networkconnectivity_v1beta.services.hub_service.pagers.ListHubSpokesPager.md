---
url: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.services.hub_service.pagers.ListHubSpokesPager
title: Class ListHubSpokesPager (2.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:15.646798+00:00
---

# Class ListHubSpokesPager (2.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.services.hub_service.pagers.ListHubSpokesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListHubSpokesPager (2.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.18.0 (latest)  2.17.0  2.16.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1  2.6.0  2.5.1  2.4.5  2.3.0  2.2.0  2.0.2  1.6.1  1.5.0  1.4.4  1.3.2  1.2.2  1.1.0  1.0.1  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    ListHubSpokesPager(
        method: typing.Callable[
            [...], google.cloud.networkconnectivity_v1beta.types.hub.ListHubSpokesResponse
        ],
        request: google.cloud.networkconnectivity_v1beta.types.hub.ListHubSpokesRequest,
        response: google.cloud.networkconnectivity_v1beta.types.hub.ListHubSpokesResponse,
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

A pager for iterating through `list_hub_spokes` requests.

This class thinly wraps an initial [ListHubSpokesResponse](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse) object, and provides an `__iter__` method to iterate through its `spokes` field.

If there are more pages, the `__iter__` method will make additional `ListHubSpokes` requests and continue to iterate through the `spokes` field on the corresponding responses.

All the usual [ListHubSpokesResponse](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListHubSpokesPager
    
    
    ListHubSpokesPager(
        method: typing.Callable[
            [...], google.cloud.networkconnectivity_v1beta.types.hub.ListHubSpokesResponse
        ],
        request: google.cloud.networkconnectivity_v1beta.types.hub.ListHubSpokesRequest,
        response: google.cloud.networkconnectivity_v1beta.types.hub.ListHubSpokesResponse,
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
`request` |  `[google.cloud.networkconnectivity_v1beta.types.ListHubSpokesRequest](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.ListHubSpokesRequest)`   
The initial request object.  
`response` |  `[google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse](https://docs.cloud.google.com/python/docs/reference/networkconnectivity/latest/google.cloud.networkconnectivity_v1beta.types.ListHubSpokesResponse)`   
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
