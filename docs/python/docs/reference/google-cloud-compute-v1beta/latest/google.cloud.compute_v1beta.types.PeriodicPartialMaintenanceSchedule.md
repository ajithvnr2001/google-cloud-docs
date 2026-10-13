---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PeriodicPartialMaintenanceSchedule
title: Class PeriodicPartialMaintenanceSchedule (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:36.967149+00:00
---

# Class PeriodicPartialMaintenanceSchedule (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.PeriodicPartialMaintenanceSchedule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PeriodicPartialMaintenanceSchedule (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    PeriodicPartialMaintenanceSchedule(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The periodic partial maintenance schedule includes 52 weeks worth of maintenance windows. LINT.IfChange(PeriodicPartialMaintenanceSchedule)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`sub_type` |  `str`   
The maintenance type in which the zone is during the given window. Check the SubType enum for the list of possible values. This field is a member of `oneof`_ `_sub_type`.   
`target_resource` |  `str`   
The target resource that the maintenance window is for. For example, "projects/my-project/zones/us-central1-a". This field is a member of `oneof`_ `_target_resource`.   
`type_` |  `str`   
Check the Type enum for the list of possible values. This field is a member of `oneof`_ `_type`.   
`window_end_time` |  `[google.cloud.compute_v1beta.types.DateTime](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DateTime)`   
The end civil timestamp of the window (not inclusive). This contains a time zone. This field is a member of `oneof`_ `_window_end_time`.   
`window_start_time` |  `[google.cloud.compute_v1beta.types.DateTime](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DateTime)`   
The start civil timestamp of the window. This contains a time zone. This field is a member of `oneof`_ `_window_start_time`.   
  
## Classes 

### SubType
    
    
    SubType(value)

The maintenance type in which the zone is during the given window.

### Type
    
    
    Type(value)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
