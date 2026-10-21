---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/unusual-configs/
title: Unusual configurations \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:21.726564+00:00
---

# Unusual configurations  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/unusual-configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Unusual configurations Stay organized with collections  Save and categorize content based on your preferences. 

## Running outside of Google Cloud

If your cluster is not running inside Google Cloud, you must manually configure values for the `project_id` and `location` labels. We recommend the following:

  * Set `project_id` based on how this cluster fits in your multi-tenant monitoring model. Your service account must be configured with the correct permissions for your chosen `project_id`.

  * Set `location` based on the closest Google Cloud region to your deployment.




You can't rewrite these labels using a relabeling rule.

## Having more than 3,500 projects in your organization

The maximum supported number of projects in a metrics scope is 375, but the maximum unsupported number of projects in a metrics scope is 3,500.

If you have more than 3,500 projects, the recommended workaround is to configure your collectors to use a central `project_id` instead of the ID of the project they are running in. Metrics from all your projects are then stored in Monarch under that central project ID, and you can simply put the central project into a metrics scope.

If you use this approach, then be aware of the following potential drawbacks:

  * You lose some multi-tenancy granularity by doing this, as permissions can only be set at a per-project level. You might want to logically group projects into a few categories and use a different central project for each.
  * The `project_id` value of Google Cloud system metrics cannot be overridden. This workaround will not let you see [free Google Kubernetes Engine metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) in the central project, as those metrics stay within each originating project.
  * Using a central project might complicate your use of Rules and ClusterRules, because those rules are scoped to the project in which they are installed, and you are unlikely to have the same set of cluster and namespace names in each project. You might have to use GlobalRules instead.



## Manually locating data in a single Google Cloud region

By default, Managed Service for Prometheus stores data in the Google Cloud region from which the data originates, and queries are naturally global, meaning you do not have to geographically co-locate data in order to query data across multiple Google Cloud regions.

In most situations, this default behavior is sufficient. However, there might be some situations where you want to store all metric data in a single Google Cloud region, for example, if you are in a highly-regulated environment.

To store all metric data in a single region, configure your collectors to use a single `location` instead of the auto-detected location of the cluster they are running in.

Storing data in a single Google Cloud region might complicate your use of Rules and ClusterRules, as those are scoped to the location in which they are installed, and you are unlikely to have the same set of cluster and namespace names in each Google Cloud region. You might have to use GlobalRules instead.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
