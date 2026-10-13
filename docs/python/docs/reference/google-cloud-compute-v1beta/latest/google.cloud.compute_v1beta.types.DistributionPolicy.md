---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DistributionPolicy
title: Class DistributionPolicy (0.12.7) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:14:13.344565+00:00
---

# Class DistributionPolicy (0.12.7)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DistributionPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DistributionPolicy (0.12.7) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.7 (latest)  0.12.6  0.11.0  0.4.0  0.3.0  0.2.0  0.1.8 
    
    
    DistributionPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`target_shape` |  `str`   
The distribution shape to which the group converges either proactively or on resize events (depending on the value set inupdatePolicy.instanceRedistributionType). Check the TargetShape enum for the list of possible values. This field is a member of `oneof`_ `_target_shape`.   
`zones` |  `MutableSequence[[google.cloud.compute_v1beta.types.DistributionPolicyZoneConfiguration](https://docs.cloud.google.com/python/docs/reference/google-cloud-compute-v1beta/latest/google.cloud.compute_v1beta.types.DistributionPolicyZoneConfiguration)]`   
Zones where the regional managed instance group will create and manage its instances. By default, a regional MIG doesn't automatically select an AI zone to create instances, even if an AI zone is available in the specified region. To create instances in an AI zone in the selected region, you must explicitly specify it in the distribution policy together with the other preferred zones.   
  
## Classes 

### TargetShape
    
    
    TargetShape(value)

The distribution shape to which the group converges either proactively or on resize events (depending on the value set inupdatePolicy.instanceRedistributionType).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
