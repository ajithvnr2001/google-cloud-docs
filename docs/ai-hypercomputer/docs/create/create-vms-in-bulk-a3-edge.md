---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-edge/
title: Create AI-optimized instances in bulk with A3 Edge \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:01.597289+00:00
---

# Create AI-optimized instances in bulk with A3 Edge  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-edge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create AI-optimized instances in bulk with A3 Edge Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document explains how to create virtual machine (VM) instances in bulk that use A3 Edge accelerator-optimized machine types. To learn more about the machine type, see [A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) in the Compute Engine documentation.

For more information about creating VMs in bulk, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation) in the Compute Engine documentation.

To learn about other ways to create VMs or clusters, see the [Overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) page.

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

Creating instances in bulk with the A3 Edge machine type includes the following steps:

  1. Create VPC networks
  2. Optional: Create a compact placement policy
  3. Create instances in bulk
  4. Install GPU drivers



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

A3 Edge requires four data networks. Use the following command to create four data networks, each with subnets and firewall rules.
    
    
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
    

### Optional: Create a compact placement policy

**Tip:** Decide whether to create a compact placement policy as follows:

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



### Create A3 Edge VMs in bulk

To create A3 Edge VMs in bulk, use one of the following methods.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create an A3 Edge VM, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).

To create instances in bulk, use the [ `gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances bulk create \
        --name-pattern=NAME_PATTERN \
        --count=COUNT \
         --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --region=REGION \
        --boot-disk-type=DISK_TYPE \
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
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --restart-on-failure
    

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern to use for the A3 Edge instances. For example, using `instance-#` for the name pattern generates A3 Edge instances with names such as `instance-1` and `instance-2`, up to the number of A3 Edge instances specified by `--count`.
     * `COUNT`: the number of A3 Edge instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A3 Edge instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
       * To create instances across blocks or on a single block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, apply a compact placement policy that specifies a block collocation (`maxDistance=2`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

       * To create instances on a specific block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A3 Edge instance at the end of the reservation period. 

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
        --boot-disk-type=DISK_TYPE \
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
    

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern to use for the A3 Edge instances. For example, using `instance-#` for the name pattern generates A3 Edge instances with names such as `instance-1` and `instance-2`, up to the number of A3 Edge instances specified by `--count`.
     * `COUNT`: the number of A3 Edge instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A3 Edge instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Run the command.



###  REST 

To create A3 Edge VMs, use the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

To create instances in bulk, make a `POST` request to the [ `instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

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
              "diskType": "DISK_TYPE",
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

     * `PROJECT_ID`: the project ID of the project where you want to create the A3 Edge instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the A3 Edge instances. For example, using `instance-#` for the name pattern generates A3 Edge instances with names such as `instance-1` and `instance-2`, up to the number of A3 Edge instances specified by `--count`.
     * `COUNT`: the number of A3 Edge instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A3 Edge instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `REGION`: the region of the subnetwork.
     * `RESERVATION`: either the reservation name or a specific block within a reservation. To get the reservation name or the available blocks, see [View reserved capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/view-reserved-capacity). Based on your requirement for instance placement, choose one of the following: 
       * To create instances across blocks or on a single block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME

Additionally, for a single block, apply a compact placement policy that specifies a block collocation (`maxDistance=2`) . Compute Engine then applies the policy to the reservation and creates instances on the same block.

       * To create instances on a specific block:
             
             projects/RESERVATION_OWNER_PROJECT_ID/reservations/RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME

**Tip:** If the reservation exists in the current project, then you can omit `projects/RESERVATION_OWNER_PROJECT_ID/reservations/` from the `RESERVATION` value. 
     * `TERMINATION_ACTION`: whether Compute Engine stops (`STOP`) or deletes (`DELETE`) the A3 Edge instance at the end of the reservation period. 

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
              "diskType": "DISK_TYPE",
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

     * `PROJECT_ID`: the project ID of the project where you want to create the A3 Edge instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the A3 Edge instances. For example, using `instance-#` for the name pattern generates A3 Edge instances with names such as `instance-1` and `instance-2`, up to the number of A3 Edge instances specified by `--count`.
     * `COUNT`: the number of A3 Edge instances to create.
     * `MACHINE_TYPE`: the machine type to use for the A3 Edge instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNIC NICs.
     * `REGION`: the region of the subnetwork.
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

## What's next

  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [View the topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)
  * [Run workloads overview](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
