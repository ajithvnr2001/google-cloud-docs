---
url: https://docs.cloud.google.com/compute/docs/eol/centos6/
title: CentOS 6 end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:06.961765+00:00
---

# CentOS 6 end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/centos6/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  CentOS 6 end of support Stay organized with collections  Save and categorize content based on your preferences. 

CentOS 6 operating systems reaching end of support (EOS) can expose your projects to security risks. This document explains the EOS process and provides migration paths to supported operating system versions on Google Cloud.

## How will this impact my existing virtual machine instances (VMs)

Your current VMs that are running CentOS 6 operating systems are not affected. After the EOS date, you will still be able to start or stop your existing VMs that are using these images.

However, your projects might be at risk because you will be running CentOS 6 VMs that are not receiving security updates.

## What do I need to know

After this date, the following changes take effect:

  * CentOS 6 images will still be available but will be marked as deprecated.
  * For your existing CentOS 6 based VMs, limited technical support is available through Google Cloud.



## What do I need to do

  1. Review the [operating system lifecycle and support policy](https://docs.cloud.google.com/compute/docs/images#lifecycle_policy).
  2. If you will need to create VMs that use these CentOS 6 images after the EOS date, [make copies of the images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) in your projects.
  3. Plan and migrate your CentOS 6 workloads and applications to a supported operating system version.



If you have specific questions about CentOS 6 EOS, contact [Google Cloud Support](https://docs.cloud.google.com/compute/docs/support).

## What's next

  * Learn more about [images](https://docs.cloud.google.com/compute/docs/images) on Compute Engine.
  * Learn more about the [CentOS operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#centos) that are available on Compute Engine.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
