---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/saphana/
title: SAP HANA \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:59.824896+00:00
---

# SAP HANA  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/saphana/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  SAP HANA Stay organized with collections  Save and categorize content based on your preferences. 

The SAP HANA integration collects SAP HANA metrics and logs. The metrics are collected by querying relevant monitoring views. This integration writes structured trace logs.

For more information about HANA, see the [SAP HANA documentation](https://www.sap.com/products/hana.html).

**Note:** For new installations, we recommend that you use [ Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana). The Agent for SAP is required for all SAP on Google Cloud workloads, as mandated by SAP. The Ops Agent SAP HANA integration duplicates some of the monitoring features of the Agent for SAP, but the Agent for SAP is the recommended solution. For more information, see [ Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

## Prerequisites

To collect HANA telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics, install version 2.18.1 or higher.
  * For logs, install version 2.18.1 or higher.



This integration supports HANA version 2.0.

## Configure your HANA instance

To collect metrics, a monitoring user requires `SELECT` access to the relevant monitoring views. The following SQL script creates a monitoring role and applies it to a monitoring user if executed by a user with sufficient permissions connected to the SAP HANA instance.
    
    
    --Create the user
    CREATE RESTRICTED USER otel_monitoring_user PASSWORD ;
    --Enable user login
    ALTER USER otel_monitoring_user ENABLE CLIENT CONNECT;
    --Create the monitoring role
    CREATE ROLE OTEL_MONITORING;
    --Grant permissions to the relevant views
    GRANT CATALOG READ TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_BACKUP_CATALOG TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_BLOCKED_TRANSACTIONS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_CONNECTIONS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_CS_ALL_COLUMNS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_CS_TABLES TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_DATABASE TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_DISKS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_HOST_RESOURCE_UTILIZATION TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_LICENSES TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_RS_TABLES TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_SERVICE_COMPONENT_MEMORY TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_SERVICE_MEMORY TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_SERVICE_REPLICATION TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_SERVICE_STATISTICS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_SERVICE_THREADS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_SERVICES TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_VOLUME_IO_TOTAL_STATISTICS TO OTEL_MONITORING;
    GRANT SELECT ON SYS.M_WORKLOAD TO OTEL_MONITORING;
    GRANT SELECT ON _SYS_STATISTICS.STATISTICS_CURRENT_ALERTS TO OTEL_MONITORING;
    GRANT SELECT ON DUMMY TO OTEL_MONITORING;
    --Add the OTEL_MONITOR role to the monitoring user
    GRANT OTEL_MONITORING TO otel_monitoring_user;
    

## Configure the Ops Agent for HANA

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from HANA instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for HANA:
    
    
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
    logging:
      receivers:
        saphana:
          type: saphana
          include_paths:
          - /usr/sap/*/HDB*/*/trace/*.trc
          exclude_paths:
          - /usr/sap/*/HDB*/*/trace/nameserver_history*.trc
          - /usr/sap/*/HDB*/*/trace/nameserver*loads*.trc
          - /usr/sap/*/HDB*/*/trace/nameserver*executed_statements*.trc
      service:
        pipelines:
          saphana:
            receivers:
              - saphana
    metrics:
      receivers:
        saphana:
          type: saphana
          username: SYSTEM
          password: G00g3l21
          # To use the googlesecretmanager provider to replace plaintext passwords, refer to the example below.
          # password: ${googlesecretmanager:projects/<project-id>/secrets/<secret-id>/versions/<version-id>}
          endpoint: localhost:30015
      service:
        pipelines:
          saphana:
            receivers:
              - saphana
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

To ingest logs from HANA, you must create a receiver for the logs that HANA produces and then create a pipeline for the new receiver.

To configure a receiver for your `saphana` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` | `[/usr/sap/*/HDB*/${HOSTNAME}/trace/nameserver_history*.trc, /usr/sap/*/HDB*/${HOSTNAME}/trace/nameserver*loads*.trc, /usr/sap/*/HDB*/${HOSTNAME}/trace/nameserver*executed_statements*.trc]` | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/usr/sap/*/HDB*/${HOSTNAME}/trace/*.trc]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | The value must be `saphana`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `saphana` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.component` | string | SAP HANA component  
`jsonPayload.connection_id` | number | ID of the connection where the message originated, if message was logged within the scope of a connection  
`jsonPayload.message` | string | Log message  
`jsonPayload.severity_flag` | string | Log entry level  
`jsonPayload.thread_id` | number | ID of the thread logging the message  
`jsonPayload.transaction_id` | number | ID of the transaction where the message originated, if message was logged within the scope of a transaction  
`jsonPayload.update_transaction_id` | number | ID of the update transaction where the message originated, if message was logged within the scope of an update transaction  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
`sourceLocation.file` | string | Source file name  
`sourceLocation.line` | number | Line within the source file  
  
### Configure metrics collection

To ingest metrics from HANA, you must create a receiver for the metrics that HANA produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `saphana` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`ca_file` |  | Path to the CA certificate. As a client, this verifies the server certificate. If empty, the receiver uses the system root CA.  
`cert_file` |  | Path to the TLS certificate to use for mTLS-required connections.  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `localhost:30015` | The `hostname:port` used to connect to the SAP HANA instance.  
`insecure` | `true` | Sets whether or not to use a secure TLS connection. If set to `false`, then TLS is enabled.  
`insecure_skip_verify` | `false` | Sets whether or not to skip verifying the certificate. If `insecure` is set to `true`, then the `insecure_skip_verify` value is not used.  
`key_file` |  | Path to the TLS key to use for mTLS-required connections.  
`password` |  | The password used to connect to the instance.  
`type` |  | This value must be `saphana`.  
`username` |  | The username used to connect to the instance.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the HANA instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/saphana.alert.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `rating`  
`workload.googleapis.com/saphana.backup.latest`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/saphana.column.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`subtype`  
`type`  
`workload.googleapis.com/saphana.component.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `component`  
`host`  
`workload.googleapis.com/saphana.connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`status`  
`workload.googleapis.com/saphana.cpu.used`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.disk.size.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`state`  
`usage_type`  
`workload.googleapis.com/saphana.host.memory.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.host.swap.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.instance.code_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.instance.memory.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.instance.memory.shared.allocated`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.instance.memory.used.peak`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.license.expiration.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `product`  
`system`  
`workload.googleapis.com/saphana.license.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `product`  
`system`  
`workload.googleapis.com/saphana.license.peak`  
`GAUGE`, `INT64`  
**gce_instance** |  `product`  
`system`  
`workload.googleapis.com/saphana.network.request.average_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.network.request.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`state`  
`workload.googleapis.com/saphana.network.request.finished.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.replication.average_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `mode`  
`port`  
`primary`  
`secondary`  
`workload.googleapis.com/saphana.replication.backlog.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `mode`  
`port`  
`primary`  
`secondary`  
`workload.googleapis.com/saphana.replication.backlog.time`  
`GAUGE`, `INT64`  
**gce_instance** |  `mode`  
`port`  
`primary`  
`secondary`  
`workload.googleapis.com/saphana.row_store.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.schema.memory.used.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`type`  
`workload.googleapis.com/saphana.schema.memory.used.max`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`workload.googleapis.com/saphana.schema.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`type`  
`workload.googleapis.com/saphana.schema.record.compressed.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`workload.googleapis.com/saphana.schema.record.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`schema`  
`type`  
`workload.googleapis.com/saphana.service.code_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`status`  
`workload.googleapis.com/saphana.service.memory.compactors.allocated`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.compactors.freeable`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.effective_limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.heap.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`state`  
`workload.googleapis.com/saphana.service.memory.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.memory.shared.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`state`  
`workload.googleapis.com/saphana.service.memory.used`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`type`  
`workload.googleapis.com/saphana.service.stack_size`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`service`  
`workload.googleapis.com/saphana.service.thread.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`status`  
`workload.googleapis.com/saphana.transaction.blocked`  
`GAUGE`, `INT64`  
**gce_instance** |  `host`  
`workload.googleapis.com/saphana.transaction.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`type`  
`workload.googleapis.com/saphana.volume.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`type`  
`usage_type`  
`workload.googleapis.com/saphana.volume.operation.size`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`type`  
`usage_type`  
`workload.googleapis.com/saphana.volume.operation.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `host`  
`path`  
`type`  
`usage_type`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the HANA receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that HANA logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("saphana")
         




To verify that HANA metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/saphana.connection.count", monitored_resource="gce_instance"}
         




## View dashboard

To view your HANA metrics, you must have a chart or dashboard configured. The HANA integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for HANA and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The HANA integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for HANA and click **View Details**. 
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
