---
url: https://docs.cloud.google.com/monitoring/agent/monitoring/
title: Monitoring agent overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:17:42.795734+00:00
---

# Monitoring agent overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Monitoring agent overview Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). **Caution:** The 5.x version of the Monitoring agent has been [deprecated and decommissioned](https://docs.cloud.google.com/stackdriver/docs/deprecations/mon-agent). For information about the latest agent versions, see [Listing all agent versions](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#list-versions).

The Monitoring agent is a [collectd](https://collectd.org/)-based daemon that gathers system and application metrics from virtual machine instances and sends them to Monitoring. By default, the Monitoring agent collects disk, CPU, network, and process metrics. You can configure the Monitoring agent to monitor [third-party applications](https://docs.cloud.google.com/monitoring/agent/plugins) to get the [full list of agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent).

To install the agent, see [Installing the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/install-index).

**Note:** If your [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) is configured with a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) Service Perimeter for the Monitoring API, then the Monitoring agent won't work on any virtual machine instance outside the perimeter. To learn more about Service Perimeters, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters). 

## Purpose

Using the Monitoring agent is optional but recommended. Monitoring can access some instance metrics without the Monitoring agent, including CPU utilization, some disk traffic metrics, network traffic, and uptime information. Monitoring uses the Monitoring agent to access additional system resources and application services in virtual machine (VM) instances. If you want these additional capabilities, you should install the Monitoring agent.

**Note:** The Monitoring agent is designed to ingest system, third-party, custom, and agent telemetry metrics. Some of these metrics are chargeable. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing).

After installing the Monitoring agent, you can monitor supported third-party applications by adding application-specific `collectd` configurations. See [Monitoring third-party applications](https://docs.cloud.google.com/monitoring/agent/plugins) for details.

For a complete list of the built-in metrics you can get with the Monitoring agent, see [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-agent).

To send any custom metric to Monitoring using the agent, see [Monitoring custom applications](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent). If you have access to the source code of your application, it may be more convenient to instrument it with OpenTelemetry. For information about instrumentation, see [Instrumentation and observability](https://docs.cloud.google.com/stackdriver/docs/instrumentation/overview).

## Supported configurations

The Monitoring agent is compatible with the following environments.

### Virtual machine instances

You can install the Monitoring agent on the following kinds of VM instances:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs) instances. The Monitoring agent sends monitoring information to each instance's associated project.

For instances without external IP addresses, you must [enable Private Google Access](https://docs.cloud.google.com/compute/docs/private-google-access/configure-private-google-access) to allow the Monitoring agent to send metrics.

To create a Compute Engine instance, see [Compute Engine getting started guide](https://docs.cloud.google.com/compute/docs/quickstart).


**Note:** The Monitoring agent is not supported on on-premises machines. 

The following types of VM instances belong to managed services that implement service-specific Monitoring support. Don't try to manually install or configure the Monitoring agent on them: 

  * App Engine standard has built-in Monitoring support. Agents aren't needed. 
  * App Engine flexible environment instances have pre-installed agents with service-specific configurations. 
  * [Dataflow](https://docs.cloud.google.com/dataflow/docs) instances have pre-installed Monitoring agents with service-specific configurations. 
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) instances prior to image version 2.2 have pre-installed Monitoring agents with service-specific configurations.

You can install the [ Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent) on Managed Service for Apache Spark clusters that use image version 2.2 and later to collect syslog logs and host metrics. For more information, see [ Managed Service for Apache Spark 2.2.x release versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.2).

  * Google Kubernetes Engine node instances: 
    * [GKE on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs) clusters are configured to [collect logs and metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke) with Logging and Monitoring by default. You can also configure metric and log collection for existing container clusters. For information, see [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing). 
    * [Google Distributed Cloud](https://docs.cloud.google.com/anthos/gke/docs/on-prem) instances have an integrated logging and monitoring solution that collects status about system components. For information, see [ Logging and monitoring](https://docs.cloud.google.com/anthos/gke/docs/on-prem/concepts/logging-and-monitoring). 



### Operating systems

The Monitoring agent supports the following operating systems on compatible VM instances.

#### Linux operating systems

The Monitoring agent supports the following Linux operating systems:

  * Rocky Linux 8
  * RHEL 8: rhel-8-6-sap-ha, rhel-8-8-sap-ha
  * SLES 12: sles-12-sp5-sap
  * SLES 15: sles-15-sp5, sles-15-sp3-sap, sles-15-sp4-sap, sles-15-sp5-sap



The Monitoring agent does not presently support the Container-Optimized OS that is the default in Google Kubernetes Engine clusters.

#### Windows operating systems:

All versions of the Monitoring agent support the following Windows operating systems:

  * Windows Server 2019
  * Windows Server Core 2019
  * Windows Server 2016
  * Windows Server Core 2016



The Monitoring agent does not presently support Windows Server Core 2019 for containers.

### Supported applications

You can configure Monitoring to monitor a variety of popular open source software applications. Configuration is only possible for agents running on Linux. Agents running on Windows can monitor IIS and MS SQL applications, but they are not configurable for other applications.

For more information, see [Monitoring third-party applications](https://docs.cloud.google.com/monitoring/agent/plugins).

**Note:** The interoperability of the agent and third-party plugins on SUSE Linux has not been tested. This is a known limitation.

### Agent access requirements

Running the agent requires access to the following DNS names:

  * OAuth2 token server: `oauth2.googleapis.com`

Earlier versions of the agent may require access to `www.googleapis.com` (full URL: `https://www.googleapis.com/oauth2/v3/token`).

If you're using an older version of the agent, it's recommended that you [upgrade your agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#upgrade) to the latest version.

  * Monitoring APIs: `monitoring.googleapis.com`




Installing the agent requires access to the following DNS names:

  * (Linux) Google Cloud package repository: `packages.cloud.google.com`

  * (Linux) Google downloads subdomain: `dl.google.com`

  * (Windows) Legacy Stackdriver download server: `repo.stackdriver.com`




## Getting the Monitoring agent source code

The source code for the Monitoring agent is available for only the Linux-hosted Monitoring agent. The Windows-hosted Monitoring agent is not open source.

The Monitoring agent is installed by a script described in the [installation instructions](https://docs.cloud.google.com/monitoring/agent/monitoring/installation). You can skip this section if you only want to install and use the agent. If you want to understand the source code, then read this section.

The Monitoring agent, `stackdriver-agent`, is based on the original [collectd](http://www.collectd.org/) system statistics collection daemon. `stackdriver-agent` source code is available at [Stackdriver/collectd](https://github.com/Stackdriver/collectd). The build and packaging scripts for the Monitoring agent are available at [Stackdriver/agent-packaging](https://github.com/Stackdriver/agent-packaging). The configuration files for third-party applications are in the agent's [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs).

The software package for `stackdriver-agent` contains:

  * The collectd daemon.
  * The plugin shared libraries, including the Cloud Monitoring API output plugin.
  * The top-level configuration files for the Monitoring agent.



## Deprecation policy

The Monitoring agent is subject to the [Agents deprecation policy](https://docs.cloud.google.com/stackdriver/docs/agent-deprecation-policy).

For deprecation information for legacy features and versions, refer to [Google Cloud Observability deprecations](https://docs.cloud.google.com/stackdriver/docs/deprecations).

## What's next

  * See [Quickstart](https://docs.cloud.google.com/monitoring/monitor-compute-engine-virtual-machine) to monitor a VM instance running an Apache web server. The quickstart includes installing the agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
