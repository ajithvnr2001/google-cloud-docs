---
url: https://docs.cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane/
title: Monitor on-premises resources with BindPlane \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:15.062615+00:00
---

# Monitor on-premises resources with BindPlane  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/monitoring-on-premises-resources-with-bindplane/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Monitor on-premises resources with BindPlane Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-02 UTC

This document is one part of a two-part series on extending Cloud Logging and Cloud Monitoring to include on-premises infrastructure and apps.

  * [Log on-premises resources with BindPlane](https://docs.cloud.google.com/architecture/logging-on-premises-resources-with-bindplane): Read about how Cloud Logging supports logging from on-premises resources.
  * Monitor on-premises resources with BindPlane (this document): Read about how Cloud Monitoring supports monitoring of on-premises resources.



You might consider using Logging and Monitoring for logging and monitoring of your on-premises resources for the following reasons:

  * You need a temporary solution as you move infrastructure to Google Cloud and you want to monitor your on-premises resources until they're decommissioned.
  * You might have a diverse computing environment with multiple clouds and on-premises resources.



In either case, with the Logging and Monitoring APIs and [BindPlane](https://bindplane.com/), you can gain visibility into your on-premises resources. This document is intended for DevOps practitioners, managers, and executives who are interested in a monitoring strategy for resources in Google Cloud and their remaining on-premises infrastructure and apps.

## Ingesting metrics with Monitoring

You can get metrics into Monitoring in the following two ways:

  * Use BindPlane from observIQ to ingest metrics from your on-premises or other cloud sources.
  * Use OpenCensus to write to the Cloud Monitoring API.



### Using BindPlane to ingest metrics

The following diagram shows the architecture of how BindPlane collects metrics and then how these metrics are ingested into Monitoring.

![Architecture of using Monitoring and BindPlane to monitor on-premises resources.](https://docs.cloud.google.com/static/architecture/images/monitoring-on-premises-resources-with-stackdriver-and-blue-medora-1-architecture-monitoring-bindplane.svg)

observIQ offers several versions of BindPlane: BindPlane for Google, self-hosted, SaaS, and Enterprise. For more information about these versions, see the [BindPlane documentation page](https://docs.bindplane.com/).

Advantages:

  * Requires configuration, not instrumentation of your apps, which reduces time to implement.
  * Included in the cost of using [Monitoring](https://cloud.google.com/stackdriver/pricing).
  * Supported configuration by Monitoring product and support.
  * Can extend to metrics not provided by the default configuration.



Disadvantages:

  * Requires the use of the observIQ BindPlane agent to relay metrics to Monitoring, which can add complexity to the overall system.



This option is the recommended method because it requires the lowest amount of effort. This solution requires configuration rather than development.

### Using OpenCensus to write to the Monitoring API

The following diagram shows the architecture of how OpenCensus collects metrics and how these metrics are ingested into Monitoring.

![Architecture of using Monitoring API to monitor on-premises resources directly.](https://docs.cloud.google.com/static/architecture/images/monitoring-on-premises-resources-with-stackdriver-and-blue-medora-2-architecture-monitoring-directly.svg)

Using the Monitoring API directly means that you need to add instrumentation code to your apps to send metrics directly to the API. You can do this directly by [using the Monitoring API to write metrics](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#writing-ts) or by instrumenting your app with the [Monitoring exporter for OpenCensus](https://opencensus.io/exporters/supported-exporters/python/stackdriver/). OpenCensus is an open source project that defines a standard data structure for traces and metrics. Using OpenCensus has the advantage of supporting multiple backends, including Monitoring. Using OpenCensus also implements all the low-level technical details of using the Monitoring API.

Advantages:

  * Provides flexibility because the instrumentation required is easily implemented with the use of the OpenCensus Exporter



Disadvantages:

  * Requires a separate solution for infrastructure metrics by writing a custom agent.
  * Requires app instrumentation, which might mean higher cost to implement.
  * Requires open source libraries.



This option isn't the recommended method because it requires the highest amount of effort and doesn't cover infrastructure metrics.

## Using BindPlane

This document covers using BindPlane from observIQ to ingest metrics into Monitoring. The BindPlane service works by defining a series of sources, ingesting those metrics, and then sending the metrics to Monitoring as the destination. BindPlane supports agents that run on [select versions](https://docs.bindplane.com/how-to-guides#cloud-and-platform-integrations) of Windows, Linux, and Kubernetes.

### Sources, agents, destinations, and processors

BindPlane has the following features:

  * **[Sources](https://docs.bindplane.com/integrations/sources)** : Items that generate metrics such as Google Kubernetes Engine (GKE), Amazon Elastic Container Service for Kubernetes (Amazon EKS), or Microsoft Azure Container Service.
  * **[Agents](https://docs.bindplane.com/going-to-production/bindplane-agent)** : Lightweight processes that remotely monitor your environment and forward metric data to BindPlane.
  * **[Destinations](https://docs.bindplane.com/integrations/destinations)** : Services that BindPlane forwards the metrics. In this case, the destination is the process on BindPlane that uses the Monitoring API to write metrics to Monitoring.
  * **[Processors](https://docs.bindplane.com/integrations/processors)** : Configurations that can transform your data before it arrives at your destination. This includes adding attributes, filtering, and converting logs to metrics.



For more detailed information about sources, agents, destinations, and processors, see the [BindPlane QuickStart Guide](https://docs.bindplane.com/#quickstart).

### Example use case

As an example, ExampleOrganization has resources deployed to Google Cloud, Microsoft Azure, and on-premises resources deployed by using vSphere. In Google Cloud, there is a GKE cluster and a demo app deployed, which runs the company's website. In the Microsoft Azure environment, Azure Kubernetes Service (AKS) is running a set of microservices, providing a REST API endpoint to external developers. In the vSphere environment, MySQL, Oracle, and Microsoft SQL Server support several corporate apps.

With resources in each environment, ExampleOrganization wants to monitor each component regardless of where the component is deployed. Sending the metrics from each environment to Logging and Monitoring by using BindPlane brings all the metrics into a single location for monitoring and alerting purposes.

### Send metrics from BindPlane to Monitoring

After BindPlane is set up and begins sending metrics, those metrics are sent to your Monitoring Workspace. You can then use Monitoring to view, configure, alert, and build dashboards from the time series like you can for any metrics or time series in Monitoring. For more information, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

### Use metrics in Monitoring

In the previous example, BindPlane was configured to send metrics from Google Cloud, Microsoft Azure, and on-premises sources. The following three metrics appear in Monitoring:

  * GKE cluster metrics
  * AKS cluster metrics
  * vSphere on-premises database metrics



#### GKE cluster metrics

If you have GKE clusters set up, the GKE cluster metrics appear in the [Kubernetes Clusters page](https://console.cloud.google.com/kubernetes/list/overview) or [Kubernetes Workloads page](https://console.cloud.google.com/kubernetes/workload/overview). You can see multiple views of the Kubernetes components running in Monitoring. The metrics, logs, and configuration are available for each pod.

For details, see [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

#### AKS cluster metrics

In the same [Monitoring](https://console.cloud.google.com/monitoring) environment, metrics for AKS are collected. The metrics appear in Monitoring and can be used for any purposes in Monitoring including dashboards, alerting, and the Metrics Explorer.

The [Metrics Explorer page](https://console.cloud.google.com/monitoring/metrics-explorer) provides a way to find, filter, and build charts from metrics. Note that the metrics sent in by BindPlane have the `workload.googleapis.com/THIRD_PARTY_APP_NAME` prefix for the metric name.

The Metrics Explorer can produce a chart for the metric. For more information about charts, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

Like all metrics in Monitoring, you can use these metrics to build dashboards that display multiple charts. The dashboard can represent metrics produced by AKS, collected by BindPlane, and stored in Monitoring. For more information about dashboards, see [View and customize Google Cloud dashboards](https://docs.cloud.google.com/monitoring/charts/predefined-dashboards).

#### vSphere on-premises cluster metrics

The last part of this example includes database metrics from vSphere. The metrics from vSphere appear in Monitoring and can be used in the same way as any other metric in Monitoring. The Oracle metrics from vSphere appear in the list of metrics on the [Metrics Explorer page](https://console.cloud.google.com/monitoring/metrics-explorer).

Like all metrics in Monitoring, metrics can be used to build alerts. The alert can represent metrics produced by Oracle running in vSphere, collected by BindPlane, stored in Monitoring. For more information about alerts, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

## Conclusion

Monitoring provides dashboards, alerting, and incident response for you to get insights into your platforms. Together, Monitoring and BindPlane provide you the ability to gain visibility into your on-premises resources.

## What's next

  * [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring)
  * [BindPlane QuickStart Guide](https://docs.bindplane.com/#quickstart)
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-02 UTC."],[],[]] 
