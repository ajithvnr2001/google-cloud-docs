---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/iis/
title: Internet Information Services \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:48.030020+00:00
---

# Internet Information Services  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/iis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Internet Information Services Stay organized with collections  Save and categorize content based on your preferences. 

The Internet Information Services (IIS) integration collects telemetry from your IIS web servers. The metrics provide connection information and also data on transferred bytes. The integration also collects information from access logs.

For more information on IIS, see the [Internet Information Services documentation](https://docs.microsoft.com/iis/).

## Before you begin

The Ops Agent version 2.15.0 introduces support for a new set of IIS metrics using the `workload.googleapis.com/` prefix. You must configure the agent to collect these metrics, as described in Example configuration.

The Ops Agent has always supported a limited set of IIS metrics; these metrics use the `agent.googleapis.com/iis/` prefix. No additional configuration is needed to collect these metrics on Windows VMs.

This document refers to the `agent`-prefixed metrics as the _v1_ metrics and to the `workload`-prefixed metrics as the _v2_ metrics. For tables of these metrics, see What is monitored.

Starting with the Ops Agent version 2.15.0, you can configure the agent to collect v1 metrics, v2 metrics, or both.

**Note:** If you have alerts or other configurations built on the v1 metrics and you switch to the v2 metrics, then you have to migrate your configurations as well. If you stop collecting v1 metrics, then alerts and other monitoring of those metrics will stop working. The following table shows the mapping of v1 metrics to v2 metrics: v1 metric (`agent.googleapis.com/iis/`) | v2 metric (`workload.googleapis.com/`)  
---|---  
`current_connections` | `iis.connection.active`  
`network/transferred_bytes_count` | `iis.network.io`  
`new_connection_count` | `iis.connection.attempt.count`  
`request_count` | `iis.request.count`  
  
## Prerequisites

To collect IIS telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index):

  * For metrics v1, install version 1.0.0 or higher.
  * For metrics v2, install version 2.15.0 or higher
  * For logs, install version 2.14.0 or higher.



This integration supports IIS versions 8.5 and 10.0.

## Configure the Ops Agent for IIS

