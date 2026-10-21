---
url: https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns/
title: Hybrid and multicloud monitoring and logging patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:37:20.822124+00:00
---

# Hybrid and multicloud monitoring and logging patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Hybrid and multicloud monitoring and logging patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-06-11 UTC

This document discusses monitoring and logging architectures for hybrid and multicloud deployments, and provides best practices for implementing them by using Google Cloud. With this document, you can identify which patterns and products are best suited for your environments.

Every enterprise has a unique portfolio of application workloads that place requirements and constraints on the architecture of a hybrid or multicloud setup. Although you must design and tailor your architecture to meet these constraints and requirements, you can rely on some common patterns.

The patterns covered in this document fall into two categories:

  * In a _single pane of glass_ architecture, all monitoring and logging is centralized, with the aim of providing a single point of access and control.
  * In a _separate application and operations_ architecture, sensitive application data is segregated from less sensitive operations data, with the aim of meeting compliance requirements for sensitive data.



## Choosing your architecture pattern

You can use the decision tree in the following diagram to identify the best architecture for your use case.

![Decision tree for selecting a monitoring and logging architecture.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-1.svg)

Details of each architecture are discussed further in this document, but at a high level, your choices are as follows:

  * Export from Monitoring to legacy solution.
  * Export directly to legacy solution.
  * Use Monitoring with Prometheus and Fluentd or Fluent Bit.
  * Use Monitoring with observIQ BindPlane.



## Single pane of glass architecture

A common goal for a hybrid system is to integrate monitoring and logging information from various sources across multiple applications and environments into a single display. This type of display is called a _single pane of glass_.

The following diagram illustrates this pattern where monitoring and logging data from all applications, both on-premises and in the cloud, is centralized into a single repository hosted in the cloud.

![High-level architecture for monitoring and logging.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-2.svg)

This architecture has the following advantages:

  * You have a single, consistent view for all monitoring and logging.
  * You have a single place to manage data storage and retention.
  * You get centralized access control and auditing. However, you still need to ensure the security of data in transit to the central repository.



## Monitoring as a single pane of glass

