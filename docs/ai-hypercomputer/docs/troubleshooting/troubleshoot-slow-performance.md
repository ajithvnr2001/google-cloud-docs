---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance/
title: Troubleshoot slow performance \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:07.262780+00:00
---

# Troubleshoot slow performance  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Troubleshoot slow performance Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to troubleshoot slow performance that you've identified for workloads that run on AI-optimized VMs or clusters.

To learn how to identify slow performance, see [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor). 

  1. **Identify and address any suspected stragglers for your workload** : Complete the following steps: 

     1. Check if you can use straggler detection for your workload. To review the limitations and requirements for using straggler detection, see [Monitor Compute Engine instances and Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor).

If you can't use straggler detection, then use other options for troubleshooting slow-performance.

     2. To check if any VMs for your workload are suspected stragglers, view straggler detection metrics. 

For example, to visualize all the suspected stragglers for your project in Cloud Monitoring, complete the following steps:

**Tip:** Alternatively, if you want to filter the suspected stragglers for your project, follow the instructions to [view straggler detection logs](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#view-straggler-detection-logs) and specify the [query for logs with suspected stragglers for specific VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#suspected-straggler-logs-specific-vm-query).
        1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

        2. In the **Type arrow_right** section of the filters pane, click **Google Services**.

        3. In the **Name** column, click **Cluster Director Health Monitoring**.

The details page for the dashboard opens.

        4. Use the time-range selector in the toolbar to select the time range of the slow performance. Straggler detection typically takes up to 10 minutes to report a straggler.

        5. To check if any VMs for your workload are suspected stragglers, review the **Straggler Detection** section. Use this query to see if the **Suspected Straggler Instances** table lists any VMs for your workload.

     3. Based on the number of VMs for your workload that are suspected stragglers, proceed as follows:

        * If _no_ VMs are suspected stragglers, then verify if straggler detection is running correctly. To verify if the straggler detection service is running for your project, follow the instructions to [view straggler detection logs](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#view-straggler-detection-logs) and specify the [query for all straggler detection logs in your project](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#all-straggler-logs-query). Then, proceed as follows:

          * If your project doesn't have straggler detection logs while VMs are running for at least 10 minutes, then the straggler detection service is not running for your project. To resolve this, [contact Cloud Customer Care](https://docs.cloud.google.com/support/docs/overview) or try again later.

          * Otherwise, if you've verified that straggler detection is running for your project and your workload supports straggler detection, then the slow performance might be caused by a different issue. Use other options for troubleshooting slow-performance.

        * If a _small number_ of VMs in your workload are reported as suspected stragglers, test migrating your workload off of the suspected VMs. Then, proceed as follows:

          * If migration does restore performance for your workload, then the suspected VMs might be faulty. For each of these VMs, follow steps to [report a faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host), and set `FAULT_REASON` to `PERFORMANCE` and set `DESCRIPTION` to `straggler node`.

          * If migration doesn't restore performance, then there might be more suspected straggler VMs or the slow performance might be caused by a different issue. You can check if more VMs for your workload are suspected stragglers or use other options for troubleshooting slow-performance.

        * If a _large number_ of VMs in your workload are reported as suspected stragglers, then use other options for troubleshooting slow-performance.

  2. **Use other options for troubleshooting slow performance** : If the reported list of suspected straggler VMs is large or if removing reported straggler VMs doesn't restore performance, use other options to troubleshoot slow performance, such as the following: 

     * [Review other metrics for performance](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#view-metrics).
     * Review other troubleshooting documentation. For example, see [Troubleshoot GPU VMs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus) in the Compute Engine documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
