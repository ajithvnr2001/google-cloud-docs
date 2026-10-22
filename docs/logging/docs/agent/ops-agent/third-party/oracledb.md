---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/oracledb/
title: Oracle Database \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:06.931391+00:00
---

# Oracle Database  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/oracledb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Oracle Database Stay organized with collections  Save and categorize content based on your preferences. 

The Oracle DB integration collects Oracle DB metrics and logs. The metrics are collected by querying relevant monitoring views. This integration writes structured trace logs.

For more information about Oracle DB, see the [Oracle Database documentation](https://www.oracle.com/database/).

## Prerequisites

To collect Oracle DB telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index) on a [supported operating system](https://docs.cloud.google.com/logging/docs/agent/ops-agent#supported_operating_systems):

  * For metrics, install version 2.22.0 or higher.
  * For logs, install version 2.22.0 or higher.



This integration supports Oracle DB versions 12.2, 18c, 19c, and 21c running on Compute Engine instances. It doesn't support Oracle [RAC](https://docs.oracle.com/en/database/oracle/oracle-database/19/racad/introduction-to-oracle-rac.html) or [OCI](https://www.oracle.com/cloud/) configurations.

## Configure your Oracle DB instance

To collect metrics, a monitoring user requires `SELECT` access to the relevant views. The following sql script should create a monitoring user and give it the appropriate permissions if executed by a user with sufficient permissions connected to the Oracle DB instance as SYSDBA or SYSOPER.
    
    
    -- Create the monitoring user "otel"
    CREATE USER otel IDENTIFIED BY ;
    
    -- Grant the "otel" user the required permissions
    GRANT CONNECT TO otel;
    GRANT SELECT ON SYS.GV_$DATABASE to otel;
    GRANT SELECT ON SYS.GV_$INSTANCE to otel;
    GRANT SELECT ON SYS.GV_$PROCESS to otel;
    GRANT SELECT ON SYS.GV_$RESOURCE_LIMIT to otel;
    GRANT SELECT ON SYS.GV_$SYSMETRIC to otel;
    GRANT SELECT ON SYS.GV_$SYSSTAT to otel;
    GRANT SELECT ON SYS.GV_$SYSTEM_EVENT to otel;
    GRANT SELECT ON SYS.V_$RMAN_BACKUP_JOB_DETAILS to otel;
    GRANT SELECT ON SYS.V_$SORT_SEGMENT to otel;
    GRANT SELECT ON SYS.V_$TABLESPACE to otel;
    GRANT SELECT ON SYS.V_$TEMPFILE to otel;
    GRANT SELECT ON SYS.DBA_DATA_FILES to otel;
    GRANT SELECT ON SYS.DBA_FREE_SPACE to otel;
    GRANT SELECT ON SYS.DBA_TABLESPACE_USAGE_METRICS to otel;
    GRANT SELECT ON SYS.DBA_TABLESPACES to otel;
    GRANT SELECT ON SYS.GLOBAL_NAME to otel;
    

## Configure the Ops Agent for Oracle DB

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from Oracle DB instances, and [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Oracle DB:
    
    
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
        oracledb_audit:
          type: oracledb_audit
          oracle_home: /opt/oracle
        oracledb_alert:
          type: oracledb_alert
          oracle_home: /opt/oracle
      service:
        pipelines:
          oracledb:
            receivers:
              - oracledb_audit
              - oracledb_alert
    metrics:
      receivers:
        oracledb:
          type: oracledb
          username: otel
          password: ora19c
          sid: ORCLCDB
          service_name: ORCLCDB
      service:
        log_level: debug
        pipelines:
          oracledb:
            receivers:
              - oracledb
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

To ingest logs from Oracle DB, you must create a receiver for the logs that Oracle DB produces and then create a pipeline for the new receiver.

To configure a receiver for your `oracledb_audit` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` |  | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths. Cannot be provided with the `oracle_home` field.  
`oracle_home` |  | Location of the `ORACLE_HOME` for the environment, when provided it sets the include_paths to `$ORACLE_HOME/admin/*/adump/*.aud`. Cannot be provided with the `include_paths` field.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `oracledb_audit`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
To configure a receiver for your `oracledb_alert` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` |  | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths. Cannot be provided with the `oracle_home` field.  
`oracle_home` |  | Location of the `ORACLE_HOME` for the environment, when provided it sets the `include_paths` to `$ORACLE_HOME/diag/rdbms/*/*/trace/alert_*.log`. Cannot be provided with the `include_paths` field.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | The value must be `oracledb_alert`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `oracledb_alert` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.message` | string | Log message  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `oracledb_audit` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.action` | string | Action being logged in the audit log  
`jsonPayload.action_number` | number | Number identifying the type of action being logged  
`jsonPayload.client_terminal` | string | Identifier of the client terminal where the action originated  
`jsonPayload.client_user` | string | Client user for the audited action  
`jsonPayload.database_user` | string | Database user for the audited action  
`jsonPayload.dbid` | number | Database identifier  
`jsonPayload.length` | number | Length of the string representing the action being logged  
`jsonPayload.privilege` | string | Database privilege the action was executed under  
`jsonPayload.sessionid` | number | Session identifier  
`jsonPayload.status` | string | Status of the action  
`jsonPayload.user_host` | string | Host where the audited action originated  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Oracle DB, you must create a receiver for the metrics that Oracle DB produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `oracledb` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `localhost:1521` | The endpoint used to connect to the oracle DB instance. This field supports either `host:port` or a Unix socket path.  
`insecure` | `true` | Sets whether or not to use a secure TLS connection. If set to `false`, then TLS is enabled.  
`insecure_skip_verify` | `false` | Sets whether or not to skip verifying the certificate. If `insecure` is set to `true`, then the `insecure_skip_verify` value is not used.  
`password` |  | The password used to connect to the instance.  
`service_name` |  | The Service Name of the Oracle database being monitored. Use this field _or_ the `sid` field as appropriate.  
`sid` |  | The SID of the Oracle database being monitored. Use this field _or_ the `service_name` field as appropriate.  
`type` |  | This value must be `oracledb`.  
`username` |  | The username used to connect to the instance.  
`wallet` |  | Path to the directory containing the oracle wallet optionally used for authentication and securing connections.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Oracle DB instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/oracle.backup.latest`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`workload.googleapis.com/oracle.buffer.cache.ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.cursor.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.cursor.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.disk.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`direction`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.disk.operation.size`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`direction`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.logon.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.logon.current`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.network.data`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`direction`  
`global_name`  
`instance_id`  
`target`  
`workload.googleapis.com/oracle.process.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.process.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.process.pga_memory.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`program`  
`state`  
`workload.googleapis.com/oracle.row.cache.ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.service.response_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.session.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.session.limit`  
`GAUGE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.sort.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`workload.googleapis.com/oracle.sort.row.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.tablespace.count`  
`GAUGE`, `INT64`  
**gce_instance** |  `contents`  
`database_id`  
`db_system`  
`global_name`  
`status`  
`workload.googleapis.com/oracle.tablespace.size`  
`GAUGE`, `INT64`  
**gce_instance** |  `contents`  
`database_id`  
`db_system`  
`global_name`  
`state`  
`tablespace_name`  
`workload.googleapis.com/oracle.user.calls`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.user.commits`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.user.rollbacks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`workload.googleapis.com/oracle.wait.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`wait_class`  
`workload.googleapis.com/oracle.wait.time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`wait_class`  
`workload.googleapis.com/oracle.wait.timeouts`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database_id`  
`db_system`  
`global_name`  
`instance_id`  
`type`  
`wait_class`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the Oracle DB receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Oracle DB logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("oracledb_alert") OR log_id("oracledb_audit"))
         




To verify that Oracle DB metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/oracle.logon.count", monitored_resource="gce_instance"}
         




## View dashboard

To view your Oracle DB metrics, you must have a chart or dashboard configured. The Oracle DB integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for Oracle DB and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Oracle DB integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Oracle DB and click **View Details**. 
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
