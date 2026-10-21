---
url: https://docs.cloud.google.com/compute/docs/instance-groups/bulk-create-instances-in-mig/
title: Create a MIG that uses the bulk mode \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:23:25.094868+00:00
---

# Create a MIG that uses the bulk mode  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/bulk-create-instances-in-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG that uses the bulk mode Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use bulk mode in a MIG to create all of the virtual machine (VM) instances that you require at the same time. Creating instances all at once ensures that the MIG creates instances only when all necessary resources are available.

To learn how bulk mode works, see [About bulk creation of instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode).

## Create an instance template

Bulk mode in MIGs is only supported with instance templates that specify either a reservation-bound or flex-start provisioning model. To use bulk mode, create an instance template using one of these provisioning model as described in the following sections. For more information about the provisioning models, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

### Use the reservation-bound provisioning model

To create an instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page opens.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select one of the following options:

     * To create a regional instance template, select **Regional (recommended)** , and then select a region that [supports TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all). 

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
  * `REGION`: the region in which to create the instance template. Specify a region that [supports TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all). 

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

  * `REGION`: the region in which to create the instance template. Specify a region that [supports TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all). 

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

### Use the flex-start provisioning model

To create an instance template, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page opens.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select one of the following options:

     * To create a regional instance template, select **Regional (recommended)** , and then select a region that [supports TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all). 

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
  * `REGION`: the region in which to create the instance template. Specify a region that [supports TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all). 

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

  * `REGION`: the region in which to create the instance template. Specify a region that [supports TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all). 

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to create.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. Specify an image family to use the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type to use for the Flex-start VMs. If you specify an N1 machine type, then you must include the [`guestAccelerators` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert#request-body) to define the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration, in seconds, you want the requested VMs to run. The value must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).




For more information about creating an instance template, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

## Create a MIG that uses bulk mode

To enable bulk creation of instances in a MIG, set the `targetSizePolicy.mode` field to `BULK` in the MIG's configuration. When you use this bulk mode, the MIG waits for full resource availability and then creates instances all at once.

**Note:** If some instances fail to create after provisioning begins, then the MIG automatically deletes the instances that were successfully created and continues to wait for sufficient capacity to try again.

###  Console 

  1. Go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**. The **Create instance group** page opens.

  3. In the **Name** field, enter a name for the MIG.

  4. Before you select an instance template, you must do the following:

     1. If you use the flex-start provisioning model, then you must turn off repairs as follows: 
        1. In the **VM instance lifecycle** section, clear the **Allow repair of VMs in an alternate zone** checkbox.
        2. In the **Default action on failure** list, select **No action**.
     2. In the **Location** section, do the following: 
        * To create a zonal MIG, select **Single zone**.
        * To create a regional MIG, select **Multiple zones**. In the **Target distribution shape** , select **Any single zone**. In the dialog that appears, select **Disable instance redistribution**.
  5. Go back to the **Instance template** field. In the **Instance template** list, select the instance template that you created in the previous section.

  6. In the **Number of instances** field, specify the number of instances that you want to create all at once.

  7. Select the **Obtain VMs all at once with bulk target size policy** checkbox.

  8. Click **Create**.




###  gcloud 

To create a MIG that has bulk creation enabled, use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) with the `--target-size-policy-mode` flag set to `bulk`.

If you use the flex-start provisioning model, then you must turn off repairs in the MIG by including the `--default-action-on-vm-failure=do-nothing` flag in the following commands.

  * To create a zonal MIG, run the following command:


    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --size=SIZE \
        --target-size-policy-mode=bulk \
        --template=INSTANCE_TEMPLATE_URL \
        --zone=ZONE \
    

  * To create a regional MIG, run the following command:


    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --size=SIZE \
        --target-size-policy-mode=bulk \
        --template=INSTANCE_TEMPLATE_URL \
        --zones=LIST_OF_ZONES \
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `SIZE`: the number of instances in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `ZONE`: the zone where the MIG creates instances.
  * `LIST_OF_ZONES`: a comma-separated list of zones where the regional MIG creates instances. For example, `us-central1-a, us-central1-b, us-central1-c`.



###  REST 

To create a MIG that has bulk creation enabled, make a `POST` request as follows. In the request body, set the `targetSizePolicy.mode` field to `bulk`.

If you use the flex-start provisioning model, then you must turn off repairs in the MIG by including the `"instanceLifecyclePolicy": {"defaultActionOnFailure": "DO_NOTHING"}` field in the following requests.

  * To create a zonal MIG, make a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "targetSize": SIZE,
          "targetSizePolicy": {
            "mode": "bulk"
          },
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ]
        }
        

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "targetSize": SIZE,
          "targetSizePolicy": {
            "mode": "bulk"
          },
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ]
        }
        




Replace the following:

  * `PROJECT_ID`:the project ID.
  * `ZONE`:the zone where the MIG creates instances.
  * `REGION`:the region where the MIG creates instances.
  * `INSTANCE_GROUP_NAME`:the name of the MIG.
  * `SIZE`:the number of instances in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`



## Add or delete instances

In a MIG that uses the bulk mode, you can add or remove instances by manually increasing or decreasing the target size of the MIG.

  * **Add instances** : When you increase the target size from zero, the MIG adds instances the same way as when creating a MIG. You can also create instances with specific names by using the `createInstances` method when there is no instance in the MIG. To create instances with specific names, see [Creating instances with specific names in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

  * **Delete instances** : When you decrease the target size to zero, the MIG deletes all existing instances in the group and cancels any creation operation that was in progress. You can remove instances by decreasing the target size to `0`. To decrease to a non-zero size, the MIG must not have a bulk instance operation in progress (`bulkInstanceOperation.inProgress` must be `false`). 




To add or remove instances from a MIG by changing the target size, see [Manually setting the size of a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

## What's next

  * Learn how to [view or cancel bulk creation of instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/view-cancel-vm-bulk-creation-in-migs).
  * Learn how to [work with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).
  * [View information about MIGs and managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
