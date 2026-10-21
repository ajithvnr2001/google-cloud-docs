---
url: https://docs.cloud.google.com/network-security-integration/docs/in-band/monitor-in-band-integration/
title: Monitor in-band integration \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:27:21.186154+00:00
---

# Monitor in-band integration  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/in-band/monitor-in-band-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)



Send feedback 

#  Monitor in-band integration Stay organized with collections  Save and categorize content based on your preferences. 

Network Security Integration in-band integration exports monitoring data about intercepted traffic to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). In-band integration provides the following consumer metrics for intercepted packets:

  * `/intercept/intercepted_packets_count`
  * `/intercept/intercepted_bytes_count`



For more information, see the [metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-compute) for Compute Engine in the Monitoring documentation.

Service producers can use [Internal passthrough Network Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring) for each internal passthrough Network Load Balancer that provides packet inspection services.

## View packet intercept metrics

  1. Go to the **Metics explorer** page.

[Go to the Metrics explorer page](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Select your Google Cloud project.

  3. In the **Metric** element, expand the **Select a metric** menu and specify the metric: **Intercepted bytes** or **Intercepted packets**

  4. View the charts to see the intercepted bytes and intercepted packets.




For more information about creating and using charts, see [Select metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).

To define alerting policies, see [Create new alerting policies](https://docs.cloud.google.com/monitoring/alerts#condition-types). To view and customize dashboards, see [View and copy Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).

## What's next

  * [Network Security Integration overview](https://docs.cloud.google.com/network-security-integration/docs/nsi-overview)
  * [In-band integration overview](https://docs.cloud.google.com/network-security-integration/docs/in-band/in-band-integration-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
