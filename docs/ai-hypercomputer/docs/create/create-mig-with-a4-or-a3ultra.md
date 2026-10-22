---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra/
title: Create an AI-optimized A4 or A3 Ultra MIG \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:52.763399+00:00
---

# Create an AI-optimized A4 or A3 Ultra MIG  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized A4 or A3 Ultra MIG Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes how to create a managed instance group (MIG) that uses A4 or A3 Ultra machine types. To learn more about these accelerator-optimized machine types, see [A4](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4) or [A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-ultra).

Creating a MIG lets you manage multiple virtual machines (VMs) as a single entity. Each VM in a MIG is based on an instance template. By automatically managing the VMs in the group, MIGs offer high availability and scalability. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) in the Compute Engine documentation.

To learn about other ways to create VMs or clusters, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

## Limitations

When you create a MIG with A4 or A3 Ultra VMs, consider the limitations for both the machine type and the MIG.

### Limitations for A4 or A3 Ultra VMs

Depending on the machine series that the VMs in your MIG use, the following limitations apply:

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



### Limitations for the MIG

When you create a MIG with A4 or A3 Ultra VMs, the following limitations apply:

  * You must turn off repairs in the MIG, as described in this document.



  * If you create a regional MIG that uses RDMA networking, then the MIG can only create A4 or A3 Ultra instances in the zone where you [configured the network profile for RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra#setup-network). 

  * You can't configure [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility) in the MIG.



  * If you want the MIG to use a workload policy, then review the [limitations for workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#limitations).



#### Limitations for MIG resize requests

For MIG resize requests, the following limitations apply:

  * In regional MIGs, you can use only the `ANY_SINGLE_ZONE` [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).

  * You can only set the [standby pool mode of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig#standby_policy) to `manual` (default).

  * You can't set [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler).

  * If the MIG contains accepted resize requests, then you can't change the [target size of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size).

  * You can't delete or abandon the managed instances in a `CREATING` status that the MIG creates for a resize request. To delete those managed instances, you must [cancel the resize request](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig#cancel-request).




For more information, see [all the limitations for resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig#limitations).

## Before you begin

Before creating a MIG, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). 



### Required roles

To get the permissions that you need to create a MIG, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a MIG. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a MIG:

  * To create a MIG: `compute.instanceGroupManagers.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

Creating a MIG with the A4 or A3 Ultra machine type includes the following steps:

  1. Create VPC networks
  2. Optional: Create a workload policy
  3. Create an instance template
  4. Create a MIG
  5. Install GPU drivers
  6. Optional: Enable NVIDIA Multi-Instance GPU mode



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



### Optional: Create a workload policy

If you want your VMs to be placed in a single or adjacent blocks, then specify VM placement by creating a [workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy). However, if you want Compute Engine to place your VMs on a specific block, skip this step and provide the name of the block in the reservation affinity when you create the instance template. 

To create a workload policy, select one of the following options:

### gcloud

To create a workload policy, use the [ `gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy).

  * For a best-effort placement of A4 VMs, specify the `--type=high-throughput` flag in the command:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --region=REGION
        

  * For strict colocation of A4 or A3 Ultra VMs, specify the `--max-topology-distance` and `--type=high-throughput` flags in the command:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --max-topology-distance=TOPOLOGY_DISTANCE \
            --region=REGION
        




Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.
  * `TOPOLOGY_DISTANCE`: the maximum topology distance. Specify one of the following values: 
    * To place A4 or A3 Ultra VMs in the same sub-block: `SUBBLOCK`
    * To place A4 or A3 Ultra VMs in the same block: `BLOCK`
    * To place A4 VMs in the same cluster: `CLUSTER`

**Note:** A shorter maximum distance can reduce the probability of VM availability. For more information, see [ Maximum topology distance property](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance).

  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).



### REST

To create a workload policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert).

  * For a best-effort placement of A4 VMs, specify the `type` field in the request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
          {
            "name": "WORKLOAD_POLICY_NAME"
            "workloadPolicy": {
              "type": "HIGH_THROUGHPUT"
            }
          }
        

  * For strict colocation of A4 or A3 Ultra VMs, specify the `maxTopologyDistance` and `type` fields in the request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
          {
            "name": "WORKLOAD_POLICY_NAME"
            "workloadPolicy": {
              "type": "HIGH_THROUGHPUT",
              "maxTopologyDistance": "TOPOLOGY_DISTANCE"
            }
          }
        




Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.
  * `TOPOLOGY_DISTANCE`: the maximum topology distance. Specify one of the following values: 
    * To place A4 or A3 Ultra VMs in the same sub-block: `SUBBLOCK`
    * To place A4 or A3 Ultra VMs in the same block: `BLOCK`
    * To place A4 VMs in the same cluster: `CLUSTER`

**Note:** A shorter maximum distance can reduce the probability of VM availability. For more information, see [Maximum topology distance property](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance).




### Create an instance template

Specify the VM properties for a MIG by creating an instance template.

