---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/operational-logs-overview/
title: Operational logs overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:07.512725+00:00
---

# Operational logs overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/operational-logs-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Operational logs overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped provides operational logging capabilities to help you manage your applications and services effectively. Operational logs capture information about the conditions, changes, and actions occurring within your deployments, letting developers and operators do the following:

  * **Troubleshoot issues** : Identify and diagnose errors or unexpected behavior in your applications and infrastructure.
  * **Monitor performance** : Track resource usage, maintain a record of system events, and optimize application performance.



This section helps to understand and query operational logs. Use this section for reference when constructing [LogQL](https://grafana.com/docs/loki/latest/logql/) (Log Query Language) expressions to search for operational logs. For more information, see [Query and view logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/query-and-view-logs).

GDC collects operational logs for various resources, including the following:

  * **Kubernetes workloads** : Logs are captured from the standard output (`stdout`) and standard error (`stderr`) streams of your applications, adhering to the Kubernetes Container Runtime Interface (CRI) logging format. This practice ensures consistency and compatibility with Kubernetes' logging tools and practices. For more information on this format, refer to the official Kubernetes documentation: <https://github.com/kubernetes/design-proposals-archive/blob/main/node/kubelet-cri-logging.md>.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
