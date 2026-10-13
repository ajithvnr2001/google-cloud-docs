---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.SlurmPartition
title: Class SlurmPartition (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:26.507924+00:00
---

# Class SlurmPartition (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.SlurmPartition

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SlurmPartition (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.2.0  0.1.0 
    
    
    SlurmPartition(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for Slurm partitions in the cluster. Partitions are groups of nodesets, and are how clients specify where their workloads should be run.

## Attributes  
  
---  
**Name** | **Description**  
`id` |  `str`   
Required. ID of the partition, which is how users will identify it. Must conform to `RFC-1034 `__ (lower-case, alphanumeric, and at most 63 characters).   
`node_set_ids` |  `MutableSequence[str]`   
Required. IDs of the nodesets that make up this partition. Values must match SlurmNodeSet.id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
