---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/tomcat/
title: Apache Tomcat \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:42.676514+00:00
---

# Apache Tomcat  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/tomcat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Apache Tomcat Stay organized with collections  Save and categorize content based on your preferences. 

The Apache Tomcat integration collects traffic-related metrics, such as the number of active sessions or network throughput. The integration also collects access and Catalina logs. Access logs are parsed into a JSON payload focused on request details, whereas Catalina logs are parsed for general details. The `tomcat` receiver collects telemetry from the Tomcat server's Java Virtual Machine (JVM) via [JMX](https://www.oracle.com/java/technologies/javase/javamanagement.html).

For more information about Tomcat, see the [Apache Tomcat documentation](https://tomcat.apache.org/).

## Prerequisites

To collect Tomcat telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index):

  * For metrics, install version 2.9.0 or higher.
  * For logs, install version 2.9.0 or higher.



This integration supports Tomcat versions 10.x and 9.0.x.

## Configure your Tomcat instance

To expose a JMX endpoint, you must set the `com.sun.management.jmxremote.port` system property when starting the JVM. We also recommend setting the `com.sun.management.jmxremote.rmi.port` system property to the same port. To expose a JMX endpoint remotely, you must also set the `java.rmi.server.hostname` system property.

By default, these properties are set in a Tomcat deployment's `tomcat-env.sh` file.

To set system properties by using command-line arguments, prepend the property name with `-D` when starting the JVM. For example, to set `com.sun.management.jmxremote.port` to port `8050`, specify the following when starting the JVM:
    
    
    -Dcom.sun.management.jmxremote.port=8050
    

## Configure the Ops Agent for Tomcat

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from Tomcat instances, and [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for Tomcat:
    
    
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
        tomcat:
          type: tomcat
          endpoint: service:jmx:rmi:///jndi/rmi://127.0.0.1:8050/jmxrmi
      service:
        pipelines:
          tomcat:
            receivers:
              - tomcat
    
    logging:
      receivers:
        tomcat_access:
          type: tomcat_access
        tomcat_system:
          type: tomcat_system
      service:
        pipelines:
          tomcat:
            receivers:
              - tomcat_access
              - tomcat_system
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

To ingest logs from Tomcat, you must create a receiver for the logs that Tomcat produces and then create a pipeline for the new receiver.

To configure a receiver for your `tomcat_system` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/opt/tomcat/logs/catalina.out]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | The value must be `tomcat_system`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
To configure a receiver for your `tomcat_access` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` |  | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `[/opt/tomcat/logs/localhost_access_log*.txt]` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`type` |  | The value must be `tomcat_access`.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Given as a [time duration](https://pkg.go.dev/time#ParseDuration), for example `30s` or `2m`. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `tomcat_system` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.level` | string | Log entry level  
`jsonPayload.message` | string | Log message, including detailed stacktrace where provided  
`jsonPayload.module` | string | Module of tomcat where the log originated  
`jsonPayload.source` | string | Source of where the log originated  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
The `tomcat_access` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`httpRequest` | object | See [`HttpRequest`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest)  
`jsonPayload.host` | string | Contents of the Host header  
`jsonPayload.user` | string | Authenticated username for the request  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from Tomcat, you must create a receiver for the metrics that Tomcat produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `tomcat` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collect_jvm_metrics` | `true` | Configures the receiver to also collect the supported JVM metrics.  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`endpoint` | `localhost:8050` | The [JMX Service URL](https://docs.oracle.com/javase/8/docs/api/javax/management/remote/JMXServiceURL.html) or host and port used to construct the service URL. This value must be in the form of `service:jmx:<protocol>:<sap>` or `host:port`. Values in `host:port` form are used to create a service URL of `service:jmx:rmi:///jndi/rmi://<host>:<port>/jmxrmi`.  
`password` |  | The configured password if JMX is configured to require authentication.  
`type` |  | This value must be `tomcat`.  
`username` |  | The configured username if JMX is configured to require authentication.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the Tomcat instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/tomcat.errors`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.max_time`  
`GAUGE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.processing_time`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.request_count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `proto_handler`  
`workload.googleapis.com/tomcat.sessions`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/tomcat.threads`  
`GAUGE`, `INT64`  
**gce_instance** |  `proto_handler`  
`state`  
`workload.googleapis.com/tomcat.traffic`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`proto_handler`  
  
## Verify the configuration

This section describes how to verify that you correctly configured the Tomcat receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that Tomcat logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         (log_id("tomcat_system") OR log_id("tomcat_access"))
         




To verify that Tomcat metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/tomcat.threads", monitored_resource="gce_instance"}
         




## View dashboard

To view your Tomcat metrics, you must have a chart or dashboard configured. The Tomcat integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for Tomcat and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The Tomcat integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for Tomcat and click **View Details**. 
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
