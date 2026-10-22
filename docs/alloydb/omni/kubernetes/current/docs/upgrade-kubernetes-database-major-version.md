---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-database-major-version/
title: Upgrade to AlloyDB Omni version 18.4.0 on 1.9.0 \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:43:00.664136+00:00
---

# Upgrade to AlloyDB Omni version 18.4.0 on 1.9.0  |  AlloyDB Omni using the container orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-database-major-version/

This page documents AlloyDB Omni version **18.4.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/overview)



Send feedback 

#  Upgrade to AlloyDB Omni version 18.4.0 on 1.9.0 Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-database-major-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/upgrade-kubernetes-database-major-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-database-major-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-database-major-version)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/upgrade-kubernetes-database-major-version)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-database-major-version)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/upgrade-kubernetes-database-major-version)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/upgrade-kubernetes-database-major-version)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/upgrade-kubernetes-database-major-version)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/upgrade-kubernetes-database-major-version)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/upgrade-kubernetes-database-major-version)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-database-major-version)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/upgrade-kubernetes-database-major-version)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/upgrade-kubernetes-database-major-version)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/upgrade-kubernetes-database-major-version)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/upgrade-kubernetes-database-major-version)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-database-major-version)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-database-major-version)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/upgrade-kubernetes-database-major-version)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/upgrade-kubernetes-database-major-version)

This page describes how to perform a major version upgrade to AlloyDB Omni version 18.4.0 on Kubernetes. 

## Before you begin

  * Verify that your AlloyDB Omni Kubernetes operator version is `1.9.0`. To upgrade your AlloyDB Omni operator version, see [Migrate to the latest AlloyDB Omni Kubernetes operator version](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-operator-version).

  * Verify that you have at least 5GB of free disk space.

  * If you run external or remote backup systems, perform a full backup and pause any scheduled backups to avoid backing up during the upgrade process.

  * For [high availability (HA) and data resilience (DR)](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/high-availability/overview) environments, decouple your database clusters before upgrading them.


**Note:** Starting with AlloyDB Omni Kubernetes operator version 1.6.0, you can specify the base operating system for the database image using the `databaseImageOSType` field in your `DBCluster` manifest. The recommended value is `UBI9` for improved security and compatibility. If you need to continue using Debian-based images, you can set this field to `Debian`. During a major version upgrade, you can set this field in the patch command.

## Upgrade your AlloyDB Omni version

To upgrade your AlloyDB Omni version using `pg_upgrade`, do one of the following:

  * Run the Bash script that performs the upgrade for you.

  * Run the upgrade instructions manually.




## Perform scripted upgrade

