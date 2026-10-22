---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-spot-vms/
title: Create a MIG that uses Spot VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:36.223325+00:00
---

# Create a MIG that uses Spot VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-spot-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG that uses Spot VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a managed instance group (MIG) that uses Spot VMs.

[Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) are virtual machine (VM) instances that you can obtain at a deeply discounted price. However, Compute Engine can stop or delete Spot VMs at any time to reclaim capacity. Use Spot VMs to run fault-tolerant workloads, such as batch processing jobs or stateless applications, at a low cost.

For other methods that you can use to create MIGs, see [Basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group).

## Before you begin

  * Read about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot), especially the [limitations](https://docs.cloud.google.com/compute/docs/instances/spot#limitations). 
  * Verify that you have sufficient quota for the resources that you want to request. For more information, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage). 
    * To prevent Spot VMs from consuming your quotas for standard VMs' CPUs, GPUs, and disks, consider requesting [preemptible quota](https://docs.cloud.google.com/compute/docs/instances/spot#quotas) for Spot VMs. 
  * Before you create Spot VMs for a workload, complete the following steps:

    1. **Configure your workload to manage preemption.** Specifically, we recommend that you either prepare a script to handle preemption that runs as part of your workload or is a file that you can add in VM metadata to run during shutdown. For instructions, see [Manage preemption of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#manage-preemption).

    2. **We strongly recommend that you view data for Spot VMs to help you choose a machine type and location.** By selecting a machine type and location with a higher availability of resources, you can help improve your chances of avoiding resource availability errors and of having a longer uptime before preemption.

       * For historical preemption and pricing data, which is especially helpful when planning long-term workloads, see [View the preemption rate and pricing data for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-spot-preemption-price).

       * For current availability data, which is especially helpful immediately before you create Spot VMs for short-term workloads, see [View the availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).

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

To get the permissions that you need to create MIGs that use Spot VMs, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create MIGs that use Spot VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create MIGs that use Spot VMs:

  * To create an instance template: `compute.instanceTemplates.create` on the project 
  * To create a MIG: `compute.instanceGroupManagers.create` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a MIG that uses Spot VMs

To create a MIG that uses Spot VMs, you must complete the following steps:

  1. Create an instance template configured for creating Spot VMs

  2. Create a regional or zonal MIG




### Create an instance template configured for creating Spot VMs

To create an instance template configured for creating Spot VMs, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instanceTemplates)

  2. Click **Create instance template**. The **Create an instance template** page appears.

  3. In the **Name** field, enter a name for the instance template.

  4. In the **Location** section, select the type of instance template that you want to create:

     * For a regional instance template, select **Regional** , and then select the region in which to create your template. Based on the machine type that you want your Spot VMs to use, specify a [supported region](https://docs.cloud.google.com/compute/docs/regions-zones#available).

     * For a global instance template, select **Global**.

  5. In the **Machine configuration** section, select a supported machine series for Spot VMs.

  6. In the **Provisioning model** section, do the following:

     1. In the **VM provisioning model** list, select **Spot**. The **VM provisioning model advanced settings** section expands.

     2. In the **Preemption notice duration** list, select an option based on how you want to [handle preemption](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#handle-preemption).

        * If you select **120 seconds** (recommended), ensure that you handle preemption within your workload before you create a Spot VM. For example, verify that your workload includes a script to save your progress that waits to run until preemption is detected.

        * If you select **0 seconds (default)** , ensure that you handle preemption using a shutdown script. Before creating a Spot VM, create a file that contains a shutdown script that saves your progress when shutdown is caused by preemption. Attach this shutdown script as explained in a later step.

     3. To specify whether to stop or delete Spot VMs on preemption, in the **On VM termination** list, select one of the following options:

        * To stop Spot VMs, select **Stop**.

        * To delete Spot VMs, select **Delete**.

  7. To add a shutdown script, complete the following steps. If you selected **0 seconds (default)** for the **Preemption notice duration** , then this step is required to handle preemption. Otherwise, if you selected **120 seconds** , then this step is optional.

     1. Expand the **Advanced options** section.
     2. Expand the **Management** section.
     3. In the **Metadata** section, click add **Add item**.
     4. In the **Key** field, enter `shutdown-script` for the metadata key.
     5. In the **Value** field, add the contents of a shutdown script that handles preemption.
  8. Optional: To change the default value boot disk type or image, in the **Boot disk** section, click **Change**. Then, follow the prompts to change the boot disk.

  9. Click **Create**.




###  gcloud 

To create an instance template configured for creating Spot VMs, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create).

The following command creates a regional instance template. If you want to create a global instance template, then use the same command without the `--instance-template-region` flag.
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --instance-template-region=REGION \
        --instance-termination-action=TERMINATION_ACTION \
        --machine-type=MACHINE_TYPE \
        --provisioning-model=SPOT \
        --preemption-notice-duration=PREEMPTION_NOTICE_DURATION \
        --metadata shutdown-script=SHUTDOWN_SCRIPT
    

Replace the following:

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to create.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details). This specifies the most recent, non-deprecated OS image. For example, if you specify `debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

**Note:** If you want to use a specific version of the OS image, such as `debian-12-bookworm-v20240701`, then replace the `--image-family` flag with the `--image` flag.
  * `REGION`: the region where to create the instance template. Based on the machine type that you want the Spot VMs to use, specify a [supported region](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `TERMINATION_ACTION`: whether Compute Engine stops or deletes the Spot VMs on preemption. You must specify to either stop (`STOP`) or delete (`DELETE`) VMs.

  * `MACHINE_TYPE`: a supported machine type for Spot VMs. If you specify an N1 machine type, then you must include the [`--accelerator` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create#--accelerator) to define the number and type of GPUs to attach to your VMs.

  * `PREEMPTION_NOTICE_DURATION`: whether to enable a [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration). For gcloud CLI, the value must be either `120s` or `0s`.

    * If you specify `120s` (recommended), handle preemption within your workload. (Optionally, you can also specify a shutdown script.)

    * If you specify `0s` (default), handle preemption within a shutdown script.

  * `SHUTDOWN_SCRIPT`: a shutdown script.

    * If you set `PREEMPTION_NOTICE_DURATION` to `0s` (default), then, to handle preemption, you must specify a shutdown script. For more information about how to format and specify a shutdown script, see [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).

    * Otherwise, if you don't want to specify a shutdown script, then you can remove the `--metadata shutdown-script` flag.




###  REST 

To create an instance template configured for creating Spot VMs, make one of the following `POST` requests:

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
          "instanceTerminationAction": "TERMINATION_ACTION",
          "provisioningModel": "SPOT",
          "preemptionNoticeDuration": { "seconds": PREEMPTION_NOTICE_DURATION }
        },
        "metadata": {
          "items": [
            {
              "key": "shutdown-script",
              "value": "SHUTDOWN_SCRIPT"
            }
          ]
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the instance template.

  * `REGION`: the region where to create the instance template. Based on the machine type that you want the Spot VMs to use, specify a [supported region](https://docs.cloud.google.com/compute/docs/regions-zones#available).

  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template.

  * `IMAGE_PROJECT`: the image project that contains the image; for example, `debian-cloud`. For more information about the supported image projects, see [Public images](https://docs.cloud.google.com/compute/docs/images#os-compute-support).

  * `IMAGE`: specify one of the following:

    * A specific version of the OS image—for example, `debian-12-bookworm-v20240617`.

    * An [image family](https://docs.cloud.google.com/compute/docs/images/os-details), which must be formatted as `family/IMAGE_FAMILY`. This specifies the most recent, non-deprecated OS image. For example, if you specify `family/debian-12`, the latest version in the Debian 12 image family is used. For more information about using image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

  * `MACHINE_TYPE`: a supported machine type for Spot VMs. If you specify an N1 machine type, then you must include the [`guestAccelerators` field](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert#request-body) to define the number and type of GPUs to attach to your VMs.

  * `TERMINATION_ACTION`: whether Compute Engine stops or deletes the Spot VMs on preemption. You must specify to either stop (`STOP`) or delete (`DELETE`) VMs.

  * `PREEMPTION_NOTICE_DURATION`: whether to enable a [preemption notice duration](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-notice-duration). For REST, the value must be either `120` or `0`.

    * If you specify `120` (recommended), handle preemption within your workload. (Optionally, you can also specify a shutdown script.)

    * If you specify `0` (default), handle preemption within a shutdown script.

  * `SHUTDOWN_SCRIPT`: a shutdown script.

    * If you set `PREEMPTION_NOTICE_DURATION` to `0s` (default), then, to handle preemption, you must specify a shutdown script. For more information about how to format and specify a shutdown script, see [Run shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).

    * Otherwise, if you don't want to specify a shutdown script, then you can remove the `metadata` field and subfields.

  * `TERMINATION_ACTION`: Optional: specify which [termination action](https://docs.cloud.google.com/compute/docs/instances/spot#termination-action) to take when Compute Engine preempts the VM, either `STOP` (default behavior) or `DELETE`.




After you create the instance template, you can [view the template's details](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) to review its properties.

### Create a regional or zonal MIG

To create regional or zonal MIG, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create instance group**. The **Create instance group** page opens.

  3. In the **Name** field, enter a name for the MIG.

  4. In the **Instance template** list, select the instance template that you created in the previous section.

  5. In the **Number of instances** field, enter the number of Spot VMs to create in the MIG. If your workload requires VMs with specific names, then enter `0` to skip the creation of VMs at this stage. After you create the MIG, [add VMs with specific names to it](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

  6. In the **Location** section, specify whether you want to create a zonal or a regional MIG as follows:

     1. To create a zonal MIG, select **Single zone**. Or, to create a regional MIG, select **Multiple zones**.

     2. Select the **Region** and **Zones** for the MIG.

  7. Click **Create**.




###  gcloud 

To create a MIG, use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).

Based on the type of MIG that you want to create, include the following flags in the command:

  * To create a zonal MIG, include the `--zone` flag:
        
        gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
            --size=SIZE \
            --template=INSTANCE_TEMPLATE_URL \
            **--zone= ZONE**
        

  * To create a regional MIG, include the `--region` flag:
        
        gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
            --size=SIZE \
            --template=INSTANCE_TEMPLATE_URL \
            **--region= REGION**
        




Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.

  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you created in the previous section. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or the name of the instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`

    * For a global instance template: `INSTANCE_TEMPLATE_ID`

  * `SIZE`: the number of Spot VMs to create in the MIG. If your workload requires specific VM names, then specify `0` to skip the creation of VMs at this stage. After you create the MIG, [add VMs with specific names to it](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

  * `ZONE`: the zone where to create the zonal MIG. If you use a regional instance template to create the MIG, then you must specify a zone within the same region as the template.

  * `REGION`: the region where to create the regional MIG. If you use a regional instance template to create the MIG, then you must specify the same region as the template's region.




###  REST 

To create a MIG, make a `POST` request to one of the following methods:

  * To create a zonal MIG, make a `POST` request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "versions": [
            {
              "instanceTemplate": "INSTANCE_TEMPLATE_URL"
            }
          ],
          "targetSize": SIZE
        }
        

  * To create a regional MIG, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert):
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
        
        {
          "name": "INSTANCE_GROUP_NAME",
          "instanceTemplate": "INSTANCE_TEMPLATE_URL",
          "targetSize": SIZE
        }
        




Replace the following:

  * `PROJECT_ID`: the ID of the project in which to create the regional or zonal MIG.

  * `ZONE`: the zone where to create the zonal MIG. If you use a regional instance template to create the MIG, then you must specify a zone within the same region as the template.

  * `REGION`: the region where to create the regional MIG. If you use a regional instance template to create the MIG, then you must specify the same region as the template's region.

  * `INSTANCE_GROUP_NAME`: the name of the MIG.

  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you created in the previous section. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or the name of the instance template. Specify one of the following values:

    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`

    * For a global instance template: `INSTANCE_TEMPLATE_ID`

  * `SIZE`: the number of Spot VMs to create in the MIG. If your workload requires specific VM names, then specify `0` to skip the creation of VMs at this stage. After you create the MIG, [add VMs with specific names to it](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).




After you create the MIG, you can [view the MIG's details](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties) to review its properties.

## What's next

  * Learn more about [the best practices for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot#best-practices).

  * Learn more about [repairing VMs for high availability in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

  * Learn more about [autoscaling VMs in MIGs](https://docs.cloud.google.com/compute/docs/autoscaler).

  * Learn more about [stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
