---
url: https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups/
title: Create a MIG with VMs in multiple zones in a region \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:43.516417+00:00
---

# Create a MIG with VMs in multiple zones in a region  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG with VMs in multiple zones in a region Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that has its VMs spread across multiple zones in a region. Spreading your application load across multiple zones protects your workload against zonal failures. If a zonal failure happens, your application can continue serving from instances running in the remaining available zones in the same region.

This type of MIG is also known as a _regional MIG_. For more information, see [About regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).

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




## Limitations

To see the full list of MIG limitations, which varies based on the configuration that you use, see [MIG limitations](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations).

## Create a MIG with VMs in multiple zones in a region

Use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create), Terraform, or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/insert).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups?walkthrough_id=compute--instance-groups--create-regional-mig&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create instance group** to create a new instance group. 
  3. Select one of the **New managed instance group options** : 
     * Stateless (default) 
     * [Stateful](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs)
  4. Assign a name and optionally a description to your instance group. 
  5. Choose an instance template for the instance group or [create a new one](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates). 
  6. In **Number of instances** or in **Autoscaling** , specify the number of instances for this group. Remember to [provision](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) enough VMs to support your application if a zone failure happens. 
  7. For **Location** , select **Multiple zones**. 
  8. Choose a region and select the zones you want to use. If you chose a regional instance template, then the **Region** is automatically selected based on the template's region. 
  9. Under **Target distribution shape** , select **Even**. If you want to select a different shape, see [Set a target distribution shape for VMs in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape). 
  10. If you want to disable [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution), then under **Instance redistribution** , deselect the **Allow instance redistribution** checkbox. 
  11. Continue with the rest of the MIG creation process. 
  12. To create the MIG, click **Create**.



###  gcloud 

All MIGs require an instance template. If you don't have one, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates). For example, the following command creates an instance template in the `us-east1` region with default instance properties:
    
    
    gcloud compute instance-templates create example-template --instance-template-region us-east1

When you create the MIG, you can specify either the ID or the name of an instance template. Google recommends that you specify the ID because, unlike names, instance template IDs can't be reused. To view the unique ID of the instance template that you created, use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe):
    
    
    gcloud compute instance-templates describe example-template --region us-east1 --format="value(id)"

Next, use the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) with the `--region` flag. For example, the following command creates a regional MIG in three zones within the `us-east1` region:
    
    
    gcloud compute instance-groups managed create example-rmig \
        --template projects/my-project/regions/us-east1/instanceTemplates/1234567890 \
        --size 30 \
        --region us-east1

If you want to select [specific zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) that the group should use, provide the `--zones` flag:
    
    
    gcloud compute instance-groups managed create example-rmig \
        --template projects/my-project/regions/us-east1/instanceTemplates/1234567890 \
        --size 30 \
        --zones us-east1-b,us-east1-c

If you don't need to use specific zones, you can specify all zones and use a balanced distribution shape. For more information, see Distribution of VMs across zones.

If you want to disable proactive instance redistribution, see Proactive instance redistribution.

###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a regional MIG, you can use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_region_instance_group_manager" "default" {
      name                      = "example-rmig"
      region                    = "us-east1"
      distribution_policy_zones = ["us-east1-b", "us-east1-c"]
      target_size               = 30
      base_instance_name        = "instance"
      version {
        instance_template = google_compute_instance_template.default.id
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

All MIGs require an instance template. If you don't have one, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

When you create the MIG, you can specify either the ID or the name of an instance template. Google recommends that you specify the ID because, unlike names, instance template IDs can't be reused. To view the unique ID of the instance template that you created, use the `get` method on the [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceTemplates/get) or [global instance template](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/get) that you created.

Next, construct a `POST` request to the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/v1/regionInstanceGroupManagers/insert). In the request body, specify the group name, group size, and the URL to the instance template. Optionally, specify other fields, such as the base name for instances in the group.

