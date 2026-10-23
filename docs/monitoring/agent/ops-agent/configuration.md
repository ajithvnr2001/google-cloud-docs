---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration/
title: Configure the Ops Agent \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:50.288349+00:00
---

# Configure the Ops Agent  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Configure the Ops Agent Stay organized with collections  Save and categorize content based on your preferences. 

This document provides details about the Ops Agent's default and custom configurations. Read this document if any of the following applies to you:

  * You want to change the configuration of the Ops Agent to achieve the following goals:

    * Turn off the built-in logging or metrics ingestion.

      * To turn off logging ingestion, see Example logging `service` configurations.

      * To turn off host-metrics ingestion, see Example metrics `service` configurations.

    * Customize the file path of the log files that the agent collects logs from; see Logging receivers.

    * Customize the structured log format that the agent uses to process the log entries, by parsing the JSON or by using regular expressions; see Logging processors.

    * Change the sampling rate for metrics; see Metrics receivers.

    * Customize which group or groups of metrics to enable. The agent collects all system metrics, like `cpu` and `memory`, by default; see Metrics processors.

    * Customize how the agent rotates logs; see Log-rotation configuration.

    * Collect metrics and logs from supported third-party applications. See [Monitor third-party applications](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party) for the list of supported applications. 

    * Use the [Prometheus receiver](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus) to collect custom metrics.

    * Use the [OpenTelemetry Protocol (OTLP) receiver](https://docs.cloud.google.com/monitoring/agent/ops-agent/otlp) to collect custom metrics and traces. 

  * You're interested in learning the technical details of the Ops Agent's configuration.




## Configuration model

The Ops Agent uses a built-in default configuration; you can't directly modify this built-in configuration. Instead, you create a file of overrides that are merged with the built-in configuration when the agent restarts.

The building blocks of the configuration are as follows:

  * `receivers`: This element describes what is collected by the agent.
  * `processors`: This element describes how the agent can modify the collected information.
  * `service`: This element links receivers and processors together to create data flows, called _pipelines_. The `service` element contains a `pipelines` element, which can contain multiple pipelines.



The built-in configuration is made up of these elements, and you use the same elements to override that built-in configuration.

**Note:** The Ops Agent sends logs to Cloud Logging and metrics to Cloud Monitoring. You can't configure the agent to export logs or metrics to other services. You can, however, configure Cloud Logging to export logs; for more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

### Built-in configuration

The built-in configuration for the Ops Agent defines the default collection for logs and metrics. The following shows the built-in configuration for Linux and for Windows:

### Linux

By default, the Ops Agent collects file-based `syslog` logs and host metrics.

For more information about the metrics collected, see Metrics ingested by the receivers.
    
    
    logging:
      receivers:
        syslog:
          type: files
          include_paths:
          - /var/log/messages
          - /var/log/syslog
      service:
        pipelines:
          default_pipeline:
            receivers: [syslog]
    metrics:
      receivers:
        hostmetrics:
          type: hostmetrics
          collection_interval: 60s
      processors:
        metrics_filter:
          type: exclude_metrics
          metrics_pattern: []
      service:
        pipelines:
          default_pipeline:
            receivers: [hostmetrics]
            processors: [metrics_filter]
    

### Windows

By default, the Ops Agent collects Windows event logs from `System`, `Application`, and `Security` channels, as well as host metrics, IIS metrics, and SQL Server metrics.

For more information about the metrics collected, see Metrics ingested by the receivers.
    
    
    logging:
      receivers:
        windows_event_log:
          type: windows_event_log
          channels: [System, Application, Security]
      service:
        pipelines:
          default_pipeline:
            receivers: [windows_event_log]
    metrics:
      receivers:
        hostmetrics:
          type: hostmetrics
          collection_interval: 60s
        iis:
          type: iis
          collection_interval: 60s
        mssql:
          type: mssql
          collection_interval: 60s
      processors:
        metrics_filter:
          type: exclude_metrics
          metrics_pattern: []
      service:
        pipelines:
          default_pipeline:
            receivers: [hostmetrics, iis, mssql]
            processors: [metrics_filter]
    

These configurations are discussed in more detail in Logging configuration and Metrics configuration.

### User-specified configuration

To override the built-in configuration, you add new configuration elements to the user configuration file. Put your configuration for the Ops Agent in the following files:

  * For Linux: `/etc/google-cloud-ops-agent/config.yaml`
  * For Windows: `C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml`



Any user-specified configuration is merged with the built-in configuration when the agent restarts.

**Note:** If you make any configuration changes, then you must [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart) to apply the updated configurations.

To override a built-in receiver, processor, or pipeline, redefine it in your `config.yaml` file by declaring it with the same identifier. Starting with Ops Agent version 2.31.0, you can also configure the agent's log-rotation feature; for more information, see [Configure log rotation in the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/rotate-logs#configure-log-rotation).

For example, the built-in configuration for metrics includes a `hostmetrics` receiver that specifies a 60-second collection interval. To change the collection interval for host metrics to 30 seconds, include a metrics receiver called `hostmetrics` in your `config.yaml` file that sets the `collection_interval` value to 30 seconds, as shown in the following example:
    
    
    metrics:
      receivers:
        hostmetrics:
          type: hostmetrics
          collection_interval: 30s
    

For other examples of changing the built-in configurations, see Logging configuration and Metrics configuration. You can also turn off the collection of logging or metric data. These changes are described in the example logging `service` configurations and metrics `service` configurations.

You can use this file to prevent the agent from collecting self logs and sending those logs to Cloud Logging. For more information, see Collection of self logs.

You also configure the agent's log-rotation feature by using this file; for more information, see [Configure log rotation in the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/rotate-logs#configure-log-rotation).

You can't configure the Ops Agent to export logs or metrics to services other than Cloud Logging and Cloud Monitoring.

## Logging configurations

The `logging` configuration uses the configuration model described previously:

  * `receivers`: This element describes the data to collect from log files; this data is mapped into a <timestamp, record> model.
  * `processors`: This optional element describes how the agent can modify the collected information.
  * `service`: This element links receivers and processors together to create data flows, called _pipelines_. The `service` element contains a `pipelines` element, which can include multiple pipeline definitions.



Each receiver and each processor can be used in multiple pipelines.

The following sections describe each of these elements.

The Ops Agent sends logs to Cloud Logging. You can't configure it to export logs to other services. You can, however, configure Cloud Logging to export logs; for more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2).

## Logging receivers

The `receivers` element contains a set of receivers, each identified by a RECEIVER_ID. A receiver describes how to retrieve the logs; for example, by tailing files, by using a TCP port, or from the Windows Event Log.

### Structure of logging receivers

Each receiver must have an identifier, RECEIVER_ID, and include a `type` element. The valid types are:

  * `files`: Collect logs by tailing files on disk.
  * `fluent_forward` (Ops Agent versions 2.12.0 and later): Collect logs sent via the Fluent Forward protocol over TCP.
  * `tcp` (Ops Agent versions 2.3.0 and later): Collect logs in JSON format by listening to a TCP port.
  * Linux only: 
    * `syslog`: Collect Syslog messages over TCP or UDP.
    * `systemd_journald` (Ops Agent versions 2.4.0 and later): Collect systemd journal logs from the systemd-journald service.
  * Windows only: 
    * `windows_event_log`: Collect Windows Event Logs using the Windows Event Log API.
  * [Third-party application log receivers](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party)



The `receivers` structure looks like the following:
    
    
    receivers:
      RECEIVER_ID:
        type: files
        ...
      RECEIVER_ID_2:
        type: syslog
        ...
    

Depending on the value of the `type` element, there might be other configuration options, as follows:

  * `files` receivers:

    * `include_paths`: Required. A list of filesystem paths to read by tailing each file. The following wildcards can be used in the paths:

      * `*`: Matches any sequence of non-path-separator characters within a single directory or file name.

        * Example (Linux): `/var/log/*.log` matches all files ending in `.log` directly within `/var/log/`.
        * Example (Linux): `/var/log/app_*/server.log` matches `/var/log/app_1/server.log` and `/var/log/app_2/server.log`, but **doesn't** match `/var/log/app_1/v2/server.log`.
      * `**` (globstar): Matches zero or more directories in a path. This pattern is used to match files across multiple directory levels (recursively).

        * Example (Linux): `/var/log/**/*.log` matches any file ending with `.log` within `/var/log` or any of its subdirectories at any depth (e.g., `/var/log/app1.log`,`/var/log/apache2/access.log`).
        * Example (Linux): To collect logs from application instances that create versioned or instance-specific subdirectories, like `/opt/my-app/logs/instance-01/app.log`, `/opt/my-app/logs/groupA/instance-02/app.log`, globstar can be used: `/opt/my-app/logs/**/*.log`
**Note:** When specifying wildcards on Windows, you must use `\` as a separator.

For a list of common Linux application log files, see Common Linux log files.

    * `exclude_paths`: Optional. A list of filesystem path patterns to exclude from the set matched by `include_paths`.

    * `record_log_file_path`: Optional. If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.

    * `wildcard_refresh_interval`: Optional. The interval at which wildcard file paths in `include_paths` are refreshed. Given as a time duration, for example, `30s`, `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval. If not specified, the default interval is 60 seconds.

  * `fluent_forward` receivers:

    * `listen_host`: Optional. An IP address to listen on. The default value is `127.0.0.1`.

    * `listen_port`: Optional. A port to listen on. The default value is `24224`.

  * `syslog` receivers (for Linux only):

    * `transport_protocol`: Supported values: `tcp`, `udp`.

    * `listen_host`: An IP address to listen on.

    * `listen_port`: A port to listen on.

  * `tcp` receivers:

    * `format`: Required. Log format. Supported value: `json`.

    * `listen_host`: Optional. An IP address to listen on. The default value is `127.0.0.1`.

    * `listen_port`: Optional. A port to listen on. The default value is `5170`.

  * `windows_event_log` receivers (for Windows only):

    * `channels`: Required. A list of Windows Event Log channels from which to read logs.
    * `receiver_version`: Optional. Controls which Windows Event Log API to use. Supported values are `1` and `2`. The default value is `1`.

**Caution:** Version `1` is supported for backwards compatibility only. When configuring a new receiver, use version `2`. To read from channels under the "Applications and Services" category in Event Viewer, you must use version `2`.
    * `render_as_xml`: Optional. If set to `true`, then all Event Log fields, except for `jsonPayload.Message` and `jsonPayload.StringInserts`, are rendered as an XML document in a string field named `jsonPayload.raw_xml`. The default value is `false`. This cannot be set to `true` when `receiver_version` is `1`.




### Examples of logging receivers

Sample `files` receiver:
    
    
    receivers:
      RECEIVER_ID:
        type: files
    
        include_paths: [/var/log/*.log]
        exclude_paths: [/var/log/not-this-one.log]
        record_log_file_path: true
    

Sample `fluent_forward` receiver:

**Note:** [Tags](https://docs.fluentbit.io/manual/concepts/key-concepts#tag) from incoming records are preserved in the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)'s `logName` field as a dot-separated suffix (`logName` = "projects/PROJECT_ID/logs/RECEIVER_ID.TAG"). 
    
    
    receivers:
      RECEIVER_ID:
        type: fluent_forward
    
        listen_host: 127.0.0.1
        listen_port: 24224
    

Sample `syslog` receiver (Linux only):
    
    
    receivers:
      RECEIVER_ID:
        type: syslog
    
        transport_protocol: tcp
        listen_host: 0.0.0.0
        listen_port: 5140
    

Sample `tcp` receiver:
    
    
    receivers:
      RECEIVER_ID:
        type: tcp
    
        format: json
        listen_host: 127.0.0.1
        listen_port: 5170
    

Sample `windows_event_log` receiver (Windows only):
    
    
    receivers:
      RECEIVER_ID:
        type: windows_event_log
    
        channels: [System,Application,Security]
    

Sample `windows_event_log` receiver that overrides the built-in receiver to use version `2`:
    
    
    receivers:
      windows_event_log:
        type: windows_event_log
    
        channels: [System,Application,Security]
        receiver_version: 2
    

Sample `systemd_journald` receiver:
    
    
    receivers:
      RECEIVER_ID:
        type: systemd_journald
    

### Special fields in structured payloads

For processors and receivers that can ingest structured data (the `fluent_forward` and `tcp` receivers and the `parse_json` processor), you can set special fields in the input that will map to specific fields in the `LogEntry` object that the agent writes to the Logging API.

When the Ops Agent receives external structured log data, it places top-level fields into the `LogEntry`'s `jsonPayload` field unless the field name is listed in the following table:

Record field | [LogEntry field](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)  
---|---  
Option 1
    
    
    "timestamp": {
      "seconds": CURRENT_SECONDS,
      "nanos": CURRENT_NANOS,
    }

Option 2
    
    
    {
      "timestampSeconds": CURRENT_SECONDS,
      "timestampNanos": CURRENT_NANOS,
    }

| `timestamp`  
receiver_id (not a record field) | `logName`  
`logging.googleapis.com/httpRequest` ([HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#httprequest)) | `httpRequest`  
`logging.googleapis.com/severity` ([string](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity)) | `severity`  
`logging.googleapis.com/labels` ([struct of string:string](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)) | `labels`  
`logging.googleapis.com/operation` ([struct](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logentryoperation)) | `operation`  
`logging.googleapis.com/sourceLocation` ([struct](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logentrysourcelocation)) | `sourceLocation`  
`logging.googleapis.com/trace` ([string](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.trace)) | `trace`  
`logging.googleapis.com/spanId` ([string](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.span_id)) | `spanId`  
  
Any remaining structured record fields remain part of the `jsonPayload` structure.

### Common Linux log files

The following table lists common log files for frequently used Linux applications:

Application | Common log files  
---|---  
apache | For information about Apache log files, see [ Monitoring third-party applications: Apache Web Server](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/apache).   
cassandra | For information about Cassandra log files, see [ Monitoring third-party applications: Cassandra](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/cassandra).   
chef |  ` /var/log/chef-server/bookshelf/current  
/var/log/chef-server/chef-expander/current  
/var/log/chef-server/chef-pedant/http-traffic.log  
/var/log/chef-server/chef-server-webui/current  
/var/log/chef-server/chef-solr/current  
/var/log/chef-server/erchef/current  
/var/log/chef-server/erchef/erchef.log.1  
/var/log/chef-server/nginx/access.log  
/var/log/chef-server/nginx/error.log  
/var/log/chef-server/nginx/rewrite-port-80.log  
/var/log/chef-server/postgresql/current `  
gitlab |  ` /home/git/gitlab/log/application.log  
/home/git/gitlab/log/githost.log  
/home/git/gitlab/log/production.log  
/home/git/gitlab/log/satellites.log  
/home/git/gitlab/log/sidekiq.log  
/home/git/gitlab/log/unicorn.stderr.log  
/home/git/gitlab/log/unicorn.stdout.log  
/home/git/gitlab-shell/gitlab-shell.log `  
jenkins |  ` /var/log/jenkins/jenkins.log  
`  
jetty |  ` /var/log/jetty/out.log  
/var/log/jetty/*.request.log  
/var/log/jetty/*.stderrout.log `  
joomla |  ` /var/www/joomla/logs/*.log `  
magento |  ` /var/www/magento/var/log/exception.log  
/var/www/magento/var/log/system.log  
/var/www/magento/var/report/* `  
mediawiki |  ` /var/log/mediawiki/*.log `  
memcached | For information about Memcached log files, see [ Monitoring third-party applications: Memcached](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/memcached).   
mongodb | For information about MongoDB log files, see [ Monitoring third-party applications: MongoDB](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mongodb).   
mysql | For information about MySQL log files, see [ Monitoring third-party applications: MySQL](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mysql).   
nginx | For information about nginx log files, see [ Monitoring third-party applications: nginx](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/nginx).   
postgres | For information about PostgreSQL log files, see [ Monitoring third-party applications: PostgreSQL](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/postgresql).   
puppet |  ` /var/log/puppet/http.log  
/var/log/puppet/masterhttp.log `  
puppet-enterprise |  ` /var/log/pe-activemq/activemq.log  
/var/log/pe-activemq/wrapper.log  
/var/log/pe-console-auth/auth.log  
/var/log/pe-console-auth/cas_client.log  
/var/log/pe-console-auth/cas.log  
/var/log/pe-httpd/access.log  
/var/log/pe-httpd/error.log  
/var/log/pe-httpd/other_vhosts_access.log  
/var/log/pe-httpd/puppetdashboard.access.log  
/var/log/pe-httpd/puppetdashboard.error.log  
/var/log/pe-httpd/puppetmasteraccess.log  
/var/log/pe-mcollective/mcollective_audit.log  
/var/log/pe-mcollective/mcollective.log  
/var/log/pe-puppet-dashboard/certificate_manager.log  
/var/log/pe-puppet-dashboard/event-inspector.log  
/var/log/pe-puppet-dashboard/failed_reports.log  
/var/log/pe-puppet-dashboard/live-management.log  
/var/log/pe-puppet-dashboard/mcollective_client.log  
/var/log/pe-puppet-dashboard/production.log  
/var/log/pe-puppetdb/pe-puppetdb.log  
/var/log/pe-puppet/masterhttp.log  
/var/log/pe-puppet/rails.log `  
rabbitmq | For information about RabbitMQ log files, see [ Monitoring third-party applications: RabbitMQ](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/rabbitmq).   
redis | For information about Redis log files, see [ Monitoring third-party applications: Redis](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/redis).   
redmine |  ` /var/log/redmine/*.log `  
salt |  ` /var/log/salt/key  
/var/log/salt/master  
/var/log/salt/minion  
/var/log/salt/syndic.loc `  
solr | For information about Apache Solr log files, see [ Monitoring third-party applications: Apache Solr](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/solr).   
sugarcrm |  ` /var/www/*/sugarcrm.log `  
syslog |  ` /var/log/syslog  
/var/log/messages `  
tomcat | For information about Apache Tomcat log files, see [ Monitoring third-party applications: Apache Tomcat](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/tomcat).   
zookeeper | For information about Apache ZooKeeper log files, see [ Monitoring third-party applications: Apache ZooKeeper](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/zookeeper).   
  
### Default ingested labels

Logs can contain the following labels by default in the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry):

Field | Sample Value | Description  
---|---|---  
`labels."compute.googleapis.com/resource_name"` | `test_vm` | The name of the virtual machine from which this log originates. Written for all logs.  
`labels."logging.googleapis.com/instrumentation_source"` | `agent.googleapis.com/apache_access` | The value of the receiver `type` from which thus log originates, prefixed by `agent.googleapis.com/`. Written only by receivers from third-party integrations.  
  
## Logging processors

The optional `processors` element contains a set of processing directives, each identified by a PROCESSOR_ID. A processor describes how to manipulate the information collected by a receiver.

Each processor must have a unique identifier and include a `type` element. The valid types are:

  * `parse_json`: Parse JSON-formatted structured logs.
  * `parse_multiline`: Parse multiline logs. (Linux only)
  * `parse_regex`: Parse text-formatted logs via regex patterns to turn them into JSON-formatted structured logs.
  * `exclude_logs`: Exclude logs that match specified rules (starting in 2.9.0).
  * `modify_fields`: Set/transform fields in log entries (starting in 2.14.0).



The `processors` structure looks like the following:
    
    
    processors:
      PROCESSOR_ID:
        type: parse_json
        ...
      PROCESSOR_ID_2:
        type: parse_regex
        ...
    

Depending on the value of the `type` element, there are other configuration options, as follows.

### `parse_json` processor

#### Configuration structure
    
    
    processors:
      PROCESSOR_ID:
        type: parse_json
    
        time_key:    <field name within jsonPayload>
        time_format: <strptime format string>
    

The `parse_json` processor parses the input JSON into the `jsonPayload` field of the `LogEntry`. Other parts of the `LogEntry` can be parsed by setting certain special top-level fields.

  * `time_key`: Optional. If the log entry provides a field with a timestamp, this option specifies the name of that field. The extracted value is used to set the `timestamp` field of the resulting [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and is removed from the payload.

If the `time_key` option is specified, you must also specify the following:

    * `time_format`: Required if `time_key` is used. This option specifies the format of the `time_key` field so it can be recognized and analyzed properly. For details of the format, see the [`strptime(3)`](https://linux.die.net/man/3/strptime) guide.



##### Example configuration
    
    
    processors:
      PROCESSOR_ID:
        type: parse_json
    
        time_key:    time
        time_format: "%Y-%m-%dT%H:%M:%S.%L%Z"
    

### `parse_multiline` processor

#### Configuration structure
    
    
    processors:
      PROCESSOR_ID:
        type: parse_multiline
    
        match_any:
        - type: <type of the exceptions>
          language: <language name>
    

  * `match_any`: Required. A list of one or more rules.

    * `type`: Required. Only a single value is supported:

      * `language_exceptions`: Allows the processor to concatenate exceptions into one `LogEntry`, based on the value of the `language` option.
    * `language`: Required. Only a single value is supported:

      * `java`: Concatenates common Java exceptions into one `LogEntry`.
      * `python`: Concatenates common Python exceptions into one `LogEntry`.
      * `go`: Concatenates common Go exceptions into one `LogEntry`.



##### Example configuration
    
    
    logging:
      receivers:
        custom_file1:
          type: files
          include_paths:
          - /tmp/test-multiline28
      processors:
        parse_java_multiline:
          type: parse_multiline
          match_any:
          - type: language_exceptions
            language: java
        extract_structure:
          type: parse_regex
          field: message
          regex: "^(?<time>[\d-]*T[\d:.Z]*) (?<severity>[^ ]*) (?<file>[^ :]*):(?<line>[\d]*) - (?<message>(.|\\n)*)$"
          time_key: time
          time_format: "%Y-%m-%dT%H:%M:%S.%L"
        move_severity:
          type: modify_fields
          fields:
            severity:
              move_from: jsonPayload.severity
      service:
        pipelines:
          pipeline1:
            receivers: [custom_file1]
            processors: [parse_java_multiline, extract_structure, move_severity]
    

In the `extract_structure` processor, the `field: message` statement means that the regular expression is applied to the log entry's `jsonPayload.message` field. By default, the files receiver places each line of the log file into a log entry with a single payload field called `jsonPayload.message`.

The `extract_structure` processor places extracted fields into subfields of the `LogEntry.jsonPayload` field. Other statements in the YAML file cause two of the extracted fields, `time` and `severity`, to be moved. The `time_key: time` statement pulls the `LogEntry.jsonPayload.time` field, parses the timestamp, and then adds the `LogEntry.timestamp` field. The `move_severity` processor moves the severity field from the `LogEntry.jsonPayload.severity` field to the `LogEntry.severity` field.

Example log file:
    
    
    2022-10-17T22:00:00.187512963Z ERROR HelloWorld:16 - javax.servlet.ServletException: Something bad happened
        at com.example.myproject.OpenSessionInViewFilter.doFilter(OpenSessionInViewFilter.java:60)
        at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1157)
        at com.example.myproject.ExceptionHandlerFilter.doFilter(ExceptionHandlerFilter.java:28)
        at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1157)
        at com.example.myproject.OutputBufferFilter.doFilter(OutputBufferFilter.java:33)
    Caused by: com.example.myproject.MyProjectServletException
        at com.example.myproject.MyServlet.doPost(MyServlet.java:169)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:727)
        at javax.servlet.http.HttpServlet.service(HttpServlet.java:820)
        at org.mortbay.jetty.servlet.ServletHolder.handle(ServletHolder.java:511)
        at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1166)
        at com.example.myproject.OpenSessionInViewFilter.doFilter(OpenSessionInViewFilter.java:30)
        ... 27 common frames omitted
    

The agent ingests each line from the log file into Cloud Logging in the following format:
    
    
    {
      "insertId": "...",
      "jsonPayload": {
        "line": "16",
        "message": "javax.servlet.ServletException: Something bad happened\n    at com.example.myproject.OpenSessionInViewFilter.doFilter(OpenSessionInViewFilter.java:60)\n    at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1157)\n    at com.example.myproject.ExceptionHandlerFilter.doFilter(ExceptionHandlerFilter.java:28)\n    at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1157)\n    at com.example.myproject.OutputBufferFilter.doFilter(OutputBufferFilter.java:33)\nCaused by: com.example.myproject.MyProjectServletException\n    at com.example.myproject.MyServlet.doPost(MyServlet.java:169)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:727)\n    at javax.servlet.http.HttpServlet.service(HttpServlet.java:820)\n    at org.mortbay.jetty.servlet.ServletHolder.handle(ServletHolder.java:511)\n    at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1166)\n    at com.example.myproject.OpenSessionInViewFilter.doFilter(OpenSessionInViewFilter.java:30)\n    ... 27 common frames omitted\n",
        "file": "HelloWorld"
      },
      "resource": {
        "type": "gce_instance",
        "labels": {
          "instance_id": "...",
          "project_id": "...",
          "zone": "..."
        }
      },
      "timestamp": "2022-10-17T22:00:00.187512963Z",
      "severity": "ERROR",
      "labels": {
        "compute.googleapis.com/resource_name": "..."
      },
      "logName": "projects/.../logs/custom_file",
      "receiveTimestamp": "2022-10-18T03:12:38.430364391Z"
    }
    

### `parse_regex` processor

#### Configuration structure
    
    
    processors:
      PROCESSOR_ID:
        type: parse_regex
    
        regex: <regular expression>
    
        time_key:    <field name within jsonPayload>
        time_format: <format string>
    

  * `time_key`: Optional. If the log entry provides a field with a timestamp, this option specifies the name of that field. The extracted value is used to set the `timestamp` field of the resulting [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) and is removed from the payload.

If the `time_key` option is specified, you must also specify the following:

    * `time_format`: Required if `time_key` is used. This option specifies the format of the `time_key` field so it can be recognized and analyzed properly. For details of the format, see the [`strptime(3)`](https://linux.die.net/man/3/strptime) guide.
  * `regex`: Required. The regular expression for parsing the field. The expression must include key names for the matched subexpressions; for example, `"^(?<time>[^ ]*) (?<severity>[^ ]*) (?<msg>.*)$"`.

The text matched by named capture groups will be placed into fields in the `LogEntry`'s `jsonPayload` field. To add additional structure to your logs, use the `modify_fields` processor.

For a set of regular expressions for extracting information from common Linux application log files, see Common Linux log files.




##### Example configuration
    
    
    processors:
      PROCESSOR_ID:
        type: parse_regex
    
        regex:       "^(?<time>[^ ]*) (?<severity>[^ ]*) (?<msg>.*)$"
        time_key:    time
        time_format: "%Y-%m-%dT%H:%M:%S.%L%Z"
    

### `exclude_logs` processor

#### Configuration structure:
    
    
    type: exclude_logs
    match_any:
      - <filter>
      - <filter>
    

The top-level configuration for this processor contains a single field, `match_any`, which contains a list of filter rules.

  * `match_any`: Required. A list of one or more rules. If a log entry matches any rule, then the Ops Agent doesn't ingest that entry.

The logs that are ingested by Ops Agent follow the [`LogEntry` structure](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Field names are case-sensitive. You can only specify rules based on the following fields and their subfields:

    * `httpRequest`
    * `jsonPayload`
    * `labels`
    * `operation`
    * `severity`
    * `sourceLocation`
    * `trace`
    * `spanId`

The following example rule
    
    severity =~ "(DEBUG|INFO)"
    

uses a regular expression to exclude all `DEBUG` and `INFO` level logs.

Rules follow the [Cloud Logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) syntax but only support a subset of the features that Logging query language supports:

    * Comparison operators: `=`, `!=`, `:`, `=~`, `!~`. Only string comparisons are supported.
    * Navigation operator: `.`. For example `jsonPayload.message`.
    * Boolean operators: `AND`, `OR`, `NOT`.
    * Grouping expressions with `(` `)`.

**Note:** Using the `exclude_logs` processor has performance implications, so it's recommended that you avoid using this processor if you can exclude logs from the source or if you can set up [exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions). If you need to use the `exclude_logs` processor, we recommend the following best practices: 

  * Minimize the number of `exclude_logs` processors.
  * Use exact matches whenever possible instead of using regular-expression matches.



#### Example configuration
    
    
    processors:
      PROCESSOR_ID:
        type: exclude_logs
        match_any:
        - '(jsonPayload.message =~ "log spam 1" OR jsonPayload.message =~ "log spam 2") AND severity = "ERROR"'
        - 'jsonPayload.application = "foo" AND severity = "INFO"'
    

### `modify_fields` Processor

The `modify_fields` processor allows customization of the structure and contents of log entries.

#### Configuration structure
    
    
    type: modify_fields
    fields:
      <destination field>:
        # Source
        move_from: <source field>
        copy_from: <source field>
        static_value: <string>
        
        # Mutation
        default_value: <string>
        map_values:
          <old value>: <new value>
        type: {integer|float}
        omit_if: <filter>
    

The top-level configuration for this processor contains a single field, `fields`, which contains a map of output field names and corresponding translations. For each output field, an optional source and zero or more mutation operations are applied.

All field names use [the dot-separated syntax](https://docs.cloud.google.com/logging/docs/view/logging-query-language#comparisons) from the Cloud Logging query language. Filters use the Cloud Logging query language.

All transformations are applied in parallel, which means that sources and filters operate on the original input log entry and therefore can not reference the new value of any other fields being modified by the same processor.

**Source options** : At most one specified source is allowed.

  * No source specified

If no source value is specified, the existing value in the destination field will be modified.

  * `move_from: <source field>`

The value from `<source field>` will be used as the source for the destination field. Additionally, `<source field>` will be removed from the log entry. If a source field is referenced by both `move_from` and `copy_from`, the source field will still be removed.

  * `copy_from: <source field>`

The value from `<source field>` will be used as the source for the destination field. `<source field>` will not be removed from the log entry unless it is also referenced by a `move_from` operation or otherwise modified.

  * `static_value: <string>`

The static string `<string>` will be used as the source for the destination field.




**Mutation options** : Zero or more mutation operators may be applied to a single field. If multiple operators are supplied, they will always be applied in the following order.

  1. `default_value: <string>`

If the source field did not exist, the output value will be set to `<string>`. If the source field already exists (even if it contains an empty string), the original value is unmodified.

  2. `map_values: <map>`

If the input value matches one of the keys in `<map>`, the output value will be replaced with the corresponding value from the map.

  3. `map_values_exclusive: {true|false}`

In case the `<source field>` value does not match any keys specified in the `map_values` pairs, the destination field will be forcefully unset if `map_values_exclusive` is true, or left untouched if `map_values_exclusive` is false.

  4. `type: {integer|float}`

The input value will be converted to an integer or a float. If the string cannot be converted to a number, the output value will be unset. If the string contains a float but the type is specified as `integer`, the number will be truncated to an integer.

Note that the Cloud Logging API uses JSON and therefore it does not support a full 64-bit integer; if a 64-bit (or larger) integer is needed, it must be stored as a string in the log entry.

  5. `omit_if: <filter>`

If the filter matches the input log record, the output field will be unset. This can be used to remove placeholder values, such as:
         
         httpRequest.referer:
           move_from: jsonPayload.referer
           omit_if: httpRequest.referer = "-"
         




#### Sample Configurations

The `parse_json` processor would transform a JSON file containing
    
    
    {
      "http_status": "400",
      "path": "/index.html",
      "referer": "-"
    }
    

into a [LogEntry structure](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) that looks like this:
    
    
    {
      "jsonPayload": {
        "http_status": "400",
        "path": "/index.html",
        "referer": "-"
      }
    }
    

This could then be transformed with `modify_fields` into this `LogEntry`:
    
    
    {
      "httpRequest": {
        "status": 400,
        "requestUrl": "/index.html",
      }
    }
    

by using this Ops Agent configuration:
    
    
    logging:
      receivers:
        in:
          type: files
          include_paths:
          - /var/log/http.json
      processors:
        parse_json:
          type: parse_json
        set_http_request:
          type: modify_fields
          fields:
            httpRequest.status:
              move_from: jsonPayload.http_status
              type: integer
            httpRequest.requestUrl:
              move_from: jsonPayload.path
            httpRequest.referer:
              move_from: jsonPayload.referer
              omit_if: jsonPayload.referer = "-"
      service:
        pipelines:
          pipeline:
            receivers: [in]
            processors: [parse_json, set_http_request]
    

This configuration reads JSON-formatted logs from `/var/log/http.json` and populates part of the `httpRequest` structure from fields in the logs.

## Logging service

The logging service customizes verbosity for the Ops Agent's own logs, and links logging receivers and processors together into pipelines. The `service` section has the following elements:

  * `log_level`
  * `pipelines`



### Log verbosity level

The `log_level` field, available with Ops Agent versions 2.6.0 and later, customizes verbosity for Ops Agent logging submodule's own logs. The default is `info`. Available options are: `error`, `warn`, `info`, `debug`, `trace`.

**Warning:** Setting the `log_level` to `debug` (or `trace`) triggers a feedback loop in the logging sub-agent, resulting in a continuous stream of logs. This is a known issue, and is being addressed. In the meantime, _do not_ set `log_level` to anything above `info`.

The following configuration customizes log verbosity for the logging submodule to be `debug` instead:
    
    
    logging:
      service:
        log_level: debug
    

### Logging pipelines

The `pipelines` field can contain multiple pipeline IDs and definitions. Each `pipeline` value consists of the following elements:

  * `receivers`: Required for new pipelines. A list of receiver IDs, as described in Logging receivers. The order of the receivers IDs in the list doesn't matter. The pipeline collects data from all of the listed receivers.

  * `processors`: Optional. A list of processor IDs, as described in Logging processors. The order of the processor IDs in the list matters. Each record is run through the processors in the listed order.




### Example logging `service` configurations

A `service` configuration has the following structure:
    
    
    service:
      log_level: CUSTOM_LOG_LEVEL
      pipelines:
        PIPELINE_ID:
          receivers:  [...]
          processors: [...]
        PIPELINE_ID_2:
          receivers:  [...]
          processors: [...]
    

To stop the agent from collecting and sending either `/var/log/message` or `/var/log/syslog` entries, redefine the default pipeline with an empty `receivers` list and no processors. This configuration does not stop the agent's logging subcomponent, because the agent must be able to collect logs for the monitoring subcomponent. The entire empty logging configuration looks like the following:
    
    
    logging:
      service:
        pipelines:
          default_pipeline:
            receivers: []
    

The following `service` configuration defines a pipeline with the ID `custom_pipeline`:
    
    
    logging:
      service:
        pipelines:
          custom_pipeline:
            receivers:
            - RECEIVER_ID
            processors:
            - PROCESSOR_ID
    

## Metrics configurations

The `metrics` configuration uses the configuration model described previously:

  * `receivers`: a list of receiver definitions. A `receiver` describes the source of the metrics; for example, system metrics like `cpu` or `memory`. The receivers in this list can be shared among multiple pipelines.
  * `processors`: a list of processor definitions. A `processor` describes how to modify the metrics collected by a receiver.
  * `service`: contains a `pipelines` section that is a list of `pipeline` definitions. A `pipeline` connects a list of `receivers` and a list of `processors` to form the data flow.



The following sections describe each of these elements.

The Ops Agent sends metrics to Cloud Monitoring. You can't configure it to export metrics to other services.

### Metrics receivers

The `receivers` element contains a set of receiver definitions. A receiver describes from where to retrieve the metrics, such as `cpu` and `memory`. A receiver can be shared among multiple pipelines.

#### Structure of metrics receivers

Each receiver must have an identifier, RECEIVER_ID, and include a `type` element. Valid built-in types are:

  * `hostmetrics`
  * `iis` (Windows only)
  * `mssql` (Windows only)



A receiver can also specify the operation `collection_interval` option. The value is in the format of a duration, for example, `30s` or `2m`. The default value is `60s`.

Each of these receiver types collects a set of metrics; for information about the specific metrics included, see Metrics ingested by the receivers.

#### Changing the collection interval in the metrics receivers

Some critical workloads might require fast alerting. By reducing the the collection interval for the metrics, you can configure more sensitive alerts. For information on how alerts are evaluated, see [Behavior of metric-based alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth).

For example, the following receiver changes the collection interval for host metrics (the receiver ID is `hostmetrics`) from the default of 60 seconds to 10 seconds:
    
    
    metrics:
      receivers:
        hostmetrics:
          type: hostmetrics
          collection_interval: 10s
    

**Note:** This override works because the receiver ID, `hostmetrics`, is the same as the ID of a receiver in the built-in configuration. Any pipeline that uses the `hostmetrics` receiver now uses this overridden configuration. 

You can also override the collection interval for the Windows `iis` and `mssql` metrics receivers using the same technique.

#### Metrics ingested by the receivers

The metrics ingested by the Ops Agent have identifiers that begin with the following pattern: `agent.googleapis.com/GROUP`. The GROUP component identifies a set of related metrics; it has values like `cpu`, `network`, and others.

##### The `hostmetrics` receiver

The `hostmetrics` receiver ingests the following metric groups. For more information, see the linked section for each group on the [Ops Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent) page.

Group | Metric  
---|---  
[ `cpu`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-cpu) | CPU load at 1 minute intervals  
CPU load at 5 minute intervals  
CPU load at 15 minute intervals  
CPU usage, with labels for CPU number and CPU state  
CPU usage percent, with labels for CPU number and CPU state   
[ `disk`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-disk) | Disk bytes read, with label for device  
Disk bytes written, with label for device  
Disk I/O time, with label for device  
Disk weighted I/O time, with label for device  
Disk pending operations, with label for device  
Disk merged operations, with labels for device and direction  
Disk operations, with labels for device and direction  
Disk operation time, with labels for device and direction  
Disk usage, with labels for device and state  
Disk utilization, with labels for device and state   
[ `gpu`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu)  
Linux only; see [ About the `gpu` metrics](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#receiver-nvml-metrics) for other important information.  | Current number of GPU memory bytes used, by state  
Maximum amount of GPU memory, in bytes, that has been allocated by the process  
Percentage of time in the process lifetime that one or more kernels has been running on the GPU  
Percentage of time, since last sample, the GPU has been active   
[ `interface`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-interface)  
Linux only  | Total count of network errors  
Total count of packets sent over the network  
Total number of bytes sent over the network   
[ `memory`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-memory) | Memory usage, with label for state (buffered, cached, free, slab, used)  
Memory usage percent, with label for state (buffered, cached, free, slab, used)   
[ `network`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-network) | TCP connection count, with labels for port and TCP state   
[ `swap`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-swap) | Swap I/O operations, with label for direction  
Swap bytes used, with labels for device and state  
Swap percent used, with labels for device and state   
[ `pagefile`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-pagefile)  
Windows only  | Current percentage of pagefile used by state   
[ `processes`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-processes) | Processes count, with label for state  
Processes forked count  
Per-process disk read I/O, with labels for process name + others  
Per-process disk write I/O, with labels for process name + others  
Per-process RSS usage, with labels for process name + others  
Per-process VM usage, with labels for process name + others   
**About the`gpu` metrics:**  


The `hostmetrics` receiver collects metrics reported by the [NVIDIA Management Library (NVML)](https://developer.nvidia.com/nvidia-management-library-nvml) as `agent.googleapis.com/gpu` metrics.

To collect these metrics, you must [ create your VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus) and [ install the GPU driver](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). The `hostmetrics` receiver doesn't collect these metrics on VMs with no attached GPUs.

Only Ops Agent version 2.38.0 or versions 2.41.0 or higher are compatible with GPU monitoring. **Do not install Ops Agent versions 2.39.0 and 2.40.0 on VMs with attached GPUs.** For more information, see [Agent crashes and report mentions NVIDIA](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#nvidia-crashes). 

You can install or upgrade the NVIDIA GPU driver by using package managers or local installation scripts. When using local installation scripts, the Ops Agent service must be stopped before the driver installation can proceed. To stop the agent, run the following command: 
    
    
    sudo systemctl stop google-cloud-ops-agent
    

You must also reboot the VM after installing or upgrading an NVIDIA GPU driver.

##### The `iis` receiver (Windows only)

The `iis` receiver (Windows only) ingests metrics of the `iis` group. For more information, see the [Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-iis) page.

Group | Metric  
---|---  
[ `iis`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-iis)  
Windows only  | Currently open connections to IIS  
Network bytes transferred by IIS  
Connections opened to IIS  
Requests made to IIS   
  
##### The `mssql` receiver (Windows only)

The `mssql` receiver (Windows only) ingests metrics of the `mssql` group. For more information, see the [Ops Agent metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-mssql) page.

Group | Metric  
---|---  
[ `mssql`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-mssql)  
Windows only  | Currently open connections to SQL server  
SQL server total transactions per second  
SQL server write transactions per second   
  
### Metrics processors

The `processor` element contains a set of processor definitions. A processor describes metrics from the receiver type to exclude. The only supported type is `exclude_metrics`, which takes a `metrics_pattern` option. The value is a list of globs that match the [Ops Agent metric types](https://docs.cloud.google.com/monitoring/api/metrics_opsagent) you want to exclude from the group collected by a receiver. For example:

  * To exclude all agent [CPU metrics](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-cpu), specify `agent.googleapis.com/cpu/*`.
  * To exclude the agent CPU utilization metric, specify `agent.googleapis.com/cpu/utilization`.
  * To exclude the client-side request-count metric from the [metrics collected by the Apache Cassandra third-party integration](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#opsagent-cassandra), specify `workloads.googleapis.com/cassandra.client.request.count`.
  * To exclude all client-side metrics from the [metrics collected by the Apache Cassandra third-party integration](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#opsagent-cassandra), specify `workloads.googleapis.com/cassandra.client.*`.



#### Sample metrics processor

The following example shows the `exclude_metrics` processor supplied in the built-in configurations. This processor supplies an empty `metrics_pattern` value, so it doesn't exclude any metrics.
    
    
    processors:
      metrics_filter:
        type: exclude_metrics
        metrics_pattern: []
    

To disable the collection of all process metrics by the Ops Agent, add the following to your `config.yaml` file:
    
    
    metrics:
      processors:
        metrics_filter:
          type: exclude_metrics
          metrics_pattern:
          - agent.googleapis.com/processes/*
    

This excludes process metrics from collection in the `metrics_filter` processor that applies to the default pipeline in the `metrics` service.

### Metrics service

The metrics service customizes verbosity for the Ops Agent metrics module's own logs and links metrics receivers and processors together into pipelines. The `service` section has two elements: `log_level` and `pipelines`.

#### Metrics verbosity level

`log_level`, available with Ops Agent versions 2.6.0 and later, customizes verbosity for Ops Agent metrics submodule's own logs. The default is `info`. Available options are: `error`, `warn`, `info`, `debug`.

#### Metrics pipelines

The `service` section has a single element, `pipelines`, which can contain multiple pipeline IDs and definitions. Each `pipeline` definition consists of the following elements:

  * `receivers`: Required for new pipelines. A list of receiver IDs, as described in Metrics receivers. The order of the receivers IDs in the list doesn't matter. The pipeline collects data from all of the listed receivers.

  * `processors`: Optional. A list of processor IDs, as described in Metrics processors. The order of the processor IDs in the list _does_ matter. Each metric point is run through the processors in the listed order.




#### Example metrics `service` configurations

A `service` configuration has the following structure:
    
    
    service:
      log_level: CUSTOM_LOG_LEVEL
      pipelines:
        PIPELINE_ID:
          receivers:  [...]
          processors: [...]
        PIPELINE_ID_2:
          receivers:  [...]
          processors: [...]
    

To turn off the built-in ingestion of host metrics, redefine the default pipeline with an empty `receivers` list and no processors. The entire metrics configuration looks like the following:
    
    
    metrics:
      service:
        pipelines:
          default_pipeline:
            receivers: []
    

The following example shows the built-in `service` configuration for Windows:
    
    
    metrics:
      service:
        pipelines:
          default_pipeline:
            receivers:
            - hostmetrics
            - iis
            - mssql
            processors:
            - metrics_filter
    

The following `service` configuration customizes log verbosity for the metrics submodule to be `debug` instead:
    
    
    metrics:
      service:
        log_level: debug
    

## Collection of self logs

By default, the Ops Agent's Fluent Bit self logs are sent to Cloud Logging. These logs can include a lot of information, and the additional volume might increase your costs to use Cloud Logging.

You can disable the collection of these self logs, starting with Ops Agent version 2.44.0, by using the `default_self_log_file_collection` option.

To disable self-log collection, add a `global` section to your user-specified configuration file and set the `default_self_log_file_collection` option to the value `false`:
    
    
    logging:  ...
    metrics:  ...
    global:
      default_self_log_file_collection: false
    

## Log-rotation configuration

Starting with Ops Agent version 2.31.0, you can also set up the agent's log-rotation feature by using the configuration files. For more information, see [Configure log rotation in the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/rotate-logs#configure-log-rotation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
