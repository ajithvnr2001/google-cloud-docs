---
url: https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs/
title: Applying, viewing, and removing stateful configuration in MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:47:32.724486+00:00
---

# Applying, viewing, and removing stateful configuration in MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Applying, viewing, and removing stateful configuration in MIGs Stay organized with collections  Save and categorize content based on your preferences. 

After you [create or update a stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs) for a [stateful managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs), you can:

  * Apply the stateful configuration for it to take effect.
  * View the stateful configuration as well as the effective preserved state of your managed instances.
  * Remove the stateful configuration.



## Before you begin

  * Review [when to use stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) and [how stateful MIGs work](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work).
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




## Applying stateful configuration to managed instances

Your stateful configuration is effective after you or the MIG applies it.

  * Configuration changes in a stateful policy are automatically applied to all managed instances.
  * Configuration changes in a per-instance configuration can be applied manually or automatically.



For more conceptual information, read [How stateful configuration is applied to managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_stateful_configuration_is_applied_to_managed_instances).

### Applying configuration from a stateful policy

All configuration changes in a stateful policy are automatically applied to all managed instances. Updates to a stateful policy do not disrupt running virtual machine (VM) instances.

### Verifying whether a stateful policy has been applied

#### Verifying all VMs

Verify whether changes to a stateful policy have been applied to all VMs by checking if the MIG [has become stable](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group) after the changes.

#### Verifying specific VMs

Verify if the changes to a stateful policy have been applied to a specific VM in a MIG by viewing the preserved state of the managed instance and checking if all disks from the stateful policy are present in either `preservedStateFromPolicy` or `preservedStateFromConfig` for the managed instance.

### Applying stateful configuration from per-instance configurations

You can apply new or updated per-instance configurations either manually or automatically. Use one of the following approaches:

  * **Selectively apply updated configurations to specific instances** : Use this approach to control the disruption, the timing, and the sequence of the updates.
  * **Automatically apply updated configurations with rolling updates** : Use this approach to apply configuration changes to managed instances in an automated, rolling fashion.



