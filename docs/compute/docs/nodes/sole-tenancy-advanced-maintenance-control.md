---
url: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control/
title: Enable advanced maintenance control for sole-tenant nodes \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:39.239616+00:00
---

# Enable advanced maintenance control for sole-tenant nodes  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/nodes/sole-tenancy-advanced-maintenance-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable advanced maintenance control for sole-tenant nodes Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

Advanced maintenance control for sole-tenancy lets you control planned maintenance events for sole-tenant node groups and minimize maintenance-related disruptions. This feature is available only for sole-tenant node groups. To use this feature with your existing virtual machines, you must first move your VMs to sole-tenant node groups that have advanced maintenance control enabled.

The advanced maintenance control for sole-tenancy feature lets you:

  * Check for maintenance events scheduled for a sole-tenant node 28 days in advance.
  * Trigger maintenance immediately or schedule it for later. Note that if you trigger maintenance immediately, the maintenance takes place within 6 hours from the time you trigger the request.



The following is the process for creating a sole-tenant node group with advanced maintenance control:

  1. Opt into advanced maintenance control on compatible sole-tenancy node groups. This feature is available only for sole-tenant node groups. To use this feature with your existing VMs or sole-tenant workloads, you must first move your VMs to sole-tenant node groups with advanced maintenance control enabled.

**Note:** For a new sole-tenant node created within a node group, no maintenance event is planned for the first 28 days.
  2. Check for upcoming maintenance for your sole-tenant nodes. Maintenance for a sole-tenant node happens at most every 28 days. You can check the maintenance event for a node 28 days before the start of the 6-hour maintenance window in which maintenance is scheduled to happen for that node.

  3. If maintenance is scheduled for a sole-tenant node, and before the scheduled maintenance window begins, you can:

     * Trigger maintenance immediately, or schedule it for later. If you choose to trigger maintenance immediately, maintenance takes place within 6 hours from the time you trigger the request. Note that the scheduled date and time you choose must be before the start time of the initial maintenance window.

     * If you don't trigger maintenance immediately or schedule it for later, maintenance happens within the time provided in the initial maintenance window.




You can opt to autoscale sole-tenant node groups with advanced maintenance control enabled. Audit logs are generated in all cases.

### Supported machine families

