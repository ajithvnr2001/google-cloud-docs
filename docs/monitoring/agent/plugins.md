---
url: https://docs.cloud.google.com/monitoring/agent/plugins/
title: Monitoring third-party applications \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:32.976726+00:00
---

# Monitoring third-party applications  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Monitoring third-party applications Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

This guide explains how to configure the legacy Cloud Monitoring agent to monitor supported third-party applications. Configuration is only possible when the legacy Monitoring agent is running on Linux. The agent on Windows monitors IIS and MS SQL applications; however, on these systems the agent cannot be configured to collect metrics from other third-party applications.

See [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent) for a list of the available metrics from the third-party applications. The configuration files are in the Monitoring agent's [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs).

After you have [installed the legacy Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation), see the following configuration instructions for supported third-party applications:

  * [Apache web server](https://docs.cloud.google.com/monitoring/agent/plugins/apache)
  * [JVM Monitoring](https://docs.cloud.google.com/monitoring/agent/plugins/jvm)
  * [Memcached](https://docs.cloud.google.com/monitoring/agent/plugins/memcached)
  * [MySQL](https://docs.cloud.google.com/monitoring/agent/plugins/mysql)
  * [Nginx](https://docs.cloud.google.com/monitoring/agent/plugins/nginx)
  * [Redis](https://docs.cloud.google.com/monitoring/agent/plugins/redis)
  * [StatsD](https://docs.cloud.google.com/monitoring/agent/plugins/statsd)



The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

  * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
  * Data about labels and cardinality of metrics.
  * Number of reads for each metric.
  * Use of metrics in alerting policies and custom dashboards.
  * Rate of metric-write errors.



You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
