---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-g4/
title: Create an AI-optimized G4 MIG \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:59.482558+00:00
---

# Create an AI-optimized G4 MIG  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-g4/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized G4 MIG Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document describes how to create a managed instance group (MIG) that uses G4 machine types. To learn more about these accelerator-optimized machine types, see [G4 series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g4).

Creating a MIG lets you manage multiple virtual machines (VMs) as a single entity. Each VM in a MIG is based on an instance template. By automatically managing the VMs in the group, MIGs offer high availability and scalability. To learn more about MIGs, see [Managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) in the Compute Engine documentation.

To learn about other ways to create VMs or clusters, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

## Limitations

When you create a MIG with G4 VMs, consider the limitations for both the machine type and the MIG.

### Limitations for G4 VMs

When you create G4 VMs, the following limitations apply:

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use a G4 machine type.
  * You can only use a G4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) (regional or zonal) on an instance that uses a G4 machine type.
  * The G4 machine type is only available on the [AMD EPYC Turin 5th Generation platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_processors).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with the `g4-standard-48` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1). All the [limitations for Confidential VM running on the G4 machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.
  * You can't use Windows operating systems on `g4-standard-384` instances.
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to G4 machine types.
  * When creating G4 instances that have less than one GPU attached (fractional GPUs), don't use the `--no-service-account` or `--no-scopes` flags. To authenticate NVIDIA vGPU drivers, Compute Engine must [verify the VM's identity](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity). This process requires that service accounts are enabled.



### Limitations for the MIG

  * You can't use placement policies and resize requests together. For each MIG, choose if you want to use one or neither of the following features:

    * If you want to reduce latency by collocating VMs, then use a compact placement policy in the instance template.
    * If you want to create VMs all at one time, want a higher probability of obtainability, and chose a supported consumption option, then use resize requests for the MIG.


  * If you want to use a compact placement policy, then review the [restrictions for placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#restrictions).


  * If you want to use resize requests, then review the [limitations for resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig#limitations).



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

Creating a MIG with the G4 machine type includes the following steps:

  1. Optional: Create a compact placement policy
  2. Create an instance template
  3. Create a MIG
  4. Install GPU drivers
  5. Optional: Enable NVIDIA Multi-Instance GPU mode



For each MIG, you must choose if you want to use a compact placement policy, use resize requests, or neither. For more information about when to use each option, see Limitations for the MIG in this document.

### Optional: Create a compact placement policy

**Tip:** Decide whether to create a compact placement policy as follows:

  * If you want to use Flex-start VMs, then skip this step.
  * If you want to use resize requests, then skip this step. For more information about when to use each option, see Limitations for the MIG in this document.
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



### Create an instance template

Specify the VM properties for a MIG by creating an instance template.

To create an instance template, select one of the following options:

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  gcloud 

To create a regional instance template, use the [ `gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

G4 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * On-demand reservations
  * Standard future reservations



To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY \
        --reservation=RESERVATION
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
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

  5. Run the command.



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
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
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

  5. Run the command.



### Flex-start

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --instance-termination-action=DELETE \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE \
        --provisioning-model=FLEX_START
    
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `RUN_DURATION`: the duration you want the requested VMs to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days. 
  2. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation. Specifically, G4 machine types use [Titanium SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local_ssd_types).
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  3. Run the command.



### Spot

Before you run the command, review all of the following steps to determine whether to include additional flags.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --instance-template-region=REGION \
        --boot-disk-type=hyperdisk-balanced \
        --boot-disk-size=DISK_SIZE \
        --scopes=cloud-platform \
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --no-restart-on-failure
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
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

To create a regional instance template, make a `POST` request to the [ `regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

G4 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

  * On-demand reservations
  * Standard future reservations



To consume these types of reservations, an instance must use the _standard provisioning model_. For example, use the following creation parameters.

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
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

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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



### Flex-start

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
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
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `RUN_DURATION`: the duration, in seconds, you want the requested VMs to run. The value must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).
  2. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

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

  3. Submit the request.



### Spot

Before you submit the request, review all of the following steps to determine whether to include additional fields.
    
    
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

     * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.
     * `MACHINE_TYPE`: the machine type to use for the G4 instance. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `REGION`: the region where you want to create the instance template. Specify a region in which the machine type that you want to use is available. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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

Create a zonal or regional MIG as follows:

  * To create a zonal MIG, use the following command: 
        
        gcloud compute instance-groups managed create MIG_NAME \
          --template=INSTANCE_TEMPLATE_URL \
          --size=TARGET_SIZE \
          --zone=ZONE
        

  * To create a regional MIG, use the following command: 
        
        gcloud compute instance-groups managed create MIG_NAME \
            --template=INSTANCE_TEMPLATE_URL \
            --size=TARGET_SIZE \
            --region=REGION
        


Replace the following: 
  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `TARGET_SIZE`: the number of instances that you want in the MIG. 
  * `ZONE`: the zone in which you want to create the MIG. 
  * `REGION`: the region in which you want to create the MIG. For a regional MIG, instead of a region, you can specify the zones in that region by using the `--zones` flag.



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
          "targetSize": TARGET_SIZE
        }
        

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert). 
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
          {
            "name": "MIG_NAME",
            "instanceTemplate": "INSTANCE_TEMPLATE_URL",
            "targetSize": TARGET_SIZE
          }
        


