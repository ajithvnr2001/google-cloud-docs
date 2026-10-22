---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-configure-barman/
title: Set up Barman for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using containers: 15.18.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:18.491195+00:00
---

# Set up Barman for AlloyDB Omni  |  AlloyDB Omni using containers: 15.18.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-configure-barman/

This page documents AlloyDB Omni version **15.18.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/overview)



Send feedback 

#  Set up Barman for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.18.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-configure-barman)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-configure-barman)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/install-configure-barman)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/install-configure-barman)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/install-configure-barman)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/install-configure-barman)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/install-configure-barman)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/install-configure-barman)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/install-configure-barman)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/install-configure-barman)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/install-configure-barman)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-configure-barman)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/install-configure-barman)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install-configure-barman)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install-configure-barman)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/install-configure-barman)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/install-configure-barman)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/install-configure-barman)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/install-configure-barman)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/install-configure-barman)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install-configure-barman)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-configure-barman)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/install-configure-barman)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/install-configure-barman)

This page shows you how to protect your data by configuring AlloyDB Omni to work with [Barman](https://pgbarman.org/), an open-source database backup server. 

The information on this page applies only to AlloyDB Omni using containers. It does not apply to AlloyDB Omni using the container orchestrator.

You can protect your AlloyDB Omni data using any database backup technology that works with PostgreSQL. For example, you can configure AlloyDB Omni to allow connections from a Barman server that you control. This enables the Barman server to perform continuous backups of the data stored in your AlloyDB Omni server.

After you configure your Barman and AlloyDB Omni servers to work together, you can subsequently [run Barman commands](https://docs.pgbarman.org/release/latest/#general-commands) to accomplish a variety of data-protection and disaster-recovery tasks, including the following:

  * Create an on-demand backup of your data.
  * Set up synchronous WAL streaming of your data changes to your backup server.
  * Restore from a specific backup.
  * Perform a point-in-time restoration.



For more information about the operation of Barman, see [the Barman manual](https://docs.pgbarman.org/release/latest/).

## Before you begin

Before configuring AlloyDB Omni to work with Barman, you need the following:

  * [AlloyDB Omni installed and running](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/install) on a server that you control.

  * [Barman installed](https://docs.pgbarman.org/release/latest/#installation) on a separate server. The server that you installed Barman on must be able to communicate with the AlloyDB Omni server over TCP.




## Configure AlloyDB Omni to work with Barman

To prepare your AlloyDB Omni server to work with Barman, run the following commands on the server where you have installed AlloyDB Omni.

  1. Create the `barman` database user, with the appropriate privileges:

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -c "
         CREATE USER barman;
         GRANT EXECUTE ON FUNCTION pg_backup_start(text, boolean) to barman;
         GRANT EXECUTE ON FUNCTION pg_backup_stop(boolean) to barman;
         GRANT EXECUTE ON FUNCTION pg_switch_wal() to barman;
         GRANT EXECUTE ON FUNCTION pg_create_restore_point(text) to barman;
         GRANT pg_read_all_settings TO barman;
         GRANT pg_read_all_stats TO barman;
         CREATE USER streaming_barman WITH REPLICATION;
         "

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

###  Podman 
         
         podman exec CONTAINER_NAME psql -h localhost -U postgres -c "
         CREATE USER barman;
         GRANT EXECUTE ON FUNCTION pg_backup_start(text, boolean) to barman;
         GRANT EXECUTE ON FUNCTION pg_backup_stop(boolean) to barman;
         GRANT EXECUTE ON FUNCTION pg_switch_wal() to barman;
         GRANT EXECUTE ON FUNCTION pg_create_restore_point(text) to barman;
         GRANT pg_read_all_settings TO barman;
         GRANT pg_read_all_stats TO barman;
         CREATE USER streaming_barman WITH REPLICATION;
         "

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

  2. Add the following lines in the `DATA_DIR/pg_hba.conf` file **before** the `host all all all scram-sha-256` line that exists in the file:
         
         host all barman BARMAN_IP/32 AUTHN_METHOD
         host replication streaming_barman BARMAN_IP/32 AUTHN_METHOD
         

Replace the following:

     * `DATA_DIR`: the file system path used for the AlloyDB Omni data directory.

     * `BARMAN_IP`: the IP address of the Barman server.

     * `AUTHN_METHOD`: the PostgreSQL authentication method that your AlloyDB for PostgreSQL server expects from the Barman server. We recommend one of the following values:

       * To allow the Barman server to authenticate without a password, use `trust`.

       * To require a password from the Barman server, use `scram-sha-256`.

  3. Add the following lines to the `DATA_DIR/postgresql.conf` file:
         
         archive_command='/bin/true'
         archive_mode=on
         listen_addresses='*'
         wal_level='replica'
         

  4. Restart the AlloyDB Omni service:

###  Docker 
         
         docker restart CONTAINER_NAME

###  Podman 
         
         podman restart CONTAINER_NAME

Replace `CONTAINER_NAME` with the name that you assigned to the AlloyDB Omni container when you installed it.

  5. Confirm the necessary parameters are all set appropriately by running the following command:

###  Docker 
         
         docker exec CONTAINER_NAME psql -h localhost -U postgres -c "
         SELECT name, setting
            FROM pg_catalog.pg_settings
            WHERE name IN ('archive_command',
                           'archive_mode',
                           'listen_addresses',
                           'wal_level')
            ORDER BY name;"

###  Podman 
         
         podman exec CONTAINER_NAME psql -h localhost -U postgres -c "
         SELECT name, setting
            FROM pg_catalog.pg_settings
            WHERE name IN ('archive_command',
                           'archive_mode',
                           'listen_addresses',
                           'wal_level')
            ORDER BY name;"

The output is as follows:
         
         name          |  setting
         ------------------|-----------
         archive_command   | /bin/true
         archive_mode      | on
         listen_addresses  | *
         wal_level         | replica
         (4 rows)
         




## Set up the Barman backup server

To set up and configure Barman to work with your AlloyDB Omni server, run the following commands on your Barman server.

  1. Verify that the streaming replication connection works:
         
         psql -h DATABASE_IP -U streaming_barman -c "IDENTIFY_SYSTEM" replication=1

The output is similar to the following:
         
         systemid       | timeline |  xlogpos   | dbname
         ---------------------+----------+------------+--------
          7265722823667040273 |        1 | 0/1F0AFCD0 |
         (1 row)
         

  2. Ensure that Barman can connect to the AlloyDB Omni server as the `barman` database user.
         
         psql -t -h DATABASE_IP -U barman -d postgres -c "SELECT 'Connected as: '||current_user"

Replace `DATABASE_IP` with the IP address of your AlloyDB Omni server.

The output is similar to the following:
         
         Connected as: barman
         

  3. [Configure the Barman backup server](https://docs.pgbarman.org/release/latest/#setup-of-a-new-server-in-barman) according to your needs and preferences.

Your configuration must include the following settings:

     * Set `conninfo` to connect to the AlloyDB Omni `postgres` database as the `barman` user.
     * Set `streaming_conninfo` to use the `streaming_barman` user.
     * Configure other directives required to enable WAL streaming, as directed by the Barman documentation.

The following minimal but complete example modifies [a streaming-configuration example from the Barman documentation](https://docs.pgbarman.org/release/latest#examples-of-configuration):
    
    [CONFIGURATION_TAG]
    description = "Backup settings for my AlloyDB Omni server"
    conninfo = host=DATABASE_IP user=barman dbname=postgres
    streaming_conninfo = host=DATABASE_IP user=streaming_barman
    backup_method = postgres
    streaming_archiver = on
    slot_name = barman
    

Replace the following:

     * `CONFIGURATION_TAG`: a short tag to identify this server configuration when running `barman` commands—for example, `omni`.

     * `DATABASE_IP`: the IP address of your AlloyDB Omni server.

  4. Switch to the `barman` user.
         
         sudo su - barman

  5. Use [the `barman receive-wal` command](https://docs.pgbarman.org/release/3.10.0/#receive-wal) to create a replication slot, and then begin receiving a WAL stream from the database server:
         
         barman receive-wal --create-slot CONFIGURATION_TAG
         barman receive-wal CONFIGURATION_TAG &

Replace `CONFIGURATION_TAG` with the configuration tag that you chose in the previous step.




Barman is now configured to work with your AlloyDB Omni server. To check the replication status, create manual backups, and perform other tasks, see [General commands](https://docs.pgbarman.org/release/latest/#general-commands).

For example, to create a manual backup, run [the `barman backup` command](https://docs.pgbarman.org/release/latest/#backup).

## What's next

  * [Restore an AlloyDB Omni cluster using Barman](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/clone-omni-barman)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
