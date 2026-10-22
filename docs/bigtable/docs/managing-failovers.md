---
url: https://docs.cloud.google.com/bigtable/docs/managing-failovers/
title: Manage failovers \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:43.509128+00:00
---

# Manage failovers  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/managing-failovers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage failovers

If a Bigtable cluster becomes unresponsive, replication makes it possible for incoming traffic to fail over to another cluster in the same instance. Failovers can be either manual or automatic, depending on the [app profile](https://docs.cloud.google.com/bigtable/docs/app-profiles) an application is using and how the app profile is configured. 

This page describes the steps for performing a failover between clusters.

  * If an app profile routes all requests to a single cluster, you can perform a manual failover.
  * If an app profile uses multi-cluster routing, failovers are automatic and you don't need to take any action.



Before you read this page, you should be familiar with the [overview of Bigtable replication](https://docs.cloud.google.com/bigtable/docs/replication-overview). You should also be familiar with the [routing options](https://docs.cloud.google.com/bigtable/docs/routing) that are available for Bigtable.

## Perform a manual failover

Use a manual failover if an app profile routes all requests to a single cluster and that cluster becomes unresponsive. For examples of the criteria you could use to determine that a cluster is unresponsive, see [Manual failovers](https://docs.cloud.google.com/bigtable/docs/failovers#manual). Check your instance's replication latency before you decide to fail over. For more information, see [Charts for replication](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

To perform a manual failover, update your app profile so that it routes requests to a responsive cluster instead of the unresponsive cluster:

###  Console 

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. In the **Application profiles** column, click the app profile that is routing traffic to the unresponsive cluster.

If you don't see the app profile you want to edit, you can view a complete list by clicking the name of the instance, then clicking **Application profiles** in the left pane.

  3. Under **Cluster routing** , select a responsive cluster in your instance.

**Important:** If **Any cluster (multi-cluster)** is selected, the app profile handles failovers automatically. Click **Cancel** to exit without saving.
  4. Click **Save**. A confirmation dialog appears.

  5. Carefully review the warnings in the confirmation dialog, then follow the instructions in the dialog and click **Continue**.




###  gcloud 

  1. If you don't know the instance ID, use the [`bigtable instances list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/instances/list) to view a list of your project's instances: 
         
         gcloud bigtable instances list
         

  2. If you don't know the instance's cluster IDs, use the [`bigtable clusters list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/clusters/list) to view a list of clusters in the instance: 
         
         gcloud bigtable clusters list --instances=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  3. If you don't know the app profile's ID, use the [`bigtable app-profiles list` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/list) to view a list of the instance's app profiles: 
         
         gcloud bigtable app-profiles list --instance=INSTANCE_ID
         

Replace `INSTANCE_ID` with the permanent identifier for the instance. 

  4. Use the [`bigtable app-profiles update` command](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/app-profiles/update) to change the cluster that the app profile uses:
         
         gcloud bigtable app-profiles update APP_PROFILE_ID \
             --instance=INSTANCE_ID \
             --route-to=CLUSTER_ID
         

Provide the following: 

     * `APP_PROFILE_ID`: The permanent identifier for the app profile. 
     * `INSTANCE_ID`: The permanent identifier for the instance. 
     * `CLUSTER_ID`: The cluster ID that all requests should be routed to. This flag enables [single-cluster routing](https://docs.cloud.google.com/bigtable/docs/routing#single-cluster). 

If you receive an error message, carefully review any warnings in the error message. If you want to override the error, run the command again with the `--force` flag.




Shortly after you update the app profile, any applications that use the app profile will start to direct all of their requests to the healthy cluster that you selected. The unhealthy cluster will continue using CPU to handle replication and other maintenance tasks.

After the unhealthy cluster recovers, you can follow the same steps to update your app profile so that it routes all requests to the recovered cluster.

## Perform an automatic failover

With Bigtable, automatic failovers truly are automatic. If an app profile uses multi-cluster routing, and the nearest cluster to the application server becomes unhealthy, you don't need to take any action. Bigtable automatically fails over, even if the cluster is only briefly unhealthy, and uses the nearest healthy cluster to handle requests until the unhealthy cluster has recovered.

The speed of an automatic failover depends on your request deadline. Shorter deadlines trigger faster failovers, but the deadline must still allow enough time for the request to complete on the backup cluster. For more information, see [Automatic failovers](https://docs.cloud.google.com/bigtable/docs/failovers#automatic).

To view the number of requests that were automatically rerouted over a given period of time, look at the **Automatic Failovers** graph in the Google Cloud console: open the [list of instances](https://console.cloud.google.com/bigtable/instances), click the instance name, then click **Monitoring**.

## What's next

Learn how to [monitor a Bigtable instance](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
