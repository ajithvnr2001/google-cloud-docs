---
url: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/
title: Google Cloud Managed Service for Prometheus \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:02.396260+00:00
---

# Google Cloud Managed Service for Prometheus  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Google Cloud Managed Service for Prometheus Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Managed Service for Prometheus is Google Cloud's fully managed, multi-cloud, cross-project solution for [Prometheus](https://prometheus.io) and [OpenTelemetry](https://opentelemetry.io/docs/collector/) metrics. It lets you globally monitor and alert on your workloads, using Prometheus and OpenTelemetry, without having to manually manage and operate Prometheus at scale.

Managed Service for Prometheus collects metrics from Prometheus exporters and lets you query the data globally using PromQL, meaning that you can keep using any existing [Grafana](https://grafana.com/grafana) dashboards, PromQL-based alerts, and workflows. It is hybrid- and multi-cloud compatible, can monitor Kubernetes, VMs, and serverless workloads on Cloud Run, retains data for 24 months, and maintains portability by staying compatible with upstream Prometheus. You can also supplement your Prometheus monitoring by querying [over 6,500 free metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) in Cloud Monitoring, including [free GKE system metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes), using PromQL.

This document gives an overview of the managed service, and further documents describe how to set up and run the service. To receive regular updates about new features and releases, submit the optional [sign-up form](https://docs.google.com/forms/d/e/1FAIpQLScXB4ezLOF_0ifXrz9THQz7w9B4fS0yPkX4Ul1w-gkbPRf2EA/viewform).

Hear how The Home Depot uses Managed Service for Prometheus to get unified observability across 2,200 stores running on-prem Kubernetes clusters: 

## System overview

Google Cloud Managed Service for Prometheus gives you the familiarity of Prometheus backed by the global, multi-cloud, and cross-project infrastructure of Cloud Monitoring.

![Managed Service for Prometheus gives you access to features of Prometheus and Cloud Monitoring.](https://docs.cloud.google.com/static/stackdriver/images/gmp-architecture.png)

Managed Service for Prometheus is built on top of Monarch, the same [globally scalable datastore](https://research.google/pubs/pub50652/) used for Google's own monitoring. Because Managed Service for Prometheus uses the same backend and APIs as [Cloud Monitoring](https://docs.cloud.google.com/monitoring), both Cloud Monitoring metrics and metrics ingested by Managed Service for Prometheus are queryable by using [PromQL in Cloud Monitoring](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm), [Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query), or [any other tool that can read the Prometheus API](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-api-ui).

In a standard Prometheus deployment, data collection, query evaluation, rule and alert evaluation, and data storage are all handled within a single Prometheus server. Managed Service for Prometheus splits responsibilities for these functions into multiple components:

  * Data collection is handled by managed collectors, self-deployed collectors, the OpenTelemetry Collector, or [the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus), which scrape local exporters and forward the collected data to Monarch. These collectors can be used for Kubernetes, serverless, and traditional VM workloads and can run everywhere, including other clouds and on-prem deployments.
  * Query evaluation is handled by Monarch, which executes queries and unions results across all Google Cloud regions and across up to 3,500 Google Cloud projects.
  * Rule and alert evaluation is handled either by writing [PromQL alerts in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting) which fully execute in the cloud, or by using locally run and locally configured rule evaluator components which execute rules and alerts against the global Monarch data store and forward any fired alerts to [Prometheus AlertManager](https://prometheus.io/docs/alerting/latest/alertmanager/).
  * Data storage is handled by Monarch, which stores all Prometheus data for 24 months at no additional cost.



Grafana connects to the global Monarch data store instead of connecting to individual Prometheus servers. If you have Managed Service for Prometheus collectors configured in all your deployments, then this single Grafana instance gives you a unified view of all your metrics across all your clouds.

## Data collection

You can use Managed Service for Prometheus in one of four modes: with [managed data collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed), with [self-deployed data collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged), with [the OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel), or with [the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus).

Managed Service for Prometheus offers an operator for managed data collection in Kubernetes environments. We recommend that you use managed collection; using it eliminates the complexity of deploying, scaling, sharding, configuring, and maintaining Prometheus servers. Managed collection is supported for both GKE and non-GKE Kubernetes environments.

With self-deployed data collection, you manage your Prometheus installation as you always have. The only difference from upstream Prometheus is that you run the Managed Service for Prometheus drop-in replacement binary instead of the upstream Prometheus binary.

The OpenTelemetry Collector can be used to scrape Prometheus exporters and send data to Managed Service for Prometheus. OpenTelemetry supports a single-agent strategy for all signals, where one collector can be used for metrics (including Prometheus metrics), logs, and traces in any environment.

You can configure the Ops Agent on any Compute Engine instance to scrape and send Prometheus metrics to the global datastore. Using an agent greatly simplifies VM discovery and eliminates the need to install, deploy, or configure Prometheus in VM environments.

If you have a Cloud Run service that writes [Prometheus metrics](https://prometheus.io/docs/concepts/metric_types/) or [OTLP metrics](https://opentelemetry.io/docs/concepts/signals/metrics/), then you can use a sidecar and Managed Service for Prometheus to send the metrics to Cloud Monitoring.

  * To collect Prometheus metrics from Cloud Run, use the [Prometheus sidecar](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cloudrun-sidecar).
  * To collect OTLP metrics from Cloud Run, use the [OpenTelemetry sidecar](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar).



You can run managed, self-deployed, and OpenTelemetry collectors in on-prem deployments and on any cloud. Collectors running outside of Google Cloud send data to Monarch for long-term storage and global querying.

When choosing between collection options, consider the following:

  * Managed collection:

    * Google's recommended approach for all Kubernetes environments.
    * Deployed by using the GKE UI, the gcloud CLI, the `kubectl` CLI, or Terraform.
    * Operation of Prometheus—generating scrape configurations, scaling ingestion, scoping rules to the right data, and so forth—is fully handled by the Kubernetes operator.
    * Scraping and rules are configured by using lightweight custom resources (CRs).
    * Good for those who want a more hands-off, fully managed experience.
    * Intuitive migration from [prometheus-operator](https://github.com/prometheus-operator) configs.
    * Supports most current Prometheus use cases.
    * Full assistance from Google Cloud technical support.
  * Self-deployed collection:

    * A drop-in replacement for the upstream Prometheus binary.
    * You can use your preferred deployment mechanism, like [prometheus-operator](https://github.com/prometheus-operator) or manual deployment.
    * Scraping is configured by using your preferred methods, like annotations or prometheus-operator.
    * Scaling and functional sharding is done manually.
    * Good for quick integration into more complex existing setups. You can reuse your existing configs and run upstream Prometheus and Managed Service for Prometheus side by side.
    * Rules and alerts typically run within individual Prometheus servers, which might be preferable for edge deployments as local rule evaluation does not incur any network traffic.
    * Might support long-tail use cases that aren't yet supported by managed collection, such as [local aggregations](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation) to reduce cardinality.
    * Limited assistance from Google Cloud technical support.
  * The OpenTelemetry Collector:

    * A single collector that can collect metrics (including Prometheus metrics) from any environment and send them to any compatible backend. Can also be used to collect logs and traces and send them to any compatible backend, including Cloud Logging and Cloud Trace.
    * Deployed in any compute or Kubernetes environment either manually or by using Terraform. Can be used to send metrics from stateless environments such as Cloud Run.
    * Scraping is configured using Prometheus-like configs in the collector's Prometheus receiver.
    * Supports push-based metric collection patterns.
    * Metadata is injected from any cloud using resource detector processors.
    * Rules and alerts can be executed using a Cloud Monitoring alerting policy or the stand-alone rule evaluator.
    * Best supports cross-signal workflows and features such as exemplars.
    * Limited assistance from Google Cloud technical support.
  * The Ops Agent:

    * The easiest way to collect and send Prometheus metric data originating from Compute Engine environments, including both Linux and Windows distros.
    * Deployed by using the gcloud CLI, the Compute Engine UI, or Terraform.
    * Scraping is configured using Prometheus-like configs in the Agent's Prometheus receiver, powered by OpenTelemetry.
    * Rules and alerts can be executed using Cloud Monitoring or the stand-alone rule evaluator.
    * Comes bundled with optional Logging agents and [process metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-processes).
    * Full assistance from Google Cloud technical support.



To get started, see [Get started with managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed), [Get started with self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged), [Get started with the OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel), or [Get started with the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus).

If you use the managed service outside of Google Kubernetes Engine or Google Cloud, some additional configuration might be necessary; see [Run managed collection outside of Google Kubernetes Engine](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed#gmp-outside-gke), [Run self-deployed collection outside of Google Cloud](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged#gmp-outside-gcp), or [Add OpenTelemetry processors](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel#add-processors).

## Query evaluation

Managed Service for Prometheus supports any query UI that can call the Prometheus query API, including Grafana and the Cloud Monitoring UI. Existing Grafana dashboards continue to work when switching from local Prometheus to Managed Service for Prometheus, and you can continue using PromQL found in popular open-source repositories and on community forums.

You can use PromQL to query [over 6,500 free metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp) in Cloud Monitoring, even without sending data to Managed Service for Prometheus. You can also use PromQL to query [free Kubernetes metrics](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes), [custom metrics](https://docs.cloud.google.com/monitoring/custom-metrics) and [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics).

For information on how to configure Grafana to query Managed Service for Prometheus data, see [Query using Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query).

For information on how to query Cloud Monitoring metrics using PromQL, see [PromQL in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

## Rule and alert evaluation

Managed Service for Prometheus provides both a fully cloud-based alerting pipeline and a stand-alone rule evaluator, both of which evaluate rules against all Monarch data accessible in a [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope). Evaluating rules against a multi-project metrics scope eliminates the need to co-locate all data of interest on a single Prometheus server or within a single Google Cloud project, and it lets you set IAM permissions on groups of projects.

Because all rule evaluation options accept the standard Prometheus `rule_files` format, you can easily migrate to Managed Service for Prometheus by copy-pasting existing rules or by copy-pasting rules found in popular open source repositories. For those using self-deployed collectors, you can continue to evaluate recording rules locally in your collectors. The results of recording and alerting rules are stored in Monarch, just like directly collected metric data. You can also migrate your Prometheus alerting rules to PromQL-based alerting policies in Cloud Monitoring.

For alert evaluation with Cloud Monitoring, see [PromQL alerts in Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql/promql-in-alerting).

For rule evaluation with managed collection, see [Managed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-managed).

For rule evaluation with self-deployed collection, the OpenTelemetry Collector, and the Ops Agent, see [Self-deployed rule evaluation and alerting](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/rules-unmanaged).

For information on reducing cardinality using recording rules on self-deployed collectors, see [Cost controls and attribution](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls#local-aggregation).

## Data storage

All Managed Service for Prometheus data is stored for 24 months at no additional cost.

Managed Service for Prometheus supports a minimum scrape interval of 5 seconds. Data is stored at full granularity for 1 week, then is downsampled to 1-minute points for the next 5 weeks, then is downsampled to 10-minute points and stored for the remainder of the retention period.

Managed Service for Prometheus has no limit on the number of active time series or total time series.

For more information, see [Quotas and limits within the Cloud Monitoring documentation](https://docs.cloud.google.com/monitoring/quotas).

## Billing and quotas

Managed Service for Prometheus is a Google Cloud product, and billing and usage quotas apply.

### Billing

Billing for the service is based primarily on the number of metric samples ingested into storage. There is also a nominal charge for read API calls. Managed Service for Prometheus does not charge for storage or retention of metric data.

  * For current pricing, see the Cloud Monitoring sections of the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.
  * To estimate your bill based on your expected number of time series or your expected samples per second, see the Cloud Operations tab within the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).
  * For tips on how to lower your bill or determine the sources of high costs, see [Cost controls and attribution](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/cost-controls).
  * For information about the rationale for the pricing model, see [Optimize costs for Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/observability/pricing-optimize-and-monitor#sample-pricing-rationale).
  * For pricing examples, see [Metric data charged by samples ingested](https://cloud.google.com/stackdriver/observability-pricing-examples#pricing_examples_samples).



### Quotas

Managed Service for Prometheus shares ingest and read quotas with Cloud Monitoring. The default ingest quota is 500 QPS per project with up to 200 samples in a single call, equivalent to 100,000 samples per second. The default read quota is 100 QPS per [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope).

You can increase these quotas to support your metric and query volumes. For information about managing quotas and requesting quota increases, see [Working with quotas](https://docs.cloud.google.com/docs/quota).

### Terms of Service and compliance

Managed Service for Prometheus is part of Cloud Monitoring and therefore inherits certain agreements and certifications from Cloud Monitoring, including (but not limited to):

  * The [Google Cloud terms of service](https://cloud.google.com/terms/services)
  * The [Operations Service Level Agreement (SLA)](https://cloud.google.com/operations/sla)
  * [US DISA](https://cloud.google.com/security/compliance/disa) and [FedRAMP](https://cloud.google.com/security/compliance/fedramp) compliance levels
  * [VPC-SC (VPC Service Controls)](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_monitoring) support



## What's next

  * Get started with [managed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-managed).
  * Get started with [self-deployed collection](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-unmanaged).
  * Get started with [the OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/setup-otel).
  * Get started with [the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus).
  * [Use PromQL in Cloud Monitoring to query Prometheus metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query-cm).
  * [Use Grafana to query Prometheus metrics](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query).
  * [Query Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/promql) using PromQL.
  * Read up on [best practices and view architecture diagrams](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/best-practices/ingest-and-query).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
