---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.pagers
title: Module pagers (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:33.593655+00:00
---

# Module pagers (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

API documentation for `ftp_v1.services.cloud_ftp.pagers` module.

## Classes 

### [ListServersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.pagers.ListServersPager)
    
    
    ListServersPager(
        method: typing.Callable[
            [...], google.cloud.ftp_v1.types.service.ListServersResponse
        ],
        request: google.cloud.ftp_v1.types.service.ListServersRequest,
        response: google.cloud.ftp_v1.types.service.ListServersResponse,
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

A pager for iterating through `list_servers` requests.

This class thinly wraps an initial [ListServersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListServersResponse) object, and provides an `__iter__` method to iterate through its `servers` field.

If there are more pages, the `__iter__` method will make additional `ListServers` requests and continue to iterate through the `servers` field on the corresponding responses.

All the usual [ListServersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListServersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListUsersPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.services.cloud_ftp.pagers.ListUsersPager)
    
    
    ListUsersPager(
        method: typing.Callable[[...], google.cloud.ftp_v1.types.service.ListUsersResponse],
        request: google.cloud.ftp_v1.types.service.ListUsersRequest,
        response: google.cloud.ftp_v1.types.service.ListUsersResponse,
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

A pager for iterating through `list_users` requests.

This class thinly wraps an initial [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListUsersResponse) object, and provides an `__iter__` method to iterate through its `users` field.

If there are more pages, the `__iter__` method will make additional `ListUsers` requests and continue to iterate through the `users` field on the corresponding responses.

All the usual [ListUsersResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-ftp/latest/google.cloud.ftp_v1.types.ListUsersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
