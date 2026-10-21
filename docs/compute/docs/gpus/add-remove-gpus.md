---
url: https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus/
title: Add or remove GPUs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:43.755685+00:00
---

# Add or remove GPUs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add or remove GPUs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Compute Engine provides graphics processing units (GPUs) that you can add to your Compute Engine instances. You can use these GPUs to accelerate specific workloads on your compute instances such as artificial intelligence (AI), machine learning (ML), and graphics-intensive workloads.

You can only use two machine families when running GPUs on Compute Engine:

  * The [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines). These machine types have attached GPUs.
  * The [N1 general-purpose machine family](https://docs.cloud.google.com/compute/docs/general-purpose-machines). You can use most N1 machine types except the N1 shared-core machine type.



## Before you begin

  * To review additional prerequisite steps such as selecting an OS image and checking GPU quota, review the [overview](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus) document. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Accelerator-optimized instances

Review the following modification options and limitations for accelerator-optimized machine types:

  * You can't remove GPUs from accelerator-optimized machine types.

  * For A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High, A3 Edge, and A2 Ultra instances, you can't change the machine type. If you need to switch to a machine type from another machine family or series, create a new instance with your chosen machine type. Then, migrate your workload to the new instance.

  * For G4, G2, and A2 Standard instances, you can adjust the GPU count by switching to a different machine type within the same machine series. For example, to add GPUs to a G2 instance you might change the machine type from `g2-standard-16` to `g2-standard-48`.

You can't switch G4, G2, or A2 Standard instances to a machine type from a different machine series or family. For example, you can't change the machine type of an instance from `g2-standard-16` to `g4-standard-48` because G2 and G4 are different machine series. If you need to switch to a machine type from another machine series or family, create a new instance with your chosen machine type. Then, migrate your workload to the new instance.




### Modify the GPU count

You can modify the GPU count of a G4, G2, or A2 standard accelerator-optimized instance by using either the Google Cloud console or REST.

###  Console 

You can modify the number of GPUs for your instance by stopping the instance and editing the instance configuration.

  1. Verify that all of your critical applications are stopped on the instance.

  2. In the Google Cloud console, go to the **VM instances** page to see your list of instances.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Click the name of the instance that you want to modify the number of GPUs for. The **Details** page opens.

  4. Complete the following steps from the **Details** page.

     1. If the instance is running, click stop **Stop** to stop the instance. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

     2. Click edit **Edit**.

     3. In the **Machine configuration** section, select the **GPUs** machine family, and then do the following:

        1. In the **Number of GPUs** list, increase or decrease the GPU count.

**Note:** Each accelerator-optimized machine type has a specific number of GPUs attached. If you adjust the number of GPUs, the machine type changes.
     4. To apply your changes, click **Save**.

     5. To restart the instance, click **Start/Resume**.




###  REST 

You can modify the number of GPUs on your instance by stopping the instance and changing the machine type. Each accelerator-optimized machine type has a specific number of GPUs attached. If you change the machine type, this adjusts the number of GPUs that are attached to the instance.

  1. Verify that all of your critical applications are stopped on the instance, and then create a `POST` request to stop the instance so it can move to a host system where GPUs are available.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

  2. After the instance stops, create a `POST` request to modify the machine type.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMachineType
         
         {
            machineType: "zones/ZONE/machineTypes/MACHINE_TYPE"
         }
         

  3. Create a `POST` request to start the instance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         




Replace the following:

  * `PROJECT_ID`: your project ID.
  * `VM_NAME`: the name of the instance that you want to add GPUs to.
  * `ZONE`: the zone where the instance is located. This zone must support [GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `MACHINE_TYPE`: the machine type that you want to use. It must be one of the following:

    * If your instance uses a G4 machine, select another [G4 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-machine-types).
    * If your instance uses a G2 machine type, select another [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms). G2 machine types also support custom memory. Memory must be a multiple of 1024 MB and within the supported memory range. For example, the machine type name for an instance with 4 vCPUs and 19 GB of memory would be `g2-custom-4-19456`.
    * If your instance uses an A2 standard machine, select another [A2 Standard machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms).



### Limitations

###  G4 instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for a G4 machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use a G4 machine type.
  * You can only use a G4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) (regional or zonal) on an instance that uses a G4 machine type.
  * The G4 machine type is only available on the [AMD EPYC Turin 5th Generation platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_processors).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with the `g4-standard-48` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1). All the [limitations for Confidential VM running on the G4 machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.
  * You can't use Windows operating systems on `g4-standard-384` instances.
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to G4 machine types.
  * When creating G4 instances that have less than one GPU attached (fractional GPUs), don't use the `--no-service-account` or `--no-scopes` flags. To authenticate NVIDIA vGPU drivers, Compute Engine must [verify the VM's identity](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity). This process requires that service accounts are enabled.



