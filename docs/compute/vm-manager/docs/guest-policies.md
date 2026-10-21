---
url: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/
title: OS guest policies (legacy) \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:20.080583+00:00
---

# OS guest policies (legacy)  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  OS guest policies (legacy) Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This page includes instructions about the legacy OS guest policies. A later version of OS policies is now [Generally Available (GA)](https://cloud.google.com/products/#product-launch-stages). To use the later GA version, see [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies). 

To view a comparison of the two versions, see [Comparing OS policies versions](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/comparing_policy_options). 

This page describes the legacy OS guest policies.

You can use OS guest policies to deploy, query, and maintain consistent configurations (desired state and software) for your VM instance (VM). On Compute Engine, you must use guest policies to maintain consistent software configurations on a VM.

To create a guest policy, see [Create a guest policy](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy).

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Overview

A guest policy is a resource that contains settings such as the desired package, package repository, and software configurations. The guest policy also specifies which VMs these settings should apply to.

You can use guest policies to complete the following tasks:

  * Install, remove, and auto-update software packages.
  * Configure software package repositories.
  * Install software using software recipes.



### Key terms

  * Package: Software packages such as dpkg or rpm.
  * Package repository: A repository where software packages can be installed from.
  * Software recipe: A set of instructions for installing unpackaged software for a guest operating system. With software recipes, you can specify instructions for installing software on the VMs. These instructions include additional steps such as:

    * Downloading files
    * Decompressing archives such as zip or tar
    * Running commands or scripts required to configure the software

Software recipes are ideal if you want to install software that is not delivered as a conventional software package, or for packages that require additional installation arguments or instructions.




## Pricing

For information about pricing, see [VM Manager pricing](https://docs.cloud.google.com/compute/vm-manager/docs/pricing).

## How guest policies work

After you set up guest policies for your project or specific VM instances and install the OS Config agent, the OS Config agent runs on your VM and uses the specifications in the guest policy to maintain the desired state for the VM. The OS Config agent applies the configurations during the agent's first run and then polls the service and corrects any drift every 10 minutes.

The OS Config agent uses the standard system package manager to apply the changes where applicable. On Linux, this means running a system package manager such as `apt install` or `yum install` for package installation.

For example you can set a policy that ensures that the [Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent) is installed on all instances in your project that have the prefix `test-`. For more information, see [Configuring a guest policy yaml or JSON file](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy#create-policy-file).

## How the configuration management service handles assignment conflicts

Because guest policies apply to existing and future running VMs, during the guest policy creation process, the service verifies that there are no current or possible future conflicts.

The configuration management service prevents conflicting configurations from being assigned to the same VMs by rejecting the latter of two policies that are deemed in conflict with each other.

For example, if you have the following policies:

  * Policy A, which installs a package `foo` on all VM instances that are labeled `color=red`.
  * Policy B, which removes package `foo` on all instances with a name prefix `dev-`.



Suppose you create an instance named `dev-instance` with a label `color=red`, this results in conflicting policies. To mitigate this problem, the service restricts `policy B` from being created.

## What's next?

  * [Create a guest policy](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/create-guest-policy).
  * [Manage guest policies](https://docs.cloud.google.com/compute/vm-manager/docs/guest-policies/manage-guest-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
