---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster/
title: Create a fully managed Slurm cluster for AI workloads \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:53.004985+00:00
---

# Create a fully managed Slurm cluster for AI workloads  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create a fully managed Slurm cluster for AI workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to configure and deploy a fully managed Slurm cluster by using Cluster Director with A4X, A4, A3 Ultra, or A3 Mega machine types. To learn more about these accelerator-optimized machine types, see [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus).

[Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) is a Google Cloud product that automates the setup and configuration of Slurm clusters. This product is designed for IT administrators and AI researchers who want to avoid the overhead of managing a cluster and focus on running their workloads. If you want more control over cluster deployment, then [create your cluster by using Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster).

## Limitations

Depending on the machine type that the Compute Engine instances in your cluster use, the following limitations apply:

###  A4X 

**Caution:** The [ Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X machine series.

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) or [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use this machine type.
  * You can only create instances in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * This machine type is only available on the [NVIDIA Grace platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
  * Machine type changes aren't supported for A4X. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on this machine type. For a list of supported Linux operating systems, review the [supported operating systems for GPU instances](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).
  * For A4X instances, when you use `ethtool -S` to monitor GPU networking, the physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).
  * A4X instances don't support the following: 
    * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)
  * You can't attach Hyperdisk ML disks created before February 4, 2026 to A4X machine types.



###  A4 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A4 machine type.
  * You can only use an A4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The A4 machine type is only available on the [Emerald Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * You can't change the machine type of an instance to or from A4 machine type. You must create a new instance with this machine type.
  * A4 machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
  * You can't run Windows operating systems on an A4 machine type.
  * For A4 instances, when you use `ethtool -S` to monitor GPU networking, physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to A4 machine types.



###  A3 Ultra 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Ultra machine type.
  * You can only use an A3 Ultra machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The A3 Ultra machine type is only available on the [Emerald Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Ultra machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Ultra machine type.
  * A3 Ultra machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
  * For A3 Ultra instances, when you use `ethtool -S` to monitor GPU networking, physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).



###  A3 Mega 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Mega machine type.
  * You can only use an A3 Mega machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Mega machine type.
  * The A3 Mega machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Mega machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Mega machine type.



## Before you begin

Before creating a Slurm cluster, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). 
  3. **Verify that you have enough Filestore capacity quota** : you need to have enough Filestore quota in your target region before deploying. For A4X, A4, A3 Ultra, and A3 Mega machine types, you require a minimum of 10 TiB (10,240 GiB) of HIGH_SCALE_SSD (zonal) capacity. 

