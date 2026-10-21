---
url: https://docs.cloud.google.com/monitoring/agent/plugins/bindplane-transition/
title: Transition guide for deprecated third-party integrations \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.508144+00:00
---

# Transition guide for deprecated third-party integrations  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/bindplane-transition/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Transition guide for deprecated third-party integrations Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

Cloud Monitoring provides integrations for [monitoring third-party applications](https://docs.cloud.google.com/monitoring/agent/plugins), but support for some of these integrations has been deprecated. For information about which integrations were deprecated, go to the [deprecation guide for third-party integrations](https://docs.cloud.google.com/stackdriver/docs/deprecations/third-party-apps).

This guide provides the steps to transition these integrations to [BindPlane](https://docs.bindplane.bluemedora.com/docs/), a solution provided by Monitoring partner, [Blue Medora](https://bluemedora.com).

Cloud Monitoring offers BindPlane at no additional cost to Monitoring customers, but metrics collected through BindPlane are charged at standard custom metric rates. For information on the cost of this added consumption, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). You might also review the managing your costs section of this document.

**About BindPlane from Blue Medora:** BindPlane is a service that connects the health, performance data, and logs of over [ 150 data sources](https://docs.bindplane.bluemedora.com/docs/) directly into Monitoring. These data sources provide an alternative to the deprecated integrations, as well as adding support for new use cases, such as databases, Microsoft Windows, on-premise or hosted data centers, and hybrid cloud in Azure and AWS. See [ this video](https://www.youtube.com/watch?v=GNb3y0aQ41U) for a quick introduction to BindPlane. For more information about Blue Medora, see [ About Blue Medora](https://docs.cloud.google.com/stackdriver/blue-medora). 

## Uninstalling the plugin for the third-party integration

Uninstall the plugin for the third-party integration by logging into each host and removing the configuration for each plugin instance.

## Installing the BindPlane integration

The following sections provide details on installing and configuring BindPlane with Cloud Monitoring.

### Creating a BindPlane account

To get started, create an [account with BindPlane](https://bindplane.bluemedora.com/sign_up/stackdriver). After receiving an account-verification message, you can continue with the remainder of these procedures.

### Connecting BindPlane to Cloud Monitoring

To connect to Monitoring, add a destination. In this case, your destination is **Stackdriver**. The most up-to-date information on linking your Monitoring account with BindPlane can be found at Blue Medora's [guide for configuring a destination](https://docs.bindplane.bluemedora.com/docs/google-stackdriver) guide.

### Installing the BindPlane collector

[BindPlane collectors](https://docs.bindplane.bluemedora.com/docs/getting-started-1#section--install-a-collector-) reside within your network and connect to any data source that you want to monitor. The collector requires a server with network access to the data sources you're planning to monitor.

**Note:** To continue sending metrics to the agent namespace, `agent.googleapis.com`, you must install the collector on the host system of the technology being monitored. If the collector is not installed on the host system, metrics are still sent to Monitoring, but to a separate, external namespace, `external.googleapis.com/bluemedora/generic_node/`. As a result, existing dashboards and alerts may not function correctly since the namespace of the underlying metrics changed.

To install the collector, complete the following steps:

  1. In BindPlane, navigate to **Collectors**.

  2. Click **Add Collector**.

  3. Select your host system's operating system.

  4. Click the **Clipboard** icon to copy the installation command.

  5. Log into the host system you want to install the collector on and paste and run the command.




You can also install the collector through Google Deployment Manager. For instructions and security requirements on this deployment, refer to the [GCP Collector Deployments](https://docs.bindplane.bluemedora.com/docs/gcp-collector-deployments) guide.

### Connecting to a data source

A source is any object you want to monitor. It could be a database, a web service, or even a hardware device in your data center. To add a source, complete the following steps:

  1. In BindPlane, navigate to **Sources**.

  2. Click **Add Source**.

  3. Select which type of source you want to monitor.

  4. Select the collector you installed on the host system.

  5. Enter your credentials and click **Test Connection** to verify that your connection is working correctly.

  6. Optionally, you can review the metrics that are configured to be sent to Monitoring and turn off any metrics that you don't need. Turning off these metrics can help you manage costs.

  7. Click **Add** to begin monitoring. To see what credentials each source requires or for other information, refer to the [source documentation](https://docs.bindplane.bluemedora.com/docs/).




### Transferring existing dashboards and alerts

After installing the collector and connecting to a data source, your existing dashboards and alerts continue to work as they did previously.

If you have any issues, such as missing data, ensure the following conditions are met:

  * The collector is installed on the host system of the technology you're trying to monitor.

  * The data source is in a healthy state in BindPlane.




## Managing your costs

Google has partnered with Blue Medora to bring BindPlane to Monitoring customers at no additional cost, licenses, or contracts. However, if you ingest more monitoring data and log data through Blue Medora than you did through the Monitoring agents, you might incur higher usage fees. For information on pricing, which applies to all custom metrics and logs over the free quota, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

To help manage your costs, BindPlane lets you to control how much data is sent to Monitoring in two ways:

  * **Tune your collection intervals** : Collection intervals are set to 1 minute by default. Increasing the collection interval to 2 minutes would send half as much data to Monitoring for the given source. Increasing the interval to 10 minutes would send one-tenth as much data. Tuning the data collection interval lets you to find the balance between data resolution and cost that is right for your organization.

To tune this interval, on the **Sources** detail page, click **Configure** and then update the **Collection interval** field.

  * **Disable the collection of unneeded metrics** : When a source is configured, collection is enabled for all resource types and metrics. If you don't need a specific resource type or individual metric sent to Cloud Monitoring, then you can disable them to reduce the amount of data sent, reducing your costs.

To disable unneeded metrics, on the **Sources** detail page, click **Metrics** and disable metrics collection by clicking the **Collect** toggle.




## Metrics guide

In addition to the metrics previously collected by the Monitoring agent, the Bindplane integration collects additional metrics, expanding the number of metrics collected for each technology. These additional metrics are sent to the `external.googleapis.com/bluemedora/generic_node/` namespace. Deprecated Monitoring agent metrics that are now collected by the equivalent BindPlane integrations are sent to the `agent.googleapis.com` namespace.

The following table lists the number of metrics collected by the Cloud Monitoring agent and the number of additional metrics available from BindPlane.

Integration name | Cloud Monitoring metrics | BindPlane metrics  
---|---|---  
Cassandra | [7 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-cassandra) | [257 metrics](https://docs.bindplaneoriginal.observiq.com/docs/all-metrics-cassandra)  
Elasticsearch | [18 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-elasticsearch) | [160 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-elasticsearch)  
HBase | [23 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-hbase) | [200 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-hbase)  
Kafka | [18 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-kafka) | [100 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-kafka)  
MongoDB | [12 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-mongodb) | [90 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-mongodb)  
PostgreSQL | [7 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-postgresql) | [100 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-postgresql)  
RabbitMQ | [4 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-rabbitmq) | [100 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-rabbitmq)  
Tomcat | [ 7 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-tomcat) | [100 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-tomcat)  
Varnish | [3 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-varnish) | [170 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-varnish)  
ZooKeeper | [14 metrics](https://docs.bindplane.bluemedora.com/docs/stackdriver-agent-migration-zookeeper) | [30 metrics](https://docs.bindplane.bluemedora.com/docs/all-metrics-zookeeper)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
