---
url: https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq/
title: Ubuntu Pro FAQ \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:52.712860+00:00
---

# Ubuntu Pro FAQ  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro-faq/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Ubuntu Pro FAQ Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

Get answers to common questions about support, migration, and software licensing for Ubuntu Pro on Compute Engine. This guide helps you manage your Ubuntu Pro deployments on Google Cloud.

## General FAQs

This section answers general questions about Ubuntu Pro on Compute Engine.

### What is Ubuntu Pro on Compute Engine?

Ubuntu Pro is a version of Ubuntu offered by Canonical for public clouds, focused on enterprise and production use. It is based on Ubuntu components but comes with a set of additional services that are activated out of the box. Ubuntu Pro also provides [Extended Security Maintenance (ESM)](https://ubuntu.com/security/esm).

Ubuntu Pro on Compute Engine images are optimized to run on Google Cloud. For more information see [Ubuntu Pro for Google Cloud](https://ubuntu.com/gcp/pro).

### What is Ubuntu Advantage?

[Ubuntu Advantage](https://ubuntu.com/legal/ubuntu-advantage-service-description) is Canonical's service package for Ubuntu. It offers tiered levels of support for desktop, server and cloud deployments.

Subscriptions available are as follows:

  * [Ubuntu Advantage Essential](https://ubuntu.com/legal/ubuntu-advantage-service-description#uasd-essential) \- no phone or ticket support available
  * [Ubuntu Advantage Standard](https://ubuntu.com/legal/ubuntu-advantage-service-description#uasd-standard-and-advanced) \- 24/5 phone and ticket support available
  * [Ubuntu Advantage Advanced](https://ubuntu.com/legal/ubuntu-advantage-service-description#uasd-standard-and-advanced) \- 24/7 phone and ticket support available



### Do I need to get Ubuntu Advantage for support?

If you need 24/5 or 24/7 phone and ticket support, you should subscribe to Ubuntu Advantage Standard or Advanced. To subscribe, see the [Ubuntu Advantage](https://ubuntu.com/support#get-in-touch) support documentation.

### What versions of Ubuntu Pro are available on Compute Engine?

For a full list of the Ubuntu Pro versions that are available on Compute Engine, see [Ubuntu Pro operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro).

### How are the public Ubuntu Pro images made available on Compute Engine?

Canonical, in partnership with Google, builds the Ubuntu Pro images that are available on Compute Engine.

For more information about image updates, see the [Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro) section on the operating system details page.

For detailed information about support phases, see [Ubuntu Lifecycle and Release Cadence](https://ubuntu.com/about/release-cycle).

For more information about the image lifecycle on Compute Engine, see [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).

### How does billing work for Ubuntu Pro on Compute Engine?

There are two cost components for Ubuntu Pro images running on Compute Engine:

  * Infrastructure costs for running your Ubuntu Pro VMs in Compute Engine. For more information, see [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * Licensing costs for Ubuntu Pro. The following licensing option is available:

    * Pay as you go model (PAYG) in Compute Engine. You pay Google directly for this option.

For information about licensing cost, see the [Ubuntu Pro](https://docs.cloud.google.com/compute/disks-image-pricing#ubuntu_pro_pricing) section in the premium images pricing documentation.




### Are there any additional cost optimizations available for running Ubuntu Pro on Compute Engine?

In addition to the pay-as-you-go (PAYG) license model that lets you pay for only what you use, your infrastructure costs can be further reduced by taking advantage of [committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts).

[Machine type recommendations](https://docs.cloud.google.com/compute/docs/instances/apply-sizing-recommendations-for-instances) also reduce your costs by helping you optimize resource usage.

You can also use the [pricing calculator](https://cloud.google.com/products/calculator) to estimate your costs of running VMs on Compute Engine.

### Do your prices include tax?

No, the prices listed are exclusive of applicable taxes and duties, including applicable VAT and applicable sales tax.

### Can I create Ubuntu Pro images in my Google Cloud Free Trial account?

Yes, you can create Ubuntu Pro VMs in Compute Engine on your [Free Trial Cloud Billing account](https://docs.cloud.google.com/free/docs/free-cloud-features#confirm-status-of-account).

You will incur charges for any Cloud Marketplace products and premium operating system licenses you use, even if your Compute Engine use is covered by Always Free. For more information, see [Google Cloud Marketplace products and Premium OS licenses](https://docs.cloud.google.com/free/docs/free-cloud-features#premium-os-and-marketplace).

## Support FAQs

This section answers questions about the support that you get for Ubuntu Pro on Compute Engine.

### How is support offered for pay-as-you-go (PAYG) Ubuntu Pro licenses on Compute Engine?

Google provides support for Google-specific configuration and for the Google platform that the Ubuntu Pro images run on. To leverage this infrastructure support, Google Cloud offers different support packages to meet different needs, such as 24/7 coverage, phone support, and access to a technical support manager. For more information, see [Google Cloud Support](https://docs.cloud.google.com/support).

However, for support on the Ubuntu Pro images themselves, you need to contact Canonical for support. You can do this using a [private offer](https://ubuntu.com/support#get-in-touch), by launching an Ubuntu Pro instance that includes support under the Ubuntu Advantage services but on a metered basis, or using an Ubuntu Advantage annual subscription.

### What kind of support does Canonical offer today for Ubuntu Pro?

To learn more about Canonical's support for Ubuntu Pro images, see the [Ubuntu support page](https://ubuntu.com/support).

### How can I be notified when updates are available for Ubuntu Pro?

To be notified when updates are made available by Canonical, subscribe to [Ubuntu security notices](https://ubuntu.com/security/notices).

All Ubuntu Pro VMs running on Compute Engine receive updates shortly after these updates are made available from Canonical. Updates can be installed using the standard Ubuntu Pro packaging tools.

These updates are made available to the Ubuntu Pro images that are provided by Compute Engine as outlined in the [Operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).

### Are there any restrictions on the machine types supported for Ubuntu Pro on Compute Engine?

Ubuntu Pro is supported by all machine types in all regions. For more information about machine types, see [Machine types](https://docs.cloud.google.com/compute/docs/machine-resource).

In addition to the different machine configurations, Ubuntu Pro can also be run on multi-tenant nodes or [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

## Migration FAQs

This section answers questions about migrating to Compute Engine with an Ubuntu Pro image.

### Can I migrate my Ubuntu LTS VM to Ubuntu Pro?

Yes, you can migrate existing Ubuntu LTS VMs to Ubuntu Pro. For more information, see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu).

### How do I get started with a Ubuntu Pro VM on Compute Engine?

To create a new Ubuntu Pro VM instance on Google Compute Engine, see the [Quickstart using a Linux VM](https://docs.cloud.google.com/compute/docs/create-linux-vm-instance) guide. When creating the VM, on the public images tab, choose a Ubuntu Pro version.

To migrate an instance running Ubuntu Pro on-premise or on other clouds to Google Cloud, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

### I plan to migrate Ubuntu Pro instances from AWS or Azure to Compute Engine. What is the recommended toolset or method to do so?

You can add VM instances, custom images, or disks that are available in an existing environment, such as on-premise or on other cloud providers, to Compute Engine.

To migrate an instance running Ubuntu Pro on-premise or on other clouds to Google Cloud, see [Choose a migration path](https://docs.cloud.google.com/compute/docs/import).

## What's next

  * Learn more about the [operating system images](https://docs.cloud.google.com/compute/docs/images/os-details) that Compute Engine provides.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
