---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-create-oracle/
title: Create Backup and DR Workflows for Oracle databases in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:43.919578+00:00
---

# Create Backup and DR Workflows for Oracle databases in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-create-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Create Backup and DR Workflows for Oracle databases in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR Workflows are defined in the **App Manager**. Backup and DR Workflows use backup production data as the source data from which they generate.

  * **Direct mounts** : Direct mounts are used when application data does not need to be scrubbed before it is mounted and made available to users. The application data can be mounted with a standard mount as just the data, a virtual application, or as both the data and as a virtual application. Direct mounts make backup data available almost instantly without actually moving data.
  * **LiveClones** : LiveClones are typically used in Backup and DR Workflows when an application contains sensitive data that must be scrubbed before it is mounted and made available to users. The application data can be mounted with a standard mount as just the data, or a virtual application, or as both the data and as a virtual application. Updates to the LiveClone, scrubbing, and mounting can be done automatically, either according to a schedule or on-demand.

**Note:** Backup and DR Workflows consist of a number of options. Not specifying an option lets users to specify that option when running the Backup and DR Workflow on-demand.



## Direct mounting Oracle data as a virtual application

Direct mount Backup and DR Workflows are used when the application backup does not contain sensitive data. This allows the Backup and DR Workflow to mount an application's data as a virtual application, or as application data only, without first having to define a LiveClone and then scrub the LiveClone. Direct mounts make application data and virtual applications available almost instantly.

In this example, you define a Backup and DR Workflow that does the following:

  * Generates or updates mounted application data from a single selected production backup.
  * Defines a schedule for updating the application data with the latest production data. Scheduled Backup and DR Workflows can also be run on-demand.
  * Mounts the application data.
  * Lets you create a virtual application with the data.



Use these instructions to define the Backup and DR Workflow for an Oracle database:

  1. From the Backup and DR appliance management console, click **App Manager** > **Workflows**.

**Note:** To modify an existing Backup and DR Workflow for an application, go to **Applications** and right-click the application. Then select **Manage Workflows**.
  2. Click **Workflow** in the upper-right corner of the page.

