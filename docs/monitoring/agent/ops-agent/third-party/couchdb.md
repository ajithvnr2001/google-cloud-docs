---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/couchdb/
title: Apache CouchDB \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:40.488622+00:00
---

# Apache CouchDB  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party/couchdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Apache CouchDB Stay organized with collections  Save and categorize content based on your preferences. 

The Apache CouchDB integration collects traffic-related metrics, such as the number of requests to a node and responses from the node. It also collects database metrics, such as how many are open and the number of operations. The integration collects general CouchDB and access logs and parses them into a JSON payload. The result includes fields for user, host, level, and message.

For more information about CouchDB, see the [Apache CouchDB documentation](https://couchdb.apache.org/).

## Prerequisites

To collect CouchDB telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index):

  * For metrics, install version 2.10.0 or higher.
  * For logs, install version 2.11.0 or higher.



This integration supports CouchDB versions 2.3.x and 3.1 and higher.

## Configure your CouchDB instance

This integration does not require any additional configuration with CouchDB versions prior to 3.4.0, or on Debian-based distributions.

As of version 3.4.0, CouchDB behaves differently on RPM-based distributions (like RHEL or Rocky Linux). To make CouchDB work with this logging receiver's default configuration on such systems, you must configure Apache CouchDB to write to `/var/log/couchdb/couchdb.log` instead of journald.

To write logs to `/var/log/couchdb/couchdb.log`, complete the following steps:

  1. Create the file `/opt/couchdb/etc/local.d/ops-agent-filelog.ini`.

  2. Add the following lines to the file:
         
         [log]
         writer = file
         file = /var/log/couchdb/couchdb.log
         level = info
         

  3. Restart Apache CouchDB:
         
         sudo systemctl restart couchdb
         




## Configure the Ops Agent for CouchDB

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from CouchDB instances, and [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for CouchDB:
    
    
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
        couchdb:
          type: couchdb
          username: admin
          password: otelp
          # To use the googlesecretmanager provider to replace plaintext passwords, refer to the example below.
          # password: ${googlesecretmanager:projects/<project-id>/secrets/<secret-id>/versions/<version-id>}
      service:
        pipelines:
          couchdb:
            receivers:
              - couchdb
    
    logging:
      receivers:
        couchdb:
          type: couchdb
      service:
        pipelines:
          couchdb:
            receivers:
              - couchdb
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

To ingest logs from CouchDB, you must create a receiver for the logs that CouchDB produces and then create a pipeline for the new receiver.

To configure a receiver for your `couchdb` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/var/log/couchdb/couchdb.log]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths; for example, `/var/log/couchdb*/*.log`.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | This value must be `couchdb`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `couchdb` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`httpRequest` | object | See [`HttpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest)  
`jsonPayload.host` | string | Host instance name  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message  
`jsonPayload.node` | string | Node instance name  
`jsonPayload.path` | string | Request path  
`jsonPayload.pid` | string | Process ID  
`jsonPayload.remote_user` | string | Authenticated username for the request  
`jsonPayload.status_message` | string | Status code message  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from CouchDB, you must create a receiver for the metrics that CouchDB produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `couchdb` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`password` |  | The password used to connect to the server.  
`server_status_url` | `http://localhost:5984` | The URL exposed by CouchDB.  
`type` |  | This value must be `couchdb`.  
`username` |  | The username used to connect to the server.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the CouchDB instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/couchdb.average_request_time`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/couchdb.database.open`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/couchdb.database.operations`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `operation`  
`workload.googleapis.com/couchdb.file_descriptor.open`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/couchdb.httpd.bulk_requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/couchdb.httpd.requests`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `http_method`  
`workload.googleapis.com/couchdb.httpd.responses`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `http_status_code`  
`workload.googleapis.com/couchdb.httpd.views`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `view`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the CouchDB receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that CouchDB logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("couchdb")
         




To verify that CouchDB metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/couchdb.database.open", monitored_resource="gce_instance"}
         




## View dashboard

To view your CouchDB metrics, you must have a chart or dashboard configured. The CouchDB integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for CouchDB and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The CouchDB integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for CouchDB and click **View Details**. 
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
