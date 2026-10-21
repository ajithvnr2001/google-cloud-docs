---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info/
title: Google Cloud's Agent for SAP diagnostic information \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:49.681552+00:00
---

# Google Cloud's Agent for SAP diagnostic information  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  Google Cloud's Agent for SAP diagnostic information Stay organized with collections  Save and categorize content based on your preferences. 

For problems that are related to **version 3.15 (latest)** of Google Cloud's Agent for SAP, provide the following diagnostic information to Cloud Customer Care as soon as you can:

  * A complete and detailed description of the problem.
  * The support bundle for the agent.
  * The most recent data collected by the agent.
  * The configuration file for the agent.
  * The log file for the agent.



## Detailed description of the problem

Provide a complete and detailed description of the problem, including the version of the agent, and the date and time when the problem occurred.

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




## Support Bundle

Support bundle is a collection of information from Google Cloud's Agent for SAP, that helps Customer Care in providing you troubleshooting support. This feature is available for Google Cloud's Agent for SAP version 2.1 or later.

From version 3.4 of the agent, you can upload the output of the `supportbundle` command by using the `result-bucket` option. For this, you need to make sure that the service account used by the agent has the following IAM permission: `storage.objects.create`.

### What the support bundle contains

  * The agent's log and configuration files.

From version 3.0 of the agent, this includes the logs and configuration files related to the [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) and [disk snapshot](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery) features of the agent.

  * SAP HANA traces and topology files for the given hostname and SID.

  * Cloud Storage Backint agent for SAP HANA configuration file and logs.

  * For a high-availability (HA) cluster on RHEL, when you specify `pacemaker-diagnosis="true"`, the output of the `sosreport` is saved in the following directory: `/tmp/google-cloud-sap-agent/pacemaker-TIMESTAMP`. If the execution of the `sosreport` command fails, then the output of `crm_report` is saved in the specified directory.

  * For an HA cluster on SUSE, when you specify `pacemaker-diagnosis=true`, the output of the `hb_report` and `supportconfig` utilities is saved in the following directory: `/tmp/google-cloud-sap-agent/pacemaker-TIMESTAMP`. If the execution of these utilities fails, then the output of the `hb_report` and `crm_report` are saved in the specified directory.

  * The `/var/log/messages` file, which helps by providing useful information about your Linux system operations.

  * From version 3.8 of the agent, the `sapdiscovery.json` file is included by default. The file contains information about the SAP products and related components that are running on the compute instance. This information provides Customer Care better context about the role and configuration of your SAP system.

