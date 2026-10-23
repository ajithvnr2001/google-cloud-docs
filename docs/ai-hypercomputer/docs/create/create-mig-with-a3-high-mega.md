---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-high-mega/
title: Create an AI-optimized A3 High or A3 Mega MIG \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:10.962818+00:00
---

# Create an AI-optimized A3 High or A3 Mega MIG  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-high-mega/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized A3 High or A3 Mega MIG Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes how to create a managed instance group (MIG) that uses an A3 High or A3 Mega accelerator-optimized machine type. To learn more about the machine types, see [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus).

Creating a MIG lets you manage multiple virtual machines (VMs) as a single entity. Each VM in a MIG is based on an instance template. By automatically managing the VMs in the group, MIGs offer high availability and scalability. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) in the Compute Engine documentation.

To learn about other ways to create VMs or clusters, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

## Limitations

When you create a MIG with A3 Mega or A3 High VMs, consider the limitations for both the machine type and the MIG.

### Limitations for A3 Mega or A3 High VMs

Depending on the machine series that the VMs in your MIG use, the following limitations apply:

###  A3 Mega 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Mega machine type.
  * You can only use an A3 Mega machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Mega machine type.
  * The A3 Mega machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Mega machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Mega machine type.



###  A3 High 

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 High machine type.
  * You can only use an A3 High machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 High machine type.
  * The A3 High machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 High machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 High machine type.
  * For `a3-highgpu-1g`, `a3-highgpu-2g`, and`a3-highgpu-4g` machine types, you must create instances by using Spot VMs or Flex-start VMs. For detailed instructions on these options, review the following: 
    * To create Spot VMs, set the provisioning model to `SPOT` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
    * To create Flex-start VMs, you can use one of the following methods: 
      * Create a standalone VM and set the provisioning model to `FLEX_START` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
      * Create a resize request in a managed instance group (MIG). For instructions, see [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with an `a3-highgpu-1g` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1), and all the [limitations for Confidential VM running on the A3 High machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.



### Limitations for the MIG

When you create a MIG with A3 Mega or A3 High VMs, the following limitations apply:

  * You must turn off repairs in the MIG, as described in this document.



  * If you create a regional MIG that uses RDMA networking, then the MIG can only create A3 Mega or A3 High instances in the zone where you [configured the network profile for RDMA](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-high-mega#setup-network). 

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

Creating a MIG with the A3 Mega or A3 High (8 GPUs) machine type includes the following steps:

  1. Create VPC networks
  2. Optional: Create a workload policy
  3. Create an instance template
  4. Create a MIG
  5. Install GPU drivers
  6. Optional: Enable NVIDIA Multi-Instance GPU mode



### Create VPC networks

To enable efficient communication for your GPU VMs, you need to create a management network and one or more data networks. The management network is used for external access, for example SSH, and for most general network communication. The data networks are used for high-performance communication between the GPUs on different VMs, for example, for Remote Direct Memory Access (RDMA) traffic.

For these VPC networks, we recommend setting the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) to a larger value. Higher MTU values increase the packet size and reduce the packet-header overhead, which increases payload data throughput. For more information about how to create VPC networks, see [Create and verify a jumbo frame MTU network](https://docs.cloud.google.com/vpc/docs/configure-jumbo-frame-mtu-vpc).

#### Create management network, subnet, and firewall rule

Complete the following steps to set up the management network:

  1. Create the management network by using the [`networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
         
         gcloud compute networks create NETWORK_NAME_PREFIX-mgmt-net \
             --project=PROJECT_ID \
             --subnet-mode=custom \
             --mtu=8244
         

  2. Create the management subnet by using the [`networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create):
         
         gcloud compute networks subnets create NETWORK_NAME_PREFIX-mgmt-sub \
             --project=PROJECT_ID \
             --network=NETWORK_NAME_PREFIX-mgmt-net \
             --region=REGION \
             --range=192.168.0.0/24
         

  3. Create firewall rules by using the [`firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create).

     1. Create a firewall rule for the management network.
            
            gcloud compute firewall-rules create NETWORK_NAME_PREFIX-mgmt-internal \
                --project=PROJECT_ID \
                --network=NETWORK_NAME_PREFIX-mgmt-net \
                --action=ALLOW \
                --rules=tcp:0-65535,udp:0-65535,icmp \
                --source-ranges=192.168.0.0/16
            

     2. Create the `tcp:22` firewall rule to limit which source IP addresses can connect to your VM by using SSH.
            
            gcloud compute firewall-rules create NETWORK_NAME_PREFIX-mgmt-external-ssh \
                --project=PROJECT_ID \
                --network=NETWORK_NAME_PREFIX-mgmt-net \
                --action=ALLOW \
                --rules=tcp:22 \
                --source-ranges=SSH_SOURCE_IP_RANGE
            

     3. Create the `icmp` firewall rule that can be used to check for data transmission issues in the network.
            
            gcloud compute firewall-rules create NETWORK_NAME_PREFIX-mgmt-external-ping \
                --project=PROJECT_ID \
                --network=NETWORK_NAME_PREFIX-mgmt-net \
                --action=ALLOW \
                --rules=icmp \
                --source-ranges=0.0.0.0/0
            




Replace the following:

  * `NETWORK_NAME_PREFIX`: the name prefix to use for the VPC networks and subnets.
  * `PROJECT_ID` : your project ID.
  * `REGION`: the region where you want to create the networks.
  * `SSH_SOURCE_IP_RANGE`: IP range in CIDR format. This specifies which source IP addresses can connect to your VM by using SSH.



#### Create data networks, subnets, and firewall rule

The number of data networks varies depending on the type of GPU machine you are creating.

### A3 Mega

A3 Mega requires eight data networks. To create eight data networks, each with subnets and firewall rules, use the following command.
    
    
    for N in $(seq 1 8); do
    gcloud compute networks create NETWORK_NAME_PREFIX-data-net-$N \
        --project=PROJECT_ID \
        --subnet-mode=custom \
        --mtu=8244
    
    gcloud compute networks subnets create NETWORK_NAME_PREFIX-data-sub-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --region=REGION \
        --range=192.168.$N.0/24
    
    gcloud compute firewall-rules create NETWORK_NAME_PREFIX-data-internal-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --action=ALLOW \
        --rules=tcp:0-65535,udp:0-65535,icmp \
        --source-ranges=192.168.0.0/16
    done
    

### A3 High

A3 High require four data networks. Use the following command to create four data networks, each with subnets and firewall rules.
    
    
    for N in $(seq 1 4); do
    gcloud compute networks create NETWORK_NAME_PREFIX-data-net-$N \
        --project=PROJECT_ID \
        --subnet-mode=custom \
        --mtu=8244
    
    gcloud compute networks subnets create NETWORK_NAME_PREFIX-data-sub-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --region=REGION \
        --range=192.168.$N.0/24
    
    gcloud compute firewall-rules create NETWORK_NAME_PREFIX-data-internal-$N \
        --project=PROJECT_ID \
        --network=NETWORK_NAME_PREFIX-data-net-$N \
        --action=ALLOW \
        --rules=tcp:0-65535,udp:0-65535,icmp \
        --source-ranges=192.168.0.0/16
    done
    

### Optional: Create a workload policy

If you want your VMs to be placed in a single or adjacent blocks, then specify VM placement by creating a [workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy#workload-policy). However, if you want Compute Engine to place your VMs on a specific block, skip this step and provide the name of the block in the reservation affinity when you create the instance template. 

To create a workload policy, select one of the following options:

### gcloud

To create a workload policy, use the [ `gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy).

  * For a best-effort placement of VMs, specify the `--type=high-throughput` flag in the command:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --region=REGION
        

  * For strict colocation of VMs, specify the `--max-topology-distance` and `--type=high-throughput` flags in the command:
        
        gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
            --type=high-throughput \
            --max-topology-distance=TOPOLOGY_DISTANCE \
            --region=REGION
        




Replace the following:

  * `WORKLOAD_POLICY_NAME`: the name of the workload policy.
  * `TOPOLOGY_DISTANCE`: the maximum topology distance. Specify one of the following values: 
    * To place VMs in the same block: `BLOCK`
    * To place VMs in the same cluster: `CLUSTER`

**Note:** A shorter maximum distance can reduce the probability of VM availability. For more information, see [ Maximum topology distance property](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance).

  * `REGION`: the region where you want to create the workload policy. Specify a region in which you want to create the MIG and the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).



### REST

To create a workload policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies/insert).

  * For a best-effort placement of VMs, specify the `type` field in the request as follows:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
          {
            "name": "WORKLOAD_POLICY_NAME"
            "workloadPolicy": {
              "type": "HIGH_THROUGHPUT"
            }
          }
        

  * For strict colocation of VMs, specify the `maxTopologyDistance` and `type` fields in the request as follows:
        
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
    * To place VMs in the same block: `BLOCK`
    * To place VMs in the same cluster: `CLUSTER`

