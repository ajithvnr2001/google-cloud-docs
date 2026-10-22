---
url: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4/
title: Create an A3 Ultra or A4 instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:31.041329+00:00
---

# Create an A3 Ultra or A4 instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an A3 Ultra or A4 instance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create A3 Ultra or A4 instances with attached GPUs. To learn more about creating Compute Engine instances with attached GPUs, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).

The A4 and A3 Ultra machine series are designed to enable you to run large-scale AI/ML clusters with features such as targeted workload placement, advanced cluster maintenance controls, and topology-aware scheduling. For more information, see [Cluster management overview](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities).

## Before you begin

  * To review limitations and additional prerequisite steps for creating instances with attached GPUs, such as how to select an OS image or check GPU quota, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




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

## Determine how to create A3 Ultra or A4 instances

To determine the options that you want to use to create A3 Ultra or A4 instances, complete the following steps:

  1. **Choose a consumption option** : To learn how to choose a consumption option for an A3 Ultra or A4 instance, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) in the AI Hypercomputer documentation.

**Note:** A3 Ultra and A4 instances don't support on-demand instances, which is the default option when creating Compute Engine instances.
  2. **Obtain capacity** : To learn how to obtain capacity for A3 Ultra or A4 instances for the consumption option that you chose, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity) in the AI Hypercomputer documentation.

  3. **Select creation instructions** : To learn about all the options that you can use to create A3 Ultra or A4 instances, such as managed instance groups (MIGs) or clusters, see [Overview of creating VMs and clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation.

If you want to use the cluster management features of A3 Ultra or A4, or if you don't want to create standalone instances, then select a creation option in the AI Hypercomputer documentation instead.




## Create an A3 Ultra or A4 instance

To create an A3 Ultra or A4 instance, complete the following steps:

  1. Create VPC networks

  2. Optional: Create a compact placement policy

  3. Create the instance

  4. Prepare the instance for use




### Create VPC networks

**Tip:** If you are setting up a quick test, you can skip this step and specify a single NIC `--network-interface=nic-type=GVNIC` instead. 

To set up the network for A4 or A3 Ultra machine types, create three VPC networks for the following network interfaces:

  * 2 regular VPC networks for the [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic) network interfaces (NICs). The NICs then use these VPC networks for host-to-host communication. 
  * 1 VPC network with the [ RoCE network profile ](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles) for the CX-7 NICs. The RoCE VPC network for VM instances must have 8 subnets, one subnet for each CX-7 NIC. These NICs use RDMA over Converged Ethernet (RoCE), providing the high-bandwidth, low-latency communication that's essential for GPU-to-GPU communication. 



For more information about NIC arrangement, see [Review network bandwidth and NIC arrangement](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#review-network-nic).

Create the networks either manually by following the instruction guides or automatically by using the provided script.

### Instruction guides

To create the networks, you can use the following instructions:

  * To create the regular VPC networks for the gVNIC network interfaces, see [Create and manage Virtual Private Cloud networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 
  * To create the RoCE VPC network for VM instances (`roce`), see [Create a Virtual Private Cloud network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma).



For these VPC networks, set the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value. For A4 or A3 Ultra machine types, the recommended MTU is `8896` bytes. To review the recommended MTU settings for other GPU machine types, see [MTU settings for GPU machine types](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mtu-gpu). 

### Script

To create the networks, follow these steps.

For these VPC networks, set the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value. For A4 or A3 Ultra machine types, the recommended MTU is `8896` bytes. To review the recommended MTU settings for other GPU machine types, see [MTU settings for GPU machine types](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mtu-gpu). 

  1. Use the following script to create VPC networks for the gVNICs and CX-7 NICs.
         
         #!/bin/bash
         
             # Create regular VPC networks and subnets for the gVNICs
             for N in $(seq 0 1); do
               gcloud compute networks create GVNIC_NAME_PREFIX-net-$N \
                 --subnet-mode=custom \
                 --mtu=8896
         
               gcloud compute networks subnets create GVNIC_NAME_PREFIX-sub-$N \
                 --network=GVNIC_NAME_PREFIX-net-$N \
                 --region=REGION \
                 --range=10.$N.0.0/16
         
               gcloud compute firewall-rules create GVNIC_NAME_PREFIX-internal-$N \
                 --network=GVNIC_NAME_PREFIX-net-$N \
                 --action=ALLOW \
                 --rules=tcp:0-65535,udp:0-65535,icmp \
                 --source-ranges=10.0.0.0/8
             done
         
             # Create SSH firewall rules
             gcloud compute firewall-rules create GVNIC_NAME_PREFIX-ssh \
               --network=GVNIC_NAME_PREFIX-net-0 \
               --action=ALLOW \
               --rules=tcp:22 \
               --source-ranges=IP_RANGE
         
             # Assumes that an external IP is only created for vNIC 0
             gcloud compute firewall-rules create GVNIC_NAME_PREFIX-allow-ping-net-0 \
               --network=GVNIC_NAME_PREFIX-net-0 \
               --action=ALLOW \
               --rules=icmp \
               --source-ranges=IP_RANGE
         
         
             #!/bin/bash
         
             # List and make sure network profiles exist in the machine type's zone
             gcloud compute network-profiles list --filter "location.name=ZONE"
         
             # Create network for RDMA NICs
             gcloud compute networks create RDMA_NAME_PREFIX-mrdma \
               --network-profile=ZONE-vpc-roce \
               --subnet-mode custom \
               --mtu=8896
         
             # Create subnets
             for N in $(seq 0 7); do
               gcloud compute networks subnets create RDMA_NAME_PREFIX-mrdma-sub-$N \
                 --network=RDMA_NAME_PREFIX-mrdma \
                 --region=REGION \
                 --range=10.$((N+2)).0.0/16 # offset to avoid overlap with gVNICs
             done
         
               

Replace the following:

     * `GVNIC_NAME_PREFIX`: the custom name prefix to use for the regular VPC networks and subnets for the gVNICs.
     * `RDMA_NAME_PREFIX`: the custom name prefix to use for the RoCE VPC network for VM instances (`roce`) and subnets for the CX-7 NICs. 
     * `ZONE`: specify a zone in which the machine type that you want to use is available, such as `us-central1-a`. For information about regions, see [ GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `REGION`: the region where you want to create the subnets. This region must correspond to the zone specified. For example, if your zone is `us-central1-a`, then your region is `us-central1`.
     * `IP_RANGE`: the IP range to use for the [SSH firewall rules](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#use-firewall-policies). 
  2. Optional: To verify that the VPC network resources are created successfully, check the network settings in the Google Cloud console: 
     1. In the Google Cloud console, go to the **VPC networks** page. 

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. Search the list for the networks that you created in the previous step. 
     3. To view the subnets, firewall rules, and other network settings, click the name of the network. 



### Create a compact placement policy

To place your A4 or A3 Ultra instances in single or adjacent [_blocks_](https://docs.cloud.google.com/ai-hypercomputer/docs/terminology#block), you can specify instance placement by creating and applying a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) to your instances. To place your instances on a specific block, skip this step and provide the name of the block when you create instances.

For instructions on how to create a compact placement policy with a maximum distance value of `3` (to place instances in adjacent blocks) or `2` (to place instances in a single block), see [Create a compact placement policy](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-compact-policy).

### Create the instance

To create an instance that specifies a compact placement policy, use the gcloud CLI or REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, complete the following steps:

     1. Specify a **Name** for your instance. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

     2. Select the **Region** and **Zone** where you have reserved capacity.

     3. Click the **GPUs** tab, and then complete the following steps:

        1. In the **GPU type** list, select your GPU type.

           * For A4 instances, select **NVIDIA B200**.

           * For A3 Ultra instances, select **NVIDIA H200 141GB**.

        2. In the **Number of GPUs** list, select **8**.

  3. In the navigation menu, click **OS and storage**. In the **OS and storage** pane that appears, complete the following steps:

     1. Click **Change**. The **Boot disk configuration** pane appears.

     2. On the **Public images** tab, select a recommended image. For a list of recommended images, see [Operating systems](https://docs.cloud.google.com/ai-hypercomputer/docs/software-stack#os-image).

     3. To confirm your boot disk options, click **Select**.

  4. To create a multi-NIC instance, complete the following steps. For a single-NIC instance, skip these steps.

     * In the navigation menu, click **Networking**. In the **Networking** pane that appears, complete the following steps:

       1. In the **Network interfaces** section, complete the following steps:

       2. Delete the default network interface. To delete the interface, click delete **Delete**.

       3. Click **Add a network interface**. Use this option to add network interfaces that attach to the VPC networks that you created in the previous section. When you add the network interfaces, remember the following:

          * For a network interface that is used for host to host communication, select a regular VPC network and subnet from the **Network** and **Subnetwork** lists, and set the **Network interface card** list to **gVNIC**.

          * For a network interface that is used for GPU to GPU communication, select the RoCE VPC network and subnet from the **Network** and **Subnetwork** lists, and set the **Network interface card** list to **MRDMA** for these network interfaces.

  5. In the navigation menu, click **Advanced**. Then, complete the following steps for the [provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#provisioning-models) that you want to use.

###  Flex-start 

     1. In the **Provisioning model** section, in the **VM provisioning model** list, select **Flex-start**.
     2. In the **Enter number of hours** field, enter the maximum amount of time that you want the VM to run. The value must be between `0.01` (0.01 hours, or 36 seconds) or `168` (168 hours, or seven days).

     3. Select **Set a wait time for VM creation**.

Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

        * **Workloads with strict zonal requirements** : if your workload requires you to create the VM in a specific zone, then specify a duration between **90 seconds** and **2 hours**. Longer durations give you higher chances of obtaining resources. 
        * **Workloads without strict zonal requirements** : if the VM can run in any zone within the region, then specify a duration of **0 seconds** or clear the **Set a wait time for VM creation** checkbox. This action specifies that Compute Engine only allocates resources if they are immediately available. If the VM creation request fails because resources are unavailable, then retry the request in a different zone. 
     4. In the **On VM termination** field, select whether to stop or delete the VM at the end of its run duration:

        * To delete the VM, select **Delete**.
        * To stop the VM, select **Stop**.

###  Reservation-bound 

     1. Click **Choose a reservation**. This action opens a pane with a list of available reservations within your selected zone. From the reservation list, complete the following steps:

        1. Select the reservation that you want to use for the VM. You can also select a specific block within the reservation.
        2. Click **Choose**.

###  Spot 

     1. In the **Provisioning model** section, select **Spot** from the **VM provisioning model** list.
     2. Optional: To select the [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) that happens when Compute Engine preempts the VM, complete the following steps:

        1. Expand the **VM provisioning model advanced settings** section.
        2. In the **On VM termination** list, select one of the following options: 
           * To stop the VM during preemption, select **Stop** (default).
           * To delete the VM during preemption, select **Delete**.

  6. To create and start the instance, click **Create**.




###  gcloud 

To create the VM, use the [ `gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A4 or A3 Ultra instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.

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



###  REST 

To create the VM, make a `POST` request to the [ `instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A4 or A3 Ultra instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
      "name": "INSTANCE_NAME",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "diskSizeGb": "DISK_SIZE",
            "diskType": "hyperdisk-balanced",
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
          },
          "mode": "READ_WRITE",
          "type": "PERSISTENT"
        }
      ],
      "serviceAccounts": [
        {
          "email": "default",
          "scopes": [
            "https://www.googleapis.com/auth/cloud-platform"
          ]
        }
      ],
      "networkInterfaces": [
          {
            "accessConfigs": [
              {
                "name": "external-nat",
                "type": "ONE_TO_ONE_NAT"
              }
            ],
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-0",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-0"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-1",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-1"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-0"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-1"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-7"
          }
         ],
      "reservationAffinity": {
        "consumeReservationType": "SPECIFIC_RESERVATION",
        "key": "compute.googleapis.com/reservation-name",
        "values": [
          "RESERVATION"
        ]
      },
      "scheduling": {
        "provisioningModel": "RESERVATION_BOUND",
        "instanceTerminationAction": "TERMINATION_ACTION",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": true
      }
    }
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the VM.
     * `ZONE`: the zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `INSTANCE_NAME`: the name of the VM.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `REGION`: the region of the subnetwork.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
       * To create the instance on any block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, to create multiple instances in the same block, apply the same compact placement policy that specifies a block collocation (`maxDistance=2`) when creating each instance. Compute Engine then applies the policy to the reservation and creates instances on the same block.

       * To create the instance on a specific block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the VM at the end of the reservation period. 

  2. Optional: If you chose to use a compact placement policy, then add the following field to the request body:
         
         "resourcePolicies": [
             "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
           ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Submit the request.



### Flex-start

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
      "name": "INSTANCE_NAME",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "diskSizeGb": "DISK_SIZE",
            "diskType": "hyperdisk-balanced",
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
          },
          "mode": "READ_WRITE",
          "type": "PERSISTENT"
        }
      ],
      "serviceAccounts": [
        {
          "email": "default",
          "scopes": [
            "https://www.googleapis.com/auth/cloud-platform"
          ]
        }
      ],
      "networkInterfaces": [
          {
            "accessConfigs": [
              {
                "name": "external-nat",
                "type": "ONE_TO_ONE_NAT"
              }
            ],
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-0",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-0"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-1",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-1"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-0"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-1"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-7"
          }
         ],
      "scheduling": {
        "provisioningModel": "FLEX_START",
        "requestValidForDuration": {
          "seconds": REQUEST_VALID_FOR_DURATION
        },
        "maxRunDuration": {
          "seconds": MAX_RUN_DURATION
        },
        "instanceTerminationAction": "TERMINATION_ACTION",
        "onHostMaintenance": "TERMINATE",
      }
    }
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the VM.
     * `ZONE`: the zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `INSTANCE_NAME`: the name of the VM.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `REGION`: the region of the subnetwork.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `REQUEST_VALID_FOR_DURATION`: the duration, in seconds, that the request to create the VM remains valid.

Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

       * **Workloads with strict zonal requirements** : if your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90`) and two hours (`7200`). Longer durations give you higher chances of obtaining resources. 
       * **Workloads without strict zonal requirements** : if the VM can run in any zone within the region, then specify a duration of zero seconds (`0`). This action specifies that Compute Engine only allocates resources if they are immediately available. If the VM creation request fails because resources are unavailable, then retry the request in a different zone. 
     * `MAX_RUN_DURATION`: the duration you want the requested VMs to run. You must format the value as the number of seconds. For example, specify `86400` for 86,400 seconds (24 hours). The value must be between 10 minutes and seven days.

     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the VM at the end of its run duration.

  2. Optional: If you chose to use a compact placement policy, then add the following field to the request body:
         
         "resourcePolicies": [
             "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
           ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Submit the request.



### Spot

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
      "name": "INSTANCE_NAME",
      "disks": [
        {
          "boot": true,
          "initializeParams": {
            "diskSizeGb": "DISK_SIZE",
            "diskType": "hyperdisk-balanced",
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
          },
          "mode": "READ_WRITE",
          "type": "PERSISTENT"
        }
      ],
      "serviceAccounts": [
        {
          "email": "default",
          "scopes": [
            "https://www.googleapis.com/auth/cloud-platform"
          ]
        }
      ],
      "networkInterfaces": [
          {
            "accessConfigs": [
              {
                "name": "external-nat",
                "type": "ONE_TO_ONE_NAT"
              }
            ],
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-0",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-0"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-1",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-1"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-0"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-1"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/RDMA_NAME_PREFIX-mrdma",
            "nicType": "MRDMA",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/RDMA_NAME_PREFIX-mrdma-sub-7"
          }
         ],
      "scheduling":
      {
        "provisioningModel": "SPOT",
        "instanceTerminationAction": "TERMINATION_ACTION",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": false
      }
    }
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the VM.
     * `ZONE`: the zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `INSTANCE_NAME`: the name of the VM.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `REGION`: the region of the subnetwork.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, then add the following field to the request body:
         
         "resourcePolicies": [
             "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
           ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Submit the request.



### Prepare the instance for use

To prepare an instance that has GPUs attached for use, complete the following steps:

  1. A4 and A3 Ultra instances require GPU drivers. If the OS image that your instance uses doesn't include GPU drivers, then [install them](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).

  2. If you created a Spot VM in the previous section, then complete the following steps:

     * To prepare your Spot VM for a potential preemption, see [Manage preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#manage-preemption).

     * Optional: Learn about [best practices for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#best-practices).




## What's next

  * To monitor GPU performance, see [Monitor GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).

  * To troubleshoot GPU instances, see [Troubleshoot GPU VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus).

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
