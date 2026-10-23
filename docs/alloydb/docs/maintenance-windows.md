---
url: https://docs.cloud.google.com/alloydb/docs/maintenance-windows/
title: Manage AlloyDB for PostgreSQL cluster maintenance windows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:45.108770+00:00
---

# Manage AlloyDB for PostgreSQL cluster maintenance windows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/maintenance-windows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Manage AlloyDB for PostgreSQL cluster maintenance windows Stay organized with collections  Save and categorize content based on your preferences. 

Configuring maintenance windows and deny periods lets you control when automatic updates occur on your AlloyDB for PostgreSQL clusters to avoid disruptions during peak traffic hours. Across both primary and secondary clusters, you can set, view, or clear maintenance windows, monitor upcoming scheduled maintenance events, and configure or remove deny periods. You can also opt in to email notifications for scheduled maintenance events.

For an overview of how maintenance works, see [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance). You can also learn how to [manage AlloyDB maintenance updates by using a staging cluster](https://docs.cloud.google.com/alloydb/docs/manage-maintenance-updates-staging-cluster).

## Before you begin

To ensure maintenance and updates can create temporary replication slots for state synchronization, ensure that the total number of replication slots is at least one less than the `max_wal_senders` limit. For more information about configuring this flag, see [Configure your source instances](https://docs.cloud.google.com/alloydb/docs/cluster-upgrade#configure-source-instances).

## Set a maintenance window on a cluster

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, in **Maintenance** , click **Edit**.

  4. In **Maintenance window** , select the day of the week for this maintenance window.

The default option is **Any window**. When you create a cluster, the cluster is assigned this default maintenance window.

  5. Select the hour of the day for this maintenance window.

  6. Click **Update** to save the changes.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To set a maintenance window on a cluster, run the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command with the `--maintenance-window-day` and `--maintenance-window-hour` flags:
    
    
    gcloud alloydb clusters update CLUSTER_ID \
      --region LOCATION_ID \
      --maintenance-window-day DAY_OF_WEEK \
      --maintenance-window-hour HOUR_OF_DAY

Replace the following:

  * `CLUSTER_ID`: the cluster to set the maintenance window on.

  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.

  * `DAY_OF_WEEK`: the day of the week, in the Coordinated Universal Time (UTC) time zone, for this maintenance window. Valid values are `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, and `SUNDAY`.

The default value is **Any window**. When you create a cluster, the cluster is assigned this default maintenance window.

  * `HOUR_OF_DAY`: an integer between `0` and `23` representing the hour of the day, in the UTC time zone, for this maintenance window.




If you make changes to your maintenance window setting while the cluster is already undergoing maintenance or is scheduled for maintenance, then the changes don't take effect until after the current or scheduled maintenance is complete.

**Note:** You can set a maintenance window on a new cluster while you create it. To do this, [create the cluster using the gcloud CLI](https://docs.cloud.google.com/alloydb/docs/cluster-create), adding the `--maintenance-window-day` and `--maintenance-window-hour` flags to the `gcloud alloydb clusters create` command.

## Clear a maintenance window

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, in **Maintenance** , click **Edit**.

  4. In **Maintenance window** , select **Any window**.

  5. Click **Update** to save the changes.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To clear the maintenance window from a cluster, run the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command with the `--maintenance-window-any` flag:
    
    
    gcloud alloydb clusters update CLUSTER_ID \
      --region LOCATION_ID \
      --maintenance-window-any

Replace the following:

  * `CLUSTER_ID`: the cluster to set the maintenance window on.

  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.




## View the maintenance window of a cluster

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, in **Maintenance** , view the maintenance window details for your cluster.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To review the current maintenance window on a cluster, run the [`gcloud alloydb clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/describe) command:
    
    
    gcloud alloydb clusters describe CLUSTER_ID \
      --region LOCATION_ID

Replace the following:

  * `CLUSTER_ID`: the cluster to set the maintenance window on.

  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.




If the cluster has a maintenance window set, then the output of the command includes lines that resemble the following:
    
    
    maintenanceUpdatePolicy:
      maintenanceWindows:
      - day: TUESDAY
        startTime:
          hours: 23
    

If the output doesn't include a `maintenanceUpdatePolicy` section, then the cluster has no maintenance window set.

## View upcoming maintenance on a cluster

### Console

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Locate your cluster, and view the **Maintenance** column for information about the upcoming maintenance window.




### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To see upcoming maintenance planned for a cluster that has a maintenance window set, run the [`gcloud alloydb clusters describe`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/describe) command:
    
    
    gcloud alloydb clusters describe CLUSTER_ID \
      --region LOCATION_ID

Replace the following:

  * `CLUSTER_ID`: the cluster to set the maintenance window on.

  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.




If the cluster has a planned maintenance event in its future, then the output of the command includes lines that resemble the following:
    
    
    maintenanceSchedule:
      startTime: 2024-07-03T09:46:40Z
    

The UTC-formatted timestamp specifies the moment at which AlloyDB plans to start updating the system software of all of the nodes in this cluster.

## Opt in to maintenance notifications

Maintenance notifications are disabled by default. When you choose to opt in to receive email notifications about upcoming AlloyDB maintenance events, keep the following in mind:

  * You receive an automated notification about the event as soon as it's scheduled. Maintenance events are scheduled at least one week ahead of time.
  * Maintenance notifications are enabled at the Google Cloud project level. You can't choose to be notified about a subset of clusters in a project.
  * You can only enable notifications for yourself. Each user must opt in separately to receive maintenance notifications.



For more information, see [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance).

To receive an automated email notification whenever a maintenance event is scheduled or canceled for a cluster that has a maintenance window set, follow these steps using the Google Cloud console:

  1. Go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Click a cluster in the **Resource Name** column.

  3. In the **Overview** page, in **Maintenance** , click **Edit** in the `Notifications:` row.

  4. Click **Communication**.

  5. In the row for **AlloyDB** , **Maintenance window** , select the toggle in the **Email** column.




## Configure a deny maintenance period

To prevent maintenance operations during a specific time period, you can configure a deny maintenance period. You can set deny maintenance on a cluster running the latest version of AlloyDB. A deny maintenance period can span from one to 30 days.

Clusters with instances on earlier versions don't always support setting deny periods. If you need to set a deny period on a cluster that isn't sufficiently up to date, you can [perform self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance) to update your cluster.

Existing deny periods don't block self-service maintenance.

### Set deny maintenance periods

To configure a deny maintenance period, you set its start date, end date, and the time of day the interval begins and ends.

The start and end dates must be in the following format:

  * `YYYY-MM-DD`: indicates a specific date



The start date, end date, and time are in the UTC time zone.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To add a deny maintenance period to an AlloyDB cluster, run the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command with the `--deny-maintenance-period-start-date`, `--deny-maintenance-period-end-date`, and `--deny-maintenance-period-time` flags:
    
    
    gcloud alloydb clusters update CLUSTER_ID \
       --region LOCATION_ID \
       --deny-maintenance-period-start-date START_DATE \
       --deny-maintenance-period-end-date END_DATE \
       --deny-maintenance-period-time TIME

Replace the following:

  * `CLUSTER_ID`: the cluster to configure for the maintenance-free period.
  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.
  * `START_DATE`: the maintenance-free period start date in `YYYY-MM-DD` UTC format.
  * `END_DATE`: the end of the maintenance-free period in `YYYY-MM-DD` UTC format.
  * `TIME`: the time of the maintenance-free period in `HH:MM` UTC format. The hours are represented in the 24-hour format where values range from `00:00` to `23:59`—for example, `16:45`.



###  REST v1 

This example adds a deny maintenance period to an existing cluster. For a complete list of parameters for this call, see [Method: projects.locations.clusters.patch](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/patch).

Before you use any of the request data, make the following replacements:

  * `CLUSTER_ID`: the cluster to configure for the maintenance-free period.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.
  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.
  * `START_YEAR`: the year when the maintenance-free period starts in the `YYYY` format.
  * `START_MONTH`: the month when the maintenance-free period starts in the `MM` format. A leading zero for single-digit months is optional—for example, both `2` and `02` are valid for February.
  * `START_DAY`: the day when the maintenance-free period starts in the `DD` format. A leading zero for single-digit days is optional—for example, both `1` and `01` are valid for the first day of the month.
  * `END_YEAR`: the year when the maintenance-free period ends in the `YYYY` format.
  * `END_MONTH`: the month when the maintenance-free period ends in the `MM` format.
  * `END_DAY`: the day when the maintenance-free period ends in the `DD` format.
  * `HOURS`: the maintenance-free period hour in 24-hour format—for example, `16`. A leading zero for single-digit hours is optional—for example, both `2` and `02` are valid.
  * `MINUTES`: the minute of the maintenance-free period that accepts values from `0` to `59`—for example, `45`. A leading zero for single-digit minutes is optional— `7` and `07` are valid.



To add a deny maintenance period, use the following [`PATCH`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/patch) request:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?update_mask=maintenance_update_policy.deny_maintenance_periods
    

The `maintenance_update_policy.deny_maintenance_periods` query parameter tells the API to update the `denyMaintenancePeriods` field within the `maintenanceUpdatePolicy` block.

The request JSON body looks as follows:
    
    
    {
     "maintenanceUpdatePolicy": {
       "denyMaintenancePeriods": [
         {
           "startDate": {
             "year": START_YEAR,
             "month": START_MONTH,
             "day": START_DAY
           },
           "endDate": {
             "year": END_YEAR,
             "month": END_MONTH,
             "day": END_DAY
           },
           "time": {
             "hours": HOURS,
             "minutes": MINUTES
           }
         }
       ]
     }
    }
    

### Deny upcoming maintenance

Deny maintenance periods take precedence over scheduled maintenance. If a timing conflict occurs, the deny maintenance period overrides the scheduled maintenance window.

Setting a deny period that conflicts with a scheduled maintenance event doesn't immediately cancel the maintenance and clear the schedule. AlloyDB shows the existing scheduled maintenance as [upcoming](https://docs.cloud.google.com/alloydb/docs/maintenance-windows#view-upcoming), but it cancels the scheduled maintenance window when the scheduled time starts.

To help apply critical updates, the system does not typically allow setting a deny period to skip more than one maintenance event and may in rare cases apply emergency maintenance outside of configured maintenance preferences.

## Remove a deny maintenance period from a cluster

You can remove a deny maintenance period at any time.

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

To remove a deny maintenance period from an AlloyDB cluster, run the [`gcloud alloydb clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/alloydb/clusters/update) command with the `--remove-deny-maintenance-period` flag:
    
    
    gcloud alloydb clusters update CLUSTER_ID --region LOCATION_ID  --remove-deny-maintenance-period

Replace the following:

  * `CLUSTER_ID`: the cluster to remove the deny maintenance period from.
  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.



###  REST v1 

This example removes a deny maintenance period from an AlloyDB cluster. For a complete list of parameters for this call, see [Method: projects.locations.clusters.patch](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/patch).

Before you use any of the request data, make the following replacements:

  * `CLUSTER_ID`: the ID of the cluster that you add a deny maintenance period to.
  * `PROJECT_ID`: the ID of the project where the cluster is placed.
  * `LOCATION_ID`: the Google Cloud region that this cluster is located in—for example, `us-central1`.



To remove a deny maintenance period, use the following [`PATCH`](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/patch) request:
    
    
    PATCH https://alloydb.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID?update_mask=maintenance_update_policy.deny_maintenance_periods
    

The `maintenance_update_policy.deny_maintenance_periods` query parameter tells the API to update the `denyMaintenancePeriods` field within the `maintenanceUpdatePolicy` block.

The request JSON body looks as follows:
    
    
    {}
    

## What's next

  * [Perform self-service maintenance](https://docs.cloud.google.com/alloydb/docs/self-service-maintenance).
  * [Manage AlloyDB maintenance updates using a staging cluster](https://docs.cloud.google.com/alloydb/docs/manage-maintenance-updates-staging-cluster).
  * [Learn more about AlloyDB maintenance](https://docs.cloud.google.com/alloydb/docs/maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
