---
url: https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility/
title: Add instance flexibility \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:43.156039+00:00
---

# Add instance flexibility  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add instance flexibility Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to add instance flexibility that lets you set multiple machine types in a MIG.

You can add instance flexibility when creating a MIG or by editing an existing MIG. To add the flexibility, configure an instance flexibility policy in the MIG. The policy overrides the machine type specified in the instance template. Each time the MIG creates a virtual machine (VM) instance, it automatically selects one of the machine types you've listed in the policy based on resource availability. You can also assign ranks to the lists of machine types to indicate your preference.

To know how instance flexibility works in a MIG, see [About instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

## Before you begin

  * Verify that you choose machine types that are supported in the region where your MIG is located. To see the machine types in a region, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). 

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

### Terraform

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Create a MIG with instance flexibility

Before creating a MIG, you must first [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template), if you don't already have one. You can then create a MIG with instance flexibility to override the machine type specified in the instance template.

Create a MIG with instance flexibility in one of the following ways:

  * Use multiple machine types
  * Use multiple machine types and preferences



### Create a MIG with multiple machine types

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**.

  3. In the **Name** field, enter a name for the MIG.

  4. In the **Instance template** list, select the instance template that you want to use for the MIG.

  5. Before you can specify the **Number of instances** and add **Instance selections** , you need to do the following:

     1. Go to the **Location** section on the page and set a location as follows:

        1. Select **Multiple zones**.

        2. In the **Regions** and the **Zones** drop-downs, select a region and the zones in which you want to create the VMs in the MIG. If you selected a regional instance template, then the region of that template is selected by default.

        3. In the **Target distribution shape** field, select **Balanced** , **Any** , or **Any single zone**.

           * If you select **Balanced** or **Any single zone** , then in the dialog that opens, click **Disable instance redistribution**.

           * If you select **Any** , then make sure that the **Allow instance redistribution** checkbox is not selected.

     2. Go to the **Autoscaling** section on the page and delete the autoscaling configuration as follows:

        1. In the **Autoscaling mode** drop-down, click **Delete autoscaling configuration**.

        2. In the dialog that opens, click **Delete**.

     3. Scroll back to the **Number of instances** field.

  6. In the **Number of instances** field, specify the number of VMs that you want in the group.

  7. In the **Instance selections** section, click **Add selections**.

The **Instance selections** window opens. 

     1. Click **Add instance selection**.

     2. In the **New instance selection** section, do the following:

        1. In the **Name** field, enter a name for the instance selection.

        2. In the **Machine types** section, click **Add machine type** , select a machine type that you want to add in the instance selection, and then click **Done**.

Repeat this step for each machine type that you want to add to the instance selection.

     3. After you complete adding the machine types, click **Done**.



* In the **Instance selections** window, click **Done**.

* Leave the other fields in their default settings or modify as needed.

* Click **Create**.

### gcloud

To create a regional MIG with multiple machine types, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) as follows:
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --region REGION \
        --size TARGET_SIZE \
        --template INSTANCE_TEMPLATE_URL \
        --target-distribution-shape SHAPE \
        --instance-redistribution-type none \
        --instance-selection-machine-types MACHINE_TYPE,MACHINE_TYPE,...
    

