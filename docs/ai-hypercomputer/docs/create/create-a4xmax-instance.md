---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instance/
title: Create an AI-optimized instance with A4X Max \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:23.059022+00:00
---

# Create an AI-optimized instance with A4X Max  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized instance with A4X Max Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes the steps to create standalone Compute Engine instances that use A4X Max accelerator-optimized machine types. To learn how to create a GKE cluster that uses A4X Max instances, see [Create an AI-optimized GKE cluster that uses A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4x-max). To learn about all compute instance and cluster creation options, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

### A4X Max instance type

A Compute Engine instance, _or compute instance_ , is a computing resource hosted on Google's infrastructure that can be either a virtual machine (VM) or a bare metal instance. A4X Max instances are available as _[bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances)_ , which differ from VM instances by providing direct, non-virtualized access to the underlying physical hardware. To learn more about the A4X Max machine type, see [A4X Max series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) and [GPU network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#a4x-family-gpus) in the Compute Engine documentation.

## Limitations

When you create a standalone A4X Max instance, the following limitations apply:

**Caution:** The [ Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X Max machine series.

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) or [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use this machine type.
  * You can only create instances in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * This machine type is only available on the [NVIDIA Grace platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
  * Machine type changes aren't supported for A4X Max. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on this machine type. For a list of supported Linux operating systems, review the [supported operating systems for GPU instances](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).
  * A4X Max instances don't support the following: 
    * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)
  * You can't attach Hyperdisk ML disks created before February 4, 2026 to A4X Max machine types.

Also review the [restrictions for placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions). 

## Before you begin

Before creating A4X Max instances, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). **Note:** When you request A4X Max or A4X capacity, you obtain it in the _all capacity mode_. This mode is the only supported reservation operational mode for A4X Max or A4X machine types. For more information about all capacity mode, see [ Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode). 



Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

### Required roles

To get the permissions that you need to create compute instances, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create compute instances. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create compute instances:

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

## A4X Max fundamentals

An A4X Max cluster is organized into a hierarchy of blocks and sub-blocks to facilitate large-scale, non-blocking network performance. Understanding this topology is key when reserving capacity and deploying workloads.

A4X Max instance
    An A4X Max instance is a single A4X Max machine type that has 4 GPUs attached.
Sub-block
    A sub-block is the fundamental unit of A4X Max capacity. For A4X Max, a sub-block consists of 18 A4X Max instances (72 GPUs); these instances form an NVLink domain and are connected using a [multi-node NVLink](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html) system. You create an A4X Max sub-block by applying a compact placement policy that specifies a `1x72` topology.
Block
    An A4X Max block is composed of 25 sub-blocks (NVLink domains), totalling up to 450 A4X Max instances (1,800 GPUs). The sub-blocks are rail-aligned for efficient scaling. Each sub-block requires a compact placement policy. Therefore, for a single A4X Max block, you can create 25 compact placement policies.

The following table shows the supported topology options for A4X Max instances:

Topology (`gpuTopology`) | Number of GPUs | Number of instances  
---|---|---  
`1x72` | 72 | 18  
  
## Overview

**Tip:** To use an NVLink domain with the `1x72` topology, you can run the single instance creation commands 18 times or use the `instances.bulkInsert` method that is designed to create multiple instances with a single API request. To create A4X Max instances in bulk, see [Create A4X Max instances in bulk](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instances-in-bulk). 

Creating an instance with the A4X Max machine type includes the following steps:

  1. Create VPC networks
  2. Create a compact placement policy
  3. Create an instance
  4. Install GPU drivers



## Create VPC networks

**Tip:** If you are setting up a quick test, you can skip this step and specify a single NIC `--network-interface=nic-type=IDPF` instead. 

