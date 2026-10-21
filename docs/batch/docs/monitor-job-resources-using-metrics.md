---
url: https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics/
title: Monitor and optimize job resources by viewing metrics \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:29:26.696043+00:00
---

# Monitor and optimize job resources by viewing metrics  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Monitor and optimize job resources by viewing metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to monitor and try to optimize the resources for a Batch job by viewing metrics in Cloud Monitoring. To learn more about the resources that a job runs on, see [Job resources](https://docs.cloud.google.com/batch/docs/create-run-job#resources).

For any job, Monitoring provides basic metrics such as CPU utilization and network traffic. However, some metrics, such as memory and process utilization, can only be collected if a job installs the Ops Agent. Metrics for a job's resources help you evaluate the performance and utilization of each resource. This information can help you identify improvements for any future iterations of the job. For example, you might remove unutilized resources to help optimize costs, or you might improve or increase strained resources to help enhance performance.

**Note:** Monitoring and the Ops Agent feature are not part of Batch and have their own pricing. For more information, see [Monitoring pricing](https://cloud.google.com/stackdriver/pricing#monitoring-pricing-summary) and [Ops Agent pricing](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#pricing) in the Google Cloud Observability documentation.

## Before you begin

  1. If you haven't used Batch before, review [Get started with Batch](https://docs.cloud.google.com/batch/docs/get-started) and enable Batch by completing the [prerequisites for projects and users](https://docs.cloud.google.com/batch/docs/get-started#prerequisites).
  2. Optional: To collect additional metrics for a job, [create and run a job that automatically installs the Ops Agent.](https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent)
  3. If your project hasn't already, enable the Monitoring API: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=monitoring.googleapis.com)

  4. To get the permissions that you need to view observability metrics, ask your administrator to grant you the [Monitoring Metric Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricViewer) (`roles/monitoring.metricViewer`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 




## View metrics for job resources

**Important:** You cannot view metrics after they are deleted, which happens automatically after the [Monitoring retention periods](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy). If you need to retain metrics for a longer period, [export Monitoring metrics to BigQuery](https://docs.cloud.google.com/architecture/monitoring-metric-export).

[Observe and monitor VMs](https://docs.cloud.google.com/compute/docs/instances/observe-monitor-vms) in the Compute Engine documentation provides relevant conceptual information about VM metrics; however, different methods are recommended for viewing VM metrics for Batch jobs. Specifically, the Compute Engine documentation explains how to view metrics by using the predefined Monitoring dashboards for Compute Engine or Compute Engine pages in the Google Cloud console. But, importantly, those methods don't display information about VMs that have been deleted. As a result, don't use those methods unless you only want to view metrics for Batch jobs while they are running.

View metrics for running and finished Batch jobs by using Metrics Explorer charts as explained in this section. Notably, charts are temporary unless you save them to custom dashboards.

**Tip:** To see if your project already has a custom dashboard that you can use instead of creating a new chart, [view custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards#view-dashboard).

To create a chart for viewing one or more metrics, do the following:

  1. Optional: If you plan to save the chart, [identify or create a custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) for the chart.
  2. [Create a Metrics Explorer chart for one or more metrics](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

Without filters, each VM metric in a chart includes data from all the VMs in your project. Optionally, if you want to filter the chart to only include metrics from all or specific Batch jobs, add the following filter:
         
         group=RESOURCE_GROUP_NAME
         

Replace `RESOURCE_GROUP_NAME` with the name of a resource group for Batch jobs. For more information, see Create resource groups to filter metrics in this document.




### Create resource groups to filter metrics

You can use [resource groups](https://docs.cloud.google.com/monitoring/groups) as customizable filters for Metrics Explorer charts. To create a resource group for all or specific Batch jobs in your project, do the following:

  1. Select a [label](https://docs.cloud.google.com/batch/docs/organize-resources-using-labels) to use as the membership criteria based on which jobs you want to include in the group:

     * **All Batch jobs:** Use the predefined `batch-node` label, which is automatically applied to all the resources for all Batch jobs and has a null value.
     * **Specific Batch jobs:** Use a label that is applied to the resources only for specific Batch jobs.

For example, if you want to create a group based on full or partial job names, use the predefined `batch-job-id` label name with a specific value. The `batch-job-id` label is automatically applied to all the resources for all Batch jobs and defined with the job name.

Alternatively, if you use a custom label, you must apply the custom label to all the resources of the Batch jobs that you want to be included in the group when you create the jobs.

  2. Ensure that your project has at least one job with your selected label and that this job is in the `RUNNING` state. Otherwise, this label won't appear as an option when you try to create the resource group.

  3. [Create a resource group](https://docs.cloud.google.com/monitoring/groups). When you are specifying the membership criteria, do the following:

     1. Set the **Type** to **Tag**.
     2. Set the **Tag** field to the name of your selected label. Then, set the following fields based on the label values that you want the group to include.

For example, if you want this group to include all Batch jobs, set **Tag** to `batch-node`, and set **Operator** to **Exists**. Alternatively, you want this group to include Batch jobs with names that start with `test`, set **Tag** to `batch-job-id`, set **Operator** to **Starts with** , and set **Value** to `test`.




## What's next

  * Learn more about job resource metrics: 
    * [Collect additional resource metrics using the Ops Agent](https://docs.cloud.google.com/batch/docs/create-run-job-ops-agent).
    * [Create and manage custom Monitoring dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).
    * [Monitor GPUs](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).
  * Learn about other methods to monitor and optimize Batch jobs: 
    * [Monitor job status using Pub/Sub notifications and BigQuery](https://docs.cloud.google.com/batch/docs/monitor-jobs-using-notifications).
    * [Colocate VMs to reduce latency](https://docs.cloud.google.com/batch/docs/create-run-job-placement-policy).
    * Learn about more [job creation options](https://docs.cloud.google.com/batch/docs/create-run-job#job-creation-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
