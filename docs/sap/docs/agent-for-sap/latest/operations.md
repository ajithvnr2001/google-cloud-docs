---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations/
title: Google Cloud's Agent for SAP operations guide \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:48.451922+00:00
---

# Google Cloud's Agent for SAP operations guide  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Google Cloud's Agent for SAP operations guide Stay organized with collections  Save and categorize content based on your preferences. 

This guide covers operational considerations and procedures for running **version 3.15 (latest)** of Google Cloud's Agent for SAP on Compute Engine instances and Bare Metal Solution servers.

## Understand the agent lifecycle

When managing the operations of Google Cloud's Agent for SAP, it's helpful to understand what the agent does. In general, here's how it works:

  * You must install Google Cloud's Agent for SAP on each Compute Engine instance or Bare Metal Solution server that hosts SAP systems. The agent runs as a Linux service or a Windows service.
  * On Compute Engine instances, the agent combines monitoring data from Monitoring and the Compute Engine APIs.
  * On Bare Metal Solution servers, for collection of only SAP Host Agent metrics, the agent does not access the Google Cloud APIs.
  * The SAP Host Agent polls Google Cloud's Agent for SAP for its cached data, over HTTP. It aggregates the SAP Host Agent metrics, reports them, and stores them in the SAP NetWeaver database.
  * The SAP transaction `ST06` or the `saposcol` command line interface displays the aggregated SAP Host Agent metrics.
  * You can view the SAP Host Agent metrics from Google Cloud's Agent for SAP by running a command in a terminal window.



## Verify that the agent is running

After installing the agent or restarting the agent, you can verify that the agent is running as expected.

To check whether the agent is running, follow these steps:

###  Linux 

  1. Establish an SSH connection with your Bare Metal Solution server or Compute Engine instance. 

  2. Run the following command: 
         
         systemctl status google-cloud-sap-agent

If the agent is functioning properly, then the output contains `active (running)`. For example: 
         
         google-cloud-sap-agent.service - Google Cloud Agent for SAP
         Loaded: loaded (/usr/lib/systemd/system/google-cloud-sap-agent.service; enabled; vendor preset: disabled)
         Active: **active (running)** since Fri 2022-12-02 07:21:42 UTC; 4 days ago
         Main PID: 1337673 (google-cloud-sa)
         Tasks: 9 (limit: 100427)
         Memory: 22.4 M (max: 1.0G limit: 1.0G)
         CGroup: /system.slice/google-cloud-sap-agent.service
                └─1337673 /usr/bin/google-cloud-sap-agent
         




###  Windows 

  1. Use RDP to connect to the Compute Engine instance.

  2. As an administrator, run the following command from PowerShell: 
         
         $(Get-Service -Name 'google-cloud-sap-agent' -ErrorAction Ignore).Status

If the agent is running, then the status shows `Running`.



If Google Cloud's Agent for SAP isn't running, then restart the agent.

## Check the version of the agent

After installing or restarting Google Cloud's Agent for SAP, you can check the version of the agent.

To check the version of your agent, complete the following steps:

###  Linux 

For RHEL, follow these steps:

  1. Use SSH to connect to the host Compute Engine instance or Bare Metal Solution server.
  2. Run the following command: 
         
         yum info google-cloud-sap-agent




For SLES, follow these steps:

  1. Use SSH to connect to the host Compute Engine instance or Bare Metal Solution server.
  2. Run the following command: 
         
         zypper info google-cloud-sap-agent




###  Windows 

  1. Use RDP to connect to the host Compute Engine instance or Bare Metal Solution server.
  2. As an administrator, run the following command from PowerShell: 
         
         googet installed google-cloud-sap-agent




## List all available versions of the agent

To list all the available versions of Google Cloud's Agent for SAP:

**Note:** The following commands work only for installations done using `google-cloud-sap-agent` RPM repository.

###  RHEL 

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Run the following command:
         
         sudo yum list --showduplicates google-cloud-sap-agent




###  SLES 

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Run the following command:
         
         sudo zypper search -s -t package -r google-cloud-sap-agent google-cloud-sap-agent




## Verify that SAP Host Agent is receiving metrics

To verify that the infrastructure metrics are collected by Google Cloud's Agent for SAP and sent correctly to the SAP Host Agent, follow these steps:

  1. In your SAP system, enter transaction `ST06`.
  2. In the overview pane, check the availability and content of the following fields for the correct end-to-end setup of the SAP and Google monitoring infrastructure:

     * **Cloud Provider** : `Google Cloud Platform`
     * **Enhanced Monitoring Access** : `TRUE`
     * **Enhanced Monitoring Details** : `ACTIVE`



