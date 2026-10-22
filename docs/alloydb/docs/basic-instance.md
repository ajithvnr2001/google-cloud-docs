---
url: https://docs.cloud.google.com/alloydb/docs/basic-instance/
title: Reduce costs using basic instances \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:21.622323+00:00
---

# Reduce costs using basic instances  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/basic-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Reduce costs using basic instances Stay organized with collections  Save and categorize content based on your preferences. 

By default, an AlloyDB for PostgreSQL primary instance is highly available (HA), with the ability to perform an automated failover to a standby node in the case of an outage. If your AlloyDB for PostgreSQL cluster does not require HA, then you have the option to reduce your operating costs by making the cluster's primary instance a _basic instance_ , instead of an HA one.

This page provides an overview of basic instances. It also shows you how to perform the following procedures:

  * Create a basic instance within an AlloyDB cluster.

  * Change a basic instance into an HA instance, and vice-versa.

  * Determine whether a given instance is basic or HA.




For a more general overview of AlloyDB clusters and instances, see [AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/overview).

## Overview of basic instances

A basic instance works exactly like an HA primary instance, with one key difference: it lacks a standby node. This simpler architecture makes a basic instance, also known as a _zonal instance_ , cost less to operate than an HA instance.

Because of its single node, a basic instance doesn't support automated failover. If the zone that hosts a basic instance's active node has an outage, then the instance becomes unavailable to any queries until the outage ends. This behavior is in contrast with an HA primary instance, which responds to any outage of its active node by automatically turning the instance's standby node into the new active node.

During maintenance operations, both an HA primary instance and a basic instance, typically experience minimal maintenance downtime of less than a second.

**Warning:** Avoid using basic instances in production. The uptime guarantees of the AlloyDB Service Level Agreement (SLA) apply only to HA instances, not basic instances.

Basic instances are appropriate for use in development or staging environments, which don't necessarily need to provide high availability. Google strongly recommends using only HA instances, and not basic instances, in production deployments of AlloyDB clusters. The uptime guarantees provided by the [AlloyDB SLA](https://cloud.google.com/alloydb/sla) apply only to multi-zone instances. Since basic instances consist of only one node in a single zone, we cannot guarantee high availability for basic instances.

## Create a cluster with a basic instance

### Console

Follow the procedure described in [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create), with the following modification:

After clicking **Create cluster** , select either **Basic** or **Basic with read pool(s)** as the cluster type. Then, proceed with the cluster creation process as usual.

### gcloud

Follow the procedure described in [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create), with the following modification:

When running the `gcloud alloydb instances create` command to create the new cluster's primary instance, add the argument `--availability-type=ZONAL`.

## Create a basic instance for an existing cluster

### Console

Follow the procedure described in [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create), with the following modification:

In the **Configure primary instance** pane, under **Zonal availability** , select **Single zone**.

### gcloud

Follow the procedure described in [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create), with the following modification:

When running the `gcloud alloydb instances create` command to create the primary instance, add the argument `--availability-type=ZONAL`.

## Upgrade a basic instance to an HA instance

This operation effectively brings a new node online, and sets it as the instance's standby.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the more_vert **Actions** column of the primary instance that you want to upgrade from basic to HA.

  3. Select **Edit**.

  4. In the **Edit primary instance** pane, under **Zonal availability** , select **Multiple zones (Highly available)**.

  5. Click **Update instance**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to turn a basic instance into a highly available one.
    
    
    gcloud alloydb instances update INSTANCE_ID \
    --availability-type=REGIONAL
    --region=REGION_ID \
    --cluster=CLUSTER_ID \
    --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: The ID of the instance that you are updating.

  * `REGION_ID`: The region where the instance is placed.

  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.

  * `PROJECT_ID`: The ID of the project where the cluster is placed.




## Downgrade an HA instance to a basic instance

This operation effectively takes the instance's standby node offline, leaving it with only its active node.

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click the more_vert **Actions** column of the primary instance that you want to downgrade from HA to basic.

  3. Select **Edit**.

  4. In the **Edit primary instance** pane, under **Zonal availability** , select **Single zone**.

  5. Click **Update instance**.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Use the [`gcloud alloydb instances update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/update) command to turn a basic instance into a highly available one.
    
    
    gcloud alloydb instances update INSTANCE_ID \
    --availability-type=ZONAL
    --region=REGION_ID \
    --cluster=CLUSTER_ID \
    --project=PROJECT_ID

Replace the following:

  * `INSTANCE_ID`: The ID of the instance that you are updating.

  * `REGION_ID`: The region where the instance is placed.

  * `CLUSTER_ID`: The ID of the cluster where the instance is placed.

  * `PROJECT_ID`: The ID of the project where the cluster is placed.




## Determine whether an instance is HA or basic

###  Console 

  1. Follow the procedure described in [View instance details](https://docs.cloud.google.com/alloydb/docs/instance-view).

  2. Find the **High availability** row in the instance's details table. It has one of the following values:

     * **Highly available:** This instance has more than one node across multiple zones, making it HA.

     * **No:** This instance has only one node, and is not HA.




###  gcloud 

  1. Follow the procedure described in [View instance details](https://docs.cloud.google.com/alloydb/docs/instance-view).

  2. Find the `availabilityType` line in the command output.

Its value is either `REGIONAL`, for an HA instance, or `ZONAL`, for a basic instance.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
