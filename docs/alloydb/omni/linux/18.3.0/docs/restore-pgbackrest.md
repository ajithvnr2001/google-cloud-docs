---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/restore-pgbackrest/
title: Restore from a pgBackRest-based backup for AlloyDB Omni on Linux \u00a0|\u00a0 AlloyDB Omni using RPM: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:00.843733+00:00
---

# Restore from a pgBackRest-based backup for AlloyDB Omni on Linux  |  AlloyDB Omni using RPM: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/restore-pgbackrest/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)



Send feedback 

#  Restore from a pgBackRest-based backup for AlloyDB Omni on Linux Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/restore-pgbackrest)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/restore-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/restore-pgbackrest)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/restore-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/restore-pgbackrest)

This page shows you how to restore an AlloyDB Omni cluster using a backup created with [pgBackRest](https://pgbackrest.org/), the open-source backup solution included with the AlloyDB Omni. 

Because AlloyDB Omni is compatible with PostgreSQL, the data-restoration commands and techniques described by [the pgBackRest manual](https://pgbackrest.org/user-guide-index.html) apply to AlloyDB Omni as well. This page demonstrates a selection of common recovery tasks, with examples of relevant commands.

TDE-enabled clusters also support backup and restores using pgBackRest. For more information, see [Create a TDE-enabled cluster](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/create-tde-cluster).

For more information about configuring pgBackRest to work with AlloyDB Omni, see [Set up pgBackRest for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/set-up-pgbackrest).

## Before you begin

Before restoring an AlloyDB Omni cluster, ensure that you have the following:

  * Run `sudo dnf install pgbackrest` to install pgBackRest.

  * [Set up and configure pgBackRest](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/set-up-pgbackrest) for your AlloyDB Omni instance. 

  * Sufficient disk space on destination file system to store the restored AlloyDB Omni database cluster.

  * Same major version of AlloyDB Omni used for the restoration database instance as the original source database instance.

To check your version of PostgreSQL, run the following command:
        
        /usr/lib/postgresql/18/bin/psql -h localhost -U postgres -c "SELECT version();"
        

To check your version of pgBackRest, run the following command:
        
        pgbackrest version
        

If your target database instance has a different version of PostgreSQL, pgBackRest, or both, then you need to create a new target database instance with a matching version. If this is not possible, then you need to use an alternative method, such as the PostgreSQL included `pg_dump` or `pg_dumpall` utilities to copy your databases across versions.




## Stop AlloyDB Omni

To simulate your AlloyDB Omni database cluster not being available, stop the service.
    
    
    sudo systemctl stop 18
    

## Remove your data directory

To clear your AlloyDB Omni database cluster, remove the data directory.
    
    
    sudo rm -rf DATA_DIR/*
    

Replace the following variable:

  * `DATA_DIR`: Host directory path that your data is stored in. 



## Validate that your backups are visible
    
    
    sudo -u postgres pgbackrest \
    --config-path=/var/lib/BACKUP_DIR \
    --stanza=STANZA_NAME \
    info
    

Replace the following variables:

* `STANZA_NAME`: Name of the stanza you created. For example, `my-stanza`.

## Restore your backup
    
    
    sudo -u postgres pgbackrest \
    --stanza=STANZA_NAME \
    restore
    

Replace the following variables:

* `STANZA_NAME`: Name of the stanza you created. For example, `my-stanza`. 

## Start AlloyDB Omni

Start the AlloyDB Omni service.
    
    
    sudo systemctl start 18
    

## Validate that AlloyDB Omni started
    
    
    sudo systemctl status 18
    

## Other options

The pgBackRest `restore` command is very flexible, with an array of options and features that you can control through passing in different command-line options. For a complete guide to performing restores, see [Restore](https://pgbackrest.org/user-guide.html#restore). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
