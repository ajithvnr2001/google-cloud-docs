---
url: https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig/
title: Add and remove VMs from a MIG \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:42.251408+00:00
---

# Add and remove VMs from a MIG  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add and remove VMs from a MIG Stay organized with collections  Save and categorize content based on your preferences. 

After you've [created a managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances), you might want to add or remove VMs from that group to meet your workload's needs. If you have reached the default [limit](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations) for the maximum number of VMs that you can add to a MIG, and you need more VMs, you can increase the size limit of the MIG.

To add or remove VMs in a MIG, you can do the following:

  * Automatically add or remove VMs by setting the target size of the MIG: 
    * Use autoscaling for stateless applications
    * Create a resize request in the MIG
    * Manually set the size of the MIG
  * Manually add, remove or abandon specific instances: 
    * Create instances with specific names
    * Delete specific instances
    * Abandon specific instances
    * Configure VM instance names in a MIG



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




## Set the group's target size

You can set a MIG's target size automatically by using an autoscaler or set the size manually.

### Automatically adding and removing VMs in a MIG

You can configure managed instance groups to automatically add or remove VMs based on their workloads. Your applications can gracefully handle increases in traffic, and you can reduce your costs when the need for compute resources is lower. To start scaling your managed instance groups, see [Create a MIG with autoscaling](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling).

For more information, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

### Create a resize request

You can use resize requests to add GPU VMs to a MIG all at once. This feature helps you avoid charges for partial capacity while Compute Engine provisions all resources. MIG resize requests use the flex-start or reservation-bound provisioning models. These models let you obtain vCPUs and GPUs at a discounted price.

For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

### Manually setting the size of a MIG

If a MIG isn't already set to [automatically scale](https://docs.cloud.google.com/compute/docs/autoscaler), you can manually resize the group to change the number of compute instances in it. If you increase the size, the MIG uses the current instance template to add new compute instances. If you decrease the size, the MIG deletes compute instances from the group based on several factors. For more information, see [Factors that affect the deletion of VM instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#factors_affecting_vm_deletion).

When you manually set the size of a MIG, consider the following:

  * If the group is part of a [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service) that has [enabled connection draining](https://docs.cloud.google.com/compute/docs/load-balancing/enabling-connection-draining), then it can take up to an additional 60 seconds after the connection draining period finishes before the compute instance is removed or deleted. 
  * If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in the instance template that your MIG uses, then the compute instances in your MIG gracefully shut down when the MIG deletes them.


**Note:** If both graceful shutdown and connection draining are enabled in a MIG, then Compute Engine drains connections before it gracefully shuts down the compute instances in the MIG.

When you manually set the size of a MIG, by default, the MIG creates the VMs independently as soon as the resources become available. To obtain all of your required VMs all at once, you must set the target size policy mode to `BULK` when you create the MIG. For more information about bulk mode, see [About bulk creation of instances in MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the instance group where you want to change the group size.

  3. Click **Edit** to modify this managed instance group.

  4. Click **Group size & autoscaling** to expand the section.

  5. In the **Number of instances** field, specify the number of instances that you want to include in this managed instance group.

If **Autoscaling** is enabled, the group automatically adds or removes instances as necessary. However, you can change the **Minimum number of instances** and the **Maximum number of instances** values to indirectly adjust the group size through autoscaler.

  6. Click **Save** to apply the new template.




###  gcloud 

Use the [`resize` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/resize).
    
    
    gcloud compute instance-groups managed resize INSTANCE_GROUP_NAME \
        --size NEW_SIZE \
        --zone ZONE

###  REST 

Call the `resize` method for a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/resize) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/resize) MIG resource. Specify the new instance group size as a parameter.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME/resize?size=NEW_SIZE

If the instance group is a regional managed instance group, replace `zones/ZONE` with `regions/REGION`.

