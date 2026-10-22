---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-overview/
title: Overview \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:38.589143+00:00
---

# Overview  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

Metrics are quantitative measurements taken from the workloads deployed in your Google Distributed Cloud (GDC) air-gapped appliance projects that help you monitor resources.

This section provides information about metrics collected from all components in GDC and contains information about metric types, duration, and labels for each. Use this document for reference when constructing [PromQL](https://prometheus.io/docs/prometheus/latest/querying/basics/) (Prometheus Query Language) expressions to query metrics in the monitoring instance of your project.

Review information about metrics for the following GDC components:

  * [Add on Manager (ADD)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-add)
  * [Controller Manager (COM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metric-com)
  * [Domain Name System (DNS)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/metrics-dns)
  * [Inventory Management (INV)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-operations/metrics-inv)
  * [User clusters (KUB)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-kub)
  * [Virtual Machine Management (VMM)](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform-application/pa-ao-operations/metrics-vmm)



## Metrics visualization

For information about the monitoring and visualizing processes, see see [Collect and query metrics](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/monitoring-overview).

PAs can use the following URL to access the metrics in the PA Grafana project:
    
    
    https://GDCH_APPLIANCE_HOST/platform-obs/grafana/explore
    

Replace `GDCH_APPLIANCE_HOST` with the name of your organization in GDC.

AOs can use the following URL to access the metrics in your Grafana project:
    
    
    https://GDCH_APPLIANCE_HOST/PROJECT_NAME/grafana/explore
    

Replace the following:

  * `GDCH_APPLIANCE_HOST`: the name of your organization in GDC.
  * `PROJECT_NAME`: the name of your project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
