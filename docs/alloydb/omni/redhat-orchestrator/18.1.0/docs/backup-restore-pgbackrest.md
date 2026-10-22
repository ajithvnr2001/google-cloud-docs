---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/backup-restore-pgbackrest/
title: Back up and restore data using pgBackRest \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:36.333810+00:00
---

# Back up and restore data using pgBackRest  |  AlloyDB Omni using the RPM orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/backup-restore-pgbackrest/

This page documents AlloyDB Omni version **18.1.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/overview)



Send feedback 

#  Back up and restore data using pgBackRest Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/backup-restore-pgbackrest)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/backup-restore-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/backup-restore-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/backup-restore-pgbackrest)

Configure [pgBackRest](https://pgbackrest.org/), an open-source database backup and restore solution, to protect your data. AlloyDB Omni uses pgBackRest with Cloud Storage. The AlloyDB Omni orchestrator interfaces with pgBackRest and Cloud Storage through `alloydbctl` and Ansible to manage the backups. 

AlloyDB Omni manages backups through custom resource definitions (CRDs):

  * `BackupPlan`: each database cluster can have one or more `BackupPlan` CRDs with different configurations and schedules.
  * `Backup`: initiates backups based on your `BackupPlan` CRDs.



## Before you begin

Before you set up and configure pgBackRest, ensure that you have the following:

  * [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets): AlloyDB Omni stores backups in Cloud Storage buckets. For information on how to create buckets, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).



## Create a backup plan

To create a backup plan, complete the following steps:

  1. Create a `BackupPlan` CRD using the following format:
         
         BackupPlan:
           metadata:
             name: BACKUP_PLAN_NAME
           spec:
             dbclusterRef: DBCLUSTER_NAME
             backupLocation:
               type: GCS
               gcsOptions:
                 bucket: BUCKET_NAME
                 key: BUCKET_FOLDER
         

Replace the following variables:

     * `BACKUP_PLAN_NAME`: name for this `BackupPlan` CRD. For example, `my-backup-plan-1`.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).

     * `BUCKET_NAME`: name of the Cloud Storage bucket you created in Before you begin.

     * `BUCKET_FOLDER`: path to the directory in Cloud Storage that backups should write to. You must provide an absolute path, which begins with `/`.

  2. If you're using Ansible, create a playbook for your `BackupPlan` CRD.
         
         - name: BACKUP_PLAN_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.backup
         

Replace the following variables:

     * `BACKUP_PLAN_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My BackupPlan`.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  3. Apply your `BackupPlan` resource.

### `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC" -r "BACKUP_PLAN_CRD"

Replace the following variables:

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `BACKUP_PLAN_CRD`: path to the `BackupPlan` CRD you created in step one.

### Ansible
    
    ansible-playbook BACKUP_PLAN_PLAYBOOK -i "DEPLOYMENT_SPEC" \
      -e resource_spec="BACKUP_PLAN_CRD"

Replace the following variables:

     * `BACKUP_PLAN_PLAYBOOK`: path to the playbook that you created for your `BackupPlan` CRD in step two.

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `BACKUP_PLAN_CRD`: path to the `BackupPlan` CRD you created in step one.

  4. Confirm that the status field, `status.phase`, for your `BackupPlan` CRD is `Ready`. If the CRD is not ready, wait until it is.

### `alloydbctl`
         
         alloydbctl get -d "DEPLOYMENT_SPEC" -t BackupPlan -n BACKUP_PLAN_NAME -o yaml

### Ansible
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC" -e resource_type=BackupPlan \
           -e resource_name=BACKUP_PLAN_NAME




## Delete a backup plan

To delete a backup plan, use either of the following methods:

### `alloydbctl`
    
    
    alloydbctl delete -d "DEPLOYMENT_SPEC" -t BackupPlan -n BACKUP_PLAN_NAME

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `BACKUP_PLAN_NAME`: name of the `BackupPlan` CRD to delete.




### Ansible

  1. Create a playbook for deleting the `BackupPlan` CRD.
         
         - name: BACKUP_PLAN_DELETE_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.delete
         

Replace the following variables:

     * `BACKUP_PLAN_DELETE_PLAYBOOK_NAME`: name of your Ansible playbook.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  2. Run `ansible-playbook` to delete the `BackupPlan` CRD.
         
         ansible-playbook BACKUP_PLAN_DELETE_PLAYBOOK_NAME -i "DEPLOYMENT_SPEC" -e resource_type=BackupPlan \
           -e resource_name=BACKUP_PLAN_NAME

