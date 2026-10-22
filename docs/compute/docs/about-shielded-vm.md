---
url: https://docs.cloud.google.com/compute/docs/about-shielded-vm/
title: About Shielded VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:04.841952+00:00
---

# About Shielded VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/about-shielded-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Shielded VMs Stay organized with collections  Save and categorize content based on your preferences. 

You can enable the Shielded VM service on your Compute Engine VM instances to help defend against rootkits and bootkits. Shielded VM leverages advanced platform security capabilities such as [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot), [Virtual trusted platform module (vTPM)](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#vtpm)-enabled [Measured Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#measured-boot), and [Integrity monitoring](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#integrity-monitoring).

**Note:** To help prevent security issues, you must ensure your instances have the latest available Microsoft Secure Boot certificates. For detailed instructions on identifying and updating affected VMs, see the [Microsoft Secure Boot certificates expiration guide](https://docs.cloud.google.com/compute/docs/security/ms-secure-boot-certificates-expiration).

For a more detailed overview, see [Key concepts for Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).

To get started using Shielded VM, try the [quickstart](https://docs.cloud.google.com/compute/shielded-vm/docs/quickstart) or see [Modifying Shielded VM options](https://docs.cloud.google.com/compute/shielded-vm/docs/modifying-shielded-vm).

You can monitor the integrity of your Shielded VMs in some of the following ways:

  * You can use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) to [monitor the boot integrity](https://docs.cloud.google.com/compute/shielded-vm/docs/integrity-monitoring) of Shielded VM instances. Next, you can identify the cause of an integrity validation failure, and update the integrity policy baseline accordingly.

  * You can also [use a Cloud Run functions trigger to automatically act](https://docs.cloud.google.com/compute/shielded-vm/docs/automating-responses-integrity-failures) on integrity monitoring events.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
