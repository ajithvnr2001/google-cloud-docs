---
url: https://docs.cloud.google.com/container-optimized-os/docs/concepts/supported-filesystems/
title: Supported filesystems \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:49.052740+00:00
---

# Supported filesystems  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/concepts/supported-filesystems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Supported filesystems Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the filesystems available in Container-Optimized OS. Container-Optimized OS comes with two built-in filesystems: EXT4 and XFS.

## EXT4 filesystem

Container-Optimized OS comes with a fully-supported EXT4 filesystem. Container-Optimized OS recommends using the EXT4 filesystem for production workloads.

Container-Optimized OS enables the following EXT4-related features:

  * **Support for the EXT4 filesystem in kernel** : The Linux kernel in Container-Optimized OS has the most commonly used EXT4 features enabled:
        
        CONFIG_EXT4_FS=y
        CONFIG_EXT4_USE_FOR_EXT2=y
        CONFIG_EXT4_FS_POSIX_ACL=y
        CONFIG_EXT4_FS_SECURITY=y
        CONFIG_JBD2=y
        

  * **e2fsprogs package** : The e2fsprogs package contains several critical user space utilities available for the EXT4 filesystem (for example, `mkfs` and `fsck`). These packages are necessary for the creation and maintenance of the EXT4 filesystem.




## XFS filesystem

Container-Optimized OS comes with a fully-supported XFS filesystem starting from COS M105. The recommended filesystem for production workloads on Container-Optimized OS is still EXT4. XFS is primarily targeted for users who have some existing dependency on XFS that cannot be migrated to EXT4. We recommend using XFS only for advanced users that are familiar with the filesystem functionality.

Container-Optimized OS enables the following XFS-related features:

  * **Support for the XFS filesystem in kernel** : The Linux kernel in Container-Optimized OS has the most commonly used XFS features enabled:
        
        CONFIG_XFS_FS=y
          CONFIG_XFS_SUPPORT_V4=y
          CONFIG_XFS_QUOTA=y
          CONFIG_XFS_POSIX_ACL=y
        

  * **xfsprogs package** : The xfsprogs package contains several critical user space utilities available for the XFS filesystem (for example, `mkfs` and `fsck`). These packages are necessary for creation and maintenance of the XFS filesystem.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
