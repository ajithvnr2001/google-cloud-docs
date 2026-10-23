---
url: https://docs.cloud.google.com/logging/docs/agent/logging/fluentd-config-compatibility/
title: Configuration compatibility for upstream Fluentd \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:19.071158+00:00
---

# Configuration compatibility for upstream Fluentd  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/logging/fluentd-config-compatibility/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Configuration compatibility for upstream Fluentd Stay organized with collections  Save and categorize content based on your preferences. 

As you migrate from the Logging agent to upstream Fluentd, you might encounter configuration incompatibilities that require workarounds to prevent startup errors. This document describes how to resolve the configuration incompatibilities.

## Syntax changes between the legacy Logging agent and upstream Fluentd

While the legacy Logging agent relies on Fluentd v0.12 syntax, upstream Fluentd adopts the v1 standard. This transition involves the deprecation of various parameters and the introduction of new nested directives to handle core functionality, replacing the previously used flat configuration structures.

**Important:** You must avoid mixing v0.12 and v1 syntax within the same plugin directive. If you mix styles, Fluentd ignores the v0.12 parameters, potentially causing data loss.

To prevent startup failures and ensure your logs are processed correctly, you must remove or replace the deprecated parameters. The following sections describe how to update the deprecated parameters.

### Output plugin configuration

The following table lists the parameters that must be updated in your output plugin configuration to avoid errors:

Legacy Logging agent syntax | Upstream Fluentd syntax | Notes  
---|---|---  
N/A | `<buffer>` | Fluentd output plugins support a `<buffer>` section, under the `<match>` section, to configure the buffering of events. For more information, see the [Config: Buffer Section](https://docs.fluentd.org/configuration/buffer-section) Fluentd documentation.  
`buffer_type` | `@type` |   
`buffer_path` | `path` |   
`buffer_chunk_limit` | `chunk_limit_size` |   
`disable_retry_limit` | `retry_forever` |   
`retry_limit` | `retry_max_times` |   
`max_retry_wait` | `retry_max_interval` |   
`num_threads` | `flush_thread_count` |   
`partial_success` | N/A | Remove this parameter. Upstream Fluentd permanently enables partial success by default, dropping only invalid lines.  
  
The following is an example of the `google-cloud` output plugin configuration in the legacy Logging agent:
    
    
    <match **>
      @type google_cloud
      buffer_type file
      buffer_path /var/log/google-fluentd/buffers
      buffer_chunk_limit 512KB
      flush_interval 5s
      disable_retry_limit false
      retry_limit 3
      retry_wait 10
      max_retry_wait 300
      num_threads 8
    </match>
    

After performing the updates, the configuration looks as follows:
    
    
    <match **>
      @type google_cloud
      <buffer>
        @type file
        path /var/log/google-fluentd/buffers
        chunk_limit 512KB
        flush_interval 5s
        retry_forever false
        retry_max_times 3
        retry_wait 10
        retry_max_interval 300
        flush_thread_count 8
      </buffer>
    </match>
    

### Input plugin configuration

The following table lists the parameters that must be updated in your input plugin configuration to avoid errors:

Legacy Logging agent syntax | Upstream Fluentd syntax | Notes  
---|---|---  
`format` | `<parse>` | For more information, see the [Config: Parse Section](https://docs.fluentd.org/configuration/parse-section) Fluentd documentation.  
`protocol_type` | `<transport>` | Indicate the protocol of the `syslog` transport, either `udp`, `tcp,` or `tls`.  
`auto_typecast` |  | Remove this parameter when used within the `json` parse plugin.  
  
The following is an example of an input plugin configuration in the legacy Logging agent:
    
    
    <source>
        @type tail
        path /var/log/my-app.log
        format json
    </source>
    

After performing the updates, the configuration looks as follows:
    
    
    <source>
        @type tail
        path /var/log/my-app.log
        <parse>
          @type json
        </parse>
    </source>
    

## Ruby `Time` object serialization

Upstream Fluentd requires explicit casting for raw Ruby `Time` objects used inside `<record>` filters, such as `record_transformer`. Without explicit casting, these objects cause a fatal serialization error during buffer flushing.

If your configuration uses `${time}` with `enable_ruby true`, you must explicitly cast the object to a primitive type, integer or string.

The following is an example of a filter plugin configuration in the legacy Logging agent:
    
    
    <filter foo.bar>
      @type record_transformer
       enable_ruby true
      <record>
        raw_timestamp ${time}
      </record>
    </filter>
    

After performing the updates, the configuration looks as follows:
    
    
    <filter foo.bar>
      @type record_transformer
       enable_ruby true
      <record>
        raw_timestamp ${time.to_i}
      </record>
    </filter>
    

## gRPC transport and compression defaulting

The `google_cloud` output plugin lets you configure whether to use gRPC instead of REST/JSON to communicate to the Cloud Logging API.

For improved performance, we recommend enabling gRPC transport and configuring `grpc_compression_algorithm gzip`. This combination minimizes network overhead and CPU consumption, particularly when processing substantial log volumes.

To implement these optimizations, use the following configuration:
    
    
    <match **>
      @type google_cloud
      use_grpc true
      grpc_compression_algorithm gzip
    </match>
    

Additionally, because gRPC relies on HTTP/2 streaming on port `443`, you must ensure that your network infrastructure permits gRPC/HTTP/2 traffic. In environments where gRPC is restricted, you must explicitly define `use_grpc false` to revert to standard HTTP/REST communication.

## RabbitMQ regular expression pattern

The regular expression patterns used by the legacy Logging agent for RabbitMQ log ingestion are often incompatible with the output formats of modern RabbitMQ versions. These discrepancies can lead to logs being incorrectly processed or silently discarded during the collection process.

Modern RabbitMQ logs incorporate millisecond precision in timestamps, such as `YYYY-MM-DD HH:MM:SS.L`, and feature specific severity and PID markers like `[info] <0.213.0>`, which the legacy regular expression failed to match.

If your Fluentd agent is configured to collect RabbitMQ logs, then you must update the `<parser>` section to correctly handle the current log format.

The following is an example of the RabbitMQ input plugin configuration for the legacy Logging agent:
    
    
    <source>
      @type tail
      path /var/log/rabbitmq/*.log
      pos_file /var/lib/google-fluentd/pos/rabbitmq.pos
      tag rabbitmq
      format multiline
      format_firstline /^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}/
      format1 /^(?<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) \[(?<severity>\w+)\] (?<message>.*)/
      time_format %Y-%m-%d %H:%M:%S
    </source>
    

After performing the updates, the configuration looks as follows:
    
    
    <source>
      @type tail
      path /var/log/rabbitmq/*.log
      pos_file /var/log/fluentd/pos/rabbitmq.pos
      read_from_head true
      tag rabbitmq
      <parse>
        @type multiline
        format_firstline /^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}/
        format1 /^(?<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}) \[(?<severity>[^\]]+)\] <(?<pid>[^>]+)> (?m:(?<message>.*))$/
        time_format %Y-%m-%d %H:%M:%S.%L
      </parse>
    </source>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