Following the guide to [configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from IIS instances, and [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for IIS:
    
    
    $ErrorActionPreference = 'Stop'
    
    # This config gets merged with the built-in Ops Agent config, which already
    # includes the v1 receiver in the default pipeline.
    # Because the v2 receiver here uses a unique ID, it does not overwrite
    # the default receiver and so both receivers will be active simultaneously
    # during the test.
    
    # Create an empty config.yaml file if it doesn't exist.
    $configFilePath  = 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml'
    
    if (-not (Test-Path -Path $configFilePath -PathType Leaf)) {
        New-Item -ItemType File -Path $configFilePath -Force | Out-Null
    }
    
    # Create a back up of the existing file so existing configurations are not lost.
    Copy-Item -Path 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml' -Destination 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml.bak'
    
    # Configure the Ops Agent.
    Add-Content 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml' "
    metrics:
      receivers:
        iis_v2:
          type: iis
          receiver_version: 2
      service:
        pipelines:
          iispipeline:
            receivers:
              - iis_v2
    logging:
      receivers:
        iis_access:
          type: iis_access
      service:
        pipelines:
          iis:
            receivers:
            - iis_access
    "
    
    if (Get-Service google-cloud-ops-agent* -ErrorAction SilentlyContinue) {
      (Get-Service google-cloud-ops-agent*).WaitForStatus('Running', '00:03:00')
    }

For these changes to take effect, you must restart the Ops Agent:

  1. Connect to your instance using RDP or a similar tool and login to Windows. 
  2. Open a PowerShell terminal with administrator privileges by right-clicking the PowerShell icon and selecting **Run as Administrator**
  3. To restart the agent, run the following PowerShell command: 
         
         Restart-Service google-cloud-ops-agent -Force
         

  4. To confirm that the agent restarted, run the following command and verify that the components "Metrics Agent" and "Logging Agent" started: 
         
         Get-Service google-cloud-ops-agent*
         




This receiver supports only the default W3C logging format.

### Configure logs collection

To ingest access logs from IIS, you must create receivers for the logs and then create a pipeline for the new receivers.

To configure a receiver for your `iis_access` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`exclude_paths` | `[]` | A list of filesystem path patterns to exclude from the set matched by `include_paths`.  
`include_paths` | `['C:\inetpub\logs\LogFiles\W3SVC1\u_ex*']` | A list of filesystem paths to read by tailing each file. A wild card (`*`) can be used in the paths; for example, `C:\inetpub\logs\LogFiles\W3SVC1\u_ex*`.  
`type` |  | The value must be `iis_access`.  
`record_log_file_path` | `false` | If set to `true`, then the path to the specific file from which the log record was obtained appears in the output log entry as the value of the `agent.googleapis.com/log_file_path` label. When using a wildcard, only the path of the file from which the record was obtained is recorded.  
`wildcard_refresh_interval` | `60s` | The interval at which wildcard file paths in `include_paths` are refreshed. Specified as a time interval parsable by [`time.ParseDuration`](https://pkg.go.dev/time#ParseDuration), for example 30s or 2m. This property might be useful under high logging throughputs where log files are rotated faster than the default interval.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

`iis_access` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`httpRequest.referer` | string | Contents of the `Referer` header  
`httpRequest.remoteIp` | string | IP of the client that made the request  
`httpRequest.requestMethod` | string | HTTP method  
`httpRequest.requestUrl` | string | Request URL (typically just the path part of the URL)  
`httpRequest.serverIp` | string | The server's IP and port that was requested  
`httpRequest.status` | number | HTTP status code  
`httpRequest.userAgent` | string | Contents of the `User-Agent` header  
`jsonPayload.sc_substatus` | number | The substatus error code  
`jsonPayload.sc_win32_status` | number | The Windows status code  
`jsonPayload.time_taken` | number | The length of time that the action took, in milliseconds  
`jsonPayload.user` | string | Authenticated username for the request  
`timestamp` | string ([`Timestamp`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)) | Time the request was received  
  
### Configure v1 metrics collection

The Ops Agent on a Microsoft Windows VM automatically collects IIS v1 metrics. No additional configuration is required. For information about collecting _only_ v2 metrics, see Configure v2 metrics collection.

After you set up a new IIS instance, IIS might not immediately report any metrics. Using the Server Manager console that comes installed on Windows Server, you might see that your server has a status of **Online - Performance Counters not started** in the Manageability column.

One way to enable IIS to generate metrics is to right click on your IIS server in the Server Manager console and select **Start Performance Counters**. Your server should begin sending metrics to the Ops Agent.

### Configure v2 metrics collection

To ingest v2 metrics from IIS, you must create a receiver for the metrics that IIS produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `iis` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | 60s | A time.Duration value, such as 30s or 5m.  
`receiver_version` |  | Version of the metrics collected; use `2` to collect v2 metrics.  
`type` |  | This value must be `iis`.  
  
By default, the v1 metrics are collected automatically. You can either augment the v1 metrics by additionally collecting v2 metrics, or you can override the v1 metrics to collect only v2 metrics.

  * To collect _only_ v2 metrics, do the following:

    * Name your receiver `iis`.
    * Set the `type` field to `iis`.
    * Set the `receiver_version` field to `2`.
    * Use this receiver in your `default_pipeline` pipeline. This configuration overrides the built-in configuration of the `iis` receiver.
  * To collect both v1 and v2 metrics, do the following:

    * Name your receiver something other than `iis`, like `iis_v2`.
    * Set the `type` field to `iis`.
    * Set the `receiver_version` to `2`.
    * Use this receiver in your new pipeline. This configuration adds a v2 receiver rather than overriding the built-in receiver. The script in Example configuration uses this approach.



## What is monitored

Starting with version 2.15.0, the Ops Agent can collect two different sets of metrics:

  * The v1 metrics: `agent.googleapis.com/iis/`.
  * The v2 metrics: `workload.googleapis.com/`.



##### V1 metrics

The following table provides the list of v1 metrics that the Ops Agent collects from the IIS instance. 

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/iis/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`current_connections` GA ** _(project)_**   
IIS open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Currently open connections to IIS. Sampled every 60 seconds._  
`network/transferred_bytes_count` GA ** _(project)_**   
IIS transferred bytes   
`CUMULATIVE`, `INT64`, `By`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Network bytes transferred by IIS. Sampled every 60 seconds._   
`direction`: Direction (sent, received)   
`new_connection_count` GA ** _(project)_**   
IIS connections   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Connections opened to IIS. Sampled every 60 seconds._  
`request_count` GA ** _(project)_**   
IIS requests   
`CUMULATIVE`, `INT64`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Requests made to IIS. Sampled every 60 seconds._   
`http_method`: Http method (post, put, get, delete, option, trace, head)   
  
Table generated at 2026-10-14 20:24:33 UTC.

##### V2 metrics

The following table provides the list of v2 metrics that the Ops Agent collects from the IIS instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/iis.connection.active`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.connection.anonymous`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.connection.attempt.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.network.blocked`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.network.file.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/iis.network.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`workload.googleapis.com/iis.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `request`  
`workload.googleapis.com/iis.request.queue.age.max`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.request.queue.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.request.rejected`  
`CUMULATIVE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.thread.active`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/iis.uptime`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
## Verify the configuration

This section describes how to verify that you correctly configured the IIS receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that IIS logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("iis_access")
         




To verify that IIS metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
     * For v1 metrics, enter the following query in the editor, and then click **Run query** :   

           
           {"agent.googleapis.com/iis/request_count", monitored_resource="gce_instance"}
           

     * For v2 metrics, enter the following query in the editor, and then click **Run** :   

           
           {"workload.googleapis.com/iis.request.count", monitored_resource="gce_instance"}
           




## View dashboard

To view your IIS metrics, you must have a chart or dashboard configured. The IIS integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for IIS and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The IIS integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for IIS and click **View Details**. 
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
