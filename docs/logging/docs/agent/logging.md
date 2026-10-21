---
url: https://docs.cloud.google.com/logging/docs/agent/logging/
title: About the Logging agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:11:25.288278+00:00
---

# About the Logging agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  About the Logging agent Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Logging agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

This guide provides basic information about the Logging agent, an application based on [fluentd](https://www.fluentd.org/) that runs on your virtual machine (VM) instances.

In its default configuration, the Logging agent streams logs from common third-party applications and system software to Logging; review the list of [default logs](https://docs.cloud.google.com/logging/docs/agent/default-logs). You can configure the agent to stream additional logs; go to [Configure the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/configuration) for details on agent configuration and operation.

It is a best practice to run the Logging agent on all your VM instances. The agent runs under both Linux and Windows.

To install the Logging agent, see [Installing the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/install-index).

![How the Logging agent works](https://docs.cloud.google.com/static/logging/docs/images/logging-agent-operation.png)

## Supported operating systems

You can run the Logging agent on the following operating systems on compatible virtual machine (VM) instances:

  * Rocky Linux 8
  * RHEL 8: rhel-8-6-sap-ha, rhel-8-8-sap-ha
  * SLES 12: sles-12-sp5-sap
  * SLES 15: sles-15-sp6, sles-15-sp3-sap, sles-15-sp4-sap, sles-15-sp5-sap
  * Windows Server 2016, and 2019
  * Windows Server Core 2016, and 2019



If you're running [Container-Optimized OS VMs](https://docs.cloud.google.com/container-optimized-os/docs/concepts/features-and-benefits), then follow the [Container-Optimized OS instructions](https://docs.cloud.google.com/container-optimized-os/docs/how-to/logging) for collecting logs from your VMs.

## Supported environments

The Logging agent is compatible with the following environments:

  * [Compute Engine](https://docs.cloud.google.com/compute) instances. The Logging agent sends the logs to the project associated with each VM instance.

For instances without external IP addresses, you must [enable Private Google Access](https://docs.cloud.google.com/compute/docs/private-google-access/configure-private-google-access) to allow the Logging agent to send logs.


**Note:** The standard Logging agent isn't supported on on-premise machines. However, Google Distributed Cloud comes with a version of the agent already installed and ready to use.

For these VM instances, a minimum of 250 MiB of resident (RSS) memory is required to run the Logging agent, but 1 GiB is recommended. For example, at a rate of 100 1-KB-sized log entries per second, the Logging agent with default configurations consumes 5% CPU on one core and 150 MiB memory.

The following VM instances support Logging using their own software, so manually installing the Logging agent on them is not supported:

  * [App Engine](https://docs.cloud.google.com/appengine) standard environment instances. App Engine includes built-in support for Logging. For more information, go to [Writing application logs](https://docs.cloud.google.com/appengine/docs/standard/python3/writing-application-logs).

  * [App Engine](https://docs.cloud.google.com/appengine) flexible environment instances. Apps running in the App Engine flexible environment can write logs that are in addition to what is included in the App Engine standard environment. For more information, go to [Writing application logs](https://docs.cloud.google.com/appengine/docs/flexible/python/writing-application-logs).

  * [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) node instances. Log collection with Logging is enabled by default for new container clusters, or you can enable it for your existing clusters. For information, see [Configuring logging and monitoring for GKE](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/installing).

  * For instances running on [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/docs), the agent collects system logs but doesn't collect application logs.

  * [Cloud Run](https://docs.cloud.google.com/run/docs) container instances. Cloud Run includes built-in support for Logging. For more information, go to [Logging and viewing logs](https://docs.cloud.google.com/run/docs/logging).

  * [Cloud Run functions](https://docs.cloud.google.com/functions/docs) HTTP and background functions. Cloud Run functions includes built-in support for Logging.




### Support for on-premise and hybrid clouds

Google Cloud partners with [Bindplane](https://www.observiq.com) to provide logging services for [on-premise and hybrid cloud platforms](https://docs.cloud.google.com/logging/docs/bindplane/on-premise-hybrid-logging) in a consistent and predictable way. Using Bindplane, you can collect your own data and send it to Logging for analysis. [Bindplane](https://bindplane.com/solutions#product-matrix) integrates with Cloud Logging to capture data from your infrastructure and is included with your project at no additional cost.

For more information about Bindplane and Bindplane, see [About Bindplane and Bindplane](https://docs.cloud.google.com/stackdriver/bindplane).

## Agent access requirements

Running the agent requires access to the following DNS names:

  * OAuth2 token server: `oauth2.googleapis.com`

Older versions of the agent may require access to `www.googleapis.com` (full URL: `https://www.googleapis.com/oauth2/v3/token`).

If you're using an older version of the agent, it's recommended that you [upgrade your agent](https://docs.cloud.google.com/logging/docs/agent/logging/installation#upgrade) to the latest version.

  * Logging APIs: `logging.googleapis.com`




Installing the agent requires access to the following DNS names:

  * (Linux) Google Cloud package repository: `packages.cloud.google.com`

  * Google download server: `dl.google.com`




## Logging agent source code

You don't need the information in this section unless you want to understand the source code or you have other special needs. The Logging agent is installed by the script described in the [installation instructions](https://docs.cloud.google.com/logging/docs/agent/logging/installation).

The Logging agent, `google-fluentd`, is a modified version of the [fluentd](https://www.fluentd.org/) log data collector. `google-fluentd` is distributed in two separate packages. The source code is available from the associated GitHub repositories:

  * The GitHub repository named [`google-fluentd`](https://github.com/GoogleCloudPlatform/google-fluentd) which includes the core `fluentd` program, the custom packaging scripts, and the output plugin for the Cloud Logging API. 
    * The output plugin is packaged as a Ruby gem and is included in the `google-fluentd` package. It is also available separately at the Ruby gem hosting service at [fluent-plugin-google-cloud](https://rubygems.org/gems/fluent-plugin-google-cloud).
    * The content related to the Windows installer is found in the [windows-installer](https://github.com/GoogleCloudPlatform/google-fluentd/tree/master/windows-installer) folder.
  * The GitHub repository named [`google-fluentd-catch-all-config`](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config) which includes the configuration files for the Logging agent for ingesting the logs from various third-party software packages.



## Logging agent release notes

  * The release notes for the `google-fluentd` Linux package can be found at [`google-fluentd/releases`](https://github.com/GoogleCloudPlatform/google-fluentd/releases), where the release tags follow the `[Major].[Minor].[Patch]` semantic versioning format.

  * The release notes for the Windows installers can be found at the same location: [`google-fluentd/releases`](https://github.com/GoogleCloudPlatform/google-fluentd/releases). But the release tags are prefixed with `Windows` instead.

  * The release notes for the stand-alone gem `fluent-plugin-google-cloud` can be found at [`fluent-plugin-google-cloud/releases`](https://github.com/GoogleCloudPlatform/fluent-plugin-google-cloud/releases), where the release tags follow the `[Major].[Minor].[Patch]` semantic versioning format.




## Deprecation policy

The Logging agent is subject to the [Google Cloud Observability agents deprecation policy](https://docs.cloud.google.com/stackdriver/docs/agent-deprecation-policy).

## Next steps

  * [Installing the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/installation)

  * [Configure the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/configuration)

  * [Authorize the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/authorization)

  * [Upgrading the Logging agent](https://docs.cloud.google.com/logging/docs/agent/logging/installation#upgrade)

  * After installing the agent, view your logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
