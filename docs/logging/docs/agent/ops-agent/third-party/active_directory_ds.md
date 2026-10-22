---
url: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/active_directory_ds/
title: Active Directory Domain Services (AD DS) \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:17:40.997283+00:00
---

# Active Directory Domain Services (AD DS)  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/ops-agent/third-party/active_directory_ds/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Active Directory Domain Services (AD DS) Stay organized with collections  Save and categorize content based on your preferences. 

Active Directory Domain Services (AD DS) stores information about objects on the network so that administrators and users can easily access this information.

For more information about AD DS, see the [Active Directory Domain Services (AD DS) documentation](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).

## Prerequisites

To collect AD DS telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/install-index):

  * For metrics, install version 2.15.0 or higher.
  * For logs, install version 2.15.0 or higher.



This integration supports AD DS versions windows-server-2016 and windows-server-2019.

## Configure your AD DS instance

By default, Active Directory Windows event logs and performance counters are enabled.

## Configure the Ops Agent for AD DS

Following the guide to [Configure the Ops Agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/configuration#file-location), add the required elements to collect telemetry from AD DS instances, and [restart the agent](https://docs.cloud.google.com/logging/docs/agent/ops-agent/installation#restart).

### Example configuration

The following commands create the configuration to collect and ingest telemetry for AD DS:
    
    
    $ErrorActionPreference = 'Stop'
    
    # Create an empty config.yaml file if it doesn't exist.
    $configFilePath  = 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml'
    
    if (-not (Test-Path -Path $configFilePath -PathType Leaf)) {
        New-Item -ItemType File -Path $configFilePath -Force | Out-Null
    }
    
    # Create a back up of the existing file so existing configurations are not lost.
    Copy-Item -Path 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml' -Destination 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml.bak'
    
    # Configure the Ops Agent.
    Add-Content 'C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml' "
    logging:
      receivers:
        active_directory_ds:
          type: active_directory_ds
      service:
        pipelines:
          active_directory_ds:
            receivers:
            - active_directory_ds
    
    metrics:
      receivers:
        active_directory_ds:
          type: active_directory_ds
      service:
        pipelines:
          active_directory_ds:
            receivers:
            - active_directory_ds
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
         




### Configure logs collection

To ingest logs from AD DS, you must create a receiver for the logs that AD DS produces and then create a pipeline for the new receiver.

To configure a receiver for your `active_directory_ds` logs, specify the following fields:

Field | Default | Description  
---|---|---  
`type` |  | The value must be `active_directory_ds`.  
  
#### What is logged

The `logName` is derived from the receiver IDs specified in the configuration. Detailed fields inside the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) are as follows.

The `active_directory_ds` logs contain the following fields in the `LogEntry`:

Field | Type | Description  
---|---|---  
`jsonPayload.Channel` | string | The event log channel where the log was logged.  
`jsonPayload.ComputerName` | string | The name of the computer from which this log originates.  
`jsonPayload.Data` | string | Extra event-specific data included with the log.  
`jsonPayload.EventCategory` | number | The category of the event.  
`jsonPayload.EventID` | number | An ID identifying the type of the event.  
`jsonPayload.EventType` | string | The type of event.  
`jsonPayload.Message` | string | The log message.  
`jsonPayload.Qualifiers` | number | A qualifier number that is used for event identification.  
`jsonPayload.RecordNumber` | number | The sequence number of the event log.  
`jsonPayload.Sid` | string | The security identifier identifying a security principal or security group of the process that logged this message.  
`jsonPayload.SourceName` | string | The source component that logged this message.  
`jsonPayload.StringInserts` | []string | Dynamic string data that was used to construct the log message.  
`jsonPayload.TimeGenerated` | string | A timestamp representing when the record was generated.  
`jsonPayload.TimeWritten` | string | A timestamp representing when the record was written to the event log.  
`severity` | string ([`LogSeverity`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#LogSeverity)) | Log entry level (translated).  
  
### Configure metrics collection

To ingest metrics from AD DS, you must create a receiver for the metrics that AD DS produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them.

To configure a receiver for your `active_directory_ds` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`type` |  | The value must be `active_directory_ds`.  
  
#### What is monitored

The following table provides the list of metrics that the Ops Agent collects from the AD DS instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/active_directory.ds.bind.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/active_directory.ds.ldap.bind.last_successful.time`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.ldap.bind.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.ldap.client.session.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.ldap.search.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.name_cache.hit_rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.notification.queued`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.operation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/active_directory.ds.replication.network.io`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `direction`  
`type`  
`workload.googleapis.com/active_directory.ds.replication.object.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `direction`  
`workload.googleapis.com/active_directory.ds.replication.operation.pending`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.replication.property.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `direction`  
`workload.googleapis.com/active_directory.ds.replication.sync.object.pending`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.replication.sync.request.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `result`  
`workload.googleapis.com/active_directory.ds.replication.value.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `direction`  
`type`  
`workload.googleapis.com/active_directory.ds.security_descriptor_propagations_event.queued`  
`GAUGE`, `INT64`  
**gce_instance** |   
`workload.googleapis.com/active_directory.ds.suboperation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/active_directory.ds.thread.count`  
`GAUGE`, `INT64`  
**gce_instance** |   
  
## Verify the configuration

This section describes how to verify that you correctly configured the AD DS receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that AD DS logs are being sent to Cloud Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query in the editor, and then click **Run query** :   

         
         resource.type="gce_instance"
         log_id("active_directory_ds")
         




To verify that AD DS metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
  3. Enter the following query in the editor, and then click **Run query** :   

         
         {"workload.googleapis.com/active_directory.ds.bind.rate", monitored_resource="gce_instance"}
         




## View dashboard

To view your AD DS metrics, you must have a chart or dashboard configured. The AD DS integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for AD DS and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The AD DS integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for AD DS and click **View Details**. 
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
