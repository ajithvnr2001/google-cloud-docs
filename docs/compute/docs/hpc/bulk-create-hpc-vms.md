---
url: https://docs.cloud.google.com/compute/docs/hpc/bulk-create-hpc-vms/
title: Bulk create HPC-optimized instances with H4D \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:59.979414+00:00
---

# Bulk create HPC-optimized instances with H4D  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/hpc/bulk-create-hpc-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Bulk create HPC-optimized instances with H4D Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a large number of high performance computing (HPC) virtual machine (VM) instances in bulk that are identical and independent from each other. The instances use H4D machine types and run on reserved [blocks of capacity](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#block).

For more information about creating VMs in bulk, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation). To create instances in bulk that don't use reservations for enhanced cluster management capabilities, see instead [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

To learn about other ways to create large clusters of tightly-coupled H4D VMs, see the [Overview of HPC cluster creation](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters) page.

## Before you begin

  * **Choose a consumption option** : to create compute instances in bulk and enable enhanced cluster management capabilities, you can choose a Future Reservation in Calendar mode or [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

If you choose to use Spot VMs, the VMs might not be compactly collocated. Also, Spot VMs can be preempted as needed and they are not eligible for [managing host maintenance events for groups of VMs](https://docs.cloud.google.com/compute/docs/hpc/manage-host-events-vms-h4d). 

  * **Obtain capacity** : the process to obtain capacity differs for each consumption option.

To learn more, see [Choose a consumption option and obtain capacity](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity).

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

To get the permissions that you need to create VMs in bulk, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create VMs in bulk. To see the exact permissions that are required, expand the **Required permissions** section: 

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

Creating HPC instances in bulk with the H4D machine type includes the following steps:

  1. Optional: Create Virtual Private Cloud networks.
  2. Optional: Create a placement policy if you aren't creating the compute instances on the same block or sub-block.
  3. Create H4D instances in bulk.



## Optional: Create Virtual Private Cloud networks

When you create a compute instance, you can specify a VPC network and subnet. If you omit this configuration, the default network and subnet are used.

  * If you want to configure the H4D instances in the MIG to use Cloud RDMA, then complete the steps in this section.
  * If you don't want to use Cloud RDMA, then you can skip this section and use the default network instead



To use Cloud RDMA with H4D instances, you must have at least two networks configured, one for each type of network interface (NIC):

  * NIC type `GVNIC`: uses the `gve` driver for TCP/IP and Internet traffic for normal VM-VM and VM-Internet communication.
  * NIC type `IRDMA`: uses IDPF/iRDMA drivers for Cloud RDMA networking between instances.



Instances that use Cloud RDMA can have only one `IRDMA` interface. You can add up to eight additional `GVNIC` network interfaces for a total of 10 vNICs per instance.

To set up the [Falcon VPC networks](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#overview) to use with your instances, you can either follow the documented instructions or use the provided script.

### Instruction guides

To create the networks, you can use the following instructions: 

  * To create the host networks for the `GVNIC` network interfaces, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

If you are configuring only one `GVNIC` network interface, you can use the default VPC network and the auto subnet that's in the same region as the instance.

  * To create a network for the `IRDMA` network interface, see [Create a VPC network with a Falcon VPC network profile](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma). Use the default value for the [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) for a Falcon VPC network, which is `8896`.




### Script

You can create up to nine gVNIC network interfaces and one IRDMA network interface per instance. Each network interface must attach to a separate network. To create the networks, you can use the following script, which creates two networks for gVNIC and one network for IRDMA. 

  1. Optional: Before running the script, list the Falcon VPC network profiles to verify there is one available. 
         
         gcloud compute network-profiles list
           

  2. Copy the following code and run it in a Linux shell window.
         
         #!/bin/bash
           # Set the number of GVNIC interfaces to create. You can create up to 9.
           NUM_GVNIC=NUMBER_OF_GVNIC
         
           # Create regular VPC networks and subnets for the GVNIC interfaces
             for N in $(seq 0 $(($NUM_GVNIC - 1))); do
               gcloud compute networks create GVNIC_NAME_PREFIX-net-$N \
                   --subnet-mode=custom
         
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
         
           # Optional: Create a firewall rule for the external IP address for the
           #  first GVNIC network interface
           gcloud compute firewall-rules create GVNIC_NAME_PREFIX-allow-ping-net-0 \
               --network=GVNIC_NAME_PREFIX-net-0 \
               --action=ALLOW \
               --rules=icmp \
               --source-ranges=IP_RANGE
         
           # Create a Falcon VPC network for the Cloud RDMA network interface
           gcloud compute networks create RDMA_NAME_PREFIX-irdma \
               --network-profile=ZONE-vpc-falcon \
               --subnet-mode custom
         
           # Create a subnet in the Falcon VPC network
           gcloud compute networks subnets create RDMA_NAME_PREFIX-irdma-sub \
               --network=RDMA_NAME_PREFIX-irdma \
               --region=REGION \
               --range=10.2.0.0/16  # offset to avoid overlap with GVNIC subnet ranges
           

Replace the following:

     * `NUMBER_OF_GVNIC`: the number of GVNIC interfaces to create. Specify a number from 1 to 9.
     * `GVNIC_NAME_PREFIX`: the name prefix to use for the regular VPC network and subnet that uses a GVNIC NIC type.
     * `REGION`: the region where you want to create the networks. This must correspond to the zone specified for the `--network-profile` flag, when creating the Falcon VPC network. For example, if you specify the zone as `europe-west4-b`, then your region is `europe-west4`.
     * `IP_RANGE`: the range of IP addresses outside of the VPC network to use for the [SSH firewall rules](https://docs.cloud.google.com/compute/docs/connect/ssh-best-practices/network-access#use-firewall-policies). As a best practice, specify the specific IP address ranges that you need to allow access from, rather than all IPv4 or IPv6 sources. Don't use `0.0.0.0/0` or `::/0` as a source range because this allows traffic from all IPv4 or IPv6 sources, including sources outside of Google Cloud.
     * `RDMA_NAME_PREFIX`: the name prefix to use for the VPC network and subnet that uses the IRDMA NIC type.
     * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where you want to create the networks and compute instances. Use either `us-central1-a` or `europe-west4-b`.
  3. Optional: To verify that the VPC network resources are created successfully, check the network settings in the Google Cloud console:

     1. In the Google Cloud console, go to the **VPC networks** page. 

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

     2. Search the list for the networks that you created in the previous step.
     3. To view the subnets, firewall rules, and other network settings, click the name of the network.



## Optional: Create a placement policy

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
  * `REGION`: the region where you want to create the compact placement policy. Specify the region that contains the zone where you plan to create instances, and verify that the machine type that you want to use is available in that region. For information about regions, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 



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
  * `REGION`: the region where you want to create the compact placement policy. Specify the region that contains the zone where you plan to create instances, and verify that the machine type that you want to use is available in that region. For information about regions, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 



## Create VM instances in bulk

The instructions in this section describe how to create H4D VMs in bulk.

Review the following limitations before creating H4D instances with Cloud RDMA:

  * You can't use Live migration during host maintenance events with instances that have a Cloud RDMA network interface. You must configure the instance to terminate during maintenance events.
  * The gVNIC network interface can have only one IPv6 address, either internal or external, but not both.
  * You can use only IPv4 addresses with IRDMA network interfaces and Falcon VPC networks.




###  gcloud 

To create VMs in bulk, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

Start with the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). 
    
    
       gcloud compute instances bulk create \
           --name-pattern=NAME_PATTERN \
           --count=COUNT \
           --machine-type=MACHINE_TYPE \
           --image-family=IMAGE_FAMILY \
           --image=project= IMAGE_PROJECT \
           --instance-termination=action=DELETE \
           --maintenance-policy=TERMINATE \
           --region=REGION \
           --boot-disk-type=hyperdisk-balanced \
           --boot-disk-size=DISK_SIZE
       

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern for the instances. For example, using `vm-#` for the name pattern generates instances with names such as `vm-1` and `vm-2`, up to the number specified by the `--count` flag.
     * `COUNT`: the number of instances to create.
     * `MACHINE_TYPE`: the machine type to use for the instances. Use one of the [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types), for example `h4d-highmem-192-lssd`.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use, for example `rocky-linux-9-optimized-gcp`.

For a list of supported OS images, see [Supported operating system](https://docs.cloud.google.com/compute/docs/images/os-details). Choose an OS image version that supports the IRDMA interface. 

     * `IMAGE_PROJECT`: the project ID for the OS image, for example, `rocky-linux-cloud`.
     * `REGION`: specify a region in which the machine type that you want to use is available, for example `europe-west4`. For information about available regions, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 
     * `DISK_SIZE`: Optional: the size of the boot disk in GiB. The value must be a whole number.
  2. Optional: If you chose to use a compact placement policy, include the ` --resource-policies` flag:
         
         --resource-policies=POLICY_NAME
                  

Replace POLICY_NAME with the name of the compact placement policy.

  3. To specify the reservation, do one of the following:

     * If you are using a placement policy or if VMs can be placed anywhere in your reservation block, then add the following flags to the command:
           
           --provisioning-model=RESERVATION_BOUND \
                      --reservation-affinity=specific \
                      --reservation=RESERVATION_NAME \
                      

Replace RESERVATION_NAME with the name of the reservation, for example, `h4d-highmem-exfr-prod`.

     * If you aren't using a compact placement policy and you want the instances placed in a specific block, then add the following flags to the command:
           
           --provisioning-model=RESERVATION_BOUND \
                      --reservation-affinity=specific \
                      --reservation=<RESERVATION_BLOCK_NAME \
                      

Replace RESERVATION_BLOCK_NAME with the name of a block in the reservation, for example, `h4d-highmem-exfr-prod/reservationBlocks/h4d-highmem-exfr-prod-block-1`. 

To view the reservation name or the available reservation blocks, see [View capacity](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#view-capacity). 

  4. Optional: To configure the instances to use Cloud RDMA, add the flags similar to the following to the command. This example configures two GVNIC network interfaces and one IRDMA network interface:
         
         --network-interface=nic-type=GVNIC, \
                     network=GVNIC_NAME_PREFIX-net-0, \
                     subnet=GVNIC_NAME_PREFIX-sub-0, \
                     stack-type=STACK_TYPE, \
                     address=EXTERNAL_IPV4_ADDRESS \
                 --network-interface=nic-type=GVNIC, \
                     network=GVNIC_NAME_PREFIX-net-1, \
                     subnet=GVNIC_NAME_PREFIX-sub-1, no-address \
                 --network-interface=nic-type=IRDMA, \
                     network=RDMA_NAME_PREFIX-irdma, \
                     subnet=RDMA_NAME_PREFIX-irdma-sub, \
                     stack-type=IPV4_ONLY, no-address \
                 

Replace the following:

     * `GVNIC_NAME_PREFIX`: the name prefix you used when creating the VPC network and subnet for the GVNIC interface.

For the first GVNIC network interface, you can omit the `network` and `subnet` flags to use the `default` network instead.

     * `STACK_TYPE`: Optional: the stack type for the GVNIC network interface. `STACK_TYPE` must be one of `IPV4_ONLY`, or `IPV4_IPV6`. The default value is `IPV4_ONLY`. 
     * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following: 
       * Specify a valid IPv4 address from the subnet.
       * Use the flag `no-address` instead if you don't want the network interface to have an external IP address.
       * Specify `address=''` if you want the interface to receive an ephemeral external IP address.

To specify an external IPv6 address, use the flag `--external-ipv6-address` instead.

     * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA interface.
  5. Optional: Add additional flags to customize the rest of the instance properties, as needed.
  6. Run the command.



### Spot

Start with the following [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). 
    
    
       gcloud compute instances bulk create \
           --name-pattern=NAME_PATTERN \
           --count=COUNT \
           --machine-type=MACHINE_TYPE \
           --image-family=IMAGE_FAMILY \
           --image=project= IMAGE_PROJECT \
           --region=REGION \
           --boot-disk-type=hyperdisk-balanced \
           --boot-disk-size=DISK_SIZE \
           --provisioning-model=SPOT \
           --instance-termination=action=TERMINATION_ACTION
       

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern for the instances. For example, using `vm-#` for the name pattern generates instances with names such as `vm-1` and `vm-2`, up to the number specified by the `--count` flag.
     * `COUNT`: the number of instances to create.
     * `MACHINE_TYPE`: the machine type to use for the instances. Use one of the [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types), for example `h4d-highmem-192-lssd`.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use, for example `rocky-linux-9-optimized-gcp`.

For a list of supported OS images, see [Supported operating system](https://docs.cloud.google.com/compute/docs/images/os-details). Choose an OS image version that supports the IRDMA interface. 

     * `IMAGE_PROJECT`: the project ID for the OS image, for example, `rocky-linux-cloud`.
     * `REGION`: specify a region in which the machine type that you want to use is available, for example `europe-west4`. For information about available regions, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 
     * `DISK_SIZE`: Optional: the size of the boot disk in GiB. The value must be a whole number.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, we recommend that you handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME \
               

Replace `POLICY_NAME` with the name of the compact placement policy.

  3. Optional: To configure the instances to use Cloud RDMA, add the flags similar to the following to the command. This example configures two GVNIC network interfaces and one IRDMA network interface:
         
         --network-interface=nic-type=GVNIC, \
                   network=GVNIC_NAME_PREFIX-net-0, \
                   subnet=GVNIC_NAME_PREFIX-sub-0, \
                   stack-type=STACK_TYPE, \
                   address=EXTERNAL_IPV4_ADDRESS \
               --network-interface=nic-type=GVNIC, \
                   network=GVNIC_NAME_PREFIX-net-1, \
                   subnet=GVNIC_NAME_PREFIX-sub-1, no-address \
               --network-interface=nic-type=IRDMA, \
                   network=RDMA_NAME_PREFIX-irdma, \
                   subnet=RDMA_NAME_PREFIX-irdma-sub, \
                   stack-type=IPV4_ONLY, no-address \
               

Replace the following:

     * `GVNIC_NAME_PREFIX`: the name prefix you used when creating the VPC network and subnet for the GVNIC interface.

For the first GVNIC network interface, you can omit the `network` and `subnet` flags to use the `default` network instead.

     * `STACK_TYPE`: Optional: the stack type for the GVNIC network interface. `STACK_TYPE` must be one of `IPV4_ONLY`, or `IPV4_IPV6`. The default value is `IPV4_ONLY`. 
     * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). Do one of the following: 
       * Specify a valid IPv4 address from the subnet.
       * Use the flag `no-address` instead if you don't want the network interface to have an external IP address.
       * Specify `address=''` if you want the interface to receive an ephemeral external IP address.

To specify an external IPv6 address, use the flag `--external-ipv6-address` instead.

     * `RDMA_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the IRDMA interface.
  4. Optional: Add additional flags to customize the rest of the instance properties, as needed.
  5. Run the command.



###  REST 

To create VM instances in bulk, make a `POST` request to the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert)

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters#consumption-and-capacity) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model.

### Reservation-bound

Start with the following `POST` request to the `instances.bulkInsert` method.
    
    
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
        {
          "namePattern":"NAME_PATTERN",
          "count":"COUNT",
          "instanceProperties":{
            "machineType":"MACHINE_TYPE",
            "disks":[
              {
                "boot":true,
                "initializeParams":{
                  "diskSizeGb":"DISK_SIZE",
                  "diskType":"hyperdisk-balanced",
                  "sourceImage":"projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                },
                "mode":"READ_WRITE",
                "type":"PERSISTENT"
              }
            ],
            "scheduling":{
                "provisioningModel":"RESERVATION_BOUND",
                "instanceTerminationAction":"DELETE",
                "onHostMaintenance": "TERMINATE",
                "automaticRestart":true
            }
          }
        }
        

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the instances.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you are using a compact placement policy, then use a zone in the same region as the compact placement policy. For information about the regions where H4D machine types are available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 
     * `NAME_PATTERN`: the name pattern for the instances. For example, using `vm-#` for the name pattern generates instances with names such as `vm-1` and `vm-2`, up to the number specified by the `count` field.
     * `COUNT`: the number of instances to create.
     * `MACHINE_TYPE`: the machine type to use for the instances. Use one of the [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types), for example `h4d-highmem-192-lssd`.
     * `DISK_SIZE`: the size of the boot disk in GiB.
     * `IMAGE_PROJECT`: the project ID for the OS image, for example, `debian-cloud`.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use, for example `rocky-linux-9-optimized-gcp`. For a list of supported OS images, see [Supported operating system](https://docs.cloud.google.com/compute/docs/images/os-details). Choose an OS image version that supports the IRDMA interface. 
  2. Optional: If you chose to use a compact placement policy, include the `resourcePolicies` parameter in the request body as part of the `"instanceProperties"` parameter.
         
         "resourcePolicies": [
                     "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
                   ],
                   

Replace POLICY_NAME with the name of the compact placement policy.

  3. To specify the reservation, do one of the following:

     * If you are using a placement policy or if VMs can be placed anywhere in your reservation block, then add the following to the request body as part of the `"instanceProperties"` parameter:
           
           "reservationAffinity":{
                        "consumeReservationType":"SPECIFIC_RESERVATION",
                        "key":"compute.googleapis.com/reservation-name",
                        "values":[
                          "RESERVATION_NAME"
                        ],
                      },
                      

Replace RESERVATION_NAME with the name of the reservation, for example, `h4d-highmem-exfr-prod`.

     * If you aren't using a compact placement policy or you want the instances placed in a specific block, then add the following to the request body as part of the `"instanceProperties"` parameter:
           
           "reservationAffinity":{
                         "consumeReservationType":"SPECIFIC_RESERVATION",
                         "key":"compute.googleapis.com/reservation-name",
                         "values":[
                           "RESERVATION_BLOCK_NAME"
                         ],
                       },
                      

Replace RESERVATION_BLOCK_NAME with the name of a block in the reservation, for example, `h4d-highmem-exfr-prod/reservationBlocks/h4d-highmem-exfr-prod-block-1`. 

To view the reservation name or the available reservation blocks, see [View capacity](https://docs.cloud.google.com/compute/docs/hpc/view-reserved-capacity#view-capacity). 

  4. If you want to configure the instances to use Cloud RDMA, then include a parameter block similar to the following to the request body as part of the `"instanceProperties"` parameter. This example configures two GVNIC network interfaces and one IRDMA network interface:
         
         "networkInterfaces": [
                   {
                     "network": "GVNIC_NAME_PREFIX-net-0",
                     "subnetwork": "GVNIC_NAME_PREFIX-sub-0",
                     "accessConfigs": [
                        {
                           "type": "ONE_TO_ONE_NAT",
                           "name": "External IP",
                           "natIP": "EXTERNAL_IPV4_ADDRESS"
                        }
                     ],
                     "stackType": "IPV4_ONLY",
                     "nicType": "GVNIC",
                   },
                   {
                     "network": "GVNIC_NAME_PREFIX-net-1",
                     "subnetwork": "GVNIC_NAME_PREFIX-sub-1",
                     "stackType": "IPV4_ONLY",
                     "nicType": "GVNIC",
                   },
                   {
                     "network": "RDMA_NAME_PREFIX-irdma",
                     "subnetwork": "RDMA_NAME_PREFIX-irdma-sub",
                     "stackType": "IPV4_ONLY",
                     "nicType": "IRDMA",
                   }
                 ],
                  

Replace the following:

     * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the GVNIC interface.

For the GVNIC network interface, you can omit the `network` and `subnetwork` fields to use the `default` network instead.

     * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). 
     * `RDMA_NAME_PREFIX`: the name prefix you used when creating the VPC network and subnet for the IRDMA interface.
  5. Optional: Customize the rest of the instance properties, as needed.
  6. Submit the request.



### Spot

Start with the following `POST` request to the `instances.bulkInsert` method.
    
    
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/bulkInsert
        {
          "namePattern":"NAME_PATTERN",
          "count":"COUNT",
          "instanceProperties":{
            "machineType":"MACHINE_TYPE",
            "disks":[
              {
                "boot":true,
                "initializeParams":{
                  "diskSizeGb":"DISK_SIZE",
                  "diskType":"hyperdisk-balanced",
                  "sourceImage":"projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
                },
                "mode":"READ_WRITE",
                "type":"PERSISTENT"
              }
            ],
            "scheduling":{
                "provisioningModel":"SPOT",
                "instanceTerminationAction":"TERMINATION_ACTION"
            }
          }
        }
        

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the instances.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you are using a compact placement policy, then use a zone in the same region as the compact placement policy. For information about the regions where H4D machine types are available, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 
     * `NAME_PATTERN`: the name pattern for the instances. For example, using `vm-#` for the name pattern generates instances with names such as `vm-1` and `vm-2`, up to the number specified by the `count` field.
     * `COUNT`: the number of instances to create.
     * `MACHINE_TYPE`: the machine type to use for the instances. Use one of the [H4D machine types](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types), for example `h4d-highmem-192-lssd`.
     * `DISK_SIZE`: the size of the boot disk in GiB.
     * `IMAGE_PROJECT`: the project ID for the OS image, for example, `debian-cloud`.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use, for example `rocky-linux-9-optimized-gcp`. For a list of supported OS images, see [Supported operating system](https://docs.cloud.google.com/compute/docs/images/os-details). Choose an OS image version that supports the IRDMA interface. 
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, we recommend that you handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, include the `resourcePolicies` parameter as part of the `"instanceProperties"` parameter.
         
         "resourcePolicies": [
                     "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
                   ]
                   

  3. If you want to configure the instances to use Cloud RDMA, then include a parameter block similar to the following to the request body as part of the `"instanceProperties"` parameter. This example configures two GVNIC network interfaces and one IRDMA network interface:
         
         "networkInterfaces": [
                   {
                     "network": "GVNIC_NAME_PREFIX-net-0",
                     "subnetwork": "GVNIC_NAME_PREFIX-sub-0",
                     "accessConfigs": [
                        {
                           "type": "ONE_TO_ONE_NAT",
                           "name": "External IP",
                           "natIP": "EXTERNAL_IPV4_ADDRESS"
                        }
                     ],
                     "stackType": "IPV4_ONLY",
                     "nicType": "GVNIC",
                   },
                   {
                     "network": "GVNIC_NAME_PREFIX-net-1",
                     "subnetwork": "GVNIC_NAME_PREFIX-sub-1",
                     "stackType": "IPV4_ONLY",
                     "nicType": "GVNIC",
                   },
                   {
                     "network": "RDMA_NAME_PREFIX-irdma",
                     "subnetwork": "RDMA_NAME_PREFIX-irdma-sub",
                     "stackType": "IPV4_ONLY",
                     "nicType": "IRDMA",
                   }
                 ],
                  

Replace the following:

     * `GVNIC_NAME_PREFIX`: the name prefix that you used when creating the VPC network and subnet for the GVNIC interface.

For the GVNIC network interface, you can omit the `network` and `subnetwork` fields to use the `default` network instead.

     * `EXTERNAL_IPV4_ADDRESS`: Optional: a static external IPv4 address to use with the network interface. You must have previously [reserved an external IPv4 address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address). 
     * `RDMA_NAME_PREFIX`: the name prefix you used when creating the VPC network and subnet for the IRDMA interface.
  4. Optional: Customize the rest of the instance properties, as needed.
  5. Submit the request.



## What's next

  * [View H4D cluster topology](https://docs.cloud.google.com/compute/docs/hpc/view-h4d-topology).
  * [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).
  * [Set up and scale MPI applications on H4D VMs with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
