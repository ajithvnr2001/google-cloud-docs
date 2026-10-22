---
url: https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups/
title: Automatically apply VM configuration updates in a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:45.260220+00:00
---

# Automatically apply VM configuration updates in a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Automatically apply VM configuration updates in a MIG Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to automatically apply configuration updates to the virtual machine (VM) instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).

Compute Engine maintains the VMs in a MIG based on the [configuration components](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#vm_configuration_components) that you use: instance template, optional all-instances configuration, and optional stateful configuration.

Whenever you update a MIG's VM configuration by changing those components, Compute Engine automatically applies your updated configuration to new VMs that are added to the group.

To apply an updated configuration to existing VMs, you can set up an automatic update–also known as a _proactive_ update type. The MIG automatically rolls out configuration updates to all or to a subset of the group's VMs. You can control the speed of deployment, the level of disruption to your service, and, by using a canary update, the number of instances that the MIG updates with the new configuration. After you specify the new configuration, you don't need to provide additional input and the update completes on its own.

Alternatively, if you want to selectively apply a new configuration only to new or to specific instances in a MIG, see [Selectively apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig). To help you decide, see [Methods to apply a new configuration to existing VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates).

## Before you begin

  * If you're updating a stateful MIG, review [Applying, viewing, and removing stateful configuration in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs).
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




## Limitations

  * If you have a stateful MIG and you want to use automated rolling updates, you must keep the instance names when replacing instances or, equivalently, set the replacement method to `RECREATE`.
  * [Per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) for IP addresses aren't supported for Dynamic Network Interfaces (NICs).



## Start a basic rolling update

A basic rolling update is an update that is gradually applied to all instances in a MIG until all instances have been updated to the latest intended configuration. The rolling update automatically skips instances that are already in their latest configuration.

You can control various aspects of a rolling update, such as how many instances can be taken offline for the update, how long to wait between updating instances, whether the new template affects all or just a portion of instances, and so on.

Here are things to keep in mind when making a rolling update:

  * **Updates are intent based.** When you make the initial update request, the Compute Engine API returns a successful response to confirm that the request is valid, but that doesn't indicate that the update succeeded. You must check the status of the group to determine whether your update was deployed successfully.

  * **The[Instance Group Updater API](https://console.cloud.google.com/marketplace/details/google/replicapoolupdater.googleapis.com?filter=category:compute&id=c9ffe91b-fca0-4e64-9111-80e036db8dbc) is a declarative API.** The API expects a request to specify the desired post-update configuration of the MIG, rather than an explicit function call.

  * **Automated updates support up to two instance template versions in your MIG.** This means that you can specify two different instance template versions for your group, which is useful for performing canary updates.




To start a basic rolling update where the update is applied to all instances in the group, select one of the following options:

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch)
  * For regional MIGs, all permissions required to call the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the MIG that you want to update.

  3. Click **Edit**.

  4. Click **Instance template & overrides** to expand the section and add a template for testing as follows: 

     1. Click **Add a template for testing**.

     2. In the **Instance template for testing** list, select a new template. 

If the template that you want to test is not available, use the **Create a new instance template** option and follow the prompts to create one.

     3. In the **Target running** field, enter the number or percentage of instances to which you want to apply the new template.

     4. In the **Instances or percentage** field, select either **instances** or **percent** indicating the number that you entered in the **Target running** field.
  5. Click **Update policy** to expand the section and do the following:

     1. Select **Automatic** , if not already selected.
     2. Leave default values for the other options or modify them as needed.
  6. Click **Save** to start the update.




###  gcloud 

Use the [`rolling-action start-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/start-update).
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=INSTANCE_TEMPLATE_URL
        [--zone=ZONE | --region=REGION]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG
  * `INSTANCE_TEMPLATE_URL`: the URL of the instance template that you want to use to create instances in the MIG. The URL can contain either the [ID](https://docs.cloud.google.com/compute/docs/instance-templates/get-list-delete-instance-templates#get_information_about_an_instance_template) or name of the instance template. Specify one of the following values: 
    * For a regional instance template: `projects/PROJECT_ID/regions/REGION/instanceTemplates/INSTANCE_TEMPLATE_ID`
    * For a global instance template: `INSTANCE_TEMPLATE_ID`
  * `ZONE`: for zonal MIGs, provide the [zone](https://docs.cloud.google.com/compute/docs/regions-zones)
  * `REGION`: for regional MIGs, provide the region



###  REST 

Call the `patch` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) MIG resource.

For example, for a regional MIG, the following request shows the minimal configuration necessary for automatically updating 100% of the instances to the new instance template.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE",
      "updatePolicy": {
        "type": "PROACTIVE"
       }
    }

After you make a request, you can monitor the update to know when the update has finished.

For advanced configurations, include other update options. If you don't specify otherwise, the `maxSurge` and `maxUnavailable` options default to `1` multiplied by the number of affected zones. This means that only 1 instance is taken offline in each affected zone, and the MIG creates only 1 additional instance per zone, during the update.

## Configure options for your update

For more complex updates you can configure additional options, as described in the following sections.

### Update type

Managed instance groups support two types of update:

  * Automatic, or **proactive** , updates
  * Selective, or **opportunistic** , updates



If you want to apply updates automatically, set the type to **proactive**.

Alternatively, if an automated update is potentially too disruptive, you can choose to perform an **opportunistic** update. The MIG applies an opportunistic update only when you manually initiate the update on selected instances or when new instances are created. New instances can be created when you or another service, such as an autoscaler, [resizes](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size) the MIG. Compute Engine does not actively initiate requests to apply opportunistic updates on existing instances.

For more information about automated versus selective updates, see [Methods to apply a new configuration to existing VMs](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#choosing_between_automated_and_selective_updates).

### Maximum surge

Use the `maxSurge` option to configure how many new instances the MIG can create above its `targetSize` during an automated update. For example, if you set `maxSurge` to 5, the MIG uses the new instance template to create up to 5 new instances above your target size. Setting a higher `maxSurge` value speeds up your update, at the cost of additional instances, which are billed according to the Compute Engine [price sheet](https://cloud.google.com/compute/all-pricing). 

You can specify either a fixed number, or, if the group has 10 or more instances, a percentage. If you set a percentage, the Updater rounds up the number of instances if necessary.

If you don't set the `maxSurge` value, the default value is used. For zonal MIGs, the default for `maxSurge` is `1`. For regional MIGs, the default is the number of zones associated with the group, by default `3`.

`maxSurge` only works if you have enough quota or resources to support the additional resources.

If your update does not require VMs to be replaced, this option is ignored. You can force VMs to be replaced during an update by setting the minimal action option.

### Maximum unavailable

Use the `maxUnavailable` option to configure how many instances are unavailable at any time during an automated update. For example, if you set `maxUnavailable` to 5, then only 5 instances are taken offline for updating at a time. Use this option to control how disruptive the update is to your service and to control the rate at which the update is deployed.

This number also includes any instances that are unavailable for other reasons. For example, if the group is in the process of being [resized](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#set_the_groups_target_size), instances in the middle of being created might be unavailable. These instances count toward the `maxUnavailable` number.

You can specify a fixed number, or, if the group has 10 or more instances, a percentage. If you set a percentage, the Updater rounds down the number of instances, if necessary.

If you do not want any unavailable machines during an update, set the `maxUnavailable` value to `0` and the `maxSurge` value to greater than 0. With these settings, Compute Engine removes each old machine only after its replacement new machine is created and running.

If you don't set the `maxUnavailable` value, the default value is used. For zonal MIGs, the default is `1`. For regional MIGs, the default is the number of zones associated with the group, by default `3`.

**Note:** If you set both `maxSurge` and `maxUnavailable` properties and both properties resolve to `0`, the Updater automatically sets `maxUnavailable=1`, to ensure that the automated update can always proceed.

### Minimum wait time

**Note:** `minReadySec` is only available in the beta Compute Engine API and might be deprecated in a future release.

Use the `minReadySec` option to specify the amount of time to wait before considering a new or restarted instance as updated. Use this option to control the rate at which the automated update is deployed. The timer starts when both of the following conditions are satisfied:

  * The instance's status is `RUNNING`.
  * If [health checking](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) is enabled, when the health check returns `HEALTHY`.



Note that for the health check to return healthy, the Updater waits for the following conditions:

  1. Waits for up to the period of time specified by the MIG's `autohealingPolicies.initialDelaySec` value for the health check to return as `HEALTHY`.
  2. Then, waits for the period of time specified by `minReadySec`.



If the health check doesn't return `HEALTHY` within the `initialDelaySec`, then the Updater declares the VM instance as unhealthy and potentially stops the update. While the VM instance is waiting for verification during the `initialDelaySec` and the `minReadySec` time period, the instance's `currentAction` is [`VERIFYING`](https://docs.cloud.google.com/compute/docs/reference/v1/instanceGroupManagers/list). However, the underlying VM instance status remains [`RUNNING`](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

If there are no health checks for the group, then the timer starts when the instance's status is `RUNNING`.

The maximum value for the `minReadySec` field is 3600 seconds (1 hour).

The following diagram shows how the target size, maximum unavailable, maximum surge, and minimum wait time options affect your instances. For more information about target size, see Canary updates.

![How update policy options affect your request.](https://docs.cloud.google.com/static/compute/images/updater-configuration.svg)

### Minimal action

Use the minimal action option to minimize disruption as much as possible or to apply a more disruptive action than is strictly necessary. For example, Compute Engine does not need to restart a VM to change its metadata. But if your application reads instance metadata only when a VM is restarted, you can set the minimal action to restart in order to pick up metadata changes.

If your update requires a more disruptive action than you set with this flag, Compute Engine performs the necessary action to execute the update. For example, if you specify a restart as the minimal action, the Updater attempts to restart instances to apply the update. But, if you are changing the OS, which can't be done by restarting the instance, then the Updater replaces the instances in the group with new VM instances.

For more information, including valid options, see Controlling the disruption level during a rolling update.

### Most disruptive allowed action

Use the most disruptive allowed action option to prevent an update if it requires more disruption than you can afford. If an update cannot be completed due to this setting, then the update fails and your VMs maintain their previous configuration.

For more information, see Controlling the disruption level during a rolling update.

### Replacement method

By default, when you proactively update a MIG, the group deletes your VM instances and swaps them with new instances with new names. If you need to preserve the names of your VM instances, use the `replacementMethod` option.

Preserving existing instance names might be useful if you have applications or systems that rely on using specific instance names. For example, some applications, like Memcached, rely on instance names because they don't have a discovery service; as a result, whenever an instance name changes, the application loses connection to that specific VM.

To preserve instance names, set the replacement method to `RECREATE` instead of `SUBSTITUTE` if you update the MIG with the gcloud CLI or the Compute Engine API. Alternatively, if you update the MIG from the Google Cloud console, select the checkbox **Keep names when replacing VMs**.

![Managed instance replacement methods.](https://docs.cloud.google.com/static/compute/images/mig-instance-replacement-methods.svg)

Valid `replacementMethod` values are:

  * `SUBSTITUTE` (default). Replaces VM instances faster during updates because new VMs are created before old ones are shut down. However, instance names aren't preserved because the names are still in use by the old instances.

  * `RECREATE`. Preserves instance names through an update. Compute Engine releases the instance name as the old VM is shut down. Then Compute Engine creates a new instance using that same name. To use this mode, you must set `maxSurge` to `0`.


**Note:** If you set the replacement method to `RECREATE`, then the instance name is preserved. However, the instance's ID and creation timestamp might change. To confirm that the `RECREATE` operation has created a new instance when the instance creation timestamp has not changed, check the creation timestamp of the boot disk attached to that instance.

For more information, see Preserving instance names.

## Additional update examples

Here are some command-line examples with common configuration options.

**Perform a rolling update of all VM instances, but create up to 5 new instances above the target size at a time**
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=NEW_TEMPLATE \
        --max-surge=5 \
        [--zone=ZONE | --region=REGION]
    

**Perform a rolling update with at most 3 unavailable machines and a minimum wait time of 3 minutes before marking a new instance as available**
    
    
    gcloud beta compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=NEW_TEMPLATE \
        --min-ready=3m \
        --max-unavailable=3 \
        [--zone=ZONE | --region=REGION]
    

**Perform a rolling update of all VM instances, but create up to 10% new instances above the target size at a time**

For example, if you have 1,000 instances and you run the following command, the Updater creates up to 100 instances before it starts to remove instances that are running the previous instance template.
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=NEW_TEMPLATE \
        --max-surge=10% \
        [--zone=ZONE | --region=REGION]
    

## Canary updates

A canary update is an update that is applied to a subset of instances in the group. With a canary update, you can test new features or upgrades on a random subset of instances, instead of rolling out a potentially disruptive update to all your instances. If an update is not going well, you only need to roll back the subset of instances, minimizing the disruption for your users.

A canary update is the same as a standard rolling update, except that the number of instances that should be updated is less than the total size of the instance group. Like a standard rolling update, you can configure additional options to control the level of disruption to your service.

### Start a canary update

To initiate a canary update, specify up to two instance template versions, typically a new instance template to canary and the current instance template for the remainder of the instances. For example, you can specify that 20% of your instances be created based on `NEW_INSTANCE_TEMPLATE` while the rest of the instances continue to run on the `OLD_INSTANCE_TEMPLATE`. You can't specify more than two instance templates at a time. The `NEW_INSTANCE_TEMPLATE` can be either a regional instance template from the same region as that of your MIG or a global instance template.

You must always specify a target size (`targetSize`) for the canary version. You can't initiate a canary update if you omit the target size for the canary version. For example, if you specified that 10% of instances should be used for canarying, the remaining 90% are untouched and use the current instance template.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * For zonal MIGs, all permissions required to call the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch)
  * For regional MIGs, all permissions required to call the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the managed instance group that you want to update.

  3. Click **Edit**.

  4. Click **Instance template & overrides** to expand the section. 

     1. Click **Add a template for testing**.

     2. In the **Instance template for testing** list, select a new template. 

If the template that you want to test is not available, use the **Create a new instance template** option and follow the prompts to create one.

     3. In the **Target running** field, enter the number or percentage of instances to which you want to apply the new template.

     4. In the **Instances or percentage** field, select either **instances** or **percent** indicating the number that you entered in the **Target running** field.
  5. Optional: To configure other options for the updates, click **Update policy** to expand the section. Modify the fields as needed.

  6. Click **Save** to start the update.




###  gcloud 

Use the [`rolling-action start-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/start-update). Provide both the current template and the new template to explicitly express how many instances should use each template:
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=CURRENT_INSTANCE_TEMPLATE \
        --canary-version=template=NEW_TEMPLATE,target-size=SIZE \
        [--zone=ZONE | --region=REGION]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the instance group name.
  * `CURRENT_INSTANCE_TEMPLATE`: the current instance template used by the group.
  * `NEW_TEMPLATE`: the new template that you want to test.
  * `SIZE`: the number or percentage of instances that you want to apply this update to. You must apply the `target-size` property to the `--canary-version` template. You can only set a percentage if the group contains 10 or more instances.
  * `ZONE`: for zonal MIGs, provide the [zone](https://docs.cloud.google.com/compute/docs/regions-zones).
  * `REGION`: for regional MIGs, provide the region.



For example, the following command performs a canary update that rolls out `example-template-B` to 10% of instances in the group:
    
    
    gcloud compute instance-groups managed rolling-action start-update example-mig \
        --version=template=example-template-A \
        --canary-version=template=example-template-B,target-size=10%
    

###  REST 

Call the `patch` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) MIG resource. In the request body, include both the current instance template and the new instance template that you want to canary. For example:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
     "versions": [
      {
       "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE",
       "targetSize": {
        "[percent|fixed]": NUMBER|PERCENTAGE # Use `fixed` for a specific number of instances
       }
      },
      {
       "instanceTemplate": "global/instanceTemplates/CURRENT_INSTANCE_TEMPLATE"
      }
     ]
    }

