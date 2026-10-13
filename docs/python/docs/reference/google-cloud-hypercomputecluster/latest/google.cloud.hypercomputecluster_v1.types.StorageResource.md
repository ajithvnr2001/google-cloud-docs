---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.StorageResource
title: Class StorageResource (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:51.134161+00:00
---

# Class StorageResource (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.StorageResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StorageResource (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.2.0  0.1.0 
    
    
    StorageResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource representing a form of persistent storage that is accessible to compute resources in the cluster.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`filestore` |  `[google.cloud.hypercomputecluster_v1.types.FilestoreReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.FilestoreReference)`   
Reference to a Filestore instance. Populated if and only if the storage resource was configured to use Filestore. This field is a member of `oneof`_ `reference`.   
`bucket` |  `[google.cloud.hypercomputecluster_v1.types.BucketReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.BucketReference)`   
Reference to a Google Cloud Storage bucket. Populated if and only if the storage resource was configured to use Google Cloud Storage. This field is a member of `oneof`_ `reference`.   
`lustre` |  `[google.cloud.hypercomputecluster_v1.types.LustreReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.LustreReference)`   
Reference to a Managed Lustre instance. Populated if and only if the storage resource was configured to use Managed Lustre. This field is a member of `oneof`_ `reference`.   
`config` |  `[google.cloud.hypercomputecluster_v1.types.StorageResourceConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-hypercomputecluster/latest/google.cloud.hypercomputecluster_v1.types.StorageResourceConfig)`   
Required. Immutable. Configuration for this storage resource, which describes how it should be created or imported. This field only controls how the storage resource is initially created or imported. Subsequent changes to the storage resource should be made via the resource's API and will not be reflected in the configuration.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