**Note:** A shorter maximum distance can reduce the probability of VM availability. For more information, see [Maximum topology distance property](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies#max-distance).




### Create an instance template

Specify the VM properties for a MIG by creating an instance template.

To create an instance template, select one of the following options:

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

### A3 Mega

To create an instance template for A3 Mega VMs, you must specify eight additional network interfaces for GPUDirect-TCPXO traffic. If you haven't already, make sure that you have created eight VPC networks as described in Create VPC networks.

###  gcloud 

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A3 Mega or A3 High (8 GPUs) instances support multiple provisioning models for reservations. Select the tab that corresponds to the [type of reservation](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) that you want to consume.

  * Use the _Reservation-bound_ parameters, which specify the reservation-bound provisioning model, for the following:

    * Future reservations for capacity blocks
    * Future reservations in calendar mode
  * Use the _Standard reservation_ parameters, which specify the standard provisioning model, for the following:

    * On-demand reservations
    * Standard future reservations



### Reservation-bound
    
    
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-5,subnet=GVNIC_NAME_PREFIX-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-6,subnet=GVNIC_NAME_PREFIX-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-7,subnet=GVNIC_NAME_PREFIX-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-8,subnet=GVNIC_NAME_PREFIX-sub-8,no-address \
        --reservation-affinity=specific \
        --reservation=RESERVATION \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=DELETE \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Standard reservation

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-5,subnet=GVNIC_NAME_PREFIX-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-6,subnet=GVNIC_NAME_PREFIX-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-7,subnet=GVNIC_NAME_PREFIX-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-8,subnet=GVNIC_NAME_PREFIX-sub-8,no-address \
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY \
        --reservation=RESERVATION
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`any` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Caution:** When matching reservation capacity is unavailable, the instance uses the on-demand consumption option instead, which has different billing and capacity assurance. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). 
       * **`specific` (Reservation capacity is required)**: Require the instance to use capacity from a [_specifically targeted_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type). The instance isn't allowed to use on-demand capacity. If reservation capacity is unavailable, then the instance creation fails.

     * `RESERVATION`: the reservation to use. Specify one of the following based on the value you specified for `RESERVATION_AFFINITY`:

       * If you specified `any`, then replace `RESERVATION` with an empty string (`""`). Alternatively, you can remove the `--reservation` flag entirely.
       * If you specified `specific`, then replace `RESERVATION` with the following:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Replace the following:

         * `RESERVATION_OWNER_PROJECT_ID`: the project ID of the project where the reservation was created.
