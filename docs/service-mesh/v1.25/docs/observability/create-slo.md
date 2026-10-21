---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/create-slo/
title: Creating SLOs \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:51.397683+00:00
---

# Creating SLOs  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/create-slo/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating SLOs

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

This page describes how to create a service level objective (SLO) in the Google Cloud console. For information on creating a SLO programmatically, see [Working with the SLO API](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/api/api-structures)

For an overview and information on designing SLOs, see the following:

  * [Service level objectives overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/slo-overview)
  * [Designing SLOs](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/design-slo)



To create an SLO:

  1. Go to the **Health** tab for a service:

     1. In the Google Cloud console, go to **Cloud Service Mesh**.

[Go to Cloud Service Mesh](https://console.cloud.google.com/kubernetes/services)

     2. Select the Google Cloud project from the drop-down list on the menu bar.

     3. Click the service that you want to create an SLO for.

     4. In the left navigation bar, click **Health**.

  2. Click the **Create an SLO** link.

  3. Click **Set your service-level indicator (SLI)** to select the type of service level indicator (SLI) to track for this SLO. Choose one of the following:

     * **Availability** : The ratio of the number of successful responses to the number of all responses. Requests that fail before they reach the Envoy sidecar proxy for your service (because of networking or DNS failures, for example) aren't included in this ratio.
     * **Latency** : The ratio of the number of calls that are below the specified **Latency Threshold** to the number of all calls.
  4. For latency SLIs, enter the **Latency Threshold** in milliseconds.

  5. In the **Performance Goal** section, enter a percentage in the **Goal** field to set the performance target for the SLI. Cloud Service Mesh uses this value to calculate the [error budget](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/design-slo#error_budgets) you have for this SLO.

  6. In the **Compliance Period** section, select the **Period Type** and the **Period Length**. See [Compliance periods](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/design-slo#compliance_periods) for more information on these settings.

  7. Alternatively, in the **Set your SLI** section, you may select **Windows-based** SLI. A windowed SLI can help you catch periods of time when the service won't meet the SLO **Compliance target** (such as when there are spikes in the number of requests that increase latency for a short period of time). When you select this option, you must specify:

     * **Goodness criterion** : Set a threshold for the percentage of "good performance" that must be met in order for a given window to count as "good."
     * **Duration** : Set the length of each window, over which SLO performance will be measured in increments during the compliance period.

For example, suppose you have an **Availability** SLO with a **Rolling** **7** day period, and an **SLO Goal** of **99** %. Then you add a **Goodness criterion** of **95** % and a **Duration** of **5** minutes. To be compliant, the service needs **95** % of all **5** minute windows over the last **7** days to be available at least **99** % of the time.

  8. Optionally, click **Name your SLO** to change the default SLO display name. Cloud Service Mesh supplies a default name that describes the SLO based on the settings.

  9. Click **Submit**.




## What's next

  * [Monitoring SLOs](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/monitor-slo)
  * [Creating an alerting policy on an SLO](https://docs.cloud.google.com/service-mesh/v1.25/docs/observability/alert-policy-slo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
