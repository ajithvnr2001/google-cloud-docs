---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-mig/
title: Create an AI-optimized A4X Max MIG \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:58.057326+00:00
---

# Create an AI-optimized A4X Max MIG  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized A4X Max MIG Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes how to create a managed instance group (MIG) that uses A4X Max accelerator-optimized machine types. To learn about compute instance and cluster creation options, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) page.

### A4X Max instance type

A Compute Engine instance, _or compute instance_ , is a computing resource hosted on Google's infrastructure that can be either a virtual machine (VM) or a bare metal instance. A4X Max instances are available as _[bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances)_ , which differ from VM instances by providing direct, non-virtualized access to the underlying physical hardware. To learn more about the A4X Max machine type, see [A4X Max series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) in the Compute Engine documentation.

Create a MIG if you want to manage multiple A4X Max instances as a single entity. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) in the Compute Engine documentation.

## Limitations

When you use A4X Max machine types to create a MIG, the following limitations apply:

  * If you create a regional MIG that uses RDMA networking, then the MIG can only create A4X Max instances in the zone where you [configured the network profile for RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-mig#setup-network). 

  * You can't configure [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) in the MIG.



  * Review the [limitations for workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#limitations).


  * You must use the [reservation-bound](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-bound) provisioning model. Other provisioning models aren't supported.

  * You can't use a resize request to add A4X Max instances to the MIG. You must set the target size of the MIG to add the instances.




## Before you begin

Before creating a MIG, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). **Note:** When you request A4X Max or A4X capacity, you obtain it in the _all capacity mode_. This mode is the only supported reservation operational mode for A4X Max or A4X machine types. For more information about all capacity mode, see [ Reservation operational mode](https://docs.cloud.google.com/ai-hypercomputer/docs/create/review-configurations#reservation-operational-mode). 



### Required roles

To get the permissions that you need to create a MIG, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a MIG. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a MIG:

  * To create a MIG: `compute.instanceGroupManagers.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## A4X Max fundamentals

An A4X Max cluster is organized into a hierarchy of blocks and sub-blocks to facilitate large-scale, non-blocking network performance. Understanding this topology is key when reserving capacity and deploying workloads.

A4X Max instance
    An A4X Max instance is a single A4X Max machine type that has 4 GPUs attached.
Sub-block
    A sub-block is the fundamental unit of A4X Max capacity. For A4X Max, a sub-block consists of 18 A4X Max instances (72 GPUs); these instances form an NVLink domain and are connected using a [multi-node NVLink](https://docs.nvidia.com/multi-node-nvlink-systems/mnnvl-user-guide/overview.html) system. You create an A4X Max sub-block by applying a workload policy that specifies a `1x72` topology.
Block
    An A4X Max block is composed of 25 sub-blocks (NVLink domains), totalling up to 450 A4X Max instances (1,800 GPUs). The sub-blocks are rail-aligned for efficient scaling. Each sub-block requires a MIG. Therefore, for a single A4X Max block, you can create 25 MIGs.

The following table shows the supported topology options for A4X Max instances:

Topology (`acceleratorTopology`) | Number of GPUs | Number of instances  
---|---|---  
`1x72` | 72 | 18  
  
## Overview

Creating a MIG with the A4X Max machine type includes the following steps:

  1. Create VPC networks
  2. Create a workload policy
  3. Create an instance template
  4. Create a MIG
  5. Install GPU drivers



### Create VPC networks

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



###  Create a workload policy

If you want to create a single A4X Max instance in the MIG for testing, then skip this step. Otherwise, you must create a workload policy to create a MIG with A4X Max instances.

To create a workload policy, select one of the following options:

### gcloud

To create a workload policy, use the [ `gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy).

For inter-accelerator network configuration, specify the `--accelerator-topology` flag in the command.

Use the following command for A4X Max machine type. The accelerator topology of `1x72` indicates that 72 GPUs are connected through an NVLink within a block.
    
    
    gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
        --type=high-throughput \
        --accelerator-topology=1x72 \
        --region=REGION
    

Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.
  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).



### REST

To create a workload policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert).

For inter-accelerator network configuration, specify the `acceleratorTopology` field in the request. 

