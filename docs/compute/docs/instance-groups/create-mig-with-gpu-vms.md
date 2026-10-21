---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms/
title: Create a MIG that adds GPU VMs all at once \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:05.902199+00:00
---

# Create a MIG that adds GPU VMs all at once  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG that adds GPU VMs all at once Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a managed instance group (MIG) to add GPU virtual machine (VM) instances all at once.

The MIG uses the _bulk mode_ of its target size policy to add the VMs all at once. It also uses the _flex-start provisioning model_ to improve obtainability of resources. For more information about the flex-start provisioning model, see [About provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models#models).

Another method to add GPU VMs all at once in a MIG is by creating resize requests. To determine whether bulk mode or resize request is more suitable for your workload, see the [Comparison of bulk mode and resize request](https://docs.cloud.google.com/compute/docs/instance-groups/overview-add-vms-all-at-once-in-mig#comparison_of_bulk_mode_and_resize_request).

If your workload doesn't require the MIG to creates VMs all at once but you still want to improve resource obtainability, use the flex-start provisioning model as described in [Create a MIG with Flex-start VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms).

## Before you begin

  * To make sure that you have sufficient GPU quota for the resources you're requesting, [check your GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  * To understand quota consumption, read [GPU VMs and preemptible allocation quotas](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas).
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




## Limitations

The following limitations apply:

  * [Limitations of bulk mode in MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode#limitations)

  * [Limitations of flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations)




## Create a MIG and add GPU VMs all at once

To create the GPU VMs all at once, do the following:

  1. Create an instance template, which is required to create a MIG. The MIG then uses this template to create each VM in the group. In the template, specify the configurations for the flex-start provisioning model.

For more information about instance templates, see [About instance templates](https://docs.cloud.google.com/compute/docs/instance-templates).

  2. Create a MIG for bulk provisioning of VMs. During the MIG creation, enable the bulk provisioning capability in the MIG by setting the target size policy mode to `BULK`. In `BULK` mode, the MIG attempts to create all VMs at once to meet the target size that you set.




### Create an instance template

Create an instance template that specifies a [GPU machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines). Then, use the template to create a MIG.

Note: If you want to run data science or machine learning workloads, consider using a Deep Learning VM image when you create an instance template. Deep Learning VM Images is a set of prepackaged VM images that comes with machine learning frameworks and essential tools. For more information about these images, see [Choose an image](https://docs.cloud.google.com/deep-learning-vm/docs/images) in the Deep Learning VM Images documentation. 

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert).



###  Console 

  1. Go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page opens.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Machine configuration** section, do the following:

     1. Click the **GPUs** tab.

     2. In the **GPU type** list, select the GPU type.

     3. In the **Number of GPUs** list, select the number of GPUs.

     4. In the **Machine type** section, select a machine type.

  5. In the **Provisioning model** section, do the following:

     1. In the **VM provisioning model** list, select **Flex-start**.

     2. To set a run duration for the VMs created through the instance template, in the **Enter number of hours** field, enter the number of hours. The value must be between one hour (`1`) and seven days (`168`).

  6. Optional: To change the default value boot disk type or image, in the **Boot disk** section, click **Change**. Then, follow the prompts to change the boot disk.

  7. Click **Create**.




###  gcloud 

Create an instance template by using the [`instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create):
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --instance-termination-action=DELETE \
        --instance-template-region=REGION \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --max-run-duration=RUN_DURATION \
        --provisioning-model=FLEX_START
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

**Note:** If you want to use a specific version of the OS image, such as `debian-12-bookworm-v20240701`, then replace the `--image-family` flag with the `--image` flag.
  * `REGION`: the region in which to create the instance template.

  * `MACHINE_TYPE`: a [GPU machine type](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types). If you specify an N1 machine type, then include the [`--accelerator` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--accelerator) to specify the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration you want the requested VMs to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, or `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days.




###  REST 

Create an instance template by making a `POST` request to the [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceTemplates
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "disks": [
          {
            "boot": true,
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE
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

  * `PROJECT_ID`: the ID of the project in which you want to create the instance template.

  * `REGION`: the region in which to create the instance template.

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image—for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: a [GPU machine type](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types). If you specify an N1 machine type, then include the [`guestAccelerators` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert#request-body) to specify the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration, in seconds, you want the requested VMs to run before the MIG automatically deletes them. The value must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).




After you create the instance template, you can [view it](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to see its ID and review its instance properties.

### Create a MIG and add GPU VMs all at once

Create a MIG as described in this section. When enabling bulk provisioning in the MIG, you must turn off [repairs](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).



###  Console 

  1. Go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**. The **Create instance group** page opens.

  3. In the **Name** field, enter a name for the MIG.

  4. Before you select an instance template, you must turn off repairs and set the location as follows:

     1. To turn off repairs, do the following: 
        1. In the **VM instance lifecycle** section, clear the **Allow repair of VMs in an alternate zone** checkbox.
        2. In the **Default action on failure** list, select **No action**.
     2. To set the **Location** section, do the following: 
        * To create a zonal MIG, select **Single zone**.
        * To create a regional MIG, select **Multiple zones**. In the **Target distribution shape** , select **Any single zone**. In the dialog that appears, select **Disable instance redistribution**.
  5. Go back to the **Instance template** field. In the **Instance template** list, select the instance template that you created in the previous section.

  6. In the **Number of instances** field, specify the number of instances that you want to create all at once.

  7. Select the **Obtain VMs all at once with bulk target size policy** checkbox.

  8. Click **Create**.




###  gcloud 

To create a MIG with bulk provisioning capability, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

  * To create a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
            --default-action-on-vm-failure=do-nothing \
            --size=SIZE \
            --target-size-policy-mode=bulk \
            --template=INSTANCE_TEMPLATE_URL \
            --zone=ZONE \
        

  * To create a regional MIG, run the following command:
        
        gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
            --default-action-on-vm-failure=do-nothing \
            --size=SIZE \
            --target-size-policy-mode=bulk \
            --template=INSTANCE_TEMPLATE_URL \
            --zones=LIST_OF_ZONES \
        




Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `SIZE`: the number of VMs in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `ZONE`: the zone where the MIG creates VMs.
  * `LIST_OF_ZONES`: a comma separated list of zones where the regional MIG creates VMs. For example, `us-central1-a, us-central1-b, us-central1-c`.



###  REST 

To create a MIG that has bulk creation enabled, make a `POST` request as follows. In the request body, set the `targetSizePolicy.mode` field to `bulk`.

If the instance template that you use specifies the flex-start provisioning model, then you must turn off repairs in the MIG by including the `"instanceLifecyclePolicy": {"defaultActionOnFailure": "DO_NOTHING"}` field in the following requests.

  * To create a zonal MIG, make a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "targetSize": SIZE,
          "targetSizePolicy": {
            "mode": "bulk"
          },
          "instanceLifecyclePolicy": {
              "defaultActionOnFailure": "DO_NOTHING"
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
          "instanceLifecyclePolicy": {
              "defaultActionOnFailure": "DO_NOTHING"
          },
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ]
        }
        




Replace the following:

  * `PROJECT_ID`:the project ID.
  * `ZONE`:the zone where the MIG creates VMs.
  * `REGION`:the region where the MIG creates VMs.
  * `INSTANCE_GROUP_NAME`:the name of the MIG.
  * `SIZE`:the number of VMs in the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`



## What's next

  * Learn how to [view information about MIGs and managed VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).


  * Learn how to [view the actual and forecasted usage of your VMs and GPUs](https://docs.cloud.google.com/capacity-planner/docs/view-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
