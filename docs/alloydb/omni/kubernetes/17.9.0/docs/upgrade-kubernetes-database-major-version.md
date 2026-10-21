---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-database-major-version/
title: Upgrade to AlloyDB Omni version 17.9.0 on 1.8.2 \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:49:37.205343+00:00
---

# Upgrade to AlloyDB Omni version 17.9.0 on 1.8.2  |  AlloyDB Omni using the container orchestrator: 17.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-database-major-version/

This page documents AlloyDB Omni version **17.9.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/overview)



Send feedback 

#  Upgrade to AlloyDB Omni version 17.9.0 on 1.8.2 Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.9.0keyboard_arrow_down

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

This page describes how to perform a major version upgrade to AlloyDB Omni version 17.9.0 on Kubernetes. 

## Before you begin

  * Verify your AlloyDB Omni Kubernetes operator version is `1.8.2`. To upgrade your AlloyDB Omni operator version, see [Migrate to the latest AlloyDB Omni Kubernetes operator version](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-operator-version).

  * Verify you have at least 5GB of free disk space.

  * If you run external or remote backup systems, perform a full backup and pause any scheduled backups to avoid backing up during the upgrade process.

  * For [high availability (HA) and data resilience (DR)](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/high-availability/overview) environments, decouple your database clusters before upgrading them.


**Note:** Starting with AlloyDB Omni Kubernetes operator version 1.6.0, you can specify the base operating system for the database image using the `databaseImageOSType` field in your `DBCluster` manifest. The recommended value is `UBI9` for improved security and compatibility. If you need to continue using Debian-based images, you can set this field to `Debian`. During a major version upgrade, you can set this field in the patch command.

## Upgrade your AlloyDB Omni version

To upgrade your AlloyDB Omni version using `pg_upgrade`, do one of the following:

  * Run the Bash script that performs the upgrade for you.

  * Run the upgrade instructions manually.




## Perform scripted upgrade

