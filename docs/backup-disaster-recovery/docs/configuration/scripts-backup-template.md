---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/scripts-backup-template/
title: Add scripts to a backup template in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:49.445922+00:00
---

# Add scripts to a backup template in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/scripts-backup-template/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add scripts to a backup template in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page explains how to add scripts to a backup template. It describes the different phases that a script executes during a backup job.

You can write your scripts and run them to perform an action at the start of a backup job, during it, or after it's completed. These are also called pre and post scripts.

## Scripts location

A script folder is created automatically during agent installation where the file system or database that needs protection is running. You need to place the scripts in the following folders in order to execute them:

  * For Windows host: `\Program Files\Google Cloud Backup and DR\scripts`
  * For Linux host: `/act/scripts` and set the script to executable (chmod 755 *.sh)



## Script phases

Scripts execute in the following phases. If your script isn't executing, check if it is in the scripts folder.

  * **INIT** : This phase starts when the backup/recovery appliance connects to the agent, In this phase, the job is initialized and the credentials are verified.
  * **PRE** : This phase starts just before the major operation of the job. For snapshots, this phase starts before the application is frozen. For mount type jobs, this is after devices are mapped to the host but before agent based operations like rescan, import, and mounting of file systems is started.
  * **POST** : This phase starts immediately after the major operation of the job is completed. For backup type jobs, this is after the application is unfrozen. For mount type jobs this phase starts after all import, mount, or bring applications online operations are complete.
  * **FINAL** : This phase is the end of the job. Unless the script returns a non-zero code that causes the job to fail, the job is complete.
  * **ABORT** : This phase handles aborted jobs when they fail.



## Example: scripts

The following example shows how to run a host side script at various phases of the backup job process. It has five scripts that output the date or time, app name (file system or database name), job type, job name, log retention value in days, and text to indicate the phase of the backup job that is processing.
    
    
        ```sh
        $ cat /act/scripts/init.sh
            #!/bin/sh
            if [ "${ACT_JOBTYPE}" = "logbackup" ]; then
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_ARCHIVELOG_BACKUP JobPhase:INIT" >> /tmp/backup_status.log
            else
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_INCREMENTAL_BACKUP JobPhase:INIT" >> /tmp/backup_status.log
            fi
    
            $ cat /act/scripts/pre.sh
            #!/bin/sh
            if [ "${ACT_JOBTYPE}" = "logbackup" ]; then
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_ARCHIVELOG_BACKUP JobPhase:PRE" >> /tmp/backup_status.log
            else
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_INCREMENTAL_BACKUP JobPhase:PRE" >> /tmp/backup_status.log
            fi
    
            $ cat /act/scripts/post.sh
            #!/bin/sh
            if [ "${ACT_JOBTYPE}" = "logbackup" ]; then
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_ARCHIVELOG_BACKUP JobPhase:POST" >> /tmp/backup_status.log
            else
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_INCREMENTAL_BACKUP JobPhase:POST" >> /tmp/backup_status.log
            fi
    
            $ cat /act/scripts/fini.sh
            #!/bin/sh
            if [ "${ACT_JOBTYPE}" = "logbackup" ]; then
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_ARCHIVELOG_BACKUP JobPhase:FINAL" >> /tmp/backup_status.log
            else
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_INCREMENTAL_BACKUP JobPhase:FINAL" >> /tmp/backup_status.log
            fi
    
            $ cat /act/scripts/abort.sh
            #!/bin/sh
            if [ "${ACT_JOBTYPE}" = "logbackup" ]; then
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_ARCHIVELOG_BACKUP JobPhase:ABORT" >> /tmp/backup_status.log
            else
              echo `date` "${ACT_JOBNAME}_${ACT_APPNAME}_INCREMENTAL_BACKUP JobPhase:ABORT" >> /tmp/backup_status.log
            fi
            ```
    

In the preceding example, `ACT_JOBTYPE = logbackup` indicates the job being run is a log backup task, rather than a full database backup task.

You might not need to run all five phases to achieve your chosen log output. You can use only the init and final phases to indicate the start and end of the backup process.

