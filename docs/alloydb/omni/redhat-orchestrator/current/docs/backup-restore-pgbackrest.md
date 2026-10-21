---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/backup-restore-pgbackrest/
title: Back up and restore data using pgBackRest \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.3.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:17.408359+00:00
---

# Back up and restore data using pgBackRest  |  AlloyDB Omni using the RPM orchestrator: Current (18.3.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/backup-restore-pgbackrest/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Back up and restore data using pgBackRest Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/backup-restore-pgbackrest)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/backup-restore-pgbackrest)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/backup-restore-pgbackrest)

To protect your data, AlloyDB Omni provides automated data backup and recovery using declarative manifests. The AlloyDB Omni orchestrator works with `alloydbctl` and Ansible to apply these manifest configurations and automate backups to Cloud Storage, standard Amazon S3 buckets, or S3-compliant software such as MinIO. 

To enable AlloyDB Omni continuous backup and recovery, you must create a backup plan for each database cluster. Backups are taken based on the backup schedules defined in the BackupPlan resource. You can restore using a Backup resource or any timestamp in the recovery window at seconds granularity.

AlloyDB Omni manages automated backups and recovery through manifests:

  * `BackupPlan`: each database cluster can have one or more `BackupPlan` manifests with different configurations and schedules across backup tiers.
  * `Backup`: initiates full, differential, or incremental backups based on your `BackupPlan` manifests.
  * `Restore`: initiates an in-place restore of your database cluster using a specific backup or a point in time.



## Before you begin

Before you set up and configure your backup plan, make sure that you have the following:

  * **A storage location for your backups** : AlloyDB Omni stores backups in one of the following storage options:

    * **Cloud Storage** : A Cloud Storage bucket. For information on how to create buckets, see [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
    * **Amazon S3** : An Amazon S3 bucket. For information on how to create S3 buckets, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html).
    * **S3-compliant storage** : A bucket in S3-compliant software, such as MinIO. For information on how to create MinIO buckets, see the [MinIO documentation](https://min.io/docs/minio/linux/index.html).
  * **Authentication credentials** : If your storage option requires authentication keys such as Amazon S3, MinIO, or Cloud Storage with a specific service account, you must create a `Secret` resource containing these credentials before you create the backup plan. For instructions, see Create a Secret resource to authenticate storage.




### Create a Secret resource to authenticate storage

If the storage you use requires authentication, you must create a `Secret` resource before you create the backup plan.

#### Create a Secret resource for Cloud Storage

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) for adding backups to the bucket.
  2. [Grant the `roles/storage.objectAdmin` Identity and Access Management role to the service account](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) on the bucket.
  3. [Generate a service account key in JSON format](https://docs.cloud.google.com/iam/docs/keys-create-delete).
  4. Encode the content of the downloaded JSON key file in base64. Run `base64 -w 0` or ensure that the encoded text is a single continuous line.
  5. Create a `Secret` resource manifest. The key name in the `data` section must be `key.json`.
         
         Secret:
           metadata:
             name: SECRET_NAME
           spec:
             type: Opaque
             data:
               key.json: "BASE64_ENCODED_JSON_KEY"
         

Replace the following:

     * `SECRET_NAME`: the name for your `Secret` resource.
     * `BASE64_ENCODED_JSON_KEY`: the base64-encoded content of your service account JSON key file.



#### Create a Secret resource for S3 or S3-compliant storage

  1. Encode your S3 access key ID in base64.
  2. Encode your S3 secret access key in base64.
  3. Create a `Secret` resource manifest. The key names in the `data` section must be `access-key-id` and `access-key`.
         
         Secret:
           metadata:
             name: SECRET_NAME
           spec:
             type: Opaque
             data:
               access-key-id: "BASE64_ENCODED_ACCESS_KEY_ID"
               access-key: "BASE64_ENCODED_SECRET_ACCESS_KEY"
         

Replace the following:

     * `SECRET_NAME`: the name for your `Secret` resource.
     * `BASE64_ENCODED_ACCESS_KEY_ID`: the base64-encoded S3 access key ID.
     * `BASE64_ENCODED_SECRET_ACCESS_KEY`: the base64-encoded S3 secret access key.



#### Apply the Secret resource

Apply the `Secret` resource manifest before you apply the `BackupPlan` manifest. You can apply the `Secret` resource manifest using either of the following methods:

### `alloydbctl`

To apply the `Secret` resource manifest using `alloydbctl`, run the following command:
    
    
    alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "SECRET_MANIFEST"

Replace the following variables:

  * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).
  * `SECRET_MANIFEST`: path to the `Secret` resource manifest you created.