You can find a script that performs the manual upgrade steps in the [AlloyDB Omni samples on GitHub](https://github.com/GoogleCloudPlatform/alloydb-omni-samples/tree/main/samples/MVU.sh).

To use the upgrade script, download the script and run the following command:
    
    
    ./MVU.sh 18.4.0 1.9.0 NAME NAMESPACE OS_TYPE
    

Replace the following variables:

  * NAME: the name of your database cluster.
  * NAMESPACE: the namespace for your database cluster.
  * OS_TYPE: the base operating system for the database image. Valid values are `Debian` and `UBI9`. If not specified, the operator defaults to `UBI9` for database versions 16.9.0 and later.



## Perform manual upgrade steps

**Important:** Due to an extension incompatibility issue, direct major version upgrades from some versions fail. Before you perform a major version upgrade, you might need to perform a minor version upgrade first. 

The following upgrade paths are not supported:

  * From version `15.12.0` and lower to `17.5.0` or `16.9.0`
  * From version `16.8.0` and lower to `17.5.0`



To upgrade from these versions, you must perform a minor version upgrade as an intermediate step:

  * From `15.12.0` and lower, first upgrade to `15.13.0`.
  * From `16.8.0` and lower, first upgrade to `16.9.0`.



For example, to upgrade from version `15.12.0` to `17.5.0`, you must follow this path: `15.12.0` > `15.13.0` > `17.5.0`

Follow the instructions for the major version you upgrade from.

### Upgrade from version 17.x.x to 18.1.0

  1. [Back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes) to avoid any data loss.

  2. [Remove your backup plan](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes#disable).

  3. Terminate all replication processes. This includes physical replication used for [high availability (HA) and data resilience (DR)](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-ha) as well as all [logical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-replication-slots) streams.

  4. Annotate your database cluster to specify a manual version upgrade.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME dbs.dbadmin.goog.com/manualmvu=true
         

Replace the following variable:

     * NAME: the name of your database cluster.
  5. Stop the PostgreSQL process and move the data for the upgrade.
         
         kubectl exec -ti POD_NAME -- /bin/Bash
         # Shut down postgres
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         postgres@POD_NAME:~$ mkdir /mnt/disks/pgsql/17; mv /mnt/disks/pgsql/data /mnt/disks/pgsql/17/data; cp -r /usr/lib/postgresql/17/bin /mnt/disks/pgsql/17/.; cp -r /usr/lib/postgresql/17/lib /mnt/disks/pgsql/17/.; cp -r /usr/share/postgresql/17 /mnt/disks/pgsql/17/share; rm /mnt/disks/pgsql/17/share/postgresql.conf.sample; cp /usr/share/postgresql/postgresql.conf.sample /mnt/disks/pgsql/17/share/postgresql.conf.sample; chmod 2740 /mnt/disks/pgsql/17/data
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  6. Patch your database cluster to version `18.4.0` and your control plane agents (CPA) to `1.9.0`.
         
         kubectl patch dbclusters.alloydbomni.dbadmin.goog NAME --type=merge -p '{"spec":{"databaseVersion":"18.4.0","controlPlaneAgentsVersion":"1.9.0","databaseImageOSType":"UBI9"}}'
         

Replace the following variable:

     * NAME: the name of your database cluster.
**Note:** For database versions 16.9.0 and later, specifying `databaseImageOSType:"UBI9"` is optional, as `UBI9` is the default base OS. If you want to use the Debian-based image, you must explicitly set this field to `"Debian"`.
  7. Create an empty database cluster for the upgraded AlloyDB Omni version.
         
         kubectl exec -ti POD_NAME -- /bin/Bash
         
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         # Initialize a new, empty database cluster for the new version.
         postgres@POD_NAME:~$ rm -fr /mnt/disks/pgsql/data; initdb -D /mnt/disks/pgsql/data -U alloydbadmin --data-checksums --encoding=UTF8 --locale=C --locale-provider=icu --icu-locale=und-x-icu --auth-host=trust --auth-local=reject; cd ~
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  8. Modify `pg_hba.conf` in your pre-existing database cluster to provide the upgrade process the permissions and connections it needs.
         
         # Backup pg_hba.conf of the pg17 cluster
         postgres@POD_NAME:~$ cp /mnt/disks/pgsql/17/data/pg_hba.conf /mnt/disks/pgsql/17/data/pg_hba.conf.bak
         
         # Update pg17 configurations
         postgres@POD_NAME:~$ echo "local      all           all                      trust" >> /mnt/disks/pgsql/17/data/pg_hba.conf; echo "host       all           all      127.0.0.1/32    trust" >> /mnt/disks/pgsql/17/data/pg_hba.conf
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  9. Modify `pg_hba.conf` in the new database cluster to provide the upgrade process the permissions and connections it needs.
         
         postgres@POD_NAME:~$ rm /mnt/disks/pgsql/data/pg_hba.conf; echo "local      all           all                      trust" >> /mnt/disks/pgsql/data/pg_hba.conf; echo "host       all           all      127.0.0.1/32    trust" >> /mnt/disks/pgsql/data/pg_hba.conf; chmod 2740 /mnt/disks/pgsql/17/data
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  10. Upgrade your database cluster.
         
         # (optional) Make sure postgres is stopped
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         # (optional) Check to verify that data can be upgraded.
         postgres@POD_NAME:~$ pg_upgrade -U alloydbadmin --check -b /mnt/disks/pgsql/17/bin -B /usr/lib/postgresql/18/bin -d /mnt/disks/pgsql/17/data -D /mnt/disks/pgsql/data --link -v
         
         postgres@POD_NAME:~$ pg_upgrade -U alloydbadmin -b /mnt/disks/pgsql/17/bin -B /usr/lib/postgresql/18/bin -d /mnt/disks/pgsql/17/data -D /mnt/disks/pgsql/data --link -v
         
         # Recover pg17 configurations
         postgres@POD_NAME:~$ cp /mnt/disks/pgsql/17/data/pg_hba.conf.bak /mnt/disks/pgsql/data/pg_hba.conf; cp -r /mnt/disks/pgsql/17/data/postgresql.conf /mnt/disks/pgsql/data/.; cp -r /mnt/disks/pgsql/17/data/postgresql.conf.d /mnt/disks/pgsql/data/.; cp -r /mnt/disks/pgsql/17/data/parambackup /mnt/disks/pgsql/data/.
         
         # Start postgres
         postgres@POD_NAME:~$ supervisorctl.par start postgres
         
         # Clean up backup data
         postgres@POD_NAME:~$ rm -fr /mnt/disks/pgsql/17/
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  11. After a successful upgrade, remove the manual version upgrade annotation from your database cluster.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME dbs.dbadmin.goog.com/manualmvu-
         

Replace the following variable:

     * NAME: the name of your database cluster.
  12. Resume normal operations and re-enable any backups, backup plans, or replication processes that you disabled in steps one through three.




### Upgrade from version 16.x.x to 17.5.0

  1. [Back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes) to avoid any data loss.

  2.      1. [Remove your backup plan](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes#disable).
  3. Terminate all replication processes. This includes physical replication used for [high availability (HA) and data resilience (DR)](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-ha) as well as all [logical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-replication-slots) streams.

  4. Annotate your database cluster to specify a manual version upgrade.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME dbs.dbadmin.goog.com/manualmvu=true
         

Replace the following variable:

     * NAME: the name of your database cluster.
  5. Stop the PostgreSQL process and move the data for the upgrade.
         
         kubectl exec -ti POD_NAME -- /bin/Bash
         # Shut down postgres
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         postgres@POD_NAME:~$ mkdir /mnt/disks/pgsql/16; mv /mnt/disks/pgsql/data /mnt/disks/pgsql/16/data; cp -r /usr/lib/postgresql/16/bin /mnt/disks/pgsql/16/.; cp -r /usr/lib/postgresql/16/lib /mnt/disks/pgsql/16/.; cp -r /usr/share/postgresql/16 /mnt/disks/pgsql/16/share; rm /mnt/disks/pgsql/16/share/postgresql.conf.sample; cp /usr/share/postgresql/postgresql.conf.sample /mnt/disks/pgsql/16/share/postgresql.conf.sample; chmod 2740 /mnt/disks/pgsql/16/data
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  6. Patch your database cluster to version `17.5.0` and your control plane agents (CPA) to `1.6.2`.
         
         kubectl patch dbclusters.alloydbomni.dbadmin.goog NAME --type=merge -p '{"spec":{"databaseVersion":"17.5.0","controlPlaneAgentsVersion":"1.6.2","databaseImageOSType":"UBI9"}}'
         

Replace the following variable:

     * NAME: the name of your database cluster.
**Note:** For database versions 16.9.0 and later, specifying `databaseImageOSType:"UBI9"` is optional, as `UBI9` is the default base OS. If you want to use the Debian-based image, you must explicitly set this field to `"Debian"`.
  7. Create an empty database cluster for the upgraded AlloyDB Omni version.
         
         kubectl exec -ti POD_NAME -- /bin/Bash
         
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         # Initialize a new, empty database cluster for the new version.
         postgres@POD_NAME:~$ rm -fr /mnt/disks/pgsql/data; initdb -D /mnt/disks/pgsql/data -U alloydbadmin --data-checksums --encoding=UTF8 --locale=C --locale-provider=icu --icu-locale=und-x-icu --auth-host=trust --auth-local=reject; cd ~
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  8. Modify `pg_hba.conf` in your pre-existing database cluster to provide the upgrade process the permissions and connections it needs.
         
         # Backup pg_hba.conf of the pg16 cluster
         postgres@POD_NAME:~$ cp /mnt/disks/pgsql/16/data/pg_hba.conf /mnt/disks/pgsql/16/data/pg_hba.conf.bak
         
         # Update pg16 configurations
         postgres@POD_NAME:~$ echo "local      all           all                      trust" >> /mnt/disks/pgsql/16/data/pg_hba.conf; echo "host       all           all      127.0.0.1/32    trust" >> /mnt/disks/pgsql/16/data/pg_hba.conf
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  9. Modify `pg_hba.conf` in the new database cluster to provide the upgrade process the permissions and connections it needs.
         
         postgres@POD_NAME:~$ rm /mnt/disks/pgsql/data/pg_hba.conf; echo "local      all           all                      trust" >> /mnt/disks/pgsql/data/pg_hba.conf; echo "host       all           all      127.0.0.1/32    trust" >> /mnt/disks/pgsql/data/pg_hba.conf; chmod 2740 /mnt/disks/pgsql/16/data
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  10. Upgrade your database cluster.
         
         # (optional) Make sure postgres is stopped
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         # (optional) Check to verify that data can be upgraded.
         postgres@POD_NAME:~$ pg_upgrade -U alloydbadmin --check -b /mnt/disks/pgsql/16/bin -B /usr/lib/postgresql/17/bin -d /mnt/disks/pgsql/16/data -D /mnt/disks/pgsql/data --link -v
         
         postgres@POD_NAME:~$ pg_upgrade -U alloydbadmin -b /mnt/disks/pgsql/16/bin -B /usr/lib/postgresql/17/bin -d /mnt/disks/pgsql/16/data -D /mnt/disks/pgsql/data --link -v
         
         # Recover pg16 configurations
         postgres@POD_NAME:~$ cp /mnt/disks/pgsql/16/data/pg_hba.conf.bak /mnt/disks/pgsql/data/pg_hba.conf; cp -r /mnt/disks/pgsql/16/data/postgresql.conf /mnt/disks/pgsql/data/.; cp -r /mnt/disks/pgsql/16/data/postgresql.conf.d /mnt/disks/pgsql/data/.; cp -r /mnt/disks/pgsql/16/data/parambackup /mnt/disks/pgsql/data/.
         
         # Start postgres
         postgres@POD_NAME:~$ supervisorctl.par start postgres
         
         # Clean up backup data
         postgres@POD_NAME:~$ rm -fr /mnt/disks/pgsql/16/
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  11. After a successful upgrade, remove the manual version upgrade annotation from your database cluster.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME dbs.dbadmin.goog.com/manualmvu-
         

Replace the following variable:

     * NAME: the name of your database cluster.
  12. Resume normal operations and re-enable any backups, backup plans, or replication processes that you disabled in steps one through three.




### Upgrade from version 15.x.x to 17.5.0

  1. [Back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes) to avoid any data loss.

  2. [Remove your backup plan](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/backup-kubernetes#disable).

  3. Terminate all replication processes. This includes physical replication used for [high availability (HA) and data resilience (DR)](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-ha) as well as all [logical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/create-replication-slots) streams.

  4. Annotate your database cluster to specify a manual version upgrade.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME dbs.dbadmin.goog.com/manualmvu=true
         

Replace the following variable:

     * NAME: the name of your database cluster.
  5. Stop the PostgreSQL process and move the data for the upgrade.
         
         kubectl exec -ti POD_NAME -- /bin/Bash
         # Shut down postgres
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         postgres@POD_NAME:~$ mkdir /mnt/disks/pgsql/15; mv /mnt/disks/pgsql/data /mnt/disks/pgsql/15/data; cp -r /usr/lib/postgresql/15/bin /mnt/disks/pgsql/15/.; cp -r /usr/lib/postgresql/15/lib /mnt/disks/pgsql/15/.; cp -r /usr/share/postgresql/15 /mnt/disks/pgsql/15/share; rm /mnt/disks/pgsql/15/share/postgresql.conf.sample; cp /usr/share/postgresql/postgresql.conf.sample /mnt/disks/pgsql/15/share/postgresql.conf.sample; chmod 2740 /mnt/disks/pgsql/15/data
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  6. Patch your database cluster to version `17.5.0` and your control plane agents (CPA) to `1.6.2`.
         
         kubectl patch dbclusters.alloydbomni.dbadmin.goog NAME --type=merge -p '{"spec":{"databaseVersion":"17.5.0","controlPlaneAgentsVersion":"1.6.2","databaseImageOSType":"UBI9"}}'
         

Replace the following variable:

     * NAME: the name of your database cluster.
**Note:** For AlloyDB Omni versions 16.9.0 and later, specifying `databaseImageOSType:"UBI9"` is optional, as UBI9 is the default base OS. You only need to set this field if you want to use the Debian-based image, in which case you set it to `"Debian"`.
  7. Create an empty database cluster for the upgraded AlloyDB Omni version.
         
         kubectl exec -ti POD_NAME -- /bin/Bash
         
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         # Initialize a new, empty database cluster for the new version.
         postgres@POD_NAME:~$ rm -fr /mnt/disks/pgsql/data; initdb -D /mnt/disks/pgsql/data -U alloydbadmin --data-checksums --encoding=UTF8 --locale=C --locale-provider=icu --icu-locale=und-x-icu --auth-host=trust --auth-local=reject; cd ~
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  8. Modify `pg_hba.conf` in your pre-existing database cluster to provide the upgrade process the permissions and connections it needs.
         
         # Backup pg_hba.conf of the pg15 cluster
         postgres@POD_NAME:~$ cp /mnt/disks/pgsql/15/data/pg_hba.conf /mnt/disks/pgsql/15/data/pg_hba.conf.bak
         
         # Update pg15 configurations
         postgres@POD_NAME:~$ echo "local      all           all                      trust" >> /mnt/disks/pgsql/15/data/pg_hba.conf; echo "host       all           all      127.0.0.1/32    trust" >> /mnt/disks/pgsql/15/data/pg_hba.conf
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  9. Modify `pg_hba.conf` in the new database cluster to provide the upgrade process the permissions and connections it needs.
         
         postgres@POD_NAME:~$ rm /mnt/disks/pgsql/data/pg_hba.conf; echo "local      all           all                      trust" >> /mnt/disks/pgsql/data/pg_hba.conf; echo "host       all           all      127.0.0.1/32    trust" >> /mnt/disks/pgsql/data/pg_hba.conf; chmod 2740 /mnt/disks/pgsql/15/data
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  10. Upgrade your database cluster.
         
         # (optional) Make sure postgres is stopped
         postgres@POD_NAME:~$ supervisorctl.par stop postgres
         
         # (optional) Check to verify that data can be upgraded.
         postgres@POD_NAME:~$ pg_upgrade -U alloydbadmin --check -b /mnt/disks/pgsql/15/bin -B /usr/lib/postgresql/17/bin -d /mnt/disks/pgsql/15/data -D /mnt/disks/pgsql/data --link -v
         
         postgres@POD_NAME:~$ pg_upgrade -U alloydbadmin -b /mnt/disks/pgsql/15/bin -B /usr/lib/postgresql/17/bin -d /mnt/disks/pgsql/15/data -D /mnt/disks/pgsql/data --link -v
         
         # Recover pg15 configurations
         postgres@POD_NAME:~$ cp /mnt/disks/pgsql/15/data/pg_hba.conf.bak /mnt/disks/pgsql/data/pg_hba.conf; cp -r /mnt/disks/pgsql/15/data/postgresql.conf /mnt/disks/pgsql/data/.; cp -r /mnt/disks/pgsql/15/data/postgresql.conf.d /mnt/disks/pgsql/data/.; cp -r /mnt/disks/pgsql/15/data/parambackup /mnt/disks/pgsql/data/.
         
         # Start postgres
         postgres@POD_NAME:~$ supervisorctl.par start postgres
         
         # Clean up backup data
         postgres@POD_NAME:~$ rm -fr /mnt/disks/pgsql/15/
         

Replace the following variable:

     * POD_NAME: the name of your pod.
  11. After a successful upgrade, remove the manual version upgrade annotation from your database cluster.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME dbs.dbadmin.goog.com/manualmvu-
         

Replace the following variable:

     * NAME: the name of your database cluster.
  12. Resume normal operations and re-enable any backups, backup plans, or replication processes that you disabled in steps one through three. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
