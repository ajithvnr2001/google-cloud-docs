---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/set-up-pgbackrest/
title: Set up pgBackRest for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:24.696478+00:00
---

# Set up pgBackRest for AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/set-up-pgbackrest/

This page documents AlloyDB Omni version **15.5.4** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/overview)



Send feedback 

#  Set up pgBackRest for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/set-up-pgbackrest)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/set-up-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/set-up-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/set-up-pgbackrest)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/set-up-pgbackrest)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/set-up-pgbackrest)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/set-up-pgbackrest)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/set-up-pgbackrest)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/set-up-pgbackrest)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/set-up-pgbackrest)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/set-up-pgbackrest)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/set-up-pgbackrest)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/set-up-pgbackrest)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/set-up-pgbackrest)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/set-up-pgbackrest)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/set-up-pgbackrest)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/set-up-pgbackrest)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/set-up-pgbackrest)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/set-up-pgbackrest)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/set-up-pgbackrest)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/set-up-pgbackrest)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/set-up-pgbackrest)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/set-up-pgbackrest)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-pgbackrest)

This page shows you how to protect your data by configuring AlloyDB Omni to work with [pgBackRest](https://pgbackrest.org/), an open-source database backup server. For an overview of available backup solutions, see [Back up and restore AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/15.5.4/docs/backup-overview). 

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

See [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/backup-kubernetes) for Kubernetes-based information.

pgBackRest is a flexible backup and restore utility for PostgreSQL. Because AlloyDB Omni is PostgreSQL compatible, you can use pgBackRest to protect your AlloyDB Omni data using manual, scheduled, and continuous backups.

pgBackRest writes its backup data to local, remote, or cloud-based repositories. After you have established at least one repository, you can use pgBackRest to restore your AlloyDB Omni data through various methods, including point-in-time recovery (PITR).

AlloyDB Omni includes pgBackRest in its Docker container. This means that you can use pgBackRest to back up and restore your AlloyDB Omni data without the need to install any additional software.

For more information about pgBackRest, see [its user guide](https://pgbackrest.org/user-guide-index.html). 

## Before you begin

Before configuring AlloyDB Omni to work with pgBackRest, you need to have [AlloyDB Omni installed and running](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install) on a server that you control.

## A note about file system paths

When using pgBackRest with AlloyDB Omni, refer to file system paths from the container's perspective.

The pgBackRest software included with AlloyDB Omni runs in the same Docker container as AlloyDB Omni. Because of this, all of the file system paths that you provide pgBackRest through its configuration file or as command-line arguments are locations on the container's file system, and not your host machine's file system.

Many of the commands and examples on this page refer to your data directory as `/var/lib/postgresql/data`, regardless of the location of your data directory on your host system. This is because AlloyDB Omni mounts your data directory to `/var/lib/postgresql/data` on its containerized file system. As a result, you can use the data directory as a location to store pgBackRest configuration and repositories without further setup. 

**Note:** You can replace `/var/lib/postgresql/data` with the path to the PGDATA directory where your database cluster is stored.

If you want to configure the containerized pgBackRest to read from or write to directories on your host machine's file system outside of your AlloyDB Omni data directory, then you need to [make these directories available to the container](https://docs.docker.com/storage/bind-mounts/).

## Basic configuration with local backups

The steps in this section guide you through a basic setup of pgBackRest, including a short configuration file that directs pgBackRest to write continuous backup data into a subdirectory of your AlloyDB Omni data directory.

**Note:** Basic configurations don't enable backups on a schedule. See Set up scheduled backups for more information.

Because pgBackRest is a flexible third-party product compatible with AlloyDB Omni, you can modify any of these steps as appropriate for your own needs and preferences. If you do change any file system paths, remember that they must be visible to the container; see A note about file system paths.

### Set up trusted Unix-socket authentication

Allow your AlloyDB Omni host machine to authenticate the database server's `postgres` user without requiring a password. This simplifies subsequent steps.

  1. Add the following line to your `DATA_DIR/pg_hba.conf` file:
         
         local       all      postgres       trust
         

Replace DATA_DIR with the file system path to your data directory—for example, `/home/$USER/alloydb-data`.

  2. Restart AlloyDB Omni:
         
         docker restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it—for example, `my-omni`.




### Create and configure a backup repository

The configuration file created in this section is an example, enabling a minimal setup for locally stored, continuous backups. You can modify this file in any way that suits your needs. For more information, see [Configure cluster stanza](https://pgbackrest.org/user-guide.html#quickstart/configure-stanza).

  1. Create a `backups` subdirectory in your AlloyDB Omni data directory:
         
         mkdir DATA_DIR/backups

  2. Create a file named `pgbackrest.conf` inside your data directory, and copy the following content into it:
         
         [global]
         
         # Paths (all mandatory):
         repo1-path=/var/lib/postgresql/data/backups
         spool-path=/var/lib/postgresql/data
         lock-path=/var/lib/postgresql/data
         
         # Retention details:
         repo1-retention-full=3
         repo1-retention-full-type=count
         repo1-retention-diff=16
         
         # Force a checkpoint to start backup immediately:
         start-fast=y
         
         # Logging parameters:
         log-path=/var/lib/postgresql/data/backups
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
         pg1-socket-path=/var/lib/postgresql/data
         pg1-path=/var/lib/postgresql/data/data
         

  3. Initialize the backup location using [the `pgbackrest stanza-create` command](https://pgbackrest.org/command.html#command-stanza-create):
         
         docker exec CONTAINER_NAME pgbackrest --config-path=/var/lib/postgresql/data/backups --stanza=omni stanza-create




### Configure the database for continuous backups

  1. To enable continuous backups, run the following command to set several PostgreSQL parameters:
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres \
         -c "ALTER SYSTEM SET archive_command='pgbackrest --config-path=/var/lib/postgresql/data/backups --stanza=omni archive-push %p';" \
         -c "ALTER SYSTEM SET archive_mode=on;" \
         -c "ALTER SYSTEM SET max_wal_senders=10;" \
         -c "ALTER SYSTEM SET wal_level=replica;"

  2. Restart AlloyDB Omni:
         
         docker restart CONTAINER_NAME




## Run pgBackRest commands

Completing the steps in the previous section configures pgBackRest to work with your AlloyDB Omni server. To check the backup status, create manual backups, and perform other tasks, see [Command reference](https://pgbackrest.org/command.html).

As a best practice, run pgBackRest commands directly from the host machine that the AlloyDB Omni container is installed on, using the `docker exec` command. For example, to create a manual backup, use [the `pgbackrest backup` command](https://pgbackrest.org/command.html#command-backup). Modify it so that it runs within a `docker exec` command, and refers to the configuration file that you created earlier:
    
    
    docker exec CONTAINER_NAME pgbackrest --config-path=/var/lib/postgresql/data/backups --stanza=omni --type=full backup

You can also use environment variables to set the location of your pgBackRest configuration file. For more information, see [Config Path Option](https://pgbackrest.org/configuration.html#section-general/option-config-path).

## Set up scheduled backups

To set up scheduled backups, create a cron job that runs the `pgbackrest backup` command as often as needed. For more information, see [Schedule a backup](https://pgbackrest.org/user-guide.html#quickstart/schedule-backup).

## Custom configuration and remote backups

After you have a basic configuration working, you can tune your configuration file to suit your needs and preferences using the options documented in [the pgBackRest configuration reference](https://pgbackrest.org/configuration.html).

This includes specifying additional backup repositories located on remote machines, or in the cloud. If you define multiple repositories, then pgBackRest simultaneously writes to them all as its default backup action.

For example, pgBackRest supports [using a Cloud Storage bucket as a backup repository](https://www.crunchydata.com/blog/announcing-google-cloud-storage-gcs-support-for-pgbackrest), with [a number of related configuration options](https://pgbackrest.org/configuration.html#section-repository/option-repo-gcs-bucket). The following section demonstrates one way to use these options.

### An example configuration using Cloud Storage

The steps in this section build on the configuration file introduced in Basic configuration with local backups. These modifications to that file define a second backup repository in a Cloud Storage bucket, accessed through Identity and Access Management (IAM).

The automatic authentication style in this example requires an AlloyDB Omni cluster to run on a Compute Engine VM instance. If you don't run AlloyDB Omni on a Compute Engine VM instance, then you can still back up to a Cloud Storage bucket by using another authentication method, such a Google Cloud service account key saved to the local file system.

To extend the earlier configuration file to define a Cloud Storage-based pgBackRest repository, follow these steps:

  1. [Configure the bucket permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to allow the service account attached to your VM instance to write to the bucket. This requires [the Storage Object User IAM role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) set on that service account.

  2. Add these lines to your `pgbackrest.conf` file:
         
         # Cloud Storage access details:
         repo2-type=gcs
         repo2-gcs-key-type=auto
         repo2-storage-verify-tls=n
         
         # Cloud Storage bucket and path details:
         repo2-gcs-bucket=BUCKET_NAME
         repo2-path=/pgbackrest
         
         # Cloud Storage backup retention parameters:
         repo2-retention-full=8
         repo2-retention-full-type=count
         

Replace BUCKET_NAME with the name of the Cloud Storage bucket that you want pgBackRest to store backups to.

  3. Initialize the cloud-based backup location using [the `pgbackrest stanza-create` command](https://pgbackrest.org/command.html#command-stanza-create):
         
         docker exec CONTAINER_NAME pgbackrest --config-path=/var/lib/postgresql/data/backups --stanza=omni stanza-create




After you initialize the backup repository in your Cloud Storage bucket using the `pgbackrest stanza-create` command, pgBackRest backs up to two locations:

  * The location in the local file system, defined elsewhere in the configuration file as `repo1-path`.

  * The Cloud Storage bucket, defined using the `repo2-` configuration directives set up by this example.




## What's next

  * [Restore an AlloyDB Omni cluster using pgBackRest](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/restore-pgbackrest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
