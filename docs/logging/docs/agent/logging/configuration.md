---
url: https://docs.cloud.google.com/logging/docs/agent/logging/configuration/
title: Configure the Logging agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:26:43.978553+00:00
---

# Configure the Logging agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/logging/configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Configure the Logging agent Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Logging agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

This page provides details about the Cloud Logging agent's default and custom configurations.

Most users don't need to read this page. Read this page if:

  * You're interested in learning deep technical details of the Cloud Logging agent's configuration.

  * You want to change the configuration of the Cloud Logging agent.




## Default configuration

The Logging agent `google-fluentd` is a modified version of the [fluentd](https://www.fluentd.org/) log data collector. The Logging agent comes with a default configuration; in most common cases, no additional configuration is required.

In its default configuration, the Logging agent streams logs, as included in the [list of default logs](https://docs.cloud.google.com/logging/docs/agent/default-logs), to Cloud Logging. You can configure the agent to stream additional logs; for details, see the Customizing the Logging agent configuration section on this page.

![How the Logging Agent Works.](https://docs.cloud.google.com/static/logging/docs/images/logging-agent-operation.png)

The Logging agent uses `fluentd` input plugins to retrieve and pull event logs from external sources, such as files on disk, or to parse incoming log records. Input plugins are bundled with the agent or can be installed separately as Ruby gems; review the list of [bundled plugins](https://docs.fluentd.org/input).

The agent reads **log records** stored in log files on the VM instance using `fluentd`'s built-in `in_tail` plugin. Each log record is converted to a **[log entry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)** structure for Cloud Logging. The content of each log record is mostly recorded in the **payload** of the log entries, but log entries also contain standard elements like a **timestamp** and **severity**. The Logging agent requires every log record to be tagged with a string-format tag; all of the queries and output plugins match a specific set of tags. The log name usually follows the format `projects/[PROJECT_ID]/logs/[TAG]`. For example, this log name includes the tag `structured-log`:
    
    
    projects/my-sample-project-12345/logs/structured-log
    

The output plugin transforms each internalized structured message to a log entry in Cloud Logging. The payload becomes the text or JSON payload.

The following sections on this page discuss the default configuration in detail.

## Default configuration definitions

The following sections describe the default configuration definitions for syslog, the forward input plugin, input configurations for third-party application logs, such as those in the [list of default logs](https://docs.cloud.google.com/logging/docs/agent/default-logs), and the Google Cloud `fluentd` output plugin.

### Root configuration file location

  * Linux: `/etc/google-fluentd/google-fluentd.conf`

This root configuration file imports all configuration files from the `/etc/google-fluentd/config.d` folder as well.

  * Windows: `C:\Program Files (x86)\Stackdriver\LoggingAgent\fluent.conf`

If you are running a Logging agent before version 1.5, the location is: `C:\GoogleStackdriverLoggingAgent\fluent.conf`




### Syslog configuration

**Note:** The following default `syslog` configuration, as part of the `google-fluentd-catch-all-config` package, is exclusive to Linux operating systems.

  * **Configuration file locations** : `/etc/google-fluentd/config.d/syslog.conf`

  * **Description** : This file includes the configuration to specify syslog as a log input.

  * Review the [config repository](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/tree/master/configs/config.d/syslog.conf).


Configuration name | Type | Default | Description  
---|---|---|---  
`format` | string | `/^(?<message>(?<time>[^ ]*\s*[^ ]* [^ ]*) .*)$/` | The format of the syslog.  
`path` | string | `/var/log/syslog` | The path of the syslog file.  
`pos_file` | string | `/var/lib/google-fluentd/pos/syslog.pos` | The path of the position file for this log input. `fluentd` records the position it last read into this file. Review the detailed [`fluentd` documentation](https://docs.fluentd.org/input/tail#pos_file-highly-recommended).  
`read_from_head` | bool | `true` | Whether to start reading the logs from the head of the file instead of the bottom. Review the detailed [`fluentd` documentation](https://docs.fluentd.org/input/tail#read_from_head).  
`tag` | string | `syslog` | The log tag for this log input.  
  
### `in_forward` input plugin configuration

**Note:** The following default `in_forward` plugin configuration, as part of the `google-fluentd-catch-all-config` package, is exclusive to Linux operating systems.

  * **Configuration file locations** : `/etc/google-fluentd/config.d/forward.conf`

  * **Description** : This file includes the configuration for the `in_forward` `fluentd` input plugin. The `in_forward` input plugin lets you pass in logs using a TCP socket.

  * Review the detailed [`fluentd` documentation](https://docs.fluentd.org/input/forward) for this plugin and the [config repository](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/tree/master/configs/config.d/forward.conf).


Configuration name | Type | Default | Description  
---|---|---|---  
`port` | int | `24224` | The port to monitor.  
`bind` | string | `127.0.0.1` | The bind address to monitor. By default, only connections from localhost are accepted. To open this up, this configuration needs to be changed to `0.0.0.0`.  
  
### Third-party application log input configuration

**Note:** The following default third-party application log configuration, as part of the `google-fluentd-catch-all-config` package, is exclusive to Linux operating systems.

  * **Configuration file locations** : `/etc/google-fluentd/config.d/[APPLICATION_NAME].conf`

  * **Description** : This directory includes configuration files to specify third-party applications' log files as log inputs. Each file, except `syslog.conf` and `forward.conf`, represents one application (e.g., `apache.conf` for the Apache application).

  * Review the [config repository](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/tree/master/configs/config.d).


Configuration name | Type | Default | Description  
---|---|---|---  
`format`1 | string | Varies per application | The format of the log. Review the detailed [`fluentd` documentation](https://docs.fluentd.org/parser).  
`path` | string | Varies per application | The path of the log file(s). Multiple paths can be specified, separated by ','. The `*` wildcard and strftime formats can be included to add or remove watched files dynamically. Review the detailed [`fluentd` documentation](https://docs.fluentd.org/input/tail#path).  
`pos_file` | string | Varies per application | The path of the position file for this log input. `fluentd` records the position it last read into this file. Review the detailed [`fluentd` documentation](https://docs.fluentd.org/input/tail#pos_file-highly-recommended).  
`read_from_head` | bool | `true` | Whether to start reading the logs from the head of the file instead of the bottom. Review the detailed [`fluentd` documentation](https://docs.fluentd.org/input/tail#read_from_head).  
`tag` | string | Varies; the name of the application. | The log tag for this log input.  
  
1 If you are using the `<parse>` stanza, then specify the format of the log by using `@type`.

### Google Cloud `fluentd` output plugin configuration

  * **Configuration file locations** :

    * Linux: `/etc/google-fluentd/google-fluentd.conf`
    * Windows: `C:\Program Files (x86)\Stackdriver\LoggingAgent\fluent.conf`

If you are running a Logging agent before version 1.5, the location is: `C:\GoogleStackdriverLoggingAgent\fluent.conf`

  * **Description** : This file includes configuration options to control the Google Cloud `fluentd` output plugin's behavior.

  * Go to the [config repository](https://github.com/GoogleCloudPlatform/google-fluentd/blob/master/templates/etc/td-agent/td-agent.conf).


Configuration name | Type | Default | Description  
---|---|---|---  
`buffer_chunk_limit` | string | `512KB` | As log records come in, those that cannot be written to downstream components fast enough are pushed into a queue of chunks. This configuration sets the size limit of each chunk. By default, the chunk limit is set conservatively to avoid exceeding the recommended chunk size of 5MB per write request in Logging API. Log entries in the API request can be 5-8 times larger than the original log size with all the additional metadata attached. A buffer chunk gets flushed if one of the two conditions is met:   
1\. `flush_interval` is reached.   
2\. The buffer size reaches `buffer_chunk_limit`.  
`flush_interval` | string | `5s` | As log records come in, those that cannot be written to downstream components fast enough are pushed into a queue of chunks. The configuration sets how long before a buffer chunk is flushed. A buffer chunk gets flushed if one of the two conditions is met:   
1\. `flush_interval` is reached.   
2\. The buffer size reaches `buffer_chunk_limit`.  
`disable_retry_limit` | bool | `false` | Enforces a limit on the number of retries of failed flush of buffer chunks. Review detailed specifications in `retry_limit`, `retry_wait` and `max_retry_wait`.  
`retry_limit` | int | `3` | When a buffer chunk fails to be flushed, `fluentd` by default retries later. This configuration sets how many retries to perform before dropping one problematic buffer chunk.  
`retry_wait` | int | `10s` | When a buffer chunk fails to be flushed, `fluentd` by default retries later. This configuration sets the wait interval in seconds before the first retry. The wait interval doubles on each following retry (20s, 40s, ...) until either `retry_limit` or `max_retry_wait` is reached.  
`max_retry_wait` | int | `300` | When a buffer chunk fails to be flushed, `fluentd` by default retries later. The wait interval doubles on each following retry (20s, 40s, ...). This configuration sets the maximum wait interval in seconds. If the wait interval reaches this limit, the doubling stops.  
`num_threads` | int | `8` | The number of simultaneous log flushes that can be processed by the output plugin.  
`use_grpc` | bool | `true` | Whether to use gRPC instead of REST/JSON to communicate to the Logging API. With gRPC enabled, CPU usage is typically lower.  
`grpc_compression_algorithm` | enum | `none` | If using gRPC, sets which compression schema to use. Can be `none` or `gzip`.  
`partial_success` | bool | `true` | Whether to support partial success for logs ingestion. If `true`, invalid log entries in a full set are dropped, and valid log entries are successfully ingested into the Logging API. If `false`, the full set would be dropped if it contained any invalid log entries.  
`enable_monitoring` | bool | `true` | When set to `true`, the Logging agent exports internal telemetry. See Output plugin telemetry for details.  
`monitoring_type` | string | `opencensus` | The type of monitoring. The supported options are `opencensus` and `prometheus`. See Output plugin telemetry for details.  
`autoformat_stackdriver_trace` | bool | `true` | When set to `true`, the trace is reformatted if the value of structured payload field `logging.googleapis.com/trace` matches the [ResourceTrace](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces#Trace) `traceId` format. Details of the autoformatting can be found in Special fields in structured payloads on this page.  
  
### Monitoring configuration

This section describes the Cloud Monitoring configuration.

#### Output plugin telemetry

The `enable_monitoring` option controls whether the Google Cloud `fluentd` output plugin collects its internal telemetry. When set to `true`, the Logging agent keeps track of the number of log entries requested to be sent to Cloud Logging and the actual number of log entries successfully ingested by Cloud Logging. When set to `false`, no metrics are collected by the output plugin.

The `monitoring_type` option controls how this telemetry is exposed by the agent. See the following for the list of metrics.

When set to `prometheus`, the Logging agent exposes metrics in Prometheus format on the Prometheus endpoint (`localhost:24231/metrics` by default; see prometheus and prometheus_monitor plugin configuration for details on customizing this). On Compute Engine VMs, in order for those metrics to be written to the Monitoring API, the [Monitoring agent](https://docs.cloud.google.com/monitoring/agent) has to be installed and running as well.

When set to `opencensus` (default since [v1.6.25](https://github.com/GoogleCloudPlatform/google-fluentd/releases/tag/1.6.25)), the Logging agent directly writes its own health metrics to the Monitoring API. This requires the `roles/monitoring.metricWriter` role to be granted to the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), even if the Monitoring agent is not installed.

The following metrics are written to the Monitoring API by both the Monitoring agent and the Logging agent in `opencensus` mode:

  * `agent.googleapis.com/agent/uptime` with a `version` label: Uptime of the Logging agent.
  * `agent.googleapis.com/agent/log_entry_count` with a `response_code` label: Count of log entries written by the Logging agent.
  * `agent.googleapis.com/agent/log_entry_retry_count` with a `response_code` label: Count of log entries written by the Logging agent.
  * `agent.googleapis.com/agent/request_count` with a `response_code` label: Count of API requests from the Logging agent.



These metrics are described in more detail on the [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-agent) page.

In addition, the following Prometheus metrics are exposed by the output plugin in `prometheus` mode:

  * `uptime` with a `version` label: Uptime of the Logging agent.
  * `stackdriver_successful_requests_count` with `grpc` and `code` labels: The number of successful requests to the Logging API.
  * `stackdriver_failed_requests_count` with `grpc` and `code` labels: The number of failed requests to the Logging API, broken down by the error code.
  * `stackdriver_ingested_entries_count` with `grpc` and `code` labels: The number of log entries ingested by the Logging API.
  * `stackdriver_dropped_entries_count` with `grpc` and `code` labels: The number of log entries rejected by the Logging API.
  * `stackdriver_retried_entries_count` with `grpc` and `code` labels: The number of log entries that failed to be ingested by the Google Cloud `fluentd` output plugin due to a transient error and were retried.



#### prometheus and prometheus_monitor plugin configuration

**Note:** The following default monitoring configuration is exclusive to Linux operating systems.

  * **Configuration file locations** : `/etc/google-fluentd/google-fluentd.conf`

  * **Description** : This file includes configuration options to control the behavior of the `prometheus` and `prometheus_monitor` plugins. The `prometheus_monitor` plugin monitors Fluentd's core infrastructure. The `prometheus` plugin exposes the metrics including the ones from the `prometheus_monitor` plugin and the ones from the `google_cloud` plugin using a local port in Prometheus format. For more information, see [Monitoring by Prometheus](https://docs.fluentd.org/monitoring-fluentd/monitoring-prometheus).

  * Go to the [config repository](https://github.com/GoogleCloudPlatform/google-fluentd/blob/master/templates/etc/td-agent/td-agent.conf).




For monitoring Fluentd, the built-in Prometheus http metrics server is enabled by default. You can remove the following section from the configuration to stop this endpoint from starting:
    
    
    # Prometheus monitoring.
    <source>
      @type prometheus
      port 24231
    </source>
    <source>
      @type prometheus_monitor
    </source>
    

## Processing payloads

Most of the supported logs under the default configuration of the Logging agent are from log files and are ingested as unstructured (text) payloads in the log entries.

The only exception is that the `in_forward` input plugin, which is also enabled by default, only accepts structured logs and ingests them as structured (JSON) payloads in the log entries. For details, read Streaming structured (JSON) log records using `in_forward` plugin on this page.

When the log line is a serialized JSON object and the `detect_json` option is enabled, the output plugin transforms the log entry into a structured (JSON) payload. This option is enabled by default in VM instances running on App Engine flexible environment. This option isn't enabled by default in VM instances running on App Engine standard environment. Any JSON parsed with the `detect_json` option enabled is always ingested as `jsonPayload`.

You can customize the agent's configuration to support ingesting structured logs from additional resources. See Streaming structured (JSON) log records to Cloud Logging for details.

The payload of log records streamed by a custom-configured Logging agent can be either a single unstructured text message (`textPayload`) or a structured JSON message (`jsonPayload`).

### Special fields in structured payloads

When the Logging agent receives a structured log record, it moves any key that matches the following table into the corresponding field in the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object. Otherwise, the key becomes part of the `LogEntry.jsonPayload` field. This behavior lets you set specific fields in the `LogEntry` object, which is what is written to the Logging API. For example, if the structured log record contains a key of `severity`, then the Logging agent populates the `LogEntry.severity` field.

JSON log field  |  [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) field  | Cloud Logging agent function  |  Example value   
---|---|---|---  
`severity` | `severity` | The Logging agent attempts to match a variety of common severity strings, which includes the list of [LogSeverity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity) strings recognized by the Logging API. | `"severity":"ERROR"`  
`message` | `textPayload` (or part of `jsonPayload`)  | The message that appears on the log entry line in the Logs Explorer.  | `"message":"There was an error in the application."`   
  
**Note** : `message` is saved as `textPayload` if it is the only field remaining after the Logging agent moves the other special-purpose fields _and_ `detect_json` wasn't enabled; otherwise `message` remains in `jsonPayload`. `detect_json` is not applicable to managed logging environments like Google Kubernetes Engine. If your log entry contains an exception stack trace, the exception stack trace should be set in this `message` JSON log field, so that the exception stack trace can be parsed and saved to Error Reporting.  
`log` (legacy Google Kubernetes Engine only) | `textPayload` | Only applies to legacy Google Kubernetes Engine: if, after moving special purpose fields, only a `log` field remains, then that field is saved as `textPayload`. |   
`httpRequest` | `httpRequest` | A structured record in the format of the `LogEntry` [`HttpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) field. | `"httpRequest":{"requestMethod":"GET"}`  
time-related fields  | `timestamp` | For more information, see [Time-related fields](https://docs.cloud.google.com/logging/docs/agent/logging/configuration#timestamp-processing).  | `"time":"2025-10-12T07:20:50.52Z"`  
`logging.googleapis.com/insertId` | `insertId` | For more information, see [`insertId`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.insert_id) on the `LogEntry` page. | `"logging.googleapis.com/insertId":"42"`  
`logging.googleapis.com/labels` | `labels` | The value of this field must be a structured record. For more information, see [`labels`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.labels) on the `LogEntry` page. | `"logging.googleapis.com/labels":` `{"user_label_1":"value_1","user_label_2":"value_2"}`  
`logging.googleapis.com/operation` | `operation` | The value of this field is also used by the Logs Explorer to group related log entries. For more information, see [`operation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.operation) on the `LogEntry` page. | `"logging.googleapis.com/operation":` `{"id":"get_data","producer":"github.com/MyProject/MyApplication",` `"first":"true"}`  
`logging.googleapis.com/sourceLocation` | `sourceLocation` | Source code location information associated with the log entry, if any. For more information, see [`LogEntrySourceLocation`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogEntrySourceLocation) on the `LogEntry` page. | `"logging.googleapis.com/sourceLocation":` `{"file":"get_data.py","line":"142","function":"getData"}`  
`logging.googleapis.com/spanId` | `spanId` | The span ID within the trace associated with the log entry. For more information, see [`spanId`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.span_id) on the `LogEntry` page. | `"logging.googleapis.com/spanId":"000000000000004a"`  
`logging.googleapis.com/trace` | `trace` | Resource name of the trace associated with the log entry if any. For more information, see [`trace`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.trace) on the `LogEntry` page.  | `"logging.googleapis.com/trace":"[TRACE_ID]"`  
`"logging.googleapis.com/trace":"projects/my-projectid/traces/[TRACE_ID]"`   
  
**Note** : If not writing to `stdout` or `stderr`, format this field as `[TRACE_ID]` or use the legacy format `projects/[PROJECT_ID]/traces/[TRACE_ID]`. Both formats let the Logs Explorer and Trace Explorer correlate log and trace data. If `autoformat_stackdriver_trace` is true and `[V]` matches the format of the `traceId` field in the [ResourceTrace](https://docs.cloud.google.com/trace/docs/reference/v1/rest/v1/projects.traces#Trace) object, then the LogEntry `trace` field has the value `projects/[PROJECT_ID]/traces/[V]`.  
`logging.googleapis.com/trace_sampled` | `traceSampled` | The value of this field must be either `true` or `false`. For more information, see [`traceSampled`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.trace_sampled) on the `LogEntry` page. | `"logging.googleapis.com/trace_sampled": false`  
  
### Time-related fields

In general, time-related information about a log entry is stored in the [`timestamp`](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) field of the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object:
    
    
    {
    insertId: "1ad8d08f-6529-47ea-832e-467f869a2da4"
    ...
    resource: {2}
    timestamp: "2023-10-30T16:33:15.505196Z"
    }
    

When the source for a log entry is structured data, the Logging agent uses the following rules to search the fields in the `jsonPayload` entry for time-related information:

  1. Search for a `timestamp` field that is a JSON object that includes the `seconds` and `nanos` fields, representing, respectively, a signed number of seconds from the UTC epoch and a nonnegative number of fractional seconds:
         
         jsonPayload: {
           ...
           "timestamp": {
             "seconds": CURRENT_SECONDS,
             "nanos": CURRENT_NANOS
           }
         }
         

  2. If the previous search fails, then search for a pair of `timestampSeconds` and `timestampNanos` fields:
         
         jsonPayload: {
           ...
           "timestampSeconds": CURRENT_SECONDS,
           "timestampNanos": CURRENT_NANOS
         }
         

  3. If the previous search fails, then search for a `time` field that is a string in [RFC 3339](https://tools.ietf.org/html/rfc3339) format:
         
         jsonPayload: {
           ...
           "time": CURRENT_TIME_RFC3339
         }
         




When time-related information is found, the Logging agent uses that information to set the value of the `LogEntry.timestamp`, and it doesn't copy that information from the structured record into the `LogEntry.jsonPayload` object.

Time-related fields that aren't used to set the value of the `LogEntry.timestamp` field are copied from the structured record into the `LogEntry.jsonPayload` object. For example, if the structured record contains a `timestamp` JSON object and a `time` field, then the data in the `timestamp` JSON object is used to set the `LogEntry.timestamp` field. The `LogEntry.jsonPayload` object contains a `time` field, because this field wasn't used to set the `LogEntry.timestamp` value.

## Customizing agent configuration

Besides the [list of default logs](https://docs.cloud.google.com/logging/docs/agent/default-logs) that the Logging agent streams by default, you can customize the Logging agent to send additional logs to Logging or to adjust agent settings by adding input configurations.

The configuration definitions in these sections apply to the `fluent-plugin-google-cloud` output plugin only and specify how logs are transformed and ingested into Cloud Logging.

  * **Main configuration file locations** :

    * Linux: `/etc/google-fluentd/google-fluentd.conf`
    * Windows: `C:\Program Files (x86)\Stackdriver\LoggingAgent\fluent.conf`

If you are running a Logging agent before version 1.5, the location is: `C:\GoogleStackdriverLoggingAgent\fluent.conf`

  * **Description** : This file includes configuration options to control the `fluent-plugin-google-cloud` output plugin's behavior.

  * Review the [config repository](https://github.com/GoogleCloudPlatform/google-fluentd/blob/master/templates/etc/td-agent/td-agent.conf).




### Streaming logs from additional inputs

You can customize the Logging agent to send additional logs to Logging by adding input configurations.

#### Streaming unstructured (text) logs using log files

**Note:** This section contains a Linux command example. If you use Windows, then you must adapt the command steps to that environment. `C:\Program Files (x86)\Stackdriver\LoggingAgent\config.d` is the third-party configuration directory for Windows. Also, ensure that you use forward slashes, (`/`), in the configuration file for Windows. For more information about why this is required, see [Wildcard pattern in path does not work on Windows](https://docs.fluentd.org/input/tail#wildcard-pattern-in-path-does-not-work-on-windows-why).

  1. From the Linux command prompt, create a log file:
         
         touch /tmp/test-unstructured-log.log
         

  2. Create a new configuration file labeled `test-unstructured-log.conf` in the additional configuration directory `/etc/google-fluentd/config.d`:
         
         sudo tee /etc/google-fluentd/config.d/test-unstructured-log.conf <<EOF
         <source>
             @type tail
             <parse>
                 # 'none' indicates the log is unstructured (text).
                 @type none
             </parse>
             # The path of the log file.
             path /tmp/test-unstructured-log.log
             # The path of the position file that records the position in the log
             # file that has already been processed. This is useful when the agent
             # restarts.
             pos_file /var/lib/google-fluentd/pos/test-unstructured-log.pos
             read_from_head true
             # The log tag for this log input.
             tag unstructured-log
         </source>
         EOF
         

An alternative to creating a new file is to add the configuration information to an existing configuration file.

  3. Restart the agent to apply the configuration changes:
         
         sudo service google-fluentd restart
         

  4. Generate a log record into the log file:
         
         echo 'This is a log from the log file at test-unstructured-log.log' >> /tmp/test-unstructured-log.log
         

  5. Check the Logs Explorer to see the ingested log entry:
         
         {
           insertId:  "eps2n7g1hq99qp"
           labels: {
           compute.googleapis.com/resource_name:  "add-unstructured-log-resource"
           }
           logName:  "projects/my-sample-project-12345/logs/unstructured-log"
           receiveTimestamp:  "2018-03-21T01:47:11.475065313Z"
           resource: {
           labels: {
             instance_id:  "3914079432219560274"
             project_id:  "my-sample-project-12345"
             zone:  "us-central1-c"
           }
           type:  "gce_instance"
           }
           textPayload:  "This is a log from the log file at test-unstructured-log.log"
           timestamp:  "2018-03-21T01:47:05.051902169Z"
         }
         




#### Streaming structured (JSON) logs using log files

**Note:** This section contains a Linux command example. If you use Windows, then you must adapt the command steps to that environment. `C:\Program Files (x86)\Stackdriver\LoggingAgent\config.d` is the third-party configuration directory for Windows. Also, ensure that you use forward slashes, (`/`), in the configuration file for Windows. For more information about why this is required, see [Wildcard pattern in path does not work on Windows](https://docs.fluentd.org/input/tail#wildcard-pattern-in-path-does-not-work-on-windows-why).

You can configure the Logging agent to require each log entry for certain log inputs to be [structured](https://docs.cloud.google.com/logging/docs/structured-logging). You can also customize the Logging agent to ingest JSON formatted content from a log file. When the agent is configured to ingest JSON content, the input **must** be formatted so that each JSON object is on a newline: 
    
    
        {"name" : "zeeshan", "age" : 28}
        {"name" : "reeba", "age" : 15}
    

To configure the Logging agent to ingest JSON formatted content, do the following:

  1. From the Linux command prompt, create a log file:
         
         touch /tmp/test-structured-log.log
         

  2. Create a new configuration file labeled `test-structured-log.conf` in the additional configuration directory `/etc/google-fluentd/config.d`:
         
         sudo tee /etc/google-fluentd/config.d/test-structured-log.conf <<EOF
         <source>
             @type tail
             <parse>
                 # 'json' indicates the log is structured (JSON).
                 @type json
             </parse>
             # The path of the log file.
             path /tmp/test-structured-log.log
             # The path of the position file that records the position in the log
             # file that has already been processed. This is useful when the agent
             # restarts.
             pos_file /var/lib/google-fluentd/pos/test-structured-log.pos
             read_from_head true
             # The log tag for this log input.
             tag structured-log
           </source>
           EOF
         

An alternative to creating a new file is to add the configuration information to an existing configuration file.

  3. Restart the agent to apply the configuration changes:
         
         sudo service google-fluentd restart
         

  4. Generate a log record into the log file:
         
         echo '{"code": "structured-log-code", "message": "This is a log from the log file at test-structured-log.log"}' >> /tmp/test-structured-log.log
         

  5. Check the Logs Explorer to see the ingested log entry:
         
         {
           insertId:  "1m9mtk4g3mwilhp"
           jsonPayload: {
           code:  "structured-log-code"
           message:  "This is a log from the log file at test-structured-log.log"
           }
           labels: {
           compute.googleapis.com/resource_name:  "add-structured-log-resource"
           }
           logName:  "projects/my-sample-project-12345/logs/structured-log"
           receiveTimestamp:  "2018-03-21T01:53:41.118200931Z"
           resource: {
           labels: {
             instance_id:  "5351724540900470204"
             project_id:  "my-sample-project-12345"
             zone:  "us-central1-c"
           }
           type:  "gce_instance"
           }
           timestamp:  "2018-03-21T01:53:39.071920609Z"
         }
         

In the Logs Explorer, filter by your resource type and a **logName** of `structured-log`.




For additional options to customize your log input format for common third-party applications, see [Common Log Formats and How To Parse Them](https://docs.fluentd.org/v/0.12/articles/common-log-formats).

#### Streaming structured (JSON) logs using `in_forward` plugin

Additionally, you can send logs using the `fluentd` `in_forward` plugin. `fluentd-cat` is a built-in tool that helps send logs to the `in_forward` plugin. The [`fluentd` documentation](https://docs.fluentd.org/deployment/command-line-option#fluent-cat) contains more details for this tool.

To send logs using the `fluentd` `in_forward` plugin, read the following instructions:

  1. Execute the following command on the VM with the Logging agent installed:
         
         echo '{"code": "send-log-via-fluent-cat", "message": "This is a log from in_forward plugin."}' | /opt/google-fluentd/embedded/bin/fluent-cat log-via-in-forward-plugin
         

  2. Check the Logs Explorer to see the ingested log entry:
         
         {
           insertId:  "1kvvmhsg1ib4689"
           jsonPayload: {
           code:  "send-log-via-fluent-cat"
           message:  "This is a log from in_forward plugin."
           }
           labels: {
           compute.googleapis.com/resource_name:  "add-structured-log-resource"
           }
           logName:  "projects/my-sample-project-12345/logs/log-via-in-forward-plugin"
           receiveTimestamp:  "2018-03-21T02:11:27.981020900Z"
           resource: {
           labels: {
             instance_id:  "5351724540900470204"
             project_id:  "my-sample-project-12345"
             zone:  "us-central1-c"
           }
           type:  "gce_instance"
           }
           timestamp:  "2018-03-21T02:11:22.717692494Z"
         }
         




#### Streaming structured (JSON) log records from application code

You can enable connectors in various languages to send structured logs from application code; for more information, review the [`fluentd` documentation](https://docs.fluentd.org/v/0.12/use-cases/logging-from-apps). These connectors are based on the `in_forward` plugin.

### Setting log entry labels

The following configuration options let you override [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) labels and [MonitoredResource](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) labels when ingesting logs to Cloud Logging. All log entries are associated with monitored resources; for more information, review the list of [Cloud Logging monitored resource types](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#resource-types).

Configuration name | Type | Default | Description  
---|---|---|---  
`label_map` | hash | nil | `label_map` (specified as a JSON object) is an unordered set of `fluentd` field names whose values are sent as labels rather than as part of the structured payload. Each entry in the map is a {`field_name`: `label_name`} pair. When `field_name` (as parsed by the input plugin) is encountered, a label with the corresponding `label_name` is added to the log entry. The value of the field is used as the value of the label. The map gives you additional flexibility in specifying label names, including the ability to use characters that wouldn't be legal as part of `fluentd` field names. For an example, see Setting labels in structured log entries.  
`labels` | hash | nil | `labels` (specified as a JSON object) is a set of custom labels provided at configuration time. It lets you inject extra environmental information into every message or customize labels otherwise detected automatically. Each entry in the map is a {`label_name`: `label_value`} pair.  
  
The Logging agent output plugin supports three ways to set [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) labels:

  * Dynamically, replacing specific labels in a structured entry with different labels. For details, see Setting labels in structured log entries on this page.
  * Statically, attaching a label to any occurrence of a value. For details, see Setting labels statically on this page.



#### Setting labels in structured log entries

Suppose you wrote a structured log entry payload like this:
    
    
    { "message": "This is a log message", "timestamp": "Aug 10 20:07:00", "env": "production" }
    

And suppose you want to translate the payload field `env` to a metadata label `environment`. To do this, add the following to your output plugin configuration in the main configuration file (`/etc/google-fluentd/google-fluentd.conf` on Linux or `C:\Program Files (x86)\Stackdriver\LoggingAgent\fluent.conf` on Windows):
    
    
    # Configure all sources to output to Cloud Logging
    <match **>
      @type google_cloud
      label_map {
        "env": "environment"
      }
      ...
    </match>
    

The `label_map` setting here replaces the `env` label in the payload with `environment`, so the resulting log entry has a label `environment` with the value `production`.

#### Setting labels statically

If you don't have this information in the payload and want to add a static metadata label called `environment`, then add the following to your output plugin configuration in the main configuration file (`/etc/google-fluentd/google-fluentd.conf` on Linux or `C:\Program Files (x86)\Stackdriver\LoggingAgent\fluent.conf` on Windows):
    
    
    # Configure all sources to output to Cloud Logging
    <match **>
      @type google_cloud
      labels {
        "environment": "production"
      }
      ...
    </match>
    

In this case, instead of using a map to replace one label with another, we use a `labels` setting to attach a label with a given literal value to a log entry, regardless of whether the entry already has a label or not. This approach can be used even if you are sending unstructured logs.

For more on how to configure `labels`, `label_map` and other Logging agent settings, see the Setting Log Entry Labels section of this page.

### Modifying Log Records

Fluentd provides [built-in filter plugins](https://docs.fluentd.org/filter) that can be used to modify log entries.

The most commonly used filter plugin is [`filter_record_transformer`](https://docs.fluentd.org/filter/record_transformer). It lets you do the following:

  * Add new fields to log entries
  * Update fields in log entries
  * Delete fields in log entries



Some output plugins also let you modify log entries. The [`fluent-plugin-record-reformer`](https://github.com/sonots/fluent-plugin-record-reformer/blob/master/README.md) output plugin provides functionality similar to the `filter_record_transformer` filter plugin, except that it also lets you modify log tags. More resource usage is expected with this plugin: each time a log tag is updated, it generates a new log entry with the new tag. Note that the `tag` field in the configuration is required. It is also recommended that you modify this field to avoid entering an infinite loop.

The [`fluent-plugin-detect-exceptions`](https://github.com/GoogleCloudPlatform/fluent-plugin-detect-exceptions/blob/master/README.rdoc) output plugin scans a log stream, either unstructured (text) or JSON-format log records, for multi-line exception stack traces. If a consecutive sequence of log entries forms an exception stack trace, the log entries are forwarded as a single, combined log message. Otherwise, the log entry is forwarded as it was.

### Advanced (non-default) configuration definitions

If you want to customize the configuration of your Logging agent, beyond its default configuration, then continue reading this page.

#### Buffer-related configuration options

The following configuration options let you adjust the Logging agent's internal buffering mechanism.

Configuration name | Type | Default | Description  
---|---|---|---  
`buffer_type` | string | `buf_memory` | Records that cannot be written to the Logging API fast enough are pushed into a buffer. The buffer can be in memory or in files. Recommended value: `buf_file`. The default `buf_memory` is fast but not persistent. There is a risk of losing logs. If `buffer_type` is `buf_file`, `buffer_path` needs to be specified as well.  
`buffer_path` | string | User-specified | The path where buffer chunks are stored. This parameter is required if `buffer_type` is `buf_file`. This configuration must be unique to avoid a race condition.  
`buffer_queue_limit` | int | `64` | Specifies the length limit of the chunk queue. When the buffer queue reaches this limit, the buffer behavior is controlled by `buffer_queue_full_action`. By default, it throws exceptions. This option in combination with `buffer_chunk_limit` determines the maximum disk space `fluentd` takes for buffering.  
`buffer_queue_full_action` | string | `exception` | Controls the buffer behavior when the buffer queue is full. Possible values:   
1\. `exception`: Throw `BufferQueueLimitError` when the queue is full. How `BufferQueueLimitError` is handled depends on input plugins. For example, the `in_tail` input plugin stops reading new lines while the `in_forward` input plugin returns an error.   
2\. `block`: This mode stops the input plugin thread until the buffer-full condition is resolved. This action is good for batch-like use cases. `fluentd` doesn't recommend using the block action to avoid `BufferQueueLimitError`. If you hit `BufferQueueLimitError` frequently, it means your destination capacity is insufficient for your traffic.   
3\. `drop_oldest_chunk`: This mode drops the oldest chunks.  
  
#### Project- and monitored resource-related configuration options

The following configuration options let you manually specify a project and certain fields from the [MonitoredResource](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/MonitoredResource) object. **These values are automatically gathered by the Logging agent; it is not recommended that you manually specify them.**

Configuration name | Type | Default | Description  
---|---|---|---  
`project_id` | string | nil | If specified, this overrides the `project_id` identifying the underlying Google Cloud or AWS project in which the Logging agent is running.  
`zone` | string | nil | If specified, this overrides the zone.  
`vm_id` | string | nil | If specified, this overrides the VM ID.  
`vm_name` | string | nil | If specified, this overrides the VM name.  
  
#### Other output plugin configuration options

Configuration name | Type | Default | Description  
---|---|---|---  
`detect_json`1 | bool | `false` | Whether to try to detect if the log record is a text log entry with JSON content that needs to be parsed. If this option is `true`, and an unstructured (text) log entry is detected to be in JSON format, then it is parsed and sent as a structured (JSON) payload.  
`coerce_to_utf8` | bool | `true` | Whether to allow non-UTF-8 characters in user logs. If set to `true`, any non-UTF-8 character is replaced by the string specified by `non_utf8_replacement_string`. If set to `false`, any non-UTF-8 character causes the plugin to error out.  
`require_valid_tags` | bool | `false` | Whether to reject log entries with invalid tags. If this option is set to `false`, tags are made valid by converting any non-string tag to a string, and sanitizing any non-UTF-8 or other invalid characters.  
`non_utf8_replacement_string` | string | `""` (empty string) or `" "`(space) | If `coerce_to_utf8` is set to `true`, any non-UTF-8 character is replaced by the string specified here.  
  
1This feature is **enabled by default in VM instances running on App Engine flexible environment.**

### Applying customized agent configuration

Customizing the Logging agent lets you add your own `fluentd` configuration files:

### Linux instance

  1. Copy your configuration files into the following directory:
         
         /etc/google-fluentd/config.d/
         

The Logging agent installation script populates this directory with the default catch-all configuration files. For more information, see [Getting the Logging agent source code](https://docs.cloud.google.com/logging/docs/agent/logging#source).

  2. Optional. Validate your configuration change by running the following command:
         
         sudo service google-fluentd configtest
         

  3. Restart the agent by running the following command:
         
         sudo service google-fluentd force-reload
         




### Windows instance

**Note:** If you are running an agent version before version 1.5, then you cannot add your own configuration files. [Upgrade to the latest agent](https://docs.cloud.google.com/logging/docs/agent/installation#upgrade).

  1. Copy your config files into the `config.d` subdirectory of your agent-installation directory. If you accepted the default installation directory, this directory is:
         
         C:\Program Files (x86)\Stackdriver\LoggingAgent\config.d\
         

  2. Restart the agent by running the following commands in a command-line shell:
         
         net stop StackdriverLogging
         net start StackdriverLogging
         




For more information about `fluentd` configuration files, see [fluentd's Configuration File Syntax documentation](https://docs.fluentd.org/configuration/config-file).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
