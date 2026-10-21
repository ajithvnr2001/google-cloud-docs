---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/monitor-health-status/
title: Monitor health status \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:41:47.955891+00:00
---

# Monitor health status  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/monitor-health-status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Monitor health status Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to access the health status dashboards to monitor and identify potential issues.

Health status helps you visualize the essential metrics of your Google Distributed Cloud (GDC) air-gapped appliance infrastructure and provides a high-level overview of component health. Visualizing health status dashboards helps you identify root causes, diagnose behaviors, and obtain additional context during your investigation for resolving problems.

GDC monitors and provides the health status for each hardware and software component which includes:

  * Hardware: server node
  * Software: clusters, VMs, and storage



Health status dashboards let you visualize the metrics with which each component measures monitoring status.

## Before you begin

The root clusters contain a Grafana instance for infrastructure operators. These Grafana instances contain the health status dashboards.

You need role-based access controls to access data visualizations safely on dashboards of the Grafana instance. For this reason, follow the instructions of the [Before you begin section to query and view metrics on dashboards](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/query-and-view-metrics#before-you-begin-grafana) to access the dashboards on the Grafana instances.

## Grafana endpoint

Open one of the following URLs to access the Grafana endpoint of either the `infra-obs` project or the root admin cluster:

  * **Grafana endpoint of the`infra-obs` project:**
        
        https://GDC_URL/infra-obs/grafana
        

Replace GDC_URL with the URL of an organization in GDC.

  * **Grafana endpoint of the root admin cluster:**
        
        https://ROOT_ADMIN_CLUSTER_URL/grafana
        

Replace ROOT_ADMIN_CLUSTER_URL with the URL of the root admin cluster in GDC.




## Use case examples

This section includes examples on how you can use the dashboard for practical cases.

### Performance tuning

If a component is performing poorly but not necessarily impacting SLO or firing alerts, you can communicate proactively to developers and prevent future issues from occurring.

Likewise, a component might want to know how its feature operates to make the right performance tradeoffs. Health status are one mechanism for collecting the information that components need.

### Feature development

Suppose a customer requests changes or GDC plans to release a new feature. In that case, you can observe health status for the relevant components to determine the feasibility of supporting the new feature or change. Also, health status can be used to make product decisions when prioritizing the work.

For example, suppose a component has an average latency of 500 ms and is interested in reducing it to 250 ms. In that case, the team can calculate the relative cost of a 50% incremental reduction and compare it with designing an endpoint with 250 ms response time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
