---
url: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/monitoring-overview/
title: Logging and monitoring overview \u00a0|\u00a0 Kf 2.6 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:27:19.659633+00:00
---

# Logging and monitoring overview  |  Kf 2.6  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.6/how-to/monitoring-overview/

Version 2.6

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.6 ](https://docs.cloud.google.com/migrate/kf/docs/2.6)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.6/getting-started)



Send feedback 

#  Logging and monitoring overview Stay organized with collections  Save and categorize content based on your preferences. 

By default, Kf includes native integration with [Cloud Monitoring](https://docs.cloud.google.com/monitoring) and [Cloud Logging](https://docs.cloud.google.com/logging/docs). When you create a cluster, both Monitoring and Cloud Logging are enabled by default. This integration lets you monitor your running clusters and help analyze your system and application performance using advanced profiling and tracing capabilities.

Application level performance metrics is provided by [Istio sidecar injection](https://docs.cloud.google.com/service-mesh/docs/proxy-injection) which is injected alongside applications deployed via Kf. You can also create [SLO](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-slo) and [Alerts](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring/ui/create-alert) using this default integration to monitor performance and availability of both system and applications.

Ensure the following are setup on your cluster:

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring) and [Cloud Logging](https://docs.cloud.google.com/logging/docs) are enabled on the Kf cluster by default unless you disabled them explicitly, so no extra step is required.

  * [Istio sidecar injection](https://docs.cloud.google.com/service-mesh/docs/proxy-injection) is enabled. Sidecar proxy will inject application level [performance metrics](https://docs.cloud.google.com/monitoring/api/metrics_istio).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
