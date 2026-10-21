---
url: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mssql/
title: Microsoft SQL Server \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:27.579644+00:00
---

# Microsoft SQL Server  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mssql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Microsoft SQL Server Stay organized with collections  Save and categorize content based on your preferences. 

The Microsoft SQL Server integration collects transaction, connection, and other metrics from your SQL Server instances.

For more information about SQL Server, see the [SQL Server](https://docs.microsoft.com/en-us/sql/sql-server) documentation.

## Before you begin

The Ops Agent version 2.15.0 introduces support for a new set of SQL Server metrics using the `workload.googleapis.com/` prefix. You must configure the agent to collect these metrics, as described in Example configuration.

The Ops Agent has always supported a limited set of SQL Servier metrics; these metrics use the `agent.googleapis.com/mssql/` prefix. No additional configuration is needed to collect these metrics on Windows VMs.

This document refers to the `agent`-prefixed metrics as the _v1_ metrics and to the `workload`-prefixed metrics as the _v2_ metrics.

  * The v1 metrics include transaction-rate and connection-count information.
  * The v2 metrics include batch, lock, page, and user connection-count information at the instance level, and transaction and transaction-log information at the database level.



For tables of these metrics, see What is monitored.

Starting with the Ops Agent version 2.15.0, you can configure the agent to collect v1 metrics, v2 metrics, or both.

**Note:** If you have alerts or other configurations built on the v1 metrics and you switch to the v2 metrics, then you have to migrate your configurations as well. If you stop collecting v1 metrics, then alerts and other monitoring of those metrics will stop working. The following table shows the mapping of v1 metrics to v2 metrics: v1 metric (`agent.googleapis.com/mssql/`) | v2 metric (`workload.googleapis.com/`)  
---|---  
`connections_user` | `sqlserver.user.connection.count`  
`transaction_rate` | `sqlserver.transaction.rate`  
`write_transaction_rate` | `sqlserver.transaction.write.rate`  
  
## Prerequisites

To collect SQL Server telemetry, you must [install the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/install-index):

  * For metrics v1, install version 1.0.0 or higher.
  * For metrics v2, install version 2.15.0 or higher.



This integration supports SQL Server versions 11.x, 12.x, 13.x, 14.x, 15.x, and 16.x.

## Configure the Ops Agent for SQL Server

When using the Ops Agent on a Microsoft Windows VM, the agent automatically collects SQL Server v1 metrics. No additional configuration is required.

Following the guide to [configure the Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/configuration#file-location), add the required elements to collect telemetry from SQL Server instances, and [restart the agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/installation#restart).

After setting up a new SQL Server instance, you might not immediately see metrics display in Metrics Explorer. The Ops Agent begins collecting SQL Server metrics only after there is database activity to report.

### Example configuration

The following commands create the configuration to collect and ingest telemetry for SQL Server:
    
    
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
        mssql_v2:
          type: mssql
          receiver_version: 2
      service:
        pipelines:
          mssql_v2:
            receivers:
            - mssql_v2
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
         




### Configure v1 metrics collection

The Ops Agent on a Microsoft Windows VM automatically collects SQL Server v1 metrics. No additional configuration is required. For information about collecting _only_ v2 metrics, see Configure v2 metrics collection.

After you set up a new SQL Server instance, SQL Server might not immediately report any metrics. The Ops Agent begins collecting SQL Server metrics after there is database activity to report.

### Configure v2 metrics collection

To ingest v2 metrics from SQL Server, you must create a receiver for the metrics that SQL Server produces and then create a pipeline for the new receiver.

This receiver does not support the use of multiple instances in the configuration, for example, to monitor multiple endpoints. All such instances write to the same time series, and Cloud Monitoring has no way to distinguish among them. The Ops Agent doesn't support SQL Server named instances.

To configure a receiver for your `mssql` metrics, specify the following fields:

Field | Default | Description  
---|---|---  
`collection_interval` | `60s` | A [time.Duration](https://pkg.go.dev/time#ParseDuration) value, such as `30s` or `5m`.  
`receiver_version` |  | Version of the metrics collected; use `2` to collect v2 metrics.  
`type` |  | This value must be `mssql`.  
  
By default, the v1 metrics are collected automatically. You can either augment the v1 metrics by additionally collecting v2 metrics, or you can override the v1 metrics to collect only v2 metrics.

  * To collect _only_ v2 metrics, do the following:

    * Name your receiver `mssql`.
    * Set the `type` field to `mssql`.
    * Set the `receiver_version` field to `2`.
    * Use this receiver in your `default_pipeline` pipeline. This configuration overrides the built-in configuration of the `mssql` receiver.
  * To collect both v1 and v2 metrics, do the following:

    * Name your receiver something other than `mssql`, like `mssql_v2`.
    * Set the `type` field to `mssql`.
    * Set the `receiver_version` to `2`.
    * Use this receiver in your new pipeline. This configuration adds a v2 receiver rather than overriding the built-in receiver. The script in Example configuration uses this approach.



## What is monitored

Starting with version 2.15.0, the Ops Agent can collect two different sets of metrics:

  * The v1 metrics: `agent.googleapis.com/mssql/`.
  * The v2 metrics: `workload.googleapis.com/`.



##### V1 metrics

The following table provides the list of v1 metrics that the Ops Agent collects from the SQL Server instance. 

The "metric type" strings in this table must be prefixed with `agent.googleapis.com/mssql/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`connections/user` GA ** _(project)_**   
SQL Server open connections   
`GAUGE`, `DOUBLE`, `1`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _Currently open connections to SQL server. Sampled every 60 seconds._  
`transaction_rate` GA ** _(project)_**   
SQL Server transaction rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _SQL server total transactions per second. Sampled every 60 seconds._  
`write_transaction_rate` GA ** _(project)_**   
SQL Server write transaction rate   
`GAUGE`, `DOUBLE`, `1/s`   
**[aws_ec2_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_aws_ec2_instance)**   
**[gce_instance](https://docs.cloud.google.com/monitoring/api/resources#tag_gce_instance)** |  _SQL server write transactions per second. Sampled every 60 seconds._  
  
Table generated at 2026-10-14 20:24:33 UTC.

##### V2 metrics

The following table provides the list of v2 metrics that the Ops Agent collects from the SQL Server instance. 

Metric type   
---  
Kind, Type  
Monitored resources | Labels  
`workload.googleapis.com/sqlserver.batch.request.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.batch.sql_compilation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.batch.sql_recompilation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.lock.wait.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.lock.wait_time.avg`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.buffer_cache.hit_ratio`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.checkpoint.flush.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.lazy_write.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.life_expectancy`  
`GAUGE`, `INT64`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.page.operation.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `type`  
`workload.googleapis.com/sqlserver.page.split.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  ` `  
`workload.googleapis.com/sqlserver.transaction.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction.write.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.flush.data.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.flush.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.flush.wait.rate`  
`GAUGE`, `DOUBLE`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.growth.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.percent_used`  
`GAUGE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.transaction_log.shrink.count`  
`CUMULATIVE`, `INT64`  
**gce_instance** |  `database`  
`workload.googleapis.com/sqlserver.user.connection.count`  
`GAUGE`, `INT64`  
**gce_instance** |  ` `  
  
## Verify the configuration

This section describes how to verify that you correctly configured the SQL Server receiver. It might take one or two minutes for the Ops Agent to begin collecting telemetry.

To verify that SQL Server metrics are being sent to Cloud Monitoring, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.
     * For v1 metrics, enter the following query in the editor, and then click **Run query** :   

           
           {"agent.googleapis.com/mssql/connections/user", monitored_resource="gce_instance"}
           

     * For v2 metrics, enter the following query in the editor, and then click **Run** :   

           
           {"workload.googleapis.com/sqlserver.user.connection.count", monitored_resource="gce_instance"}
           




## View dashboard

To view your SQL Server metrics, you must have a chart or dashboard configured. The SQL Server integration includes one or more dashboards for you. Any dashboards are automatically installed after you configure the integration and the Ops Agent has begun collecting metric data.

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
  3. Locate the entry for SQL Server and click **View Details**. 
  4. Select the **Dashboards** tab to see a static preview. If the dashboard is installed, then you can navigate to it by clicking **View dashboard**.



For more information about dashboards in Cloud Monitoring, see [Dashboards and charts](https://docs.cloud.google.com/monitoring/dashboards).

For more information about using the **Integrations** page, see [Manage integrations](https://docs.cloud.google.com/monitoring/agent/integrations).

## Install alerting policies

Alerting policies instruct Cloud Monitoring to notify you when specified conditions occur. The SQL Server integration includes one or more alerting policies for you to use. You can view and install these alerting policies from the **Integrations** page in Monitoring.

To view the descriptions of available alerting policies and install them, do the following: 

  1. In the Google Cloud console, go to the ![](https://docs.cloud.google.com/static/monitoring/images/integrations-icon.png) **Integrations** page: 

[Go to **Integrations**](https://console.cloud.google.com/monitoring/integrations)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Locate the entry for SQL Server and click **View Details**. 
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
