---
url: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution/
title: Disable and re-enable proactive VM redistribution in a regional MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:17:00.253115+00:00
---

# Disable and re-enable proactive VM redistribution in a regional MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Disable and re-enable proactive VM redistribution in a regional MIG Stay organized with collections  Save and categorize content based on your preferences. 

In a [regional managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), to maintain an even number of virtual machine (VM) instances across the selected zones in the [region](https://docs.cloud.google.com/docs/geography-and-regions), use [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution). This configuration option maximizes the availability of your application in the event of a zone-level failure.

Proactive instance redistribution is turned on by default for regional MIGs. When proactive instance redistribution is turned off, the group does not attempt to proactively redistribute VMs across zones. Turning off proactive instance redistribution is useful if you need to:

  * [Delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) or [abandon](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) VMs from the group without affecting other running VMs. For example, you can delete a batch worker VM after job completion without affecting other workers.
  * Protect VMs with stateful workloads from unwanted automatic deletion due to proactive redistribution.
  * Set the MIG's [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) to `BALANCED` or `ANY_SINGLE_ZONE`.



You can disable proactive instance redistribution when creating a regional MIG. You can also enable or disable it for an existing regional MIG.

**Note:** If you've configured autoscaling, then proactive instance distribution does not affect the [behavior](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#autoscaling_a_regional_mig) of your autoscaled MIGs.

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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Creating a group with proactive instance redistribution disabled

To create a regional MIG with proactive instance redistribution disabled, use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create), Terraform or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/insert).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/)

  2. Click **Create instance group** to create a new instance group.
  3. Assign a name and optionally a description to your instance group.
  4. Choose an instance template for the instance group or create a new one.
  5. Specify the number of VMs for this group. For highly available workloads, remember to [provision](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) enough VMs to support your application if a zone failure happens.
  6. Under **Location** , select **Multiple zones**.
  7. Choose a region and select the zones you want to use.
  8. To disable [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution), under **Instance redistribution** , deselect the **Allow instance redistribution** checkbox.
  9. Continue with the rest of the MIG creation process.



###  gcloud 

To create a new regional MIG without proactive instance redistribution, use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) with the `--instance-redistribution-type` flag set to `NONE`.
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --template INSTANCE_TEMPLATE_NAME \
        --size TARGET_SIZE \
        --zones ZONES \
        --instance-redistribution-type NONE

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name for the MIG
  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to use for the group
  * `TARGET_SIZE`: the target size of the group
  * `ZONES`: the list of zones in a single region where you want to deploy VMs



For example:
    
    
    gcloud compute instance-groups managed create example-rmig \
        --template example-template \
        --size 30 \
        --zones us-east1-b,us-east1-c \
        --instance-redistribution-type NONE

###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).

To disable proactive instance redistribution in a regional MIG, include the `update_policy` block, and set the `instance_redistribution_type` field to `NONE`.
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name                      = "example-rmig"
      region                    = "us-east1"
      distribution_policy_zones = ["us-east1-b", "us-east1-c"]
      update_policy {
        type                         = "PROACTIVE"
        minimal_action               = "REFRESH"
        instance_redistribution_type = "NONE"
        max_unavailable_fixed        = 3
      }
      target_size        = 30
      base_instance_name = "instance"
      version {
        instance_template = google_compute_instance_template.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To create a non-autoscaled regional MIG without proactive instance redistribution, make a `POST` request to the [`regionInstanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) method. In the request body, include the `updatePolicy` property, and set its `instanceRedistributionType` field to `NONE`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
        "name": "INSTANCE_GROUP_NAME",
        "instanceTemplate": "global/instanceTemplates/INSTANCE_TEMPLATE_NAME",
        "targetSize": TARGET_SIZE,
        "distributionPolicy": {
            "zones": [
                {"zone": "zones/ZONE"},
                {"zone": "zones/ZONE"}
            ]
        },
        "updatePolicy": {
            "instanceRedistributionType": "NONE"
        }
    }

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `REGION`: the region for the instance group
  * `INSTANCE_GROUP_NAME`: the name for the MIG
  * `INSTANCE_TEMPLATE_NAME`: the name of the instance template to use for the group
  * `TARGET_SIZE`: the target size of the instance group
  * `ZONE`: the name of a zone in the single region where you want to deploy VMs



## Turning off proactive instance redistribution

To disable or re-enable proactive instance redistribution, use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/patch).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups/)

  2. In the **Name** column of the list, click the name of the instance group that you want to modify.
  3. Click **Edit** to modify this managed instance group.
  4. Click **Location** to expand the section.
  5. In the **Instance redistribution** section, deselect the **Allow instance redistribution** checkbox.
  6. Click **Save**.



###  gcloud 

To turn off proactive instance redistribution, use the [`compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) and set the `--instance-redistribution-type` flag to `NONE` as follows:
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        --instance-redistribution-type NONE \
        --region REGION
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG
  * `REGION`: the region of the instance group



###  REST 

To turn off proactive instance redistribution, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) and set the `instanceRedistributionType` field to `NONE` as follows:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
      {
         "updatePolicy": {
            "instanceRedistributionType": "NONE"
         }
      }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request
  * `REGION`: the region for the instance group
  * `INSTANCE_GROUP_NAME`: the name of the MIG



## Turning on proactive instance redistribution

To turn on proactive instance redistribution, use a similar command as for turning off proactive instance redistribution, but set the instance redistribution type to `PROACTIVE`.

If you manually deleted or abandoned some managed instances resulting in an uneven distribution of VMs across the region, then, before you can re-enable proactive instance redistribution, you must [manually rebalance](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-rebalance-manually) the group. The difference in the number of VMs between any two zones shouldn't exceed 1 VM.

A regional MIG does not allow turning on proactive instance redistribution when VMs are distributed unevenly across zones (the difference in the number of VMs between two zones is 2 or more VMs). This is to prevent an unintended automatic deletion of VMs from zones with more VMs, which would be triggered to achieve even distribution.

## What's next

  * Learn about [Viewing info about MIGs and their VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).
  * Learn about [Working with VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances), including adding, recreating, and removing instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
