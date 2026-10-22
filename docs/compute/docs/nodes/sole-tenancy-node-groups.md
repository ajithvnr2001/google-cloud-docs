---
url: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups/
title: Create sole-tenant node groups \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:07.079319+00:00
---

# Create sole-tenant node groups  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create sole-tenant node groups Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes how to create and delete sole-tenant node groups. If you haven't [created a sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates) yet, you must do so before you can create a node group.

Node groups are zonal resources that inherit properties from the node template they are based on. When you create a node group, you must specify configuration such as the number of nodes and maintenance settings. 

## Create a sole-tenant node group

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.nodeTemplates.use` on the node template
  * `compute.nodeGroups.create` on the project or organization



To create a sole-tenant node group, use one of the following methods:

###  Console 

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Create node group** to begin creating a node group.

  3. Specify a **Name** for the node group.

  4. Specify the **Region** for the node group to display the available node templates in that region.

  5. Specify the **Zone** within the region to create the node group in.

  6. Specify the **Node template** to create the node group or click **Create node template** to [create a new sole-tenant node template](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates#creating-a-sole-tenant-node-template). The selected node template is applied to the node group.

  7. Choose one of the following for the **Autoscaling mode** for the [node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups):

     * **Off** : Manually manage the size of the node group.

     * **On** : Have nodes automatically added to or removed from the node group.

     * **Only scale out** : Add nodes to the node group when extra capacity is required.

  8. Specify the **Number of nodes** for the group. If you enable the [node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups), specify a range for the size of the node group. You can manually change the values later.

  9. Set the **Maintenance policy** of the sole-tenant node group in the **Configure Maintenance Settings** section to one of the following values. The maintenance policy lets you configure the behavior of VMs on the node group during host maintenance events. For more information, see [Maintenance policies](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy):

     * **Default**
     * **Restart in place**
     * **Migrate within node group**
  10. You can choose between _regular maintenance windows_ and _advanced maintenance control_ to handle maintenance for your sole-tenant node group, as follows:

     * **Maintenance Window:** Select the time period during which you want planned maintenance events to happen for the nodes in the sole-tenant node groups.

     * **Opt-in for advanced maintenance control for sole-tenancy:** [Advanced maintenance control for sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in) lets you control planned maintenance events for sole-tenant node groups and minimize maintenance-related disruptions. To opt-in for advanced maintenance control, click the **Opt-in for advanced maintenance control for sole-tenancy** toggle to the _on_ position. If you choose to use this option for node maintenance, the **Maintenance window** field is disabled, and maintenance occurs as configured in advanced maintenance control.

Note that advanced maintenance control only supports the _Default_ maintenance policy.

  11. Configure the share settings by specifying one of the following in **Configure share settings** :

     * To share the node group with all projects in your organization, choose **Share this node group with all projects within the organization**.
     * To share the node group with specific projects within your organization, choose **Share this node group with selected projects within the organization**.

If you don't want to share the node group, choose **Do not share this node group with other projects**. For more information about sharing node groups, see [Share sole-tenant node groups](https://docs.cloud.google.com/compute/docs/nodes/share-node-groups).

  12. Click **Create** to finish creating the node group.




###  gcloud 

Run the [`gcloud compute sole-tenancy node-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create) command to create a node group based on a previously created node template:
    
    
    gcloud compute sole-tenancy node-groups create GROUP_NAME \
      --node-template=TEMPLATE_NAME \
      --target-size=TARGET_SIZE \
      [--zone=ZONE] \
      [--maintenance-policy=MAINTENANCE_POLICY] \
      [--maintenance-window-start-time=START_TIME] \
      [--autoscaler-mode=AUTOSCALER_MODE \
      --min-nodes=MIN_NODES \
      --max-nodes=MAX_NODES]
    

Replace the following:

  * `GROUP_NAME`: the name for the new node group.
  * `TEMPLATE_NAME`: the name of the node template to use to create this group.
  * `TARGET_SIZE`: the number of nodes to create in the group.
  * `ZONE`: the zone to create the node group in. This must be the same region as the node template on which you are basing the node group.
  * `MAINTENANCE_POLICY`: the maintenance policy for the node group. For more information, see [Maintenance policies](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy). This must be one of the following values:

    * `default`
    * `restart-in-place`
    * `migrate-within-node-group`

