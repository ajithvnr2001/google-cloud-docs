---
url: https://docs.cloud.google.com/monitoring/agent/monitoring/troubleshooting/
title: Troubleshoot the Monitoring agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.066212+00:00
---

# Troubleshoot the Monitoring agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/monitoring/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Troubleshoot the Monitoring agent Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

This page helps you diagnose problems in the installation or running of the Monitoring agent.

**Note:** If you see the following message on a Linux virtual machine (VM), then you can safely ignore it:  
`Need to set STACKDRIVER_API_KEY in /etc/sysconfig/stackdriver Not starting. Configuration error.` This message is emitted by a legacy service that is gradually being replaced. This message is benign and will eventually disappear.

## Checklist

If you are having trouble installing or using the Monitoring agent, here are some things to check:

  * If Linux installation commands result in errors, then make sure that you prefix the installation commands with `sudo`.

  * Verify that the agent service is running on your VM instance:

    * For a Windows VM, use the following PowerShell command:
          
          Get-Service -Name StackdriverMonitoring
          

Search for a service called **Stackdriver Monitoring**. If the agent isn't running, you might need to restart it.

    * For a Linux VM, use the following command:
          
          sudo service stackdriver-agent status
          

If the agent isn't running, you might need to restart it using the following command:
          
          sudo service stackdriver-agent restart
          

