---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource
title: Class RepositoryResource (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:14:15.208846+00:00
---

# Class RepositoryResource (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RepositoryResource (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    RepositoryResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A resource that manages a package repository.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`apt` |  `[google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.AptRepository](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.AptRepository)`   
An Apt Repository. This field is a member of `oneof`_ `repository`.   
`yum` |  `[google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.YumRepository](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.YumRepository)`   
A Yum Repository. This field is a member of `oneof`_ `repository`.   
`zypper` |  `[google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.ZypperRepository](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.ZypperRepository)`   
A Zypper Repository. This field is a member of `oneof`_ `repository`.   
`goo` |  `[google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.GooRepository](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.OSPolicy.Resource.RepositoryResource.GooRepository)`   
A Goo Repository. This field is a member of `oneof`_ `repository`.   
  
## Classes 

### AptRepository
    
    
    AptRepository(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a single apt package repository. These will be added to a repo file that will be managed at `/etc/apt/sources.list.d/google_osconfig.list`.

### GooRepository
    
    
    GooRepository(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a Goo package repository. These are added to a repo file that is managed at `C:/ProgramData/GooGet/repos/google_osconfig.repo`.

### YumRepository
    
    
    YumRepository(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a single yum package repository. These are added to a repo file that is managed at `/etc/yum.repos.d/google_osconfig.repo`.

### ZypperRepository
    
    
    ZypperRepository(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents a single zypper package repository. These are added to a repo file that is managed at `/etc/zypp/repos.d/google_osconfig.repo`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