Alternately, you can opt in for advanced maintenance control for the sole-tenant node group, using the `--maintenance-interval` flag. For more information, see [Enable advanced maintenance control on a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in).

  * `START_TIME`: the start time in GMT for the maintenance window for the VMs in this node group. Set to one of: `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. If not set, the node group does not have a set maintenance window.

  * `AUTOSCALER_MODE`: the autoscaler policy for the node group. This must be one of:

    * `off`: manually manage the size of the node group.
    * `on`: have nodes automatically added to or removed from the node group.
    * `only-scale-out`: add nodes to the node group when extra capacity is required.
  * `MIN_NODES`: the minimum size of the node group. The default value is `0` and must be an integer value less than or equal to `MAX_NODES`.

  * `MAX_NODES`: the maximum size of the node group. This must be less than or equal to `100` and greater than or equal to `MIN_NODES`. Required if `AUTOSCALER_MODE` is not set to `off`.




###  REST 

Use the [`nodeGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/insert) to create a node group based on a previously created node template:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/nodeGroups?initialNodeCount=TARGET_SIZE
    {
      "nodeTemplate": "regions/REGION/nodeTemplates/TEMPLATE_NAME",
      "name": "GROUP_NAME",
      "maintenancePolicy": MAINTENANCE_POLICY,
      "maintenanceWindow": {
          "startTime": "START_TIME"
      },
      "autoscalingPolicy": {
          "mode": AUTOSCALER_MODE,
          "minNodes": MIN_NODES,
          "maxNodes": MAX_NODES
      },
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID.

  * `ZONE`: the zone to create the node group in. This must be in the same region as the node template on which you are basing the node group.

  * `TARGET_SIZE`: the number of nodes to create in the group.

  * `REGION`: the region to create the node group in. You must have a node template in the selected region.

  * `TEMPLATE_NAME`: the name of the node template to use to create this group.

  * `GROUP_NAME`: the name for the new node group.

  * `MAINTENANCE_POLICY`: the [maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy) for the node group. This must be one of the following values:

    * `DEFAULT`
    * `RESTART_IN_PLACE`
    * `MIGRATE_WITHIN_NODE_GROUP`

Alternately, you can opt-in for advanced maintenance control for the sole-tenant node group, using the `maintenanceInterval` field. For more information, see [Enable advanced maintenance control on a sole-tenant node](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control#opt-in).

  * `START_TIME`: the start time in GMT for the maintenance window for the VMs in this node group. Set to one of: `00:00`, `04:00`, `08:00`, `12:00`, `16:00`, or `20:00`. If not set, the node group does not have a set maintenance window.

  * `AUTOSCALER_MODE`: the autoscaler policy for the node group. This must be one of the following values:

    * `OFF`: manually manage the size of the node group.
    * `ON`: have nodes automatically added to or removed from the node group.
    * `ONLY_SCALE_OUT`: add nodes to the node group when extra capacity is required.
  * `MIN_NODES`: the minimum size of the node group. The default is `0` and must be an integer value less than or equal to `MAX_NODES`.

  * `MAX_NODES`: the maximum size of the node group. This must be less than or equal to `100` and greater than or equal to `MIN_NODES`. Required if `AUTOSCALER_MODE` is not set to `OFF`.




## Delete a node group

If you need to delete a sole-tenant node group, first remove any VMs from the node group.

###  Console 

  1. Go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click the **Name** of the node group to delete.

  3. For each node in the node group, click the node's name and delete individual VM instances on the node details page, or follow the [standard procedure to delete an individual VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance). To delete VMs in a managed instance group, [delete the managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig).

  4. After deleting all VM instances running on all nodes of the node group, return to the **Sole-tenant nodes** page.

[Go to **Sole-tenant nodes**](https://console.cloud.google.com/compute/soleTenancy)

  5. Click **Node groups**.

  6. Select the name of the node group you need to delete.

  7. Click **Delete**.




###  gcloud 

  1. List running VM instances on nodes in the node group by using the [`gcloud compute sole-tenancy node-groups list-nodes` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/list-nodes):
         
         gcloud compute sole-tenancy node-groups list-nodes GROUP_NAME \
           --zone=ZONE

Replace the following:

     * `GROUP_NAME`: name of the node group
     * `ZONE`: zone of the node group
  2. If there are any VMs running on the node group, follow the [procedure to delete an individual VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) or the [procedure to delete a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig).

  3. After deleting all VMs running on all nodes of the node group, delete the node group by using the [`gcloud compute sole-tenancy node-groups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/delete):
         
         gcloud compute sole-tenancy node-groups delete GROUP_NAME \
             --zone=ZONE

Replace the following:

     * `GROUP_NAME`: the name of the node group
     * `ZONE`: the zone of the node group



###  REST 

  1. List running VM instances on nodes in the node group by using the [`nodeGroups.listNodes` method](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/list-nodes):
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/nodeGroups/GROUP_NAME/listNodes

Replace the following:

     * `PROJECT_ID`: the project ID
     * `ZONE`: the zone of the node group
     * `GROUP_NAME`: the group for which to list the VMs
  2. If there are any VMs running on the node group, follow the [procedure to delete an individual VM](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) or the [procedure to delete a managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/delete-mig).

  3. After deleting all VMs running on all nodes of the node group, delete the node group by using the [`nodeGroups.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/delete):
         
         DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/nodeGroups/GROUP_NAME
         

Replace the following:

     * `PROJECT_ID`: the project ID
     * `ZONE`: the zone of the node group
     * `GROUP_NAME`: the name of the node group to delete



## What's next

  * [Provision VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).

  * [Delete sole-tenant node templates](https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-node-templates#deleting-node-template).



  * For information about sole-tenant node pricing, see [Sole-tenant nodes pricing](https://cloud.google.com/compute/sole-tenant-pricing).


  * For information about how to enable autoscaling on sole-tenant node groups, see [Node group autoscaler](https://docs.cloud.google.com/compute/docs/nodes/autoscaling-node-groups).

  * For more information about bringing existing licenses to Google Cloud, see [Bring existing licenses](https://docs.cloud.google.com/compute/docs/nodes/bringing-your-own-licenses).

  * For more information about sole-tenant nodes, see [Sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
