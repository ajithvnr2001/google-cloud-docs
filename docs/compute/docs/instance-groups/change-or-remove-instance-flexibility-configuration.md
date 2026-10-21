---
url: https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration/
title: Change or remove instance flexibility \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:22:01.271648+00:00
---

# Change or remove instance flexibility  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Change or remove instance flexibility Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to make changes or remove instance flexibility in a managed instance group (MIG) by editing the instance flexibility policy. It also describes how to update a VM's machine type when the machine type is removed from the instance flexibility configuration.

## Before you begin

  * If you want to create Spot VMs in a MIG, then view the availability of resources before you add VMs to the MIG. Checking the availability of resources helps reduce your chances of encountering resource availability errors. For instructions, see [View resource availability of Spot VMs](https://docs.cloud.google.com/compute/docs/instances/view-vm-availability).
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




## Change instance flexibility configuration

You can make the following changes by editing the instance flexibility configuration in a MIG:

  * Add a machine type to an instance selection
  * Remove a machine type from an instance selection
  * Change the ranks of instance selections
  * Add an instance selection
  * Add minimum CPU platform and disk overrides ([Preview](https://cloud.google.com/products#product-launch-stages))



The MIG applies the changes based on the instance selection names that you specify. Any instance selections that you don't specify remain unchanged. When you make changes to an instance selection, you must specify its full configuration when editing. If you don't specify the full configuration, the MIG will overwrite the unspecified parts of the instance selection. For example, if you want to change only a rank, specify the new rank along with the machine types and any other overrides set in that selection. To view the existing configuration, see [View instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration#view_the_instance_flexibility_configuration).

After you remove a machine type from the configuration, the existing VMs with the removed machine types continue to use them. If you want to change those VMs' machine types, you must update or recreate the specific VMs. For more information, see Update a VM's machine type to use the latest configuration.

To change the instance flexibility configuration in a MIG, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the name of the MIG in which you want to change the instance flexibility.

  3. Click **Edit**.

  4. Click **Instance flexibility** to expand the section.

  5. In the **Instance selections** section, click **Edit selections**.

  6. In the **Instance selections** window, click the expand_more **Toggle** icon of an instance selection to open the **Edit instance selection** view.

When editing an instance selection, you can make the following changes:

     * Change the name and rank of the instance selection. To do this, edit the values in the **Name** and **Rank** fields.
     * Add a new machine type to the selection. To do this, click **Add machine type**.
     * Remove machine types. To do this, select the machine types, and then click **Remove**.
     * Add or modify the minimum CPU platform or disk overrides ([Preview](https://cloud.google.com/products#product-launch-stages)). To do this, follow the prompts in the **Overrides** section.
  7. Modify the selection as required and click **Done**.

  8. After you complete making the changes in the **Instance selections** window, click **Done**.

  9. Click **Save** to apply the changes.




### gcloud

To edit an instance flexibility configuration, use the [beta `instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/update).
    
    
      gcloud beta compute instance-groups managed update INSTANCE_GROUP_NAME \
          --region REGION \
          --instance-flexibility-policy={"instanceSelections": \
            {"INSTANCE_SELECTION_1":{"rank":RANK_1,"machineTypes":["MACHINE_TYPE_1","MACHINE_TYPE_2"],"minCpuPlatform":"MIN_CPU_PLATFORM_1","disks":[{"deviceName":"DEVICE_NAME_1","boot":true,"initializeParams":{"sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"}}]}, \
            "INSTANCE_SELECTION_2":{"rank":RANK_2,"machineTypes":["MACHINE_TYPE_3","MACHINE_TYPE_4"],"minCpuPlatform":"MIN_CPU_PLATFORM_2","disks":[{"deviceName":"DEVICE_NAME_2","boot":true,"initializeParams":{"sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"}}]}}}
    

You can also use a YAML or JSON file to configure the instance flexibility policy. To do so, use the [`--flags-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) instead of the `--instance-flexibility-policy` flag and specify the filename. For example, use `--flags-file=FILE_NAME.YAML`. See [Example for YAML file to configure instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility#yaml-file-example)

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG in which you want to check the instance flexibility configuration.
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_SELECTION`: the name of the instance selection to modify. When updating an instance selection, you must specify its complete configuration, including any properties that you are not changing, to ensure that the MIG retains the unchanged properties.



###  REST 

To edit an instance flexibility configuration, make a `PATCH` request to the [beta `regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch).
    
    
      PATCH https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
      {
        "instanceFlexibilityPolicy": {
          "instanceSelections": {
            "INSTANCE_SELECTION_1": {
              "machineTypes": [
                "MACHINE_TYPE_1",
                "MACHINE_TYPE_2"
              ],
              "minCpuPlatform": "MIN_CPU_PLATFORM_1",
              "disks": [
                DISK_DEFINITION_1
              ],
              "rank": RANK_1
            },
            "INSTANCE_SELECTION_2": {
              "machineTypes": [
                "MACHINE_TYPE_3",
                "MACHINE_TYPE_4"
              ],
              "minCpuPlatform": "MIN_CPU_PLATFORM_2",
              "disks": [
                DISK_DEFINITION_2
              ],
              "rank": RANK_2
            }
          }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG in which you want to check the instance flexibility configuration.
  * `INSTANCE_SELECTION`: the name of the instance selection to modify. When updating an instance selection, you must specify its complete configuration, including any properties that you are not changing, to ensure that the MIG retains the unchanged properties.



## Remove instance flexibility configuration

You can remove all or specific instance selections in a MIG.

  * To remove all instance selections in a MIG, see Remove all instance selections. When you remove all instance selections, the MIG uses the machine type specified in the instance template to create new VMs in the group.

  * To remove individual instance selections by names, see Remove specific instance selections. This removes only specific instance selections and the MIG retains the other ones.




After removing instance selections, the existing VMs that use the machine types from the removed instance selections continue to use the same machine type. For the changes to take effect, you must update or recreate those VMs. For more information, see Update a VM's machine type to use the latest configuration.

### Remove all instance selections

To remove all instance selections, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the name of the MIG in which you want to remove all instance selections.

  3. Click **Edit**.

  4. Click **Instance flexibility** to expand the section.

  5. In the **Instance selections** section, click **Edit selections**.

  6. In the **Instance selections** window, click the delete **Delete** icon next to each instance selection.

  7. Click **Done**.

  8. Click **Save**.




### gcloud

To remove all instance selections in a MIG, use the [`instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
      gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
          --region REGION \
          --remove-instance-selections-all
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG from which you want to remove all the instance selections.
  * `REGION`: the region where the MIG is located.



###  REST 

To remove all instance selections in a MIG, make a `PATCH` request to the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
      {
        "instanceFlexibilityPolicy": {
          "instanceSelections": null
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG from which you want to remove an instance selection.



### Remove specific instance selections

To remove specific instance selections, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the name of the MIG in which you want to remove specific instance selections.

  3. Click **Edit**.

  4. Click **Instance flexibility** to expand the section.

  5. In the **Instance selections** section, click **Edit selections**.

  6. In the **Instance selections** window, click the delete **Delete** icon next to the instance selection that you want to remove.

  7. Click **Done**.

  8. Click **Save**.




### gcloud

To remove specific instance selections in a MIG, use the [`instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
      gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
          --region REGION \
          --remove-instance-selections INSTANCE_SELECTION
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG from which you want to remove an instance selection.
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_SELECTION`: the name of the instance selection which you want to remove. If there are multiple instance selections, provide a comma separated list of the names.



###  REST 

To remove specific instance selections in a MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
      PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
      {
        "instanceFlexibilityPolicy": {
          "instanceSelections": {
            "INSTANCE_SELECTION": null
          }
        }
      }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG from which you want to remove an instance selection.
  * `INSTANCE_SELECTION`: the name of the instance selection which you want to remove. If there are multiple instance selections, specify all of them. For example, `"selection-1": null,"selection-2": null`.



## Update a VM's machine type to use the latest configuration

If any VMs in a MIG use a machine type that was removed from the instance flexibility configuration, then you must update or recreate the VM to update its machine type.

To update or recreate a VM, use one of the following options:

  * [Update the VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#updating_selected_instances) using the `regionInstanceGroupManagers.applyUpdatesToInstances` method. When using the `applyUpdatesToInstances` method, the `mostDisruptiveAllowedAction` field must be `RESTART` OR `REPLACE`.

**Note:** If your instance flexibility configuration contains machine types from different generations of machine series, then set the `mostDisruptiveAllowedAction` field to `REPLACE`. To know the generation of a machine series, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology).
  * [Recreate the VMs](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#recreate_instances) using the `regionInstanceGroupManagers.recreateInstances` method.

  * Recreate the VMs by first [deleting the VMs](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) and then [resizing the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) to the required number of VMs.




## What's next

  * [View instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration).
  * [Add instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
