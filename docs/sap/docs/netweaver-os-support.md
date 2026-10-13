---
url: https://docs.cloud.google.com/sap/docs/netweaver-os-support/
title: OS support for SAP NetWeaver on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:10.318627+00:00
---

# OS support for SAP NetWeaver on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/netweaver-os-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  OS support for SAP NetWeaver on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

When choosing an operating system (OS) for SAP NetWeaver on Google Cloud, in addition to confirming that the OS version is certified by SAP, you also need to confirm that all three companies, SAP, the OS vendor, and Google Cloud, still support the OS version.

Your decision should also take into account:

  * Whether a given OS version is available from Google Cloud. The [OS images](https://docs.cloud.google.com/compute/docs/images) provided by Compute Engine are configured to work with Google Cloud. If an OS is not available from Google Cloud, you can bring your own OS image (BYOI) and license. BYOI OS images are referred to by Compute Engine as [_custom images_](https://docs.cloud.google.com/compute/docs/images#custom_images).
  * The available licensing options for a given OS version. Does it have an on-demand licensing option or do you have to bring-your-own-subscription (BYOS) from the OS vendor?
  * Are the integrated high-availability capabilities of a given OS version enabled for Google Cloud?
  * The [committed use discount option](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments) for SLES for SAP images.



The following operating systems are certified for use with SAP NetWeaver on Google Cloud:

  * [Red Hat Enterprise Linux (RHEL)](https://access.redhat.com/articles/3751271)
  * [SUSE Linux Enterprise Server (SLES)](https://www.suse.com/products/sles-for-sap/)
  * [Microsoft Windows Server](https://docs.microsoft.com/en-us/windows-server/)
  * [Oracle Linux](https://docs.oracle.com/en/operating-systems/oracle-linux/index.html)



## Quick reference table

The support information in the following table is for quick reference only and does not replace or supersede SAP information regarding which operating systems SAP supports for SAP NetWeaver on Google Cloud. The information in the following table is subject to change by SAP, the OS providers, or Google Cloud.

The OS versions in the following table are certified or are pending certification by SAP for use with SAP NetWeaver on Google Cloud.

Operating system | SAP certified | OS vendor supported | Runs on Google Cloud | Images provided by Google Cloud  
---|---|---|---|---  
**RHEL 10 for SAP**  
RHEL 10.0 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
**RHEL 9 for SAP**  
RHEL 9.6 for SAP Note | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 9.4 for SAP Note | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 9.2 for SAP Note | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 9.0 for SAP Note | Yes | Yes | Yes | On demand, BYOS, GC-HA  
**RHEL 8 for SAP**  
RHEL 8.10 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 8.8 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 8.6 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 8.4 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 8.2 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
RHEL 8.1 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
**RHEL 7 for SAP**  
RHEL 7.9 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA, RHEL ELS Add-On  
RHEL 7.7 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
RHEL 7.6 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
RHEL 7.5 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
RHEL 7.4 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
**RHEL 6**  
RHEL 6 | Deprecated | Deprecated | Deprecated | Discontinued  
**SLES 16 for SAP**  
SLES 16 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
**SLES 15 for SAP**  
SLES 15 SP7 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 SP6 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 SP5 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 SP4 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 SP3 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 SP2 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 SP1 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 15 for SAP | Yes | Yes | Yes | None  
**SLES 12 for SAP**  
SLES 12 SP5 for SAP | Yes | Yes | Yes | On demand, BYOS, GC-HA  
SLES 12 SP4 for SAP | Yes | Yes | Yes | None  
SLES 12 SP3 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
SLES 12 SP2 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
SLES 12 SP1 for SAP | Deprecated | Deprecated | Deprecated | Discontinued  
**SLES 11 for SAP**  
SLES 11 SP4 for SAP | Yes | Yes | Deprecated | Discontinued  
**Oracle Linux with UEK**  
Oracle Linux 9 | Yes | Yes | Yes | On demand, BYOS  
Oracle Linux 8 | Yes | Yes | Yes | On demand, BYOS  
**Windows Server**  
Windows Server 2025 | Yes | Yes | Yes | On demand  
Windows Server 2022 | Yes | Yes | Yes | On demand  
Windows Server 2019 | Yes | Yes | Yes | On demand  
Windows Server 2016 | Yes | Yes | Yes | On demand  
  
Table notes:

  * **BYOS:** You can apply your existing subscription or license from the OS vendor to the Google-provided OS image. The image that is provided by Google Cloud contains enhancements that might not be included if you bring your own OS image.

  * **GC-HA:** This OS includes integrated high-availability capabilities that are enabled for Google Cloud.

  * **None** This OS is not currently available from Google Cloud. You might be able to import it into Google Cloud as a custom image if you bring your own subscription (BYOS) or license from the OS vendor. See [Custom images](https://docs.cloud.google.com/compute/docs/images#custom_images).

  * **On demand:** This OS is available from Google Cloud with an on-demand license.

  * **RHEL ELS Add-On:** Only supported with Extended Lifecycle Support (ELS). For information about how to append the ELS Add-On to RHEL VMs that have on-demand licenses for their images and have reached end of maintenance, see [Append RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses).

  * **Note:** Before you install any SAP software on RHEL for SAP 9.x, additional packages must be installed on your host machines, especially `chkconfig` and `compat-openssl11`. If you use an image provided by Compute Engine, then these packages are automatically installed for you. For more information from SAP, see the SAP note [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316). 




## Additional SAP and OS vendor information

To confirm SAP support for an operating system for SAP NetWeaver, see the following SAP notes:

  * [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432)
  * [2799900 - Central Technical Note for Oracle Database 19c](https://me.sap.com/notes/2799900)
  * [SAP Product Availability Matrix](https://apps.support.sap.com/sap/support/pam)



For information from the operating system providers about their support for specific versions of their operating systems, see:

  * [RHEL for SAP Offerings on Certified Cloud Providers](https://access.redhat.com/articles/3751271)
  * [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata/)
  * [SUSE Product Support Lifecycle](https://www.suse.com/lifecycle/)
  * [Microsoft Lifecycle Policy](https://support.microsoft.com/en-us/lifecycle/search/1163)
  * [Oracle Linux Cloud Images](https://yum.oracle.com/oracle-linux-templates.html)



For information about the Compute Engine policies for the lifecycle and support for operating system images, see:

  * [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy)
  * [Operating system details](https://docs.cloud.google.com/compute/docs/images#os-details)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