## View the SAP Host Agent metrics

After installing or updating the configuration of Google Cloud's Agent for SAP, you can view the collected SAP Host Agent metrics.

To view the SAP Host Agent metrics collected by Google Cloud's Agent for SAP, follow these steps:

###  Linux 

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Run the following command: 
         
         curl http://localhost:18181

If the metrics are available, then you should receive an XML output containing information about your system. For example:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <metrics>
           <metric category="cpu" context="vm" type="double" unit="Percent" last-refresh="1670422670" refresh-interval="60">
           <name>VM Processing Power Consumption</name>
           <value>0.0</value>
           </metric>




###  Windows 

  1. Use RDP to connect to the Compute Engine instance.

  2. As an administrator, run the following command from PowerShell: 
         
         (Invoke-WebRequest -Uri 'http://localhost:18181').RawContent

If the metrics are available, you should see a XML output containing information about your system. For example:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
           <metrics>
           <metric category="cpu" context="vm" type="double" unit="Percent" last-refresh="1670422528" refresh-interval="60">
           <name>VM Processing Power Consumption</name>
           <value>10.0</value>
           </metric>




## View the other metrics

After you update the configuration of Google Cloud's Agent for SAP to collect the Process Monitoring metrics or the SAP HANA monitoring metrics, we recommend that you view them to verify that the agent is collecting the metrics as expected.

You can view the metrics and information collected by Google Cloud's Agent for SAP in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) by completing the following steps:

  1. In the Google Cloud console, go to the Monitoring **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Select the **Configuration** tab.

  3. Expand the **Select a metric** menu.

  4. In the **Resources** menu, select **VM instance**.

  5. In the **Metric category** menu, select **sap**.

  6. In the **Metric** menu, select `metric: workload.googleapis.com/sap/service/active` or any of the new metrics to chart.

  7. Click **Apply**.




You should see a chart with the time series metric values.

**Note:** Any missing metrics indicates that no metrics were collected during the searched timeframe and therefore excluded from the filtered list.

## Restart the agent

Up to version 3.6, if the agent stops working or you update its configuration, then you need to restart the agent.

From version 3.7, you need not restart the agent for any configuration updates because the changes are automatically picked by the agent within the next 30 seconds.

To manually restart the agent, select your operating system, and then follow the steps:

###  Linux 

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Run the following command: 
         
         sudo systemctl restart google-cloud-sap-agent
         




###  Windows 

  1. Establish an RDP connection with your host host Compute Engine instance or Bare Metal Solution server.

  2. As an administrator, run the following command from PowerShell: 
         
         Restart-Service -Name 'google-cloud-sap-agent' -Force
         




## Disable or enable the agent

To enable proper monitoring, the `systemd` service of Google Cloud's Agent for SAP on your compute instance must be running at all times. However, if you're required to disable or stop the agent on your Linux based compute instance, then run the following command:
    
    
    sudo /usr/bin/google_cloud_sap_agent service -disable

To enable and start the agent's `systemd` service on your Linux based compute instance:
    
    
    sudo /usr/bin/google_cloud_sap_agent service -enable

When you disable or enable the agent's `systemd` service on Linux, the action is logged in the following file: `/var/log/google-cloud-sap-agent/service.log`.

## Upgrade to Google Cloud's Agent for SAP from other Google Cloud agents

Google Cloud's Agent for SAP is the successor to other Google Cloud agents. The following sections provide information for upgrading from these agents to version 3.15 (latest) of Google Cloud's Agent for SAP.

For instructions on installing and configuring Google Cloud's Agent for SAP, see [Choose your Google Cloud's Agent for SAP installation and configuration guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).

### Upgrading from the legacy Backint agent

To upgrade from the Cloud Storage Backint agent for SAP HANA to version 3.15 (latest), complete the following steps:

  1. Make sure that no data backups are in-progress or scheduled for the period overlapping with the upgrade.

  2. Disable automatic log backups by setting the SAP HANA parameter `enable_auto_log_backup` parameter to `no`. For instructions, see the SAP HANA document [Enable and Disable Automatic Log Backup](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/241c0f0020b2492fb93a69a40b1b1b9a.html).

  3. Install Google Cloud's Agent for SAP. For instructions, see the [installation guide for your scenario](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).

  4. Enable the Backint feature of Google Cloud's Agent for SAP. For instructions, see [Configure Backint based backup and recovery](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery).