###  G2 instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for a G2 machine type.
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



###  A2 instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A2 Standard machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A2 Standard machine type.
  * You can only use an A2 Standard machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * The A2 Standard machine type is only available on the [Cascade Lake platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * If your instance uses an A2 Standard machine type, you can only switch from one A2 Standard machine type type to another A2 Standard machine type. You can't change to any other machine type. For more information, see [Modify accelerator-optimized instances](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus#accelerator-optimized_vms).
  * You can't use the Windows operating system with the `a2-megagpu-16g` machine type. When using a Windows operating system, choose a different A2 Standard machine type.
  * You can't do a quick format of the attached Local SSDs on Windows instances that use A2 Standard machine types. To format these Local SSDs, you must do a full format by using the [diskpart utility](https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart) and specifying `format fs=ntfs label=tmpfs`.



## N1-general purpose instances

This section covers how to add, modify, or remove GPUs from a VM instance created with a N1 general-purpose machine type.

In summary, the process to add, modify, or remove GPUs from an existing instance is as follows:

  1. Check that your instance has a boot disk size of at least 40 GiB.
  2. Stop the instance.
  3. Add, modify, or remove the GPUs.

If your N1 instance doesn't have any GPUs attached, you need to complete the following steps:

     1. Prepare your instance for the modification.
     2. Modify the host maintenance setting for the instance. Instances with GPUs cannot [live migrate](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#live_migrate) because they are assigned to specific hardware devices. For more information, see [GPU restrictions](https://docs.cloud.google.com/compute/docs/gpus#restrictions).
     3. Change the machine type. GPUs are only supported on [select N1 machine types](https://docs.cloud.google.com/compute/docs/machine-resource#gpus).
     4. [Install a GPU driver on your instance](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu), so that your system can use the GPU device.



### Prepare your instance

When a GPU is added to an instance, the order of the network interface can change.

Most public images on Compute Engine don't have persistent network interface names and adjust to the new order.

However, if you are using either SLES or a custom image, you must update the system setting to prevent the network interface from persisting. To prevent the network interface from persisting, run the following command on your instance:
    
    
     rm /etc/udev/rules.d/70-persistent-net.rules 

### Add GPUs or modify GPU type on existing instances

This section covers how to add GPUs, or modify the GPU type on an existing N1 general-purpose instance. This procedure supports the following GPU types:

**Caution:** NVIDIA T4 and P4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).  NVIDIA GPUs: 

  * NVIDIA T4: `nvidia-tesla-t4`
  * NVIDIA P4: `nvidia-tesla-p4`
  * NVIDIA V100: `nvidia-tesla-v100`



NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

  * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
  * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.




###  Console 

To add GPUs or modify the GPU type, complete the following steps.

  1. Verify that all of your critical applications are stopped on the instance.

  2. In the Google Cloud console, go to the **VM instances** page to see your list of instances.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Click the name of the instance that you want to update. The **Details** page opens.

  4. Complete the following steps from the **Details** page.

     1. If the instance is running, click stop **Stop**. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

     2. Click edit **Edit**.

     3. In the **Machine configuration** section, select the **GPUs** machine family, and then do the following:

        1. In the **GPU type** list, select or switch to any of the GPU types supported on N1 VMs.

        2. In the **Number of GPUs** list, select the number of GPUs.

        3. If your GPU model supports [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), and you plan on running graphics-intensive workloads on this instance, select **Enable Virtual Workstation (NVIDIA GRID)**.

     4. If your instance didn't have GPUs attached before, complete the following:

        1. If the instance has a shared-core machine type, you must change the machine type. In the **Machine type** list, select one of the preset N1 machine types. Alternatively, you can also specify custom machine type settings.

        2. In the **Management** section, complete the following:

           1. In the **On host maintenance** list, select **Terminate VM instance**. instances with attached GPUs can't live migrate. See [Handle GPU host events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).

           2. In the **Automatic restart** list, select **On**.

     5. To apply your changes, click **Save**.

     6. To restart the VM, click **Start/Resume**.




###  REST 

You can add or modify GPUs on your instance by stopping the instance and changing your instance's configuration through the API.

  1. Verify that all of your critical applications are stopped on the instance and then create a `POST` request to stop the instance so it can move to a host system where GPUs are available.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

  2. If your instance does not have any GPUs attached, complete the following steps:

     1. Identify the GPU type that you want to add to your instance. You can submit a `GET` request to list the GPU types that are available to your project in a specific zone.
            
            GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/acceleratorTypes
            

     2. If the instance has a shared-core machine type, you must [change the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type) to have one or more vCPUs. You cannot add accelerators to instances with shared-core machine types.

     3. Create a `POST` request to set the scheduling options for the instance.
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
            
            {
            "onHostMaintenance": "TERMINATE",
            "automaticRestart": true
            }
            

  3. Create a `POST` request to add or modify the GPUs that are attached to your instance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMachineResources
         
             {
              "guestAccelerators": [
               {
                 "acceleratorCount": ACCELERATOR_COUNT,
                 "acceleratorType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/acceleratorTypes/ACCELERATOR_TYPE"
               }
              ]
             }
         

  4. Create a `POST` request to start the instance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         




Replace the following:

  * `PROJECT_ID`: your project ID.
  * `VM_NAME`: the name of the instance that you want to add GPUs to.
  * `ZONE`: the zone where the instance is located.
  * `ACCELERATOR_COUNT`: the number of GPUs that you want attached to your instance. For a list of GPU limits based on the machine type of your instance, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction).
  * `ACCELERATOR_TYPE`: the [GPU model](https://docs.cloud.google.com/compute/docs/gpus#introduction) that you want to attach or switch to. If you plan on running graphics-intensive workloads on this instance, use one of the [virtual workstation models](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations).

Choose one of the following values:

    * NVIDIA GPUs:

      * NVIDIA T4: `nvidia-tesla-t4`
      * NVIDIA P4: `nvidia-tesla-p4`
      * NVIDIA V100: `nvidia-tesla-v100`
    * NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

      * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
      * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.




#### Install drivers

To install the drivers, choose one of the following options:

  * If you plan to run graphics-intensive workloads, such as those for gaming and visualization, [install drivers for the NVIDIA RTX Virtual Workstation](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers).
  * For most workloads, [install the GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).



### Remove GPUs

This section covers how to remove the following GPU types from an existing N1 general-purpose instance.

**Caution:** NVIDIA T4 and P4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).  NVIDIA GPUs: 

  * NVIDIA T4: `nvidia-tesla-t4`
  * NVIDIA P4: `nvidia-tesla-p4`
  * NVIDIA V100: `nvidia-tesla-v100`



NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

  * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
  * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.




You can use the [Google Cloud console](https://console.cloud.google.com/) to remove GPUs from an existing instance. To remove GPUs, complete the following steps:

  1. Verify that all of your critical applications are stopped on the instance.

  2. In the Google Cloud console, go to the **VM instances** page to see your list of instances.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  3. Click the name of the instance that you want to remove GPUs from. The **Details** page opens.

  4. Complete the following steps from the **Details** page.

     1. If the instance is running, click stop **Stop** to stop the instance. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.

     2. On the toolbar, click edit **Edit**.

     3. In the **Machine configuration** section, select the **General purpose** machine family, and then do the following:

        1. To view attached GPUs, expand **Advanced configurations**.

        2. In the **GPUs** section, remove GPUs using one of the following options:

           * To remove some GPUs, in the **Number of GPUs** list, select a new number.

           * To remove all GPUs, click delete **Delete GPU**.

     4. Optional: Modify the instance host maintenance policy setting. instances with GPUs must have the host maintenance policy set to **Terminate VM instance**. But if you removed all GPUs, you have the option to live migrate this instance during host maintenance. For more information, see [Set VM host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options).

     5. To apply your changes, click **Save**.

     6. To restart the instance, click **Start/Resume**.




## What's next?

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).
  * [Add Local SSDs to your instances](https://docs.cloud.google.com/compute/docs/disks/local-ssd). Local SSD devices pair well with GPUs when your apps require high-performance storage.
  * [Create groups of GPU instances using instance templates](https://docs.cloud.google.com/compute/docs/gpus/gpu-instance-groups).
  * To monitor GPU performance, see [Monitoring GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).
  * To improve network performance, see [Use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus).
  * To handle GPU host maintenance, see [Handling GPU host events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).
  * Try the [Running TensorFlow Inference Workloads at Scale with TensorRT5 and NVIDIA T4 GPU](https://docs.cloud.google.com/compute/docs/tutorials/ml-inference-t4) tutorial.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
