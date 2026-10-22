---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/set-up-pgbackrest/
title: Set up pgBackRest for AlloyDB Omni on Linux \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:49.858569+00:00
---

# Set up pgBackRest for AlloyDB Omni on Linux  |  AlloyDB Omni using RPM: 18.1.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/set-up-pgbackrest/

This page documents AlloyDB Omni version **18.1.1** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/overview)



Send feedback 

#  Set up pgBackRest for AlloyDB Omni on Linux Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/set-up-pgbackrest)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/set-up-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/set-up-pgbackrest)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/set-up-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/set-up-pgbackrest)

This page shows you how to protect your data by configuring AlloyDB Omni to work with [pgBackRest](https://pgbackrest.org/), an open-source database backup server. 

TDE-enabled clusters support transparent backups and restores using pgBackRest, and you do not need to perform any additional steps. For more information, see [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/create-tde-cluster).

For more information about pgBackRest, see [its user guide](https://pgbackrest.org/user-guide-index.html).

## Before you begin

Before configuring AlloyDB Omni to work with pgBackRest, complete the following prerequisites:

  * [Install and run AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/deploy-vm) on a server that you control.



## Basic configuration with local backups

The steps in this section guide you through a basic setup of pgBackRest. Basic configurations don't enable backups on a schedule. For more information, see Set up scheduled backups.

Because pgBackRest is a flexible third-party product compatible with AlloyDB Omni, you can modify any of these steps as appropriate for your own needs and preferences.

### Create a backup directory

For organization purposes, we strongly recommend that you create a separate directory for pgBackRest backups. To set up a new directory, complete the following steps:

  1. If AlloyDB Omni is running, stop it.
         
         sudo systemctl stop alloydbomni18
         

  2. Create a backup directory.
         
         sudo mkdir -p BACKUP_DIR
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in.
  3. Make the backups directory readable by `postgres`.
         
         sudo chown -R postgres:postgres BACKUP_DIR
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in. 



### Configure local backups

pgBackRest creates subdirectories for each backup taken and includes a plain-text manifest file.

pgBackRest uses the term stanza to refer to the configuration for a PostgreSQL database cluster. The stanza name is arbitrary and doesn't need to match the host server, PostgreSQL cluster, or database name. The pgBackRest documentation suggests naming the stanza after the cluster's function.

The repository is where backups are written. pgBackRest supports writing to more than one repository in a given stanza. Most configuration parameters related to repositories are indexed with a numeric value. For example, `repo1-`. Parameters related to PostgreSQL clusters are also independently indexed. For example, parameters specific to the first PostgreSQL cluster in a stanza are prefixed with `pg1-`.

pgBackRest leverages a configuration file, called `pgbackrest.conf`, to hold global and stanza-specific parameters.

To build and initialize a configuration file for backing up your AlloyDB Omni cluster, create the `pgbackrest.conf` file in the host-side backups directory you created in Mount a backup volume to your container or Create a backup directory.
    
    
    [global]
    # Paths (all mandatory):
    
    
    repo1-path=BACKUP_DIR
    spool-path=BACKUP_DIR/spool
    lock-path=BACKUP_DIR
    
    
    # Retention details:
    repo1-retention-full=3
    repo1-retention-full-type=count
    repo1-retention-diff=16
    
    # Force a checkpoint to start backup immediately:
    start-fast=y
    
    # Logging parameters:
    
    
    log-path=BACKUP_DIR
    
    log-level-console=info
    log-level-file=info
    
    # Recommended ZSTD compression:
    compress-type=zst
    
    # Other performance parameters:
    archive-async=y
    archive-push-queue-max=1024MB
    archive-get-queue-max=256MB
    archive-missing-retry=y
    
    [global:archive-push]
    process-max=2
    
    [global:archive-get]
    process-max=2
    
    [omni]
    pg1-user=postgres
    pg1-socket-path=/tmp
    
    
    
    pg1-path=DATA_DIR
    
    
    

Some parameters are mandatory, but others can be adjusted to meet your specific requirements if needed, such as the following:

  * [`repo1-path`](https://pgbackrest.org/configuration.html#section-repository/option-repo-path): Directory location where the backups are written to. We recommend a location visible to both the host server and the container.

  * [`log-path`](https://pgbackrest.org/configuration.html#section-log/option-log-path): Directory location where the log files are written to. If you want to write the log files to a separate location, not mixed with the backups themselves, adjust this parameter.

  * [`repo1-retention-full`](https://pgbackrest.org/configuration.html#section-repository/option-repo-retention-full): Number of full backups to retain.

  * [`repo1-retention-full-type`](https://pgbackrest.org/configuration.html#section-repository/option-repo-retention-full-type): Whether the retention is measured by count or time period (days).

  * [`repo1-retention-diff`](https://pgbackrest.org/configuration.html#section-repository/option-repo-retention-diff): Number of differential backups to retain.




Other non-critical, but recommended, parameter settings that are compatible with AlloyDB Omni in the configuration file include the following:

  * [`log-level-console`](https://pgbackrest.org/configuration.html#section-log/option-log-level-console): Level of logging written to the screen (STDOUT) when running pgBackup commands. You can adjust this to meet your needs in the configuration file, or override this value with the `--log-level-console` command line argument. The default is `warn`.

  * [`start-fast`](https://pgbackrest.org/configuration.html#section-backup/option-start-fast): Forces a checkpoint to start the backups quickly. The default is `n`.

  * [`archive-async`](https://pgbackrest.org/configuration.html#section-archive/option-archive-async): Push WAL segment files asynchronously for performance. The default is `n`.

  * [`process-max`](https://pgbackrest.org/configuration.html#section-general/option-process-max): Maximum number of processes to use for compression and transfer. This is typically set to `max_cpu/4` on a primary or `max_cpu/2` on a standby cluster. The default is `1`.

  * [`compress-type`](https://pgbackrest.org/configuration.html#section-general/option-compress-type): Compression algorithm to use. The default is `gz`.




Many other pgBackRest configuration parameters exist and can be adjusted. This documentation covers only the parameters mandatory for the default AlloyDB Omni configuration and some recommended parameter settings. For the full list of configuration parameters, refer to the [pgBackRest Configuration Reference](https://pgbackrest.org/configuration.html) online documentation.

After configuring pgBackRest, the target repositories where backups are written to must be initialized by creating the stanza, which uses the parameters as set in the configuration file.

To configure your database for backups, complete the following steps:

  1. Create the stanza using the `stanza-create` command.
         
         sudo -u postgres pgbackrest \
         --config-path=/var/lib/BACKUP_DIR \
         --stanza=omni stanza-create
         

  2. Configure your database for backups.
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres \
         -c "ALTER SYSTEM SET archive_command='pgbackrest --config-path=BACKUP_DIR --stanza=omni archive-push %p';" \
         -c "ALTER SYSTEM SET archive_mode=on;" \
         -c "ALTER SYSTEM SET max_wal_senders=10;" \
         -c "ALTER SYSTEM SET wal_level=replica;"
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in.
  3. Restart AlloyDB Omni.
         
         sudo systemctl restart 18
         

  4. Validate the backup configuration.
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres \
         -c "SELECT name, setting
             FROM pg_catalog.pg_settings
             WHERE name IN ('archive_command',
                            'archive_mode',
                            'max_wal_senders',
                            'wal_level')
             ORDER BY name"
         

  5. Perform a pgBackRest check.
         
         sudo -u postgres pgbackrest \
         --config-path=BACKUP_DIR \
         --stanza=omni \
         check
         




Replace the following variable:

  * `BACKUP_DIR`: Host directory that your backups will be stored in.



## Perform a backup

  1. Perform a full backup.
         
         sudo -u postgres pgbackrest \
         --config-path=BACKUP_DIR \
         --stanza=omni \
         --type=full backup
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in.
  2. Perform a differential backup.
         
         sudo -u postgres pgbackrest \
         --config-path=BACKUP_DIR \
         --stanza=omni \
         --type=diff backup
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in.
  3. Report backups.
         
         sudo -u postgres pgbackrest \
         --config-path=BACKUP_DIR \
         --stanza=omni \
         info
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in.



## Set up scheduled backups

To set up scheduled backups, create a cron job that runs the `pgbackrest backup` command as often as needed. For more information, see [Schedule a backup](https://pgbackrest.org/user-guide.html#quickstart/schedule-backup).

## Custom configuration and remote backups

After you have a basic configuration working, you can tune your configuration file to suit your needs and preferences using the options documented in the [pgBackRest configuration reference](https://pgbackrest.org/configuration.html).

This includes specifying additional backup repositories located on remote machines, or in the cloud. If you define multiple repositories, then pgBackRest simultaneously writes to them all as its default backup action.

For example, pgBackRest supports [using a Cloud Storage bucket as a backup repository](https://pgbackrest.org/release.html#2.33), with [a number of related configuration options](https://pgbackrest.org/configuration.html#section-repository/option-repo-gcs-bucket). The following section demonstrates one way to use these options.

### An example configuration using Cloud Storage

The steps in this section build on the configuration file introduced in Basic configuration with local backups. These modifications to that file define a second backup repository in a Cloud Storage bucket, accessed through Identity and Access Management (IAM).

The automatic authentication style in this example requires an AlloyDB Omni cluster to run on a Compute Engine VM instance. If you don't run AlloyDB Omni on a Compute Engine VM instance, then you can still back up to a Cloud Storage bucket by using another authentication method, such a Google Cloud service account key saved to the local file system.

To extend the earlier configuration file to define a Cloud Storage-based pgBackRest repository, follow these steps:

  1. [Configure the bucket permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to allow the service account attached to your VM instance to write to the bucket. This requires [the Storage Object User IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) set on that service account.

  2. Add these lines to the `[global]` section of your `pgbackrest.conf` file:
         
         # Cloud Storage access details:
         repo2-type=gcs
         repo2-gcs-key-type=auto
         repo2-storage-verify-tls=n
         
         # Cloud Storage bucket and path details:
         repo2-gcs-bucket=BUCKET_NAME
         repo2-path=PATH_IN_BUCKET
         
         # Cloud Storage backup retention parameters:
         repo2-retention-full=8
         repo2-retention-full-type=count
         

Replace the following variable:

     * `BUCKET_NAME`: Name of the Cloud Storage bucket that you want pgBackRest to store backups to.
     * `PATH_IN_BUCKET`: Directory path in the Cloud Storage bucket that you want pgBackRest to store backups in.
  3. Initialize the cloud-based backup location using the [`pgbackrest stanza-create`](https://pgbackrest.org/command.html#command-stanza-create) command:
         
         sudo -u postgres pgbackrest \
         --config-path=BACKUP_DIR \
         --stanza=omni stanza-create
         

Replace the following variable:

     * `BACKUP_DIR`: Host directory that your backups will be stored in.



After you initialize the backup repository in your Cloud Storage bucket using the `pgbackrest stanza-create` command, pgBackRest may back up to two locations:

  * Location in the local file system, defined elsewhere in the configuration file as `repo1-path`. This is the default location when `--repo` is not specified in the `pgbackrest` command.

  * Cloud Storage bucket, defined using the `repo2-gcs-bucket` configuration directives set up by this example. To use the Cloud Storage bucket, specify `--repo=2` in the `pgbackrest` command.




## What's next

  * [Restore an AlloyDB Omni cluster using pgBackRest](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/restore-pgbackrest) Send feedback 




Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