[Cloud Monitoring](https://docs.cloud.google.com/monitoring) is a Google-managed monitoring and management solution for services, containers, applications, and infrastructure. For a single pane of glass and a robust storage solution for metrics, logs, traces, and events, use Google Cloud Observability. The suite also provides a complete suite of observability tooling, such as dashboards, reporting, and alerting.

All Google Cloud products and services support integration with Monitoring. In addition, there are several integrated tools that you can use to extend Monitoring to hybrid and on-premises resources.

The following best practices apply to all architectures using Monitoring as a single pane of glass:

  * To fulfill compliance requirements for log retention, set up log sinks for your organization.
  * For fast analysis of log events, set up [log exports to BigQuery for security and access analytics](https://docs.cloud.google.com/solutions/exporting-stackdriver-logging-for-security-and-access-analytics).
  * To analyze logs that are stored in your log bucket, run SQL queries through [Observability Analytics](https://docs.cloud.google.com/logging/docs/log-analytics).
  * For projects containing sensitive data, consider enabling [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit), so you can track who has accessed the data.
  * To remove sensitive information, such as Social Security numbers, credit card numbers, and email addresses, you can filter log data. You can filter by using [a custom Fluent Bit configuration](https://medium.com/google-cloud/customizing-fluent-bit-for-google-kubernetes-engine-logs-a484b5d80072) or [ingest with logs exclusions](https://docs.cloud.google.com/logging/docs/exclusions). You can also export unfiltered logs separately to meet compliance requirements.



### Hybrid monitoring and logging with Monitoring and BindPlane by observIQ

With BindPlane from Google's partner [observIQ](https://observiq.com), you can import monitoring and logging data from both on-premises VMs and other cloud providers, such as Amazon Web Services (AWS), Microsoft Azure, Alibaba Cloud, and IBM Cloud into Google Cloud. The following diagram shows how Monitoring and BindPlane can provide a single pane of glass for a hybrid cloud.

![High-level architecture for monitoring and logging with BindPlane and
Monitoring.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-3.svg)

This architecture has the following advantages:

  * In addition to monitoring resources like VMs, BindPlane has built-in deep integration for [over 50 popular data sources](https://bindplane.com/docs/resources/sources).
  * [There are no additional licensing costs for using BindPlane](https://docs.cloud.google.com/stackdriver/bindplane). BindPlane metrics are imported into Monitoring as custom metrics, which are [chargeable](https://cloud.google.com/monitoring/pricing#monitoring-costs). Likewise, BindPlane logs are charged at the same rate as other Logging logs.



For more details about implementing this pattern, see [Logging and monitoring on-premises resources with BindPlane](https://docs.cloud.google.com/architecture/logging-and-monitoring-on-premises-resources-with-bindplane).

### Hybrid Google Kubernetes Engine monitoring with Prometheus and Monitoring

With [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus), a popular open source monitoring solution fully managed by Google Cloud, you can monitor applications running on multiple Kubernetes clusters with Monitoring. This architecture is useful when running Kubernetes workloads distributed across Google Kubernetes Engine (GKE) on Google Cloud and Google Distributed Cloud in your on-premises data center, because it provides a unified interface across both. The following diagram shows how to use Prometheus and the Monitoring collectors for data collection.

![High-level architecture for GKE monitoring with Prometheus and
Monitoring.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-4.svg)

This architecture has the following advantages:

  * Consistent Kubernetes metrics across cloud and on-premises environments.
  * It lets you globally monitor and alert on your workloads by using Prometheus, without having to manually manage and operate Prometheus at scale.
  * There are no additional licensing costs for using Prometheus. Prometheus metrics are imported into Monitoring. The imports are [chargeable](https://cloud.google.com/monitoring/pricing#monitoring-costs) and priced by the number of samples ingested.



This architecture has the following disadvantages:

  * Prometheus supports monitoring only, so logging has to be configured separately. The following section discusses a common option for logging using either Fluentd or Fluent Bit.



We recommend the following best practice:

  * By default, Prometheus collects all exposed metrics, each of which becomes a chargeable metric. To avoid unexpected costs, consider implementing [Monitoring cost controls](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls).



### Hybrid GKE logging with Fluentd or Fluent Bit and Cloud Logging

With [Fluentd](https://www.fluentd.org/) or [Fluent Bit](https://fluentbit.io/), a popular open source logging agent and Cloud Logging, you can ingest logs from applications running on multiple GKE clusters to Cloud Logging. This architecture is useful when running Kubernetes workloads distributed across GKE on Google Cloud and Google Distributed Cloud in your on-premises data center, because it provides a unified interface across both. The following diagram illustrates the flow of logs.

![High-level architecture for GKE monitoring with Fluentd or Fluent Bit,
Monitoring, and Logging.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-5.svg)

This architecture has the following advantages:

  * You can have consistent Kubernetes logging across cloud and on-premises environments.
  * You can customize Logging to filter out sensitive information.
  * There are no additional licensing costs for using Fluentd or Fluent Bit. Logs that are imported into Logging by using Fluentd or Fluent Bit are [chargeable](https://cloud.google.com/logging/pricing#logging-costs).



This architecture has the following disadvantages:

  * Fluentd and Fluent Bit support logging only, so monitoring has to be configured separately. The previous section discusses a common option for monitoring with Prometheus.



For more details about implementing this pattern, see [Customizing Fluent Bit for Google Kubernetes Engine logs](https://medium.com/google-cloud/customizing-fluent-bit-for-google-kubernetes-engine-logs-a484b5d80072).

## Partner services as single panes of glass

If you are already using a third-party monitoring or logging service such as Datadog or Splunk, you might not want to move to Logging. If so, you can export data from Google Cloud to many common monitoring and logging services. You can choose to use an integrated monitoring and logging service, or select separate monitoring and logging services that best fit your needs.

### Export from Logging to partner services

In this pattern, you authorize the partner's monitoring service, such as [Datadog](https://www.datadoghq.com/partner/gcp/), to connect to the Cloud Monitoring API. This authorization lets the service ingest all the metrics available to Logging, so Datadog can function as a single pane of glass for monitoring.

For logging data, Logging provides exports (log sinks) to [Pub/Sub](https://docs.cloud.google.com/pubsub). These exports provide a performant and resilient method for partner logging services such as [Elastic](https://www.elastic.co/partners/google-cloud) and [Splunk](https://docs.cloud.google.com/solutions/exporting-stackdriver-logging-for-splunk) to ingest large volumes of logs from Logging in real time, so these partner services can serve a single pane of glass for logs.

The combined architecture for logging and monitoring is shown in the following diagram.

![High-level architecture for exporting monitoring and logging data to partner services.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-6.svg)

This architecture has the following advantages:

  * You can continue to use familiar existing tools.
  * Google Cloud Support continues to have access to Logging logs for troubleshooting.



This architecture has the following disadvantages:

  * Partner solutions are typically externally hosted, which means they might not be available or collect data if network connections are disrupted. Sometimes, you can mitigate this risk by self-hosting, but at the cost of having to maintain the infrastructure for the solution yourself.
  * Externally hosted dashboards aren't directly available to Google Cloud Support. This lack of availability can slow down troubleshooting and mitigation.
  * Commercial partner solutions might entail more licensing fees.



Some detailed example integrations include the following:

  * Datadog: [Monitoring Compute Engine metrics](https://www.datadoghq.com/blog/monitoring-google-compute-engine-performance/) and [Collect Logging Logs](https://www.datadoghq.com/blog/collect-stackdriver-logs-with-datadog/)
  * Elastic: [Exporting Logging logs to Elastic Cloud](https://cloud.google.com/blog/products/data-analytics/export-google-cloud-data-into-elasticsearch-with-dataflow-templates)
  * Splunk: [Scenarios for exporting Logging](https://docs.cloud.google.com/solutions/exporting-stackdriver-logging-for-splunk)



### Analyze metrics from Prometheus and Logging with Grafana

[Grafana](https://grafana.com) is a popular open source monitoring tool commonly paired with [Prometheus](https://prometheus.io/) for metrics collection. In this architecture, you use Prometheus as the on-premises collection layer and use Grafana as a single pane of glass for both Google Cloud and on-premises resources. The following diagram shows a sample architecture that analyzes metrics from Google Cloud and on-premises.

![High-level architecture for monitoring with Grafana as a single pane of
glass.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-7.svg)

This architecture has the following advantages:

  * It's suitable for hybrid environments with both VMs and containers.
  * If your organization is already using Prometheus and Grafana, your users can continue to use them.



This architecture has the following disadvantages:

  * Prometheus supports monitoring only, so logging has to be configured separately, for example, using Fluentd or the [Cloud Logging plugin for Grafana](https://grafana.com/grafana/plugins/googlecloud-logging-datasource/).
  * Prometheus is open source and extensible, but supports only a [limited range of enterprise software integrations](https://prometheus.io/docs/instrumenting/exporters/).
  * Prometheus and Grafana are third-party tools and not official Google products. Google doesn't offer support for Prometheus or Grafana.



For more information, see [Better troubleshooting with a Cloud Logging plugin for Grafana](https://cloud.google.com/blog/products/devops-sre/cloud-logging-data-source-plugin-for-grafana).

### Export logs using Fluentd

An earlier pattern covered using Fluentd or Fluent Bit as a log collector for Logging. The same basic architecture can also be used for other logging or data analytics systems that support Fluentd or Fluent Bit, including [BigQuery](https://docs.cloud.google.com/bigquery), Elastic, and Splunk. The following diagram illustrates this pattern.

![High-level architecture of exporting logs directly from Fluentd or Fluent Bit.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-8.svg)

This architecture has the following advantages:

  * It's suitable for hybrid environments with both VMs and containers.
  * Fluentd can read from many [data sources](https://www.fluentd.org/datasources), including system logs.
  * Fluentd offers [output plugins](https://www.fluentd.org/plugins/all) for many popular third-party logging and data analytics systems.
  * Fluent Bit can also read from many [inputs](https://docs.fluentbit.io/manual/pipeline/inputs), including system logs.
  * Fluent Bit offers [outputs](https://docs.fluentbit.io/manual/pipeline/outputs) for many popular third-party logging and data analytics systems.



This architecture has the following disadvantages:

  * Fluentd and Fluent Bit support logs only, so monitoring has to be configured separately. The previous section discusses common options for monitoring with Prometheus and Grafana.
  * Fluentd and Fluent Bit are third-party tools and not official Google products. Google doesn't offer support for them.
  * Exported logs are not available to Google Cloud Support for troubleshooting. In particular, Google does not offer [support for Google Distributed Cloud](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/getting-support) clusters without Logging enabled.



## Separate application and operations data

Single pane of glass architectures require streaming application monitoring and logging data to the cloud. However, you might have regulatory or compliance requirements that either require keeping customer data on-premises or place strict constraints on what data can be stored in the public cloud.

A useful pattern for these hybrid environments is to separate sensitive application data from lower-risk operations data, as illustrated in the following diagram.

![High-level architecture for separating application and operations data.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-9.svg)

### Separate application and system data with a hybrid and multi-cloud architecture

To monitor on-premises clusters, you can use open source tools like Prometheus and Grafana. To collect and route telemetry data, you can use a solution like the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) or [observIQ BindPlane](https://docs.bindplane.com/). These tools let you configure sensitive application data to be ingested and viewed entirely on-premises, such as in a self-hosted monitoring and logging solution. You can export less sensitive system data to Monitoring and Logging on Google Cloud. The following diagram illustrates this architecture.

![Separating application and system data with GKE.](https://docs.cloud.google.com/static/architecture/images/hybrid-and-multi-cloud-monitoring-and-logging-patterns-10.svg)

This architecture has the following advantages:

  * Sensitive application data is kept entirely on-premises.
  * On-premises monitoring and logging have no cloud dependencies and remain available even if the network connection is interrupted.
  * All GKE system data, both on-premises and Google Cloud, is centralized in Monitoring and Logging and is also accessible to Google Cloud Support as needed.



## What's next

  * Learn more about hybrid and multicloud best practices with the [Hybrid and multicloud patterns and practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns) series, including [architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices) and [secure networking architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns).
  * Enroll in the [Cloud Kubernetes Best Practice quest](https://cloud.google.com/blog/topics/training-certifications/on-a-quest-learn-gke-security-and-monitoring-best-practices) for hands-on exercises about observability and more on GKE.
  * Explore reference architectures, diagrams, and best practices about Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-06-11 UTC."],[],[]] 
