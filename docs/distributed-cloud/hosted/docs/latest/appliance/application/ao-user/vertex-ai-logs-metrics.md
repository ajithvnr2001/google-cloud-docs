---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-logs-metrics/
title: View Vertex AI logs and metrics \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:14.863585+00:00
---

# View Vertex AI logs and metrics  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-logs-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  View Vertex AI logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

Logs and metrics let you monitor your services and troubleshoot issues with service performance. You can view logs and metrics from Vertex AI services using the monitoring and logging resources from Google Distributed Cloud (GDC) air-gapped appliance. You can also create queries to monitor specific Vertex AI metrics.

This page describes how to query and view logs and metrics from Vertex AI services in Grafana.

This page also contains sample queries that you can use to monitor the Vertex AI platform and services, such as Optical Character Recognition (OCR), Speech-to-Text, and Vertex AI Translation.

## Before you begin

To get the permissions you need to view logs and metrics from Vertex AI, ask your Project IAM Admin to grant you the Project Grafana Viewer (`project-grafana-viewer`) role in your project namespace.

## Visualize logs and metrics in dashboards

You can view Vertex AI metrics and logs in dashboards. For example, you can create a query to view how Vertex AI affects CPU usage.

Follow these steps to view Vertex AI logs and metrics in dashboards:

  1. [Sign in to the GDC console and select your project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in).

  2. In the navigation menu, click **Vertex AI** > **Pre-trained APIs**.

  3. On the **Pre-trained APIs** page, make sure that [the Vertex AI API for the service you want to monitor is enabled](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-enable-pre-trained-apis).

  4. Click **Monitor services in Grafana** to open the Grafana home page.

  5. In the navigation menu of the home page, click explore **Explore** to open the **Explore** page.

  6. From the menu at the **Explore** page, select one of the following data sources:

     * **Operational Logs** : retrieve operational logs.
     * **Audit Logs** : retrieve audit logs.
     * **Prometheus** : retrieve metrics.
  7. If you want to display metrics, enter a query using [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) (Prometheus Query Language) expressions.

  8. If you want to display logs, enter a query using [LogQL](https://grafana.com/docs/loki/latest/logql/) (Log Query Language) expressions.




The page displays the metrics or logs matching your query.

## Sample queries

**Important:** Audit logs from Vertex AI platform and services are only available to Infrastructure Operators (IO).

The following table contains sample queries to monitor the Vertex AI platform in your environment:

**Vertex AI platform**  
---  
**Data source** | **Description** | **Component** | **Query**  
Metrics | CPU usage percentage of the container | Level 1 operator | `rate(container_cpu_usage_seconds_total{namespace="ai-system",container="l1operator"}[30s]) * 100`  
Level 2 operator | `rate(container_cpu_usage_seconds_total{namespace="ai-system",container="l2operator"}[30s]) * 100`  
Memory usage in MB of the container | Level 1 operator | `container_memory_usage_bytes{namespace="ai-system",container="l1operator"} * 1e-6`  
Level 2 operator | `container_memory_usage_bytes{namespace="ai-system",container="l2operator"} * 1e-6`  
Operational logs | L1 operator logs | Level 1 operator | `{service_name="vai-l1operator"}`  
L2 operator logs | Level 2 operator | `{service_name="vai-l2operator"}`  
Audit logs  
**Important:** Audit logs from Vertex AI platform and services are only available to Infrastructure Operators (IO). | Platform frontend audit logs | Vertex AI web plugin frontend | `{service_name="istio"} |~ upstream_cluster:.*(vai-web-plugin-frontend.ai-system)`  
Platform backend audit logs | Vertex AI web plugin backend | `{service_name="istio"} |~ upstream_cluster:.*(vai-web-plugin-backend.ai-system)`  
  
The following table contains sample queries to monitor Vertex AI API services, such as OCR, Speech-to-Text, and Vertex AI Translation, in your environment:

**Vertex AI services**  
---  
**Data source** | **Description** | **Service** | **Query**  
Metrics | The effect of a pre-trained API on  
CPU usage. | OCR | `rate(container_cpu_usage_seconds_total{namespace="g-vai-ocr-sie",container="CONTAINER_NAME"}[30s]) * 100 CONTAINER_NAME values: vision-extractor | vision-frontend | vision-vms-ocr`  
Speech-to-Text | `rate(container_cpu_usage_seconds_total{namespace="g-vai-speech-sie",container="CONTAINER_NAME"}[30s]) * 100`  
Vertex AI Translation | `rate(container_cpu_usage_seconds_total{namespace="g-vai-translation-sie",container="CONTAINER_NAME"}[30s]) * 100 CONTAINER_NAME values: translation-aligner | translation-frontend | translation-prediction`  
Use the `destination_service` filter label to get the error rate over the last 60 minutes. | OCR | `rate(istio_requests_total{destination_service=~".*g-vai-ocr-sie.svc.cluster.local",response_code=~"[4-5][0-9][0-9]"}[60m])`  
Speech-to-Text | `rate(istio_requests_total{destination_service=~".*g-vai-speech-sie.svc.cluster.local",response_code=~"[4-5][0-9][0-9]"}[60m])`  
Vertex AI Translation | `rate(istio_requests_total{destination_service=~".*g-vai-translation-sie.svc.cluster.local",response_code=~"[4-5][0-9][0-9]"}[60m])`  
Operational logs | Operational logs from Vertex AI services  
**Note:** Use the namespace of the service to specify the main filter.  
  
You can create more granular results by adding additional labels, such as `service_name` or `pod`, to your query. | OCR | `{namespace="g-vai-ocr-sie"}`  
Speech-to-Text | `{namespace="g-vai-speech-sie"}`  
Vertex AI Translation | `{namespace="g-vai-translation-sie"}`  
Audit logs  | Audit logs from Vertex AI services  
**Important:** Audit logs from Vertex AI platform and services are only available to Infrastructure Operators (IO). | OCR | `{service_name="istio"} |= "vision-frontend-server"`  
Speech-to-Text | `{service_name="istio"} |= "speech-frontend-server"`  
Vertex AI Translation | `{service_name="istio"} |= "translation-frontend-server"`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
