---
url: https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs/
title: View information about MIGs and managed instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:37:08.303801+00:00
---

# View information about MIGs and managed instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View information about MIGs and managed instances Stay organized with collections  Save and categorize content based on your preferences. 

Use the methods on this page to view information about your [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups) and to view information about the virtual machine (VM) instances within each MIG.

**Note:** Various policies and actions can create, delete, and modify instances that are managed by a MIG. Those operations are returned as `DONE` after the group has scheduled actions to create, delete, or update those instances. However, a `DONE` status doesn't mean that the creation, deletion, or update of instances in the group is complete; these operations might still be in progress. You must verify the status of the group, or alternatively verify the status of those instances.

## Before you begin

  * Review the [limitations](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#limitations) and then [create](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances#create_managed_group) a group.
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




## View information about MIGs

You can retrieve information about groups themselves, for example, to inspect the policies that are attached to the group and to check if the group is stable or undergoing changes. For information about the VM instances within a MIG, see View information about managed instances.

### List MIGs

To get a list of your MIGs, use the [console](https://console.cloud.google.com/compute/instanceGroups), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe), or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers/get).

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups).

If you have existing instance groups, the page lists those groups, including both MIGs and [unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

The **Group type** column specifies whether the group is managed, stateful, or unmanaged. The stateful group types are also managed instance groups.




###  gcloud 

List all MIGs within a project:
    
    
    gcloud compute instance-groups managed list

###  REST 

For zonal MIGs, call the [`instanceGroupManagers.list` method](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers/list) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroupManagers

For regional MIGs, call the [`regionInstanceGroupManagers.list` method](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/list).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/regions/region/instanceGroupManagers
    

### View a MIG's properties

To view information about a specific MIG, including its policies (for example, the group's autohealing and update policies), use the [console](https://console.cloud.google.com/compute/instanceGroups), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe), or [REST](https://docs.cloud.google.com/compute/docs/reference/latest).

To view the group's `id` value, you must use the gcloud CLI or the Compute Engine API.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups).

If you have existing instance groups, the page lists those groups. The page also lists [unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

  2. Under the **Name** column of the list, click the name of the MIG that you want to examine. A page opens with the MIG properties and a list of instances that are included in the group.

  3. Click **Details** to see the group's configuration.




###  gcloud 

To get information about a specific group:
    
    
    gcloud compute instance-groups managed describe instance-group \
        [--zone zone | --region region]

The command returns details about the group, including attached policies.

Use the `--format` flag to limit the output. For example, the following command only returns the group's autoscaler configuration if it exists.
    
    
    gcloud compute instance-groups managed describe instance-group --format="(autoscaler)"

###  REST 

For zonal MIG, call the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers/get). For regional MIGs, call the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/get).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/regions/region/instanceGroupManagers/instance-group

The response includes details about the group, including attached policies except for the group's autoscaling policy. Although autoscaling is a feature of MIGs, it is a separate REST resource.

**Autoscaling policy**

If an autoscaler is attached to the group, the autoscaler resource is listed in the group's `status.autoscaler` field.

To get information about that autoscaler, call the [`autoscalers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/get) for a zonal MIG or the [`regionAutoscalers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/get) for a regional MIG. The URL of the autoscaler resource includes its name, which, by default, is the name of the group that the autoscaler is attached to. For example, you might make the following request for a regional MIG's autoscaler:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/regions/region/regionAutoscalers/mig_name

### Check whether a MIG is stable

A MIG is stable when no instances are undergoing or scheduled for changes, and the MIG itself is not being modified.

Check a MIG's stability before you start an application-related task that depends on all instances being healthy and serving. For example, you might want to confirm that a MIG is stable before you start scheduling jobs, sending traffic, or assigning key ranges to the VMs.

Verify that all instances in a managed instance group are running and healthy by checking the value of the group's `status.isStable` field.

###  gcloud 

Use the [`describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe):
    
    
    gcloud compute instance-groups managed describe instance-group-name \
        [--zone zone | --region region]

The gcloud CLI returns detailed information about the MIG including its `status.isStable` field.

To pause a script until the MIG is stable, use the [`wait-until`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/wait-until) command with the `--stable` flag. For example:
    
    
    gcloud compute instance-groups managed wait-until instance-group-name \
        --stable \
        [--zone zone | --region region]
    Waiting for group to become stable, current operations: deleting: 4
    Waiting for group to become stable, current operations: deleting: 4
    ...
    Group is stable
    

The command returns after `status.isStable` is set to `true` for the MIG.

###  REST 

For a zonal MIG, make a `GET` request to the [`instanceGroupManagers.get`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get) method:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroupManagers/instance-group-name/get

For a regional managed instance group, replace `zones/zone` with `regions/region`:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/regions/region/instanceGroupManagers/instance-group-name/get

These requests returns detailed information about the MIG including its `status.isStable` field.

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

For individual VM instances, see Checking the status of managed instances.

### Check the repair configuration in a MIG

To check the repair configuration in a MIG, select one of the following options:

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the instance group
  * `compute.instanceGroupManagers.list` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG that you want to view. A page opens with the MIG properties and a list of VM instances that are in the group.
  3. Click the **Details** tab.
  4. In the **VM instance lifecycle** section, check the values of the following fields:

     * **Default action on failure** : If the value is **No action** , then automatic repairs of failed VMs are off.

     * **On failed health check** :

       * If the value is **No action** , then autohealing is off.
       * If the value is **Default action** and the value of **Default action on failure** field is **No action** , then also autohealing is off.
     * **Change zone during VM instance repair** : If this option is selected and when the MIG can't repair a VM in the original zone, then the MIG repairs that VM in one of the other MIG's selected zones.




###  gcloud 

Use the [`describe` method](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) as follows:
    
    
    gcloud compute instance-groups managed describe instance-group \
        --format="(instanceLifecyclePolicy)" \
        --zone=zone
    

Replace the following:

  * `instance-group`: The name of the MIG.
  * `zone`: For a zonal MIG, specify the zone. For a regional MIG, use the `--region=region` flag.



In the output, check the following values:

  * `defaultActionOnFailure`: If the value is `DO_NOTHING`, then automatic repairs of failed VMs are off.
  * `onFailedHealthCheck`: If the value is any of the following, then autohealing is off. 
    * `DEFAULT_ACTION`, provided the value of `defaultActionOnFailure` field is `DO_NOTHING`
    * `DO_NOTHING`
  * `allowChangingZone`: If the value is `YES` and when the MIG can't repair a VM in the original zone, then the MIG repairs that VM in one of the other MIG's selected zones.



The following is a sample output when repairs of failed and unhealthy VMs are turned off in a MIG:
    
    
      instanceLifecyclePolicy:
        defaultActionOnFailure: DO_NOTHING
        forceUpdateOnRepair: NO
        onFailedHealthCheck: DEFAULT_ACTION
        onRepair:
          allowChangingZone: YES
    

###  REST 

For a zonal MIG, use the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get), or, for a regional MIG, use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/get).

To view the MIG action on VM failures in a zonal MIG, make the following call:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project_ID/zones/zone/instanceGroupManagers/instance_group
    

In the response body, check the values of the following fields:

  * `defaultActionOnFailure`: If the value is `DO_NOTHING`, then automatic repairs of failed VMs are off.
  * `onFailedHealthCheck`: If the value is any of the following, then autohealing is off. 
    * `DEFAULT_ACTION`, provided the value of `defaultActionOnFailure` field is `DO_NOTHING`
    * `DO_NOTHING`
  * `allowChangingZone`: If the value is `YES` and when the MIG can't repair a VM in the original zone, then the MIG repairs that VM in one of the other MIG's selected zones.



The following is a sample output when repairs of failed and unhealthy VMs are turned off in a MIG:
    
    
    ...
    "instanceLifecyclePolicy": {
      "forceUpdateOnRepair": "NO",
      "defaultActionOnFailure": "DO_NOTHING",
      "onFailedHealthCheck": "DEFAULT_ACTION",
      "onRepair": {
        "allowChangingZone": "YES"
      }
    }
    ...
    

If the repairs are turned off and you want to turn them back on again, see [Turn on repairs or autohealing](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig#set_a_mig_to_repair_failed_and_unhealthy_vms).

### View historical autohealing operations

If you configured autohealing, then you can [view past autohealing events](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#viewing_historical_autohealing_operations).

### Monitor rolling updates

If you initiated a rolling update, and want to know when the update is complete, then see [Monitoring updates](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#monitorupdates).

### View stateful configuration

If you configured a [stateful MIG](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) and want to review your configuration, then see [Viewing stateful configuration](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_stateful_configuration_and_preserved_state).

### View the status of a TPU slice

When you create a MIG with TPU VMs or increase the MIG's size, the MIG creates TPU VMs in a `PENDING` state. When the capacity becomes available and matches your workload policy configuration, the VMs then transition through `PROVISIONING` and `STAGING` statuses before reaching the `RUNNING` status. This transition can take time, depending on the number of instances in the group.

To monitor the progress of the slice formation, you can view the status of TPU VMs and the topology using the following fields in your MIG details.

  * `currentInstanceStatuses` field shows the number of instances in each instance lifecycle state. For a list of lifecycle states, see [VM instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

To view the state of a specific instance, see [List a MIG's managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#listing_a_migs_managed_instances).

  * `appliedAcceleratorTopologies` field shows the state of slice formation. For a list of valid values for this field, see Accelerator topology states in this document.




To view the `currentInstanceStatuses` and `appliedAcceleratorTopologies` fields, use one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Select the name of the MIG. A page opens with the instance group properties and a list of instances that are included in the group.

  3. Select the **Details** tab to view the group's configuration.




###  gcloud 

To view the status of a TPU slice, use the [`gcloud compute instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe). In the output look for the `currentInstanceStatuses` and `acceleratorTopologyState` fields.

  * For a zonal MIG, run the following command:
        
        gcloud compute instance-groups managed describe MIG_NAME \
            --zone=ZONE
        

  * For a regional MIG, run the following command:
        
        gcloud compute instance-groups managed describe MIG_NAME \
            --region=REGION
        




Replace the following:

  * `MIG_NAME`: the name of your MIG.
  * `ZONE`: the zone where your MIG exists.
  * `REGION`: the region where your MIG exists.



###  REST 

To view the status of a TPU slice, send a `GET` request by using one of the following methods:

  * For a zonal MIG, use the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers/get) as follows:
        
        GET https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/zones/<var>ZONE</var>/instanceGroupManagers/<var>MIG_NAME</var>
        

  * For regional MIGs, use the [`regionInstanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/get).
        
        GET https://compute.googleapis.com/compute/v1/projects/<var>PROJECT_ID</var>/regions/<var>REGION</var>/instanceGroupManagers/<var>MIG_NAME</var>
        




Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: the zone where your MIG exists.
  * `REGION`: the region where your MIG exists.
  * `MIG_NAME`: the name of your MIG.



**Example output**

The output is similar to the following.
    
    
      {
        ...
        "name": "example-mig",
        ...
        "currentActions": {
          "none": 0,
          "creating": 2,
          "creatingWithoutRetries": 0,
          "verifying": 0,
          "recreating": 0,
          "deleting": 0,
          "abandoning": 0,
          "restarting": 0,
          "refreshing": 0,
          "suspending": 0,
          "resuming": 0,
          "stopping": 0,
          "starting": 0
        },
        ...
          "bulkInstanceOperation": {
            "inProgress": true,
            "lastProgressCheck": {
              "error": {
                "errors": [
                  {
                    "code": "ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS",
                    "message": "Waiting for resources. Currently there are not enough resources available to fulfill the request."
                  }
                ]
              },
              "timestamp": "2026-03-18T18:35:32.720925Z"
            }
          },
          **"appliedAcceleratorTopologies": [
            {
              "state": "ACTIVATING"
            }
          ],
          "currentInstanceStatuses": {
            "pending": 2
          },**
        "targetSize": 2,
        "targetSizePolicy": {
          "mode": "BULK"
        },
        ...
      }
      

If the `bulkInstanceOperation.lastProgressCheck.error` field reports `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error, then it indicates that there are not enough TPU resources available in the zone to create the slice, and the MIG is waiting for resources to become available.

#### Accelerator topology states

The `acceleratorTopologyState` field indicates the current status of the TPU slice. It can have the following values:

State | Description  
---|---  
`INCOMPLETE` | The slice hasn't formed yet. The MIG target size is `0`.  
`ACTIVATING` | The slice is being formed. The MIG is provisioning the instances, and activating inter-chip connectivity (ICI). The MIG target size equals the slice size.  
`ACTIVE` | The slice is fully operational. The MIG has the required number of instances in the `RUNNING` state.  
`REACTIVATING` | The slice has failed due to an issue with the host or the inter-chip interconnect (ICI). Compute Engine attempts to reactivate the accelerator topology. The MIG target size equals the slice size and all instances are in the `REPAIRING` state. For more information about failure recovery, see [Slice availability and failure recovery](https://docs.cloud.google.com/compute/docs/tpus/tpus-and-migs#availability-recovery).  
`DEACTIVATING` | The slice is being deformed because Compute Engine is deprovisioning the instances. The MIG target size is set to `0`, and at least one instance is in a `STOPPING`, `STOPPED`, or `TERMINATED` state.  
`FAILED` | The slice has failed due to one of the following conditions depending on the provisioning model or reservation mode used.

  * **All Capacity mode reservations:**
    * A host failure. In this case, the affected instance enters the `REPAIRING` state.
    * An ICI failure. In this case, the instances remain in the `RUNNING` state.
  * **On-demand, flex-start, spot, and reservations (excluding All Capacity mode reservations):**
    * Manual deletion or stopping of an instance, including from within the operating system.
    * A Spot VM preemption.

If your slice transitions to the `FAILED` state, then you can recover it by doing one of the following:

  * Delete and recreate the MIG.
  * Resize the MIG to `0`, and then increase it to the required size.

  
  
## View details about the managed VM instances within a MIG

This section explains how to view various details about managed instances in a MIG.

### List a MIG's managed instances

To view a list of the managed instances in a group, including their states and templates, use the [console](https://console.cloud.google.com/compute/instanceGroups), the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe), or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instanceGroupManagers/get).

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instanceGroupManagers.get` on the instance group
  * `compute.instanceGroupManagers.list` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups).

If you have existing instance groups, the page lists those groups. The page also lists [unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances).

  2. Under the **Name** column of the list, click the name of the MIG that you want to examine. A page opens with the MIG properties and a list of instances that are included in the group.




###  gcloud 

Use the gcloud CLI [`list-instances`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances) sub-command.
    
    
    gcloud compute instance-groups managed list-instances instance-group \
        [--zone zone | --region region]
    

The command returns a list of instances and their details, including their current status, instance template, and last error.

The following is a sample output:
    
    
    NAME: example-mig-cmx0
    ZONE: us-central1-a
    STATUS: RUNNING
    HEALTH_STATE:
    ACTION: NONE
    INSTANCE_TEMPLATE: example-instance-template
    VERSION_NAME:
    LAST_ERROR:
    
    NAME: example-mig-qdwq
    ZONE: us-central1-b
    STATUS: PENDING
    HEALTH_STATE:
    ACTION: CREATING
    INSTANCE_TEMPLATE: example-instance-template
    VERSION_NAME:
    LAST_ERROR: Error ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS: Waiting for resources. Currently there are not enough resources available to fulfill the request.
    ...
    

If instances are in a `PENDING` state with a `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error, then it indicates that they are waiting for resources to be allocated.

###  REST 

For a zonal MIG, construct a `GET` request to the [`instanceGroupManagers.listManagedInstances` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listManagedInstances) and include the name of the MIG:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroupManagers/instance-group
    

For a regional (multiple-zone) MIG, use the [`regionInstanceGroupManagers.listManagedInstances` method](https://docs.cloud.google.com/compute/docs/reference/latest/regionInstanceGroupManagers/listManagedInstances).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/regions/region/instanceGroupManagers/instance-group
    

The response includes a list of instances and their details, including their current status and instance template.

The following is a sample response:
    
    
    {
      "managedInstances": [
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances/example-mig-cmx0",
          "instanceStatus": "RUNNING",
          "currentAction": "NONE",
          "id": "2605978238927153426",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-instance-template"
          },
          "name": "example-mig-cmx0"
        },
        {
          "instance": "https://www.googleapis.com/compute/v1/projects/example-project/zones/us-central1-b/instances/example-mig-qdwq",
          "instanceStatus": "PENDING",
          "currentAction": "CREATING",
          "lastAttempt": {
            "errors": {
              "errors": [
                {
                  "code": "ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS",
                  "message": "Waiting for resources. Currently there are not enough resources available to fulfill the request."
                }
              ]
            }
          }
          "id": "334721596325800210",
          "version": {
            "instanceTemplate": "https://www.googleapis.com/compute/v1/projects/example-project/global/instanceTemplates/example-instance-template"
          },
    
          "name": "example-mig-qdwq"
        }
      ]
    }
    

If instances are in a `PENDING` state with a `ZONE_RESOURCE_POOL_EXHAUSTED_WITH_DETAILS` error, then it indicates that they are waiting for resources to be allocated.

### Check the status of managed instances

When you create, delete, or modify instances in a MIG, the operation returns a `DONE` status after the group _schedules_ the actions. This `DONE` status doesn't mean that the instances are fully created, deleted, or updated. To confirm the instances' actual state, you must verify their status or check the group's status.

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



To check if the group as a whole is stable or is undergoing changes, see Checking the status of the group.

### Check health states

If you have configured autohealing for your MIG, you can review the health state of each VM. See [Checking health status](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#health_states).

### List instance errors

If your managed instances encountered errors, you can view those errors to diagnose and mitigate the cause.

Use the Google Cloud console, the gcloud CLI, or REST to list errors.

###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Under the **Name** column of the list, click the name of the MIG that you want to examine. A page opens with the MIG properties and a list of instances that are included in the group.

  3. Click **Errors**.




###  gcloud 

Use the [`instance-groups managed list-errors` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-errors) to list the most recent errors in the group
    
    
    gcloud compute instance-groups managed list-errors instance-group-name \
        [--zone zone | --region region]

For example:
    
    
    gcloud compute instance-groups managed list-errors example-group \
        --region us-west1
    
    
    INSTANCE_URL                                                                                        ACTION    ERROR_CODE      ERROR_MESSAGE                                                                                     TIMESTAMP                      INSTANCE_TEMPLATE                                                                                                            VERSION_NAME
    
    https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/igm-1-v0hl  CREATING  QUOTA_EXCEEDED  Instance 'igm-1-v0hl' creation failed: Quota 'CPUS' exceeded.  Limit: 1.0 in zone us-central1-a.  2019-07-11T07:44:40.156-07:00  https://www.googleapis.com/compute/v1/projects/my-project/global/instanceTemplates/instance-template-1
    https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-a/instances/igm-1-qp3d  CREATING  QUOTA_EXCEEDED  Instance 'igm-1-qp3d' creation failed: Quota 'CPUS' exceeded.  Limit: 1.0 in zone us-central1-a.  2019-07-11T07:44:40.081-07:00  https://www.googleapis.com/compute/v1/projects/my-project/global/instanceTemplates/instance-template-1
    ...
    

###  REST 

Construct a `GET` request to the `listErrors` method for a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/listErrors) or [regional MIG](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/listErrors).

For example:
    
    
    GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroupManagers/instance-group-name/listErrors&maxResults=100

The request gets a response similar to:
    
    
    {
     "items": [
      {
       "error": {
        "code": "QUOTA_EXCEEDED",
        "message": "Instance 'example-mig-m1sz' creation failed: Quota 'CPUS' exceeded.  Limit: 50.0 in zone us-central1-c."
       },
       "timestamp": "2019-01-03T18:47:28.457-08:00",
       "instanceDetails" : {
        "instance": "zones/us-central1-c/instances/example-mig-m1sz",
        "action": "CREATING",
        "version": {
         "name": "example-version-name",
         "instanceTemplate": "global/instanceTemplates/example-template",
        }
       }
      }
     ],
     ...
     "nextPageToken": "Ch0yMDE5LTA3LTI5VDExOjA4OjA2LjYxMi0wNzowMBJ5aHR0cHM6Ly93d3cuZ29vZ2xlYXBpcy5jb20vY29tcHV0ZS9zdGFnaW5nX2FscGhhL3Byb2plY3RzL215cnpha2VyZXltcy1zdGFnaW5nL3pvbmVzL3VzLWNlbnRyYWwxLWlyMS9pbnN0YW5jZXMvaWdtLTEtcXAzZA=="
    }
    
    

The `listErrors` API supports [list pagination](https://docs.cloud.google.com/apis/design/design_patterns#list_pagination). To get the next page of results, use the `nextPageToken` field from one response in a subsequent request. For example: `GET https://compute.googleapis.com/compute/v1/projects/project-id/zones/zone/instanceGroupManagers/instance-group-name/listErrors&maxResults=100&nextPageToken=next-page-token`, replacing `next-page-token` with the token that was obtained from the previous response.

The list of possible errors includes, but is not limited to, the following examples:

  * A new instance cannot be created due to: 
    * Unavailability of preemptible capacity.
    * Lack of quota, for example, for CPUs in a given region.
    * The limit on the number of VM instances was reached for the network associated with the group.
    * The disk image specified in the instance template's `properties.disks[].initializeParams.sourceImage` field was deleted, or its permissions have changed.
    * The credit card on the billing account associated with the project refused a payment.
  * An existing instance cannot be deleted because: 
    * The service account that group uses doesn't have `compute.instances.delete` permission.
    * Too many concurrent deletions were requested, exceeding rate limits.
  * An instance cannot be added to a target pool because the target pool was deleted.



After inspecting such errors, you can mitigate them. For example:

  * Move your workload to a different zone that has preemptible capacity.
  * Request a quota increase in a given region.
  * Add the `compute.instances.delete` permission to the service account used by the group.



If an action that is triggered by a MIG fails (for example, if an autoscaler encounters an error when attempting to increase the group's size), the group might immediately retry that action. If the last immediate retry attempt fails, the MIG records the error, and you can view the error by listing instance errors. After some backoff time, the group again retries the failed action. If the error persists, it might be recorded multiple times.

Compute Engine retains the most recent 500 errors for the last 8 days even if the underlying instances no longer exist or couldn't be created.

### Check if a VM instance is part of a MIG

To check if a specific VM is a member of a group, you can use the console or REST.

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click an instance to access its **VM instance details**.
  3. If the VM instance is a member of a MIG, the name of that MIG appears under the heading **In use by**. If the VM instance is not a member of a group, the heading **In use by** doesn't appear on the instance details page.



###  REST 

See [Viewing referrers to VM instances](https://docs.cloud.google.com/compute/docs/instances/view-references-between-resources).

Alternatively, to identify whether a VM is or was a member of a MIG, look for these two metadata keys in the instance's metadata:

  * `instance-template` indicates the template the VM was created from.
  * `created-by` indicates the MIG that created the VM.



Even if you [abandon](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#abandoning_instances) the instance, the VM will still have these metadata entries, unless you manually remove them.

For example, if there was a VM named `random-instance-biy` and you wanted to know whether the VM was created by a MIG, you can describe the instance and look for the metadata keys. For example:
    
    
    gcloud compute instances describe random-instance-biy \
        --zone us-central1-f
    

gcloud CLI returns a response similar to:
    
    
    canIpForward: false
    cpuPlatform: Intel Ivy Bridge
    creationTimestamp: '2016-08-24T14:11:38.012-07:00'
    ...
    metadata:
      items:
      - key: instance-template
        value: projects/123456789012/global/instanceTemplates/example-it
      - key: created-by
        value: projects/123456789012/zones/us-central1-f/instanceGroupManagers/igm-metadata
    

### View the preserved state of a managed instance

If you configured a [stateful MIG](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) and want to view the [preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/how-stateful-migs-work#preserved_state_of_a_managed_instance) of each managed instance, see [Viewing stateful configuration and preserved state](https://docs.cloud.google.com/compute/docs/instance-groups/applying-viewing-removing-stateful-config-in-migs#viewing_stateful_configuration_and_preserved_state).

## What's next

  * [Learn more about MIGs](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups).
  * [Create an instance template](https://docs.cloud.google.com/compute/docs/instance-templates) that you can use to [create a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