To check quota or request a quota increase, see the following:

     * To check quota in your project, see [View API-specific quota](https://docs.cloud.google.com/docs/quotas/view-manage#api_specific_quota).
     * If you don't have enough quota, then [request a quota increase](https://docs.cloud.google.com/filestore/docs/requesting-quota-increases).
  4. **Verify trusted image policy** : if the organization in which your project exists has a trusted image policy (`constraints/compute.trustedImageProjects`), then verify that the `clusterdirector-public-images` project is included in the list of allowed projects. To learn more, see [Setting up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access).



### Required roles

To create a Slurm cluster, you need the following IAM roles and permissions:

  * To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles: 

    * To create and manage a cluster: [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) on your project 
    * To create and manage VMs in a cluster: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
    * To consume a single-project reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project 
    * To consume a shared reservation: [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on both the owner project and any consumer project where you want to consume the reservation 
    * To connect to the login node in a cluster: 
      * [Compute OS Login ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.osLogin) (`roles/compute.osLogin`) on your project
      * [IAP-Secured Tunnel User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iap#iap.tunnelResourceAccessor) (`roles/iap.tunnelResourceAccessor`) on your project

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * To get the permissions that you need to complete this quickstart, ask your administrator to grant you the following IAM roles on the Compute Engine default service account: 

    * To create a cluster: [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 
    * To manage resources in a cluster: 
      * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`)
      * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`)
      * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`)




## Create a Slurm cluster

To create an AI-optimized cluster by using Cluster Director, complete the following steps:

  1. Configure compute resource configurations

  2. Configure network

  3. Configure storage resources

  4. Configure the Slurm environment




### Configure compute resource configurations

To configure compute resource configurations when creating a cluster, complete the following steps:

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director/overview)

  2. Click add **Create cluster**.

  3. In the dialog that appears, click **Reference architecture**. The **Create a cluster** page opens.

  4. Click one of the available templates. You can optionally edit the template to adapt it to your workload's needs.

  5. Click **Customize**.

  6. In the **Compute** section, in the **Cluster name** field, enter a name for your cluster. The name can contain up to 10 characters, and it can only use numbers or lowercase letters (`a`-`z`).

  7. To add information to the pre-configured compute resource configuration, or edit the number and type of compute instances that the configurations specifies, do the following:

     1. In the **Compute** section, click edit **Edit resource configuration**. The **Add resource configuration** pane appears.

     2. Optional: To change the compute resource configuration name, in the **Name** field, enter a new name.

     3. Optional: To change the number and type of compute instances that your cluster uses, in the **Machine configuration** section, follow the prompts to update the compute resources.

     4. In the **Consumption options** section, specify the consumption option that you want to use to obtain resources:

        * To create compute instances by using a reservation, do the following:

          1. Click the **Use reservation** tab.

          2. Click **Select reservation**. The **Choose a reservation** pane appears. If you want to use a reservation of A4X VMs, then you can optionally choose the [block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) or [sub-block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) to control the placement of your VMs.

          3. Select the reservation that you want to use. Then, click **Choose**. This action automatically sets the **Region** and **Zone** of your compute resources.

        * To create Flex-start VMs, do the following:

          1. Click the **Flex start** tab.

          2. In the **Time limit for the VM** section, specify the run duration for the compute instances. The value must be between 10 minutes and 7 days.

          3. In the **Location** section, select the region where you want to create Flex-start VMs. The Google Cloud console automatically filters the available regions to only show those regions that support Flex-start VMs for your selected machine type.

        * To create Spot VMs, do the following:

          1. Click the **Use spot** tab.

          2. In the **On VM termination** list, select one of the following options:

             * To delete Spot VMs on preemption, select **Delete**.

             * To stop Spot VMs on preemption, select **Stop**.

          3. In the **Location** section, select the **Region** and **Zone** where you want to create Spot VMs. The Google Cloud console automatically filters the available regions to only show those regions that support Spot VMs for your selected machine type.

     5. Click **Done**.

     6. Optional: To create additional compute resource configurations for a partition, click the add **Add resource configuration** , and then follow the prompts to specify the compute resources.

  8. Click **Continue**.




### Configure network

To configure the network that your cluster uses, complete the following steps:

  1. In the **Choose a Virtual Private Cloud (VPC) network** section, do one of the following:

     * Recommended: To let AI Hypercomputer automatically create a pre-configured VPC network for your cluster, do the following:

       1. Select **Create a new VPC network**.

       2. In the **Network name** field, enter a name for the VPC network.

     * To use an existing VPC or Shared VPC network, do the following:

       1. Select **Use a VPC network in the current project** or **Use a Shared VPC network hosted in another project**.

       2. In the **Select VPC network** or **Shared VPC network** list, select a VPC or Shared VPC network that meets the [required configurations](https://docs.cloud.google.com/cluster-director/docs/create/process-overview#existing-network).

       3. In the **Select subnetwork** list, select an existing subnetwork.

  2. Click **Continue**.




### Configure storage resources

When you create a cluster from a Cluster Director template, Cluster Director automatically configures a Filestore or Managed Lustre instance as the storage resource for your cluster.

To optionally add or edit the storage resources that your cluster uses, in the **Storage** section, complete the following steps. For more information about the storage services that you can configure, see [Supported storage services for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/storage).

  1. Optional: To edit a storage resource, click edit **Edit storage plan** , and then follow the prompts to update the configuration of the storage resource.

  2. Optional: To add storage resources to your cluster, click add **Add storage configuration** , and then follow the prompts to specify the configuration for the storage resources.

To view the available storage services you can configure, see [Supported storage services for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/storage).

  3. Click **Continue**.




### Configure the Slurm environment

To configure the Slurm environment in your cluster, complete the following steps:

  1. Optional: To edit the number and type of compute instances that the login node uses, expand the **Login node** section, and then follow the prompts to update the compute resources.

  2. Optional: To edit partitions of your cluster to organize your compute resources, expand the **Partitions** section, and then do one of the following:

     * To add a partition, click **Add partition** , and then do the following:

       1. In the **Partition name** field, enter a name for the partition.

       2. To edit a nodeset, click **Toggle nodeset**. Otherwise, to add a nodeset, click **Add nodeset**.

       3. In the **Nodeset name** field, enter a name for your nodeset.

       4. In the **Resource configuration** field, select a compute resource configuration that you created in the previous steps.

       5. In the **Source image** list, select one of the [supported OS images for AI Hypercomputer](https://docs.cloud.google.com/cluster-director/docs/compute#os-images).

       6. In the **Static node count** field, enter the minimum number of compute instances that must always be running in the cluster.

       7. In the **Dynamic node count** field, enter a maximum number of compute instances that AI Hypercomputer can increase the cluster to during increases in traffic.

**Important:** If you create compute instances in the nodeset by using a reservation, especially a shared reservation, then verify that the reservation has enough resources available to create your specified maximum number of compute instances. Other workloads that use the same reservation might fully consume it and, therefore, AI Hypercomputer might be unable to create more compute instances in your nodeset.
       8. In the **Boot disk type** list and **Boot disk size** field, enter the type and size of the boot disk for the compute instances to use.

       9. Click **Done**.

     * To remove a partition, click delete **Delete partition**.

  3. Optional: To add [prolog or epilog scripts](https://slurm.schedmd.com/prolog_epilog.html) to your Slurm environment, do the following:

     1. Expand the **Advanced orchestration settings** section.

     2. In the **Scripts** section, follow the prompts to add scripts.

  4. Click **Create**. The **Clusters** page appears. Creating the cluster can take some time to complete. The completion time depends on the number of compute instances that you request and resource availability in the compute instances' zone. If your requested resources are unavailable, then AI Hypercomputer maintains the creation request until resources become available. To view the status of the cluster create operation, [view your cluster's details](https://docs.cloud.google.com/cluster-director/docs/manage/view-clusters#describe).




## Connect to the Slurm cluster

When AI Hypercomputer creates your login node, the cluster state changes to **Ready**. You can then connect to your cluster; however, you can run workloads only after AI Hypercomputer creates the compute nodes in the cluster.

To connect to a cluster's login node through SSH by using the Google Cloud console, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/cluster-director/clusters/list)

  2. In the **Clusters** table, in the **Name** column, click the name of the cluster that you created in the previous section. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  3. Click the **Nodes** tab.

  4. In the **Login nodes** section, in the **Connect** column, locate the cluster's login node, which name is `CLUSTER_NAME-login-001`.

  5. In the **Connect** column within the login's node, click the **SSH** button. The **SSH-in-browser** window opens.

  6. If prompted, then click **Authorize**. Connecting to your node can take up to a minute to complete.

**Note:** If you encounter errors when connecting to your node, then see [Troubleshooting SSH errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-ssh-errors).



## Verify Slurm cluster health

Before you run a job on a compute node, Slurm automatically runs a quick GPU health check on the node. If the node fails the check, then Slurm drains the node and prevents scheduling new jobs on it.

To more thoroughly test GPU health and network bandwidth across the compute nodes in a cluster partition, you can manually run [NVIDIA Collective Communications Library (NCCL) tests](https://developer.nvidia.com/nccl). If an NCCL test identifies any unhealthy nodes, then you can repair the nodes or modify your cluster. NCCL tests help you verify a cluster's health before you run critical workloads. For more information, see [Verify cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#verify-health).

## Delete the Slurm cluster

To delete a Slurm cluster in your project, select one of the following options:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/cluster-director/clusters/list)

  2. In the **Clusters** table, in the **Name** column, click the name of the cluster that you want to delete. A page that gives the details of the cluster appears, and the **Details** tab is selected.

  3. Click delete **Delete**.

  4. In the dialog that appears, enter the name of your cluster, and then click **Delete** to confirm. The **Clusters** page appears. Deleting your cluster can take some time to complete.




## What's next

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)

  * [View cluster topology](https://docs.cloud.google.com/cluster-director/docs/monitor/view-topology)

  * [Manage cluster health](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health)

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
