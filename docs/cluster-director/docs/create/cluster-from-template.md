---
url: https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template/
title: Create an AI-optimized cluster based on a template \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:10.755416+00:00
---

# Create an AI-optimized cluster based on a template  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Create an AI-optimized cluster based on a template Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a cluster in Cluster Director by using a pre-configured template that is optimized for running artificial intelligence (AI) and machine learning (ML) training workloads.

Cluster Director provides a set of templates that are pre-configured for most AI and ML training workloads. Each template specifies a set of optimized compute, networking, and storage resources that are designed for high reliability and resiliency. This approach helps you to quickly provision a cluster while maintaining the flexibility to make changes if your workload needs it.

To create a fully customized cluster, see instead [Create a custom cluster](https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster).

## Limitations

When you create a cluster in Cluster Director, the following limitations apply:

  * **Zonal scope** : all cluster resources must exist within the same zone. You can only create or use compute resources, storage resources, and subnetworks that exist within the same zone as your cluster. 
  * **Compute resource configuration per nodeset** : each nodeset in your cluster must meet the following requirements: 
    * You can specify only one compute resource configuration for each nodeset in your cluster. 
    * If you create A4X virtual machine (VM) instances in a cluster partition, then the total number of A4X VMs for each nodeset must be a multiple of 18. This total is the sum of the static node count and the dynamic node count. Because Compute Engine provisions A4X capacity in sub-blocks of 18 VMs, nodesets can't share unused capacity. 
  * **Storage classes for new Cloud Storage buckets** : if you plan to add new Cloud Storage buckets to your cluster, then you can specify only the Rapid storage class, Standard storage class, or Autoclass. If you want to use other storage classes, then you must update your buckets after you create them. For instructions, see [Change object storage classes](https://docs.cloud.google.com/storage/docs/changing-storage-classes). **Caution** : You can't change the storage class of a Rapid bucket after you create it. Rapid buckets are zonal resources and must always use the Rapid storage class. 
  * **Slurm controller version** : compute nodes can't run a newer Slurm version than the controller node. For example, if the controller node in your cluster uses Slurm 25.05, then your compute nodes can't use an OS image that requires Slurm 26.05. To check the Slurm version of an OS image, see [Supported OS images](https://docs.cloud.google.com/cluster-director/docs/os-images#included-software). 
  * **Hyperdisk pools** : if you plan to use storage pools for node boot disks, then you can use only existing storage pools or Hyperdisk Exapools that use Hyperdisk Balanced volumes. Storage pools must reside in the same project and zone as the nodes that use them.



## Templates for AI-optimized clusters

The following table describes the templates that you can use to create AI-optimized clusters in Cluster Director. When you create your cluster, you can either use the pre-configured settings in the template, or edit one or more settings based on the demands of your workloads.

Name | Description | Consumption option | Use cases  
---|---|---|---  
Large-scale model training with A3 Ultra | 

  * **Compute nodes** : 4 A3 Ultra VMs
  * **Storage** : 
    * 1 5 TiB basic SSD Filestore instance
    * 1 36 TiB Managed Lustre instance
  * **Login nodes** : 1 N2 VM

| 

  * Future reservations for more than 90 days (for capacity blocks)
  * Future reservations for up to 90 days (in calendar mode)

| This template is optimized for large-scale AI or ML training workloads.  
High-performance training with A4X | 

  * **Compute nodes** : 18 A4X VMs
  * **Storage** : 1 36 TiB and a 1,000 MBps/TiB tier Managed Lustre instance
  * **Login nodes** : 1 C4A VM

| Future reservations for capacity blocks | This template is optimized for compute and memory intensive workloads, such as multimodal inference workloads, and for the fastest reads and writes.  
Short-term training and experimentation with A4 | 

  * **Compute nodes** : 4 A4 VMs
  * **Storage** : 
    * 1 2 TiB basic SSD Filestore instance
    * 1 18 TiB Managed Lustre instance
  * **Login nodes** : 1 N2 VM

| Flex-start | This template is optimized for running pre-training, fine-tuning, and experimentation workloads for up to seven days.  
  
## Before you begin

Before you create a cluster in Cluster Director, do the following:

  1. **Choose consumption options**. If you haven't already, then you must choose the consumption options for the VMs that you want to use in each partition for your cluster. Each consumption option determines the availability, obtainability, and pricing for your VMs.

To learn more, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option).

  2. **Obtain capacity and quota**. Based on your chosen consumption option, review the quota requirements for the VMs that you want to create in the cluster. If you lack sufficient quota, then creating your cluster fails.

To learn more, see [Capacity and quota overview](https://docs.cloud.google.com/cluster-director/docs/obtain-capacity).

  3. **Verify usable reservations**. If you want to create your cluster by using one or more reservations, then verify that the reservations have enough available resources to create your chosen number of VMs in the cluster. Otherwise, skip this step.

To learn more, see [Consumable VMs in a reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-view#number-instances-reservation).

  4. **Verify trusted image policy**. If the organization in which your project exists has a trusted image policy (`constraints/compute.trustedImageProjects`), then verify that the `clusterdirector-public-images` project is included in the list of allowed projects.

To learn more, see [Setting up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access).

  5. **Verify existing resource requirements**. If you plan to use existing storage or networking resources in your cluster instead of creating new ones, then you must verify that those resources are correctly configured. Otherwise, skip this step.

To learn more, see [Cluster creation process overview](https://docs.cloud.google.com/cluster-director/docs/create/process-overview).




### Required roles

To get the permissions that you need to create a cluster based on a template, ask your administrator to grant you the following IAM roles: 

  * To create and manage a cluster: 
    * [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) on your project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account
  * To manage resources in a cluster: 
    * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project
    * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the Compute Engine default service account
    * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on the Compute Engine default service account
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Compute Engine default service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a cluster based on a template. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a cluster based on a template:

  * To create a cluster: `hypercomputecluster.clusters.create`
  * To check the status of the cluster creation operation: `hypercomputecluster.operations.get`
  * To view the details of a cluster: `hypercomputecluster.clusters.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an AI-optimized cluster based on a template

To create an AI-optimized cluster based on a template, complete the following steps:

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

  4. Select one of the available templates.

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

          3. In the **Location** section, select the region where you want to create Flex-start VMs. The Google Cloud console automatically filters the available regions to only show only those regions that support Flex-start VMs for your selected machine type.

        * To create Spot VMs, do the following:

          1. Click the **Use spot** tab.

          2. In the **On VM termination** list, select one of the following options:

             * To delete Spot VMs on preemption, select **Delete**.

             * To stop Spot VMs on preemption, select **Stop**.

          3. In the **Location** section, select the **Region** and **Zone** where you want to create Spot VMs. The Google Cloud console automatically filters the available regions to only show only those regions that support Spot VMs for your selected machine type.

     5. Click **Done**.

     6. Optional: To create additional compute resource configurations for a partition, click the add **Add resource configuration** , and then follow the prompts to specify the compute resources.

  8. Click **Continue**.




### Configure network

To configure the network that your cluster uses, complete the following steps:

  1. In the **Choose a Virtual Private Cloud (VPC) network** section, do one of the following:

     * Recommended: To let Cluster Director automatically create a pre-configured VPC network for your cluster, do the following:

       1. Select **Create a new VPC network**.

       2. In the **Network name** field, enter a name for the VPC network.

     * To use an existing VPC or Shared VPC network, do the following:

       1. Select **Use a VPC network in the current project** or **Use a Shared VPC network hosted in another project**.

       2. In the **Select VPC network** or **Shared VPC network** list, select a VPC or Shared VPC network that meets the [required configurations](https://docs.cloud.google.com/cluster-director/docs/create/process-overview#existing-network).

       3. In the **Select subnetwork** list, select an existing subnetwork.

  2. Click **Continue**.




### Configure storage resources

To configure the storage resources that your cluster uses, in the **Storage** section, complete the following steps:

  1. Optional: To edit a storage resource, click the edit **Edit storage plan** , and then follow the prompts to update the configuration of the storage resource.

  2. Optional: To add storage resources to your cluster, click add **Add storage configuration** , and then follow the prompts to specify the configuration for the storage resources.

**Tip:** If you want to use different Cloud Storage buckets for different projects or jobs, then you can mount the buckets on your cluster nodes for the duration of a Slurm job. This action lets you read or write data to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets). 
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

       5. In the **Source image** list, select one of the [supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images).

       6. In the **Static node count** field, enter the minimum number of compute instances that must always be running in the cluster.

       7. In the **Dynamic node count** field, enter a maximum number of compute instances that Cluster Director can increase the cluster to during increases in traffic.

**Important:** If you create compute instances in the nodeset by using a reservation, especially a shared reservation, then verify that the reservation has enough resources available to create your specified maximum number of compute instances. Other workloads that use the same reservation might fully use it and, thus, Cluster Director might be unable to create more compute instances in your nodeset.
       8. In the **Boot disk type** list and **Boot disk size** field, enter the type and size of the boot disk for the compute instances to use.

       9. Optional: To specify more advanced configurations for the compute node, expand **Advanced nodeset settings**. Then, follow the prompts to add or remove startup scripts, specify a startup script timeout, or add or remove labels.

       10. Click **Done**.

     * To remove a partition, click delete **Delete partition**.

  3. Optional: To add [prolog or epilog scripts](https://slurm.schedmd.com/prolog_epilog.html) to your Slurm environment, do the following:

     1. Expand the **Advanced orchestration settings** section.

     2. In the **Scripts** section, follow the prompts to add scripts.

  4. Click **Create**. The **Clusters** page appears.

Creating the cluster can take some time to complete. The completion time depends on the number of compute instances that you request and resource availability in the compute instance zone. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available. When Cluster Director creates your login node, you can connect to your cluster; however, you can only run workloads when Cluster Director creates the compute nodes in your cluster.




## What's next

  * [Connect to a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/connect-to-cluster)

  * [Node lifecycle](https://docs.cloud.google.com/cluster-director/docs/manage/node-lifecycle)

  * [Submit and monitor jobs with Slurm](https://docs.cloud.google.com/cluster-director/docs/workloads/configure-slurm)

  * [Modify a cluster](https://docs.cloud.google.com/cluster-director/docs/manage/modify-cluster)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
