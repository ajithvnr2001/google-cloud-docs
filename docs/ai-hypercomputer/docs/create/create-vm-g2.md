---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g2/
title: Create an AI-optimized G2 instance \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:44.659869+00:00
---

# Create an AI-optimized G2 instance  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Create an AI-optimized G2 instance Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

This document describes the steps to create standalone virtual machine (VM) instances that use the G2 machine series. To learn more about these accelerator-optimized machine types, see [G2 series](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g2).

To learn about other ways to create VMs or clusters, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview). 

## Limitations

When you create a standalone G2 VM, the following limitations apply:

  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use a G2 machine type.
  * You can only use a G2 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * The G2 machine type is only available on the [Cascade Lake platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Standard Persistent Disk (`pd-standard`) isn't supported on instances that use the G2 machine type. For supported disk types, see [Supported disk types for G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-disks).
  * You can't create [Multi-Instance GPUs](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) on an instance that uses a G2 machine type.
  * If you need to change the machine type of a G2 instance, review [Modify accelerator-optmized instances](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus#accelerator-optimized_vms).
  * You can't use [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) as boot disks for instances that use the G2 machine type.
  * The current default driver for Container-Optimized OS doesn't support L4 GPUs running on G2 machine types. Also, Container-Optimized OS only supports a select set of drivers. If you want to use Container-Optimized OS on G2 machine types, review the following notes: 
    * Use a Container-Optimized OS version that supports the minimum recommended NVIDIA driver version `525.60.13` or later. For more information, review the [Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes). 
    * When you [install the driver](https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-gpus#install-driver), specify the latest available version that works for the L4 GPUs. For example, `sudo cos-extensions install gpu -- -version=525.60.13`. 
  * You must use the Google Cloud CLI or REST to [create G2 instances](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized#create-vm) for the following scenarios: 
    * You want to specify custom memory values.
    * You want to customize the number of visible CPU cores.

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

Creating an instance with the G2 machine type includes the following steps:

  1. Optional: Create a compact placement policy
  2. Create an instance
  3. Install GPU drivers



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



### Create a G2 VM

To create a G2 VM, use one of the following methods.

The following commands also set the access scope for your instances. To simplify permissions management, Google recommends that you set the access scope on an instance to `cloud-platform` access and then use IAM roles to define what services the instance can access. For more information, see [Scopes best practice](https://docs.cloud.google.com/compute/docs/access/service-accounts#scopes_best_practice). 

###  Console 

**Important:** If you choose to use a compact placement policy or if you want to use [NVIDIA RTX Virtual Workstation (vWS) for graphics-intensive workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), then you must use Google Cloud CLI or REST to create the VM. 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify a **Name** for your VM. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  3. Select the **Region** and **Zone** where you want to create a VM. See the list of available [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  4. Click the **GPUs** tab, and then complete the following steps:

     1. To use the G2 machine series, in the **GPU type** list, select `NVIDIA L4`.
     2. In the **Number of GPUs** list, select a number of GPUs.
     3. In the **Machine type** list, select a machine type.
  5. Based on the consumption option that you want to use, select one of the following options and complete the following steps.

###  Reservation 

G2 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

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

           * To optionally use reservation capacity, select **Use automatic selection**. (This option is selected by default.)

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

     3. Optional: To configure the boot disk size, see either the [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.

     4. To confirm your boot disk options, click **Select**.

     5. Optional: If you want to add [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd), then complete the following steps:

        1. Click **add Add local SSD**. The **Configure local SSD** pane opens.
        2. In the **Configure local SSD** pane, configure the options for the Local SSD disks. For more information, see [Add a Local SSD disk to your compute instance](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd) in the Compute Engine documentation.
        3. To confirm your boot disk options, click **Save**.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#formatandmount) before you can use it.

  7. Configure the service account and access scopes as follows. Workloads running on the instance use the attached service account to authorize requests to other Google Cloud services.

     1. In the navigation menu, click **Security**.
     2. In the **Service account** list, select a service account to use.
     3. For **Access scopes** , select the **Allow full access to all Cloud APIs** option. This best practice lets you manage access by adding or removing IAM roles from the service account. For more information, see [Attaching a service account to an instance](https://docs.cloud.google.com/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance).
  8. To create and start the VM, click **Create**.




###  gcloud 

To create the VM, use the [ `gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

G2 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

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
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY \
        --reservation=RESERVATION
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
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

  3. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  4. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  5. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-l4-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  6. Run the command.



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
        --provisioning-model=STANDARD \
        --maintenance-policy=TERMINATE \
        --reservation-affinity=RESERVATION_AFFINITY
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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
  4. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  5. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-l4-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  6. Run the command.



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
        --provisioning-model=FLEX_START \
        --request-valid-for-duration=REQUEST_VALID_FOR_DURATION \
        --max-run-duration=MAX_RUN_DURATION \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
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
  3. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  4. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-l4-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Run the command.



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
        --provisioning-model=SPOT \
        --instance-termination-action=TERMINATION_ACTION \
        --maintenance-policy=TERMINATE \
        --no-restart-on-failure
    

Complete the following steps:

  1. Replace the following:

     * `INSTANCE_NAME`: the name of the VM.
     * `MACHINE_TYPE`: the machine type to use for the VM. For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) in the Compute Engine documentation.
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `ZONE`: the zone in which the machine type that you want to use is available. To specify a compact placement policy, use a zone in the same region as the compact placement policy. For information about regions, see [GPU availability by regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table).
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `DISK_SIZE`: the size of the boot disk in GB. For more information, see either [Google Cloud Hyperdisk size limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#size-limits) or [Persistent Disk size limits](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk#size_limits) based on the type of disk.
     * `TERMINATION_ACTION`: the action to take when Compute Engine preempts the instance, either `STOP` (default) or `DELETE`.

**Important:** Make sure your application can handle preemption. For example, handle preemption by specifying a shutdown script during instance creation. Learn how to [handle preemption with a shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption). 
  2. Optional: To use a compact placement policy, add the following flag:
         
         --resource-policies=POLICY_NAME
         

Replace the following:

     * `POLICY_NAME`: the name of the compact placement policy.
  3. Optional: To attach Local SSD disks, then add the following `--local-ssd` flag for _each_ Local SSD disk.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
         --local-ssd interface=INTERFACE_TYPE
         

Replace the following:

     * `INTERFACE_TYPE`: the disk interface type that you want to use for the Local SSD disk. If your boot disk image has [optimized NVMe drivers](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface), then specify `NVME`. Specify `SCSI` for other images.

After creating a VM with Local SSD disks, you must [format and mount each device](https://docs.cloud.google.com/compute/docs/disks/local-ssd#formatandmount) before you can use it.

  4. Optional: To use [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), add the following flag.

When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).
         
         --accelerator=type=nvidia-l4-vws,count=VWS_ACCELERATOR_COUNT
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Run the command.



###  REST 

To create the VM, make a `POST` request to the [ `instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

The parameters that you need to specify depend on the [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) that you are using for this deployment. Select the tab that corresponds to your consumption option.

### Reservation

G2 instances support the following [types of reservations](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type):

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
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
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
  2. Optional: If you chose to use a compact placement policy, then add the following field to the request body:
         
         "resourcePolicies": [
             "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
           ]
         

Replace the following:

     * `PROJECT_ID`: the project ID of the compact placement policy.
     * `REGION`: the region of the compact placement policy.
     * `POLICY_NAME`: the name of the compact placement policy.
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
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
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-l4-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



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
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
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
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
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
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-l4-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



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
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
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
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
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
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-l4-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



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
     * `DISK_TYPE`: the type of the boot disk. For more information about the supported disk types for your machine type, see [GPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation. 
     * `IMAGE_PROJECT`: the project ID of the OS image. 
     * `IMAGE_FAMILY`: the image family of the OS image that you want to use. For a list of all supported operating systems, see [Supported operating systems](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). 
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
  3. Optional: To use Local SSD disks, add the following field to the `disks[]` field for _each_ Local SSD disk. Separate each `disks[]` subfield (including the boot disk) with a comma.

Ensure that the number of Local SSD disks that you attach is allowed for your machine type; for details, see [About Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options) in the Compute Engine documentation.
         
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
               "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/nvidia-l4-vws"
             }
           ]
         

Replace `VWS_ACCELERATOR_COUNT` with the number of virtual GPUs that you want.

  5. Submit the request.



### Install GPU drivers

After you create an instance, the instance can't use its GPUs unless the correct GPU drivers are already installed. The driver that you need to install depends on whether the instance enabled [NVIDIA RTX Virtual Workstation (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). Use one of the following options: 

  * If you enabled vWS, then see [Install drivers for NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers) in the Compute Engine documentation.
  * Otherwise, use the default GPU drivers as follows:

    * If you specified an [OS image that includes GPU drivers](https://docs.cloud.google.com/ai-hypercomputer/docs/images#accelerator-os-images), then no action is required.
    * If the OS image doesn't include GPU drivers, then see [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) in the Compute Engine documentation.



## What's next

  * [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * [Verify reservation consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#verify-consumption)
  * [Troubleshoot reservation consumption](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reservation-consumption)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
