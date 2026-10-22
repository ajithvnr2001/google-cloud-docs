---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/llm-d/
title: llm-d \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:18.755749+00:00
---

# llm-d  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/llm-d/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  llm-d Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how your Google Kubernetes Engine deployment can use Google Cloud Managed Service for Prometheus to collect metrics from [llm-d](https://llm-d.ai/). llm-d consists of many components, including GKE Inference Gateway and vLLM.

For information about collecting metrics from GKE Inference Gateway and vLLM, see the following documents:

  * [ GKE Inference Gateway](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/inference-optimized-gateway)
  * [ vLLM](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/exporters/vllm). Use the configuration for the PodMonitoring resource described in this document.



The instructions in these documents apply only if you are using [ managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed) with Managed Service for Prometheus. If you are using self-deployed collection, then see the [llm-d documentation](https://github.com/llm-d/llm-d/tree/main/docs/monitoring).

After you configure GKE Inference Gateway and vLLM, you can access a predefined dashboard in Cloud Monitoring to view the metrics.

## Prerequisites

To collect metrics from llm-d by using Managed Service for Prometheus and managed collection, your deployment must meet the following requirements:

  * Your cluster must be running Google Kubernetes Engine version 1.28.15-gke.2475000 or later.
  * You must be running Managed Service for Prometheus with managed collection enabled. For more information, see [ Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).



You must also change the configuration of the PodMonitoring resource for vLLM. Use the following configuration:
    
    
    apiVersion: monitoring.googleapis.com/v1
    kind: PodMonitoring
    metadata:
      name: llm-d-metrics
    spec:
      selector:
        matchLabels:
          llm-d.ai/model: ms-pd-llm-d-modelservice
      endpoints:
      - port: 8200
        interval: 10s
        path: /metrics
      targetLabels:
        fromPod:
        - from: llm-d.ai/role
          to: role
        metadata:
        - pod
        - container
        - node
        - top_level_controller_name
        - top_level_controller_type
    

## View dashboards

The Cloud Monitoring integration includes the **llm-d Prometheus Overview** dashboard. Dashboards are automatically installed when you configure the integration. You can also view static previews of dashboards without installing the integration.

To view an installed dashboard, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab.
  3. Choose the **Integrations** category.
  4. Click the name of the dashboard, for example, **llm-d Prometheus Overview**.



To view a static preview of the dashboard, do the following:

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Kubernetes Engine** deployment-platform filter.
  3. Locate the llm-d integration and click **View Details**.
  4. Select the **Dashboards** tab.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
