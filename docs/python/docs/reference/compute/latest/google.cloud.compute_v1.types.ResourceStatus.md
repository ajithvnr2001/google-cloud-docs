---
url: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatus
title: Class ResourceStatus (1.56.0rc1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:41.028974+00:00
---

# Class ResourceStatus (1.56.0rc1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ResourceStatus (1.56.0rc1) Stay organized with collections  Save and categorize content based on your preferences. 

1.56.0-rc1  1.55.0 (latest)  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.1  1.19.2  1.18.0  1.17.0  1.16.1  1.15.0  1.14.1  1.13.0  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 
    
    
    ResourceStatus(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Contains output only fields. Use this sub-message for actual values set on Instance attributes as compared to the value requested by the user (intent) in their instance CRUD calls.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`effective_instance_metadata` |  `[google.cloud.compute_v1.types.ResourceStatusEffectiveInstanceMetadata](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatusEffectiveInstanceMetadata)`   
Output only. [Output Only] Effective metadata is a field that consolidates project, zonal instance settings, and instance-level predefined metadata keys to provide the overridden value for those metadata keys at the instance level. This field is a member of `oneof`_ `_effective_instance_metadata`.   
`physical_host` |  `str`   
Output only. [Output Only] The precise location of your instance within the zone's data center, including the block, sub-block, and host. The field is formatted as follows: blockId/subBlockId/hostId. This field is a member of `oneof`_ `_physical_host`.   
`physical_host_topology` |  `[google.cloud.compute_v1.types.ResourceStatusPhysicalHostTopology](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatusPhysicalHostTopology)`   
Output only. [Output Only] A series of fields containing the global name of the Compute Engine cluster, as well as the ID of the block, sub-block, and host on which the running instance is located. This field is a member of `oneof`_ `_physical_host_topology`.   
`reservation_consumption_info` |  `[google.cloud.compute_v1.types.ResourceStatusReservationConsumptionInfo](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatusReservationConsumptionInfo)`   
Output only. [Output Only] Reservation information that the instance is consuming from. This field is a member of `oneof`_ `_reservation_consumption_info`.   
`scheduling` |  `[google.cloud.compute_v1.types.ResourceStatusScheduling](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatusScheduling)`   
This field is a member of `oneof`_ `_scheduling`.   
`shutdown_details` |  `[google.cloud.compute_v1.types.ResourceStatusShutdownDetails](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.ResourceStatusShutdownDetails)`   
Output only. [Output Only] Details about the instance stopping state. This field is a member of `oneof`_ `_shutdown_details`.   
`upcoming_maintenance` |  `[google.cloud.compute_v1.types.UpcomingMaintenance](https://docs.cloud.google.com/python/docs/reference/compute/latest/google.cloud.compute_v1.types.UpcomingMaintenance)`   
This field is a member of `oneof`_ `_upcoming_maintenance`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
