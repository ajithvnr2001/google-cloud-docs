---
url: https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards/
title: Curated queries overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:37.595755+00:00
---

# Curated queries overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Curated queries overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google SecOps offers curated dashboards—predefined dashboards designed for visibility across various security use cases. While you cannot edit or delete curated dashboards, you can create a copy and customize it to fit your needs. For more information on how to create dashboards, see [Manage dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards#new-dashboards).

**Note:** You must have the `chronicle.nativeDashboards.list` IAM permission to view the list of curated dashboards.

## Out-of-the-box dashboards catalog

The out-of-the-box dashboards catalog lists predefined dashboards available in Google SecOps, organized by data source. Each catalog document details the individual charts within a dashboard, including chart descriptions and underlying search queries.

You can inspect the query syntax for each chart to identify the Unified Data Model (UDM) fields, event types, or metrics visualized by the dashboard. You can also use these queries in the query editor or as a baseline to create custom widgets and reports. To locate specific dashboards or charts, use the search and filter controls on each catalog page.

For operational guidance and use cases for common curated dashboards, see [Common curated dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/native-curated-dashboards-overview).

Explore the out-of-the-box dashboards by data source:

Dashboard category | Description  
---|---  
[Entities](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-entities) | Analyzes assets and entities that communicate with indicators of compromise (IoCs).  
[IoC matches](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-ioc-matches) | Provides visibility into the IoC matching events within the enterprise.  
[Ingestion metrics](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-ingestion-metrics) | Monitors data flow, error counts, and log distributions.  
[Rules and detections](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-rules-detections) | Evaluates rule performance and highlights threat patterns from detections.  
[Security orchestration, automation, and response cases](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-cases) | Provides metrics on security orchestration, automation, and response (SOAR) cases.  
[SOAR case history](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-case-history) | Reviews historical activity and performance across SOAR cases.  
[SOAR playbooks](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-playbooks) | Displays automation metrics and playbook execution results.  
[Unified Data Model](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-udm-) | Visualizes UDM security telemetry.  
[UDM and datatable](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-udm-datatable) | Visualizes UDM metrics and structured datatable telemetry.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