Zonal MIGs don't support instance flexibility. However, if you want to create a MIG in a single zone, set the target distribution shape to `any-single-zone`. Furthermore, if you want a specific zone, use the `any-single-zone` distribution shape and include the `--zones ZONE` flag.

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `REGION`: the region where you want to create the MIG.
  * `TARGET_SIZE`: the number of VMs you want the MIG to create and maintain.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SHAPE`: the target distribution shape. The value can be `balanced`, `any`, or `any-single-zone`.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG—for example, `n1-standard-16,n2-standard-16,e2-standard-16`.



###  Terraform 

If you haven't already created an instance template, which specifies the VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a regional MIG with multiple machine types, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name               = "flex-igm"
      base_instance_name = "tf-test-flex-igm"
      region             = "us-central1"
    
      target_size                      = 3
      distribution_policy_target_shape = "ANY_SINGLE_ZONE"
    
      version {
        instance_template = google_compute_instance_template.default.id
      }
    
      instance_flexibility_policy {
        instance_selections {
          name          = "default-instance-selection"
          machine_types = ["n1-standard-16", "n2-standard-16", "e2-standard-16"]
        }
      }
    
      update_policy {
        instance_redistribution_type = "NONE"
        type                         = "OPPORTUNISTIC"
        minimal_action               = "REPLACE"
        max_surge_fixed              = 0
        max_unavailable_fixed        = 6
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a regional MIG with multiple machine types, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
      "name": "INSTANCE_GROUP_NAME",
      "targetSize": TARGET_SIZE,
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "distributionPolicy": {
        "targetShape": "SHAPE"
      },
      "updatePolicy": {
        "instanceRedistributionType": "NONE"
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "INSTANCE_SELECTION": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2",
              ...
            ]
          }
        }
      }
    }
    

Zonal MIGs don't support instance flexibility. However, if you want to create a MIG in a single zone, set the target distribution shape to `ANY_SINGLE_ZONE`. Furthermore, if you want a specific zone, use the `ANY_SINGLE_ZONE` distribution shape and include the `distributionPolicy.zones[].zone` field in the request.

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where you want to create the MIG.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of VMs you want the MIG to create and maintain.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SHAPE`: the target distribution shape. The value can be `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`.
  * `INSTANCE_SELECTION`: the name for the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG—for example, `"n1-standard-16","n2-standard-16","e2-standard-16"`.



### Create a MIG with multiple machine types and preferences

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**.

  3. In the **Name** field, enter a name for the MIG.

  4. In the **Instance template** list, select the instance template that you want to use for the MIG.

  5. Before you can specify the **Number of instances** and add **Instance selections** , you need to do the following:

     1. Go to the **Location** section on the page and set a location as follows:

        1. Select **Multiple zones**.

        2. In the **Regions** and the **Zones** drop-downs, select a region and the zones in which you want to create the VMs in the MIG. If you selected a regional instance template, then the region of that template is selected by default.

        3. In the **Target distribution shape** field, select **Balanced** , **Any** , or **Any single zone**.

           * If you select **Balanced** or **Any single zone** , then in the dialog that opens, click **Disable instance redistribution**.

           * If you select **Any** , then make sure that the **Allow instance redistribution** checkbox is not selected.

     2. Go to the **Autoscaling** section on the page and delete the autoscaling configuration as follows:

        1. In the **Autoscaling mode** drop-down, click **Delete autoscaling configuration**.

        2. In the dialog that opens, click **Delete**.

     3. Scroll back to the **Number of instances** field.

  6. In the **Number of instances** field, specify the number of VMs that you want in the group.

  7. In the **Instance selections** section, click **Add selections**.

The **Instance selections** window opens. Repeat the following steps for each instance selection that you want to add in the MIG.

     1. Click **Add instance selection**.

     2. In the **New instance selection** section, do the following:

        1. In the **Name** field, enter a name for the instance selection.

        2. In the **Rank** field, enter the order of preference among the instance selections that you add for the MIG.

        3. In the **Machine types** section, click **Add machine type** , select a machine type that you want to add in the instance selection, and then click **Done**.

Repeat this step for each machine type that you want to add to the instance selection.

     3. After you complete adding the machine types, click **Done**.



* After you complete adding the instance selections, click **Done**.

* Leave the other fields in their default settings or modify as needed.

* Click **Create**.

###  gcloud 

To create a regional MIG with multiple machine types and preferences, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --region REGION \
        --size TARGET_SIZE \
        --template INSTANCE_TEMPLATE_URL \
        --target-distribution-shape SHAPE \
        --instance-redistribution-type none \
        --instance-selection "name=INSTANCE_SELECTION_1,machine-type=MACHINE_TYPE_1,machine-type=MACHINE_TYPE_2,rank=RANK_1" \
        --instance-selection "name=INSTANCE_SELECTION_2,machine-type=MACHINE_TYPE_3,machine-type=MACHINE_TYPE_4,rank=RANK_2"
    

