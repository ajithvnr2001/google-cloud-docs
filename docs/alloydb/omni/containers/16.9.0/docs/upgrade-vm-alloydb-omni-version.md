---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/upgrade-vm-alloydb-omni-version/
title: Upgrade to AlloyDB Omni version 16.9.0 on a VM \u00a0|\u00a0 AlloyDB Omni for containers: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:28:04.065539+00:00
---

# Upgrade to AlloyDB Omni version 16.9.0 on a VM  |  AlloyDB Omni for containers: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/upgrade-vm-alloydb-omni-version/

This page documents AlloyDB Omni version **16.9.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/overview)



Send feedback 

#  Upgrade to AlloyDB Omni version 16.9.0 on a VM Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/upgrade-vm-alloydb-omni-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/upgrade-vm-alloydb-omni-version)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-vm-alloydb-omni-version)

This page describes how to upgrade your AlloyDB Omni PostgreSQL 15-based containers to AlloyDB Omni PostgreSQL 16 using `pg_upgrade`. The instructions in this page describe upgrade steps for AlloyDB Omni deployed as a standalone server and for AlloyDB Omni configured as replicated standby nodes. Using `pg_upgrade` helps to ensure that the upgrade completes without data loss. 

For more information about PostgreSQL upgrade options, see [pg_upgrade](https://www.postgresql.org/docs/current/pgupgrade.html).

## Before you begin

  * Before you initiate the upgrade, we recommend that you take a full backup of your database cluster.
  * To ensure that the AlloyDB Omni 15 service is running, execute the following command:

### Docker
        
        docker exec ALLOYDB15_CONTAINER psql -U postgres -c "SELECT 1;"
        

### Podman
        
        podman exec ALLOYDB15_CONTAINER psql -U postgres -c "SELECT 1;"
        

  * The `pg_squeeze` extension in PostgreSQL 15 isn't supported in AlloyDB Omni PostgreSQL 16.9.0. If `pg_squeeze` is in your AlloyDB Omni 15 installation, you must remove the extension before you perform the upgrade to AlloyDB Omni 16.

If you installed custom extensions on top of AlloyDB Omni, make sure that those custom extensions are also installed in the 16.9.0 image. Check the installed extensions by running the following command:

### Docker
        
        docker exec ALLOYDB15_CONTAINER psql -U postgres -d postgres -c "
        SELECT * FROM pg_extension;"
        

### Podman
        
        podman exec ALLOYDB15_CONTAINER psql -U postgres -d postgres -c "
        SELECT * FROM pg_extension;
        

  * If you're upgrading from AlloyDB Omni version 15.5.2 or earlier, you must first upgrade to a more recent version of AlloyDB Omni 15\. [Migrate from AlloyDB Omni version 15.5.2 and earlier to the latest version](https://docs.cloud.google.com/alloydb/omni/15.7.1/docs/migrate-to-latest-version).




## Upgrade AlloyDB Omni in a Docker container environment

To upgrade from AlloyDB Omni PostgreSQL 15 to AlloyDB Omni PostgreSQL 16.9.0 in a Docker or Podman container environment, follow these steps:

### Docker

  1. Copy `bin` and share the directory from the version of the AlloyDB Omni container that you want to upgrade:
         
         mkdir -p TMP/alloydb15_bin TMP/alloydb15_share
         docker cp ALLOYDB15_CONTAINER:/usr/lib/postgresql/15 TMP/alloydb15_bin
         docker cp ALLOYDB15_CONTAINER:/usr/share/postgresql/15 TMP/alloydb15_share
         

  2. Create a new data directory for the AlloyDB Omni PostgreSQL 16 container where the upgraded data will be stored:
         
         mkdir -p DATA_PATH/16/data
         chown 999 DATA_PATH/16/data
         

**Note:** If you're using a UBI-based AlloyDB Omni image, run the following command instead, because the `postgres` user in UBI-based images runs with UID 26:  

         
         chown 26 DATA_PATH/16/data

  3. Start the AlloyDB Omni PostgreSQL 16 running container with all the paths mounted in the same network as the previous AlloyDB Omni container. See the following example:
         
         docker run -d --name ALLOYDB16_CONTAINER \
           -e POSTGRES_PASSWORD=PASSWORD -e PGPORT=5433 \
           -v DATA_PATH/16/data:/var/lib/postgresql/data \
           -v DATA_PATH/15/data:/var/lib/postgresql/old_data \
           -v TMP/alloydb15_bin/15:/usr/lib/postgresql/15 \
           -v TMP/alloydb15_share/15:/usr/share/postgresql/15 \
           --network container:ALLOYDB15_CONTAINER \
           google/alloydbomni:IMAGE_TAG /bin/sleep infinity
         

**Note:** If you're using a UBI-based AlloyDB Omni image, run the following commands to set the correct permissions for the data directory:  

         
         docker exec ALLOYDB16_CONTAINER bash -c "
         chown -R 999:999 /var/lib/postgresql/data /var/lib/postgresql/old_data && \
         chmod -R 700 /var/lib/postgresql/data /var/lib/postgresql/old_data
         "
         

  4. Initialize the new data directory for the upgraded version of container.
         
         docker exec -u postgres ALLOYDB16_CONTAINER bash -c "
           cd /tmp;
           initdb -D /var/lib/postgresql/data --frozen-collations --encoding=UTF8 --locale=C --locale-provider=icu --icu-locale=und-x-icu
         

If the old cluster had any special settings, for example, `--data-checksum` or `--locale`, then you must also pass those parameters to create the AlloyDB Omni 16 container.

  5. If you enabled the restart policy on the earlier version container, then you must disable the restart policy, as shown in the following example:
         
         docker update --restart=no ALLOYDB15_CONTAINER
         

  6. Run `pg_upgrade --check` to verify that the cluster is ready to be upgraded to AlloyDB Omni 16.

**Note:** When you execute use the `--check` command, `pg_upgrade` shuts down the PostgreSQL 15 container. If you have failure detectors like `systemd` or `supervisord`, which automatically restart your AlloyDB Omni instance, make sure to disable the failure detectors so that they don't interfere with `pg_upgrade` operations.
         
         docker exec -u postgres ALLOYDB16_CONTAINER bash -c "
          cd /tmp;
         
          pg_upgrade -p 5432 -P 5433 --check -v \
                     -b /usr/lib/postgresql/15/bin \
                     -B /usr/lib/postgresql/16/bin \
                     -d /var/lib/postgresql/old_data \
                     -D /var/lib/postgresql/data"
         

After the `pg_upgrade --check` command completes, you see an output that ends with `Clusters are compatible`, which indicates that the cluster is ready to be upgraded. This command also checks and shuts down the AlloyDB Omni PostgreSQL 15 container. After `pg_upgrade --check` completes, applications are no longer able to connect to the database or execute any queries.

  7. Run `pg_upgrade` to copy the upgraded data onto the new data directory, and then verify that `pg_upgrade` completed successfully and that the AlloyDB Omni PostgreSQL 15 container exited:
         
         docker exec -u postgres ALLOYDB16_CONTAINER bash -c "
           cd /tmp;
           pg_upgrade -v --copy \
                -b /usr/lib/postgresql/15/bin \
                -B /usr/lib/postgresql/16/bin \
                -d /var/lib/postgresql/old_data \
                -D /var/lib/postgresql/data"
         
         docker ps -a
         

  8. If `pg_upgrade` fails, roll back to the AlloyDB Omni PostgreSQL 15 container by starting the PostgreSQL 15 container:
         
         docker logs ALLOYDB16_CONTAINER
         docker rm -f ALLOYDB15_CONTAINER ALLOYDB16_CONTAINER
         docker run -d --name ALLOYDB15_CONTAINER -p 5432:5432 \
           -e POSTGRES_PASSWORD=postgres \
           -v DATA_PATH/15/data:/var/lib/postgresql/data \
           google/alloydbomni:15
         

To determine the reasons for the upgrade failure, review the logs.

  9. If the upgrade is successful, clean up and then restart the AlloyDB Omni PostgreSQL 16 container:
         
         docker rm -f ALLOYDB16_CONTAINER ALLOYDB15_CONTAINER
         docker run -d --name ALLOYDB16_CONTAINER -p 5432:5432 \
           -e POSTGRES_PASSWORD=postgres \
           -v DATA_PATH/16/data:/var/lib/postgresql/data \
           google/alloydbomni:16
         




### Podman

  1. Copy `bin` and share the directory from the version of the AlloyDB Omni container that you want to upgrade:
         
         mkdir -p TMP/alloydb15_bin TMP/alloydb15_share
         podman cp ALLOYDB15_CONTAINER:/usr/lib/postgresql/15 TMP/alloydb15_bin
         podman cp ALLOYDB15_CONTAINER:/usr/share/postgresql/15 TMP/alloydb15_share
         

  2. Create a new data directory for the AlloyDB Omni PostgreSQL 16 container where the upgraded data will be stored:
         
         mkdir -p DATA_PATH/16/data
         chown 999 DATA_PATH/16/data
         

  3. Start the AlloyDB Omni PostgreSQL 16 running container with all the paths mounted in the same network as the previous AlloyDB Omni container. See the following example:
         
         podman run -d --name ALLOYDB16_CONTAINER \
           -e POSTGRES_PASSWORD=PASSWORD -e PGPORT=5433 \
           -v DATA_PATH/16/data:/var/lib/postgresql/data \
           -v DATA_PATH/15/data:/var/lib/postgresql/old_data \
           -v TMP/alloydb15_bin/15:/usr/lib/postgresql/15 \
           -v TMP/alloydb15_share/15:/usr/share/postgresql/15 \
           --network container:ALLOYDB15_CONTAINER \
           google/alloydbomni:16 /bin/sleep infinity
         

  4. Initialize the new data directory for the upgraded version of container.
         
         podman exec -u postgres ALLOYDB16_CONTAINER bash -c "
           cd /tmp;
           initdb -D /var/lib/postgresql/data --frozen-collations --encoding=UTF8 --locale=C --locale-provider=icu --icu-locale=und-x-icu
         

If the old cluster had any special settings, for example, `--data-checksum` or `--locale`, then you must also pass those parameters to create the AlloyDB Omni 16 container.

  5. If you enabled the restart policy on the earlier version container, then you must disable the restart policy, as shown in the following example:
         
         podman update --restart=no ALLOYDB15_CONTAINER
         

  6. Run `pg_upgrade --check` to verify that the cluster is ready to be upgraded to AlloyDB Omni 16.

**Note:** When you execute use the `--check` command, `pg_upgrade` shuts down the PostgreSQL 15 container. If you have failure detectors like `systemd` or `supervisord`, which automatically restart your AlloyDB Omni instance, make sure to disable the failure detectors so that they don't interfere with `pg_upgrade` operations.
         
         podman exec -u postgres ALLOYDB16_CONTAINER bash -c "
          cd /tmp;
         
          pg_upgrade -p 5432 -P 5433 --check -v \
                     -b /usr/lib/postgresql/15/bin \
                     -B /usr/lib/postgresql/16/bin \
                     -d /var/lib/postgresql/old_data \
                     -D /var/lib/postgresql/data"
         

After the `pg_upgrade --check` command completes, you see an output that ends with `Clusters are compatible`, which indicates that the cluster is ready to be upgraded. This command also checks and shuts down the AlloyDB Omni PostgreSQL 15 container. After `pg_upgrade --check` completes, applications are no longer able to connect to the database or execute any queries.

  7. Run `pg_upgrade` to copy the upgraded data onto the new data directory, and then verify that `pg_upgrade` completed successfully and that the AlloyDB Omni PostgreSQL 15 container exited:
         
         podman exec -u postgres ALLOYDB16_CONTAINER bash -c "
           cd /tmp;
           pg_upgrade -v --copy \
                -b /usr/lib/postgresql/15/bin \
                -B /usr/lib/postgresql/16/bin \
                -d /var/lib/postgresql/old_data \
                -D /var/lib/postgresql/data"
         
         podman ps -a
         

  8. If `pg_upgrade` fails, roll back to the AlloyDB Omni PostgreSQL 15 container by starting the PostgreSQL 15 container:
         
         podman logs ALLOYDB16_CONTAINER
         podman rm -f ALLOYDB15_CONTAINER ALLOYDB16_CONTAINER
         podman run -d --name ALLOYDB15_CONTAINER -p 5432:5432 \
           -e POSTGRES_PASSWORD=postgres \
           -v DATA_PATH/15/data:/var/lib/postgresql/data \
           google/alloydbomni:15
         

To determine the reasons for the upgrade failure, review the logs.

  9. If the upgrade is successful, clean up and then restart the AlloyDB Omni PostgreSQL 16 container:
         
         podman rm -f ALLOYDB16_CONTAINER ALLOYDB15_CONTAINER
         podman run -d --name ALLOYDB16_CONTAINER -p 5432:5432 \
           -e POSTGRES_PASSWORD=postgres \
           -v DATA_PATH/16/data:/var/lib/postgresql/data \
           google/alloydbomni:16
         




### Upgrade the AlloyDB Omni server on standby node

If your AlloyDB Omni server is deployed with an active and streaming replicated standby configuration, then you can't run `pg_upgrade` on the standby node. To upgrade the AlloyDB Omni server on a standby node, we recommend that, before you upgrade AlloyDB Omni on the active node, you ensure that there are no replication lags on the standby node.

To upgrade the standby AlloyDB Omni server, you follow these high-level steps:

  1. Stop the standby AlloyDB Omni container before you upgrade Active node.
  2. After the active node is upgraded, sync the upgraded data directory from the new active node to the standby node using [rsync](https://en.wikipedia.org/wiki/Rsync). For more information about upgrading a streaming replicated standby server, see [`pg_upgrade`](https://www.postgresql.org/docs/16/pgupgrade.html).
  3. Start the container using the AlloyDB for PostgreSQL PostgreSQL 16 image using the same data directory.



If you're using logical replication, see [Upgrading Data via Replication](https://www.postgresql.org/docs/16/upgrading.html#UPGRADING-VIA-REPLICATION).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
