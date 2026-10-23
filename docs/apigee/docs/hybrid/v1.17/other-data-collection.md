---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/other-data-collection/
title: Debug, analytics, and deployment status data collection \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:50.748194+00:00
---

# Debug, analytics, and deployment status data collection  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/other-data-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Debug, analytics, and deployment status data collection Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/other-data-collection.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/other-data-collection.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/other-data-collection.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/other-data-collection.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/other-data-collection.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/other-data-collection.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/other-data-collection.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/other-data-collection.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/other-data-collection.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/other-data-collection.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/other-data-collection.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/other-data-collection.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/other-data-collection.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/other-data-collection.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/other-data-collection.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/other-data-collection.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/other-data-collection.html)



Apigee hybrid makes debug, analytics, and deployment status data available to you. This data is sent from the runtime components directly to the management plane via a Google Cloud Pub/Sub-based data pipeline so that you can view and analyze it and set up monitoring and alerts.

## About the data

All Message Processor (MP) services in hybrid stream debug (when initiated), analytics, and deployment status data directly to the Apigee control plane using Google Cloud Pub/Sub.

The UAP (Unified Analytics Platform) service in the management plane processes the incoming analytics and deployment status data and makes it available to you via the hybrid UI or the [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).

The debug, analytics, and deployment status data is not stored in the same location or accessed in the same way as the logging and metrics data: 

  * _Logging and metrics data_ are stored on your Google Cloud Project and accessed via a tool such as Cloud Operations or whatever you choose to use.
  * _Debug, analytics and deployment status data_ , on the other hand, is stored in the hybrid management plane and you access it via Apigee services such as the hybrid UI or [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).



The following table summarizes the data collected:

Type of Data | Description | Update Frequency | APIs  
---|---|---|---  
Analytics | API usage data including transactions per second, cache usage, errors, latencies, request/response sizes, and traffic counts. For more information, see [Apigee Analytics overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview). | Up to 30 second delay | [Analytics admin API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin)  
Deployment Status | The current deployment status of the API proxy. For more information about how you can see this information, see [View deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status). | Immediately | [Deployments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.deployments)  
Debug | Debug session data for API proxies. This data includes the request/response parameters along with transformations applied to them at policy execution time. Because of its size, debug data—unlike analytics and deployment status data—is not collected all the time. Instead, debug data is collected when you initiate a debug session. For more information, see [Debug overview](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview). | Immediately | [Debug session API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions)  
[Debug session data API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data)  
  
## View the data in the hybrid UI

This section describes how to view the debug, analytics, and deployment status data in the Apigee hybrid UI.

### Debug

Debug data for hybrid services is accessible in the same way as Edge debug data, with some differences such as increased filter support. For more information, see [Debug overview](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview).

### Analytics

Analytics data for hybrid services is accessible in the same way as Edge analytics data. For more information, see [Using the analytics dashboards](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards) in the Edge documentation.

### Proxy deployment status

For information on viewing deployment status, see [View deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status).

## Configure the data collection

The Pub/Sub-based data pipeline is enabled by default. You must ensure that your service accounts are properly configured with control plane access, as described in [Step 8: Enable control plane access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
