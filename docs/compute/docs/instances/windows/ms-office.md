---
url: https://docs.cloud.google.com/compute/docs/instances/windows/ms-office/
title: Use Microsoft Office with License Manager \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:25.691141+00:00
---

# Use Microsoft Office with License Manager  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/ms-office/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use Microsoft Office with License Manager Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

Learn how to configure and use Microsoft Office licenses on Google Cloud with License Manager. This page also covers supported versions, installation media deployment, and billing considerations.

## Supported versions of Microsoft Office

License Manager supports the following versions of Microsoft Office:

  * Microsoft Office LTSC 2021 Professional Plus: $21.40 per user per month
  * Microsoft Office LTSC 2024 Professional Plus: $21.40 per user per month

**Note:** Office LTSC products available on Google Cloud differ from Microsoft 365 Apps for enterprise. To review feature differences, see the Microsoft documentation for [Office LTSC 2021](https://learn.microsoft.com/en-us/office/ltsc/2021/overview) and [Office LTSC 2024](https://learn.microsoft.com/en-us/office/ltsc/2024/overview).

Microsoft Office LTSC is available on Compute Engine and Google Cloud VMware Engine.

For information about bringing your own license (BYOL) for Microsoft Office to Google Cloud, see the [Microsoft Licensing FAQ](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq).

## Before you begin

Before you begin, ensure you meet the following requirements:

  * Install Office LTSC on a Windows virtual machine (VM) running either a Windows Desktop OS or Windows Server.
  * For Google Cloud VMware Engine, verify that VMware Tools is installed on the Windows VM.
  * Ensure that your VM has outbound internet access during activation. Microsoft requires Office LTSC licenses from Service Provider License Agreement (SPLA) providers to activate over the internet directly with Microsoft servers. You can disable internet access after activation completes. For more information, see [Install the License Manager agent](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager#install-activate).



## Install Microsoft Office LTSC

Download the installation media for Office LTSC products directly from Microsoft by using the Office Deployment Tool (ODT). For deployment instructions, see the Microsoft guides for [Office LTSC 2021](https://learn.microsoft.com/en-us/office/ltsc/2021/deploy) and [Office LTSC 2024](https://learn.microsoft.com/en-us/office/ltsc/2024/deploy).

When configuring the `Product ID` attribute in your ODT `configuration.xml` file, specify the volume licensing product ID for your edition:

  * For Office LTSC 2021 Professional Plus, use `ProPlusSPLA2021Volume`.
  * For Office LTSC 2024 Professional Plus, use `ProPlus2024Volume`.



To migrate an existing VM from Office LTSC 2021 to Office LTSC 2024, see [Migrate from Office LTSC 2021 to Office LTSC 2024](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager#migrate-office-2024).

## Use your Microsoft Office licenses

License Manager manages and activates Microsoft Office licenses on Google Cloud. To enable your licenses, see [Get started with License Manager](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager#get-started).

**Note:** If you activate Microsoft Office on Google Cloud VMware Engine, then add the `vcenter_domain` property with your vCenter FQDN to the `conf/configuration.json` file when configuring the License Manager agent (for example, `"vcenter_domain": "vcenter.example.com"`).

## Billing considerations

Review the following billing considerations when using Microsoft Office licenses with License Manager on Google Cloud.

### Calendar month billing

License Manager bills Microsoft Office licenses by the calendar month in which they are authorized. Billing begins when you [create a license configuration](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager#create-license-configuration). License Manager does not prorate billing based on the creation date within the month.

If you deactivate a license configuration or reduce the license count, then you remain responsible for charges for the current calendar month. The reduction in authorized users takes effect at the start of the next calendar month.

When you increase the license count for an active license configuration, the increase takes effect immediately and appears on the current month's bill.

### Authorized access compared to actual access

License Manager bills licenses based on the number of authorized users, regardless of actual software usage. You must purchase licenses for all users authorized to access the VM, whether or not they sign in.

Authorization begins when you [create a license configuration](https://docs.cloud.google.com/compute/docs/instances/windows/license-manager#create-license-configuration). Verify that your configured license volume is accurate before creating the configuration, as you are billed for that amount for the current calendar month.

#### Enforced limits and overages

License Manager does not enforce hard limits on software access. You must ensure that the number of users accessing Microsoft Office does not exceed your authorized license count.

If License Manager detects that the number of users accessing VMs with Microsoft Office exceeds the authorized count in your license configuration, then Google Cloud treats the additional users as authorized and bills for the extra licenses in that calendar month.

## What's next

  * [Microsoft Licensing on Google Cloud](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing)
  * [Microsoft Licensing on Google Cloud FAQ](https://docs.cloud.google.com/compute/docs/instances/windows/ms-licensing-faq)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
