---
url: https://docs.cloud.google.com/compute/docs/instances/windows/end-of-support/
title: Windows end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:15.306857+00:00
---

# Windows end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/end-of-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Windows end of support Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

Microsoft sets the end of support (EOS) date for each Windows operating system version that is used by virtual machine (VM) instances on Compute Engine. In this document, EOS refers to the Microsoft Extended Support end date, as defined in the [Microsoft Lifecycle Policy](https://support.microsoft.com/en-us/hub/4095338/microsoft-lifecycle-policy). On this date:

  * Google can no longer access updates.
  * Google can no longer access security patches.
  * The OS image is deleted from the Compute Engine images project. If you need to create VMs that use any of these EOS versions after the EOS date, [make copies of the images](https://docs.cloud.google.com/compute/docs/images/create-custom) before the EOS date.



If you are running VM instances on Compute Engine based on one of these operating system images, keep in mind that beginning on the EOS date:

  * VMs based on images that are beyond their EOS date continue to operate, and billing continues for [premium images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages).

  * Future Google Cloud features might not perform as expected if you use an image that is beyond its EOS date.

  * Google can no longer provide updates or security patches. Microsoft might provide additional support through its [Extended Security Update (ESU)](https://support.microsoft.com/en-us/help/4497181/lifecycle-faq-extended-security-updates) program. It is your responsibility to install and test all updates provided by Microsoft.

  * Google provides support for VMs that use EOS images. For more information, review [End of support (EOS)](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#eos) documentation.




Using an unsupported and unpatched version might create material security risks. If you are running VM instances based on an operating system image with an announced EOS date, Google recommends that before the EOS date, you:

  * Upgrade or migrate to a [supported version of the Windows operating system](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server).

  * If you anticipate needing to create VM instances after the EOS date, make copies of the images in your projects.

  * Remove any [external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#externaladdresses) because publicly accessible instances might be vulnerable to unpatched security exploits. Instead, use the instance's [internal IP address](https://docs.cloud.google.com/compute/docs/ip-addresses#networkaddresses) to host services and enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  * Consider configuring a [Remote Desktop Gateway](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-plan-access-from-anywhere) to restrict remote access to your instance.




If you continue to use an image after the EOS date for that image, Google recommends that you not update the [guest environment](https://docs.cloud.google.com/compute/docs/images/guest-environment) because Google doesn't test new versions of the image against the EOS version. When Google releases additional [image families](https://docs.cloud.google.com/compute/docs/images#image_families), those newly released image families might not support the EOS versions of the images, so we recommend that you continue to use the image family that you are using.

The following table shows Microsoft operating systems that are no longer supported, their EOS dates, where to find Microsoft's EOS announcements, and links to content about upgrading or migrating:

Operating system | EOS date | More information  
---|---|---  
Windows Server 2012 R2  | October 10, 2023  | 

  * [Windows Server 2012 and 2012 R2 reaching end of support](https://learn.microsoft.com/en-us/lifecycle/announcements/windows-server-2012-r2-end-of-support)
  * [Performing an in-place upgrade of Windows Server](https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server)

  
Windows Server 2008 R2  | January 14, 2020  | 

  * [End of support for Windows Server 2008 and Windows Server 2008 R2](https://support.microsoft.com/en-us/help/4456235/end-of-support-for-windows-server-2008-and-windows-server-2008-r2)
  * [Performing an in-place upgrade of Windows Server](https://docs.cloud.google.com/compute/docs/tutorials/performing-in-place-upgrade-windows-server)

  
Windows Server 2008  | January 14, 2020  | 

  * [End of support for Windows Server 2008 and Windows Server 2008 R2](https://support.microsoft.com/en-us/help/4456235/end-of-support-for-windows-server-2008-and-windows-server-2008-r2)

  
Windows Server 2003 R2  | July 14, 2015  | 

  * [Windows Server 2003 extended support ended on July 14, 2015](https://www.microsoft.com/en-us/cloud-platform/windows-server-2003)
  * [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine)

  
Windows Server 2003  | July 14, 2015  | 

  * [Windows Server 2003 extended support ended on July 14, 2015](https://www.microsoft.com/en-us/cloud-platform/windows-server-2003)
  * [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine)

  
  
## What's next

  * Learn about the [licensing options for Microsoft software](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) on Compute Engine.

  * Learn more about the [operating system images](https://docs.cloud.google.com/compute/docs/images) that Compute Engine provides.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
