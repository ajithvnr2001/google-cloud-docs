---
url: https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic/
title: Override instance template properties with an all-instances configuration \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:36.858125+00:00
---

# Override instance template properties with an all-instances configuration  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/set-mig-aic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Override instance template properties with an all-instances configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can use an all-instances configuration to set [labels](https://docs.cloud.google.com/compute/docs/labeling-resources) and [metadata](https://docs.cloud.google.com/compute/docs/metadata/overview) properties for all virtual machine (VM) instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) without the need to create a new instance template.

You can continue to use instance templates to set instance properties in MIG. However, using a MIG's all-instances configuration is easier in some scenarios, such as the following:

  * You need to update instance metadata or labels frequently and without the overhead of creating new templates each time. Remember that instance templates are immutable, which means they cannot be modified after they are created.

  * You want to have multiple MIGs based on one instance template, but you need to configure labels or metadata for each MIG differently. For example, if you have one app but you want to support different environments for development, testing, and production. You can create a single instance template and reuse it for all environments by setting different metadata with a different all-instances configuration for each environment.

  * You have one team who owns infrastructure and images while another team runs apps that require configuration. You can have one team provision infrastructure with an instance template while the app team can manage app configurations with all-instances configurations.

  * You have an agent running on your VMs and you want to configure it using metadata. You want to make sure the VM agent configuration persists even after the group's instance template changes. Use the instance template to control the app version and configure the VM agent using an all-instances configuration.




If you set the same property using both the MIG's instance template and its all-instances configuration, the MIG prioritizes the value from the all-instances configuration. For example, if metadata for `enable-guest-attributes` is set to `FALSE` in the MIG's instance template and `TRUE` in the MIG's all-instances configuration then Compute Engine applies `TRUE` on all instances in the group. This lets you use an all-instances configuration to override properties that are defined in the instance template.

## Before you begin

  * [Create a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).
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




### Required roles

