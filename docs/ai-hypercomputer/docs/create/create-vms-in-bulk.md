---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk/
title: Create AI-optimized A4 or A3 Ultra VMs in bulk \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:57.079857+00:00
---

# Create AI-optimized A4 or A3 Ultra VMs in bulk  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create AI-optimized A4 or A3 Ultra VMs in bulk Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to create virtual machine (VM) instances in bulk that use A4 or A3 Ultra machine types. To learn more about these accelerator-optimized machine types, see [A4](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4) or [A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3-ultra).

For more information about creating VMs in bulk, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation) in the Compute Engine documentation.

To learn about other ways to create VMs or clusters, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

## Limitations

When you create A4 or A3 Ultra VMs in bulk, the following limitations apply:

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



If you want to use a compact placement policy, then review the [restrictions for placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions). 

## Before you begin

Before creating VMs in bulk, if you haven't already done so, complete the following steps:

  1. **Choose a consumption option** : your choice of consumption option determines how you get and use GPU resources. To learn more, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  2. **Obtain capacity** : the process to obtain capacity differs for each consumption option. To learn about the process to obtain capacity for your chosen consumption option, see [Capacity overview](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity). 



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

To get the permissions that you need to create VMs in bulk, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create VMs in bulk. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VMs in bulk:

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

## Overview

Creating instances in bulk with the A4 or A3 Ultra machine type includes the following steps:

  1. Create VPC networks
  2. Optional: Create a compact placement policy
  3. Create instances in bulk
  4. Install GPU drivers
  5. Optional: Enable NVIDIA Multi-Instance GPU mode



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



### Optional: Create a compact placement policy

**Tip:** Decide whether to create a compact placement policy as follows:

  * If you want to place VMs on a specific block, then use the reservation-bound provisioning model, skip this step, and provide the name of the block when you create VMs.
  * If you want to place your VMs in single or adjacent blocks, then specify VM placement by creating a compact placement policy and applying it when you create VMs.