Enabling the Backint feature of Google Cloud's Agent for SAP automatically detects the legacy Backint agent on your host and disables it from your host machine.

  5. To create a JSON version of your existing Backint configuration text file, run the following command for each of your text files:
         
         /usr/bin/google_cloud_sap_agent configurebackint -f=PATH_TO_PARAMETERS_FILE

Replace `PATH_TO_PARAMETERS_FILE` with the path to your `PARAMETERS.txt` file.

The JSON files are created in the same location in your file system as the text files as long as Google Cloud's Agent for SAP has the permission to access those locations. While Google Cloud's Agent for SAP is capable of interpreting the Backint related parameters specified in the text file, we recommend that you use the JSON files for updating any configuration.

  6. Enable automatic log backups by setting the SAP HANA parameter `enable_auto_log_backup` parameter to `yes`. For instructions, see the SAP HANA document [Enable and Disable Automatic Log Backup](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/241c0f0020b2492fb93a69a40b1b1b9a.html).

  7. [Validate backup and recovery](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#validate_backup_and_recovery).




When you perform this upgrade, the following happen:

  * For backup and reference purposes, all installation files in the `backint-gcs` directory of legacy Backint agent are copied to `backint-gcs-old-TIMESTAMP/`. These are required in case you need to revert to using the legacy Backint agent.
  * The `backint-gcs` folder is then cleaned up to contain only those files that are required to run Google Cloud's Agent for SAP, which includes its configuration file, `parameters.json`, and the Backint configuration files such as `PARAMETERS.txt`.



For information about the mapping of the configuration parameters between the legacy Backint agent and Google Cloud's Agent for SAP, expand the following section.

#### Mapping of configuration parameters

Parameter name in legacy Backint agent | Parameter name in Google Cloud's Agent for SAP  
---|---  
`BUCKET` | `bucket`  
`DISABLE_COMPRESSION` | `compress`  
`ENCRYPTION_KEY` | `encryption_key`  
`KMS_KEY_NAME` | `kms_key`  
`MAX_GCS_RETRY` | `retries`  
`PARALLEL_FACTOR` | `parallel_streams`  
`PARALLEL_PART_SIZE` | This is not available in Google Cloud's Agent for SAP.  
`RATE_LIMIT_MB` | `rate_limit_mb`  
`SERVICE_ACCOUNT` | `service_account_key`  
`THREADS` | `thread`  
`READ_IDLE_TIMEOUT` | `file_read_timeout_ms`  
`CHUNK_SIZE_MB` | `buffer_size_mb`  
`HTTP_READ_TIMEOUT` | This is not available in Google Cloud's Agent for SAP.  
  
### Upgrading from monitoring agent for SAP HANA

Installing version 3.15 (latest) of Google Cloud's Agent for SAP automatically detects versions of the monitoring agent for SAP HANA, disables them, and then removes them from your host machines during installation.

If this agent is detected, then its configuration is migrated to Google Cloud's Agent for SAP during its installation. For backup and reference purposes, the configuration of the monitoring agent for SAP HANA is copied to the following file:
    
    
    /etc/google-cloud-sap-agent/backup-of-hanamonitoring-configuration.yaml

#### Upgrading SSL-enabled instances

If you have configured the monitoring agent for SAP HANA to use SSL certificates for communication with your SAP HANA instances, then when you install Google Cloud's Agent for SAP, all the SAP HANA monitoring configuration except the SSL configuration are migrated to Google Cloud's Agent for SAP. In such a case, to use Google Cloud's Agent for SAP for monitoring your SAP HANA instances, you must complete the following steps:

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Open the configuration file of Google Cloud's Agent for SAP:
         
         /etc/google-cloud-sap-agent/configuration.json

  3. In the `hana_monitoring_configuration` section, set the parameter `enabled` to `true`.

  4. In the `hana_monitoring_configuration.hana_instances` section, perform the following for each SAP HANA instance that uses the TLS/SSL protocol for secure communication:

     1. Specify the parameter `enable_ssl` and set its value to `true`.

     2. Specify the parameter `host_name_in_certificate` and set the SAP HANA hostname, as specified in the TLS/SSL certificate, as its value.

     3. Specify the parameter `tls_root_ca_file` and set the path, where the TLS/SSL certificate is stored, as its value.

  5. Save the configuration file.

  6. Restart the agent for the new settings to take effect:
         
         sudo systemctl restart google-cloud-sap-agent

  7. Verify that the agent is collecting the SAP HANA monitoring metrics. For instructions, see View the other metrics.

  8. Uninstall the monitoring agent for SAP HANA.




If you experience any connection issues with your SAP HANA instances after this upgrade, then you can view the agent's logs in Logging and use the [troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting) to resolve the issue.

### Upgrading from monitoring agent for SAP NetWeaver

Installing version 3.15 (latest) of Google Cloud's Agent for SAP automatically detects versions of the monitoring agent for SAP NetWeaver.

If this agent is detected, then its configuration is migrated to Google Cloud's Agent for SAP during its installation.

## Update Google Cloud's Agent for SAP

To ensure that you have the latest version of Google Cloud's Agent for SAP, you need to check for updates periodically and update the agent.

### Check for updates

Select your operating system, and then follow these steps:

### RHEL

  1. Establish an SSH connection with your instance.
  2. Run the following command: 
         
         sudo yum check-update google-cloud-sap-agent




### SLES

  1. Establish an SSH connection with your instance.
  2. Run the following command: 
         
         sudo zypper list-updates -r google-cloud-sap-agent




### Windows

  1. Establish an RDP connection with your host Compute Engine instance.
  2. As an administrator, run the following command from PowerShell: 
         
         googet latest google-cloud-sap-agent




### Install an update

Select your operating system, and then follow the steps:

### RHEL

  1. Establish an SSH connection with your instance.
  2. Update your agent instance: 
     * (Recommended) To update to version 3.15 (latest) of the agent: 
           
           sudo yum --nogpgcheck update google-cloud-sap-agent

     * To update to a specific version of the agent: 
           
           sudo yum install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent). 




