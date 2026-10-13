---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-privilegedaccessmanager/latest/google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess
title: Class PrivilegedAccess (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:42.544159+00:00
---

# Class PrivilegedAccess (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-privilegedaccessmanager/latest/google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PrivilegedAccess (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.9 
    
    
    PrivilegedAccess(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Privileged access that this service can be used to gate.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attribute  
  
---  
**Name** | **Description**  
`gcp_iam_access` |  `[google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess.GcpIamAccess](https://docs.cloud.google.com/python/docs/reference/google-cloud-privilegedaccessmanager/latest/google.cloud.privilegedaccessmanager_v1.types.PrivilegedAccess.GcpIamAccess)`   
Access to a Google Cloud resource through IAM. This field is a member of `oneof`_ `access_type`.   
  
## Classes 

### GcpIamAccess
    
    
    GcpIamAccess(mapping=None, *, ignore_unknown_fields=False, **kwargs)

`GcpIamAccess` represents IAM based access control on a Google Cloud resource. Refer to <https://cloud.google.com/iam/docs> to understand more about IAM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