**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
         * `RESERVATION_NAME`: the name of the reservation.
  2. By default, the instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. If you want to disable automatic restart, then add the following flag:
         
         --no-restart-on-failure

  3. Run the command.



### On-demand

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-5,subnet=GVNIC_NAME_PREFIX-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-6,subnet=GVNIC_NAME_PREFIX-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-7,subnet=GVNIC_NAME_PREFIX-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-8,subnet=GVNIC_NAME_PREFIX-sub-8,no-address \
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`any` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
       * **`none` (On-demand capacity is required)**: Block the instance from using any reservation capacity.

  2. By default, the instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. If you want to disable automatic restart, then add the following flag:
         
         --no-restart-on-failure

  3. Run the command.



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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-5,subnet=GVNIC_NAME_PREFIX-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-6,subnet=GVNIC_NAME_PREFIX-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-7,subnet=GVNIC_NAME_PREFIX-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-8,subnet=GVNIC_NAME_PREFIX-sub-8,no-address \
        --instance-termination-action=DELETE \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE \
        --provisioning-model=FLEX_START
    
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-5,subnet=GVNIC_NAME_PREFIX-sub-5,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-6,subnet=GVNIC_NAME_PREFIX-sub-6,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-7,subnet=GVNIC_NAME_PREFIX-sub-7,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-8,subnet=GVNIC_NAME_PREFIX-sub-8,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --no-restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