Zonal MIGs don't support instance flexibility. However, if you want to create a MIG in a single zone, set the target distribution shape to `any-single-zone`. Furthermore, if you want a specific zone, use the `any-single-zone` distribution shape and include the `--zones ZONE` flag.

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `REGION`: the region where you want to create the MIG.
  * `TARGET_SIZE`: the number of VMs that you want the MIG to create and maintain.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SHAPE`: the target distribution shape. The value can be `balanced`, `any`, or `any-single-zone`. The other target distribution shapes are not supported.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



###  Terraform 

If you haven't already created an instance template, which specifies the VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a regional MIG with multiple machine types and preferences, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name               = "flex-igm"
      base_instance_name = "tf-test-flex-igm"
      region             = "us-central1"
    
      target_size                      = 3
      distribution_policy_target_shape = "ANY_SINGLE_ZONE"
    
      version {
        instance_template = google_compute_instance_template.default.id
      }
    
      instance_flexibility_policy {
        instance_selections {
          name          = "best-choice"
          rank          = 1
          machine_types = ["n1-standard-1", "n1-standard-2"]
        }
        instance_selections {
          name          = "still-ok"
          rank          = 2
          machine_types = ["n2-standard-1"]
        }
        instance_selections {
          name          = "if-nothing-else"
          rank          = 3
          machine_types = ["e2-standard-2"]
        }
      }
    
      update_policy {
        instance_redistribution_type = "NONE"
        type                         = "OPPORTUNISTIC"
        minimal_action               = "REPLACE"
        max_surge_fixed              = 0
        max_unavailable_fixed        = 6
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a regional MIG with multiple machine types and preferences, make a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
      "name": "INSTANCE_GROUP_NAME",
      "targetSize": TARGET_SIZE,
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "distributionPolicy": {
        "targetShape": "SHAPE"
      },
      "updatePolicy": {
        "instanceRedistributionType": "NONE"
      },
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "INSTANCE_SELECTION_1": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2",
              ...
            ],
            "rank": RANK_1
          },
          "INSTANCE_SELECTION_2": {
            "machineTypes": [
              "MACHINE_TYPE_3",
              "MACHINE_TYPE_4",
              ...
            ],
            "rank": RANK_2
          },
          ...
        }
      }
    }
    

Zonal MIGs don't support instance flexibility. However, if you want to create a MIG in a single zone, set the target distribution shape to `ANY_SINGLE_ZONE`. Furthermore, if you want a specific zone, use the `ANY_SINGLE_ZONE` distribution shape and include the `distributionPolicy.zones[].zone` field in the request.

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where you want to create the MIG.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of VMs that you want the MIG to create and maintain.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SHAPE`: the target distribution shape. The value can be `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`. The other target distribution shapes are not supported.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



### Create a MIG with multiple machine types, preferences, and additional overrides

**Preview — Minimum CPU platform and disk overrides**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When creating a MIG with multiple machine types, optionally, you can set a minimum CPU platform and disk definitions for each instance selection.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click **Create instance group**.

  3. In the **Name** field, enter a name for the MIG.

  4. In the **Instance template** list, select the instance template that you want to use for the MIG.

  5. Before you can specify the **Number of instances** and add **Instance selections** , you need to do the following:

     1. Go to the **Location** section on the page and set a location as follows:

        1. Select **Multiple zones**.

        2. In the **Regions** and the **Zones** drop-downs, select a region and the zones in which you want to create the VMs in the MIG. If you selected a regional instance template, then the region of that template is selected by default.

        3. In the **Target distribution shape** field, select **Balanced** , **Any** , or **Any single zone**.

           * If you select **Balanced** or **Any single zone** , then in the dialog that opens, click **Disable instance redistribution**.

           * If you select **Any** , then make sure that the **Allow instance redistribution** checkbox is not selected.

     2. Go to the **Autoscaling** section on the page and delete the autoscaling configuration as follows:

        1. In the **Autoscaling mode** drop-down, click **Delete autoscaling configuration**.

        2. In the dialog that opens, click **Delete**.

     3. Scroll back to the **Number of instances** field.

  6. In the **Number of instances** field, specify the number of VMs that you want in the group.

  7. In the **Instance selections** section, click **Add selections**.

