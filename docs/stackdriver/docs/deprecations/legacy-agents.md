---
url: https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents/
title: Legacy Monitoring and Logging agents end of support \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:41.168049+00:00
---

# Legacy Monitoring and Logging agents end of support  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Resources ](https://docs.cloud.google.com/stackdriver/quotas)



Send feedback 

#  Legacy Monitoring and Logging agents end of support Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : This deprecation applies only to environments where you installed the legacy Monitoring agent or the legacy Logging agent, not to managed environments with built-in or pre-installed [ monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring#unsupported_managed_environments) and [logging](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging#unsupported_managed_environments) agents. 

As of **September 28, 2026** , the legacy Monitoring and Logging agents have officially reached their end of support. We will no longer release new versions of this software, and all standard support and maintenance have ended.

While existing installations of the legacy agents won't be shut down and will continue streaming logs to Cloud Logging and metrics to Cloud Monitoring, the use of these agents is no longer recommended. However, the distributions remain available to download and install.

Continuing to use the legacy agents means you won't receive updates, bug fixes, or support for new operating systems, leading to eventual incompatibility with Google Cloud Observability. We highly recommend migrating to a supported alternative.

## Key points and dates

The following are the key dates for the legacy Logging agent deprecation:

  * On **September 28, 2026** , standard maintenance and regular bug fixes for the legacy agents ends. A 12-month migration grace period begins. During this time, Cloud Customer Care will assist with your migration efforts through support tickets.
  * On **September 28, 2027** , Cloud Customer Care migration assistance officially ends. After this date, you are responsible for handling the migration independently.



## Migration options

We recommend migrating to one of the following supported alternatives as soon as possible:

  * **[Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent):** The primary and preferred agent for collecting telemetry from your Compute Engine instances. This agent combines logging and metrics into a single agent, providing YAML-based configurations for collecting your logs and metrics, and features high-throughput logging. For more information, see [Migrating from the legacy agents to the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/transition#migrate_legacy). 
  * **[Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel):** Google's production-ready build of the open-source [OpenTelemetry Collector](https://opentelemetry.io/). It lets you send correlated [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) traces, metrics, and logs to Google Cloud Observability and other backends from applications. For more information, see [Overview of the Google-Built OpenTelemetry Collector](https://docs.cloud.google.com/stackdriver/docs/instrumentation/google-built-otel). 
  * **[Upstream Fluentd](https://www.fluentd.org/) (logging only):** The open-source, community-driven log data collector that the legacy Logging agent was built upon. Many legacy environments use highly customized Fluentd configurations that can't be translated for the Ops Agent. By pairing upstream Fluentd with the Google-platform plugins, you can maintain your current setups and make sure your logs continue to flow into Cloud Logging without interruption. For more information, see [Migrate from the legacy Logging agent to upstream Fluentd](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging/migrating-to-fluentd). 



## Identify affected Compute Engine instances

To identify Compute Engine instances running the legacy Monitoring agent or the legacy Logging agent, follow these steps: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**. 
  3. In the **Results** pane, select the **Table**. 
  4. Enter one of the following queries into the editor, and then click **Run query** : 
     * To generate a table that lists the instance of ID each VM running an agent, along with the version of the agent, use: 
           
           max by (instance_id, version, ${__groupby}) ({__name__="agent.googleapis.com/agent/uptime", monitored_resource="gce_instance"})
                   

     * To generate a table that shows the total number of instances running each agent version, use: 
           
           count by (version, ${__groupby}) ({__name__="agent.googleapis.com/agent/uptime", monitored_resource="gce_instance"})
                   

In the **version** column, entries showing `stackdriver_agent` refer to the legacy Monitoring agent, while entries showing `google-fluentd` refer to the legacy Logging agent. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
