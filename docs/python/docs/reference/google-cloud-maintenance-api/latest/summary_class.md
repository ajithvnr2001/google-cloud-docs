---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/summary_class/
title: Package Classes (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:19.692669+00:00
---

# Package Classes (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.1 

Summary of entries of Classes for google-cloud-maintenance-api.

## Classes 

### [MaintenanceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient)

Unified Maintenance service

### [MaintenanceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient)

Unified Maintenance service

### [ListResourceMaintenancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesAsyncPager)

A pager for iterating through `list_resource_maintenances` requests.

This class thinly wraps an initial [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ListResourceMaintenancesResponse) object, and provides an `__aiter__` method to iterate through its `resource_maintenances` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceMaintenances` requests and continue to iterate through the `resource_maintenances` field on the corresponding responses.

All the usual [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ListResourceMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceMaintenancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesPager)

A pager for iterating through `list_resource_maintenances` requests.

This class thinly wraps an initial [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ListResourceMaintenancesResponse) object, and provides an `__iter__` method to iterate through its `resource_maintenances` field.

If there are more pages, the `__iter__` method will make additional `ListResourceMaintenances` requests and continue to iterate through the `resource_maintenances` field on the corresponding responses.

All the usual [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ListResourceMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SummarizeMaintenancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesAsyncPager)

A pager for iterating through `summarize_maintenances` requests.

This class thinly wraps an initial [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesResponse) object, and provides an `__aiter__` method to iterate through its `maintenances` field.

If there are more pages, the `__aiter__` method will make additional `SummarizeMaintenances` requests and continue to iterate through the `maintenances` field on the corresponding responses.

All the usual [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SummarizeMaintenancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesPager)

A pager for iterating through `summarize_maintenances` requests.

This class thinly wraps an initial [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesResponse) object, and provides an `__iter__` method to iterate through its `maintenances` field.

If there are more pages, the `__iter__` method will make additional `SummarizeMaintenances` requests and continue to iterate through the `maintenances` field on the corresponding responses.

All the usual [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GetResourceMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.GetResourceMaintenanceRequest)

The request structure for the GetResourceMaintenance method.

### [ListResourceMaintenancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ListResourceMaintenancesRequest)

The request structure for the ListResourceMaintenances method.

### [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ListResourceMaintenancesResponse)

The response structure for the ListResourceMaintenances method.

### [MaintenanceCategory](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceCategory)

The Category of the maintenance.

### [MaintenanceControl](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceControl)

The control of the maintenance.

### [Control](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceControl.Control)

Sets the type of control supported. comment (as in logs).

### [MaintenanceSummary](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceSummary)

MaintenanceSummary contains maintenance statistics calculated based on ResourceMaintenances within the scope: project and location.

### [Aggregate](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceSummary.Aggregate)

Aggregate is a <group, count> pair.

### [Stats](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.MaintenanceSummary.Stats)

Stats indicates the type of aggregate and the corresponding aggregates.

### [ResourceMaintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ResourceMaintenance)

ResourceMaintenance is a resource that represents a maintenance operation on a resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ResourceMaintenance.AnnotationsEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ResourceMaintenance.LabelsEntry)

The abstract base class for a message.

### [Maintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ResourceMaintenance.Maintenance)

Maintenance is the maintenance details of a resource's maintenance.

### [Resource](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ResourceMaintenance.Resource)

Resource contains information about the resource affected by maintenance.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.ResourceMaintenance.State)

State is the state of a resource maintenance.

### [SummarizeMaintenancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesRequest)

Request message for SummarizeMaintenances custom method.

### [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.types.SummarizeMaintenancesResponse)

Request message for SummarizeMaintenances custom method.

### [MaintenanceAsyncClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient)

Unified Maintenance service

### [MaintenanceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient)

Unified Maintenance service

### [ListResourceMaintenancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesAsyncPager)

A pager for iterating through `list_resource_maintenances` requests.

This class thinly wraps an initial [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ListResourceMaintenancesResponse) object, and provides an `__aiter__` method to iterate through its `resource_maintenances` field.

If there are more pages, the `__aiter__` method will make additional `ListResourceMaintenances` requests and continue to iterate through the `resource_maintenances` field on the corresponding responses.

All the usual [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ListResourceMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListResourceMaintenancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesPager)

A pager for iterating through `list_resource_maintenances` requests.

This class thinly wraps an initial [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ListResourceMaintenancesResponse) object, and provides an `__iter__` method to iterate through its `resource_maintenances` field.

If there are more pages, the `__iter__` method will make additional `ListResourceMaintenances` requests and continue to iterate through the `resource_maintenances` field on the corresponding responses.

All the usual [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ListResourceMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SummarizeMaintenancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesAsyncPager)

A pager for iterating through `summarize_maintenances` requests.

This class thinly wraps an initial [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.SummarizeMaintenancesResponse) object, and provides an `__aiter__` method to iterate through its `maintenances` field.

If there are more pages, the `__aiter__` method will make additional `SummarizeMaintenances` requests and continue to iterate through the `maintenances` field on the corresponding responses.

All the usual [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.SummarizeMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SummarizeMaintenancesPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesPager)

A pager for iterating through `summarize_maintenances` requests.

This class thinly wraps an initial [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.SummarizeMaintenancesResponse) object, and provides an `__iter__` method to iterate through its `maintenances` field.

If there are more pages, the `__iter__` method will make additional `SummarizeMaintenances` requests and continue to iterate through the `maintenances` field on the corresponding responses.

All the usual [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.SummarizeMaintenancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [GetResourceMaintenanceRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.GetResourceMaintenanceRequest)

The request structure for the GetResourceMaintenance method.

### [ListResourceMaintenancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ListResourceMaintenancesRequest)

The request structure for the ListResourceMaintenances method.

### [ListResourceMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ListResourceMaintenancesResponse)

The response structure for the ListResourceMaintenances method.

### [MaintenanceCategory](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceCategory)

The Category of the maintenance.

### [MaintenanceControl](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceControl)

The control of the maintenance.

### [Control](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceControl.Control)

Sets the type of control supported. comment (as in logs).

### [MaintenanceSummary](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceSummary)

MaintenanceSummary contains maintenance statistics calculated based on ResourceMaintenances within the scope: project and location.

### [Aggregate](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceSummary.Aggregate)

Aggregate is a <group, count> pair.

### [Stats](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.MaintenanceSummary.Stats)

Stats indicates the type of aggregate and the corresponding aggregates.

### [ResourceMaintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ResourceMaintenance)

ResourceMaintenance is a resource that represents a maintenance operation on a resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.AnnotationsEntry)

The abstract base class for a message.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.LabelsEntry)

The abstract base class for a message.

### [Maintenance](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.Maintenance)

Maintenance is the maintenance details of a resource's maintenance.

### [Resource](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.Resource)

Resource contains information about the resource affected by maintenance.

### [State](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.ResourceMaintenance.State)

State is the state of a resource maintenance.

### [SummarizeMaintenancesRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.SummarizeMaintenancesRequest)

Request message for SummarizeMaintenances custom method.

### [SummarizeMaintenancesResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.types.SummarizeMaintenancesResponse)

Request message for SummarizeMaintenances custom method.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers)

API documentation for `maintenance_api_v1.services.maintenance.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers)

API documentation for `maintenance_api_v1beta.services.maintenance.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
