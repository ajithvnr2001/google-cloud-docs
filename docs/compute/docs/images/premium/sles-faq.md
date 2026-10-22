---
url: https://docs.cloud.google.com/compute/docs/images/premium/sles-faq/
title: SUSE Linux Enterprise Server FAQ \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:03.142786+00:00
---

# SUSE Linux Enterprise Server FAQ  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/premium/sles-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  SUSE Linux Enterprise Server FAQ Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document covers frequently asked questions around support, migration and licenses when running SUSE Linux Enterprise Server (SLES) on Compute Engine.

## General FAQs

This section answers general questions about SLES on Compute Engine.

### What is SLES on Compute Engine?

[SUSE Linux Enterprise Server (SLES)](https://www.suse.com/products/server) on Compute Engine are any SLES images that are optimized to run on Google Cloud. You can use these SLES images to migrate and modernize your SLES workloads on Google Cloud by taking advantage of the scalability, security, and performance of Compute Engine. For more information about Compute Engine, see the [Compute Engine overview](https://docs.cloud.google.com/compute).

### What versions of SLES are available on Compute Engine?

For a full list of the SUSE Linux Enterprise Server (SLES) versions that are available on Google Compute Engine, see [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#suse_linux_enterprise_server_sles).

### Is SLES for SAP Applications with high availability (HA) available on Compute Engine?

Yes, SLES for SAP Application with HA is available on Compute Engine. For a full list of the SLES versions that are available on Compute Engine, see [operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#suse_linux_enterprise_server_sles).

### What's the difference between SLES and SLES for SAP Applications?

[SUSE Linux Enterprise Server (SLES)](https://links.imagerelay.com/cdn/3404/ql/d656c9f6cee340aaad4790980ce2e988/suse_linux_enterprise_server_ds.pdf) is a highly scalable, secure and enterprise class performant enterprise operating system for general Linux workloads.

[SUSE Linux Enterprise Server (SLES) for SAP Applications](https://links.imagerelay.com/cdn/3404/ql/2e3a502eaa984bd1b0ce4c94cabb9440/suse_linux_enterprise_server_for_sap_applications_faq.pdf) is a Linux platform that is uniquely optimized for SAP Netweaver, SAP HANA and SAP S/4 HANA solutions with high availability, HANA replication, automation and monitoring components included.

### How are the public SLES images made available on Compute Engine?

SUSE, in partnership with Google, builds and maintains the SLES images that are available on Compute Engine. For images that are in SUSE's "General and Extended support" phase, SUSE publishes image updates such as CVE-security, packages, and other service pack updates.

  * For more information about image updates, see the [SLES: automatic updates](https://docs.cloud.google.com/compute/docs/images/os-details#auto-update-sles) section on the operating system details page.
  * For detailed information about support phases, see the [SUSE Linux Enterprise Server (SLES) Life Cycle](https://www.suse.com/support/policy-products/#cloud).
  * For more information about the image lifecycle on Compute Engine, see [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).



### Are there any differences between SLES on Google Cloud and other versions that I run in my data center?

Fundamentally, no. SUSE maintains the versions of SLES and SLES for SAP Applications that are available on Compute Engine, and the base OS is identical to the version of SLES available for installations on physical hardware. The versions available on Compute Engine include additional tooling and metadata that is needed to run and manage SLES VMs on the Google Cloud Platform.

### How does billing work for SLES VMs on Compute Engine?

There are two cost components for SLES VMs running on Compute Engine:

  * Infrastructure costs for running your SLES VMs on Compute Engine. For more information, see [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * Licensing costs for SLES or SLES for SAP. The following licensing options are available:

    * Pay-As-You-Go model (PAYG) on Compute Engine. For this option, you pay Google directly.
    * Committed Use Discounts. For this option, you purchase a commitment for your SLES or SLES for SAP licenses in return for discounted prices. Learn more about [resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) and [how to purchase resource-based commitments for OS licenses](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-license-commitments).
    * Bring your own subscription (BYOS) using. For this option, you use a subscription you have purchased directly from SUSE.



For more information about licensing options on Compute Engine, see [Picking the right licensing model for your VMs](https://cloud.google.com/blog/products/compute/compute-engine-licensing-explained).

### What is the SUSE BYOS (Bring Your Own Subscription) program?

Use the SUSE BYOS program to bring eligible SUSE product subscriptions to Google Cloud. With this option, you pay SUSE directly for license subscriptions and pay Google Cloud only for infrastructure costs incurred. For more information on how to buy, see [SUSE](https://www.suse.com/shop/).

### Are there any additional cost optimizations available for running SUSE on Compute Engine?

In addition to the pay-as-you-go (PAYG) license model that lets you pay for only what you use, your infrastructure costs can be further reduced by taking advantage of [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

[Machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-machine-type-recommendations-for-instances) also reduce your costs by helping you optimize resource usage.

You can also use the [pricing calculator](https://cloud.google.com/products/calculator) to estimate your costs of running VMs on Compute Engine.

### Do your prices include tax?

No, the prices listed are exclusive of applicable taxes and duties, including applicable VAT, and applicable sales tax.

### Can I create SLES VMs in my Google Cloud Free Trial account?

Yes, you can create SLES VMs in your [Free Trial Cloud Billing account](https://docs.cloud.google.com/free/docs/free-cloud-features#confirm-status-of-account).

You will incur charges for any Cloud Marketplace products and premium operating system licenses that you use, even if your Compute Engine use is covered by Always Free. For more information, see [Google Cloud Marketplace products and Premium OS licenses](https://docs.cloud.google.com/free/docs/free-cloud-features#premium-os-and-marketplace).

### How can my SLES VMs connect to SUSE update servers without a proxy or an external IP address?

SLES VMs on Compute Engine don't support non-transparent proxies or person-in-the-middle (PITM) proxies. Therefore, the best practice is to rely on an internal, centralized update architecture.

Instead of using Subscription Management Tool (SMT), which has been deprecated and removed, we recommend deploying a [SUSE Multi-Linux Manager](https://documentation.suse.com/multi-linux-manager/5.2/en/docs/index.html) (SMLM) server or a [Repository Mirroring Tool (RMT)](https://documentation.suse.com/sles/15-SP7/html/SLES-all/book-rmt.html) in your Virtual Private Cloud (VPC) network.

With this architecture, your SLES VMs without external IP addresses can connect directly and securely to the internal update server (RMT or SMLM) using their internal IP addresses. In turn, only the RMT or SMLM server requires outbound internet access (for example, using Cloud NAT) to communicate with the SUSE Customer Center and fetch updates on behalf of your VMs.

### What is SUSE Multi-Linux Manager (SMLM), and what are the benefits of using it in my Google Cloud environment?

[SUSE Multi-Linux Manager](https://www.suse.com/products/multi-linux-manager/) (formerly SUSE Manager) is an advanced, comprehensive infrastructure management platform for system lifecycle management, automated patch deployment, configuration management, and security compliance. It provides several strategic benefits for customers on Google Cloud, including the following:

  * **Efficient management at scale** : It provides a single pane of glass that simplifies the management of medium- to large-sized environments, significantly reducing operational overhead.
  * **Multi-Linux distribution support** : It isn't limited to SLES. You can manage multiple Linux distributions (including RHEL, Ubuntu, and others) from a single centralized interface, unifying operations across diverse environments.
  * **Bypassing network and proxy limitations** : It serves as a secure internal hub for distributing updates within your VPC network. This eliminates the need to expose your VMs to the internet or contend with the complexities of unsupported proxies.



### Is SUSE Multi-Linux Manager free for SLES for SAP customers on Google Cloud?

Customers running 10 or more SLES for SAP Applications VMs on Google Cloud are [entitled to a free SUSE Multi-Linux Manager subscription](https://documentation.suse.com/multi-linux-manager/5.2/en/docs/specialized-guides/public-cloud-guide/payg/payg-overview.html#_introduction_to_payg) to manage those instances, avoiding additional licensing costs.

### How can I get SUSE Multi-Linux Manager from the Google Cloud Marketplace?

You can purchase SUSE Multi-Linux Manager through the Google Cloud Marketplace by completing the following steps:

  1. In the Google Cloud console, go to the **Cloud Marketplace** page, and then search for `SUSE Multi-Linux Manager`.
  2. Select the **SUSE Multi-Linux Manager** image, and then click **Deploy**.



### Is there a SUSE-specific guide for deploying SUSE Multi-Linux Manager on Google Cloud?

Yes, SUSE provides the following resources and documentation to help you deploy SUSE Multi-Linux Manager (SMLM) on Google Cloud:

  * For a practical, step-by-step walkthrough, read the SUSE blog post [Deploy SUSE Multi-Linux Manager on Google Cloud](https://www.suse.com/c/deploy-suse-multi-linux-manager-google-cloud/).
  * For comprehensive, official technical documentation, see the [SUSE Multi-Linux Manager Public Cloud Guide](https://documentation.suse.com/multi-linux-manager/5.2/en/docs/specialized-guides/public-cloud-guide/overview.html).



## Support FAQs

This section answers questions about the support that you get for SLES on Compute Engine.

### How is support offered for Pay-As-You-Go (PAYG) SLES licenses on Compute Engine?

When you are running PAYG SUSE images on Compute Engine, support for issues with the images is included in [Google Cloud Support packages](https://docs.cloud.google.com/support) when the image is [GA](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#ga). If the image is [EOL](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#deprecated), Google Cloud support doesn't support the image.

If you have issues with GA images, contact Google Cloud Support. You don't need to contact SUSE separately. Google works with SUSE to resolve issues needing escalation. If you have issues with images that are related to LTSS, you must contact SUSE directly.

### How is support offered for Bring Your Own Subscription (BYOS) licenses on Compute Engine?

If you bring your own SUSE subscription to Google Cloud, you will receive support directly from SUSE. To access support, file issues directly to SUSE by logging into your [SUSE Customer Center](https://scc.suse.com/login). For access and more details, see the [SUSE Technical Support Documentation](https://www.suse.com/support/handbook/).

### How can I be notified when security updates are available for SLES?

To be notified when security updates are made available by SUSE, subscribe to [SUSE Security Announcements](https://www.suse.com/support/update/).

All SLES VMs running on Compute Engine receive updates shortly after these updates are made available from SUSE Public Cloud update infrastructure. You can then install these updates by using standard SLES packaging tools like `Zypper` or `YaST`. These patches and updates are made available for the SUSE images on a regular schedule as outlined in the [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).

### Are there any restrictions on the machine types supported for SUSE on Compute Engine?

SLES offerings are supported for all machine types in all regions. For more information about machine types, see [Machine types](https://docs.cloud.google.com/compute/docs/machine-resource). In addition to the different machine configurations, SLES offerings can also be run on multi tenant nodes or [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

### What are the SAP certified machine types on Compute Engine?

SAP and Google Cloud certify both major and minor releases of SLES on the machine types that are available on Compute Engine.

For SAP HANA, SAP publishes the Compute Engine machine types and SLES versions that are certified for Google Cloud in the [SAP HANA Hardware Directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29).

Google Cloud also publishes the SAP HANA certifications in [Certifications for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-hana).

For SAP NetWeaver, the certified machine types and operating systems are listed in [SAP Note 2456432](https://launchpad.support.sap.com/#/notes/2456432). To access this information, you need an SAP user account.

Google Cloud also publishes the SAP NetWeaver list in [Certifications for SAP applications on Google Cloud](https://docs.cloud.google.com/sap/docs/certifications-sap-apps).

### Does SUSE provide Long Term or Extended service pack Overlay Support for SLES versions?

Yes, but support varies for SLES and SLES for SAP.

  * **SLES** : SUSE provides [Long-Term Service Pack Support (LTSS) through the Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-ltss) for SLES versions that have reached their end of general support date. For more details, review the [SUSE Product Support Lifecycle](https://www.suse.com/lifecycle/).

  * **SLES for SAP** : SUSE provides Extended service pack Overlap Support (ESPOS) for SLES for SAP versions that have reached their end of general support date. ESPOS is included in the base pay-as-you-go (PAYG) license for all SLES for SAP versions except for the last SP version before the next major version release.

Extended service pack Overlap Support (ESPOS) provides an additional 3 years support for a specific SP version. During this period, you receive support and all relevant maintenance updates under the terms of Long-Term service pack Support (LTSS) - without needing to get the additional LTSS add-on. For more details, review the [SUSE Product Support Lifecycle](https://www.suse.com/lifecycle/).

ESPOS isn't offered for the last SP version before the next major version release. For example, the last SP version of SLES 12 for SAP is SP5, thus ESPOS isn't available for this version. If you require extended support for these images, you must purchase [Long-Term service pack Support (LTSS) through the Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-ltss).




### How to purchase and enable LTSS?

To purchase LTSS for your SLES and SLES for SAP instances, go to the [Long-Term service pack Support Google Cloud Marketplace listing](https://console.cloud.google.com/marketplace/product/mp-images-public/suse-ltss) and fill out the form.

A SUSE representative will contact you to complete the purchase. After the purchase is finalized, enable LTSS by following the instructions in [SUSE's documentation](https://www.suse.com/support/kb/doc/?id=000021193).

To learn more about the enablement process, see [Long Term service pack Support for PAYG Instances Simplified](https://www.suse.com/c/long-term-service-pack-support-for-payg-instances-simplified/).

## License FAQs

This section answers questions about SLES licenses.

### How does pay-as-you-go (PAYG) licenses work for SLES on Compute Engine?

With PAYG, you pay for only what you use. With this model you can take advantage of Google Cloud's partnership with SUSE for PAYG licenses that scales with your elastic workloads. With this option you pay for exactly what you need when your workloads spike, rather than paying a predetermined amount through fixed agreements. SUSE licenses associated with these images are charged in one-second increments, with a one minute minimum. To see additional pricing details, see the [premium images pricing documentation](https://docs.cloud.google.com/compute/disks-image-pricing#sles_images).

Image options for PAYG:

  * Use Google Cloud's premium SLES and SLES for SAP with HA images that have PAYG licenses already attached.
  * Bring your own image into Google Cloud by using either [Image import](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) or [Migrate for Compute Engine](https://docs.cloud.google.com/migrate/compute-engine/docs/4.11/getting-started) and attach a PAYG license to it.



All PAYG billing is handled through Google; there is no need for a separate agreement with SUSE.

### If I create a VM using a PAYG SLES image and prepare a custom image from that VM, will new VMs created from that custom image be PAYG?

Yes, the VMs deployed using a custom image created from a PAYG SLES VM are also PAYG SLES VMs.

### If I create multiple VMs from a snapshot of a PAYG SLES image, will the new VMs also have PAYG licensing for SUSE?

Yes, the new VMs created from the snapshot of an original PAYG SUSE Linux Enterprise Server VM's boot disk are also SUSE PAYG VMs.

### How does the Bring Your Own Subscription (BYOS) license model work for SLES on Compute Engine?

You will need an active [SUSE](https://www.suse.com/shop/) subscription to specify your own license on SLES images on Compute Engine.

To check whether your subscriptions are eligible for the SUSE BYOS to Google Cloud, contact `google [at] suse.com`. You will pay Google only for compute infrastructure costs and will have a separate license agreement with SUSE.

### Can I switch from PAYG to BYOS or BYOS to PAYG?

Yes, switching between these two licensing options is supported on Compute Engine. For more information, see [Switch between PAYG and BYOS](https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos).

### If I perform an in-place major OS upgrade on my SLES instance (for example, from SLES 12 to SLES 15), will the license attached to the Compute Engine VM automatically update?

No, the license attached to the Compute Engine VM's root disk doesn't automatically update when you perform an in-place operating system major version upgrade, such as from SLES 12 to SLES 15.

However, Google Cloud lets you manually update the license indicator after the operating system upgrade is complete, provided you remain within the same product and licensing, such as PAYG to PAYG or BYOS to BYOS.

To update the license after the OS upgrade, use the `gcloud compute disks update` command with the `--replace-license` flag. This command updates the license URI on the disk to match the new SLES version. For example, if you upgraded a PAYG instance from SLES 12 to SLES 15, you update the license from `.../sles-12` to `.../sles-15`. For more information on updating the license, see [Switch between PAYG and BYOS licenses](https://docs.cloud.google.com/compute/docs/licenses/switch-between-payg-and-byos).

### Can I perform an in-place service pack (SP) upgrade on my SLES instance?

Yes, you can perform in-place SP upgrades on your SLES Pay-As-You-Go (PAYG) instances, for example, from SLES 15 SP4 to SLES 15 SP5. SP upgrades don't require changes to the license attached to your VM. For instructions on how to perform an SP upgrade, see the upgrade guide for your version in the [SUSE Linux Enterprise Server documentation](https://www.suse.com/documentation/sles/).

### Can I use Google provided SLES images and specify a BYOS license?

Yes, you can use BYOS with Google Cloud provided SLES images. To do this, contact your Google Cloud account representative.

## Migration FAQs

This section answers questions about migrating to Compute Engine with a SLES image.

### Can I use my own SLES images on Compute Engine?

Yes, you can add VM instances, custom images, or disks that are available in an existing environment (such as on-premise or on other cloud providers) to Compute Engine. Multiple solutions are available to import your SLES images to Google Cloud. For more information, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

You can also take advantage of your existing agreement with SUSE and specify your own license while importing your images into Compute Engine. For this option, you need an eligible [SUSE](https://www.suse.com/shop/) subscription to specify your own license on Compute Engine.

### How do I get started with a SLES VM on Compute Engine?

To create a new SUSE SLES VM instance on Compute Engine, see the [quickstart guide](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) guide. When creating the VM, on the public images tab, choose a SLES version.

To migrate an instance running SLES on-premise or on other clouds to Google Cloud, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

### I plan to migrate SLES VMs from AWS or Azure to Compute Engine. What is the recommended toolset or method to do so?

You can add VM instances, custom images, or disks that are available in an existing environment, such as on-premise or on other cloud providers, to Compute Engine.

To migrate a VM running SLES on-premise or on other clouds to Google Cloud, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

### Is it possible to migrate SLES on-demand VM instance to SLES for SAP on-demand images?

**No.** The public guide available for [SUSE](https://www.suse.com/support/kb/doc/?id=000018895) is valid for BYO subscriptions and are not applicable for Compute Engine PAYG images.

## What's next

  * Learn more about the [operating system images](https://docs.cloud.google.com/compute/docs/images/os-details) that Compute Engine provides.

  * If you encountered any problems with registration of your SUSE products, read about [Troubleshooting SLES PAYG registration](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suse-registration).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
