---
url: https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1beta1.types.Replication
title: Class Replication (2.31.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:49.209127+00:00
---

# Class Replication (2.31.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1beta1.types.Replication

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Replication (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.23.3  2.22.1  2.21.1  2.20.2  2.19.0  2.18.3  2.17.0  2.16.3  2.15.1  2.14.0  2.13.0  2.12.6  2.11.1  2.10.0  2.9.2  2.8.0  2.7.3  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.2  0.2.0  0.1.1 
    
    
    Replication(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A policy that defines the replication configuration of data.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`automatic` |  `[google.cloud.secretmanager_v1beta1.types.Replication.Automatic](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1beta1.types.Replication.Automatic)`   
The Secret will automatically be replicated without any restrictions. This field is a member of `oneof`_ `replication`.   
`user_managed` |  `[google.cloud.secretmanager_v1beta1.types.Replication.UserManaged](https://docs.cloud.google.com/python/docs/reference/secretmanager/latest/google.cloud.secretmanager_v1beta1.types.Replication.UserManaged)`   
The Secret will only be replicated into the locations specified. This field is a member of `oneof`_ `replication`.   
  
## Classes 

### Automatic
    
    
    Automatic(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A replication policy that replicates the Secret payload without any restrictions.

### UserManaged
    
    
    UserManaged(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A replication policy that replicates the Secret payload into the locations specified in Replication.UserManaged.replicas

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
