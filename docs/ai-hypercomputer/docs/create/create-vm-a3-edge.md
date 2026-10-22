---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-edge/
title: Create an AI-optimized instance with A3 Edge \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:50.644119+00:00
---

# Create an AI-optimized instance with A3 Edge  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-edge/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized instance with A3 Edge Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes the steps to create standalone virtual machine (VM) instances that use A3 Edge accelerator-optimized machine types. To learn more about the machine types, see [A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#a3-edge).

To learn about other ways to create VMs or clusters, see the [Overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) page. 

## Limitations

When you create a standalone A3 Edge VM, the following limitations apply:

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Edge machine type.
  * You can only use an A3 Edge machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Edge machine type.
  * The A3 Edge machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Edge machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Edge machine type.
  * A3 Edge machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).

If you want to use a compact placement policy, then review the [restrictions for placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions). 

## Before you begin

Before creating VMs, if you haven't already done so, complete the following steps:

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

To get the permissions that you need to create VMs, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VMs:

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

Creating an instance with the A3 Edge machine type includes the following steps:

  1. Create VPC networks
  2. Optional: Create a compact placement policy
  3. Create an instance
  4. Install GPU drivers
  5. Optional: Enable NVIDIA Multi-Instance GPU mode



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

  * If you only need one VM for your workload, then skip this step.
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



### Create an A3 Edge VM

To create an A3 Edge VM, use one of the following methods.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  Console 

**Important:** If you choose to use a compact placement policy, then you must use Google Cloud CLI or REST to create the VM. 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify a **Name** for your VM. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  3. Select the **Region** and **Zone** where you want to create a VM. See the list of available [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  4. Click the **GPUs** tab, and then complete the following steps:

     1. In the **GPU type** list, select `NVIDIA H100 80GB`.
     2. In the **Number of GPUs** list, select `8`.
     3. In the **Machine type** list, select a **a3-edgegpu-8g**.
  5. Based on the consumption option that you want to use, select one of the following options and complete the following steps.

###  Reservation 

A3 Edge instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

     * On-demand reservations
     * Standard future reservations

To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

     1. In the **Provisioning model** section, in the **VM provisioning model** list, select **Standard**. (This option is selected by default.)
     2. To configure which reservations this VM uses, complete the following steps:

        1. In the navigation menu, click **Advanced**.
        2. For **Reservations** , select one of the following options:

           * To optionally use reservation capacity, select **Use automatic selection**. (This option is selected by default.)

The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Caution:** When matching reservation capacity is unavailable, the instance uses the on-demand consumption option instead, which has different billing and capacity assurance. For more information, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). 

           * To require reservation capacity, select **Choose a reservation** , and then click **Choose reservation** to specify which reservation to use.

The instance is required to use capacity from a [_specifically targeted_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) and isn't allowed to use on-demand capacity. If reservation capacity is unavailable, then the instance creation fails.

###  On-demand 

     1. In the **Provisioning model** section, in the **VM provisioning model** list, select **Standard**. (This option is selected by default.)
     2. Optional: To configure whether or not this VM uses reservations, complete the following steps:

        1. In the navigation menu, click **Advanced**.
        2. For **Reservations** , select one of the following options:

           * To optionally use reservation capacity, select **Use automatic selection**. (This is the default.)

The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 

           * To require on-demand capacity, select **Don't use a reservation**.

The instance is blocked from using any reservation capacity.

###  Flex-start 

     1. In the **Provisioning model** section, in the **VM provisioning model** list, select **Flex-start**.
     2. In the **Enter number of hours** field, enter the maximum amount of time that you want the VM to run. The value must be between 46 seconds (`0.01`) and seven days (`168`, or 168 hours).

     3. Select **Set a wait time for VM creation**.

Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

        * **Workloads with strict zonal requirements** : if your workload requires you to create the VM in a specific zone, then specify a duration between **90 seconds** and **2 hours**. Longer durations give you higher chances of obtaining resources. 
        * **Workloads without strict zonal requirements** : if the VM can run in any zone within the region, then specify a duration of **0 seconds** or clear the **Set a wait time for VM creation** checkbox. This action specifies that Compute Engine only allocates resources if they are immediately available. If the VM creation request fails because resources are unavailable, then retry the request in a different zone. 
     4. In the **On VM termination** field, select whether to stop or delete the VM at the end of its run duration:

        * To delete the VM, select **Delete**.
        * To stop the VM, select **Stop**.

###  Spot 

     1. In the **Provisioning model** section, select **Spot** from the **VM provisioning model** list.
     2. Optional: To select the [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) that happens when Compute Engine preempts the VM, complete the following steps:

        1. Expand the **VM provisioning model advanced settings** section.
        2. In the **On VM termination** list, select one of the following options: 
           * To stop the VM during preemption, select **Stop** (default).
           * To delete the VM during preemption, select **Delete**.

  6. In the navigation menu, click **OS and storage** , and then complete the following steps:

     1. Click **Change**. The **Boot disk configuration** pane opens.
     2. On the **Public images** tab, select a recommended image. For a list of recommended images, see [Operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).

