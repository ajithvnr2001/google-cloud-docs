---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies/
title: Zonal VM extension policies \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:48:34.694938+00:00
---

# Zonal VM extension policies  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Zonal VM extension policies Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of zonal policies in VM Extension Manager. With zonal extension policies, you can manage extensions in a single zone within a project. Each policy specifies extensions that you need to install and a scope, such as VMs in a specific zone or VMs with particular labels.

For more information, see [About VM Extension Manager](https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager).

The following diagram illustrates how you can use zonal extension policies to apply to VMs based on zones and labels:

![VM Extension Manager architecture diagram showing policies being applied to
VMs based on labels and
zones.](https://docs.cloud.google.com/static/compute/images/vm-extensions/vm-ext-manager-zonal-arch.svg)

As shown in the preceding diagram, you can define zonal extension policies at the project level. These policies apply to VMs in a specific zone that match the selection criteria. For example, in Zone A, extension policy `E1` targets VMs with the label `env=prod` to install Extension for SAP, and in Zone B, extension policy `E4` targets VMs with no labels to install Extension for Compute Workload and Ops Agent.

The guest agent on each VM periodically communicates with Google Cloud to check for applicable policies. If a VM is targeted by a policy, VM Extension Manager installs the specified extensions and keeps it up-to-date according to the policy. If no extensions are installed on a VM, the guest agent checks for policy updates every eight minutes. If there are extensions installed, it checks every minute.

## What's next

To learn more about managing extensions, see the following resources:

  * [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy)
  * [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
