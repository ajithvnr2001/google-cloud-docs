---
url: https://docs.cloud.google.com/docs/get-started/consider-resource-maintenance/
title: Consider resource maintenance \u00a0|\u00a0 Get started \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:26:22.203540+00:00
---

# Consider resource maintenance  |  Get started  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/get-started/consider-resource-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Get started ](https://docs.cloud.google.com/docs/get-started)
  * [ Guides ](https://docs.cloud.google.com/docs/overview)



Send feedback 

#  Consider resource maintenance Stay organized with collections  Save and categorize content based on your preferences. 

Before you create resources, you must consider maintenance requirements for each resource that you deploy. Additionally, you must consider maintenance on any underlying resources.

For example, some services deploy to underlying Compute Engine VMs. The maintenance policy that you set for your deployed service is distinct from the maintenance policy on the underlying VMs.

The following example maintenance dynamics are provided to help you understand the planning required to keep your resources available and running efficiently.

## Set virtual machine (VM) maintenance policies

When you create VMs you set a maintenance policy that dictates VM behavior when there is an update pending, a VM crashes, or other host events occur. For example, you can create a policy to live migrate workloads to another VM, or shut down and restart the impacted VM.

For more information, see the following:

  * [About host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview)
  * [Monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event)



### Distinguish between VM maintenance and service maintenance

The maintenance policy that you set for VMs is distinct from maintenance policies that you set for services that run on your VMs.

For example, GKE deploys clusters on Compute Engine VMs. You can set maintenance policies to control when some GKE cluster maintenance happens, but those policies don't prevent automatic maintenance triggered on the underlying Compute Engine VMs.

To learn more about maintenance policies for services running on Compute Engine VMs, review the respective documentation for those services.

### Maintain workloads on VMs with GPUs or TPUs

Some Compute Engine resources you create might have GPUs or TPUs attached. For example, you might create VMs that use GPUs or TPUs to handle AI workloads. If a host event occurs on these VMs, live migration from the impacted VM to a new VM is not supported. As a result, host maintenance events result in VM downtime and potential disruption to your workloads. To handle maintenance events on resources with GPUs or TPUs, see the following:

  * [Handle GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance)
  * [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



## Retain connections during network infrastructure maintenance

Network Connectivity products help you connect your peer networks to your Virtual Private Cloud networks. Google Cloud performs regular maintenance on this infrastructure. To help prevent downtime during maintenance events, we recommend that you follow the maintenance recommendations for each networking product, as in the following examples:

  * Cloud Router maintenance does not interrupt routing, but might require you to configure settings on your peer network router. For more information, see [Software maintenance and automated task restarts](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#maintenance).

  * Cloud Interconnect experiences regular automated maintenance, which might require you to set up notifications and create redundant connections. For more information, see [Infrastructure maintenance events](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events).




## Manage maintenance with Unified Maintenance

Unified Maintenance helps you to manage maintenance across Google Cloud services. You can view historical, in-progress, and upcoming maintenance activities in Cloud Hub or get the same information using the Unified Maintenance API. You can also configure alerts for upcoming maintenance in Cloud Logging. To learn more, see the [Unified Maintenance overview](https://docs.cloud.google.com/unified-maintenance/docs/overview).

[ Previous arrow_back  Organize resources  ](https://docs.cloud.google.com/docs/get-started/organize-resources)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
