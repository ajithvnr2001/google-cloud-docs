---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/other-data-collection/
title: Debug, analytics, and deployment status data collection \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:05:51.444847+00:00
---

# Debug, analytics, and deployment status data collection  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/other-data-collection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Debug, analytics, and deployment status data collection Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

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



Apigee hybrid makes debug, analytics, and deployment status data available to you. This data is collected by a data collection pod which sends it to the management plane so that you can view and analyze it and set up monitoring and alerts.

## About the data

All Message Processor (MP) services in hybrid stream debug (when initiated), analytics, and deployment status data via TCP to a data collection pod in the cluster. The data collection pod stores the streamed data on the pod's file system via a fluentd service.

The UDCA (Universal Data Collection Agent) periodically extracts the stored data and sends it to the UAP (Unified Analytics Platform) service in the management plane. The UAP processes the incoming analytics and deployment status data and makes it available to you via the hybrid UI or the [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).

Apigee hybrid implements the data collection pod as a [ReplicaSet](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) with a minimum of two replicas.

The following image shows the debug, analytics, and deployment status data collection process:

![Architectural diagram
showing the flow of data starting at the Message Processor, being stored by the UDCP, and ultimately
processed by an Apigee API or the Apigee hybrid UI.](https://docs.cloud.google.com/static/apigee/docs/hybrid/v1.10/images/arch-trace-analytics-status-data.png)

Note that the debug, analytics, and deployment status data is not stored in the same location or accessed in the same way as the logging and metrics data: 

  * _Logging and metrics data_ are stored on your Google Cloud Project and accessed via a tool such as Cloud Operations or whatever you choose to use.
  * _Debug, analytics and deployment status data_ , on the other hand, is stored in the hybrid management plane and you access it via Apigee services such as the hybrid UI or [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).



The following table summarizes the data collected by the data collection pod:

Type of Data | Dataset Name | Description | Update Frequency | APIs  
---|---|---|---|---  
Analytics | `api` | API usage data including transactions per second, cache usage, errors, latencies, request/response sizes, and traffic counts. For more information, see [Apigee Analytics overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview). | Up to 30 second delay | [Analytics admin API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.analytics.admin)  
Deployment Status | `event` | The current deployment status of the API proxy. For more information about how you can see this information, see [View deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status). | Immediately | [Deployments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.deployments)  
Debug | `debug` | Debug session data for API proxies. This data includes the request/response parameters along with transformations applied to them at policy execution time. Because of its size, debug data—unlike analytics and deployment status data—is not collected all the time. Instead, debug data is collected when you initiate a debug session. For more information, see [Debug overview](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview). | Immediately | [Debug session API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions)  
[Debug session data API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.apis.revisions.debugsessions.data)  
**TIP:** The _dataset name_ is the name by which this type of data is referred to in the UDCA configuration properties. For example, analytics data is configured with the dataset name `api`. As a result, the configuration property that sets the location of the analytics data files is called `**api** DataSubDir`. 

You can access this data through the Apigee hybrid UI or [Apigee APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest) on the management plane.

## View the data in the hybrid UI

This section describes how to view the debug, analytics, and deployment status data in the Apigee hybrid UI.

### Debug

Debug data for hybrid services is accessible in the same way as Edge debug data, with some differences such as increased filter support. For more information, see [Debug overview](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview).

### Analytics

Analytics data for hybrid services is accessible in the same way as Edge analytics data. For more information, see [Using the analytics dashboards](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/using-analytics-dashboards) in the Edge documentation.

### Proxy deployment status

For information on viewing deployment status, see [View deployment status](https://docs.cloud.google.com/apigee/docs/api-platform/deploy/ui-deploy-overview#viewing-deployment-status).

## Configure the data collection

To set how and where debug, analytics, and deployment status data is collected on the data collection pod, you configure the UDCA service via its configuration properties. The UDCA properties include properties that are general to the UDCA as well as properties that are specific to each dataset.

**To configure the UDCA:**

  1. Open the `overrides.yaml` file for editing on your Kubernetes administration machine, as described in [Manage runtime plane components](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/customize-services).
  2. Set the values of the UDCA configuration settings. For the UDCA, you can set custom values for properties such as: 
     * Polling interval
     * Number of replicas (min and max)
     * Target CPU percentage (that triggers additional replicas)

For a complete list of UDCA properties that you can customize, see [`udca`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/config-prop-ref#udca).

  3. Save your changes to the overrides.yaml file.
  4. Apply your changes to your cluster by executing the `apigeectl apply` command, as the following example shows: 
         
         apigeectl apply -f my-overrides.yaml --org --env env-name

**TIP** : To see the default configuration properties, the UDCA service (under `udca:`) in the [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/config-prop-ref).

For more information about the `apply` command, see [Apply the cluster configuration](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cli-reference#apply).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
