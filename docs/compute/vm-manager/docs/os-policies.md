---
url: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/
title: About OS policies \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:18.725053+00:00
---

# About OS policies  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  About OS policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of OS policies. Use OS policies to automate and centralize the deployment, configuration, maintenance, and reporting of software configurations on your virtual machine (VM) instances.

## Use cases

OS policies are ideal for the following scenarios:

  * Installing and maintaining agents for tasks such as monitoring and logging
  * Deploying agents such as security agents, and ensuring that these agent are running on all VMs
  * Improving startup script flexibility. With OS policies you can modify existing scripts and re-deploy them
  * Running compliance checks
  * Adding update repositories for software packages
  * Managing files on the operating system
  * Running condition-based scripts. You can set up scripts that run based on certain conditions to maintain consistent state within the operating system.

**Note:** Custom OS policy scripts and output files that you define using the [`Exec`](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.locations.osPolicyAssignments#exec) resource don't use [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek). These OS policies are incompatible with Google Cloud's [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview) and [Access Approval](https://docs.cloud.google.com/assured-workloads/access-approval/docs/overview). Make sure that you don't include any sensitive information in these scripts or output files.

## Components

### OS policy

An OS policy is a file that contains the declarative configuration for OS resources such as packages, repositories, files, or custom resources defined by scripts.

An OS resource can perform a single task such as installing an agent and can be reused without changes in different assignments. You can create a multi-step workflow by combining multiple OS resources into a single OS policy. For example, an OS policy can have one resource that sets up a repository and a second resource that installs specific packages from that repository.

For more information about OS policies, see [OS policy and OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).

### OS policy assignment

OS policy assignments are used by VM Manager to apply your OS policies to VMs. Use OS policy assignments to combine multiple OS policies and target them to a dynamic group of VMs by using filters such as labels, OS families, and zones.

For example, an OS policy assignment that applies three policies to all the Ubuntu VMs in your test environment, while excluding those that are running Google Kubernetes Engine, can be created by specifying the following:

  * Policy A: install monitoring agent
  * Policy B: install logging agent
  * Policy C: install security agent
  * Include label: `env:test`
  * Exclude label: `goog-gke-node`
  * OS family: `ubuntu`

**Note:** OS policy assignments are zonal resources. One assignment can target multiple VMs in a single zone. For more information about zonal resources, see [Zonal resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#zoneresource).

#### Rollouts

When you create a new OS policy assignment, VM Manager applies the OS policies to each VM according to the rollout configuration. During the rollout, a copy of each OS policy is placed on the VM. When you update an OS policy assignment, VM Manager checks and enforces the configuration changes for the OS policy that is on the target VM.

We recommend that you apply new configuration changes slowly to ensure that you have time to identify any potential disruptions that might be caused by configuration changes. This provides you with time needed to cancel the rollout and address the issue.

Specifying the rollout option enables you to pace configuration changes and control the speed of configuration deployments. Each operation for an OS policy assignment starts a rollout process. Operations include the creation, update, or deletion of an OS policy assignment.

You can use the rollout option to set the following:

  * Wave size (disruption budget): the fixed number or percentage of VMs that can experience a rollout at one time. This means that at any moment of the rollout only a specified number of VMs are targeted.
  * Wait time: the time between when the service applies policies to the VM and when a VM is removed from the disruption threshold. For example, a wait time of 15 minutes means that the rollout process must wait 15 minutes after applying the policies to a VM before it can remove the VM from the disruption threshold and the rollout can proceed. The wait time helps control the speed of a rollout and also lets you catch and resolve potential rollout issues early. Select a time that is long enough for you to monitor the status of your rollouts.



For information about how to create OS policy assignments, see [Creating an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).

### OS Config agent

During VM Manager setup, OS Config agents are enabled on the VMs in your project. The OS Config agents that are running on these target VMs use standard system utilities to apply the changes that are specified in the OS policies.

  * Linux VMs run system package managers such as `apt` or `yum` for package installation, or `/bin/sh` for scripting.
  * Windows VMs run `googet` package manager and PowerShell for scripting.



For information about how to set up VM Manager, see [Setting up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup#overview).

## How OS policies work

To use OS policies for maintaining your operating systems, do the following:

  1. Create or download OS policies
  2. Create OS policy assignments that applies these OS policies to the target VMs

[ ![OS policies architecture.](https://docs.cloud.google.com/static/compute/images/os-config/os-configuration-arch.png)](https://docs.cloud.google.com/static/compute/images/os-config/os-configuration-arch.png) Figure 1. OS policies architecture overview

After the OS policy assignments are created, VM Manager periodically checks and enforces these OS policies. The time interval between each enforcement check is 60 minutes.

During the check and enforcement, VM Manager completes the following steps:

  1. Identifies the OS policy assignments for a VM.
  2. Identifies the OS policies associated with the OS policy assignments.
  3. Sends the information for each OS policy to the OS Config agent that is running on the VM.
  4. The OS Config agent then validates each policy and makes the following updates:

     * If resources within an OS policy are already in their desired state, then the OS Config agent does not perform any actions
     * If resources within an OS policy are not in their desired state, then the OS Config agent takes appropriate actions to bring the resources to the desired state
  5. Collects the compliance status of each OS policy that is applied to the VM. To view compliance reports, see [View compliance reports](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/view-compliance).




## Pricing

For information about pricing, see [VM Manager pricing](https://docs.cloud.google.com/compute/vm-manager/pricing).

## What's next?

  * Review [OS policy and OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/working-with-os-policies).
  * Learn how to [create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).
  * Learn how to [manage OS policy assignments](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/manage-os-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