After you make a request to resize a managed instance group, the compute instances start or stop as soon as the system can provision or delete them. This process can take a significant amount of time depending on the number of compute instances in the group. [Verify the status of instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances) in your managed instance group.

**Note:** Because new compute instances are created with the current instance template, your group can contain dissimilar compute instances if you add compute instances to the group after you change the instance template. Existing compute instances use their previous instance templates until you [recreate them](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#recreate_instances), and new compute instances use the specified instance template for the MIG.

### Disable the creation retries mode during a resize operation

**Beta**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, if the initial creation of an instance fails, the MIG continuously retries to create the instance, until the instance is successfully created. For regional MIGs that use `BALANCED` or `ANY` target distribution shapes, the MIG automatically attempts to create the instance in other selected zones if the initial creation fails, rather than retrying in the same zone.

However, you can disable this automatic creation retry when you resize the instance group. When creation retries are disabled, the MIG attempts to create each instance only once. If an [error](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_instance_errors) occurs during instance creation, the MIG doesn't retry to create that instance. Instead, the MIG removes the instance from the group's [list of managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances) and decreases the target size of the MIG.

This creation retries mode is applicable only during the first creation attempt of an instance. If an instance is created successfully while this mode is enabled, the instance behaves like all other VMs created by a regular resize operation. In particular, if a running instance dies unexpectedly at a later time and needs to be recreated, this mode does not affect the recreation behavior in that scenario.

Disabling the creation retries mode is especially useful in scenarios where you have systems automatically creating groups of instances where an exact number of instances is not required. You might prefer to stabilize quickly on the size of the MIG and be flexible in the number of instances in the group, rather than to wait indefinitely until all the requested instances are created. Instance creation can delay temporarily or permanently because of quota errors or other unrelated issues.

#### Limitations

  * You cannot disable creation retries in a MIG that has the following configuration:

    * [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler)
    * [`EVEN` target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape#how_even_works) in regional MIGs
    * [Bulk mode](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode) of target size policy
  * For regional MIGs with a `BALANCED` or `ANY_SINGLE_ZONE` target distribution shape, you must disable [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution) before you can disable creation retries mode.




To disable the creation retries mode while resizing a MIG, use the Google Cloud CLI or REST.

**Important:** Google recommends that you don't concurrently run two resize operations with different creation retries modes as it might result in an unexpected target size. For example, if you issue a resize command without creation retries and, before it completes, you issue a second resize command with creation retries enabled, the second command does not invalidate the first one. Some instances are created without retries and if any of them fail, the group's target size decreases accordingly.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  gcloud 

Use the [beta `resize` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/instance-groups/managed/resize) with the `--no-creation-retries` flag.
    
    
    gcloud beta compute instance-groups managed resize INSTANCE_GROUP_NAME \
        --size NEW_SIZE \
        **--no-creation-retries** \
        [--region REGION | --zone ZONE]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: The name of the MIG that you want to resize.
  * `NEW_SIZE`: The target number of running instances in managed instance group.
  * `ZONE`: For zonal MIGs, the zone where the MIG is located.
  * `REGION`: For regional MIGs, the region where the MIG is located.



###  REST 

For a zonal MIG, use the [beta `instanceGroupManagers.resizeAdvanced` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/resizeAdvanced) or, for a regional MIG, use the [beta `regionInstanceGroupManagers.resizeAdvanced` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/regionInstanceGroupManagers/resizeAdvanced). Specify the new group size and the `noCreationRetries` field in the request body.

For example, make the following call to resize a zonal MIG with creation retries mode disabled.
    
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME/resizeAdvanced
    
    {
     "targetSize": NEW_SIZE,
     **"noCreationRetries": true**
    }

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `ZONE`: The zone where the MIG is located. For a regional MIG, replace `zones/ZONE` with `regions/REGION` and specify the region. For more information, see [About regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).
  * `INSTANCE_GROUP_NAME`: The name of the MIG that you want to resize.
  * `NEW_SIZE`: The target number of running instances in the managed instance group.

You can see which instances are being created and in which mode by using the `listManagedInstances` method. When the creation retries mode is disabled, instances that you create have a [`currentAction`](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances) of `CREATING_WITHOUT_RETRIES`.




## Add, remove or abandon specific instances

The following sections show how to add, remove, or abandon specific instances in a MIG.

### Creating instances with specific names in MIGs

If your workload or orchestration system requires specific instance names, you can add those instances to an existing MIG. This section shows how to add instances based on availability. If resources are unavailable, then the MIG adds a portion of the instances and creates the remaining ones when resources become available. To add GPU instances with specific names all at once to a MIG, see instead Create a resize request in this document.

The names that you assign to these instances persist if the MIG recreates them. For more information about preserving the state of MIG instances, see [stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs).

To use specific naming patterns for instances within a MIG, refer to the Configure VM instance names in a MIG section of this document.

#### Limitations

If you create instances with specific names:

  * You must [turn off](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler) autoscaling during the instance creation process.
  * You must set the MIG's update policy to be [opportunistic](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs#setting_up_an_opportunistic_or_proactive_update).
  * If you are updating a regional MIG: 
    * You must disable [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-enable-disable-proactive-redistribution).
    * You can't select which zone to create the VM in.
  * You can't use duplicate VM instance names within a project.



You can use the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance) or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances) to add VMs with specific names to an existing MIG.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  gcloud 

