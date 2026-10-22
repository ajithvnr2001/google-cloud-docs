---
url: https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm/
title: Create a Flex-start VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:18.383094+00:00
---

# Create a Flex-start VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a Flex-start VM Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a Flex-start virtual machine (VM) instance. Flex-start VMs run for up to seven days and help you acquire high-demand resources like GPUs or TPUs at a discounted price. These features make Flex-start VMs a cost-effective solution for running short-duration workloads, such as model fine-tuning and batch inference.

To learn more about the key characteristics of Flex-start VMs, including the requirements and limitations that you apply when you create them, see [About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

## Before you begin

  * Verify that your project has sufficient preemptible quota for the machine type that you want your Flex-start VMs to use. For instructions, see [View the quotas for your project](https://docs.cloud.google.com/docs/quotas/view-manage#view_project_quotas). 
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

To get the permissions that you need to create a standalone Flex-start VM, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create a standalone Flex-start VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a standalone Flex-start VM:

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

## Create a Flex-start VM

If you want to create a Flex-start VM that uses a machine type other than A2, G4, G2, or N1, then see the following:

  * [Create an A3 Ultra or A4 VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4)

  * [Create an A3 Mega, A3 High, or A3 Edge VM](https://docs.cloud.google.com/compute/docs/gpus/gpudirect)

  * [Create an H4D VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma)

  * [Create a TPU VM](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance#create_a_tpu)




To create an A2 or G2 Flex-start VM that specifies a [compact placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) for minimal network latency, use the gcloud CLI or REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Machine configuration** pane, complete the following steps:

     1. In the **Name** field, enter a name for the Flex-start VM.

     2. Specify the **Region** and **Zone** where you want to create your VM. You can only specify a [supported region and zone for A2, G4, G2, or N1 machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available).

     3. Based on the workload that you want to run, specify a machine type as follows:

        * To specify an accelerator-optimized machine type, do the following:

          1. Click the **GPUs** tab.

          2. In the **GPU type** list, select a GPU type, except **NVIDIA GB200 192GB**.

          3. In the **Number of GPUs** list, select the number of GPUs to attach to your VM.

          4. Optional: If your GPU model supports [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), and you plan to run graphics-intensive workloads, select **Enable Virtual Workstation (NVIDIA GRID)**.

        * To specify an H4D machine type, do the following:

          1. Click the **Compute optimized** tab.

          2. In the **Series** column, select **H4D**.

  3. In the navigation menu, click **Advanced**. In the **Advanced** pane that appears, complete the following steps:

     1. In the **Provisioning model** section, in the **VM provisioning model** list, select **Flex-start**.

     2. In the **Enter number of hours** field, enter the maximum amount of time that you want the VM to run. The value must be between `0.01` (0.01 hours, or 36 seconds) or `168` (168 hours, or seven days).

     3. Select the **Set a wait time for VM creation** checkbox. Then, based on the zonal requirements for your workload, specify one of the following durations to help increase the chances that your VM creation request succeeds:

        * If your workload requires you to create the VM in a specific zone, then specify a duration between **90 seconds** and **2 hours**. Longer durations give you higher chances of obtaining resources.

        * If the VM can run in any zone within the region, then specify a duration of **0 seconds** or clear the **Set a wait time for VM creation** checkbox. This action specifies that Compute Engine only allocates resources if they are immediately available. If the VM creation request fails because resources are unavailable, then retry the request in a different zone.

     4. In the **On VM termination** field, select whether to stop or delete the Flex-start VM at the end of its run duration:

        * To delete the VM, select **Delete**.

        * To stop the VM, select **Stop**.

  4. To create the Flex-start VM, click **Create**.




###  gcloud 

To create an A2, G4, G2, or N1 Flex-start VM, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the following flags:

  * The `--request-valid-for-duration` flag

  * The `--provisioning-model=FLEX_START` flag

  * The `--instance-termination-action` flag

  * The `--max-run-duration` flag

  * The `--maintenance-policy=TERMINATE` flag




To create a Flex-start VM, run the following command:
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --zone=ZONE \
        --request-valid-for-duration=VALID_FOR_DURATION \
        --provisioning-model=FLEX_START \
        --instance-termination-action=TERMINATION_ACTION \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE
    

Replace the following:

  * `VM_NAME`: the name of your new VM.

  * `MACHINE_TYPE`: the machine type to use for the Flex-start VM. If you specify a G4, G2, or N1 machine type, then consider the following:

    * For G4 or G2 machine types, you can optionally specify a [NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations) to use for graphic-intensive workloads. To do so, include the `--accelerator` flag in the command as follows:
          
          --accelerator=count=VWS_ACCELERATOR_COUNT,type=VWS_ACCELERATOR_TYPE
          

Replace the following:

      * `VWS_ACCELERATOR_COUNT`: the number of NVIDIA RTX vWS that your workload requires. This number must match the number of GPUs that are attached in the G4 or G2 machine type that you want to use.

      * `VWS_ACCELERATOR_TYPE`: the type of NVIDIA RTX vWS accelerator to use. Specify one of the following values:

        * For G4 machine types: `nvidia-rtx-pro-6000-vws`

        * For G2 machine types: `nvidia-l4-vws`

    * For N1 machine types, you must specify the number and type of GPUs to attach to your VM. Otherwise, creating the VM fails. To attach GPUs to an N1 VM, include the `--accelerator` flag in the command as follows:
          
          --accelerator=count=NUMBER_OF_ACCELERATORS,type=ACCELERATOR_TYPE
          

Replace the following:

      * `NUMBER_OF_ACCELERATORS`: the number of GPUs to attach to your N1 VM.

      * `ACCELERATOR_TYPE`: a [supported GPU model for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus).

  * `ZONE`: the zone where you want to create the VM. You can only specify a [supported zone for A2, G4, G2, or N1 machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `VALID_FOR_DURATION`: the maximum time to wait for provisioning your requested resources. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1h2m3s` for one hour, two minutes, and three seconds. Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

    * If your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90s`) and two hours (`2h`). Longer durations give you higher chances of obtaining resources.

    * If the VM can run in any zone within the region, then specify a duration of zero seconds (`0s`). This value specifies that Compute Engine only allocates resources if they are immediately available. If the creation request fails because resources are unavailable, then retry the request in a different zone.

  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of its run duration. Specify one of the following values:

    * To stop the VM: `STOP`

    * To delete the VM: `DELETE`

  * `RUN_DURATION`: the maximum time that the VM runs before Compute Engine automatically stops or deletes it. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. The value must be between 10 minutes and seven days.




If you want to apply a compact placement policy to an A2 or G2 Flex-start VM, then include the `--resource-policies` flag in the command:
    
    
    gcloud compute instances create VM_NAME \
        --machine-type=MACHINE_TYPE \
        --zone=ZONE \
        --request-valid-for-duration=VALID_FOR_DURATION \
        --provisioning-model=FLEX_START \
        --instance-termination-action=TERMINATION_ACTION \
        --max-run-duration=RUN_DURATION \
        --maintenance-policy=TERMINATE \
        **--resource-policies= POLICY_NAME**
    

Replace `POLICY_NAME` with the name of an existing compact placement policy. You can only create your Flex-start VM in the same region as the placement policy.

###  REST 

To create an A2, G4, G2, or N1 Flex-start VM, make a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). In the request body, include the following fields:

  * The `params.requestValidForDuration` field.

  * The `scheduling.provisioningModel` field set to `FLEX_START`.

  * The `scheduling.instanceTerminationAction` field.

  * The `scheduling.maxRunDuration` field.

  * The `scheduling.onHostMaintenance` field set to `TERMINATE`.




To create a Flex-start VM, make a `POST` request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          },
          "boot": true
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "params": {
        "requestValidForDuration": {
          "seconds": VALID_FOR_DURATION
        }
      },
      "scheduling": {
        "provisioningModel": "FLEX_START",
        "instanceTerminationAction": "TERMINATION_ACTION",
        "maxRunDuration": {
          "seconds": RUN_DURATION
        },
        "onHostMaintenance": "TERMINATE"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the VM.

  * `ZONE`: the zone where you want to create the VM. You can only specify a [supported zone for A2, G4, G2, or N1 machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `VM_NAME`: the name of your new VM.

  * `MACHINE_TYPE`: the machine type to use for the Flex-start VM. If you specify a G4, G2, or N1 machine type, then consider the following:

    * For G4 or G2 machine types, you can optionally specify a [NVIDIA RTX Virtual Workstations (vWS)](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations) to use for graphic-intensive workloads. To do so, include the `guestAccelerators` field in the request body as follows:
          
          "guestAccelerators": [
            {
              "acceleratorCount": VWS_ACCELERATOR_COUNT,
              "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/VWS_ACCELERATOR_TYPE"
            }
          ]
          

Replace the following:

      * `VWS_ACCELERATOR_COUNT`: the number of NVIDIA RTX vWS that your workload requires. This number must match the number of GPUs that are attached in the G4 or G2 machine type that you want to use.

      * `VWS_ACCELERATOR_TYPE`: the type of NVIDIA RTX vWS accelerator to use. Specify one of the following values:

        * For G2 machine types: `nvidia-l4-vws`
        * For G4 machine types: `nvidia-rtx-pro-6000-vws`
    * For N1 machine types, you must specify the number and type of GPUs to attach to your VM. Otherwise, creating the VM fails. To attach GPUs to an N1 VM, include the `guestAccelerators` field in the request body as follows:
          
          "guestAccelerators": [
            {
              "acceleratorCount": ACCELERATOR_COUNT,
              "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/ACCELERATOR_TYPE"
            }
          ]
          

Replace the following:

      * `NUMBER_OF_ACCELERATORS`: the number of GPUs to attach to your N1 VM.

      * `ACCELERATOR_TYPE`: a [supported GPU model for N1 VMs](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus).

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This value specifies to use the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `VALID_FOR_DURATION`: the maximum time in seconds to wait for the VM to be provisioned. Based on the zonal requirements for your workload, specify one of the following durations to help increase your chances that your VM creation request succeeds:

    * If your workload requires you to create the VM in a specific zone, then specify a duration between 90 seconds (`90`) and two hours (`7200`). Longer durations give you higher chances of obtaining resources.

    * If the VM can run in any zone within the region, then specify a duration of zero seconds (`0`). This value specifies that Compute Engine only allocates resources if they are immediately available. If the creation request fails because resources aren't available, then retry the request in a different zone.

  * `TERMINATION_ACTION`: whether to stop or delete the VM at the end of its run duration. Specify one of the following values:

    * To stop the VM: `STOP`

    * To delete the VM: `DELETE`

  * `RUN_DURATION`: the maximum time, in seconds, that the VM runs before Compute Engine automatically stops or deletes it. The value must be between `600` (600 seconds, or 10 minutes) and `604800` (604,800 seconds, or seven days).




If you want to apply a compact placement policy to an A2 or G2 Flex-start VM, then include the `resourcePolicies` field in the request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
          },
          "boot": true
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ],
      "params": {
        "requestValidForDuration": {
          "seconds": VALID_FOR_DURATION
        }
      },
      "scheduling": {
        "provisioningModel": "FLEX_START",
        "instanceTerminationAction": "TERMINATION_ACTION",
        "maxRunDuration": {
          "seconds": RUN_DURATION
        },
        "onHostMaintenance": "TERMINATE"
      },
      **"resourcePolicies": [
        "projects/ PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
      ]**
    }
    

Replace the following:

  * `REGION`: the region where the compact placement policy exists. You can only create your Flex-start VM in the same region as the placement policy.

  * `POLICY_NAME`: the name of the compact placement policy.




## What's next

  * [Connect to your VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance)

  * [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript)

  * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates)

  * [Stop or restart a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