To set up the network for A4X Max machine types, create three VPC networks for the following network interfaces:

  * 2 regular VPC networks for the IDPF network interfaces (NICs). The NICs then use these VPC networks for host-to-host communication. 
  * 1 VPC network with the [ RoCE metal network profile ](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles) for the CX-8 NICs when creating multiple A4X Max subblocks. A RoCE VPC network for bare metal instances automatically creates a single subnet named `default-subnet-1-RDMA_NAME_PREFIX-net` for all eight CX-8 NICs. These NICs use RDMA over Converged Ethernet (RoCE), providing the high-bandwidth, low-latency communication that's essential for scaling out to multiple A4X Max subblocks. 

**Important:** For a single A4X Max subblock, you don't need to create a VPC network with the RoCE metal network profile because within a single subblock, direct GPU-to-GPU communication is handled by the multi-node NVLink. 

For more information about NIC arrangement, see [Review network bandwidth and NIC arrangement](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#review-network-nic).

Create the networks either manually by following the instruction guides or automatically by using the provided script.

### Instruction guides

To create the networks, you can use the following instructions:

  * To create the regular VPC networks for the IDPF network interfaces, see [Create and manage Virtual Private Cloud networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 
  * To create the RoCE VPC network for bare metal instances (`roce-metal`), see [Create a Virtual Private Cloud network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma).



For these VPC networks, set the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value. For A4X Max machine types, the recommended MTU is `8896` bytes. To review the recommended MTU settings for other GPU machine types, see [MTU settings for GPU machine types](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mtu-gpu). 

### Script

To create the networks, follow these steps.

For these VPC networks, set the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value. For A4X Max machine types, the recommended MTU is `8896` bytes. To review the recommended MTU settings for other GPU machine types, see [MTU settings for GPU machine types](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mtu-gpu). 

  1. Use the following script to create regular VPC networks for the IDPF NICs. 
         
         #!/bin/bash
         
             # Create regular VPC network for the IDPF NICs
             gcloud compute networks create IDPF_NETWORK_PREFIX-net \
                 --subnet-mode=custom \
                 --mtu=8896 \
                 --enable-ula-internal-ipv6
         
             # Create subnets for the IDPF NICs
             for N in $(seq 0 1); do
               gcloud compute networks subnets create IDPF_NETWORK_PREFIX-$N \
                 --network=IDPF_NETWORK_PREFIX-net \
                 --region=REGION \
                 --stack-type=IPV6_ONLY \
                 --ipv6-access-type=INTERNAL
             done
         
             gcloud compute firewall-rules create IDPF_NETWORK_PREFIX-internal \
               --network=IDPF_NETWORK_PREFIX-net \
                 --action=ALLOW \
                 --rules=tcp:0-65535,udp:0-65535,58 \
                 --source-ranges=IP_RANGE
         
         
         
               

  2. If you require multiple A4X Max subblocks, use the following script to create the RoCE VPC network for bare metal instances (`roce-metal`) and use the automatically created subnet for the eight CX-8 NICs on each A4X Max instance. 

**Important:** If your deployment consists of only a single A4X Max subblock, you can skip this step. 
         
         #!/bin/bash
         
             # List and make sure network profiles exist in the machine type's zone
             gcloud compute network-profiles list --filter "location.name=ZONE"
         
             # Create RoCE VPC network for bare metal instances (roce-metal)
             gcloud compute networks create RDMA_NAME_PREFIX-net \
               --network-profile=ZONE-vpc-roce-metal \
               --subnet-mode custom \
               --mtu=8896
         
             # For RoCE VPC networks for bare metal instances, a single subnet named
             # default-subnet-1-RDMA_NAME_PREFIX-net is automatically provided.
             # For more details, see https://cloud.google.com/vpc/docs/rdma-network-profiles.
         
         
               

Replace the following:

     * `IDPF_NETWORK_PREFIX`: the custom name prefix to use for the regular VPC networks and subnets for the IDPF NICs.
     * `RDMA_NAME_PREFIX`: the custom name prefix to use for the RoCE VPC network for bare metal instances (`roce-metal`) for the CX-8 NICs. 
     * `ZONE`: specify a zone in which the machine type that you want to use is available, such as `us-central1-a`. For information about regions, see [ GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `REGION`: the region where you want to create the subnets. This region must correspond to the zone specified. For example, if your zone is `us-central1-a`, then your region is `us-central1`.
     * `IP_RANGE`: the IP range to use for the [SSH firewall rules](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#use-firewall-policies). 
  3. Optional: To verify that the VPC network resources are created successfully, check the network settings in the Google Cloud console: 
     1. In the Google Cloud console, go to the **VPC networks** page. 

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. Search the list for the networks that you created in the previous step. 
     3. To view the subnets, firewall rules, and other network settings, click the name of the network. 



### Create a compact placement policy

**Important:** To create multiple NVLink domains in a block, create separate compact placement policy for each NVLink domain. If you reuse a compact placement policy, Compute Engine attempts to place the instances in the same subblock, which is already in use.

To create a compact placement policy, select one of the following options: 

### gcloud

To create a compact placement policy, use the [ `gcloud compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement):
    
    
    gcloud compute resource-policies create group-placement POLICY_NAME \
        --collocation=collocated \
        --gpu-topology=1x72 \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of the compact placement policy.
  * `REGION`: the region where you want to create the compact placement policy. Specify the region that contains the zone where you plan to create instances, and verify that the machine type that you want to use is available in that region. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). 



### REST

To create a compact placement policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies). 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
      {
        "name": "POLICY_NAME",
        "groupPlacementPolicy": {
          "collocation": "COLLOCATED",
          "gpuTopology": "1x72"
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_NAME`: the name of the compact placement policy.
  * `REGION`: the region where you want to create the compact placement policy. Specify the region that contains the zone where you plan to create instances, and verify that the machine type that you want to use is available in that region. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). 



## Create an A4X Max instance

Choose the creation option that aligns with your workload architecture:

  * Create an instance in a 72-GPU NVLink domain (NVL72): Best for large-scale distributed training, fine-tuning, and multi-node inference workloads that require high-bandwidth, low-latency GPU communication across up to 18 instances (72 GPUs) over the multi-node NVLink fabric. You must use a compact placement policy.
  * Create a standalone 4-GPU instance (NVL4): Best for single-node workloads, smaller model inference, batch processing, and interactive development that fit within four GPUs and only require intra-node NVLink peering. You must target a specific reservation sub-block to partition that sub-block into standalone instances. You don't need to use a compact placement policy.



### Create an instance in a 72-GPU NVLink domain (1x72 topology)

To obtain a GPU topology of `1x72`, create 18 A4X Max instances. When you create the instances, apply the compact placement policy that specifies the `gpuTopology` field. Applying the policy ensures that Compute Engine creates all 18 A4X Max instances in one sub-block to use an NVLink domain. If a sub-block lacks capacity for an A4X Max instance, then the request to create the instance fails. 

**Important:** When you create an A4X Max instance with a `1x72` topology, Compute Engine allocates an entire 18-instance sub-block (NVLink domain) to the placement policy used in the creation. If you create fewer than 18 instances, the unused instances in that sub-block remain idle and are unavailable for other requests that use a different placement policy. However, it's possible to provision these unused instances by using the same policy. To maximize resource efficiency, we recommend that you create exactly 18 instances. 

To create an A4X Max instance, select one of the following options.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create the A4X Max instance, use the [ `gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

**Important:** The following example uses the networking setup for multiple sub-blocks. If you're creating only a single A4X Max sub-block and you only created the IDPF network in the Create VPC networks step, then remove the eight RDMA subnets indicated by the `MRDMA` NIC type from the example.

A4X Max instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=a4x-maxgpu-4g-metal \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=IDPF,network=IDPF_NETWORK_PREFIX-net,stack-type=IPV6_ONLY,subnet=IDPF_NETWORK_PREFIX-sub-0 \
        --network-interface=nic-type=IDPF,network=IDPF_NETWORK_PREFIX-net,stack-type=IPV6_ONLY,subnet=IDPF_NETWORK_PREFIX-sub-1,no-address \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --reservation-affinity=specific \
        --reservation=RESERVATION \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --restart-on-failure \
        --resource-policies=POLICY_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the A4X Max instance.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `ZONE`: the zone in which the machine type that you want to use is available. You must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `IDPF_NETWORK_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use IDPF NICs.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RESERVATION`: the reservation name, a block, or a subblock within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirements for instance placement, choose one of the following: 
    * To create A4X Max instances on any single block: 
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME
              

    * To create A4X Max instances on a specific block: 
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME
              

    * To create A4X Max instances in a specific subblock: 
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUBBLOCK_NAME
              

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
  * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A4X Max instance at the end of the reservation period. 

  * `POLICY_NAME`: the name of the compact placement policy.



###  REST 

To create the A4X Max instance, make a `POST` request to the [ `instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

**Important:** The following example uses the networking setup for multiple sub-blocks. If you're creating only a single A4X Max sub-block and you only created the IDPF network in the Create VPC networks step, then remove the eight RDMA subnets indicated by the `MRDMA` NIC type from the example.

A4X Max instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/a4x-maxgpu-4g-metal",
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
          "network": "projects/NETWORK_PROJECT_ID/global/networks/IDPF_NETWORK_PREFIX-net",
          "nicType": "IDPF",
          "stackType": "IPV6_ONLY",
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/IDPF_NETWORK_PREFIX-sub-0"
        },
        {
          "network": "projects/NETWORK_PROJECT_ID/global/networks/IDPF_NETWORK_PREFIX-net",
          "nicType": "IDPF",
          "stackType": "IPV6_ONLY",
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/IDPF_NETWORK_PREFIX-sub-1"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
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
      },
      "resourcePolicies": [
        "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project where you want to create the A4X Max instance.
  * `ZONE`: the zone in which the machine type that you want to use is available. You must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `INSTANCE_NAME`: the name of the A4X Max instance.
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `IDPF_NETWORK_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use IDPF NICs.
  * `REGION`: the region of the subnetwork.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RESERVATION`: the reservation name, a block, or a subblock within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirements for instance placement, choose one of the following: 
    * To create A4X Max instances on any single block: 
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME
              

    * To create A4X Max instances on a specific block: 
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME
              

    * To create A4X Max instances in a specific subblock: 
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUBBLOCK_NAME
              

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
  * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A4X Max instance at the end of the reservation period. 

  * `PROJECT_ID`: the project ID of the compact placement policy.
  * `REGION`: the region of the compact placement policy.
  * `POLICY_NAME`: the name of the compact placement policy.



### Create a standalone 4-GPU instance (NVL4)

NVL4 partitions the NVLink domain to create independent instances on the NVLink fabric. To create standalone NVL4 instances, you must specify which sub-block within the reservation to partition. Because each A4X Max instance operates independently, you don't need to use compact placement policies. Intra-node four GPU NVLink communication is fully supported for intra-instance workloads.

Before you create standalone NVL4 instances, note the following:

  * **Capacity and sub-block targeting** : To create standalone NVL4 instances, you must target a specific reservation sub-block. The atomic unit of reserved capacity is an entire sub-block, which is an NVLink domain of 18 instances or 72 GPUs. You can't reserve single NVL4 instances individually. When deploying NVL4 instances, you partition a reserved sub-block into up to 18 independent nodes. You can also share a sub-block reservation from a host project with consumer projects.
  * **Static partitioning and configuration changes** : Sub-block deployments are static. To change the configuration of a sub-block, such as switching from a `1x72` multi-node NVLink domain to standalone NVL4 instances, or vice versa, you must delete all existing instances in that sub-block before re-creating them with the new configuration.
  * **Mixed deployments in a sub-block** : You can allocate instances within the same sub-block reservation across both standalone Compute Engine instances and GKE node pools, such as provisioning 12 standalone Compute Engine instances for development and 6 instances in a GKE node pool.
  * **NCCL and NVLS configuration** : If you run distributed workloads by using NCCL across NVL4 instances, disable NVLink SHARP by setting the environment variable `NCCL_NVLS_ENABLE=0`. Google Cloud doesn't configure CUDA multicast groups for multi-node communication on partitioned domains.



If you reserved an entire sub-block, which consists of 18 instances or 72 GPUs, and want to deploy all 18 standalone A4X Max instances, run the creation command 18 times, and ensure that each command targets the same reservation sub-block.

To create a standalone A4X Max instance with four GPUs, select one of the following options:

### gcloud

To create the A4X Max instance, use the [ `gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

**Important:** The following example uses the networking setup for multiple sub-blocks. If you're creating only a single A4X Max sub-block and you only created the IDPF network in the Create VPC networks step, then remove the eight RDMA subnets indicated by the `MRDMA` NIC type from the example.

A4X Max instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=a4x-maxgpu-4g-metal \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=IDPF,network=IDPF_NETWORK_PREFIX-net,stack-type=IPV6_ONLY,subnet=IDPF_NETWORK_PREFIX-sub-0 \
        --network-interface=nic-type=IDPF,network=IDPF_NETWORK_PREFIX-net,stack-type=IPV6_ONLY,subnet=IDPF_NETWORK_PREFIX-sub-1,no-address \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=MRDMA \
        --reservation-affinity=specific \
        --reservation=RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUB_BLOCK_NAME \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Replace the following:

  * `INSTANCE_NAME`: the name of the A4X Max instance.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `ZONE`: the zone in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `IDPF_NETWORK_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use IDPF NICs.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RESERVATION_NAME`: the name of your reservation.
  * `BLOCK_NAME`: the name of a specific block within the reservation.
  * `SUB_BLOCK_NAME`: the name of the specific sub-block within the block.
  * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A4X Max instance at the end of the reservation period. 




### REST

To create the A4X Max instance, make a `POST` request to the [ `instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

**Important:** The following example uses the networking setup for multiple sub-blocks. If you're creating only a single A4X Max sub-block and you only created the IDPF network in the Create VPC networks step, then remove the eight RDMA subnets indicated by the `MRDMA` NIC type from the example.

A4X Max instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/a4x-maxgpu-4g-metal",
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
          "network": "projects/NETWORK_PROJECT_ID/global/networks/IDPF_NETWORK_PREFIX-net",
          "nicType": "IDPF",
          "stackType": "IPV6_ONLY",
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/IDPF_NETWORK_PREFIX-sub-0"
        },
        {
          "network": "projects/NETWORK_PROJECT_ID/global/networks/IDPF_NETWORK_PREFIX-net",
          "nicType": "IDPF",
          "stackType": "IPV6_ONLY",
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/IDPF_NETWORK_PREFIX-sub-1"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        },
        {
          "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/default-subnet-1-RDMA_NAME_PREFIX-net",
          "nicType": "MRDMA",
          "stackType": "IPV6_ONLY"
        }
      ],
      "reservationAffinity": {
        "consumeReservationType": "SPECIFIC_RESERVATION",
        "key": "compute.googleapis.com/reservation-name",
        "values": [
          "RESERVATION_NAME/reservationBlocks/BLOCK_NAME/reservationSubBlocks/SUB_BLOCK_NAME"
        ]
      },
      "scheduling": {
        "provisioningModel": "RESERVATION_BOUND",
        "instanceTerminationAction": "TERMINATION_ACTION",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": true
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project where you want to create the A4X Max instance.
  * `ZONE`: the zone in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `INSTANCE_NAME`: the name of the A4X Max instance.
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `IDPF_NETWORK_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use IDPF NICs.
  * `REGION`: the region of the subnetwork.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RESERVATION_NAME`: the name of your reservation.
  * `BLOCK_NAME`: the name of a specific block within the reservation.
  * `SUB_BLOCK_NAME`: the name of the specific sub-block within the block.
  * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A4X Max instance at the end of the reservation period. 




### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. If you didn't specify an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation. 

## What's next

  * [View VMs topology](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/vms-topology)
  * [Run workloads overview](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