The **Instance selections** window opens. Repeat the following steps for each instance selection that you want to add in the MIG.

     1. Click **Add instance selection**.

     2. In the **New instance selection** section, do the following:

        1. In the **Name** field, enter a name for the instance selection.

        2. In the **Rank** field, enter the order of preference among the instance selections that you add for the MIG.

        3. In the **Machine types** section, click **Add machine type** , select a machine type that you want to add in the instance selection, and then click **Done**.

Repeat this step for each machine type that you want to add to the instance selection.

        4. If you want to override the minimum CPU platform specified in the instance template, then select the **Override CPU platform for this selection** checkbox. In the **CPU platform** list, select the platform that you want to use for the instance selection.

        5. If you want to override the disk configuration specified in the instance template or to attach a storage, then select the **Override disks** checkbox.

           * To override the boot disk, in the **Boot disk** section, click **Change** , and follow the prompts.

           * To attach a storage, click **Add new disk** or **Attach existing disk** , and follow the prompts.

        6. After you complete adding the machine types and the overrides, click **Done**.

  8. After you complete adding the instance selections, click **Done**.

  9. Leave the other fields in their default settings or modify as needed.

  10. Click **Create**.




###  gcloud 

Use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create).
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --region REGION \
        --size TARGET_SIZE \
        --template INSTANCE_TEMPLATE_URL \
        --force-update-on-repair \
        --target-distribution-shape SHAPE \
        --instance-redistribution-type none \
        --instance-flexibility-policy={"instanceSelections": \
            {"INSTANCE_SELECTION_1":{"rank":RANK_1,"machineTypes":["MACHINE_TYPE_1","MACHINE_TYPE_2"],"minCpuPlatform":"MIN_CPU_PLATFORM_1","disks":[{"deviceName":"DEVICE_NAME_1","boot":true,"initializeParams":{"sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"}}]}, \
            "INSTANCE_SELECTION_2":{"rank":RANK_2,"machineTypes":["MACHINE_TYPE_3","MACHINE_TYPE_4"],"minCpuPlatform":"MIN_CPU_PLATFORM_2","disks":[{"deviceName":"DEVICE_NAME_2","boot":true,"initializeParams":{"sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"}}]}}}
    

