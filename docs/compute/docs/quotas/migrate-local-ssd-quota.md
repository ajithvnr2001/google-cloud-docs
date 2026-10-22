---
url: https://docs.cloud.google.com/compute/docs/quotas/migrate-local-ssd-quota/
title: View and manage local SSD quota \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:16.711661+00:00
---

# View and manage local SSD quota  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/quotas/migrate-local-ssd-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)



Send feedback 

#  View and manage local SSD quota Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of the local SSD quota per machine family. It also describes how to update your monitoring dashboards, alerting policies, and queries to use the quota metric for local SSD quota per machine family.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## About the local SSD quota per machine family

[Local SSD quota](https://docs.cloud.google.com/compute/resource-usage#disk_quota) defines the total combined size of local SSD disk partitions attached to VMs in a region based on the machine type for each VM.

## Metric and limits for the local SSD quota per machine family

Compute Engine local SSD quota is migrated to use the local SSD per machine family quota metric. Use the quota metric `compute.googleapis.com/local_ssd_total_storage_per_vm_family`BETA instead of `compute.googleapis.com/local_ssd_total_storage` to view the quota usage and limits.

You can use Google Cloud console to [view your current quota values](https://docs.cloud.google.com/docs/quotas/view-manage) for the local SSD quota per machine family for each region. The limit for local SSD quota per machine family is calculated based on your existing limit and usage for local SSD quota and any submitted Quota Increase Requests (QIRs).

In the gcloud CLI and the API, this quota is referred as `LOCAL_SSD_TOTAL_GB_PER_VM_FAMILY`.

## Migrate Cloud Monitoring metrics

If you're using Cloud Monitoring to monitor the local SSD quota usage over time and to receive alerts, you must manually update the Cloud Monitoring dashboards, alerts, and queries to use the metric for local SSD quota per machine family.

### Monitor the usage of local SSD quota per machine family

To update a chart on the Cloud Monitoring dashboard to use the local SSD quota per machine family metric, do the following:

  1. In the Google Cloud console, select **Monitoring**.

  2. In the navigation pane, select **Dashboards**.

  3. Select the dashboard that you want to edit to use the per machine family quota metric for local SSD.

  4. Click **Edit dashboard**.

  5. Select the chart you want to modify and click **Edit** from the **More chart options** menu.

  6. In the **Resource & Metric** section, click **Select a metric**.

  7. Select **Compute Location > Quota > Local SSD disk per VM family (GB). quota usage**, and then click **Apply**. Alternatively, select **Local SSD disk per VM family (GB). quota limit** to create a chart to monitor the local SSD quota limit.

![Filter to select a SSD limits.](https://docs.cloud.google.com/static/compute/images/quotas/ssd-metric.png)

  8. Optional: Specify a filter criteria for the chart:

     1. Click add_box **Add filter** , and then in the **Label** menu, select one of the following options:

        * **limit_name** : to filter local SSD quota usage across all machine types in a region or a zone. Possible values are:

          * `LOCAL-SSD-TOTAL-GB-PER-VM-FAMILY-per-project-region`
          * `LOCAL-SSD-TOTAL-GB-PER-VM-FAMILY-per-project-zone`

![Filter to select a limit.](https://docs.cloud.google.com/static/compute/images/quotas/filter-limit-name.png)

        * **vm_family** : to filter local SSD quota usage for a specific machine family such as `N1`,`N2D`, and `C1`. See [Local SSDs and supported machine types](https://docs.cloud.google.com/compute/docs/disks#localssds).

![Filter to select a VM family.](https://docs.cloud.google.com/static/compute/images/quotas/filter-vm-family.png)

     2. Click **Done** to save changes.

  9. Click **Close editor**.




### Create alerting policies for local SSD quota usage per machine family

To change an alerting policy that monitors the existing local SSD quota metric, do the following:

  1. In the Google Cloud console, select **Monitoring**.

  2. In the navigation pane, select **Alerting**. The Alerting page displays panes that list summary information, incidents, and alerting policies.

  3. Click the alerting policy that you want to change to use the new metric.

  4. Click **Copy** to copy the alerting policy conditions to a new policy.

  5. Click **Select a metric** and select **Compute Location > Quota > Local SSD disk per VM family (GB). quota usage**, and then click **Apply**. Alternatively, select **Local SSD disk per VM family (GB). quota limit** to create an alerting policy for the local SSD quota limit.

![Filter to select a SSD limits.](https://docs.cloud.google.com/static/compute/images/quotas/ssd-metric.png)

  6. Optional: Edit the filter that corresponds to the metric that you want to migrate:

     1. Click add_box **Add filter** , and then in the **Label** menu, select one of the following options:

        * **limit_name** : to filter local SSD quota usage across all machine types in a region or a zone. Possible values are:

          * `LOCAL-SSD-TOTAL-GB-PER-VM-FAMILY-per-project-region`
          * `LOCAL-SSD-TOTAL-GB-PER-VM-FAMILY-per-project-zone`

![Filter to select a limit.](https://docs.cloud.google.com/static/compute/images/quotas/filter-limit-name.png)

        * **vm_family** : to filter local SSD quota usage for a specific machine family such as `N1`,`N2D`, and `C1`. See [Local SSDs and supported machine types](https://docs.cloud.google.com/compute/docs/disks#localssds).

![Filter to select a VM family.](https://docs.cloud.google.com/static/compute/images/quotas/filter-vm-family.png)

     2. Click **Done** to save changes in the filter.

  7. Click **Create policy**.




### Update Cloud Monitoring queries

To change the quota metric in an MQL-based alerting policy or a chart in a dashboard, use the Query Editor and edit the query filter. See [Using the Query Editor](https://docs.cloud.google.com/monitoring/mql/query-editor).

Open the Query Editor and edit the following query:

![MQL that uses the local SSD quota metric](https://docs.cloud.google.com/static/compute/images/quotas/mql-local-ssd-old.png)

Update the metric name and add a filter for the machine family as shown in the following example:

![MQL that uses the local SSD quota per VM family metric](https://docs.cloud.google.com/static/compute/images/quotas/mql-local-ssd.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
