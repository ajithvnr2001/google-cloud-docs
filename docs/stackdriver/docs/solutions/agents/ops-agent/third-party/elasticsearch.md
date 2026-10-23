---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/elasticsearch/
title: Elasticsearch 7.9+ \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:41:07.347575+00:00
---

# Elasticsearch 7.9+  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/elasticsearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Elasticsearch 7.9+ Stay organized with collections  Save and categorize content based on your preferences. 

Elasticsearch is an open-source search server, based on the [Lucene](https://lucene.apache.org/) search library. It runs in a Java virtual machine on top of a number of operating systems. The `elasticsearch` receiver collects node- and cluster-level telemetry from your Elasticsearch instances.

**Note:** This document refers only to the support for Elasticsearch 7.9+ versions. For information about later versions, see [Elasticsearch 8.0+ and 9.0+](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/elasticsearch9). The most significant difference between the two documents is in the names of some of the log fields.

For more information about Elasticsearch, see the [Elasticsearch 7.9+ documentation](http://elasticsearch.org/).

## Prerequisites

To collect Elasticsearch telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics, install version 2.21.0 or higher.
  * For logs, install version 2.9.0 or higher.



This integration supports Elasticsearch version 7.9+.

## Configure your Elasticsearch instance

If you enable [Elasticsearch security features](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/secure-cluster.html), you must configure a user with the `monitor` or `manage` [cluster privilege](https://www.elastic.co/guide/en/elasticsearch/reference/7.16/security-privileges.html#privileges-list-cluster).

## Configure the Ops Agent for Elasticsearch

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from Elasticsearch instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Elasticsearch:
    
    
    # Configures Ops Agent to collect telemetry from the app. You must restart the agent for the configuration to take effect.
    
    set -e
    
    # Check if the file exists
    if [ ! -f /etc/google-cloud-ops-agent/config.yaml ]; then
      # Create the file if it doesn't exist.
      sudo mkdir -p /etc/google-cloud-ops-agent
      sudo touch /etc/google-cloud-ops-agent/config.yaml
    fi
    
    # Create a back up of the existing file so existing configurations are not lost.
    sudo cp /etc/google-cloud-ops-agent/config.yaml /etc/google-cloud-ops-agent/config.yaml.bak
    
    # Configure the Ops Agent.
    sudo tee /etc/google-cloud-ops-agent/config.yaml > /dev/null << EOF
    metrics:
      receivers:
        elasticsearch:
          type: elasticsearch
      service:
        pipelines:
          elasticsearch:
            receivers:
              - elasticsearch
    
    logging:
      receivers:
        elasticsearch_json:
          type: elasticsearch_json
        elasticsearch_gc:
          type: elasticsearch_gc
      service:
        pipelines:
          elasticsearch:
            receivers:
              - elasticsearch_json
              - elasticsearch_gc
    EOF
    
    

For these changes to take effect, you must restart the Ops Agent:

### Linux

  1. To restart the agent, run the following command on your instance: 
         
         sudo systemctl restart google-cloud-ops-agent
         

  2. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         sudo systemctl status "google-cloud-ops-agent*"
         




### Windows

  1. Connect to your instance using RDP or a similar tool and login to Windows. 
  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**
  3. To restart the agent, run the following PowerShell command: 
         
         Restart-Service google-cloud-ops-agent -Force
         

  4. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         Get-Service google-cloud-ops-agent*
         




### Configure logs collection

To ingest logs from Elasticsearch, you must create a receiver for the logs that Elasticsearch produces and then create a pipeline for the new receiver.

To configure a receiver for your `elasticsearch_json` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/elasticsearch/*_server.json, /var/log/elasticsearch/*_deprecation.json, /var/log/elasticsearch/*_index_search_slowlog.json, /var/log/elasticsearch/*_index_indexing_slowlog.json, /var/log/elasticsearch/*_audit.json]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `elasticsearch_json`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
To configure a receiver for your `elasticsearch_gc` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/elasticsearch/gc.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `elasticsearch_gc`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `elasticsearch_json` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.cluster` | string | The cluster emitting the log record  
`jsonPayload.cluster.name` | string | The name of the cluster emitting the log record  
`jsonPayload.cluster.uuid` | string | The UUID of the cluster emitting the log record  
`jsonPayload.component` | string | The component of Elasticsearch that emitted the log  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message  
`jsonPayload.node` | string | The node emitting the log record  
`jsonPayload.node.name` | string | The name of the node emitting the log record  
`jsonPayload.node.uuid` | string | The UUID of the node emitting the log record  
`jsonPayload.type` | string | The type of log, indicating which log the record came from (e.g. _server_ indicates this LogEntry came from the server log)  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `elasticsearch_gc` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.gc_run` | number | The run of the garbage collector  
`jsonPayload.message` | string | Log message  
`jsonPayload.type` | string | The type of the log record  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Elasticsearch, you must create a receiver for the metrics that Elasticsearch produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `elasticsearch` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`ca_file` |  | Path to the CA certificate. As a client, this verifies the server certificate. If empty, the receiver uses the system root CA.  
`cert_file` |  | Path to the TLS certificate to use for mTLS-required connections.  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `http://localhost:92002` | The base URL for the Elasticsearch REST API.  
`insecure` | `true` | Sets whether or not to use a secure TLS connection. If set to `false`, then TLS is enabled.  
`insecure_skip_verify` | `false` | Sets whether or not to skip verifying the certificate. If `insecure` is set to `true`, then the `insecure_skip_verify` value is not used.  
`key_file` |  | Path to the TLS key to use for mTLS-required connections.  
`password` |  | Password for authentication with Elasticsearch. Required if `username` is set.  
`type` |  | This value must be `elasticsearch`.  
`username` |  | Username for authentication with Elasticsearch. Required if `password` is set.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Elasticsearch instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/elasticsearch.breaker.memory.estimated`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.breaker.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.breaker.tripped`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.cluster.data_nodes`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.health`  
`GAUGE`, `INT64`  
**gce_instance** |  `status`  
`workload.googleapis.com/elasticsearch.cluster.in_flight_fetch`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.nodes`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.pending_tasks`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.published_states.differences`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.published_states.full`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.cluster.shards`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.state_queue`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.state_update.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.cluster.state_update.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`type`  
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.total.primary_rejections`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.indexing_pressure.memory.total.replica_rejections`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.memory.indexing_pressure`  
`GAUGE`, `INT64`  
**gce_instance** |  `stage`  
`workload.googleapis.com/elasticsearch.node.cache.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `type`  
`workload.googleapis.com/elasticsearch.node.cache.evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `cache_name`  
`workload.googleapis.com/elasticsearch.node.cache.memory.usage`  
`GAUGE`, `INT64`  
**gce_instance** |  `cache_name`  
`workload.googleapis.com/elasticsearch.node.cluster.connections`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.cluster.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/elasticsearch.node.disk.io.read`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.disk.io.write`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.documents`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`workload.googleapis.com/elasticsearch.node.fs.disk.available`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.fs.disk.free`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.fs.disk.total`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.http.connections`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.ingest.documents`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.ingest.documents.current`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.ingest.operations.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.open_files`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.operations.completed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/elasticsearch.node.operations.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.documents.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.documents.preprocessed`  
`GAUGE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.node.pipeline.ingest.operations.failed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `name`  
`workload.googleapis.com/elasticsearch.node.script.cache_evictions`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.script.compilation_limit_triggered`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.script.compilations`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.shards.data_set.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.shards.reserved.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.shards.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.thread_pool.tasks.finished`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `state`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.thread_pool.tasks.queued`  
`GAUGE`, `INT64`  
**gce_instance** |  `thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.thread_pool.threads`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
`thread_pool_name`  
`workload.googleapis.com/elasticsearch.node.translog.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.translog.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.node.translog.uncommitted.size`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.15m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.1m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.load_avg.5m`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.cpu.usage`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/elasticsearch.os.memory`  
`GAUGE`, `INT64`  
**gce_instance** |  `state`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the Elasticsearch receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Elasticsearch logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("elasticsearch_json") OR log_id("elasticsearch_gc"))
         




To verify that Elasticsearch metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/elasticsearch.node.open_files", monitored_resource="gce_instance"}
         




## View dashboard

To view your Elasticsearch metrics, you must have a chart or dashboard configured. The Elasticsearch integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

You can also view static previews of dashboards without installing the integration.

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab, and then choose the **Integrations** category.
  3. Click the name of the dashboard you want to view. 



If you have configured an integration but the dashboard has not been installed, then check that the Ops Agent is running. When there is no metric data for a chart in the dashboard, installation of the dashboard fails. After the Ops Agent begins collecting metrics, the dashboard is installed for you.

To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Compute Engine** deployment-platform filter.
  3. Locate the entry for Elasticsearch and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Elasticsearch integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Elasticsearch and click **View Details**. 
  3. Select the **Alerts** tab. This tab provides descriptions of available alerting policies and provides an interface for installing them.
  4. Install alerting policies. Alerting policies need to know where to send notifications that the alert has been triggered, so they require information from you for installation. To install alerting policies, do the following: 
     1. From the list of available alerting policies, select those that you want to install.
     2. In the **Configure notifications** section, select one or more notification channels. You have the option to disable the use of notification channels, but if you do, then your alerting policies fire silently. You can check their status in Monitoring, but you receive no notifications.

For more information about notification channels, see [Manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

     3. Click **Create Policies**.



For more information about alerting policies in Cloud Monitoring, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## What's next

For a walkthrough on how to use Ansible to install the Ops Agent, configure a third-party application, and install a sample dashboard, see the [ Install the Ops Agent to troubleshoot third-party applications](https://www.youtube.com/watch?v=GQgNygd-XJU&t=7s) video.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
