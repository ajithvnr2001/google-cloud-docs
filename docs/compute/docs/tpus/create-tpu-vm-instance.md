---
url: https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance/
title: Create a TPU VM instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:55.159924+00:00
---

# Create a TPU VM instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a TPU VM instance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a TPU virtual machine (VM) instance. A TPU VM is also called a single-host TPU slice.

To create a group of single-host slices, see [Create a MIG with single-host TPU slices](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-single-host-slice).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




## Prerequisites

Before you proceed to create a TPU instance, you must do the following:

  1. **Choose the TPU version** : select the TPU version that is suitable for your workload. For a list of TPU versions by workload type, see [Recommended TPU versions by workload types](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_versions_and_workload_types).

  2. **Validate TPU availability in your preferred location** : TPUs are available in specific Google Cloud regions. To use a TPU version, ensure its availability in your preferred region. For a list of TPU locations, see [TPU availability](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones#view-using-table).

  3. **Ensure that your project has sufficient TPU quota** : if you are creating a TPU instance with on-demand, Flex-start VMs, or Spot VMs, you must have sufficient TPU quota available in the region that you want to use. Creating a TPU instance that consumes a TPU reservation doesn't require any TPU quota as quota is used when the reservation was created. For a list of TPU quota names, see [TPU quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota) and for instructions on how to view the quota, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)

  4. **Choose a TPU consumption option** : select a consumption option that best fits your workload, its duration, and your cost needs. For a list of consumption option availability by TPU versions, see [TPU consumption options](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#consumption_options).




## Create a TPU VM instance

The parameters you use to create a TPU VM instance depend on the consumption option you are using: on-demand, Spot, reservation-bound, or flex-start. For more information, see [About VM provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) .

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
  * ZONE: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) for the TPU VM (for example `us-central1-b`).



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
  * ZONE: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) for the TPU VM (for example `us-central1-b`).



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
  * ZONE: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) for the TPU VM (for example `us-central1-b`).
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
  * ZONE: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) for the TPU VM (for example `us-central1-b`).
  * MAX_RUN_DURATION: The maximum run duration for the TPU VM (for example `6h`). For REST, specify this as a number of seconds (for example `21600` for 6 hours).
  * VALID_DURATION: The maximum duration for which the request is valid. For REST, specify this as a number of seconds (for example `3600` for 1 hour).



For more information about creating Compute Engine instances, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## Limitations

  * **Lifecycle operations** : You can't stop, start, resume, or suspend TPU instances. To change configurations that require a restart or to stop incurring charges, you must delete the instances. 

  * **Update VM details** : You can [update the properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#updatable-properties) that only require a refresh (`REFRESH`) action. If a configuration requires a restart (`RESTART`), then you must recreate the instance.

  * **Automatic restart** : In All Capacity mode, you must not disable [automatic restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#autorestart) by setting the `scheduling.automaticRestart` field to `false`.




## What's next

  * [Connect to a TPU instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh)
  * [View the details of a TPU instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)
  * [Monitor TPUs](https://docs.cloud.google.com/tpu/docs/monitor-tpu)
  * [Delete a TPU instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
