---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/redis/
title: Redis \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:47.029086+00:00
---

# Redis  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Redis Stay organized with collections  Save and categorize content based on your preferences. 

The Redis integration collects metrics related to performance and usage. Performance metrics focus on CPU, memory, and network throughput, and usage metrics focus on keys, commands, and replication. The integration also collects Redis logs and parses them into a JSON payload. During this process, the symbols for role and level are transformed into a human readable format.

For more information about Redis, see the [Redis documentation](http://redis.io/).

## Prerequisites

To collect Redis telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics, install version 2.7.0 or higher.
  * For logs, install version 2.5.0 or higher.



This integration supports Redis version 6.2.

## Configure the Ops Agent for Redis

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from Redis instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Redis:
    
    
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
        redis:
          type: redis
      service:
        pipelines:
          redis:
            receivers:
            - redis
    logging:
      receivers:
        redis:
          type: redis
      service:
        pipelines:
          redis:
            receivers:
            - redis
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

To ingest logs from Redis, you must create a receiver for the logs that Redis produces and then create a pipeline for the new receiver.

To configure a receiver for your `redis` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/redis/redis-server.log, /var/log/redis_6379.log, /var/log/redis/redis.log, /var/log/redis/default.log, /var/log/redis/redis_6379.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths; for example, `/var/log/redis/*.log`.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `redis`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `redis` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message, including detailed stacktrace where provided  
`jsonPayload.pid` | number | The process ID issuing the log  
`jsonPayload.role` | string | Translated from redis role character (sentinel, RDB/AOF_writing_child, slave, master)  
`jsonPayload.roleChar` | string | Redis role character (X, C, S, M)  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Redis, you must create a receiver for the metrics that Redis produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `redis` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`address` | `localhost:6379` | The URL exposed by Redis.  
`ca_file` |  | Path to the CA certificate. As a client, this verifies the server certificate. If empty, the receiver uses the system root CA.  
`cert_file` |  | Path to the TLS certificate to use for mTLS-required connections.  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`insecure` | `true` | Sets whether or not to use a secure TLS connection. If set to `false`, then TLS is enabled.  
`insecure_skip_verify` | `false` | Sets whether or not to skip verifying the certificate. If `insecure` is set to `true`, then the `insecure_skip_verify` value is not used.  
`key_file` |  | Path to the TLS key to use for mTLS-required connections.  
`password` |  | The password used to connect to the server.  
`type` |  | This value must be `redis`.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Redis instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/redis.clients.blocked`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.clients.connected`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.clients.max_input_buffer`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.clients.max_output_buffer`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.commands.processed`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.connections.received`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.connections.rejected`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.cpu.time`  
`CUMULATIVE`, `DOUBLE`  
**gce_instance** |  `state`  
`workload.googleapis.com/redis.keys.evicted`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.keys.expired`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.keyspace.hits`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.keyspace.misses`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.latest_fork`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.fragmentation_ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.lua`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.peak`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.rss`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.net.input`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.net.output`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.rdb.changes_since_last_save`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.replication.backlog_first_byte_offset`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.replication.offset`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/redis.slaves.connected`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
## Verify the configuration

This section describes how to verify that you correctly configured the Redis receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Redis logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("redis")
         




To verify that Redis metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/redis.clients.max_input_buffer", monitored_resource="gce_instance"}
         




## View dashboard

To view your Redis metrics, you must have a chart or dashboard configured. The Redis integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for Redis and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Redis integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Redis and click **View Details**. 
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

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
