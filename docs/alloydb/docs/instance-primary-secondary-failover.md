---
url: https://docs.cloud.google.com/alloydb/docs/instance-primary-secondary-failover/
title: Fail over a primary or secondary instance manually \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:17.084788+00:00
---

# Fail over a primary or secondary instance manually  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-primary-secondary-failover/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Fail over a primary or secondary instance manually Stay organized with collections  Save and categorize content based on your preferences. 

To test application resilience, rebalance zones, or recover from node-level performance issues, you can manually fail over an AlloyDB for PostgreSQL primary or secondary instance to its standby node within the same region.

Common use cases for triggering a manual failover include:

  * Zone rebalancing: Swapping the nodes back to their preferred zones after an automatic failover moved the active node to the standby zone.
  * Troubleshooting: Failing over to the standby node if the active node experiences performance issues that don't trigger an automatic failover.
  * Controlled maintenance: Initiating the failover manually before a maintenance window to control when the brief connection interruption occurs.

**Note:** To promote a secondary cluster to primary and automatically recreate the original primary as a secondary across regions, see [Perform a cross-region failover](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#promote-secondary-cluster).

## High availability on primary and secondary instances

AlloyDB for PostgreSQL supports high availability on both primary and secondary instances.

### High availability on primary instances

To help ensure high availability (HA), every AlloyDB primary instance has both an active node and a standby node, which are located in different zones. If the active node becomes unavailable, then AlloyDB automatically _fails over_ the primary instance to its standby node, making it the new active node.

You can manually fail over your primary instance to its standby node at any time, even if the active node is working as expected. When you initiate a manual failover, AlloyDB does the following:

  1. Takes the primary node offline.

  2. Turns the standby node into the new active node.

  3. Reactivates the previous active node as the new standby node.




Manual failover swaps the active and standby roles of the nodes of your primary instance. You can trigger a manual failover any time that you want this exchange to occur.

For example, imagine that you have a primary instance whose active and standby nodes reside in the `us-central1-a` and `us-central1-b` zones, respectively. An outage in `us-central1-a` triggers an automatic failover, resulting in the `us-central1-b` zone hosting the active node. If you prefer to keep the active node in the `us-central1-a` zone, then you can initiate a manual failover to cause AlloyDB to swap the primary instance nodes back to their pre-outage locations.

During maintenance operations, an HA primary instance and a basic instance typically experience minimal maintenance downtime of less than a second. Because manual failover is an intentional and controlled procedure, it isn't intended for simulating unexpected hardware or network faults. Instead, you can [test high availability for your primary instance by using fault injection](https://docs.cloud.google.com/alloydb/docs/test-high-availability).

### High availability on secondary instances

AlloyDB offers HA on secondary instances to support disaster recovery and to reduce downtime when a secondary instance becomes unavailable.

By default, HA is configured on a secondary instance.

An AlloyDB secondary instance includes the following nodes: 

  * An active secondary node, which responds to requests
  * A standby secondary node



The active and standby nodes are located in two different zones in a region. If AlloyDB detects unavailability of the active node, the active node fails over to the standby node to act as the new active node. Your data is then rerouted to the new active node. This process is called a _failover_.

## Before you begin

  * The Google Cloud project you are using must have been [enabled to access AlloyDB](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin). 
  * You must have one of these IAM roles in the Google Cloud project you are using: 
    * `roles/alloydb.admin` (the AlloyDB Admin predefined IAM role)
    * `roles/owner` (the Owner basic IAM role)
    * `roles/editor` (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.




## Perform a manual failover on a primary instance

**Note:** This procedure doesn't apply to [basic instances](https://docs.cloud.google.com/alloydb/docs/basic-instance), which don't have a standby node to failover to.

###  Console 

  1. Go to the **Clusters** page.



[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  1. In the **Resource Name** column, click a cluster name.

  2. In the **Instances in your cluster** section, open your primary instance's more_vert **Instance actions menu**.

  3. Click **Failover**.

  4. In the dialog that appears, enter the instance's ID.

  5. Click **Trigger failover**.




###  gcloud 

Run the [`gcloud alloydb instances failover`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover) command:
    
    
    gcloud alloydb instances failover INSTANCE_ID \
        --region=REGION_ID \
        --cluster=CLUSTER_ID \
        --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: The ID of the instance.
  * `REGION_ID`: The region where the instance is placed.
  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.
  * `PROJECT_ID`: The ID of the project where the cluster is placed.



To confirm that the failover worked, follow these steps:

  1. Before performing the failover, [note the zones of the primary instance's nodes](https://docs.cloud.google.com/alloydb/docs/instance-view#zones).

  2. After running the failover, note the two nodes' new zones.

  3. Confirm that the zones of the active and standby nodes have switched places.




## Perform a manual failover on a secondary instance

Failing over a secondary instance manually is similar to the steps followed for failing over the primary instance manually.

To fail over a secondary cluster manually, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the name of a secondary cluster in the **Resource Name** column.

  3. On the **Overview** page, go to the **Instances in your cluster** section, choose the secondary instance, and click **Failover**.

  4. In the dialog that appears, enter the instance's ID, and click **Trigger failover**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances failover`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/failover) command to force a secondary instance to fail over its standby.
    
    
     gcloud alloydb instances failover SECONDARY_INSTANCE_ID \
     --cluster=SECONDARY_CLUSTER_ID \
     --region=REGION_ID \
     --project=PROJECT_ID

Replace the following:

  * `SECONDARY_INSTANCE_ID`: The ID of the secondary instance that you want to fail over.
  * `SECONDARY_CLUSTER_ID`: The ID of the secondary cluster that the secondary instance is associated with.
  * `REGION_ID`: The ID of the secondary instance's region—for example, `us-central1`.
  * `PROJECT_ID`: The ID of the secondary cluster's project.



## What's next

  * [Work with cross-region replication](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