### Ansible

To apply the `Secret` resource manifest using Ansible, complete the following:

  1. Create a playbook for your `Secret` resource manifest:
         
         - name: Create Secret
           hosts: localhost
           become: true
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.backup
         

Replace the following variables:

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.
     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.
  2. Apply the `Secret` resource manifest:
         
         ansible-playbook SECRET_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
           -e resource_spec="SECRET_MANIFEST"

Replace the following variables:

     * `SECRET_PLAYBOOK`: path to the playbook that you created for your `Secret` resource manifest.
     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).
     * `SECRET_MANIFEST`: path to the `Secret` resource manifest you created.



## Create a backup plan

  1. Create a `BackupPlan` manifest using the format for your storage option:

###  Cloud Storage 

The `gcsOptions` field is required.
         
         BackupPlan:
           metadata:
             name: BACKUP_PLAN_NAME
           spec:
             dbclusterRef: DBCLUSTER_NAME
             backupLocation:
               type: GCS
               gcsOptions:
                 bucket: BUCKET_NAME
                 key: BUCKET_PATH
                 secretRef:
                   name: SECRET_NAME
             backupRetainDays: RETAIN_DAYS
             backupSchedules:
               full: "FULL_SCHEDULE"
               differential: "DIFF_SCHEDULE"
               incremental: "INC_SCHEDULE"
         

Replace the following variables:

     * `BACKUP_PLAN_NAME`: name of the `BackupPlan` manifest. For example, `my-backup-plan-1`.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster).

     * `BUCKET_NAME`: name of the Cloud Storage bucket that you created.

     * `BUCKET_PATH`: path to the directory in Cloud Storage that backups should write to. You must provide an absolute path that begins with `/`. For example, `/backups`.

     * `SECRET_NAME` (Optional): name of the `Secret` resource that stores the authentication keys.

     * `RETAIN_DAYS` (Optional): number of days to retain backups before the backups are automatically deleted.

     * `FULL_SCHEDULE` (Optional): cron schedule expression for full backups. For example, `0 2 * * *`.

     * `DIFF_SCHEDULE` (Optional): cron schedule expression for differential backups. For example, `0 2 * * *`.

     * `INC_SCHEDULE` (Optional): cron schedule expression for incremental backups. For example, `0 2 * * *`.

### Amazon S3 or S3-compliant

The `s3Options` field is required.
    
    BackupPlan:
      metadata:
        name: BACKUP_PLAN_NAME
      spec:
        dbclusterRef: DBCLUSTER_NAME
        backupLocation:
          type: S3
          s3Options:
            bucket: BUCKET_NAME
            key: BUCKET_PATH
            endpoint: ENDPOINT_URL
            region: REGION
            secretRef:
              name: SECRET_NAME
        backupRetainDays: RETAIN_DAYS
        backupSchedules:
          full: "FULL_SCHEDULE"
          differential: "DIFF_SCHEDULE"
          incremental: "INC_SCHEDULE"
    

Replace the following variables:

     * `BACKUP_PLAN_NAME`: name of the `BackupPlan` manifest. For example, `my-backup-plan-1`.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster).

     * `BUCKET_NAME`: name of the S3 bucket that you created.

     * `BUCKET_PATH`: path to the directory in the S3 bucket that backups should write to. You must provide an absolute path that begins with `/`. For example, `/backups`.

     * `ENDPOINT_URL`: custom endpoint URL for connecting to S3-compliant software such as MinIO. For example, `http://minio.example.com:9000`. For Amazon S3 buckets, you don't need to provide any endpoint URL.

     * `REGION_` (Optional): region of the storage bucket. Required when connecting to standard Amazon S3 buckets or S3-compliant software where region validation is enforced.

     * `SECRET_NAME`: reference to a `Secret` resource you created earlier, and which contains your `ACCESS_KEY_ID` and `SECRET_ACCESS_KEY`.

     * `RETAIN_DAYS` (Optional): number of days to retain backups before the backups are automatically deleted.

     * `FULL_SCHEDULE` (Optional): cron schedule expression for full backups. For example, `0 2 * * *`.

     * `DIFF_SCHEDULE` (Optional): cron schedule expression for differential backups. For example, `0 2 * * *`.

     * `INC_SCHEDULE` (Optional): cron schedule expression for incremental backups. For example, `0 2 * * *`.

  2. Apply the backup plan using either of the following methods:

### `alloydbctl`

     1. Apply your `BackupPlan` resource:
            
            alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "BACKUP_PLAN_MANIFEST"

Replace the following variables:

        * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

        * `BACKUP_PLAN_MANIFEST`: path to the `BackupPlan` manifest you created earlier.

     2. Confirm that the status field, `status.phase`, for your `BackupPlan` manifest is `Ready`. If the manifest is not ready, wait until it is:
            
            alloydbctl get -d "DEPLOYMENT_SPEC_PATH" -t BackupPlan -n BACKUP_PLAN_NAME -o yaml

### Ansible

     1. Create a playbook for your `BackupPlan` manifest:
            
            - name: BACKUP_PLAN_PLAYBOOK_NAME
              hosts: localhost
              vars:
                ansible_user: ANSIBLE_USER
                ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
              roles:
                - role: google.alloydbomni_orchestrator.backup
            

Replace the following variables:

        * `BACKUP_PLAN_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My BackupPlan`. Note the path to the playbook as it is required in the next step.

        * `ANSIBLE_USER`: name of the OS user that Ansible uses to log into your AlloyDB Omni nodes.

        * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

     2. Apply your `BackupPlan` resource:
            
            ansible-playbook BACKUP_PLAN_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
              -e resource_spec="BACKUP_PLAN_MANIFEST"

Replace the following variables:

        * `BACKUP_PLAN_PLAYBOOK`: path to the playbook that you created for your `BackupPlan` manifest earlier.

        * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

        * `BACKUP_PLAN_MANIFEST`: path to the `BackupPlan` manifest you created earlier.

     3. Create a `status.yaml` playbook if you have not already. For information on how to create the playbook, see View status and list backup resources.

     4. Confirm that the status field, `status.phase`, for your `BackupPlan` manifest is `Ready`. If the manifest is not ready, wait until it is:
            
            ansible-playbook status.yaml -i "DEPLOYMENT_SPEC_PATH" -e resource_type=BackupPlan \
              -e resource_name=BACKUP_PLAN_NAME


**Note:** If `status.phase` transitions to `Failed`, inspect the controller logs or run `alloydbctl get` with the `-o yaml` option against your resource to identify underlying issues.

## Update a backup plan

To update a backup plan to change the backup schedule, modify the retention period, or pause scheduled backups, modify the `BackupPlan` manifest and then re-apply it.

  1. Open the `BackupPlan` manifest that you created in Create a backup plan.

  2. Modify the fields you want to update.

     * To update the backup schedules, modify the cron expressions under `backupSchedules`.
     * To update the retention period, modify `backupRetainDays`.
     * To pause scheduled backups, add the `paused` field to the `spec` section and set it to `true`. To resume backups, set the field to `false` or remove the field.

For example, the following example updates the retention days to `30`, modifies the `full` and `differential` schedules, adds an `incremental` schedule, and pauses the backup plan:
    
    BackupPlan:
      metadata:
        name: BACKUP_PLAN_NAME
      spec:
        dbclusterRef: DBCLUSTER_NAME
        backupLocation:
          type: GCS
          gcsOptions:
            bucket: BUCKET_NAME
            key: BUCKET_PATH
            secretRef:
              name: SECRET_NAME
        backupRetainDays: 30
        backupSchedules:
          full: "0 4 * * *"
          differential: "0 0 * * 0"
          incremental: "0 12 * * *"
        paused: true
    

  3. Apply the updated backup plan using either of the following methods:

### `alloydbctl`

     1. Apply your `BackupPlan` resource:
            
            alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "BACKUP_PLAN_MANIFEST"

Replace the following variables:

        * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

        * `BACKUP_PLAN_MANIFEST`: path to the `BackupPlan` manifest you modified.

     2. Confirm that the status field, `status.phase`, for your `BackupPlan` manifest is `Ready`. If the manifest is not ready, wait until it is:
            
            alloydbctl get -d "DEPLOYMENT_SPEC_PATH" -t BackupPlan -n BACKUP_PLAN_NAME -o yaml

