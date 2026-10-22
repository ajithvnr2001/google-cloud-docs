---
url: https://docs.cloud.google.com/chronicle/docs/secops/understand-the-secops-platform/
title: Understand the Google SecOps platform \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:53.696777+00:00
---

# Understand the Google SecOps platform  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/understand-the-secops-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand the Google SecOps platform

Supported in:

Google SecOps 

In the Google Security Operations platform, you will see that there are areas divided into SIEM and SOAR. This is because the platform provides tools for security information and event management (SIEM) and security orchestration, automation, and response (SOAR). Some parts of the Google SecOps platform are specific to either SIEM or SOAR only and therefore are labeled as such.

## SIEM Search and SOAR Search

In the Google SecOps platform, there is a Search page for SIEM and another Search page for SOAR.

On the **SIEM Search** page, you can find and investigate the following:

  * **Unified Data Model (UDM) events** : UDM is a standardized data format used within Google SecOps to represent security events from various sources consistently. An _event_ is generated from a raw log source that is ingested into Google SecOps and processed by Google SecOps's ingestion and normalization process. 
  * **Alerts** : Rule detections with alerting enabled—or alerts ingested from SOAR connectors and webhooks.
  * **Raw logs** : Raw, unparsed log telemetry.
  * **Joins** : Correlate and combine raw data from multiple sources based on common field values. 
  * **Statistics** : UDM events with the results grouped for statistical analysis.
  * **Cases** and **case histories** : Security cases and historical case audit logs, which you can correlate with other security data.



For more information about SIEM Search, see [Understand search](https://docs.cloud.google.com/chronicle/docs/investigation/udm-search).

The **SOAR Search** page focuses on two main areas: cases and entities. From this page, you can search for both open or closed cases or search for entities that were involved in cases. You can drill down to the entities you are looking for to see further information on them. You can perform bulk actions such as merge cases on your search results. For more information, see [Search cases and entities](https://docs.cloud.google.com/chronicle/docs/soar/investigate/search/working-with-search-screen). 

## Legacy SIEM dashboards and Legacy SOAR dashboards

Legacy SIEM dashboards display information about your UDM events data. This includes security telemetry, ingestion metrics, detections, alerts, IOCs, and more. For more information, see [Legacy SIEM dashboard overview](https://docs.cloud.google.com/chronicle/docs/investigation/dashboards-user-guide). 

The legacy SOAR dashboards display information on cases, playbooks, and SOC analyst data. You can create new dashboards and share them with other users. For more information, see [Legacy SOAR dashboards overview](https://docs.cloud.google.com/chronicle/docs/soar/monitor-and-report/soar-dashboards/dashboard-overview). 

For general information about dashboards, see [Dashboards overview](https://docs.cloud.google.com/chronicle/docs/reports/native-dashboards2). 

## SIEM Settings and SOAR Settings

The majority of the SOAR administration and configuration is located within the SOAR Settings, and the majority of the SIEM administration and configuration is located within the SIEM Settings. The permissions are set separately for each side of the platform and there is no dependency between them. For example, you could choose to limit permissions to Playbooks in the SOAR Settings for certain user groups while giving full permissions to all modules in the SIEM Settings. 

For details about data retention, see [Configure SIEM data retention](https://docs.cloud.google.com/chronicle/docs/about/data-retention). 

For information about SOAR data-retention settings, refer to [Configure SOAR data retention](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/define-system-data-retention). 

## Ingesting data using Google SecOps SIEM and third-party SIEM systems

The Google SecOps platform lets you not only ingest alerts using the inbuilt SIEM platform (which ingests raw logs using connectors and data feeds) but also accepts alerts from third-party SIEM systems and tools (using SOAR > Connectors and Webhooks). 

This ability provides you with the flexibility to take advantage of other SIEM systems in addition to the Google SecOps SIEM offering. Google recommends using the inbuilt SIEM wherever possible for a more streamlined experience.   
Alerts ingested from both the inbuilt SIEM and third-party systems can be grouped into Cases and looked at as part of the Case Management features. Alerts ingested from third-party systems are sent to the SIEM side of the platform and can be seen using the SIEM search but are not subjected to the inbuilt SIEM rules. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