Make the following request for A4X Max machine type. The accelerator topology of `1x72` indicates that 72 GPUs are connected through an NVLink within a block.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
      {
        "name": "WORKLOAD_POLICY_NAME"
        "workloadPolicy": {
          "type": "HIGH_THROUGHPUT",
          "acceleratorTopology": "1x72"
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.



### Create an instance template

Specify the instance properties for a MIG by creating an instance template.

To create an instance template, select one of the following options.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

**Important:** The following example uses the networking setup for multiple sub-blocks. If you're creating only a single A4X Max sub-block and you only created the IDPF network in the Create VPC networks step, then remove the eight RDMA subnets indicated by the `MRDMA` NIC type from the example.

A4X Max instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=a4x-maxgpu-4g-metal \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=IDPF,network=IDPF_NETWORK_PREFIX-net,stack-type=IPV6_ONLY,subnet=IDPF_NETWORK_PREFIX-sub-0 \
        --network-interface=nic-type=IDPF,network=IDPF_NETWORK_PREFIX-net,stack-type=IPV6_ONLY,subnet=IDPF_NETWORK_PREFIX-sub-1,no-address \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --network-interface=subnet=default-subnet-1-RDMA_NAME_PREFIX-net,stack-type=IPV6_ONLY,nic-type=mrdma \
        --reservation-affinity=specific \
        --reservation=RESERVATION \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=DELETE \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
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



###  REST 

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).

**Important:** The following example uses the networking setup for multiple sub-blocks. If you're creating only a single A4X Max sub-block and you only created the IDPF network in the Create VPC networks step, then remove the eight RDMA subnets indicated by the `MRDMA` NIC type from the example.

A4X Max instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "a4x-maxgpu-4g-metal",
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
            "instanceTerminationAction": "DELETE",
            "onHostMaintenance": "TERMINATE",
            "automaticRestart": true
          }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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



### Create a MIG

When creating a MIG using the A4X Max machine type, specify the instance count by using the MIG's target size. You can set the target size during MIG creation to either the required number of instances or start with zero and increase it later. Note that you cannot use [resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) to add instances to an A4X Max MIG. 

To obtain a GPU topology of `1x72`, create a MIG with 18 A4X Max instances. When you create the MIG, apply the workload policy that specifies the `acceleratorTopology` field. Applying the policy ensures that Compute Engine creates all 18 A4X Max instances in one sub-block to use an NVLink domain. If a sub-block lacks capacity for all 18 instances, then any [managed instance](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#what_is_a_managed_instance) that can't be created immediately will remain in `CREATING` state until capacity becomes available. These managed instances represent the compute instances that the MIG creates when there is capacity. 

**Important:** When you create an A4X Max MIG with a `1x72` topology, Compute Engine allocates an entire 18-instance sub-block (NVLink domain) to that MIG. If you create fewer than 18 instances, the unused instances in that sub-block remain idle and are unavailable for other MIGs. However, it's possible to provision these unused instances by resizing the MIG. To maximize resource efficiency, we recommend that you create exactly 18 instances in a MIG. 

When you apply a workload policy with the `acceleratorTopology` field set to `1x72`, you cannot create more than 18 A4X Max instances in a MIG. Specifying more than 18 instances causes the MIG creation to fail. To create multiple NVLink domains, create a separate MIG for each domain and apply the same workload policy to each MIG.

To create a MIG, select one of the following options:

###  gcloud 

To create a MIG with a specified target size, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

**Important:** If the instance template specifies Flex-start VMs, then you must also [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by adding the `--default-action-on-vm-failure=do-nothing` flag to the command. 

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, use the following command: 
        
        gcloud compute instance-groups managed create MIG_NAME \
          --template=INSTANCE_TEMPLATE_URL \
          --size=TARGET_SIZE \
          --workload-policy=WORKLOAD_POLICY_URL \
          --zone=ZONE
        

  * To create a regional MIG, use the following command: 
        
        gcloud compute instance-groups managed create MIG_NAME \
            --template=INSTANCE_TEMPLATE_URL \
            --size=TARGET_SIZE \
            --workload-policy=WORKLOAD_POLICY_URL \
            --region=REGION
        


Replace the following: 
  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `TARGET_SIZE`: the number of instances that you want in the MIG. For the accelerator topology of `1x72`, set the target size to `18`.
  * `WORKLOAD_POLICY_URL`: The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. 
  * `ZONE`: the zone in which you want to create the MIG. Specify a zone within the workload policy's region.
  * `REGION`: the region in which you want to create the MIG. Specify the same region as that of the workload policy. For a regional MIG, instead of a region, you can specify the zones in that region by using the `--zones` flag.



###  REST 

To create a MIG with a specified target size, make a `POST` request.

**Important:** If the instance template specifies Flex-start VMs, then you must also [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by adding the `"defaultActionOnFailure": "DO_NOTHING"` field to the request. 

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, make a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert). 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
        {
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ],
          "name": "MIG_NAME",
          "targetSize": TARGET_SIZE,
          "resourcePolicies": {
            "workloadPolicy": "WORKLOAD_POLICY_URL"
          }
        }
        

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert). 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
          {
            "name": "MIG_NAME",
            "instanceTemplate": "INSTANCE_TEMPLATE_URL",
            "targetSize": TARGET_SIZE,
            "resourcePolicies": {
              "workloadPolicy": "WORKLOAD_POLICY_URL"
            }
          }
        


Replace the following: 
  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. Specify a zone within the workload policy's region. 
  * `REGION`: the region in which you want to create the MIG. Specify the same region as that of the workload policy. 
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of instances that you want in the MIG. For the accelerator topology of `1x72`, set the target size to `18`.
  * `WORKLOAD_POLICY_URL`: The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. 



### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. If you didn't specify an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation. 

## What's next?

  * [View the topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * [Monitor VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
