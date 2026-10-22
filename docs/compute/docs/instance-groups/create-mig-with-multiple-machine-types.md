---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-multiple-machine-types/
title: Create a MIG with multiple machine types \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:18.889798+00:00
---

# Create a MIG with multiple machine types  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-multiple-machine-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG with multiple machine types Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) with _instance flexibility_ , which lets you specify multiple machine types in the MIG.

Instance flexibility helps to improve resource obtainability, particularly for applications that can operate on different machine types and that require large-scale capacity or hardware with high demand. For more information, see [About instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

You can also read about other [basic scenarios for creating a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group).

## Before you begin

  * [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates), which is required in order to create a managed instance group.
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




## Create a MIG with multiple machine types

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



## What's next

  * [Check instance flexibility configuration](https://docs.cloud.google.com/compute/docs/instance-groups/view-instance-flexibility-configuration).
  * [Change instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration#change_instance_flexibility_configuration) to use machine types based on your preferences.
  * [Create a MIG with multiple machine types and preferences](https://docs.cloud.google.com/compute/docs/instance-groups/configure-instance-flexibility#create-mig-with-multiple-machine-types-and-preference).
  * [Remove instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/change-or-remove-instance-flexibility-configuration#remove_instance_flexibility_configuration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