###  REST 

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A3 Mega or A3 High (8 GPUs) instances support multiple provisioning models for reservations. Select the tab that corresponds to the [type of reservation](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) that you want to consume.

  * Use the _Reservation-bound_ parameters, which specify the reservation-bound provisioning model, for the following:

    * Future reservations for capacity blocks
    * Future reservations in calendar mode
  * Use the _Standard reservation_ parameters, which specify the standard provisioning model, for the following:

    * On-demand reservations
    * Standard future reservations



### Reservation-bound
    
    
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-5",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-6",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-7",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-7"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-8",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-8"
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
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Standard reservation
    
    
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-5",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-6",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-7",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-7"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-8",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-8"
          }
        ],
        "scheduling": {
        "provisioningModel": "STANDARD",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": AUTOMATIC_RESTART
      },
      "reservationAffinity": {
        "consumeReservationType": "RESERVATION_AFFINITY",
        "key": "compute.googleapis.com/reservation-name",
        "values": [
          "RESERVATION"
        ]
      }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `AUTOMATIC_RESTART`: if your instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. Specify either `true` to enable automatic restart (default) or `false` to disable automatic restart.

  * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

    * **`ANY_RESERVATION` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Caution:** When matching reservation capacity is unavailable, the instance uses the on-demand consumption option instead, which has different billing and capacity assurance. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). 
    * **`SPECIFIC_RESERVATION` (Reservation capacity is required)**: Require the instance to use capacity from a [_specifically targeted_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type). The instance isn't allowed to use on-demand capacity. If reservation capacity is unavailable, then the instance creation fails.

  * `RESERVATION`: the reservation to use. Specify one of the following based on the value you specified for `RESERVATION_AFFINITY`:

    * If you specified `ANY_RESERVATION`, then delete `RESERVATION` so that the value is an empty string (`""`). Alternatively, you can remove the `key` and `values` fields entirely.
    * If you specified `SPECIFIC_RESERVATION`, then replace `RESERVATION` with the following:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Replace the following:

      * `RESERVATION_OWNER_PROJECT_ID`: the project ID of the project where the reservation was created.
**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
      * `RESERVATION_NAME`: the name of the reservation.



### On-demand
    
    
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-5",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-6",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-7",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-7"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-8",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-8"
          }
        ],
        "scheduling": {
        "provisioningModel": "STANDARD",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": AUTOMATIC_RESTART
      },
      "reservationAffinity": {
        "consumeReservationType": "RESERVATION_AFFINITY"
      }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `AUTOMATIC_RESTART`: if your instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. Specify either `true` to enable automatic restart (default) or `false` to disable automatic restart.

  * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

    * **`ANY_RESERVATION` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
    * **`NO_RESERVATION` (On-demand capacity is required)**: Block the instance from using any reservation capacity.




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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-5",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-6",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-7",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-7"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-8",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-8"
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
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-5",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-5"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-6",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-6"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-7",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-7"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-8",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-8"
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
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



### A3 High

To create an instance template for A3 High VMs, you must specify four additional network interfaces for GPUDirect-TCPX traffic. If you haven't already, make sure that you have created four VPC networks as described in Create VPC networks.

###  gcloud 

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A3 Mega or A3 High (8 GPUs) instances support multiple provisioning models for reservations. Select the tab that corresponds to the [type of reservation](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) that you want to consume.

  * Use the _Reservation-bound_ parameters, which specify the reservation-bound provisioning model, for the following:

    * Future reservations for capacity blocks
    * Future reservations in calendar mode
  * Use the _Standard reservation_ parameters, which specify the standard provisioning model, for the following:

    * On-demand reservations
    * Standard future reservations



### Reservation-bound
    
    
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --reservation-affinity=specific \
        --reservation=RESERVATION \
        --provisioning-model=RESERVATION_BOUND \
        --instance-termination-action=DELETE \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Standard reservation

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY \
        --reservation=RESERVATION
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`any` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Caution:** When matching reservation capacity is unavailable, the instance uses the on-demand consumption option instead, which has different billing and capacity assurance. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). 
       * **`specific` (Reservation capacity is required)**: Require the instance to use capacity from a [_specifically targeted_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type). The instance isn't allowed to use on-demand capacity. If reservation capacity is unavailable, then the instance creation fails.

     * `RESERVATION`: the reservation to use. Specify one of the following based on the value you specified for `RESERVATION_AFFINITY`:

       * If you specified `any`, then replace `RESERVATION` with an empty string (`""`). Alternatively, you can remove the `--reservation` flag entirely.
       * If you specified `specific`, then replace `RESERVATION` with the following:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Replace the following:

         * `RESERVATION_OWNER_PROJECT_ID`: the project ID of the project where the reservation was created.