To let the agent collect this information, you need to satisfy the following requirements:

    * Specify `"log_to_cloud": true` in the agent's configuration file.
    * Grant the `logging.logEntries.list` IAM permission to the service account that the agent uses.
  * From version 3.8 of the agent, when you specify the `metrics` option, the bundle includes information about the occurrences of [predefined SAP events](https://docs.cloud.google.com/sap/docs/show-sap-events-on-dashboard#supported_sap_event_types) and the changes in values of [Process Monitoring metric](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#process_monitoring_metrics) and [SAP HANA Monitoring metric](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana#sap_hana_monitoring_metrics) for a specific time period.

    * To let the agent collect information about the occurrences of [predefined SAP events](https://docs.cloud.google.com/sap/docs/show-sap-events-on-dashboard#supported_sap_event_types) from Cloud Logging logs, you need to satisfy the following requirements: 
      * Specify `"log_to_cloud": true` in the agent's configuration file.
      * Grant the `logging.logEntries.list` IAM permission to the service account that the agent uses.
    * To let the agent collect information about changes in metric values from Cloud Monitoring, you need to satisfy the following requirements: 
      * Specify `"send_metrics_to_monitoring": true` in the agent's configuration file.
      * Grant the following IAM permission to the service account that the agent uses: `monitoring.metricDescriptors.get`, `monitoring.metricDescriptors.list`, `monitoring.monitoredResourceDescriptors.get`, `monitoring.monitoredResourceDescriptors.list`, and `monitoring.timeSeries.list`.
    * The time period with which the agent filters the Cloud Logging logs and Cloud Monitoring entries is determined by the behavior of the following options: 
      * `timestamp`: the timestamp, in the `YYYY-MM-DD HH:MM:SS` format, around which you want to collect information about occurrences of the predefined SAP event types and changes in metric values. The default value is the time when you run the `supportbundle` command.
      * `before-duration`: the number of seconds before `timestamp` during which the agent searches for the occurrences of predefined SAP events and changes in metric values. The default value is 3600 seconds.
      * `after-duration`: the number of seconds after `timestamp` during which the agent searches for the occurrences of predefined SAP events and changes in metric values. The default value is 1800 seconds.
    * The collected information is organized into folders that contain JSON files for each SAP event type that occurred and each metric that changed its value. The following is an example of how the output appears:
          
          supportbundle/
          |--- process_metrics/
            |--- pm_sap_control_cpu_utilization.json
            |--- pm_sap_control_memory_utilization.json
          |--- hana_monitoring_metrics/
            |--- hm_sap_hanamonitoring_disk_readtime.json
            |--- hm_sap_hanamonitoring_disk_writetime.json
          |--- sap_events/
            |--- se_HA_Availability.json
            |--- se_HA_Replication.json




### Generate support bundle

To generate the support bundle for an agent instance running on Linux, run the following command on your compute instance:
    
    
    sudo /usr/bin/google_cloud_sap_agent supportbundle --sid="SID" --instance-numbers="INSTANCE_NUMBERS" --hostname="HOST_NAME" [--pacemaker-diagnosis="BOOLEAN_VALUE"] [--result-bucket="BUCKET_NAME"] [--metrics] [--timestamp="TIMESTAMP"] [-before-duration=BEFORE_DURATION] [-after-duration=AFTER_DURATION]

Replace the following:

  * `SID`: your SAP system ID.
  * `INSTANCE_NUMBERS`: the SAP instance numbers for which you want to generate the support bundle. 

To specify multiple instance numbers, separate them using a space. For example, `00 11 22`. When you specify two or more SAP instance numbers, the command generates one combined support bundle for the specified instances.

  * `HOST_NAME`: the name of the host on which you run the command.
  * `BOOLEAN_VALUE`: the value `true` or `false`, which determines if the Pacemaker related diagnosis is performed or not; the default value is `false`.
  * `BUCKET_NAME`: the name of the Cloud Storage bucket where you want to upload the output of the `supportbundle` command.
  * `TIMESTAMP`: the timestamp, in the `YYYY-MM-DD HH:MM:SS` format, around which you want to collect information about occurrences of the predefined SAP event types and changes in metric values. The default value is the time when you run the `supportbundle` command.
  * `BEFORE_DURATION`: the number of seconds before value of the `timestamp` option during which the agent searches for the occurrences of predefined SAP events and changes in metric values. The default value is 3600 seconds.
  * `AFTER_DURATION`: the number of seconds after value of the `timestamp` option during which the agent searches for the occurrences of predefined SAP events and changes in metric values. The default value is 1800 seconds.



## Most recent data collected by the agent

Provide the most recent data collected by the agent. Save the most recent data collected by the agent to a file and attach the file to your support case.

To view the most recent data collected by the agent, complete the following steps:

###  Linux 

  1. Use SSH to connect to the host machine.
  2. Run the following command: 
         
         curl http://localhost:18181/




###  Windows 

  1. Use RDP to connect to the host machine.
  2. As an administrator, run the following command from PowerShell: 
         
         "(Invoke-WebRequest -Uri 'http://localhost:18181').RawContent"




## Configuration file

After removing credentials such as the SAP HANA database username and passwords, provide the configuration file for Google Cloud's Agent for SAP.

To find the configuration file for the agent, navigate to the following path:

###  Linux 
    
    
    /etc/google-cloud-sap-agent/configuration.json

###  Windows 
    
    
    C:\Program Files\Google\google-cloud-sap-agent\conf\configuration.json

## Log file

Provide the log file for Google Cloud's Agent for SAP.

To find the log file for the agent, navigate to the following path:

###  Linux 
    
    
    /var/log/google-cloud-sap-agent.log

###  Windows 
    
    
    C:\Program Files\Google\google-cloud-sap-agent\logs\google-cloud-sap-agent.log

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español – América Latina
  * Français
  * Português – Brasil
  * 中文 – 简体
  * 日本語
  * 한국어


