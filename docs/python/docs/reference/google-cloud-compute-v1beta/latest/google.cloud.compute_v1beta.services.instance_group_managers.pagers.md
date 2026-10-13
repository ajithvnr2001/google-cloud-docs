---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers
title: Module pagers (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:19:25.758404+00:00
---

# Module pagers (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module pagers (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 

API documentation for `compute_v1beta.services.instance_group_managers.pagers` module.

## Classes 

### [AggregatedListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.AggregatedListPager)
    
    
    AggregatedListPager(
        method: typing.Callable[
            [...],
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagerAggregatedList,
        ],
        request: google.cloud.compute_v1beta.types.compute.AggregatedListInstanceGroupManagersRequest,
        response: google.cloud.compute_v1beta.types.compute.InstanceGroupManagerAggregatedList,
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

A pager for iterating through `aggregated_list` requests.

This class thinly wraps an initial [InstanceGroupManagerAggregatedList](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagerAggregatedList) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `AggregatedList` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [InstanceGroupManagerAggregatedList](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagerAggregatedList) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListErrorsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListErrorsPager)
    
    
    ListErrorsPager(
        method: typing.Callable[
            [...],
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersListErrorsResponse,
        ],
        request: google.cloud.compute_v1beta.types.compute.ListErrorsInstanceGroupManagersRequest,
        response: google.cloud.compute_v1beta.types.compute.InstanceGroupManagersListErrorsResponse,
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

A pager for iterating through `list_errors` requests.

This class thinly wraps an initial [InstanceGroupManagersListErrorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersListErrorsResponse) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `ListErrors` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [InstanceGroupManagersListErrorsResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersListErrorsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListManagedInstancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListManagedInstancesPager)
    
    
    ListManagedInstancesPager(
        method: typing.Callable[
            [...],
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersListManagedInstancesResponse,
        ],
        request: google.cloud.compute_v1beta.types.compute.ListManagedInstancesInstanceGroupManagersRequest,
        response: google.cloud.compute_v1beta.types.compute.InstanceGroupManagersListManagedInstancesResponse,
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

A pager for iterating through `list_managed_instances` requests.

This class thinly wraps an initial [InstanceGroupManagersListManagedInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersListManagedInstancesResponse) object, and provides an `__iter__` method to iterate through its `managed_instances` field.

If there are more pages, the `__iter__` method will make additional `ListManagedInstances` requests and continue to iterate through the `managed_instances` field on the corresponding responses.

All the usual [InstanceGroupManagersListManagedInstancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersListManagedInstancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPager)
    
    
    ListPager(
        method: typing.Callable[
            [...], google.cloud.compute_v1beta.types.compute.InstanceGroupManagerList
        ],
        request: google.cloud.compute_v1beta.types.compute.ListInstanceGroupManagersRequest,
        response: google.cloud.compute_v1beta.types.compute.InstanceGroupManagerList,
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

A pager for iterating through `list` requests.

This class thinly wraps an initial [InstanceGroupManagerList](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagerList) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `List` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [InstanceGroupManagerList](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagerList) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPerInstanceConfigsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.services.instance_group_managers.pagers.ListPerInstanceConfigsPager)
    
    
    ListPerInstanceConfigsPager(
        method: typing.Callable[
            [...],
            google.cloud.compute_v1beta.types.compute.InstanceGroupManagersListPerInstanceConfigsResp,
        ],
        request: google.cloud.compute_v1beta.types.compute.ListPerInstanceConfigsInstanceGroupManagersRequest,
        response: google.cloud.compute_v1beta.types.compute.InstanceGroupManagersListPerInstanceConfigsResp,
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

A pager for iterating through `list_per_instance_configs` requests.

This class thinly wraps an initial [InstanceGroupManagersListPerInstanceConfigsResp](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersListPerInstanceConfigsResp) object, and provides an `__iter__` method to iterate through its `items` field.

If there are more pages, the `__iter__` method will make additional `ListPerInstanceConfigs` requests and continue to iterate through the `items` field on the corresponding responses.

All the usual [InstanceGroupManagersListPerInstanceConfigsResp](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.InstanceGroupManagersListPerInstanceConfigsResp) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
