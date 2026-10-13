---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RegionInstanceGroupsListInstancesRequest
title: Class RegionInstanceGroupsListInstancesRequest (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:17.936636+00:00
---

# Class RegionInstanceGroupsListInstancesRequest (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.RegionInstanceGroupsListInstancesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RegionInstanceGroupsListInstancesRequest (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    RegionInstanceGroupsListInstancesRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`instance_state` |  `str`   
Instances in which state should be returned. Valid options are: 'ALL', 'RUNNING'. By default, it lists all instances. Check the InstanceState enum for the list of possible values. This field is a member of `oneof`_ `_instance_state`.   
`port_name` |  `str`   
Name of port user is interested in. It is optional. If it is set, only information about this ports will be returned. If it is not set, all the named ports will be returned. Always lists all instances. This field is a member of `oneof`_ `_port_name`.   
  
## Classes 

### InstanceState
    
    
    InstanceState(value)

Instances in which state should be returned. Valid options are: 'ALL', 'RUNNING'. By default, it lists all instances.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