To create an instance template, select one of the following options:

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A4 or A3 Ultra instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
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
        --instance-termination-action=DELETE \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Flex-start
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
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
        --instance-termination-action=DELETE \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE \
        --provisioning-model=FLEX_START
    
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RUN_DURATION`: the duration you want the requested VMs to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days. 



### Spot
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
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
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



###  REST 

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A4 or A3 Ultra instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
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
            "instanceTerminationAction": "DELETE",
            "onHostMaintenance": "TERMINATE",
            "automaticRestart": true
          }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Flex-start
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
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
            "instanceTerminationAction": "DELETE",
            "maxRunDuration": {
              "seconds": RUN_DURATION
            },
            "onHostMaintenance": "TERMINATE",
            "provisioningModel": "FLEX_START"
          }
    
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `RUN_DURATION`: the duration, in seconds, you want the requested VMs to run. The value must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).



### Spot
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "machineType": "MACHINE_TYPE",
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
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
  * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



After you create the instance template, you can [view it](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to see its ID and review its instance properties.

### Create a MIG

After you complete all the previous steps, create a MIG based on your scenario as follows:

Scenario | Method to create a MIG and VMs in it | Example  
---|---|---  
You have multiple or parallel jobs that can start with any number of VMs. | Create a MIG and use the target size to specify the number of VMs that you want in the group.  
See Create a MIG with a target size. | ML inference jobs  
You have a job that requires distribution across an exact number of VMs. | Create a MIG without any VMs in it, and then create a resize request in the MIG. The resize request helps you to obtain VMs all at once.   
See Create a MIG and a resize request. | Distributed ML training and fine-tuning jobs  
  
#### Create a MIG with a target size

If you can start your job without creating all of the VMs at once, then create a MIG with a _target size_. The target size determines the number of VMs in the MIG. The MIG starts creating VMs based on current resource availability. If any resources are temporarily unavailable, then the MIG continuously attempts to create VMs to meet the target size.

To create a MIG with a target size, select one of the following options:

###  gcloud 

To create a MIG with a specified target size, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

**Important:** If the instance template specifies Flex-start VMs, then you must also [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by adding the `--default-action-on-vm-failure=do-nothing` flag to the command. 

The commands that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

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
  * `TARGET_SIZE`: the number of instances that you want in the MIG. 
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `--workload-policy` flag.
  * `ZONE`: the zone in which you want to create the MIG. If you use a workload policy, then specify a zone within the policy's region.
  * `REGION`: the region in which you want to create the MIG. If you use a workload policy, then specify the same region as that of the policy. For a regional MIG, instead of a region, you can specify the zones in that region by using the `--zones` flag.



###  REST 

To create a MIG with a specified target size, make a `POST` request.

**Important:** If the instance template specifies Flex-start VMs, then you must also [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) by adding the `"defaultActionOnFailure": "DO_NOTHING"` field to the request. 

The requests that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.

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
  * `ZONE`: the zone in which you want to create the MIG. If you use a workload policy, then specify a zone within the policy's region.
  * `REGION`: the region in which you want to create the MIG. If you use a workload policy, then specify the same region as that of the policy. 
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of instances that you want in the MIG. 
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field. 



#### Create a MIG and a resize request

**Preview — Resize request creation by specifying VM names**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you require multiple VMs all at once to start a job, then create a MIG, and create a [resize request](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) in the MIG as described in this section.

To create a resize request in a MIG, select one of the following options:

###  gcloud 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model. 

### Reservation

The commands that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --zone=ZONE
           

  * To create a regional MIG and a resize request in it, do the following:

    1. Create a regional MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zones=ZONE \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




### Flex-start

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --default-action-on-vm-failure=do-nothing \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --zone=ZONE
           

  * To create a regional MIG and a resize request in it, do the following:

    1. Create a regional MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --default-action-on-vm-failure=do-nothing \
           
               --workload-policy=WORKLOAD_POLICY_URL \
           
               --region=REGION \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none \
               --workload-policy=WORKLOAD_POLICY_URL
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




### Spot

The commands that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `--workload-policy` flag.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zone=ZONE
           

    2. Create a resize request in the zonal MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --zone=ZONE
           

  * To create a regional MIG and a resize request in it, do the following:

    1. Create a regional MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
               --workload-policy=WORKLOAD_POLICY_URL \
               --zones=ZONE \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




Replace the following: 

  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `--workload-policy` flag.
  * `ZONE`: the zone in which you want to create the MIG. For a regional MIG also, you must specify a zone. This zone must be the zone that contains the profile for your VPC network and must be a [zone where the machine type is available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). For more information, see Limitations.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `COUNT`: the number of instances to add to the MIG all at once.
  * `REGION`: the region in which you want to create the MIG.



#### Create a resize request by specifying a list of VM names

If your workload requires specific VM names, then specify a list of names to create the VMs. The number of names that you specify determines the number of VMs that the MIG creates all at once.

To create a resize request with specific VM names in a MIG, use the [beta `gcloud compute instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize-requests/create) with the `--instances` flag:

  * In a zonal MIG, run the following command:
        
        gcloud beta compute instance-groups managed resize-requests create MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --instances=INSTANCE_NAMES \
            --zone=ZONE
        

  * In a regional MIG, run the following command:
        
        gcloud beta compute instance-groups managed resize-requests create MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --instances=INSTANCE_NAMES \
            --region=REGION
        


