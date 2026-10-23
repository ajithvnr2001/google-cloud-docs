---
url: https://docs.cloud.google.com/vmware-engine/docs/howto-migrate-ve1-hardware/
title: Migrate workloads from retiring ve1 hardware \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:14.088586+00:00
---

# Migrate workloads from retiring ve1 hardware  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/howto-migrate-ve1-hardware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate workloads from retiring ve1 hardware

This document explains how to migrate your Google Cloud VMware Engine workloads from retiring `ve1` hardware to supported `ve1` or `ve2` hardware. You can migrate workloads by using one of two methods: Option 1 involves adding new hardware clusters to an existing private cloud to create a mixed-node private cloud, while Option 2 involves deploying a new private cloud using new hardware.

Google Cloud is retiring first-generation `ve1` hardware on a rolling basis as the physical infrastructure reaches the end of its useful life. Retirements occur in batches based on [placement groups](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware) across different service regions.

When Google Cloud schedules your hardware for retirement, you receive a targeted End-of-Life (EoL) notification containing a detailed timeline, resource limits, and migration instructions. These targeted notifications begin rolling out in Q1 2026, and the first batches of `ve1` hardware reach end-of-life by Q1 2027. As your placement group reaches its scheduled retirement date, you can migrate your workloads to newer hardware.

This document describes the EoL notice details and the steps to migrate your workloads. To maintain service continuity and ensure service level agreement (SLA) coverage, complete the migration before your clusters reach their EoL dates.

## Before you begin

Before you configure new resources, review the requirements, limitations, and factors that could block your migration in this section. This information helps you plan a successful migration and avoid service disruption.

**Caution:** To avoid service disruptions and prevent migration failures, verify your resource limits, IP address space availability, and licensing agreements before you begin the migration process.

The critical requirements to consider before you start a migration are as follows:

  * **Strict 60-day migration window:** Google supports your migration for a maximum of 60 days after Cloud Customer Care or you provision the target cluster: 
    * You must complete the workload migration and decommission the retired hardware within this period.
    * If your workload migration duration exceeds 60 days after Cloud Customer Care or you provision the target cluster, you must bring your own Broadcom license (BYOL) to cover any consumption exceeding standard entitlements.



The factors that could potentially block your migration are as follows:

  * **IP address space blocker (Option 1 blocker):** Option 1 (mixed-node private cloud) requires that your existing private cloud has sufficient free management IP address space. You need enough space to support the added target cluster, which requires a minimum of three nodes. If your existing CIDR block can't support at least three additional nodes, you can't use Option 1. In this case, you must deploy a new private cloud instead (Option 2). Review Plan capacity for the IP address space to determine your eligibility.
  * **Live migration database support:** Some database platforms can't tolerate live vMotion migrations. Identify these VM database instances and plan to rebuild them directly on the target cluster.
  * **VMware HCX connectivity:** VMware HCX Fleet appliances don't support standard live vMotion. You must plan to redeploy your HCX service meshes on the target cluster. For more information, see the Broadcom article [Migrating HCX appliances to a different SSO, PSC, or vCenter](https://knowledge.broadcom.com/external/article/323627/hcx-migrating-hcx-appliances-to-a-differ.html).



### Plan capacity for the IP address space

