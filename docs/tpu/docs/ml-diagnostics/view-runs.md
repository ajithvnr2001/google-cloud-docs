---
url: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/view-runs/
title: View machine learning runs with ML Diagnostics \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:04.502413+00:00
---

# View machine learning runs with ML Diagnostics  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ml-diagnostics/view-runs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View machine learning runs with ML Diagnostics

A machine learning run is a single, complete execution of a machine learning script or pipeline. With ML Diagnostics, you can view machine learning runs in the Google Cloud console using either the CLI or SDK.

To view all your machine learning runs in Cluster Director:

  1. In the Google Cloud console, go to the **Cluster Director** page.
  2. Click the **Run Diagnostics** tab.



[Go to Cluster Director Run Diagnostics](https://console.cloud.google.com/cluster-director/diagnostics)

To view all your machine learning runs in Google Kubernetes Engine:

  1. In the Google Cloud console, go to the **Kubernetes** page.
  2. In the navigation menu, click **AI/ML**.
  3. Click the **Run Diagnostics** tab.



[Go to GKE AI/ML Run Diagnostics](https://console.cloud.google.com/kubernetes/aiml/diagnostics)

In both Cluster Director and GKE, you will find the following information:

  * **Run summaries** : A list view table with summary information for all your machine learning runs.
  * **Run details** : Run details for each run, including configs and run information.
  * **Time series charts for metrics** : All metrics, including model metrics, performance metrics, and system metrics. You can also view these metrics with Logs Explorer. Metrics recorded with the `metrics.record()` method are written as log entries and can be filtered or used to create log-based metrics.
  * **Profiling information** : A Profiles tab with all profile sessions for a particular run, with links to the [XProf viewer](https://openxla.org/xprof/trace_viewer). This includes both programmatic and on-demand profile captures. You can also capture an on-demand profile session directly from the user interface.
  * **On-demand Profiling from the Google Cloud console** : Within the **Profiles** tab, you can capture an on-demand profile session directly from the Google Cloud console. Click the **Capture new profile session** button, specify the duration to capture for the profile session, and select the required hosts to capture the profile. The hosts running the workload are autopopulated in the table, without any manual entry required. After the specified on-demand capture time, the profile session shows up automatically in the **Sessions** table. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