You can also use a YAML or JSON file to configure the instance flexibility policy. To do so, use the [`--flags-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) instead of the `--instance-flexibility-policy` flag and specify the filename. For example, use `--flags-file=FILE_NAME.YAML`.

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `REGION`: the region where you want to create the MIG.
  * `TARGET_SIZE`: the number of VMs that you want the MIG to create and maintain.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SHAPE`: the target distribution shape. The value can be `balanced`, `any`, or `any-single-zone`. The other target distribution shapes are not supported.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `MIN_CPU_PLATFORM`: the minimum CPU platform for the instances.
  * `DEVICE_NAME`: the device name for the disk.
  * `IMAGE_PROJECT`: the project ID of the source image.
  * `IMAGE_NAME`: the name of the source image.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



###  Terraform 

If you haven't already created an instance template, which specifies the VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a regional MIG with multiple machine types, preferences, and additional overrides, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      provider           = google-beta
      name               = "flex-igm"
      base_instance_name = "flex-igm-instance"
      region             = "us-central1"
    
      target_size                      = 2
      distribution_policy_target_shape = "ANY"
    
      version {
        instance_template = google_compute_instance_template.default.id
      }
    
      instance_flexibility_policy {
        instance_selections {
          name          = "first-preference"
          rank          = 1
          machine_types = ["n4-standard-4"]
          disks {
            auto_delete  = true
            device_name  = "boot"
            boot         = true
            source_image = "projects/debian-cloud/global/images/family/debian-12"
            disk_size_gb = 10
            disk_type    = "hyperdisk-balanced"
          }
        }
    
        instance_selections {
          name             = "second-preference"
          rank             = 2
          machine_types    = ["n2-standard-4"]
          min_cpu_platform = "Intel Ice Lake"
          disks {
            auto_delete  = true
            device_name  = "boot"
            boot         = true
            source_image = "projects/debian-cloud/global/images/family/debian-12"
            disk_size_gb = 10
            disk_type    = "pd-ssd"
          }
        }
      }
    
      instance_lifecycle_policy {
        force_update_on_repair = "YES"
      }
    
      update_policy {
        instance_redistribution_type = "NONE"
        type                         = "OPPORTUNISTIC"
        minimal_action               = "REPLACE"
        max_surge_fixed              = 0
        max_unavailable_fixed        = 6
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

Make a `POST` request to the [beta `regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/insert).
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
    "name": "INSTANCE_GROUP_NAME",
    "targetSize": "TARGET_SIZE",
    "instanceTemplate": "INSTANCE_TEMPLATE_URL",
    "distributionPolicy": {
      "targetShape": "SHAPE"
    },
    "updatePolicy": {
      "instanceRedistributionType": "NONE"
    },
    "instanceLifecyclePolicy": {
      "forceUpdateOnRepair": "YES",
    },
    "instanceFlexibilityPolicy": {
      "instanceSelections": {
        "INSTANCE_SELECTION_1": {
          "machineTypes": ["MACHINE_TYPE_1", "MACHINE_TYPE_2", …],
          "minCpuPlatform": "MIN_CPU_PLATFORM_1",
          "disks": [
            {
              "deviceName": "DEVICE_NAME_1",
              "initializeParams": {
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"
              },
              "boot": true
            }
          ],
          "rank": RANK_1
        },
        "INSTANCE_SELECTION_2": {
          "machineTypes": ["MACHINE_TYPE_3", "MACHINE_TYPE_4", …],
          "minCpuPlatform": "MIN_CPU_PLATFORM_2",
          "disks": [
            {
              "deviceName": "DEVICE_NAME_2",
              "initializeParams": {
                "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"
              },
              "boot": true
            }
          ],
          "rank": RANK_2
        }
      }
    }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where you want to create the MIG.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `TARGET_SIZE`: the number of VMs that you want the MIG to create and maintain.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SHAPE`: the target distribution shape. The value can be `BALANCED`, `ANY`, or `ANY_SINGLE_ZONE`. The other target distribution shapes are not supported.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `MIN_CPU_PLATFORM`: the minimum CPU platform for the instances.
  * `DEVICE_NAME`: the device name for the disk.
  * `IMAGE_PROJECT`: the project ID of the source image.
  * `IMAGE_NAME`: the name of the source image.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



## Add instance flexibility to an existing MIG

You can add instance flexibility to an existing MIG. You can set multiple machine types and also set preferences for certain machine types.

If your MIG already has VMs in it, those VMs continue to use the machine type specified in the instance template. If you want the existing VMs in the MIG to use the machine types from the instance flexibility policy, then, after you add the policy, [delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) the existing VMs and then [resize the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) to the required number of VMs. When resizing, the new VMs will use the machine types from the policy.

To modify an existing instance flexibility policy, see [Change instance flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration#change_instance_flexibility_configuration).

Add instance flexibility to a MIG in one of the following ways:

  * Add multiple machine types
  * Add multiple machine types and preferences
  * Add multiple machine types, preferences, and additional overrides



### Add multiple machine types

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the name of the MIG in which you want to set multiple machine types.

  3. Click **Edit**.

  4. Click **Instance flexibility** to expand the section.

  5. In the **Instance selections** section, click **Add selections**.

The **Instance selections** window opens. 

     1. Click **Add instance selection**.

     2. In the **New instance selection** section, do the following:

        1. In the **Name** field, enter a name for the instance selection.

        2. In the **Machine types** section, click **Add machine type** , select a machine type that you want to add in the instance selection, and then click **Done**.

Repeat this step for each machine type that you want to add to the instance selection.

     3. After you complete adding the machine types, click **Done**.



* In the **Instance selections** window, click **Done**.

* Click **Save**.

###  gcloud 

To add multiple machine types to an existing MIG, use the [`instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update).
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --region REGION \
        --instance-selection-machine-types MACHINE_TYPE,MACHINE_TYPE,...
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `REGION`: the region where the MIG is located.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.



###  REST 

To add multiple machine types to an existing MIG, make a `PATCH` request to the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
        "INSTANCE_SELECTION": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2"
              ...
            ]
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



### Add multiple machine types and preferences

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the name of the MIG in which you want to set multiple machine types.

  3. Click **Edit**.

  4. Click **Instance flexibility** to expand the section.

  5. In the **Instance selections** section, click **Add selections**.

The **Instance selections** window opens. Repeat the following steps for each instance selection that you want to add in the MIG.

     1. Click **Add instance selection**.

     2. In the **New instance selection** section, do the following:

        1. In the **Name** field, enter a name for the instance selection.

        2. In the **Rank** field, enter the order of preference among the instance selections that you add for the MIG.

        3. In the **Machine types** section, click **Add machine type** , select a machine type that you want to add in the instance selection, and then click **Done**.

Repeat this step for each machine type that you want to add to the instance selection.

     3. After you complete adding the machine types, click **Done**.



* After you complete adding the instance selections, click **Done**.

* Click **Save**.

### gcloud

To add multiple machine types and preferences to an existing MIG, use the [`instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update)
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --region REGION \
        --instance-selection "name=INSTANCE_SELECTION_1,machine-type=MACHINE_TYPE_1,machine-type=MACHINE_TYPE_2,rank=RANK_1" \
        --instance-selection "name=INSTANCE_SELECTION_2,machine-type=MACHINE_TYPE_3,machine-type=MACHINE_TYPE_4,rank=RANK_2"
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



###  REST 

To add multiple machine types and preferences to an existing MIG, make a `PATCH` request to the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "instanceFlexibilityPolicy": {
        "instanceSelections": {
          "INSTANCE_SELECTION_1": {
            "machineTypes": [
              "MACHINE_TYPE_1",
              "MACHINE_TYPE_2"
            ],
            "rank": RANK_1
          },
          "INSTANCE_SELECTION_2": {
            "machineTypes": [
              "MACHINE_TYPE_3",
              "MACHINE_TYPE_4"
            ],
            "rank": RANK_2
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



### Add multiple machine types, preferences, and additional overrides

**Preview — Minimum CPU platform and disk overrides**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups/list)

  2. Click the name of the MIG in which you want to set multiple machine types.

  3. Click **Edit**.

  4. Click **Instance flexibility** to expand the section.

  5. In the **Instance selections** section, click **Add selections**.

The **Instance selections** window opens. Repeat the following steps for each instance selection that you want to add in the MIG.

     1. Click **Add instance selection**.

     2. In the **New instance selection** section, do the following:

        1. In the **Name** field, enter a name for the instance selection.

        2. In the **Rank** field, enter the order of preference among the instance selections that you add for the MIG.

        3. In the **Machine types** section, click **Add machine type** , select a machine type that you want to add in the instance selection, and then click **Done**.

Repeat this step for each machine type that you want to add to the instance selection.

        4. If you want to override the minimum CPU platform specified in the instance template, then select the **Override CPU platform for this selection** checkbox. In the **CPU platform** list, select the platform that you want to use for the instance selection.

        5. If you want to override the disk configuration specified in the instance template or to attach a storage, then select the **Override disks** checkbox.

           * To override the boot disk, in the **Boot disk** section, click **Change** , and follow the prompts.

           * To attach a storage, click **Add new disk** or **Attach existing disk** , and follow the prompts.

        6. After you complete adding the machine types and the overrides, click **Done**.

  6. After you complete adding the instance selections, click **Done**.

  7. Click **Save**.




### gcloud

To add multiple machine types, preferences, and instance property overrides to an existing MIG, use the [beta `instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/update).

**Important:** When updating the instance flexibility policy, you must always specify all instance selection properties. Compute Engine will overwrite any properties that are not included in your update command. To view the existing configuration, see [View instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration#instance-flexibility-policy).
    
    
    gcloud beta compute instance-groups managed update INSTANCE_GROUP_NAME \
        --region REGION \
        --instance-flexibility-policy= '{"instanceSelections": \
            {"INSTANCE_SELECTION_1":{"rank":RANK_1,"machineTypes":["MACHINE_TYPE_1","MACHINE_TYPE_2"],"minCpuPlatform":"MIN_CPU_PLATFORM_1","disks":[{"device-name":"DEVICE_NAME_1","boot":true,"initializeParams":{"sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"}}]}, \
            "INSTANCE_SELECTION_2":{"rank":RANK_2,"machineTypes":["MACHINE_TYPE_3","MACHINE_TYPE_4"],"minCpuPlatform":"MIN_CPU_PLATFORM_2","disks":[{"device-name":"DEVICE_NAME_2","boot":true,"initializeParams":{"sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"}}]}}}'
    

You can also use a YAML or JSON file to configure the instance flexibility policy. To do so, use the [`--flags-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) instead of the `--instance-flexibility-policy` flag and specify the filename. For example, use `--flags-file=FILE_NAME.YAML`.

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `MIN_CPU_PLATFORM`: the minimum CPU platform for the instances.
  * `DEVICE_NAME`: the device name for the disk.
  * `IMAGE_PROJECT`: the project ID of the source image.
  * `IMAGE_NAME`: the name of the source image.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



###  REST 

To add multiple machine types, preferences, and instance property overrides to an existing MIG, make a `PATCH` request to the [beta `regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/patch).

**Important:** When updating the instance flexibility policy, you must always specify all instance selection properties. Compute Engine will overwrite any properties that are not included in your update request. To view the existing configuration, see [View instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration#instance-flexibility-policy).
    
    
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
              {
                "deviceName": "DEVICE_NAME_1",
                "initializeParams": {
                  "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"
                },
                "boot": true
              }
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
              {
                "deviceName": "DEVICE_NAME_2",
                "initializeParams": {
                  "sourceImage":"projects/IMAGE_PROJECT/global/images/IMAGE_NAME"
                },
                "boot": true
              }
            ],
            "rank": RANK_2
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `INSTANCE_SELECTION`: the name of the list of machine types.
  * `MACHINE_TYPE`: the machine types that you want to configure in the MIG.
  * `MIN_CPU_PLATFORM`: the minimum CPU platform for the instances.
  * `DEVICE_NAME`: the device name for the disk.
  * `IMAGE_PROJECT`: the project ID of the source image.
  * `IMAGE_NAME`: the name of the source image.
  * `RANK`: a number representing your order of preference for instance selection. A lower value means a higher preference.



## Example for YAML file to configure instance flexibility

You can use a YAML or JSON file to configure the instance flexibility policy. To do so, use the [`--flags-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/flags-file) in your gcloud CLI command and specify the filename. For example, use `--flags-file=FILE_NAME.YAML`.

The following is an example of YAML file:
    
    
    --instance-flexibility-policy:
      instanceSelections:
        first-preference:
          rank: 1
          machineTypes:
            - n2-standard-8
          minCpuPlatform: "Intel Ice Lake"
          disks:
            - deviceName: data-disk
              boot: false
              initializeParams:
                sourceImage: projects/debian-cloud/global/images/debian-12
                diskType: pd-ssd
    

## What's next

  * [View the instance flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration).
  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution) to view how instances are distributed across machine types and zones.
  * [Change or remove flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
