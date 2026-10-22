---
url: https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig/
title: Selectively apply VM configuration updates in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:02.850642+00:00
---

# Selectively apply VM configuration updates in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Selectively apply VM configuration updates in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to selectively apply configuration updates to the virtual machine (VM) instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

Compute Engine maintains the VMs in a MIG based on the [configuration components](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#vm_configuration_components) that you use: instance template, optional all-instances configuration, and optional stateful configuration.

Whenever you update a MIG's VM configuration by changing those components, Compute Engine automatically applies your updated configuration to new VMs that are added to the group.

To apply an updated configuration to existing VMs, you can set up a selective update–also known as a "opportunistic" update type. This type of update offers the following advantages:

  * You can select the VMs that you want to update.
  * You can control the timing and the sequence of the updates.
  * You can use the gcloud CLI or REST to update all VMs immediately.



Alternatively, if you want to automate the rollout of a new configuration to all or to a random subset of the VMs in a MIG, see [Automatically apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups). To help you decide, see [Methods to apply a new configuration to existing VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates).

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




## Apply updated configuration to selected VMs

Ensure your group's update policy type is set to "opportunistic" to prevent the MIG from automatically applying new a VM configuration to existing VMs. For more information, see [Check your group's update policy type](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#check_update_policy).

Then use the gcloud CLI or REST to update your MIG's configuration and to apply the latest configuration to specific VMs in the group or to all VMs in the group.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch)
  * For regional MIGs, all permissions required to call the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)



###  gcloud 

To set up a new instance template for your group, you can use the [`set-instance-template` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-instance-template).
    
    
    gcloud compute instance-groups managed set-instance-template INSTANCE_GROUP_NAME \
        --template=INSTANCE_TEMPLATE
    

**Apply configuration to specific VMs**

To apply the updated configuration to specific VMs, use the [`update-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances) with the `--instances` flag.
    
    
    gcloud compute instance-groups managed update-instances INSTANCE_GROUP_NAME \
        **--instances INSTANCE_NAMES** \
        --most-disruptive-allowed-action DISRUPTION_LEVEL \
        --minimal-action DISRUPTION_LEVEL
    

**Apply configuration to all VMs**

To apply the updated configuration to all VMs, use the [`update-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-instances) with the `--all-instances` flag.
    
    
    gcloud compute instance-groups managed update-instances INSTANCE_GROUP_NAME \
        **--all-instances** \
        --most-disruptive-allowed-action DISRUPTION_LEVEL \
        --minimal-action DISRUPTION_LEVEL
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG
  * `INSTANCE_TEMPLATE`: new instance template
  * `INSTANCE_NAMES`: a list of VMs to apply the template to
  * `DISRUPTION_LEVEL`: the minimal or maximal disruption level: `none`, `refresh`, `restart`, or `replace`
    * The default minimal action is `none`
    * The default most disruptive allowed action is `replace`



###  REST 

To set up a new instance template for your group, call the `patch` method on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG and update the `versions.instanceTemplate` field. To avoid automatically rolling out the new template to all VMs in the group, set the `updatePolicy.type` field to `OPPORTUNISTIC`.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "updatePolicy": {
        "type": "OPPORTUNISTIC"
      },
      "versions": [{
        "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE",
      }]
    }

**Apply configuration to specific VMs**

To apply the updated configuration to specific VMs, call the `applyUpdatesToInstances` method for your [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/applyUpdatesToInstances) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/applyUpdatesToInstances) MIG and specify a list of VMs in the request.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/applyUpdatesToInstances
    {
      **"instances": [
        "zones/ ZONE/instances/INSTANCE_NAME_1",
        "zones/ZONE/instances/INSTANCE_NAME_2"
      ]**,
      "minimalAction": DISRUPTION_LEVEL,
      "mostDisruptiveAllowedAction": DISRUPTION_LEVEL
    }

**Apply configuration to all VMs**

To apply the updated configuration to all existing VMs, set the `allInstances` field to `true`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/applyUpdatesToInstances
    {
      **"allInstances": true,**
      "minimalAction": DISRUPTION_LEVEL,
      "mostDisruptiveAllowedAction": DISRUPTION_LEVEL
    }

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the group
  * `NEW_TEMPLATE`: the name of the new template
  * `ZONE`: the zone of an instance to update
  * `INSTANCE_NAME_1` and `INSTANCE_NAME_2`: the names of the VMs to update
  * `DISRUPTION_LEVEL`: the minimal or maximal disruption level: `NONE`, `REFRESH`, `RESTART`, or `REPLACE`
    * The default `minimalAction` is `NONE`.
    * The default `mostDisruptiveAllowedAction` is `REPLACE`.



Similar to other managed instance group methods, `applyUpdatesToInstances` is intent-based, which means it [returns an operation response](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses). The operation can take some time to complete.

After you make a request, you can [check the status](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances) to verify that the update is complete.

## Control the disruption level during selective updates

Depending on the nature of an update, it might disrupt an instance's [state](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle). For example, changing an instance's boot disk requires replacing the instance. You can control the level of disruption during a selective update by setting the following options:

  * **Minimal action** : Use this option to minimize disruption as much as possible or to apply a more disruptive action than is necessary.

    * To limit disruption as much as possible, set the minimal action to `NONE`. If your update requires a more disruptive action, Compute Engine performs the necessary action to execute the update.
    * To apply a more disruptive action than is strictly necessary, set the minimal action to `RESTART` or `REPLACE`. For example, Compute Engine does not need to restart a VM to change its metadata. But if your application reads instance metadata only when a VM is restarted, you can set the minimal action to `RESTART` in order to pick up metadata changes.
  * **Most disruptive allowed action** : Use this option to prevent an update if it requires more disruption than you can afford. If your update requires a more disruptive action than you set with this flag, the update request fails. For example, if you set the most disruptive allowed action to `RESTART`, then an attempt to update the boot disk image fails because that update requires instance recreation, a more disruptive action than a restart.




When updating selected VMs, both of these options accept the following values:

Value | Description | Which instance properties can be updated?  
---|---|---  
`NONE` | Don't disrupt the instance at all. | None  
`REFRESH` | Don't stop the instance. | Additional disks, Dynamic Network Interfaces (NICs), instance metadata, labels, tags  
`RESTART` | Stop the instance and start it again. | Additional disks, Dynamic NICs, instance metadata, labels, tags, machine type  
`REPLACE` | Delete the instance and create it again. | All instance properties stored in the instance template or per-instance configuration  
  
The most disruptive allowed action can't be less disruptive than the minimal action.

When you selectively update VMs, the following defaults apply:

  * The default minimal action is `NONE`, which limits disruption as much as possible.
  * The default most disruptive allowed action is `REPLACE`. If you cannot tolerate such disruption, set the most disruptive allowed action to be less disruptive.



## What's next

  * Learn about [Viewing info about MIGs and managed VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).
  * Learn about [Creating instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).
  * Learn how to use image families and a rolling replace to [update the OS image](https://docs.cloud.google.com/compute/docs/instance-groups/upgrading-images-in-migs) on all VMs in a MIG.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
