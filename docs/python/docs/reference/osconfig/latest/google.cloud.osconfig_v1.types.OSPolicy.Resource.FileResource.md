---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.FileResource
title: Class FileResource (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:36:45.698940+00:00
---

# Class FileResource (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.FileResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class FileResource (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    FileResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource that manages the state of a file.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`file` |  `google.cloud.osconfig_v1.types.OSPolicy.Resource.File`   
A remote or local source. This field is a member of `oneof`_ `source`.   
`content` |  `str`   
A a file with this content. The size of the content is limited to 1024 characters. This field is a member of `oneof`_ `source`.   
`path` |  `str`   
Required. The absolute path of the file within the VM.   
`state` |  `[google.cloud.osconfig_v1.types.OSPolicy.Resource.FileResource.DesiredState](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.FileResource.DesiredState)`   
Required. Desired state of the file.   
`permissions` |  `str`   
Consists of three octal digits which represent, in order, the permissions of the owner, group, and other users for the file (similarly to the numeric mode used in the linux chmod utility). Each digit represents a three bit number with the 4 bit corresponding to the read permissions, the 2 bit corresponds to the write bit, and the one bit corresponds to the execute permission. Default behavior is 755. Below are some examples of permissions and their associated values: read, write, and execute: 7 read and execute: 5 read and write: 6 read only: 4   
  
## Classes 

### DesiredState
    
    
    DesiredState(value)

Desired state of the file.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
