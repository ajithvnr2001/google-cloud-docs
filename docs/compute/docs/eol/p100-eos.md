---
url: https://docs.cloud.google.com/compute/docs/eol/p100-eos/
title: NVIDIA P100 end of support \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:02.897556+00:00
---

# NVIDIA P100 end of support  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/eol/p100-eos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Resources ](https://docs.cloud.google.com/compute/docs/resources)



Send feedback 

#  NVIDIA P100 end of support Stay organized with collections  Save and categorize content based on your preferences. 

NVIDIA P100 GPUs on Google Cloud will reach End of Support (EOS) on **September 15, 2026**.

## What do I need to know

After September 15, 2026, you cannot create or access any Google Cloud resources that run NVIDIA P100 GPUs. This deprecation affects resources for the following services:

  * Compute Engine: VM instances
  * Google Kubernetes Engine (GKE): nodes
  * Gemini Enterprise Agent Platform: models, jobs, and endpoints
  * Gemini Enterprise Agent Platform Workbench: instances
  * Colab Enterprise: notebooks, runtimes, and runtime templates
  * Cloud Workstations: workstations
  * Dataflow: pipeline jobs
  * Managed Service for Apache Spark: clusters and serverless batches
  * Deep Learning VM and Container-Optimized OS instances



## How will this EOS impact my existing resources

Until September 15, 2026, your resources that are running NVIDIA P100 GPUs are not affected. However, your projects might be at risk because you are running a GPU model that is approaching its EOS. EOS products or features are not supported by Google Cloud.

## What do I need to do

To transition your workloads to supported GPUs, you must choose a new GPU model, review its availability in your regions, and then migrate your workloads.

### Choose a GPU model

We recommend moving to modern GPU alternatives, specifically the G2 or G4 machine series. To determine the best GPU model for your workload, compare the following options:

Feature | G2 (NVIDIA L4) | G4 (NVIDIA RTX PRO 6000)  
---|---|---  
**Best for** | High-performance AI inference, generative AI, media streaming, and graphics. L4 GPUs provide up to four times the performance of T4 GPUs. | High-performance simulation, NVIDIA Omniverse workloads, 3D graphics rendering, local LLM fine-tuning and inference, virtual workstations (vWS), and fractional GPU (vGPU) sharing.  
**Architecture and memory** | Ada Lovelace architecture with 24 GB GDDR6 GPU memory. | Blackwell architecture with 96 GB GPU memory per GPU.  
**Machine series** | [G2 accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) | [G4 accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series)  
**Migration path** | **New VM migration** : Move to a new VM to transition to the G2 machine series. | **New VM migration** : Move to a new VM to transition to the G4 machine series.  
  
For a comprehensive list and comparison of all GPU models, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus).

### Review available locations

