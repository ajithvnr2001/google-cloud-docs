---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/monitoring-overview/
title: Monitoring overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:45.278268+00:00
---

# Monitoring overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/monitoring-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Monitoring overview Stay organized with collections  Save and categorize content based on your preferences. 

Gaining visibility into your applications and infrastructure is crucial for maintaining performance and stability. Therefore, Google Distributed Cloud (GDC) air-gapped provides a monitoring platform for collecting and analyzing your metrics.

The GDC monitoring platform lets you collect and query metrics from your deployed workloads. You can monitor and visualize your systems using built-in observability tools from the monitoring platform.

By effectively collecting and querying metrics, you can gain valuable insights into your air-gapped environment and ensure the optimal performance of your workloads.

## Key concepts

The GDC monitoring platform introduces the following concepts:

  * **Metrics** are quantitative measurements collected from your GDC workloads that provide valuable insights into resource utilization and performance. GDC uses Prometheus for this purpose. Prometheus is an open-source monitoring system that ensures efficient and reliable data collection.

  * **Dashboards** are visual representations of your metrics to observe trends and system behaviour. Your GDC project includes a dedicated Grafana instance for metrics visualization. Grafana is an analytics platform that lets you create insightful dashboards and explore your metrics data. GDC provides prebuilt dashboards for standard components, offering immediate visibility into your environment.




## Monitoring workflow

To facilitate the monitoring processes of your components, the GDC monitoring platform operates in the following workflow:

  1. **Collect metrics:** When your GDC environment is up and running, metrics from core components are automatically collected and displayed in pre-configured Grafana dashboards. This feature provides immediate network and server monitoring.

You can also configure scraping targets for your own applications and services by deploying custom resources that define workload-specific metrics to collect and the collection frequency.

  2. **Query metrics:** You can query your collected metrics using PromQL (Prometheus Query Language). Querying metrics lets you do the following:

     * Filter metrics based on labels and values.
     * Aggregate data over time.
     * Perform calculations on metric values.
  3. **Build dashboards and visualize metrics:** Use Grafana to build custom dashboards that visualize your metrics. These dashboards provide a clear and comprehensive view of your system's performance, enabling you to do the following:

     * Identify trends and anomalies.
     * Troubleshoot issues effectively.
     * Make informed decisions about resource allocation and optimization.



## Metrics retention

Retention policies define how long metrics and logs are stored. These policies are crucial for meeting compliance requirements and supporting operational analysis.

GDC uses retention times to set up lifecycle and retention policies for metrics. The system applies a default value of 90 days for metrics retention times.

## Access methods

The following access methods are available to operate with component metrics:

  * **Grafana user interface:** You can access your project's Grafana instance through the GDC console or directly using its URL. The user interface lets you query and visualize metrics.
  * **HTTP API:** Programmatically retrieve metrics data using the HTTP API. This method enables integration with external tools and automation scripts.



## Further resources

Consult [the comprehensive list of metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-overview) for detailed descriptions of all collected metrics from GDC components. This resource provides valuable context and facilitates advanced monitoring strategies.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
