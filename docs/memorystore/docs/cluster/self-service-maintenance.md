---
url: https://docs.cloud.google.com/memorystore/docs/cluster/self-service-maintenance/
title: Self-service maintenance \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:04:14.447438+00:00
---

# Self-service maintenance  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/self-service-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Self-service maintenance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes self-service maintenance, which lets you accept a maintenance update on your cluster outside of the typical flow of scheduled maintenance. To see which vulnerabilities are addressed by each self-service maintenance update, see [Memorystore for Redis Cluster maintenance changelogs](https://docs.cloud.google.com/memorystore/docs/cluster/maintenance-changelog).

## Overview

Memorystore for Redis Cluster releases software improvements regularly, such as patches for known vulnerabilities, through new maintenance versions. Although Memorystore for Redis Cluster schedules maintenance updates once every few months to ensure that you have the latest maintenance version, you might want to use self-service maintenance if any of the following conditions apply:

  * You need an update sooner than your next scheduled maintenance event.
  * You want to stay up-to-date with CVE patches necessary for FedRAMP Compliance.



You're not required to update to the latest version manually. You can let Memorystore for Redis Cluster update your maintenance version automatically during your next scheduled maintenance event.

**Note:** You can update your cluster's maintenance version to a newer version only.

### Impact of self-service maintenance

Self-service maintenance updates have the same impact on your applications as standard maintenance updates. For more information, see [About maintenance](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance).

## View maintenance versions

You can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to view the following information about maintenance versions that are associated with your cluster:

  * The current maintenance version.
  * Available maintenance versions to which you can update your cluster.




### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster about which you want to view maintenance version information.

  3. On the **Cluster at a glance** page, scroll until the **Maintenance** card appears.

Next to the **Maintenance version** field, the current maintenance version appears. Also, if there are available maintenance versions to which you can update the cluster, then the **Update available** status appears next to the **Self-service maintenance** field. If the **No updates are available** status appears, then the cluster has the latest version.




### gcloud

To view maintenance version information about your cluster, use the [`gcloud redis clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/describe) command.
    
    
    gcloud redis clusters describe CLUSTER_ID /
    --region=REGION_NAME /
    --project=PROJECT_NAME
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster
  * REGION_NAME: the region name for the cluster
  * PROJECT_NAME: the name of the Google Cloud project that contains the cluster



The current maintenance version appears next to the `effectiveMaintenanceVersion` field. Also, the list of available maintenance versions appears next to the `availableMaintenanceVersions` field. If no versions appear, then your cluster has the latest version.

## Update your cluster to a new maintenance version

You can use either the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) to update your cluster to a newer maintenance version.

### Console

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page.

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the cluster for which you want to update the maintenance version.

  3. On the **Cluster at a glance** page, scroll until the **Maintenance** card appears.

  4. Next to the **Self-service maintenance** field, click **View and apply**.

If the **No updates are available** status appears next to this field, then the cluster has the latest version.

  5. In the **Self-service maintenance** dialog, do the following:

     1. From the **Choose maintenance version** menu, select the maintenance version to which you want to update the cluster.
     2. Click **Apply**.



### gcloud

To update the maintenance version for your cluster, use the [`gcloud redis clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/redis/clusters/update) command.
    
    
    gcloud redis clusters update CLUSTER_ID /
    --region=REGION_NAME /
    --project=PROJECT_NAME /
    --maintenance-version=MAINTENANCE_VERSION
    

Make the following replacements:

  * CLUSTER_ID: the ID of the cluster.
  * REGION_NAME: the region name for the cluster.
  * PROJECT_NAME: the name of the Google Cloud project that contains the cluster.
  * MAINTENANCE_VERSION: the maintenance version to which you want to update the cluster. To find available maintenance versions, see View maintenance versions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
