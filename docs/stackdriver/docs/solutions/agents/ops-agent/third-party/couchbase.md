---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchbase/
title: Couchbase \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:43.440638+00:00
---

# Couchbase  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/couchbase/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Couchbase Stay organized with collections  Save and categorize content based on your preferences. 

The Couchbase integration collects bucket metrics such as operations, memory usage, and ejections. The integration collects metrics from the Prometheus server exposed on a node. The integration also collects Couchbase general, HTTP access, and cross-datacenter ("goxdcr") logs.

For more information about Couchbase, see the [Couchbase documentation](https://www.couchbase.com/).

## Prerequisites

To collect Couchbase telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics, install version 2.18.2 or higher.
  * For logs, install version 2.18.2 or higher.



This integration supports Couchbase versions 6.5, 6.6, and 7.0.

## Configure the Ops Agent for Couchbase

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from Couchbase instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Couchbase:
    
    
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
        couchbase:
          type: couchbase
          username: admin 
          password: password 
          # To use the googlesecretmanager provider to replace plaintext passwords, refer to the example below.
          # password: ${googlesecretmanager:projects/<project-id>/secrets/<secret-id>/versions/<version-id>}
          collection_interval: 30s
      service:
        pipelines:
          couchbase:
            receivers:
              - couchbase
    
    logging:
      receivers:
        couchbase_general:
          type: couchbase_general
        couchbase_http_access:
          type: couchbase_http_access
        couchbase_goxdcr:
          type: couchbase_goxdcr
      service:
        pipelines:
          couchbase:
            receivers:
              - couchbase_general
              - couchbase_http_access
              - couchbase_goxdcr
    
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
         




#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `couchbase_general` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.level` | string | Log entry severity for the couchbase log  
`jsonPayload.message` | string | Log message  
`jsonPayload.module_name` | string | The name of the module issuing the entry  
`jsonPayload.node_name` | string | The name of the node issuing the log message  
`jsonPayload.source` | string | Source where the log originated  
`jsonPayload.type` | string | The type of log  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `couchbase_http_access` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`httpRequest` | object | See [`HttpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest)  
`jsonPayload.host` | string | The IP address of the client invoking the HTTP request  
`jsonPayload.level` | string | Log entry severity for the couchbase log  
`jsonPayload.message` | string | Log message  
`jsonPayload.user` | string | The name of the user making the HTTP request if basic auth is used.  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `couchbase_goxdcr` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.level` | string | Log entry severity for the couchbase log  
`jsonPayload.log_type` | string | The name of the component that is issuing the cross-datacenter log  
`jsonPayload.message` | string | Log message  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Couchbase, you must create a receiver for the metrics that Couchbase produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `couchbase` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time.Duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `localhost:8091` | The URL of the node to monitor.  
`password` |  | The password used to connect to the Couchbase server.  
`type` |  | This value must be `couchbase`.  
`username` |  | The username used to connect to the Couchbase server.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Couchbase instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/couchbase.bucket.error.oom.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `bucket_name`  
`error_type`  
`workload.googleapis.com/couchbase.bucket.item.count`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`state`  
`workload.googleapis.com/couchbase.bucket.item.ejection.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.memory.high_water_mark.limit`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.memory.low_water_mark.limit`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.memory.usage`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`workload.googleapis.com/couchbase.bucket.operation.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `bucket_name`  
`op`  
`workload.googleapis.com/couchbase.bucket.vbucket.count`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `bucket_name`  
`state`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the Couchbase receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Couchbase logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("couchbase_general") OR log_id("couchbase_http_access") OR log_id("couchbase_goxdcr"))
         




To verify that Couchbase metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/couchbase.bucket.memory.usage", monitored_resource="gce_instance"}
         




## View dashboard

To view your Couchbase metrics, you must have a chart or dashboard configured. The Couchbase integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for Couchbase and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Couchbase integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Couchbase and click **View Details**. 
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