If you migrate by using a mixed-node private cloud (Option 1), verify that your existing private cloud has enough available space in the management IP address range. The added target cluster requires a minimum of three nodes.

  1. View the management IP address range and IP plan version of your private cloud. For reference, see [Subnets CIDR range division versions](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements#example-management-network-cidr-range-division).
  2. Count the current number of nodes in your private cloud.
  3. Check the maximum nodes supported by your CIDR size. Refer to the [vSphere and vSAN subnets CIDR range size](https://docs.cloud.google.com/vmware-engine/docs/quickstart-networking-requirements#vsphere-vsan-subnets-cidr-range-size) table.
  4. Calculate: `Existing node count + 3 ≤ maximum nodes supported by CIDR size`



If your CIDR block can't support at least three additional nodes, you can't use a mixed-node private cloud. In this case, you must deploy a new private cloud instead (Option 2).

### Plan node capacity

If your future capacity offer specifies `ve2` nodes, work with your Google Cloud account team to size and determine the correct `ve2` node types (`mega`, `large`, `standard`, or `small`) and counts for your workloads. Refer to [VMware Engine HCI node types](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types#hci-node-types) for technical specifications.

### License and software requirements

Consider the following license and software requirements for your migration:

  * **Broadcom licenses** : If your workload migration duration exceeds 60 days after Cloud Customer Care or you provision the target cluster, you must bring your own Broadcom license to cover any consumption exceeding your standard entitlements.
  * **VMware HCX service meshes** : VMware HCX Fleet appliances don't support vMotion. You must redeploy your HCX service meshes on the target cluster. For more information, see the Broadcom article [Migrating HCX appliances to a different SSO, PSC, or vCenter](https://knowledge.broadcom.com/external/article/323627/hcx-migrating-hcx-appliances-to-a-differ.html).
  * **Management placement groups** : Google provisions capacity in the correct placement groups. For mixed-node setups, Cloud Customer Care sets up the new cluster in the target placement group. For new private clouds, submit the planned private cloud name to your account team before you create the private cloud to ensure Google configures it in the correct placement group.



### Plan commitments and billing

Before you select a migration path, review the following constraints for committed use discounts (CUDs):

  * **`ve1` CUD limitations:** Only one-year `ve1` CUDs with portable-license pricing options are available. To apply any new one-year commitment, you must migrate to a new `ve1` placement group in the same region.
  * **`ve2` CUD support:** Three-year CUD commitments are only supported on the `ve2` node families.
  * **Eligibility check:** Because new commitments depend on the remaining life of the node placement groups in your region, you must work with your Google Cloud account team to verify your eligibility.



## Understand your ve1 end-of-life notice

The `ve1` end-of-life (EoL) notice is an official email that informs you that your `ve1` bare metal nodes are reaching the end of their useful life.

### Key EoL notice components

The notice includes the following details:

  * **Region and zone** where the EoL notice applies.
  * **Your current usage** : Listing all your active projects and `ve1` private clouds in the region, detailing: 
    * Private cloud name
    * Project number
    * Cluster name
    * `ve1` node type (HCI or SON)
    * Number of `ve1` nodes of each type
    * End-of-Life date after which the cluster is unsupported
  * **Future capacity offer** : The EoL notice provides a future capacity offer for each `ve1` cluster in the region: 
    * **If the target capacity offer is ve1** : Same number of nodes as in the current `ve1` cluster, with a sufficiently longer useful life configuration.
    * **If the target capacity offer is ve2** : `ve2-mega-128` node type, offering equivalent or higher compute, memory, and storage capacity resources.
    * **SLA and Failure-to-Tolerate (FTT)** : For any cluster with three or more nodes, the future offer consists of a minimum of three nodes. This ensures a default FTT value of 1.

**Note:** The table of clusters in the EoL notice highlights the VMware Engine clusters subject to the current End-of-Life notice in yellow. The notice lists other clusters in the region for completeness. If you manage multiple projects, you may receive separate notifications for each project.

## Key migration steps

Your migration consists of the following sequence of steps:

  1. Review the target capacity offer for each cluster subject to EoL. If you need a different configuration (node types or quantity), work with your Google Cloud account team to adjust the capacity offer.
  2. Manage Committed Use Discounts (CUDs): If you have active `ve1` CUD commitments that outlive the hardware EoL dates, work with your account team to adjust or terminate them.
  3. Select your migration path: Choose between creating a mixed-node family private cloud or a new private cloud deployment. To help you decide, compare the migration methods in the following section.
  4. Execute the migration: Migrate your workloads using the chosen path. You have a maximum support window of 60 days to complete the migration after Cloud Customer Care or you provision the target cluster.
  5. Decommission the old hardware: Delete the retiring `ve1` clusters and associated quotas to complete the migration.



## Compare migration options

Choosing the correct migration path helps you configure your networking correctly. It also helps you avoid service disruption during the migration. The following table compares the technical, network, and operational criteria for each option.

Feature | Option 1: Mixed-node (hybrid) private cloud | Option 2: New private cloud deployment  
---|---|---  
Description | Add target hardware family clusters directly to the existing private cloud. | Deploy a completely new private cloud on target hardware.  
Requirement for management IP range | Requires sufficient free CIDR space in the existing private cloud to support the added cluster (minimum of three nodes). Insufficient space is a blocking factor for Option 1. | Flexible. Uses a new management IP address range entirely.  
Networking and DNS impact | Minimal. Preserves current networks, subnets, and management interfaces. | High. Requires configuring new network topologies, DNS, and access coordinates.  
Migration workflow | Standard live VMware vMotion and Storage vMotion. | Broad-scale migrations using VMware HCX.  
Creation method | Requested using Cloud Customer Care ticket (you can't add clusters to hybrid private clouds yourself). | Fully self-service (Console, REST API, Google Cloud CLI, or Terraform).  
  
## Option 1: Mixed-node private cloud migration

This method lets you add target hardware family clusters directly to your existing private cloud and migrate workloads on a cluster-by-cluster basis. Note that the 60-day migration limit applies to each cluster migration.

### Submit a quota request for target hardware

  1. In the Google Cloud console, submit a [quota request](https://docs.cloud.google.com/vmware-engine/quotas#requesting_quota) for the new target hardware family (`ve1` or `ve2`) and node counts.
  2. In the quota request description, explicitly write the following properties: 
     * `"ve1 hardware end of life"`
     * `"Retiring PC Name(s): [YOUR_PC_NAME(S)]"`
     * `"Retiring Cluster Name(s): [YOUR_CLUSTER_NAME(S)]"`
  3. After Google approves the request, you can view the new quota in the console.



### Create the target cluster in your private cloud

  1. You can't create clusters in mixed-node private clouds yourself. Submit a support ticket to request cluster setup.
  2. Provide the following details in the support ticket: 
     * Project number
     * Private cloud name
     * New target cluster name
     * New machine family (`ve1` or `ve2`) and node type
     * Count of HCI nodes
     * Count of storage-only nodes (if applicable)
  3. Cloud Customer Care notifies you when the target cluster is online.



### Migrate workloads

After the target cluster is ready, use the combination of VMware vMotion and storage vMotion to migrate workload VMs and VM disks:

  1. In the vSphere Client, right-click the VM and select **Migrate**.
  2. Select **Change both compute resource and storage**.
  3. Choose the new cluster and destination datastores.



### Migrate private cloud management VMs

If the cluster you are retiring is the primary (first) cluster of the private cloud, you must migrate the management VMs:

  1. Use the Google Cloud VMware Engine console or the REST API to migrate management VMs to the new cluster. For detailed instructions, see [Manage private cloud resources](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-manage-private-cloud#migrate-vms).
  2. Don't perform other cluster activities (such as adding nodes) during the migration. The private cloud status changes to updating during the process.
  3. Unmount any NFS datastores connected to the old `ve1` clusters.



### Adjust other configurations and applications

  * **VMware HCX service meshes** : Fleet appliances don't support vMotion. Redeploy HCX service mesh components on the target cluster. For more information, see the Broadcom article [Migrating HCX appliances to a different SSO, PSC, or vCenter](https://knowledge.broadcom.com/external/article/323627/hcx-migrating-hcx-appliances-to-a-differ.html). Submit a support ticket if you need assistance.
  * **Aria products** : Migrate Aria application VMs similar to standard workload VMs. Also migrate any associated Content Library items to the target cluster datastores.
  * **Database platforms** : Rebuild database instances on the target cluster if they can't tolerate vMotion.



### Decommission the retired cluster

  1. After you complete and verify the migration of workloads and management VMs, delete the retiring cluster using the Google Cloud console, the REST API, or the Google Cloud CLI command line.
  2. Submit a quota request to reduce the quota of the source cluster hardware. In the request description, specify: 
     * `"ve1 hardware end of life"`
     * `"Retiring PC Name(s): [YOUR_PC_NAME(S)]"`
     * `"Retiring Cluster Name(s): [YOUR_CLUSTER_NAME(S)]"`



## Option 2: New private cloud migration

This method lets you deploy a completely new private cloud on the target hardware and migrate workloads from the retiring private cloud using VMware HCX.

### Request quota

  1. Submit a [quota request](https://docs.cloud.google.com/vmware-engine/quotas#requesting_quota) for the target hardware.
  2. In the request description, explicitly write: 
     * `"ve1 hardware end of life"`
     * `"Retiring PC Name(s): [YOUR_PC_NAME(S)]"`
     * `"Retiring Cluster Name(s): [YOUR_CLUSTER_NAME(S)]"`
     * `"New PC Name: [YOUR_NEW_PC_NAME]"`



### Create the new private cloud

  1. Use the Google Cloud console, the REST API, the Google Cloud CLI CLI, or Terraform to deploy your new private cloud on the target hardware.
  2. If your current deployment uses a legacy VMware Engine network (a VMware Engine network created before November 2022), create the new private cloud in the same project to continue using a legacy VMware Engine network. For more information, see [Standard and Legacy Google Cloud VMware Engine networks](https://docs.cloud.google.com/vmware-engine/docs/networking/vmware-engine-network).



### Migrate workloads using HCX

  1. Set up VMware HCX in the new private cloud.
  2. Link the HCX setups and configure migration meshes to move workloads and data from the retiring private cloud clusters. If your retiring private cloud has multiple clusters, ensure your HCX compute profiles and service meshes are configured to include all clusters from which you need to migrate workloads.
  3. Plan migration batches during appropriate maintenance windows.



### Adjust services and applications

  * **VMware HCX** : Deploy HCX service meshes on the new private cloud.
  * **Aria products** : If you use Google-licensed Aria suites, request support to install Aria Suite Lifecycle Manager (LCM) on the new private cloud.



### Decommission the old private cloud

  1. After you verify that all workloads function in the new private cloud, delete the old clusters and the private cloud itself.
  2. Submit a quota request to release the retired quota. In the request description, specify: 
     * `"ve1 hardware end of life"`
     * `"Retiring PC Name(s): [YOUR_PC_NAME(S)]"`
     * `"Retiring Cluster Name(s): [YOUR_CLUSTER_NAME(S)]"`



## Manage commitments and billing

Work with your account team to organize billing structures and align Committed Use Discounts (CUDs) during the migration.

### Committed Use Discount (CUD) adjustments

The impact of your `ve1` hardware migrations on your active `ve1` committed use discounts (CUDs) depends on timeline and capacity offers:

  * **Timeline overlap** : If your CUD commitments expire before the current node placement group's EoL date, your billing doesn't change.
  * **Migrating on ve1 nodes** : If your target capacity offer uses new `ve1` hardware, your CUD commitments remain valid through their term.
  * **Migrating to ve2 nodes** : Because CUD types bind to specific hardware categories, you must work with your account team to terminate or convert active `ve1` contracts: 
    * _Non-convertible CUDs_ : You must cancel existing standard CUDs and purchase new standard `ve2` CUDs.
    * _Convertible CUDs_ : You can convert active standard `ve1` CUDs to portable-license `ve2` CUDs.

Current Use | Timelines | Future offer | CUD impact  
---|---|---|---  
`ve1` | All `ve1` CUDs expire before EoL | `ve1` or `ve2` | Existing CUDs won't be impacted.  
`ve1` | Some `ve1` CUDs expire after EoL | `ve1` | The migration won't affect existing CUDs. The target `ve1` placement group has sufficient useful life.  
`ve1` | Some non-convertible `ve1` CUDs expire after EoL | `ve2` | You must terminate existing `ve1` CUDs and purchase new `ve2` CUDs. Work with your account team.  
`ve1` | Some convertible `ve1` CUDs expire after EoL | `ve2` | Convert `ve1` CUDs to appropriate `ve2` portable-license CUDs. Work with your account team.  
  
## What's next

  * Learn about [VMware Engine high availability and redundancy options](https://docs.cloud.google.com/vmware-engine/docs/concepts-high-availability-vmware).
  * Learn how to [manage private cloud autoscale policies](https://docs.cloud.google.com/vmware-engine/docs/howto-autoscale).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
