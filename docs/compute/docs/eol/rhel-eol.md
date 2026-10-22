---
url: https://docs.cloud.google.com/compute/docs/eol/rhel-eol/
title: RHEL end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:25.036734+00:00
---

# RHEL end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/rhel-eol/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  RHEL end of support Stay organized with collections  Save and categorize content based on your preferences. 

Red Hat Enterprise Linux (RHEL) operating systems reaching end of support (EOS) can expose your projects to security risks. This document explains the EOS process and provides migration paths to supported RHEL versions on Google Cloud. For a list of supported RHEL OS versions, see [GA RHEL versions](https://docs.cloud.google.com/compute/docs/images/os-details#ga_rhel_versions).

## EOS versions

  * RHEL 7: EOS on **June 30, 2024**.
  * RHEL 6: EOL on **November 30, 2020**.



## How will this EOS impact my existing virtual machine (VM) instances

Your current VMs that are running the EOS versions are not affected. After the EOS date, you can still start or stop your existing VMs that are using these images.

However, your projects might be at risk because you are running a version of RHEL that is no longer receiving security updates.

## What do I need to know

After this date, the following changes take effect:

  * EOS RHEL versions are still available but are marked as deprecated.
  * For your existing PAYG RHEL VMs that use an EOS version, limited technical support is available through Google Cloud.



## What do I need to do

  1. Review the [lifecycle stage](https://docs.cloud.google.com/compute/docs/images/os-image-lifecycle#lifecycle-stages) documentation.
  2. If you need to create VMs that use any of these EOS versions after the EOS date, [make copies of the images](https://docs.cloud.google.com/compute/docs/images/create-custom) that are available in your projects.
  3. Plan and migrate your workloads and applications to RHEL 8. Or, if you want to continue using the EOS RHEL versions, see [Appending RHEL ELS licenses](https://docs.cloud.google.com/compute/docs/images/premium/rhel/appending-els-licenses).



## What's next

  * Learn more about [images](https://docs.cloud.google.com/compute/docs/images) on Compute Engine.
  * Learn more about the [RHEL operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#red_hat_enterprise_linux_rhel) that are available on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