Replace the following variables:

     * `BACKUP_PLAN_DELETE_PLAYBOOK_NAME`: path to the playbook that you created for deleting the `BackupPlan` CRD in the previous step.

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `BACKUP_PLAN_NAME`: name of the `BackupPlan` CRD to delete.




## Create a backup

To create and initiate a backup, complete the following steps:

  1. Create a `Backup` CRD using the following format:
         
         Backup:
           metadata:
             name: BACKUP_NAME
           spec:
             backupPlanRef: BACKUP_PLAN_NAME
             dbclusterRef: DBCLUSTER_NAME
         

Replace the following variables:

     * `BACKUP_NAME`: name for this `Backup` CRD. For example, `my-backup-1`.

     * `BACKUP_PLAN_NAME`: name for this `BackupPlan` CRD. For example, `my-backup-plan-1`.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/create-cluster).

  2. If you're using Ansible, create a playbook for your `Backup` CRD.
         
         - name: BACKUP_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.backup
         

Replace the following variables:

     * `BACKUP_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My Backup`.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  3. Apply your `Backup` CRD.

### `alloydbctl`
         
         alloydbctl apply -d "DEPLOYMENT_SPEC" -r "BACKUP_CRD"

Replace the following variables:

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `BACKUP_CRD`: path to the `Backup` CRD you created in step one.

### Ansible
    
    ansible-playbook BACKUP_PLAYBOOK -i "DEPLOYMENT_SPEC" \
      -e resource_spec="BACKUP_CRD"

Replace the following variables:

     * `BACKUP_PLAYBOOK`: path to the playbook that you created for your `Backup` CRD in step two.

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `BACKUP_CRD`: path to the `Backup` CRD you created in step one.

  4. Confirm that the status field, `status.phase`, for your `Backup` CRD is `Succeeded`. If the CRD has not succeeded, wait until it is.

### `alloydbctl`
         
         alloydbctl get -d "DEPLOYMENT_SPEC" -t Backup -n BACKUP_NAME -o yaml

### Ansible
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC" -e resource_type=Backup \
           -e resource_name=BACKUP_NAME

  5. Confirm that the backup files landed in your Cloud Storage bucket by [searching your bucket](https://docs.cloud.google.com/storage/docs/listing-buckets) for `/backup/db`.




## Delete a backup

To delete a backup, run one of the following commands:

### `alloydbctl`
    
    
    alloydbctl delete -d "DEPLOYMENT_SPEC" -t Backup -n BACKUP_NAME

Replace the following variables:

  * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

  * `BACKUP_NAME`: name of the `Backup` CRD to delete.




### Ansible

  1. Create a playbook for deleting the `Backup` CRD.
         
         - name: BACKUP_DELETE_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.delete
         

Replace the following variables:

     * `Delete Backup`: name of your Ansible playbook.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  2. Run `ansible-playbook` to delete the `Backup` CRD.
         
         ansible-playbook DELETE_BACKUP_PLAYBOOK -i "DEPLOYMENT_SPEC" -e resource_type=Backup \
           -e resource_name=BACKUP_NAME

Replace the following variables:

     * `DELETE_BACKUP_PLAYBOOK`: path to the playbook that you created for deleting the `Backup` CRD in the previous step.

     * `DEPLOYMENT_SPEC`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/install-components).

     * `BACKUP_NAME`: name of the `Backup` CRD to delete.




## Restore from a backup

To restore data from a backup into your database cluster, complete one of the following sets of instructions:

  * Restore in a high availability cluster.

  * Restore in a standalone cluster.




### High availability cluster

To restore data for a highly available database cluster, complete the following instructions:

  1. If `availability.enableAutoFailover` and `availability.enableAutoHeal` are set to `true` in your `DBCluster` specification file, set them to `false`.
         
         DBCluster:
           metadata: my-db-cluster
             name:
           spec:
             databaseVersion: 18.1.0
             mode: ""
             availability:
               ...
               **enableAutoFailover : false
               enableAutoHeal: false**
               ...
         

  2. Identify the primary node by displaying the contents of the `db-role` file on each database node. The primary node contains `DATABASE_ROLE_PRIMARY`.
         
         sudo cat /var/lib/alloydbomni/nm/kvstore/db-role