**Note:** When using REST to work with a regional MIG, always use the [`regionInstanceGroupManagers` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
      "baseInstanceName": "BASE_INSTANCE_NAME",
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "name": "INSTANCE_GROUP_NAME",
      "targetSize": "TARGET_SIZE"
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `REGION`: the region for the group.
  * `BASE_INSTANCE_NAME`: (optional) the instance name for each VM instance that is created as part of the group. For example, a base instance name of `example-instance` creates instances that have names like `example-instance-[RANDOM_STRING]` where `[RANDOM_STRING]` is generated by the server.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `TARGET_SIZE`: the target number of VMs for the group.



If you want to [select specific zones](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) or if you are creating VMs in a region with less than or more than three zones, include the `distributionPolicy` property in your request and supply a list of zones. Replace `ZONE` with the name of a zone to create VMs in.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers
    
    {
      "baseInstanceName": "BASE_INSTANCE_NAME",
      "instanceTemplate": "INSTANCE_TEMPLATE_URL",
      "name": "INSTANCE_GROUP_NAME",
      "targetSize": "TARGET_SIZE",
      **"distributionPolicy": {
         "zones": [
           {"zone": "zones/ ZONE"},
           {"zone": "zones/ZONE"}
          ]
       }**
    }

For example, the following creates a regional MIG named `example-rmig` with 10 managed instances distributed across `us-east1-b` and `us-east1-c` zones:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/myproject/regions/us-east1/instanceGroupManagers
    
    {
      "instanceTemplate": "projects/my-project/regions/us-east1/instanceTemplates/1234567890",
      "name": "example-rmig",
      "targetSize": 10,
      "distributionPolicy": {
          "zones": [
            {"zone": "zones/us-east1-b"},
            {"zone": "zones/us-east1-c"}
          ]
       }
    }

Depending on how you configure and act on a MIG, various policies and actions can affect the instances in the group. To determine which managed instances are up and running, see [Checking the status of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

If there is not enough capacity in each zone to support VMs for the group, Compute Engine creates as many VMs as possible and continues attempting to create the remaining VMs when additional capacity becomes available.

If you don't explicitly specify individual zones in your request, Compute Engine automatically chooses three zones to create VMs in. If you need to create VMs in more than or fewer than three zones, or you want to pick which zones are used, you can provide a list of zones in your request. For more information, see [Zone selection](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones).

## Distribution of VMs across zones

By default, a regional MIG distributes VMs evenly across selected zones. Because you are creating a regional MIG, keep in mind that certain resources are zonal, such as GPUs and existing persistent disks. If your MIG's instance template specifies zonal resources, you must make sure all those resources are present in all selected zones so they can be attached to the VMs created by the regional MIG. Alternatively, if you want the group to check for the existence of zonal resources for you, you can set the MIG's target distribution shape to create instances only in zones that contain those resources.

For more information, see the following documents:

  * [Set a target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape) for VMs across zones

    * [Target shape limitations](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape#limitations)
    * [Creating a group with a target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups#turning_on_proactive_instance_distribution)
    * [Changing the target distribution shape of an existing group](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape#changing_the_target_distribution_shape_of_an_existing_group)
    * [Viewing the configured instance distribution policy](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape#viewing_the_configured_instance_distribution_policy)



## Proactive instance redistribution

[Proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution) is enabled by default. If you need to manually manage the number of VMs in each zone, or if you need to set the MIG's target distribution shape to `BALANCED` or `ANY_SINGLE_ZONE`, you must disable proactive instance redistribution.

For more information, see the following documents:

  * [Disable and re-enable proactive VM redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution)
    * [Create a group with proactive instance redistribution disabled](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution#creating_a_group_with_proactive_instance_redistribution_disabled)
    * [Turn off proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution#turning_off_proactive_instance_redistribution)
    * [Turn on proactive instance distribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution#turning_on_proactive_instance_distribution)
  * [Manually rebalance a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-rebalance-manually)



## What's next

  * [Set up application-based autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs), which periodically verifies that your application responds as expected on each of the MIG's VMs and automatically recreates unresponsive VMs.
  * [Enable autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) to automatically add or delete VMs from your MIG based on increases or decreases in load.
  * Learn how to [apply a new configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) to all or to a subset of the VMs in a MIG by setting and applying a new instance template, all-instances configuration, or per-instance configuration.
  * Preserve disks, metadata, and IP addresses across disruptive events like VM recreation, autohealing, and updates by [adding stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).
  * Learn about [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances), for example, to delete, abandon, and recreate VMs in a MIG.
  * [View info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about MIGs and their VMs.
  * [Monitor instance distribution in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/monitor-instance-distribution) to observe how instances are distributed across zones.
  * [Simulate a zone outage for a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-simulate-zonal-outage)
  * Learn how to [add an external HTTP(S) load balancer frontend to your instance group](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute). For information about other types of load balancers, see the [Load balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