### Ansible

     1. Apply your updated `BackupPlan` resource using the playbook you created in Create a backup plan:
            
            ansible-playbook BACKUP_PLAN_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
              -e resource_spec="BACKUP_PLAN_MANIFEST"

Replace the following variables:

        * `BACKUP_PLAN_PLAYBOOK`: path to the playbook that you created for your `BackupPlan` manifest.

        * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

        * `BACKUP_PLAN_MANIFEST`: path to the `BackupPlan` manifest you modified.

     2. Create a `status.yaml` playbook if you have not already. For information on how to create the playbook, see View status and list backup resources.

     3. Confirm that the status field, `status.phase`, for your `BackupPlan` manifest is `Ready`. If the manifest is not ready, wait until it is before verification:
            
            ansible-playbook status.yaml -i "DEPLOYMENT_SPEC_PATH" -e resource_type=BackupPlan \
              -e resource_name=BACKUP_PLAN_NAME




## Delete a backup plan

To delete a backup plan, use either of the following methods:

**Caution:** Deleting a backup plan permanently erases all backups associated with that plan.

### `alloydbctl`
    
    
    alloydbctl delete -d "DEPLOYMENT_SPEC_PATH" -t BackupPlan -n BACKUP_PLAN_NAME

Replace the following variables:

  * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

  * `BACKUP_PLAN_NAME`: name of the `BackupPlan` manifest to delete.




### Ansible

  1. Create a playbook for deleting the `BackupPlan` manifest.
         
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

  2. Run `ansible-playbook` to delete the `BackupPlan` manifest.
         
         ansible-playbook BACKUP_PLAN_DELETE_PLAYBOOK_NAME -i "DEPLOYMENT_SPEC_PATH" -e resource_type=BackupPlan \
           -e resource_name=BACKUP_PLAN_NAME

Replace the following variables:

     * `BACKUP_PLAN_DELETE_PLAYBOOK_NAME`: path to the playbook that you created for deleting the `BackupPlan` manifest in the previous step.

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

     * `BACKUP_PLAN_NAME`: name of the `BackupPlan` manifest to delete.




## Create a backup

To create and initiate a backup, use either of the following methods:

### `alloydbctl`

  1. Create a `Backup` manifest using the following format:
         
         Backup:
           metadata:
             name: BACKUP_NAME
           spec:
             backupPlanRef: BACKUP_PLAN_NAME
             dbclusterRef: DBCLUSTER_NAME
             type: full
         

Replace the following variables:

     * `BACKUP_NAME`: name of the `Backup` manifest. For example, `my-backup-1`.

     * `BACKUP_PLAN_NAME`: name of the `BackupPlan` manifest you created earlier. For example, `my-backup-plan-1`.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster).

     * `type` (Optional): backup execution type that can set to either `full`, `diff`, or `incr`. Defaults to `full`.

  2. Apply your `Backup` manifest:
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "BACKUP_MANIFEST"

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

     * `BACKUP_MANIFEST`: path to the `Backup` manifest you created earlier.

  3. Confirm that the status field, `status.phase`, for your `Backup` manifest is `Succeeded`. If the manifest has not succeeded, wait until it is:
         
         alloydbctl get -d "DEPLOYMENT_SPEC_PATH" -t Backup -n BACKUP_NAME -o yaml

  4. Confirm that the backup files are available in your bucket by verifying if the `/backup/db` folder exists.




### Ansible

  1. Create a `Backup` manifest using the following format:
         
         Backup:
           metadata:
             name: BACKUP_NAME
           spec:
             backupPlanRef: BACKUP_PLAN_NAME
             dbclusterRef: DBCLUSTER_NAME
             type: full
         

Replace the following variables:

     * `BACKUP_NAME`: name of the `Backup` manifest. For example, `my-backup-1`.

     * `BACKUP_PLAN_NAME`: name of the `BackupPlan` manifest you created earlier. For example, `my-backup-plan-1`.

     * `DBCLUSTER_NAME`: name of your database cluster that you defined in [Create a cluster](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/create-cluster).

     * `type` (Optional): backup execution type that can set to either `full`, `diff`, or `incr`. Defaults to `full`.

  2. Create a playbook for your `Backup` manifest:
         
         - name: BACKUP_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.backup
         

