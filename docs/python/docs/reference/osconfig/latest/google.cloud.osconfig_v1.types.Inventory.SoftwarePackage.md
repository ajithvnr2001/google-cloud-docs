---
url: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.SoftwarePackage
title: Class SoftwarePackage (1.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:42.683662+00:00
---

# Class SoftwarePackage (1.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.SoftwarePackage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SoftwarePackage (1.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.26.0 (latest)  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.2  1.19.0  1.18.1  1.17.5  1.16.0  1.15.3  1.14.1  1.13.0  1.12.4  1.11.2  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.2  1.4.0  1.3.2  1.2.0  1.1.0  1.0.0  0.1.2 
    
    
    SoftwarePackage(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Software package information of the operating system.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`yum_package` |  `[google.cloud.osconfig_v1.types.Inventory.VersionedPackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.VersionedPackage)`   
Yum package info. For details about the yum package manager, see https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/ch-yum. This field is a member of `oneof`_ `details`.   
`apt_package` |  `[google.cloud.osconfig_v1.types.Inventory.VersionedPackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.VersionedPackage)`   
Details of an APT package. For details about the apt package manager, see https://wiki.debian.org/Apt. This field is a member of `oneof`_ `details`.   
`zypper_package` |  `[google.cloud.osconfig_v1.types.Inventory.VersionedPackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.VersionedPackage)`   
Details of a Zypper package. For details about the Zypper package manager, see https://en.opensuse.org/SDB:Zypper_manual. This field is a member of `oneof`_ `details`.   
`googet_package` |  `[google.cloud.osconfig_v1.types.Inventory.VersionedPackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.VersionedPackage)`   
Details of a Googet package. For details about the googet package manager, see https://github.com/google/googet. This field is a member of `oneof`_ `details`.   
`zypper_patch` |  `[google.cloud.osconfig_v1.types.Inventory.ZypperPatch](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.ZypperPatch)`   
Details of a Zypper patch. For details about the Zypper package manager, see https://en.opensuse.org/SDB:Zypper_manual. This field is a member of `oneof`_ `details`.   
`wua_package` |  `[google.cloud.osconfig_v1.types.Inventory.WindowsUpdatePackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.WindowsUpdatePackage)`   
Details of a Windows Update package. See https://docs.microsoft.com/en-us/windows/win32/api/\\_wua/ for information about Windows Update. This field is a member of `oneof`_ `details`.   
`qfe_package` |  `[google.cloud.osconfig_v1.types.Inventory.WindowsQuickFixEngineeringPackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.WindowsQuickFixEngineeringPackage)`   
Details of a Windows Quick Fix engineering package. See https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-quickfixengineering for info in Windows Quick Fix Engineering. This field is a member of `oneof`_ `details`.   
`cos_package` |  `[google.cloud.osconfig_v1.types.Inventory.VersionedPackage](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.VersionedPackage)`   
Details of a COS package. This field is a member of `oneof`_ `details`.   
`windows_application` |  `[google.cloud.osconfig_v1.types.Inventory.WindowsApplication](https://docs.cloud.google.com/python/docs/reference/osconfig/latest/google.cloud.osconfig_v1.types.Inventory.WindowsApplication)`   
Details of Windows Application. This field is a member of `oneof`_ `details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
