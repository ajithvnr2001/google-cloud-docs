---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/flink/
title: Apache Flink \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:44:07.355433+00:00
---

# Apache Flink  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/flink/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Apache Flink Stay organized with collections  Save and categorize content based on your preferences. 

The Apache Flink integration collects client, jobmanager and taskmanager logs and parses them into a JSON payload. The result includes fields for source, level, and message.

For more information about Flink, see the [Apache Flink documentation](https://flink.apache.org/).

## Prerequisites

To collect Flink telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index):

  * For metrics, install version 2.18.1 or higher.
  * For logs, install version 2.17.0 or higher.



This integration supports Flink versions 1.12.5, 1.13.6, and 1.14.4.

## Configure the Ops Agent for Flink

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from Flink instances, and [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Flink:
    
    
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
        flink:
          type: flink
      service:
        pipelines:
          flink:
            receivers:
              - flink
    logging:
      receivers:
        flink:
          type: flink
      service:
        pipelines:
          flink:
            receivers:
              - flink
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

To ingest logs from Flink, you must create a receiver for the logs that Flink produces and then create a pipeline for the new receiver.

To configure a receiver for your `flink` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/opt/flink/log/flink-*-standalonesession-*.log, /opt/flink/log/flink-*-taskexecutor-*.log, /opt/flink/log/flink-*-client-*.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `flink`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `flink` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message, including detailed stacktrace where provided  
`jsonPayload.source` | string | The source Java class of the log entry  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Flink, you must create a receiver for the metrics that Flink produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `flink` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `http://localhost:8081` | The URL exposed by Flink.  
`type` |  | This value must be `flink`.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Flink instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/flink.job.checkpoint.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `checkpoint`  
`host_name`  
`job_name`  
`workload.googleapis.com/flink.job.checkpoint.in_progress`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.job.last_checkpoint.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.job.last_checkpoint.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.job.restart.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`workload.googleapis.com/flink.jvm.class_loader.classes_loaded`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.cpu.load`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.cpu.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.gc.collections.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `garbage_collector_name`  
`host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.gc.collections.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `garbage_collector_name`  
`host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.direct.total_capacity`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.direct.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.heap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.heap.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.heap.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.mapped.total_capacity`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.mapped.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.metaspace.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.metaspace.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.metaspace.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.nonheap.committed`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.nonheap.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.memory.nonheap.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.jvm.threads.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.memory.managed.total`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.memory.managed.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`resource_type`  
`taskmanager_id`  
`workload.googleapis.com/flink.operator.record.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`operator_name`  
`record`  
`subtask_index`  
`task_name`  
`taskmanager_id`  
`workload.googleapis.com/flink.operator.watermark.output`  
`GAUGE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`operator_name`  
`subtask_index`  
`task_name`  
`taskmanager_id`  
`workload.googleapis.com/flink.task.record.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host_name`  
`job_name`  
`record`  
`subtask_index`  
`task_name`  
`taskmanager_id`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the Flink receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Flink logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("flink")
         




To verify that Flink metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/flink.jvm.memory.heap.used", monitored_resource="gce_instance"}
         




## View dashboard

To view your Flink metrics, you must have a chart or dashboard configured. The Flink integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for Flink and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Flink integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Flink and click **View Details**. 
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