Replace the following:

  * `NEW_TEMPLATE`: the name of the new template you want to canary.
  * `NUMBER|PERCENTAGE`: the fixed number or percentage of instances to canary this update. You can only set a percentage if the group contains 10 or more instances. Otherwise, provide a fixed number.
  * `CURRENT_INSTANCE_TEMPLATE`: the current instance template used by the group.



For more options, see Configuring options for your update.

After you make a request, you can monitor the update to know when the update has finished.

### Roll forward a canary update

After running a canary update, you can decide whether you want to commit the update to 100% of the MIG or roll it back.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the managed instance group that you want to update.

  3. Click **Edit**.

  4. For the instance template that you selected for testing, update the **Target running** value of the test template to **100%** to roll forward the test template to all your instances.

Alternatively, you can replace the original template with the test template and delete the instance template for testing.

  5. Click **Save** to start the update.




###  gcloud 

If you want to commit to your canary update, roll forward the update by issuing another [`rolling-action start-update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/start-update) but set only the `version` flag and omit the `--canary-version` flag.
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=NEW_TEMPLATE \
        [--zone=ZONE | --region=REGION]
    

###  REST 

Call the `patch` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) MIG resource. In the request body, specify the new instance template as a `version` and omit the earlier instance template from your request body. Omit the target size specification to roll out the update to 100% of instances. For example:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
    "versions": [
       {
       "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE" # New instance template
       }
     ]
    }
    

## Monitor updates

After you initiate an update, it can take some time for the new configuration to finish rolling out to all affected instances. You can monitor the progress of an update by checking the following:

  * To verify if all VMs have reached their target template version, view the group status.
  * To verify that specific VMs have reached their target template version, view current actions on instances.
  * For stateful MIGs, see also [Verifying whether per-instance configurations have been applied](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#verifying_whether_per-instance_configs_have_been_applied).



### Group status

At the group level, Compute Engine populates a read-only field called `status` that contains a `versionTarget.isReached` flag and an `isStable` flag. You can use the gcloud CLI or REST to access these flags. You can also use the Google Cloud console to see the current and planned number of instances being updated.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the MIG



###  Console 

You can monitor a rolling update for a group by going to the group's details page.

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the managed instance group that you want to monitor. The overview page for the group shows the template that each instance is using.

  3. To view the details, click the **Details** tab.

  4. In the **Instance template** section, you can see the current and target number of instances for each instance template.

  5. To view the update settings, click **Update parameters** to expand.




###  gcloud 

Use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).
    
    
    gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
        [--zone=ZONE | --region=REGION]
    

You can also use the [`gcloud compute instance-groups managed wait-until` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until) with the `--version-target-reached` flag to wait until `status.versionTarget.isReached` is set to `true` for the group:
    
    
    gcloud compute instance-groups managed wait-until INSTANCE_GROUP_NAME \
        --version-target-reached \
        [--zone=ZONE | --region=REGION]
    

###  REST 

Call the `get` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) MIG resource.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/get

#### Verify whether an update rollout is complete

Verify whether the rollout of an update is complete by checking the value of the MIG's `status.versionTarget.isReached` field:

  * `status.versionTarget.isReached` set to `true` indicates that all VM instances have been or are being created using the target version.

  * `status.versionTarget.isReached` set to `false` indicates that at least one VM is not yet using the target version. Or, in the case of a canary update, `false` indicates that the number of VMs using a target version doesn't match its target size.


**Note:** To verify that the update rollout is complete and also that all VM instances in the group are running and healthy, check both the `status.isStable` and `status.versionTarget.isReached` flags.

#### Check whether a managed instance group is stable

Verify that all instances in a managed instance group are running and healthy by checking the value of the group's `status.isStable` field. 

`status.isStable` set to `false` indicates that changes are active, pending, or that the MIG itself is being modified.

`status.isStable` set to `true` indicates the following:

  * None of the instances in the MIG are undergoing any type of change and the `currentAction` for all instances is `NONE`.
  * No changes are pending for instances in the MIG.
  * The MIG itself is not being modified.



Remember that the stability of a MIG depends on numerous factors because a MIG can be modified in numerous ways. For example:

  * You make a request to roll out a new instance template.
  * You make a request to create, delete, resize or update instances in the MIG.
  * An [autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler#fundamentals) requests to resize the MIG.
  * An [autohealer](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) resource is replacing one or more unhealthy instances in the MIG.
  * In a regional MIG, some of the instances are being [redistributed](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution).



As soon as all actions are finished, `status.isStable` is set to `true` again for that MIG.

### Current actions on instances

To view details about instances in a MIG, including their status and any current actions being performed by the group, use the Google Cloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the group
  * `compute.instanceGroupManagers.list` on the group



###  gcloud 

**All managed instances**

To check the status and current actions on all instances in the group, use the [`list-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances).
    
    
    gcloud compute instance-groups managed list-instances INSTANCE_GROUP_NAME \
        [--zone=ZONE | --region=REGION]

