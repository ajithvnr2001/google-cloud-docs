---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started/
title: Migration journey with Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:23.207293+00:00
---

# Migration journey with Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migration journey with Migrate to Virtual Machines Stay organized with collections  Save and categorize content based on your preferences. 

This document guides you through migrating your virtual machines (VMs) from your source environment to Google Cloud by using [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines). Your source environment might be running in an on-premises environment, in a private hosting environment, or in another cloud provider.

This document provides an overview of Migrate to Virtual Machines and what it's used for. It also contains important points for you to consider when planning a VM migration, and provides guidance about how to migrate VMs.

This document is useful if you're planning to migrate VMs from a supported source environment to [Compute Engine](https://docs.cloud.google.com/compute) with Migrate to Virtual Machines. These source environments can include the following:

  * A [VMware vSphere](https://www.vmware.com/products/vsphere.html) environment
  * A [Microsoft Azure VM](https://azure.microsoft.com/en-us/services/virtual-machines/) environment
  * An [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/) environment



Migrate to Virtual Machines lets you streamline your VM migration to Google Cloud. You don't have to spend effort in designing and implementing a reliable toolchain to manually evaluate how your VMs behave in Google Cloud, and then to manually migrate them. Migrate to Virtual Machines accelerates your VM migration, saves you time, and lets you focus on improving your workloads.

This series assumes that you have read and are familiar with the following documents:

  * [Migrate to Virtual Machines architecture](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture): describes the reference architecture of Migrate to Virtual Machines.



## Design the migration to Google Cloud

To migrate your VMs from your source environment to Google Cloud, we recommend that you follow the framework described in the [Migrate to Google Cloud series](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).

The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

The framework illustrated in the preceding diagram has four phases:

  1. **Assess**. In this phase, you assess your source environment, assess the workloads that you want to migrate to Google Cloud, and assess which VMs support each workload.
  2. **Plan**. In this phase, you create the basic infrastructure for Migrate to Virtual Machines, such as provisioning the resource hierarchy and setting up network access.
  3. **Deploy**. In this phase, you migrate the VMs from the source environment to Compute Engine.
  4. **Optimize**. In this phase, you begin to take advantage of the cloud technologies and capabilities.



## Assess the source environment and workloads

In the [assess phase](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads), you gather information about the following:

  1. Your source and target environment
  2. The workloads that you want to migrate



To help you to plan your migration and to rightsize the resources that you need for the migration and your target environment, it's crucial to assess your source environment and the workloads that you want to migrate. To learn how to assess your environment, see [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads).

After you've assessed your environment, you refine the assessment by taking into account migration aspects that are specific to Migrate to Virtual Machines, such as the following:

  * **Migrate to Virtual Machines requirements**. Evaluate Migrate to Virtual Machines requirements to ensure that both your source and target environments provide the features and the resources that Migrate to Virtual Machines needs for the migration, such as network connectivity and bandwidth, and secure communication channels. Based on the source that you want to migrate from, evaluate [VMware requirements](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-a-vmware-source#before_you_begin), [AWS requirements](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-aws-source), or [Azure requirements](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-azure-source).

  * **Required permissions for Migrate to Virtual Machines**. When you know which kind of permissions Migrate to Virtual Machines needs, you qualify whether those permissions meet your security requirements. Evaluate the [required permissions for Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/compute-engine/docs/5.0/reference/roles-reference).




## Build your foundation

This section contains guidance on how to build the foundation for Migrate to Virtual Machines.

Based on the source from which you want to migrate, see the guidance in [Migrating from VMware](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/vmware_overview), [Migrating from AWS](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-aws-source), or [Migrating from Azure](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-an-azure-source). Otherwise, continue with the guidance in this section.

To build a foundation for Migrate to Virtual Machines in the source environment and in Google Cloud, you do the following:

  * Build the foundation on Google Cloud.
  * Prepare the source environment.



### Build the foundation on Google Cloud

To build the foundation for Migrate to Virtual Machines on Google Cloud, you do the following:

  * **Provision the resource hierarchy**. Migrate to Virtual Machines [uses Google Cloud projects](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#about_projects) to control the migration process (the _host project_) and as a target environment (the _target projects_). Migrate to Virtual Machines [requires a host project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services#identifying_your_host_project). You can also optionally [add one or more target projects](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project) to use as destinations for the migrated VMs.
  * **Enable Migrate to Virtual Machines services**. Migrate to Virtual Machines depends on certain Google Cloud APIs and services. To learn how to enable the required APIs and services, see [Enabling Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).



### Prepare the source environment

To build a foundation for Migrate to Virtual Machines on your source environment, [install the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector) to configure the environment as a migration source. For more information about the Migrate Connector, see [Migrate to Virtual Machines architecture](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_sources).

## Migrate your VMs

After you build your foundation, you migrate your VMs with Migrate to Virtual Machines from your source environment to Google Cloud.

### Structure of a Migrate to Virtual Machines migration

The following terms are important for understanding how to organize a VM migration from a supported source environment to Google Cloud:

  * **VM migration lifecycle**. Each VM that you migrate with Migrate to Virtual Machines follows an ordered set of phases. Those phases are part of the [VM migration lifecycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle). Migrate to Virtual Machines automatically advances each VM to migrate through those phases.
  * **Groups**. Migrate to Virtual Machines lets you create sets of VMs to migrate. These sets are called [_groups_](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vm-groups). To logically separate VMs and to migrate VMs in batches, you can use groups. When you migrate the VMs in a group, Migrate to Virtual Machines performs all the operations of the VM migration lifecycle on each VM in the group or, optionally, on a subset of the VMs in the group. For example, you might create [test clones](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle#test-clone_phase) of one or two VMs in a large group to evaluate if the clones can function properly on Google Cloud.
  * **OS adaptations**. The VMs you migrate to Google Cloud with Migrate to Virtual Machines require changes to their configuration to function properly. These changes are referred to as [_OS adaptations_](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations). Migrate to Virtual Machines automatically applies OS adaptations to the VMs that you migrate.



### Migrate VMs with Migrate to Virtual Machines

To migrate VMs with Migrate to Virtual Machines you do the following:

  1. **Organize your migration with groups**. To help mitigate the risks of a migration, we recommend that you use groups to logically separate the VMs to migrate. To group the VMs to migrate, you can use the information gathered during the assessment phase. For example, you can group the VMs based on which application they support, or you might consider the network the VMs are connected to.
  2. **Gather machine sizing recommendations and utilization insights**. To evaluate the resources and determine the optimal target machines for your source machines, gather detailed sizing recommendations and reporting about your machines by [generating a source VM utilization report](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/create-report).
  3. **Migrate each group**. Execute the migration on each group of VMs. As part of the VM migration lifecycle, Migrate to Virtual Machines lets you run a test clone of a VM in Google Cloud. We recommend that you use test clones to validate if your VMs function properly in Google Cloud before migrating them.

For more information about migrating groups of VMs with Migrate to Virtual Machines, see [Migrating VM groups with Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vm-groups).




## Optimize your environment after migration

When you complete all the migration phases, the migration is considered done. However, your Google Cloud environment might need further optimizations. For example, you can rightsize Compute Engine VMs, or you can start using managed services.

For more information about optimization, see [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