To verify that your selected GPU model is available, review the location details for your service:

  * Gemini Enterprise Agent Platform and Colab Enterprise: review [Gemini Enterprise Agent Platform accelerator locations](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/locations#accelerators).
  * Cloud Workstations: review [Cloud Workstations GPU availability by region and zone](https://docs.cloud.google.com/workstations/docs/available-gpus#gpu_availability_by_region_and_zone).
  * For all other services: review the available [GPU regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).



## Migrate your workloads

Based on the service that you use, select one of the following transition paths:

### Compute Engine workloads

Depending on the machine type and GPU model that you want to switch to, choose _one_ of the following methods:

  * For accelerator-optimized machine types, move to a new VM.
  * For another GPU model that runs on an N1 general-purpose machine type, modify the existing VM.



#### Move to a new VM

You must move to a new VM if the new GPU model is not supported in the zone of the existing VM, or if you are switching to a GPU that runs on an [accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) machine type.

To move to a new VM, complete the following steps:

  1. If your existing VM uses Local SSD disks that contain data you want to keep, move the contents of those disks to a Persistent Disk volume.
  2. Create a new VM. For example, to create a VM that runs on the G2 (NVIDIA L4) machine type, see [Create a G2 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series).

**Note:** To reuse most of your configurations from your existing VMs, you can use the [create similar option](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-similar-instance). However, remember to update the GPU type.
  3. Move Persistent Disk volumes from the old VM to the new VM. You can do this by detaching the Persistent Disk volume from the old VM and adding it to the new VM. You can alternatively [transfer files](https://docs.cloud.google.com/compute/docs/instances/transfer-files) from one VM to the other.

  4. Optional: Move the saved data from Persistent Disk volumes back to a Local SSD disk.

  5. [Reassign any static IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#IP_assign) that were associated with the original VM to the new VM.

  6. [Install GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu) on the VM.

  7. Install your applications on the new VM.

  8. Delete the old VM.




#### Modify your existing VM

If the new GPU model that you want to switch to is supported in the same zone, and runs on the [N1 general-purpose](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus) machine types, then you can modify your existing VM to switch from an NVIDIA P100 to the new GPU model.

###  Console 

To modify your GPU type in the console, complete the following steps:

  1. [Verify that you have enough quota](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#check-quota) for the new GPU type.
  2. Verify that all of your critical applications are stopped on the VM.
  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  4. Click the name of the VM that is running the NVIDIA P100 GPU. The **VM instance details** page opens.

  5. Click stop **Stop**. If there is no **Stop** option, then click more_vert **More actions >** stop **Stop**. Check the notification panel to see when the VM is stopped.

  6. Click edit **Edit** and then complete the following steps:

     1. In the **Machine configuration** section, select the **GPU** machine family.
     2. From the **GPU type** list, change the GPU model from NVIDIA P100 to your new GPU model.
  7. To apply your changes, click **Save**.

  8. To restart the VM, click **Start/Resume**.




###  gcloud 

To modify your GPU type using the Google Cloud CLI, complete the following steps:

  1. [Verify that you have enough quota](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#check-quota) for the new GPU type.
  2. Verify that all of your critical applications are stopped on the VM.
  3. Export the VM configuration to a local YAML file:
         
         gcloud compute instances export VM_NAME \
            --destination=config.yaml \
            --zone=ZONE
         

  4. Open the exported `config.yaml` file and update the `guestAccelerators` block:
         
         guestAccelerators:
         - acceleratorCount: ACCELERATOR_COUNT
          acceleratorType: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/acceleratorTypes/ACCELERATOR_TYPE

Ensure that `scheduling.onHostMaintenance` is set to `TERMINATE` under the `scheduling` block:
         
         scheduling:
          automaticRestart: true
          onHostMaintenance: TERMINATE

  5. Stop the VM.
         
         gcloud compute instances stop VM_NAME \
            --zone=ZONE
         

  6. Apply the modified configuration using the `update-from-file` command.
         
         gcloud compute instances update-from-file VM_NAME \
            --source=config.yaml \
            --most-disruptive-allowed-action=RESTART \
            --zone=ZONE
         

  7. Start the VM.
         
         gcloud compute instances start VM_NAME \
            --zone=ZONE
         




Replace the following:

  * `PROJECT_ID`: your project ID.
  * `VM_NAME`: the name of the VM instance.
  * `ZONE`: the zone where the VM is located.
  * `ACCELERATOR_COUNT`: the number of GPUs that you want attached.
  * `ACCELERATOR_TYPE`: the GPU model (for example,`nvidia-tesla-t4`).



###  REST 

To modify your GPU type using the Compute Engine API, complete the following steps:

  1. [Verify that you have enough quota](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#check-quota) for the new GPU type.
  2. Verify that all of your critical applications are stopped on the VM.
  3. Stop the VM.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/stop
         

  4. Update the scheduling options on the stopped VM to terminate during host maintenance.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setScheduling
         
         {
          "onHostMaintenance": "TERMINATE",
          "automaticRestart": true
         }
         

  5. Add or modify the attached GPUs by calling `setMachineResources`.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/setMachineResources
         
         {
          "guestAccelerators": [
            {
              "acceleratorCount": ACCELERATOR_COUNT,
              "acceleratorType": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/acceleratorTypes/ACCELERATOR_TYPE"
            }
          ]
         }
         

  6. Start the VM.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/start
         

Replace the following:

     * `PROJECT_ID`: your project ID.
     * `VM_NAME`: the name of the VM instance.
     * `ZONE`: the zone where the VM is located.
     * `ACCELERATOR_COUNT`: the number of GPUs that you want attached.
     * `ACCELERATOR_TYPE`: the GPU model (for example, `nvidia-tesla-t4`).



### Other Google Cloud workloads

If your workloads run on services other than Compute Engine such as GKE, Gemini Enterprise Agent Platform, Agent Platform Workbench, Colab Enterprise, Cloud Workstations, Dataflow, or Managed Service for Apache Spark, then you must do the following:

  1. Update your configurations to reference a supported GPU model.

     * For GKE, Gemini Enterprise Agent Platform, Colab Enterprise, or Cloud Workstations, update your configuration or runtime templates.
     * For Agent Platform Workbench, change the machine type and GPU configuration of your instance or create a new instance.
     * For Dataflow, update your pipeline specifications.
     * For Managed Service for Apache Spark, update your cluster definitions.

For instructions about configuring GPUs for your service, see the product documentation for that service.

  2. Restart or recreate your resources.




## What's next

  * Learn more [about GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus).
  * Review [GPU pricing](https://cloud.google.com/compute/gpus-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
