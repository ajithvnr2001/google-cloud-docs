---
url: https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs/
title: Configuring stateful persistent disks in MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:06.018888+00:00
---

# Configuring stateful persistent disks in MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configuring stateful persistent disks in MIGs Stay organized with collections  Save and categorize content based on your preferences. 

Configuring persistent disks to be [stateful](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) lets you benefit from VM instance autohealing and automated updates while preserving the state of the disks.

You can configure any disk defined in the instance template to be stateful for all instances in a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) by adding that disk's device name to the MIG's [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_policy).

You can also configure stateful persistent disks individually for instances in a MIG by setting [per-instance configurations](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs); these disks don't need to be defined in the instance template.

## Before you begin

  * Review [when to use stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) and [how stateful MIGs work.](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work)
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

  * A stateful regional MIG does not automatically orchestrate cross-zone failover. When using a regional MIG, you can make your stateful application resilient to zonal failure by deploying redundant replicas to multiple zones and relying on your application's data replication functionality.




## When to use stateful persistent disks

Use stateful persistent disks to take advantage of VM [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) and [automated updates](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs) while still preserving the data on the disks. For more information, see [use cases](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#when_to_use_stateful_migs) for stateful MIGs.

When you configure stateful disks, these disks are preserved through VM instance autohealing, updates, and recreation. But that also means that stateful disks cannot be recreated from the original image or updated to a new image.

As a best practice, we recommend keeping your boot disks stateless.

Keeping the boot disk stateless has the following benefits:

  * You can repair a boot disk that was corrupted by recreating it from its original image. Autohealing does such repairs automatically.
  * You can update a boot disk to the latest image with new versions and security patches.



For more information, see how [autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state#autohealing) and [updating](https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state#updating) handle preserved state.

## Configuring stateful persistent disks for all VMs in a MIG

Configure any disk defined in an instance template to be stateful by adding that disk's device name to the MIG's [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_policy). The MIG treats disks with that device name as stateful for all existing and future VM instances.

**Note:** If an instance template attaches an existing disk in read-only mode, you don't need to configure it as stateful. The MIG already preserves this disk. It attaches the disk to all its VMs in read-only mode and detaches the disk when a VM is deleted.

### Configuring stateful disks on MIG creation

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the[`instanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) method (for zonal MIGs)
  * All permissions required to call the[`regionInstanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert) method (for regional MIGs)



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select your project and click **Continue**.

  3. Click **Create instance group**.

  4. Select **New managed instance group (stateful)**.

  5. Specify a **Name** for the instance group.

  6. Select an **Instance template**. If no templates are available, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

  7. In the **Number of instances** field, specify the number of instances for the instance group.

  8. The **Stateful configuration** section displays the disks specified in the instance template. Click a disk to edit its stateful configuration.

     1. Under **Stateful** , select **Yes**.
     2. From the **On permanent instance deletion** drop-down, select the action to perform on the stateful disk when the VM instance is deleted. The available options are:

        * Detach disk: (Default.) Never delete the disk; detach the disk when the VM is deleted.
        * Delete disk: Delete the stateful disk when its VM is permanently deleted from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.
**Note:** Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.
     3. After you finish the stateful configuration, click **Done**.

  9. Click **Create**.




###  gcloud 

To specify which disks from an instance template should be stateful on MIG creation, use the `--stateful-disk` flag with the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --template INSTANCE_TEMPLATE \
        --size SIZE \
        --stateful-disk device-name=DEVICE_NAME[,auto-delete=DELETE_RULE]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: The name of the managed instance group to create.
  * `INSTANCE_TEMPLATE`: The name of the instance template to use when creating instances.
  * `SIZE`: The initial number of VMs you need in this group.
  * `DEVICE_NAME`: The device name of a disk specified in the instance template.
  * `DELETE_RULE`: A value that prescribes what should happen to a stateful disk when a VM is deleted. Available options are:

    * `never`: (Default.) Never delete the disk; instead, detach the disk when its VM is deleted.
    * `on-permanent-instance-deletion`: Delete the disk when its VM instance is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.

Regardless of the value of the delete rule, stateful disks are always preserved on VM autohealing, update, and recreation operations.


**Note:** You can see the device names of disks that are defined in an instance template by running the `gcloud compute instance-templates describe` [command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe).

**Example**

You want to deploy a database with 12 shards, each with a stateless boot disk that contains the operating system and database binaries, and each with a stateful data disk. Use the following steps:

  1. Create an instance template with a stateless boot disk based on the image `img-example-db-v01`, which has a pre-installed OS and database, and with a stateful data disk:
         
         gcloud compute instance-templates create example-database-template-v01 \
             --image img-example-db-v01 \
             --create-disk device-name=data-disk,mode=rw,image=empty10GBext4
         

The `--create-disk` flag instructs the MIG to:

     1. Create a new 10 GB disk for each VM instance from an empty ext4 image, prepared beforehand.
     2. Attach the disk to its VM in read/write mode using device name `data-disk`.
  2. Create a MIG from the instance template and define the data disk as stateful:
         
         gcloud compute instance-groups managed create example-database-group \
           --template example-database-template-v01 \
           --base-instance-name shard \
           --size 12 \
           --stateful-disk device-name=data-disk,auto-delete=on-permanent-instance-deletion
         

The device name `data-disk` is taken from the instance template. The data disk is configured to be deleted together with the VM instance when the VM is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) (either due to manual instance deletion or due to manual decrease of the group size). The data disk is preserved on autohealing, updates, and VM recreation.

  3. Verify that the data disk is configured in the stateful policy:
         
         gcloud compute instance-groups managed describe example-database-group
         
         
         baseInstanceName: shard
         ...
         name: example-database-group
         ...
         statefulPolicy:
           preservedState:
             disks:
               data-disk:
                 autoDelete: ON_PERMANENT_INSTANCE_DELETION
         ...
         

You can see that the stateful policy declares disks with device name `data-disk` as stateful, with a rule to delete such disks on permanent VM deletion.




###  Terraform 

If you haven't already created an instance template, which specifies the machine type, boot disk image, network, and other VM properties that you want for each VM in your MIG, [create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#create_a_new_instance_template).

The following sample creates a zonal MIG with a stateful disk. To specify which disk from the instance template should be stateful on MIG creation, include the `stateful_disk` block. For more information about the resource used in the sample, see [`google_compute_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager). To create a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
      name               = "example-database-group"
      base_instance_name = "shard"
      target_size        = 12
      zone               = "us-central1-f"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
      stateful_disk {
        device_name = "data-disk"
        delete_rule = "ON_PERMANENT_INSTANCE_DELETION"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To specify which disks from the instance template should be stateful on MIG creation, include them in the `statefulPolicy` field in the request body of the `instanceGroupManagers.insert` [method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instanceGroupManagers
    
    {
      "name": "NAME",
      "versions": [
        {
          "instanceTemplate": "global/instanceTemplates/TEMPLATE"
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
  * `TEMPLATE`: The name of the instance template to use when creating instances.
  * `SIZE`: The initial number of instances you need in this group.
  * `DEVICE_NAME`: The device name of a disk specified in the instance template.
  * `DELETE_RULE`: A value that prescribes what should happen to the stateful disk when the VM instance is deleted. The available options are:

    * `never`: (Default.) Never delete the disk; detach the disk when the VM is deleted.
    * `on_permanent_instance_deletion`: Delete the stateful disk when its VM is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.
**Note:** Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.

**Note:** You can see the device names of disks that are defined in an instance template by calling the [ `instanceTemplates.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/get) and reading the `instanceTemplates.disks[].deviceName` field in the response.

**Example**

You want to deploy a database with 12 shards, each with a stateless boot disk that contains the operating system and database binaries, and each with a stateful data disk. Use the following steps.

  1. Create an instance template with a stateless boot disk based on the image `img-example-db-v01`, with pre-installed OS and database, and with a stateful data disk, using the [`instanceTemplates.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/insert) method:
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates
         
         {
           "name": "example-database-template-v01",
           "properties": {
             "machineType":"e2-standard-2",
             "disks": [
               {
                 "boot": true,
                 "deviceName": "boot-disk",
                 "initializeParams": {
                   "sourceImage": "projects/example-project/global/images/mg-example-db-v01"
                 }
               },
               {
                 "deviceName": "data-disk",
                 "mode": "READ_WRITE",
                 "initializeParams": {
                   "sourceImage": "projects/example-project/global/images/empty10GBext4"
                 }
               }
             ],
             "networkInterfaces": [
               {
                 "network": "global/networks/default"
               }
             ]
           }
         }
         

The data disk in the instance template has device name `data-disk` and is configured to be created from an empty ext4 image, prepared beforehand, and to be attached in read/write mode.

  2. Create a MIG from the instance template and define the data disk as stateful by using the [`instanceGroupManagers.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) method:
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers
         
         {
           "name": "example-database-group",
           "baseInstanceName": "shard",
           "versions": [
             {
               "instanceTemplate": "global/instanceTemplates/example-database-template-v01"
             }
           ],
           "targetSize": 12,
           "statefulPolicy": {
             "preservedState": {
               "disks": {
                 "data-disk": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
               }
             }
           }
         }
         

The MIG creates 12 instances, each with a disk with the following properties:

     * A device name, `data-disk`, taken from the instance template.
     * A delete rule to delete the data disk when the VM is deleted (either due to manual instance deletion or due to manual decrease of the group size).
     * An entry in the preserved state from policy ([`preservedStateFromPolicy`](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_according_to_stateful_policy)) of each managed instance so that the data disk is preserved on autohealing, updates, and instance recreation.
  3. Use the [`instanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) method to verify that the data disk is configured in the stateful policy of the new `instanceGroupManagers` resource:
         
         GET https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-database-group
         
         
         {
           "name": "example-database-group",
           "baseInstanceName": "shard",
           ...
           "statefulPolicy": {
             "preservedState": {
               "disks": {
                 "data-disk": {"autoDelete": "ON_PERMANENT_INSTANCE_DELETION" }
               }
             }
           }
           ...
         }
         

You can see that stateful policy declares disks with device name `data-disk` as stateful with the rule to delete such disks on permanent instance deletion.




### Setting and updating stateful configuration for disks in an existing MIG

If you run a stateful application on a stateless MIG (a MIG without any stateful configuration), you can configure existing disks that are defined in the instance template to be stateful for all instances in this MIG. This lets you preserve the disks on instance recreation, autohealing, and update operations, and optionally on deletion operations.

You can do the following operations:

  * Add disks that are defined in the instance template to the [stateful policy](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#stateful_policy) of an existing MIG to declare them as stateful. This marks disks with the given device name as stateful for all existing and future instances in the MIG.
  * Update the stateful policy to change the stateful configuration for disks.



The MIG applies the updated configuration in the stateful policy automatically and asynchronously to all instances. Updates to disk configurations in a stateful policy don't disrupt running VMs. For more information, see [applying stateful policy updates](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_stateful_configuration_is_applied_to_managed_instances).

For a regional MIG, you must [disable](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) proactive cross zone instance redistribution before you can configure stateful disks. For more information, see [how regional groups handle preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/preserved-state#regional_migs).

**Note:** If a MIG has a read-only disk attached to all of its VMs, you don't need to configure this disk as stateful. The MIG already preserves this disk. It attaches the disk to all its instances in read-only mode and detaches the disk when a VM is deleted.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the[`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) method (for zonal MIGs)
  * All permissions required to call the[`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) method (for regional MIGs)



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group in which you want to specify stateful configuration for disk.

  3. Click **Edit** to modify the managed instance group.

  4. Click **Stateful & per-instance configuration** to expand the section.

  5. In the **Group config** section, click the disk that you want to make stateful. In the expanded section, do the following:

     1. For **Stateful** , select **Yes**.
     2. In the **On permanent instance deletion** list, select the action to perform on the stateful disk when the VM instance is deleted.

        * **Detach disk** : (Default.) Never delete the disk; detach the disk when the VM is deleted.
        * **Delete disk** : Delete the stateful disk when its VM is permanently deleted from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.

**Note:** Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.
     3. After you update the stateful configuration, click **Done**.

  6. Click **Save** to complete the update.




###  gcloud 

To specify which disks from the instance template should be stateful or to update the stateful disk configuration for an existing MIG, use one or multiple `--stateful-disk` flags with the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update NAME \
      --stateful-disk device-name=DEVICE_NAME[,auto-delete=DELETE_RULE]
    

Replace the following:

  * `NAME`: The name of the managed instance group to update.
  * `DEVICE_NAME`: The device name of a disk that is specified in the instance template.
  * `DELETE_RULE`: A value that prescribes what should happen to the stateful disk when a VM instance is deleted. The available options are:

    * `never`: (Default.) Never delete the disk, detach the disk when its instance is deleted.
    * `on-permanent-instance-deletion`: Delete the stateful disk when its instance is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the managed instance is deleted manually or when the group size is decreased.
**Note:** Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.



If a specified device name is already configured in the stateful policy, the command updates the configuration.

**Note:** You can see the device names of disks that are defined in an instance template by running the [`gcloud compute instance-templates describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/describe).

**Example**

You run a database with multiple shards on a MIG named `example-database- group`. Each VM in the MIG stores a shard on an additional disk with device name `data-disk`, which is defined by the instance template. The MIG has no stateful configuration, and you want to preserve the data disks on instance recreation, autohealing, and updates. You also want to protect the data disks from deletion when a VM is deleted.

  1. Update the MIG to define the data disk as stateful by using the following command:
         
         gcloud compute instance-groups managed update example-database-group \
           --stateful-disk device-name=data-disk,auto-delete=never
         

As a result, the MIG applies the stateful policy configuration updates automatically and asynchronously to the data disks for all instances. The data disks are now preserved on autohealing, updates, and instance recreation, and the data disks are detached on instance deletion because the `auto-delete` rule is set to `never`.

  2. Verify that the data disk is configured in the stateful policy by running the [`gcloud compute instance-groups managed describe example-database-group` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).




###  REST 

To specify which disks from the instance template should be stateful or to update the stateful disk configuration for an existing MIG, configure the disks in the MIG's stateful policy using the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instanceGroupManagers/NAME
    
    {
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
  * `NAME`: The name of the MIG to update.
  * `DEVICE_NAME`: The device name of a disk, specified in the instance template, for which you would like to update stateful configuration.
  * `DELETE_RULE`: A value that prescribes what should happen to the stateful disk when a VM instance is deleted. The available options are:

    * `never`: (Default.) Never delete the disk, detach the disk when its instance is deleted.
    * `on-permanent-instance-deletion`: Delete the stateful disk when its instance is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the instance is deleted manually or when the group size is decreased.
**Note:** Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.



If the specified device name is already configured in the stateful policy, the `patch` method updates its configuration.

**Note:** You can see the device names of disks that are defined in an instance template by executing the [`instanceTemplates.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceTemplates/get) and reading the `instanceTemplates.disks[].deviceName` field in the response.

**Example**

You run a database with multiple shards on a MIG named `example-database- group`. Each VM in the MIG stores a shard on an additional disk with device name `data-disk`, which is defined by the instance template. The MIG has no stateful configuration, and you want to preserve the data disks on instance recreation, autohealing, and updates. You also want to protect the data disks from deletion when a VM is deleted.

  1. Patch the MIG to define the data disk as stateful:
         
         PATCH https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-database-group
         
         {
           "statefulPolicy": {
             "preservedState": {
               "disks": {
                 "data-disk": {"autoDelete": "NEVER" }
               }
             }
           }
         }
         

The MIG applies this stateful configuration automatically and asynchronously to the data disks for all instances. The data disks will be preserved on autohealing, updates, and instance recreation. The data disks will be detached on instance deletion because the `autoDelete` rule is set to `NEVER`.

  2. Verify that the data disk is configured in the stateful policy by viewing the `instanceGroupManagers` resource, returned by the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get).




### Declaring previously stateful persistent disks as stateless

You might need to configure a stateful disk to be treated as stateless. For example:

  * If you rearchitect your app to move the state off the disk.
  * If you configured the disk to be stateful by mistake and would like to revert it.



To declare all disks with a given device name as stateless, remove the disk's configuration from the stateful policy.

**Note:** If disk configuration for the same device name is present in a per-instance configuration, the disk remains stateful for the associated instance even if you remove its configuration from the stateful policy. In this case, you must also remove the disk's configuration from the per-instance configuration to make the disk stateless.

The MIG applies the change to the stateful policy automatically and asynchronously to all instances. Updates to disk configuration in a stateful policy don't disrupt running VM instances.

For more information, see [Applying stateful policy updates](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_stateful_configuration_is_applied_to_managed_instances).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * All permissions required to call the[`instanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) method (for zonal MIGs)
  * All permissions required to call the[`regionInstanceGroupManagers.patch`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch) method (for regional MIGs)



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group from which you want to remove stateful configuration for disks.

  3. Click **Edit** to modify the managed instance group.

  4. Click **Stateful & per-instance configuration** to expand the section.

  5. In the **Group config** section, click the stateful disks that you want to make stateless. In the expanded section, do the following:

     1. Change the **Stateful** option to **No**.
     2. Click **Done**.
  6. After you make the changes, click **Save**.




###  gcloud 

To specify which disks from a MIG's stateful policy to make stateless, use the `--remove-stateful-disks` flag with the [`gcloud compute instance-groups managed update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update NAME \
      --remove-stateful-disks DEVICE_NAME[,DEVICE_NAME,...]
    

Replace the following:

  * `NAME`: The name of the MIG to update.
  * `DEVICE_NAME`: The device name of a disk to remove from the stateful policy and to treat as stateless. You can provide one or multiple device names in the list.

**Note:** You can see the device names of disks that are configured in a MIG's stateful policy by running the [`gcloud compute instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe).

**Example**

You run a legacy application with multiple nodes on a MIG named `example-legacy-group`. Each VM in the MIG stores application data on a boot disk with device name `boot-disk`, which you configured as stateful in the MIG's stateful policy. You have moved application data to an additional disk and now want to make the boot disk stateless to make it easy to update to new images.

To remove the stateful configuration of the boot disk, update the managed instance group:
    
    
    gcloud compute instance-groups managed update example-legacy-group \
      --remove-stateful-disks boot-disk
    

The MIG removes the stateful configuration for the device name `boot-disk` automatically and asynchronously for the boot disks of all instances in the group. The boot disks remain attached to the instances but are no longer stateful. When you recreate or update the instances, or when instances are autohealed, the MIG recreates the boot disks from the image specified in the instance template.

###  REST 

To specify which disks from a MIG's stateful policy to make stateless, remove each disk's configuration from the MIG's stateful policy using the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT/zones/ZONE/instanceGroupManagers/NAME
    
    {
      "statefulPolicy": {
        "preservedState": {
          "disks": {
            "DEVICE_NAME": null,
            ...
          }
        }
      }
    }
    

Replace the following:

  * `PROJECT`: The project ID for the request.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG). 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `NAME`: The name of the MIG to update.
  * `DEVICE_NAME`: The device name of a disk that you want to remove from the stateful policy. Providing a `null` value leads to removal of the stateful configuration for that disk. You can provide one or multiple device names to remove.

**Note:** You can find out the device names of disks configured in a MIG's stateful policy from the output of the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get).

**Example**

You run a legacy application with multiple nodes on a MIG named `example-legacy-group`. Each VM in the MIG stores application data on a boot disk with device name `boot-disk`, which you configured as stateful in the MIG's stateful policy. You have moved application data to an additional disk and now want to make the boot disk stateless to make it easy to update to new images.

To remove the stateful configuration of the boot disk, patch the managed instance group:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-legacy-group
    
    {
      "statefulPolicy": {
        "preservedState": {
          "disks": {
            "boot-disk": null
          }
        }
      }
    }
    

The MIG removes the stateful configuration for the device name `boot-disk` automatically and asynchronously for the boot disks of all instances in the group. The boot disks remain attached to the instances but are no longer stateful. When you recreate or update the instances, or when instances are autohealed, the MIG recreates the boot disks from the image specified in the instance template.

### Removing stateful persistent disks from a MIG

You might need to completely remove a stateful disk from instances in a MIG, for example, if you re-architected your application and moved the state out of that disk.

MIGs don't allow removing stateful disks, so you must do the following steps:

  1. Remove the stateful configuration of the disk from the stateful policy. This makes disks with the given device name stateless.
  2. Detach the disks from the VMs if you still want to keep them.
  3. Roll out a new instance template that no longer defines the disk with the given device name.



## Configuring stateful persistent disks individually for a VM in a MIG

Configure stateful persistent disks for a specific VM in a MIG by adding the disk's device name to that VM's [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs). Update the VM to [apply the per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) and make it effective.

Configuring stateful persistent disks individually for specific VMs in a MIG is useful if you need to:

  * Migrate existing workloads (bring existing disks) from standalone VMs to stateful MIGs to benefit from autohealing and easy updates.
  * Restore backups of disks, configured individually for VMs.
  * Attach additional stateful disks to a specific VM temporarily for testing, debugging, or copying data.



**Pro Tip:** Where feasible, consider configuring stateful disks for all VMs in a MIG, instead of configuring stateful disks individually for each VM instance.

### Adding existing stateful disks to new VMs in a MIG

You can add existing stateful disks to new instances that you manually create in a MIG. This is useful for migrating a stateful application from existing standalone VMs to a stateful MIG, for example:

  1. [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) with common configuration for all VM instances.
  2. [Detach](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk) the data disks from the standalone instances and delete these instances. You can also [detach boot disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk) if they contain state that should be preserved.
  3. [Create](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group) an empty MIG using the instance template created earlier.
  4. [Create instances](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#creating_instances_with_specific_names_in_migs) in the MIG with the appropriate names and associated disks from the previous step. The MIG responds to your request with the following actions:

     1. Creates a VM from the instance template using the provided instance name. 
        * A regional MIG creates the VM in the same zone where the disk is located. If the disk is regional, the regional MIG creates the VM in any of the disk's replica zones.
     2. Creates a [per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs#per_instance_configs) with the provided stateful configuration for the disks.
     3. Attaches the disks to the new instance.



Add existing stateful disks when manually creating specific instances in a MIG using the gcloud CLI or REST. The MIG applies the configuration immediately on VM creation.

###  gcloud 

To create a VM with a custom name and attach one or more existing stateful disks to that VM, use the [`gcloud compute instance-groups managed create-instance`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance) command with one or multiple `--stateful-disk` flags.
    
    
    gcloud compute instance-groups managed create-instance NAME \
      --instance VM_NAME \
      [--zone ZONE | --region REGION] \
      --stateful-disk device-name=DEVICE_NAME,source=DISK[,mode=MODE][,auto-delete=DELETE_RULE]
    

Replace the following:

  * `NAME`: The name of the MIG in which you need to create an instance.
  * `VM_NAME`: The name of the new instance to create.
  * `ZONE`: The zone where the MIG is located (applies to a zonal MIG).
  * `REGION`: The region where the MIG is located (applies to a regional MIG).
  * `DEVICE_NAME`: The device name to use when attaching the disk.
  * `DISK`: The URI of an existing persistent disk to attach under the specified `DEVICE_NAME` in the format `projects/project-id/zones/zone/disks/disk-name` for a zonal disk and `projects/project-id/regions/region/disks/disk-name` for a regional disk.
  * `MODE`: Specifies the mode of the disk. Supported options are: 
    * `ro`: Read-only.
    * `rw`: (Default.) Read/write.
  * `DELETE_RULE`: A value that prescribes what should happen to a stateful disk when a VM instance is deleted. The available options are:

    * `never`: (Default.) Never delete the disk; instead, detach the disk when its instance is deleted.
    * `on-permanent-instance-deletion`: Delete the stateful disk when its instance is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the instance is deleted manually or when the group size is decreased.

Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.




**Example**

You want to have autohealing for a database server that is currently running on a standalone VM named `db-instance` and that currently stores data on a disk named `db-data-disk-1`.

Create a stateful MIG with autohealing, create a similar VM inside the MIG, and attach the existing data disk `db-data-disk-1` to the new instance as a stateful disk:

  1. Stop the VM, `db-instance`, during a maintenance window.
  2. [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) named `db-template` using the `db-instance` configuration.
  3. Detach `db-data-disk-1` from `db-instance` and delete `db-instance`.
  4. Create an empty MIG, `example-database-mig`, from `db-template`, and configure autohealing.
  5. Create a managed instance with the original `db-instance` name and attach the `db-data-disk-1` as a stateful disk:
         
         gcloud compute instance-groups managed create-instance example-database-mig \
           --instance db-instance \
           --zone us-east1-c \
           --stateful-disk device-name=data-disk,source=projects/example-project/zones/us-east1-c/disks/db-data-disk-1,auto-delete=never
         

The command creates an instance, `db-instance`, in the MIG, creates a corresponding per-instance configuration with `db-data-disk-1` stateful disk, and attaches the disk to the new VM, using `data-disk` as the device name.




###  REST 

To create one or multiple instances in a MIG, set custom VM names, and attach one or multiple existing stateful disks to these instances, use the [`instanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME/createInstances
    
    {
      "instances": [
        {
          "name": "VM_NAME",
          "preservedState" : {
            "disks": {
              "DEVICE_NAME" : {
                "source": "DISK",
                "mode": "MODE",
                "autoDelete": "DELETE_RULE"
              },
              ...
            }
          }
        },
        ...
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: Project ID for the request.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG). 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `NAME`: The name of the MIG in which to create an instance.
  * `VM_NAME`: The name of the instance to create.
  * `DEVICE_NAME`: The device name to use when attaching the disk.
  * `DISK`: The URI of an existing persistent disk to attach under the specified `DEVICE_NAME` in the format `projects/project-id/zones/zone/disks/disk-name` for a zonal disk or `projects/project-id/regions/region/disks/disk-name` for a regional disk.
  * `MODE`: Specifies the mode of the disk. Supported options are: 
    * `READ_ONLY`: Read-only.
    * `READ_WRITE`: (Default.) Read/write.
  * `DELETE_RULE`: A value that prescribes what should happen to a stateful disk when a VM is deleted. The available options are as follows:

    * `never`: (Default.) Never delete the disk; instead, detach the disk when its VM is deleted.
    * `on-permanent-instance-deletion`: Delete the stateful disk when its instance is permanently [deleted](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#delete_from_group) from the instance group, for example, when the instance is deleted manually or when the group size is decreased.

Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.




**Example**

You want to have autohealing for a database server that is currently running on a standalone VM named `db-instance` and that currently stores data on a disk named `db-data-disk-1`.

Create a stateful MIG with autohealing, create a similar instance inside the MIG, and attach the existing data disk `db-data-disk-1` to the new VM as a stateful disk:

  1. Stop the VM, `db-instance`, during a maintenance window.
  2. [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates#based-on-existing-instance) named `db-template` using the `db-instance` configuration.
  3. Detach `db-data-disk-1` from `db-instance`, and delete `db-instance`.
  4. Create an empty MIG, `example-database-mig`, from `db-template`, and configure autohealing.
  5. Create an instance with the original `db-instance` name, and attach the `db-data-disk-1` as a stateful disk:
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-database-mig/createInstances
         
         {
           "instances": [
             {
               "name": "db-instance",
               "preservedState" : {
                 "disks": {
                   "data-disk" : {
                     "source": "projects/example-project/zones/us-east1-c/disks/db-data-disk-1",
                     "mode": "READ_WRITE",
                     "autoDelete": "never"
                   }
                 }
               }
             }
           ]
         }
         

The method creates an instance, `db-instance`, in the MIG, creates a corresponding per-instance configuration with the `db-data-disk-1` stateful disk, and attaches the disk to the new instance, using `data-disk` as the device name.




### Adding, declaring, and replacing stateful disks individually for VMs in a MIG

Configure stateful disks individually for a managed instance by adding or updating a stateful disk configuration in the associated per-instance config. Then update the instance to [apply the per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) to the VM.

Configuring stateful disks individually is useful for the following tasks:

  * Adding a stateful disk from outside of a MIG to a VM in that MIG.
  * Declaring a previously stateless disk as stateful for a VM in a MIG.
  * Replacing a stateful disk with a different disk for a VM in a MIG.



**Adding a stateful disk from outside of a MIG to a VM in that MIG.** You can attach any disk from outside of a MIG to a managed instance by adding stateful configuration for the disk to the associated per-instance configuration. After you apply the config, the MIG automatically attaches the disk to the instance and treats it as stateful.

**Declaring a previously stateless persistent disk as stateful.** You can declare a previously stateless disk, currently attached to a VM, as stateful by adding stateful configuration for this disk, including its device name and URI, to the associated per-instance configuration. After you apply the config, the MIG starts preserving the disk as stateful.

**Replacing a stateful disk with a different disk.** Replacing one stateful disk with another stateful disk can be useful, for example, if you need access to a recovered backup. You can swap one stateful disk for another by updating the disk's URI while keeping the same device name in the per-instance configuration. After you apply the updated per-instance configuration, the MIG detaches the old disk and attaches the new one using the same device name. When [applying](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) the update, choose whether to keep the instance running, restart, or recreate it. Swapping a boot disk requires at least a VM restart.

###  gcloud 

To configure stateful disks individually for a VM in a MIG, add or update stateful disk configuration in the associated per-instance configuration. Then, update the instance to [apply the configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs).

If a per-instance configuration doesn't exist for the instance, use the [`gcloud compute instance-groups managed instance-configs create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/create) with one or multiple `--stateful-disk` flags:
    
    
    gcloud compute instance-groups managed instance-configs create NAME \
    --instance VM_NAME \
    --stateful-disk device-name=DEVICE_NAME[,source=DISK][,mode=MODE][,auto-delete=DELETE_RULE] \
    [--no-update-instance | --update-instance] \
    [--instance-update-minimal-action MINIMAL_ACTION]
    

If a per-instance configuration already exists for the instance, use the [`gcloud compute instance-groups managed instance-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/update) with one or multiple `--stateful-disk` flags.

The `--update-instance` flag (default) applies the changes immediately to the instance. If you use `--no-update-instance`, the changes remain unapplied and are [applied](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) when you next recreate or update the instance.
    
    
    gcloud compute instance-groups managed instance-configs update NAME \
    --instance VM_NAME \
    --stateful-disk device-name=DEVICE_NAME[,source=DISK][,mode=MODE][,auto-delete=DELETE_RULE] \
    [--no-update-instance | --update-instance] \
    [--instance-update-minimal-action MINIMAL_ACTION]
    

Replace the following:

  * `NAME`: The name of the managed instance group.
  * `VM_NAME`: The name of the VM instance for which to configure stateful disks.
  * `DEVICE_NAME`: The device name used for attaching the disk.
  * `DISK`: The URI of an existing persistent disk to attach under the specified `DEVICE_NAME`, in the format `projects/project-id/zones/zone/disks/disk-name` for a zonal disk and `projects/project-id/regions/region/disks/disk-name` for a regional disk.

The `source=DISK` subflag is optional if the device is already defined in the instance's per-instance configuration. Otherwise it is required.

If omitted, the currently configured disk URI remains unchanged.

  * `MODE`: Specifies the mode of the disk. You can only specify `mode` if you also specify `source`. Supported options are:

    * `ro`: Read-only.
    * `rw`: (Default.) Read/write.

If omitted, the default value is set for a new stateful disk configuration; the value remains unchanged in an existing configuration.

  * `DELETE_RULE`: A value that prescribes what should happen to a stateful disk when a VM is deleted. The available options are as follows:

    * `never`: (Default.) Never delete the disk; instead, detach the disk when its instance is deleted.
    * `on-permanent-instance-deletion`: Delete the stateful disk when its instance is permanently deleted from the instance group, for example, when the instance is deleted manually or when the group size is decreased.

If omitted, the default value is set for a new stateful disk configuration; the value remains unchanged in an existing configuration.

Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.

  * `MINIMAL_ACTION`: Perform at least the specified action when applying the per-instance configuration update to the instance. Must be used together with the `--update-instance` flag. The value must be one of:

    * `none`: No action.
    * `refresh`: Apply updates that are possible to apply without stopping the VM.
    * `restart`: Stop the VM and then start it again.
    * `replace`: Recreate the VM.

If omitted, the least disruptive action required by the update is used.




**Example**

The data on a currently attached stateful disk, `data-disk-1`, got corrupted, and you want to restore it from the latest backup. You created a disk, `data-disk-2`, from a snapshot to replace the corrupted disk in instance, `db-instance-1`, managed by a stateful MIG, `example-database-mig`. The original disk `data-disk-1`, is attached under the `data-disk` device name with an auto-delete rule to never delete the disk.

To replace `data-disk-1` with `data-disk-2`, run the following command:
    
    
    gcloud compute instance-groups managed instance-configs update example-database-mig \
      --instance db-instance-1 \
      --stateful-disk device-name=data-disk,source=projects/example-project/zones/us-east1-c/disks/data-disk-2 \
      --update-instance \
      --instance-update-minimal-action restart
    

The command does the following:

  1. Updates the per-instance configuration for `db-instance-1`: 
     1. Updates the source for the disk with device name `data-disk` from `data-disk-1` (last configuration) to `data-disk-2` (new configuration).
     2. Keeps the auto-delete rule to never delete the disk because the `auto-delete` parameter is omitted in the `--stateful-disk` flag and, by default, the delete rule is `never`.
  2. Applies the per-instance configuration update to the `db-instance-1` VM immediately because the `--update-instance` flag is included. The MIG detaches `data-disk-1` and attaches `data-disk-2` under the same device name, `data-disk`.
  3. Because the minimal action is set to `restart`, the MIG restarts the `db-instance-1` instance to update the VM, which helps the database application to start using the new disk.



###  Terraform 

To configure stateful disks individually for a VM in a MIG, add the stateful disk configuration in the associated per-instance configuration. Then, update the instance to [apply the configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs).

To add per-instance configuration for a VM, use the [`google_compute_per_instance_config` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_per_instance_config) and include the `preserved_state` block as shown in the following sample.
    
    
    resource "google_compute_per_instance_config" "default" {
      instance_group_manager = google_compute_instance_group_manager.default.name
      zone                   = google_compute_instance_group_manager.default.zone
      name                   = "db-instance"
      preserved_state {
        disk {
          device_name = "data-disk"
          source      = google_compute_disk.default.id
          delete_rule = "NEVER"
        }
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To configure stateful disks individually for VMs in a MIG, add or update the stateful disk configuration in the associated per-instance configurations. Then, update the instances to [apply the configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs).

If per-instance configurations don't yet exist for the given VMs, use the [`instanceGroupManagers.updatePerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/updatePerInstanceConfigs) or [`regionInstanceGroupManagers.updatePerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/updatePerInstanceConfigs) with stateful configuration for one or multiple disks:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME/updatePerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "VM_NAME",
          "preservedState" : {
            "disks": {
              "DEVICE_NAME" : {
                "source": "DISK",
                "mode": "MODE",
                "autoDelete": "DELETE_RULE"
              },
              ...
            }
          },
          "fingerprint: "FINGERPRINT"
        },
        ...
      ]
    }
    

**Note:** While you can use `updatePerInstanceConfigs` for updating existing per-instance configurations, it fully replaces the specified per-instance configurations with new values. Instead, we recommend that you use the `patchPerInstanceConfigs` method to update existing per-instance configurations because patching keeps the omitted configuration unchanged and prevents the risk of accidental deletion of stateful items or reset of the values to defaults.

If per-instance configurations already exist for the given VMs, use the [`instanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs) or [`regionInstanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs) with stateful configuration for one or multiple disks:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "VM_NAME",
          "preservedState" : {
            "disks": {
              "DEVICE_NAME" : {
                "source": "DISK",
                "mode": "MODE",
                "autoDelete": "DELETE_RULE"
              },
              ...
            }
          },
          "fingerprint: "FINGERPRINT"
        },
        ...
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: The project ID for the request.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG). 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `NAME`: The name of the MIG.
  * `VM_NAME`: The name of the VM, for which to configure stateful disks.
  * `DEVICE_NAME`: The device name used for attaching the disk.
  * `DISK`: The URI of an existing persistent disk to attach under the specified `DEVICE_NAME`, in the format `projects/project-id/zones/zone/disks/disk-name` for a zonal disk and `projects/project-id/regions/region/disks/disk-name` for a regional disk.

The `"source": "DISK"` field is optional if the device is already defined in the instance's per-instance configuration. Otherwise it is required.

If the `source` field is omitted, the currently configured disk URI remains unchanged.

  * `MODE`: (Optional.) Specifies the mode of the disk. `mode` can only be specified if `source` is given. Supported options are:

    * `READ_ONLY`: Read-only.
    * `READ_WRITE`: (Default.) Read/write.

If omitted, the default value is set for a new stateful disk configuration; the value remains unchanged in an existing configuration.

  * `DELETE_RULE`: (Optional.) A value that prescribes what should happen to a stateful disk when a VM is deleted. The available options are as follows:

    * never: (Default.) Never delete the disk; instead, detach the disk when its instance is deleted.
    * `on-permanent-instance-deletion`: Delete the stateful disk when its instance is permanently deleted from the instance group, for example, when the instance is deleted manually or when the group size is decreased.

If the `autoDelete` field is omitted, the default value is set for a new stateful disk configuration; the value remains unchanged in an existing configuration.

Regardless of the value of the delete rule, stateful disks are always preserved on instance autohealing, update, and recreation operations.

  * `FINGERPRINT`: (Optional). The fingerprint for the given config if it already exists. Used for optimistic locking. To see the latest fingerprint, make a `get()` request to retrieve the resource.




The `updatePerInstanceConfigs` and `patchPerInstanceConfigs` methods update the specified per-instance configurations but don't apply the configuration updates to the associated managed VMs. The changes are applied to an instance when the MIG is instructed to recreate or update the instance. You can also [selectively update the instance](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig) to apply the changes.

**Example**

The data on a currently attached stateful disk, `data-disk-1`, got corrupted, and you want to restore it from the latest backup. You created a disk, `data-disk-2`, from a snapshot to replace the corrupted disk in instance, `db-instance-1`, managed by a stateful MIG, `example-database-mig`. The original disk `data-disk-1`, is attached under the `data-disk` device name with an auto-delete rule to never delete the disk.

To update the per-instance configuration for `db-instance-1` with the new disk, call the `patchPerInstanceConfigs` method:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-database-mig/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "db-instance-1",
          "preservedState" : {
            "disks": {
              "data-disk" : {
                "source": "projects/example-project/zones/us-east1-c/disks/data-disk-2"
              }
            }
          }
        }
      ]
    }
    

The method patches the per-instance configuration for `db-instance-1`:

  1. Updates the `source` for a disk with device name `data-disk` from `data-disk-1` (last configuration) to `data-disk-2` (new configuration).
  2. Keeps `mode` and `autoDelete` parameters unchanged because the parameters are omitted in the request.



The config update is not yet applied to the `db-instance-1` VM. The MIG applies the config update when you recreate or update the instance.

To apply the per-instance configuration update to the `db-instance-1` VM, call the [`instanceGroupManagers.applyUpdatesToInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/applyUpdatesToInstances) for the instance:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-database-mig/applyUpdatesToInstances
    {
      "instances": ["/zones/us-east1-c/instances/db-instance-1"],
      "minimalAction": "RESTART"
    }
    

The method updates the managed instance's preserved state, detaching `data-disk-1` and attaching `data-disk-2` under the same device name `data-disk`. Because the `minimalAction` is set to `RESTART`, the method restarts the `db-instance-1` VM, which lets the database application start using the new disk.

### Detaching a stateful disk or declaring it stateless for an individual VM

You might need to detach a stateful disk or configure it to be treated as stateless for an individual VM. For example:

  * If you rearchitect your app to move the state off the disk.
  * If you configure the disk to be stateful by mistake and would like to revert it.



Detach a stateful disk or make it stateless for an individual VM by removing the disk's stateful configuration from the associated per-instance config or deleting the entire per-instance configuration. When you [apply](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) the change:

  * If the disk is not defined in the instance template, the MIG detaches the disk. 
    * The MIG does not delete the disk when you delete its configuration from the per-instance configuration, regardless of the auto-delete rule in the configuration.
  * If the disk is defined by the instance template, the MIG treats the disk as stateless, which means that the MIG recreates the disk from its source in the instance template on subsequent instance recreation, update, or autohealing events.

**Note:** If you set a disk configuration for the same device name in the MIG's stateful policy, the disk remains stateful even if you remove its configuration from the per-instance configuration. Remove the disk's configuration from both the stateful policy and per-instance configuration to make the disk stateless.

Removing a disk configuration from a per-instance configuration does not restart a running VM instance, unless you explicitly choose to do so.

For more information, see [Applying per-instance configurations updates](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#how_per-instance_configuration_updates_are_applied_to_instances).

###  gcloud 

To detach stateful disks or declare them stateless individually for a VM in a MIG, remove the stateful disk configuration from the associated per-instance configuration or [delete the whole per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_stateful_configuration_for_a_specific_vm) if it doesn't contain any other state. Update the instance to apply the configuration.

To remove a stateful disk configuration from the associated per-instance config, use the [`gcloud compute instance-groups managed instance-configs update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/instance-configs/update) with the `--remove-stateful-disks` flag. The `--update-instance` flag (default) applies the changes immediately to the instance. If you use `--no-update-instance`, the changes remain unapplied and are [applied](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs) when you next recreate or update the instance.
    
    
    gcloud compute instance-groups managed instance-configs update NAME \
      --instance VM_NAME \
      --remove-stateful-disks DEVICE_NAME[,DEVICE_NAME,...] \
      [--no-update-instance | --update-instance] \
      [--instance-update-minimal-action MINIMAL_ACTION]
    

Replace the following:

  * `NAME`: The name of the MIG.
  * `VM_NAME`: Name of the VM from which to remove stateful configuration.
  * `DEVICE_NAME`: The device name used for attaching the disk.
  * `MINIMAL_ACTION`: Perform at least the specified action when updating the VM with its per-instance configuration. Can only be used together with `--update-instance`. The value must be one the following:

    * `none`: No action.
    * `refresh`: Apply updates that are possible to apply without stopping the VM.
    * `restart`: Stop the VM and then start it again.
    * `replace`: Recreate the VM.

If omitted, the least disruptive action required by the update is used.




**Example**

You run a legacy application on a MIG named `example-legacy-group`. Each VM in the MIG stores application data on a boot disk with device name, `boot-disk`. Using per-instance configurations, you configured each boot disk to be stateful. Now you have moved application data to an additional disk, and you want to make the boot disk stateless for each VM to facilitate updating to new images.

For each instance, for example, for `node-1`, run the command:
    
    
    gcloud compute instance-groups managed instance-configs update example-legacy-group \
      --instance node-1 \
      --remove-stateful-disks boot-disk \
      --update-instance
    

The command does the following:

  1. Removes configuration for the disk with device name `boot-disk` from the per-instance configuration for `node-1`.
  2. Applies the per-instance configuration update to the `node-1` VM immediately because the `--update-instance` flag is included. The MIG removes the boot disk from the managed instance's [`preservedStateFromConfig`](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) and treats the boot disk as stateless, which means that the MIG recreates the disk from its boot image in the instance template on subsequent instance recreation, update, or autohealing events.



###  REST 

To detach stateful disks or declare them stateless individually for a VM in a MIG, remove the stateful disk configuration from the associated per-instance configuration or [delete the whole per-instance configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#removing_stateful_configuration_for_a_specific_vm) if it doesn't contain any other state. Then update the instance to [apply the configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#applying_per-instance_configs).

**To remove a stateful disk configuration from the associated per-instance config** , use the [`instanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patchPerInstanceConfigs) or [`regionInstanceGroupManagers.patchPerInstanceConfigs` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patchPerInstanceConfigs):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/NAME/patchPerInstanceConfigs
    
    {
      "perInstanceConfigs": [
        {
          "name": "VM_NAME",
          "preservedState" : {
            "disks": {
              "DEVICE_NAME" : null
            },
            ...
          },
          "fingerprint: "FINGERPRINT"
          ...
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: The project ID for the request.
  * `ZONE`: The [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the MIG is located (applies to a zonal MIG). 
    * For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region of the MIG.
  * `NAME`: The name of the MIG.
  * `VM_NAME`: The name of the VM from which to remove stateful configuration.
  * `DEVICE_NAME`: The device name used for attaching the disk.
  * `FINGERPRINT`: The fingerprint for the given config if it already exists. Used for optimistic locking. To see the latest fingerprint, make a `get()` request to retrieve the resource.



The `patchPerInstanceConfigs` method patches the specified per-instance configurations but does not apply the changes to the associated VMs. The changes are applied to a VM when you recreate or update the instance. You can apply the changes [manually](https://docs.cloud.google.com/compute/docs/instance-groups/updating-selected-instances-in-a-mig) or use [automated](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups) rolling updates.

**Example**

You run a legacy application on a MIG named `example-legacy-group`. Each VM in the MIG stores application data on a boot disk with device name `boot-disk`. You configured the boot disk as stateful in the MIG's per-instance configurations when migrating the standalone VMs into the MIG. You have moved application data to an additional disk and now want to make the boot disk stateless for each VM to make it easy to update to new images.

  1. Call the `patchPerInstanceConfigs` method for the instances, for example, for `node-1` with a `null` value for the boot disk:
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-legacy-group/patchPerInstanceConfigs
         
         {
           "perInstanceConfigs": [
             {
               "name": "node-1",
               "preservedState" : {
                 "disks": {
                   "boot-disk" : null
                 }
               }
             }
           ]
         }
         

The method removes configuration for the disk with device name `boot- disk` from the per-instance configuration for `node-1`. The config update is not yet applied to the `node-1` VM instance. The config update will be applied on the next instance recreation or update.

  2. To apply the per-instance configuration update to the `node-1` VM instance, call the `instanceGroupManagers.applyUpdatesToInstances` [method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/applyUpdatesToInstances) for the instance:
         
         POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-east1-c/instanceGroupManagers/example-legacy-group/applyUpdatesToInstances
         {
           "instances": ["/zones/us-east1-c/instances/node-1"]
         }
         

The MIG removes the boot disk from the [`preservedStateFromConfig`](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) for the `node-1` instance and treats the disk as stateless. That is, the MIG recreates the disk from its boot image in the instance template on subsequent instance recreation, update, or autohealing events.




## Billing

Compute Engine doesn't automatically delete stateful persistent disks that you detach from the MIG. You are still billed for the provisioned space of any detached persistent disks. To avoid incurring disk space costs after a disk is detached, delete the disk. For more information, see [Disk pricing](https://docs.cloud.google.com/compute/disks-image-pricing#disk-pricing).

## Feedback

We want to learn about your use cases, challenges, and feedback about stateful MIGs. You can share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * [Configure stateful metadata](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs) for VMs in a MIG.
  * Learn about [applying, viewing, and removing](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-metadata-in-migs) stateful configuration.
  * [Get info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about a specific MIG and its managed instances, including VM status and properties.
  * Learn more about [MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) and [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