To automate this process for multiple nodes and output the results to your control node, see the following shell script.
         
         SSH_USER=SSH_USER
         DB_NODES="DB_NODES"
         SSH_OPTIONS="SSH_OPTIONS"
         DB_ROLE=/var/lib/alloydbomni/nm/kvstore/db-role
         
         for node in $DB_NODES; do
           ssh $SSH_OPTIONS ${SSH_USER}@${node} "hostname ; sudo cat ${DB_ROLE}; echo"
         done
         

Replace the following variables:

     * `SSH_USER`: SSH user used to connect to your database nodes.
     * `DB_NODES`: space-separated list of the hostnames or IP addresses of your database nodes.
     * `SSH_OPTIONS`: SSH options that you use to connect to your database nodes. For example, `"-o StrictHostKeyChecking=no -o BatchMode=yes -o ConnectTimeout=5"`.
  3. Stop the AlloyDB Omni service on all database nodes.
         
         sudo systemctl stop alloydbomni18

  4. On each standby node, delete the contents of the data directory.
         
         sudo rm -rf PGDATA_DIR

Replace `PGDATA_DIR` with the path to the data directory. This is the value defined in the `primarySpec.resources.disks` field of your `DBCluster` resource with the name `DataDisk`.

  5. On the primary node, execute the `pgbackrest` command to restore from a backup. The example shows executing by switching to the `postgres` user.
         
         sudo -u postgres pgbackrest restore \
           --log-level-console=info \
           --stanza=db \
           --delta \
           --target-action=promote \
           --type=immediate \
           --set=BACKUP_ID

Replace `BACKUP_ID` with the backup identifier. You can find this value in the `status.backupID` field of the `Backup` CRD.

  6. Start the AlloyDB Omni service on the primary node.
         
         sudo systemctl start alloydbomni18

  7. Confirm that the AlloyDB Omni service status is `active`. If it not active, then wait for it to be active.
         
         sudo systemctl status alloydbomni18

  8. Reset the following GUCs on primary node by removing them from `PGDATA_DIR/PG_VERSION/db/postgresql.auto.conf`:

     * `restore_command`
     * `recovery_target`
     * `recovery_target_action`
     * `recovery_target_timeline`
    
    sudo sed -i '/^\(restore_command\|recovery_target\|recovery_target_action\|recovery_target_timeline\)/d' PGDATA_DIR/PG_VERSION/db/postgresql.auto.conf

Replace the following variables:

     * `PGDATA_DIR` with the path to the data directory. This is the value defined in the `primarySpec.resources.disks` field of your `DBCluster` resource with the name `DataDisk`.
     * `PG_VERSION` with the major PostgreSQL version of your AlloyDB Omni installation, for example, `18`.
  9. Update `availability.enableAutoFailover` or `availability.enableAutoHeal` to `true`, to recover database service on standby nodes to be active and be in sync with database service on primary node.

  10. Confirm that the AlloyDB Omni service on each standby node is `active`.




### Standalone cluster

  1. Stop the AlloyDB Omni service and mask it to prevent restarts.
         
         sudo systemctl stop alloydbomni18
         sudo systemctl mask alloydbomni18

  2. Run the `pgbackrest` command to restore from a backup.
         
         sudo -u postgres pgbackrest restore \
           --log-level-console=info \
           --stanza=db \
           --delta \
           --target-action=promote \
           --type=immediate \
           --set=BACKUP_ID

Replace `BACKUP_ID` with the backup identifier.

  3. Unmask and start the AlloyDB Omni service.
         
         sudo systemctl unmask alloydbomni18
         sudo systemctl start alloydbomni18

  4. Verify that the service is running.
         
         sudo systemctl status alloydbomni18




## Limitations

The following limitations apply:

  * Only Cloud Storage buckets are supported to back up your data and restore from it.

  * `Backup` CRD supports creating backups of type `"full"`. The other types, `"incr"` and `"diff"`, are not supported.

  * Scheduled backups are not supported. To configure scheduled backups, automate the creation of `Backup` specifications using an automation system of your choice.

  * Automatic restore is not supported. You must follow the manual instructions to restore your data.

  * To delete backups, delete the `Backup` CRD.

  * Deleting a `BackupPlan` CRD does not delete the `Backup` CRDs that were already created by that plan. To remove these backups, delete each `Backup` resource individually, as described in Delete a backup.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
