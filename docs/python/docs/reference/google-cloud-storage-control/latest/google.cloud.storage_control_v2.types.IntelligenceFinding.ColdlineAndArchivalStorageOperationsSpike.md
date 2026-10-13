---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.IntelligenceFinding.ColdlineAndArchivalStorageOperationsSpike
title: Class ColdlineAndArchivalStorageOperationsSpike (1.16.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:32.758363+00:00
---

# Class ColdlineAndArchivalStorageOperationsSpike (1.16.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.IntelligenceFinding.ColdlineAndArchivalStorageOperationsSpike

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ColdlineAndArchivalStorageOperationsSpike (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.3  0.2.0  0.1.3 
    
    
    ColdlineAndArchivalStorageOperationsSpike(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Represents a finding about a spike in Class A/B operations on Coldline or Archive Cloud Storage objects. This corresponds to the `COLD_AND_ARCHIVAL_STORAGE_OPERATIONS_SPIKE` finding type.

## Attributes  
  
---  
**Name** | **Description**  
`percentage_increase` |  `float`   
Output only. The percentage increase in operations across the project.   
`total_operations_count` |  `int`   
Output only. The total count of operations across the project.   
`top_buckets` |  `MutableSequence[[google.cloud.storage_control_v2.types.IntelligenceFinding.ColdlineAndArchivalStorageOperationsSpike.BucketContribution](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.IntelligenceFinding.ColdlineAndArchivalStorageOperationsSpike.BucketContribution)]`   
Output only. A list of the top buckets driving the increase in operations.   
  
## Classes 

### BucketContribution
    
    
    BucketContribution(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the operation spike details for a bucket.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
