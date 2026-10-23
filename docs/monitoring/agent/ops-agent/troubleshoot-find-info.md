---
url: https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info/
title: Find Ops Agent troubleshooting information \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:52.557392+00:00
---

# Find Ops Agent troubleshooting information  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-find-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Find Ops Agent troubleshooting information Stay organized with collections  Save and categorize content based on your preferences. 

This document describes sources of diagnostic information that you can use to identify problems in the installation or running of the Ops Agent.

## Verify agent status by using gcpdiag

You can use gcpdiag to report the status of the Ops Agent on individual VMs or the entire VM fleet within your project, confirming that the agent is installed and is actively sending logs and metrics. gcpdiag can create status reports in several formats, including as CSV or JSON format.

The following shows a fleet-wide agent status report in CSV format:
    
    
    🔎 gce/ERR/2024_004: Verify Ops Agent is installed on GCE VMs and is sending logs and metrics.
    
    gce/ERR/2024_004,projects/my-project/zones/my-location/instances/instance-1,failed,Ops Agent not installed on the VM,https://gcpdiag.dev/rules/gce/ERR/2024_004
    gce/ERR/2024_004,projects/my-project/zones/my-location/instances/instance-2,skipped,VM Manager is needed for the ops agent detection. Please enable it at: https://cloud.google.com/compute/docs/manage-os#automatic and run this check again.,https://gcpdiag.dev/rules/gce/ERR/2024_004
    gce/ERR/2024_004,projects/my-project/zones/my-location/instances/instance-3,skipped,VM Manager is needed for the ops agent detection. Please enable it at: https://cloud.google.com/compute/docs/manage-os#automatic and run this check again.,https://gcpdiag.dev/rules/gce/ERR/2024_004
    gce/ERR/2024_004,projects/my-project/zones/my-location/instances/instance-4,ok,"Ops Agent installed on the VM, and is successfully sending logs and metrics.",https://gcpdiag.dev/rules/gce/ERR/2024_004
    gce/ERR/2024_004,projects/my-project/zones/my-location/instances/instance-5,ok,"Ops Agent installed on the VM, and is successfully sending logs and metrics.",https://gcpdiag.dev/rules/gce/ERR/2024_004
    

