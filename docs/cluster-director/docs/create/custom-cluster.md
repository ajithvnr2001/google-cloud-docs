---
url: https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster/
title: Create a custom cluster \u00a0|\u00a0 Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:10.995759+00:00
---

# Create a custom cluster  |  Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/create/custom-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Create a custom cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a cluster in Cluster Director where you fully customize the compute, networking, and storage resources for your specific artificial intelligence (AI), machine learning (ML), or high performance computing (HPC) workloads.

This process lets you design a fault-tolerant and highly scalable Slurm environment with your own custom specifications, helping your cluster meet the needs of your workloads. To create a cluster based on a template that is optimized for running AI and ML workloads, see instead [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template).

## Limitations

When you create a cluster in Cluster Director, the following limitations apply:

  * **Zonal scope** : all cluster resources must exist within the same zone. You can only create or use compute resources, storage resources, and subnetworks that exist within the same zone as your cluster. 
  * **Compute resource configuration per nodeset** : each nodeset in your cluster must meet the following requirements: 
    * You can specify only one compute resource configuration for each nodeset in your cluster. 
    * If you create A4X virtual machine (VM) instances in a cluster partition, then the total number of A4X VMs for each nodeset must be a multiple of 18. This total is the sum of the static node count and the dynamic node count. Because Compute Engine provisions A4X capacity in sub-blocks of 18 VMs, nodesets can't share unused capacity. 
  * **Storage classes for new Cloud Storage buckets** : if you plan to add new Cloud Storage buckets to your cluster, then you can specify only the Rapid storage class, Standard storage class, or Autoclass. If you want to use other storage classes, then you must update your buckets after you create them. For instructions, see [Change object storage classes](https://docs.cloud.google.com/storage/docs/changing-storage-classes). **Caution** : You can't change the storage class of a Rapid bucket after you create it. Rapid buckets are zonal resources and must always use the Rapid storage class. 
  * **Slurm controller version** : clusters must meet the following Slurm version requirements: 
    * You can specify the Slurm controller version only when you create a cluster by using the Google Cloud CLI or the REST API; you can't modify the controller version for an existing cluster. 
    * Compute nodes can't run a newer Slurm version than the controller node. For example, if the controller in your cluster node uses Slurm 25.05, then your compute nodes can't use an OS image that requires Slurm 26.05. To check the Slurm version of an OS image, see [Supported OS images](https://docs.cloud.google.com/cluster-director/docs/os-images#included-software). 
  * **Hyperdisk pools** : if you plan to use storage pools for node boot disks, then you can use only existing storage pools or Hyperdisk Exapools that use Hyperdisk Balanced volumes. Storage pools must reside in the same project and zone as the nodes that use them.



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

  6. **Authenticate**. To use the samples on this page, you might need to authenticate to Google.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

     2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

     3. If you're using a local shell, then create local authentication credentials for your user account: 
            
            gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create a custom cluster from scratch, ask your administrator to grant you the following IAM roles: 

  * To create and manage a cluster: 
    * [Cluster Director Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/hypercomputecluster#hypercomputecluster.editor) (`roles/hypercomputecluster.editor`) on your project
    * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Compute Engine default service account
  * To manage resources in a cluster: 
    * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) on your project
    * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on the Compute Engine default service account
    * [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) on the Compute Engine default service account
    * [Storage Object Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectViewer) (`roles/storage.objectViewer`) on the Compute Engine default service account



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a custom cluster from scratch. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a custom cluster from scratch:

  * To create a cluster: `hypercomputecluster.clusters.create`
  * To check the status of the cluster creation operation: `hypercomputecluster.operations.get`
  * To view the details of a cluster: `hypercomputecluster.clusters.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a custom cluster from scratch

To create a custom cluster from scratch, select one of the following options. If you want to configure the Slurm controller version for the controller node, then you must use the gcloud CLI or the REST API. If you want to configure custom Slurm settings, then use the REST API.

###  Console 

  1. In the Google Cloud console, go to the **Cluster Director** page.

[Go to Cluster Director](https://console.cloud.google.com/cluster-director/overview)

  2. Click add **Create cluster**.

  3. In dialog that appears, click **Step-by-step configuration**. The **Create cluster** page opens.

  4. In the **Cluster name** field, enter a name for your cluster. The name can contain up to 10 characters, and it can only use numbers or lowercase letters (`a`-`z`). Spaces or special characters aren't allowed.

  5. In the **Compute** section, click **Configure resources**. The **Add resource configuration** pane appears.

  6. To configure a compute resource configuration, complete the following steps:

     1. In the **Machine configuration** section, select the machine series and type that you want to use.

     2. In the **Number of instances** field, enter the number of Compute Engine instances to use for the configuration.

     3. In the **Consumption options** section, specify the consumption option that you want to use to obtain resources:

        * To create GPU instances by using a reservation, do the following:

          1. Click the **Use reservation** tab.

          2. Click **Select reservation**. The **Choose a reservation** pane appears. If you want to use a reservation of A4X VMs, then you can optionally choose the [block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) or [sub-block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) to control the placement of your VMs.

          3. Select the reservation that you want to use. Then, click **Choose**. This action automatically sets the **Region** and **Zone** fields to the region and zone of your reservation.

        * To create GPU Flex-start VMs, do the following:

          1. Click the **Flex start** tab.

          2. In the **Time limit for the VM** section, specify the run duration for the Flex-start VMs. The value must be between 10 minutes and 7 days.

          3. In the **Location** section, select the region where you want to create Flex-start VMs. The Google Cloud console automatically filters the available regions to only show those regions that support Flex-start VMs for your selected machine type.

        * To create GPU or N2 Spot VMs, do the following:

          1. Click the **Use spot** tab.

          2. In the **On VM termination** list, select one of the following options:

             * To delete Spot VMs on preemption, select **Delete**.

             * To stop Spot VMs on preemption, select **Stop**.

          3. In the **Location** section, select the **Region** and **Zone** where you want to create Spot VMs. The Google Cloud console automatically filters the available regions to only show those regions that support Spot VMs for your selected machine type.

        * To create N2 instances, do the following:

          1. Click the **Use on-demand** tab.

          2. In the **Location** section, select the region where you want to create instances.

     4. Click **Done**.

     5. Optional: To create additional compute resource configurations, click the add **Add resource configuration** , and then follow the prompts to specify the compute resources.

  7. Click **Continue**.

  8. In the **Choose a Virtual Private Cloud (VPC) network** section, do one of the following:

     * Recommended: To let Cluster Director automatically create a pre-configured VPC network for your cluster, do the following:

       1. Select **Create a new VPC network**.

       2. In the **Network name** field, enter a name for the VPC network.

     * To use an existing VPC or Shared VPC network, do the following:

       1. Select **Use a VPC network in the current project** or **Use a Shared VPC network hosted in another project**.

       2. In the **Select VPC network** or **Shared VPC network** list, select a VPC or Shared VPC network that meets the [required configurations](https://docs.cloud.google.com/cluster-director/docs/create/process-overview#existing-network).

       3. In the **Select subnetwork** list, select an existing subnetwork.

  9. Click **Continue**.

  10. Optional: To edit a storage resource, in the **Storage** section, click the edit **Edit storage plan** , and then do one of the following:

     * To specify a Filestore instance, do the following:

       1. Click the **Filestore** tab.

       2. In the **Instance provisioning** section, select one of the following options:

          * To use an existing Filestore instance that uses the same network as your cluster, select **Select existing Filestore instance** , and then select the instance.

          * To create a new Filestore instance, select **Create new instance**. Then, follow the prompts to create your instance. For more information about the configurations that you can specify in the instance, see [Create an instance](https://docs.cloud.google.com/filestore/docs/creating-instances).

     * To specify a Google Cloud Managed Lustre instance, do the following:

       1. Click the **Managed Lustre** tab.

       2. In the **Instance provisioning** section, select one of the following options:

          * To use an existing Managed Lustre instance, select **Select an existing Managed Lustre instance** , and then select the instance.

          * To create a new Managed Lustre instance, select **Create new instance**. Then, follow the prompts to create your instance. For more information about the configurations that you can specify in the instance, see [Create a Managed Lustre instance](https://docs.cloud.google.com/managed-lustre/docs/create-instance).

     * To specify a Cloud Storage bucket, do the following:

       1. Click the **Cloud Storage** tab.

       2. In the **Bucket provisioning** section, select one of the following options:

          * To use an existing Cloud Storage bucket, select **Select an existing bucket** , and then select the bucket.

          * To create a new Cloud Storage bucket, select **Create a new bucket** , and then follow the prompts to create your bucket. For more information about the configurations that you can specify in the bucket, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).

  11. Optional: To add storage resources to your cluster, click add **Add storage configuration** , and then follow the prompts to specify the configuration for the storage resource.

**Tip:** If you want to use different Cloud Storage buckets for different projects or jobs, then you can mount the buckets on your cluster nodes for the duration of a Slurm job. This action lets you read or write data to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets). 
  12. Click **Continue**.

  13. Optional: To edit the number and type of compute instances that the login node uses, expand the **Login node** section, and then complete the following steps:

     1. In the **Machine type** field, specify a machine type for the login node. If you use A4X instances in your cluster, then specify a C4A machine type. Otherwise, specify an N2 machine type.

     2. Optional: To specify a custom OS image instead of the one that Cluster Director automatically configures for the login node, in the **Source image** field, select one of the [supported OS images for Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images).

  14. In the **Node count** field, enter the number of compute instances to use in the login node.

  15. Optional: To specify a startup script for the compute instances, in the **Startup script** field, enter your script. For more information about this type of scripts, see [About startup scripts](https://docs.cloud.google.com/compute/docs/instances/startup-scripts).

  16. Optional: To specify a timeout for the startup script, in the **Startup script timeout** field, enter a value in seconds. The default value is `300` (300 seconds, or five minutes). The minimum allowed value is `1` (one second).

  17. In the **Boot disk type** and **Boot disk size** fields, select a boot disk type and size for the compute instances in the login node. For more information about the boot disks that your compute instances can use, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

  18. Optional: To specify more advanced configurations for the login node, expand **Advanced login node settings**. Then, follow the prompts to manage OS login, manage public IPs, or add or remove labels to the compute instances in the login node.

  19. Optional: To edit the partitions of your cluster to organize your compute resources, expand the **Partitions** section, and then do one of the following:

     * To add a partition, click **Add partition** , and then do the following:

       1. In the **Partition name** field, enter a name for the partition.

       2. To edit a nodeset, click **Toggle nodeset**. To add a nodeset, click **Add nodeset**.

       3. In the **Nodeset name** field, enter a name for your nodeset.

       4. In the **Resource configuration** field, select a compute resource configuration that you created in the previous steps.

       5. In the **Source image** field, select an OS image to use for the compute nodes in the nodeset.

       6. In the **Static node count** field, enter the minimum number of compute instances that must always be running in the cluster.

       7. In the **Dynamic node count** field, enter a limit of compute instances that Cluster Director can increase the cluster to during increases in traffic.

**Important:** If you create compute instances in the nodeset by using a reservation, especially a shared reservation, then verify that the reservation has enough resources available to create your specified maximum number of compute instances. Other workloads that use the same reservation might fully use it and, thus, Cluster Director might be unable to create more compute instances in your nodeset.
       8. In the **Boot disk type** list and **Boot disk size** fields, enter the type and size of the boot disk for the compute instances to use.

       9. Optional: To share disk capacity and performance across nodes in a nodeset, specify an existing Hyperdisk pool or Hyperdisk Exapool as follows:

          1. Select the **Enable storage pool** checkbox.

          2. In the **Select a storage pool** list, select a storage pool that uses Hyperdisk Balanced volumes.

       10. Optional: To specify more advanced configurations for the compute node, expand **Advanced nodeset settings**. Then, follow the prompts to add or remove startup scripts, specify a startup script timeout, or add or remove labels.

       11. Click **Done**.

     * To remove a partition, click delete **Delete partition**.

  20. Optional: To add a partition to your cluster, click **Add partition** , and then follow the prompts to specify the compute resources for the partition.

  21. Optional: To add [prolog or epilog scripts](https://slurm.schedmd.com/prolog_epilog.html) to your Slurm cluster, do the following:

     1. Expand the **Advanced orchestration settings** section.

     2. In the **Scripts** section, follow the prompts to add prolog or epilog scripts.

  22. Click **Create**. The **Clusters** page appears.

Creating the cluster can take some time to complete. The completion time depends on the number of compute instances that you request and resource availability in the compute instances' zone. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available. When Cluster Director creates your login node, you can connect to your cluster; however, you can only run workloads when Cluster Director creates the compute nodes in your cluster.




###  gcloud 

To create a custom cluster from scratch, use the [`gcloud alpha cluster-director clusters create` command](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/cluster-director/clusters/create).

Based on how you want to specify the cluster configuration, use one of the following methods:

  * **Specify a configuration file** : to create a cluster by specifying the cluster configuration in a JSON file, use the `--config` flag. To run the command, select one of the following options:

###  Bash 
        
        gcloud alpha cluster-director clusters create CLUSTER_NAME \
            --location=REGION \
            --config=CONFIGURATION_FILE
        

###  Powershell 
        
        gcloud alpha cluster-director clusters create CLUSTER_NAME `
            --location=REGION `
            --config=CONFIGURATION_FILE
        

###  cmd.exe 
        
        gcloud alpha cluster-director clusters create CLUSTER_NAME ^
            --location=REGION ^
            --config=CONFIGURATION_FILE
        

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster. The name can contain up to 10 characters, and it can only use numbers or lowercase letters.

    * `REGION`: the region where to create your cluster.

    * `CONFIGURATION_FILE`: the path to the JSON file that contains the configuration details for the cluster. To review the configuration details that you can specify, review the [request body for creating a cluster by using REST](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters#Cluster).

  * **Specify cluster properties directly** : to create a cluster by specifying each configuration property directly, use the following flags:

    * To specify a network, use one of the following flags:

      * To create a new network: `--create-network`

      * To use an existing network and subnetwork: `--network` and `--subnet`

    * To specify a Filestore instance, use one of the following flags:

      * To create a new instance: `--create-filestores`

      * To use an existing instance: `--filestores`

    * Optionally, to specify a Cloud Storage bucket, use one of the following flags:

      * To create a new bucket: `--create-buckets`

      * To use an existing bucket: `--buckets`

**Tip:** If you want to use different Cloud Storage buckets for different projects or jobs, then you can mount the buckets on your cluster nodes for the duration of a Slurm job. This action lets you read or write data to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets). 
    * Optionally, to specify a Google Cloud Managed Lustre instance, use one of the following flags:

      * To create a new instance: `--create-lustres`

      * To use an existing instance: `--lustres`

    * To specify a compute resource configuration, use one of the following flags for each resource configuration that you want to create in the cluster.

      * To create compute instances by using a reservation: `--reserved-instances`

      * To create Flex-start VMs: `--dws-flex-instances`

      * To create Spot VMs: `--spot-instances`

      * To create N2 on-demand instances: `--on-demand-instances`

    * To specify the configuration for the login node, use the `--slurm-login-node` flag.

    * To specify the configuration for a compute nodeset, use the `--slurm-node-sets` flag. You can repeat this flag for each nodeset in the cluster.

    * To specify the cluster partitions, use the `--slurm-partitions` flag. You can repeat this flag for each partition in the cluster.

    * To specify the default partition for the cluster, use the `--slurm-default-partition` flag.

    * Optionally, to specify the Slurm version for the controller node in your cluster, use the `--controller-version` flag.

For example, suppose that you want to create a cluster that has one partition with reserved compute instances, one partition with Spot VMs, a new Filestore instance, and a new network. To create the example cluster, select one of the following options:

###  Bash 
    
    gcloud alpha cluster-director clusters create CLUSTER_NAME \
        --location=REGION \
        --create-network=name=NETWORK_NAME \
        --create-filestores=name="locations/FILESTORE_INSTANCE_ZONE/instances/FILESTORE_INSTANCE_NAME",tier=TIER,capacityGb=CAPACITY,fileshare=SHARE_NAME,protocol=PROTOCOL \
        --reserved-instances=id=COMPUTE_RESOURCE_NAME_1,reservation="projects/RESERVATION_PROJECT_ID/zones/RESERVATION_ZONE/reservations/RESERVATION_NAME",machineType=RESERVATION_MACHINE_TYPE \
        --spot-instances=id=COMPUTE_RESOURCE_NAME_2,zone=SPOT_VMS_ZONE,machineType=SPOT_MACHINE_TYPE \
        --slurm-login-node=machineType=LOGIN_NODE_MACHINE_TYPE,zone=LOGIN_NODE_ZONE,count=LOGIN_NODES_COUNT \
        --slurm-node-sets=id=NODESET_NAME_1,computeId=COMPUTE_RESOURCE_NAME_1,staticNodeCount=NODESET_1_STATIC_COUNT,maxDynamicNodeCount=NODESET_1_MAX_DYNAMIC_COUNT \
        --slurm-node-sets=id=NODESET_NAME_2,computeId=COMPUTE_RESOURCE_NAME_2,staticNodeCount=NODESET_2_STATIC_COUNT,maxDynamicNodeCount=NODESET_2_MAX_DYNAMIC_COUNT \
        --slurm-partitions=id=PARTITION_NAME_1,nodesetIds=[NODESET_NAME_1] \
        --slurm-partitions=id=PARTITION_NAME_2,nodesetIds=[NODESET_NAME_2] \
        --slurm-default-partition=PARTITION_NAME_1
    

###  Powershell 
    
    gcloud alpha cluster-director clusters create CLUSTER_NAME `
        --location=REGION `
        --create-network=name=NETWORK_NAME `
        --create-filestores=name="locations/FILESTORE_INSTANCE_ZONE/instances/FILESTORE_INSTANCE_NAME",tier=TIER,capacityGb=CAPACITY,fileshare=SHARE_NAME,protocol=PROTOCOL `
        --reserved-instances=id=COMPUTE_RESOURCE_NAME_1,reservation="projects/RESERVATION_PROJECT_ID/zones/RESERVATION_ZONE/reservations/RESERVATION_NAME" `
        --spot-instances=id=COMPUTE_RESOURCE_NAME_2,zone=SPOT_VMS_ZONE,machineType=SPOT_MACHINE_TYPE `
        --slurm-login-node=machineType=LOGIN_NODE_MACHINE_TYPE,zone=LOGIN_NODE_ZONE,count=LOGIN_NODES_COUNT `
        --slurm-node-sets=id=NODESET_NAME_1,computeId=COMPUTE_RESOURCE_NAME_1,staticNodeCount=NODESET_1_STATIC_COUNT,maxDynamicNodeCount=NODESET_1_MAX_DYNAMIC_COUNT `
        --slurm-node-sets=id=NODESET_NAME_2,computeId=COMPUTE_RESOURCE_NAME_2,staticNodeCount=NODESET_2_STATIC_COUNT,maxDynamicNodeCount=NODESET_2_MAX_DYNAMIC_COUNT `
        --slurm-partitions=id=PARTITION_NAME_1,nodesetIds=[NODESET_NAME_1] `
        --slurm-partitions=id=PARTITION_NAME_2,nodesetIds=[NODESET_NAME_2] `
        --slurm-default-partition=PARTITION_NAME_1
    

###  cmd.exe 
    
    gcloud alpha cluster-director clusters create CLUSTER_NAME ^
        --location=REGION ^
        --create-network=name=NETWORK_NAME ^
        --create-filestores=name="locations/FILESTORE_INSTANCE_ZONE/instances/FILESTORE_INSTANCE_NAME",tier=TIER,capacityGb=CAPACITY,fileshare=SHARE_NAME,protocol=PROTOCOL ^
        --reserved-instances=id=COMPUTE_RESOURCE_NAME_1,reservation="projects/RESERVATION_PROJECT_ID/zones/RESERVATION_ZONE/reservations/RESERVATION_NAME" ^
        --spot-instances=id=COMPUTE_RESOURCE_NAME_2,zone=SPOT_VMS_ZONE,machineType=SPOT_MACHINE_TYPE ^
        --slurm-login-node=machineType=LOGIN_NODE_MACHINE_TYPE,zone=LOGIN_NODE_ZONE,count=LOGIN_NODES_COUNT ^
        --slurm-node-sets=id=NODESET_NAME_1,computeId=COMPUTE_RESOURCE_NAME_1,staticNodeCount=NODESET_1_STATIC_COUNT,maxDynamicNodeCount=NODESET_1_MAX_DYNAMIC_COUNT ^
        --slurm-node-sets=id=NODESET_NAME_2,computeId=COMPUTE_RESOURCE_NAME_2,staticNodeCount=NODESET_2_STATIC_COUNT,maxDynamicNodeCount=NODESET_2_MAX_DYNAMIC_COUNT ^
        --slurm-partitions=id=PARTITION_NAME_1,nodesetIds=[NODESET_NAME_1] ^
        --slurm-partitions=id=PARTITION_NAME_2,nodesetIds=[NODESET_NAME_2] ^
        --slurm-default-partition=PARTITION_NAME_1
    

Replace the following:

    * `CLUSTER_NAME`: the name of the cluster. The name can contain up to 10 characters, and it can only use numbers or lowercase letters (`a`-`z`). Spaces or special characters aren't allowed.

    * `REGION`: the region where to create your cluster.

    * `NETWORK_NAME`: the name of the network that you want to create.

    * `FILESTORE_INSTANCE_ZONE`: the zone where you want to create your Filestore instance.

    * `FILESTORE_INSTANCE_NAME`: the name for your Filestore instance.

    * `TIER`: the type of [service tier](https://docs.cloud.google.com/filestore/docs/service-tiers) that you want to use for the instance and that Cluster Director supports. Specify one of the following values:

      * For the zonal tier: `ZONAL`

      * For the regional tier: `REGIONAL`

    * `CAPACITY`: the size, in GiB, that you want to allocate for the instance. The value must be between 1,024 GiB (`1024`) and 102,400 GiB (`102400`), and it must be in 256 GiB (`256`) increments.

    * `SHARE_NAME`: the name for the NFS file share that is served from the instance.

    * `PROTOCOL`: the [system protocol](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) for the instance. Specify one of the following values:

      * For NFSv3: `NFSV3`

      * For NFSv4.1: `NFSV41`

    * `COMPUTE_RESOURCE_NAME_1` and `COMPUTE_RESOURCE_NAME_2`: the name of the two compute resource configurations.

    * `RESERVATION_PROJECT_ID`: the ID of the project where the reservation exists. If you want to use a reservation from a different project, then verify that your project is allowed to consume the reservation. For more information, see [Allow and restrict projects from creating and modifying shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).

    * `RESERVATION_ZONE`: the zone where the reservation exists.

    * `RESERVATION_NAME`: the name of the reservation that you want to use to create VMs. If you use a reservation of A4X VMs, then you can optionally specify the [block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) or [sub-block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) to control the placement of your VMs:

      * **Block** : `RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME`

      * **Sub-block** : `RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUB_BLOCK_NAME`

    * `RESERVATION_MACHINE_TYPE`: the machine type that is specified in the reservation.

    * `SPOT_VMS_ZONE`: the zone where you want to create your Spot VMs. To review the regions and zones where the machine type that you want to use is available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

    * `SPOT_MACHINE_TYPE`: the machine type to use for the Spot VMs. Specify one of the following machine types:

      * For an A4X machine type: `a4x-highgpu-4g`

      * For an A4 machine type: `a4-highgpu-8g`

      * For an A3 Ultra machine type: `a3-ultragpu-8g`

      * For an A3 Mega machine type: `a3-megagpu-8g`

      * For an N2 machine type, see [N2 machine series](https://docs.cloud.google.com/cluster-director/docs/compute#n2-series).

    * `LOGIN_NODE_MACHINE_TYPE`: the machine type that you want the compute instances in the login nodeset to use. If you use A4X instances in your cluster, then specify a C4A machine type. Otherwise, specify an N2 machine type.

    * `STARTUP_SCRIPT_TIMEOUT`: the maximum time that the startup script can run, for example `300s`. The default value is `300s` (300 seconds, or five minutes). The minimum allowed value is `1s` (one second).

    * `LOGIN_NODE_ZONE`: the zone where you want to create the compute instances in the login nodeset.

    * `LOGIN_NODES_COUNT`: the number of compute instances to use for the login nodeset.

    * `NODESET_NAME_1` and `NODESET_NAME_2`: the name of the two nodesets.

    * `NODESET_1_STATIC_COUNT` and `NODESET_2_STATIC_COUNT`: the minimum number of compute instances that must always be running in each nodeset.

    * `NODESET_1_MAX_DYNAMIC_COUNT` and `NODESET_2_MAX_DYNAMIC_COUNT`: the maximum number of compute instances that Cluster Director can add to each nodeset during increases in traffic.

**Important:** If you create compute instances in the nodeset by using a reservation, especially a shared reservation, then verify that the reservation has enough resources available to create your specified maximum number of compute instances. Other workloads that use the same reservation might fully use it and, thus, Cluster Director might be unable to create more compute instances in your nodeset.
    * `PARTITION_NAME_1` and `PARTITION_NAME_2`: the name of the partitions for your cluster.




The output is similar to the following:
    
    
    Create request issued for: [cluster000]
    Waiting for operation [projects/example-project/locations/us-central1/operations/operation-1759856594716-640948b2f058e-f403bef9-1a08178a] to complete...working...
    

Creating the cluster can take some time to complete. The completion time depends on the number of compute instances that you request and resource availability in the compute instances' zone. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available. When Cluster Director creates your login node, the output is similar to the following:
    
    
    Created cluster [cluster000].
    

You can then connect to your cluster; however, you can only run workloads when Cluster Director creates the compute nodes in your cluster.

###  Terraform 

To create a custom cluster from scratch, use the [`google_hypercomputecluster_cluster` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/hypercomputecluster_cluster).

**Tip:** If you want to use different Cloud Storage buckets for different projects or jobs, then you can mount the buckets on your cluster nodes for the duration of a Slurm job. This action lets you read or write data to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets). 

For example, suppose that you want to create a cluster that has one partition with reserved compute instances, one partition with Spot VMs, a new Filestore instance, and a new network. To create the example cluster, use the following resource:
    
    
    resource "google_hypercomputecluster_cluster" "default" {
      cluster_id = "cluster001"
      location   = "europe-west1"
    
      network_resources {
        id = "cnet"
        config {
          new_network {
            network = "projects/my-project/global/networks/new-network"
          }
        }
      }
    
      compute_resources {
        id = "comp1"
        config {
          new_reserved_instances {
            reservation = "projects/my-project/zones/europe-west1-b/reservations/example-reservation"
          }
        }
      }
    
      compute_resources {
        id = "comp2"
        config {
          new_spot_instances {
            machine_type = "n2-standard-4"
            zone         = "europe-west1-b"
          }
        }
      }
    
      orchestrator {
        slurm {
          default_partition = "part1"
          login_nodes {
            count             = "1"
            enable_os_login   = true
            enable_public_ips = true
            machine_type      = "n2-standard-4"
            zone              = "europe-west1-b"
          }
    
          node_sets {
            id                = "nodeset1"
            compute_id        = "comp1"
            static_node_count = "1"
            compute_instance {
              boot_disk {
                size_gb = "100"
                type    = "pd-balanced"
              }
            }
            storage_configs {
              id          = "fs1"
              local_mount = "/home"
            }
          }
    
          node_sets {
            id                = "nodeset2"
            compute_id        = "comp2"
            static_node_count = "1"
            compute_instance {
              boot_disk {
                size_gb = "100"
                type    = "pd-balanced"
              }
            }
            storage_configs {
              id          = "fs1"
              local_mount = "/home"
            }
          }
    
          partitions {
            id           = "part1"
            node_set_ids = ["nodeset1"]
          }
          partitions {
            id           = "part2"
            node_set_ids = ["nodeset2"]
          }
        }
      }
    
      storage_resources {
        id = "fs1"
        config {
          new_filestore {
            filestore = "projects/my-project/locations/europe-west1-b/instances/filestore-instance-example"
            protocol  = "NFSV3"
            tier      = "ZONAL"
            file_shares {
              capacity_gb = "1024"
              file_share  = "nfsshare"
            }
          }
        }
      }
    }
    

Creating the cluster can take some time to complete. The completion time depends on the number of compute instances that you request and resource availability in the compute instances' zone. If your requested resources are unavailable, then Cluster Director maintains the creation request until resources become available. When Cluster Director creates your login node, you can connect to your cluster. However, you can run workloads only after Cluster Director creates the compute nodes in your cluster.

###  REST 

To create a custom cluster from scratch, make a `POST` request to the [`clusters.create` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/create).

Your request must include the following HTTP method and request URL:
    
    
    POST https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters?clusterId=CLUSTER_NAME
    

In the request body, include the following fields:

  * **`description`** : Optional. A description for your cluster.

  * **`labels`** : Optional. Key-value pairs of labels to help you organize and filter your clusters and its associated resources. For more information, see [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources).

  * **`networkResources`** : the network configuration for your cluster. You can either create a new network or use an existing one.

  * **`storageResources`** : the storage resources for your cluster. You can either create Filestore instances, Managed Lustre instances, or Cloud Storage buckets, or use existing ones.

**Tip:** If you want to use different Cloud Storage buckets for different projects or jobs, then you can mount the buckets on your cluster nodes for the duration of a Slurm job. This action lets you read or write data to Cloud Storage without permanently adding storage resources to your cluster. For more information, see [Mount Cloud Storage buckets for specific jobs](https://docs.cloud.google.com/cluster-director/docs/workloads/mount-buckets). 
  * **`computeResources`** : the compute resources for your cluster, including the machine types and provisioning models to use for the compute instances in the cluster.

  * **`orchestrator`** : the settings for the Slurm workload scheduler for your cluster, as well as the configurations for the cluster, partitions, and nodesets.




For example, suppose that you want to create a cluster that has one partition with reserved compute instances, one partition with Spot VMs, a new Filestore instance, and a new network. To create the example cluster, include the following in a JSON file named `request-body.json`:
    
    
    {
      "name": "CLUSTER_NAME",
      "networkResources": {
        "NETWORK_NAME": {
          "config": {
            "newNetwork": {
              "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME"
            }
          }
        }
      },
      "storageResources": {
        "STORAGE_RESOURCE_CONFIGURATION": {
          "config": {
            "newFilestore": {
              "filestore": "projects/PROJECT_ID/locations/FILESTORE_INSTANCE_ZONE/instances/FILESTORE_INSTANCE_NAME",
              "fileShares": {
                "capacityGb": "CAPACITY",
                "fileShare": "SHARE_NAME"
              },
              "tier": "TIER",
              "protocol": "PROTOCOL"
            }
          }
        }
      },
      "computeResources": {
        "COMPUTE_RESOURCE_NAME_1": {
          "config": {
            "newReservedInstances": {
              "reservation": "projects/RESERVATION_PROJECT_ID/zones/RESERVATION_ZONE/reservations/RESERVATION_NAME"
            }
          }
        },
        "COMPUTE_RESOURCE_NAME_2": {
          "config": {
            "newSpotInstances": {
              "zone": "SPOT_VMS_ZONE",
              "machineType": "SPOT_MACHINE_TYPE"
            }
          }
        }
      },
      "orchestrator": {
        "slurm": {
          "loginNodes": {
            "count": "LOGIN_NODES_COUNT",
            "zone": "LOGIN_NODE_ZONE",
            "machineType": "LOGIN_NODE_MACHINE_TYPE",
            "startupScriptTimeout": "STARTUP_SCRIPT_TIMEOUT"
          },
          "nodeSets": [
            {
              "id": "NODESET_NAME_1",
              "computeId": "COMPUTE_RESOURCE_NAME_1",
              "storageConfigs": [
                {
                  "id": "STORAGE_RESOURCE_CONFIGURATION",
                  "localMount": "/home"
                }
              ],
              "staticNodeCount": "NODESET_1_STATIC_COUNT",
              "maxDynamicNodeCount": "NODESET_1_MAX_DYNAMIC_COUNT",
              "computeInstance": {
                "bootDisk": {
                  "type": "projects/PROJECT_ID/zones/DISK_ZONE_1/diskTypes/DISK_TYPE_1",
                  "sizeGb": "DISK_SIZE_1"
                },
                "startupScriptTimeout": "STARTUP_SCRIPT_TIMEOUT"
              }
            },
            {
              "id": "NODESET_NAME_2",
              "computeId": "COMPUTE_RESOURCE_NAME_2",
              "storageConfigs": [
                {
                  "id": "STORAGE_RESOURCE_CONFIGURATION",
                  "localMount": "/home"
                }
              ],
              "staticNodeCount": "NODESET_2_STATIC_COUNT",
              "maxDynamicNodeCount": "NODESET_2_MAX_DYNAMIC_COUNT",
              "computeInstance": {
                "bootDisk": {
                  "type": "projects/PROJECT_ID/zones/DISK_ZONE_2/diskTypes/DISK_TYPE_2",
                  "sizeGb": "DISK_SIZE_2"
                },
                "startupScriptTimeout": "STARTUP_SCRIPT_TIMEOUT"
              }
            }
          ],
          "partitions": [
            {
              "id": "PARTITION_NAME_1",
              "nodeSetIds": [
                "NODESET_NAME_1"
              ]
            },
            {
              "id": "PARTITION_NAME_2",
              "nodeSetIds": [
                "NODESET_NAME_2"
              ]
            }
          ],
          "defaultPartition": "PARTITION_NAME_1"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where you want to create your cluster and its associated resources.

  * `REGION`: the region where to create your cluster.

  * `CLUSTER_NAME`: the name of the cluster. The name can contain up to 10 characters, and it can only use numbers or lowercase letters (`a`-`z`).

  * `NETWORK_NAME`: the name of the network that you want to create.

  * `STORAGE_RESOURCE_CONFIGURATION`: the name of the storage resource configuration.

  * `FILESTORE_INSTANCE_ZONE`: the zone where you want to create your Filestore instance.

  * `FILESTORE_INSTANCE_NAME`: the name for your Filestore instance.

  * `CAPACITY`: the size, in GiB, that you want to allocate for the instance. The value must be between 1,024 GiB (`1024`) and 102,400 GiB (`102400`), and it must be in 256 GiB (`256`) increments. For more information about the supported service tiers and capacity for Filestore instances, see [Service tiers](https://docs.cloud.google.com/filestore/docs/service-tiers).

  * `SHARE_NAME`: the name for the NFS file share that is served from the instance.

  * `TIER`: the type of service tier that you want to use for the instance and that Cluster Director supports. Specify one of the following values:

    * For the zonal tier: `ZONAL`

    * For the regional tier: `REGIONAL`

  * `PROTOCOL`: the [system protocol](https://docs.cloud.google.com/filestore/docs/about-supported-protocols) for the instance. Specify one of the following values:

    * For NFSv3: `NFSV3`

    * For NFSv4.1: `NFSV41`

  * `COMPUTE_RESOURCE_NAME_1` and `COMPUTE_RESOURCE_NAME_2`: the name of the two compute resource configurations.

  * `RESERVATION_PROJECT_ID`: the ID of the project where the reservation exists. If you want to use a reservation from a different project, then verify that your project is allowed to consume the reservation. For more information, see [Allow and restrict projects from creating and modifying shared reservations](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).

  * `RESERVATION_NAME`: the name of the reservation that you want to use to create VMs. If you use a reservation of A4X VMs, then you can optionally specify the [block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block) or [sub-block](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#sub-block) to control the placement of your VMs:

    * **Block** : `RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME`

    * **Sub-block** : `RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUB_BLOCK_NAME`

  * `SPOT_VMS_ZONE`: the zone where you want to create your Spot VMs. To review the regions and zones where the machine type that you want to use is available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `SPOT_MACHINE_TYPE`: the machine type to use for the Spot VMs. Specify one of the following machine types:

    * For an A4X machine type: `a4x-highgpu-4g`

    * For an A4 machine type: `a4-highgpu-8g`

    * For an A3 Ultra machine type: `a3-ultragpu-8g`

    * For an A3 Mega machine type: `a3-megagpu-8g`

    * For an N2 machine type, see [N2 machine series](https://docs.cloud.google.com/cluster-director/docs/compute#n2-series).

  * `LOGIN_NODES_COUNT`: the number of compute instances to use for the login nodeset.

  * `LOGIN_NODE_ZONE`: the zone where you want to create the compute instances in the login nodeset.

  * `LOGIN_NODE_MACHINE_TYPE`: the machine type that you want the compute instances in the login nodeset to use. If you use A4X instances in your cluster, then specify a C4A machine type. Otherwise, specify an N2 machine type.

  * `NODESET_NAME_1` and `NODESET_NAME_2`: the name of the two nodesets.

  * `NODESET_1_STATIC_COUNT` and `NODESET_2_STATIC_COUNT`: the minimum number of compute instances that must always be running in each nodeset.

  * `NODESET_1_MAX_DYNAMIC_COUNT` and `NODESET_2_MAX_DYNAMIC_COUNT`: the maximum number of compute instances that Cluster Director can add to each nodeset during increases in traffic.

**Important:** If you create compute instances in the nodeset by using a reservation, especially a shared reservation, then verify that the reservation has enough resources available to create your specified maximum number of compute instances. Other workloads that use the same reservation might fully use it and, thus, Cluster Director might be unable to create more compute instances in your nodeset.
  * `DISK_ZONE_1` and `DISK_ZONE_2`: the zone where you want to create the boot disks for the nodesets.

  * `DISK_TYPE_1` and `DISK_TYPE_2`: the type of boot disks for the nodesets. Based on the machine type in the node, specify one of the following values:

    * For A4X instances: `hyperdisk-balanced`

    * For A4 instances: `hyperdisk-balanced`

    * For A3 Ultra instances: `hyperdisk-balanced`

    * For A3 Mega instances: `pd-balanced`, `pd-ssd`, `hyperdisk-balanced`, `hyperdisk-ml`, `hyperdisk-extreme`, or `hyperdisk-throughput`

    * For N2 instances: `pd-standard`, `pd-balanced`, `pd-ssd`, `pd-extreme`, `hyperdisk-extreme`, or `hyperdisk-throughput`

For an overview of the different types of boot disks that you can use, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

  * `DISK_SIZE_1` and `DISK_SIZE_2`: the size of the boot disks for the two compute nodes in GB. The value must be `50` or higher.

  * `PARTITION_NAME_1` and `PARTITION_NAME_2`: the name of the partitions for your cluster.




To send your request, select one of the following options:

###  curl (Bash) 
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d @request-body.json \
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters?clusterId=CLUSTER_NAME"
    

###  Powershell 
    
    
    $cred = gcloud auth print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
        -Method POST `
        -Headers $headers `
        -ContentType: "application/json; charset=utf-8" `
        -InFile request-body.json `
        -Uri "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters?clusterId=CLUSTER_NAME" | Select-Object -Expand Content
    

###  curl (cmd.exe) 
    
    
    curl -X POST ^
         -H "Authorization: Bearer $(gcloud auth print-access-token)" ^
         -H "Content-Type: application/json; charset=utf-8" ^
         -d @request-body.json ^
         "https://hypercomputecluster.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/clusters?clusterId=CLUSTER_NAME"
    

The response is similar to the following:
    
    
    {
      "name": "projects/example-project/locations/us-central1/operations/operation-1758842430697-63fa86a4c3030-028b6436-2fbda8e1",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.hypercomputecluster.v1.OperationMetadata",
        "createTime": "2025-09-25T23:20:30.707315354Z",
        "target": "projects/example-project/locations/us-central1/clusters/clusterp6a",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

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