**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
         * `RESERVATION_NAME`: the name of the reservation.
  2. By default, the instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. If you want to disable automatic restart, then add the following flag:
         
         --no-restart-on-failure

  3. Run the command.



### On-demand

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`any` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
       * **`none` (On-demand capacity is required)**: Block the instance from using any reservation capacity.

  2. By default, the instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. If you want to disable automatic restart, then add the following flag:
         
         --no-restart-on-failure

  3. Run the command.



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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --instance-termination-action=DELETE \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE \
        --provisioning-model=FLEX_START
    
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
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
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --no-restart-on-failure
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 



###  REST 

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A3 Mega or A3 High (8 GPUs) instances support multiple provisioning models for reservations. Select the tab that corresponds to the [type of reservation](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type) that you want to consume.

  * Use the _Reservation-bound_ parameters, which specify the reservation-bound provisioning model, for the following:

    * Future reservations for capacity blocks
    * Future reservations in calendar mode
  * Use the _Standard reservation_ parameters, which specify the standard provisioning model, for the following:

    * On-demand reservations
    * Standard future reservations



### Reservation-bound
    
    
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
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
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
    * To create instances across blocks or on a single block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, create the MIG by applying a workload policy that specifies a block collocation (`maxTopologyDistance=BLOCK`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

    * To create instances on a specific block:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 



### Standard reservation
    
    
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          }
        ],
        "scheduling": {
        "provisioningModel": "STANDARD",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": AUTOMATIC_RESTART
      },
      "reservationAffinity": {
        "consumeReservationType": "RESERVATION_AFFINITY",
        "key": "compute.googleapis.com/reservation-name",
        "values": [
          "RESERVATION"
        ]
      }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `AUTOMATIC_RESTART`: if your instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. Specify either `true` to enable automatic restart (default) or `false` to disable automatic restart.

  * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

    * **`ANY_RESERVATION` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Caution:** When matching reservation capacity is unavailable, the instance uses the on-demand consumption option instead, which has different billing and capacity assurance. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). 
    * **`SPECIFIC_RESERVATION` (Reservation capacity is required)**: Require the instance to use capacity from a [_specifically targeted_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type). The instance isn't allowed to use on-demand capacity. If reservation capacity is unavailable, then the instance creation fails.

  * `RESERVATION`: the reservation to use. Specify one of the following based on the value you specified for `RESERVATION_AFFINITY`:

    * If you specified `ANY_RESERVATION`, then delete `RESERVATION` so that the value is an empty string (`""`). Alternatively, you can remove the `key` and `values` fields entirely.
    * If you specified `SPECIFIC_RESERVATION`, then replace `RESERVATION` with the following:
          
          projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Replace the following:

      * `RESERVATION_OWNER_PROJECT_ID`: the project ID of the project where the reservation was created.
**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
      * `RESERVATION_NAME`: the name of the reservation.



### On-demand
    
    
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
          }
        ],
        "scheduling": {
        "provisioningModel": "STANDARD",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": AUTOMATIC_RESTART
      },
      "reservationAffinity": {
        "consumeReservationType": "RESERVATION_AFFINITY"
      }
      }
    }
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
  * `AUTOMATIC_RESTART`: if your instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. Specify either `true` to enable automatic restart (default) or `false` to disable automatic restart.

  * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

    * **`ANY_RESERVATION` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
    * **`NO_RESERVATION` (On-demand capacity is required)**: Block the instance from using any reservation capacity.




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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
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
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
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
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-2",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-2"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-3",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-3"
          },
          {
            "network": "projects/NETWORK_PROJECT_ID/global/networks/GVNIC_NAME_PREFIX-net-4",
            "nicType": "GVNIC",
            "subnetwork": "projects/NETWORK_PROJECT_ID/region/REGION/subnetworks/GVNIC_NAME_PREFIX-sub-4"
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
  * `MACHINE_TYPE`: the machine type to use for the A3 Mega or A3 High (8 GPUs) instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
  * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
  * `IMAGE_PROJECT`: the project ID of the OS image. 
  * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
  * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
  * `NETWORK_PROJECT_ID`: the project ID of the network.
  * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
  * `REGION`: the region of the subnetwork.
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
           




### On-demand

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
           




### On-demand

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
