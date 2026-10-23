---
url: https://docs.cloud.google.com/compute/vm-manager/docs/overview/
title: VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:09.947997+00:00
---

# VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  VM Manager Stay organized with collections  Save and categorize content based on your preferences. 

VM Manager is a suite of tools that can be used to manage operating systems for large virtual machine (VM) fleets running Windows and Linux on Compute Engine.

VM Manager helps drive efficiency through automation and reduces the operational burden of maintaining these VM fleets.

VM Manager supports projects in [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_vm_manager) service perimeters.

## Overview

The following services are available as part of the VM Manager suite:

  * [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch): Use this service to apply on-demand and scheduled patches. You can also use Patch for patch compliance reporting in your environment.
  * [OS inventory management](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management): Use this service to collect and review operating system information.
  * [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies): Use this service to install, remove, and auto-update software packages.

[ ![VM Manager architecture.](https://docs.cloud.google.com/static/compute/images/manage-os/vm-manager-arch.png)](https://docs.cloud.google.com/static/compute/images/manage-os/vm-manager-arch.png) Figure 1. VM Manager architecture overview

When you set up or enable VM Manager in your Google Cloud project, you can access the full suite of VM Manager tools: Patch, OS policies, and OS inventory management.

## Enable VM Manager

You can set VM Manager to be automatically enabled or manually enabled. Automatic enablement applies to your entire project. Manual enablement can be done per VM or for the entire project.

In summary, when you enable VM Manager, whether automatically or manually, the following setup takes place:

  * OS Config service API is enabled on the Google Cloud project.
  * The OS Config agent, running on each selected VM, is activated by setting the required [instance metadata](https://docs.cloud.google.com/compute/docs/manage-os#enable-metadata) values.

**Note:** OS Config is [preinstalled](https://docs.cloud.google.com/compute/docs/manage-os#check-install) on most VMs but is not activated until instance metadata is set.



For more information about manually enabling VM Manager, see [Setup overview](https://docs.cloud.google.com/compute/docs/manage-os#overview).

Automatic enablement is done from the Google Cloud console.

## OS Config agent

When VM Manager is enabled, the OS Config agent functions as follows for each of the services:

  * For _Patch_ , the OS Config agent uses OS system utilities (such as `yum`, `apt`, `rpm` or the Windows Update Agent) to retrieve patches or updates from the OS package or update source and apply them to the VM. For more information, see [How Patch works](https://docs.cloud.google.com/compute/vm-manager/docs/patch#how_os_patch_management_works).
  * For _OS policies_ , the OS Config agent uses OS system utilities (such as `yum`, `apt`, `rpm` or the Windows Update Agent) to maintain the state for the VM that is specified in the OS policy. For more information, see [How OS policies work](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies#how_os_configuration_management_works).
  * For _OS inventory management_ , the OS Config agent collects [inventory data](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#data-collected). This inventory data is then stored in the [instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata) and in various log streams. This data can then be queried using the Google Cloud CLI. For more information, see [How OS inventory management works](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management#how_os_inventory_management_works).



## Google Cloud OS Config Service Agent

Some Google Cloud services have [Google-managed service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) that allow services to access your resources. These service accounts are sometimes known as _service agents_. For more information about service agents, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).

VM Manager manages your VMs using a service agent that collects information about your VMs on your behalf. The email for this Google-managed service agent is `service-PROJECT_NUMBER@gcp-sa-osconfig.iam.gserviceaccount.com`. This account uses the Cloud OS Config Service Agent role (`roles/osconfig.serviceAgent`).

**Note:** Google creates the service agent for VM Manager only when Patch uses its service to start a patch job and to filter out the VM data. OS policies does not use this service agent.

You can view your project's service agents and the roles granted to the service agents on the [IAM page of the Google Cloud console](https://console.cloud.google.com/iam-admin). However, if you've revoked the Cloud OS Config Service Agent role for the service agent, you cannot view the service agent on the IAM page.

## OS packages and update source

For both Patch and OS policies, your VMs must be able to access package sources and repositories. For VMs in private networks, you can set up [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## VM Manager and Terraform

You can use Terraform to extend the scope of VM Manager to multiple projects in a Google Cloud organization. To learn how to create patch jobs and OS policy assignments by using Terraform and VM Manager, see the Terraform examples and tutorials in the [OS Config GitHub repository](https://github.com/GoogleCloudPlatform/osconfig/tree/master/examples/Terraform).

For more information about Terraform configurations and its usage, review the documentation for the following resources:

  * [OS patch deployment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/os_config_patch_deployment)
  * [OS policy assignment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/os_config_os_policy_assignment)



For a list of available resources to get started with using Terraform, see [Using Terraform with Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Pricing

For pricing information, see [VM Manager pricing](https://docs.cloud.google.com/compute/vm-manager/pricing).

## Limitations

VM Manager has the following limitations:

  * VM Manager supports only those operating systems configured with an English locale. If your VM uses a non-English locale, the OS Config agent might fail to parse package manager output. This issue can cause VM Manager features, such as Patch, OS inventory management, and OS policies, to fail.



## What's next?

  * Learn about [OS inventory management](https://docs.cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management).
  * Learn about [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch).
  * Learn about [OS policies](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