Use the [`instance-groups managed create-instance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create-instance).
    
    
    gcloud compute instance-groups managed create-instance INSTANCE_GROUP_NAME \
        --instance INSTANCE_NAME \
        [--region REGION | --zone ZONE]

Replace the following:

  * INSTANCE_GROUP_NAME is the name of the regional or zonal MIG to add a new instance to.
  * INSTANCE_NAME is the name you want to assign to the new instance.



###  REST 

Send a POST request to the [`regionInstanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/createInstances) method. For a zonal managed instance group, use the [`instanceGroupManagers.createInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/createInstances) method. In the request body, include the `instances` field with names for one or more instances.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/createInstances
    {
      "instances": [
        {
          "name": "INSTANCE_NAME_1"
        },
        {
          "name": "INSTANCE_NAME_2"
        }
      ]
    }
    

### Deleting specific instances from a group

You can delete individual compute instances in a MIG. Deleting compute instances reduces the specified `targetSize` of the instance group and removes the compute instance from any [target pools](https://docs.cloud.google.com/compute/docs/load-balancing/network/target-pools) of which they are a member.

When you delete specific compute instances from a MIG, consider the following:

  * If the group is part of a [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service) that has [enabled connection draining](https://docs.cloud.google.com/compute/docs/load-balancing/enabling-connection-draining), then it can take up to an additional 60 seconds after the connection draining period finishes before the compute instance is removed or deleted. 
  * If you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) in the instance template that your MIG uses, then the compute instances in your MIG gracefully shut down when the MIG deletes them.


**Note:** If both graceful shutdown and connection draining are enabled in a MIG, then Compute Engine drains connections first, and then gracefully shuts down the compute instances in the MIG.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. In the **Name** column of the list, click the name of the instance group where you want to delete individual instances. A page opens with the instance group properties and a list of instances that are included in the group.

  3. In the **VM instances** section, select one or more instances that you want to delete.

  4. Click **Delete**.

  5. In the dialog that appears, do the following:

     1. Optional: To delete the compute instances without gracefully shutting them down, or to end an ongoing graceful shutdown, select the **Skip graceful shutdown (if applicable)** checkbox.
     2. Enter `delete`, and then click **Delete**.

The MIG deletes the selected instances.




###  gcloud 

To delete an instance with the gcloud CLI, use the [`instance-groups managed delete-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete-instances).
    
    
    gcloud compute instance-groups managed delete-instances INSTANCE_GROUP_NAME \
        --instances INSTANCE_NAME_1,INSTANCE_NAME_2 \ 
        [--region REGION | --zone ZONE]