To get the permissions that you need to set and apply an all-instances configuration, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to set and apply an all-instances configuration. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to set and apply an all-instances configuration:

  * To get the MIG: `compute.instanceGroupManagers.get` on the project 
  * To update the MIG's all-instances configuration: `compute.instanceGroupManagers.update` on the project 
  * To use an instance template when updating the MIG: `compute.instanceTemplates.get` on the project 
  * To create instances with the specified properties: `compute.instances.create` on the project 
  * To apply metadata to existing VMs: `compute.instances.setMetadata` on the project 
  * To apply labels to existing VMs: `compute.instances.setLabels` on the project 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Limitations

  * You can only override the following instance template properties with an all-instances configuration:

    * Metadata
    * Labels
  * You cannot canary update an all-instances configuration. When you apply the configuration to the group, Compute Engine applies the properties to all new instances, and to existing instances based on your [update policy](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs). If you want to control which existing instances get updated when, you can use [selective updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#selective_updates).

  * If you use stateful configuration in your MIG, you cannot set the same property in any [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) and at the same time in the group's all-instances configuration.




## Set properties in an all-instances configuration

Create and update a MIG's all-instances configuration using the gcloud CLI or REST.

**Note:** The configuration that you specify for VMs in a MIG is automatically applied to new VMs that are added to the group. To apply the latest configuration to existing VMs, see Apply an all-instances configuration to existing VMs.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the MIG of which you want to set the all-instances configuration.

  3. Click **Edit**.

  4. Click **Instance template & overrides** to expand the section.

  5. In the **All-instances configuration** section, do the following:

     * To add or update metadata values, click **Manage metadata**. Complete the setup and click **Save**.
     * To add or update labels, click **Manage labels**. Complete the setup and click **Save**.
  6. After you finish setting up the properties in the all-instances configuration, click **Save**.

If the MIG's update type is set to **Automatic** , then the all-instances configuration which you set is immediately applied to all existing VMs. If the update type is **Selective** , then you must selectively apply the configuration to existing VMs. For more information, see Apply an all-instances configuration to existing VMs.




###  gcloud 

Add or update an all-instances configuration by using the [`all-instances-config update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/update).
    
    
    gcloud compute instance-groups managed all-instances-config update INSTANCE_GROUP_NAME \
        --metadata=KEY1=VALUE1,KEY2=VALUE2 \
        --labels=KEY3=VALUE3,KEY4=VALUE4
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: name of the MIG.
  * `KEYS` and `VALUES`: key-value pairs for labels or metadata. If the key does not exist, then the update command adds it. For existing keys, their values are updated.



Remember to apply your updated configuration to existing VMs in the MIG.

###  REST 

Add or update an all-instances configuration by making a `PATCH` request on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "allInstancesConfig": {
        "properties": {
          "metadata": {
            "KEY1": "VALUE1",
            ...
          },
          "labels": {
            "KEY2": "VALUE2",
            ...
          },
        }
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in which the MIG exists.
  * `REGION`: the region where your MIG is located. For a zonal MIG, replace `regions/REGION` with `zones/ZONE`.
  * `INSTANCE_GROUP_NAME`: name of the MIG.
  * `KEYS` and `VALUES`: key-value pairs for labels or metadata. If the key does not exist, then the request adds it. For existing keys, its value is updated.



Remember to apply your updated configuration to existing VMs in the MIG.

## Apply an all-instances configuration to existing VMs

The [VM configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#vm_configuration_components) that you specify for VMs in a MIG is automatically applied to new VMs that are added to the group.

To apply an updated VM configuration–including an updated all-instances configuration–to existing VMs in the group, use one of the following methods:

  * **Automatic (proactive)** : Use this method if you want the MIG to automatically apply new configurations to all or to a subset of existing VMs in the group. The level of disruption to running VMs depends on the update policy that you configure. You can use this method to canary update new instance templates. To use this method, set the MIG's update type to "proactive".
  * **Selective (opportunistic)** : Use this method if you want to apply the update manually or if you want to update all existing VMs in the group at once. You target any or all VMs to be updated to the latest configuration. To use this method, set the MIG's update type to "opportunistic".
  * **Re-creation of VMs** : When you re-create a VM in a MIG, the MIG applies any updated configuration that has not yet been applied to that VM. For more information, see [Re-create VMs in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#recreate_instances).



### Automatic (proactive)

If you want to automatically apply an updated all-instances configuration to all existing VMs everytime you make a change to it, then set the group's update policy type to "proactive". For more information, see [Automatic (proactive) update type](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#automatic_proactive_updates).

You can control the speed of a proactive configuration rollout by using the optional [maxUnavailable](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_unavailable), [maxSurge](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_surge), and [minReadySec](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#minimum_wait_time) settings.

To use proactive updates you only need to configure it once. After that, the MIG applies all future VM configuration changes (that is, changes to the group's all-instances configuration, instance template, and per-instance configurations) automatically to all VMs in the group based on the settings in the group's update policy.

To automatically apply configuration updates, use the gcloud CLI or REST.

###  gcloud 

You can configure automatic (proactive) updates by using the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update).
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        **--update-policy-type=proactive** \
        --update-policy-max-unavailable=MAX_UNAVAILABLE \
        --update-policy-max-surge=MAX_SURGE \
        --update-policy-min-ready=MIN_READY \
        --update-policy-minimal-action=MINIMAL_ACTION \
        --update-policy-replacement-method=REPLACEMENT_METHOD
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `MAX_UNAVAILABLE` (optional): maximum number of instances that can be unavailable during the update. For example, if you set the `update-minimal-action` flag to `restart` then this flag limits how many VMs are restarted at a time. This can be a fixed number (for example, `5`) or a percentage of size to the managed instance group (for example, `10%`).
  * `MAX_SURGE` (optional): maximum additional number of instances that can be created during the update. This can be a fixed number (for example, `5`) or a percentage of size to the managed instance group (for example, `10%`).
  * `MIN_READY` (optional): minimum time for which a restarted or replaced VM should be ready to be considered available. For example `10s` for 10 seconds. See [gcloud topic datetimes](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes) for information on duration formats.
  * `MINIMAL_ACTION` (optional): action to perform on each instance during the configuration update: 
    * `refresh`: apply the new configuration on running instances without restarting them.
    * `restart`: restart VMs during the update, which is useful if your app reads metadata only during reboot.
    * `replace`: delete VMs and create new ones to apply the new configuration to.
  * `REPLACEMENT_METHOD` (optional): specifies what action is used to replace an instance: 
    * `recreate`: waits for the old instance to be deleted then creates a new instance with the same name as the old one.
    * `substitute`: creates an instance with a new name while deleting the old instance



###  REST 

You can configure automatic (proactive) updates by making a `PATCH` request on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or a [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "updatePolicy": {
        **"type": "PROACTIVE"** ,
        "maxUnavailable": {
          "percent": MAX_UNAVAILABLE
        },
        "maxSurge": {
          "percent": MAX_SURGE
        },
        "minimalAction": MINIMAL_ACTION,
        "replacementMethod": REPLACEMENT_METHOD
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the [project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in which the MIG exists.
  * `REGION`: the region where your MIG is located. For a zonal MIG, replace `regions/REGION` with `zones/ZONE`.
  * `INSTANCE_GROUP_NAME`: name of the MIG.
  * `MAX_UNAVAILABLE` (optional): maximum number of instances that can be unavailable during the update. For example if you set the `update-minimal-action` flag to `RESTART` then this flag limits how many VMs are restarted at a time. This can be a percentage (for example, specify `"percent": 80` for 80%) or a fixed number. To specify a fixed number, replace `"percent": MAX_UNAVAILABLE` with `"fixed": MAX_UNAVAILABLE`.
  * `MAX_SURGE` (optional): maximum additional number of instances that can be created during the update. This can be a percentage or a fixed number.
  * `MINIMAL_ACTION` (optional): action to perform on each instance during the configuration update: 
    * `REFRESH`: apply the new configuration on running instances without restarting them.
    * `RESTART`: restart VMs during the update, which is useful if your app reads metadata only during reboot.
    * `REPLACE`: delete VMs and create new ones to apply the new configuration to.
  * `REPLACEMENT_METHOD` (optional): specifies what action is used to replace an instance: 
    * `RECREATE`: waits for the old instance to be deleted then creates a new instance with the same name as the old one.
    * `SUBSTITUTE`: creates an instance with a new name while deleting the old instance



When optional flags are omitted, the group uses the values in the group's update policy. You can [check the update policy](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#check_update_policy) using the gcloud CLI or REST.

### Selective (opportunistic)

If you want to control when and to which VMs to apply a new configuration to, then set the group's update policy type to "opportunistic". For more information, see [Selective (opportunistic) update type](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#selective_updates).

When you choose to selectively apply configuration updates, any changes to the group's all-instances configuration, instance template, or per-instance configurations are not automatically applied to existing VMs. You must explicitly apply an updated configuration to existing VMs in order to update them.

**Note:** When you enable selective updates by setting the group's update policy type to "opportunistic", you must manually initiate the update on existing VMs every time you make changes to the group's configuration.

To selectively apply VM configuration updates to VMs in a MIG, use the gcloud CLI or REST.

###  gcloud 

You can configure selective (opportunistic) updates by using the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        **--update-policy-type=opportunistic**

When you set the group's update type to `opportunistic`, you must initiate the update when you want to apply the new configuration to existing VMs.

**Apply configuration to specific VMs**

To update selected instances, use the following command:
    
    
    gcloud compute instance-groups managed update-instances INSTANCE_GROUP_NAME \
        **--instances INSTANCE_NAMES** \
        --minimal-action=MINIMAL_ACTION \
        --most-disruptive-allowed-action=MOST_DISRUPTIVE_ALLOWED_ACTION
    

**Apply configuration to all VMs**

To update all existing instances, use the following command:
    
    
    gcloud compute instance-groups managed update-instances INSTANCE_GROUP_NAME \
        **--all-instances** \
        --minimal-action=MINIMAL_ACTION \
        --most-disruptive-allowed-action=MOST_DISRUPTIVE_ALLOWED_ACTION
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: name of the MIG.
  * `INSTANCE_NAMES`: a list of instances to apply the template to.
  * `MINIMAL_ACTION` (optional): action to perform on each instance during its configuration update: 
    * `refresh` (default): apply the new configuration on running instances without restarting them.
    * `restart`: restart VMs during the update, which is useful if your app reads metadata only during reboot.
    * `replace`: delete VMs and create new ones to apply the new configuration to.
  * `MOST_DISRUPTIVE_ALLOWED_ACTION` (optional): perform at most this action on each instance. If the configuration update requires a more disruptive action than the one specified here, then the update fails and no changes are made. 
    * `none`: no action
    * `refresh`: apply the new configuration without stopping instances, if possible. For example, use `refresh` to apply changes that only affect metadata or additional disks.
    * `restart`: apply the new configuration without replacing instances, if possible. For example, stopping instances and starting them again is sufficient to apply changes to machine type.
    * `replace`: replace old instances according to the `--replacement-method` flag.



###  REST 

You can configure selective (opportunistic) updates by making a `PATCH` request on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "updatePolicy": {
        **"type": "OPPORTUNISTIC"**
      }
    }

When you set the group's update type to `OPPORTUNISTIC`, you must initiate the update when you want to apply the new configuration to existing VMs.

**Apply configuration to specific VMs**

To update specific instances, use the following request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/applyUpdatesToInstances
    
    {
      "instances": [
        "zones/ZONE/instances/INSTANCE_NAME_1",
        "zones/ZONE/instances/INSTANCE_NAME_2"
      ],
      "minimalAction": MINIMAL_ACTION,
      "mostDisruptiveAllowedAction": MOST_DISRUPTIVE_ALLOWED_ACTION
    }

**Apply configuration to all VMs**

To update all existing instances, use the following request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/applyUpdatesToInstances
    
    {
      **"allInstances": true,**
      "minimalAction": MINIMAL_ACTION,
      "mostDisruptiveAllowedAction": MOST_DISRUPTIVE_ALLOWED_ACTION
    }

Replace the following:

  * `PROJECT_ID`: the [project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) in which the MIG exists.
  * `REGION`: the region where your MIG is located. For a zonal MIG, replace `regions/REGION` with `zones/ZONE`.
  * `INSTANCE_GROUP_NAME`: name of the MIG.
  * `MINIMAL_ACTION` (optional): action to perform on each instance during the configuration update: 
    * `REFRESH`: apply the new configuration on running instances without restarting them.
    * `RESTART`: restart VMs during the update, which is useful if your app reads metadata only during reboot.
    * `REPLACE`: delete VMs and create new ones to apply the new configuration to.
  * `MOST_DISRUPTIVE_ALLOWED_ACTION` (optional): perform at most this action on each instance. If the configuration update requires a more disruptive action than the one specified here, then the update fails and no changes are made. 
    * `NONE`: no action
    * `REFRESH`: apply the new configuration without stopping instances, if possible. For example, use `REFRESH` to apply changes that only affect metadata or additional disks.
    * `RESTART`: apply the new configuration without replacing instances, if possible. For example, stopping instances and starting them again is sufficient to apply changes to machine type.
    * `REPLACE`: replace old instances according to the group's `updatePolicy.replacementMethod` field.



## Verify if an updated all-instances configuration has been applied

You can verify if the latest all-instances configuration has been applied to all VMs in the group by using one of the following ways.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the MIG of which you want to view the all-instances configuration.

  3. Go to the **Details** tab.

  4. If the latest all-instances configuration is applied to all VMs, then in the **All instances configuration** section, the **Last modified** timestamp and the **Status** field must show the values as follows:

     * **Last modified** : Shows the time that you applied the all-instances configuration to all VMs.
     * **Status** : Shows **Applied to all VMs**. If the all-instances is not applied to all VMs, then the status is shown as **Pending VM update**.



###  gcloud 

Use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) and include the `--format` flag to look for the `status.allInstancesConfig.effective` value.
    
    
    gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
        --format="(status.allInstancesConfig)"

Sample output:
    
    
    status:
      allInstancesConfig:
        **currentRevision: 2022-12-02T10:30:15.012345Z
        effective: true**

If the `effective` value is set to `true`, then all VMs have the latest configuration applied. The `currentRevision` value shows the timestamp of the latest change to the group's all-instances configuration.

If the `effective` value is set to `false`, then the latest configuration is not yet applied to all VMs.

To check the status of each VM, you can [list all of the MIG's VMs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) or check each VM individually with the [`describe-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe-instance):
    
    
    gcloud compute instance-groups managed describe-instance INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME

Sample output:
    
    
    **allInstancesConfig:
      revision: 2022-12-02T10:30:15.012345Z**
    currentAction: NONE
    id: '8393021473297481188'
    instance: .../projects/PROJECT/zones/ZONE/instances/INSTANCE_NAME
    instanceStatus: RUNNING
    name: INSTANCE_NAME
    version:
      instanceTemplate: .../projects/PROJECT/global/instanceTemplates/INSTANCE_TEMPLATE
    

To see which VMs have the latest configuration applied, compare the `revision` timestamp on each VM with the `currentRevision` timestamp on the MIG.

###  REST 

Make a `GET` request on [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG to check for the value of `status.allInstancesConfig.effective` flag.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    

Sample response:
    
    
    {
      ...
      "status": {
        "isStable": "true",
        "versionTarget": {
          "isReached": "true"
        },
        "allInstancesConfig": {
          **"currentRevision": "2022-12-02T10:30:15.012345Z",
          "effective": "true"**
        },
      ...
      },
      ...
    }

If the `effective` field is set to `true` then all VMs have the latest configuration applied. The `currentRevision` field shows the timestamp of the latest change to the group's all-instances configuration.

If the `effective` field is set to `false`, then the latest configuration is not yet applied to all VMs.

To check the status of each instance, list managed instances for the [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances) MIG:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/listManagedInstances
    

Sample output:
    
    
    {
      "managedInstances": [
        ...
        {
          "instance": ".../zones/ZONE/instances/INSTANCE_NAME",
          "instanceStatus": "RUNNING",
          "currentAction": "NONE",
          **"allInstancesConfig": {
            "revision": "2022-12-02T10:30:15.012345Z"**
          },
          "version": {
            "name": "V1",
            "instanceTemplate": ".../projects/.../instanceTemplates/INSTANCE_TEMPLATE"
          }
        },
        {
          ...
        }
      ]
    }
    

To see which VMs have the latest configuration applied, compare the `revision` timestamp on each VM with the `currentRevision` timestamp on the MIG.

## List properties in an all-instances configuration

An all-instances configuration is part of the [MIG's configuration](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#configuration_components_for_vms_in_a_mig). To review the all-instances configuration, use one of the following ways.

**Note:** When reviewing your group's all-instances configuration, remember to make sure that you've also applied the configuration to existing VMs.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the MIG of which you want to view the all-instances configuration.

  3. Go to the **Details** tab.

  4. See the **All instances configuration** section.




###  gcloud 

Use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) and include the `--format` flag to show the group's all-instances configuration value.
    
    
    gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME \
        --format="(allInstancesConfig)"

The command returns the group's all-instances configuration, if it exists.

###  REST 

Make a `GET` request on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get) MIG and look for the `allInstancesConfig` field.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    

If the `allInstancesConfig` field is not set, then the group has no all-instances configuration.

## Delete properties from all-instances configuration

If you delete a property from the MIG's all-instances configuration, and the same property exists in the MIG's instance template, then VMs in the MIG will re-inherit that property from the instance template once the latest configuration is applied to VMs in the MIG. For more information about applying the latest configuration to existing VMs, see Apply an all-instances configuration to existing VMs.

To delete properties from an all-instances configuration, use one of the following ways.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the MIG from which you want to delete the all-instances configuration.

  3. Click **Edit**.

  4. Click **Instance template & overrides** to expand the section.

  5. In the **All-instances configuration** section, do the following:

     1. Depending on the property that you want to delete, click **Manage metadata** or **Manage labels**.
     2. In the **Manage metadata** or the **Manage labels** pane, hold the pointer over a setting to activate the delete option, and then click delete **Delete item**.
     3. Click **Save**.
  6. Click **Save** to apply the changes to the MIG.

If the MIG's update type is set to **Automatic** , then the changes in all-instances configuration is immediately applied to all existing VMs. If the update type is **Selective** , then you must selectively apply the configuration to existing VMs. For more information, see Apply an all-instances configuration to existing VMs.




###  gcloud 

To delete properties, use the [`all-instances-configuration delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/all-instances-config/delete) and specify one or more keys for the properties that you want to delete.
    
    
    gcloud compute instance-groups managed all-instances-config delete INSTANCE_GROUP_NAME \
        --metadata=KEY1[, KEY1]\
        --labels=KEY1[, KEY1]

Remember to apply your updated configuration to existing VMs in the MIG.

###  REST 

To delete properties, make a `PATCH` request on a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) MIG and specify a `null` value as the key for each property that you want to remove.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME
    {
      "allInstancesConfig": {
        "properties": {
          "metadata": {
            "KEY1": null,
            ...
          },
          "labels": {
            "KEY2": null,
            ...
          }
        }
      }
    }

**Pro Tip:** You can create, update, and delete multiple `allInstancesConfig` properties in a single API request.

Remember to apply your updated configuration to existing VMs in the MIG.

## What's next

  * Learn more about [automatically applying](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups) an updated configuration to existing VMs in a MIG.
  * Learn more about [selectively applying](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig) configuration updates to existing VMs in a MIG.
  * [View information](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about your MIG and its VMs.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
