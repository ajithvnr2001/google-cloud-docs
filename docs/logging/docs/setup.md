---
url: https://docs.cloud.google.com/logging/docs/setup/
title: Logging libraries overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:58.023508+00:00
---

# Logging libraries overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Logging libraries overview Stay organized with collections  Save and categorize content based on your preferences. 

Many programming languages have standard log-writing interfaces that you can reconfigure to use Logging. 

**Note:** Instrument your application to collect specific information that helps you understand its performance and troubleshoot failures. Several open-source instrumentation frameworks collect log, metric, and trace data, and can send that data to any vendor, including Google Cloud. For your agentic applications, some frameworks can collect your prompts and responses or pass context that allows tracing of some remote [Google Cloud MCP servers](https://docs.cloud.google.com/mcp/overview) calls.

To instrument your application, we recommend that you use an open-source, vendor-neutral instrumentation framework, such as [OpenTelemetry](https://opentelemetry.io/), instead of vendor- and product-specific APIs or client libraries. For information about these frameworks, see [ Observability for application developers](https://docs.cloud.google.com/stackdriver/docs/opentelemetry/application-developers) and [Choose an instrumentation approach](https://docs.cloud.google.com/stackdriver/docs/instrumentation/choose-approach).

## Write logs

To write logs to Cloud Logging, you can do any of the following: 

  * Write your logs to existing log files such as `syslog` on your Compute EngineVM instance and use the Ops Agent to send the logs to Cloud Logging. For more information, see [Google Cloud Observability agents](https://docs.cloud.google.com/logging/docs/agent).
  * Configure a standard logging package to send the logs you write to Logging. For more information, see the following detail pages: 
    * Any language: [fluentd](https://www.fluentd.org/)
    * [C#: Using ASP.NET or calling the API](https://docs.cloud.google.com/logging/docs/integrate/dotnet)
    * [Java: Using Logback and java.util.logging](https://docs.cloud.google.com/logging/docs/setup/java)
    * [Go: Using standard logging](https://docs.cloud.google.com/logging/docs/setup/go)
    * [Node.js: Using Winston and Bunyan](https://docs.cloud.google.com/logging/docs/setup/nodejs)
    * [PHP: Using PSR-3 logger](https://docs.cloud.google.com/logging/docs/setup/php)
    * [Python: Using the standard logging facility](https://docs.cloud.google.com/logging/docs/setup/python)
    * [Ruby: Using the Google Cloud Observability gem](https://docs.cloud.google.com/logging/docs/setup/ruby)
  * Call the Logging API using Logging's [Client Libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) for your programming language.
  * Call the Logging API REST endpoint directly. See the [Logging API reference documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest).
  * Use the [gcloud CLI](https://docs.cloud.google.com/sdk/docs). For more information, see the [`gcloud logging`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command-line interface.

**Note:** Incoming log entries with timestamps that are more than the [logs retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) in the past or that are more than 24 hours in the future are discarded.

## Associate trace data with log entries

Log entries can contain information about traces. By including trace data in log entries, you can correlate logs and traces to enable better distributed troubleshooting. For information about manual and automatic capture of trace information in log entries, see [Integrate with Cloud Logging](https://docs.cloud.google.com/trace/docs/trace-log-integration).

## Read logs

To read log entries in Logging, you can do any of the following:

  * In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

For more information, see [Logs Explorer overview](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

  * Call the Logging API through the [client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) for your programming language.

  * Call the Logging API REST endpoints directly. See the [Logging API reference documentation](https://docs.cloud.google.com/logging/docs/reference/v2/rest).

  * Use the [gcloud CLI](https://docs.cloud.google.com/sdk/docs). For more information, see the [`gcloud logging`](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) command-line interface.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
