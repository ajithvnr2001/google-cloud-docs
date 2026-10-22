---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/
title: Ops Agent overview \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:12.122740+00:00
---

# Ops Agent overview  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Ops Agent overview Stay organized with collections  Save and categorize content based on your preferences. 

The Ops Agent is the primary agent for collecting telemetry from your Compute Engine instances. Combining the collection of logs, metrics, and traces into a single process, the Ops Agent uses [Fluent Bit](https://fluentbit.io/) for logs, which supports high-throughput logging, and the [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/) for metrics and traces.

For information about installing the Ops Agent, see the following:

  * For Compute Engine instances, see [Installing the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index).
  * For Bare Metal Solution servers, see [Set up Ops Agent for Bare Metal Solution](https://docs.cloud.google.com/bare-metal/docs/set-up-ops-agent-for-bms).



### Ops Agent features

Overall features include: 

  * Single download and installation/upgrade process.
  * Simple, unified, YAML-based configuration.
  * Support for standard Linux and Windows distros.
  * Proxy support.



#### Logging features

Logging features include:

  * Improved performance compared to the legacy Logging Agent:

    * High throughput capability, taking full advantage of multi-core architecture.
    * Efficient resource (e.g. memory, CPU) management.
  * Collecting logs from [various sources](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-receivers):

    * Standard system logs (`/var/log/syslog` and `/var/log/messages` for Linux, Windows Event Log) collected with no configuration.
    * File-based logs with customizable paths and refresh interval.
    * Journald daemon / systemd logs.
    * Logs over TCP protocol.
    * Logs over Forward protocol (used by Fluent Bit and Fluentd).
  * Flexible processing:

    * Parse text logs into structured logs: [JSON-based](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processor-parse-json) and [regular-expression-based](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processor-parse-regex) parsing.
    * [Modify](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processor-modify-fields) log entries by removing, renaming, or setting fields.
    * [Exclude](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processor-exclude-logs) logs based on labels and regular expressions.
    * Detect and concatenate [multiline](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#logging-processor-parse-multiline) language-exception logs from Java, Python, and Golang.
  * Third-party application support

    * Curated third-party application log integration that recognizes common app log file paths and formats.



#### Monitoring features

Monitoring features include:

  * System metrics collected with no configuration. Metrics collected include: 
    * [cpu metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-cpu)
    * [disk metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-disk)
    * [iis metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-iis) (Windows only)
    * [interface metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-interface)
    * [gpu metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu) (Linux only)
    * [memory metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-memory)
    * [mssql metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-mssql) (Windows only)
    * [pagefile metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-pagefile) (Windows only)
    * [swap metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-swap)
    * [network metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-network)
    * [processes metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-processes)
    * [agent self metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-agent):
  * Third-party application support 
    * Curated [integrations for third-party application metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party), which collect common app metrics and offer sample dashboards and alert policies.


  * Collection of [ Prometheus metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/prometheus) from applications running on Compute Engine.
  * Collection of [ OpenTelemetry Protocol (OTLP) metrics and traces](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/otlp) from applications instrumented with [OpenTelemetry SDKs](https://opentelemetry.io/docs/instrumentation/).
  * Collection of [ NVIDIA Data Center GPU Manager (DCGM) metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party-nvidia).

**Note:** Some metrics are only available on VMs running on Linux. See detailed metrics definition and whether they are Linux only in the [agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent) page.

The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

  * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
  * Data about labels and cardinality of metrics.
  * Number of reads for each metric.
  * Use of metrics in alerting policies and custom dashboards.
  * Rate of metric-write errors.



You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

#### Trace features

Trace features include:

  * Collection of [OpenTelemetry Protocol (OTLP) traces](https://docs.cloud.google.com/trace/docs/otlp) from applications instrumented with [OpenTelemetry SDKs](https://opentelemetry.io/docs/instrumentation/).



### Virtual machine instances

You can install the Ops Agent on [Compute Engine](https://docs.cloud.google.com/compute/docs) instances. To create a Compute Engine instance, see the [Compute Engine getting started guide](https://docs.cloud.google.com/compute/docs/quickstart).

**Note:** The Ops Agent is not supported on Amazon Elastic Compute Cloud (Amazon EC2) instances or on-premises machines. 

### Operating systems

The Ops Agent supports the following operating systems on compatible VM instances. For information about Arm VM instances, see Support for Compute Engine Arm VMs.

#### Linux operating systems

The agent supports the following Linux operating systems:

**Note:** To use Cloud Logging on VMs with Container-Optimized OS, follow [Using Cloud Logging with Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs/how-to/logging) instead.

  * Rocky Linux 8
  * Rocky Linux 9
  * Rocky Linux 10
  * RHEL 8: rhel-8, rhel-8-6-sap-ha, rhel-8-8-sap-ha, rhel-8-10-sap-ha
  * RHEL 9: rhel-9
  * RHEL 10: rhel-10
  * CentOS Stream 10
  * Debian 12 (Bookworm)
  * Debian 13 (Trixie)
  * Ubuntu 22.04 LTS (Jammy Jellyfish): ubuntu-2204-lts, ubuntu-minimal-2204-lts
  * Ubuntu 24.04 LTS (Noble Numbat): ubuntu-2404-lts-amd64, ubuntu-minimal-2404-lts-amd64
  * Ubuntu 26.04 LTS (Resolute Raccoon): ubuntu-2604-lts-amd64, ubuntu-minimal-2604-lts-amd64
  * SLES 12: sles-12, sles-12-sp5-sap
  * SLES 15: sles-15, sles-15-sp3-sap, sles-15-sp4-sap, sles-15-sp5-sap, sles-15-sp6-sap



##### Support for Compute Engine Arm VMs

The Ops Agent supports Compute Engine [C4A and Tau T2A Arm](https://docs.cloud.google.com/compute/docs/general-purpose-machines) VM instances. The Ops Agent is supported for Arm VMs on the following OS images:

  * Debian 12 (Bookworm): Ops Agent version 2.44.0
  * Debian 13 (Trixie): Ops Agent version 2.61.0
  * Ubuntu 22.04 LTS (Jammy Jellyfish): Ops Agent version 2.42.0
  * Ubuntu 24.04 LTS (Noble Numbat): Ops Agent version 2.47.0
  * Ubuntu 26.04 LTS (Resolute Raccoon): Ops Agent version 2.70.0
  * RHEL 9: Ops Agent version 2.40.0
  * RHEL 10: Ops Agent version 2.64.0
  * Rocky Linux 8: Ops Agent version 2.51.0
  * Rocky Linux 9: Ops Agent version 2.40.0
  * Rocky Linux 10: Ops Agent version 2.64.0
  * CentOS Stream 10: Ops Agent version 2.64.0
  * SLES 15: Ops Agent version 2.43.0



The Ops Agent is supported on a subset of the images supported by Compute Engine. For more information about Compute Engine Arm VMs, see [Creating and starting an Arm VM instance](https://docs.cloud.google.com/compute/docs/instances/create-arm-vm-instance).

#### Windows operating systems

**Note:** `n1-standard-1` virtual machines are too small to run Windows and the Ops Agent, so you must use a larger VM.

The agent supports the following Windows operating systems:

  * Windows Server: windows-2016, windows-2019, windows-2022, windows-2025
  * Windows Server Core: windows-2016-core, windows-2019-core, windows-20h2-core, windows-2022-core, windows-2025-core



### Agent access requirements

Installing the agent requires access to the following DNS names:

  * Google Cloud package repository: `packages.cloud.google.com`

  * Google downloads subdomain: `dl.google.com`




Running the agent requires access to the following DNS names:

  * OAuth2 token server: `oauth2.googleapis.com`

Earlier versions of the agent may require access to `www.googleapis.com` (full URL: `https://www.googleapis.com/oauth2/v3/token`).

If you're using an older version of the agent, it's recommended that you [upgrade your agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#upgrade) to the latest version.

  * Monitoring APIs: `monitoring.googleapis.com`

  * Logging APIs: `logging.googleapis.com`




The agent uses TCP ports within the VM for inter-process communication. The following ports, which don't need to be open externally, must be available to the agent on your VM:

  * 20201

  * 20202




## Unsupported managed environments

The following types of VM instances belong to managed services that implement service-specific Monitoring support. Don't try to manually install or configure the Ops Agent on them: 

  * App Engine standard has built-in Monitoring support. Agents aren't needed. 
  * App Engine flexible environment instances have pre-installed agents with service-specific configurations. 
  * [Dataflow](https://docs.cloud.google.com/dataflow/docs) instances have pre-installed legacy monitoring agents with service-specific configurations. 
  * [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs) instances prior to image version 2.2 have pre-installed legacy monitoring agents with service-specific configurations.

You can install the [ Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) on Managed Service for Apache Spark clusters that use image version 2.2 and later to collect syslog logs and host metrics. For more information, see [ Managed Service for Apache Spark 2.2.x release versions](https://docs.cloud.google.com/dataproc/docs/concepts/versioning/dataproc-release-2.2).

  * Google Kubernetes Engine node instances: 
    * [GKE on Google Cloud](https://docs.cloud.google.com/kubernetes-engine/docs) clusters are configured to [collect logs and metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke) with Logging and Monitoring by default. You can also configure metric and log collection for existing container clusters. For information, see [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing). 
    * [Google Distributed Cloud](https://docs.cloud.google.com/anthos/gke/docs/on-prem) instances have an integrated logging and monitoring solution that collects status about system components. For information, see [ Logging and monitoring](https://docs.cloud.google.com/anthos/gke/docs/on-prem/concepts/logging-and-monitoring). 



## Support policy

The Ops Agent is supported according to the [support time horizons policy](https://docs.cloud.google.com/stackdriver/docs/support-info/telemetry-agents).

## Pricing

If you install the Ops Agent, then you might be charged for the metrics, logs, or traces that the agent sends to your Google Cloud project. For pricing information, see [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing). 

To collect OpenTelemetry Protocol (OTLP) traces, you must configure the agent to collect traces from an instrumented application; for more information, see [Collect (OTLP) traces with the Ops Agent](https://docs.cloud.google.com/trace/docs/otlp).

## What's next

  * To install the Ops Agent, see [Installing the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