The command returns the operation status per instance:

  * `SUCCESS` is returned if the gcloud CLI deleted the instance.
  * `FAIL` is returned for all instances if any instance that you specify in the request is not a member of the group, if any member is already being deleted or abandoned, or if the request fails for any other reason.
  * `SKIPPED` is returned only if you use the `--skip-instances-on-validation-error` flag and the instance is not a member of the group or is already being deleted or abandoned.
  * `MEMBER_NOT_FOUND` is returned only for regional groups when the gcloud CLI wasn't able to resolve the zone from the instance name.



If you anticipate that your deletion request might conflict with concurrent operations, use the `--skip-instances-on-validation-error` flag. This flag specifies whether the request should proceed even if the request includes instances that are not members of the group or that are already being deleted or abandoned—for example, instances that are being deleted by an autoscaler. By default, if you omit this flag and such an instance is specified in the request, the operation fails. The operation always fails if the request contains a badly formatted instance name or a reference to an instance that exists in a zone or region other than the group's zone or region.

For example, the following command requests deletion of four instances, but three of them are no longer in the group:
    
    
    gcloud compute instance-groups managed delete-instances example-mig \
        --instances=example-instance-1,example-instance-2,example-instance-3,example-instance-4 \
        --region=us-central1 \
        **--skip-instances-on-validation-error**

In this example, three instances didn't pass validation, so they were skipped, while `example-instance-3` was deleted:
    
    
    Updated [https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/instanceGroupManagers/example-mig].
    PROJECT          ZONE           INSTANCE               STATUS   VALIDATION_ERROR
    example-project  us-central1-a  example-instance-1     SKIPPED  Cannot delete instance https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/example-instance-1 that was already deleted.
    example-project  us-central1-a  example-instance-2     SKIPPED  Cannot delete instance https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/example-instance-2 that was already abandoned.
    example-project  us-central1-a  example-instance-3     SUCCESS
    example-project  us-central1-a  example-instance-4     SKIPPED  Cannot find instance https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/example-instance-4.
    

