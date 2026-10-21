---
url: https://docs.cloud.google.com/compute/vm-manager/docs/patch/monitor-patch-jobs/
title: Monitor patch jobs \u00a0|\u00a0 VM Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:18.849970+00:00
---

# Monitor patch jobs  |  VM Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/patch/monitor-patch-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Monitor patch jobs Stay organized with collections  Save and categorize content based on your preferences. 

After you [create a patch job](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job), you can use Cloud Monitoring to set up alerts that you can use to monitor the patching process.

When a patch job is created, VM Manager posts the aggregate VM state to the Cloud Monitoring API. This state is posted every minute after the patch job is started. The posting of the state stops 15 minutes after the patch job completes.

To monitor your patch jobs by using alerts complete the following steps:

  1. Start a patch job. See [Creating patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  2. Set up metrics in Cloud Monitoring for your patch job.
  3. Create patch alerts.



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




## Set up metrics

In this section, you set up tracking metrics for your patch job using Metrics Explorer. For more detailed information about using the Metrics Explorer, see [Selecting metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).

You can use Cloud Monitoring to track resources across multiple projects. To see metrics for patch jobs that are in separate projects, add your projects to the same monitoring workspace. For more information, see [View metrics for multiple projects](https://docs.cloud.google.com/monitoring/settings/multiple-projects)

  1. In the Google Cloud console, go to the **Cloud Monitoring > Metrics Explorer** page.

[Go to the Metrics Explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Select a metric** section, select **Patch Job**.

  3. Select the **Patch** active metric category list, and then select **VM instance patch state**.

  4. Click **Apply**.

  5. Review the metrics.

  6. Optional. Create a chart. For more information, see [Creating a chart with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).




## Create patch alerts

In Cloud Monitoring, you can set up an alerting policy that provides notifications of the patch state so that you can resolve these issues in a timely manner. For more information about alerting, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

### VM instance patch states

To create the alert for patch jobs, use the VM instance patch state as the filter condition for the alert. The following VM instance patch states are available:

  * `ACKED`: The OS Config agent received the patch notification, but has not started patching yet.
  * `APPLYING_PATCHES`: The OS Config agent is applying patches to the VM.
  * `DOWNLOADING_PATCHES`: The OS Config agent is downloading patches to the VM.
  * `FAILED`: The patch job failed.
  * `INACTIVE`: The VM is not running.
  * `NO_AGENT_DETECTED`: The Patch service is unable to communicate with the OS Config agent on the VM. Ensure your VMs are properly connected. For more information, see [Setting up VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/setup#overview).
  * `NOTIFIED`: The OS Config agent on the VM is notified, but the patch job has not started.
  * `PATCH_STATE_UNSPECIFIED`: The state of the patch job is unknown.
  * `PENDING`: The VM hasn't received a patch task as yet. This happens because either the patch job has recently started or the VM is awaiting a gradual rollout.
  * `REBOOTING`: The VM is rebooting.
  * `RUNNING_PRE_PATCH_STEP`: The OS Config agent is running pre-patch steps.
  * `RUNNING_POST_PATCH_STEP`: The OS Config agent is running post-patch steps.
  * `SKIPPED`: Instance patching was skipped, for example, if the VM's operating system does not support patching (such as Container-Optimized OS). Patching is also skipped if the VM is part of a managed instance group (MIG) and if you've not [enabled patching MIG instances](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job#patching-options-mig-unpatchable-vms) for the patch job.
  * `STARTED`: The patch job has started on the VM.
  * `SUCCEEDED`: The patch job completed successfully.
  * `SUCCEEDED_REBOOT_REQUIRED`: The patch job completed successfully but a VM reboot is required.
  * `TIMED_OUT`: The patching process timed out.



## Example patch alert

The following example creates a patch alert that notifies you if there are more than five failed VMs in a recent patch job.

You can create alerts by using either the Google Cloud console or the Cloud Monitoring API. The following example uses the Google Cloud console. For detailed information about creating an alert using the Google Cloud console, see [Creating an alerting policy](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy).

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation pane, click **Alerting**.

  3. Click **Create Policy**.

  4. Click **Add Condition**.

     1. In the **Resource type** drop-down, select **Patch Job**.
     2. In the **Metric** drop-down, select **VM instance patch state**.
     3. In the **Filter** field, specify `state=FAILED`.
     4. In the **Configuration** section set `Any time series violate = 5.`
     5. Click **Add**. 

![Setup patch alert.](https://docs.cloud.google.com/static/compute/images/manage-os/set_alerts.png)

  5. Click **Next** to advance to the notifications section.

     1. Set up notification channels.
  6. Click **Next** to advance to the documentation section.

     1. Set up an alert policy name
     2. Provide fix instructions
  7. Click **Save**.




## What's next?

  * Learn more about [Patch](https://docs.cloud.google.com/compute/vm-manager/docs/patch).
  * [Manage your patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/manage-patch-jobs).
  * [Schedule patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/schedule-patch-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
