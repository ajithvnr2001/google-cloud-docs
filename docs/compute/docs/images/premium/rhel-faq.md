---
url: https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq/
title: Red Hat Enterprise Linux FAQ \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:43.968716+00:00
---

# Red Hat Enterprise Linux FAQ  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/premium/rhel-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Red Hat Enterprise Linux FAQ Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document covers frequently asked questions around support, migration and licenses when running Red Hat Enterprise Linux (RHEL) on Compute Engine.

## General FAQs

This section answers general questions about RHEL on Compute Engine.

### What is Red Hat Enterprise Linux on Compute Engine?

Red Hat Enterprise Linux on Compute Engine are any RHEL images that are optimized to run on Compute Engine. These RHEL images enable you to modernize your RHEL workloads on Google Cloud by taking advantage of the scalability, security, and performance of Compute Engine. For more information about Compute Engine, see the [Compute Engine overview](https://docs.cloud.google.com/compute).

The Red Hat Knowledgebase is a centralized location for accessing articles, solutions, product documentation, and community discussions. For VMs that use RHEL on Compute Engine, you can access the Red Hat Knowledgebase by using a single-sign-on (SSO) option that is [available through the Google Cloud console](https://docs.cloud.google.com/compute/docs/images/premium/access-rhel-knowledgebase).

### What versions of RHEL are available on Compute Engine?

For a full list of the RHEL versions that are available on Compute Engine, see [RHEL operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel).

### Is RHEL for SAP with high availability and update services available on Compute Engine?

Yes, RHEL for SAP with HA and update services is available on Compute Engine. For a full list of the RHEL versions that are available on Compute Engine, see [RHEL operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel).

### How are the public RHEL images made available on Compute Engine?

The RHEL images that are available on Compute Engine are built by Google in partnership with Red Hat.

For images that are in Red Hat's "Full and Maintenance support" phase, Google publishes image updates such as security and other updates as they are made available by Red Hat.

  * For more information about image updates, see the [RHEL: automatic updates](https://docs.cloud.google.com/compute/docs/images/os-details#auto-update-rhel) section on the operating system details page.
  * For detailed information about support phases, see the [Red Hat Enterprise Linux Life Cycle](https://access.redhat.com/support/policy/updates/errata).
  * For more information about images lifecycle on Compute Engine, see [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).



### Can I create RHEL VMs in my Google Cloud Free Trial account?

Yes, you can create RHEL VMs in Compute Engine in your [Free Trial Cloud Billing account](https://docs.cloud.google.com/free/docs/free-cloud-features#confirm-status-of-account).

You will incur charges for any Cloud Marketplace products and premium operating system licenses you use, even if your Compute Engine use is covered by Always Free. For more information, see [Google Cloud Marketplace products and Premium OS licenses](https://docs.cloud.google.com/free/docs/free-cloud-features#premium-os-and-marketplace). 

## Pricing FAQs

This section answers questions about RHEL pricing.

### How does billing work for RHEL VMs on Compute Engine?

There are two cost components for RHEL VMs running on Compute Engine:

  * Infrastructure costs for running your RHEL VMs in Compute Engine. For more information, see [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * Licensing costs for RHEL or RHEL for SAP. The following licensing options are available:

    * Pay-as-you-go model (PAYG) in Compute Engine. For this option, you pay Google directly.
    * Bring your own subscription (BYOS) using Red Hat Cloud Access. For this option, you use a subscription you have purchased from Red Hat.

For more information about licensing options on Compute Engine, see [Picking the right licensing model for your VMs](https://cloud.google.com/blog/products/compute/compute-engine-licensing-explained).




### What is the Red Hat Cloud Access program?

The Red Hat Cloud Access program lets you use eligible Red Hat product subscriptions on Compute Engine. It makes your subscriptions portable to Google Cloud.

You pay Red Hat for license subscriptions and pay Google Cloud only for infrastructure costs incurred. For more information, see [Red Hat Cloud Access program](https://www.redhat.com/en/technologies/cloud-computing/cloud-access).

### Do your prices include tax?

No, the prices listed are exclusive of applicable taxes and duties, including applicable VAT and applicable sales tax.

### What are my options to optimize subscription costs?

On January 26, 2024, [Red Hat announced a price model update](https://www.redhat.com/en/blog/red-hat-enterprise-linux-scalable-pricing-cloud-partners-announcement) on RHEL and RHEL for SAP for all Cloud providers. The new pricing model will be reflected on Compute Engine starting July 1, 2024. For the pricing changes, see [Premium images](https://docs.cloud.google.com/compute/all-pricing#premiumimages).

With this pricing update, the subscription costs to use on-demand RHEL and RHEL for SAP images scale by vCPU count. For VMs that use these images, we expect the following impact:

  * For VMs with more than 12 vCPUs, you should see an increase on your monthly subscription bill.
  * For VMs with 12 vCPUs or fewer, you should see a decrease on your monthly subscription bill.



If your VMs have more than 12 vCPUs, you can use these recommendations to optimize your costs:

  * **Use smaller VMs for your workloads**. You can assess your workloads and their resource requirements and determine if their performance needs can be met using smaller VMs. VMs with 12 vCPUs or fewer should see a decrease in subscription costs.
  * **Use Bring Your Own Subscription (BYOS)**. If you have existing on-premise subscriptions, you can [create your RHEL VMs using BYOS](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm). With BYOS, you pay Red Hat directly for licenses while only paying Google Cloud for infrastructure usage.

For BYOS support, contact Red Hat directly through the Red Hat Customer Portal.




### Are there any further cost optimizations available for running RHEL on Compute Engine?

In addition to the pay-as-you-go (PAYG) license model that lets you pay for only what you use, your infrastructure costs can be further reduced by taking advantage of [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). and [machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances).

You can also use the [pricing calculator](https://cloud.google.com/products/calculator) to estimate your costs of running VMs on Compute Engine.

## Support FAQs

This section answers common questions related to support for RHEL licenses.

### How is support offered for pay-as-you-go (PAYG) RHEL licenses on Compute Engine?

When you are running PAYG RHEL images on Compute Engine, access to Google Cloud Support is included in the contract. When you have issues with these images, contact Google Cloud Support. You don't need to contact Red Hat separately. Google will work with Red Hat to solve issues needing escalation.

Google Cloud offers different support packages to meet different needs, such as 24/7 coverage, phone support, and access to a technical support manager. For more information, see [Google Cloud Support](https://docs.cloud.google.com/support).

### How is support offered for bring your own subscription (BYOS) licenses on Compute Engine?

If you bring your own Red Hat Cloud Access subscription to Google Cloud, you will receive support directly from Red Hat.

To access support, file issues directly to Red Hat by logging into your [Red Hat Customer Portal](https://access.redhat.com/).

For detailed Red Hat product documentation, see the [Red Hat Customer Portal](https://access.redhat.com/documentation/en-us/).

### How to access BYOS images for RHEL while creating VMs?

You can create a VM instance on Compute Engine by using images from your [Red Hat Cloud Access subscription](https://www.redhat.com/en/technologies/cloud-computing/cloud-access). For detailed instructions, see [Create a VM using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm).

### How can I be notified when updates are available for RHEL?

To be notified when updates are made available by Red Hat, subscribe to [Red Hat Security Announcements](https://access.redhat.com/security/data/meta/v1/rhsa.rss).

All RHEL VMs running on Compute Engine receive updates shortly after these updates are made available from Red Hat. You can then install these updates by using standard RHEL packaging tools.

These updates are made available to the RHEL images that are provided by Compute Engine as outlined in the [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).

### How are updates and patches delivered for bring your own subscription (BYOS) licenses on Compute Engine?

RHEL BYOS images don't have access to Red Hat repository content. For VMs created with these images, you must manage repository content by using either [Red Hat Satellite or Red Hat Subscription Management](https://docs.redhat.com/en/documentation/red_hat_satellite/6.11/html/managing_content/managing_red_hat_subscriptions_content-management#Managing_Red_Hat_Subscriptions_content-management).

RHEL BYOS images have the Google RHUI client package installed by default. To receive updates from Red Hat Satellite or Red Hat Subscription Management, you must remove the Google RHUI client package. To remove the Google RHUI client package, run the following command:
    
    
    sudo yum remove google-rhui-client*
    

### Are there any restrictions on the machine types supported for RHEL on Compute Engine?

RHEL is supported by all machine types in all regions. For more information about machine types, see the [Machine types](https://docs.cloud.google.com/compute/docs/machine-resource).

In addition to the different machine configurations, RHEL can also be run on multi-tenant nodes or [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

### What are the SAP certified machine types on Compute Engine?

SAP and Google Cloud certify both major and minor releases of RHEL on the machine types that are available on Compute Engine.

For SAP HANA, SAP publishes the Compute Engine machine types and RHEL versions that are certified for Google Cloud in the [SAP HANA Hardware Directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29).

Google Cloud also publishes the SAP HANA certifications in [Certifications for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana).

For SAP NetWeaver, the certified machine types and operating systems are listed in [SAP Note 2456432](https://launchpad.support.sap.com/#/notes/2456432). To access this information, you need an SAP user account.

Google Cloud also publishes the SAP NetWeaver list in [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps).

### Does Google Cloud provide Extended Lifecycle Support for RHEL versions post the End of Maintenance phase?

Yes, Google does provide Extended Lifecycle Support (ELS) for End-of-Maintenance RHEL versions. ELS is available for RHEL 6, which reached its [end of maintenance (EOM)](https://docs.cloud.google.com/compute/docs/eol/rhel-eol) on November 30, 2020.

For more information, see [Appending RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses).

## License FAQs

This section answers questions about RHEL licenses.

### How does pay-as-you-go (PAYG) licenses work for RHEL on Compute Engine?

You pay for only what you use. This model lets you take advantage of Google Cloud's partnership with Red Hat for pay-as-you-go licenses that scale with your elastic workloads. This lets you pay for exactly what you need when your workloads spike, rather than paying a predetermined amount through fixed agreements.

RHEL licenses associated with these images are charged in one-second increments, with a one-minute minimum. To see additional pricing details, see the [premium images pricing documentation](https://docs.cloud.google.com/compute/disks-image-pricing#rhel_images).

Image options for PAYG:

  * Use Google Cloud's premium RHEL and RHEL for SAP with HA images that have PAYG licenses already attached.
  * Bring your own image into Google Cloud by using either [image import](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) or [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/getting-started) and attach a PAYG license to it.



All PAYG billing is handled through Google; there is no need for a separate agreement with Red Hat.

### How does the bring your own subscription (BYOS) license model work for RHEL on Compute Engine?

You will need an active [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access) subscription to specify your own license on RHEL images in Compute Engine.

To check whether your subscriptions are eligible for the Red Hat Cloud Access program, see the [Red Hat Cloud Access program overview](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/red_hat_cloud_access_reference_guide/red-hat-cloud-access-program-overview_cloud-access), and review the [entitlement unit conversion](https://docs.redhat.com/en/documentation/subscription_central/1-latest/html/red_hat_cloud_access_reference_guide/red-hat-cloud-access-program-overview_cloud-access#ref_ca-unit-conversion_cloud-access) for Red Hat Cloud Access subscriptions.

You will pay Google only for compute infrastructure costs and will have a separate license agreement with Red Hat.

### Can I switch from PAYG to BYOS or BYOS to PAYG?

Yes, switching between these two licensing options is supported on Compute Engine. For more information, see [Switch between PAYG and BYOS](https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos).

### Can I use Google provided RHEL images and specify a BYOS license?

Yes, you can use BYOS license with RHEL images on Compute Engine. For more information, see [Create a VM using a RHEL BYOS image](https://docs.cloud.google.com/compute/docs/instances/create-rhel-byos-vm).

## Migration FAQs

You can use your existing Red Hat Enterprise Linux (RHEL) images on Compute Engine. You can import RHEL images from your on-premises environment or other cloud providers into Compute Engine. You can also create new RHEL virtual machines (VMs) directly in Compute Engine.

### Can I use my own RHEL images on Compute Engine?

Yes, you can add VM instances, custom images, or disks that are available in an existing environment (such as on-premise or on other cloud providers) to Compute Engine. Multiple solutions are available to import your RHEL images to Google Cloud. For more information, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

You can also take advantage of your existing agreement with Red Hat and specify your own license while importing your images into Compute Engine. For this option, you will need an eligible [Red Hat Cloud Access](https://www.redhat.com/en/technologies/cloud-computing/cloud-access) subscription to specify your own license on RHEL images in Compute Engine.

### How do I get started with a RHEL VM on Compute Engine?

To create a new RHEL VM instance on Google Compute Engine, see the [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) guide. When creating the VM, on the public images tab, choose a RHEL version.

To migrate an instance running RHEL on-premise or on other clouds to Google Cloud, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

### I plan to migrate RHEL instances from AWS or Azure to Compute Engine. What is the recommended toolset or method to do so?

You can add VM instances, custom images, or disks that are available in an existing environment, such as on-premise or on other cloud providers, to Compute Engine.

To migrate an instance running RHEL on-premise or on other clouds to Google Cloud, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

### Is it possible to migrate RHEL on-demand VM instance to RHEL for SAP on-demand images?

**No.** The public guide available for [RedHat](https://access.redhat.com/solutions/34169) is valid for BYOS subscriptions and are not applicable for Compute Engine PAYG images.

## What's next

  * Learn more about the [operating system images](https://docs.cloud.google.com/compute/docs/images/os-details) that Compute Engine provides.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