Both of these methods apply outstanding updates from both per-instance configurations and unapplied [versions](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#relationship_between_versions_and_instancetemplate_fields) or instance template, if relevant.

#### Selectively apply updated configuration to specific instances

To manually apply per-instance configurations to specific instances, use the following steps:

  1. Configure an [opportunistic update policy](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#setting_up_an_opportunistic_or_proactive_update) to prevent a race with automatic proactive updates.
  2. Create or update per-instance configurations.
  3. Apply updated configurations to specific VMs by [selectively updating](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig#updating_selected_instances) those VMs.



Alternatively, you can use the following approaches:

  * When creating or updating a per-instance configuration with the gcloud CLI, use the `--update-instance` flag to immediately apply the configuration to the associated managed instance.
  * When you [manually create new instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs), specify their names and per-instance configurations at creation time. The MIG applies configurations immediately on VM creation.



#### Automatically apply updated configuration with rolling updates

Configure [proactive rolling updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#setting_up_an_opportunistic_or_proactive_update) for your MIG to automatically apply configuration updates to corresponding managed instances in a rolling fashion.

Stateful MIGs require the following configuration for a proactive update policy:

  * You must set the [replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method) to `RECREATE`.
  * You must set [max surge](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_surge) to `0`.
  * For regional MIGs, you must [disable proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) across zones.



This configuration ensures that the MIG recreates existing stateful instances and does not substitute them with different ones.

You can also ensure that changes in per-instance configurations are applied without stopping instances, if possible, by setting the [minimal action](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#controlling_the_disruption_level_during_a_rolling_update) to `REFRESH` in the group's update policy.

### Verifying whether per-instance configurations have been applied

#### Verifying all per-instance configurations

To verify whether all per-instance configurations in a MIG have been applied, view the MIG's stateful status and check `status.stateful.perInstanceConfigs.allEffective`:

  * `true`: All per-instance configurations in the group have been applied and are effective, or the group has no per-instance configurations.
  * `false`: The group has at least one per-instance configuration that is not yet effective: either you have not yet applied it or it is in the process of being applied.



#### Verifying a specific per-instance configuration

To verify if the changes to a specific per-instance configuration have been applied to its corresponding VM, view all per-instance configurations and check the specific per-instance configuration's `status` field:

  * `UNAPPLIED`: The per-instance configuration was created or updated and you need to apply it to the VM with a manual instance update.
  * `APPLYING`: The MIG is currently applying the new or updated per-instance configuration to the VM.
  * `EFFECTIVE`: The per-instance configuration has been applied successfully to the VM and is effective.
  * `UNAPPLIED_DELETION`: The per-instance configuration is set to be deleted. You must apply this update to the VM with a manual instance update for it to take effect.
  * `DELETING`: The per-instance configuration is being deleted and the change is being applied to the VM.



## Viewing stateful configuration and preserved state

Get information about your stateful MIGs for the following tasks:

  * Verifying whether a MIG has [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration) and whether this configuration is applied and effective.
  * Viewing stateful configuration that is common to all instances in the MIG, stored in the stateful policy.
  * Viewing stateful configuration that is specific to individual instances, stored in per-instance configurations, and checking whether this configuration is applied and effective.
  * Viewing the effective [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) for each instance in a MIG based on its stateful policy and applied per-instance configurations.



### Viewing the status of a MIG's stateful configuration

A MIG is considered stateful if it has any [stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration), that is, either a stateful policy or at least one non-empty per-instance configuration.

If you create a stateful policy, the MIG automatically applies it to make it effective. If you create per-instance configurations, you might [decide](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_per-instance_configuration_updates_are_applied_to_instances) to apply them later.

To verify whether a MIG has stateful configuration and that all per-instance configurations are applied, view the MIG's stateful status by using the gcloud CLI or REST.

###  gcloud 

To verify whether a MIG has stateful configuration, view its stateful status by running the [`gcloud compute instance-groups managed describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) command. For example:
    
    
    gcloud compute instance-groups managed describe NAME
    
    baseInstanceName node
    ...
    name example-group
    ...
    status:
      isStable: true
      **stateful:
        hasStatefulConfig: true
        perInstanceConfigs:
          allEffective: true**
      versionTarget:
        isReached: true
    targetSize: 3
    ...
    

In this output:

  * `hasStatefulConfig`: 
    * `true`: The group has stateful configuration, that is, the group has a non-empty stateful policy or at least one non-empty per-instance configuration.
    * `false`: No stateful configuration exists.
  * `perInstanceConfigs.allEffective`: 
    * `true`: All per-instance configurations in the group have been applied and are effective, or the group has no per-instance configurations.
    * `false`: The group has at least one per-instance configuration that is not yet effective: either you have not yet applied it or it is in the process of being applied.



###  REST 

To verify whether a MIG has stateful configuration, use the [`instanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) or [`regionInstanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get) method and check the `status.stateful` field. For example:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME
    

The method returns the `instanceGroupManagers` object:
    
    
    {
      "name": "example-group",
      "baseInstanceName": "node",
      ...
      "status": {
        "isStable": true,
        **"stateful": {
          "hasStatefulConfig": true,
          "perInstanceConfigs": {
            "allEffective": true
          }
        }** ,
        "versionTarget": {
          "isReached": true
        }
      },
      "targetSize": 3,
      ...
    }
    

In this output:

  * `hasStatefulConfig`: 
    * `true`: The group has stateful configuration, that is, the group has a non-empty stateful policy or at least one non-empty per-instance configuration.
    * `false`: No stateful configuration exists.
  * `perInstanceConfigs.allEffective`: 
    * `true`: All per-instance configurations in the group have been applied and are effective, or the group has no per-instance configurations.
    * `false`: The group has at least one per-instance configuration that is not yet effective: either you have not yet applied it or it is in the process of being applied.



### Viewing a MIG's stateful policy

View a MIG's [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration) by checking the group's details with the Google Cloud console, gcloud CLI or REST.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group of which you want to view the stateful policy.

  3. Go to the **Details** tab.

  4. Under **Stateful resources** , all the resources in the stateful policy are listed.




###  gcloud 

To view a MIG's stateful policy, run the [`gcloud compute instance-groups managed describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) command. For example:
    
    
    gcloud compute instance-groups managed describe NAME
    
    baseInstanceName node
    ...
    name example-group
    ...
    **statefulPolicy:
      preservedState:
        disks:
          data-disk:
            autoDelete: NEVER
          logs-disk:
            autoDelete: ON_PERMANENT_INSTANCE_DELETION
        internalIPs:
          nic0:
            autoDelete: ON_PERMANENT_INSTANCE_DELETION
        externalIPs:
          nic0:
            autoDelete: NEVER**
    status:
      isStable: true
      stateful:
        hasStatefulConfig: true
        perInstanceConfigs:
          allEffective: true
      versionTarget:
        isReached: true
    targetSize: 3
    ...
    

###  REST 

To view a MIG's [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_configuration) use the [`instanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) or [`regionInstanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get) method and check the `statefulPolicy` field. For example:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME
    

The method returns the `instanceGroupManagers` object:
    
    
    {
      "name": "example-group",
      "baseInstanceName": "node",
      ...
      "status": {
          "isStable": true,
          "versionTarget": {
            "isReached": true
          },
          "stateful": {
            "hasStatefulConfig": true,
            "perInstanceConfigs": {
              "allEffective": true
            }
          }
      ...
      **"statefulPolicy": {
        "preservedState": {
          "disks": {
            "data-disk": { "autoDelete": "NEVER" },
            "logs-disk": { "autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
          },
          "internalIPs": {
             "nic0" : { "autoDelete": "ON_PERMANENT_INSTANCE_DELETION"}
          },
          "externalIPs": {
             "nic0" : { "autoDelete": "NEVER"}
          },
        }
      }** ,
      "targetSize": 3,
      ...
    }
    

### Viewing a MIG's per-instance configurations

View per-instance configurations by listing all per-instance configurations in a MIG. Use the gcloud CLI or REST.

If you [decide](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_per-instance_configuration_updates_are_applied_to_instances) to apply per-instance configurations manually, some per-instance configurations might not yet be applied to the associated instances and, therefore, the instances' preserved states might not yet reflect your per-instance configurations. For more information, see Applying per-instance configurations and Verifying whether per-instance configurations have been applied

###  gcloud 

List all per-instance configurations in a MIG by running the [`gcloud compute instance-groups managed instance-configs list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/list) command.
    
    
    gcloud compute instance-groups managed instance-configs list NAME
    

Replace the following:

  * `NAME`: the name of a MIG to list per-instance configurations from



Filter the list using the standard `--filter` [flag](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

For example, to list all per-instance configurations in `example-group`:
    
    
    gcloud compute instance-groups managed instance-configs list example-group
    ---
    **fingerprint: JxPvsKOywuY=
    name: node-1
    preservedState:
      disks:
        data-disk:
          autoDelete: NEVER
          mode: rw
          source: https://www.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/disks/data-disk-1
      metadata:
        role: primary
      internalIPs:
        nic0:
          ipAddress:
            address: /projects/example-project/regions/us-east1/addresses/node-1-int-ip
          autoDelete: ON_PERMANENT_INSTANCE_DELETION
      externalIPs:
        nic0:
          ipAddress:
            literal: 130.211.181.55
          autoDelete: NEVER
    status: EFFECTIVE**
    ---
    fingerprint: IbGmJBqqEkk=
    name: node-2
    preservedState:
    ...
    

###  REST 

List all per-instance configurations in a MIG by calling the [`instanceGroupManagers.listPerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listPerInstanceConfigs) or [`regionInstanceGroupManagers.listPerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listPerInstanceConfigs) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME/listPerInstanceConfigs
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG) 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG
  * `NAME`: the name of a MIG to list per-instance configurations from



For example, to list all per-instance configurations in `example-group`:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-group/listPerInstanceConfigs
    

The method returns the list of per-instance configurations in the group: 
    
    
    {
      "items": [
        {
          **"fingerprint": "JxPvsKOywuY=",
          "name": "node-1",
          "preservedState" : {
            "disks": {
              "data-disk" : {
                "source": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/disks/data-disk-1",
                "mode": "READ_WRITE",
                "autoDelete": "NEVER"
              }
            },
            "metadata": {
              "role": "primary"
            },
            "internalIPs": {
             "nic0" : {
               "ipAddress" : {
                 "address":  "/projects/example-project/regions/us-east1/addresses/node-1-int-ip"
               },
               "autoDelete": "ON_PERMANENT_INSTANCE_DELETION"
             }
            },
            "externalIPs": {
             "nic0": {
               "ipAddress" : {
                 "literal": "54.2.3.4"
               },
               "autoDelete": "NEVER"
             }
            }
          },
          "status": "EFFECTIVE"**
        },
        {
          "fingerprint": "IbGmJBqqEkk=",
          "name": "node-2",
          "preservedState" : {
            ...
          }
          ...
        },
        ...
      ]
    }
    

### Viewing the preserved states of managed instances

When stateful configuration is applied, the MIG generates and sets the effective preserved state of each managed instance in two fields:

  * `preservedStateFromPolicy`: Contains the preserved state that is generated based on a stateful policy, excluding any stateful configuration that is overridden by per-instance configurations.
  * `preservedStateFromConfig`: Contains the preserved state that is generated based on a per-instance configuration that has already been applied to the managed instance.

**Note:** After setting the preserved state for a managed instance, the MIG automatically and asynchronously applies that intended state to the actual VM to make it effective. To verify whether preserved states are applied to the actual VMs, check the following flags:

  * To verify that the intended state from a stateful policy is effective, check whether the MIG [is stable](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group).
  * To verify that all intended states based on per-instance configurations are effective, see Verifying whether per-instance configurations have been applied.



To see the effective [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of each managed instance in a MIG, list the managed instances using the gcloud CLI or REST.

###  gcloud 

**Check which managed instances have preserved state** by using the [`gcloud compute instance-groups managed list-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances) and viewing values in the `PRESERVED_STATE` column. For example:
    
    
    gcloud compute instance-groups managed list-instances NAME
    
    NAME    ZONE        STATUS   HEALTH_STATE  ACTION  PRESERVED_STATE  INSTANCE_TEMPLATE  ...
    node-1  us-east1-c  RUNNING                NONE    POLICY,CONFIG    example-template
    node-2  us-east1-c  RUNNING                NONE    POLICY,CONFIG    example-template
    

The `PRESERVED_STATE` column can contain the following values:

  * `POLICY`: The managed instance has preserved state based on a stateful policy.
  * `CONFIG`: The managed instance has preserved state based on a per-instance configuration.
  * No value: The manage instance has no preserved state and is stateless.



**View the preserved state of a specific managed instance** by running the [`gcloud compute instance-groups managed describe-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe-instance).
    
    
    gcloud compute instance-groups managed describe-instance INSTANCE_GROUP_NAME \
      --instance INSTANCE_NAME
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of a MIG
  * `INSTANCE_NAME`: the name of a managed instance in the group



For example, to view the preserved state of the `node-1` managed instance in `example-group`, run:
    
    
    gcloud compute instance-groups managed describe-instance example-group \
      --instance node-1
    instance: .../example-project/zones/us-east1-c/instances/node-1
    instanceStatus: RUNNING
    currentAction: NONE
    id: 123456789012345678
    version:
      instanceTemplate: .../example-project/global/instanceTemplates/example-template
    preservedStateFromPolicy:
      disks:
        data-disk:
          autoDelete: NEVER
          mode: rw
          source: .../example-project/zones/us-east1-c/disks/data-disk-1
        internalIPs:
          nic0:
            ipAddress:
              literal: 10.0.0.1
              address: .../example-project/regions/us-east1/addresses/node-1-int-ip
            autoDelete: ON_PERMANENT_INSTANCE_DELETION
    preservedStateFromConfig:
      metadata:
        role: primary
        my-key: my-value
      externalIPs:
        nic0:
          ipAddress:
            literal: 130.211.181.55
            address: .../example-project/regions/us-east1/addresses/node-1-nat-ip
          autoDelete: NEVER
    

###  REST 

List managed instances to view each instance's preserved state by calling the [`instanceGroupManagers.listManagedInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) or [`regionInstanceGroupManagers.listManagedInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listManagedInstances) method.

For example, to list all managed instances:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME/listManagedInstances
    

The method returns the list of managed instances in the group, which contains information about their preserved states:
    
    
    {
      "managedInstances": [
        {
          "instance": ".../example-project/zones/us-east1-c/instances/node-1",
          "instanceStatus": "RUNNING",
          "currentAction": "NONE",
          "id": "123456789012345678",
          "version": {
             "instanceTemplate":".../example-project/global/instanceTemplates/example-template"
          },
          "preservedStateFromPolicy": {
            "disks": {
              "data-disk" : {
                "source": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/disks/data-disk-1",
                "mode": "rw",
                "autoDelete": "NEVER"
              },
            },
            "internalIPs": {
              "nic0" : {
                "ipAddress": {
                  "literal": "10.0.0.1",
                  "address":  "/projects/example-project/regions/us-east1/addresses/node-1-int-ip"
                },
                "autoDelete": "ON_PERMANENT_INSTANCE_DELETION"
              }
            },
          },
          "preservedStateFromConfig": {
            "metadata": {
              "role": "primary",
              "my-key": "my-value"
            },
            "externalIPs": {
              "nic0": {
                "ipAddress": {
                  "literal": "130.211.181.55",
                  "address":  "/projects/example-project/regions/us-east1/addresses/node-1-nat-ip"
                },
                "autoDelete": "NEVER"
              }
            },
          }
        },
        {
          "instance": ".../example-project/zones/us-east1-c/instances/node-2",
          "instanceStatus": "RUNNING",
          ...
          "preservedStateFromPolicy": {
            ...
          },
          "preservedStateFromConfig": {
            ...
          }
        },
        ...
      ]
    }
    

## Viewing associated static IP address resources

To retrieve static IP addresses ([`Address`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses) resources) that are assigned to managed instances in a MIG, view the preserved states of these instances. You can see static addresses in the `ipAddress.address` fields.

If a MIG or the instances no longer exist, but the IP address reservations still exist, you can list the static [internal](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address#list_static_internal_ip_addresses) or [external](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address#list_ip) address reservations.

**Caution:** Do not use automation to filter and delete unassigned static IP addresses that remain after a MIG or its instances have been deleted. Static IP address reservations unrelated to the group might match your filter.

## Removing stateful configuration

Removing stateful configuration is useful in the following scenarios:

  * You have [migrated](https://docs.cloud.google.com/compute/docs/tutorials/migrate-workload-to-stateful-mig) standalone VMs to a stateful MIG and now want to move the stateful configuration from per-instance configurations to a common stateful policy.
  * You have rearchitected your workload and no longer need to keep any state on the VM instances.
  * You created a stateful configuration for testing purposes and now want to clean it up.



This section describes how to fully remove a stateful policy on a per-instance configuration. If you only need to remove a subset of a stateful policy or per-instance configuration, see the following sections:

  * [Declaring previously stateful persistent disks as stateless](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#declaring_previously_stateful_persistent_disks_as_stateless) for all VMs in a MIG.
  * [Declaring previously stateful network interfaces as stateless](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs#declaring_previously_stateful_ip_addresses_as_stateless) for all VMS in a MIG.
  * [Detaching a stateful disk or declaring it stateless](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs#detaching_a_stateful_disk_or_declaring_it_stateless_for_an_individual_vm) for a specific VM in a MIG.
  * [Removing stateful metadata](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs#setting_modifying_and_removing_stateful_metadata_individually_for_existing_vm_instances) from a specific VM in a MIG
  * [Disassociating a static IP address](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs#disassociate_static_ip_address_from_existing_vm_in_a_mig) from a specific VM in a MIG.



### Removing a stateful policy

When you remove a stateful policy, you affect all VMs in a MIG. The MIG treats all stateful resources that were configured in the stateful policy as stateless, unless those resources are also configured in per-instance configurations for individual instances. On subsequent instance recreation, autohealing, or update operations, the now-stateless resources can lose their state:

  * Disks can be deleted and recreated from the source, which is defined in the instance template.
  * IP addresses might change.



For conceptual information, see [how removing a resource from stateful policy affects preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#removing_resource_from_stateful_policy).

###  gcloud 

To delete all configuration from a stateful policy, run the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) with the applicable flags. The applicable flags are as follows:

  * `--remove-stateful-disks`, and list the device names of all configured stateful disks.
  * `--remove-stateful-internal-ips`, and list the network interface names of all configured stateful internal IP addresses.
  * `--remove-stateful-external-ips`, and list the network interface names of all configured stateful external IP addresses.



For example, if your stateful policy contains configuration for two stateful disks with device names `data-disk` and `logs-disk`, and contains configuration for stateful internal and external IP addresses within the `nic0` network interface, run the following command to clear the policy:
    
    
    gcloud compute instance-groups managed update example-group \
        --zone us-east1-c \
        --remove-stateful-disks data-disk,logs-disk \
        --remove-stateful-internal-ips nic0 \
        --remove-stateful-external-ips nic0
    

The MIG removes from its stateful policy the `data-disk` and `logs-disk` stateful configuration, as well as the stateful internal and external IP configuration for the `nic0` network interface. As a result, the MIG removes those disks and static IP addresses from the preserved states of all managed instances in the group automatically and asynchronously, unless the disks or IP addresses are also configured in per-instance configurations.

###  REST 

To delete all configuration in stateful policy, set the `statefulPolicy` field to `null` by using the [`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch). method.

For example, the following call removes stateful policy configuration:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME
    
    {
      "statefulPolicy": null
    }
    

The MIG clears stateful policy configuration and removes the stateful resources from the preserved states of all managed instances in the group automatically and asynchronously, unless the resources are also configured in per-instance configurations.

### Removing stateful configuration for a specific VM

Removing stateful configuration for a specific VM is done in two steps:

  1. Delete the associated per-instance configuration.
  2. Apply the change to the managed instance. You can choose whether the change should be applied manually or automatically.



After the change is applied, all stateful items that were previously configured in the per-instance configuration are now treated as stateless, unless they are also configured in the group's stateful policy. When the VM is subsequently recreated or updated, the state of the items is lost:

  * Disks can be detached or recreated from their source in the instance template.
  * Metadata is removed or reset to the values defined in the instance template.
  * IP addresses might change.



For more information, see [how removing items from per-instance configurations affects preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#removing_items_from_pic).

###  gcloud 

To fully delete the per-instance configuration, run the [`gcloud compute instance-groups managed instance-configs delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/delete).

Use the optional `--update-instance` flag to apply the changes immediately to the instance (the default). If you set the `--no-update-instance` flag, the changes are applied when you next recreate or update the instance.

The `--instance-update-minimal-action` flag can only be used together with the `--update-instance` flag.
    
    
    gcloud compute instance-groups managed instance-configs delete INSTANCE_GROUP_NAME \
      --instances INSTANCE_NAME[,INSTANCE_NAME,...] \
      [--no-update-instance | --update-instance] \
      [--instance-update-minimal-action MINIMAL_ACTION]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: The name of the MIG.
  * `INSTANCE_NAME`: Names of the instances for which to delete per-instance configurations
  * `MINIMAL_ACTION`: The minimal action to perform when applying the per-instance configuration update to the VM. This value must be one of the following: 
    * `none`: No action.
    * `refresh`: Apply updates that are possible to apply without stopping the VM.
    * `restart`: Stop the VM and then start it again.
    * `replace`: Recreate the VM.



For example, to delete the per-instance configuration for `node-1` in `example-group`, run the following command:
    
    
    gcloud compute instance-groups managed instance-configs delete example-group \
      --instances node-1 \
      --update-instance
    

The MIG deletes the per-instance configuration for `node-1` and, because the VM was updated and configuration changes applied, the MIG no longer treats those previously stateful items as stateful.

###  REST 

To fully delete the per-instance configuration for one or multiple instances, use the [`instanceGroupManagers.deletePerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/deletePerInstanceConfigs) or [`regionInstanceGroupManagers.deletePerInstanceConfigs`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/deletePerInstanceConfigs) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME/deletePerInstanceConfigs
    
    {
      "names": ["INSTANCE_NAME",...]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the request
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG) 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG
  * `INSTANCE_GROUP_NAME`: the name of the MIG
  * `INSTANCE_NAME`: names of the instances for which to delete per-instance configurations



The `deletePerInstanceConfig` method deletes the specified per-instance configurations but does not apply the changes to the associated VMs. The changes are applied to a VM when you recreate or update the instance. [Update selected VMs manually](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig) to apply the changes.

For example, to delete per-instance configuration for `node-1` in `example-group`, call the following method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-group/deletePerInstanceConfigs
    
    {
      "names": ["node-1"]
    }
    

The method deletes per-instance configuration for the `node-1` instance from `example-group`. The change will be applied to the managed instance when you recreate or update the instance.

To apply the configuration change, call the [`instanceGroupManagers.applyUpdatesToInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/applyUpdatesToInstances):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-group/applyUpdatesToInstances
    
    {
      "instances": ["/zones/us-east1-c/instances/node-1"]
    }
    

The method removes stateful items from the managed instance's preserved state.

## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. Please share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * [Configure a stateful MIG](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-migs).
  * [Get info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about a specific MIG and its managed instances, including VM status and properties.
  * Learn more about [stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).
  * Learn more about [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) and [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
