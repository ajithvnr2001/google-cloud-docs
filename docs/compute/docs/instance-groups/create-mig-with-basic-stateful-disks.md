---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-stateful-disks/
title: Create a MIG with stateful disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:49.420989+00:00
---

# Create a MIG with stateful disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-stateful-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG with stateful disks Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that preserves the data on disks with a given device name for all of the MIG's VMs, even in the event of VM recreation—for example when a VM in the MIG is autohealed, updated, or recreated. Preserving disks is useful for certain workloads—for example, for databases or legacy applications.

In addition to preserving disks for all VMs in the group, you can also configure a stateful MIG for the following:

  * You can add and preserve instance-specific disks.
  * You can add and preserve instance-specific metadata.
  * You can add and preserve IP addresses.



For more information, see the [stateful MIG overview](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).

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

A MIG with [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#what_makes_a_mig_stateful)—a _stateful MIG_ —has the following limitations:

  * You cannot use autoscaling if your MIG has stateful configuration.
  * If you want to use automated rolling updates, you must set the [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) to `RECREATE`.
  * For stateful regional MIGs, you must [disable proactive redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) (set the redistribution type to `NONE`) to prevent deletion of stateful instances by automatic cross-zone redistribution.
  * If you use an [all-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic) to override instance template properties, you cannot specify those properties in any per-instance configuration and at the same time in the group's all-instances configuration.



To see the full list of MIG limitations, which varies based on the configuration that you use, see [MIG limitations](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations).

## Create a MIG with stateful disks

Use the [Google Cloud console](https://console.cloud.google.com/), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create), Terraform, or [REST](https://docs.cloud.google.com/compute/docs/reference/latest).

**Pro Tip:** Consider storing data on an additional persistent disk and keeping the boot disk, containing the application, stateless. Such a configuration makes your application resilient to boot disk file system corruption. This configuration also simplifies VM updates because the MIG can recreate boot disks based on the immutable source image that you specify in the MIG's instance template.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the[`instanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) method (for zonal MIGs)
  * All permissions required to call the[`regionInstanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) method (for regional MIGs)



###  Console 

  1. Go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups?walkthrough_id=compute--instance-groups--create-mig-with-basic-stateful-disks&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create instance group**. 
  3. Select the **New managed instance group (stateful)** option. 
  4. Assign a name and optionally a description to your instance group. 
  5. Choose an instance template for the instance group or [create a new one](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates). 
  6. In the **Number of instances** field, specify the initial number of VMs you need in this group.
  7. In the **Stateful configuration** section, under **Group config** , click the disk you want to make stateful, then perform the following steps.
     1. In the **Stateful** section, select **Yes**.
     2. In the **On permanent instance deletion** list, choose whether you want to detach the disk or delete the disk when you permanently delete the VM.
     3. To save the settings, click **Done**.
  8. To create the MIG, click **Create**.



###  gcloud 

To specify which disks from the instance template should be stateful on MIG creation, use the `--stateful-disk` flag with the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --template INSTANCE_TEMPLATE_URL \
        --size SIZE \
        --stateful-disk device-name=DEVICE_NAME[,auto-delete=DELETE_RULE]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: The name of the managed instance group to create.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SIZE`: The initial number of VMs you need in this group.
  * `DEVICE_NAME`: The device name of a disk specified in the instance template.
  * `DELETE_RULE`: A value that prescribes what should happen to a stateful disk when a VM is deleted. Available options are:

    * `never`: (Default.) Never delete the disk; instead, detach the disk when its VM is deleted.
    * `on-permanent-instance-deletion`: Delete the disk when its VM instance is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.

Regardless of the value of the delete rule, stateful disks are always preserved on VM autohealing, update, and recreation operations.


**Note:** You can see the device names of disks that are defined in an instance template by running the `gcloud compute instance-templates describe` [command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe).

###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

To specify which disks from the instance template should be stateful on MIG creation, include the `stateful_disk` block. The following sample creates a zonal MIG with stateful disks. For more information about the resource that is used in the sample, see [`google_compute_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
      name               = "igm-stateful-disk-basic"
      zone               = "us-central1-f"
      base_instance_name = "instance"
      target_size        = 1
    
      version {
        instance_template = google_compute_instance_template.default.id
      }
    
      stateful_disk {
        device_name = "example-disk"
        delete_rule = "NEVER"
      }
    
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To specify which disks from the instance template should be stateful on MIG creation, include them in the `statefulPolicy` field in your request body. For a zonal MIG, use the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) or for a regional MIG, use the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instanceGroupManagers
    
    {
      "name": "NAME",
      "versions": [
        {
          "instanceTemplate": "INSTANCE_TEMPLATE_URL"
        }
      ],
      "targetSize": SIZE,
      "statefulPolicy": {
        "preservedState": {
          "disks": {
            "DEVICE_NAME": {"autoDelete": "DELETE_RULE" },
            "DEVICE_NAME": {"autoDelete": "DELETE_RULE" }
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT`: The project ID for the request.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG). 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `NAME`: The name of the MIG to create.
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `SIZE`: The initial number of instances you need in this group.
  * `DEVICE_NAME`: The device name of a disk specified in the instance template.
  * `DELETE_RULE`: A value that prescribes what should happen to the stateful disk when the VM instance is deleted. The available options are:

    * `never`: (Default.) Never delete the disk; detach the disk when the VM is deleted.
    * `on_permanent_instance_deletion`: Delete the stateful disk when its VM is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.

Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.


**Note:** You can see the device names of disks that are defined in an instance template by calling the [ `instanceTemplates.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/get) and reading the `instanceTemplates.disks[].deviceName` field in the response.

## Billing

Compute Engine doesn't automatically delete stateful persistent disks that you detach from the MIG. You are still billed for the provisioned space of any detached persistent disks. To avoid incurring disk space costs after a disk is detached, delete the disk. For more information, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk-pricing).

## What's next

  * Learn more about [stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) and when to use them.
  * Learn more about [configuring stateful disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs).
  * Learn [How stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).
  * Learn more about [configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) for [disks](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs), [metadata](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs), and [IP addresses](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