If you omit the `--skip-instances-on-validation-error` flag and if any instance does not pass validation, then no instance is deleted:
    
    
    gcloud compute instance-groups managed delete-instances example-mig \
        --instances=example-instance-1,example-instance-2,example-instance-3,example-instance-4 \
        --region=us-central1
    
    Updated [https://www.googleapis.com/compute/v1/projects/example-project/regions/us-central1/instanceGroupManagers/example-mig].
    PROJECT          ZONE             INSTANCE              STATUS
    example-project  us-central1-a    example-instance-1    FAIL
    example-project  us-central1-a    example-instance-2    FAIL
    example-project  us-central1-a    example-instance-3    FAIL
    example-project  us-central1-a    example-instance-4    FAIL
    

If you want to delete instances in a MIG without gracefully shutting them down, or to end an ongoing graceful shutdown, then use the same command with the `--no-graceful-shutdown` flag:
    
    
    gcloud compute instance-groups managed delete-instances INSTANCE_GROUP_NAME \
        --instances INSTANCE_NAME_1,INSTANCE_NAME_2 \
        **--no-graceful-shutdown** \
        [--region REGION | --zone ZONE]

###  REST 

Send a POST request to the [`regionInstanceGroupManagers.deleteInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/deleteInstances) method. For a zonal managed instance group, use the [`instanceGroupManagers.deleteInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/deleteInstances) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/deleteInstances
    
    {
      "instances": [
        "zones/ZONE/instances/INSTANCE_NAME_1",
        "zones/ZONE/instances/INSTANCE_NAME_2"
       ]
    }

If you anticipate that your deletion request might conflict with concurrent operations, use the `skipInstancesOnValidationError` field. This field specifies whether the request should proceed even if the request includes instances that are not members of the group or that are already being deleted or abandoned—for example, instances that are being deleted by an autoscaler. By default, if you omit this flag and such an instance is specified in the request, the operation fails. The operation always fails if the request contains a badly formatted instance name or a reference to an instance that exists in a zone or region other than the group's zone or region.

For example, the following request to delete 2 instances will succeed even if one of the instances is already deleted or being deleted:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/deleteInstances
    
    {
     "instances": [
      "zones/ZONE/instances/INSTANCE_NAME_1",
      "zones/ZONE/instances/INSTANCE_NAME_2"
     ],
     **"skipInstancesOnValidationError": true**
    }

You can view instances that were skipped in the operation by viewing the operation. For regional MIGs, use the [`regionOperations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations/get). For zonal MIGs, use the [`zoneOperations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations/get). Warnings are listed in the operation's warning field.

If you want to delete instances in a MIG without gracefully shutting them down or end an ongoing graceful shutdown, then include the `noGracefulShutdown` query parameter set to `true` in the request URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/deleteInstances**?noGracefulShutdown=true**
    
    {
      "instances": [
        "zones/ZONE/instances/INSTANCE_NAME_1",
        "zones/ZONE/instances/INSTANCE_NAME_2"
       ]
    }

After you make a request to delete instances in a managed instance group, the instances stop as soon as the system can delete them. This process can take a significant amount of time depending on the number of instances that you delete from the group. [Verify the status of the group](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group) or [verify the status of the managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

### Abandoning instances from a MIG

You can separate a VM instance from a managed instance group to debug issues with individual instances without affecting the group as a whole. Abandoning an instance from a group also removes the instance from [load balancers](https://docs.cloud.google.com/compute/docs/load-balancing) that were assigned to the managed instance group. [Target pools](https://docs.cloud.google.com/compute/docs/load-balancing/network/target-pools) that were manually assigned to specific individual instances are not removed.

You can't add an abandoned VM instance back to the group. Abandoning instances reduces the specified `targetSize` of the instance group, but doesn't change any specified autoscaler settings. Managed instance groups with an autoscaler continue to add or remove instances automatically as necessary. For a regional MIG with autoscaling set to `ONLY_SCALE_OUT` mode, if you abandon a VM instance to reduce the MIG target size to the [autoscaler's recommended size](https://docs.cloud.google.com/compute/docs/autoscaler#recommended_size), then the autoscaler might create a new VM instance in the same zone of the abandoned VM. In such cases, to avoid creation of a new VM instance, try abandoning VM instance from a different zone.

If the group is part of a [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service) that has [enabled connection draining](https://docs.cloud.google.com/compute/docs/load-balancing/enabling-connection-draining), then it can take up to an additional 60 seconds after the connection draining period finishes before the compute instance is removed or deleted.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page .

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. In the **Name** column of the list, click the name of the instance group from which you want to remove instances. A page opens with the instance group properties and a list of instances that are included in the group.

  3. In the **VM instances** section, select one or more instances that you want to remove from the group.

  4. Click **Remove from group**.

  5. In the dialog to confirm the removal of selected instances, type `remove`, and then click **Remove**.

The MIG removes the selected instances from the group. The removed instances continue to run outside of the group.




###  gcloud 

To remove an instance from the instance group _without deleting the VM_ , use the [`instance-groups managed abandon-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/abandon-instances).
    
    
    gcloud compute instance-groups managed abandon-instances INSTANCE_GROUP_NAME \
        --instances INSTANCE_NAME_1,INSTANCE_NAME_2 \
        [--region REGION | --zone ZONE]

###  REST 

Send a POST request to the [`regionInstanceGroupManagers.abandonInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/abandonInstances) method. For a zonal managed instance group, use the [`instanceGroupManagers.abandonInstances`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/abandonInstances) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME/abandonInstances
    
    {
     "instances": [
      "zones/ZONE/instances/INSTANCE_NAME_1",
      "zones/ZONE/instances/INSTANCE_NAME_2"
     ]
    }

After you make a request to abandon instances from a managed instance group, the group removes the instances as soon as possible. [Verify the status of the group](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_group) or [verify the status of the managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#verify_instances).

## Configure VM instance names in a MIG

You can customize the names of VMs in a managed instance group (MIG) by setting the `baseInstanceName` field. Compute Engine generates instance names based on one of the following patterns:

  * **Sequential numbering** : Set `baseInstanceName` to a string that includes one or more hash characters (`#`) to define a numbering pattern. Compute Engine replaces hash characters with sequential numbers, starting from 0. The number of hash characters determines the minimum number of digits in the name, with leading zeros added for padding.

**Note:** Sequential numbering isn't supported in regional MIGs with target distribution shape `EVEN`, `BALANCED`, or `ANY` with more than one zone specified.
    * **Example** : `"baseInstanceName": "instance-###"`
    * **Resulting VM names** : `instance-000`, `instance-001`, `instance-002`.
    * To use a different starting number for the sequence, specify the number in brackets after the hash characters—for example, `PREFIX-###[100]` such as `instance-###[100]`. This results in VM names `instance-100`, `instance-101`, and `instance-102`.
  * **Custom prefix** : Set `baseInstanceName` to a string that doesn't include hash characters (`#`). Compute Engine uses the string as a prefix, and appends a hyphen and four random characters.

    * **Example** : `"baseInstanceName": "my-vm"`
    * **Resulting VM names** : `my-vm-p4k1`, `my-vm-n2hr`.
  * **Default prefix** : If you don't set `baseInstanceName`, Compute Engine uses the MIG name as the prefix, and appends a hyphen and four random characters.

    * **MIG name example** : `my-mig`
    * **Resulting VM names** : `my-mig-xz8d`, `my-mig-4ran`.



You can configure `baseInstanceName` when you create a MIG or by updating an existing one.

**Important:** If you update `baseInstanceName` for an existing MIG, it doesn't affect the names of existing VMs; it only applies to VMs created after the update.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.update` on the managed instance group



###  gcloud 

To configure instance names when creating a MIG, use the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create) with the `--base-instance-name` flag:
    
    
      gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
          --template INSTANCE_TEMPLATE \
          --size SIZE \
          **--base-instance-name BASE_INSTANCE_NAME** \
          [--region REGION | --zone ZONE]
    

To configure instance names in an existing MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update) with the `--base-instance-name` flag:
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        **--base-instance-name BASE_INSTANCE_NAME** \
        [--region REGION | --zone ZONE]
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: The name of the MIG.
  * `INSTANCE_TEMPLATE`: The name of the instance template to use for creating VMs.
  * `SIZE`: The number of VMs in the MIG.
  * `BASE_INSTANCE_NAME`: The base name format for instances created in the MIG: 
    * To use sequential naming, include one or more hash characters (`#`) in the name—for example, `PREFIX-###` such as `instance-###`.
    * To use a custom prefix with a random suffix, use a name that doesn't include hash characters—for example, `my-vm`.
  * `REGION`: For a regional MIG, the region where the MIG is located.
  * `ZONE`: For a zonal MIG, the zone where the MIG is located.



###  REST 

To configure instance names when creating a MIG, include the `baseInstanceName` field in your request to the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) or [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers
    
    {
      "name": "INSTANCE_GROUP_NAME",
      "instanceTemplate": "global/instanceTemplates/INSTANCE_TEMPLATE",
      "targetSize": "SIZE",
      **"baseInstanceName": " BASE_INSTANCE_NAME"**
    }
    

To configure instance names in an existing MIG, include `baseInstanceName` in your request to [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      **"baseInstanceName": " BASE_INSTANCE_NAME"**
    }
    

Replace the following:

  * `PROJECT_ID`: The project ID.
  * `ZONE`: For a zonal MIG, the zone where the MIG is located.
  * `INSTANCE_GROUP_NAME`: The name of the MIG.
  * `INSTANCE_TEMPLATE`: The name of the instance template to use for creating VMs.
  * `SIZE`: The number of VMs in the MIG.
  * `BASE_INSTANCE_NAME`: The base name format for instances created in the MIG: 
    * To use sequential naming, include one or more hash characters (`#`) in the name—for example, `PREFIX-###` such as `instance-###`.
    * To use a custom prefix with a random suffix, use a name that doesn't include hash characters—for example, `my-vm`.



## Increase the group's size limit

By default, the size limit for a zonal MIG is 1,000 VMs, and the size limit for a regional MIG is 2,000 VMs. You can further increase these limits to 2,000 VMs for a zonal MIG and 4,000 VMs for a regional MIG.

To increase the limits, set the group's `listManagedInstancesResults` field to `PAGINATED`. If you still need more VMs in the group, create multiple MIGs or [contact support](https://cloud.google.com/support-hub/).

**Caution:** When you set the group's `listManagedInstancesResults` field to `PAGINATED`, the `listManagedInstances` method changes its behavior. With the default `PAGELESS` setting, the list method ignores the `maxResults` query parameter and always returns all the instances. With the `PAGINATED` setting, the list method returns paginated result with `maxResults` capped at 500 like other lists in Compute Engine. You need to make sure that all calls to these methods are aware of pagination and use the `pageToken` query parameter to page through large list of instances.  
  
There is no impact on Google Cloud CLI or the Google Cloud console which already fully support pagination.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. In the **Name** column of the list, click the name of the instance group of which you want to increase the size limit.

  3. Click **Edit** to modify the instance group.

  4. Click **Advanced Options** to expand the section.

  5. In the **Managed instance list API call results** section, select **Paginated**.

  6. Click **Save** to apply the changes.




###  gcloud 

For an existing MIG, use the [`update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update):
    
    
    gcloud compute instance-groups managed update INSTANCE_GROUP_NAME \
        **--list-managed-instances-results=PAGINATED**

For a new MIG, use the [`create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
    
    
    gcloud compute instance-groups managed create INSTANCE_GROUP_NAME \
        --template INSTANCE_TEMPLATE \
        --size SIZE \
        **--list-managed-instances-results=PAGINATED**

###  Terraform 

To increase a MIG's size limit, set the `list_managed_instances_results` argument to `PAGINATED`.

The following sample increases the size limit of a zonal MIG. For more information about the resource used in the sample, see the [`google_compute_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager). For a regional MIG, use the [`google_compute_region_instance_group_manager` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager).
    
    
    resource "google_compute_instance_group_manager" "default" {
      name                           = "my-igm"
      base_instance_name             = "test"
      target_size                    = 7
      zone                           = "us-central1-f"
      list_managed_instances_results = "PAGINATED"
      version {
        instance_template = google_compute_instance_template.default.id
        name              = "primary"
      }
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

For an existing zonal MIG, use the [`instanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/patch) or, for a regional MIG, use the [`regionInstanceGroupManagers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch)–for example:
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/regionInstanceGroupManagers/INSTANCE_GROUP_NAME
    
    {
      "listManagedInstancesResults": "PAGINATED",
    }
    

For a new zonal MIG, use the [`instanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/insert) or, for a regional MIG, use the [`regionInstanceGroupManagers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/insert).

If you want to switch back to pageless list results, you must also revert to the group's default size limit. To switch back, first ensure that the group does not exceed its default size limit, then set the `listManagedInstancesResults` field to `PAGELESS`.

## What's next

  * Learn about [working with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances), for example, to delete, abandon, and recreate managed instances.
  * [View info](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs) about managed instance groups and managed instances.
  * [Troubleshoot managed instance groups](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-migs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