If the restart fails, and the log output shows "Disabled via metadata", you are likely running an image from [Google Cloud Marketplace](https://docs.cloud.google.com/marketplace), where the Monitoring agent is disabled by default. This is controlled by the `google-monitoring-enable` instance metadata key (with the value `0`). To re-enable the agent, either remove that key or set the value to `1` (see [Setting instance metadata](https://docs.cloud.google.com/compute/docs/storing-retrieving-metadata#updatinginstancemetadata)).

If the agent isn't disabled via metadata, reinstall the agent. For information about this process, see Reinstalling the Monitoring agent.

  * See if the agent has written error messages to the logs.

    * On Windows, the Monitoring agent writes messages to the Windows Event log.

    * On Linux, the Monitoring agent is a `collectd` package and logs messages to `/var/log/syslog` or `/var/log/messages`. The log messages are prefixed by `collectd` or `stackdriver-agent`:

      * If you see HTTP 429 errors, you might have exceeded your [Monitoring API quotas](https://docs.cloud.google.com/monitoring/quotas). You can see your available quota by selecting **APIs & services > Dashboard** in the Google Cloud console. Choose the Monitoring API.

      * If you see proxy problems, check that you correctly configured you HTTP proxy. The instructions are part of [Installing on Linux and Windows](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#joint-install).

      * If you see API access or authorization problems, or error messages such as "Unable to determine collectd endpoint", see the following section, Verifying project and credentials.

      * If you see "Unsupported collectd plugin/type combination" or "Unsupported collectd id" errors in the logs, you might be sending unsupported agent metrics. This can happen in the following scenarios:

        * You modified one of the agent third-party application configurations. To revert the changes, you can reinstall the configuration for the specific plug-in by following the instructions in the relevant [documentation page](https://docs.cloud.google.com/monitoring/agent/plugins). If you want to use the agent to send that metric to Monitoring, consider converting them to [user-defined metrics](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent).

        * One of the third-party application plugins is sending new metrics that are unknown to Monitoring. See the [support page](https://docs.cloud.google.com/stackdriver/docs/getting-support) for details on how to submit a request to get these metrics reviewed and [categorized](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent#how_monitoring_handles_collectd_metrics).

  * If the agent seems to be running normally, but you aren't getting data or your alerting policies aren't acting as you think they should, then you should check that the agent is sending data to the correct project. See the following section, Verifying project and credentials.




## Verifying project and credentials

If the Monitoring agent is reporting access or authorization errors, or if the agent seems to be running normally but there is no data or your alerting policies aren't working as you expect, then check that your VM instance's credentials are correct, including that they specify the correct project:

  * If you are using a Compute Engine VM instance with standard (not private-key) credentials, then it is unlikely that data is going to the wrong project, but your credentials might still be deficient. For information about credentials, see [Authorize the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization). To verify your credentials, see Verifying Compute Engine credentials.

  * If you are using private-key credentials on your Compute Engine instance, then the credentials could be invalid or they could be from the wrong project. For information about credentials, see [Authorize the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization). To verify your credentials, see Verifying private-key credentials.


If you still haven't resolved your problem, see Reinstalling the Monitoring agent. 

## Verifying Compute Engine credentials

Use the Compute Engine **VM instances** page of the Google Cloud console to verify that your Compute Engine VM instance has adequate credential for the Monitoring agent. The credentials are typically added in the default service account of all new Compute Engine VM instances, but it is possible to overwrite those defaults when creating an instance.

In the Google Cloud console, go to the **VM instances** page: 

[Go to **VM instances**](https://console.cloud.google.com/compute/instances)

If you use the search bar to find this page, then select the result whose subheading is **Compute Engine**.

  1. If necessary, change the current Google Cloud project to be the one associated with your Compute Engine VM instance. For example, if you are prompted to **Enable billing** , then it means the current project doesn't have any Compute Engine VM instances in it.
  2. In the **VM Instances** page, click the name of your VM instance. The detail page for your VM instance appears.
  3. In the **VM instance details** page, look under the **Cloud API access scopes** heading: 
     * If you see "Allow full access to all Cloud APIs," then you have adequate credentials.
     * If you see, next to **Stackdriver Monitoring API** , an older name for the Cloud Monitoring API, that you have **Write Only** or **Full** permission, then you have adequate credentials.
     * Otherwise, your instance's default service account doesn't have the credentials needed by the agent. To use the agent on your instance, you must add private-key service account credentials. For instructions, see [Adding credentials](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization).



If you have the correct default credentials, skip ahead to [Installing on Linux and Windows](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#joint-install).

## Verifying private-key credentials

To verify that valid private-key credentials are installed on your VM instance, first verify that the credentials file exists in its expected location, and then verify that the information in the credentials file is valid. Previously-valid credentials can be revoked using the **IAM & Admin > Service accounts** section of the Google Cloud console. If valid credentials aren't present, see [Adding credentials](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization) to replace the existing credentials or to add new ones.

**Caution:** Other services besides Cloud Monitoring might use private-key credentials on your instance. Replacing existing credentials might prevent other services from working.

### Are the credentials present?

To see if private-key service account credentials are on your instance, run the following Linux commands on your instance:
    
    
    sudo cat $GOOGLE_APPLICATION_CREDENTIALS
    sudo cat /etc/google/auth/application_default_credentials.json
    

If either command displays a file like the one shown below, then your instance might have valid private-key credentials. If both commands display a file, then the file denoted by `GOOGLE_APPLICATION_CREDENTIALS` is used.
    
    
    {
      "type": "service_account",
      "project_id": "{your-project-id}",
      "private_key_id": "{your-private-key-id}",
      "private_key": "{your-private-key}",
      "client_email": "{your-project-number}-{your-key}@developer.gserviceaccount.com",
      "client_id": "{your-client-id}",
      "auth_uri": "https://accounts.google.com/o/oauth2/auth",
      "token_uri": "https://accounts.google.com/o/oauth2/token",
      "auth_provider_x509_cert_url": "{x509-cert-url}",
      "client_x509_cert_url": "{client-x509-cert-url}"
    }
    

If there are no credential files present, then see [Adding credentials](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization).

### Are the credentials valid?

In the credentials file, the `project_id` field is your Google Cloud project, `client_email` identifies the service account in the project, and `private_key_id` identifies the private key in the service account. Match this information with what is shown in the **IAM & Admin > Service accounts** section of the Google Cloud console.

The credentials file isn't valid if any of the following are true:

  * You are checking a Compute Engine VM instance, but the Google Cloud project in the credentials file isn't the project that contains your instance.
  * The listed service account doesn't exist. It might have been deleted.
  * The listed service account doesn't have the right roles enabled. It should have at least `roles/monitoring.metricWriter` (Monitoring Metric Writer) for metric collection and `roles/logging.logWriter` (Logs Writer) for writing logs.
  * The private key doesn't exist. It might have been revoked.



If the service account is all right but the private key has been revoked, then you can create a new private key and copy it to your instance. Otherwise, you must create a new service account as described in the following section, [Adding credentials](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization).

### Generating new credentials

If the credentials aren't valid, take the following steps:

  1. For each connected project containing instances that need to be authorized with a private key — each project containing Compute Engine instances that were created without including the access scope `https://www.googleapis.com/auth/monitoring.write` — create a service account and generate a private key, if they don't already exist. Follow the steps below: 
     1. In the Google Cloud console, go to the _settings_ **Settings** page: 

[Go to **Settings**](https://console.cloud.google.com/monitoring/settings)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. Select the **Netric scope** tab.
     3. Identify the project containing the Compute Engine resources in question and navigate to the [Google Cloud console](https://console.cloud.google.com/). 
     4. Go to the **IAM Service Accounts** page of the Google Cloud console, select your Google Cloud project, create a new service account, and then generate a new private key for that service account. 

To perform these steps, do one of the following: 

        * Go to the **IAM Service Accounts** page, select your Google Cloud project, and then follow the steps in [ Create a service account](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#create-service-account):

[ Go to IAM Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=_)

        * Click the following button and then select your Google Cloud project:

[ Create service account and download key](https://console.cloud.google.com/iam-admin/serviceaccounts/project?project=_&createStackdriverServiceAccount)

The previous button automates the process of creating and downloading a key to your local system for the agent-specific service account. If necessary, the process also creates the required service account and ensures that the service account has the correct permissions. Agent-specific service accounts have a name similar to `stackdriver-1234@PROJECT_ID.iam.gserviceaccount.com`. You are notified of the completion of these actions with a dialog similar to the following:

![A banner notifying the user that a service account and key were created.](https://docs.cloud.google.com/static/monitoring/images/created-service-account-key.png)

**Note:** Service accounts can have a maximum of 10 keys. For more information, see [Limits](https://docs.cloud.google.com/iam/quotas#limits).
  2. Replace the private key on the instances that correspond to the service account in question.

     * On Linux, replace the private key located in `/etc/google/auth/application_default_credentials.json`. 
     * On Windows, replace the private key located in `C:\ProgramData\Google\Auth\application_default_credentials.json`. For more information, see [ Copying the private key to your instance](https://docs.cloud.google.com/monitoring/agent/monitoring/authorization#private_key_authorization). 
  3. Restart the agent

     * On Linux, run `sudo service stackdriver-agent restart`
     * On Windows, go into the service management console and restart the `Cloud Monitoring` service. 



If you have multiple projects that need new private keys, repeat this procedure for each of them.

To verify that the private key is correct, see Are the credentials present?. Specifically:

  * Read the private key JSON file on the instance, for example (on Linux): `sudo cat /etc/google/auth/application_default_credentials.json`
  * Ensure that the value of the `project_id` field matches that of the monitored project for which you just generated credentials.



## Verifying the agent data

To verify that the agent is sending metrics correctly, use the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method of the Monitoring API to look for recent time series data from the VM instance. You can call the method using the [APIs Explorer](https://docs.cloud.google.com/monitoring/api/apis-explorer) on the method's documentation page. If you don't see any data, it may be that the agent is sending data to the wrong project. To check that, see Verifying project and credentials.

Here are detailed instructions for using the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method:

  1. Determine the instance ID of the VM instance where you installed the agent:

     * Compute Engine instances: Go to the Compute Engine detail page for your instance. At the bottom of the page, click **Equivalent REST**. The ID is a 19-digit number.
  2. Go to the documentation page for the [`timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

  3. Fill out the APIs Explorer form:

     1. Set **name** to the project containing your VM instance, prefixed by `projects/`. For example, `projects/[YOUR_PROJECT_ID]`.

     2. Set **filter** to the following line to choose an agent metric from your VM instance. Copy and paste it into the APIs Explorer, and then change the VM instance ID:
            
            metric.type = "agent.googleapis.com/memory/bytes_used" AND resource.label.instance_id = "[YOUR-VM-INSTANCE-ID]"
            

     3. Set the search time interval. You want approximately a five-minute interval:

        * Set **interval.endTime** to the current GMT time, which you can find at [time.is/GMT](https://time.is/GMT). The time must be formatted like the following example. Don't enclose the time in quotation marks:
              
              2016-10-31T14:10:00Z
              

        * Set **interval.startTime** to approximately five minutes before the end time, using the same format.

     4. Leave all the other fields blank.

  4. Click **Execute**.




You should see output like the following:
    
    
    {
     "timeSeries": [
      {
       "metric": {
        "labels": {
         "state": "buffered"
        },
        "type": "agent.googleapis.com/memory/bytes_used"
       },
       "resource": {
        "type": "[INSTANCE-TYPE]",
        "labels": {
         "instance_id": "[YOUR-VM-INSTANCE-ID]",
         "zone": "[YOUR-INSTANCE-ZONE]",
         "project_id": "[YOUR-PROJECT-ID]"
        }
       },
       "metricKind": "GAUGE",
       "valueType": "DOUBLE",
       "points": [
        {
         "interval": {
          "startTime": "[START_TIME]",
          "endTime": "[END_TIME]"
         },
         "value": {
          "doubleValue": 27451392
         }
        },
        ...
    

If the API call returns any time series data from your VM instance, as shown above, then your agent is working properly and you are finished.

If you don't see any time series data, check the following:

  * If your API call results in an error message, this doesn't indicate an agent problem. Check that the APIs Explorer fields are filled properly:

    * "Invalid argument" errors probably indicate a problem with the spelling and format of the project ID, filter, or the two timestamps.

The requirements for the time-stamp arguments depend on the metric type you specify. A metric type records `GAUGE`, `DELTA`, or `CUMULATIVE` data. See [`MetricKind`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind) for more information.

For `DELTA` and `CUMULATIVE` metrics, both the start and end times are required, and the end time must be later than the start time. These kinds of metric types record changes measured over time, so the start and end times must define a non-zero interval.

    * "Not authorized" errors can mean you misspelled the project ID.

    * "Not found" errors can indicate that you've omitted the required `projects/` prefix in the "name" field.

Fix the problems and try the API call again.

  * If the API call succeeds but you see only an empty response, `{ }`, then check that your filter and time interval are correct. Errors in formatting the timestamps can result in no data being returned. If everything seems correct but you are getting no data, then the agent isn't sending metric data, or at least not to the project you are expecting it to. This might indicate a credentials problem; see Verifying private-key credentials.




## Reinstalling the Monitoring agent

Installing the most recent version of the agent can solve many problems:

  * If you are sure that the problem isn't related to credentials, you can skip ahead to [Installing on Linux and Windows](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#joint-install).

  * For a full install of the agent and any needed credentials, see [Install the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation).




## Determining which Linux VMs have the agent installed

  * Run either of the following queries to see which Linux VMs are running the agent:

    * [APIs Explorer](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list?apix_params=%7B%22name%22%3A%22projects%2F%22%2C%22aggregation.alignmentPeriod%22%3A%22120s%22%2C%22aggregation.crossSeriesReducer%22%3A%22REDUCE_NONE%22%2C%22aggregation.groupByFields%22%3A%5B%22metadata.system_labels.name%22%2C%22resource.labels.instance_id%22%5D%2C%22aggregation.perSeriesAligner%22%3A%22ALIGN_RATE%22%2C%22filter%22%3A%22resource.type%3D%5C%22gce_instance%5C%22%20metric.type%3D%5C%22agent.googleapis.com%2Fagent%2Fuptime%5C%22%20metric.label.%5C%22version%5C%22%3Dmonitoring.regex.full_match\(%5C%22stackdriver_agent%2F.*%5C%22\)%22%2C%22interval.endTime%22%3A%222020-04-28T22%3A22%3A15Z%22%2C%22interval.startTime%22%3A%222020-04-28T22%3A20%3A15Z%22%7D)

    * [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer?pageState=%7B%22xyChart%22:%7B%22dataSets%22:%5B%7B%22timeSeriesFilter%22:%7B%22filter%22:%22metric.type%3D%5C%22agent.googleapis.com%2Fagent%2Fuptime%5C%22%20resource.type%3D%5C%22gce_instance%5C%22%20metric.label.%5C%22version%5C%22%3Dmonitoring.regex.full_match\(%5C%22stackdriver_agent%2F.*%5C%22\)%22,%22minAlignmentPeriod%22:%22120s%22,%22aggregations%22:%5B%7B%22perSeriesAligner%22:%22ALIGN_RATE%22,%22crossSeriesReducer%22:%22REDUCE_COUNT%22,%22groupByFields%22:%5B%22resource.label.%5C%22instance_id%5C%22%22,%22metadata.system_labels.%5C%22name%5C%22%22,%22resource.label.%5C%22project_id%5C%22%22%5D%7D,%7B%22crossSeriesReducer%22:%22REDUCE_NONE%22%7D%5D%7D,%22targetAxis%22:%22Y1%22,%22plotType%22:%22LINE%22%7D%5D,%22options%22:%7B%22mode%22:%22COLOR%22%7D,%22constantLines%22:%5B%5D,%22timeshiftDuration%22:%220s%22,%22y1Axis%22:%7B%22label%22:%22y1Axis%22,%22scale%22:%22LINEAR%22%7D%7D,%22isAutoRefresh%22:true,%22timeSelection%22:%7B%22timeRange%22:%22custom%22,%22start%22:%222020-04-28T22:20:08.767Z%22,%22end%22:%222020-04-28T22:22:08.767Z%22%7D%7D)

Note that for each query, you must enter your project name and adjust the time bounds.




## Automatically restarting the agent

You can set up a script to check if the agent is running and then restart the agent in the event that it crashed.

For example, on Linux, you can create the following crontab entry to check the agent status every 5 minutes:
    
    
      */5 * * * * /bin/pidof stackdriver-collectd >/dev/null 2>&1 || /usr/sbin/service stackdriver-agent restart >/dev/null 2>&1
    

## Known issues

The following sections describe issues known to the Monitoring agent.

### Process data access issue (Windows)

You might see an agent error message in the Windows Event Log similar to the following:
    
    
    Read access denied for processes: Registry (84), smss.exe (264), csrss.exe (376), wininit.exe (448), csrss.exe (456), services.exe (580), NisSrv.exe (3008), MsMpEng.exe (3624), csrss.exe (7044)
    

This message indicates that the agent doesn't have access to this data on your system. To stop seeing this message, you can provide sufficient permissions to the `SYSTEM` user to read process data for the processes and services listed in the error messages. If you don't need this data, then you can safely ignore these informational messages.

### Metadata cache issues (Linux)

You might see an error message in the Linux system log file (`/var/log/syslog` on Debian / Ubuntu or `/var/log/messages` on Red Hat / CentOS / SLES) similar to the following:
    
    
    collectd[25571]: uc_update: Value too old: name = myhost/processes-all/ps_vm;
    value time = 1511345468.180; last cache update = 1511345468.180;
    write_gcm: wg_update_stats failed.
    write_gcm: uc_update returned an error.
    

These messages are harmless warnings and aren't an indication of data loss. These messages are generated by the current processes plugin implementation when there is a timestamp mismatch.

### Infinite value data point dropped issue (Linux)

You might see an error message in the Linux system log file (`/var/log/syslog` on Debian / Ubuntu or `/var/log/messages` on Red Hat / CentOS / SLES) similar to the following:
    
    
    write_gcm: can not take infinite value
    

This message indicates that a single malformed data point is dropped. This is normally harmless and can be ignored.

### Metadata key throttle issue (Linux)

You might see an error message in the Linux system log file (`/var/log/syslog` on Debian / Ubuntu or `/var/log/messages` on Red Hat / CentOS / SLES) similar to the following:
    
    
    collectd[7440]:match_throttle_metadata_keys: uc_meta_data_add returned an error
    collectd[7440]:match_throttle_metadata_keys: mtg_update_stats failed
    

This message indicates that the status update of memory throttling fails once. It is normally harmless, but could be a sign that the agent is running out of memory, especially if it occurs frequently.

### Out of Cloud Monitoring API quota issue (Linux)

You might see an error message in the Linux system log file (`/var/log/syslog` on Debian / Ubuntu or `/var/log/messages` on Red Hat / CentOS / SLES) similar to the following:
    
    
    collectd[25198]: write_gcm: Unsuccessful HTTP request 429
    

This message indicates the Cloud Monitoring API quota limit was reached. Follow the [Quota](https://docs.cloud.google.com/monitoring/quotas#more-quota) guide for information on managing your quota limit.

### High memory usage due to low `COLLECTD_INTERVAL` (Linux)

You might see high memory usage of the agent when the `COLLECTD_INTERVAL` is configured to be shorter than the default `60 seconds`, for example, `10 seconds` instead. This is a known limitation of the agent because it sends requests serially from a single thread. To mitigate this, consider reducing the `COLLECTD_INTERVAL` only for a subset of required metrics, and leave the rest of the metrics at the default interval.

### Token buffer overflow issue (Linux)

You might see an error message in the Linux system log file (/var/log/syslog on Debian / Ubuntu or /var/log/messages on Red Hat / CentOS / SLES) similar to the following:
    
    
    write_gcm: Error or buffer overflow when building auth_header
    write_gcm: wg_oauth2_get_auth_header failed.
    write_gcm: wg_transmit_unique_segment failed.
    write_gcm: wg_transmit_unique_segments failed. Flushing.
    

These messages indicate that [the monitoring agent needs to be upgraded](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#upgrade) to version `6.1.2` or higher.

### Repository changed its 'Origin' value (Linux)

You might see an error message similar to the following when upgrading the agent, installing the agent, or running `apt-get update` on Debian/Ubuntu Linux:
    
    
    E: Repository 'https://packages.cloud.google.com/apt google-cloud-monitoring-buster-all InRelease' changed its 'Origin' value from 'google-cloud-monitoring-buster' to 'namespaces/cloud-ops-agents-artifacts/repositories/google-cloud-monitoring-buster-all'
    E: Repository 'https://packages.cloud.google.com/apt google-cloud-monitoring-buster-all InRelease' changed its 'Label' value from 'google-cloud-monitoring-buster' to 'namespaces/cloud-ops-agents-artifacts/repositories/google-cloud-monitoring-buster-all'
    

This message indicates that the package repository cache may have diverged from its source. To resolve this, run the following command:
    
    
    apt-get --allow-releaseinfo-change update
    

Then, run the upgrade or install again.

## Removed agent reported by Google Cloud console as installed

After you uninstall the agent, the Google Cloud console might take up to one hour to report this change.

## Monitoring agent doesn't appear in Windows Uninstall a program list

To uninstall the Monitoring agent when it isn't listed in the Windows Control Panel's **Uninstall a program** list, run `uninstall.exe` from the directory where you installed it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