### SLES

  1. Establish an SSH connection with your instance.
  2. Update your agent instance: 
     * (Recommended) To update to version 3.15 (latest) of the agent: 
           
           sudo zypper --no-gpg-checks update google-cloud-sap-agent

     * To update to a specific version of the agent: 
           
           sudo zypper install google-cloud-sap-agent-VERSION_NUMBER.x86_64

Replace `VERSION_NUMBER` with the agent's version number that you want to install, such as `3.1-606637668`. For information about the agent versions that you can install, see [List all available versions of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#list_all_available_versions_of_the_agent). 




### Windows

  1. Establish an RDP connection with your host Compute Engine instance.
  2. To update to version 3.15 (latest) of the agent, as an administrator, run the following command from PowerShell: 
         
         googet install google-cloud-sap-agent




## Uninstall the agent

To uninstall or remove the agent from your host:

###  RHEL 

  1. Establish an SSH connection with your host.

  2. Run the following command:
         
         sudo yum remove google-cloud-sap-agent




###  SLES 

  1. Establish an SSH connection with your host.

  2. Run the following command:
         
         sudo zypper remove google-cloud-sap-agent




###  Windows 

  1. Establish an RDP connection with your host Compute Engine instance.

  2. As an administrator, run the following command from PowerShell:
         
         Remove-Service -Name 'google-cloud-sap-agent'




## View the agent's logs in Cloud Logging

By default, the logs for Google Cloud's Agent for SAP are redirected from your Compute Engine instances and Bare Metal Solution servers to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).

To view the agent's logs in Logging, follow these steps:

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs explorer](https://console.cloud.google.com/logs/query)

  2. Go the **Query** pane.

  3. From the **Resources** drop-down menu, select **Global** , and then click **Apply**.

  4. In the query editor, enter `google-cloud-sap-agent`.

  5. Click **Run query**.




You can see the logs generated by the agent instances running on all your Compute Engine instances or Bare Metal Solution servers. To filter the logs from a specific instance or server, use the filters available in the interface.

You can disable the default redirection of agent's logs that is concerned with the collection of metrics. To do so, complete the following steps:

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Open the following configuration file:
         
         /etc/google-cloud-sap-agent/configuration.json

  3. For the parameter `log_to_cloud`, update the value to `false`.

  4. Save the configuration file.

  5. [Restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart) for this change to take effect.




To disable the default redirection of the logs related to the Backint feature of Google Cloud's Agent for SAP, edit your [Backint configuration file](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#backint_configuration_file) and set the `log_to_cloud` parameter to `false`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