The command returns a list of instances in the group, including their status, current actions, and other details:
    
    
    NAME: vm-instances-9pk4
    ZONE: us-central1-f
    STATUS:
    HEALTH_STATE:
    ACTION: CREATING
    INSTANCE_TEMPLATE: my-new-template
    VERSION_NAME:
    LAST_ERROR:
    
    NAME: vm-instances-h2r1
    ZONE: us-central1-f
    STATUS: STOPPING
    HEALTH_STATE:
    ACTION: DELETING
    INSTANCE_TEMPLATE: my-old-template
    VERSION_NAME:
    LAST_ERROR:
    

The `HEALTH_STATE` column appears empty unless you have [set up health checking](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs).

**A specific managed instance**

To check the status and current action for a specific instance in the group, use the [`describe-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe-instance).
    
    
    gcloud compute instance-groups managed describe-instance INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME \
        [--zone=ZONE | --region=REGION]

The command returns details about the instance, including instance status, current action, and, for stateful MIGs, preserved state:
    
    
    currentAction: NONE
    id: '6789072894767812345'
    instance: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/example-mig-hz41
    instanceStatus: RUNNING
    name: example-mig-hz41
    preservedStateFromConfig:
      metadata:
        example-key: example-value
    preservedStateFromPolicy:
      disks:
        persistent-disk-0:
          autoDelete: NEVER
          mode: READ_WRITE
          source: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/disks/example-mig-hz41
    version:
      instanceTemplate: https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-template
    

###  REST 

Call the `listManagedInstances` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) MIG resource. For example, to see details about the instances in a zonal MIG resource, you can make the following request:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME/listManagedInstances

The call returns a list of instances for the MIG including each instance's `instanceStatus` and `currentAction`.
    
    
    {
      "managedInstances": [
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-f/instances/vm-instances-prvp",
          "instanceStatus": "RUNNING",
          "currentAction": "REFRESHING",
          "id": "5317605642920955957",
          "version": {
            instanceTemplate": "https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-template"
          },
          "name": "vm-instances-prvp"
        },
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-f/instances/vm-instances-w2t5",
          "instanceStatus": "RUNNING",
          "currentAction": "REFRESHING",
          "id": "2800161036826218547",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-template"
          },
          "name": "vm-instances-w2t5"
        }
      ]
    }
    

If you [set up health checking](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs), then the response also includes the `instanceHealth` field.

To see a list of valid `instanceStatus` field values, see [VM instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

If an instance is undergoing some type of change, the MIG sets the instance's `currentAction` field to one of the following actions to help you track the progress of the change. Otherwise, the `currentAction` field is set to `NONE`.

Possible `currentAction` values are:

  * `ABANDONING`. The instance is being removed from the MIG.
  * `CREATING`. The instance is in the process of being created.
  * `CREATING_WITHOUT_RETRIES`. The instance is being created without retries; if the instance isn't created on the first try, the MIG doesn't try to replace the instance again.
  * `DELETING`. The instance is in the process of being deleted.
  * `RECREATING`. The instance is being replaced.
  * `REFRESHING`. The instance is being removed from its current target pools and being readded to the list of current target pools (this list might be the same or different from existing target pools).
  * `RESTARTING`. The instance is in the process of being restarted using the `stop` and `start` methods.
  * `RESUMING`. The instance is in the process of being resumed after being suspended.
  * `STARTING`. The instance is in the process of being started after being stopped.
  * `STOPPING`. The instance is being stopped.
  * `SUSPENDING`. The instance is being suspended.
  * `VERIFYING`. The instance has been created and is in the process of being verified.
  * `NONE`. No actions are being performed on the instance.

**Note:** The `pendingActions` field is deprecated and is to be removed. Contact [cloud-updater-feedback@google.com](mailto:cloud-updater-feedback@google.com) to leave feedback if your workload relies on this field.

## Roll back an update

There is no explicit command for rolling back an update to a previous version, but if you decide to roll back an update (either a fully committed update or a canary update), you can do so by making a new update request and passing in the instance template that you want to roll back to.

###  gcloud 

For example, the following gcloud CLI command rolls back an update as fast as possible. Replace `OLD_INSTANCE_TEMPLATE` with the name of the instance template you want to roll back to.
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --version=template=OLD_INSTANCE_TEMPLATE \
        --max-unavailable=100% \
        [--zone=ZONE | --region=REGION]

###  REST 

Call the `patch` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) MIG resource.

In the request body, specify the earlier instance template as a `version`:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "updatePolicy":
      {
        "maxUnavailable":
        {
          "percent": 100
        }
      },
      "versions": [
        {
          "instanceTemplate": "global/instanceTemplates/OLD_INSTANCE_TEMPLATE" # Old instance template
        }
      ]
    }

For a regional MIG with less than 10 instances, you must use a fixed value for `maxUnavailable` and set the value to the number of instances in the group.

The Updater treats a rollback request the same as a regular update request, so you can specify additional update options.

**Caution:** For canary updates, we strongly recommend fully rolling back canary updates before you try to canary another version. There is no way to selectively choose which instances are updated based on which instance template, and performing another canary update on top of an existing update can cause unintended consequences. As a best practice, you should fully roll back a canary update first and restart the canary process again from the beginning.

## Stop an update

There is no explicit method or command to stop an update. You can change an update from proactive to opportunistic, and if the group is not being resized by other services like autoscaler, the change to opportunistic effectively stops the update.

To change an update from proactive to opportunistic by using the gcloud CLI, run the following command:
    
    
    gcloud compute instance-groups managed rolling-action stop-proactive-update INSTANCE_GROUP_NAME \
        [--zone=ZONE | --region=REGION]

To stop the update completely after converting it from proactive to opportunistic, follow these steps:

  1. Make a request to determine how many instances have been updated:
         
         gcloud compute instance-groups managed list-instances INSTANCE_GROUP_NAME \
            [--zone=ZONE | --region=REGION]

The gcloud CLI returns a response that includes a list of instances in the group and their current statuses:
         
         NAME               ZONE           STATUS   HEALTH_STATE  ACTION    INSTANCE_TEMPLATE  VERSION_NAME  LAST_ERROR
         vm-instances-9pk4  us-central1-f  RUNNING  HEALTHY       NONE      example-new-template
         vm-instances-j1h8  us-central1-f  RUNNING  HEALTHY       NONE      example-old-template
         vm-instances-ngod  us-central1-f  STAGING  UNKNOWN       CREATING  example-new-template
         

In this example, two instances have already been updated.

  2. Next, make a request to perform a new update, but pass in the number of instances that have already been updated as the target size:
         
         gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
            --version template=OLD_INSTANCE_TEMPLATE \
            --canary-version template=NEW_INSTANCE_TEMPLATE,target-size=2 \
            [--zone=ZONE | --region=REGION]

To the Updater, this update appears complete, so no other instances are updated, effectively stopping the update.




## Control the speed of a rolling update

By default, when you make an update request, the Updater performs the update as fast as possible. If you aren't sure you want to apply an update fully or are tentatively testing your changes, you can control the speed of the update by using the following methods.

  1. Start a canary update rather than a full update.
  2. Set a large `minReadySec` value. Setting this value causes the Updater to wait this number of seconds before considering the instance successfully updated and proceeding to the next instance.
  3. [Enable health checking](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) to cause the Updater to wait for your application to start and to report a healthy signal before considering the instance successfully updated and proceeding to the next instance.
  4. Set low `maxUnavailable` and `maxSurge` values. This ensures that only a minimal number of instances are updated at a time.
  5. [Selectively update instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig) instead of using an automated update.



You can also use a combination of these methods to control the rate of your update.

## Control the disruption level during a rolling update

Depending on the nature of an update, it might disrupt an instance's [lifecycle state](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle). For example, changing an instance's boot disk requires replacing the instance. You can control the level of disruption during a rolling update by setting the following options:

  * **Minimal action** : Use this option to minimize disruption as much as possible or to apply a more disruptive action than is necessary.

    * To limit disruption as much as possible, set the minimal action to `REFRESH`. If your update requires a more disruptive action, Compute Engine performs the necessary action to execute the update.
    * To apply a more disruptive action than is strictly necessary, set the minimal action to `RESTART` or `REPLACE`. For example, Compute Engine does not need to restart a VM to change its metadata. But if your application reads instance metadata only when a VM is restarted, you can set the minimal action to `RESTART` in order to pick up metadata changes.
  * **Most disruptive allowed action** : Use this option to prevent an update if it requires more disruption than you can afford. If your update requires a more disruptive action than you set with this flag, the update request fails. For example, if you set the most disruptive allowed action to `RESTART`, then an attempt to update the boot disk image fails because that update requires instance replacement, a more disruptive action than a restart.




Both of these options accept the following values:

Value | Description | Which instance properties can be updated?  
---|---|---  
`REFRESH` | Don't stop the instance. | Additional disks, Dynamic Network Interfaces (NICs), instance metadata, labels, tags  
`RESTART` | Stop the instance and start it again. | Additional disks, Dynamic NICs, instance metadata, labels, tags, machine type  
`REPLACE` | (Default) Replace the instance according to the replacement method option. | All instance properties stored in the instance template or per-instance configuration  
  
The most disruptive allowed action can't be less disruptive than the minimal action.

When you automatically roll out updates, the following defaults apply:

  * The default minimal action is `REPLACE`. If you want to prevent unnecessary disruption, set the minimal action to be less disruptive.
  * The default most disruptive allowed action is `REPLACE`. If you cannot tolerate such disruption, set the most disruptive allowed action to be less disruptive.



You can change the default behavior by using the Compute Engine API to set the `updatePolicy.minimalAction` and `updatePolicy.mostDisruptiveAllowedAction` fields in your MIG resource–for example, by calling the `regionInstanceGroupManagers.patch` method. Alternatively, you can select the specific **Actions allowed to update VMs** when you update your MIG from the Google Cloud console. To view the current settings, see [Getting a MIG's properties](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties).

An update fails if it requires a more disruptive action than you allowed. If this happens, you can try the update again with a more disruptive allowed action, or you can [selectively update the instance](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#updating_selected_instances). Compute Engine performs best-effort validation to see if instances can be updated with the specified disruption limit. But due to concurrent changes in the system, the situation can change after the update starts. If an operation on a particular instance fails, [list instance errors](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors) to see the error.

## Perform a rolling restart or replace

A _rolling restart_ stops and restarts all instances, and a _rolling replace_ replaces all instances according to the replacement method option. You might want to perform a rolling restart or replace for the following reasons:

  * Clear up memory leaks.
  * Restart your application so it can run from a fresh machine.
  * Apply a periodic replace as a best practice to test your instances.
  * Update your instance's operating system image or rerun startup scripts to update your software.



When you perform a rolling restart or replace of the instances using Google Cloud console or Google Cloud CLI, the following underlying actions take place in the MIG. However, if you use REST, then you must set these fields in the request to trigger a restart or replace operation.

  * If the `updatePolicy.type` is `OPPORTUNISTIC`, then the MIG changes the type to `AUTOMATIC`.
  * The MIG updates the `versions.name` of each instance.



To perform a rolling restart or replace, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the managed instance group that has the VMs that you want to restart or replace.

  3. Click **Restart/replace VMs**.

  4. In the **Operation** section, select **Restart** or **Replace**.

     * If you select **Restart** , modify the following parameters or use the default values: 
       * Maximum unavailable instances
       * Minimum wait time
     * If you select **Replace** , do the following: 
       1. Choose if you want to keep the instances names when replacing instances.
       2. Specify the following parameters or use the default values: 
          * Temporary additional instances
          * Maximum unavailable instances
          * Minimum wait time
  5. To start the operation, click **Restart VMs** or **Replace VMs**.




###  gcloud 

Use the [`restart` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/restart) or [`replace` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action/replace).

The following commands performa a rolling restart or replace of instances in a zonal MIG. For a regional MIG, replace the `--zone=ZONE` flag with `--region=REGION`.

  * To restart all instances in a zonal MIG, one at a time:
        
        gcloud compute instance-groups managed rolling-action restart INSTANCE_GROUP_NAME \
            --zone=ZONE
        

  * To replace all instances in a zonal MIG, one at a time:
        
        gcloud compute instance-groups managed rolling-action replace INSTANCE_GROUP_NAME \
            --zone=ZONE
        




You can further customize these commands with the same options available for updates—for example, `--max-surge` and `--max-unavailable`.

###  REST 

Send a `PATCH` request using one of the following methods:

  * For a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
  * For a zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch).



In the request body, you must set the following fields. If you don't specify these fields, the request might still succeed, but the MIG doesn't perform restart or replace operation.

  * Set the `updatePolicy.minimalAction` field to either `RESTART` or `REPLACE`.

  * Set the `versions.name` field. For example, specify a version number with a timestamp—`v2-ddmmyyhhmm`.

  * Set the `versions.instanceTemplate` field to the current template URL.




To restart all instances in a zonal MIG, make the following request. To replace all instances, set the `minimialAction` field to `REPLACE` in the same request.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
     "updatePolicy": {
      "minimalAction": "RESTART",
      "type": "PROACTIVE"
     },
     "versions": [
      {
       "instanceTemplate": "global/instanceTemplates/CURRENT_INSTANCE_TEMPLATE",
       "name": "v2-1705499403"
      }
     ]
    }
    

You can further customize the request with the same options available for updates—for example, `maxSurge` and `maxUnavailable`.

After you finish a restart or replace operation, you can [list the MIG's VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) and inspect each VM's `versions.name` field to determine which VMs have been restarted or replaced.

### Additional replace/restart examples

**Perform a rolling restart of all VMs, two at a time**

The following command restarts all VMs in the group, two at a time. Notice that a new instance template isn't specified.
    
    
    gcloud compute instance-groups managed rolling-action restart INSTANCE_GROUP_NAME \
        --max-unavailable=2 \
        [--zone=ZONE | --region=REGION]

**Perform a rolling restart of all VMs as quickly as possible**
    
    
    gcloud compute instance-groups managed rolling-action restart INSTANCE_GROUP_NAME \
        --max-unavailable=100% \
        [--zone=ZONE | --region=REGION]

**Perform a rolling replace of all VMs as quickly as possible**
    
    
    gcloud compute instance-groups managed rolling-action replace INSTANCE_GROUP_NAME  \
        --max-unavailable=100% \
        [--zone=ZONE | --region=REGION]

## Preserve instance names

If you need to preserve the names of your VM instances across an update, set the `replacementMethod` to `RECREATE`. You must also set `maxUnavailable` to be greater than `0` and `maxSurge` to be `0`. Recreating instances instead of replacing them causes your update to take longer to complete, but the updated instances keep their names.

If you do not specify a replacement method, the MIG's current `updatePolicy.replacementMethod` value is used. If it's not set then the default value of `substitute` is used, which replaces VM instances with new instances that have randomly generated names.

###  gcloud 

When issuing a [`rolling-action` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/rolling-action), include the `--replacement-method=recreate` flag.
    
    
    gcloud compute instance-groups managed rolling-action start-update INSTANCE_GROUP_NAME \
        --replacement-method=recreate \
        --version=template=NEW_TEMPLATE \
        --max-unavailable=5 \
        [--zone=ZONE | --region=REGION]
    

###  REST 

Call the `patch` method on a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) or [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) MIG resource. In the request body, include the `updatePolicy.replacementMethod` field:
    
    
    PATCH /compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    {
        "updatePolicy": {
            "type": "PROACTIVE",
            "maxUnavailable": { "fixed": 5 },
            "replacementMethod": "RECREATE"
        },
        "versions": [ {
            "instanceTemplate": "global/instanceTemplates/NEW_TEMPLATE"
        } ]
    }

After you make a request, you can monitor the update to know when the update has finished.

## Update a regional managed instance group

A [regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) contains VM instances that are spread across multiple zones within a region, as opposed to a zonal MIG, which only contains instances in one zone. Regional MIGs let you distribute your instances across more than one zone to improve your application's availability and to support extreme cases where one zone fails or an entire group of instances stops responding.

Performing an update on a regional MIG is same as performing an update on a zonal MIG, with a few exceptions described below. When you initiate an update to a regional MIG, the Updater always updates instances proportionally and evenly across each zone. You cannot choose which instances in which zones are updated first nor can you choose to update instances in only one zone.

### Differences between updating regional versus zonal MIGs

Regional MIGs have the following default update values:

  * `maxUnavailable=NUMBER_OF_ZONES`
  * `maxSurge=NUMBER_OF_ZONES`



`NUMBER_OF_ZONES` is the number of zones associated with the regional MIG. By default, the number of zones for a regional MIG is `3`. But you might [select](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#selectingzones) a different number.

If you are using fixed numbers when specifying an update, the fixed number must be either `0` or equal to or greater than the number of zones associated with the regional MIG. For example, if the group is distributed across three zones, then you can't set `maxSurge` to `1` or to `2` because the Updater has to create an additional instance in each of the three zones.

### Use a fixed number or a percentage in update requests

If you specify a fixed number in your update requests, the number you specify is divided by the number of zones in the regional MIG and distributed evenly. For example, if you specify `maxSurge=10`, then the Updater divides 10 across the number of zones in the region and creates instances based on that number. If the number of instances does not divide evenly across zones, the Updater adds the remaining instances to a random zone. So, for 10 instances across three zones, two of the zones get 3 instances and one zone gets 4 instances. The same logic is applied to the `maxUnavailable` and the `targetSize` parameters for canary updates.

You can specify a percentage only if your MIG contains 10 or more VM instances. Percentages are handled slightly differently depending on the situation:

  * If you specify a percentage of VM instances for a canary update, the Updater attempts to distribute the instances evenly across zones. The remainder is rounded either up or down in each zone but the total difference isn't more than 1 VM instance per group. For example, for a MIG with 10 instances and a target size percentage of 25%, the update is rolled out to 2 to 3 VM instances.

  * If you specify a percentage for update options like `maxSurge` and `maxUnavailable`, the percentages are rounded independently per zone.




## What's next

  * Learn about [Viewing info about MIGs and managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs).
  * Learn about [Creating instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).
  * Learn how to use image families and a rolling replace to [update the OS image](https://docs.cloud.google.com/compute/docs/instance-groups/upgrading-images-in-migs) on all VMs in a MIG.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
