---
url: https://docs.cloud.google.com/trace/docs/trace-log-integration/
title: Link log entries with traces \u00a0|\u00a0 Cloud Trace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:21.382924+00:00
---

# Link log entries with traces  |  Cloud Trace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/trace/docs/trace-log-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Trace ](https://docs.cloud.google.com/trace/docs)
  * [ Guides ](https://docs.cloud.google.com/trace/docs/overview)



Send feedback 

#  Link log entries with traces Stay organized with collections  Save and categorize content based on your preferences. 

Correlating Cloud Logging log entries with Cloud Trace traces and spans lets you view logs alongside trace waterfall graphs or in the Logs Explorer when troubleshooting distributed requests. To link logs with traces, you can set the `trace`, `spanId`, and `traceSampled` fields in a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object manually, or use Logging client libraries to populate these fields automatically from [OpenTelemetry](https://opentelemetry.io) context or HTTP request headers.

## Manually associate a log entry with a trace or span

If you use the Cloud Logging API to write log data, or if you write [structured log data](https://docs.cloud.google.com/logging/docs/structured-logging), then you can associate a log entry with a trace or with a span. The log entry can also record whether the trace was sampled. For information about how the Ops Agent converts structured log data to fields in a `LogEntry`, see [Special fields in structured payloads](https://docs.cloud.google.com/logging/docs/agent/configuration#special-fields).

To associate a log entry with a trace, set the `trace` field in the [`LogEntry` object](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry):

  * Preferred format: `TRACE_ID`
  * Legacy format: `projects/PROJECT_ID/traces/TRACE_ID`



In the previous expressions, `PROJECT_ID` is your Google Cloud project ID and `TRACE_ID` is the trace identifier.

To associate a log entry with a span when using the Logging API, set the `spanId` field in the [`LogEntry` object](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) to the 16-character hexadecimal encoding of the span's ID. For example, to associate a log entry with a span that has an ID of `74`, set the span ID to `000000000000004a`.

To indicate that you are using trace sampling and that the trace was sampled for storage when the log entry was written, set the `traceSampled` field in the [`LogEntry` object](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). When you use trace sampling, it's possible that a log entry is created when the trace itself isn't captured.

## Automatically associate a log entry with a trace or span

[Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries) can automatically set the trace fields in some cases. Values set manually take precedence over values set automatically.

For example, if you are using [OpenTelemetry](https://opentelemetry.io) and are logging from an active OpenTelemetry span, then the trace fields in the log entry are populated from the [OpenTelemetry Context](https://opentelemetry.io/docs/concepts/context-propagation).

Alternatively, in some cases, when an HTTP request is present, the trace fields can be set from the [W3C `traceparent`](https://www.w3.org/TR/trace-context) field or the [`X-Cloud-Trace-Context`](https://docs.cloud.google.com/trace/docs/trace-context#legacy-http-header) value in the HTTP request.

For more information about automatic population of trace fields in log entries, see the following language-specific client-library documentation:

  * [Go](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/logging/latest#hdr-Automatic_Trace_Span_ID_Extraction)
  * [Java](https://github.com/googleapis/java-logging?tab=readme-ov-file#population-of-tracespan-id-fields-in-a-logentry)
  * [Node.js](https://docs.cloud.google.com/nodejs/docs/reference/logging/latest#automatic-tracespan-id-extraction)
  * [Python](https://docs.cloud.google.com/python/docs/reference/logging/latest/auto-trace-span-extraction)



## View logs

You can view the log entry for a trace alongside the waterfall graph or in the Logs Explorer. When you use the Logs Explorer, the time range is automatically restricted to the timestamp range of the trace. If there are no log entries to display, then the Logs Explorer displays the message `No entries found matching current filter`.

To view the log entry for the trace from the **Trace details** pane, do one of the following:

  * To display the trace log entries alongside the waterfall graph, go to the waterfall graph and click **Show logs**. When **Show logs** isn't displayed, no log entries are available.

  * To view the log entry in the Logs Explorer, click **View** next to the label **Log** in the **Details** section. When you have a Cloud Load Balancing trace, click **View** next to the label **VM Log**.




For more information about viewing log entries in Logging, see [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### Log viewing permissions

To view any log entries, you must have the `logging.logEntries.list` permission in your project. This permission is provided by the **Logs Viewer** and **Project Viewer** Identity and Access Management (IAM) roles.

To view VM instance logs, you must have the `compute.instances.get` permission in your project. This permission is provided by the **Compute Engine Network Viewer** and **Project Viewer** IAM roles.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
