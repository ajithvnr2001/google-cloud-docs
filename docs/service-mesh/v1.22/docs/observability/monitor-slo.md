---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/monitor-slo/
title: Monitoring SLOs \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:27.573203+00:00
---

# Monitoring SLOs  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/monitor-slo/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitoring SLOs

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This page describes how to monitor your service level objectives (SLOs).

For an introduction to SLOs, see the [Service level objectives overview](https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/slo-overview).

For each SLO that you create, Cloud Service Mesh creates several charts to help you monitor the SLO.

To view the charts: 

  1. Go to the **Health** tab for a service:

     1. In the Google Cloud console, go to **Cloud Service Mesh**.

[Go to Cloud Service Mesh](https://console.cloud.google.com/kubernetes/services)

     2. Select the Google Cloud project from the drop-down list on the menu bar.

     3. Click the service that you want to monitor.

     4. In the left navigation bar, click **Health**.

  2. Click the SLO that you want to review. Cloud Service Mesh provides the following charts:

     * **Service Level Indicator** : Shows the compliance of your service over the last minute compared to the specified compliance target. If there's an issue with the service, you see it right away, and you can take corrective action.

     * **Error Budget Remaining** : Shows how the service is consuming its [error budget](https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/design-slo#error_budgets) compared to the error budget threshold, which is always 0%.

     * **Compliance** : Shows how well the service is performing compared to the the compliance target. You use this chart to monitor if the service has violated or is about to violate the SLO.

  3. Click **Show Chart** under the chart name that you want to review.




## What's next

  * [Create an alerting policy for an SLO](https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/alert-policy-slo)
  * [Design SLOs](https://docs.cloud.google.com/service-mesh/v1.22/docs/observability/design-slo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
