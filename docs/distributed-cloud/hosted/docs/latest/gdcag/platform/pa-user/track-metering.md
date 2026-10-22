---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/track-metering/
title: Observability tracking for workloads \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:02.864784+00:00
---

# Observability tracking for workloads  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/track-metering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Observability tracking for workloads Stay organized with collections  Save and categorize content based on your preferences. 

The Google Distributed Cloud (GDC) air-gapped observability service offers a robust suite of monitoring and logging capabilities designed to streamline the tracking and troubleshooting of your workloads. Hosted directly on Distributed Cloud, this solution simplifies the collection of critical telemetry data, including logs and metrics.

With integrated dashboarding and advanced query tools, you can analyze performance in real-time, configure proactive alerts, and customize data retention or export policies to meet your specific compliance and operational needs.

## Observability-as-a-Service (OaaS) SKUs

The monitoring and logging SKUs enhance core functionalities by optimizing high-performance ingestion, advanced querying, and specialized routing.

  * **High-performance ingestion** : streamlined processing for both logs and metrics.

  * **Advanced querying** : faster, deeper insights into your data.

  * **Specialized routing** : intelligent log routing to optimize storage and visibility.




These SKUs use a metering-based billing model to ensure transparency across data usage. Additionally, the logging product is fully aligned with Google Cloud logging standards. This alignment resolves previous inconsistencies regarding retention periods and audit log types to provide a unified enterprise experience.

SKU name | SKU description | Units  
---|---|---  
Monitoring – metric ingestion | Chargeable metrics are ingested using Prometheus and persisted in object storage for a standard retention period of up to 90 days. | Per million samples per month.  
Monitoring – metric query | Supports data retrieval through monitoring read API calls, including queries run through Grafana or external tools within user projects. | Per 10 million samples processed.  
Monitoring – alert notifications | Webhook requests sent for notifications. | Per million web hooks per month.  
Logging – log ingestion  | Provides ingestion of chargeable logs using the Distributed Cloud logging API, with data stored in Object Storage for 30 days (Operational Logs) or 400 days (Audit Logs). | Per GB per month.  
Logging– log query | Covers the volume of data processed during log queries, including those run through Grafana LogQL or other system-level search tools. | Per GB of data scanned per month.  
Logging – log routing  | Forwarding logs to a supported destination | Per GB per month.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