The **Add Workflow: Select an Application** page opens.

  3. Right-click a managed database and click **Next**.

  4. On the **Add Workflow: Configure** page, specify a name for the Backup and DR Workflow, then select **Direct Mount** , and select the appliance to manage the Backup and DR Workflow. Backup and DR Workflow names cannot include special characters.

  5. Select **Scheduled** and assign a frequency for the Backup and DR Workflow to run for **Schedule Type**. The time selector uses a 24-hour clock. Scheduled Backup and DR Workflows can also be run on-demand.

  6. In **Direct Mount Settings** for **Source Image** , select the snapshot to run the Backup and DR Workflow on and give the mount an identifiable label.

  7. In the **Hosts** section, select the server or servers which the data mounts to. The user who runs the Backup and DR Workflow is given the option of mounting the data to other servers as needed.

  8. In the **Mapping Options** , add a **mount location**. If you do not specify a mount, the Backup and DR agent chooses a mount location.

  9. Enter a **Preferred diskgroup name** as needed.

  10. Enter a **RAC node list** as needed in a colon-separated list of IP addresses.

  11. Specify a **Pre Script** as needed. The pre-script is used to configure the environment prior to mounting or unmounting the application. This script must reside in a folder named `/act/scripts` on the server that hosts the mounted backup. See [Backup and DR Workflow pre and post scripts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/custom-scripts#script) for scripting details.

  12. Specify a **Post Script** as needed. The post script is used to perform an operation on the data after it is mounted or unmounted. This script must reside in a folder named `/act/scripts` on the server that hosts the mounted backup. See [Backup and DR Workflow pre and post scripts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/custom-scripts#script) for scripting details.

  13. If you specified scripts, specify timeouts long enough for the scripts to complete.

  14. The **Remove mounted backup after processing.** checkbox is typically used when you employ a script to process mounted data. Once the script finishes its task, this option unmounts and deletes the virtual application.

  15. Decide between these options:

     * If you only need the data, click **Done** and the Backup and DR Workflow runs as scheduled. Users with proper access can also run this Backup and DR Workflow on-demand to provision and re-provision their environments with the application data.
     * If you want to create a virtual application, continue with the following steps.
  16. Check the **Perform application aware mount** checkbox and the application specific options to perform an application aware mount are displayed.

**Note:** The **Remove mounted backup after processing** option disappears when you select **Perform application aware mount**. The **Remove mounted backup after processing** option is typically used for pre and post scripts. It unmounts the backup from the target server, and deletes it after the scripts finish. This option is typically used when scripts perform operations on the mounted data.
  17. In the spaces provided, enter the Oracle related options. Click the question mark **?** next to an option for help text.

  18. Click the black arrow to open **Advanced Options** and complete the remainder of the options as necessary.

  19. Select **Restore with Recovery**. Doing so leaves the database in a state where if logs are available they can be applied to bring the database to a specific point in time.

  20. At this point you can complete these tasks:

     * Check the **Protect new application** option. This lets you apply a backup plan policy template and a **Resource Profile** to protect the virtual application as a new application. For details see [Backup plan policy templates](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) and [Profiles](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/resource-profiles#create-profile).
     * Click **Done** and the Backup and DR Workflow runs as scheduled. Users with proper access can also run this Backup and DR Workflow on-demand to provision and re-provision their environments with the virtual application.



## Create scrubbed data or virtual applications with LiveClone and mask tools

LiveClone Backup and DR Workflows are typically used when the production data contains sensitive information. The LiveClone Backup and DR Workflow lets you to define a LiveClone from production data, and then scrub the LiveClone's data before mounting it.

In the following example, a Backup and DR Workflow can do the following:

  * Generate a new or update an existing LiveClone from a selected production backup that is marked as sensitive.
  * Define a schedule for updating the LiveClone with the latest production data. Scheduled Backup and DR Workflows can also be run on-demand.
  * Employ scripts to scrub the LiveClone of sensitive data.
  * Mark the scrubbed virtual application as non-sensitive.
  * Mount the scrubbed backup as a virtual application—application aware mount—to a specified host.



Use these instructions to define this Backup and DR Workflow:

  1. Open the appliance management console to **App Manager** > **Workflows**.
  2. In the upper-right corner, click **Add Workflow**.
  3. In the **Add Workflow: Select an Application** page, right-click the application to be scrubbed of its sensitive data and select **Next**.

The **Add Workflow: Configure** page opens.

**Note:** If the application already has a Backup and DR Workflow, click the **Add** button.
  4. Specify a name for the Backup and DR Workflow. Backup and DR Workflow names cannot include special characters.

  5. For **Workflow Type** select **LiveClone**.

The **LiveClone Settings** opens.

  6. For **Schedule Type** , select either **Scheduled** or **On Demand**. Scheduled Backup and DR Workflows can also be run on-demand.

**Note:** You can run a scheduled Backup and DR Workflow on-demand at any time. You cannot convert an on-demand Backup and DR Workflow to a scheduled Backup and DR Workflow after it has been created.
  7. If you selected **Scheduled** , define a schedule to run the Backup and DR Workflow.

The time selector uses a 24-hour clock.

  8. For **Source Image** , select the latest snapshot from the policy that produces the backup to scrub.

**Note:** If you selected on-demand, the user running the Backup and DR Workflow can select the source snapshot at runtime.
  9. Provide an identifiable label to the LiveClone.

  10. Select the **Snapshot Pool** where the LiveClone resides. Be sure enough storage space is allocated to accommodate the LiveClone.

Enable **Mount for pre-processing** and the following screen provides the opportunity to mount the LiveClone to a host and then scrub the mounted backup for sensitive data.

  11. The **Mark Data Non-Sensitive** option only appears if the selected application is marked as containing sensitive data. Check this option if the application does not contain sensitive data after scrubbing. This lets users who don't have access to sensitive data to access the Backup and DR Workflow and provision their work environments.

  12. Select a **Host** to mount the LiveClone on.

  13. In **Mapping Options** , add a **Mount Location** if you want the backup mounted to a location other than the default. If you don't specify a mount location, then the Backup and DR agent assigns a mount location.

  14. Enter a **Preferred diskgroup name** as needed.

  15. Enter a **RAC node list** as needed in a colon separated list of IP addresses.

  16. You can use Optim data privacy masking or you can use your own custom scripts:

     * If you use Optim data privacy masking, enter a **Service Set** and a **Time Out** value in minutes.
     * If you use custom scripts, specify a **Pre Script** as necessary. The pre script is used to configure the environment prior to mounting or unmounting an application. Then specify a **Post Script** as needed. The post script in this example scrubs the application of sensitive information after it has been mounted. Specify timeouts long enough for the scripts to complete.
**Note:** Custom scripts must reside in a folder named `/act/scripts` on the server that hosts the mounted backup. See [Backup and DR Workflow pre and post scripts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/custom-scripts#script) for scripting details.
  17. If you don't need a virtual application, then click **Add** and the Backup and DR Workflow runs as scheduled. Users with proper access can run this Backup and DR Workflow on-demand and provision and re-provision any server to which they have access with the application data.

If you need a virtual application of this LiveClone, continue here.

  18. Enable **Create New Virtual Application** and click **Next**. Additional Oracle settings options are displayed to complete the process.

  19. Enable **Manage New Application** if you want Backup and DR to protect it. If you select this, you have to select a policy template and a resource profile to apply to it.

  20. Click the arrow to open the **Advanced Options**. Select **Restore with Recovery** to apply available logs to bring the database to a specific point in time.

  21. Continue entering the Oracle settings as needed for this database. Click each label for help.

  22. At the end, select **Remove mounted backup after done** checkbox. It is usually selected when you employ a script to process mounted data. When the script finishes its task this option unmounts, and you can delete the virtual application.

  23. Click **Add**.




## Use a Backup and DR Workflow to refresh Oracle database schemas

If you are using Oracle 12c or later, see Present an Oracle 12c database PDB as a virtual PDB to an existing database container on a target.

If you have a source database instance with multiple applications, and each application has its own schema, do the following:

  * Create and refresh a virtual copy at the schema level, and refresh each schema individually to the same target or to a different target.
  * Create and refresh multiple virtual copies of a single schema to a single target under different schemas, each with its own refresh schedule.



This section includes the following:

  * Before you begin
  * Create the Backup and DR Workflow
  * Run the Backup and DR Workflow
  * Unmount mounted backups



### How it works: Backup and DR virtual copy with transportable tablespace

You can create and refresh multiple virtual copies under a single target Oracle instance from the same or from multiple source instances.

  1. Set up an application aware mount Backup and DR Workflow to create an application aware mount with a temporary instance.
  2. Set up a pre-script to run on the target instance—offline and drop the tablespace to be refreshed on the target instance.
  3. Set up a post-script to be run on the temporary instance and the target instance.
  4. On the temporary instance, complete the following: 
     1. Rename the tablespace
     2. Change the tablespace to read-only
     3. For EXPDP, export the tablespace metadata.
     4. Shut down the temporary instance.
  5. On the target instance: 
     1. For IMPDP, import the tablespace metadata (TRANSPORT_DATAFILES with remap schema to target instance
     2. Change the tablespace to read-write



### Before you begin

Follow these instructions before you begin.

  1. Make sure that your database backups are running as per the backup plan policy.
  2. Set up the scripts on the target server:

     1. Login to database server as root. Change directory to `/act` and create an `/act/scripts` directory—if it does not exist—by running the following commands.
            
            cd /act
              mkdir -p /act/scripts
              cd /act/scripts
            

     2. Copy all files from `/act/act_scripts/objectrefresh/`

     3. Move `act_<schema>_refresh.conf` to `act_testuser_refresh.conf` for a target schema name of testuser where `<schema>` is testuser.

where:

        * SOURCE_SCHEMA_NAME: Source database schema to be presented to target.
        * TARGET_SID: Target database SID, where schema is refreshed.
        * TARGET_SCHEMA_NAME: Target database schema to be refreshed with source schema.
**Note:** TARGET and SOURCE Schema names can be the same or different.



### Create the Backup and DR Workflow

Use the following instructions to create a Backup and DR Workflow to perform a schema refresh.

  1. Open the appliance management console to **App Manager** > **Workflows** , then select **Add Workflow**.
  2. From the **Add Workflow: Select an Application** list, right-click the database to use and click **Next**.
  3. The **Add Workflow: Configure** page appears:

     * Provide a unique name for the Backup and DR Workflow. Backup and DR Workflow names cannot include special characters.
     * Select **Direct Mount**.
     * Select the backup/recovery appliance that runs the Backup and DR Workflow.
     * For **Schedule Type** , select **On Demand**.
     * Select the **Source** backup, either latest snapshot or latest snap from production.
     * At **Mount Label** , provide a unique identifier to help identify mounts from this Backup and DR Workflow when viewing active mounts.
     * Select the target **Host** from the **Hosts** list.
  4. In **Mapping Options** , complete the following:

     * Enter the location for mounted drives—for example,. M:, D:\testdb1, or /oracledata/db1data—if the temporary copy is going to be on NON - ASM.
     * Add the **Preferred Diskgroup Name**.
     * For **RAC Node List** , enter a colon-separated list of IP addresses.
  5. Fill in the pre-script field: act_ttswf _pre.sh act_`SCHEMA` _refresh.conf Where act_`SCHEMA`_refresh.conf is the file created from step one.

  6. Fill in the post-script field: ttswf _post.sh act_`SCHEMA` _refresh.conf Where act_`SCHEMA`_refresh.conf is the file created from step one.

  7. Enter a timeout value of 1800 or more seconds.

  8. Select **Create New Virtual Application**.

  9. Fill the target database SID—this is a temporary SID.

  10. Provide the **OS Username** who owns the Oracle software binary on the target machine.

  11. Provide **ORACLE_HOME** as specified in the configuration file.

  12. Open the **Advanced Options** by clicking the arrow. Provide the **TNS ADMIN Directory Path** on the target machine, and specify the minimum SGA% for the temporary instance. Click the field labels for help.

  13. Select **Standalone Non-RAC**.

  14. Click **Add**.




### Run the Backup and DR Workflow

Once the Backup and DR Workflow is created, use the following steps to run it.

  1. Right-click the Backup and DR Workflow and click **Run Now**.
  2. Select **Initiate Scheduled Workflow Now** and click **Submit**.

Logs can be monitored on the target host at location: `/var/act/log`

  3. When the Backup and DR Workflow displays a success state, the schema on the target database is refreshed.

     1. If the TARGET_SCHEMA_NAME does not exist on the target database, Backup and DR creates a user for the first time and the default user password is abc#1234.
     2. Tablespaces for the refreshed schema on target database get presented to the target with the schema name as a prefix: (Schema)_(Source_Tablespace_Name)



### Unmount mounted backups

Use these instructions to unmount mounted backups.

  1. Drop the tablespace and datafiles on the target database.
         
         ```sql
         SQL>alter tablespace <TBS_NAME> offline immediate;
         SQL>drop tablespace <TBS_NAME> including contents and datafiles;
         ```
         

  2. Open **App Manager** > **Active Mounts** page. Right-click the backup to be unmounted and select **Unmount and Delete** and then **Submit** the job.




## Present an Oracle 12c or later database PDB as a virtual PDB to an existing database container on a target

If you are using an Oracle version earlier than 12c, then refer to Use a Backup and DR Workflow to refresh Oracle database schemas.

For example, you have a source database instance with multiple applications, and each application has its own PDB. You can create and refresh a virtual copy at the schema level, and refresh each PDB individually to the same target or to a different target. To do this, follow these steps.

  * Before you begin
  * Create a Backup and DR Workflow to perform the PDB clone job
  * Run the Backup and DR Workflow
  * Unmount mounted backups



### Before you begin

Before you begin, set up the scripts on the target server:

  1. Get the script zip file from /act/act_scripts/pdbrefresh.
  2. Login to database server as root.
  3. Go to /act and create an /act/scripts directory—if it does not exist:
         
         cd /act
         mkdir -p /act/scripts
         cd /act/scripts
         

  4. Extract the file.

  5. Copy the script files into /act/scripts:
         
         cp /act/act_scripts/pdbrefresh/act_pdbclone_pre.sh /act/scripts/
         cp /act/act_scripts/pdbrefresh/act_pdbclone_post.sh /act/scripts/
         




### Create a Backup and DR Workflow to perform the PDB clone job

  1. From the **App Manager Workflows** page, click **Add Workflow**.
  2. Right-click the Oracle database and select **Next**.
  3. Enter a name for the Backup and DR Workflow and select **Direct Mount** and **On Demand**.

**Note:** Backup and DR Workflow names cannot include special characters.
  4. Select the target host checkbox.

  5. If the temporary copy is going to be on non-ASM, then under **Mapping Options** , select **Specify Mount Location** as the **Mount Action** and then provide a mount location.

  6. Fill in the pre-script field and the post-script field: act_pdbclone _pre.sh "`TARGET_DB_SID`_`SOURCE_PDB_NAME`-`TARGET_PDB_NAME`" act_pdbclone _post.sh "`TARGET_DB_SID`_`SOURCE_PDB_NAME`-`TARGET_PDB_NAME`" Where: TARGET_DB_SID = Target database SID where PDB should be attached SOURCE_PDB_NAME = Source PDB Name that needs to be attached to target container. TARGET_PDB_NAME = Target PDB Name to which source is renamed.

  7. Set **Timeout** for both scripts to 18000.

  8. Select **Create New Virtual Application**.

  9. Fill in the target database SID—this is temporary SID as defined in the act_pdb_config.conf file.

  10. Provide the OS username who owns the Oracle software binary on the target machine.

  11. Provide ORACLE_HOME as specified in the configuration file.

  12. Open the **Advanced Options** by clicking the arrow. Provide the **TNS ADMIN Directory** on the target machine and specify the minimum SGA for the temporary instance.

  13. Select **Standalone Non-RAC**.

  14. Click **Add** at the bottom of the page.




### Run the Backup and DR Workflow

Once the Backup and DR Workflow is created, use these instructions to run it.

  1. Click **App Manager** > **Workflows** , then right-click the Backup and DR Workflow and click **Run Now**.
  2. Select **Provision New Virtual Application** , fill in the details, and click **Submit**.
  3. Logs can be monitored on the target host at: /var/act/log.

Once the Backup and DR Workflow reaches success state, the PDB on the target database is cloned.

If the target PDB must be refreshed again with latest or old source data, click the Backup and DR Workflow **Run Now** button and select **Refresh Existing Virtual Application** and click **Done**.




### Unmount mounted backups

Use these instructions to unmount any mounted backups:

  1. From the **Restore** tab, select the backup to unmount.
  2. Drop the pluggable database and datafiles on the target database.
         
         SQL>alter pluggable database <PDB_NAME> close immediate;
         SQL>drop pluggable database <PDB_NAME> including datafiles;
         

Or, execute the pre-script:
         
         cd /act/scripts
         ./ act_pdbclone_pre.sh
         

  3. Click **App Manager** > **Active Mounts** list, right-click the backup to be unmounted and select **Unmount and Delete** and then **Submit** the job.




## The Oracle DBA guide

  * [Backup and DR for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-intro)
  * [Prerequisites for protecting an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prerequisites)
  * [Oracle patches and known issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/oracle-patches-known-issues)
  * [Prepare Oracle databases for protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-db-prepare)
  * [Discover and protect an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-oracle)
  * [Details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  * [Use dNFS with Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/oracle-dnfs)
  * [Protect a discovered Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/oracle-db-protect)
  * [Mount an Oracle database as a standard mount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount)
  * [Create an instant virtual copy of an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/oracle-mount-virtualdb)
  * [Restore and recover an Oracle database](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle)
  * [Instant recovery of an Oracle database using Mount and Migrate](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/oracle-mm)
  * [Provision an environment with a Backup and DR workflow](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-workflow-oracle)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