You can also customize the scripts to perform other tasks, such as stopping a service or running other commands.

## Add scripts to a backup template

Use the following instructions to add the scripts to a backup template.

  1. Click **Backup plans** and select **Templates** from the drop-down list.
  2. Select a template that includes an OnVault policy. The **Templates** page opens with the selected backup template.
  3. In the **Policies** area of the **Templates** page, click **+Add** next to **Snapshot**.
  4. Click **Advanced Policy Settings**.
  5. Scroll to **Script Name** , then copy and paste the following script:
         
         path=init.sh:phase=init;path=pre.sh:phase=pre;path=post.sh:phase=post;path=fini.sh:phase=final:timeout=300;path=abort.sh:phase=abort
         

**Note:** The use of timeout and arguments is not mandatory, but they can be used for each different phase where required. We added a timeout of 300 seconds to the final phase for this example, but you are able to add timeout values to any phase of the script. If the timeout is reached and the script is still running, the script will exit. The default timeouts for pre, post, and final scripts are 60 seconds, while init scripts have a default timeout of 120 seconds.
  6. Click **Save Changes**.

  7. [Run an on-demand job](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs#run).

The output is displayed for two different databases. One is a log backup job, and one is an incremental snapshot.

$ cat /tmp/backup_status.log Wed Nov 22 06:11:49 UTC 2023 Job_0275501_ORCLCDB_ARCHIVELOG_BACKUP JobPhase:INIT Wed Nov 22 06:13:52 UTC 2023 Job_0275501_ORCLCDB_ARCHIVELOG_BACKUP JobPhase:PRE Wed Nov 22 06:15:01 UTC 2023 Job_0275501_ORCLCDB_ARCHIVELOG_BACKUP JobPhase:POST Wed Nov 22 06:15:01 UTC 2023 Job_0275501_ORCLCDB_ARCHIVELOG_BACKUP JobPhase:FINAL Wed Nov 22 06:18:00 UTC 2023 Job_0275637_SMALL_INCREMENTAL_BACKUP JobPhase:INIT Wed Nov 22 06:20:15 UTC 2023 Job_0275637_SMALL_INCREMENTAL_BACKUP JobPhase:PRE Wed Nov 22 06:22:06 UTC 2023 Job_0275637_SMALL_INCREMENTAL_BACKUP JobPhase:POST Wed Nov 22 06:22:06 UTC 2023 Job_0275637_SMALL_INCREMENTAL_BACKUP JobPhase:FINAL




## Passing environment variables into a log file

You can export the environment information from the job to the script using the environment variables in the following list that are prefixed with `ACT_`. Not all of the environment variables will be applicable to every job type.

  * `ACT_APPID`: the database ID of the application.
  * `ACT_APPNAME`: the name of the application.
  * `ACT_HOSTNAME`: the name of the host which is the target of this job.
  * `ACT_JOBNAME`: the name of the job.
  * `ACT_JOBTYPE`: a text version of the job class.
  * `ACT_LOGSMART_TYPE`: the only valid value is "db". This must be present for database logs to be captured.
  * `ACT_OPTIONS`: the policy options that apply to this job
  * `ACT_PHASE`: a text string that describes the job phase.
  * `ACT_POLICY`: the name of the policy related to this job.
  * `ACT_POLICYOPT_logbackupretention`: the number of days of retention for log backup jobs. This only appears in database log backup jobs.
  * `ACT_PROFILE`: the name of the profile.
  * `ACT_SCRIPT_TMOUT`: the superscripting timeout. If the response is not received within the timeout value (default 60 seconds), then the script will fail.
  * `ACT_SOURCEHOST`: the name of the host that was the source for this application.
  * `ACT_TEMPLATE`: the name of the template related to the job.
  * `ACT_TIMEOUT`: the defined duration of the script, in seconds. If the script does not complete within the timeout period, the job will fail.
  * `ACT_VOLUMES`: for generic applications, the list of volumes that are configured for backup. If you need help learning the possible environment variables you can use, add this line to your script.
        
        echo printenv >> /tmp/backup_status.log
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
