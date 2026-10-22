---
url: https://docs.cloud.google.com/compute/docs/disks/create-alert-snapshot-schedule/
title: Configure alerts for scheduled snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:16.561285+00:00
---

# Configure alerts for scheduled snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/create-alert-snapshot-schedule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Configure alerts for scheduled snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You can [create a custom metric](https://docs.cloud.google.com/monitoring/custom-metrics) to raise alerts or provide information to troubleshoot problems with scheduled snapshots.

For example, to set up an alert for scheduled snapshot failures, use the following procedure:

  1. Create a custom query to capture scheduled snapshot events.
  2. Create a metric based off of the query that counts scheduled snapshot failures.
  3. Create an alert policy to send an alert when there is a scheduled snapshot failure.



## Before you begin

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




### Required roles and permissions

To get the permissions that you need to create a snapshot schedule, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a custom query

To capture scheduled snapshot events, create a custom query in **Logs explorer**.

  1. In the Google Cloud console, go to the **Logging > Logs Explorer** page.

[Go to the Logs Explorer page](https://console.cloud.google.com/logs/query)

  2. If the query editor isn't visible at the top of the page, click the **Show query** toggle.

  3. Enter the following text in the query editor, replacing `PROJECT_ID` with your project ID:
         
         resource.type="gce_disk"
         logName="projects/PROJECT_ID/logs/cloudaudit.googleapis.com%2Fsystem_event"
         protoPayload.methodName="ScheduledSnapshots"
         severity>"INFO"
         

  4. Click **Run query**.




## Create a metric

After you create the custom query, create a metric that counts scheduled snapshot failures.

  1. At the top of the results table on the **Logs Explorer** page, click the **Actions** drop-down.
  2. Select **Create metric**.
  3. In the **Create log-based metric** window, provide the following details:

     * **Metric type** : `Counter`
     * **Log-based metric name** : `scheduled_snapshot_failure_count`
     * **Description** : `count of scheduled snapshot failures`

The **Filter selection** section is automatically populated with the query from the previous step.

  4. Under **Labels** , click **Add label** and enter the following:

     * **Label name** : `status`
     * **Description** : `status of scheduled snapshot request`
     * **Label type** : `STRING`
     * **Field name** : `protoPayload.response.status`
  5. Click **Done**.

  6. Click **Create Metric**.




## Create an alert policy

After you create the metric, create an alert policy to send an alert when there's a scheduled snapshot failure.

  1. In the Google Cloud console, go to the **Cloud Logging > Log-based metrics** page.

[Go to the Log-based metrics page](https://console.cloud.google.com/logs/metrics)

  2. In the **User-defined Metrics** section, find your new metric named `scheduled_snapshot_failure_count`.

  3. Click the more_vert **More** menu button in this row and select **Create alert from metric**.

The **Create alerting policy** page opens.

  4. In the **New condition** tab, configure your alert signal:

  5. Set the **Rolling window** to `5 minutes` or your preferred interval.

  6. For **Rolling window function** , select `Sum`.

Click **Next**.

  7. In the **Configure trigger** tab, enter the following:

     1. **Condition type** : `Threshold`
     2. **Alert trigger** : `Any time series violates`
     3. **Threshold position** : `Above threshold`
     4. **Threshold value** : `0`

Setting **Threshold value** to `0` triggers an alert if _any_ snapshot failure occurs. You can modify this value as your workload requires.

     5. **Condition name** : `Snapshot failure threshold exceeded`

Click **Next**.

  8. In the **Notifications and name** tab, set your **Alert policy name**. Optionally, you can add notification channels and documentation for this policy.

Click **Next**.

  9. Review your alert.

  10. Click **Create Policy**.




To learn more about creating alert policies, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

## What's next

  * Learn about snapshot schedule frequencies, retention policies, and naming rules in [About snapshot schedules for disks](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).
  * Learn about [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).
  * Learn how to [create scheduled snapshots for disks](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).
  * Learn how to [view logs](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
  * Learn more about [alerting](https://docs.cloud.google.com/monitoring/alerts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
