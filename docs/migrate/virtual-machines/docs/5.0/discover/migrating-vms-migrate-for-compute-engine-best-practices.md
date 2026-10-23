---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-best-practices/
title: Migrate to Virtual Machines best practices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:12.823742+00:00
---

# Migrate to Virtual Machines best practices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate to Virtual Machines best practices Stay organized with collections  Save and categorize content based on your preferences. 

This document describes best practices that you can consider while designing your virtual machine (VM) migration to Google Cloud with [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/compute-engine). Migrate to Virtual Machines helps you migrate VMs from a source environment to Google Cloud. Your source environment might be running in an on-premises environment, in a private hosting environment, or in another cloud provider.

The best practices described in this document cover the following areas:

  1. Assessing your source environment
  2. Building your foundation
  3. Migrating your VMs
  4. Troubleshooting migration issues



## Assessment best practices

This section describes best practices to address common issues that might arise during the [migration assessment phase](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started#assessing_the_source_environment_and_workloads). As described in [Designing the migration to Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started#designing_the_migration_to_google_cloud), in the _assessment_ phase, you assess your source environment, the workloads that you want to migrate to Google Cloud, and which VMs support each workload.

### Involve the teams responsible for your workloads as early as possible

During the first phase of the migration, gather information about the source environment by involving and interviewing all teams that are responsible for your environment, workloads, and VMs. For example, to assess the technical requirements of your migration, interview development teams, operation teams, security teams, and the lines of business and stakeholders that are related to the workloads to migrate. To assess the regulatory requirements of your migration, include legal and compliance teams in these interviews.

This best practice helps you avoid surprises and unexpected issues caused by unforeseen migration requirements and dependencies.

### Analyze the complexity of your environment

When assessing the source environment and VMs, evaluate factors that might affect the complexity of a migration. Determine the criteria and data points to assess the complexity of each workload. If the complexity of a migration increases, you might have to plan for additional time and effort to complete the migration. For example, you might consider the following factors:

  * Do you need to migrate VMs with operating systems that you want to update?
  * Do you need to migrate VMs with unsupported operating systems?
  * Do you need to migrate bare-metal or physical servers?
  * Do you have dependencies on a given [hypervisor](https://wikipedia.org/wiki/Hypervisor)?
  * Do you need to migrate from a hypervisor that [Migrate to Virtual Machines doesn't support](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source)?
  * Do you have dependencies on certain technologies or services that you don't want to or can't migrate?
  * How many VMs do you need to migrate?
  * Do any of these VMs have dependencies to other applications, systems, or VMs?
  * Does your migration team have experience with Google Cloud?
  * Does your migration team have experience with Migrate to Virtual Machines?
  * What are your security and governance requirements?
  * Do you have a strategy for deploying resources in the cloud?
  * Do any of your workloads have hardcoded configurations that you can't change?
  * Do your workloads require licensed operating systems or other licensed software?



For this process to work, a VMware host and a VMware vCenter instance must be in the same network as the VMs that you want to migrate. If there's no VMware host in the network, we recommend one of the following options to migrate your VMs to a source environment that Migrate to Virtual Machines supports:

  * [Migrate VMware VMs with VMware HCX](https://docs.cloud.google.com/vmware-engine/docs/workloads/howto-migrate-vms-using-hcx) to [Google Cloud VMware Engine](https://docs.cloud.google.com/vmware-engine).
  * [Migrate supported non-VMware VMs to a VMware environment with VMware HCX OS Assisted Migration](https://docs.vmware.com/en/VMware-HCX/services/user-guide/GUID-FF922494-22D9-4842-866B-5EBAC26EF835.html).



If you need to migrate a workload that supports high volumes of transactions or requests, assess the speed at which changes are synchronized between the source and the target environments. The speed during the migration might be less than the speed at which the changes are generated by the workload. In such cases, we recommend that you [assess other data migration approaches](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#data_migration_approaches) that are specific to these types of workloads. For example, if you migrate a database that supports a high volume of transactions per time unit, the speed at which the transactions are propagated to the target environment might not be fast enough to complete the synchronization. In this case, the VMs in the target environment might not be able to complete the data synchronization, making your migration wave impossible to complete.

This best practice helps you estimate the difficulty of a migration, and to manage expectations of the stakeholders of your migration project.

### Analyze your current environment to rightsize the target environment

To draft a complete migration plan, define the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) of each VM in the target environment for each VM that you want to migrate from the source environment. We recommend that you gather information about the provisioned resources of each VM in the source environment, and the utilization rate of those resources, as described in [Migration to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads).

This best practice helps ensure that you gain in-depth insights about your workloads.

### Analyze the migration plan

Before you start your migration plan analysis, and to help you to understand the architecture of Migrate to Virtual Machines, we recommend that you read the following documents:

  * The structure of a [Migrate to Virtual Machines migration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started).



After you've familiarized yourself with the concepts that are discussed in these documents, analyze your migration plan to gather information about schedule, duration, effort, and costs. We recommend that you use [weighted medians](https://wikipedia.org/wiki/Weighted_median) and [weighted means](https://wikipedia.org/wiki/Weighted_arithmetic_mean) instead of single values, so that you can refine the results of your analysis after each migration wave.

For example, after analyzing the migration plan, you might determine values for the following:

  * The expected migration duration
  * The expected number of VMs to migrate for each time unit
  * The total migration cost
  * The migration cost per VM
  * The available network throughput
  * The compatibility of the tools you're using for backup and disaster recovery with the target environment



Consider all deployment environments for your applications when you analyze the migration plan. If a workload requires multiple deployment environments, consider these environments and the differences between each environment in your analysis. For example, if you deploy a workload in a development, a quality assurance, and a production environment, you might discover in your analysis that these environments have a different number of VMs. You might have to adjust your migration plan to consider these differences and to meet the migration deadlines.

### Adjust the migration plan while you gain experience

After establishing a migration plan, and starting to implement that plan, you gain experience about migrating apps and VMs, Google Cloud, and Migrate to Virtual Machines. While the migration is in process, use this knowledge to regularly revisit, adjust, and improve your migration plan. Amend the migration plan at least once per iteration. You might discover that you set unrealistic goals, or spent effort on unanticipated issues.

This best practice helps you optimize the migration plan.

### Schedule a maintenance window for the VMs to migrate

To complete the migration of a VM, Migrate to Virtual Machines has to perform operations that might require downtime of the VM. Plan for redundancy and for a cutover window to perform the operations that require a downtime. For example, if you migrate a cluster of VMs, you might have to split the cluster and recompose it after the migration.

This best practice helps you avoid unexpected downtimes of your workloads.

## Planning best practices

This section describes best practices to address common issues that might arise while [building the foundation for Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started). As described in [Designing the migration to Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started#designing_the_migration_to_google_cloud), in the planning phase, you create the basic infrastructure for Migrate to Virtual Machines.

### Ensure your environment meets the requirements

When you provision and configure the infrastructure to support your migration, ensure that your environment meets the Migrate to Virtual Machines requirements:

  * The [supported operating systems](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/reference/supported-os-versions)
  * The [required roles and permissions](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/reference/roles-reference) on Google Cloud and in your source environment
  * The [required Google Cloud services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services)
  * The [maximum number of concurrent migrations](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#step_1_onboard_a_vm)



Ensure that you involve all the relevant teams in the analysis of these requirements because the requirements span different areas, such as computing, networking, security, and compliance. For example, opening a firewall port might require collaboration between the security team and the networking team.

To maximize the network throughput, we also recommend that you configure the [maximum transmission unit](https://wikipedia.org/wiki/Maximum_transmission_unit) while considering the recommended values for [Virtual Private Cloud networks](https://docs.cloud.google.com/vpc/docs/mtu), [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers), and [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/mtu-considerations).

This best practice helps you avoid unanticipated issues due to incompatibilities and requirements that you can't meet.

### Ensure that you have enough resource quota

Google Cloud [enforces quotas on resource usage](https://docs.cloud.google.com/docs/quotas/overview). Migrate to Virtual Machines requires enough resource quotas to complete the VM migration.

We also recommend that you review [VPC quotas and limits for Compute Engine instances](https://docs.cloud.google.com/vpc/docs/quota#per_instance).

To ensure that you have enough quotas to complete the migration, do the following:

  1. [Check your current available quota](https://docs.cloud.google.com/compute/quotas#checking_your_quota).
  2. Ensure that your available quota meets [Migrate to Virtual Machines quota requirements](https://docs.cloud.google.com/migrate/compute-engine/quotas).
  3. [Request an increase in quotas](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota), if necessary.



This best practice helps you avoid delays due to quota increase requests turnaround time and quota requirements.

## Migrating your VMs best practices

This section describes best practices to address common issues that might arise while migrating your VMs with Migrate to Virtual Machines.

### Ensure that the guest OS is correctly configured in VMWare

Before migrating your VMs, ensure that VMWare vCenter is not [reporting any warnings related to the guest operating system (OS)](https://kb.vmware.com/s/article/67671). If you see a warning, fix the guest OS configuration by [changing the configured guest OS](https://docs.vmware.com/en/VMware-vSphere/6.7/com.vmware.vsphere.vm_admin.doc/GUID-3B66132C-F3E7-4F86-836F-80A03AC99E2A.html).

This best practice helps you avoid errors during the migration.

### Ensure that your VMs are correctly prepared

Before you migrate your VMs or physical servers, ensure that they are correctly prepared for the migration without any errors or warnings. If your VMs and physical servers aren't prepared for the migration, there can be unexpected results for the migration attempt, such as failure to migrate the VMs. This best practice helps you avoid errors during the migration.

Migrate to Virtual Machines automatically prepares your VMs before migration. For more information, see [Adapting VMs to run on Google Cloud](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/resources/vm-adaptations).

### Ensure that your VMs are working properly in Google Cloud

We recommend that you verify that your VMs are working correctly in Google Cloud both during the replication and after the cut-over phase. This best practice helps you validate that your workloads and VMs are working as you'd expect.

When you start the [replication phase](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle#replication_phase), you verify your VMs by creating [test clones](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle#test-clone_phase) in a sandbox environment. You can repeat the test clones creation process multiple times to evaluate how your VMs work in the cloud as you apply changes to the source environment. We recommend that you run these tests before you advance your VMs to the [cut-over phase](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle#cut-over_phase).

After you complete the cut-over phase, check the operation of your VMs by involving the owner of each workload, and asking them to assess if there are any issues with such workloads. We recommend that you run this verification before you advance your VMs to the [finalize phase](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle#finalize_phase).

### Uninstalling Migrate to Virtual Machines

After you complete the migration, we recommend that you uninstall Migrate to Virtual Machines. This best practice ensures that you decommission Migrate to Virtual Machines components, and avoid any unnecessary billing and management effort.

To uninstall Migrate to Virtual Machines, do the following:

  1. Delete and uninstall Migrate Connectors from your VMware vSphere data center. For more information, see [Deleting a Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector#deleting_a_migrate_connector).
  2. Deactivate the Migrate to Virtual Machines service: `vmmigration.googleapis.com`. For more information about deactivating services in a project, see [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling).
  3. Delete any test clones you created to verify that your workloads work correctly in Google Cloud.



## Troubleshooting best practices

This section describes best practices to help you investigate any migration issue that might occur when using Migrate to Virtual Machines.

To effectively troubleshoot migration issues, or issues that occur after the migration, you gather information about Migrate to Virtual Machines, your environment, and your workloads. Start by gathering information about the following:

  * Check if the issues you're experiencing are mentioned in the [Migrate to Virtual Machines release notes](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/resources/release-notes).
  * Migration lifecycle phases. If the migration is failing, take note of the lifecycle phase during which you experience the issue, and if the issue is reproducible and not transient.
  * Use Cloud Monitoring and Cloud Logging. To gather information about your environment, we recommend that you use Cloud Monitoring and Cloud Logging to [understand the status and performance of your migration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/audit-logging). Ensure that Cloud Monitoring and Cloud Logging are enabled by [checking that the necessary metadata are set for your Compute Engine instances](https://docs.cloud.google.com/marketplace/docs/manage-deployments#managing_logging_and_monitoring_for_your_deployment).



For more information, see [Migrate to Virtual Machines troubleshooting](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/support/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
