---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-custom-scripts/
title: Custom scripts in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:15.560224+00:00
---

# Custom scripts in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-custom-scripts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Custom scripts in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

When defining a LiveClone Backup and DR Workflow that performs pre-scrubbing you can select from Optim privacy data masking or custom scripts.

For custom scripts, specify at least one pre- or post-processing script.

  * Specify a pre-script as needed. The pre-script is used to configure the environment prior to mounting or unmounting the application. This script must reside in a folder named `/act/scripts` on the server that hosts the mounted backup.
  * In the corresponding **Timeout in Seconds** , specify the time that is needed for the script to complete.
  * Specify a post-script as needed. The post-script used to perform an operation on the data after it is mounted or unmounted. This script must reside in a folder named `/act/scripts` on the server that hosts the mounted backup.
  * In the corresponding **Timeout in Seconds** , specify the time that is needed for the script to complete.



## Backup and DR Workflow Pre and Post Scripts

Backup and DR Workflows mount and unmount backups according to a schedule or on-demand. In a Backup and DR Workflow you can call the following:

  * A pre-script that runs before a backup is mounted or unmounted
  * A post-script that runs after a backup is mounted or unmounted



The ability to run a script before and after data is mounted or unmounted lets you do the following:

  * Scrub for sensitive information
  * Generate reports
  * Warehouse data, especially for extract, transform, and load—ETL— operations



Scripts must reside in a folder named `/act/scripts` on the server that hosts the mounted Backup and DR Workflow backup.

**Note:** For Backup and DR Workflows that involve both a database and its logs, you must configure scripts in such as way that pre- and post-script operations are not applied to the database's logs. See _Example Script_ for a script example that contains a command that skips a database's log.

### Environment variables

Environment variables allow you to invoke commands that apply to specific jobs, job types, or applications. Environment variables are prefixed with `ACT_`. For example, an environment variable for a database could look like:
    
    
        [$ACT_APPNAME =="productiondb"]
    

or an environment variable for a mount operation could look like:
    
    
        [$ACT_JOBTYPE == "mount"]
    

The following is a list of common environment variables with sample values:

  * **JOBNAME** : The name of the job—for example, Job_0123456.
  * **APPID** : The ID of the application—for example, 4186.
  * **APPNAME** : Name of the application—for example, My-DB.
  * **HOSTNAME** : The name of the host which is the target of this job—for example, Jupiter.
  * **SOURCEHOST** : The name of the host that was the source for this application—for example, Saturn.
  * **JOBTYPE** : A text version of the job class—for example, mount or unmount.
  * **PHASE** : A text string that describes the job phase—for example, pre or post.
  * **TIMEOUT** : Define the duration of the script, how long the script is allowed to run.
  * **OPTIONS** : Policy options that apply to this job.



### Example script

The following script example uses three environment variables:

  * **ACT_JOBTYPE** : Identifies whether the job is a mount or unmount operation.
  * **ACT_PHASE** : Identifies whether the phase is either pre or post.
  * **ACT_MULTI_END** : Used only if both a database and its log are mounted. When this is true, the database is in a state where it can be accessed.

**Note:** The following example script is not meant to be used in a production environment, has not been tested, and is not warranted by Backup and DR.
        
        ```sh
        #!/bin/sh
        set +x
        echo "*** Running user script: Job - $ACT_JOBNAME Type - $ACT_JOBTYPE Phase - $ACT_PHASE***"
        
        #Use the first if clause to perform application specific operations during mount and in this example scrub-mount operation.
        
        #Use the second if clause to perform any application specific operation during unmount and in this example, #scrub-unmount operation.
        
        #if [[ $ACT_JOBTYPE == "mount" ]] || [[ $ACT_JOBTYPE == "scrub-mount" ]]; then
        if [[ $ACT_JOBTYPE == "unmount" ]] || [[ $ACT_JOBTYPE == "scrub-unmount" ]]; then
            echo "NO-OP for job type $ACT_JOBTYPE"
            exit 0
        fi
        
        #Use the first if clause to perform application specific operations during the pre phase.
        
        #Use the second if clause to perform application specific operations during the post phase.
        
        #if [[ $ACT_PHASE == "post" ]]; then
        if [[ $ACT_PHASE == "pre" ]]; then
            echo "NO-OP for phase $ACT_PHASE"
            exit 0
        fi
        
        #For multi-phase jobs (database and logs) check if the database has been mounted and the logs applied then #skip logs.
        
        #If the operation needs to be performed in phases other than the last phase, modify the clause.
        
        if [[ -z "$ACT_MULTI_END" ]] && [[ $ACT_MULTI_END != "true" ]]; then
            echo "NO-OP for multi-phase operation"
            exit 0
        fi
        
        cd /act/scripts
        
        echo "**** Running application specific logic: Job - $ACT_JOBNAME Type - $ACT_JOBTYPE Phase - $ACT_PHASE *"
        
        Any application specific commands will go here
        
        echo "** Finished running application specific logic : Job - $ACT_JOBNAME Type - $ACT_JOBTYPE Phase - $ACT_PHASE*"
        exit $?
        ```
        




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