Replace the following variables:

     * `BACKUP_PLAYBOOK_NAME`: name of your Ansible playbook. For example, `My Backup`.

     * `ANSIBLE_USER`: name of the OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  3. Apply your `Backup` manifest:
         
         ansible-playbook BACKUP_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
           -e resource_spec="BACKUP_MANIFEST"

Replace the following variables:

     * `BACKUP_PLAYBOOK`: path to the playbook that you created for your `Backup` manifest that you created earlier.

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

     * `BACKUP_MANIFEST`: path to the `Backup` manifest you created earlier.

  4. Create a `status.yaml` playbook if you have not already. For information on how to create the playbook, see View status and list backup resources.

  5. Confirm that the status field, `status.phase`, for your `Backup` manifest is `Succeeded`. If the manifest has not succeeded, wait until it has before verification:
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC_PATH" -e resource_type=Backup \
           -e resource_name=BACKUP_NAME

  6. Confirm that the backup files are available in your bucket by verifying if the `/backup/db` folder exists.




**Note:** If `status.phase` transitions to `Failed`, inspect the controller logs or run `alloydbctl get` with the `-o yaml` option against your resource to identify underlying issues.

## Delete a backup

To delete a backup, run one of the following commands:

### `alloydbctl`
    
    
    alloydbctl delete -d "DEPLOYMENT_SPEC_PATH" -t Backup -n BACKUP_NAME

Replace the following variables:

  * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

  * `BACKUP_NAME`: name of the `Backup` manifest to delete.




### Ansible

  1. Create a playbook for deleting the `Backup` manifest.
         
         - name: BACKUP_DELETE_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.delete
         

Replace the following variables:

     * `BACKUP_DELETE_PLAYBOOK_NAME`: name of your Ansible playbook.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  2. Run `ansible-playbook` to delete the `Backup` manifest.
         
         ansible-playbook BACKUP_DELETE_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" -e resource_type=Backup \
           -e resource_name=BACKUP_NAME

Replace the following variables:

     * `BACKUP_DELETE_PLAYBOOK`: path to the playbook that you created for deleting the `Backup` manifest in the previous step.

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

     * `BACKUP_NAME`: name of the `Backup` manifest to delete.




## Restore from a backup or point in time (PITR)

To restore data from a backup, apply a `Restore` manifest. The RPM orchestrator performs recovery in-place, which modifies your target database cluster directly without spinning up a cloned cluster or requiring manual script execution.

**Caution:** Restoring from a backup overwrites all of your database cluster's data.

To restore from a backup, use either of the following methods:

### `alloydbctl`

  1. Create a `Restore` manifest using the following format:

     * To restore from a specific named backup run:
    
    Restore:
      metadata:
        name: RESTORE_NAME
      spec:
        sourceDBCluster: DBCLUSTER_NAME
        backup: BACKUP_NAME
    

     * To perform a Point-in-Time Restore (PITR):
           
           Restore:
             metadata:
               name: RESTORE_NAME
             spec:
               sourceDBCluster: DBCLUSTER_NAME
               pointInTime: "TIMESTAMP"
           

Replace the following variables:

     * `RESTORE_NAME`: name for this `Restore` manifest. For example, `my-restore-1`.

     * `DBCLUSTER_NAME`: name of your target database cluster to recover in-place.

     * `BACKUP_NAME`: name of the completed `Backup` manifest to restore from.

     * `TIMESTAMP`: RFC 3339 timestamp identifying the exact point in time to recover to. For example, `2026-06-19T14:30:00Z`.

  2. Apply your `Restore` manifest:
         
         alloydbctl apply -d "DEPLOYMENT_SPEC_PATH" -r "RESTORE_MANIFEST"

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification you created in [Install AlloyDB Omni components](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/install-components).

     * `RESTORE_MANIFEST`: path to the `Restore` manifest specification file you created in step 1.

  3. Confirm that `status.phase` for your `Restore` manifest transitions to `Succeeded`:
         
         alloydbctl get -d "DEPLOYMENT_SPEC_PATH" -t Restore -n RESTORE_NAME -o yaml




### Ansible

  1. Create a `Restore` manifest using the following format:

     * To restore from a specific named backup run:
    
    Restore:
      metadata:
        name: RESTORE_NAME
      spec:
        sourceDBCluster: DBCLUSTER_NAME
        backup: BACKUP_NAME
    

     * To perform a Point-in-Time Restore (PITR):
           
           Restore:
             metadata:
               name: RESTORE_NAME
             spec:
               sourceDBCluster: DBCLUSTER_NAME
               pointInTime: "TIMESTAMP"
           

