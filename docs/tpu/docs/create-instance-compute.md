---
url: https://docs.cloud.google.com/tpu/docs/create-instance-compute/
title: Create a Cloud TPU VM instance using Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:14.919736+00:00
---

# Create a Cloud TPU VM instance using Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/create-instance-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Cloud TPU VM instance using Compute Engine

This document shows you how to create a single TPU VM with the Compute Engine `gcloud compute instances create` command. You can also create a TPU VM instance by specifying an [instance template](https://docs.cloud.google.com/compute/docs/instance-templates). For more information, see [Create a VM from an instance template](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-instance-template).

## Prerequisites

Complete the following prerequisites:

  1. Create a Google Cloud project for your TPUs as described in [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

  2. Determine your TPU requirements as described in [Plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).




## Create a TPU VM instance

The parameters you use to create a TPU VM instance depend on the consumption option you are using: on-demand, Spot, reservation-bound, or flex-start. For more information, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus) .

### Create an on-demand TPU VM instance

To create an _on-demand_ TPU VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create):

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instances create TPU_NAME \
      --machine-type=MACHINE_TYPE \
      --image-family=IMAGE_FAMILY \
      --image-project=IMAGE_PROJECT \
      --zone=ZONE \
      --maintenance-policy=TERMINATE
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "TPU_NAME",
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            }
          }
        ],
        "scheduling": {
          "onHostMaintenance": "TERMINATE"
        },
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ]
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).



### Create a TPU Spot VM instance

To create a TPU Spot VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--provisioning-model=SPOT` flag:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instances create TPU_NAME \
      --machine-type=MACHINE_TYPE \
      --image-family=IMAGE_FAMILY \
      --image-project=IMAGE_PROJECT \
      --zone=ZONE \
      --provisioning-model=SPOT \
      --instance-termination-action=DELETE \
      --maintenance-policy=TERMINATE
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "TPU_NAME",
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            }
          }
        ],
        "scheduling": {
          "onHostMaintenance": "TERMINATE",
          "provisioningModel": "SPOT",
          "instanceTerminationAction": "DELETE"
        },
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ]
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).



### Create a TPU VM instance using a reservation

To create a TPU VM instance using the _reservation-bound_ consumption option, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--reservation-affinity=specific` and `--reservation` flags:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).**Note:** You can't use the [`--request-valid-for-duration`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--request-valid-for-duration) flag with All Capacity mode reservations.

###  gcloud 
    
    
    gcloud compute instances create TPU_NAME \
      --machine-type=MACHINE_TYPE \
      --image-family=IMAGE_FAMILY \
      --image-project=IMAGE_PROJECT \
      --zone=ZONE \
      --provisioning-model=reservation-bound \
      --reservation-affinity=specific \
      --reservation=RESERVATION_NAME \
      --instance-termination-action=DELETE \
      --maintenance-policy=TERMINATE
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "TPU_NAME",
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            }
          }
        ],
        "scheduling": {
          "onHostMaintenance": "TERMINATE",
          "provisioningModel": "RESERVATION_BOUND",
          "instanceTerminationAction": "DELETE"
        },
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "reservationAffinity": {
          "consumeReservationType": "SPECIFIC_RESERVATION",
          "key": "compute.googleapis.com/reservation-name",
          "values": [
            "RESERVATION_NAME"
          ]
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * RESERVATION_NAME: The name of the specific reservation to consume. For All Capacity mode reservations, you can target a block or sub-block by specifying the reservation URL as follows:

    * Specify a block:
          
          RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME
          

    * Specify a sub-block:
          
          RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUBBLOCK_NAME
          




### Create a TPU Flex-start VM

To create a TPU _Flex-start_ VM instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the `--provisioning-model=FLEX_START` flag:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instances create TPU_NAME \
      --machine-type=MACHINE_TYPE \
      --image-family=IMAGE_FAMILY \
      --image-project=IMAGE_PROJECT \
      --zone=ZONE \
      --provisioning-model=FLEX_START \
      --max-run-duration=MAX_RUN_DURATION \
      --request-valid-for-duration=VALID_DURATION \
      --instance-termination-action=DELETE \
      --maintenance-policy=TERMINATE
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "TPU_NAME",
        "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE",
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
            }
          }
        ],
        "params": {
          "requestValidForDuration": {
            "seconds": VALID_DURATION
          }
        },
        "scheduling": {
          "onHostMaintenance": "TERMINATE",
          "provisioningModel": "FLEX_START",
          "instanceTerminationAction": "DELETE",
          "maxRunDuration": {
            "seconds": MAX_RUN_DURATION
          }
        },
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ]
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances"
    

Replace the following placeholders:

  * PROJECT_ID: The ID of your Google Cloud project.
  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for the TPU VM (for example `us-central1-b`).
  * MAX_RUN_DURATION: The maximum run duration for the TPU VM (for example `6h`). For REST, specify this as a number of seconds (for example `21600` for 6 hours).
  * VALID_DURATION: The maximum duration for which the request is valid. For REST, specify this as a number of seconds (for example `3600` for 1 hour).



For more information about creating Compute Engine instances, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## What's next

  * Learn how to [Create a MIG with single-host Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/create-single-host-mig).
  * Learn how to [Create a MIG with a multi-host Cloud TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig).
  * Learn how to [manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to run an ML workload on TPUs, for example, [Serve Qwen2-72B-Instruct with vLLM on TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen2-7b-instruct).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