Replace `INSTANCE_NAMES` with a comma-separated list of names for the VMs. For example, `instance-1,instance-2,instance-3`. 

###  REST 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model. 

### Reservation

The requests that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following: 
    1. Create a zonal MIG by making a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           

  * To create a regional MIG and a resize request in it, do the following: 
    1. Create a regional MIG by making a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "distributionPolicy": {
               "targetShape": "ANY_SINGLE_ZONE",
               "zones": [
                 {
                   "zone": "projects/PROJECT_ID/zones/ZONE"
                 }
               ]
             },
             "updatePolicy": {
               "instanceRedistributionType": "NONE"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




### Flex-start

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following: 
    1. Create a zonal MIG by making a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "instanceLifecyclePolicy": {
               "defaultActionOnFailure": "DO_NOTHING"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           

  * To create a regional MIG and a resize request in it, do the following: 
    1. Create a regional MIG by making a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "distributionPolicy": {
               "targetShape": "ANY_SINGLE_ZONE",
               "zones": [
                 {
                   "zone": "projects/PROJECT_ID/zones/ZONE"
                 }
               ]
             },
             "updatePolicy": {
               "instanceRedistributionType": "NONE"
             },
             "instanceLifecyclePolicy": {
               "defaultActionOnFailure": "DO_NOTHING"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




### Spot

The requests that you use to create a MIG use a workload policy to specify instance placement. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following: 
    1. Create a zonal MIG by making a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the zonal MIG by making a `POST` request to the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           

  * To create a regional MIG and a resize request in it, do the following: 
    1. Create a regional MIG by making a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
           {
             "versions": [
               {
                 "instanceTemplate": "INSTANCE_TEMPLATE_URL"
               }
             ],
             "name": "MIG_NAME",
             "targetSize": 0,
             "distributionPolicy": {
               "targetShape": "ANY_SINGLE_ZONE",
               "zones": [
                 {
                   "zone": "projects/PROJECT_ID/zones/ZONE"
                 }
               ]
             },
             "updatePolicy": {
               "instanceRedistributionType": "NONE"
             },
             "resourcePolicies": {
               "workloadPolicy": "WORKLOAD_POLICY_URL"
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




Replace the following: 

  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. This zone must be the same as the zone that contains the profile for your VPC network and must be a [zone where your chosen machine type is available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). For more information, see Limitations. 
  * `REGION`: the region in which you want to create the MIG. This region must be the same region that contains the profile for your VPC network and must contain a [zone where your chosen machine type is available](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). For more information, see Limitations. 
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `WORKLOAD_POLICY_URL`: Optional. The URL of the workload policy—for example, `projects/example-project/regions/us-central1/resourcePolicies/example-workload-policy`. If you don't want to use a workload policy, then remove the `resourcePolicies.workloadPolicy` field.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `COUNT`: the number of instances to add to the MIG all at once



#### Create a resize request by specifying a list of VM names

If your workload requires specific VM names, then specify a list of names to create the VMs. The number of names that you specify determines the number of VMs that the MIG creates all at once.

To create a resize request with specific VM names in a MIG, use one of the following methods:

  * In a zonal MIG, send a `POST` request by using the [`beta.instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagerResizeRequests/insert):
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
        

  * In a regional MIG, send a `POST` request by using the [`beta.regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagerResizeRequests/insert):
        
        POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
        




For example, to specify two VM names, include the following in the request body:
    
    
    {
      "name": "RESIZE_REQUEST_NAME",
      "instances": [
        {
          "name": "INSTANCE_NAME_1"
        },
        {
          "name": "INSTANCE_NAME_2"
        }
      ]
    }
    

  
Replace `INSTANCE_NAME_1, INSTANCE_NAME_2` with the names for the VMs. 

### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. If you didn't specify an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation. 

### Optional: Enable NVIDIA Multi-Instance GPU mode

**Note:** In this section, _MIG_ refers to Multi-Instance GPU from NVIDIA, not a managed instance group.  Multi-Instance GPU (MIG) mode is a feature that you can enable for a [supported NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html). After you create an instance, you can enable MIG mode on a single GPU that is attached to your machine. With MIG mode enabled, the single GPU is partitioned into as many as seven independent GPU instances. Each instance runs simultaneously, each with its own memory, cache, and streaming multiprocessors. You can then run different workloads on these GPU instances in parallel. For more information about using MIG mode, see the [Multi-Instance GPU (MIG) User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#getting-started-with-mig) in the NVIDIA documentation. 

## What's next?

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View the topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * [Monitor VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor)
  * [Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)
  * [View, cancel, or delete resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
