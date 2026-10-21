---
url: https://docs.cloud.google.com/tpu/docs/create-single-host-mig/
title: Create a MIG with single-host Cloud TPU slices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:20.567438+00:00
---

# Create a MIG with single-host Cloud TPU slices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/create-single-host-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a MIG with single-host Cloud TPU slices

This document describes how to create a managed instance group (MIG) with multiple, independent single-host TPU slices.

## Prerequisites

Complete the following prerequisites:

  1. Create a project for your TPUs as described in [Set up a project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).
  2. Determine your TPU requirements as described in [Plan your resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).



## Create a MIG with multiple single-host TPU slices

To create multiple, independent TPU VMs in a MIG:

  1. Create an instance template.
  2. Create the MIG.



### Create an instance template

Instance template configurations vary based on the consumption option you use: on-demand, Spot, reservations, or Flex-start. For more information about consumption options, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus) .

#### Create an instance template for an on-demand TPU VM

The following command creates an instance template that uses the _on-demand_ consumption option:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "INSTANCE_TEMPLATE_NAME",
        "properties": {
          "machineType": "MACHINE_TYPE",
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
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `INSTANCE_TEMPLATE_NAME`: The name of your instance template.
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example, `ct6e-standard-8t`).
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



#### Create an instance template for a TPU Spot VM

The following command creates an instance template that uses the _Spot_ consumption option:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --instance-termination-action=STOP \
        --provisioning-model=SPOT \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "INSTANCE_TEMPLATE_NAME",
        "properties": {
          "machineType": "MACHINE_TYPE",
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
            "instanceTerminationAction": "STOP"
          },
          "networkInterfaces": [
            {
              "network": "global/networks/default"
            }
          ]
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `INSTANCE_TEMPLATE_NAME`: The name of your instance template.
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example, `ct6e-standard-8t`).
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



#### Create an instance template for a TPU reservation-bound VM

The following command creates an instance template that uses the _reservation-bound_ consumption option:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --instance-termination-action=DELETE \
        --reservation-affinity=specific \
        --provisioning-model=reservation-bound \
        --reservation=RESERVATION_NAME \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "INSTANCE_TEMPLATE_NAME",
        "properties": {
          "machineType": "MACHINE_TYPE",
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
          "reservationAffinity": {
            "consumeReservationType": "SPECIFIC_RESERVATION",
            "key": "compute.googleapis.com/reservation-name",
            "values": [
              "RESERVATION_NAME"
            ]
          },
          "networkInterfaces": [
            {
              "network": "global/networks/default"
            }
          ]
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `INSTANCE_TEMPLATE_NAME`: The name of your instance template.
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example, `ct6e-standard-8t`).
  * `RESERVATION_NAME`: The name of a specific reservation that you want to consume. For All Capacity mode reservations, you can target a block or sub-block by specifying the reservation URL as follows:

    * Specify a block:
          
          RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME
          

    * Specify a sub-block:
          
          RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUBBLOCK_NAME
          

  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).

  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.




#### Create an instance template for a TPU Flex-start VM

The following command creates an instance template that uses the _Flex-start_ consumption option:

**Important:** When you use the `ct6e-standard-8t` machine type, you must set the threads per core to `1` by including the [`--threads-per-core=1` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--threads-per-core) in the following command. For more information on threads per core, see [Set the number of threads per core](https://docs.cloud.google.com/compute/docs/instances/set-threads-per-core).

###  gcloud 
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --instance-termination-action=DELETE \
        --provisioning-model=FLEX_START \
        --max-run-duration=DURATION \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "INSTANCE_TEMPLATE_NAME",
        "properties": {
          "machineType": "MACHINE_TYPE",
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
            "provisioningModel": "FLEX_START",
            "instanceTerminationAction": "DELETE",
            "maxRunDuration": {
              "seconds": "DURATION"
            }
          },
          "networkInterfaces": [
            {
              "network": "global/networks/default"
            }
          ]
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `INSTANCE_TEMPLATE_NAME`: The name of your instance template.
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example, `ct6e-standard-8t`).
  * `DURATION`: The maximum run duration for the TPU VM. For REST, specify this as a string containing the number of seconds followed by "s" (for example, `3600s` for 1 hour, or `604800s` for 7 days).
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



