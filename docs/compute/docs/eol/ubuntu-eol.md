---
url: https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol/
title: Ubuntu LTS end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:09.971436+00:00
---

# Ubuntu LTS end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/ubuntu-eol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  Ubuntu LTS end of support Stay organized with collections  Save and categorize content based on your preferences. 

Ubuntu LTS operating systems reaching end of support (EOS) can expose your projects to security risks. This document explains the EOS process and provides migration paths to supported Ubuntu LTS versions on Google Cloud. For a list of supported Ubuntu LTS OS versions, see [GA Ubuntu LTS versions](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions).

## EOS versions

  * Ubuntu 20.04 LTS (Focal): EOS on **May 31, 2025**.
  * Ubuntu 18.04 LTS (Bionic): EOS on **May 31, 2023**.
  * Ubuntu 16.04 LTS (Xenial): EOS on **April 30, 2021**.



## How will this EOS impact my existing virtual machine (VM) instances

Your current VMs that are running the EOS versions are not affected. After the EOS date, you can still start or stop your existing VMs that are using these images.

However, your projects might be at risk because you are running a version of Ubuntu that is no longer receiving security updates.

## What do I need to know

After this date, the following changes take effect:

  * EOS Ubuntu versions are still available but are marked as deprecated.
  * For your existing VMs, limited technical support is available through Google Cloud.



## What do I need to do

  1. Review the [lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) documentation.
  2. If you need to create VMs that use any of these EOS versions after the EOS date, [make copies of the images](https://docs.cloud.google.com/compute/docs/images/create-custom) that are available in your projects.
  3. Evaluate and move your Compute Engine VMs to either Ubuntu 22.04 LTS or Ubuntu 24.04 LTS before the EOS date. In-place upgrades of cloud images from LTS to LTS are supported by Canonical. For more information, see the [Canonical upgrade documentation](https://ubuntu.com/server/docs/upgrade-introduction).



## Additional information

To ensure continued support for your EOS Ubuntu LTS VMs on Compute Engine, consider the following options:

  * Get Extended Security Maintenance with an Ubuntu Advantage subscription from Canonical.

Extended Security Maintenance (ESM) is provided to Ubuntu VMs that have an attached [Ubuntu Advantage (UA)](https://ubuntu.com/advantage?utm_source=gcp&utm_medium=email&utm_content=pc-esm) subscription. Canonical ESM for Ubuntu LTS provides at least three additional years of security patches.

  * ESM with Ubuntu Pro

Google and Canonical are working together to simplify ESM enrollment for continuity of security coverage with [Ubuntu Pro](https://ubuntu.com/gcp/pro) on Compute Engine. This will ensure that you don't have to upgrade to newer Ubuntu versions immediately.

Ubuntu Pro is a premium image that is now [available](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro) on Compute Engine. Premium images incur additional license fees to run on Compute Engine. Upgrading to Ubuntu Pro enables ESM for new Ubuntu Pro LTS VMs with hourly billing as an alternative to an annual UA subscription. For information about how to upgrade to Ubuntu Pro, see [Upgrade from Ubuntu to Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu).




## What's next

  * Learn more about [images](https://docs.cloud.google.com/compute/docs/images) on Compute Engine.
  * Learn more about the [Ubuntu LTS operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_lts) that are available on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
