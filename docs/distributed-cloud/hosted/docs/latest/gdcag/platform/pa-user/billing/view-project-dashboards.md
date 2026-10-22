---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/view-project-dashboards/
title: View project-level dashboards \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:41.011584+00:00
---

# View project-level dashboards  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/billing/view-project-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View project-level dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This document provides instructions for viewing project-level dashboards in GDC. Project-level dashboards allow users to monitor the resource usage and costs associated with their projects.

## Before you begin

To get the permissions that you need to view project-level dashboards, ask your **IAM Project Admin** to grant you the **Project Grafana Viewer** (`project-grafana-viewer`) role for the `platform-obs` project.

## Access project dashboards

To access these Grafana dashboards, do the following:

  1. Open the following URL to access the Grafana home page:
         
         https://GDC_URL/platform-obs/grafana/
         

Replace `GDC_URL` with the URL of your Distributed Cloud organization.

  2. In the navigation menu, click **Dashboards**.

  3. In the **Search for dashboards** field, enter the name of the dashboard you want to view.




## Projected Cost dashboard

The Projected Cost dashboard helps you anticipate future SKU costs per project. You can filter this dashboard by billing account ID, month, and project name to view custom projections.

## Real Time Cost dashboard

The Customer Real Time Cost dashboard helps you monitor real-time cost and resource usage for your infrastructure as it occurs. This dashboard displays active resource consumption and accumulated costs through line graph panels for costs and usage. You can filter this dashboard by aggregation level, project name, SKU, and time range to view active spending.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
