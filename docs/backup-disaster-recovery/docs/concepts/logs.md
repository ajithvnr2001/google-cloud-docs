---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/logs/
title: Backup/recovery appliance debug logs \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:40.441565+00:00
---

# Backup/recovery appliance debug logs  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup/recovery appliance debug logs Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR generates many logs that are useful for troubleshooting. This section describes the log types and how they work together.

## Download logs from the backup/recovery appliance

You can use the **Downloads** tab in the Logs section of the **Appliance Configuration** to download log files. Each downloaded log is bundled as a zip file in the download folder. You can then extract the downloaded log files and use a text editor to view the contents of each log.

Use these instructions to download logs from backup/recovery appliances:

  1. In the appliance management console, select **Manage** > **Appliances**.
  2. Right-click the appliance and select **Configure Appliance** to open the **Appliance Configuration** page.
  3. From the left panel, select **Configuration** > **Logs**.

The **Logs** page appears, listing the logs that you can download.

  4. By default, the backup/recovery appliance downloads logs from the past 3 days (starting with the current date). To specify a particular date range from which you want to download logs, click the calendar icon and select a start date in the **From Date** field and an end date in the **To Date** fields.

  5. Check the boxes of the logs to download. See Log types are detailed in what you can learn from logs. You can also select **ALL** in the upper right corner to download all logs.

  6. Click **Download Logs**.




You can also [view the event logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events) created on backup/recovery appliances in Cloud Logging by using the Google Cloud console and the gcloud CLI CLI.

## Download agent logs

Backup and DR agent logs are a great tool for troubleshooting. You don't need access to the host where the agent is running to download the agent logs; you can use the same method used to download backup/recovery appliance logs.

Use these instructions to download agent logs from one of your hosts:

  1. In the appliance management console, select **Manage** > **Appliances**.
  2. Right-click the appliance and select **Configure Appliance** to open the **Appliance Configuration** page.
  3. From the left panel, select **Configuration** > **Logs**.

The **Logs** page appears, listing the logs that you can download.

  4. By default, the backup/recovery appliance downloads logs from the past three days (starting with the current date). To specify a particular date range from which you want to download logs, click the calendar icon and select a start date in the **From Date** field and an end date in the **To Date** fields.

  5. Select the agent checkbox from log types.

  6. To download logs from the Backup and DR agent installed on a specific host, click the **Select Hosts** drop-down and choose from the list of available hosts.

  7. Click **Download Logs**.


**Note:** The UDSAgent.log log file can be found on Linux and Windows operating systems and aamservice.log on Windows operating system at these paths: 

  * On a Linux host: `/var/act/Log/`
  * On a Windows host: `C:\Program Files\Google Cloud Backup and DR\log`
  * To retrieve AAM service log path on a Windows host: `C:\Program Files\Google Cloud Backup and DR\Log\aamservice.log`



## Log types

The following table lists the different log types and log details:

Log types | What the Logs Include  
---|---  
agent | The Backup and DR agent log includes information related to the server where it is installed, as well as details of all requests received from an appliance and the execution of those requests, such as backup and recovery jobs.  
appliance | Primary trace logs for reviewing failovers and node reboots, ethernet status, and more on backup/recovery appliances  
cloudbacker | OnVault details  
database | The internal database  
enginemgr | Running all jobs  
flasher | Snapshot details  
install | Events during the installation process  
network | Routing and DHCP information to troubleshoot network connectivity  
omd | Creation and deletion of vDisks before creating snapshots  
patch | Events during the patch update process  
psrv | Communications between internal components related to user tasks and scheduled processes  
streamsnapd | Disk to remote disk replication operations  
supportbundle | Output of several reports with details of resource consumption, storage consumption, job history, overall health, and more, to be used as a foundation for troubleshooting of issues  
systemlog | CLI command history   
Events for the creation of VDisks.   
Operating system messages file.  
  
tomcat | Communications with the APIs and web server. The sequence number increases as you go back in time.  
udppm | Scheduling of jobs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
