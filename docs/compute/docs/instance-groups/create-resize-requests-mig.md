---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig/
title: Create resize requests in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:56:00.809370+00:00
---

# Create resize requests in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create resize requests in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create resize requests in a managed instance group (MIG) of virtual machine (VM) instances. To learn more about MIG resize requests, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

Creating a MIG resize request helps you obtain highly-demanded resources, like GPUs, and optimize costs by creating the exact number of VMs all at once. To create a MIG resize request that can use the features and services available from AI Hypercomputer, see instead [Create a MIG and a resize request](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra#create-mig-and-resize-request) in the AI Hypercomputer documentation.

You can also use _bulk mode_ in MIGs to create instances all at once to achieve the target size that you set. To learn more about this option, see [About bulk mode](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode).

## Before you begin

  * To use MIG resize requests to create Flex-start VMs for workloads that run for up to seven days, verify that you have sufficient quota for your requested resources. Otherwise, your resize request remains pending until you have sufficient quota.
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

To get the permissions that you need to create MIG resize requests, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create MIG resize requests. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create MIG resize requests:

  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To create a zonal MIG: `compute.instanceGroupManagers.create` on the project 
  * To create a MIG resize request: `compute.instanceGroupManagers.update` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare a MIG for resize requests

To create a MIG resize requests, you must configure an instance template and the MIG as described in the following sections.

### Create an instance template

Based on your use case for MIG resize requests, create an instance template by using one of the following methods:

  * If you want to create Flex-start VMs for workloads that run for up to seven days, then create an instance template by using the flex-start provisioning model.

  * If you want to create VMs by consuming an auto-created reservation for a future reservation in calendar mode, then create an instance template by using the reservation-bound provisioning model.




#### Use the flex-start provisioning model

To create an instance template configured for creating MIG resize requests and Flex-start VMs, you must specify the following settings in the template:

  * Use a [GPU machine type](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types) (except A4X Max or A4X), or an [H4D machine type](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types).

  * Delete VMs at the end of their run duration by using the [`maxRunDuration` and `instanceTerminationAction` fields](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#set-duration).

  * Stop VMs during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).

  * Use the [flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




Note: If you want to run data science or machine learning workloads, then consider using a Deep Learning VM Images image when you create an instance template. Deep Learning VM is a set of prepackaged VM images that comes with machine learning frameworks and essential tools. For more information about these images, see [Choose an image](https://docs.cloud.google.com/deep-learning-vm/docs/images) in the Deep Learning VM documentation. 

To create an instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page opens.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select one of the following options:

     * To create a regional instance template, select **Regional (recommended)** , and then select a region that [supports GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

     * To create a global instance template, select **Global**.

  5. In the **Machine configuration** section, specify a machine type.

  6. In the **Provisioning model** section, complete the following steps:

     1. In the **VM provisioning model** field, select **Flex-start**.

     2. Expand **VM provisioning model advanced settings**.

     3. Select the **Set a time limit for the VM** checkbox.

     4. To set a run duration for the VMs that are created by using the instance template, in the **Enter number of hours** field, enter the number of hours. The value must be between 36 seconds (`0.01`) and seven days (`168`).

  7. Optional: To change the default value boot disk type or image, in the **Boot disk** section, click **Change**. Then, follow the prompts to change the boot disk.

  8. Click **Create**.




###  gcloud 

To create an instance template, use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the following flag settings:

  * The `--instance-termination-action` flag set to `DELETE`.

  * The `--maintenance-policy` flag set to `TERMINATE`.

  * The `--max-run-duration` flag.

  * The `--provisioning-model` flag set to `FLEX_START`.




The following example command creates a regional instance template. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --instance-template-region=REGION \
        --instance-termination-action=DELETE \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --max-run-duration=RUN_DURATION \
        --provisioning-model=FLEX_START
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to create.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). Specify an image family to use the most recent, non-deprecated OS image. For example, if you specify `debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

**Note:** If you want to use a specific version of the OS image, such as `debian-12-bookworm-v20240701`, then replace the `--image-family` flag with the `--image` flag.
  * `REGION`: the region in which to create the instance template. Specify a region that [supports GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

  * `MACHINE_TYPE`: the machine type to use for the Flex-start VMs. If you specify an N1 machine type, then you must include the [`--accelerator` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--accelerator) to define the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration you want the requested VMs to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days.




###  REST 

To create an instance template, make a `POST` request to one of the following methods:

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert)




In the request body, include the following fields:

  * The `scheduling.instanceTerminationAction` field set to `DELETE`.

  * The `scheduling.maxRunDuration` field.

  * The `scheduling.onHostMaintenance` field set to `TERMINATE`.

  * The `scheduling.provisioningModel` field set to `FLEX_START`.




The following example request creates a regional instance template:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
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
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `REGION`: the region in which to create the instance template. Specify a region that [supports GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to create.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. Specify an image family to use the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type to use for the Flex-start VMs. If you specify an N1 machine type, then you must include the [`guestAccelerators` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert#request-body) to define the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration, in seconds, you want the requested VMs to run. The value must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).




For more information about creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

#### Use the reservation-bound provisioning model

To create an instance template configured for MIG resize requests and for consuming a reservation, you must specify the following in the template:

  * To use an [A4 or A3 Ultra machine type](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types), or an [H4D machine type](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_machine_types), as specified in the reservation that you want to consume.

  * To stop VMs during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).

  * To delete VMs at the end of the reservation period by using the [`instanceTerminationAction` field](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#set-duration).

  * To [target the reservation for consumption](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation).

  * To use the [reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




**Note** : If you want to run data science or machine learning workloads, then consider using a Deep Learning VM Images image when you create an instance template. Deep Learning VM is a set of prepackaged VM images that comes with machine learning frameworks and essential tools. For more information about these images, see [Choose an image](https://docs.cloud.google.com/deep-learning-vm/docs/images) in the Deep Learning VM documentation. 

To create an instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page opens.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select one of the following options:

     * To create a regional instance template, select **Regional (recommended)** , and then select a region that [supports GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

     * To create a global instance template, select **Global**.

  5. In the **Machine configuration** section, specify a machine type.

  6. In the **Provisioning model** section, complete the following steps:

     1. Expand **VM provisioning model advanced settings**.

     2. In the **On VM termination** list, select **Delete**.

  7. Optional: To change the default value boot disk type or image, in the **Boot disk** section, click **Change**. Then, follow the prompts to change the boot disk.

  8. Expand the **Advanced options** section, and then do the following:

     1. Expand the **Management** section.

     2. In the **Reservations** section, select **Choose a reservation** , and then click **Choose reservation**. In the pane that appears, follow the prompts to select the reservation that you want to consume.

  9. Click **Create**.




###  gcloud 

To create an instance template, use the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create) with the following flag settings:

  * The `--instance-termination-action` flag set to `DELETE`.

  * The `--maintenance-policy` flag set to `TERMINATE`.

  * The `--provisioning-model` flag set to `RESERVATION_BOUND`.

  * The `--reservation-affinity` flag set to `specific`.

  * The `--reservation` flag.




The following example command creates a regional instance template. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --instance-termination-action=DELETE \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --provisioning-model=RESERVATION_BOUND \
        --reservation-affinity=specific \
        --reservation=RESERVATION_URL
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to create.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). Specify an image family to use the most recent, non-deprecated OS image. For example, if you specify `debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

**Note:** If you want to use a specific version of the OS image, such as `debian-12-bookworm-v20240701`, then replace the `--image-family` flag with the `--image` flag.
  * `REGION`: the region in which to create the instance template. Specify a region that [supports GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

  * `MACHINE_TYPE`: the machine type that is specified in the reservation that you want to consume.

  * `RESERVATION_URL`: the URL of the auto-created reservation for a future reservation in calendar mode that you want to consume. Specify one of the following values:

    * If the auto-created reservation exists in your project: `RESERVATION_NAME`.

    * If the auto-created reservation exists in a different project: `projects/PROJECT_ID/reservations/RESERVATION_NAME`.




###  REST 

To create an instance template, make a `POST` request to one of the following methods:

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert)




In the request body, include the following fields:

  * The `reservationAffinity.consumeReservationType` field set to `SPECIFIC_RESERVATION`.

  * The `reservationAffinity.key` field set to `compute.googleapis.com/reservation-name`.

  * The `reservationAffinity.values` field set to the URL of the auto-created reservation.

  * The `scheduling.instanceTerminationAction` field set to `DELETE`.

  * The `scheduling.onHostMaintenance` field set to `TERMINATE`.

  * The `scheduling.provisioningModel` field set to `RESERVATION_BOUND`.




For example, to create a regional instance template, make a request as follows:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE"
            }
          }
        ],
        "machineType": "MACHINE_TYPE",
        "networkInterfaces": [
          {
            "network": "global/networks/default"
          }
        ],
        "reservationAffinity": {
          "consumeReservationType": "SPECIFIC_RESERVATION",
          "key": "compute.googleapis.com/reservation-name",
          "values": [
            "RESERVATION_URL"
          ]
        },
        "scheduling": {
          "instanceTerminationAction": "DELETE",
          "onHostMaintenance": "TERMINATE",
          "provisioningModel": "RESERVATION_BOUND"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `REGION`: the region in which to create the instance template. Specify a region that [supports GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to create.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. Specify an image family to use the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type that is specified in the reservation that you want to consume.

  * `RESERVATION_URL`: the URL of the auto-created reservation for a future reservation in calendar mode that you want to consume. Specify one of the following values:

    * If the auto-created reservation exists in your project: `RESERVATION_NAME`

    * If the auto-created reservation exists in a different project: `projects/PROJECT_ID/reservations/RESERVATION_NAME`




For more information about creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

### Create or update a MIG

After creating the instance template as described in the previous section, use that instance template to create a MIG as follows, or [update a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#updating_selected_instances). Additionally, you must do the following to prepare the MIG for resize requests:

  * [Set the MIG's update type to opportunistic](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#set_up_a_proactive_or_an_opportunistic_update) (default).

  * [Turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig).

  * If you've configured autoscaling in the MIG, then [delete the autoscaling configuration](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#delete_an_autoscaler).

  * If you're using a regional MIG, then [set the target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) to `ANY_SINGLE_ZONE`.




To create the MIG, select one of the following options. If you want to specify a [workload policy](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies) to minimize network latency among your VMs, then you must use the gcloud CLI or REST API.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**. The **Create instance group** page opens.

  3. In the **Name** field, enter a name for the MIG.

  4. Before you select an instance template, you must turn off repairs as follows:

     1. In the **VM instance lifecycle** section, clear the **Allow repair of VMs in an alternate zone** checkbox.

     2. In the **Default action on failure** list, select **No action**.

  5. Go back to the **Instance template** field. In the **Instance template** list, select the instance template that you created in the previous section. If you select a regional instance template, then the **Region** list is set to the template's region.

  6. In the **Number of instances** field, enter `0`.

  7. In the **Location** section, specify whether you want to create a zonal or a regional MIG as follows:

     1. To create a zonal MIG, select **Single zone**. Or, to create a regional MIG, select **Multiple zones**.

     2. Select the **Region** and **Zones** of the MIG.

     3. If you're creating a regional MIG, then do the following:

        1. In the **Target distribution shape** field, select **Any single zone**.

        2. In the dialog that appears, click **Disable instance redistribution**.

  8. Click **Create**.




###  gcloud 

Use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) with the `--default-action-on-vm-failure` flag set to `do_nothing`. If you're creating a regional MIG, then you must also include the `--target-distribution-shape` flag set to `any-single-zone`, and the `--instance-redistribution-type` flag set to `none`.

  * To create a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed create MIG_NAME \
            --template=INSTANCE_TEMPLATE_URL \
            --size=0 \
            --zone=ZONE \
            --default-action-on-vm-failure=do_nothing
        

  * To create a regional MIG, run the following command:
        
        gcloud compute instance-groups managed create MIG_NAME \
            --template=INSTANCE_TEMPLATE_URL \
            --size=0 \
            --region=REGION \
            --target-distribution-shape=any-single-zone \
            --instance-redistribution-type=none \
            --default-action-on-vm-failure=do_nothing
        




Replace the following:

  * `MIG_NAME`: the name of the MIG to create.

  * `INSTANCE_TEMPLATE_URL`: the partial URL of the instance template that you created in the previous section. If you want to use a regional instance template to create the MIG, then you can only create the MIG within the template's region. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `INSTANCE_TEMPLATE_NAME`

  * `ZONE`: the zone in which to create the MIG.

  * `REGION`: the region in which to create the MIG.




If you want to apply a workload policy to your MIG, then include the [`--workload-policy` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create#--workload-policy) in the command. You must specify a workload policy that is in the same region as the MIG.

###  REST 

  * To create a zonal MIG, send a `POST` request using the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) as follows:
        
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
        

  * To create a regional MIG, send a `POST` request using the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) as follows:
        
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
            "targetShape": "ANY_SINGLE_ZONE"
          },
          "updatePolicy": {
            "instanceRedistributionType": "NONE"
          },
          "instanceLifecyclePolicy": {
            "defaultActionOnFailure": "DO_NOTHING"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the instance template that you created in the previous section exists.

  * `INSTANCE_TEMPLATE_URL`: the partial URL of the instance template that you created in the previous section. If you want to use a regional instance template to create the MIG, then you can only create the MIG within the template's region. Specify one of the following values:

    * For a regional instance template: `regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_NAME`

    * For a global instance template: `global/instanceTemplates/INSTANCE_TEMPLATE_NAME`

  * `ZONE`: the zone in which to create the MIG.

  * `REGION`: the region in which to create the MIG.

  * `MIG_NAME`: the name of the MIG to create.




If you want to apply a workload policy to your MIG, then include the [`workloadPolicy` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert#body.request_body.FIELDS.resource_policies) in the request body. You must specify a workload policy that is in the same region as the MIG.

## Create a resize request in a MIG

**Preview — Resize request creation by specifying VM names**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Before you create MIG resize requests, make sure that you've prepared the MIG as described in the previous section.

After you create a resize request and all your requested resources become available, the MIG creates the requested number of VMs all at once. The VMs run until the MIG deletes them after the specified run duration ends, or until you [delete them](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

To create a resize request, select one of the following options:

  * Specify the number of VMs
  * Specify a list of VM names



### Specify the number of VMs

To create a resize request that specifies the number of VMs to add to the MIG all at once, select one of the following options.

**Note:** If you want to apply a [workload policy](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies) to the MIG, use the gcloud CLI or REST API.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. In the **Name** column, click the name of the MIG in which to create the resize request. The overview page of the MIG opens.

  3. In the **Resize requests** row, click edit **Edit resize requests**.

  4. Click add **New resize request**. The **New resize requests** pane appears.

  5. In the **Name** field, enter the name of the resize request.

  6. In the **Number of additional instances needed** field, enter the number of VMs to add to the MIG all at once.

  7. Optional: If the MIG's instance template specifies a run duration, then you can specify a different run duration. To do so, in the **Requested run duration** field and **Unit** lists, specify a run duration. You must specify a duration between one hour and seven days.

  8. Click **Create**.




###  gcloud 

  * To create a resize request in a zonal MIG, use the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create).
        
        gcloud compute instance-groups managed resize-requests create MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --resize-by=COUNT \
            --zone=ZONE
        

  * To create a resize request in a regional MIG, use the [`instance-groups managed resize-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create).
        
        gcloud compute instance-groups managed resize-requests create MIG_NAME \
            --resize-request=RESIZE_REQUEST_NAME \
            --resize-by=COUNT \
            --region=REGION
        




Replace the following:

  * `MIG_NAME`: the name of the MIG configured for creating resize requests in it.

  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.

  * `COUNT`: the number of VMs to add to the MIG all at once.

  * `ZONE`: the zone where the MIG exists.

  * `REGION`: the region where the MIG exists.




Optionally, you can do one or both of the following:

  * If the MIG's instance template specifies a run duration, then you can specify a different run duration. To do so, include the [`--requested-run-duration` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize-requests/create#--requested-run-duration) in the command. You must specify a duration between 10 minutes and seven days.



###  REST 

  * To create a resize request in a zonal MIG, send a `POST` request using the [`instanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/MIG_NAME/resizeRequests
        {
          "name": "RESIZE_REQUEST_NAME",
          "resizeBy": COUNT
        }
        

  * To create a resize request in a regional MIG, send a `POST` request using the [`regionInstanceGroupManagerResizeRequests.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagerResizeRequests/insert).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME/resizeRequests
        {
          "name": "RESIZE_REQUEST_NAME",
          "resizeBy": COUNT
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project where the specified MIG exists.

  * `ZONE`: the zone where the MIG exists.

  * `REGION`: the region where the MIG exists.

  * `MIG_NAME`: the name of the MIG configured for creating resize requests in it.

  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.

  * `COUNT`: the number of VMs to add all at once to the MIG.




Optionally, you can do one or both of the following:

  * If the MIG's instance template specifies a run duration, then you can specify a different run duration. To do so, include the [`requestedRunDuration` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagerResizeRequests/insert#body.request_body.FIELDS.requested_run_duration) in the request body. You must specify a duration, in seconds, between 10 minutes and seven days.



### Specify a list of VM names

If your workload requires specific VM names, then specify a list of names to create the VMs. The number of names that you specify determines the number of VMs that the MIG creates all at once.

To create a resize request in a MIG by specifying a list of VM names, use the gcloud CLI or REST API.

###  gcloud 

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
        




Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `INSTANCE_NAMES`: a comma-separated list of names for the VMs that you want to create. For example, `instance-1,instance-2,instance-3`.
  * `ZONE`: the zone where the MIG exists.
  * `REGION`: the region where the MIG exists.



###  REST 

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
    

Replace the following:

  * `PROJECT_ID`: the ID of the project where the specified MIG exists.
  * `MIG_NAME`: the name of the MIG.
  * `RESIZE_REQUEST_NAME`: the name of the resize request, which must be unique within the specified MIG. Otherwise, creating the resize request fails.
  * `INSTANCE_NAME_1`, `INSTANCE_NAME_2`: names for the VMs that you want to create.
  * `ZONE`: the zone where the MIG exists.
  * `REGION`: the region where the MIG exists.



## What's next

  * Learn how to [view, cancel, or delete resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/manage-resize-requests-mig).

  * Learn how to [view information about MIGs and managed VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).



  * Learn how to [view the actual and forecasted usage of your VMs and GPUs](https://docs.cloud.google.com/capacity-planner/docs/view-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
