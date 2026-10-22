---
url: https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing/
title: Microsoft Licensing on Google Cloud \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:01.650603+00:00
---

# Microsoft Licensing on Google Cloud  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Microsoft Licensing on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

Google Cloud is committed to providing an enterprise-class experience for Microsoft workloads to meet the needs of your organization. This page documents the most common concepts and questions related to Microsoft licensing and best practices.

**Types of Microsoft Licensing**

Microsoft licensing on Google Cloud generally falls into two categories:

  * On-demand Licenses from Google Cloud
  * Bring Your Own License (BYOL)



## On-demand Licenses from Google Cloud

The on-demand licensing model lets you pay for Microsoft licenses directly from Google Cloud, and only pay for the licensing costs on the resources you consume. This simplifies deployment because you don't need to manage separate licensing agreements and billing with Microsoft.

### On-demand licenses for prebuilt and custom images

On-demand licenses are available directly from prebuilt images provided by Google Cloud in the Google Cloud console. You can also attach an on-demand license to your custom image during the image import process. Google Cloud provides on-demand licenses for the following Microsoft products:

  * Windows Server
  * SQL Server



The following are the potential advantages of on-demand licenses:

  * **Simplified billing and compliance:** Google handles the licensing and you pay an hourly fee that includes both the base compute cost and the Microsoft license.
  * **No upfront investment:** You don't need to purchase licenses in advance, making it ideal for short-term projects, testing, or scaling needs.
  * **Automatic updates:** Google handles software updates and patches, potentially easing administrative burden.
  * **Get started quickly:** If you don't have existing Microsoft licenses, on-demand licenses on Google Cloud offer a quick way to get started with Microsoft products without additional licensing agreements.



## Bring Your Own License (BYOL)

If you have existing Microsoft licenses being used in your on-premises data centers, you might be eligible to use them with Google Cloud. When using your existing licenses on a resource in Google Cloud, you are only billed for the Compute Engine infrastructure that you consume for that resource. For example, a virtual machine (VM) running your own BYOL-eligible Windows Server license will only accrue infrastructure costs, but no additional Windows Server licensing costs are applied.

The following are the potential advantages of using your own license:

  * **Cost savings:** If you have existing licenses with active software assurance, you might save costs compared to Google's on-demand licensing, especially for long-term, stable workloads. However, if your licenses require dedicated hardware with sole-tenant nodes, you might need to factor in this additional cost to your Google Cloud deployment.
  * **Hybrid-cloud flexibility:** In some scenarios, BYOL can offer flexibility in how you deploy and manage your Microsoft workloads in a multicloud or hybrid cloud scenario.



### Every licensing situation is unique

While this page attempts to give an overview of using your own Microsoft license on Google Cloud, there are many possible situations that are unique to your use case and licensing agreements with Microsoft.

You are responsible for ensuring that use of your licenses is compliant with your agreement with Microsoft, and any potential advantages are dependent upon your specific terms and workload.

For an in-depth assessment of your licenses or software rights, work with your legal team, license vendor, or consult the [Microsoft Licensing Guide for Google Cloud (PDF download)](https://services.google.com/fh/files/misc/softwareone-msft-guide.pdf).

## Common options for BYOL Microsoft licenses on Google Cloud

There are two common pathways for using your own Microsoft licenses on Google Cloud:

  * Software Assurance with License Mobility
  * Outsourcing Software Management Rights



### Software Assurance with License Mobility

**Software Assurance** is an add-on program from Microsoft that you can purchase alongside core Microsoft software licenses through volume licensing agreements. Think of it as a premium upgrade package for your Microsoft licenses, offering a range of benefits beyond the license itself.

**License Mobility** is one of the included benefits of Software Assurance. It helps you transition your Microsoft application servers to Google Cloud using perpetual or term subscription licenses acquired through their Microsoft volume licensing agreements.

### Products eligible for License Mobility

Not all Microsoft products are eligible for BYOL with License Mobility. Application server licenses like SQL Server and Sharepoint Server are typically eligible for BYOL with License Mobility. Windows Server licenses are typically not eligible for BYOL using License Mobility, but might be eligible for BYOL by Outsourcing Software Management Rights. For more information on determining the eligibility of your Windows Server licenses, see [BYOL Windows Server FAQs](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq#byol-windows-server).

For the most up to date complete list of products covered by License Mobility, see [Microsoft's Resources for Software Assurance](https://www.microsoft.com/en-us/licensing/licensing-programs/software-assurance-learn-more).

### Additional information

With License Mobility, you are responsible for managing true ups and renewals according to your agreements. For the licenses to remain valid, you must maintain Software Assurance coverage with Microsoft.

License Mobility is subject to the following restrictions:

  * You must be an existing Microsoft Volume Licensing customer with [eligible server applications](https://www.microsoft.com/licensing/terms/) that are covered by active Software Assurance contracts with License Mobility.
  * You must maintain appropriate Client Access Licenses (CALs) with Software Assurance in your Volume Licensing agreement.
  * After deploying a license within a [region](https://docs.cloud.google.com/compute/docs/regions-zones), you cannot move that license to another region for 90 days. For more information, see the [Microsoft Product Terms site](https://www.microsoft.com/licensing/terms/).



## Outsourcing Software Management Rights

Some Microsoft products are eligible for BYOL without Software Assurance. This option can be useful when you want to use your own licenses on Google Cloud for products that are not covered by License Mobility, such as Windows Server 2019.

Check your agreement with Microsoft to determine whether your Outsourcing Software Management Rights provide flexibility on where you can run your workload.

Your Windows Server license might be [eligible](https://www.microsoft.com/en-us/licensing/news/updated-licensing-rights-for-dedicated-cloud) for use on Google Cloud using [Outsourcing Software Management Rights](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing#outsourcing-software-management) if it meets the following conditions, provided that you are not otherwise prevented from outsourcing the management of your software:

  * **Products released in 2019 or earlier:** The license covers a Microsoft product version released before October 1, 2019. For example, Windows 2019 might be eligible for BYOL with Outsourcing Software Management Rights, but Windows Server 2022 is not eligible.
  * **Acquired or effective before October 1, 2019:** You acquired the Microsoft license under an enrollment effective before October 1, 2019, OR you acquired the Microsoft license after October 1, 2019 under a [Microsoft's Enterprise Agreement True-up (PDF download)](https://www.microsoft.com/download/details.aspx?id=14452), for an enrollment with an effective date before October 1, 2019. This includes both the server licenses and any CALs.
  * **Sole-tenant nodes (dedicated hardware) are required:** You can only use software brought using Outsourcing Software Management Rights with dedicated servers such as [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses). Microsoft doesn't allow the use of Outsourcing Software Management right in a multi-tenant environment, and therefore you cannot use the software with the default tenancy for Compute Engine VMs.



## What's next

  * Read the [Microsoft licensing FAQ](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq).

  * Learn more about [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes).

  * Learn more about the [operating system images](https://docs.cloud.google.com/compute/docs/images) that Compute Engine provides.

  * Estimate the costs of your project by doing the following:

    * Using the [Pricing calculator](https://cloud.google.com/products/calculator).

    * Viewing the estimated costs of your instances and resources when you create them in the [Google Cloud console](https://console.cloud.google.com/).

    * Viewing and downloading prices from the pricing table in the [Google Cloud console](https://docs.cloud.google.com/billing/docs/how-to/pricing-table).

    * Accessing pricing information programmatically by using the [Cloud Billing API](https://docs.cloud.google.com/billing/v1/getting-started).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