The gcpdiag tool was created by the Google Cloud support to help you self-diagnose common issues in your Google Cloud project, including issues with the Ops Agent. gcpdiag is an open-source tool, not an official Google Cloud product, but it is actively developed and maintained by the Google Cloud support team. Contribute or report issues on [GitHub](https://github.com/GoogleCloudPlatform/gcpdiag/issues).

### Before you begin

gcpdiag is integrated with Cloud Shell, so you can run it without any installation required. To run gcpdiag, you must first meet the following prerequisites:

  * **Authorization** : gcpdiag uses [application default credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC) in Cloud Shell to authenticate.   
Ensure that the credentials used with gcpdiag have at least the following roles on the Google Cloud project where the Ops Agent is running:

    * Viewer (`roles/viewer`)
    * Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`)
  * **APIs** : To use gcpdiag in a project, the following APIs must be enabled:

    * Cloud Resource Manager API: `cloudresourcemanager.googleapis.com`
    * Identity and Access Management API: `iam.googleapis.com`
    * Cloud Logging API: `logging.googleapis.com`
    * Service Usage: `serviceusage.googleapis.com`

To enable these APIs, run the following command in Cloud Shell or another command line:
    
    gcloud --project=PROJECT_ID services enable \
       cloudresourcemanager.googleapis.com \
       iam.googleapis.com \
       logging.googleapis.com \
       serviceusage.googleapis.com
    

  * **VM Manager** : Enable [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager#pricing) at free tier on your instance. If you installed the Ops Agent [during VM creation](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-agent-vm-creation) or if [an agent policy](https://docs.cloud.google.com/monitoring/agent/ops-agent/managing-agent-policies) manages the Ops Agent installation on your VM instances, you've already met the requirements for [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager).




### Run gcpdiag

The `gcpdiag` command for use with the Ops Agent has the following basic syntax:
    
    
    gcpdiag lint --project=PROJECT_ID [--name=INSTANCE_NAME] --show-skipped --include=gce/err/2024_004 [--output=[CSV|JSON]]
    

  * PROJECT_ID is the ID of your Google Cloud project.
  * INSTANCE_NAME is the name of your Compute Engine VM. Use the `--name` option to query a specific VM; omit the option to query the entire fleet.
  * Use the `--output` option to save the report in a CSV- or JSON-formatted file; omit the option if you don't want an output file.



The value of the `--include` option specifies one or more gcpdiag rules; `gce/ERR/2024-004` is the rule for the Ops Agent. For more information about the syntax of the gcpdiag command, see [gcpdiag - Diagnostics for Google Cloud Platform](https://gcpdiag.dev/docs/usage/).

For example, to generate a fleet-wide report for the project "my-project", run the following command:
    
    
    gcpdiag lint --project=my-project --show-skipped --include=gce/ERR/2024_004
    

The output resembles the following:
    
    
    🔎 gce/ERR/2024_004: Verify Ops Agent is installed on GCE VMs and is sending logs and metrics.
      - my-project/instance-1                                                 [FAIL] Ops Agent not installed on the VM
      - my-project/instance-2                                                 [FAIL] Ops Agent not installed on the VM
      - my-project/instance-3                                                 [SKIP] Unable to confirm Ops Agent installation
      VM Manager is needed for the ops agent detection. Please enable it at: https://cloud.google.com/compute/docs/manage-os#automatic and run this check again.
      - my-project/instance-4                                            [FAIL] Ops Agent is installed, but it's failing to send both logs and metrics to Google Cloud.
      Is Ops Agent sending logs? (Yes)  Is Ops Agent sending metrics? (No)
      - my-project/instance-5                                                 [FAIL] Ops Agent is installed, but it's failing to send both logs and metrics to Google Cloud.
      Is Ops Agent sending logs? (No)   Is Ops Agent sending metrics? (No)
      - my-project/instance-6                                                 [ OK ] Ops Agent installed on the VM, and is successfully sending logs and metrics.
      - my-project/instance-7                                                 [ OK ] Ops Agent installed on the VM, and is successfully sending logs and metrics.
    

To generate a report for the instance "my-instance" in project "my-project", run the following command:
    
    
    gcpdiag lint  --project=my-project --name=my-instance --show-skipped --include=gce/err/2024_004
    

The output resembles the following:
    
    
    🔎 gce/ERR/2024_004: Verify Ops Agent is installed on GCE VMs and is sending logs and metrics.
      - my-project/my-instance   [ OK ] Ops Agent installed on the VM, and is successfully sending logs and metrics.
    

If your `gcpdiag` command fails with output that resembles the following, verify that you have met all of the prerequisites for running the tool.
    
    
    WARNING:googleapiclient.http:Encountered 403 Forbidden with reason "PERMISSION_DENIED"
    [ERROR]:can't access project my-project: Cloud Resource Manager API has not been used in project my-project before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview?project=my-project then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry..
    [DEBUG]: An Http Error occurred whiles accessing projects.get
    
    HttpError 403 when requesting https://cloudresourcemanager.googleapis.com/v3/projects/my-project?alt=json returned Cloud Resource Manager API has not been used in project my-project before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/cloudresourcemanager.googleapis.com/overview?project=my-project then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry. Details: ...
    [ERROR]:exiting program...
    error getting project details
    

### Interpret gcpdiag output

This section provides information to help you understand and use the reports generated by gcpdiag.

The gcpdiag command generates reports that contain the following information:

  * An indicator of the gcpdiag rule with which the command was invoked. For the Ops Agent, this information looks like the following:  
`🔎 gce/ERR/2024_004: Verify Ops Agent is installed on GCE VMs and is sending logs and metrics`
  * An identifier of the result for a specific VM with the format PROJECT_ID/INSTANCE_ID. For a fleet-wide report, the output contains an entry for each VM. For a single-VM report, the output contains a single entry. 
  * The status of the check. The status has one of the following values: 
    * `OK`
    * `FAIL`
    * `SKIP`
  * A description of the status value. 



The following sections provide more information about the status values and their meaning.

#### Status: `OK`

A status of `OK` means that the Ops Agent is running on the VM and sending both logs and metrics from the VM. The report includes the following status description:  
`Ops Agent installed on the VM, and is successfully sending logs and metrics.`

#### Status: `FAIL`

A status of `FAIL` means that the Ops Agent is not installed, or it is not sending both logs and metrics from the VM. The status description indicates which problem has been detected:

  * If the Ops Agent is not installed, then you see the following status description:  
`Ops Agent not installed on the VM`
  * If the Ops Agent is not sending both logs and metrics from the VM, then you see a status description like the following:  
`Agent is installed, but it's failing to send both logs and metrics to Google Cloud.  
Is Ops Agent sending logs? (Yes) Is Ops Agent sending metrics? (No) `



If the Ops Agent is not installed, then [install the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation). If the installation fails, then the problem might be one of the following: 

  * The VM does not have an associated service account. To resolve this issue, [ attach a service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account#changeserviceaccountandscopes) to the VM, and then try [installing the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation) again. 
  * The VM has one of the legacy agents (the Monitoring agent or the Logging agent) [ installed already](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#legacy-agent-installed). To resolve this issue, uninstall the legacy agents, and then try [installing the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation) again. 



If the Ops Agent is not sending logs or metrics from the VM, then use the agent health checks for start-time errors to determine and correct the problem.

#### Status: `SKIP`

A status of `SKIP` means that gcpdiag wasn't able to determine if the Ops Agent is installed on the VM. The report includes the following status description:  
` Unable to confirm Ops Agent installation  
VM Manager is needed for the ops agent detection.  
Please enable it at: https://cloud.google.com/compute/docs/manage-os#automatic and run this check again. `

To test the status of the agent, gcpdiag needs [VM Manager](https://docs.cloud.google.com/compute/docs/vm-manager) to be running on your VM. To resolve this problem, install the [VM Manager free tier](https://docs.cloud.google.com/compute/docs/vm-manager#pricing) on your instance. After installing, wait 15 minutes, and then try running the `gcpdiag` command again.

## Agent health checks

Version 2.25.1 introduced start-time health checks for the Ops Agent. When the Ops Agent starts, it performs a series of checks for conditions that prevent the agent from running correctly. If the agent detects one of the conditions, it logs a message describing the problem. The Ops Agent checks for the following: 

  * Connectivity problems
  * Availability of ports used by the agent to report metrics about itself
  * Permission problems
  * Availability of the APIs used by the agent to write logs or metrics
  * A problem in the health-check routine itself.

For information about locating start-time errors, see Find start-time errors. 

Version 2.37.0 introduced runtime health checks for the Ops Agent. These errors are reported to Cloud Logging and Error Reporting. For information about locating runtime errors, see Find runtime errors.

Version 2.46.0 introduced the informational `LogPingOpsAgent` code. This code does not represent an error. For more information, see  Verify successful log collection.

The following table lists each health-check code in alphabetical order and describes what each code means. Codes that end with the string `Err` indicate errors; other codes are informational. 

Health-check code | Category | Meaning | Suggestion  
---|---|---|---  
`DLApiConnErr` |  Connectivity  |  Request to the downloads subdomain, `dl.google.com`, failed.  |  Check your internet connection and firewall rules. For more information, see [ Network-connectivity issues](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest#network-issues).   
`FbMetricsPortErr` |  Port availability  |  Port 20202, needed for Ops Agent self metrics, is unavailable.  |  Verify that port 20202 is open. For more information, see [ Required port is unavailable](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#port-errors).   
`HcFailureErr` |  Generic  |  The Ops Agent health-check routine encountered an internal error.  |  Submit a support case from the Google Cloud console. For more information, see [ Getting support](https://docs.cloud.google.com/stackdriver/docs/getting-support).   
`LogApiConnErr` |  Connectivity  |  Request to the Logging API failed.  |  Check your internet connection and firewall rules. For more information, see [ Network-connectivity issues](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest#network-issues).   
`LogApiDisabledErr` |  API  |  The Logging API is disabled in the current Google Cloud project.  |  [ Enable the Logging API](https://docs.cloud.google.com/logging/docs/api/enable-api).   
`LogApiPermissionErr` |  Permission  |  Service account is missing the Logs Writer role (`roles/logging.logWriter`).  |  Grant the [ Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter) to the service account. For more information, see [ Agent lacks API permissions](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#agent-svc-acct-permissions).   
`LogApiScopeErr` |  Permission  |  The VM is missing the https://www.googleapis.com/​auth/​logging.write access scope.  |  Add the https://www.googleapis.com/​auth/​logging.write scope to the VM. For more information, see [ Verify your access scopes](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#before_you_begin).   
`LogApiUnauthenticatedErr` |  API  |  The current VM couldn't authenticate to the Logging API.  |  Verify that your credential files, VM access scopes, and permissions are set up correctly. For more information, see [ Authorize the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization).   
`LogPingOpsAgent` |  |  An informational payload message written every 10 minutes to the `ops-agent-health` log. You can use the resulting log entries to verify that the agent is sending logs. This message is not an error.  |  This message is expected to appear every 10 minutes. If the message does not appear for 20 minutes or longer, then agent might have encountered a problem. For troubleshooting information, see [ Troubleshoot the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshooting).   
`LogParseErr` |  Runtime  |  The Ops Agent was unable to parse one or more logs.  |  Check the configuration of any logging processors you've created. For more information see [Log-parsing errors](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest#parselog-errors).   
`LogPipeLineErr` |  Runtime  |  The Ops Agent's logging pipeline failed.  |  Verify that the agent has access to the buffer files; check for a full disk, and verify that the Ops Agent configuration is correct. For more information, see [ Pipeline errors](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest#pipeline-errors).   
`MetaApiConnErr` |  Connectivity  |  Request to the G​C​E Metadata server, for querying VM access scopes, OAuth tokens, and resource labels, failed.  |  Check your internet connection and firewall rules. For more information, see [ Network-connectivity issues](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest#network-issues).   
`MonApiConnErr` |  Connectivity  |  A request to the Monitoring API failed.  |  Check your internet connection and firewall rules. For more information, see [ Network-connectivity issues](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-run-ingest#network-issues).   
`MonApiDisabledErr` |  API  |  The Monitoring API is disabled in the current Google Cloud project.  |  [ Enable the Monitoring API](https://docs.cloud.google.com/monitoring/api/enable-api).   
`MonApiPermissionErr` |  Permission  |  Service account is missing the Monitoring Metric Writer role (`roles/monitoring.metricWriter`).  |  Grant the [ Monitoring Metric Writer role ](https://docs.cloud.google.com/monitoring/access-control#mon_roles_desc) to the service account. For more information, see [ Agent lacks API permissions](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#agent-svc-acct-permissions).   
`MonApiScopeErr` |  Permission  |  The VM is missing the https://www.googleapis.com/​auth/​monitoring.write access scope.  |  Add the https://www.googleapis.com/​auth/​monitoring.write scope to the VM. For more information, see [ Verify your access scopes](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization#before_you_begin).   
`MonApiUnauthenticatedErr` |  API  |  The current VM couldn't authenticate to the Monitoring API.  |  Verify that your credential files, VM access scopes, and permissions are set up correctly. For more information, see [ Authorize the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/authorization).   
`OtelMetricsPortErr` |  Port availability  |  Port 20201, needed for Ops Agent self metrics, is unavailable.  |  Verify that port 20201 is open. For more information, see [ A required port is unavailable](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#port-errors).   
`PacApiConnErr` |  Connectivity  |  This health-check code is unreliable. This code is disabled in Ops Agent version 2.46.1.  |  Update to version Ops Agent version 2.46.1 or above.   
  
### Find start-time errors

The location of the local health-check logs files differs for agents [ installed by using VM Extension Manager extension policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies) and for agents installed by all other methods. 

### Not installed by VM Extension Manager

Starting with version 2.35.0, health-check information is written to the `ops-agent-health` log by the Cloud Logging API (versions 2.33.0, 2.34.0 use `ops-agent-health-checks`). The same information is also written to a `health-checks.log` file as follows: 

  * **Linux** : `/var/log/google-cloud-ops-agent/health-checks.log`
  * **Windows** : `C:\ProgramData\Google\Cloud Operations\Ops Agent\log\health-checks.log`



You can also view any health-check messages by querying the status of the Ops Agent service as follows: 

  * On Linux, run the following command: 
        
        sudo systemctl status google-cloud-ops-agent"*"
           

Look for messages like "[Ports Check] Result: PASS". Other results include "ERROR" and "FAIL".

  * On Windows, use the Windows **Event Viewer**. Look for "Information", "Error", or "Failure" messages associated with the `google-cloud-ops-agent` service. 



After you resolve any problems, you must [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/installation#restart). The health checks are run when the agent starts, so to re-run the checks, you must restart the agent.

### Installed by VM Extension Manager

Health-check information is written to the `ops-agent-health` log by the Cloud Logging API. When the Ops Agent is managed by a VM Extension Manager extension policy, the same information is also written to a `health-checks.log` file as follows: 

  * **Linux** : ` /var/lib/google-guest-agent/INSTANCE_ID/agent_state/plugins/ops-agent/logs/google-cloud-ops-agent/health-checks.log`
  * **Windows** : `C:\ProgramData\Google\Compute Engine\google-guest-agent\INSTANCE_ID\agent_state\plugins\ops-agent\health-checks.log`



After you resolve any problems, you must [restart the agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies#restart-agent-vmem). The health checks are run when the agent starts, so to re-run the checks, you must restart the agent.

### Find runtime errors

The runtime health checks are reported to both Cloud Logging and Error Reporting. If the agent failed to start but was able to report errors before failing, you might also see start-time errors reported.

To view runtime errors from the Ops Agent in Logging, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Enter the following query and click **Run query** :  

         
         log_id("ops-agent-health")




To view runtime errors from the Ops Agent in Error Reporting, do the following: 

  1. In the Google Cloud console, go to the **Error Reporting** page: 

[Go to **Error Reporting**](https://console.cloud.google.com/errors)

You can also find this page by using the search bar.

  2. To see errors from the Ops Agent, filter the errors for `Ops Agent`.



### Verify successful log collection

Version 2.46.0 of the Ops Agent introduced the informational `LogPingOpsAgent` health check. This check writes an informational message to the `ops-agent-health` every 10 minutes. You can use the presence of these messages to verify that the Ops Agent is writing logs by doing any of the following: 

  * Search logs of a specific VM for the ping messages by using Logs Explorer.
  * Check the value of the metric [ `log_entry_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/log_entry_count) for a specific VM by using Metrics Explorer.
  * Create an alerting policy to notify you if a specific VM is not updating the [ `log_entry_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/log_entry_count) metric.



If any of these options indicates that the log messages are not being ingested, then you can do the following: 

  * Check for error codes indicating start-up errors or runtime errors.
  * Determine if the Ops Agent is [ up and running](https://docs.cloud.google.com/monitoring/agent/ops-agent/troubleshoot-install-startup#agent-not-running).
  * Run the agent diagnostics script.



To check the status of the Ops Agent on a specific VM, you need the instance ID of the VM. To find the instance ID, do the following: 

  * In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  * Click the name of a VM instance.
  * On the **Details** tab, locate the **Basic information** section. The instance ID appears as a numeric string. Use this string for the INSTANCE_ID value in the subsequent sections.



####  Search for messages by using Logs Explorer

To use Logs Explorer to search the logs of a VM for the ping messages, do the following: 

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. To look for ping messages from the Ops Agent on a specific VM instance, enter the following query and replace INSTANCE_ID with the identifier for a Compute Engine VM, then click **Run query** : 
         
         resource.type="gce_instance"
         resource.labels.instance_id="INSTANCE_ID"
         log_id("ops-agent-health")
         jsonPayload.code="LogPingOpsAgent"
             




####  View the `log_entry_count` metric

To use Metrics Explorer to check the value of the metric [ `log_entry_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#logging/log_entry_count) for a VM, do the following: 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the **Select a metric** field, do the following: 
     1. Enter `log entries`.
     2. For the **Resource type** , select **VM Instance**.
     3. For the **Metric category** , select **Logs-based metrics**.
     4. For the **Metric** , select **Log entries**.
     5. Select **Apply**.
  3. In the **Filter** field, add the following filters: 
     * Filter for a specific VM's instance ID: 
       1. Select the resource label **instance_id**.
       2. Select the comparator **= (equals)**.
       3. Enter the INSTANCE_ID of a VM.
     * Filter for the `ops-agent-health` log: 
       1. Select the resource label **log**.
       2. Select the comparator **= (equals)**.
       3. Select the value **ops-agent-health**.



####  Create an alerting policy for the `log_entry_count` metric

To create an alerting policy that monitors the value of the `log_entry_count` metric for log pings from a specific VM, do the following: 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels.
  3. From the **Alerting** page, select **Create policy**.
  4. In the **Select a metric** field, do the following: 
     1. Enter `log entries`.
     2. For the **Resource type** , select **VM Instance**.
     3. For the **Metric category** , select **Logs-based metrics**.
     4. For the **Metric** , select **Log entries**.
     5. Select **Apply**.
  5. In the **Filter** field, add the following filters: 
     * Filter for a specific VM's instance ID: 
       1. Select the resource label **instance_id**.
       2. Select the comparator **= (equals)**.
       3. Enter the INSTANCE_ID of a VM.
     * Filter for the `ops-agent-health` log: 
       1. Select the resource label **log**.
       2. Select the comparator **= (equals)**.
       3. Select the value **ops-agent-health**.
  6. In the **Transform data** section, select the following: 
     * For the **Rolling window** field, select **10 min**. To detect missing log entries over a longer period, enter a larger value.
     * For the **Rolling window function** field, select **delta**.
  7. Click **Next**.
  8. The settings in the **Configure alert trigger** page determine when the alert is triggered. Complete this page with the settings in the following table.  
**Configure alert trigger** page  
Field |   
Value  
---|---  
**`Condition type`** | `Threshold`  
**`Alert trigger`** | `Any time series violates`  
**`Threshold position`** | `Below threshold`  
**`Threshold value`** | `1`  
**`Advanced Options: Retest window`** | `No retest`  
  9. Click **Next**.
  10. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  11. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  12. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  13. Click **Alert name** and enter a name for the alerting policy.
  14. Click **Create Policy**.



For more information, see [Alerting policies](https://docs.cloud.google.com/monitoring/alerts).

## Agent diagnostics tool for VMs

The agent diagnostics tool gathers critical local debugging information from your VMs for all the following agents: Ops Agent, legacy Logging agent, and legacy Monitoring agent. The debugging information includes things like project info, VM info, agent configuration, agent logs, agent service status, information that typically requires manual work to gather. The tool also checks the local VM environment to ensure it meets certain requirements for the agents to function properly, for example, network connectivity and required permissions.

**When filing a customer case for an agent on a VM, run the agent diagnostics tool and attach the collected information to the case. Providing this information reduces the time needed to troubleshoot your support case. Before you attach the information to the support case, redact any sensitive information like passwords.**

The agent diagnostics tool must be run from inside the VM, so you will typically need to SSH into the VM first. The following command retrieves the agent diagnostics tool and executes it:

**Linux**
    
    
    curl -sSO https://dl.google.com/cloudagents/diagnose-agents.sh
    sudo bash diagnose-agents.sh
    

**Windows**
    
    
    (New-Object Net.WebClient).DownloadFile("https://dl.google.com/cloudagents/diagnose-agents.ps1", "${env:UserProfile}\diagnose-agents.ps1")
    Invoke-Expression "${env:UserProfile}\diagnose-agents.ps1"
    

Follow the output of the script execution to locate the files that include the collected info. Typically you can find them in the `/var/tmp/google-agents` directory on Linux and in the `$env:LOCALAPPDATA/Temp` directory on Windows, unless you have customized the output directory when running the script.

For detailed information, examine the `diagnose-agents.sh` script on Linux or `diagnose-agents.ps1` script on Windows.

## Agent diagnostics tool for automatic installation policies

If an attempt to install the Ops Agent by using an Ops Agent OS policy fails, you can use the diagnostics script described in this section for debugging. For example, you might see one of the following cases:

  * The Ops Agent installation fails when you used the **Install Ops Agent for Monitoring and Logging** checkbox to [install the Ops Agent during VM creation](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-agent-vm-creation).
  * The agent status on the Cloud Monitoring **VM instances** dashboard or the **Observability** tab on a Compute Engine VM details page stays in the **Pending** state for more than 10 minutes. A prolonged **Pending** status might indicate one of the following:

    * A problem applying the policy.
    * A problem in the actual installation of the Ops Agent.
    * A connectivity problem between the VM and Cloud Monitoring.

For some of these issues, the general agent-diagnostics script and health checks might also be helpful.




To run the policy-diagnostics script, run the following commands:
    
    
    curl -sSO https://dl.google.com/cloudagents/diagnose-ui-policies.sh
    bash diagnose-ui-policies.sh VM_NAME VM_ZONE
    

**Note:** You must have the `roles/osconfig.osPolicyAssignmentViewer` role to run this script.

This script shows information about affected VMs and related automatic installation policies.

**When filing a customer case for an agent on a VM, run the agent diagnostics tools and attach the collected information to the case. Providing this information reduces the time needed to troubleshoot your support case. Before you attach the information to the support case, redact any sensitive information like passwords.**

## Agent self logs

If the agent fails to ingest logs to Cloud Logging, then you might have to inspect the agent's logs locally on the VM for troubleshooting. You can also [use log rotation](https://docs.cloud.google.com/monitoring/agent/ops-agent/rotate-logs) to manage the agent's self logs.

The location of the agent's self log files differs for agents [ installed by using VM Extension Manager extension policies](https://docs.cloud.google.com/monitoring/agent/ops-agent/agent-vmem-policies) and for agents installed by all other methods. See the following sections:

  * For an Ops Agent installed by any method except extension policies
  * For an Ops Agent installed by using extension policies



### Not installed by VM Extension Manager

**Linux**

**Note:** Everything in the Linux section has been automated as part of the diagnostic tool. To perform the log inspection manually, continue with the following steps.

To inspect self logs that are written to `Journald`, run the following command:
    
    
    journalctl -u google-cloud-ops-agent*
    

To inspect the self logs that are written to the disk by the logging module, run the following command:
    
    
    vim -M /var/log/google-cloud-ops-agent/subagents/logging-module.log
    

**Windows**

To inspect self logs that are written to `Windows Event Logs`, run the following command:
    
    
    Get-WinEvent -FilterHashtable @{ Logname='Application'; ProviderName='google-cloud-ops-agent*' } | Format-Table -AutoSize -Wrap
    

To inspect the self logs that are written to the disk by the logging module, run the following command:
    
    
    notepad "C:\ProgramData\Google\Cloud Operations\Ops Agent\log\logging-module.log"
    

To inspect the logs from the `Windows Service Control Manager` for Ops Agent services, run the following command::
    
    
    Get-WinEvent -FilterHashtable @{ Logname='System'; ProviderName='Service Control Manager' } | Where-Object -Property Message -Match 'Google Cloud Ops Agent' | Format-Table -AutoSize -Wrap
    

### Installed by VM Extension Manager

**Linux**

To inspect the self logs that are written to the disk by the logging module, run the following command:
    
    
    vim -M /var/lib/google-guest-agent/INSTANCE_ID/agent_state/plugins/ops-agent/log/google-cloud-ops-agent/subagents/logging-module.log
    

**Windows**

To inspect self logs that are written to `Windows Event Logs`, run the following command:
    
    
    Get-WinEvent -FilterHashtable @{ Logname='Application'; ProviderName='google-cloud-ops-agent*' } | Format-Table -AutoSize -Wrap
    

To inspect the self logs that are written to the disk by the logging module, run the following command:
    
    
    notepad "C:\ProgramData\Google\Compute Engine\google-guest-agent\INSTANCE_ID\agent_state\plugins\ops-agent\logging-module.log"
    

## View metric usage and diagnostics in Cloud Monitoring

The Cloud Monitoring **Metrics Management** page provides information that can help you control the amount you spend on billable metrics without affecting observability. The **Metrics Management** page reports the following information: 

  * Ingestion volumes for both byte- and sample-based billing, across metric domains and for individual metrics.
  * Data about labels and cardinality of metrics.
  * Number of reads for each metric.
  * Use of metrics in alerting policies and custom dashboards.
  * Rate of metric-write errors.



You can also use the **Metrics Management** page to [exclude unneeded metrics](https://docs.cloud.google.com/monitoring/docs/metrics-management#exclude-metrics), eliminating the cost of ingesting them. 

To view the **Metrics Management** page, do the following: 

  1. In the Google Cloud console, go to the  query_stats **Metrics management** page: 

[Go to **Metrics management**](https://console.cloud.google.com/monitoring/metrics-management)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar, select your time window. By default, the **Metrics Management** page displays information about the metrics collected in the previous one day.



For more information about the **Metrics Management** page, see [View and manage metric usage](https://docs.cloud.google.com/monitoring/docs/metrics-management).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
