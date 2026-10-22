---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mysql/
title: MySQL \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:54.841303+00:00
---

# MySQL  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  MySQL Stay organized with collections  Save and categorize content based on your preferences. 

The MySQL integration collects performance metrics related to InnoDB, the buffer pool, and various other operations. It also collects general, error, and slow-query logs and parses them into a JSON payload. Error logs are parsed for their error code and subsystem. Slow-query logs are parsed into key-value pairs that describe the performance of a query, including query time and rows examined.

For more information about MySQL, see the [MySQL documentation](http://www.mysql.com/).

## Prerequisites

To collect MySQL telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index):

  * For metrics, install version 2.32.0 or higher.
  * For logs, install version 2.5.0 or higher.



This integration supports MySQL versions 5.7 and 8.0.

## Configure your MySQL instance

The `mysql` receiver connects by default to a local MySQL server using a Unix socket and Unix authentication as the `root` user.

## Configure the Ops Agent for MySQL

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from MySQL instances, and [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for MySQL:
    
    
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
          username: root
          password: Ss123%321
          # To use the googlesecretmanager provider to replace plaintext passwords, refer to the example below.
          # password: ${googlesecretmanager:projects/<project-id>/secrets/<secret-id>/versions/<version-id>}
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

To ingest logs from MySQL, you must create a receiver for the logs that MySQL produces and then create a pipeline for the new receiver.

To configure a receiver for your `mysql_error` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/mysqld.log, /var/log/mysql/mysqld.log, /var/log/mysql/error.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths; for example, `/var/log/mysql/*.log`.  
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
`jsonPayload.bytesReceived` † | number | The number of bytes received from all clients  
`jsonPayload.bytesSent` † | number | The number of bytes sent to all clients  
`jsonPayload.createdTmpDiskTables` † | number | The number of internal on-disk temporary tables created by the server  
`jsonPayload.createdTmpTables` † | number | The number of internal temporary tables created by the server  
`jsonPayload.database` | string | Database where the query was executed  
`jsonPayload.endTime` † | string | The statement execution end time  
`jsonPayload.errorNumber` † | number | The statement error number, or 0 if no error occurred  
`jsonPayload.host` | string | Host of the database instance  
`jsonPayload.ipAddress` | string | Address of the database instance  
`jsonPayload.killed` † | number | If the statement was terminated, the error number indicating why, or 0 if the statement terminated normally  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.lockTime` | number | The time to acquire locks in seconds  
`jsonPayload.message` | string | Full text of the query  
`jsonPayload.queryTime` | number | The statement execution time in seconds  
`jsonPayload.readFirst` † | number | The number of times the first entry in an index was read  
`jsonPayload.readKey` † | number | The number of requests to read a row based on a key  
`jsonPayload.readLast` † | number | The number of requests to read the last key in an index  
`jsonPayload.readNext` † | number | The number of requests to read the next row in key order  
`jsonPayload.readPrev` † | number | The number of requests to read the previous row in key order  
`jsonPayload.readRnd` † | number | The number of requests to read a row based on a fixed position  
`jsonPayload.readRndNext` † | number | The number of requests to read the next row in the data file  
`jsonPayload.rowsExamined` | number | The number of rows examined by the server layer  
`jsonPayload.rowsSent` | number | The number of rows sent to the client  
`jsonPayload.sortMergePasses` † | number | The number of merge passes that the sort algorithm has had to do  
`jsonPayload.sortRangeCount` † | number | The number of sorts that were done using ranges  
`jsonPayload.sortRows` † | number | The number of sorted rows  
`jsonPayload.sortScanCount` † | number | The number of sorts that were done by scanning the table  
`jsonPayload.startTime` † | string | The statement execution start time  
`jsonPayload.tid` | number | Thread ID where the query was logged  
`jsonPayload.user` | string | User that executed the query  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
† These fields are only provided if the `log_slow_extra` system variable is set to `'ON'`. This variable is available as of MySQL 8.0.14.

For information about these fields, refer to the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/slow-query-log.html).

### Configure metrics collection

To ingest metrics from MySQL, you must create a receiver for the metrics that MySQL produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `mysql` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `/var/run/mysqld/mysqld.sock` | The `hostname:port` or Unix socket path starting with `/` used to connect to the MySQL server.  
`password` |  | The password used to connect to the server.  
`type` |  | This value must be `mysql`.  
`username` | `root` | The username used to connect to the server.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the MySQL instance. 

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

This section describes how to verify that you correctly configured the MySQL receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that MySQL logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("mysql_error") OR log_id("mysql_general") OR log_id("mysql_slow"))
         




To verify that MySQL metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/mysql.threads", monitored_resource="gce_instance"}
         




## View dashboard

To view your MySQL metrics, you must have a chart or dashboard configured. The MySQL integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for MySQL and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The MySQL integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for MySQL and click **View Details**. 
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
