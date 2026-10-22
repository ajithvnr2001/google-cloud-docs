---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms/
title: Create a MIG that uses Flex-start VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:22.602560+00:00
---

# Create a MIG that uses Flex-start VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG that uses Flex-start VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a managed instance group (MIG) that uses Flex-start virtual machine (VM) instances. [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms) run uninterrupted for up to seven days and help you obtain high-demand resources, such as GPUs or TPUs, at a discounted price. These features make Flex-start VMs a cost-effective solution for running short-duration workloads, such as model fine-tuning and batch inference workloads.

The steps in this document explain how to create a MIG that creates individual Flex-start VMs as resources become available. Thus, the MIG might initially create only a portion of the requested VMs, and then add the remaining VMs later as capacity permits. If you want to create Flex-start VMs all at once in a MIG, then use one of the following methods:

  * To create GPU or H4D Flex-start VMs, see [About MIG resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

  * To create TPU Flex-start VMs, see [TPU instances in MIGs](https://docs.cloud.google.com/compute/docs/tpus/tpus-and-migs).




For other methods that you can use to create MIGs, see [Basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group).

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

To get the permissions that you need to create MIGs that use Flex-start VMs, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create MIGs that use Flex-start VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create MIGs that use Flex-start VMs:

  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To create a MIG: `compute.instanceGroupManagers.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a MIG that uses Flex-start VMs

To create a MIG that uses Flex-start VMs, you must complete the following steps:

  1. Create an instance template that's configured for creating Flex-start VMs

  2. Create a regional or zonal MIG




### Create an instance template that's configured for creating Flex-start VMs

You must create an instance template that's configured for creating Flex-start VMs, as described in this section. After you create the template, you use it to create the MIG.

**Note:** If you want to run data science or machine learning (ML) workloads, then we recommend that you specify a Deep Learning VM Images image in your instance template. Deep Learning VM is a set of prepackaged OS images that contain ML frameworks and essential tools. For more information, see [Choose an image](https://docs.cloud.google.com/deep-learning-vm/docs/images) in the Deep Learning VM documentation.

To create an instance template that's configured for creating Flex-start VMs, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page appears.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select the type of instance template that you want to create:

     * For a regional instance template, select **Regional** , and then select a region that supports [GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available), or [TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all).

     * For a global instance template, select **Global**.

  5. In the **Machine configuration** section, select a machine type to use for your Flex-start VMs.

  6. In the **Provisioning model** section, do the following:

     1. In the **VM provisioning model** list, select **Flex-start**.

     2. To set a run duration for the VMs that are created through the instance template, in the **Enter number of hours** field, enter the number of hours that the VMs run for. The value must be between one hour (`1`) and seven days (`168`). When the VMs reach the end of their run duration, Compute Engine deletes each VM individually relative to its own creation time.

  7. Optional: To change the default value boot disk type or image, in the **Boot disk** section, click **Change**. Then, follow the prompts to change the boot disk.

  8. Click **Create**.




###  gcloud 

To create an instance template that's configured for creating Flex-start VMs, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The following command creates a regional instance template. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
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

  * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which specifies the most recent, non-deprecated OS image. For example, if you specify `debian-12`, you use the latest version in the Debian 12 image family. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

**Note:** If you want to use a specific version of the OS image, such as `debian-12-bookworm-v20240701`, then replace the `--image-family` flag with the `--image` flag.
  * `REGION`: the region in which to create the instance template. Specify a region that supports [GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available), or [TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all).

  * `MACHINE_TYPE`: the machine type to use for your Flex-start VMs. If you specify an N1 machine type, then you must include the [`--accelerator` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--accelerator) to define the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration you want the requested VMs to run. When the VMs reach the end of their run duration, Compute Engine deletes each VM individually relative to its own creation time. You must format the run duration as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s` respectively. For example, specify `30m` for 30 minutes or `1d2h3m4s` for one day, two hours, three minutes, and four seconds. The value must be between 10 minutes and seven days.




###  REST 

To create an instance template that's configured for creating Flex-start VMs, make one of the following `POST` requests:

  * To create a regional instance template: [`regionInstanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/insert)

  * To create a global instance template: [`instanceTemplates.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert)




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

  * `REGION`: the region in which to create the instance template. Specify a region that supports [GPU or H4D machine types](https://docs.cloud.google.com/compute/docs/regions-zones#available), or [TPU machine types](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms#limitations-all).

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This value specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: the machine type to use for your Flex-start VMs. If you specify an N1 machine type, then you must include the [`guestAccelerators` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert#request-body) to define the number and type of GPUs to attach to your VMs.

  * `RUN_DURATION`: the duration, in seconds, you want the requested VMs to run. When the VMs reach the end of their run duration, Compute Engine deletes each VM individually relative to its own creation time. The run duration must be between `600`, which is 600 seconds (10 minutes), and `604800`, which is 604,800 seconds (seven days).




After you create the instance template, you can [view the template's details](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to review its properties.

### Create a regional or zonal MIG

Create a regional or zonal MIG as described in this section. You must not configure [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) and must turn off [repairs](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair). If your requested resources are unavailable, then Compute Engine keeps attempting to allocate resources until the request succeeds, you [reduce the number of VMs in the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group), or you delete your MIG.

To create regional or zonal MIG, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**. The **Create instance group** page appears.

  3. In the **Name** field, enter a name for the MIG.

  4. In the **Instance template** list, select the instance template that you created in the previous section.

  5. In the **Number of instances** field, enter the number of Flex-start VMs to create in the MIG. If your workload requires specific VM names, then enter `0` to not create any VMs. After you create the MIG, [add VMs with specific names to it](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

  6. In the **Location** section, specify whether you want to create a zonal or a regional MIG as follows:

     1. To create a zonal MIG, select **Single zone**. Or, to create a regional MIG, select **Multiple zones**.

     2. Select the **Region** and **Zones** for the MIG.

     3. If you're creating a regional MIG, then do the following:

        1. In the **Target distribution shape** field, select **Any single zone**.

        2. In the dialog that appears, click **Disable instance redistribution**.

  7. To delete the autoscaling configuration, in the **Autoscaling** section, do the following:

     1. Click settings **Configure autoscaling**.

     2. In the **Autoscaling mode** list, click **Delete autoscaling configuration**.

     3. In the confirmation dialog, click **Delete**.

  8. To turn off repairs, in the **Action on failure** section, in the **Default action on failure** list, select **No action**.

  9. Click **Create**.




###  gcloud 

To create a MIG, use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

Based on the type of MIG that you want to create, include the following flags in the command:

  * To create a zonal MIG, include the `--zone` flag:
        
        gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
            --default-action-on-vm-failure=do-nothing \
            --size=SIZE \
            --template=INSTANCE_TEMPLATE_URL \
            **--zone= ZONE**
        

  * To create a regional MIG, include the `--region` and `--target-distribution-shape` flags:
        
        gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
            --default-action-on-vm-failure=do-nothing \
            --size=SIZE \
            --template=INSTANCE_TEMPLATE_URL \
            **--region= REGION** \
            **--target-distribution-shape= SHAPE**
        




Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.

  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you created in the previous section. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or the name of the instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`

    * For a global instance template: `INSTANCE_TEMPLATE_ID`

  * `SIZE`: the number of Flex-start VMs to create in the MIG. If your workload requires specific VM names, then specify `0` to not create any VMs. After you create the MIG, [add VMs with specific names to it](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

  * `ZONE`: the zone in which to create the zonal MIG. If you use a regional instance template to create the MIG, then you must specify a zone within the same region as the template.

  * `REGION`: the region in which to create the regional MIG. If you use a regional instance template to create the MIG, then you must specify the same region as the template's region.

  * `SHAPE`: how your MIG distributes the Flex-start VMs across zones in your regional MIG. Specify one of the following values:

    * To create VMs in multiple zones based on availability: `ANY`

    * To create VMs in a single zone based on availability: `ANY_SINGLE_ZONE`

For more information, see [Regional MIG target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).




###  REST 

To create a MIG, make a `POST` request to one of the following methods:

  * To create a zonal MIG, make the following request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ],
          "instanceLifecyclePolicy": {
            "defaultActionOnFailure": "DO_NOTHING"
          },
          "targetSize": SIZE
        }
        

  * To create a regional MIG, make the following request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "instanceTemplate": "INSTANCE_TEMPLATE_URL",
          "instanceLifecyclePolicy": {
            "defaultActionOnFailure": "DO_NOTHING"
          },
          "targetSize": SIZE,
          "distributionPolicy": {
            "targetShape": "SHAPE"
          }
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the regional or zonal MIG.

  * `ZONE`: the zone in which to create the zonal MIG. If you use a regional instance template to create the MIG, then you must specify a zone within the same region as the template.

  * `REGION`: the region in which to create the regional MIG. If you use a regional instance template to create the MIG, then you must specify the same region as the template's region.

  * `INSTANCE_GROUP_NAME`: the name of the MIG.

  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you created in the previous section. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or the name of the instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`

    * For a global instance template: `INSTANCE_TEMPLATE_ID`

  * `SIZE`: the number of Flex-start VMs to create in the MIG. If your workload requires specific VM names, then specify `0` to not create any VMs. After you create the MIG, [add VMs with specific names to it](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

  * `SHAPE`: how your MIG distributes the Flex-start VMs across zones in your regional MIG. Specify one of the following values:

    * To create VMs in multiple zones based on availability: `ANY`

    * To create VMs in a single zone based on availability: `ANY_SINGLE_ZONE`

For more information, see [Regional MIG target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape).




## What's next

  * Learn how to [view info about MIGs and managed VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).

  * Learn how to [view the actual and forecasted usage of your VMs, GPUs, and TPUs](https://docs.cloud.google.com/capacity-planner/docs/view-data).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
