---
url: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListProjectDataProfilesPager
title: Class ListProjectDataProfilesPager (3.40.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:45.331238+00:00
---

# Class ListProjectDataProfilesPager (3.40.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.pagers.ListProjectDataProfilesPager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ListProjectDataProfilesPager (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.39.0  3.38.0  3.37.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.1  3.24.0  3.23.0  3.22.0  3.20.0  3.19.0  3.18.1  3.17.0  3.16.0  3.15.3  3.14.0  3.13.0  3.12.3  3.11.1  3.10.1  3.9.2  3.8.1  3.7.1  3.6.2  3.5.0  3.4.0  3.3.1  3.2.4  3.1.1  3.0.1  2.0.2  1.0.2  0.15.2  0.14.0  0.13.0  0.12.1 
    
    
    ListProjectDataProfilesPager(
        method: typing.Callable[
            [...], google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesResponse
        ],
        request: google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesRequest,
        response: google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesResponse,
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

A pager for iterating through `list_project_data_profiles` requests.

This class thinly wraps an initial [ListProjectDataProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesResponse) object, and provides an `__iter__` method to iterate through its `project_data_profiles` field.

If there are more pages, the `__iter__` method will make additional `ListProjectDataProfiles` requests and continue to iterate through the `project_data_profiles` field on the corresponding responses.

All the usual [ListProjectDataProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

## Methods 

### ListProjectDataProfilesPager
    
    
    ListProjectDataProfilesPager(
        method: typing.Callable[
            [...], google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesResponse
        ],
        request: google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesRequest,
        response: google.cloud.dlp_v2.types.dlp.ListProjectDataProfilesResponse,
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
`request` |  `[google.cloud.dlp_v2.types.ListProjectDataProfilesRequest](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesRequest)`   
The initial request object.  
`response` |  `[google.cloud.dlp_v2.types.ListProjectDataProfilesResponse](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.ListProjectDataProfilesResponse)`   
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
