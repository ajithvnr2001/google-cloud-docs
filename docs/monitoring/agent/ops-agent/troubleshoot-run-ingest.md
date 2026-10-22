---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest/
title: Troubleshoot Ops Agent data ingestion \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:47.927517+00:00
---

# Troubleshoot Ops Agent data ingestion  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Troubleshoot Ops Agent data ingestion Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information to help you diagnose and resolve data-ingestion problems, for logs and metrics, in the running Ops Agent. If the Ops Agent isn't running, then see [Troubleshoot installation and start-up](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup).

## Before you begin

Before trying to fix a problem, check the status of the agent's [health checks](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info#health-checks).

## Google Cloud console shows Ops Agent installation stuck on 'Pending'

Even after successfully installing the Ops Agent, the Google Cloud console might still display a 'Pending' status. Use [gcpdiag](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info#agent-status-gcpdiag-cmd) to confirm Ops Agent installation and to verify that the agent if the agent is transmitting logs and metrics from your VM instance.

### Common reasons for installation failure

Installation of the Ops Agent might fail for the following reasons:

  * The VM doesn't have an attached service account. [Attach a service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes) to the VM and then [reinstall the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation).

  * The VM already has the one of the [legacy agents installed](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#legacy-agent-installed), which prevents installation of the Ops Agent. Uninstall the legacy agents and then [reinstall the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation).




### Common reasons for telemetry-transmission failures

An installed and running Ops Agent can fail to send logs, metrics, or both from a VM for the following reasons:

  * The service account attached to the VM is missing the [`roles/logging.logWriter`](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter) or [`roles/monitoring.metricWriter`](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) role.
  * The logging or monitoring access scope is not enabled. For information about checking and updating access scopes, see [Verify your access scopes](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#before_you_begin).
  * The [Logging API](https://docs.cloud.google.com/logging/docs/api/enable-api) or the [Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api) is not enabled.



Use [agent health checks](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info#start-checks) to identify the root cause and the corresponding solution.

## Agent is running, but data is not ingested

Use Metrics Explorer to query the agent `uptime` metric, and verify that the agent component, `google-cloud-ops-agent-metrics` or `google-cloud-ops-agent-logging`, is writing to the metric.

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toggle labeled **Builder Code** , select **Code** , and then set the language to **PromQL**.
  3. Enter the following query, then click **Run** :
         
         rate({"__name__"="agent.googleapis.com/agent/uptime", monitored_resource="gce_instance"}[1m])
         




### Is the agent sending logs to Cloud Logging?

If the agent is running but not sending logs, then check the status of the agent's runtime [health checks](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info#health-checks).

#### Upgraded logging pipelines

Beginning in Ops Agent 2.66.0, the default logging pipeline is handled by the Metrics Agent service instead of the Logging Agent service. Beginning in Ops Agent 2.72.0, all supported logging pipelines are handled by the Metrics Agent service. If your logging pipelines don't work as expected, then you can try reverting to the old Logging Agent service by updating your configuration:
    
    
    logging:
      service:
        experimental_otel_logging: false
    

This setting will eventually be removed, so if you need to revert, please [contact Cloud Customer Care](https://docs.cloud.google.com/stackdriver/docs/getting-support) to report the issue.

**Note:** Each service maintains its own record of the logs it has processed, so switching from either one to the other will cause duplicate logs to be processed.

#### Pipeline errors

If you see the runtime error `LogPipelineErr` ("Ops Agent logging pipeline failed"), then the Logging subagent has encountered a problem with writing logs. Check the following conditions:

  * Verify that the Logging subagent's storage files are accessible. These files are found in the following locations: 
    * Linux: `/var/lib/google-cloud-ops-agent/fluent-bit/buffers/`
    * Windows: `C:\Program Files\Google\Cloud Operations\Ops Agent\run\buffers\`
  * Verify that the VM's disk is not full.
  * Verify that the [logging configuration](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#logging-config) is correct.



These steps require you to SSH into the VM.

If you change the logging configuration, or if the buffer files are accessible and the VM's disk is not full, then restart the Ops Agent:

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
         




#### Log-parsing errors

If you see the runtime error `LogParseErr` ("Ops Agent failed to parse logs"), then the most likely problem is in the configuration of a logging processor. To resolve this problem, do the following:

  * Verify that the configuration of any [`parse_json` processors](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#logging-processor-parse-json) is correct.
  * Verify that the configuration of any [`parse_regex` processors](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#logging-processor-parse-regex) is correct.
  * If you have no `parse_json` or `parse_regex` processors, then check the configuration of any other [logging processors](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#logging-processors).



These steps require you to SSH into the VM.

If you change the logging configuration, then restart the Ops Agent:

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
         




#### Check the local metrics

**Note:** The local metrics service is not available on Windows.

These steps require you to SSH into the VM.

  * Is the logging module running? Use the following commands to check:



**Linux**
    
    
    sudo systemctl status google-cloud-ops-agent"*"
    

**Windows**

Open Windows PowerShell as administrator and run:
    
    
    Get-Service google-cloud-ops-agent
    

You can also check service status in the Services app and inspect running processes in the Task Manager app.

#### Check the logging module log

This step requires you to SSH into the VM.

You can find the logging module logs at `/var/log/google-cloud-ops-agent/subagents/*.log` for Linux and `C:\ProgramData\Google\Cloud Operations\Ops Agent\log\logging-module.log` for Windows. If there are no logs, then the agent service is not running properly. Go to the [Agent is installed but not running](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#agent-not-running) section first to fix that condition.

  * You might see 403 permission errors when writing to the Logging API. For example:
        
        [2020/10/13 18:55:09] [ warn] [output:stackdriver:stackdriver.0] error
        {
        "error": {
          "code": 403,
          "message": "Cloud Logging API has not been used in project 147627806769 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/logging.googleapis.com/overview?project=147627806769 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
          "status": "PERMISSION_DENIED",
          "details": [
            {
              "@type": "type.googleapis.com/google.rpc.Help",
              "links": [
                {
                  "description": "Google developers console API activation",
                  "url": "https://console.developers.google.com/apis/api/logging.googleapis.com/overview?project=147627806769"
                }
              ]
            }
          ]
        }
        }
        

To fix this error, [enable the Logging API](https://console.cloud.google.com/apis/library/logging.googleapis.com) and set the [**Logs Writer**](https://docs.cloud.google.com/logging/docs/access-control#permissions_and_roles) role.

  * You might see a quota issue for the Logging API. For example:
        
        error="8:Insufficient tokens for quota 'logging.googleapis.com/write_requests' and limit 'WriteRequestsPerMinutePerProject' of service 'logging.googleapis.com' for consumer 'project_number:648320274015'." error_code="8"
        

To fix this error, raise the quota or reduce the log throughput.

  * You might see the following errors in the module log:
        
        {"error":"invalid_request","error_description":"Service account not enabled on this instance"}
        

or
        
        can't fetch token from the metadata server
        

These errors might indicate that you deployed the agent with no service account or specified credentials. For information about resolving this issue, see [Authorize the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization).




### Is the agent sending metrics to Cloud Monitoring?

#### Check the metrics module log

This step requires you to SSH into the VM.

You can find the metrics module logs in syslog. If there are no logs, this indicates that the agent service is not running properly. Go to the [Agent is installed but not running](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#agent-not-running) section first to fix that condition.

  * You might see `PermissionDenied` errors when writing to the Monitoring API. This error occurs if the permission for the Ops Agent are not properly configured. For example:
        
        Nov  2 14:51:27 test-ops-agent-error otelopscol[412]: 2021-11-02T14:51:27.343Z#011info#011exporterhelper/queued_retry.go:231#011Exporting failed. Will retry the request after interval.#011{"kind": "exporter", "name": "googlecloud", "error": "[rpc error: code = PermissionDenied desc = Permission monitoring.timeSeries.create denied (or the resource may not exist).; rpc error: code = PermissionDenied desc = Permission monitoring.timeSeries.create denied (or the resource may not exist).]", "interval": "6.934781228s"}
        

To fix this error, [enable the Monitoring API](https://console.cloud.google.com/apis/library/monitoring.googleapis.com) and set the [**Monitoring Metric Writer**](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) role.

  * You might see `ResourceExhausted` errors when writing to the Monitoring API. This error occurs if the project is hitting the limit for any Monitoring API quotas. For example:
        
        Nov  2 18:48:32 test-ops-agent-error otelopscol[441]: 2021-11-02T18:48:32.175Z#011info#011exporterhelper/queued_retry.go:231#011Exporting failed. Will retry the request after interval.#011{"kind": "exporter", "name": "googlecloud", "error": "rpc error: code = ResourceExhausted desc = Quota exceeded for quota metric 'Total requests' and limit 'Total requests per minute per user' of service 'monitoring.googleapis.com' for consumer 'project_number:8563942476'.\nerror details: name = ErrorInfo reason = RATE_LIMIT_EXCEEDED domain = googleapis.com metadata = map[consumer:projects/8563942476 quota_limit:DefaultRequestsPerMinutePerUser quota_metric:monitoring.googleapis.com/default_requests service:monitoring.googleapis.com]", "interval": "2.641515416s"}
        

To fix this error, raise the quota or reduce the metrics throughput.

  * You might see the following errors in the module log:
        
        {"error":"invalid_request","error_description":"Service account not enabled on this instance"}
        

or
        
        can't fetch token from the metadata server
        

These errors might indicate that you deployed the agent with no service account or specified credentials. For information about resolving this issue, see [Authorize the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization).




### Network-connectivity issues

If the agent is running but sending neither logs nor metrics, you might have a networking problem. The kinds of networking-connectivity problems you might encounter vary with the topology of your application. For an overview of Compute Engine networking, see [Networking overview for VMs](https://docs.cloud.google.com/compute/docs/networking/network-overview).

Common causes of connectivity issues include the following:

  * Firewall rules that interfere with incoming traffic. For information about firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls).
  * Problems in the HTTP proxy configuration.
  * DNS configuration.



The Ops Agent runs health checks that detect network connectivity errors. Refer to the [health checks documentation](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info#health-checks) for suggested actions to take for connectivity errors.

#### Understanding "failed to flush chunk" error messages

Starting with Ops Agent version 2.28.0, the Ops Agent limits the amount of disk space it can use to store buffer chunks. The Ops Agent creates buffer chunks when logging data can't be sent to the Cloud Logging API. Without a limit, these chunks might consume all available space, interrupting other services on the VM. When a network outage causes buffer chunks to be written to disk, the Ops Agent uses a platform-specific amount of disk space to store the chunks. A message like the following example also appears in `/var/log/google-cloud-ops-agent/subagents/logging-module.log` on Linux VMs or `C:\ProgramData\Google\Cloud Operations\Ops Agent\log\logging-module.log` on Windows VMs when the VM can't send the buffer chunks to Cloud Logging API:
    
    
    [2023/04/15 08:21:17] [warn] [engine] failed to flush chunk
    

#### Problems in the HTTP proxy

A problem with the HTTP proxy configuration might generate errors. For example, errors from `flb_upstream` with the term `context` indicates a problem with the proxy configuration:
    
    
    [2024/03/25 12:21:51] [error] [C:\work\submodules\fluent-bit\src\flb_upstream.c:281 errno=2] No such file or directory
    [2024/03/25 12:21:51] [error] [upstream] error creating context from URL: https://oauth2.googleapis.com/token
    [2024/03/25 12:21:51] [error] [oauth2] error creating upstream context
    

To fix this issue, confirm that the HTTP proxy has been configured correctly. For instructions on how to set up the HTTP proxy, see [Configure an HTTP proxy](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#configure-proxy).

For HTTP proxy format specifications, see the [Fluent Bit official manual](https://docs.fluentbit.io/manual/administration/http-proxy).

## I want to collect only metrics or logs, not both

By default, the Ops Agent collects both metrics and logs. To disable the collection of metrics or logs, use the Ops Agent `config.yaml` file to override the default `logging` or `metrics` service so that the default pipeline has no receivers. For more information, see the following:

  * [Example logging `service` configurations](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#logging-service-examples).
  * [Example metrics `service` configurations](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#metrics-service-examples).



Stopping data ingestion by disabling the Ops Agent sub-agent services "Logging Agent" or "Metrics Agent" results in an invalid configuration and isn't supported.

## Metrics are being collected, but something seems wrong

This section describes some common error conditions.

### Agent is logging "Exporting failed. Will retry" messages

You see "Exporting failed" log entries when the first data point of a cumulative metric gets dropped. The following logs are not harmful and can be safely ignored:
    
    
    Jul 13 17:28:03 debian9-trouble otelopscol[2134]: 2021-07-13T17:28:03.092Z        info        exporterhelper/queued_retry.go:316        Exporting failed. Will retry the request a
    fter interval.        {"kind": "exporter", "name": "googlecloud/agent", "error": "rpc error: code = InvalidArgument desc = Field timeSeries[1].points[0].interval.start_time had a
    n invalid value of \"2021-07-13T10:25:18.061-07:00\": The start time must be before the end time (2021-07-13T10:25:18.061-07:00) for the non-gauge metric 'agent.googleapis.com/ag
    ent/uptime'.", "interval": "23.491024535s"}
    Jul 13 17:28:41 debian9-trouble otelopscol[2134]: 2021-07-13T17:28:41.269Z        info        exporterhelper/queued_retry.go:316        Exporting failed. Will retry the request a
    fter interval.        {"kind": "exporter", "name": "googlecloud/agent", "error": "rpc error: code = InvalidArgument desc = Field timeSeries[0].points[0].interval.start_time had a
    n invalid value of \"2021-07-13T10:26:18.061-07:00\": The start time must be before the end time (2021-07-13T10:26:18.061-07:00) for the non-gauge metric 'agent.googleapis.com/ag
    ent/monitoring/point_count'.", "interval": "21.556591578s"}
    

### Agent is logging "TimeSeries could not be written: Points must be written in order." messages

If you have upgraded to the Ops Agent from the legacy Monitoring agent and are seeing the following error message when writing cumulative metrics, then the solution is to reboot your VM. The Ops Agent and the Monitoring agent calculate the start times for cumulative metrics differently, which can lead to points appearing out of order. Rebooting the VM resets the start time and fixes this problem.
    
    
    Jun 2 14:00:06 * otelopscol[4035]: 2023-06-02T14:00:06.304Z#011error#011exporterhelper/queued_retry.go:367#011Exporting failed.
    Try enabling retry_on_failure config option to retry on retryable errors#011{"error": "failed to export time series to GCM: rpc error: code = InvalidArgument desc =
    One or more TimeSeries could not be written: Points must be written in order. One or more of the points specified had an older start time than the most recent point.:
    gce_instance{instance_id:*,zone:*} timeSeries[0-199]: agent.googleapis.com/memory/bytes_used{state:slab}
    

### Agent is logging "One or more points were written more frequently than the maximum sampling period"

If the same receiver is used in multiple pipelines in your Ops Agent configuration, then metrics collected by that receiver are sent by each pipeline that uses the receiver. This configuration can cause metric duplication and results in "points were written more frequently than the maximum sampling period" errors in your logs:
    
    
    Jan 26 11:11:06 * otelopscol[1234]: 2026-01-26T11:11:06.665Z#011error#011exporterhelper/queued_retry.go:367#011Exporting failed. Dropping data.
    {"error": "failed to export metrics to projects/*: rpc error: code = InvalidArgument desc = One or more TimeSeries could not be written:
    timeSeries[...] (... metric.type=\"agent.googleapis.com/cpu/utilization\", ... resource.type=\"gce_instance\", ...):
    write for resource failed: One or more points were written more frequently than the maximum sampling period configured for the metric."}
    

Metric duplication often occurs when you add a receiver to a new pipeline that is already used in the Ops Agent's built-in default configuration. Because the default configuration is not explicitly shown in your `config.yaml` file, you might not be aware that a receiver is already in use. When creating new pipelines, review the [Ops Agent default configuration](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration#default) documentation to see which receivers are used in the default pipelines. For example, the `hostmetrics` receiver is enabled by default in the `default_pipeline`. If you create and enable a new pipeline that also uses the `hostmetrics` receiver in your `config.yaml`, then metrics from `hostmetrics` are sent twice because the receiver is now used in two pipelines.

To resolve this issue, prevent metric duplication by ensuring that the same receiver is not used in multiple pipelines that write to Cloud Monitoring. You can do this by removing the receiver from your user-defined pipeline, or by overriding the `default_pipeline` to remove that receiver from it.

### Agent is logging "Token must be a short-lived token (60 minutes) and in a reasonable timeframe" messages

If you are seeing the following error message when the agent writes metrics, then it indicates the system clock is not synchronized correctly:
    
    
    Invalid JWT: Token must be a short-lived token (60 minutes) and in a
    reasonable timeframe. Check your iat and exp values in the JWT claim.
    

For information about synchronizing system clocks, see [Configure NTP on a VM](https://cloud.google.com/compute/docs/instances/configure-ntp#windows).

### Agent is logging 'metrics receiver with type "nvml" is not supported'

If you are collecting NVIDIA Management Library (NVML) GPU metrics ([`agent.googleapis.com/gpu`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu)) by using the `nvml` receiver, then you have been using a version of the Ops Agent with preview support for the NVML metrics. Support for these metrics became generally available in Ops Agent version 2.38.0. In the GA version, the metric collection done by the `nvml` receiver was merged into the `hostmetrics` receiver, and the `nvml` receiver was removed.

You see the error message 'metrics receiver with type "nvml" is not supported' after installing Ops Agent version 2.38.0 or newer when you were using the preview `nvml` receiver and you overrode the default collection interval in your user-specified configuration file. The error occurs because because the `nvml` receiver no longer exists but your user-specified configuration file still refers to it.

To correct this problem, update your user-specified configuration file to override the collection interval on the `hostmetrics` receiver instead.

### GPU metrics are missing

If the Ops Agent is collecting some metrics but some or all of the NVIDIA Management Library (NVML) GPU ([`agent.googleapis.com/gpu`](https://docs.cloud.google.com/monitoring/api/metrics_opsagent#agent-gpu)) metrics are missing, then you might have a configuration problem or have no processes using the GPU.

If you are not collecting any GPU metrics, then check the GPU driver. To collect GPU metrics, the Ops Agent requires the GPU driver to be installed and configured on the VM. To check the driver, do the following:

  1. To verify that the driver is installed and running correctly, follow the steps to [verify the GPU driver install](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#verify-driver-install).

  2. If the driver is not installed, do the following:

     1. [Install the GPU driver](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).
     2. [Restart the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart).

You must restart the Ops Agent after installing or upgrading the GPU driver.

     3. Check the Ops Agent logs to verify that the communication has been successfully initiated. The log messages resemble the following:
            
            Jul 11 18:28:12 multi-gpu-debian11-2 otelopscol[906670]: 2024-07-11T18:28:12.771Z        info        nvmlreceiver/client.go:128        Successfully initialized Nvidia Management Library
            Jul 11 18:28:12 multi-gpu-debian11-2 otelopscol[906670]: 2024-07-11T18:28:12.772Z        info        nvmlreceiver/client.go:151        Nvidia Management library version is 12.555.42.06
            Jul 11 18:28:12 multi-gpu-debian11-2 otelopscol[906670]: 2024-07-11T18:28:12.772Z        info        nvmlreceiver/client.go:157        NVIDIA driver version is 555.42.06
            Jul 11 18:28:12 multi-gpu-debian11-2 otelopscol[906670]: 2024-07-11T18:28:12.781Z        info        nvmlreceiver/client.go:192        Discovered Nvidia device 0 of model NVIDIA L4 with UUID GPU-fc5a05a7-8859-ec33-c940-3cf0930c0e61.
            




If the GPU driver is installed and the Ops Agent logs indicate that the Ops Agent is communicating with the driver, but you are not seeing any GPU metrics, then the problem might be a problem with the chart you are using. For information about troubleshooting charts, see [Chart doesn't display any data](https://docs.cloud.google.com/monitoring/charts/troubleshooting-charts#no-data-on-chart).

If you are collecting some GPU metrics but are missing the `processes` metrics—`processes/max_bytes_used` and `processes/utilization`—then you have no processes running on GPUs. The GPU `processes` metrics aren't collected if there are no processes running on the GPU.

### Some of the metrics are missing or inconsistent

There is a small number of metrics that the Ops Agent version 2.0.0 and newer handles differently from the "preview" versions of the Ops Agent (versions less than 2.0.0) or the Monitoring agent.

The following table describes differences in the data ingested by the Ops Agent and the legacy Monitoring agent. Metric type, omitting  
`agent.googleapis.com` | Ops Agent (GA)† | Ops Agent (Preview)† | Legacy Monitoring agent  
---|---|---|---  
[ `cpu_state`](https://docs.cloud.google.com/monitoring/api/metrics_agent#cpu/utilization) | The possible values for Windows are `idle`, `interrupt,`   
`system` and `user`. | The possible values for Windows are `idle`, `interrupt,`   
`system` and `user`. | The possible values for Windows are `idle` and `used`.   
[ `disk/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/bytes_used) and  
[ `disk/percent_used`](https://docs.cloud.google.com/monitoring/api/metrics_agent#disk/percent_used) | Ingested with the full path in the `device` label; for example, `/dev/sda15`.  
  
Not ingested for virtual devices like `tmpfs` and `udev`. | Ingested without `/dev` in the path in the `device` label; for example, `sda15`.  
  
Ingested for virtual devices like `tmpfs` and `udev`. | Ingested without `/dev` in the path in the `device` label; for example, `sda15`.  
  
Ingested for virtual devices like `tmpfs` and `udev`.  
†The **GA** column refers to Ops Agent versions 2.0.0 and higher. The **Preview** column refers to Ops Agent versions less than 2.0.0.

## Windows-specific problems

The following sections apply only to the Ops Agent running on Windows.

### Delay in arrival of logs

If you notice a delay in the arrival of logs and but are seeing the arrival of Windows SuccessAudit log entries, such as `"An attempt was made to access an object."`, then the number of SuccessAudit log entries might be preventing your logs from ingesting on time. To fix this issue, disable SuccessAudit log entries if they are not needed.

### Corrupt performance counters on Windows

If the metrics sub-agent fails to start, you might see one of the following errors in Cloud Logging:
    
    
    Failed to retrieve perf counter object "LogicalDisk"
    Failed to retrieve perf counter object "Memory"
    Failed to retrieve perf counter object "System"
    

These errors can occur if your system's performance counters become corrupt. You can resolve the errors by rebuilding the performance counters. In PowerShell as administrator, run:
    
    
    cd C:\Windows\system32
    lodctr /R
    

The previous command can fail occasionally; in that case, reload PowerShell and try it again until it succeeds.

After the command succeeds, restart the Ops Agent:
    
    
    Restart-Service -Name google-cloud-ops-agent -Force
    

## Completely reset the agent state

If the agent enters a non-recoverable state, follow these steps to restore the agent to a fresh state.

**Note:** This process removes all buffer state, which can result in log loss. For a process that doesn't reset buffer state, see Reset but save buffer files.

**Linux**

Stop the agent service:
    
    
    sudo service google-cloud-ops-agent stop
    

Remove the agent package:
    
    
    curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
    sudo bash add-google-cloud-ops-agent-repo.sh --uninstall --remove-repo
    

Remove the agent's self logs on disk:
    
    
    sudo rm -rf /var/log/google-cloud-ops-agent
    

Remove the agent's local buffers on disk:
    
    
    sudo rm -rf /var/lib/google-cloud-ops-agent/fluent-bit/buffers/*/
    

**Note:** The directory `/var/lib/google-cloud-ops-agent/fluent-bit/buffers/` contains the following types of files: 

  * Buffer files: These files are buffered log entries that were tailed and processed by the Ops Agent but not yet ingested into Cloud Logging. When there are corrupted chunks, Ops Agent should skip them in versions >= 2.15.0. In some cases, they need to be cleaned up manually though. These files are stored in the nested folders like: `/var/lib/google-cloud-ops-agent/fluent-bit/buffers/tail.1/*`
  * Log file tailing position files: These files record at which location in the log files the Ops Agent has already tailed. If these files are removed, the Ops Agent will start from the top of the files that it is configured to tail. Deleting these files can lead to log duplication if those logs had previously been ingested successfully. These files are stored directly in the directory as files like: `/var/lib/google-cloud-ops-agent/fluent-bit/buffers/default_pipeline_syslog*`. 



The syntax `.../buffers/*/` in the previous command ensures that only the buffer files are deleted. The position files are not deleted.

Reinstall and restart the agent:
    
    
    curl -sSO https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.sh
    sudo bash add-google-cloud-ops-agent-repo.sh --also-install
    sudo service google-cloud-ops-agent restart
    

**Windows**

**Note:** The commands for Windows need to be run in Powershell as **Administrator**.

Stop the agent service:
    
    
    Stop-Service google-cloud-ops-agent -Force;
    Get-Service google-cloud-ops-agent* | %{sc.exe delete $_};
    taskkill /f /fi "SERVICES eq google-cloud-ops-agent*";
    

Remove the agent package:
    
    
    (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.ps1", "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1");
    $env:REPO_SUFFIX="";
    Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -Uninstall -RemoveRepo"
    

Remove the agent's self logs on disk:
    
    
    rmdir -R -ErrorAction SilentlyContinue "C:\ProgramData\Google\Cloud Operations\Ops Agent\log";
    

Remove the agent's local buffers on disk:
    
    
    Get-ChildItem -Path "C:\ProgramData\Google\Cloud Operations\Ops Agent\run\buffers\" -Directory -ErrorAction SilentlyContinue | %{rm -r -Path $_.FullName}
    

**Note:** Similar to Linux, this command deletes only the subdirectories in the `C:\ProgramData\Google\Cloud Operations\Ops Agent\run\buffers` directory, so that buffer files are removed but position files are untouched.

Reinstall and restart the agent:
    
    
    (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/add-google-cloud-ops-agent-repo.ps1", "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1");
    $env:REPO_SUFFIX="";
    Invoke-Expression "${env:UserProfile}\add-google-cloud-ops-agent-repo.ps1 -AlsoInstall"
    

### Reset but save the buffer files

If the VM does not have corrupted buffer chunks (that is, there are no `format check failed` messages in the Ops Agent's self log file), then you can skip the previous commands that remove the local buffers when resetting the agent state.

If the VM does have corrupted buffer chunks, then you have to remove them. The following options describe different ways to handle the buffers. The other steps described in Completely reset the agent state are still applicable.

  * **Option 1:** Delete the entire `buffers` directory. This is the easiest option, but it can result in loss of the uncorrupted buffered logs or log duplication due to the loss of the position files.

**Linux**
        
        sudo rm -rf /var/lib/google-cloud-ops-agent/fluent-bit/buffers
        

**Windows**
        
        rmdir -R -ErrorAction SilentlyContinue "C:\ProgramData\Google\Cloud Operations\Ops Agent\run\buffers";
        

  * **Option 2:** Delete the buffer subdirectories from the `buffers` directory, but leave the position files. This approach is described in Completely reset the agent state.

  * **Option 3:** If you don't want to delete all the buffer files, then you can extract the names of the corrupted buffer files from the agent's self logs and delete only corrupted buffer files.

**Linux**
        
        grep "format check failed" /var/log/google-cloud-ops-agent/subagents/logging-module.log | sed 's|.*format check failed: |/var/lib/google-cloud-ops-agent/fluent-bit/buffers/|' | xargs sudo rm -f
        

**Windows**
        
        $oalogspath="C:\ProgramData\Google\Cloud Operations\Ops Agent\log\logging-module.log";
        if (Test-Path $oalogspath) {
          Select-String "format check failed" $oalogspath |
          %{$_ -replace '.*format check failed: (.*)/(.*)', '$1\$2'} |
          %{rm -ErrorAction SilentlyContinue -Path ('C:\ProgramData\Google\Cloud Operations\Ops Agent\run\buffers\' + $_)}
        };
        

  * **Option 4:** If there are many corrupted buffers and you want to reprocess all log files, then you can use the commands from Option 3 and also delete the position files (which store Ops Agent progress per log file). Deleting the position files can result in log duplication for any logs that are already successfully ingested. This option only reprocesses current log _files_ ; it does not reprocess files that had been rotated out already or logs from other sources like a TCP port. The position files are stored in the `buffers` directory but are stored as files. The local buffers are stored as subdirectories in the `buffers` directory,

**Linux**
        
        grep "format check failed" /var/log/google-cloud-ops-agent/subagents/logging-module.log | sed 's|.*format check failed: |/var/lib/google-cloud-ops-agent/fluent-bit/buffers/|' | xargs sudo rm -f
        sudo find /var/lib/google-cloud-ops-agent/fluent-bit/buffers -maxdepth 1 -type f -delete
        

**Windows**
        
        $oalogspath="C:\ProgramData\Google\Cloud Operations\Ops Agent\log\logging-module.log";
        if (Test-Path $oalogspath) {
          Select-String "format check failed" $oalogspath |
          %{$_ -replace '.*format check failed: (.*)/(.*)', '$1\$2'} |
          %{rm -ErrorAction SilentlyContinue -Path ('C:\ProgramData\Google\Cloud Operations\Ops Agent\run\buffers\' + $_)}
        };
        Get-ChildItem -Path "C:\ProgramData\Google\Cloud Operations\Ops Agent\run\buffers\" -File -ErrorAction SilentlyContinue | %{$_.Delete()}
        




## Known issues in recent Ops Agent releases

The following sections describe issues known to recent Ops Agent releases.

## Ops Agent version 2.56.0 fails to send Prometheus metrics

If you are using Ops Agent version 2.56.0 in conjunction with the [Prometheus receiver](https://docs.cloud.google.com/monitoring/agent/ops-agent/prometheus) and if your scrape target is emitting metrics with additional `*_created` metrics for counters (to support the new experimental [Created Timestamps feature](https://github.com/prometheus/proposals/blob/0c31275fb33a2e5dd9b7a2cab64a5904a6b5dcca/proposals/2023-06-13_created-timestamp.md#created-timestamps)), then the agent might fail to write metrics and report errors that start times must be positive. The log messages resemble the following:
    
    
    Field points[0].interval.start_time had an invalid value of \"1781-05-03T21:46:07.592596-07:52\": The start time must be positive.;
    

This is a problem with upstream OpenTelemetry. To resolve the error until it can be fixed in a new Ops Agent release, use version 2.55.0, which is unaffected. If you are using Agent Policies, then you can also pin the version to 2.55.0 to prevent upgrades. For more information, see [Installing a specific version of the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#install-specific-version).

### Ops Agent version 2.47.0, 2.48.0, or 2.49.0 crash-looping

Versions 2.47.0, 2.48.0, and 2.49.0 incorporated a faulty FluentBit component for logging. This component fails on specific log lines and causes the Ops Agent to crash-loop.

This issue is resolved in version 2.50.0 of the Ops Agent.

### Prometheus metrics namespace includes instance name in addition to instance ID starting from Ops Agent version 2.46.0

Starting with version 2.46.0, the Ops Agent includes the VM name as part of the `namespace` label when ingesting metrics in the Prometheus ingestion format. In earlier versions, Prometheus metrics used only the instance ID of the VM as part of the `namespace` label, but starting with version 2.46.0, `namespace` is set to `INSTANCE_ID/INSTANCE_NAME`.

If you have charts, dashboards, or alerting policies that use the `namespace` label, you might have to update your queries after upgrading your Ops Agent to version 2.46.0 or later. For example, if your PromQL query looked like: `http_requests_total{namespace="123456789"}`, you have to change it to `http_requests_total{namespace=~"123456789.*"}`, since the `namespace` label is of the format `INSTANCE_ID/INSTANCE_NAME`.

### Prometheus untyped metrics change metric type starting with Ops Agent version 2.39.0

Starting with version 2.39.0, the Ops Agent supports ingesting Prometheus metrics with unknown types. In earlier versions, these metrics are treated by the Ops Agent as gauges, but starting with version 2.39.0, untyped metrics are treated as both gauges and counters. Users can now use cumulative operations on these metrics as a result.

If you use PromQL, then you can apply cumulative operations to untyped Prometheus metrics after upgrading your Ops Agent to version 2.39.0 or later.

### High memory usage on Windows VMs (versions 2.27.0 to 2.29.0)

On Windows in Ops Agent versions 2.27.0 to 2.29.0, a bug that caused the agent to sometimes leak sockets led to increased memory usage and a high number of handles held by the `fluent-bit.exe` process.

To mitigate this problem, [upgrade the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#upgrade) to version 2.30.0 or greater, and [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart).

### Event Log time zones are wrong on Windows (versions 2.15.0 to 2.26.0)

The timestamps associated with Windows Event Logs in Cloud Logging might be incorrect if you change your VM's timezone from UTC. This was fixed in Ops Agent 2.27.0, but due to the known Windows high memory issue, we recommend that you upgrade to at least Ops Agent 2.30.0 if you are running into this issue. If you are unable to upgrade, you can try one of the following workarounds.

**Use a UTC time-zone**

In PowerShell, run the following commands as administrator:
    
    
    Set-TimeZone -Id "UTC"
    Restart-Service -Name "google-cloud-ops-agent-fluent-bit" -Force
    

**Override the time-zone setting for the logging sub-agent service only**

In PowerShell, run the following commands as administrator:

**Caution:** This will overwrite the **Environment** registry value for the service if it already exists.
    
    
    Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\google-cloud-ops-agent-fluent-bit" -Name "Environment" -Type "MultiString" -Value "TZ=UTC0"
    Restart-Service -Name "google-cloud-ops-agent-fluent-bit" -Force
    

### Parsed timestamps on Windows have incorrect timezone (any version before 2.27.0)

If you use a log processor that parses a timestamp, the timezone value will be not be parsed properly on Windows. This was fixed in Ops Agent 2.27.0, but due to the known Windows high memory issue, we recommend that you upgrade to at least Ops Agent 2.30.0 if you are running into this issue.

## Known issues in older Ops Agent releases

The following sections describe issues known to occur with older Ops Agent releases.

### Non-harmful logs (versions 2.9.1 and older)

You might see errors when scraping metrics from pseudo-processes or restricted processes. The following logs are not harmful and can be safely ignored. To eliminate these messages, upgrade the Ops Agent to version 2.10.0 or newer.
    
    
        Jul 13 17:28:55 debian9-trouble otelopscol[2134]: 2021-07-13T17:28:55.848Z        error        scraperhelper/scrapercontroller.go:205        Error scraping metrics        {"kind"
      : "receiver", "name": "hostmetrics/hostmetrics", "error": "[error reading process name for pid 2: readlink /proc/2/exe: no such file or directory; error reading process name for
      pid 3: readlink /proc/3/exe: no such file or directory; error reading process name for pid 4: readlink /proc/4/exe: no such file or directory; error reading process name for pid
      5: readlink /proc/5/exe: no such file or directory; error reading process name for pid 6: readlink /proc/6/exe: no such file or directory; error reading process name for pid 7: r
      eadlink /proc/7/exe: no such file or directory; error reading process name for pid 8: readlink /proc/8/exe: no such file or directory; error reading process name for pid 9: readl
      ink /proc/9/exe: no such file or directory; error reading process name for pid 10: readlink /proc/10/exe: no such file or directory; error reading process name for pid 11: readli
      nk /proc/11/exe: no such file or directory; error reading process name for pid 12: readlink /proc/12/exe: no such file or directory; error reading process name for pid 13: readli
      nk /proc/13/exe: no such file or directory; error reading process name for pid 14: readlink /proc/14/exe: no such file or directory; error reading process name for pid 15: readli
      nk /proc/15/exe: no such file or directory; error reading process name for pid 16: readlink /proc/16/exe: no such file or directory; error reading process name for pid 17: readli
      nk /proc/17/exe: no such file or directory; error reading process name for pid 18: readlink /proc/18/exe: no such file or directory; error reading process name for pid 19: readli
      nk /proc/19/exe: no such file or directory; error reading process name for pid 20: readlink /proc/20/exe: no such file or directory; error reading process name for pid 21: readli
      nk /proc/21/exe: no such file or directory; error reading process name for pid 22: readlink /proc/22/exe: no such file or directory; error reading process name for pid
      Jul 13 17:28:55 debian9-trouble otelopscol[2134]: 23: readlink /proc/23/exe: no such file or directory; error reading process name for pid 24: readlink /proc/24/exe: no such file
       or directory; error reading process name for pid 25: readlink /proc/25/exe: no such file or directory; error reading process name for pid 26: readlink /proc/26/exe: no such file
       or directory; error reading process name for pid 27: readlink /proc/27/exe: no such file or directory; error reading process name for pid 28: readlink /proc/28/exe: no such file
       or directory; error reading process name for pid 30: readlink /proc/30/exe: no such file or directory; error reading process name for pid 31: readlink /proc/31/exe: no such file
       or directory; error reading process name for pid 43: readlink /proc/43/exe: no such file or directory; error reading process name for pid 44: readlink /proc/44/exe: no such file
       or directory; error reading process name for pid 45: readlink /proc/45/exe: no such file or directory; error reading process name for pid 90: readlink /proc/90/exe: no such file
       or directory; error reading process name for pid 92: readlink /proc/92/exe: no such file or directory; error reading process name for pid 106: readlink /proc/106/exe: no such fi
      le or directory; error reading process name for pid 360: readlink /proc/360/exe: no such file or directory; error reading process name for pid 375: readlink /proc/375/exe: no suc
      h file or directory; error reading process name for pid 384: readlink /proc/384/exe: no such file or directory; error reading process name for pid 386: readlink /proc/386/exe: no
       such file or directory; error reading process name for pid 387: readlink /proc/387/exe: no such file or directory; error reading process name for pid 422: readlink /proc/422/exe
      : no such file or directory; error reading process name for pid 491: readlink /proc/491/exe: no such file or directory; error reading process name for pid 500: readlink /proc/500
      /exe: no such file or directory; error reading process name for pid 2121: readlink /proc/2121/exe: no such file or directory; error reading
      Jul 13 17:28:55 debian9-trouble otelopscol[2134]: process name for pid 2127: readlink /proc/2127/exe: no such file or directory]"}
      Jul 13 17:28:55 debian9-trouble otelopscol[2134]: go.opentelemetry.io/collector/receiver/scraperhelper.(_controller).scrapeMetricsAndReport
      Jul 13 17:28:55 debian9-trouble otelopscol[2134]:         /root/go/pkg/mod/go.opentelemetry.io/collector@v0.29.0/receiver/scraperhelper/scrapercontroller.go:205
      Jul 13 17:28:55 debian9-trouble otelopscol[2134]: go.opentelemetry.io/collector/receiver/scraperhelper.(_ controller).startScraping.func1
      Jul 13 17:28:55 debian9-trouble otelopscol[2134]:         /root/go/pkg/mod/go.opentelemetry.io/collector@v0.29.0/receiver/scraperhelper/scrapercontroller.go:186
      

### Agent self logs consume too much CPU, memory, and disk space (versions 2.16.0 and older)

Versions of the Ops Agent prior to 2.17.0 might consume a lot of CPU, memory, and disk space with `/var/log/google-cloud-ops-agent/subagents/logging-module.log` files on Linux VMs or `C:\ProgramData\Google\Cloud Operations\Ops Agent\log\logging-module.log` files on Windows VMs due to corrupted buffer chunks. When this happens, you see a large number of messages like the following in the `logging-module.log` file.
    
    
      [2022/04/30 05:23:38] [error] [input chunk] error writing data from tail.2 instance
      [2022/04/30 05:23:38] [error] [storage] format check failed: tail.2/2004860-1650614856.691268293.flb
      [2022/04/30 05:23:38] [error] [storage] format check failed: tail.2/2004860-1650614856.691268293.flb
      [2022/04/30 05:23:38] [error] [storage] [cio file] file is not mmap()ed: tail.2:2004860-1650614856.691268293.flb
      

To resolve this problem, [upgrade the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#upgrade) to version 2.17.0 or newer, and Completely reset the agent state.

If your system still generates a large volume of agent self logs, consider using log rotation. For more information, see [Set up log rotation](https://docs.cloud.google.com/monitoring/agent/ops-agent/rotate-logs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
