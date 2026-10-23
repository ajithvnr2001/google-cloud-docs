---
url: https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone/
title: Repair a VM in an alternate zone \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:27.819149+00:00
---

# Repair a VM in an alternate zone  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/repair-vm-in-alternate-zone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Repair a VM in an alternate zone Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to allow a regional managed instance group (MIG) to repair a virtual machine (VM) instance in an alternate zone when the MIG cannot repair the VM in its original zone. To learn more about repairs in a MIG, see [About repairing VMs for high availability](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair).

When you create a regional MIG, you select one or more zones where the MIG distributes its VMs. By default, if a VM in the MIG fails, the MIG tries to repair that VM in its original zone. You can optionally allow the MIG to repair that VM in one of the other selected zones, which is useful in cases where the MIG cannot repair the VM in its original zone. The MIG picks the alternate zone based on available capacity and quota.

## Limitations

When you configure a regional MIG to repair a VM in alternate zone, the following limitations apply:

  * You must enable [update on repair](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair).

  * Regional MIGs with the following configuration aren't supported:

    * MIGs with [`EVEN`](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#how_even_works) or [`ANY_SINGLE_ZONE`](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#how_any_single_zone_works) target distribution shapes.

    * MIGs with [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration).




## Before you begin

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




## Allow repairs in an alternate zone

To allow a MIG to repair a VM in an alternate zone, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. If you already have a MIG, do the following:

     1. Click the name of the MIG.
     2. Click **Edit**.
  3. If you don't have a MIG yet, do the following:

     1. Click **Create instance group**.
     2. Enter a **Name**.
     3. Select an **Instance template**.
     4. In the **Location** section, select **Multiple zones** , and then select a region and zones.
     5. In the **Target distribution shape** drop-down, select **Balanced** or **Any**.

        * If you select **Balanced** , in the dialog that appears, click **Disable instance redistribution**.

        * If you want to select **Any** , you must first delete the autoscaling configuration. To delete autoscaling, in the **Autoscaling mode** drop-down, click **Delete autoscaling configuration**.

  4. In the **VM instance lifecycle** section, make sure that the following fields are set as follows:

     1. The **Default action on failure** list is set to **Repair instance**.

     2. The **Updates during VM instance repair** is set to **Update the instance configuration**.

     3. In the **Change zone during VM instance repair** section, select the **Allow repair of VMs in an alternate zone** checkbox.

  5. For the other settings, you can either use the default values or modify the fields.

  6. After you finish, click **Save** for an existing MIG or **Create** for a new MIG.




###  gcloud 

To configure an existing MIG to repair VM in an alternate zone, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --on-repair-allow-changing-zone=YES \
        --force-update-on-repair \
        --region=REGION
    

To create a MIG that can repair VM in an alternate zone, use the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
    
    
    gcloud compute instance-groups managed create MIG_NAME \
        --template=INSTANCE_TEMPLATE_URL \
        --size=SIZE \
        --zones=ZONES \
        --target-distribution-shape=SHAPE \
        --instance-redistribution-type=none \
        --on-repair-allow-changing-zone=YES \
        --force-update-on-repair
    

Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SIZE`: the target size of the MIG.
  * `ZONES`: the list of zones in a region where you want to create the VMs in the MIG.
  * `SHAPE`: the target distribution shape. This value can be either `balanced` or `any`.
  * `REGION`: the region where the MIG is located.



###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a MIG that can repair VM in an alternate zone, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      provider           = google-beta
      name               = "example-rmig"
      base_instance_name = "example-rmig-instance"
      region             = "us-central1"
    
      target_size                      = 3
      distribution_policy_target_shape = "BALANCED"
    
      version {
        instance_template = google_compute_instance_template.default.id
      }
    
      instance_lifecycle_policy {
        default_action_on_failure = "REPAIR"
        force_update_on_repair    = "YES"
        on_repair {
          allow_changing_zone = "YES"
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

To configure an existing MIG to repair VM in an alternate zone, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME
    {
        "instanceLifecyclePolicy": {
          "onRepair": {
            "allowChangingZone": "YES"
          },
          "forceUpdateOnRepair": "YES"
        }
    }
    

To create a MIG that can repair VM in an alternate zone, use the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
      "name": "MIG_NAME",
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "targetSize": SIZE,
      "distributionPolicy": {
        "targetShape": "SHAPE"
      }
      "updatePolicy": {
        "instanceRedistributionType": none
      }
      "instanceLifecyclePolicy": {
        "forceUpdateOnRepair": "YES",
        "onRepair": {
          "allowChangingZone": "YES"
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `MIG_NAME`: the name of the MIG.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SIZE`: the target size of the MIG.
  * `SHAPE`: the target distribution shape. This value can be either `BALANCED` or `ANY`.



## Disallow repairs in an alternate zone

If you configured a MIG to repair VM in an alternate zone, then you can restore the default setting in which the MIG repairs the VM in the original zone.

To disallow repairs in an alternate zone, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG.

  3. Click **Edit**.

  4. Go to the **VM instance lifecycle** section.

  5. In the **Change zone during VM instance repair** section, clear the **Allow repair of VMs in an alternate zone** checkbox.

  6. Click **Save**.




###  gcloud 

To disallow repairs in an alternate zone, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update MIG_NAME \
        --on-repair-allow-changing-zone=NO \
        --region=REGION
    

Replace the following:

  * `MIG_NAME`: the name of the MIG.
  * `REGION`: the region where the MIG is located.



###  REST 

To disallow repairs in an alternate zone, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/MIG_NAME
    {
        "instanceLifecyclePolicy": {
          "onRepair": {
            "allowChangingZone": "NO"
          }
        }
    }
    

Replace the following:

  * `PROJECT_ID`: your [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * `REGION`: the region where the MIG is located.
  * `MIG_NAME`: the name of the MIG.



## What's next

  * [Check the repair configuration in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#check_vm_repairs_turned_off).
  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution) to observe how instances are distributed across zones over time.
  * Check the zone of a VM by [listing the managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
