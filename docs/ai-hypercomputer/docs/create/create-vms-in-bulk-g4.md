---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-g4/
title: Create AI-optimized G4 VMs in bulk \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:43.324162+00:00
---

# Create AI-optimized G4 VMs in bulk  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-g4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create AI-optimized G4 VMs in bulk Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document explains how to create virtual machine (VM) instances in bulk that use the G4 machine series. To learn more about these accelerator-optimized machine types, see [G4 series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g4).

For more information about creating VMs in bulk, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation) in the Compute Engine documentation.

To learn about other ways to create VMs or clusters, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

## Limitations

When you create G4 VMs in bulk, the following limitations apply:

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use a G4 machine type.
  * You can only use a G4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) (regional or zonal) on an instance that uses a G4 machine type.
  * The G4 machine type is only available on the [AMD EPYC Turin 5th Generation platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_processors).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with the `g4-standard-48` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1). All the [limitations for Confidential VM running on the G4 machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.
  * You can't use Windows operating systems on `g4-standard-384` instances.
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to G4 machine types.
  * When creating G4 instances that have less than one GPU attached (fractional GPUs), don't use the `--no-service-account` or `--no-scopes` flags. To authenticate NVIDIA vGPU drivers, Compute Engine must [verify the VM's identity](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity). This process requires that service accounts are enabled.

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

Creating instances in bulk with the G4 machine type includes the following steps:

  1. Optional: Create a compact placement policy
  2. Create instances in bulk
  3. Install GPU drivers
  4. Optional: Enable NVIDIA Multi-Instance GPU mode



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



### Create G4 VMs in bulk

