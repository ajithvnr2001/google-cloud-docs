---
url: https://docs.cloud.google.com/compute/docs/instances/use-aci-images/
title: Create an instance with Advanced Compute Images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:25.555300+00:00
---

# Create an instance with Advanced Compute Images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/use-aci-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an instance with Advanced Compute Images Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can create an instance that uses Advanced Compute Images to provide an optimized environment for your artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) workloads. You can use the following interfaces:

  * [ **Google Cloud CLI** ](https://docs.cloud.google.com/compute/docs/gcloud-compute)
  * **Google Cloud console**
  * [**SchedMD's Slurm workload manager**](https://cloud.google.com/blog/topics/hpc/introducing-the-latest-slurm-on-gcp-scripts)



To learn about Advanced Compute Images, see [Overview of Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images). 

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).




### Required roles

To get the permissions that you need to create instances, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create instances:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Quickstart

This tutorial describes the steps to create an [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) or [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) instance that uses Advanced Compute Images to configure and customize the guest OS.

### Prerequisites

Before creating an instance, complete the following tasks for creating A3 Ultra and A4 instances:

  1. [Obtain resource capacity for A3 Ultra or A4 instances](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-overview).
  2. [Create VPC networks](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#setup-network).
  3. Optional: [Create a compact placement policy](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#placement-policy)



### Create a compute instance with Advanced Compute Images

After you have completed the prerequisite tasks, you can use either of the following methods to create the instance.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

If prompted, select your project and click **Continue**. The **Create an instance** page appears and displays the **Machine configuration** pane.

  2. In the **Machine configuration** pane, do the following:

     1. In the **Name** field, specify a name for your compute instance. For more information, see [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
     2. Select a **Region** and **Zone** for the instance. If you have reserved the compute resources, the region and zone you select must match the region and zone of your reservation.

     3. Click the **GPUs** tab, and then complete the following steps:

        1. In the **GPU type** list, select your GPU type. 
           * For A4 instances, select **NVIDIA B200**.
           * For A3 Ultra instances, select **NVIDIA H200 141GB**.
        2. In the **Number of GPUs** list, select **8**.
        3. Optional: Select a different machine type.
  3. In the navigation menu, click **OS and storage**. In the **OS and storage** pane that appears, complete the following steps: 

     1. Click **Change**. The **Boot disk** pane appears and displays the **Public images** tab.
     2. In the **Operating system** list, select **Advanced Compute Images**.
     3. In the **Version** list, select the OS version.
     4. Optional: In the **Boot disk type** list, select the type of the boot disk.
     5. Optional: Specify additional properties for the boot disk, such as the disk size.
     6. Optional: For advanced configuration options, expand the expand_more **Show advanced configurations** section.
     7. To confirm your boot disk options and return to the **Operating system and storage** pane, click **Select**.
**Note:** Unless you explicitly choose a different boot disk, if the name you specified for the instance matches the name of an existing disk, then the existing disk automatically attaches to the new instance as the boot disk.
  4. In the navigation menu, click **Networking**. The **Networking** pane appears.

  5. Optional: To configure access to your instance from outside Google Cloud, complete the following steps:

     1. Go to the **Firewall** section.
     2. To permit HTTP or HTTPS traffic to the compute instance, select **Allow HTTP traffic** or **Allow HTTPS traffic**.

The Compute Engine adds a network tag to your compute instance and creates the corresponding ingress firewall rule that allows all incoming traffic on `tcp:80` (HTTP) or `tcp:443` (HTTPS). The network tag associates the firewall rule with the instance. For more information, see [Firewall rules overview](https://docs.cloud.google.com/firewall/docs/firewalls) in the Cloud Next Generation Firewall documentation.

  6. To create a multi-NIC instance, complete the following steps in the **Networking** pane. For a single-NIC instance, skip these steps.

     1. In the **Network interfaces** section, complete the following steps:
     2. Delete the default network interface. To delete the interface, click delete **Delete**.
     3. Click **Add a network interface**. Use this option to add network interfaces that attach to the VPC networks that you created in the previous section. When you add the network interfaces, remember the following:

        * For a network interface that is used for host to host communication, select a regular VPC network and subnet from the **Network** and **Subnetwork** lists, and set the **Network interface card** list to **gVNIC**.

        * For a network interface that is used for GPU to GPU communication, select the RoCE VPC network and subnet from the **Network** and **Subnetwork** lists, and set the **Network interface card** list to **MRDMA** for these network interfaces.

  7. In the navigation menu, click **Advanced**. Then, complete the following steps for the [provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#provisioning-models) that you want to use.

###  Flex-start 

     1. In the **Provisioning model** section, in the **VM provisioning model** list, select **Flex-start**.
     2. In the **Enter number of hours** field, enter the maximum amount of time that you want the compute instance to run. The value must be between `0.01` (0.01 hours, or 36 seconds) or `168` (168 hours, or seven days).

     3. Select **Set a wait time for VM creation**.

Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

        * **Workloads with strict zonal requirements** : if your workload requires you to create the VM in a specific zone, then specify a duration between **90 seconds** and **2 hours**. Longer durations give you higher chances of obtaining resources. 
        * **Workloads without strict zonal requirements** : if the VM can run in any zone within the region, then specify a duration of **0 seconds** or clear the **Set a wait time for VM creation** checkbox. This action specifies that Compute Engine only allocates resources if they are immediately available. If the VM creation request fails because resources are unavailable, then retry the request in a different zone. 
     4. In the **On VM termination** field, select whether to stop or delete the compute instance at the end of its run duration:

        * To delete the instance, select **Delete**.
        * To stop the instance, select **Stop**.

###  Reservation-bound 

     1. Click **Choose a reservation**. This action opens a pane with a list of available reservations within your selected zone. From the reservation list, complete the following steps:

        1. Select the reservation that you want to use for the compute instance. You can also select a specific block within the reservation.
        2. Click **Choose**.

###  Spot 

     1. In the **Provisioning model** section, select **Spot** from the **VM provisioning model** list.
     2. Optional: To select the [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) that happens when Compute Engine preempts the Spot VM, complete the following steps:

        1. Expand the **VM provisioning model advanced settings** section.
        2. In the **On VM termination** list, select one of the following options:
        3. To stop the Spot VM during preemption, select **Stop** (default).
        4. To delete the Spot VM during preemption, select **Delete**.

  8. To create and start the instance, click **Create**.




###  gcloud 

To create the VM, use the [ `gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-0,subnet=GVNIC_NAME_PREFIX-sub-0 \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-1,subnet=GVNIC_NAME_PREFIX-sub-1,no-address 
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-0,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-1,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-2,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-3,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-4,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-5,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-6,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-7,no-address \
        --reservation-affinity=specific \
        --reservation=RESERVATION \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
       * To create the instance on any block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, to create multiple instances in the same block, apply the same compact placement policy that specifies a block collocation (`maxDistance=2`) when creating each instance. Compute Engine then applies the policy to the reservation and creates instances on the same block.

       * To create the instance on a specific block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the VM at the end of the reservation period. 

  2. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Run the command.



### Flex-start

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-0,subnet=GVNIC_NAME_PREFIX-sub-0 \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-1,subnet=GVNIC_NAME_PREFIX-sub-1,no-address 
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-0,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-1,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-2,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-3,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-4,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-5,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-6,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-7,no-address \
        --provisioning-model=FLEX_START \
        --request-valid-for-duration=REQUEST_VALID_FOR_DURATION \
        --max-run-duration=MAX_RUN_DURATION \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `REQUEST_VALID_FOR_DURATION`: how long the request to create the VM remains valid. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1h2m3s` for one hour, two minutes, and three seconds.

Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

       * **Workloads with strict zonal requirements** : if your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90s`) and two hours (`2h`). Longer durations give you higher chances of obtaining resources. 
       * **Workloads without strict zonal requirements** : if the VM can run in any zone within the region, then specify a duration of zero seconds (`0s`). This action specifies that Compute Engine only allocates resources if they are immediately available. If the VM creation request fails because resources are unavailable, then retry the request in a different zone. 
     * `MAX_RUN_DURATION`: how long you want the requested VMs to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. The value must be between 10 minutes and seven days.

     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the VM at the end of its run duration.

  2. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Run the command.



### Spot

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-0,subnet=GVNIC_NAME_PREFIX-sub-0 \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-1,subnet=GVNIC_NAME_PREFIX-sub-1,no-address 
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-0,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-1,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-2,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-3,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-4,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-5,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-6,no-address \
        --network-interface=nic-type=MRDMA,network=RDMA_NAME_PREFIX-mrdma,subnet=RDMA_NAME_PREFIX-mrdma-sub-7,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --no-restart-on-failure
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Run the command.



After some time, the compute instance creation completes. To verify the instance configuration and to see its status, run the following command:
    
    
    gcloud compute instances describe INSTANCE_NAME
    

### Configure Spot VMs

If you created a Spot VM, then complete the following steps:

  * To prepare your Spot VM for a potential preemption, see [Manage preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#manage-preemption).

  * Optional: Learn about [best practices for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#best-practices).




### Access the compute instance

After you create the compute instance, the instance starts automatically. To access the instance, do one of the following:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the name of your compute instance.

  3. In the **Remote Access** section, click the first drop-down list and choose how you want to access the instance.




Compute Engine propagates your SSH keys and creates your user. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

###  gcloud 

To access the instance using SSH, use the [`gcloud compute ssh` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh):
    
    
    gcloud compute ssh INSTANCE_NAME --zone ZONE
    

Compute Engine propagates your SSH keys and creates your user. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

### Clean up

To avoid incurring charges to your Google Cloud account for the resources used in these quickstarts, delete any compute instances and all attached resources that you created.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the instances that you want to delete.

  3. Click delete **Delete**.

  4. In the dialog, do the following:

     1. Optional: To delete the instances without gracefully shut them down, or end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.

     2. To confirm, click **Delete**.

  5. To delete the disks used by the deleted instances, go to the **Disks** page, then perform the following steps:

[Go to Disks](https://console.cloud.google.com/compute/disks)

     1. Select the disks that you want to delete. The disks you select can't have a value in the **In use by** column.

     2. Click delete **Delete**.

     3. To confirm, click **Delete**.




###  gcloud 

To delete one or more instances in the same zone, use the [`gcloud compute instances delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete). To force the deletion of the disks attached to one or more instances, include the `--delete-disks` flag:
    
    
    gcloud compute instances delete INSTANCE_NAMES \
            --delete-disks=DELETE_DISK_TYPE \
            --zone=ZONE
    

Replace the following:

  * `INSTANCE_NAMES`: a list of instance names separated by spaces—for example, `instance-01 instance-02 instance-03`.

  * `ZONE`: the zone where the instances are located.

  * `DELETE_DISK_TYPE`: specify one of the following values:

    * To delete attached boot and non-boot persistent storage: `all`
    * To delete only attached boot persistent storage: `boot`
    * To delete only non-boot persistent storage: `data`



## Create a custom image based on Advanced Compute Images

You can create a customized image that is based on an Advanced Compute Images image. You can then use the custom image when creating new compute instances for your workloads and applications.

To create a custom image, complete the following tasks:

  1. Configure a storage location for the image. To create, modify, and delete OS images stored in Cloud Storage, you must have been granted the role `roles/compute.storageAdmin`.

  2. Create a compute instance with Advanced Compute Images.

  3. Customize the guest OS as needed for your compute instance.

  4. Stop the compute instance to prevent any writes to the disks. If you can't stop the instance, then complete the steps in [Minimize writing data to the persistent disk](https://docs.cloud.google.com/compute/docs/images/create-custom#minimize_writing_data_to_the_persistent_disk).

  5. [Disable the auto-delete option for the boot disk](https://docs.cloud.google.com/compute/docs/images/create-custom#disable_the_auto-delete_option_for_the_disk).

  6. Create a custom image using the boot disk of your compute instance as the source disk. You can do so using the [Google Cloud console](https://console.cloud.google.com/) or the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).

###  Console 

     1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

     2. Click **Create image**.

     3. Specify a **Name** for your image.

     4. Under **Source disk** , select the name of the boot disk for your compute instance that uses Advanced Compute Images.

If the compute instance isn't stopped, then select **Keep instance running** to confirm that you want to create the image while the instance is running. You should have previously completed the steps to minimize writes to the boot disk.

     5. In the **Based on source disk location (default)** drop-down list, specify the location to store the custom image. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store the custom image in the `us-central1`region.

If you don't make a selection, Compute Engine stores the image in the multi-region closest to the source location for the custom image.

     6. Optional: Specify other properties for your image:

        * **Family** : the [image family](https://docs.cloud.google.com/compute/docs/images#image_families) this new image belongs to.
        * **Description** : a description for your custom image.
        * **Label** : a [label](https://docs.cloud.google.com/compute/docs/labeling-resources) to group together resources.
     7. Specify the encryption key. You can choose between a Google-owned and Google-managed encryption key or a [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms/docs) key. If no encryption key is specified, then images are encrypted using a Google-owned and Google-managed encryption key.

     8. Click **Create** to create the image.

###  gcloud 

Use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) to create a custom image.

The `--force` flag is an optional flag that lets you create the image from a running instance. By default, you cannot create images from running instances. Specify this flag only if you are sure that you want to create the image while the instance is running.
    
    gcloud compute images create IMAGE_NAME \
        --source-disk=SOURCE_DISK \
        --source-disk-zone=ZONE \
        [--family=IMAGE_FAMILY] \
        [--storage-location=LOCATION] \
        [--force]
    

Replace the following:

     * `IMAGE_NAME`: a name for the new image
     * `SOURCE_DISK`: the disk from which you want to create the image
     * `ZONE`: the zone where the disk is located
     * `IMAGE_FAMILY`: Optional: a flag that specifies which [image family](https://docs.cloud.google.com/compute/docs/images#image_families) this image belongs to
     * `LOCATION`: Optional: a flag that lets you designate the region or multi-region where your image is stored. For example, specify `us` to store the image in the `us` multi-region, or `us-central1` to store it in the `us-central1` region. If you don't make a selection, Compute Engine stores the image in the multi-region closest to your image's source location.




For more information about creating custom images, see [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom).

### Share the image

After creating a custom image, you can [share it across projects](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images#share-images-within-organization). If you allow users from another project to use your custom images, then they can [access these images by specifying the image project](https://docs.cloud.google.com/compute/docs/images/managing-access-custom-images#accessing_images) in their request.

## Use Advanced Compute Images with instance templates

You can create an instance template that specifies an Advanced Compute Images image and then use the template to do the following:

  * Create [individual compute instances](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).

  * Create compute instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

  * Create [reservations for compute instances](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).




### Limitations for creating instance templates

Note the following limitations when creating an instance template:

  * Shared VPC on interfaces other than `nic0` for instance templates is supported in gcloud CLI and REST, but not in Google Cloud console.
  * You can't update an existing instance template or change an instance template after it has been created. If an instance template goes out of date, or you need to make changes to the configuration, create a new instance template.
  * If you want to specify an image family in an instance template, you can't use the Google Cloud console. You can use the Google Cloud CLI or REST instead.
  * If you want to specify regional disks instead of zonal disks in an instance template, you can't use the Google Cloud console. You can use the Google Cloud CLI or REST instead.
  * You can use an instance template to create compute instances with a Hyperdisk Balanced boot disk that is in a [storage pool](https://docs.cloud.google.com/compute/docs/disks/use-storage-pool-capacity#create-template), but only if the storage pool is in the same zone as the instance.
  * You can't use global instance templates to create compute instances with non-boot disks that are in a storage pool.
  * To create a regional instance template, the GPU type that you specify in the template must be available in at least one zone in the specified region.



### Create an instance template

Most of the instance properties that you can specify in a request to create an individual compute instance can also be specified for an instance template, including any instance metadata, startup scripts, persistent disks, and service accounts. Required information for an instance template includes the machine type, boot disk, and network.

You can create a regional or global instance template that uses Advanced Compute Images by using the Google Cloud console or Google Cloud CLI.

To create an instance template, your user account must have been granted all the permissions required to call the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).

The following sections describe how to create an instance template for use with Managed Instance Groups (MIGs), individual compute instances, or reservations. To create an instance template for use with AI Hypercomputer, follow the instructions at [Create an AI-optimized MIG with A4 or A3 Ultra machine type](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra) instead.

#### Create additional resources needed for A3 ultra or A4 instances

Before you create an instance template for instances that use Advanced Compute Images, you must first create the resources that you will specify in the instance template. Complete the tasks listed in Prerequisites to create these resources.

#### Create an instance template that specifies an Advanced Compute Images image

You can create the instance template by using either the Google Cloud console or gcloud CLI commands.

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**.

  3. In the **Name** field, enter a name for the instance template.

  4. Select the **Location** as follows:

     1. To use the instance template across regions, choose **Global** (default).
     2. To reduce cross-region dependency, choose **Regional** and then select the **Region** where you want to create your instance template.
  5. In the **Machine configuration** section, do the following:

     1. Click the **GPUs** tab.
     2. In the **GPU type** list, select the GPU type. For A4 instances, select `NVIDIA B200` or for A3 Ultra instances, select `NVIDIA H200 141GB`.
     3. In the **Number of GPUs** list, select 8.
     4. Optional: Select a different machine type than the default.
  6. In the **Boot disk** section, click **Change** , and then do the following:

     1. In the **Operating system** list, select **Advanced Compute Images**.
     2. In the **Version** list, select the OS version.
     3. Optional: Specify additional properties for the boot disk, such as the disk size.
  7. Click **Create** to create the instance template.




###  gcloud 

To create a regional or global instance template, use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create). For a regional instance template, you must use the `--instance-template-region` flag to set the region of the template.

When creating an instance template for GPU instances, you must set the `--maintenance-policy` flag set to `TERMINATE`.

  * Create a regional instance template using the following command.
        
        gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
          --instance-template-region=REGION \
          --accelerator=count=8,type=GPU_TYPE \
          --machine-type=MACHINE_TYPE \
          --image-project=advanced-compute-images \
          --image-family=IMAGE_FAMILY \
          --maintenance-policy=TERMINATE
        

  * Create a global instance template using the following command:
        
        gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME
          --accelerator=count=8,type=GPU_TYPE \
          --machine-type=MACHINE_TYPE \
          --image-project=advanced-compute-images \
          --image-family=IMAGE_FAMILY \
          --maintenance-policy=TERMINATE
        




Replace the following:

  * INSTANCE_TEMPLATE_NAME: a name for the instance template.
  * REGION: for regional instance templates, this is the region to create the template in.
  * GPU_TYPE: the type of GPU to use with the compute instances. When using Advanced Compute Images, you must specify either `nvidia-b200` for A4 or `nvidia-h200-141gb` for A3 Ultra instances.
  * MACHINE_TYPE: the machine type of the compute instance. To use Advanced Compute Images, you must specify an [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) or [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-machine-type) machine type.
  * IMAGE_FAMILY: specify one of the following: 
    * IMAGE_FAMILY: an image family. This specifies the most recent OS image version in that family. For example, you might specify `aci-gpu-u2204-slurm-2511-cuda-130-nvidia-580-amd64`.
    * IMAGE: a specific version of the OS image; for example, `aci-gpu-u2204-slurm-2511-cuda-130-nvidia-580-amd64-v20260427-1`. To specify a specific version of the OS image instead of an image family, you must use the `--image` flag instead of the `--image-family` flag.



You can add up to 15 secondary non-boot disks. Specify the `--create-disk` flag for each secondary disk you create.

  * To create secondary disks from a public or custom image, specify the `image` and `image-project` properties for each disk in the `--create-disk` flag.
  * To create a blank disk, don't include the `image` or `image-project` properties
  * Optionally, include properties for the disk `size` and `type`.



For a list of all available subcommands and flags, see the [`instance-templates` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates).

## What's next

* Review [Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances). * Learn how to [check the status of an instance](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle) to see when it is ready to use. * Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
