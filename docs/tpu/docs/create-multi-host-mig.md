---
url: https://docs.cloud.google.com/tpu/docs/create-multi-host-mig/
title: Create a MIG with a multi-host Cloud TPU slice \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:13.704065+00:00
---

# Create a MIG with a multi-host Cloud TPU slice  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/create-multi-host-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a MIG with a multi-host Cloud TPU slice

This document describes how to create a managed instance group (MIG) with a multi-host TPU slice.

## Prerequisites

Complete the following prerequisites:

  1. Create a project for your TPUs as described in [Set up a project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).
  2. Determine your TPU requirements as described in [Plan your resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).



## Create a MIG with multi-host TPU slices

  1. Create an instance template.
  2. Create a workload policy.
  3. Create the MIG.



### Create an instance template

The command to create an instance template depends on the consumption option you use: on-demand, Spot, reservation-bound, or flex-start. For more information about consumption options, see [Plan your TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus).

#### Create an instance template for an on-demand TPU VM

The following command creates an instance template using the on-demand consumption option:

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
          "scheduling": {
            "onHostMaintenance": "TERMINATE"
          },
          "disks": [
            {
              "boot": true,
              "initializeParams": {
                "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
              }
            }
          ],
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
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



#### Create an instance template for a TPU Spot VM

The following command creates an instance template using the Spot consumption option:

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
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



#### Create an instance template for a TPU reservation-bound VM

The following command creates an instance template using the reservation-bound consumption option:

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
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
  * `RESERVATION_NAME`: The name of the specific reservation to consume. For All Capacity mode reservations, you can target a block or sub-block by specifying the reservation URL as follows:

    * Specify a block:
          
          RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME
          

    * Specify a sub-block:
          
          RESERVATION_NAME/reservationBlocks/RESERVATION_BLOCK_NAME/reservationSubBlocks/RESERVATION_SUBBLOCK_NAME
          

  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).

  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.




#### Create an instance template for a TPU Flex-start VM

The following command creates an instance template using the flex-start consumption option:

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
  * `MACHINE_TYPE`: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
  * `DURATION`: The maximum duration for which the TPU VM can run. For REST, specify this as a number of seconds (for example, `3600` for 1 hour, or `604800` for 7 days).
  * `IMAGE_FAMILY`: The [OS image family](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * `IMAGE_PROJECT`: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.



### Create a workload policy

You must create a workload policy with the `accelerator-topology` parameter (for example, `4x4`, `8x8`, or `4x4x4`). The accelerator topology configures the MIG to treat the instances as a single, interconnected slice.

The following command creates a workload policy for a specific topology:

###  gcloud 
    
    
    gcloud compute resource-policies create workload-policy WORKLOAD_POLICY_NAME \
      --type=high-throughput \
      --accelerator-topology=TOPOLOGY \
      --region=REGION
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "WORKLOAD_POLICY_NAME",
        "workloadPolicy": {
          "type": "HIGH_THROUGHPUT",
          "acceleratorTopology": "TOPOLOGY"
        }
      }' \
      "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/resourcePolicies"
    

Replace the following placeholders:

  * `PROJECT_ID`: The ID of your Google Cloud project.
  * `WORKLOAD_POLICY_NAME`: The name of your workload policy.
  * `TOPOLOGY`: The topology of the TPU VMs, for example, `4x4x8`. For more information about topology for each version of TPU, see [System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `REGION`: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) for your workload policy.



### Create a MIG

To create a zonal MIG containing a multi-host TPU slice, use the following command:

###  gcloud 
    
    
    gcloud compute instance-groups managed create MIG_NAME \
       --size=MIG_SIZE \
       --target-size-policy-mode=bulk \
       --template=INSTANCE_TEMPLATE_URL \
       --zone=ZONE \
       --default-action-on-vm-failure=do-nothing \
       --workload-policy=WORKLOAD_POLICY_URL
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MIG_NAME",
        "targetSize": MIG_SIZE,
        "targetSizePolicy": {
          "mode": "BULK"
        },
        "instanceTemplate": "INSTANCE_TEMPLATE_URL",
        "instanceLifecyclePolicy": {
          "defaultActionOnFailure": "DO_NOTHING"
        },
        "resourcePolicies": {
          "workloadPolicy": "WORKLOAD_POLICY_URL"
        }
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
  * `WORKLOAD_POLICY_URL`: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`.



To create a regional MIG containing a multi-host TPU slice, use the following command:

###  gcloud 
    
    
    gcloud compute instance-groups managed create MIG_NAME \
       --size=MIG_SIZE \
       --target-size-policy-mode=bulk \
       --template=INSTANCE_TEMPLATE_URL \
       --region=REGION \
       --default-action-on-vm-failure=do-nothing \
       --workload-policy=WORKLOAD_POLICY_URL \
       --target-distribution-shape=any-single-zone \
       --instance-redistribution-type=none
    

###  REST 
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{
        "name": "MIG_NAME",
        "targetSize": MIG_SIZE,
        "targetSizePolicy": {
          "mode": "BULK"
        },
        "instanceTemplate": "INSTANCE_TEMPLATE_URL",
        "instanceLifecyclePolicy": {
          "defaultActionOnFailure": "DO_NOTHING"
        },
        "resourcePolicies": {
          "workloadPolicy": "WORKLOAD_POLICY_URL"
        },
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
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/regions-zones) for your MIG.
  * `REGION`: The [region](https://docs.cloud.google.com/tpu/docs/regions-zones) for your MIG.
  * `WORKLOAD_POLICY_URL`: The URL of the workload policy that you want to use to create instances in the MIG. For example: `projects/PROJECT_ID/regions/WORKLOAD_POLICY_REGION/resourcePolicies/WORKLOAD_POLICY_NAME`.



## Create VMs with custom names in a MIG

You can create VMs in a MIG by specifying custom names for each VM. This is useful for debugging and ensuring instances are created in a specific order. 

MIGs that contain a multi-host TPU slice use the bulk mode of target size policy. When creating VMs with custom names in such a MIG, the following applies:

  * You must first [verify](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) that the MIG doesn't have VMs in it. If the MIG has VMs, you must either [resize the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) to target size `0` or create another MIG with target size `0`.

  * You can only use the REST API to create VMs with custom names.




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
  * Learn how to [Create a MIG with a single-host Cloud TPU slice](https://docs.cloud.google.com/tpu/docs/create-single-host-mig).
  * Learn how to [manage TPU VMs](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to run an ML workload on TPUs, for example, [Serve Qwen2-72B-Instruct with vLLM on TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen2-7b-instruct).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
