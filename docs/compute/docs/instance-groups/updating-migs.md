---
url: https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs/
title: Apply new VM configurations in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:26:53.914328+00:00
---

# Apply new VM configurations in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Apply new VM configurations in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can configure the virtual machine (VM) instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) and the methods you can use to apply the configuration to existing VMs in the group.

You specify the intended configuration for the VMs in a MIG by using the following VM configuration components:

  * Required: Instance template
  * Optional: All-instances configuration
  * Optional: Stateful configuration



Whenever you update the intended configuration by using those components, Compute Engine automatically applies your updated configuration to new VMs that are added to the group.

To apply an updated configuration to existing VMs, use the methods described on this page:

  * Automatic rollouts with a disruption budget and optional canary updates of new templates
  * Selective, manual updates to specific VMs only, to minimize disruption
  * Re-creation of specific VMs



You can also configure your MIG to apply the latest available configuration to VMs during VM repairs. For more information, see [Apply configuration updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair).

If you only need to resize a MIG, see the documentation for how to [add or remove VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig). If you want to learn about configuring MIG features, see the docs for [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler), [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs), [load balancing](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer), and [stateful workloads](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).

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




## Configuration components for VMs in a MIG

You configure the VMs in a MIG through the following components:

Component| Properties| Use case  
---|---|---  
**[Instance template](https://docs.cloud.google.com/compute/docs/instance-templates)** | Machine type, boot disk image, labels, startup script, network interfaces, and other VM properties | **Required** : Use an instance template to define required and optional instance properties for all VMs in the group.  
  
Optional: If you want to canary test a second VM configuration, you can add a second instance template to the group and apply it to a subset of the VMs in the group.  
**[All-instances configuration](https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic)** | Labels and metadata | Optional: Use an all-instances configuration to quickly override instance template properties for all VMs in the group.  
**[Stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs)** | Stateful disks, IP addresses, and metadata | Optional: If you need to support a [stateful workload](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#how_stateful_workloads_are_different_from_stateless_workloads), add stateful configuration to VMs in the group.  
  
If you update any configuration for the group through those components, you must apply the updated configuration to existing VMs in the group in order to make the updated configuration effective.

## Methods to apply a new configuration to existing VMs

After you update a MIG's VM configuration, you can apply the new configuration to existing VMs in the group by using the following methods:

  * **Automatic (proactive)** : Use this method if you want the MIG to automatically apply new configurations to all or to a subset of existing VMs in the group. The level of disruption to running VMs depends on the update policy that you configure. You can use this method to canary update new instance templates. To use this method, set the MIG's update type to "proactive".
  * **Selective (opportunistic)** : Use this method if you want to apply the update manually or if you want to update all existing VMs in the group at once. You target any or all VMs to be updated to the latest configuration. To use this method, set the MIG's update type to "opportunistic".
  * **Re-creation of VMs** : Apply new configurations by re-creating specific VMs.



For more information about setting a MIG's update type, see Set up a proactive or an opportunistic update.

### Automatic (proactive)

An automatic update type is also known as a _proactive_ update type. When you set the MIG's update type to proactive, the MIG automatically applies updated configurations to VMs as necessary.

Setting the MIG's update type to proactive offers two primary advantages:

  * The rollout of an update happens automatically to your specifications, without the need for additional input after the initial request. You can specify the speed of deployment, the level of disruption to your service, and the scope of the update.
  * You can automate partial rollouts, which allows for canary testing.



To learn how to set the MIG's update type, see Set up a proactive or an opportunistic update.

For more information about automatic rollouts, see [Automatically apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).

### Selective (opportunistic)

A selective update type is also known as an _opportunistic_ update type. When you set the MIG's update type to opportunistic, the MIG applies new configurations to existing VMs only when you selectively target specific VMs to be updated.

Setting the MIG's update type to opportunistic offers the following advantages:

  * You can select the VMs that you want to update.
  * You can control the timing and the sequence of the updates.
  * You can use the gcloud CLI or REST to update all instances immediately.



In certain scenarios, a selective update type is useful because you don't want to cause instability to the system if it can be avoided. For example, consider the following:

  * One of the VMs in your MIG goes down and needs to be repaired but you don't want its configuration to change. If you set the MIG's update type to opportunistic and you do not forcefully apply [updates during repairs](https://docs.cloud.google.com/compute/docs/instance-groups/update-on-repair), then Compute Engine repairs the VM using the same configuration that was used to create that VM, even if the original instance template no longer exists.

  * You have an autoscaled MIG and you want to apply a non-critical update without any urgency. To ensure that Compute Engine does not tear down your existing VMs to apply the update, set the MIG's update type to opportunistic. When scaling in, the autoscaler preferentially terminates VMs with the old configuration. When the group scales out, it creates VMs with the latest configuration.




To learn how to set the MIG's update type, see Set up a proactive or an opportunistic update.

For more information about selectively updating VMs, see [Selectively apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig).

### Re-creation of VMs

You can re-create any VM in a MIG. When you do, the MIG applies any updated configuration that has not yet been applied to that VM. For more information, see [Re-creating VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#recreate_instances).

## Set up a proactive or an opportunistic update

To apply new configurations to existing VMs automatically, set the MIG's update type to "proactive". To apply new configurations to existing VMs only when you select a VM to be updated, set the MIG's update type to "opportunistic".

Use the Google Cloud console, the Google Cloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch)
  * For regional MIGs, all permissions required to call the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to the Instance groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the MIG that you want to update.

  3. Click **Edit**.

  4. Click **Update policy** to expand the section.

  5. Choose either **Selective** or **Automatic** update.

  6. Optional: If you choose **Automatic** , then you can set the additional [options](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#options) or use the default values.

  7. Click **Save**.




###  gcloud 

Use the [`rolling-action start-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/start-update) and set the `--type` flag to `opportunistic` or `proactive`.
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=NEW_TEMPLATE \
        --type=TYPE
    

You can also use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) and include the `--update-policy-type` flag.
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        **--update-policy-type= TYPE**

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the group
  * `NEW_TEMPLATE`: the name of the new template for the group
  * `TYPE`: the type of update, `opportunistic` or `proactive`



###  REST 

Call the `patch` method on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG resource.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "updatePolicy": {
        "type": "TYPE" # Choose an opportunistic or proactive update
      },
      "versions": [{
        "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE",
        }]
    }

Replace the following:

  * `PROJECT_ID`: the project in which the MIG exists.
  * `REGION`: the region where your MIG is located. For a zonal MIG, replace `regions/REGION` with `zones/ZONE`.
  * `INSTANCE_GROUP_NAME`: the name of the group.
  * `NEW_TEMPLATE`: the name of the new template for the group.
  * `TYPE`: the type of update, `OPPORTUNISTIC` or `PROACTIVE`.



To learn more about setting a new template and then applying that template to new and existing VMs in a MIG, see the following pages:

  * [Automatically apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups)
  * [Selectively apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig)



## Check your group's update policy type

You can view your MIG's currently configured update policy type ("opportunistic" or "proactive") and other [update policy settings](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#options) by using the gcloud CLI or REST.

###  gcloud 

Use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) and include the `--format` flag to only list the `updatePolicy` settings.
    
    
    gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
        --format="(updatePolicy)"

###  REST 

Make a `GET` request on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG and check the `updatePolicy` field.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    

To change the policy type, see Set up a proactive or an opportunistic update.

## Updates for suspended and stopped VMs

If you have suspended and stopped pools of VMs in a MIG, you can selectively (opportunistic) update suspended or stopped VMs like you update other running VMs. If you configure automatic (proactive) updates, the MIG updates the VMs in the following order:

  1. Running, suspended, and stopped VMs
  2. VMs with status `SUSPENDING` or `STOPPING`



For an automatic update, the MIG calculates the [maximum surge](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_surge) and [maximum unavailable](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_unavailable) based on the target number of running VMs only, and doesn't consider the VMs in the standby pool.

If the automatic update requires replacing of VMs in the group, then the MIG does the following:

  1. Deletes the suspended and stopped VMs.
  2. Creates new VMs with the new instance template.
  3. Performs the initialization process.
  4. Suspends or stops the VMs.



If the automatic update requires only refreshing or restarting of VMs in the group, then the MIG does the following:

  1. Resumes or starts the VMs.
  2. Performs the update on the VMs when they are running.
  3. Performs the initialization process.
  4. Suspends or stops the VMs.



**Canary updates**

If you want to initiate [canary updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups#starting_a_canary_update) in a MIG that has suspended or stopped VMs, the following applies:

  * In the `manual` standby policy mode, the MIG updates only the running VMs based on the number or percentage of VMs to which you want to apply the update. The suspended and stopped VMs remain in the previous versions.
  * In the `scale-out-pool` standby policy mode, you cannot initiate a canary update in the MIG.



## Relationship between `versions` and `instanceTemplate` fields

If you use REST, we recommend using the `instanceGroupManagers.versions` and `regionInstanceGroupManagers.versions` fields to configure instance templates for zonal and regional MIGs.

The legacy `instanceTemplate` field overlaps in functionality with the `versions` field because both fields let you specify which instance template the MIG uses to create VMs. However, only the `versions` field lets you specify an advanced two-template (canary) configuration.

For backward compatibility, MIGs continue to support setting the top-level `instanceTemplate` field, even though we recommend that you switch to using only the `versions` field. Using both the top-level `instanceTemplate` field and the `versions` field at the same time can lead to ambiguity and confusion.

If you specify both the `instanceTemplate` field and the `versions` field when calling the `update()` or `patch()` method, there are three possible outcomes:

  * **You set both fields to the same value.**

This is a valid request. In this case, it creates no ambiguity, and the new instance template is applied to the MIG.

For example, in the following request, the top-level `instanceTemplate` and the `versions` field specify the same instance template which is different from the existing current template, so the MIG is updated to the new instance template:
        
        {
         "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE",
         "versions": [
          {
           "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE"
          }
         ],
         "updatePolicy": {
           "type": "PROACTIVE"
         }
        }
        

  * **You set both fields to values that don't match but only one value differs from the current instance template in the MIG.**

This is a valid request. The field that's different from the current setting is taken as the intended value. For example, you call the `update()` method and supply both fields, but only one field is updated:
        
        {
         "instanceTemplate": "global/instanceTemplates/CURRENT_TEMPLATE",
         "versions": [
          {
           "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE"
          }
         ],
         "updatePolicy": {
           "type": "PROACTIVE"
         }
        }
        

  * **You set both fields to values that don't match, and both values differ from the current instance template in the MIG.**

This setting is invalid and returns an error because there is no clear intent.
        
        {
         "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE",
         "versions": [
          {
           "instanceTemplate": "global/instanceTemplates/A_DIFFERENT_NEW_TEMPLATE"
          }
         ],
         "updatePolicy": {
           "type": "PROACTIVE"
         }
        }
        




### The `versions` field, `instanceTemplate` field, and the `get()` method

If you only specify one instance template, either through the top-level `instanceTemplate` field or through the `versions` field or through both, the `get()` method returns both fields in its response. This makes the new `versions` field backward compatible. As long as you specify a single instance template in either of these fields, there is no change to what the `get()` method returns in the `instanceTemplate` field.

If the `versions` field has two instance templates specified, the `get()` method returns an empty top-level `instanceTemplate` field. There is no way to unambiguously express a canary, two-instance template configuration in the top-level `instanceTemplate` field, so the field is not used during a canary update.

### The `versions` field and the `setInstanceTemplate()` method

For backward compatibility, the `setInstanceTemplate()` method behaves as it has previously, letting you change the template the MIG uses to create VMs. When you call this method, the `versions` field is overridden with the instance template specified by the `setInstanceTemplate()` method.

The `setInstanceTemplate()` method also sets the `updatePolicy` to `OPPORTUNISTIC`. This prevents the MIG from actively deploying an instance template that isn't explicitly specified in the `versions` field.

## What's next

  * Learn more about [automatically rolling out a new instance template to a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).
  * Learn more about [selectively updating VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig).
  * [View information](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about your MIG and its VMs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