Replace the following: 
  * `PROJECT_ID`: the project ID.
  * `ZONE`: the zone in which you want to create the MIG. 
  * `REGION`: the region in which you want to create the MIG. 
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `MIG_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of instances that you want in the MIG. 



#### Create a MIG and a resize request

**Preview — Resize request creation by specifying VM names**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you require multiple VMs all at once to start a job, then create a MIG, and create a [resize request](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig) in the MIG as described in this section.

To create a resize request in a MIG, select one of the following options:

###  gcloud 

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option's provisioning model. 

### Reservation

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
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
               --zones=ZONE \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




### On-demand

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
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
           
               --region=REGION \
               --target-distribution-shape=any-single-zone \
               --instance-redistribution-type=none
             

    2. Create a resize request in the regional MIG using the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create) as follows. This command specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           gcloud compute instance-groups managed resize-requests create MIG_NAME \
               --resize-request=RESIZE_REQUEST_NAME \
               --resize-by=COUNT \
               --region=REGION
           




### Spot

Create a zonal or regional MIG and a resize request as follows:

  * To create a zonal MIG and a resize request in it, do the following:

    1. Create a zonal MIG using the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows.
           
           gcloud compute instance-groups managed create MIG_NAME \
               --template=INSTANCE_TEMPLATE_URL \
               --size=0 \
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
             "targetSize": 0
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
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




### On-demand

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
             "targetSize": 0
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
             }
           }
           

    2. Create a resize request in the regional MIG by making a `POST` request to the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert) as follows. This request specifies the number of VMs that you want to create. If your workload requires specific VM names, then create a resize request by specifying a list of VM names. 
           
           POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
           {
             "name": "RESIZE_REQUEST_NAME",
             "resizeBy": COUNT
           }
           




### Spot

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
             "targetSize": 0
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

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. The driver that you need to install depends on whether the instance has fractional GPUs or enabled [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). Use one of the following options: 

  * If you specified a machine type with fractional GPUs, such as `g4-standard-6`, `g4-standard-12`, or `g4-standard-24`, then see [Install vGPU drivers (fractional GPUs)](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#fractional-vms) in the Compute Engine documentation.
  * If you enabled vWS, then see [Install drivers for NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers) in the Compute Engine documentation.
  * Otherwise, use the default GPU drivers as follows:

    * If you specified an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then no action is required.
    * If the OS image doesn't include GPU drivers, then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation.



### Optional: Enable NVIDIA Multi-Instance GPU mode

**Note:** In this section, _MIG_ refers to Multi-Instance GPU from NVIDIA, not a managed instance group.  Multi-Instance GPU (MIG) mode is a feature that you can enable for a [supported NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/supported-gpus.html). After you create an instance, you can enable MIG mode on a single GPU that is attached to your machine. With MIG mode enabled, the single GPU is partitioned into as many as seven independent GPU instances. Each instance runs simultaneously, each with its own memory, cache, and streaming multiprocessors. You can then run different workloads on these GPU instances in parallel. MIG mode is distinct from using G4 machine types that have fractional GPUs attached, where multiple workloads share access to a single physical GPU through fractional (vGPUs) partitioning. For more information about using MIG mode, see the [Multi-Instance GPU (MIG) User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#getting-started-with-mig) in the NVIDIA documentation. 

## What's next?

  * [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * [View information about MIGs and managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs)
  * [View, cancel, or delete resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig)
  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
