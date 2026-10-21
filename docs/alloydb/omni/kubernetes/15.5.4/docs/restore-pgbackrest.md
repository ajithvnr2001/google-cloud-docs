---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/restore-pgbackrest/
title: Restore an AlloyDB Omni cluster using pgBackRest \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:58:18.333387+00:00
---

# Restore an AlloyDB Omni cluster using pgBackRest  |  AlloyDB Omni for Kubernetes: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/restore-pgbackrest/

This page documents AlloyDB Omni version **15.5.4** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)



Send feedback 

#  Restore an AlloyDB Omni cluster using pgBackRest Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/restore-pgbackrest)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/restore-pgbackrest)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/restore-pgbackrest)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/restore-pgbackrest)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/restore-pgbackrest)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/restore-pgbackrest)

This page shows you how to restore an AlloyDB Omni cluster using a backup created with [pgBackRest](https://pgbackrest.org/), the open-source backup solution included with the AlloyDB Omni Docker container. 

Because AlloyDB Omni is compatible with PostgreSQL, the data-restoration commands and techniques described by [the pgBackRest manual](https://pgbackrest.org/user-guide-index.html) apply to AlloyDB Omni as well. This page demonstrates a selection of common recovery tasks, with examples of relevant commands.

For more information about configuring pgBackRest to work with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/set-up-pgbackrest).

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

See [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/backup-kubernetes) for Kubernetes-based information.

## Before you begin

Before configuring AlloyDB Omni to work with pgBackrest, you need to have [AlloyDB Omni installed and running](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install) on a server that you control.

  * A target database server, running the same major version of AlloyDB Omni as the backup you want to restore. For more information about installing AlloyDB Omni, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install).

  * A pgBackRest backup repository containing at least one backup of the source AlloyDB Omni database.

  * Enough free disk space on the target server to hold the restored database.




## Overview

To perform an AlloyDB Omni restore using pgBackRest, run [the `pgbackrest restore` command](https://pgbackrest.org/command.html#command-restore). The parameters that you provide the command vary depending upon your situation.

In general, you run the `pgbackrest restore` command with flags that provide the following information:

  * The location of your `pgbackrest.conf` file.
  * The name of pgBackRest backup repository that you want to restore to. These repositories are named and defined in the `pgbackrest.conf` file.
  * The location on the local file system to write the restored data to.
  * An identifier of the particular backup or point in time that you want to restore from.



When running the containerized `pgbackrest restore` commands, remember to use file system paths from the container's point of view. For example, the path to your AlloyDB Omni data directory is always `/var/lib/postgresql/data`, no matter its location on your host server. For more information, see [A note about file system paths](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/set-up-pgbackrest#paths).

## Perform a point-in-time restore

This example restores data from a pgBackRest repository, naming a particular point in time to restore to. If you have defined multiple repositories in the target environment's `pgbackrest.conf` file, then pgBackRest chooses the repository to restore from based on availability, expected speed, and other factors.

The example assumes the following:

  * You have a `pgbackrest.conf` file located at the top level of your target AlloyDB Omni data directory. This makes the file available to the containerized `pgbackrest` as `/var/lib/postgresql/data`.

  * [You have enabled continuous backups](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/set-up-pgbackrest#continuous) with your pgBackRest configuration.



  1. In the target environment, perform a PITR restore, specifying a timestamp to restore to:

###  Docker 
         
         docker exec CONTAINER_NAME pgbackrest \
           --config-path=/var/lib/postgresql/data \
           --stanza=STANZA \
           --type=time \
           --pg1-path=/var/lib/postgresql/data/data-RESTORED \
           --target="TIMESTAMP" \
           restore

Replace the following:

     * `CONTAINER_NAME`: the name that you assigned to the AlloyDB Omni container when you installed it—for example, `my-omni`.

     * `STANZA`: the configuration stanza, defined by the `pgbackrest.conf` file, to apply to this restore—for example, `omni`.

     * `TIMESTAMP`: the time to restore to—for example, `2024-02-22 19:50:00`.

###  Podman 
    
    podman exec CONTAINER_NAME pgbackrest \
      --config-path=/var/lib/postgresql/data \
      --stanza=STANZA \
      --type=time \
      --pg1-path=/var/lib/postgresql/data/data-RESTORED \
      --target="TIMESTAMP" \
      restore

Replace the following:

     * `CONTAINER_NAME`: the name that you assigned to the AlloyDB Omni container when you installed it—for example, `my-omni`.

     * `STANZA`: the configuration stanza, defined by the `pgbackrest.conf` file, to apply to this restore—for example, `omni`.

     * `TIMESTAMP`: the time to restore to—for example, `2024-02-22 19:50:00`.

  2. On the target environment, stop the container using the following command:

###  Docker 
         
         docker container stop CONTAINER_NAME

###  Podman 
         
         podman container stop CONTAINER_NAME

  3. Rename the `data` subdirectory of your data directory, as a safety precaution:
         
         cd DATA_DIR
         sudo mv data data-OLD

Replace `DATA_DIR` with the file system path to your AlloyDB Omni data directory.

  4. Move the restored data into place, and clean up `postgresql.auto.conf`:
         
         sudo mv data-RESTORED data
         sudo sed -i 's|data-RESTORED|data|' data/postgresql.auto.conf

  5. Start the AlloyDB Omni container with the database server:

###  Docker 
         
         docker container start CONTAINER_NAME

###  Podman 
         
         podman container start CONTAINER_NAME




You can now connect to your database using `psql` and confirm that the data has been restored as you expect. If so, you can delete the `data-OLD` copy of the `data` subdirectory that you created earlier.

For more information about PITR in pgBackRest, see [Point-in-Time Recovery](https://pgbackrest.org/user-guide.html#pitr). For more information about preparing a `pgbackrest.conf` file for use with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/set-up-pgbackrest).

## Other options

The `pgbackrest restore` command is very flexible, with an array of options and features that you can control through passing in different command-line options. These include the following:

  * Limiting a restore only to changed files.
  * Restoring only selected databases.



For a complete guide to performing restores in pgBackRest, see [Restore](https://pgbackrest.org/user-guide.html#restore).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
