---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/restore-pgbackrest/
title: Restore an AlloyDB Omni cluster using pgBackRest \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:53:28.302330+00:00
---

# Restore an AlloyDB Omni cluster using pgBackRest  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/restore-pgbackrest/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Restore an AlloyDB Omni cluster using pgBackRest Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/restore-pgbackrest)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/restore-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/restore-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/restore-pgbackrest)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/restore-pgbackrest)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/restore-pgbackrest)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/restore-pgbackrest)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/restore-pgbackrest)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/restore-pgbackrest)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/restore-pgbackrest)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/restore-pgbackrest)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/restore-pgbackrest)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/restore-pgbackrest)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/restore-pgbackrest)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/restore-pgbackrest)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/restore-pgbackrest)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/restore-pgbackrest)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/restore-pgbackrest)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/restore-pgbackrest)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/restore-pgbackrest)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/restore-pgbackrest)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/restore-pgbackrest)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/restore-pgbackrest)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/restore-pgbackrest)

This page shows you how to restore an AlloyDB Omni cluster using a backup created with [pgBackRest](https://pgbarman.org/), the open-source backup solution included with the AlloyDB Omni Docker container. 

Because AlloyDB Omni is compatible with PostgreSQL, the data-restoration commands and techniques described by [the pgBackRest manual](https://pgbackrest.org/user-guide.html) apply to AlloyDB Omni as well. This page demonstrates a selection of common recovery tasks, with examples of relevant commands.

For more information about configuring pgBackRest to work with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-pgbackrest).

The information on this page applies only to AlloyDB Omni for containers. It does not apply to AlloyDB Omni for Kubernetes.

## Before you begin

Before configuring AlloyDB Omni to work with pgBackrest, you need to have [AlloyDB Omni installed and running](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install) on a server that you control.

  * A target database server, running the same major version of AlloyDB Omni as the source database server. For more information about installing AlloyDB Omni, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install).

The target server can be the same machine as the source server.

  * A pgBackRest backup repository containing at least one backup of the source AlloyDB Omni database.

  * Enough free disk space on the target server to hold the restored database.




## Overview

To perform a AlloyDB Omni restore using pgBackRest, run [the `pgbackrest restore` command](https://pgbackrest.org/command.html#command-restore). The arguments that you provide the command vary depending upon your situation.

In general, you run the `pgbackrest restore` command with flags that provide the following information:

  * The location of your `pgbackrest.conf` file.
  * The name of pgBackRest backup repository that you want to restore from. These repositories are named and defined in the `pgbackest.conf` file.
  * The location on the local file system to write the restored data to.
  * An identifier of the particular backup or point in time that you want to restore from.



When running the containerized `pgbackrest restore` commands, remember to use file system paths from the container's point of view. For example, the path to your AlloyDB Omni data directory is always `/mnt/disks/pgsql`, no matter its location on your host server. For more information, see [A note about file system paths](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-pgbackrest#paths).

## Perform a point-in-time restore

This example restores data from a pgBackRest repository, naming a particular point in time to restore from. If you have defined multiple repositories in the target environment's the `pgbackrest.conf` file, then pgBackRest chooses the repository to restore from based on availability, expected speed, and other factors.

The example assumes the following:

  * You have a `pgbackrest.conf` file located at the top level of your target AlloyDB Omni data directory. This makes the file available to the containerized `pgbackrest` as `/mnt/disks/pgsql/pgbackrest.conf`.

  * [You have enabled continuous backups](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/set-up-pgbackrest#continuous) with your pgBackRest configuration.



  1. In the target environment, perform a PITR restore, specifying a timestamp to restore from:
         
         sudo docker exec pg-service pgbackrest \
           --config-path=/mnt/disks/pgsql \
           --stanza=STANZA \
           --type=time \
           --pg1-path=/mnt/disks/pgsql/data-RESTORED \
           --target="TIMESTAMP" \
           restore

Replace the following:

     * `STANZA`: the configuration stanza, defined by the `pgbackrest.conf` file, to apply to this restore—for example, `omni`.

     * `TIMESTAMP`: the time to restore from—for example, `2024-02-22 19:50:00`.

  2. On the target environment, stop the database server:
         
         sudo alloydb database-server stop

  3. Rename the `data` subdirectory of your data directory, as a safety precaution:
         
         cd DATA_DIR
         sudo mv data data-OLD

Replace `DATA_DIR` with the file system path to your AlloyDB Omni data directory.

  4. Move the restored data into place, and clean up `postgresql.auto.conf`:
         
         sudo mv data-RESTORED data
         sudo sed -i 's|data-RESTORED|data|' data/postgresql.auto.conf

  5. Start the database server:
         
         sudo alloydb database-server start




You can now connect to your database using `psql` and confirm that the data has been restored as you expect. If so, you can delete the `data-OLD` copy of the `data` subdirectory that you created earlier.

For more information about PITR in pgBackRest, see [Point-in-Time Recovery](https://pgbackrest.org/user-guide.html#pitr). For more information about preparing a `pgbackrest.conf` file for use with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/15.5.2/docs/set-up-pgbackrest).

## Other options

The `pgbackrest restore` command is very flexible, with an array of options and features that you can control through passing in different command-line options. These include the following:

  * Limiting a restore only to changed files.
  * Restoring only selected databases.



For a complete guide to performing restores in pgBackRest, see [Restore](https://pgbackrest.org/user-guide.html#restore).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
