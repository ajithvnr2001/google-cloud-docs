---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/
title: Legacy Monitoring and Logging agents end of support \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:50.885730+00:00
---

# Legacy Monitoring and Logging agents end of support  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Reference ](https://docs.cloud.google.com/stackdriver/docs/reference/api-overview)



Send feedback 

#  Legacy Monitoring and Logging agents end of support Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : This deprecation applies only to environments where you installed the legacy Monitoring agent or the legacy Logging agent, not to managed environments with built-in or pre-installed [ monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/monitoring#unsupported_managed_environments) and [logging](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/logging#unsupported_managed_environments) agents. 

Google Cloud Observability is phasing out the legacy Monitoring and Logging agents.

As of **September 28, 2026** , all standard maintenance and regular bug fixes for the agents officially end, initiating a 12-month migration grace period. During this time, Cloud Customer Care will assist with your migration efforts via support tickets. Migration support ends on **September 28, 2027** , after which all migration efforts must be managed independently.

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

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