Advanced maintenance control for sole-tenant nodes is supported for the C2, C3, C3D, C4, G2, H3, M1, M2, M3, and M4 machine families in [General Availability](https://cloud.google.com/products/#product-launch-stages).

### Limitations

The following are the limitations of the advanced maintenance control for sole-tenancy feature:

  * **Local SSDs and GPUs:** Local SSDs and GPUs are not supported by this feature.
  * **Maintenance policies** : This feature supports the default-maintenance policy (live migration). Other maintenance policies, such as, restart in place and migrate within node group are not supported.
  * **Nodes:** This feature can support a maximum of 20 nodes per project, per zone.
  * **Advanced maintenance control for existing sole-tenant node groups:** You cannot opt-in existing sole-tenant node groups for advanced maintenance control. If you want to run your existing workloads on sole-tenant node groups with advanced maintenance control enabled, you must first create a new node group with advanced maintenance control enabled and then migrate your workload into this group. Similarly, to opt out of advanced maintenance control, you must migrate your sole-tenant nodes into sole-tenant node groups that don't have advanced maintenance control enabled.
  * **Impact on current maintenance policies:** When you opt-in for this feature, it overrides any existing maintenance windows associated with the sole-tenant nodes.



## Costs

There is no additional cost for using advanced maintenance control on sole-tenant nodes.

## Before you begin

  * Before provisioning VMs on a sole-tenant node, [check your quota](https://docs.cloud.google.com/compute/quotas-limits#check_your_allocation_quota). Depending on the number and size of nodes that you reserve, you might need to [request additional quota](https://docs.cloud.google.com/compute/quotas-limits#edit_your_quota). 
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




## Enable advanced maintenance control on a sole-tenant node

Advanced maintenance control for sole-tenancy is an opt-in feature and is available only for sole-tenant node groups. To use this feature with your existing VMs or sole-tenant workloads, you must first move your VMs to sole-tenant node groups with advanced maintenance control enabled.

###  Console 

You can opt in for advanced maintenance control when you create a node group by selecting the **Opt-in for sole-tenancy advanced maintenance** option in the **Configure Maintenance Settings** section. For more information, see [Create a sole-tenant node group](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#create_a_sole-tenant_node_group).

###  gcloud 

To create a sole-tenant node group with advanced maintenance control, use the [`gcloud compute sole-tenancy node-groups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/create).

The `--maintenance-interval=RECURRENT` flag in the following command specifies that the sole-tenant node is opted-in for advanced maintenance control.
    
    
    gcloud compute sole-tenancy node-groups create NODE_GROUP_NAME \
    --node-template=NODE_TEMPLATE_NAME \
    --zone=NODE_GROUP_ZONE \
    --target-size=NODE_GROUP_SIZE \
    --maintenance-interval=RECURRENT
    

Replace the following:

  * `NODE_GROUP_NAME`: the name of the node group.

  * `NODE_TEMPLATE_NAME`: the name of the node template to use to create this group.

  * `NODE_GROUP_SIZE`: the number of nodes to create in the group.

  * `NODE_GROUP_ZONE`: the zone to create the node group in. This must be the same region as the node template on which you are basing the node group.




###  REST 

To create a sole-tenant node group with advanced maintenance control based on a previously created node template, use the [`nodeGroups.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/insert).

The `maintenanceInterval` parameter in the following command specifies that the sole-tenant node is opted-in for advanced maintenance control.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/NODE_GROUP_ZONE/nodeGroups
    {
    "name": "NODE_GROUP_NAME",
    "nodeTemplate": "NODE_TEMPLATE_URL",
    "zone": "NODE_GROUP_ZONE",
    "size": "NODE_GROUP_SIZE",
    "maintenanceInterval": "RECURRENT"
    }
    

Replace the following:

  * `PROJECT_ID`: the name of the project in which the node group exists.

  * `NODE_GROUP_ZONE`: the zone of the node group.

  * `NODE_GROUP_NAME`: the name of the node group.

  * `NODE_TEMPLATE_URL`: the URL of the node template to use to create this group.

  * `NODE_GROUP_SIZE`: the number of nodes to create in the group.




The node-level flag overrides any VM flags previously assigned. Hence, opting into advanced maintenance control overrides any prior maintenance flags.

## Check for upcoming maintenance

Maintenance for a sole-tenant node happens at most every 28 days. You can check the maintenance event for a node 28 days before the start of the 6-hour maintenance window, in which maintenance is scheduled to happen for that node.

###  Console 

After you opt-in a sole-tenant node group for advanced maintenance control, you will see upcoming maintenance events in the following way:

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node groups** to see a list of sole-tenant node groups.

  3. For any sole-tenant node group, you can see the **Maintenance Status** and **Maintenance Time** columns in the table for upcoming maintenance. As maintenance is set at the node-level, the maintenance information you see here is the next maintenance scheduled for any of the nodes within the node-group.

  4. To see maintenance information for each node in a sole-tenant node group, click the **Name** of the node group to open the details page. For each node in the node-group, the **Maintenance Status** and **Maintenance Time** columns in the table displays upcoming maintenance information.




###  gcloud 

To list the nodes of a sole-tenant node group with advanced maintenance control along with their maintenance information, use the [`gcloud compute sole-tenancy node-groups list-nodes` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/list-nodes).
    
    
    gcloud compute sole-tenancy node-groups list-nodes NODE_GROUP_NAME \
    --format "table(name, status, node_type, instances, server_id, upcoming_maintenance)"
    

Replace `NODE_GROUP_NAME` with the name of the node group.

###  REST 

To list the nodes of a sole-tenant node group with advanced maintenance control along with their maintenance information, use the [`nodeGroups.listNodes` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/listNodes).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/NODE_GROUP_ZONE/nodeGroups/NODE_GROUP_ID/listNodes
    

Replace the following:

  * `PROJECT_ID`: the name of the project in which the node group exists.

  * `NODE_GROUP_ZONE`: the zone of the node group.

  * `NODE_GROUP_ID`: the ID of the node group.




The following is the response of the [`nodeGroups.listNodes` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/listNodes):
    
    
    {
      …
      "items": [
        …
        {
          "name": string,
          "status": string,
          …
          "upcomingMaintenance": {
            "canReschedule": boolean,
            "maintenanceType": enum, // SCHEDULED | UNSCHEDULED
            "windowStartTime": string, // RFC 3339 timestamp string
            "windowEndTime": string, // RFC 3339 timestamp string
            "latestWindowStartTime": string, // RFC 3339 timestamp string
            "maintenanceStatus": enum // PENDING | ONGOING
          },
          …
        },
        …
      ],
      …
    }
    

The following are the details of the maintenance event for the node group:

Parameter name | Description  
---|---  
`windowStartTime` | Start time of the maintenance window.  
`windowEndTime` | End time of the maintenance window.  
`latestWindowStartTime` | Start time of the initial maintenance window. You can choose to trigger maintenance immediately, or schedule it for a later date and time only before the `latestWindowStartTime`.   
`maintenanceType` | The type of maintenance that will be performed:  
\- **Scheduled** : Maintenance is scheduled for this node.  
\- **Unscheduled** : Maintenance represents critical updates for which much less notice is given.   
`canReschedule` | Whether the maintenance can be rescheduled.  
`maintenanceStatus` | The current maintenance operation's status:  
\- **Pending** : The maintenance operation has not yet started, but is scheduled.  
\- **Ongoing** : The maintenance window has started.  
  
If you don't see any maintenance event, it means that there is no upcoming maintenance for any nodes in the node group.

## Trigger maintenance immediately or schedule maintenance for a node

After you know which nodes in a sole-tenant node group are scheduled for maintenance, you can do one of the following:

  * Trigger maintenance immediately. If you choose to trigger maintenance immediately, maintenance takes place within 6 hours from the time you trigger the request.

  * Schedule maintenance for later based on your requirements.




If you don't trigger maintenance immediately or schedule it for a later date and time, maintenance occurs within the initial maintenance window. Once maintenance for a node begins, you cannot pause or reschedule it.

###  Console 

**To trigger maintenance for a node immediately** , do the following:

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node groups**.

  3. Click the **name** of the node group to open the details page.

  4. Select the node for which you want to trigger maintenance immediately and click **Start Now**.




You will see a confirmation message and maintenance takes place within 6 hours from the time you trigger the request.

**To schedule maintenance for a node** , do the following:

  1. In the Google Cloud console, go to the **Sole-tenant nodes** page.

[Go to Sole-tenant nodes](https://console.cloud.google.com/compute/soleTenancy)

  2. Click **Node groups** to see a list of sole-tenant node groups.

  3. Click the **Name** of the node group to open the details page.

  4. Select the node for which you want to schedule maintenance and click **Schedule Maintenance**.

  5. In the **Schedule Maintenance** pane that is displayed, select a date and time of your choice for maintenance. Note that you can schedule maintenance for a node anytime before the start time of the initial maintenance window.




You will see a confirmation message and maintenance takes place within 6 hours from the time of triggering the request.

###  gcloud 

To start or schedule maintenance for a sole-tenant node with advanced maintenance control, use the [`gcloud compute sole-tenancy node-groups perform-maintenance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/perform-maintenance) .
    
    
    gcloud compute sole-tenancy node-groups perform-maintenance NODE_GROUP_NAME \
    --zone=NODE_GROUP_ZONE \
    --nodes=NODE_NAMES \
    --window-start-time=WINDOW_START_TIME
    

Replace the following:

  * `NODE_GROUP_NAME`: the name of the node group.

  * `NODE_GROUP_ZONE`: the zone of the node group.

  * `NODE_NAMES`: the name for the node for which you want to perform maintenance.

  * `WINDOW_START_TIME`: start date and time of the maintenance. If you want the maintenance to start as soon as possible, omit this flag.




###  REST 

Use the [`nodeGroups.performMaintenance` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/performMaintenance) to start or schedule maintenance for a sole-tenant node with advanced maintenance control.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/NODE_GROUP_ZONE/nodeGroups/NODE_GROUP_NAME/performMaintenance
    
    {
    "nodes": [
      "NODE_NAME"
    ],
    "startTime": "START_TIME"
    }
    

Replace the following:

  * `PROJECT_ID`: the name of the project in which the node group exists.

  * `NODE_GROUP_ZONE`: the zone of the node group.

  * `NODE_GROUP_NAME`: the name of the node group.

  * `NODE_NAME`: the name of the node on which you want to perform maintenance. You must specify at least one node.

  * `START_TIME`: optional: the start date and time of the maintenance, formatted as an RFC 3339 timestamp. If omitted, maintenance starts as soon as possible.




The **Maintenance Status** field of a node displays the following status during the maintenance process:

  * **Pending:** The maintenance operation has not yet started, but is scheduled.
  * **Ongoing** : The maintenance window has started. The maintenance event remains **Ongoing** until the maintenance is successfully completed for the node.



### Check if maintenance is complete

To query the maintenance status of a node with advanced maintenance control, use the [`gcloud compute sole-tenancy node-groups list-nodes` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/list-nodes) or the[`nodeGroups.listNodes` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/listNodes).

For more information, see check maintenance status.

  * **Maintenance is successful:** If the maintenance of a sole-tenant node is successful, the maintenance notification is removed. When you query the node group name, the `upcomingMaintenance` section will no longer be present for the node.
  * **Maintenance has failed:** If maintenance fails to complete in the 6-hour time window, the maintenance event remains **Ongoing** until the maintenance is successfully completed for the node. Upon successful completion, the maintenance notification is removed.



Sometimes, the maintenance trigger request for the date and time of your choice might be rejected if Google Cloud internal limits on advanced maintenance control for sole-tenancy nodes have exceeded for the specified date and time. In this case, you must select another date and time for the maintenance of the node. **Maintenance Status** for this node is **Ongoing** and remains so until maintenance is successfully completed.

### Change scheduled maintenance date and time

You can modify the scheduled maintenance date and time for a sole-tenancy node using the same procedure that you use to trigger or schedule maintenance for a node.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
