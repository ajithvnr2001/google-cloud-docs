---
url: https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview/
title: API insights \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:31:47.001556+00:00
---

# API insights  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API insights Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

API insights offers a unified view of your API traffic and performance across all connected gateways (or plugin instances) in API hub. You can use this view to gain a holistic understanding of your API ecosystem health and quickly analyze areas for optimization. Expanding on [API analytics in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview), API insights enables proactive identification and mitigation of any issues across your API ecosystem. 

**Key Points:**

  * This feature includes GeoLite Data created by MaxMind, available from [https://www.maxmind.com](https://www.maxmind.com/). 
  * The terms _gateways_ and _plugin instances_ are used interchangeably in this document. 



## Enable API insights

API insights collects and analyzes API data from your attached gateways in API hub. To start viewing your API data in API insights, depending on your gateway type, you must first either [attach a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project) or [create a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances) in API hub. 

If you have an existing runtime project attached, but are unable to see any API data in API insights, then you may need to edit the project settings to import the necessary API assets into API hub. For more information, see [Edit project association settings](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#edit-project-association-settings). 

**Note:** When you provision API hub as part of Apigee provisioning, it automatically identifies and attaches any associated Apigee runtime projects. API insights for such attached projects are collected and analyzed automatically. 

For more information about configuring API insights in API hub, see [Configure API insights](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights). 

## View API insights

To view API insights, go to the **API hub** page in the Google Cloud console and click **API insights** from the left navigation menu. The API insights page appears, displaying the following dashboards: 

  * **Gateway performance:** provides insights into the traffic and performance of your gateways.
  * **API performance:** provides insights into the traffic and performance of your APIs.
  * **API error analysis:** provides insights about the errors encountered while using your APIs.
  * **Latency analysis:** provides insights into the latency of your APIs across multiple percentiles.
  * **Target performance:** provides insights into the traffic and performance of your targets.
  * **AI performance:** provides insights into the token usage and performance of the large language models (LLMs) called through your gateways.
  * **Tool performance:** provides insights into the traffic and performance of your Model Context Protocol (MCP) tools.



For detailed information about each dashboard, see [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard). 

## IAM roles and permissions

To view API insights in API hub, you need the following IAM roles and permissions: 

IAM role | Permissions  
---|---  
**API hub API Insights Viewer**(`roles/apihub.apiInsightsViewer`) | 

  * apihub.locations.getApiInsights
  * apihub.apis.list
  * apihub.apis.get
  * apihub.plugininstances.list
  * apihub.plugininstances.get
  * apihub.deployments.list
  * apihub.deployments.get
  * apihub.apiHubInstances.get
  * apihub.apiHubInstances.list
  * monitoring.dashboards.get
  * monitoring.dashboards.list
  * monitoring.monitoredResourceDescriptors.list
  * monitoring.monitoredResourceDescriptors.get
  * monitoring.metricDescriptors.list
  * monitoring.metricDescriptors.get
  * apigee.projectorganizations.get

  
**Note:** IAM roles for API insights provide broad access, applying across all configured gateways rather than offering gateway-specific permissions. This means that once a user is granted the required IAM permissions, they can view data from all your gateways within the API insights page in API hub. 

For information on granting roles to principals, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

## Limitations

  * API insights doesn't support data ingestion for [custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-types) and [API observations](https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview). 
  * API insights is supported only for Apigee, Apigee hybrid, Apigee Edge Public Cloud, and Apigee Edge Private Cloud (OPDK). 
  * API insights data is not accessible through API calls. 
  * API insights doesn't support exporting metric data to other Google Cloud services such as BigQuery, Cloud Storage, or Data Studio. 



## What's next

  * Learn about [configuring API insights](https://docs.cloud.google.com/apigee/docs/apihub/configure-api-insights).
  * Learn about [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard).
  * Learn about [attaching a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project) or [creating a plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances) in API hub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
