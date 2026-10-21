---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mariadb/
title: MariaDB \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:18.746939+00:00
---

# MariaDB  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mariadb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  MariaDB Stay organized with collections  Save and categorize content based on your preferences. 

The MariaDB integration collects performance metrics related to InnoDB, the buffer pool, and various other operations. It also collects general, error, and slow-query logs and parses them into a JSON payload. Error logs are parsed for their error code and subsystem. Slow-query logs are parsed into key-value pairs that describe the performance of a query, including query time and rows examined.

For more information about MariaDB, see the [MariaDB documentation](http://www.mariadb.com/).

## Prerequisites

To collect MariaDB telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics, install version 2.37.0 or higher.
  * For logs, install version 2.37.0 or higher.



This integration supports MariaDB versions 10.1.X through 10.7.X.

## Configure your MariaDB instance

MariaDB is a community-developed, commercially supported fork of the MySQL relational database management system (RDBMS). To collect logs and metrics for MariaDB, use the `mysql` receivers.

The `mysql` metrics receiver connects by default to a local MariaDB server using a Unix socket and Unix authentication as the `root` user.

The `mysql_error` logging receiver collects logs from the default file paths shown in the following table. On some platforms, MariaDB logs to `journald` by default instead of to file. To configure MariaDB to log to a file instead, set the `log_error` option in the MariaDB configuration. For more information about `log_error` configuration, see [Writing the Error Log to a File](https://mariadb.com/kb/en/error-log/#writing-the-error-log-to-a-file).

## Configure the Ops Agent for MariaDB

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from MariaDB instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for MariaDB:
    
    
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
        mysql:
          type: mysql
      service:
        pipelines:
          mysql:
            receivers:
            - mysql
    logging:
      receivers:
        mysql_error:
          type: mysql_error
        mysql_general:
          type: mysql_general
        mysql_slow:
          type: mysql_slow
      service:
        pipelines:
          mysql:
            receivers:
              - mysql_error
              - mysql_general
              - mysql_slow
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

To ingest logs from MariaDB, you must create a receiver for the logs that MariaDB produces and then create a pipeline for the new receiver.

To configure a receiver for your `mysql_error` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/mysqld.log, /var/log/mysql/mysqld.log, /var/log/mysql/error.log, /run/mysqld/mysqld.err, /var/lib/mysql/${HOSTNAME}.err]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths; for example, `/var/log/mysql/*.log`.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `mysql_error`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
To configure a receiver for your `mysql_general` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/lib/mysql/${HOSTNAME}.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `mysql_general`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
To configure a receiver for your `mysql_slow` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/lib/mysql/${HOSTNAME}-slow.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `mysql_slow`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `mysql_error` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.errorCode` | string | MySQL error code associated with the log  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message  
`jsonPayload.subsystem` | string | MySQL subsystem where the log originated  
`jsonPayload.tid` | number | Thread ID where the log originated  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `mysql_general` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.command` | string | Type of database action being logged  
`jsonPayload.message` | string | Log of the database action  
`jsonPayload.tid` | number | Thread ID where the log originated  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `mysql_slow` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.bytesSent` | number | The number of bytes sent to all clients  
`jsonPayload.createdTmpDiskTables` † | number | The number of internal on-disk temporary tables created by the server  
`jsonPayload.createdTmpTables` † | number | The number of internal temporary tables created by the server  
`jsonPayload.createdTmpTableSizes` † | number | The number of bytes used by internal temporary tables created by the server  
`jsonPayload.database` | string | Database where the query was executed  
`jsonPayload.filesort` † | boolean | The statement used filesort  
`jsonPayload.filesortOnDisk` † | boolean | The statement used filesort that needed temporary tables on disk  
`jsonPayload.fullJoin` † | boolean | The statement didn't use an index to join tables  
`jsonPayload.fullScan` † | boolean | The statement used a full table scan  
`jsonPayload.host` | string | Host name the client connected from  
`jsonPayload.ipAddress` | string | IP address the client connected from  
`jsonPayload.lockTime` | number | The time to acquire locks in seconds  
`jsonPayload.message` | string | Full text of the query  
`jsonPayload.priorityQueue` † | boolean | The statement used a priority queue filesort  
`jsonPayload.queryCacheHit` | boolean | The statement was served from the query cache  
`jsonPayload.queryTime` | number | The statement execution time in seconds  
`jsonPayload.rowsAffected` | integer | The number of rows affected by the statement  
`jsonPayload.rowsExamined` | number | The number of rows examined by the server layer  
`jsonPayload.rowsSent` | number | The number of rows sent to the client  
`jsonPayload.sortMergePasses` † | number | The number of merge passes that the sort algorithm has had to do  
`jsonPayload.storedRoutine` | string | The name of the stored routine currently being executed  
`jsonPayload.tid` | number | Thread ID where the query was logged  
`jsonPayload.user` | string | Authenticated user that executed the query  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
† These fields are only provided if the `log_slow_verbosity` system variable contains `'query_plan'`.

### Configure metrics collection

To ingest metrics from MariaDB, you must create a receiver for the metrics that MariaDB produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `mysql` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `/var/run/mysqld/mysqld.sock` | The `hostname:port` or Unix socket path starting with `/` used to connect to the MariaDB server.  
`password` |  | The password used to connect to the server.  
`type` |  | This value must be `mysql`.  
`username` | `root` | The username used to connect to the server.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the MariaDB instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/mysql.buffer_pool_data_pages`  
`GAUGE`, `INT64`  
**gce_instance** |  `status`  
`workload.googleapis.com/mysql.buffer_pool_limit`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.buffer_pool_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.buffer_pool_page_flushes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.buffer_pool_pages`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.buffer_pool_size`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.commands`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `command`  
`workload.googleapis.com/mysql.double_writes`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.handlers`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.locks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.log_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.page_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.replica.sql_delay`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.replica.time_behind_source`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/mysql.row_locks`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.row_operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/mysql.sorts`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `kind`  
`workload.googleapis.com/mysql.threads`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `kind`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the MariaDB receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that MariaDB logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("mysql_error") OR log_id("mysql_general") OR log_id("mysql_slow"))
         




To verify that MariaDB metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/mysql.threads", monitored_resource="gce_instance"}
         




## View dashboard

To view your MariaDB metrics, you must have a chart or dashboard configured. MariaDB uses the same dashboards as MySQL. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

You can also view static previews of dashboards without installing the integration.

To view an installed dashboard, do the following: 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Dashboard List** tab, and then choose the **Integrations** category.
  3. Click the name of the dashboard you want to view. MariaDB uses the same dashboards as MySQL.



If you have configured an integration but the dashboard has not been installed, then check that the Ops Agent is running. When there is no metric data for a chart in the dashboard, installation of the dashboard fails. After the Ops Agent begins collecting metrics, the dashboard is installed for you.

To view a static preview of the dashboard, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click the **Compute Engine** deployment-platform filter.
  3. Locate the entry for MySQL and click **View Details**. MariaDB uses the same dashboards as MySQL. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. MariaDB uses the same alerting policies as MySQL. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for MySQL and click **View Details**. MariaDB uses the same alerting policies as MySQL. 
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
