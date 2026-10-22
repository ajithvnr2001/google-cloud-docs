---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig/
title: Create a MIG in a single zone \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:07.391465+00:00
---

# Create a MIG in a single zone  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG in a single zone Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) in a single zone. Putting all your MIG's VMs in a single zone helps to minimize latency, which is useful for certain workloads—for example, batch workloads.

This type of MIG is also known as a _zonal MIG_.

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

## Create a MIG in a single zone

To create a MIG in a single zone, use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create), Terraform, or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers/insert).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert).



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups?walkthrough_id=compute--instance-groups--create-zonal-mig&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create instance group**. 
  3. If you want to create a stateful MIG, select the **New managed instance group (stateful)** option. To help you decide, see [When to use stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs). 
  4. Assign a name and optionally a description to your instance group. 
  5. Choose an instance template for the instance group or [create a new one](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates). 
  6. Specify the number of VMs for this group. Remember to [provision](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision) enough VMs to support your application if a zone failure happens. 
  7. For **Location** , select **Single zone**. 
  8. Select the **Region** and the **Zone** where you want to create your MIG. If you chose a regional instance template, then the **Region** is automatically selected based on the template's region. 
  9. For stateless MIGs, **Autoscaling** is enabled by default. With autoscaling, your group [automatically adds or removes instances](https://docs.cloud.google.com/compute/docs/autoscaler) based on its utilization. 
  10. Optionally, enable [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) to perform application-based health checking on VMs within the group. 
  11. Click **Create** to create the new group. 



###  gcloud 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

Create a managed instance group with the [`instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) and specify the group name, group size, instance template, and zone.
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --size SIZE \
        --template INSTANCE_TEMPLATE_URL \
        --zone ZONE

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name for this instance group.
  * `SIZE`: the size of the instance group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `ZONE`: one of the [zones](https://docs.cloud.google.com/compute/docs/regions-zones) available for Compute Engine. If you want to distribute your MIG's VMs across multiple zones in a region, see [Create a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).



You can optionally supply the `--base-instance-name` flag. Because these VMs are based on a common template, each VM is assigned a random string as part of its VM name. The base name is prepended to this random string. For example, if you set the base name to `test`, VMs will have names like `test-yahs` and `test-qtyz`. If you need specific names, see [Creating instances with specific names in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

For example, the following command creates an instance group named example-group, with base VM name `test`. The group contains three instances:
    
    
    gcloud compute instance-groups managed create example-group \
        --base-instance-name test \
        --size 3 \
        --template an-instance-template \
        --zone us-central1-f

###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To create a zonal MIG, you can use the [`google_compute_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
    
      name               = "example-group"
      base_instance_name = "test"
      target_size        = 3
      zone               = "us-central1-f"
    
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

Create a managed instance group with the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert). In the request body, include the group name, group size, and the URL to the instance template.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
    
    {
      "versions": [
        {
          "instanceTemplate": "INSTANCE_TEMPLATE_URL"
        }
      ],
      "name": "INSTANCE_GROUP_NAME",
      "targetSize": SIZE
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the request. If you want to distribute your MIG's VMs across multiple zones in a region, replace `zones/ZONE` with `regions/REGION` and specify a region. For more information, see [Create a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups).
  * `INSTANCE_GROUP_NAME`: the name for this instance group.
  * `SIZE`: the size of the instance group.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`



You can optionally supply the `base-name` field. Because these VMs are based on a common template, each VM is assigned a random string as part of its VM name. The base name is prepended to this random string. For example, if you set the base name to `test`, VMs will have names like `test-yahs` and `test-qtyz`. If you need specific names, see [Creating instances with specific names in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).

Depending on how you configure and act on a MIG, various policies and actions can affect the instances in the group. To determine which managed instances are up and running, see [Checking the status of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

## What's next

  * [Set up application-based autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs), which periodically verifies that your application responds as expected on each of the MIG's VMs and automatically recreates unresponsive VMs.
  * [Enable autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) to automatically add or delete VMs from your MIG based on increases or decreases in load.
  * Learn how to [apply a new configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) to all or to a subset of the VMs in a MIG by setting and applying a new instance template, all-instances configuration, or per-instance configuration.
  * Preserve disks, metadata, and IP addresses across disruptive events like VM recreation, autohealing, and updates by [adding stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).
  * Learn about [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances), for example, to delete, abandon, and recreate VMs in a MIG.
  * [View info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about MIGs and their VMs.
  * Learn how to [add an external HTTP(S) load balancer frontend to your instance group](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute). For information about other types of load balancers, see the [Load balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