You can specify VM placement by creating a compact placement policy. When you apply a compact placement policy to your VMs, Compute Engine makes best-effort attempts to create VMs that are as close to each other as possible. If your application is latency-sensitive and requires maximum compactness, then specify the `maxDistance` field ([Preview](https://cloud.google.com/products/#product-launch-stages)) when you create a compact placement policy. A lower `maxDistance` value ensures closer VM placement, but it also increases the chance that some VMs won't be created.

To create a compact placement policy, select one of the following options: 

### gcloud

To create a compact placement policy, use the [ `gcloud compute resource-policies create group-placement` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/group-placement):
    
    
    gcloud compute resource-policies create group-placement POLICY_NAME \
        --collocation=collocated \
        --max-distance=MAX_DISTANCE \
        --region=REGION
    

Replace the following:

  * `POLICY_NAME`: the name of the compact placement policy.
  * `MAX_DISTANCE`: the maximum distance configuration for your VMs, which can either be specified ([Preview](https://cloud.google.com/products/#product-launch-stages), recommended) or unspecified (remove the `--max-distance` flag). Based on what your machine type supports, you can specify one of the following values: 
    * To place VMs in the same sub-block: `1`
    * To place VMs in the same block: `2`
    * To place VMs in adjacent blocks: `3`
Ensure that the maximum distance configuration supports the machine series and number of VMs that you plan to create. For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) in the Compute Engine documentation.
  * `REGION`: the region where you want to create the compact placement policy. Specify the region that contains the zone where you plan to create instances, and verify that the machine type that you want to use is available in that region. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). 



### REST

To create a compact placement policy, make a `POST` request to the [`resourcePolicies.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/resourcePolicies). In the request body, include the `collocation` field set to `COLLOCATED`, and the `maxDistance` field.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies
      {
        "name": "POLICY_NAME",
        "groupPlacementPolicy": {
          "collocation": "COLLOCATED",
          "maxDistance": MAX_DISTANCE
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `POLICY_NAME`: the name of the compact placement policy.
  * `MAX_DISTANCE`: the maximum distance configuration for your VMs, which can either be specified ([Preview](https://cloud.google.com/products/#product-launch-stages), recommended) or unspecified (remove the `maxDistance` field). Based on what your machine type supports, you can specify one of the following values: 
    * To place VMs in the same sub-block: `1`
    * To place VMs in the same block: `2`
    * To place VMs in adjacent blocks: `3`
Ensure that the maximum distance configuration supports the machine series and number of VMs that you plan to create. For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) in the Compute Engine documentation.
  * `REGION`: the region where you want to create the compact placement policy. Specify the region that contains the zone where you plan to create instances, and verify that the machine type that you want to use is available in that region. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table). 



### Create A3 Ultra or A4 VMs in bulk

To create A3 Ultra or A4 VMs in bulk, use one of the following methods.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create instances in bulk, use the [ `gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A4 or A3 Ultra instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --count=COUNT \
         --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --region=REGION \
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

     * `NAME_PATTERN`: the name pattern to use for the A4 or A3 Ultra instances. For example, using `instance-#` for the name pattern generates A4 or A3 Ultra instances with names such as `instance-1` and `instance-2`, up to the number of A4 or A3 Ultra instances specified by `--count`.
     * `COUNT`: the number of A4 or A3 Ultra instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
       * To create instances across blocks or on a single block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, apply a compact placement policy that specifies a block collocation (`maxDistance=2`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

       * To create instances on a specific block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A4 or A3 Ultra instance at the end of the reservation period. 

  2. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Run the command.



### Spot

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --count=COUNT \
         --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --region=REGION \
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

     * `NAME_PATTERN`: the name pattern to use for the A4 or A3 Ultra instances. For example, using `instance-#` for the name pattern generates A4 or A3 Ultra instances with names such as `instance-1` and `instance-2`, up to the number of A4 or A3 Ultra instances specified by `--count`.
     * `COUNT`: the number of A4 or A3 Ultra instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Run the command.



###  REST 

To create instances in bulk, make a `POST` request to the [ `instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A4 or A3 Ultra instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * Future reservations for capacity blocks
  * Future reservations in calendar mode



To consume these types of reservations, an instance must use the _reservation-bound provisioning model_. For example, use the following creation parameters.

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    {
      "namePattern": "NAME_PATTERN",
      "count": "COUNT",
      "instanceProperties": {
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
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the A4 or A3 Ultra instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the A4 or A3 Ultra instances. For example, using `instance-#` for the name pattern generates A4 or A3 Ultra instances with names such as `instance-1` and `instance-2`, up to the number of A4 or A3 Ultra instances specified by `--count`.
     * `COUNT`: the number of A4 or A3 Ultra instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `REGION`: the region of the subnetwork.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
       * To create instances across blocks or on a single block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, apply a compact placement policy that specifies a block collocation (`maxDistance=2`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

       * To create instances on a specific block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A4 or A3 Ultra instance at the end of the reservation period. 

  2. Optional: If you chose to use a compact placement policy, then add the following `instanceProperties` subfield to the request body:
         
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
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
    {
      "namePattern": "NAME_PATTERN",
      "count": "COUNT",
      "instanceProperties": {
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
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the A4 or A3 Ultra instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the A4 or A3 Ultra instances. For example, using `instance-#` for the name pattern generates A4 or A3 Ultra instances with names such as `instance-1` and `instance-2`, up to the number of A4 or A3 Ultra instances specified by `--count`.
     * `COUNT`: the number of A4 or A3 Ultra instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A4 or A3 Ultra instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). **Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `REGION`: the region of the subnetwork.
     * `RDMA_NAME_PREFIX`: the name prefix that you specified when creating the VPC networks and subnets that use RDMA NICs.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, then add the following `instanceProperties` subfield to the request body:
         
         "resourcePolicies": [
               "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
             ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Submit the request.



For more information about the configuration options when creating VMs in bulk, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk) in the Compute Engine documentation.

### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. If you didn't specify an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation. 

### Optional: Enable NVIDIA Multi-Instance GPU mode

Multi-Instance GPU (MIG) mode is a feature that you can enable for a [supported NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html). After you create an instance, you can enable MIG mode on a single GPU that is attached to your machine. With MIG mode enabled, the single GPU is partitioned into as many as seven independent GPU instances. Each instance runs simultaneously, each with its own memory, cache, and streaming multiprocessors. You can then run different workloads on these GPU instances in parallel. For more information about using MIG mode, see the [Multi-Instance GPU (MIG) User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#getting-started-with-mig) in the NVIDIA documentation. 

## What's next

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View the topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * [Run workloads overview](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
