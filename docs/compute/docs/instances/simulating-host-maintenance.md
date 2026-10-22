---
url: https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance/
title: Simulate a host maintenance event \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:58.264665+00:00
---

# Simulate a host maintenance event  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/simulating-host-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Simulate a host maintenance event Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes how to test the effects of your Compute Engine instance's [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) on your applications.

You might simulate a maintenance event on your VMs to test the following:

  * The effects of [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration-process) on your applications.
  * How your applications and batch jobs handle preemption and shutdown when using one or more [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).
  * How your applications handle the shutdown and restart process for instances that are configured to [terminate and restart](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#terminate_and_optionally_restart) during maintenance events rather than live migrate.
  * How workloads that are running on [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) behave during a host maintenance event, and see the effects of the sole-tenant VM's [host maintenance policy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy) on the applications running on the VMs.



If you try to simulate a host maintenance event on an instance that [doesn't support live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration#limitations), the instance is either terminated or restarted, depending on the configured [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-options).

## Before you begin

  * Review the [regional API rate limit](https://cloud.google.com/compute/api-quota#api-rate-limits-regional) for `SimulateMaintenanceEventRequestsPerMinutePerProjectPerRegion`. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

  * To correctly simulate a maintenance event on a sole-tenant node group that has a host maintenance policy set to [migrate within node group](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#migrate_within_node_group_host_maintenance_policy), you need to trigger the maintenance event sequentially on each node.
  * For a sole-tenant node group, when you try to simulate a host maintenance event and the node group has a host maintenance policy set to migrate within the node group: 
    * If the number of nodes specified is less than or equal to the total number of holdback nodes that are reserved, then the host maintenance event simulation runs for all the specified nodes simultaneously.
    * If the number of nodes specified is greater than the total number of reserved holdback nodes, then the simulation fails.
  * The number of maintenance event simulations you can start per minute per region is limited by the [API rate limit](https://docs.cloud.google.com/compute/api-quota) for the `simulate_maintenance_event_requests_per_region` metric.



## Simulate host maintenance events to test live migration

You can simulate a maintenance event for a compute instance by using either the Google Cloud CLI or an API request. This simulated event includes the different maintenance activities that occur in a regular maintenance event. This lets you observe the end-to-end process and test any automation that you might have implemented.

During the simulation of host maintenance event for an instance that uses live migration, the `maintenance-event` metadata key of the instance goes through the following changes:

  1. At the start of the simulation, the value of the `maintenance-event` metadata key changes from `NONE` to `MIGRATE_ON_HOST_MAINTENANCE`.
  2. Throughout the duration of the simulation event, the value remains as `MIGRATE_ON_HOST_MAINTENANCE`.
  3. After the simulation ends, the value returns to `NONE`.



To query the maintenance event key, see [Query the maintenance event metadata key](https://docs.cloud.google.com/compute/docs/metadata/getting-live-migration-notice#query_the_maintenance_event_metadata_key).

###  gcloud 

Use the [`compute instances simulate-maintenance-event` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event) to simulate a maintenance event for an instance and test its configured host maintenance policy settings:
    
    
    gcloud compute instances simulate-maintenance-event INSTANCE_NAME \
        --zone=ZONE --with-extended-notifications=True
    

Replace the following:

  * `INSTANCE_NAME`: the name of the compute instance where you want to simulate the maintenance event.

You can specify multiple instance names separated by single spaces to simulate maintenance events on more than one instance in the same zone. For example, `instance-1 instance-2 instance-3`.

  * `ZONE`: the zone where the instance is located.




###  REST 

Construct a `POST` request to the [`compute.instances.simulateMaintenanceEvent` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/simulateMaintenanceEvent):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/simulateMaintenanceEvent
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `INSTANCE_NAME`: the name of the instance for which you want to simulate the maintenance event.
  * `ZONE`: the zone where the instance is located.



## Simulate host maintenance for compute instances that terminate

You can simulate a maintenance event for a compute instance by using either the Google Cloud CLI or an API request. This simulated event includes the different maintenance activities that occur in a regular maintenance event. This lets you observe the end-to-end process and test any automation that you might have implemented.

Additionally, by using the parameter `--with-extended-notifications` with a [supported machine type](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event#limitations) you can test manually starting host maintenance during the simulated event.

###  gcloud 

  1. Use the [`compute instances simulate-maintenance-event` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/simulate-maintenance-event) to simulate a maintenance event for an instance and test its configured host maintenance policy settings. You can optionally include the `--with-extended-notifications` flag.
         
         gcloud compute instances simulate-maintenance-event INSTANCE_NAME \
            --zone=ZONE --with-extended-notifications=True
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance where you want to simulate the maintenance event.

You can specify multiple instance names separated by single spaces to simulate maintenance events on more than one instance in the same zone. For example, `instance-1 instance-2 instance-3`.

     * `ZONE`: the zone where the instance is located.

  2. Optional: To manually start the simulated maintenance event, use the [`compute instances perform-maintenance` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/perform-maintenance).
         
         gcloud compute instances perform-maintenance INSTANCE_NAME \
            --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance where you want to simulate the maintenance event.

You can specify multiple instance names separated by single spaces to simulate maintenance events on more than one instance in the same zone. For example, `instance-1 instance-2 instance-3`.

     * `ZONE`: the zone where the instances are located.




###  REST 

  1. Construct a `POST` request to the [`compute.instances.simulateMaintenanceEvent` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/simulateMaintenanceEvent). You can optionally include the query parameter `withExtendedNotifications`.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/simulateMaintenanceEvent?withExtendedNotifications=True
         

Replace the following:

     * `PROJECT_ID`: the project ID for this request.
     * `INSTANCE_NAME`: the name of the instance for which you want to simulate the maintenance event.
     * `ZONE`: the zone where the instance is located.
  2. Optional: To manually start the simulated maintenance event, construct a `POST` request to the [`compute.instances.performMaintenance` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/performMaintenance).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/performMaintenance
         

Replace the following:

     * `INSTANCE_NAME`: the name of the compute instance where you want to start the maintenance event.

You can specify multiple instance names separated by single spaces to perform maintenance events on more than one instance in the same zone. For example, `instance-1 instance-2 instance-3`.

     * `ZONE`: the zone where the instances are located.




## Simulate host maintenance events on sole-tenant nodes

You can simulate a host maintenance event on sole-tenant nodes using either the Google Cloud CLI or an API request. During the simulation of the host maintenance event on a sole-tenant VM, the `maintenance-event` metadata key value doesn't change and remains `NONE` throughout the simulation.

###  gcloud 

Run the [`sole-tenancy node-groups simulate-maintenance-event` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/sole-tenancy/node-groups/simulate-maintenance-event) to force sole-tenant nodes to activate their configured maintenance policy:
    
    
     gcloud compute sole-tenancy node-groups simulate-maintenance-event NODE_GROUP \
        --nodes=NODE_NAMES \
        --zone=ZONE \
        --async
    

Replace the following:

  * `NODE_GROUP`: the name of the node group where you want to simulate the maintenance event.

  * `NODE_NAMES`: the names of the nodes where you want to simulate the maintenance event. While specifying multiple node names, use comma-separated values, for example, `node-1,node-2,node-3`.

  * `ZONE`: the zone where the nodes are located.




###  REST 

Construct a `POST` request to the [`compute.nodeGroups.simulateMaintenanceEvent` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/nodeGroups/simulateMaintenanceEvent):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/nodeGroups/NODE_GROUP/simulateMaintenanceEvent
    
    {
      "nodes": [
          "NODE_NAMES"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for this request.
  * `ZONE`: the zone where the nodes are located.
  * `NODE_GROUP`: the name of the node group where you want to simulate the maintenance event.
  * `NODE_NAMES`: the names of the nodes where you want to simulate the maintenance event. Enclose the node name within double quotes, for example, `"node-1"`. And, while specifying multiple node names, use comma-separated values, for example, `"node-1","node-2","node-3"`.



## What's next

  * Learn more about [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).
  * Learn more about [host maintenance on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#host_maintenance_policy).
  * Learn more about [setting VM host maintenance policy options](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options).
  * Learn how to [view VM operations](https://docs.cloud.google.com/compute/docs/instances/viewing-compute-operations).
  * Learn more about [multi- and sole-tenancy](https://docs.cloud.google.com/compute/docs/instances/about-vm-tenancy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
