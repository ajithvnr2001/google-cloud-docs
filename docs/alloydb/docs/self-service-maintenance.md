---
url: https://docs.cloud.google.com/alloydb/docs/self-service-maintenance/
title: Perform self-service maintenance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:58.061910+00:00
---

# Perform self-service maintenance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/self-service-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Perform self-service maintenance Stay organized with collections  Save and categorize content based on your preferences. 

You can perform self-service maintenance if you need to apply the latest AlloyDB for PostgreSQL updates to your clusters as soon as possible. Updating to the latest version can unlock AlloyDB features, apply patches, and let you [set a deny period](https://docs.cloud.google.com/alloydb/docs/maintenance-windows#set-deny-maintenance-periods) to prevent disruption during sensitive time periods.

For more information, see [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance).

## Self-maintenance use cases

AlloyDB typically applies maintenance to your clusters for you, performing maintenance operations to upgrade the database software in clusters. By default, AlloyDB performs maintenance outside of regional business hours. You can optionally [set a maintenance window](https://docs.cloud.google.com/alloydb/docs/maintenance-windows) to define a preferred scheduled maintenance time and receive notifications of upcoming scheduled maintenance. For a given release and PostgreSQL version, maintenance is completed first for clusters without maintenance windows, then scheduled for clusters with maintenance windows.

You might decide to perform self-service maintenance for the following reasons:

  * Your cluster skipped maintenance. This occurs if you set up a deny period, or if your cluster was in a bootstrapping state during migration.
  * Your cluster requires an update before scheduled maintenance occurs.
  * You need to set a deny period on a cluster that isn't up to date. Clusters with instances on earlier versions don't always support setting deny periods.
  * You want to run maintenance on a customized or irregular cadence. In this case, you can set a deny period and then perform self-service maintenance when you need it. Deny periods don't block self-service maintenance.



## Resource granularity during updates

AlloyDB only supports maintenance at the cluster level. Within the cluster, AlloyDB determines the order of instance updates. AlloyDB attempts and completes maintenance for each instance independently, so it's possible for instances to be on different releases. For example, a cluster might skip maintenance on existing instances due to a deny period and then create an instance on the latest version afterwards.

## View the latest available version

See the AlloyDB [maintenance changelogs](https://docs.cloud.google.com/alloydb/docs/maintenance-changelog/overview) for the latest version. The changelog is updated after maintenance is applied to clusters in all regions. For more information about how latest versions are applied to regions, see [Latest version](https://docs.cloud.google.com/alloydb/docs/maintenance#latest-version).

## View an instance's current version

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

Viewing the version is supported only on the instance level.

  1. To view the instance's current maintenance version, run the [`gcloud alloydb instances describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/instances/describe) command:
         
         gcloud alloydb instances describe INSTANCE_ID \
         --cluster CLUSTER_ID \
         --region LOCATION_ID

Replace the following:

     * `INSTANCE_ID`: the ID of the instance you are viewing the version for.
     * `CLUSTER_ID`: the ID of the cluster where the instance is placed.
     * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.
  2. In the response, find the `maintenanceVersionName` field to see the version that the instance is running. For example:
         
         "maintenanceVersionName": "POSTGRES_16.20251015.04_00"
         

**Note:** In rare cases, if your instances are running a much earlier version, the `maintenanceVersionName` field might not be populated.



## Before you begin

To ensure maintenance and updates can create temporary replication slots for state synchronization, ensure that the total number of replication slots is at least one less than the `max_wal_senders` limit. For more information about configuring this flag, see [Configure your source instances](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade#configure-source-instances).

## Update the cluster to the latest available version

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To update the cluster to the latest version, run the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command with the `maintenance-version` flag:
    
    
    gcloud alloydb clusters update CLUSTER_ID \
    --region LOCATION_ID \
    --maintenance-version=latest

Replace the following:

  * `CLUSTER_ID`: the ID of the cluster to update to the latest version.
  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.



Example response:
    
    
    Operation ID: operation-1746645915198-63490b152e3c8-2aed1bd1-3fd73867
    Updating cluster...done.
    

###  REST v1 

This example updates this cluster to the latest version. For a complete list of parameters for this call, see [Method: projects.locations.clusters.patch](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/patch).

Before you use any of the request data, make the following replacements:

  * `CLUSTER_ID`: the cluster to update to the latest version.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.
  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.



To update your cluster to the latest version, use the following [`PATCH`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/patch) request:
    
    
    PATCH https://alloydb.googleapis.com/v1/{cluster.name=projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?update_mask=maintenance_version_selection_policy}
    

The `maintenance_version_selection_policy` query parameter specifies the version to which to update the cluster's instances.

The request JSON body looks as follows:
    
    
    {
      "maintenanceVersionSelectionPolicy": "MAINTENANCE_VERSION_SELECTION_POLICY_LATEST",
    }
    

**Note:** If the cluster is already scheduled for maintenance when you perform self-service maintenance, then upcoming maintenance is canceled when the scheduled maintenance time is reached.

## What's next

  * [Manage AlloyDB maintenance updates using a staging cluster](https://docs.cloud.google.com/alloydb/docs/manage-maintenance-updates-staging-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
