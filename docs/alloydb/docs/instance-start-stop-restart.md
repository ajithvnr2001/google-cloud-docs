---
url: https://docs.cloud.google.com/alloydb/docs/instance-start-stop-restart/
title: Start, stop, or restart instances \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:28.466008+00:00
---

# Start, stop, or restart instances  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/instance-start-stop-restart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Start, stop, or restart instances Stay organized with collections  Save and categorize content based on your preferences. 

Managing instance state in AlloyDB for PostgreSQL lets you reduce compute costs during idle periods, reset database connections, or recover from transient issues. You can start, stop, or restart a primary instance or a read pool instance, and you can restart a secondary instance or individual nodes in a read pool.

These operations don't change the inbound public IP address or the Private Service Connect URI of the instance.

## Before you begin

  * The Google Cloud project you are using must be enabled to access AlloyDB.

  * You must have one of the following IAM roles in the Google Cloud project you are using:

    * (`roles/alloydb.admin`) (the AlloyDB Admin predefined IAM role)
    * (`roles/owner`) (the Owner basic IAM role)
    * (`roles/editor`) (the Editor basic IAM role)

If you don't have any of these roles, contact your Organization Administrator to request access.

  * The AlloyDB cluster is in `READY` state.




## Activation policy

When you start or stop instance, the activation policy must be set to indicate the operation you are performing. The activation policy indicates if the instance is activated to accept connection requests.

Activation policy options are:

  * `ALWAYS` \- The instance is always up and running.
  * `NEVER`\- The instance is inactive and isn't accepting connections.



To start your instance, set your activation policy to `ALWAYS`. To stop your instance and avoid instance charges, set your activation policy to `NEVER`.

## Stop an instance

You can manually stop a primary or read pool instance when needed. When you stop an instance, it remains stopped, and doesn't respond to application connections, until you start it again. You can't stop a secondary instance.

Stopping an instance temporarily halts automatic updates. The data stored in the cluster is unaffected and any backup configuration for the cluster remains active.

Stopped instances don't incur any compute charges associated with the instance. If public IP is enabled on the instance, then you incur idle static external IP charges.

**Note:** Before stopping the primary instance, you must stop any active read pool instances or cross region replication (CRR) clusters (secondary clusters). For CRR (secondary) clusters, ensure that you either promote or delete the CRR (secondary) cluster before stopping the primary instance. To stop an active read pool instance ensure that the primary instance is in `READY` state.

To stop an instance:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section and view the details about your instance.

  4. In **Stop database instance?** , click **Stop**.




The activation policy of the instance is set to `NEVER` and the instance is stopped.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to stop an instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
     --region=REGION_ID \
     --cluster=CLUSTER_ID \
     --activation-policy=NEVER
     ```
    Replace the following:

  * `INSTANCE_ID`: The ID of the instance.
  * `REGION_ID`: The instance's region ID.
  * `CLUSTER_ID`: The ID of the instance's cluster.



## Start an instance

When you start the instance, AlloyDB applies the latest minor version for the database. As starting an instance isn't a maintenance activity, any maintenance deny periods configured for the instance are ignored.

To start a stopped instance:

### Console

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page that opens, go to the **Instances in your cluster** section and view the details about your instance.

  4. In **Start database instance?** , click **Start**.




The activation policy of the instance is set to `ALWAYS` and the instance is started.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to start an instance.
    
    
    gcloud alloydb instances update INSTANCE_ID \
     --region=REGION_ID \
     --cluster=CLUSTER_ID \
     --activation-policy=ALWAYS
     ```
    Replace the following:

  * `INSTANCE_ID`: The ID of the instance.
  * `REGION_ID`: The instance's region ID.
  * `CLUSTER_ID`: The ID of the instance's cluster.



## Restart an instance

When you initiate a restart of an instance, it disrupts all connections that are available on the instance. After the instance restarts, it's ready to accept new connections. Restarting an instance doesn't change the private IP address of the instance.

### Restart a primary, secondary, or read pool instance

### Console

  1. In the Google Cloud console, go to the **Clusters** page. 

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.
  3. In the **Overview** page, go to the **Instances in your cluster** section, choose the primary or a read pool instance, and click **Restart**. 



### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Restart the instance:
    
    
    gcloud alloydb instances restart INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --project=PROJECT_ID \
        [--async]
        

  * `INSTANCE_ID`: the ID of the instance.
  * `CLUSTER_ID`: the ID of the cluster where the instance is available.
  * `REGION_ID`: the region where the instance is placed.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.
  * `--async`: an optional flag to return immediately, without waiting for the operation in progress to complete.



### Restart specific nodes of a read pool

You can use the gcloud CLI to restart one or more nodes of a read pool.

The following command shows how you can restart a node of a read pool:
    
    
    gcloud alloydb instances restart INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --node-ids=NODE_ID \
        --project=PROJECT_ID \
        [--async]

  * `INSTANCE_ID`: the ID of the read pool instance.
  * `CLUSTER_ID`: the ID of the cluster where the instance is available.
  * `REGION_ID`: the region where the instance is placed.
  * `NODE_ID`: the [ID of the node](https://docs.cloud.google.com/alloydb/docs/troubleshoot/read-pools#list-nodes) that needs a restart, for example `j71a-read-pool-054b8861-2ln8`.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.
  * `--async`: an optional flag to return immediately, without waiting for the operation in progress to complete.



The following example shows how you can restart multiple nodes:
    
    
    gcloud alloydb instances restart INSTANCE_ID \
        --cluster=CLUSTER_ID \
        --region=REGION_ID \
        --node-ids=NODE_ID1,NODE_ID2 \
        --project=PROJECT_ID \
        [--async]

  * `INSTANCE_ID`: the ID of the read pool instance.
  * `CLUSTER_ID`: the ID of the cluster where the instance is available.
  * `REGION_ID`: the region where the instance is placed.
  * `NODE_ID1,NODE_ID2`: the list of nodes that need a restart.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.
  * `--async`: an optional flag to return immediately, without waiting for the operation in progress to complete.



## What's next

  * Learn about [creating a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create)
  * Update [Cluster and instance settings](https://docs.cloud.google.com/alloydb/docs/reference/cluster-settings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
