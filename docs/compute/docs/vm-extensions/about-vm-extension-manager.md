---
url: https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager/
title: About VM Extension Manager \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:02.997127+00:00
---

# About VM Extension Manager  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/vm-extensions/about-vm-extension-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About VM Extension Manager Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of VM Extension Manager. Use VM Extension Manager to manage extensions on your fleet of Compute Engine instances (VMs) at scale, which helps you monitor and manage your workloads.

## VM Extension Manager overview

VM extensions are optional plugins of the [Compute Engine guest agent](https://docs.cloud.google.com/compute/docs/images/guest-agent) that run on your compute instances (VMs). You can use VM Extension Manager to automate the lifecycle of these extensions across your entire fleet of compute instances, without connecting to each instance. VM Extension Manager installs and runs extensions on instances only when you apply a policy to the instance, and removes the extensions when you delete the policy. After you install extensions, VM Extension Manager monitors their health status while they are running.

For a list of extensions that you can manage by using VM Extension Manager, see Supported extensions.

You can use VM Extension Manager to create policies that declare which extensions you want to install on VMs. You can also choose VMs that match specific criteria—for example, VMs with specific labels. These extension policies apply to both existing VMs and any new VMs that match the criteria. You can create either [zonal extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies) or [global extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies) to manage extensions on your VMs.

## VM Extension Manager functions

VM Extension Manager lets you do the following:

  * **Install extensions at scale.** Use policies to install extensions across large fleets of VMs, instead of connecting to each machine individually.
  * **Automate extension updates.** Configure policies to keep extensions pinned to a specific version, or automatically updated to the latest version as it becomes available.

**Note:** Pinning extensions to a specific version is supported only for the Ops Agent.
  * **View extension status.** See which extensions are installed on each VM without logging in to individual machines.




## Supported extensions

VM Extension Manager supports installing and managing the following extensions:

**Note:** For extensions to install successfully, you must first [enable the required APIs](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling) in the project where the VMs exist. If you don't enable these APIs, extensions fail to install even if you create a policy. The following table lists the required APIs for each extension.Extension | Description | Required APIs  
---|---|---  
Ops Agent(`ops-agent`) | Installs the [Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent), which collects logs and metrics from your Compute Engine instances, so that you can view these telemetry on Google Cloud Observability dashboards. For details, see [Install and manage the Ops Agent by using VM Extension Manager policies](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/agent-vmem-policies). | Cloud Monitoring API  
Cloud Logging API  
Extension for SAP(`google-cloud-sap-extension`) | Installs [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning), which is required for SAP systems running on Google Cloud. The agent collects SAP Host Agent metrics, Process Monitoring metrics, and Workload Manager evaluation metrics. For details, see [Install and manage Agent for SAP on a fleet of VMs](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-manage-on-vm-fleet). | Workload Manager API  
Extension for Compute Workload(`google-cloud-workload-extension`) | Installs [Agent for Compute Workloads](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads), which you can configure to collect metrics from multiple workloads running on Compute Engine instances. For example, to install and manage Agent for Compute Workloads for SQL Server, see [Install and manage Agent for Compute Workloads on a fleet of VMs](https://docs.cloud.google.com/workload-manager/docs/evaluate/set-up-agent-for-sql-server#install-manage-agent-on-vm-fleet-by-using-vm-ext-mgr). | Workload Manager API  
  
## Supported operating systems

**Note:** Support for SUSE Linux Enterprise Server (SLES) and Ubuntu operating systems is not available.

VM Extension Manager supports installing extensions on any operating system that is supported by the specific extension. For details about supported operating systems for each extension, see the following:

  * Ops Agent: [Supported operating systems](https://docs.cloud.google.com/monitoring/agent/ops-agent#supported_operating_systems)
  * Extension for SAP: [Supported operating systems](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#supported_operating_systems)
  * Extension for Compute Workloads: [Supported operating systems](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads#supported-os-versions)



## Limitations

VM Extension Manager supports creating extension policies only at a project level.

## Quotas

Each Google Cloud project has a limit of 100 VM extension policies per zone. There is no limit on the number of VMs you can select per policy.

## Pricing

There is no charge for using VM Extension Manager. However, you might incur charges from using the extensions installed by the policies. For more information, see the pricing pages for the specific extensions:

  * [Ops Agent pricing](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#pricing)
  * [Extension for SAP pricing](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#pricing)
  * [Extension for Compute Workloads pricing](https://docs.cloud.google.com/compute/docs/instances/agent-for-compute-workloads#pricing)



## What's next

To learn more about managing extensions, see the following resources:

  * [Learn about global extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-global-policies)
  * [Learn about zonal extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/about-zonal-policies)
  * [Install VM extensions by creating extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy)
  * [Manage VM extensions by using extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions)
  * [View VM extension logs](https://docs.cloud.google.com/compute/docs/vm-extensions/view-vm-extension-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