You can find a script that performs the manual upgrade steps in the [AlloyDB Omni samples on GitHub](https://github.com/GoogleCloudPlatform/alloydb-omni-samples/tree/main/samples/MVU.sh).

To use the upgrade script, download the script and run the following command:
    
    
    ./MVU.sh 17.9.0 1.8.2 NAME NAMESPACE
    

Replace the following variables:

  * NAME: the name of your database cluster.
  * NAMESPACE: the namespace of your database cluster.



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

### Upgrade from an earlier major version

  1. Get the current and target major versions of your database.
         
         export OLD_PG_VERSION=$(kubectl get dbcluster.alloydbomni.dbadmin.goog NAME -n NAMESPACE -o jsonpath='{.spec.databaseVersion}' | cut -d'.' -f1)
         export NEW_PG_VERSION=$(echo '17.9.0' | cut -d'.' -f1)
         

Replace the following variables:

     * `NAME`: the name of your database cluster.
     * `NAMESPACE`: the namespace for your database cluster.
  2. [Back up your data](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/backup-kubernetes) to avoid any data loss.

  3. [Remove your backup plan](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/backup-kubernetes).

  4. Terminate all replication processes. This includes [physical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/about-pglogical) used for [high availability (HA) and data resilience (DR)](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/high-availability/overview) as well as all [logical replication](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/create-replication-slots) streams.

  5. Annotate your database cluster to specify a manual version upgrade.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME -n NAMESPACE dbs.dbadmin.goog.com/manualmvu=true
         

Replace the following variables:

     * `NAME`: the name of your database cluster.
     * `NAMESPACE`: the namespace for your database cluster.
  6. Stop the PostgreSQL process and move the data for the upgrade.
         
         kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "
         # Shut down postgres
         supervisorctl.par stop postgres;
         
         # Check data directory and move it for upgrade if necessary
         if [ -d /mnt/disks/pgsql/data ]; then
             echo 'Found data directory at /mnt/disks/pgsql/data, moving it to /mnt/disks/pgsql/${OLD_PG_VERSION}/db'
             mkdir -p /mnt/disks/pgsql/${OLD_PG_VERSION};
             mv /mnt/disks/pgsql/data /mnt/disks/pgsql/${OLD_PG_VERSION}/db;
         elif [ ! -d /mnt/disks/pgsql/${OLD_PG_VERSION}/db ]; then
             echo 'ERROR: Neither /mnt/disks/pgsql/data nor /mnt/disks/pgsql/${OLD_PG_VERSION}/db directory found' >&2;
             exit 1;
         fi
         
         cp -r /usr/lib/postgresql/${OLD_PG_VERSION}/bin /mnt/disks/pgsql/${OLD_PG_VERSION}/.;
         cp -r /usr/lib/postgresql/${OLD_PG_VERSION}/lib /mnt/disks/pgsql/${OLD_PG_VERSION}/.;
         cp -r /usr/share/postgresql/${OLD_PG_VERSION} /mnt/disks/pgsql/${OLD_PG_VERSION}/share;
         rm -f /mnt/disks/pgsql/${OLD_PG_VERSION}/share/postgresql.conf.sample;
         cp /usr/share/postgresql/postgresql.conf.sample /mnt/disks/pgsql/${OLD_PG_VERSION}/share/postgresql.conf.sample;
         chmod 2740 /mnt/disks/pgsql/${OLD_PG_VERSION}/db
         "
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  7. Patch your database cluster to version `17.9.0` and your control plane agents (CPA) to `1.8.2`.
         
         kubectl patch dbclusters.alloydbomni.dbadmin.goog NAME -n NAMESPACE --type=merge -p '{"spec":{"databaseVersion":"17.9.0","controlPlaneAgentsVersion":"1.8.2","databaseImageOSType":"UBI9"}}'
         

Replace the following variables:

     * `NAME`: the name of your database cluster.
     * `NAMESPACE`: the namespace for your database cluster.
**Note:** For database versions 16.9.0 and later, specifying `databaseImageOSType:"UBI9"` is optional, as `UBI9` is the default base OS. If you want to use the Debian-based image, you must explicitly set this field to `"Debian"`.
  8. Get the post-upgrade data directory path and set it as an environment variable.
         
         export POST_UPGRADE_DATA_DIR=$(kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "if [ -d /mnt/disks/pgsql/data ]; then echo /mnt/disks/pgsql/data; else echo /mnt/disks/pgsql/${NEW_PG_VERSION}/db; fi")
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  9. Create an empty database cluster for the upgraded AlloyDB Omni version.
         
         kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "
         supervisorctl.par stop postgres;
         # Initialize a new, empty database cluster for the new version.
         rm -fr $POST_UPGRADE_DATA_DIR;
         initdb -D $POST_UPGRADE_DATA_DIR -U alloydbadmin --data-checksums --encoding=UTF8 --locale=C --locale-provider=icu --icu-locale=und-x-icu --auth-host=trust --auth-local=reject;
         cd ~
         "
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  10. Modify `pg_hba.conf` in your pre-existing database cluster to provide the upgrade process the permissions and connections it needs.
         
         kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "
         # Backup pg_hba.conf of the old postgres cluster
         cp /mnt/disks/pgsql/${OLD_PG_VERSION}/db/pg_hba.conf /mnt/disks/pgsql/${OLD_PG_VERSION}/db/pg_hba.conf.bak;
         # Update old postgres configurations
         echo 'local      all           all                      trust' >> /mnt/disks/pgsql/${OLD_PG_VERSION}/db/pg_hba.conf;
         echo 'host       all           all      127.0.0.1/32    trust' >> /mnt/disks/pgsql/${OLD_PG_VERSION}/db/pg_hba.conf
         "
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  11. Modify `pg_hba.conf` in the new database cluster to provide the upgrade process the permissions and connections it needs.
         
         kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "
         rm $POST_UPGRADE_DATA_DIR/pg_hba.conf;
         echo 'local      all           all                      trust' >> $POST_UPGRADE_DATA_DIR/pg_hba.conf;
         echo 'host       all           all      127.0.0.1/32    trust' >> $POST_UPGRADE_DATA_DIR/pg_hba.conf;
         "
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  12. Check for upgrade eligibility.
         
         kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "
         cd /mnt/disks/pgsql;
         
         # Make sure postgres is stopped
         supervisorctl.par stop postgres;
         
         # Check to verify that data can be upgraded.
         pg_upgrade -U alloydbadmin --check -b /mnt/disks/pgsql/${OLD_PG_VERSION}/bin -B /usr/lib/postgresql/${NEW_PG_VERSION}/bin -d /mnt/disks/pgsql/${OLD_PG_VERSION}/db -D $POST_UPGRADE_DATA_DIR --link -v;
         "
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  13. Perform the database upgrade.
         
         kubectl exec -i POD_NAME -n NAMESPACE -c database -- /bin/bash -c "
         cd /mnt/disks/pgsql;
         pg_upgrade -U alloydbadmin -b /mnt/disks/pgsql/${OLD_PG_VERSION}/bin -B /usr/lib/postgresql/${NEW_PG_VERSION}/bin -d /mnt/disks/pgsql/${OLD_PG_VERSION}/db -D $POST_UPGRADE_DATA_DIR --link -v;
         
         # Recover old cluster configurations
         cp /mnt/disks/pgsql/${OLD_PG_VERSION}/db/pg_hba.conf.bak $POST_UPGRADE_DATA_DIR/pg_hba.conf;
         cp -r /mnt/disks/pgsql/${OLD_PG_VERSION}/db/postgresql.conf $POST_UPGRADE_DATA_DIR/.;
         cp -r /mnt/disks/pgsql/${OLD_PG_VERSION}/db/postgresql.conf.d $POST_UPGRADE_DATA_DIR/.;
         cp -r /mnt/disks/pgsql/${OLD_PG_VERSION}/db/parambackup $POST_UPGRADE_DATA_DIR/.;
         
         # Start postgres
         supervisorctl.par start postgres;
         
         # Clean up backup data
         rm -fr /mnt/disks/pgsql/${OLD_PG_VERSION}/
         "
         

Replace the following variables:

     * `POD_NAME`: the name of your pod.
     * `NAMESPACE`: the namespace for your database cluster.
  14. After a successful upgrade, remove the manual version upgrade annotation from your database cluster.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog NAME -n NAMESPACE dbs.dbadmin.goog.com/manualmvu-
         

Replace the following variables:

     * `NAME`: the name of your database cluster.
     * `NAMESPACE`: the namespace for your database cluster.
  15. Resume normal operations and re-enable any backups, backup plans, or replication processes that you disabled in steps one through three.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
