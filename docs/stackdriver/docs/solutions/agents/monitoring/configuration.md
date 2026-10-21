---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring/configuration/
title: Configure the Monitoring agent \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:17.457529+00:00
---

# Configure the Monitoring agent  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring/configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Configure the Monitoring agent Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent and Logging agent have reached theis end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

This page describes how to configure which built-in metrics the Monitoring agent collects from a Linux VM. The content on this page is intended for system administrators who want to modify the default configuration of the Monitoring agent.

You cannot configure the Monitoring agent when it is installed on a Windows VM.

This page doesn't describe how to configure the Monitoring agent to monitor third-party applications or how to use the agent to collect user-defined metrics. For information on those topics, see the following pages:

  * [Monitoring third party applications](https://docs.cloud.google.com/monitoring/agent/plugins)
  * [User-defined metrics from the agent](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent)



## Before you begin

If you haven't installed the Monitoring agent on a VM, see [Install the Monitoring agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring/installation#joint-install).

## Changing the default Monitoring agent configuration

To change the configuration of the Monitoring agent, do the following:

  1. Edit the Monitoring agent configuration file `/etc/stackdriver/collectd.conf`.

  2. Restart the Monitoring agent by running the following command:



    
    
           sudo service stackdriver-agent restart
    

## Stopping the collection of process metrics

For information about how to stop the collection of process metrics—the metrics with the prefix `agent.googleapis.com/processes`—see [Disable collection of process metrics](https://docs.cloud.google.com/monitoring/agent/process-metrics#disable-collection).

## Configuring reported CPU metrics

By default, the Monitoring agent reports the total CPU utilization by state for all CPUs on the VM by using the [`agent.googleapis.com/cpu/utilization`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/utilization) metric type. This behavior is specified in the configuration file by the following settings:

  * `ValuesPercentage true`
  * `ReportByCpu false`



You must modify these settings if you want the agent to report the utilization per CPU, or if you want it to report CPU usage time, [`agent.googleapis.com/cpu/usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/usage_time), metrics:

  * To configure the Monitoring agent to report the [`agent.googleapis.com/cpu/utilization`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/utilization) per CPU, do the following:

    * Leave `ValuesPercentage` at the default value of `true`.
    * Set `ReportByCpu` to `true`.
  * To configure the Monitoring agent to report the [`agent.googleapis.com/cpu/usage_time`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/usage_time) per CPU, do the following:

    * Set `ValuesPercentage` to `false`.
    * Set `ReportByCpu` to `true`.



The Monitoring agent can either report the CPU utilization or the CPU usage, but not both metrics. This is a known limitation of [collectd](https://collectd.org/wiki/index.php/Main_Page). When `ReportByCpu` is `true`, the `ValuesPercentage` field determines if the utilization or usage is reported. When `ReportByCpu` is `false`, the agent reports the CPU utilization.

## Troubleshooting

If you're having trouble installing or running the agent, see [Troubleshooting agent installation](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
