---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery/
title: Back up and recover SAP HANA by using disk snapshots \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:49.089519+00:00
---

# Back up and recover SAP HANA by using disk snapshots  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/perform-disk-snapshot-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Back up and recover SAP HANA by using disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to back up and recover your SAP HANA database by using the _disk snapshot_ feature of Google Cloud's Agent for SAP.

For information about this feature, see [Backup and recovery for SAP HANA by using disk snapshots](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).

## Before you begin

  * Validate the installation of Google Cloud's Agent for SAP. For instructions, see [Install and configure Google Cloud's Agent for SAP on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm).
  * Validate that your SAP HANA system is deployed on a Compute Engine instance as follows:

    * It is not deployed with the host auto-failover solution. For more information, see [Using snapshots with scale-out deployments](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery#using_snapshots_with_scaleout_deployments).
    * It uses an SAP-certified operating system (OS). For more information, see [OS support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support)
    * The `/hana/data` volume is independently hosted on one or more SSD-based Persistent Disk or Hyperdisk volume. These disks must host no other SAP HANA volume. As described in the SAP Note [2039883 - FAQ: SAP HANA database and data snapshots (storage snapshots)](https://me.sap.com/notes/2039883), to be able to recover your SAP HANA database, the storage snapshot must not include the log area of the database.

If you're using more than one disk to host your `/hana/data` volume, then you can use the disk snapshot feature of the agent only when the underlying disks are Hyperdisk volumes.

    * The `/hana/data` volume is mapped to a logical volume. This enables the agent correctly handle the mount point during disk snapshot based backup or recovery operations.
    * The underlying infrastructure is not deployed using Infrastructure as Code (IaC) tools such as Terraform. For more information, see [Using snapshots with IaC tool based deployments](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery#using_snapshots_with_iac).



## Set permissions

To back up and recover your SAP HANA database by using the disk snapshot feature of Google Cloud's Agent for SAP, you must set the following permissions:

  * To let the agent attach disks to a compute instance hosting your SAP HANA workload, grant the compute instance's service account the [Service Account User (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) IAM role.

  * To create [disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots), grant the following IAM permissions:

###  Scale-up with one data disk 

If your `/hana/data` volume is hosted on one Persistent Disk or Hyperdisk volume, then grant the following permissions to your Compute Engine instance's service account:

    * To create disk snapshots during backup operations, and create new disks during recovery operations: `compute.disks.create`, `compute.disks.createSnapshot`, `compute.snapshots.create`
    * To detach disks from compute instances, and attach new disks to those compute instances: `compute.instances.attachDisk`, `compute.instances.detachDisk`
    * To verify the completion of tasks during backup and recovery operations: `compute.disks.get`, `compute.disks.use`, `compute.globalOperations.get`, `compute.instances.get`, `compute.snapshots.get`, `compute.snapshots.useReadOnly`, `compute.zoneOperations.get`
    * To apply labels to disks and disk snapshots for identifying backups and mapping restored disks to the appropriate compute instances: `compute.disks.setLabels`, `compute.snapshots.setLabels`

The following snippet lists these IAM permissions:
    
    # Mandatory permissions
    compute.disks.create
    compute.disks.createSnapshot
    compute.disks.get
    compute.disks.setLabels
    compute.disks.use
    compute.globalOperations.get
    compute.instances.attachDisk
    compute.instances.detachDisk
    compute.instances.get
    compute.snapshots.create
    compute.snapshots.get
    compute.snapshots.setLabels
    compute.snapshots.useReadOnly
    compute.zoneOperations.get
    

###  Scale-up with striped data disks 

If your `/hana/data` volume is hosted on more than one Persistent Disk or Hyperdisk volume, then grant the following permissions to your Compute Engine instance:

    * To create disk snapshots during backup operations, and create new disks during recovery operations: `compute.disks.create`, `compute.instantSnapshotGroups.create`, `compute.snapshotGroups.create`, `compute.snapshots.create`
    * To detach disks from compute instances, and attach new disks to those compute instances: `compute.instances.attachDisk`, `compute.instances.detachDisk`
    * To verify the completion of tasks during backup and recovery operations: `compute.disks.get`, `compute.disks.list`, `compute.disks.use`, `compute.disks.useReadOnly`, `compute.globalOperations.get`, `compute.instances.get`, `compute.instantSnapshotGroups.get`, `compute.instantSnapshotGroups.list`, `compute.instantSnapshotGroups.useReadOnly`, `compute.instantSnapshots.list`, `compute.instantSnapshots.useReadOnly`, `compute.resourcePolicies.use`, `compute.resourcePolicies.useReadOnly`, `compute.snapshots.get`, `compute.snapshots.list`, `compute.snapshots.useReadOnly`, `compute.snapshotGroups.get`, `compute.snapshotGroups.list`, `compute.snapshotGroups.useReadOnly`, `compute.zoneOperations.get`
    * To apply labels to disks and disk snapshots for identifying backups and mapping restored disks to the appropriate compute instances: `compute.disks.setLabels`, `compute.snapshots.setLabels`
    * (Recommended) To remove and add disks from your [consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#consistency_groups) during backup and recovery operations: `compute.disks.addResourcePolicies`, `compute.disks.removeResourcePolicies`
    * (Recommended) To delete the temporary instant snapshot groups after the successful creation of durable snapshots, and let the agent to roll back the created snapshot groups if it fails to register a backup in the SAP HANA backup catalog: `compute.instantSnapshotGroups.delete`, `compute.snapshotGroups.delete`

The following snippet lists these IAM permissions:
    
    # Mandatory permissions
    compute.disks.create
    compute.disks.get
    compute.disks.list
    compute.disks.setLabels
    compute.disks.use
    compute.disks.useReadOnly
    compute.globalOperations.get
    compute.instances.attachDisk
    compute.instances.detachDisk
    compute.instances.get
    compute.instantSnapshotGroups.create
    compute.instantSnapshotGroups.get
    compute.instantSnapshotGroups.list
    compute.instantSnapshotGroups.useReadOnly
    compute.instantSnapshots.list
    compute.instantSnapshots.useReadOnly
    compute.resourcePolicies.use
    compute.resourcePolicies.useReadOnly
    compute.snapshots.create
    compute.snapshots.get
    compute.snapshots.list
    compute.snapshots.setLabels
    compute.snapshots.useReadOnly
    compute.snapshotGroups.create
    compute.snapshotGroups.get
    compute.snapshotGroups.list
    compute.snapshotGroups.useReadOnly
    compute.zoneOperations.get
    
    # Recommended permissions
    compute.disks.addResourcePolicies
    compute.disks.removeResourcePolicies
    compute.instantSnapshotGroups.delete
    compute.snapshotGroups.delete
    

###  Scale-out except host auto-failover 

For a scale-out deployment, grant the following permissions to your Compute Engine instance:

    * To create disk snapshots during backup operations, and create new disks during recovery operations: `compute.disks.create`, `compute.instantSnapshotGroups.create`, `compute.snapshotGroups.create`, `compute.snapshots.create`
    * To detach disks from compute instances, and attach new disks to those compute instances: `compute.instances.attachDisk`, `compute.instances.detachDisk`
    * To verify the completion of tasks during backup and recovery operations: `compute.disks.get`, `compute.disks.list`, `compute.disks.use`, `compute.disks.useReadOnly`, `compute.globalOperations.get`, `compute.instances.get`, `compute.instantSnapshotGroups.get`, `compute.instantSnapshotGroups.list`, `compute.instantSnapshotGroups.useReadOnly`, `compute.instantSnapshots.list`, `compute.instantSnapshots.useReadOnly`, `compute.resourcePolicies.use`, `compute.resourcePolicies.useReadOnly`, `compute.snapshots.get`, `compute.snapshots.list`, `compute.snapshots.useReadOnly`, `compute.snapshotGroups.get`, `compute.snapshotGroups.list`, `compute.snapshotGroups.useReadOnly`, `compute.zoneOperations.get`
    * To apply labels to disks and disk snapshots for identifying backups and mapping restored disks to the appropriate compute instances: `compute.disks.setLabels`, `compute.snapshots.setLabels`
    * (Recommended) To remove and add disks from your [consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/about#consistency_groups) during backup and recovery operations: `compute.disks.addResourcePolicies`, `compute.disks.removeResourcePolicies`
    * (Recommended) To delete the temporary instant snapshot groups after the successful creation of durable snapshots, and let the agent to roll back the created snapshot groups if it fails to register a backup in the SAP HANA backup catalog: `compute.instantSnapshotGroups.delete`, `compute.snapshotGroups.delete`

The following snippet lists these IAM permissions:
    
    # Mandatory permissions
    compute.disks.create
    compute.disks.get
    compute.disks.list
    compute.disks.setLabels
    compute.disks.use
    compute.disks.useReadOnly
    compute.globalOperations.get
    compute.instances.attachDisk
    compute.instances.detachDisk
    compute.instances.get
    compute.instantSnapshotGroups.create
    compute.instantSnapshotGroups.get
    compute.instantSnapshotGroups.list
    compute.instantSnapshotGroups.useReadOnly
    compute.instantSnapshots.list
    compute.instantSnapshots.useReadOnly
    compute.resourcePolicies.use
    compute.resourcePolicies.useReadOnly
    compute.snapshots.create
    compute.snapshots.get
    compute.snapshots.list
    compute.snapshots.setLabels
    compute.snapshots.useReadOnly
    compute.snapshotGroups.create
    compute.snapshotGroups.get
    compute.snapshotGroups.list
    compute.snapshotGroups.useReadOnly
    compute.zoneOperations.get
    
    # Recommended permissions
    compute.disks.addResourcePolicies
    compute.disks.removeResourcePolicies
    compute.instantSnapshotGroups.delete
    compute.snapshotGroups.delete
    

  * To encrypt restored disks with a Customer-Managed Encryption Key (CMEK), make sure that the Compute Engine service agent (`service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`) has the [Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) IAM role on the target KMS key specified by `-target-kms-key`, and on any KMS key used by the source snapshot(s) if they are CMEK-encrypted.

For more information about the required roles for CMEK encryption, see [Customer-managed encryption keys required roles](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#required-roles) and [Using CMEK with Cloud KMS keys from another project](https://docs.cloud.google.com/kms/docs/cmek#kms-keys-other-project).

If the target Cloud KMS key resides in a different Google Cloud organization than your VM instance, ensure the following organization-level prerequisites are met in the organization hosting the KMS key:

    * **Domain Restricted Sharing (DRS)** : The administrator of the destination organization must configure the `constraints/iam.allowedPolicyMemberDomains` organization policy to permit identities from your VM's organization (for example, by adding your organization's Google Workspace Customer ID to the allowed list). For more information, see [Restricting identities by domain](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains).
    * **VPC Service Controls (VPC-SC)** : If the destination project is protected by a VPC-SC perimeter, the perimeter must be configured with ingress rules to allow the VM's service account to access the Cloud KMS API and the specific key resource within the perimeter. For more information, see [VPC Service Controls overview](https://docs.cloud.google.com/vpc-service-controls/docs/overview) and [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).
  * To create disk snapshot based backups, the SAP HANA database user used by the agent must have the `BACKUP OPERATOR` or `BACKUP ADMIN` privilege. For more information, see the SAP document [Authorizations Needed for Backup and Recovery](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/c4b71703bb571014810ebb38dc59cf51.html#backup-admin-versus-backup-operator)

  * To back up and recover your SAP HANA database, the operating system user running the agent's commands must either be the `root` user, or have `sudo` access to run the following commands. You can also provide `sudo` access by creating a group in your `/etc/sudoers.d` directory, for example:
        
        %sapagent_snapshot_sudoers ALL=(ALL:ALL) NOPASSWD:/sbin/lvdisplay, /sbin/vgscan, /sbin/dmsetup, /sbin/lvscan, /usr/sbin/xfs_freeze, /usr/bin/google_cloud_sap_agent




### Validate the setup for disk snapshot based backup and recovery

You can validate if you have the correct Google Cloud setup for using the agent to perform disk snapshot based backup and recovery operations for your SAP HANA system. You do this by running the agent's `status` command, which is supported from version 3.7 of the agent.

To do this, complete the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.
  2. Run the following command:
         
         sudo /usr/bin/google_cloud_sap_agent status -f="disk_snapshot"
         

If your setup for disk snapshot based backup and recovery is correct, then the output includes the following. Your configuration might have values other than the **`default`** ones.
         
         Agent Status:
             ...
             Systemd Service Enabled: True
             Systemd Service Running: True
             Cloud API Full Scopes: True
             Configuration File: /etc/google-cloud-sap-agent/configuration.json
             Configuration Valid: True
         ...
         ----------------------------------------------------------------------------
         Disk Snapshot: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
         ...




## Create a disk consistency group

If your `/hana/data` volume is hosted on one disk, then skip this section.

If your `/hana/data` volume is hosted on more than one disk, then you must create a consistency group and add the disks hosting your `/hana/data` volume to that consistency group. You must create the consistency group in the same region as the disks.

For information about how to do this, see [Create a consistency group](https://docs.cloud.google.com/compute/docs/disks/async-pd/manage-consistency-groups#create_a_consistency_group).

Make note of the consistency group name. It's used by the agent while creating the snapshot based backup.

## Create a disk snapshot based backup

To create a disk snapshot based backup for the `/hana/data` volume of your SAP HANA database, run the `hanadiskbackup` command of Google Cloud's Agent for SAP:

###  Scale-up with one data disk 

To create a disk snapshot based backup for the `/hana/data` volume of your SAP HANA database, run the `hanadiskbackup` command of Google Cloud's Agent for SAP:

From version 3.3, the arguments `-source-disk` and `-source-disk-zone` are optional for use with the `hanadiskbackup` command. This is because the agent can auto-detect the disk that hosts your `/hana/data` directory. However, if you specify these arguments, then they override the agent's auto-detection.

  * If you want to use an [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -sid=SID \
              -hdbuserstore-key=HDB_USERSTORE_KEY

  * If you want to use a username and Secret Manager secret for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -host=HANA_HOST_ADDRESS \
              -port=HANA_PORT_NUMBER \
              -sid=SID \
              -hana-db-user=HANA_USERNAME \
              -password-secret=HANA_USER_PWD_SECRET_NAME

  * If you want to use a username and password for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -host=HANA_HOST_ADDRESS \
              -port=HANA_PORT_NUMBER \
              -sid=SID \
              -hana-db-user=HANA_USERNAME \
              -password=HANA_PASSWORD




Replace the following:

  * `DESTINATION_PROJECT_ID`: the ID of the Google Cloud project in which you want to create the disk snapshot
  * `HANA_HOST_ADDRESS`: the hostname or IP address of the Compute Engine instance that hosts your SAP HANA database

In a high-availability (HA) system, specify the hostname or IP address of the local host in the primary SAP HANA node. Don't use the virtual IP (VIP) used in the cluster to identify the primary node. In a disaster recovery (DR) deployment, specify the hostname or IP address of the local host in the primary SAP HANA instance.

  * `HANA_PORT_NUMBER`: the SAP HANA port that accepts the backup and recovery requests

  * `SID`: the SAP system identifier (SID) of your SAP HANA system

  * `HANA_USERNAME`: the SAP HANA database username using which you want to create the backup

  * `HDB_USERSTORE_KEY`: if you've created an [`hdbuserstore`](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key to authenticate the specified SAP HANA user, then specify that key

  * `HANA_USER_PWD_SECRET_NAME`: if you're using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the SAP HANA database user's password, then specify the corresponding secret name

  * `HANA_PASSWORD`: if you're using a plain text password for SAP HANA authentication, then specify that password 




The following table describes the arguments supported by the `hanadiskbackup` command:

Argument | Description  
---|---  
`-port` | Specify the SAP HANA port that accepts the backup and recovery requests.  
`-sid` | Specify the SAP system identifier (SID) of your SAP HANA system.  
`-hana-db-user` | Specify the SAP HANA database username using which you want to create the backup. If you specify `-hdbuserstore-key`, then you can skip specifying the `-hana-db-user` argument.  
`-password` |  Specify the password of the SAP HANA database user that you use to create the backup. Don't specify this argument if you're using the `-password-secret` or the `-hdbuserstore-key` argument. We recommend that you use either of them instead of using `-password`. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-password-secret` |  Optional. If you're using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the SAP HANA database user's password, then specify the corresponding secret name. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the same Google Cloud project that you specify for the `-project` argument.For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-hdbuserstore-key` |  To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. If you specify `-hdbuserstore-key`, then you can skip specifying the `-host`, `-port`, and `-hana-db-user` arguments. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-host` | Optional. Specify the IP address of the Compute Engine instance that hosts your SAP HANA system. The default value is `localhost`.  
`-project` | Optional. Specify the ID of the Google Cloud project where your SAP HANA instance is running.  
`-abandon-prepared` | Optional. Specifies whether to ignore any existing snapshot based backup or not. The default value is `false`.  
`-snapshot-name` |  Optional. Specify the name for the disk snapshot that you're creating. This argument is applicable only when your `/hana/data` volume is hosted on one disk. By default, the snapshot is named by using the following format: `PREFIX-TIMESTAMP_IN_UTC-SOURCE_DISK_NAME`. From version 3.11 of the agent, while creating backup, you can specify a prefix for the snapshot name by specifying the `-snapshot-prefix` argument. If you don't specify this argument, then the prefix defaults to `snapshot`.  
`-snapshot-prefix` |  Optional. Specify the prefix that you want to set for the names of the snapshots or group snapshots. This argument is supported from version 3.11 of the agent.  
`-snapshot-description` | Optional. Specify a description for the disk snapshot. This argument is applicable only when your `/hana/data` volume is hosted on one disk.  
`-snapshot-type` |  Optional. Specify the type of snapshots that you want to create for the disks hosting your `/hana/data` volume. This argument is applicable only when your `/hana/data` volume is hosted on more than one disk. By default, the agent creates standard snapshots. Supported values for this argument: `STANDARD`, `ARCHIVE`. For information about these snapshot types, see [ About archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots#incremental-snapshots). This argument is supported from version 3.6 of the agent.  
`-group-snapshot-name` |  Optional. Specify the snapshot group name for the snapshots of the disks hosting your `/hana/data` volume. This argument is supported from version 3.6 of the agent. By default, the snapshot group name is set by using the following format: `PREFIX-TIMESTAMP_IN_UTCCONSISTENCY_GROUP_NAME`. Here, `CONSISTENCY_GROUP_NAME` is the name of the disk consistency group that you created in the section Create a disk consistency group. From version 3.11 of the agent, you can specify a prefix for the snapshot name. If you don't specify the `-snapshot-prefix` while creating the backup, then the prefix defaults to `group-snapshot`.  
`-labels` | Optional. Specify one or more label-value pairs that you want to associate with the disk snapshots you're creating. For example: `-labels="label1=value1,label2=value2"`.  
`-storage-location` | Optional. Specify the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your disk snapshot.  
`-freeze-file-system` |  Optional. Specifies whether or not the agent is to freeze the file system of your SAP HANA database. The default value is `false`. This argument is supported from version 3.2 of the agent.  
`-send-metrics-to-monitoring` | Optional. Specifies whether or not the execution status of the snapshot creation is sent to Cloud Monitoring. The default value is `TRUE`.  
`-loglevel` | Optional. Specify the logging level for the snapshot creation operation. The default logging level is `info`. The available log levels are: `debug`, `info`, `warn`, and `error`.  
`-confirm-data-snapshot-after-create` |  Optional. If you want to confirm the snapshot creation to SAP HANA immediately after the snapshot is created but without confirming that it has been uploaded to the Cloud Storage bucket specified for the `-storage-location` argument, then specify the value `TRUE`. The default value is `FALSE`, which causes the agent to confirm snapshot creation after the completion of both `CREATE` and `UPLOAD` operations. This argument is supported from version 3.4 of the agent.  
`-hana-query-timeout` |  Optional. Specify the timeout for SAP HANA database queries in seconds. The default value is `600` (10 minutes). This argument is supported from version 3.15-952132455 of the agent.  
  
###  Scale-up with striped data disks 

To create a disk snapshot based backup for the `/hana/data` volume of your SAP HANA database, run the `hanadiskbackup` command of Google Cloud's Agent for SAP:

From version 3.3, the arguments `-source-disk` and `-source-disk-zone` are optional for use with the `hanadiskbackup` command. This is because the agent can auto-detect the disk that hosts your `/hana/data` directory. However, if you specify these arguments, then they override the agent's auto-detection.

  * If you want to use an [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -sid=SID \
              -hdbuserstore-key=HDB_USERSTORE_KEY

  * If you want to use a username and Secret Manager secret for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -host=HANA_HOST_ADDRESS \
              -port=HANA_PORT_NUMBER \
              -sid=SID \
              -hana-db-user=HANA_USERNAME \
              -password-secret=HANA_USER_PWD_SECRET_NAME

  * If you want to use a username and password for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -host=HANA_HOST_ADDRESS \
              -port=HANA_PORT_NUMBER \
              -sid=SID \
              -hana-db-user=HANA_USERNAME \
              -password=HANA_PASSWORD




Replace the following:

  * `DESTINATION_PROJECT_ID`: the ID of the Google Cloud project in which you want to create the disk snapshot
  * `HANA_HOST_ADDRESS`: the hostname or IP address of the Compute Engine instance that hosts your SAP HANA database

In a high-availability (HA) system, specify the hostname or IP address of the local host in the primary SAP HANA node. Don't use the virtual IP (VIP) used in the cluster to identify the primary node. In a disaster recovery (DR) deployment, specify the hostname or IP address of the local host in the primary SAP HANA instance.

  * `HANA_PORT_NUMBER`: the SAP HANA port that accepts the backup and recovery requests

  * `SID`: the SAP system identifier (SID) of your SAP HANA system

  * `HANA_USERNAME`: the SAP HANA database username using which you want to create the backup

  * `HDB_USERSTORE_KEY`: if you've created an [`hdbuserstore`](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key to authenticate the specified SAP HANA user, then specify that key

  * `HANA_USER_PWD_SECRET_NAME`: if you're using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the SAP HANA database user's password, then specify the corresponding secret name

  * `HANA_PASSWORD`: if you're using a plain text password for SAP HANA authentication, then specify that password 




The following table describes the arguments supported by the `hanadiskbackup` command:

Argument | Description  
---|---  
`-port` | Specify the SAP HANA port that accepts the backup and recovery requests.  
`-sid` | Specify the SAP system identifier (SID) of your SAP HANA system.  
`-hana-db-user` | Specify the SAP HANA database username using which you want to create the backup. If you specify `-hdbuserstore-key`, then you can skip specifying the `-hana-db-user` argument.  
`-password` |  Specify the password of the SAP HANA database user that you use to create the backup. Don't specify this argument if you're using the `-password-secret` or the `-hdbuserstore-key` argument. We recommend that you use either of them instead of using `-password`. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-password-secret` |  Optional. If you're using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the SAP HANA database user's password, then specify the corresponding secret name. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the same Google Cloud project that you specify for the `-project` argument.For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-hdbuserstore-key` |  To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. If you specify `-hdbuserstore-key`, then you can skip specifying the `-host`, `-port`, and `-hana-db-user` arguments. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-host` | Optional. Specify the IP address of the Compute Engine instance that hosts your SAP HANA system. The default value is `localhost`.  
`-project` | Optional. Specify the ID of the Google Cloud project where your SAP HANA instance is running.  
`-abandon-prepared` | Optional. Specifies whether to ignore any existing snapshot based backup or not. The default value is `false`.  
`-snapshot-name` |  Optional. Specify the name for the disk snapshot that you're creating. This argument is applicable only when your `/hana/data` volume is hosted on one disk. By default, the snapshot is named by using the following format: `PREFIX-TIMESTAMP_IN_UTC-SOURCE_DISK_NAME`. From version 3.11 of the agent, while creating backup, you can specify a prefix for the snapshot name by specifying the `-snapshot-prefix` argument. If you don't specify this argument, then the prefix defaults to `snapshot`.  
`-snapshot-prefix` |  Optional. Specify the prefix that you want to set for the names of the snapshots or group snapshots. This argument is supported from version 3.11 of the agent.  
`-snapshot-description` | Optional. Specify a description for the disk snapshot. This argument is applicable only when your `/hana/data` volume is hosted on one disk.  
`-snapshot-type` |  Optional. Specify the type of snapshots that you want to create for the disks hosting your `/hana/data` volume. This argument is applicable only when your `/hana/data` volume is hosted on more than one disk. By default, the agent creates standard snapshots. Supported values for this argument: `STANDARD`, `ARCHIVE`. For information about these snapshot types, see [ About archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots#incremental-snapshots). This argument is supported from version 3.6 of the agent.  
`-group-snapshot-name` |  Optional. Specify the snapshot group name for the snapshots of the disks hosting your `/hana/data` volume. This argument is supported from version 3.6 of the agent. By default, the snapshot group name is set by using the following format: `PREFIX-TIMESTAMP_IN_UTCCONSISTENCY_GROUP_NAME`. Here, `CONSISTENCY_GROUP_NAME` is the name of the disk consistency group that you created in the section Create a disk consistency group. From version 3.11 of the agent, you can specify a prefix for the snapshot name. If you don't specify the `-snapshot-prefix` while creating the backup, then the prefix defaults to `group-snapshot`.  
`-labels` | Optional. Specify one or more label-value pairs that you want to associate with the disk snapshots you're creating. For example: `-labels="label1=value1,label2=value2"`.  
`-source-disks` | Optional. Specify the names of the disks hosting the `/hana/data` volume in your deployment. Use a comma to separate the disk names. For example: `-source-disks="disk-name-1, disk-name-2"`.   
`-storage-location` | Optional. Specify the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your disk snapshot.  
`-freeze-file-system` |  Optional. Specifies whether or not the agent is to freeze the file system of your SAP HANA database. The default value is `false`. This argument is supported from version 3.2 of the agent.  
`-send-metrics-to-monitoring` | Optional. Specifies whether or not the execution status of the snapshot creation is sent to Cloud Monitoring. The default value is `TRUE`.  
`-loglevel` | Optional. Specify the logging level for the snapshot creation operation. The default logging level is `info`. The available log levels are: `debug`, `info`, `warn`, and `error`.  
`-confirm-data-snapshot-after-create` |  Optional. If you want to confirm the snapshot creation to SAP HANA immediately after the snapshot is created but without confirming that it has been uploaded to the Cloud Storage bucket specified for the `-storage-location` argument, then specify the value `TRUE`. The default value is `FALSE`, which causes the agent to confirm snapshot creation after the completion of both `CREATE` and `UPLOAD` operations. This argument is supported from version 3.4 of the agent.  
`-hana-query-timeout` |  Optional. Specify the timeout for SAP HANA database queries in seconds. The default value is `600` (10 minutes). This argument is supported from version 3.15-952132455 of the agent.  
  
###  Scale-out except host auto-failover 

To create a disk snapshot based backup for the `/hana/data` volume of your SAP HANA database, run the `hanadiskbackup` command of Google Cloud's Agent for SAP:

  * If you want to use an [`hdbuserstore` key](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -sid=SID \
              -hdbuserstore-key=HDB_USERSTORE_KEY \
              -source-disks="COMMA_SEPARATED_DISK_NAMES"

  * If you want to use a username and Secret Manager secret for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -host=HANA_HOST_ADDRESS \
              -port=HANA_PORT_NUMBER \
              -sid=SID \
              -hana-db-user=HANA_USERNAME \
              -password-secret=HANA_USER_PWD_SECRET_NAME \
              -source-disks="COMMA_SEPARATED_DISK_NAMES"

  * If you want to use a username and password for SAP HANA authentication, then run the following command: 
        
        sudo /usr/bin/google_cloud_sap_agent hanadiskbackup \
              -project=DESTINATION_PROJECT_ID \
              -host=HANA_HOST_ADDRESS \
              -port=HANA_PORT_NUMBER \
              -sid=SID \
              -hana-db-user=HANA_USERNAME \
              -password=HANA_PASSWORD \
              -source-disks="COMMA_SEPARATED_DISK_NAMES"




Replace the following:

  * `DESTINATION_PROJECT_ID`: the ID of the Google Cloud project in which you want to create the disk snapshot
  * `HANA_HOST_ADDRESS`: the hostname or IP address of the Compute Engine instance that hosts your SAP HANA database

In a high-availability (HA) system, specify the hostname or IP address of the local host in the primary SAP HANA node. Don't use the virtual IP (VIP) used in the cluster to identify the primary node. In a disaster recovery (DR) deployment, specify the hostname or IP address of the local host in the primary SAP HANA instance.

  * `HANA_PORT_NUMBER`: the SAP HANA port that accepts the backup and recovery requests

  * `SID`: the SAP system identifier (SID) of your SAP HANA system

  * `HANA_USERNAME`: the SAP HANA database username using which you want to create the backup

  * `HDB_USERSTORE_KEY`: if you've created an [`hdbuserstore`](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key to authenticate the specified SAP HANA user, then specify that key

  * `HANA_USER_PWD_SECRET_NAME`: if you're using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the SAP HANA database user's password, then specify the corresponding secret name

  * `HANA_PASSWORD`: if you're using a plain text password for SAP HANA authentication, then specify that password 

  * `COMMA_SEPARATED_DISK_NAMES`: a comma-separated list of disk names that host the `/hana/data` volume in your scale-out system 




The following table describes the arguments supported by the `hanadiskbackup` command:

Argument | Description  
---|---  
`-port` | Specify the SAP HANA port that accepts the backup and recovery requests.  
`-sid` | Specify the SAP system identifier (SID) of your SAP HANA system.  
`-hana-db-user` | Specify the SAP HANA database username using which you want to create the backup. If you specify `-hdbuserstore-key`, then you can skip specifying the `-hana-db-user` argument.  
`-password` |  Specify the password of the SAP HANA database user that you use to create the backup. Don't specify this argument if you're using the `-password-secret` or the `-hdbuserstore-key` argument. We recommend that you use either of them instead of using `-password`. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-password-secret` |  Optional. If you're using [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the SAP HANA database user's password, then specify the corresponding secret name. In Secret Manager, make sure that the **Secret value** , which is the password, contains at least 8 characters and includes at least one uppercase letter, one lowercase letter, and a number. **Important:** The secret must exist in the same Google Cloud project that you specify for the `-project` argument.For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-hdbuserstore-key` |  To securely connect to an SAP HANA system, specify a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key that you've created for that system.  To use an `hdbuserstore` key for authentication, ensure the following:

  * The SAP tools `hdbsql` and `hdbuserstore` are installed on the compute instance hosting the agent.
  * The `hdbuserstore` key corresponds to one specific SAP HANA instance. You can't use keys that contain hostnames of multiple SAP HANA instances.
  * The `SIDadm` user can query the SAP HANA database using this key. Here `SID` refers to the value that you've specified for the `sid` parameter. You can verify this by running the following command as the `SIDadm` user: 
        
        hdbsql -U HDB_USERSTORE_KEY "SELECT * FROM DUMMY"


This configuration parameter is supported from version 3.3 of the agent. If you specify `-hdbuserstore-key`, then you can skip specifying the `-host`, `-port`, and `-hana-db-user` arguments. For SAP HANA authentication, the agent uses the following order of preference: if specified, the `-hdbuserstore-key` argument is preferred over the `-password` argument, which is preferred over the `-password-secret` argument. We recommend that you specify only one authentication option while running the `hanadiskbackup` command.  
`-host` | Optional. Specify the IP address of the Compute Engine instance that hosts your SAP HANA system. The default value is `localhost`.  
`-project` | Optional. Specify the ID of the Google Cloud project where your SAP HANA instance is running.  
`-abandon-prepared` | Optional. Specifies whether to ignore any existing snapshot based backup or not. The default value is `false`.  
`-snapshot-name` |  Optional. Specify the name for the disk snapshot that you're creating. This argument is applicable only when your `/hana/data` volume is hosted on one disk. By default, the snapshot is named by using the following format: `PREFIX-TIMESTAMP_IN_UTC-SOURCE_DISK_NAME`. From version 3.11 of the agent, while creating backup, you can specify a prefix for the snapshot name by specifying the `-snapshot-prefix` argument. If you don't specify this argument, then the prefix defaults to `snapshot`.  
`-snapshot-prefix` |  Optional. Specify the prefix that you want to set for the names of the snapshots or group snapshots. This argument is supported from version 3.11 of the agent.  
`-snapshot-description` | Optional. Specify a description for the disk snapshot. This argument is applicable only when your `/hana/data` volume is hosted on one disk.  
`-snapshot-type` |  Optional. Specify the type of snapshots that you want to create for the disks hosting your `/hana/data` volume. This argument is applicable only when your `/hana/data` volume is hosted on more than one disk. By default, the agent creates standard snapshots. Supported values for this argument: `STANDARD`, `ARCHIVE`. For information about these snapshot types, see [ About archive and standard disk snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots#incremental-snapshots). This argument is supported from version 3.6 of the agent.  
`-group-snapshot-name` |  Optional. Specify the snapshot group name for the snapshots of the disks hosting your `/hana/data` volume. This argument is supported from version 3.6 of the agent. By default, the snapshot group name is set by using the following format: `PREFIX-TIMESTAMP_IN_UTCCONSISTENCY_GROUP_NAME`. Here, `CONSISTENCY_GROUP_NAME` is the name of the disk consistency group that you created in the section Create a disk consistency group. From version 3.11 of the agent, you can specify a prefix for the snapshot name. If you don't specify the `-snapshot-prefix` while creating the backup, then the prefix defaults to `group-snapshot`.  
`-labels` | Optional. Specify one or more label-value pairs that you want to associate with the disk snapshots you're creating. For example: `-labels="label1=value1,label2=value2"`.  
`-source-disks` | Specify the names of the disks hosting the `/hana/data` volume in your scale-out deployment. Use a comma to separate the disk names. For example: `-source-disks="disk-name-1, disk-name-2"`.   
`-storage-location` | Optional. Specify the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your disk snapshot.  
`-freeze-file-system` |  Optional. Specifies whether or not the agent is to freeze the file system of your SAP HANA database. The default value is `false`. This argument is supported from version 3.2 of the agent.  
`-send-metrics-to-monitoring` | Optional. Specifies whether or not the execution status of the snapshot creation is sent to Cloud Monitoring. The default value is `TRUE`.  
`-loglevel` | Optional. Specify the logging level for the snapshot creation operation. The default logging level is `info`. The available log levels are: `debug`, `info`, `warn`, and `error`.  
`-confirm-data-snapshot-after-create` |  Optional. If you want to confirm the snapshot creation to SAP HANA immediately after the snapshot is created but without confirming that it has been uploaded to the Cloud Storage bucket specified for the `-storage-location` argument, then specify the value `TRUE`. The default value is `FALSE`, which causes the agent to confirm snapshot creation after the completion of both `CREATE` and `UPLOAD` operations. This argument is supported from version 3.4 of the agent.  
`-hana-query-timeout` |  Optional. Specify the timeout for SAP HANA database queries in seconds. The default value is `600` (10 minutes). This argument is supported from version 3.15-952132455 of the agent.  
  
### Verify the disk snapshots

You can verify that the disk snapshots are created by using the following options:

  * In the Google Cloud console, go to the Compute Engine **Snapshots** page, and then filter the entries by using the disk name. If your `/hana/data` volume is hosted on one disk, then you can also filter by using the snapshot name. If your `/hana/data` volume is hosted on more than one disk, then you can also filter by using the snapshot group's name.

[Go to Snapshots](https://console.cloud.google.com/compute/snapshots)

  * Alternatively, you can view the disk snapshot details in the following log file of the agent:
        
        /var/log/google-cloud-sap-agent/hanadiskbackup.log




### Review the SAP HANA backup catalog

In addition to creating the disk snapshot based backup, the `hanadiskbackup` command creates an entry for it in your SAP HANA backup catalog. The following is an example SQL query to view the snapshot based backup entries in your SAP HANA backup catalog:
    
    
    SELECT BACKUP_ID, STATE_NAME, COMMENT FROM M_BACKUP_CATALOG WHERE ENTRY_TYPE_NAME = 'data snapshot'

The output is similar to the following example:
    
    
    BACKUP_ID,STATE_NAME,COMMENT
    BACKUP_ID,"successful","SNAPSHOT_IDENTIFIER"
    

This output includes the following values:

  * `BACKUP_ID`: the backup ID assigned to the disk snapshot based backup in your SAP HANA backup catalog
  * `SNAPSHOT_IDENTIFIER`: 
    * For a `/hana/data` volume on one disk, the value of this identifier is determined by the usage of the `-snapshot-name` argument with the `hanadiskbackup` command. If you didn't specify this argument, then the argument's default value is set, which is: `snapshot-SOURCE_DISK_NAME-YYYYMMDD-HHMMSS`.
    * If your `/hana/` volume is hosted on more than one disk, then the value of this identifier is determined by the usage of the `-group-snapshot-name` argument with the `hanadiskbackup` command. If you didn't specify this argument, then the argument's default value is set, which is `CONSISTENCY_GROUP_NAME-YYYYMMDD-HHMMMSS`.
  * `SOURCE_DISK_NAME`: this value is determined by the usage of the `-source-disk` argument with the `hanadiskbackup` command.
  * `CONSISTENCY_GROUP_NAME`: this value is determined by the usage of the `-group-snapshot-name` argument with the `hanadiskbackup` command
  * `YYYYMMDD-HHMMMSS`: the date and time when the snapshot was created.



## Recover the database by using a disk snapshot based backup

To recover your SAP HANA database by using the disk snapshot feature of Google Cloud's Agent for SAP, see the instructions for your scenario:

  * Recover the database for a scale-up system
  * Recover the database for a scale-up HA system
  * Recover the database for a scale-up DR deployment
  * Recover the database for a scale-out system
  * Perform a system copy or system refresh



When performing any of these recovery operations, you can specify a target Cloud KMS key to encrypt the newly restored disks. The agent supports Customer-Managed Encryption Keys (CMEK) for both single-disk and striped multi-disk SAP HANA systems. You can restore disks from Google Default Encryption (GMEK) to CMEK, or between different CMEK keys, including Cloud KMS keys that reside in different Google Cloud projects or completely different Google Cloud organizations.

**Note:** Customer-Supplied Encryption Keys (CSEK) are supported only for single-disk restorations (`-source-snapshot`). CSEK is not supported for multi-disk restorations (`-group-snapshot-name`). CSEK and CMEK are mutually exclusive for the target disk.

### Recover the database for a scale-up system

To recover the database for an SAP HANA scale-up system deployed on Google Cloud, complete the following steps:

  1. Recover the disk hosting the `/hana/data` volume by running the agent's `hanadiskrestore` command:

     * If your `/hana/data` volume is hosted on one disk, then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
           -project=SOURCE_PROJECT_ID \
           -sid=SID \
           -source-snapshot=SOURCE_SNAPSHOT_NAME \
           [-new-disk-name=NEW_DISK_NAME \
           -new-disk-type=NEW_DISK_TYPE \
           -target-kms-key=TARGET_KMS_KEY \
           -target-kms-keyring=TARGET_KMS_KEYRING \
           -target-kms-location=TARGET_KMS_LOCATION \
           -target-kms-project=TARGET_KMS_PROJECT_ID \
           -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

     * If your `/hana/data` volume is hosted on more than one disk, then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
           -project=SOURCE_PROJECT_ID \
           -sid=SID \
           -group-snapshot-name=SOURCE_SNAPSHOT_GROUP_NAME \
           [-source-disks=COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY \
           -new-disk-type=NEW_DISK_TYPE \
           -new-disk-names=COMMA_SEPARATED_NAMES_FOR_NEW_DISKS \
           -new-disk-suffix=NEW_DISK_SUFFIX \
           -target-kms-key=TARGET_KMS_KEY \
           -target-kms-keyring=TARGET_KMS_KEYRING \
           -target-kms-location=TARGET_KMS_LOCATION \
           -target-kms-project=TARGET_KMS_PROJECT_ID \
           -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

Replace the following: 
     * `SOURCE_PROJECT_ID`: the ID of the Google Cloud project in which the disk snapshot exists
     * `SID`: the SAP system identifier (SID) of your SAP HANA system 
     * `SOURCE_SNAPSHOT_NAME`: if your `/hana/data` volume is hosted on one disk, then specify the name of the disk snapshot using which you're creating the new disk
     * `SOURCE_SNAPSHOT_GROUP_NAME`: if your `/hana/data` volume is hosted on more than one disk, then specify the snapshot group name using which you're creating the new disks
     * `NEW_DISK_NAME`: the name that you want to set for the new disk. For more information, see the description of `-new-disk-name` in Supported arguments for disk restoration. 
     * `NEW_DISK_TYPE`: the type of disk that you want to create. For more information, see the description of `-new-disk-type` in Supported arguments for disk restoration.
     * `COMMA_SEPARATED_NAMES_FOR_NEW_DISKS`: a comma-separated list of names that you want to set for the disks that the agent creates
     * `NEW_DISK_SUFFIX`: the suffix that you want to add to the names of the new disks
     * `COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY`: a comma-separated list of disk names that you want to restore by using the snapshot based backup
     * `TARGET_KMS_KEY`: the name of the Cloud KMS key to use for encrypting the restored disk(s)
     * `TARGET_KMS_KEYRING`: the name of the Cloud KMS key ring containing the target KMS key
     * `TARGET_KMS_LOCATION`: the location of the Cloud KMS key ring
     * `TARGET_KMS_PROJECT_ID`: the ID of the Google Cloud project in which the Cloud KMS key resides
     * `TARGET_KMS_SERVICE_ACCOUNT`: the service account to use for accessing the Cloud KMS key
**Note:** If you're creating a script that includes the `hanadiskrestore` command, and if your Compute Engine instances are running RHEL for SAP images, then use the following command instead: 
    
    sudo su - -c "/usr/bin/google_cloud_sap_agent hanadiskrestore"

For more information about the arguments that you can use with the `hanadiskrestore` command, see Supported arguments for disk restoration. 

  2. Recover your SAP HANA database using the required option:

### Recover to snapshot time

To recover you SAP HANA database by restoring it to the time the disk snapshot was created, follow these steps: 

     1. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     2. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command="RECOVER DATA USING SNAPSHOT CLEAR LOG;"

     3. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     4. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATA FOR TENANT_SID USING SNAPSHOT CLEAR LOG

Replace `TENANT_SID` with the SID of the tenant database.

### Recover to a specific point in time

**Note:** The database timestamp is interpreted as UTC time. For more information, see the SAP documentation [RECOVER DATABASE Statement (Backup and Recovery)](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/c4205f73bb571014ba46d209981bc1f5.html?version=2.0.00#example%3A). 

To recover you SAP HANA database by restoring it to a specific point in time, follow these steps: 

     1. Verify that you have created a backup for the `/hana/log` volume in Cloud Storage by using the _Backint_ feature of Google Cloud's Agent for SAP. For more information about this feature, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). 
     2. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     3. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command "RECOVER DATABASE UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' CLEAR LOG USING SNAPSHOT"

     4. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     5. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATABASE FOR TENANT_SID UNTIL TIMESTAMP '2099-12-31 12:00:00' CLEAR LOG USING SNAPSHOT

Replace `TENANT_SID` with the SID of the tenant database.




### Recover the database for a scale-up HA system

To recover the database for an SAP HANA scale-up system deployed in a high-availability (HA) cluster on Google Cloud, complete the following steps:

  1. Verify that you have a snapshot of the disk hosting the `/hana/data` volume in your primary SAP HANA node.

  2. As the root user, put the HA cluster in maintenance mode. If you're using Pacemaker, then run the following command:

###  RHEL 
         
         pcs property set maintenance-mode=true

###  SLES 
         
         crm configure property maintenance-mode=true

  3. Stop your SAP HANA database instances by running the following command on both the primary and standby nodes of your HA cluster:
         
         HDB stop

  4. Switch to the primary node of your SAP HANA HA system.

  5. Recover the disk hosting the `/hana/data` volume by running the agent's `hanadiskrestore` command:

     * If your `/hana/data` volume is hosted on one disk, then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
           -project=SOURCE_PROJECT_ID \
           -sid=SID \
           -source-snapshot=SOURCE_SNAPSHOT_NAME \
           [-new-disk-name=NEW_DISK_NAME \
           -new-disk-type=NEW_DISK_TYPE \
           -target-kms-key=TARGET_KMS_KEY \
           -target-kms-keyring=TARGET_KMS_KEYRING \
           -target-kms-location=TARGET_KMS_LOCATION \
           -target-kms-project=TARGET_KMS_PROJECT_ID \
           -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

     * If your `/hana/data` volume is hosted on more than one disk, then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
           -project=SOURCE_PROJECT_ID \
           -sid=SID \
           -group-snapshot-name=SOURCE_SNAPSHOT_GROUP_NAME \
           [-source-disks=COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY \
           -new-disk-type=NEW_DISK_TYPE \
           -new-disk-names=COMMA_SEPARATED_NAMES_FOR_NEW_DISKS \
           -new-disk-suffix=NEW_DISK_SUFFIX \
           -target-kms-key=TARGET_KMS_KEY \
           -target-kms-keyring=TARGET_KMS_KEYRING \
           -target-kms-location=TARGET_KMS_LOCATION \
           -target-kms-project=TARGET_KMS_PROJECT_ID \
           -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

Replace the following: 
     * `SOURCE_PROJECT_ID`: the ID of the Google Cloud project in which the disk snapshot exists
     * `SID`: the SAP system identifier (SID) of your SAP HANA system 
     * `SOURCE_SNAPSHOT_NAME`: if your `/hana/data` volume is hosted on one disk, then specify the name of the disk snapshot using which you're creating the new disk
     * `SOURCE_SNAPSHOT_GROUP_NAME`: if your `/hana/data` volume is hosted on more than one disk, then specify the snapshot group name using which you're creating the new disks
     * `NEW_DISK_NAME`: the name that you want to set for the new disk. For more information, see the description of `-new-disk-name` in Supported arguments for disk restoration. 
     * `NEW_DISK_TYPE`: the type of disk that you want to create. For more information, see the description of `-new-disk-type` in Supported arguments for disk restoration.
     * `COMMA_SEPARATED_NAMES_FOR_NEW_DISKS`: a comma-separated list of names that you want to set for the disks that the agent creates
     * `NEW_DISK_SUFFIX`: the suffix that you want to add to the names of the new disks
     * `COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY`: a comma-separated list of disk names that you want to restore by using the snapshot based backup
     * `TARGET_KMS_KEY`: the name of the Cloud KMS key to use for encrypting the restored disk(s)
     * `TARGET_KMS_KEYRING`: the name of the Cloud KMS key ring containing the target KMS key
     * `TARGET_KMS_LOCATION`: the location of the Cloud KMS key ring
     * `TARGET_KMS_PROJECT_ID`: the ID of the Google Cloud project in which the Cloud KMS key resides
     * `TARGET_KMS_SERVICE_ACCOUNT`: the service account to use for accessing the Cloud KMS key
**Note:** If you're creating a script that includes the `hanadiskrestore` command, and if your Compute Engine instances are running RHEL for SAP images, then use the following command instead: 
    
    sudo su - -c "/usr/bin/google_cloud_sap_agent hanadiskrestore"

For more information about the arguments that you can use with the `hanadiskrestore` command, see Supported arguments for disk restoration. 

  6. Unregister the secondary node of your SAP HANA HA system:
         
         hdbnsutil -sr_unregister

  7. On the primary node of your SAP HANA HA system, disable the SAP HANA system replication:
         
         hdbnsutil -sr_disable

  8. On the primary node, recover your SAP HANA database using the required option:

### Recover to snapshot time

To recover you SAP HANA database by restoring it to the time the disk snapshot was created, follow these steps: 

     1. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     2. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command="RECOVER DATA USING SNAPSHOT CLEAR LOG;"

     3. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     4. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATA FOR TENANT_SID USING SNAPSHOT CLEAR LOG

Replace `TENANT_SID` with the SID of the tenant database.

### Recover to a specific point in time

**Note:** The database timestamp is interpreted as UTC time. For more information, see the SAP documentation [RECOVER DATABASE Statement (Backup and Recovery)](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/c4205f73bb571014ba46d209981bc1f5.html?version=2.0.00#example%3A). 

To recover you SAP HANA database by restoring it to a specific point in time, follow these steps: 

     1. Verify that you have created a backup for the `/hana/log` volume in Cloud Storage by using the _Backint_ feature of Google Cloud's Agent for SAP. For more information about this feature, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). 
     2. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     3. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command "RECOVER DATABASE UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' CLEAR LOG USING SNAPSHOT"

     4. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     5. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATABASE FOR TENANT_SID UNTIL TIMESTAMP '2099-12-31 12:00:00' CLEAR LOG USING SNAPSHOT

Replace `TENANT_SID` with the SID of the tenant database.

  9. On the primary node, enable the SAP HANA system replication:
         
         hdbnsutil -sr_enable --name=PRIMARY_SITE_NAME

  10. Re-register the standby node with the primary node:
         
         hdbnsutil -sr_register
            --name=SECONDARY_SITE_NAME
            --remoteHost=PRIMARY_HOST_NAME
            --remoteInstance=INSTANCE_NUMBER
            --replicationMode=sync
            --operationMode=logreplay

  11. Verify that database in the standby node is fully synchronized with the database in the primary node.

  12. As the root user, exit the HA cluster maintenance mode. If you're using Pacemaker, then run the following command:

###  RHEL 
         
         pcs property set maintenance-mode=false

###  SLES 
         
         crm configure property maintenance-mode=false




### Recover the database for a scale-up DR deployment

To recover the database for an SAP HANA scale-up system that is deployed with a disaster recovery solution on Google Cloud, complete the following steps:

  1. Stop your SAP HANA databases by running the following command on both the primary and standby instances of your DR deployment:
         
         HDB stop

  2. Switch to the primary instance of your SAP HANA DR deployment.

  3. Recover the disk hosting the `/hana/data` volume by running the agent's `hanadiskrestore` command:

     * If your `/hana/data` volume is hosted on one disk, then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
           -project=SOURCE_PROJECT_ID \
           -sid=SID \
           -source-snapshot=SOURCE_SNAPSHOT_NAME \
           [-new-disk-name=NEW_DISK_NAME \
           -new-disk-type=NEW_DISK_TYPE \
           -target-kms-key=TARGET_KMS_KEY \
           -target-kms-keyring=TARGET_KMS_KEYRING \
           -target-kms-location=TARGET_KMS_LOCATION \
           -target-kms-project=TARGET_KMS_PROJECT_ID \
           -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

     * If your `/hana/data` volume is hosted on more than one disk, then run the following command:
           
           sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
           -project=SOURCE_PROJECT_ID \
           -sid=SID \
           -group-snapshot-name=SOURCE_SNAPSHOT_GROUP_NAME \
           [-source-disks=COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY \
           -new-disk-type=NEW_DISK_TYPE \
           -new-disk-names=COMMA_SEPARATED_NAMES_FOR_NEW_DISKS \
           -new-disk-suffix=NEW_DISK_SUFFIX \
           -target-kms-key=TARGET_KMS_KEY \
           -target-kms-keyring=TARGET_KMS_KEYRING \
           -target-kms-location=TARGET_KMS_LOCATION \
           -target-kms-project=TARGET_KMS_PROJECT_ID \
           -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

Replace the following: 
     * `SOURCE_PROJECT_ID`: the ID of the Google Cloud project in which the disk snapshot exists
     * `SID`: the SAP system identifier (SID) of your SAP HANA system 
     * `SOURCE_SNAPSHOT_NAME`: if your `/hana/data` volume is hosted on one disk, then specify the name of the disk snapshot using which you're creating the new disk
     * `SOURCE_SNAPSHOT_GROUP_NAME`: if your `/hana/data` volume is hosted on more than one disk, then specify the snapshot group name using which you're creating the new disks
     * `NEW_DISK_NAME`: the name that you want to set for the new disk. For more information, see the description of `-new-disk-name` in Supported arguments for disk restoration. 
     * `NEW_DISK_TYPE`: the type of disk that you want to create. For more information, see the description of `-new-disk-type` in Supported arguments for disk restoration.
     * `COMMA_SEPARATED_NAMES_FOR_NEW_DISKS`: a comma-separated list of names that you want to set for the disks that the agent creates
     * `NEW_DISK_SUFFIX`: the suffix that you want to add to the names of the new disks
     * `COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY`: a comma-separated list of disk names that you want to restore by using the snapshot based backup
     * `TARGET_KMS_KEY`: the name of the Cloud KMS key to use for encrypting the restored disk(s)
     * `TARGET_KMS_KEYRING`: the name of the Cloud KMS key ring containing the target KMS key
     * `TARGET_KMS_LOCATION`: the location of the Cloud KMS key ring
     * `TARGET_KMS_PROJECT_ID`: the ID of the Google Cloud project in which the Cloud KMS key resides
     * `TARGET_KMS_SERVICE_ACCOUNT`: the service account to use for accessing the Cloud KMS key
**Note:** If you're creating a script that includes the `hanadiskrestore` command, and if your Compute Engine instances are running RHEL for SAP images, then use the following command instead: 
    
    sudo su - -c "/usr/bin/google_cloud_sap_agent hanadiskrestore"

For more information about the arguments that you can use with the `hanadiskrestore` command, see Supported arguments for disk restoration. 

  4. On the primary instance, disable the SAP HANA system replication:
         
         hdbnsutil -sr_disable

  5. On the DR instance, recover your SAP HANA database by using the required option:

### Recover to snapshot time

To recover you SAP HANA database by restoring it to the time the disk snapshot was created, follow these steps: 

     1. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     2. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command="RECOVER DATA USING SNAPSHOT CLEAR LOG;"

     3. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     4. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATA FOR TENANT_SID USING SNAPSHOT CLEAR LOG

Replace `TENANT_SID` with the SID of the tenant database.

### Recover to a specific point in time

**Note:** The database timestamp is interpreted as UTC time. For more information, see the SAP documentation [RECOVER DATABASE Statement (Backup and Recovery)](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/c4205f73bb571014ba46d209981bc1f5.html?version=2.0.00#example%3A). 

To recover you SAP HANA database by restoring it to a specific point in time, follow these steps: 

     1. Verify that you have created a backup for the `/hana/log` volume in Cloud Storage by using the _Backint_ feature of Google Cloud's Agent for SAP. For more information about this feature, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). 
     2. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     3. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command "RECOVER DATABASE UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' CLEAR LOG USING SNAPSHOT"

     4. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     5. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATABASE FOR TENANT_SID UNTIL TIMESTAMP '2099-12-31 12:00:00' CLEAR LOG USING SNAPSHOT

Replace `TENANT_SID` with the SID of the tenant database.

  6. On the primary instance, enable the SAP HANA system replication:
         
         hdbnsutil -sr_enable --name=PRIMARY_SITE_NAME

  7. Register the standby instance with the primary instance:
         
         hdbnsutil -sr_register
            --name=SECONDARY_SITE_NAME
            --remoteHost=PRIMARY_HOST_NAME
            --remoteInstance=INSTANCE_NUMBER
            --replicationMode=sync
            --operationMode=logreplay

  8. Verify that database in the standby instance is fully synchronized with the database in the primary instance.




### Recover the database for a scale-out system

To recover the database for an SAP HANA scale-out system deployed on Google Cloud without the host auto-failover solution, complete the following steps:

  1. On each node in your scale-out deployment, stop SAP HANA:
         
         HDB STOP
         

  2. On each node, as the root user, unmount the `/hana/data` volume.

For information about how to do this, see the SAP documentation for your SAP HANA version.

  3. Recover the disks hosting the `/hana/data` volume by running the agent's `hanadiskrestore` command:
         
         sudo /usr/bin/google_cloud_sap_agent hanadiskrestore \
             -project=SOURCE_PROJECT_ID \
             -sid=SID \
             -group-snapshot-name=SOURCE_SNAPSHOT_GROUP_NAME \
             -source-disks=COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY \
             [-new-disk-type=NEW_DISK_TYPE \
             -new-disk-names=COMMA_SEPARATED_NAMES_FOR_NEW_DISKS \
             -new-disk-suffix=NEW_DISK_SUFFIX \
             -target-kms-key=TARGET_KMS_KEY \
             -target-kms-keyring=TARGET_KMS_KEYRING \
             -target-kms-location=TARGET_KMS_LOCATION \
             -target-kms-project=TARGET_KMS_PROJECT_ID \
             -target-kms-service-account=TARGET_KMS_SERVICE_ACCOUNT]

Replace the following: 
     * `SOURCE_PROJECT_ID`: the ID of the Google Cloud project in which the disk snapshot exists
     * `SID`: the SAP system identifier (SID) of your SAP HANA system 
     * `SOURCE_SNAPSHOT_GROUP_NAME`: the name of the snapshot group that you want to use to create the new disks 
     * `NEW_DISK_TYPE`: the type of disk that you want to create. For more information, see the description of `-new-disk-type` in Supported arguments for disk restoration.
     * `COMMA_SEPARATED_NAMES_FOR_NEW_DISKS`: a comma-separated list of names that you want to set for the disks that the agent creates
     * `NEW_DISK_SUFFIX`: the suffix that you want to add to the names of the new disks
     * `COMMA_SEPARATED_DISK_NAMES_FOR_RECOVERY`: a comma-separated list of disk names that you want to restore by using the snapshot based backup
     * `TARGET_KMS_KEY`: the name of the Cloud KMS key to use for encrypting the restored disk(s)
     * `TARGET_KMS_KEYRING`: the name of the Cloud KMS key ring containing the target KMS key
     * `TARGET_KMS_LOCATION`: the location of the Cloud KMS key ring
     * `TARGET_KMS_PROJECT_ID`: the ID of the Google Cloud project in which the Cloud KMS key resides
     * `TARGET_KMS_SERVICE_ACCOUNT`: the service account to use for accessing the Cloud KMS key
**Note:** If you're creating a script that includes the `hanadiskrestore` command, and if your Compute Engine instances are running RHEL for SAP images, then use the following command instead: 
    
    sudo su - -c "/usr/bin/google_cloud_sap_agent hanadiskrestore"

For more information about the arguments that you can use with the `hanadiskrestore` command, see Supported arguments for disk restoration. 

  4. On each worker node, as the root user, rescan the volume groups:
         
         /sbin/dmsetup remove_all
         /sbin/vgscan -v --mknodes
         /sbin/vgchange -ay
         /sbin/lvscan
         mount -av
         

  5. On each worker node, as the root user, recover the SAP HANA database by using the required option:

### Recover to snapshot time

To recover you SAP HANA database by restoring it to the time the disk snapshot was created, follow these steps: 

     1. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     2. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command="RECOVER DATA USING SNAPSHOT CLEAR LOG;"

     3. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     4. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATA FOR TENANT_SID USING SNAPSHOT CLEAR LOG

Replace `TENANT_SID` with the SID of the tenant database.

### Recover to a specific point in time

**Note:** The database timestamp is interpreted as UTC time. For more information, see the SAP documentation [RECOVER DATABASE Statement (Backup and Recovery)](https://help.sap.com/docs/SAP_HANA_PLATFORM/4fe29514fd584807ac9f2a04f6754767/c4205f73bb571014ba46d209981bc1f5.html?version=2.0.00#example%3A). 

To recover you SAP HANA database by restoring it to a specific point in time, follow these steps: 

     1. Verify that you have created a backup for the `/hana/log` volume in Cloud Storage by using the _Backint_ feature of Google Cloud's Agent for SAP. For more information about this feature, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery). 
     2. Switch to the `SIDadm` user: 
            
            su - SID_LCadm

Replace `SID_LC` with the SID of your SAP HANA system. Use lowercase for any letters.

     3. Recover the system database by running the following command: 
            
            HDBSettings.sh recoverSys.py --command "RECOVER DATABASE UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' CLEAR LOG USING SNAPSHOT"

     4. Connect to the system database. For example, you can run the following command: 
            
            hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

        * `SYSTEM_DB_PASSWORD`: your system database password
        * `INSTANCE_NUMBER`: your SAP HANA instance number
     5. Recover the tenant databases by running the following command for each tenant database: 
            
            RECOVER DATABASE FOR TENANT_SID UNTIL TIMESTAMP '2099-12-31 12:00:00' CLEAR LOG USING SNAPSHOT

Replace `TENANT_SID` with the SID of the tenant database.

  6. On each worker node, start the SAP HANA database.

  7. Repeat the steps 3-5 for the master node in your scale-out deployment.




### Supported arguments for disk restoration

The following table describes the arguments supported by the agent's `hanadiskrestore` command:

Argument | Description  
---|---  
`-sid` | Specify the SAP system identifier (SID) of your SAP HANA system.  
`-data-disk-name` | Optional. Specify the name of the source disk that hosts the `/hana/data` volume. From version 3.4, the arguments `-data-disk-name` and `-data-disk-zone` are optional for use with the `hanadiskrestore` command. This is because the agent can auto-detect the disk that hosts your `/hana/data` volume. However, if you specify these arguments, then they override the agent's auto-detection.  
`-source-disks` |  Specify the names of the disks hosting the `/hana/data` volume in deployment, which you're recovering. Use a comma to separate the disk names. For example: `-source-disks="disk-name-1, disk-name-2"`.  This argument is supported from version 3.7 of Google Cloud's Agent for SAP. This argument is required for recovering scale-out systems. It's optional for scale-up systems that use striped disks to host the `/hana/data` volume. It's not supported for scale-up systems that use a single disk to host the `/hana/data` volume.   
`-data-disk-zone` | Optional. Specify the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the source disk that hosts the `/hana/data` volume, is deployed. From version 3.4, the arguments `-data-disk-name` and `-data-disk-zone` are optional for use with the `hanadiskrestore` command. This is because the agent can auto-detect the disk that hosts your `/hana/data` volume. However, if you specify these arguments, then they override the agent's auto-detection.  
`-source-snapshot` | If your `/hana/data` volume is hosted on one disk, then specify the name of the disk snapshot using which you want to perform recovery.  
`-new-disk-name` | Specify the name that you want to set for the new disk. This argument is not applicable if your `/hana/data` volume is hosted on more than one disk.  
`-group-snapshot-name` |  Specify the snapshot group name using which you want to perform recovery. This argument is supported from version 3.6 of the agent. This argument is not supported for SAP HANA scale-up systems that use a single disk to host the `/hana/data` volume.  
`-project` | Optional. Specify the ID of the Google Cloud project in which the source disk snapshot exists. By default, the snapshot is created in the Google Cloud project where your SAP HANA system is running.  
`-csek-key-file` |  Optional. If you encrypted the source disk snapshot by using the `-source-disk-key-file` argument with the `hanadiskbackup` command, then specify the absolute path to the JSON file of the [RSA-wrapped](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#rsa-encryption) customer-supplied encryption key that corresponds to the source disk snapshot. The following is an example key file: 
    
    
    [
      {
        "uri": "https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/snapshots/SNAPSHOT_NAME",
        "key": "ieCx/NcW06PcT7Ep1X6LUTc/hLvUDYyzSZPPVCVPTVEohpeHASqC8uw5TzyO9U+Fka9JFHz0mBibXUInrC/jEk014kCK/NPjYgEMOyssZ4ZINPKxlUh2zn1bV+MCaTICrdmuSBTWlUUiFoDD6PYznLwh8ZNdaheCeZ8ewEXgFQ8V+sDroLaN3Xs3MDTXQEMMoNUXMCZEIpg9Vtp9x2oeQ5lAbtt7bYAAHf5l+gJWw3sUfs0/Glw5fpdjT8Uggrr+RMZezGrltJEF293rvTIjWOEB3z5OHyHwQkvdrPDFcTqsLfh+8Hr8g+mf+7zVPEC8nEbqpdl3GPv3A7AwpFp7MA==",
        "key-type": "rsa-encrypted"
      }
    ]

This argument is supported from version 3.2 of the agent. This argument is not supported for multi-disk restore operations (`-group-snapshot-name`). It is only compatible with single disk restore operations (`-source-snapshot`).  
`-new-disk-type` |  Optional. Specify the type of Persistent Disk or Hyperdisk that you want to create. By default, the new disks are of the same type of as the source disks. Make sure that you specify an SSD-based disk type that is certified by SAP for use with SAP HANA. For more information, see [Supported disk types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#supported_disk_types_2).  
`-new-disk-prefix` |  Optional. Specify the prefix that you want to add to the names of the new disks. This argument is supported from version 3.7 to 3.10 of the agent. This argument is not supported while recovering SAP HANA scale-up systems that you use a single disk to host the `/hana/data` volume.  
`-new-disk-suffix` |  Optional. Specify the suffix that you want to set for the names of the new disks. This argument is supported from version 3.11 of the agent. This argument is not supported while recovering SAP HANA scale-up systems that you use a single disk to host the `/hana/data` volume.  
`-new-disk-names` |  Optional. Specify a comma-separated list of names that you want the agent to set for the new disks. This argument is supported from version 3.12 of the agent. This argument is not supported while recovering SAP HANA scale-up systems that you use a single disk to host the `/hana/data` volume.  
`-target-kms-key` |  Optional. Specify the name of the Cloud KMS key to use for encrypting the restored disk(s). If you specify this argument, you must also specify the `-target-kms-keyring` argument. This argument is supported from version 3.14 of the agent.  
`-target-kms-keyring` |  Optional. Specify the name of the Cloud KMS key ring containing the target KMS key specified by `-target-kms-key`. If you specify this argument, you must also specify the `-target-kms-key` argument. This argument is supported from version 3.14 of the agent.  
`-target-kms-location` |  Optional. Specify the location of the Cloud KMS key ring. You can specify a regional, multi-regional (such as `us`, `eur4`, `nam4`), or `global` location. If you don't specify this argument, the location defaults to the region of the disk zone. This argument is supported from version 3.14 of the agent.  
`-target-kms-project` |  Optional. Specify the ID of the Google Cloud project in which the Cloud KMS key resides. If you don't specify this argument, the project ID defaults to the current project. This argument is supported from version 3.14 of the agent.  
`-target-kms-service-account` |  Optional. Specify a service account to use for accessing the Cloud KMS key. This service account must have encrypter/decrypter permissions on the key (such as the [`roles/cloudkms.cryptoKeyEncrypterDecrypter`](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) role). For more information, see [Customer-managed encryption keys required roles](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#required-roles). If you don't specify this argument, the service account defaults to the Compute Engine service agent (`service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`). This argument is supported from version 3.14 of the agent.  
`-hana-sidadm` | Optional. Specify the `SIDadm` \- the operating system user of your SAP HANA system.  
`-force-stop-hana` | Optional. If you want to forcefully stop SAP HANA before the initiating the recovery operation, then specify this argument and set its value to `true`. The default value is `false`.  
`-provisioned-iops` | Optional. If you're creating a [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volume, then specify the IOPS (input/output operations per second) that it must handle.  
`-provisioned-throughput` | Optional. If you're creating a [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) volume, then specify the throughput it must support.  
`-labels-on-detached-disk` | Optional. If you're creating a new disk to host the recovered `/hana/data` directory, then use this argument to specify label-value pairs that you want to associate with the detached disk. Use a comma to separate the labels. For example: `-labels-on-detached-disk="label1=value1,label2=value2"`. This argument is supported from version 3.4 of the agent.  
`-send-metrics-to-monitoring` | Optional. Specifies whether or not the duration of the snapshot restore is sent to Cloud Monitoring. The default value is `TRUE`. This argument is supported from version 3.4 of the agent.  
`-disk-size-gb` |  Optional. Specify the size, in GB, for the new disk. By default, the new disk is of the same size as the existing disk. The new disk must not be smaller in size than the existing disk.  
`-loglevel` | Optional. Specify the logging level for all the actions performed by the `hanadiskrestore` command. The default logging level is `info`. The available log levels are: `debug`, `info`, `warn`, and `error`.  
  
### Perform a system copy or system refresh

To use a disk snapshot based backup of an SAP HANA system for recovering another SAP HANA system, complete the following steps:

  1. In the source system, create a snapshot based backup by running the agent's `hanadiskbackup` command. For instructions, see Create a disk snapshot based backup.

  2. In the target system, recover the disk hosting the `/hana/data` volume by running the agent's `hanadiskrestore` command.

If the SIDs of the source and target systems are different, then rename the `/hana/data/SID` directory in the target system so that it matches the required SID of target system:
         
         mv /hana/data/SOURCE_SID /hana/data/TARGET_SID

Replace the following:

     * `SOURCE_SID`: the SID of the source SAP HANA system
     * `TARGET_SID`: the SID of the target SAP HANA system
  3. If you've enabled data encryption for the source SAP HANA system, then before you perform recovery, you must import the encryption keys into the target system. If you've not enabled data encryption in your source system, then skip this step.

To import the data encryption keys into the target system, complete the following steps:

     1. In the source system, create a backup of the encryption keys of the system database:
            
            hdbnsutil -backupRootKeys FILE_NAME_SYS.rkb --type=ALL --database_name=SYSTEMDB

Replace `FILE_NAME_SYS` with the name that you want to set for the encryption key backup of the system database. Optionally, you can include the path where you want to store this file.

     2. In the source system, create a backup of the encryption keys of the tenant databases by running the following command for each tenant database:
            
            hdbnsutil -backupRootKeys FILE_NAME_TENANT.rkb --type=ALL --database_name=TENANT_DB_NAME

Replace the following:

        * `FILE_NAME_TENANT`: the name that you want to set for the encryption key backup of the tenant database. Optionally, you can include the path where you want to store this file.
        * `TENANT_DB_NAME`: the tenant database name
     3. Verify the backups:
            
            ls -ltr *.rkb

The output is similar to the following example:
            
            -rw-r----- 1 sbxadm sapsys 1440 Mar 24 21:09 sbxkeys.rkb
            -rw-r----- 1 sbxadm sapsys 1440 Mar 24 21:12 systemkeys.rkb

     4. In the target system, import the backed-up encryption keys of the system database:
            
            hdbnsutil -recoverRootKeys FILE_NAME_SYS.rkb --dbid=SYSTEM_DB_ID --password=SYSTEM_DB_PASSWORD

Replace the following:

        * `SYSTEM_DB_ID`: the system database ID
        * `SYSTEM_DB_PASSWORD`: the system database password
     5. Import the backed-up encryption keys of the tenant databases by running the following command for each tenant database:
            
            hdbnsutil -recoverRootKeys FILE_NAME_TENANT.rkb --dbid=TENANT_DB_ID --password=TENANT_DB_PASSWORD

Replace the following:

        * `TENANT_DB_ID`: the tenant database ID
        * `TENANT_DB_PASSWORD`: the tenant database password
  4. In the target system, recover the system database:
         
         HDBSettings.sh recoverSys.py --command "RECOVER DATABASE UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' CLEAR LOG USING SOURCE 'SYSTEMDB@SOURCE_SID' USING CATALOG BACKINT USING SNAPSHOT"

  5. If you want your tenant database to have the source system's SID, then you can rename it by following the instructions in the SAP HANA document [Rename a Tenant Database](https://help.sap.com/docs/SAP_HANA_COCKPIT/afa922439b204e9caf22c78b6b69e4f2/366d9e353cbc4f78b4f04c9ddb51a5ab.html).

  6. In the target system, connect to the system database. For example, you can run the following command:
         
         hdbsql -d SYSTEMDB -u system -p "SYSTEM_DB_PASSWORD" -i INSTANCE_NUMBER

Replace `INSTANCE_NUMBER` with the instance number of the SAP HANA system database.

  7. In the target system, recover the tenant databases by running the following command for each tenant database:
         
         RECOVER DATABASE FOR TARGET_SID UNTIL TIMESTAMP 'YYYY-MM-DD HH:MM:SS' CLEAR LOG USING SOURCE 'TARGET_SID@SOURCE_SID' USING CATALOG BACKINT USING SNAPSHOT

  8. In the target system, connect to the tenant databases by running the following command for each tenant database:
         
         hdbsql -d TENANT_SID -u system -p "TENANT_DB_PASSWORD" -i INSTANCE_NUMBER

Replace the following:

     * `TENANT_SID`: the tenant database SID
     * `INSTANCE_NUMBER`: the tenant database instance number
  9. Validate data consistency in the target database by completing the following steps:

     1. Stop the target system:
            
            HDB stop

     2. As the `SIDadm` user, run the `hdbpersdiag` tool:
            
            hdbpersdiag -c 'check all' -e HANA_DATA_DIRECTORY

Replace `HANA_DATA_DIRECTORY` with the SAP HANA data volume directory, for example: `/hana/data/SBX/mnt00001/hdb00001`.

  10. If the data consistency validation fails, then complete the following steps:

     1. For the target system, verify that data encryption is enabled on the system database and all tenant databases:
            
            SELECT * FROM SYS.M_ENCRYPTION_OVERVIEW

     2. If data encryption is `FALSE` for any database, then enable data encryption:
            
            ALTER SYSTEM PERSISTENCE ENCRYPTION ON;
            ALTER SYSTEM LOG ENCRYPTION ON;
            ALTER SYSTEM BACKUP ENCRYPTION ON;

     3. Revalidate data consistency by using the `hdbpersdiag` tool.




## Validate snapshot consistency

This section describes how you can validate the consistency of the data in your disk snapshots by using the `hdbpersdiag` tool from SAP. For information about other best practices recommended by Google Cloud for disk snapshot based backup and recovery operations, see [Best practices](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery#best_practices).

To validate the consistency of a snapshot, complete the following steps:

  1. Create a disk from a snapshot that you created by using the agent's `hanadiskbackup` command. Use the [`gcloud compute disks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create):
         
         gcloud compute disks create DISK_NAME \
            --size=SIZE \
            --source-snapshot=SNAPSHOT_NAME \
            --type=DISK_TYPE \
            --zone=ZONE
         

Replace the following:

     * `DISK_NAME`: the name of the temporary disk
     * `SIZE`: the size of the temporary disk
     * `SNAPSHOT_NAME`: the name of the source snapshot
     * `DISK_TYPE`: the disk type for the temporary disk
     * `ZONE`: the Compute Engine zone where you want to deploy the temporary disk
  2. Attach the disk to a Compute Engine instance other than your SAP HANA host. Use the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk):
         
         gcloud compute instances attach-disk COMPUTE_INSTANCE_NAME \
            --disk=DISK_NAME \
            --zone=ZONE
         

Replace the following:

     * `COMPUTE_INSTANCE_NAME`: the name of the compute instance where you want to deploy the disk you created
     * `DISK_NAME`: the name of the disk you created
     * `ZONE`: the Compute Engine zone where your compute instance is deployed
  3. Connect to your compute instance by using your preferred SSH method.

  4. Mount the new disk as a temporary file system:

     1. At the OS level, find the volume group that doesn't have any active logical volume:
            
            vgdisplay
            

The output is similar to the following example:
            
            --- Volume group ---
            VG Name               vg_hana_data
            System ID
            Format                lvm2
            Metadata Areas        1
            Metadata Sequence No  2
            VG Access             read/write
            VG Status             resizable
            MAX LV                0
            Cur LV                1
            Open LV               0
            Max PV                0
            Cur PV                1
            Act PV                1
            VG Size               250.00 GiB
            PE Size               4.00 MiB
            Total PE              63999
            Alloc PE / Size       63999 / 250.00 GiB
            Free  PE / Size       0 / 0
            VG UUID               Fa52zl-AROR-LH2k-aG4z-LbrB-cvTz-TZhEfR

     2. Rename the volume group using the **VG UUID**. In the preceding example it's `Fa52zl-AROR-LH2k-aG4z-LbrB-cvTz-TZhEfR`.
            
            vgrename Fa52zl-AROR-LH2k-aG4z-LbrB-cvTz-TZhEfR vg_hana_data_temp
            

     3. Activate the volume group and the logical volume:
            
            vgchange -a y vg_hana_data_temp
            lvchange -a y /dev/vg_hana_data_temp/data
            

     4. Mount the logical volume in a temporary file system, for example, `/hana/data_temp`:
            
            mkdir /hana/data_temp
            mount /dev/vg_hana_data_temp/data /hana/data_temp
            

     5. Verify that all the disks are properly mounted:
            
            lsblk
            

The output is similar to the following example:
            
            NAME                     MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
            sda                        8:0    0   30G  0 disk
            ├─sda1                     8:1    0    2M  0 part
            ├─sda2                     8:2    0   20M  0 part /boot/efi
            └─sda3                     8:3    0   30G  0 part /
            sdb                        8:16   0  350G  0 disk
            └─vg_hana_data_temp-data 254:5    0  250G  0 lvm  /hana/data_temp
            sdc                        8:32   0  104G  0 disk
            └─vg_hana_log-log        254:2    0  104G  0 lvm  /hana/log
            sdd                        8:48   0  208G  0 disk
            └─vg_hana_shared-shared  254:0    0  208G  0 lvm  /hana/shared
            sde                        8:64   0   32G  0 disk
            └─vg_hana_usrsap-usrsap  254:3    0   32G  0 lvm  /usr/sap
            sdf                        8:80   0  416G  0 disk
            └─vg_hanabackup-backup   254:4    0  416G  0 lvm  /hanabackup
            sdh                        8:112  0  250G  0 disk
            └─vg_hana_data-data      254:1    0  250G  0 lvm  /hana/data

  5. As the `SIDadm` user, run the `hdbpersdiag` tool for the data volumes that are included in the temporary file system:
         
         for directory in $(find /hana/data_temp/SID/mnt00001/hdb* -type d); do hdbpersdiag -c -e 'check all' $directory; done
         

  6. Verify the output from the `hdbpersdiag` tool.

  7. If you plan on performing this consistency check in the future, then you can leave the new volume group as it is. If not, then delete it.

  8. Detach the disk from the compute instance. Use the [`gcloud compute instances detach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk):
         
         COMPUTE_INSTANCE_NAME \
            --disk=DISK_NAME \
            --zone=ZONE
         

  9. Delete the disk. Use the [`gcloud compute disks delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/delete):
         
         gcloud compute disks delete DISK_NAME \
            --zone=ZONE
         




## Troubleshooting

While Google Cloud's Agent for SAP is designed to take care of most issues that can occur during disk snapshot based backup and recovery operations for SAP HANA, there are a few scenarios where manual intervention is required.

To troubleshoot any issue with the disk snapshot feature of Google Cloud's Agent for SAP, see [Issue with a disk snapshot based backup or recovery operation](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting#issue_with_a_disk_snapshot_based_backup_or_recovery_operation).

## Get support

If you need help resolving a problem with Google Cloud's Agent for SAP, then gather the required diagnostic information and contact Cloud Customer Care. For more information, see [Google Cloud's Agent for SAP for SAP HANA diagnostic information](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