**Tip:** We recommend using [accelerator OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images) for AI-optimized workloads. Unless you have unique GPU driver requirements, these images install all required GPU drivers automatically. For more information about GPU driver requirements, see Install GPU drivers in this document. 

     3. Optional: To configure the boot disk size, see either the [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.

     4. To confirm your boot disk options, click **Select**.

  7. Configure the service account and access scopes as follows. Workloads running on the instance use the attached service account to authorize requests to other Google Cloud services.

     1. In the navigation menu, click **Security**.
     2. In the **Service account** list, select a service account to use.
     3. For **Access scopes** , select the **Allow full access to all Cloud APIs** option. This best practice is recommended because it lets you manage access by adding or removing IAM roles from the service account. For more information, see [Attaching a service account to an instance](https://docs.cloud.google.com/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance).
  8. To create a multi-NIC VM, complete the following steps. Otherwise, to create a single-NIC VM, skip these steps.

     1. In the navigation menu, click **Networking**.

     2. In the **Network interfaces** section, complete the following steps:

        1. Delete the default network interface. To delete the interface, click delete **Delete**.
        2. Click **Add a network interface**. Use this option to add network interfaces that attach to the VPC networks that you created in the previous section. When you add the network interfaces, remember the following: 
           * For a network interface that is used for host to host communication, select a regular VPC network and subnet from the **Network** and **Subnetwork** lists, and set the **Network interface card** list to **gVNIC**. For each network except the first, set the **External IP address** list to **None**.
           * For a network interface that is used for GPU to GPU communication by using GPUDirect-TCPX, select the corresponding specialized VPC networks and subnets for each interface, and set the **Network interface card** list to **gVNIC** for these network interfaces as well. For each network except the first, set the **External IP address** list to **None**.
  9. To create and start the VM, click **Create**.




###  gcloud 

To create the VM, use the [ `gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

A3 Edge instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * On-demand reservations
  * Standard future reservations



To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=DISK_TYPE \
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

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
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

  3. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  4. Run the command.



### On-demand

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=DISK_TYPE \
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

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`any` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
       * **`none` (On-demand capacity is required)**: Block the instance from using any reservation capacity.

  2. By default, the instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. If you want to disable automatic restart, then add the following flag:
         
         --no-restart-on-failure

  3. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  4. Run the command.



### Flex-start

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instances create INSTANCE_NAME  \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --boot-disk-type=DISK_TYPE \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-0,subnet=GVNIC_NAME_PREFIX-sub-0 \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-1,subnet=GVNIC_NAME_PREFIX-sub-1,no-address 
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-2,subnet=GVNIC_NAME_PREFIX-sub-2,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-3,subnet=GVNIC_NAME_PREFIX-sub-3,no-address \
        --network-interface=nic-type=GVNIC,network=GVNIC_NAME_PREFIX-net-4,subnet=GVNIC_NAME_PREFIX-sub-4,no-address \
        --provisioning-model=FLEX_START \
        --request-valid-for-duration=REQUEST_VALID_FOR_DURATION \
        --max-run-duration=MAX_RUN_DURATION \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
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

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `IMAGE_PROJECT`: the project ID of the OS image. For example, use `cos-cloud` for the `cos-121-lts` or later Container-Optimized OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
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

A3 Edge instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * On-demand reservations
  * Standard future reservations



To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

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
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the VM.
     * `ZONE`: the zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `INSTANCE_NAME`: the name of the VM.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
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
  2. Optional: If you chose to use a compact placement policy, then add the following field to the request body:
         
         "resourcePolicies": [
             "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
           ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Submit the request.



### On-demand

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
      "scheduling": {
        "provisioningModel": "STANDARD",
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": AUTOMATIC_RESTART
      },
      "reservationAffinity": {
        "consumeReservationType": "RESERVATION_AFFINITY"
      }
    }
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the VM.
     * `ZONE`: the zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `INSTANCE_NAME`: the name of the VM.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `REGION`: the region of the subnetwork.
     * `AUTOMATIC_RESTART`: if your instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. Specify either `true` to enable automatic restart (default) or `false` to disable automatic restart.

     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`ANY_RESERVATION` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
       * **`NO_RESERVATION` (On-demand capacity is required)**: Block the instance from using any reservation capacity.

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
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `REGION`: the region of the subnetwork.
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
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the VM.
     * `ZONE`: the zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `INSTANCE_NAME`: the name of the VM.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `DISK_TYPE`: the type of the boot disk. For this machine series, we recommend that you use `hyperdisk-balanced`. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). For the A3 Edge machine series, we strongly recommend that you use the `cos-121-lts` or later Container-Optimized OS image and [disable automatic updates](https://docs.cloud.google.com/container-optimized-os/docs/concepts/auto-update). 
     * `NETWORK_PROJECT_ID`: the project ID of the network.
     * `GVNIC_NAME_PREFIX`: the name prefix that you specified when creating the standard VPC networks and subnets that use gVNICs.
     * `REGION`: the region of the subnetwork.
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



### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. If you didn't specify an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation. 

### Optional: Enable NVIDIA Multi-Instance GPU mode

Multi-Instance GPU (MIG) mode is a feature that you can enable for a [supported NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html). After you create an instance, you can enable MIG mode on a single GPU that is attached to your machine. With MIG mode enabled, the single GPU is partitioned into as many as seven independent GPU instances. Each instance runs simultaneously, each with its own memory, cache, and streaming multiprocessors. You can then run different workloads on these GPU instances in parallel. For more information about using MIG mode, see the [Multi-Instance GPU (MIG) User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#getting-started-with-mig) in the NVIDIA documentation. 

## What's next

  * [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