To create G4 VMs in bulk, use one of the following methods.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create instances in bulk, use the [ `gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

G4 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * On-demand reservations
  * Standard future reservations



To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

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
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY \
        --reservation=RESERVATION
    

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern to use for the G4 instances. For example, using `instance-#` for the name pattern generates G4 instances with names such as `instance-1` and `instance-2`, up to the number of G4 instances specified by `--count`.
     * `COUNT`: the number of G4 instances to create.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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

  3. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  4. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  5. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-rtx-pro-6000-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  6. Run the command.



### On-demand

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
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY
    

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern to use for the G4 instances. For example, using `instance-#` for the name pattern generates G4 instances with names such as `instance-1` and `instance-2`, up to the number of G4 instances specified by `--count`.
     * `COUNT`: the number of G4 instances to create.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`any` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
       * **`none` (On-demand capacity is required)**: Block the instance from using any reservation capacity.

  2. By default, the instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. If you want to disable automatic restart, then add the following flag:
         
         --no-restart-on-failure

  3. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  4. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  5. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-rtx-pro-6000-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  6. Run the command.



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
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --no-restart-on-failure
    

Complete the following steps:

  1. Replace the following:

     * `NAME_PATTERN`: the name pattern to use for the G4 instances. For example, using `instance-#` for the name pattern generates G4 instances with names such as `instance-1` and `instance-2`, up to the number of G4 instances specified by `--count`.
     * `COUNT`: the number of G4 instances to create.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: specify a region in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: If you chose to use a compact placement policy, then add the following flag to the command:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  4. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-rtx-pro-6000-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Run the command.



###  REST 

To create instances in bulk, make a `POST` request to the [ `instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

G4 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * On-demand reservations
  * Standard future reservations



To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

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
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the G4 instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the G4 instances. For example, using `instance-#` for the name pattern generates G4 instances with names such as `instance-1` and `instance-2`, up to the number of G4 instances specified by `--count`.
     * `COUNT`: the number of G4 instances to create.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
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
  2. Optional: If you chose to use a compact placement policy, then add the following `instanceProperties` subfield to the request body:
         
         "resourcePolicies": [
               "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
             ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         {
                "type": "SCRATCH",
                "initializeParams": {
                   "diskType": "zones/ZONE/diskTypes/local-ssd"
                },
                "autoDelete": true,
                "interface": "INTERFACE_TYPE"
             }
         

Replace the following:

     * `ZONE`: your specified zone.
     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  4. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following field.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         "guestAccelerators":
           [
             {
               "acceleratorCount": VWS_ACCELERATOR_COUNT,
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-rtx-pro-6000-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



### On-demand

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
    

Complete the following steps:

  1. Replace the following:

     * `PROJECT_ID`: the project ID of the project where you want to create the G4 instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the G4 instances. For example, using `instance-#` for the name pattern generates G4 instances with names such as `instance-1` and `instance-2`, up to the number of G4 instances specified by `--count`.
     * `COUNT`: the number of G4 instances to create.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `AUTOMATIC_RESTART`: if your instance automatically restarts if it crashes or Compute Engine stops it for a programmed stop, such as a maintenance event. Specify either `true` to enable automatic restart (default) or `false` to disable automatic restart.

     * `RESERVATION_AFFINITY`: which reservations the instance is allowed to consume, if possible. Specify one of the following:

       * **`ANY_RESERVATION` (Reservation capacity is optional)**: this is the default option. The instance tries to use capacity from an [_automatically consumed_ reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type), which only happens if matching reservation capacity is available. Otherwise, the instance uses on-demand capacity.

**Note:** If you want using reservation capacity to be _required_ , then follow the _Reservation_ steps instead. 
       * **`NO_RESERVATION` (On-demand capacity is required)**: Block the instance from using any reservation capacity.

  2. Optional: If you chose to use a compact placement policy, then add the following `instanceProperties` subfield to the request body:
         
         "resourcePolicies": [
               "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
             ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         {
                "type": "SCRATCH",
                "initializeParams": {
                   "diskType": "zones/ZONE/diskTypes/local-ssd"
                },
                "autoDelete": true,
                "interface": "INTERFACE_TYPE"
             }
         

Replace the following:

     * `ZONE`: your specified zone.
     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  4. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following field.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         "guestAccelerators":
           [
             {
               "acceleratorCount": VWS_ACCELERATOR_COUNT,
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-rtx-pro-6000-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



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

     * `PROJECT_ID`: the project ID of the project where you want to create the G4 instance.
     * `ZONE`: specify a zone in which the machine type that you want to use is available. If you want to specify a compact placement policy, then you must use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
     * `NAME_PATTERN`: the name pattern to use for the G4 instances. For example, using `instance-#` for the name pattern generates G4 instances with names such as `instance-1` and `instance-2`, up to the number of G4 instances specified by `--count`.
     * `COUNT`: the number of G4 instances to create.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
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
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         {
                "type": "SCRATCH",
                "initializeParams": {
                   "diskType": "zones/ZONE/diskTypes/local-ssd"
                },
                "autoDelete": true,
                "interface": "INTERFACE_TYPE"
             }
         

Replace the following:

     * `ZONE`: your specified zone.
     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  4. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following field.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         "guestAccelerators":
           [
             {
               "acceleratorCount": VWS_ACCELERATOR_COUNT,
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-rtx-pro-6000-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



For more information about the configuration options when creating VMs in bulk, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk) in the Compute Engine documentation.

### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. The driver that you need to install depends on whether the instance has fractional GPUs or enabled [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). Use one of the following options: 

  * If you specified a machine type with fractional GPUs, such as `g4-standard-6`, `g4-standard-12`, or `g4-standard-24`, then see [Install vGPU drivers (fractional GPUs)](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#fractional-vms) in the Compute Engine documentation.
  * If you enabled vWS, then see [Install drivers for NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers) in the Compute Engine documentation.
  * Otherwise, use the default GPU drivers as follows:

    * If you specified an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then no action is required.
    * If the OS image doesn't include GPU drivers, then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation.



### Optional: Enable NVIDIA Multi-Instance GPU mode

Multi-Instance GPU (MIG) mode is a feature that you can enable for a [supported NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html). After you create an instance, you can enable MIG mode on a single GPU that is attached to your machine. With MIG mode enabled, the single GPU is partitioned into as many as seven independent GPU instances. Each instance runs simultaneously, each with its own memory, cache, and streaming multiprocessors. You can then run different workloads on these GPU instances in parallel. MIG mode is distinct from using G4 machine types that have fractional GPUs attached, where multiple workloads share access to a single physical GPU through fractional (vGPUs) partitioning. For more information about using MIG mode, see the [Multi-Instance GPU (MIG) User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#getting-started-with-mig) in the NVIDIA documentation. 

## What's next

  * [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * [Get a list of VMs](https://docs.cloud.google.com/compute/docs/instances/get-list)
  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
