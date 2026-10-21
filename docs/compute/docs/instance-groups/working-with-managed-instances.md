---
url: https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances/
title: Work with managed instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:06:26.875124+00:00
---

# Work with managed instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Work with managed instances Stay organized with collections  Save and categorize content based on your preferences. 

A [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) creates each of its managed instances based on the [configuration components](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#vm_configuration_components) that you use: instance template, optional all-instances configuration, and optional stateful configuration.

Each _managed instance_ is a data entity that represents the intended state for an actual virtual machine (VM) instance in a MIG.

Read this document to learn how to reliably work with the managed instances in a MIG. For example, you might need to add, remove, update, or view information about a specific instance.

To ensure that your configuration changes aren't reverted by the MIG, it's important to use the methods that are described in this document. If you work outside the group's methods to modify a MIG's VMs, the MIG might or might not detect that those VMs are no longer using the group's intended configuration, and you might experience unexpected results. For example, if you delete or update a VM in a MIG by using the instances API instead of the required _instance group manager_ API, the MIG will not be aware of your intent and, at any time in the future, the MIG might automatically attempt to recreate or revert that VM according to the MIG's configuration. 

## Before you begin

  * Review the [limitations](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations) then [create](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group) a group.
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




## What is a managed instance?

A managed instance is a data entity within a MIG that contains the current status and intended state for an actual VM instance.

The current status of a managed instance includes the following fields:

  * Instance [lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle) status—for example, `RUNNING`, `STOPPING`.
  * [Current action](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances) performed by the MIG on an instance—for example: `RESTARTING`, `VERIFYING`, `NONE`.
  * Instance [health state](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#health_states)—for example, `HEALTHY`, `UNHEALTHY`. 



A managed instance's intended state for an actual VM instance includes the following:

  * Intended [version](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#relationship_between_versions_and_instancetemplate_fields), that is, the version name and instance template to be used for the instance.
  * [Preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) of items (such as disks or metadata) to be preserved.



As shown in figure 1, for each managed instance in a MIG, the MIG keeps an actual VM up and running according to the managed instance's specification.

![Based on your configuration, the MIG autogenerates managed instances, which correspond to actual VM instances that a MIG maintains on your behalf.](https://docs.cloud.google.com/static/compute/images/mig-managed-instances.png)

**Figure 1.** Relationship between managed instances and corresponding VMs.

**Note:** Various policies and actions create, delete, and modify the VM instances in a MIG. Those operations are returned as `DONE` after the group has scheduled actions to create, delete, or update those instances. However, this doesn't mean that the actual instances in the group have been created, deleted, or updated until those underlying actions are complete. You must [verify the status of the group](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group) or [verify the status of those instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

To view the specifications of a managed instance, see [Viewing information about the managed instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_info_about_managed_instances).

## Add instances to a MIG

To add more instances to a MIG, you can do the following:

  * Manually set the size of the MIG
  * Use resize requests to create VMs all at once
  * Use autoscaling for stateless applications
  * Add instances with specific names



To verify that newly added instances are up and running, [verify the status of the group](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group) or [verify the status of the managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

### Manually set the size of the MIG

If a managed instance group isn't already set to automatically scale, then you can manually set the size of the group to change the number of instances in the group. For more information, see [Manually resizing a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

### Use resize requests to create VMs all at once

You can use resize requests to add GPU VMs to a MIG all at once. This feature helps you avoid charges for partial capacity while Compute Engine provisions all resources. MIG resize requests use the flex-start or reservation-bound provisioning models. These models let you obtain vCPUs and GPUs at a discounted price. For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

### Use autoscaling for stateless applications

You can configure managed instance groups to automatically add or remove instances based on their workloads. Your applications can gracefully handle increases in traffic, and you can reduce your costs when the need for compute resources is lower. For more information about automatically scaling your MIG, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

### Add instances with specific names

If your workload or orchestration system requires specific instance names, you can add instances with those names to an existing MIG. The names that you assign to these instances persist if the MIG recreates them.

Based on how you want to add instances with specific names to a MIG, use one of the following methods:

  * To add GPU instances all at once to a MIG, [create a resize request](https://docs.cloud.google.com/compute/docs/instance-groups/create-resize-requests-mig).

  * To add instances to a MIG as resources become available, [create instances with specific names](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs).




## Update VM configuration in a MIG

If you need to change the configuration of VMs in a MIG—for example, to modify the boot disk or machine type, add disks, or change other VM properties—see [Updating VM configuration in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

## Delete instances from a MIG

When you delete managed instances, the MIG reduces the `targetSize` of the group and deletes the corresponding VM instances.

If you set up a [stateful MIG](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs), then the MIG deletes the instances' preserved state configurations. The MIG also removes the instances from any [target pools](https://docs.cloud.google.com/compute/docs/load-balancing/network/target-pools) of which they are a member.

If the group is part of a [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service) that has [enabled connection draining](https://docs.cloud.google.com/compute/docs/load-balancing/enabling-connection-draining), it can take up to an additional 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

To delete a managed instance, you can:

  * Resize the MIG. The MIG chooses which instances to delete. 
    * [Manually resize](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group) the MIG.
    * [Use autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) for stateless applications.
  * [Delete the whole group](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig).
  * [Delete](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) or [abandon](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) specific instances explicitly.



### Factors that affect the deletion of VM instances

When a MIG is scaled in, either automatically by an autoscaler or manually by resizing the group, the MIG prioritizes instances for deletion based on a number of factors, including the following. Once the MIG identified the priority instances, it then selects instances for deletion on a nondeterministic basis.

  * **Instance status** : Instances that are not running for any reason—for example, instances that are terminated or suspended.

  * **Disruptive changes** : Instances undergoing or scheduled for disruptive changes, such as create, delete, refresh, recreate, or replace.

  * **Instance configuration version** : Instances that are not yet updated to the latest intended version of the instance template.

  * **Target distribution shape** : In regional MIGs, instances that help maintain or achieve the intended [target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#balancing-instances-across-zones) across zones.

  * **Autoscaling signal** : In [autoscaled MIGs](https://docs.cloud.google.com/compute/docs/autoscaler), instances that have the lowest autoscaling signal. For example, if a MIG is configured to scale based on CPU utilization, the MIG prioritizes instances that have the lowest CPU utilization.




The MIG considers these factors together to select the most suitable instances for deletion while maintaining the group's availability and distribution requirements.

## Recreate instances in a MIG

Use this method to update selected VMs so that they use the group's latest [VM configuration components](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#vm_configuration_components). If you need to recreate all of the VMs in a managed instance group, start a [rolling update](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups) instead.

If the group is part of a [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service) that has [enabled connection draining](https://docs.cloud.google.com/compute/docs/load-balancing/enabling-connection-draining), it can take up to an additional 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

Recreate selected VM instances in a managed instance group using the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  gcloud 

Use the [`instance-groups managed recreate-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/recreate-instances).
    
    
    gcloud compute instance-groups managed recreate-instances INSTANCE_GROUP_NAME \
        --instances INSTANCE_NAME_1,INSTANCE_NAME_2 \
        [--region REGION | --zone ZONE]

###  REST 

In the API, make a POST request to the [`regionInstanceGroupManagers.recreateInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/recreateInstances) method. For a zonal managed instance group, use the [`instanceGroupManagers.recreateInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/recreateInstances) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/recreateInstances
    
    {
     "instances": [
      "zones/ZONE/instances/INSTANCE_NAME_1",
      "zones/ZONE/instances/INSTANCE_NAME_2"
     ]
    }

After you make a request to recreate VM instances in a managed instance group, the new VMs start as soon as the system can provision them. This process can take a significant amount of time depending on the number of instances that you recreate. [Verify the status of the group](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group) or [verify the status of the managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

The recreate operation preserves the VM instance name, but the instance creation timestamp might not change. To confirm that the recreate operation has created a new instance when the instance creation timestamp has not changed, check the creation timestamp of the boot disk attached to that instance.

## View information about instances in a MIG

See [Viewing info about the managed instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_info_about_managed_instances).

## Configure stateful instances in a MIG

See [Configuring stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).

## What's next

  * Learn about [applying new configurations to VMs in a MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).
  * Learn about [Applying machine type recommendations for MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/apply-sizing-recommendations-managed-instance-groups).
  * Try a tutorial: 
    * [Using autohealing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-autohealing)
    * [Using load balancing for highly available applications](https://docs.cloud.google.com/compute/docs/tutorials/high-availability-load-balancing)
    * [Using autoscaling for highly scalable applications](https://docs.cloud.google.com/compute/docs/tutorials/high-scalability-autoscaling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
