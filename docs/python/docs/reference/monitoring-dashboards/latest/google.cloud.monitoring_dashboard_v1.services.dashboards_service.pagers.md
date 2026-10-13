---
url: https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers
title: Module pagers (3.2.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:03.653383+00:00
---

# Module pagers (3.2.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.22.0  2.21.0  2.20.1  2.19.0  2.18.2  2.17.0  2.16.1  2.15.3  2.14.1  2.13.0  2.12.3  2.11.1  2.10.0  2.9.0  2.8.0  2.7.4  2.6.1  2.5.1  2.4.1  2.3.0  2.2.4  2.1.0  2.0.0  1.0.2  0.1.2 

API documentation for `monitoring_dashboard_v1.services.dashboards_service.pagers` module.

## Classes 

### [ListDashboardsAsyncPager](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers.ListDashboardsAsyncPager)
    
    
    ListDashboardsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.monitoring_dashboard_v1.types.dashboards_service.ListDashboardsResponse
            ],
        ],
        request: google.cloud.monitoring_dashboard_v1.types.dashboards_service.ListDashboardsRequest,
        response: google.cloud.monitoring_dashboard_v1.types.dashboards_service.ListDashboardsResponse,
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

A pager for iterating through `list_dashboards` requests.

This class thinly wraps an initial [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) object, and provides an `__aiter__` method to iterate through its `dashboards` field.

If there are more pages, the `__aiter__` method will make additional `ListDashboards` requests and continue to iterate through the `dashboards` field on the corresponding responses.

All the usual [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDashboardsPager](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers.ListDashboardsPager)
    
    
    ListDashboardsPager(
        method: typing.Callable[
            [...],
            google.cloud.monitoring_dashboard_v1.types.dashboards_service.ListDashboardsResponse,
        ],
        request: google.cloud.monitoring_dashboard_v1.types.dashboards_service.ListDashboardsRequest,
        response: google.cloud.monitoring_dashboard_v1.types.dashboards_service.ListDashboardsResponse,
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

A pager for iterating through `list_dashboards` requests.

This class thinly wraps an initial [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) object, and provides an `__iter__` method to iterate through its `dashboards` field.

If there are more pages, the `__iter__` method will make additional `ListDashboards` requests and continue to iterate through the `dashboards` field on the corresponding responses.

All the usual [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
