---
url: https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-single-host-slice/
title: Create a MIG with single-host TPU slices \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:52.020505+00:00
---

# Create a MIG with single-host TPU slices  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-single-host-slice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG with single-host TPU slices Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a managed instance group (MIG) that forms single-host TPU slices. A single-host TPU slice maps to one TPU virtual machine (VM) instance.

You can also create a single-host TPU slice as a standalone TPU instance. For more information, see [Create a TPU VM instance](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance).

## Before you begin

  * Review the [limitations](https://docs.cloud.google.com/compute/docs/tpus/tpus-and-migs#limitations) for creating MIGs with TPU instances.
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

Before you proceed to create a single-host TPU slice, you must do the following:

  1. **Choose the TPU version** : select the TPU version that is suitable for your workload. For a list of TPU versions by workload type, see [Recommended TPU versions by workload types](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_versions_and_workload_types).

  2. **Validate TPU availability in your preferred location** : TPUs are available in specific Google Cloud regions. To use a TPU version, ensure its availability in your preferred region. For a list of TPU locations, see [TPU availability](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones#view-using-table).

  3. **Ensure that your project has sufficient TPU quota** : if you are creating a single-host TPU slice with on-demand, Flex-start VMs, or Spot VMs, you must have sufficient TPU quota available in the region that you want to use. Creating a single-host TPU slice that consumes a TPU reservation doesn't require any TPU quota as quota is used when the reservation was created. For a list of TPU quota names, see [TPU quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota) and for instructions on how to view the quota, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage)

  4. **Choose a TPU consumption option** : select a consumption option that best fits your workload, its duration, and your cost needs. For a list of consumption option availability by TPU versions, see [TPU consumption options](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#consumption_options).

  5. **Choose a topology** : select a topology supported for the selected TPU version. For a list of topologies available for each TPU version, see [TPU topology](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_topology). 




## Create a MIG with multiple single-host TPU slices

To create multiple, independent TPU VMs in a MIG:

  1. Create an instance template.
  2. Create the MIG.



### Create an instance template

Instance template configurations vary based on the consumption option you use: on-demand, Spot, reservations, or Flex-start. For more information about consumption options, see [About VM provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) .

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
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) for your MIG.



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
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) where you want your MIG to be provisioned.
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
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) of the MIG.
  * `REGION`: The [region](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) of the MIG.
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
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) of the MIG.
  * `REGION`: The [region](https://docs.cloud.google.com/compute/docs/regions-zones/tpu-regions-zones) of the MIG.
  * `INSTANCE_NAME_1,2,..`: The names of the VMs to add to the specified MIG.



## What's next

  * [Create a multi-host slice](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-mig-multi-host-slice)
  * [Connect to a TPU instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh)
  * [View a MIG's properties](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties)
  * [View the status of a TPU slice](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#view_the_status_of_a_tpu_slice)
  * [Monitor TPUs](https://docs.cloud.google.com/tpu/docs/monitor-tpu)
  * [Delete a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
