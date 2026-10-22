---
url: https://docs.cloud.google.com/compute/docs/licenses/about/
title: About licenses \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:19.089630+00:00
---

# About licenses  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licenses/about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About licenses Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

A _license_ is a usage agreement between you and a software vendor. To use licensed software provided by Google Cloud, you must have a license. For example, if you are running a licensed operating system (OS) on a Compute Engine virtual machine (VM) instance, you must have a license for that OS.

A _license string_ is a resource that associates a usage agreement with a licensed OS, OS upgrade, or additional software. For a list of the license strings that are associated with each OS that is supported by Compute Engine, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#license-strings). To learn how to view and manage license strings, see [Manage licenses](https://docs.cloud.google.com/compute/docs/licenses/manage).

## License types and pricing

Licenses on Compute Engine are one of the following types. For information about which license types apply to each OS version, see the _license_ section of the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#license-strings) page.

Free licenses
    No charge for usage.
On-demand/Pay-as-you-go (PAYG)
    

Google Cloud charges for usage. Cost varies depending on the OS. For more information, see [pricing for premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages).

    

The Google-provided image contains enhancements that might not be included if you bring your own OS image.

Bring your own license (BYOL)/Bring your own subscription (BYOS)
    

Google Cloud does not charge you because you have a previous agreement with the original OS vendor. If you have BYOL licenses for server or client versions of Windows, you must use [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

    

License strings for BYOL and BYOS end with `byol` or `byos`. If the license string does not end with `byol` or `byos`, the license is a free or on-demand/PAYG license.

For more information about using BYOS and BYOL licenses on Compute Engine, review the following:

  * For RHEL BYOS, see [Create a VM using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm).
  * For Windows, contact your [Google Cloud Technical Account Manager](https://docs.cloud.google.com/support/docs/premium#tam).


Upgrade from Ubuntu to Ubuntu Pro
    

The following Ubuntu versions have reached the end of maintenance:

  * Ubuntu 16.04 LTS - April 21, 2021
  * Ubuntu 18.04 LTS - May 31, 2023



If you need further updates for these versions, you must upgrade and append a user license for Ubuntu Pro. For information about how to upgrade and append a user license, see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu).

Use SQL Server on Linux
    

You can install SQL Server on Linux VMs and use PAYG licenses. For more information, see [Add a SQL Server license to an existing Linux server](https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license-to-linux).

## What's next

  * [Manage licenses](https://docs.cloud.google.com/compute/docs/licenses/manage)

  * [Learn about Microsoft licenses on Compute Engine](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing)

  * Learn more about premium operating systems:

    * [Consult the RHEL FAQ](https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq)

    * [Consult the Ubuntu Pro FAQ](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq)

  * Review [Support policy by license type](https://docs.cloud.google.com/compute/docs/images/support-maintenance-policy#support-by-license)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
