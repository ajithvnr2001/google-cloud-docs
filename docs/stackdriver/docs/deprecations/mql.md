---
url: https://docs.cloud.google.com/stackdriver/docs/deprecations/mql/
title: Monitoring Query Language (MQL) \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:21.773110+00:00
---

# Monitoring Query Language (MQL)  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/deprecations/mql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Monitoring Query Language (MQL) Stay organized with collections  Save and categorize content based on your preferences. 

As of **October 22, 2024** , [ Monitoring Query Language (MQL)](https://docs.cloud.google.com/monitoring/mql) is no longer a recommended query language for Cloud Monitoring.

  * On October 22, 2024, certain usability features were turned off.
  * On July 22, 2025, Google Cloud customer support for MQL ended, and MQL is no longer available for new charts, dashboards, and alerting policies in the Google Cloud console. Existing MQL charts, dashboards, and alerting policies continue to work, and you can still create them by using the Cloud Monitoring API.



We recommend moving to [PromQL](https://docs.cloud.google.com/monitoring/promql), the open-source standard for querying time series. PromQL offers similar functionality to MQL, with a wider user base and more community resources.

## Key points and dates

**MQL is not shut down**. You can still create and run MQL queries. Charts, dashboards, and alerting policies that use MQL queries continue to work.

### October 22, 2024

On October 22, 2024, the following MQL usability features were turned off:

  * Inline autocompletion in the MQL code editor. The editor no longer suggests completion strings for metric names, resource names, functions, operators, syntactic elements, label keys and values, and project IDs when you type Monitoring Query Language queries.
  * Conversion of queries between the Metrics Explorer query builder and MQL.



### July 22, 2025

On July 22, 2025, the following occurred:

  * Google Cloud customer support for cases involving writing valid MQL ended.
  * You can no longer create MQL charts, dashboards, or alerting policies by using the Google Cloud console. You can still create them by using the Cloud Monitoring API.



The following table lists MQL-related actions and if you can perform them using the Google Cloud console:

Action | Available in Google Cloud console? | Available in Monitoring API? |   
---|---|---|---  
Execute MQL queries in Metrics Explorer | Yes | Yes  
Save charts from a MQL query in Metrics Explorer to a dashboard | No | Yes  
Edit existing MQL charts, dashboards, or alerting policies | Yes | Yes  
Create new MQL charts, dashboards, or alerting policies | No | Yes  
  
## Required and recommended actions

**No action is required** to continue using your existing MQL assets, and you can create MQL assets by using the Cloud Monitoring API.

**We recommend that you begin using PromQL** or the interactive query builder for dashboards, alerting policies, and other workflows. For more information about using PromQL to create Cloud Monitoring charts, dashboards, and alerting policies, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
