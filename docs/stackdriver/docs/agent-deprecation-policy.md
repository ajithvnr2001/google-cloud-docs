---
url: https://docs.cloud.google.com/stackdriver/docs/agent-deprecation-policy/
title: Cloud Logging and Monitoring agents deprecation policy \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:39.420979+00:00
---

# Cloud Logging and Monitoring agents deprecation policy  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/agent-deprecation-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Cloud Logging and Monitoring agents deprecation policy Stay organized with collections  Save and categorize content based on your preferences. 

This document details the deprecation policy for the following Logging and Monitoring agents and related client-side components:

  * [Legacy Cloud Logging agent](https://docs.cloud.google.com/logging/docs/agent)
  * [Legacy Cloud Monitoring agent](https://docs.cloud.google.com/monitoring/agent)
  * [Stackdriver Metadata agent](https://github.com/Stackdriver/metadata-agent/blob/master/README.md)
  * [Heapster](https://github.com/Stackdriver/heapster/blob/master/README.md) (for GKE version 1.15 and below)
  * [Cloud Monitoring-Prometheus integration](https://docs.cloud.google.com/monitoring/kubernetes-engine/prometheus)



This document does not apply to the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) or the [Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel). For information about support for these agents, see [Support time horizons for the Ops Agent and Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/support-info/telemetry-agents).

## Deprecating a release version

### Release version support

All agents and their client-side components follow the <MAJOR>.<MINOR>.<PATCH> versioning convention. For example, **stackdriver-agent 5.5.2**. A new release increments:

  * The **MAJOR** version when making backwards-incompatible changes,
  * The **MINOR** version when adding functionality in a backwards-compatible manner,
  * The **PATCH** version when making backwards-compatible bug fixes.



Supporting a version of the agent means that bugs in the agents are debugged and fixed on each of the supported platforms. Customers may need to upgrade their agent to the latest minor release of the same major version to take advantage of any bug fixes. However, they are not required to upgrade to a later major version of the agent, which may contain backward incompatible changes.

If a security issue or critical bug found in one of the supported major versions also exists in other supported major versions, the bug fix is backported to all supported major versions unless the fix is not backwards compatible. New features will not be backported.

Backwards-compatible changes, including new features or bug fixes, go to minor releases of the most recent major version at any time. Backwards-incompatible changes are incorporated into the next major release.

### Decommission

The lifespan of any major version of a Cloud Logging or Cloud Monitoring agent is at least 12 months. A major version (e.g., version N) is decommissioned 12 months after the release of the next major version (e.g., version N+1). Decommissioning a major version means that it doesn't receive any further bug fixes or minor releases. It also means that customer support is no longer available for that version. Once a version is decommissioned, the agent's installer files for that version are removed and not available to download.

Subsequent agent releases where only the minor version is updated don't reset the clock. The lifespan of any minor version follows its major version's deprecation and decommission schedule.

You will not receive a Mandatory Service Announcement (MSA) for each release. Instead, you can find the **planned decommission date** on the agent README pages.

When an environment, for example, Amazon Elastic Compute Cloud (EC2), or an operating system reaches its end of life, agent support is deprecated as well. The actual decommission happens when support for the environment or operating system ends, unless a specific decommission date has already been set for an agent. Refer to the Deprecating support for environments, operating systems, and features section of this guide for more information.

### Transition plan for existing agents and components

Versions of the agents and client-side components that existed before this deprecation policy will be available and supported at least until February 28, 2020. However, bug fixes will not be backported for these releases.

#### Click the **+** sign to see which versions of the agents and components are affected by the transition plan

Legacy Logging agent  
---  
Name| Version number  
google-fluentd | 1.6.3 and all earlier versions  
fluent-plugin-google-cloud | 0.7.4 and all earlier versions  
fluentd-catch-all-config | 1.0 and all earlier versions  
fluent-plugin-detect-exceptions | 0.0.11 and all earlier versions  
gcr.io/stackdriver-agents/stackdriver-logging-agent  | 0.8-1.6.2-1 and all earlier versions  
Legacy Monitoring agent  
---  
Name| Version number  
stackdriver-agent | 5.5.2-383 and all earlier versions  
Metadata agent  
---  
Name| Version number  
metadata | 0.0.21 and all earlier versions  
Heapster  
---  
Name| Version number  
heapster | 1.6.0-beta.1 and all earlier versions  
Prometheus Sidecar  
---  
Name| Version number  
stackdriver-prometheus-sidecar | 0.3.1 and all earlier versions  
  
To see the decommission dates for other versions of the agents and components, refer to the README page for each component.

## Deprecating support for environments, operating systems, and features

### Environments and operating systems support

Logging and Monitoring agents are binaries that are installed in client environments. Each agent supports different environment and operating system combinations. An example combination is Amazon Linux on EC2.

### Feature support

A feature refers to a unit of functionality of the agents that satisfies a requirement, represents a design decision, and/or provides a potential configuration option. An example feature would be support for ingesting metrics for a monitored resource.

### Deprecation

When support for an environment, operating system, or feature is deprecated, you will receive an MSA to announce the deprecation, including a link to this deprecation policy. The MSA is bound to the major version of the agent and component release. The decommission date for the environment, operating system, or feature is the same as the decommission date for that major version of the agent release. That major version is the last major version that supports the environment, operating system, or feature.

### Decommission

When support for an environment, operating system, or feature is decommissioned, customer support is no longer provided for that environment, operating system, or feature. An MSA will be sent out to announce the decommissioning.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
