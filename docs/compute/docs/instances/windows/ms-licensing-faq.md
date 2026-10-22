---
url: https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq/
title: Microsoft licensing on Google Cloud FAQ \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:46.608806+00:00
---

# Microsoft licensing on Google Cloud FAQ  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Microsoft licensing on Google Cloud FAQ Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the most frequently asked questions (FAQ) about licensing for the following Microsoft workloads on Google Cloud:

  * Windows Server FAQ
  * SQL Server FAQ
  * Windows Desktop OS FAQ
  * Microsoft Office FAQ



## Windows Server on Google Cloud FAQ

#### What are my options for running Windows Server on Google Cloud?

Windows Server is available using on-demand licenses available on prebuilt images in Compute Engine, or as an attached license string to custom images during image import. Additionally, you might be able to bring your own license (BYOL) of a Windows Server if it meets the eligibility requirements. For more information, see BYOL Windows Server FAQ.

### On-demand Windows Server FAQ

#### How do I use on-demand licensing on my Windows Server instances?

There are two primary ways to enable on-demand licensing for your instances:

  * **Prebuilt images from Google Cloud:** When you use a prebuilt Windows Server, or SQL Server image from the [Compute Engine image catalog](https://console.cloud.google.com/compute/images), or from [Google Cloud Marketplace](https://console.cloud.google.com/marketplace), Google provides an on-demand license and attaches it to the image. Google Cloud manages the reporting and compliance requirements so that you can get started with these Microsoft products quickly.
  * **Custom images:** When you bring your own Windows Server or SQL Server image, you can attach a Google-provided on-demand license during the [import](https://docs.cloud.google.com/compute/docs/licenses/view-append) or [migration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#licensing) process. The **License** section of the **Operating system details** page for [Windows Server](https://docs.cloud.google.com/compute/docs/images/os-details#windows_server) and [SQL Server](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server) contains license strings for each software version. If you use Google-provided on-demand licenses for SQL Server on Windows Server, you must attach a license string for each software.



#### How does billing for on-demand Windows Server instances work?

When you create a Windows Server or SQL Server instance that includes on-demand licensing, Microsoft Windows Server license stock-keeping units (SKUs) are added alongside the base Compute Engine resource SKUs. A core license is charged for each virtual CPU enabled in the instance. Reducing the number of virtual CPUs in your instance by [disabling simultaneous multithreading (SMT)](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) or [disabling cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores), or both, reduces the virtual CPU count on which licenses will be charged.

#### Who is responsible for the compliance and reporting of on-demand Windows Server licensing?

If you use on-demand licenses from Google, Google ensures compliance with the licensing requirements and manages the reporting of license usage.

#### Do I need to purchase user client access licenses (CALs) when I use an on-demand license for Windows Server?

No, the CALs and their cost are included with the OS image. You don't need to separately purchase user CALs. Active Directory domain controller instances running in a Managed Microsoft Active Directory domain, or any Windows instances that are domain-joined to such a domain also don't require any additional CALs. For more information, see [Managed Service for Microsoft Active Directory](https://docs.cloud.google.com/managed-microsoft-ad/docs).

#### Are Remote Desktop Services (RDS) CALs required for on-demand instances?

No, RDS CALs are not required for on-demand Windows Servers unless you need more than two concurrent remote desktop sessions for administrative purposes. If you need more than two concurrent remote desktop sessions, you must purchase additional RDS CALs. For more information, see [license your RDS deployment with CALs](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license).

### BYOL Windows Server FAQ

#### How do I know if my license for Windows Server is eligible for use on Google Cloud (BYOL)?

Your Windows Server license might be [eligible](https://www.microsoft.com/en-us/licensing/news/updated-licensing-rights-for-dedicated-cloud) for use on Google Cloud using [Outsourcing Software Management Rights](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#outsourcing-software-management) if it meets the following conditions, provided that you are not otherwise prevented from outsourcing the management of your software:

  * **Products released in 2019 or earlier:** The license covers a Microsoft product version released before October 1, 2019, which was the date that Microsoft announced a change to their license. For example, Windows 2019 might be eligible for BYOL with Outsourcing Management Rights, but Windows Server 2022 is not eligible.
  * **Acquired or effective before October 1, 2019:** You acquired the Microsoft license under an enrollment effective before October 1, 2019, OR you acquired the Microsoft license after October 1, 2019 under a [Microsoft's Enterprise Agreement True-up (PDF download)](https://www.microsoft.com/download/details.aspx?id=14452), for an enrollment with an effective date before October 1, 2019. This includes both the server licenses and any CALs.
  * **Sole-tenant nodes (dedicated hardware) are required:** You can only use software brought using Outsourcing Software Management Rights with dedicated servers such as [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses). Microsoft doesn't allow the use of Outsourcing Software Management Rights in a multi-tenant environment, and therefore you cannot use the software with the default tenancy for Compute Engine instances.



#### Is Windows Server covered by Software Assurance with License Mobility?

No, Windows server is not covered under License Mobility because License Mobility only applies to server applications, not the underlying operating system. For more information, see [Microsoft License Mobility](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/License-Mobility-through-Software-Assurance-Customer-Licensing-Guide.pdf).

#### What if I am eligible to run an earlier version of Windows Server on sole-tenant nodes, but later upgrade to version of Windows Server that was released after October 1, 2019?

When you upgrade to a version of Windows Server that was released after October 1, 2019, you are subject to Microsoft's licensing terms for that version. Under these conditions, your new license might not be eligible for BYOL to Google Cloud.

#### Are an instance's licenses altered when updating the tenancy of an instance?

When you [modify the tenancy](https://docs.cloud.google.com/compute/docs/nodes/updating-vm-tenancy) of an instance, Compute Engine does not alter its license. For any license that you bring to Google Cloud (BYOL), you are responsible for ensuring that the instance is using a tenancy model (sole-tenant or multi-tenant) that is compliant with your licensing agreement.

#### If I bring my own BYOL Windows Server license, do I need CALs?

Yes. If you bring your own Windows Server license, you are responsible for purchasing any required CALs. Depending on how you configure and use Windows Server, you might need additional CALs for Rights Management Services when they are used over RDP. For more information, see [License your RDS deployment with CALs](https://docs.microsoft.com/en-us/windows-server/remote/remote-desktop-services/rds-client-access-license).

#### If I bring my own BYOL Windows Server license to Compute Engine, how do I activate it?

If you import an image to Compute Engine that requires an existing license, you are responsible for activating the license. For more information, see [Bringing your own licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses). If you use an [on-demand image](https://docs.cloud.google.com/compute/docs/instances/windows), Google manages the license for you.

**What am I responsible for if I bring my own license (BYOL)?**

If you bring your own licenses to Compute Engine, you are responsible for ensuring compliance with Microsoft under your licensing terms.

**If I bring my own Windows Server license, can I apply my license by the core?**

If your Windows Server license is eligible for BYOL, then you might be able to use the license by the core as long as you meet the following criteria:

  * Per core licensing of Windows Server is only available on sole-tenant nodes.
  * For both Standard and Data center editions, the number of core licenses required equals the number of physical cores on the licensed server, subject to a minimum of 8 core licenses per physical processor, and a minimum of 16 core licenses per server. Core licenses are sold in 2-packs. For more information, see [Microsoft licensing brief](https://download.microsoft.com/download/3/d/4/3d42bdc2-6725-4b29-b75a-a5b04179958b/percorelicensing_definitions_vlbrief.pdf).



A Windows Server Standard license grants you the right to host two instances on the physical host, while the Datacenter license with per-core licensing grants you the right to host an unlimited number of instances on the physical host.

## SQL Server on Google Cloud FAQ

**What are my options for running SQL Server on Google Cloud?**

There are several ways to run SQL Server workloads on Google Cloud:

  * **On-demand SQL Server images from Google:** Prebuilt SQL Server images are available directly from Compute Engine in the Google Cloud console. These images are built on top of Windows Server and the licensing costs for both Windows Server and SQL Server are added as license SKUs alongside the base instance resource SKUs. For more information on the on-demand pricing model and getting started, see On-demand Windows Server FAQ.
  * **Bring Your Own License (BYOL) SQL Server:** If you have an existing SQL Server license for on-premise use, you might be able to bring this license to Google Cloud in the following scenarios: 
    * If you have Software Assurance with License Mobility, your SQL Server license might be eligible to run on default multi-tenant instances as long as the underlying operating system does not require the use of sole-tenant nodes.
    * If you don't have Software Assurance with License Mobility, then you can only bring your SQL Server license to Google Cloud on sole-tenant nodes, and only if your license meets the criteria for [Outsourcing Software Management Rights](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#outsourcing-software-management).
  * **Google-managed SQL Server:** Other options for running SQL Server include [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction), our Google-managed SQL Server offering, and [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine/docs/overview).



### On-demand SQL Server FAQ

#### How many SQL Server core licenses are charged for my instance?

Microsoft SQL Server licensing requires a core license to be assigned to each virtual CPU (vCPU) available to the guest operating system, with a minimum of four core licenses always being charged. Reducing the number of virtual CPUs available to the guest operating system by [disabling SMT](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core) or [disabling cores](https://docs.cloud.google.com/compute/docs/instances/customize-visible-cores), or both, reduces the number of core licenses that will be charged.

For example, a c4-standard-8 instance with default settings presents eight vCPUs to the guest operating system, and you are charged for eight core licenses.

If you set visible cores to three (with one core disabled), six vCPUs are presented to the guest operating system, and therefore, you are charged for six core licenses. If you next set threads per core to one (with SMT disabled), only three vCPUs are presented to the guest operating system. However, you are charged for four core licenses, as you will always be charged for a minimum of four core licenses.

In addition to the license charges, you are billed for the c4-standard-8 Compute Engine instance resources.

#### How are SQL Server failover clusters licensed?

When you use on-demand licenses for SQL Server, you must license all instances in the failover cluster, including passive instances.

#### Can I remove a SQL Server license from an existing instance?

Once you create or import an instance, you can't edit or delete the instance's metadata. Therefore, you can't remove SQL Server licenses that are attached to the instance.

### BYOL SQL Server FAQ

#### Is SQL Server covered by Software Assurance with License Mobility?

Yes, SQL Server is usually covered by License Mobility through Software Assurance. This means that if you have an active Software Assurance contract for your SQL Server licenses, you can move them to Google Cloud.

#### If I don't have Software Assurance with License Mobility, can I still bring my own SQL Server license (BYOL) to Google Cloud?

Without Software Assurance with License Mobility, you might be able to use your own SQL Server license (BYOL) if it meets the following requirements:

  * **Products released in 2019 or earlier:** The license covers a Microsoft product version released before October 1, 2019. For example, Windows 2019 might be eligible for BYOL with Outsourcing Management Rights, but Windows Server 2022 is not eligible.
  * **Acquired or effective before October 1, 2019:** You acquired the Microsoft license under an enrollment effective before October 1, 2019, OR you acquired the Microsoft license after October 1, 2019 under a [Microsoft's Enterprise Agreement True-up (PDF download)](https://www.microsoft.com/download/details.aspx?id=14452), for an enrollment with an effective date before October 1, 2019. This includes both the server licenses and any CALs.
  * **Sole-tenant nodes (dedicated hardware) are required:** You can only use software brought using Outsourcing Software Management Rights with dedicated servers such as [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses). Microsoft doesn't allow the use of Outsourcing Software Management Rights in a multi-tenant environment, and therefore you cannot use the software with the default tenancy for Compute Engine instances.



#### If I use License Mobility to bring my SQL Server workload to Google Cloud, does the instance need to run on dedicated hardware like sole-tenant nodes?

Workloads covered by License Mobility don't necessarily need to be placed on sole-tenant nodes, provided that:

  * The instance is solely dedicated to your use
  * The underlying operating system does not require a sole-tenant node



For example, an instance running BYOL SQL Server brought with License Mobility running on an on-demand Windows Server image from Google doesn't require sole-tenant nodes.

However, an instance running BYOL SQL Server brought with License Mobility running on a BYOL Windows Server image requires sole-tenancy. This is because the Windows Server operating system is not eligible for License Mobility and is subject to the restrictions of [Outsourcing Software Management Rights](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#outsourcing-software-management).

The following table lists tenancy options depending on how you bring your SQL Server to Google Cloud.

| On-Demand SQL Server | BYOL SQL Server - With License Mobility | BYOL SQL Server - Without License Mobility  
---|---|---|---  
**On-demand Windows Server** | Can run on multi-tenant instances or sole-tenant nodes. No version restrictions. | Can run on multi-tenant instances or sole-tenant nodes. No version restrictions. | Must run on sole-tenant nodes due to restrictions for outsourcing license management of SQL Server. Limited to SQL Server 2017 or earlier.  
**BYOL Windows Server** | Must run on sole-tenant nodes due to restrictions for outsourcing license management of BYOL Windows Server. Limited to Windows 2019 or earlier. | Must run on sole-tenant nodes due to restrictions for outsourcing license management of BYOL Windows Server. Limited to Windows 2019 or earlier. | Must run on sole-tenant nodes due to restrictions for outsourcing license management of BYOL Windows Server and BYOL SQL Server. Limited to SQL Server 2017 or earlier, and Windows 2019 or earlier.   
  
For more information, see [Microsoft License Mobility](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/License-Mobility-through-Software-Assurance-Customer-Licensing-Guide.pdf).

#### Can I use my own SQL Server license (BYOL) in an instance with a Google provided operating system?

If your SQL Server license meets the criteria for running on Google Cloud, you can install SQL Server yourself on a Windows Server or Linux image provided by Google. Costs for a [premium image](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages) such as Windows Server are charged appropriately.

#### How do I activate License Mobility for the Microsoft Workloads I bring to Google Cloud?

To use License Mobility, you must complete the license verification process, during which Microsoft ensures that your licenses are eligible for License Mobility. You can submit your License Mobility information for verification through Google or directly to Microsoft. Microsoft provides confirmation to you and to Google after verification is complete.

For specific information about your License Agreement, including how to determine your Microsoft Agreement Identifying Number, see [Microsoft's License Summary FAQ](https://docs.microsoft.com/en-us/licensing/license-faq).

  * **Submit License Mobility information through Google:**

Use the [License Mobility verification form](https://console.cloud.google.com/compute/ms-license-verification) to submit your License Mobility information through Google. You can access this form directly or when you are creating an instance in the Google Cloud console.

  * **Submit License Mobility information directly to Microsoft as follows:**

    * Visit [Microsoft's Volume Licensing Service Center](https://www.microsoft.com/Licensing/servicecenter/default.aspx).
    * Read the [License Mobility through Software Assurance Verification Guide for Customers (PDF download)](https://download.microsoft.com/download/7/9/b/79bd917e-760b-48b6-a266-796b3e47c47a/License_Mobility_Customer_Verification_Guide.pdf).
    * Specify Google as the Authorized Mobility Partner by using the following information:

      * Authorized Mobility Partner Name: Google LLC
      * Authorized Mobility Partner Website URL: https://cloud.google.com
      * Authorized Mobility Partner Email Address: google-ms-license-mobility@google.com



#### If I license my SQL Server license by the core, am I required to license a minimum number of cores?

Yes, a minimum of four core licenses are required for each physical processor on the server. When running SQL Server in a physical operating system environment, all physical cores on the server must be licensed. Software partitioning doesn't reduce the number of core licenses required, except when licensing individual instances. For more information, see [Microsoft licensing brief](https://download.microsoft.com/download/3/d/4/3d42bdc2-6725-4b29-b75a-a5b04179958b/percorelicensing_definitions_vlbrief.pdf).

#### Are passive failover rights provided when I use License Mobility through Software Assurance?

Rights for one failover instance (HA or DR) are provided by BYOL licenses that use License Mobility through Software Assurance. The failover instance must have the same or fewer virtual CPUs as the primary, and both instances must run on Google Cloud. If you want to use an Always On Availability Group secondary replica, it must be set to not-read.

#### If I use my own BYOL SQL Server license on sole-tenant nodes, are CALs required?

CALs are required if you bring your own server licenses. CALs are not required for bringing your own Core licenses.

#### If I use my own BYOL SQL Server license, can I upgrade to a later version of SQL Server?

If you use your Outsourcing Software Management Rights to bring your own SQL Server licenses to sole-tenant nodes, you cannot upgrade to a version released after October 1, 2019.

If you use License Mobility through Software Assurance to assign a SQL Server license to an instance on Google Cloud, there are no upgrade restrictions.

#### What licensing models are supported for SQL Server deployments running on sole-tenant nodes?

If you use your Outsourcing Software Management Rights to assign licenses to sole-tenant nodes, they can be licensed as follows:

  * Per-core
  * Per-processor
  * Per-server or per-CAL



#### Can I uninstall or reinstall SQL Server on a SQL Server instance with my existing license?

Yes, you can uninstall or reinstall SQL Server on a SQL Server instance with your existing license. The installation media for SQL Server is located at `C:\sql_server_install`.

Note that uninstalling SQL Server won't stop the SQL Server licensing charges.

#### Can I use my SQL Enterprise licenses for unlimited virtualization with License Mobility?

No. While SQL Enterprise per-core licenses can be used to license an unlimited number of SQL Server instances on a licensed server, that right does not extend to SQL Server instances covered by license mobility. Each instance must be covered individually.

## Windows Desktop OS FAQ

Windows Desktop OS is also known as Windows Client or Windows Enterprise. Some common versions include Windows 7, Windows 8, Windows 10, and Windows 11.

#### What are my options for running Windows Desktop operating systems on Google Cloud?

Your existing Windows Desktop OS license might be eligible for use on Google Cloud as long as you have an active Windows Enterprise VDA E3 or E5 subscription from Microsoft, and the instances run on sole-tenant nodes.

#### Can I purchase on-demand Windows Desktop OS licenses directly from Google Cloud?

No, Google Cloud does not provide Windows Desktop OS licenses.

#### Am I required to run my Windows Desktop OS instance on a sole-tenant node?

Yes, your instances with Windows Desktop OS can only run on dedicated hardware such as sole-tenant nodes.

#### Is Windows Desktop OS subject to the same Outsourcing Software Management restrictions as BYOL Windows Server?

No, the requirements for BYOL Windows Desktop OS are different from BYOL Windows Server. You are allowed to use your own Windows Desktop OS license on Google Cloud as long as you have an active Windows Enterprise VDA E3 or E5 subscriptions, and place the instance on a sole-tenant node.

## Microsoft Office FAQ

#### Can I bring my own Microsoft Office licenses to instances on Google Cloud?

Perpetual versions of Microsoft Office (Microsoft Office 2019 and earlier) are eligible for BYOL to Google Cloud, however these licenses are subject to the Outsourcing Software Management Rights requirements:

  * **Products released in 2019 or earlier:** The license covers a Microsoft product version released before October 1, 2019. For example, Windows 2019 might be eligible for BYOL with Outsourcing Management Rights, but Windows Server 2022 is not eligible.
  * **Acquired or effective before October 1, 2019:** You acquired the Microsoft license under an enrollment effective before October 1, 2019, OR you acquired the Microsoft license after October 1, 2019 under a [Microsoft's Enterprise Agreement True-up (PDF download)](https://www.microsoft.com/download/details.aspx?id=14452), for an enrollment with an effective date before October 1, 2019. This includes both the server licenses and any CALs.
  * **Sole-tenant nodes (dedicated hardware) are required:** You can only use software brought using Outsourcing Software Management Rights with dedicated servers such as [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses). Microsoft doesn't allow the use of Outsourcing Software Management Rights in a multi-tenant environment, and therefore you cannot use the software with the default tenancy for Compute Engine instances.



## End of support FAQ

#### How does Microsoft's support lifecycle work for Windows Server on Compute Engine?

Many Windows Server versions follow Microsoft's [Fixed Lifecycle Policy](https://learn.microsoft.com/en-us/lifecycle/policies/fixed), which includes two primary phases: Mainstream Support followed by Extended Support.

  * **Mainstream Support:** Typically lasts for 5 years. During this phase, Microsoft provides feature updates, security updates, and non-security updates.
  * **Extended Support:** Typically lasts for another 5 years after Mainstream Support ends. During this phase, Microsoft continues to provide **security updates at no additional cost**. However, new features and non-security updates are no longer released.
  * **End of Extended Support:** Once Extended Support ends, the product reaches its official End of Support. To continue receiving security updates, you must enroll in Microsoft's [Extended Security Update (ESU)](https://learn.microsoft.com/en-us/lifecycle/faq/extended-security-updates) program.



You can search for specific support dates for your Windows Server version using the [Microsoft Lifecycle Product Search](https://learn.microsoft.com/en-us/lifecycle/products/).

#### My instance is running a version of Windows Server that has reached the end of Extended Support. Can I configure it to receive Extended Security Updates (ESUs)?

Yes. If the Windows Server version has reached the end of its Extended Support phase (for example, Windows Server 2012 R2), you can purchase ESUs from Microsoft and configure your instances to receive them. For more details on ESU eligibility and activation, see the Microsoft [Extended Security Updates deployment guide](https://learn.microsoft.com/en-us/windows-server/get-started/extended-security-updates).

## Image Import FAQ

#### Can I customize the image import workflows?

Yes. You can customize the image import workflow. The image import workflows are available on GitHub.

#### Can I import images that are already running?

Yes. You can import images from instances that are online and running.

#### After I import my BYOL image, can I share it?

Yes. After importing your BYOL image, you can share it with users outside your project or organization. Then, they can access the shared images from their project. For more information, see [Managing access to custom images](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images).

## What's next

  * Learn about the [licensing options for Microsoft software](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing) on Compute Engine.

  * Learn more about [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes).

  * Learn more about the [operating system images](https://docs.cloud.google.com/compute/docs/images) that Compute Engine provides.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