Replace the following variables:

     * `RESTORE_NAME`: name for this `Restore` manifest. For example, `my-restore-1`.

     * `DBCLUSTER_NAME`: name of your target database cluster to recover in-place.

     * `BACKUP_NAME`: name of the completed `Backup` manifest to restore from.

     * `TIMESTAMP`: RFC 3339 timestamp identifying the exact point in time to recover to. For example, `2026-06-19T14:30:00Z`.

  2. Create a playbook for your `Restore` manifest:
         
         - name: RESTORE_PLAYBOOK_NAME
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.restore
         

Replace the following variables:

     * `RESTORE_PLAYBOOK_NAME`: name of your Ansible playbook.

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your AlloyDB Omni nodes.

     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your AlloyDB Omni nodes using SSH.

  3. Apply your `Restore` manifest:
         
         ansible-playbook RESTORE_PLAYBOOK -i "DEPLOYMENT_SPEC_PATH" \
           -e resource_spec="RESTORE_MANIFEST"

Replace the following variables:

     * `RESTORE_PLAYBOOK`: path to the playbook that you created for your `Restore` manifest in step 2.

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification.

     * `RESTORE_MANIFEST`: path to the `Restore` manifest specification file you created in step 1.

  4. Create a `status.yaml` playbook if you have not already. For information on how to create the playbook, see View status and list backup resources.

  5. Confirm that `status.phase` for your `Restore` manifest transitions to `Succeeded`:
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC_PATH" -e resource_type=Restore \
           -e resource_name=RESTORE_NAME




**Note:** If `status.phase` transitions to `Failed`, inspect the controller logs or run `alloydbctl get` with the `-o yaml` option against your resource to identify underlying issues.

## View status and list backup resources

To view the status of or list your `BackupPlan`, `Backup`, and `Restore` resources, use either of the following methods:

### `alloydbctl`

To list all resources of a specific type, run the `alloydbctl get` command:
    
    
    alloydbctl get -d "DEPLOYMENT_SPEC_PATH" -t RESOURCE_TYPE

To view the status of a specific resource, run the `alloydbctl get` command with the resource name and output format set to `yaml`:
    
    
    alloydbctl get -d "DEPLOYMENT_SPEC_PATH" -t RESOURCE_TYPE -n RESOURCE_NAME -o yaml

Replace the following variables:

  * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification.
  * `RESOURCE_TYPE`: the resource type. Set this to `BackupPlan`, `Backup`, or `Restore`.
  * `RESOURCE_NAME`: the name of the resource you want to view the status of.



### Ansible

To view the status of or list resources using Ansible, use the `google.alloydbomni_orchestrator.status` role.

  1. Create a playbook, for example `status.yaml`, using the following format:
         
         - name: Get resource status
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
           - role: google.alloydbomni_orchestrator.status
         

Replace the following variables:

     * `ANSIBLE_USER`: OS user that Ansible uses to log into your nodes.
     * `ANSIBLE_SSH_PRIVATE_KEY_FILE`: private key Ansible uses to connect to your nodes using SSH.
  2. Run the playbook.

To list all resources of a specific type, run the playbook with the `resource_type` variable:
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC_PATH" -e resource_type=RESOURCE_TYPE

To view the status of a specific resource, run the playbook with both the `resource_type` and `resource_name` variables:
         
         ansible-playbook status.yaml -i "DEPLOYMENT_SPEC_PATH" -e resource_type=RESOURCE_TYPE \
           -e resource_name=RESOURCE_NAME

Replace the following variables:

     * `DEPLOYMENT_SPEC_PATH`: path to the deployment specification.
     * `RESOURCE_TYPE`: the resource type. Set this to `BackupPlan`, `Backup`, or `Restore`.
     * `RESOURCE_NAME`: the name of the resource you want to view the status of.



## Limitations

  * If a `BackupPlan` status shows `ConfigurationFailed` with `failed to create stanza` (exit code `39`), you can resume reconciliation by granting the `roles/storage.objectAdmin` role on the bucket and re-applying the manifest. There is no need to delete the `BackupPlan`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