### Create a MIG

To create a zonal MIG containing a single-host TPU slice, use the following command:

###  gcloud 
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size=MIG_SIZE \
        --template=INSTANCE_TEMPLATE_URL \
        --zone=ZONE
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MIG_NAME",
        "targetSize": MIG_SIZE,
        "instanceTemplate": "INSTANCE_TEMPLATE_URL"
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `MIG_NAME`: The name of your MIG.
  * `MIG_SIZE`: The size of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for your MIG.



To create a regional MIG containing a single-host TPU slice, use the following command:

###  gcloud 
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --size=MIG_SIZE \
        --template=INSTANCE_TEMPLATE_URL \
        --region=REGION \
        --target-distribution-shape=ANY_SINGLE_ZONE \
        --instance-redistribution-type=none
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MIG_NAME",
        "targetSize": MIG_SIZE,
        "instanceTemplate": "INSTANCE_TEMPLATE_URL",
        "distributionPolicy": {
          "targetShape": "ANY_SINGLE_ZONE"
        },
        "updatePolicy": {
          "instanceRedistributionType": "NONE"
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `MIG_NAME`: The name of your MIG.
  * `MIG_SIZE`: The number of VMs in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) where you want your MIG to be provisioned.
  * `REGION`: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) where you want your MIG to be provisioned.



## Create VMs with custom names in a MIG

You can create VMs in a MIG by specifying custom names for each VM. This is useful for debugging and ensuring instances are created in a specific order. 

###  gcloud 

Create a VM with custom name by using the [`create-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance) and specify the `--instance` flag. To create multiple VMs, repeat the command for each VM. Otherwise, use the REST API method to specify multiple VMs in a single request.

  * For a zonal MIG, use the following command:
        
        gcloud compute instance-groups managed create-instance MIG_NAME \
            --zone=ZONE \
            --instance=INSTANCE_NAME
        

  * For a regional MIG, use the following command:
        
        gcloud compute instance-groups managed create-instance MIG_NAME \
            --region=REGION \
            --instance=INSTANCE_NAME
        




Replace the following placeholders:

  * `MIG_NAME`: The name of your MIG.
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) of the MIG.
  * `REGION`: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) of the MIG.
  * `INSTANCE_NAME`: The name of the VM to add to the specified MIG. 



###  REST 

Create VMs with custom names by using one of the following REST API methods:

  * For a zonal MIG, use the [`instanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/createInstances
         {
           "instances": [
             {
               "name": "INSTANCE_NAME_1"
             },
             {
               "name": "INSTANCE_NAME_2"
             },
             ...
           ]
         }
         

  * For a regional MIG, use the [`regionInstanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/createInstances).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/createInstances
         {
           "instances": [
             {
               "name": "INSTANCE_NAME_1"
             },
             {
               "name": "INSTANCE_NAME_2"
             },
             ...
           ]
         }
         




Replace the following placeholders:

  * `PROJECT_ID`: The ID of the project where the MIG exists.
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) of the MIG.
  * `REGION`: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) of the MIG.
  * `INSTANCE_NAME_1,2,..`: The names of the VMs to add to the specified MIG.



## What's next

  * Learn about [TPU VMs and MIGs](https://docs.cloud.google.com/tpu/docs/tpus-and-migs).
  * Learn how to [Create a MIG with a multi-host Cloud TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig).
  * Learn how to [manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to run an ML workload on TPUs, for example, [Serve Qwen2-72B-Instruct with vLLM on TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen2-7b-instruct).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
