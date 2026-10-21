---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery/
title: Configure Backint based backup and recovery for SAP HANA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:51.381942+00:00
---

# Configure Backint based backup and recovery for SAP HANA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure Backint based backup and recovery for SAP HANA Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure Google Cloud's Agent for SAP to perform Backint based backup and recovery for SAP HANA.

For conceptual information about this feature, which can help in planning your implementation, see [Backup and recovery for SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery).

For information about how to create Backint based backups and recover your SAP HANA by using them, see [Back up and recover SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#back_up_and_recover_sap_hana_by_using_backint).

## Before you begin

  * Validate your installation of **version 3.15 (latest)** of Google Cloud's Agent for SAP. For instructions, see the [installation guide for your scenario](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).
  * If you have installed the agent on a Bare Metal Solution server, then make sure that you have completed the required prerequisites and set up a service account. For instructions, see [Configure Google Cloud's Agent for SAP on Linux](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configure_agent4sap).
  * If your SAP HANA database is running in an on-premises environment, then make sure to set up a service account and its key. For information about how to do this, see [Configure Google Cloud's Agent for SAP on Linux](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configure_agent4sap).
  * If you need to enable this feature for an instance of Google Cloud's Agent for SAP that is running on a host other than a Compute Engine instance or a Bare Metal Solution server, then you must create an incident with SAP support in component `BC-OP-LNX-GOOGLE` so that both SAP and Google Cloud can evaluate your configuration.
  * Install SAP HANA: 
    * For information about automating the installation of SAP HANA on Google Cloud using Terraform, see the [deployment guide for your scenario](https://docs.cloud.google.com/sap/docs/tf-for-sap#supported_sap_solutions).
    * For information about installing SAP HANA on Bare Metal Solution, see [SAP HANA on Bare Metal Solution planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-on-bms-planning).



## Create a Cloud Storage bucket

Before you enable the Backint feature of Google Cloud's Agent for SAP, make sure that there exists a Cloud Storage bucket to store your backups. If you have a Cloud Storage bucket, then you can skip this section.

For information about storing backups in Cloud Storage buckets, see [Storing backups in Cloud Storage buckets](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#storing_backups_in_storage_bucket).

To create a Cloud Storage bucket:

### Google Cloud console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page. 

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click add_box **Create**. 
  3. On the **Create a bucket** page, enter your bucket information. To go to the next step, click **Continue**. 
     1. In the **Get started** section, do the following: 
        * Enter a globally unique name that meets the [bucket naming requirements](https://docs.cloud.google.com/storage/docs/bucket-naming#requirements).
        * To add a [bucket label](https://docs.cloud.google.com/storage/docs/tags-and-labels#bucket-labels), expand the **Labels** section (expand_more), click _add_box_ **Add label** , and specify a `key` and a `value` for your label. 
     2. In the **Choose where to store your data** section, do the following: 
        1. Select a [Location type](https://docs.cloud.google.com/storage/docs/locations).
        2. Choose a location where your bucket's data is permanently stored from the **[Location type](https://docs.cloud.google.com/storage/docs/locations#available-locations)** drop-down menu. 
           * If you select the [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr) location type, you can also choose to enable [turbo replication](https://docs.cloud.google.com/storage/docs/availability-durability#turbo-replication) by using the relevant checkbox. 
        3. To set up [cross-bucket replication](https://docs.cloud.google.com/storage/docs/availability-durability#cross-bucket-replication), select **Add cross-bucket replication via Storage Transfer Service** and follow these steps: 

#### Set up cross-bucket replication

           1. In the **Bucket** menu, select a bucket.
           2. In the **Replication settings** section, click **Configure** to configure settings for the replication job.

The **Configure cross-bucket replication** pane appears.

              * To filter objects to replicate by object name prefix, enter a prefix that you want to include or exclude objects from, then click add **Add a prefix**.
              * To set a storage class for the replicated objects, select a storage class from the **Storage class** menu. If you skip this step, the replicated objects will use the destination bucket's storage class by default.
              * Click **Done**.

     3. In the **Choose how to store your data** section, do the following: 
        1. Select a [default storage class](https://docs.cloud.google.com/storage/docs/storage-classes) for the bucket or [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) for automatic storage class management of your bucket's data.
        2. To enable [hierarchical namespace](https://docs.cloud.google.com/storage/docs/hns-overview), in the **Optimize storage for data-intensive workloads** section, select **Enable hierarchical namespace on this bucket**. **Note:** You cannot enable hierarchical namespace in existing buckets.
     4. In the **Choose how to control access to objects** section, select whether or not your bucket enforces [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), and select an [access control method](https://docs.cloud.google.com/storage/docs/access-control) for your bucket's objects. **Note:** You cannot change the **Prevent public access** setting if this setting is enforced at an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention).
     5. In the **Choose how to protect object data** section, do the following: 
        * Select any of the options under **Data protection** that you want to set for your bucket. 
          * To enable [soft delete](https://docs.cloud.google.com/storage/docs/soft-delete), click the **Soft delete policy (For data recovery)** checkbox, and specify the number of days you want to retain objects after deletion.
          * To set [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning), click the **Object versioning (For version control)** checkbox, and specify the maximum number of versions per object and the number of days after which the noncurrent versions expire.
          * To enable the retention policy on objects and buckets, click the **Retention (For compliance)** checkbox, and then do the following: 
            * To enable [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), click the **Enable object retention** checkbox.
            * To enable [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock), click the **Set bucket retention policy** checkbox, and choose a unit of time and a length of time for your retention period.
        * To choose how your object data will be encrypted, expand the **Data encryption** section (expand_more), and select a [**Data encryption** method](https://docs.cloud.google.com/storage/docs/encryption).
  4. Click **Create**. 



### Command line

Create a Cloud Storage bucket and configure it as follows:
     * Replace `STORAGE_CLASS` with your preferred [storage class](https://docs.cloud.google.com/storage/docs/storage-classes). 
     * Replace `LOCATION` with your preferred location (`ASIA`, `EU`, or `US`) 
     * Replace `BUCKET_NAME` with a bucket name that meets the [bucket name requirements](https://docs.cloud.google.com/storage/docs/buckets#naming). 
    
    gcloud storage buckets create gs://BUCKET_NAME --default-storage-class STORAGE_CLASS --location LOCATION




**Note:** The encryption options presented in the Google Cloud console during bucket creation apply generally to objects at rest in the bucket. The Backint feature of Google Cloud's Agent for SAP provides additional encryption options for your backups that are independent of the bucket encryption options. For more information, see [Encryption options for backups](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#encryption_options_for_backups).

## Set IAM roles

To allow Google Cloud's Agent for SAP perform backup and recovery operations for SAP HANA, you must ensure that the service account being used by your Compute Engine instance or Bare Metal Solution server includes the IAM role **Storage Object Admin (`storage.objectAdmin`)**.

To add this role to your service account, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/project/_/iam-admin/iam)

  2. Select your Google Cloud project.

  3. Identify the service account to which you want to add the role.

     * If the service account isn't already on the principals list, then it doesn't have any roles assigned to it. Click **Add** and enter the email address of the service account.
     * If the service account is already on the principals list, then it has existing roles. Click the **Edit** button for the service account that you want to edit.
  4. From the list of available roles, select **Storage Object Admin**.

  5. Click **Add** or **Save** to apply the roles to the service account.




For a granular level of access, you can set the following IAM permissions to your custom role for your service account on a project level:

  * `storage.objects.list`
  * `storage.objects.create`



You must also set IAM Policies on your bucket by granting your principal the following IAM permissions:

  * `storage.objects.get`
  * `storage.objects.update`
  * `storage.objects.delete`



Add the following permissions if you want to perform multipart uploads:

  * `storage.multipartUploads.create`
  * `storage.multipartUploads.abort`



For more information about how to create a custom role, see [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating). For more information on granting a principal a custom role for bucket-level access, see [Add a principal to a bucket-level policy](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

## Enable access to Cloud APIs and metadata servers

Google Cloud's Agent for SAP requires access to the following Google Cloud IP addresses and hosts during the backup and recovery operations:

  * For access to Cloud Storage, `storage.googleapis.com`.
  * For the Compute Engine instance metadata server: 
    * `oauth2.googleapis.com`, for authentication
    * `169.254.169.254`
    * `metadata.google.internal`



If Google Cloud's Agent for SAP and your SAP HANA system are running on a Compute Engine instance that does not have access to the internet, then you need to configure [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) so that the agent can interact with Cloud Storage and, if using a dedicated service account, authenticate itself with Google Cloud. For instructions, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## Enable the Backint feature

To enable the Backint feature of Google Cloud's Agent for SAP, complete the following steps:

  1. Connect to your SAP HANA host by using SSH.

If your host is a Compute Engine instance, then from the [VM instances](https://console.cloud.google.com/compute/instances) page in Google Cloud console, you can click the **SSH** button for your instance, or use your preferred SSH method.

  2. Switch to the SAP HANA system administrator:
         
         sudo su - SID_LCadm

Replace `SID_LC` with the SID. Use lowercase for any letters.

This command also sets several environment variables, including `$SAPSYSTEMNAME`, which is set with the SID of your SAP HANA database.

  3. Enable the Backint feature for Google Cloud's Agent for SAP:
         
         /usr/bin/google_cloud_sap_agent installbackint

Alternatively, to install the Backint related files on a host with a different SID, include the `sid` flag:
         
         /usr/bin/google_cloud_sap_agent installbackint -sid=DIFFERENT_SID_LC

Replace `DIFFERENT_SID_LC` with the SID of the required SAP HANA instance. Use lower case for any letters.

After the command is run successfully, all files related to the Backint feature of Google Cloud's Agent for SAP are installed in the directory `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/`. This includes files that are necessary for integrating the agent with SAP HANA. It also detects **Cloud Storage Backint Agent for SAP HANA** on your host, disables that agent, and copies its files to a recoverable directory on your host. For more information, see [Upgrading from the legacy Backint agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#upgrade_from_backint).

  4. Configure the Backint feature:

###  Run command 

     * If your SAP HANA database is running on a Compute Engine instance or a Bare Metal Solution server, then to configure the agent's Backint feature, run the `configurebackint` command. We recommend this approach over editing the agent's Backint configuration file.
           
           /usr/bin/google_cloud_sap_agent configurebackint \
            -f="PATH_TO_PARAMETERS_FILE" \
            -bucket="BUCKET_NAME"

     * If your SAP HANA database is running in an on-premises environment, then configure the agent's Backint feature by running the following command:
           
           /usr/bin/google_cloud_sap_agent configurebackint \
            -f="PATH_TO_PARAMETERS_FILE" \
            -bucket="BUCKET_NAME" \
            -service_account_key="PATH_TO_KEY" \
            -log_to_cloud=false \
            -send_metrics_to_monitoring=false

Replace the following:

       * `PATH_TO_PARAMETERS_FILE`: the path to your `PARAMETERS.json` Backint configuration file
       * `BUCKET_NAME`: the name of the Cloud Storage bucket where you want to store your SAP HANA backups
       * `PATH_TO_KEY`: the fully-qualified path to the JSON-encoded Google Cloud service account key that you set up

Optionally, you can set more parameters while running this command. For information about these parameters, see Configuration parameters.

###  Edit configuration file 

As an alternative to running the agent's `configurebackint` command, you edit the Backint configuration file as follows:

     1. Open the Backint configuration file:
            
            /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters.json

Replace `SID` with the SID of the SAP system where you installed the Backint related files.

The following is an example of what the configuration file contains:
            
            {
             "bucket": "",
             "log_to_cloud": true
            }

     2. To allow Google Cloud's Agent for SAP to perform Backint based backup and recovery operations for your SAP HANA system, edit the configuration file and then specify the following parameters:

        * `bucket`: specify the name of the Cloud Storage bucket where you want to store your SAP HANA backups
        * `service_account_key`: if you have created a service account for Google Cloud's Agent for SAP, then specify the absolute path to the directory on your host where you've uploaded the corresponding JSON-encoded service account key

For more information, see [Service account considerations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#service_account_considerations).

     3. If your SAP HANA database is running in an on-premises environment, then make sure to also set the following:

        * `"log_to_cloud": false`
        * `"send_metrics_to_monitoring": false`
     4. Optionally, you can modify other configuration parameters. For information about these parameters, see Configuration parameters.

     5. Save the configuration file.




**Caution:** The default values for the Backint configuration parameters are optimized for performance for most systems. Therefore, before you edit any default parameter value, make sure to test the new values for performance in a non-production environment. 

### Customize the Backint configuration file

Optionally, after you enable the Backint feature of Google Cloud's Agent for SAP, you can perform the following customizations:

  * Rename the `parameters.json` file.

To indicate this renaming, this file is referred to as `PARAMETERS.json` in the Google Cloud's Agent for SAP documentation.

  * Create a separate configuration file for each of the following: SAP HANA data volume, SAP HANA log volume, and SAP HANA backup catalog.

Make sure to set a unique name for each configuration file.

  * Move these configuration files to a different directory. For example, in a scale-out deployment, you can store the Backint related configuration files of all your nodes in a shared directory that is accessible to the nodes. This can make it easier for you to manage these files.




If you perform any of these customizations, then make sure to appropriately specify the filename and its path for the parameters in your SAP HANA's `global.ini` file. For instructions, see Configure SAP HANA for the Backint feature.

### Configure SAP HANA for the Backint feature

After you've enabled the Backint feature of Google Cloud's Agent for SAP, you need to configure your SAP HANA system to use this feature:

**Note:** If your SAP HANA database is using the [Database isolation](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/d84c28a3cf324e59aa17f301b13497a9.html?locale=en-US) feature, then you require additional configuration to perform Backint based backup and recovery. For more information, see [Using Backint with high isolation level databases](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#using_backint_with_high_isolation_level_databases).

  1. Use SAP HANA Studio or SAP HANA Cockpit to edit the `global.ini` configuration file.

  2. In the `backup` section of the `global.ini` file, specify values for the following parameters:

Parameter | Value  
---|---  
`data_backup_parameter_file` | `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/PARAMETERS_DATA.json`.  
`parallel_data_backup_backint_channels` | For [multistreaming data backups](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#multistreaming_data_backups), specify the number of channels considering the type of Cloud Storage bucket you're using, the required performance, and the disk throughput.   
`log_backup_using_backint` | If you're using a separate configuration file for the SAP HANA backup log volume, then specify the value `true`.   
`log_backup_parameter_file` |  If you're using a separate configuration file for the SAP HANA backup log volume, then specify the following value: `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/PARAMETERS_LOG.json`. Replace `PARAMETERS_LOG` with the name of the configuration file that you're using for the backups of the SAP HANA log volume.  
`catalog_backup_using_backint` | If you're using a separate configuration file for the SAP HANA backup catalog, then specify the value `true`.   
`catalog_backup_parameter_file` |  If you're using a separate configuration file for the SAP HANA backup catalog, then specify the following value: `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/PARAMETERS_CATALOG.json`. Replace `PARAMETERS_CATALOG` with the name of the configuration file that you're using for the backups of the SAP HANA backup catalog.  
  
The following is an example of a `global.ini` file that is configured to use the Backint feature of Google Cloud's Agent for SAP:
         
         [backup]
         log_backup_using_backint = true
         catalog_backup_using_backint = true
         parallel_data_backup_backint_channels = 16
         catalog_backup_parameter_file = /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters-catalog.json
         data_backup_parameter_file = /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters-data.json
         log_backup_parameter_file = /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters-log.json

  3. In the `persistence` section of the `global.ini` file, specify values for the following parameters:

     * `basepath_logbackup`: specify the directory in your file system where SAP HANA can store log backups when it is not able to connect to your Cloud Storage bucket; make sure that this directory has enough space to store backups.
     * `basepath_catalogbackup`: specify the directory in your file system where SAP HANA can store backups of the SAP HANA backup catalog when it is not able to connect to your Cloud Storage bucket; make sure that this directory has enough space to store backups.

![The parameters basepath_catalogbackup and basepath_logbackup show the same value in the persistence section of the global.ini file](https://docs.cloud.google.com/static/sap/docs/images/sap-hana-backint-globalini-persistence.png)




### Validate the setup for Backint based backup and recovery

You can validate if you have the correct Google Cloud setup for using the agent to perform Backint based backup and recovery for your SAP HANA system. You do this validation by running the agent's `status` command, which is supported from version 3.7 of the agent.

To do this, complete the following steps:

  1. Establish an SSH connection with your Compute Engine instance or Bare Metal Solution server.
  2. Run the following command:
         
         sudo /usr/bin/google_cloud_sap_agent status -b="BACKINT_PARAM_FILE_PATH" -f="backint"
         

If your Google Cloud setup for Backint based backup and recovery is correct, then the output includes the following. Your configuration would have different values for the configuration parameters related to Backint.
         
         Agent Status:
             ...
             Systemd Service Enabled: True
             Systemd Service Running: True
             Cloud API Full Scopes: True
             Configuration File: /etc/google-cloud-sap-agent/configuration.json
             Configuration Valid: True
         ...
         ----------------------------------------------------------------------------
         Backint: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
             Configuration:
                 bucket:           my-bucket                                                           (configuration file)
                 log_to_cloud:     true                                                                (default)
                 parallel_streams: 16                                                                  (configuration file)
                 param_file:       /usr/sap/NS1/SYS/global/hdb/opt/backint/backint-gcs/parameters.json (configuration file)
                 threads:          32                                                                  (configuration file)
         ...




### Validate backup and recovery

After you enable the Backint feature of Google Cloud's Agent for SAP, make sure to validate it by creating and restoring a backup in a test system.

**Note:** For use with SAP HANA scale-out deployments, you must install Google Cloud's Agent for SAP and enable this feature on each node of your SAP HANA system.

For testing, you can use the built-in [self diagnostics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#self_diagnostics) tool of the agent. You need at least 18 GB of available disk space on your file system to run this built-in tool. To use this built-in tool to validate backup and recovery, run the following command:
    
    
    sudo /usr/bin/google_cloud_sap_agent backint -u=IDENTIFIER -p=PATH_TO_PARAMETERS_FILE -f=diagnose

Replace the following:

  * `IDENTIFIER`: a value that identifies the execution of the command. This identifier is used to name the temporary folder that is created in the Cloud Storage bucket while performing the diagnostics.
  * `PATH_TO_PARAMETERS_FILE`: the path to your `PARAMETERS.json` file



While using this tool, you can use the optional parameters `diagnose_file_max_size_gb` and `diagnose_tmp_directory`. For more information about these parameters, see their descriptions in Configuration parameters.

If you had installed the Backint agent on your host, then the first time you use Google Cloud's Agent for SAP to perform a backup operation, Google Cloud's Agent for SAP creates JSON versions of the text configuration files. For more information, see [Upgrade from Backint agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#upgrade_from_backint).

## Example configuration file

The following is a completed `PARAMETERS.json` configuration file of the Backint feature of Google Cloud's Agent for SAP:
    
    
    {
      "bucket": "example-bucket-backup",
      "recovery_bucket": "example-bucket-recovery",
      "parallel_streams": 8,
      "service_account_key": "path/to/key/file.json",
      "rate_limit_mb": 100,
      "log_to_cloud": true,
      "log_level": "DEBUG"
    }

## Configuration parameters

The following table explains the configuration parameters of Google Cloud's Agent for SAP that are specific to the Backint feature.

For information about the mapping between the configuration parameters of the Backint agent and Google Cloud's Agent for SAP, see [Mapping of configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#backint_migration).

For information about the configuration parameters of Google Cloud's Agent for SAP, including the parameters related to metrics collection, see the [installation guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config) for your scenario.

**Caution:** The default values for the Backint configuration parameters are optimized for performance for most systems. Therefore, before you edit any default parameter value, make sure to test the new values for performance in a non-production environment. 

Parameters  
---  
`bucket` |  `String` Specify the name of the Cloud Storage bucket that the Google Cloud's Agent for SAP writes to and reads from. The agent creates backup objects with the storage class of the bucket and supports all storage classes. The agent uses the Compute Engine default encryption to encrypt data at rest.  
`recovery_bucket` |  `String` Optional. Specify the name of the Cloud Storage bucket that the agent reads during `RESTORE` operations. If you don't specify this parameter, then the agent uses the bucket specified for the `bucket` parameter for all operations: `BACKUP`, `RESTORE`, `INQUIRE`, `DELETE`, and `DIAGNOSE` operations. While we recommend using this parameter to simplify configuration management for system copy and system refresh operations, it's incompatible with the `CHECK ACCESS USING BACKINT` argument during SAP HANA restore operations.   
`log_to_cloud` |  `Boolean` Optional. To redirect the Backint related logs of Google Cloud's Agent for SAP, to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), specify `true`. The default value is `true`. If your SAP HANA database is running in an on-premises environment, then you must set this parameter's value to `false`. For information about the Backint related log file, see [Logging](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#logging).  
`log_level` |  `String` Optional. Specify the logging level for the Backint feature of Google Cloud's Agent for SAP, set the required value. The available log levels are as follows:

  * `DEBUG`
  * `INFO`
  * `WARNING`
  * `ERROR`

The default value is `INFO`. Don't change the logging level unless you are directed by Cloud Customer Care.  
`compress` |  `Boolean` Optional. Specify whether or not Google Cloud's Agent for SAP is to enable compression while writing backups to the Cloud Storage bucket. The default value is `false`. We recommend that you don't enable compression. Although compression reduces the cost of storage for backups in Cloud Storage, it requires more CPU processing during backup operations and slows down the effective backup throughput. Regardless of this parameter, Google Cloud's Agent for SAP supports both compressed and uncompressed backup files during a restore operation.  
`encryption_key` |  `String` Optional. Specify the path to the [customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) that you've configured your Cloud Storage bucket to use to encrypt backups. Make sure to specify a fully-qualified path to a base64-encoded AES-256 key. You cannot specify the `encryption_key` parameter with the `kms_key` or `parallel_streams` parameters.  
`kms_key` |  `String` Optional. Specify the path to the [customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) that you've configured your Cloud Storage bucket to use to encrypt backups. Specify the path by using the format `projects/KMS_PROJECT_ID/locations/LOCATION/keyRings/KEY_RING_NAME/cryptoKeys/KMS_KEY_NAME`, where:

  * `KMS_PROJECT_ID`: the ID of the Google Cloud project where the KMS key exists
  * `LOCATION`: the [Cloud KMS location](https://docs.cloud.google.com/kms/docs/locations) where your KMS key exists
  * `KEY_RING_NAME`: the name of the key ring that contains the KMS key
  * `KMS_KEY_NAME`: the name of the KMS key

If your SAP HANA system is running on a Compute Engine instance, then the key must be accessible to that instance. If your SAP HANA system is running on a host other than a Compute Engine instance, then the Cloud KMS key must be accessible to the service account used by Google Cloud's Agent for SAP. For more information, see [Service accounts](https://docs.cloud.google.com/kms/docs/iam#granting_permissions_on_a_resource). You cannot specify the `kms_key` parameter with the `encryption_key` or `parallel_streams` parameters.  
`folder_prefix` |  `String` Optional. Specify to set a prefix for the folders in the Cloud Storage bucket that the Google Cloud's Agent for SAP writes to and reads from. You can use this parameter to organize backups of different SAP HANA instances in the same Cloud Storage bucket. You can specify a single folder, like `folder1` or a multi-level path of folders, like `folder1/folder2/folder3`. This prefix is inserted as a folder between the `BUCKET_NAME` and `SID` values in the path for your SAP HANA backups in Cloud Storage. For more information, see [Supported customizations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#supported_customizations). This parameter is available from version 3.1 of the agent. **Warning:** Changing the value of this parameter changes the path for your backup files, which can lead to failures during database recovery operations. Therefore, before you change this parameter's value, make sure to test backup and recovery with the new parameter value in a non-production environment.   
`recovery_folder_prefix` |  `String` Optional. Specify to set a prefix for the folders in the Cloud Storage bucket that the agent reads during `RESTORE` operations. You can use this parameter to organize backups of different SAP HANA instances in the same Cloud Storage bucket. You can specify a single folder, like `folder1` or a multi-level path of folders, like `folder1/folder2/folder3`. For more information, see [Supported customizations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#supported_customizations). This parameter is available from version 3.1 of the agent. While we recommend using this parameter to simplify configuration management for system copy and system refresh operations, it's incompatible with the `CHECK ACCESS USING BACKINT` argument during SAP HANA restore operations.  **Warning:** Changing the value of this parameter changes the path for your backup files, which can lead to failures during database recovery operations. Therefore, before you change this parameter's value, make sure to test backup and recovery with the new parameter value in a non-production environment.   
`shorten_folder_path` |  `Boolean` Optional. Specify to shorten the object path in the Cloud Storage bucket that the agent reads and writes during all Backint operations. For more information, see [Supported customizations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#supported_customizations). This parameter is available from version 3.3 of the agent. **Warning:** Changing the value of this parameter changes the path for your backup files, which can lead to failures during database recovery operations. Therefore, before you change this parameter's value, make sure to test backup and recovery with the new parameter value in a non-production environment.   
`retries` |  `Int` Specifies the maximum number of times that Google Cloud's Agent for SAP retries a failed attempt to read or write to Cloud Storage. The default value is `5`, which is also the recommended value.  
`parallel_streams` |  `Int` Optional. Specify this parameter to enable parallel upload of backups to your Cloud Storage bucket. The value you specify for this parameter is the maximum number of parallel upload streams that Google Cloud's Agent for SAP can use. The maximum value is 32. Any value exceeding this is capped to 32. The default value is `1`, which disables parallel uploading. If you want to enable parallel upload for streaming data, or if your Cloud Storage bucket has a retention policy, then you must also set `xml_multipart_upload` to `true`. Don't enable parallel upload if any of the following apply:

  * The target Cloud Storage bucket uses a retention policy.
  * You have specified the `encryption_key` or `kms_key` parameters.

If any of the preceding conditions are met, then the agent exits with a status of `1`. For information about parallel uploads, see [Parallel uploads](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#parallel_uploads).  
`xml_multipart_upload` |  `Boolean` Optional. Specifies whether or not the [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) method is used when writing backups to the Cloud Storage bucket. The default value is `false`. This parameter is available from version 3.2 of the agent. To use the XML API multipart upload method, `parallel_streams` must have a value greater than `1`. If you set `xml_multipart_upload` to `true` but don't specify `parallel_streams`, then `parallel_streams` is automatically assigned the value `16`. We recommend using `xml_multipart_upload` only to parallelize log or catalog backups. To parallelize data backups, we recommend setting `parallel_data_backup_backint_channels` in the `backup` section of your `global.ini` file. For information about how to create separate parameter files for log and data backups, or how to set value for `parallel_data_backup_backint_channels`, see [Configure SAP HANA for the Backint feature](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#configure_sap_hana_for_the_backint_feature). In case of any failure, the XML multipart uploads are aborted automatically and the data being uploaded is deleted. We also recommend setting lifecycle conditions for [AbortIncompleteMultipartUpload](https://docs.cloud.google.com/storage/docs/lifecycle#abort-mpu) to ensure that data is deleted if the upload operation fails.  
`parallel_recovery_streams` |  `Int` Optional. Specify this parameter to enable parallel download of backups from your Cloud Storage bucket. The value you that specify for this parameter is the maximum number of parallel download streams that Google Cloud's Agent for SAP can use. The maximum value is 32. Any value exceeding this is capped to 32. The default value is `1`, which disables parallel downloading. This parameter is supported from version 3.7 of the agent. We recommend using `parallel_recovery_streams` only to parallelize the download of log or catalog backups. To parallelize the download of data backups, we recommend setting the `parallel_data_backup_backint_channels` parameter in the `backup` section of your `global.ini` file. For information about how to create separate parameter files for log and data backups, or how to set value for the `parallel_data_backup_backint_channels` parameter, see Configure SAP HANA for the Backint feature. Don't enable parallel recovery while downloading compressed backups, which you created by specifying the `compress` parameter. The agent exits with a status of 1.  
`storage_class` |  `String` Optional. Specify the [storage class](https://docs.cloud.google.com/storage/docs/storage-classes) to be used for writing backups to the Cloud Storage bucket. The available storage classes are as follows:

  * `STANDARD`
  * `NEARLINE`
  * `COLDLINE`
  * `ARCHIVE`

From version 3.7 of the agent, the default value is the storage class of your Cloud Storage bucket. For earlier versions of the agent, the default value is `STANDARD`. This parameter is available from version 3.2 of the agent.  
`metadata` |  `Map<String, String>` Optional. Specify key:value fields to store as metadata for objects when writing backups to the Cloud Storage bucket. This parameter is available from version 3.3 of the agent. The format in an example `PARAMETERS.json` configuration file is as follows:
    
    
    {
      "bucket": "example-bucket-backup",
      "metadata": {"key1": "value1", "key2": "value2"},
      "log_to_cloud": true
    }

The default metadata written is `{"X-Backup-Type": "PIPE"}` or `{"X-Backup-Type": "FILE"}` depending on the file type.  **Warning:** The key `X-Backup-Type` must not be overwritten by custom metadata.   
`custom_time` |  `String` Otional. Specify a date and time that you want to set for the `Custom-Time` metadata for the backups you upload to Cloud Storage. You must specify the date and time in the format specified in [`Custom-Time`](https://docs.cloud.google.com/storage/docs/metadata#custom-time). This parameter is available from version 3.4 of the agent. You can set this parameter with the value `UTCNow`, which sets the `Custom-Time` metadata with the UTC date and time when the backup is created. From version 3.6 of the agent, you can set a future date for the `Custom-Time` metadata by using `UTCNow+NUMBERd`. For example, to set the `Custom-Time` to 30 days from the backup creation time, set your configuration like the following example: 
    
    
    {
      "bucket": "example-bucket-backup",
      "custom_time": "UTCNow**+30d** ",
      "log_to_cloud": true
    }

The following is an example of how you can specify this parameter with a date-time value in your `PARAMETERS.json` file:
    
    
    {
      "bucket": "example-bucket-backup",
      "custom_time": "2024-06-25T13:25:00Z",
      "log_to_cloud": true
    }  
  
`rate_limit_mb` |  `Int` Optional. Specify the upper limit, in MB, for the outbound network bandwidth of Compute Engine during backup or restore operations. By default, Google Cloud does not limit the network bandwidth for Google Cloud's Agent for SAP. When you set this parameter, the throughput might vary, but won't exceed the specified limit.  
`service_account_key` |  `String` If Google Cloud's Agent for SAP is not running on a Compute Engine instance, then specify the fully-qualified path to the JSON-encoded Google Cloud service account. If Google Cloud's Agent for SAP is running on a Compute Engine instance, then we recommend that you don't specify this parameter and instead use the Compute Engine default authentication. Specifying this parameter directs Google Cloud's Agent for SAP to use the service account key when authenticating to Cloud Storage.  
`diagnose_file_max_size_gb` |  `Int` Optional. Specify the upper limit for the size of the temporary file, in GB, that the agent's [self diagnostics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#self_diagnostics) tool creates and deletes. The default value is 16 GB. This parameter is available from version 3.3 of the agent. For the successful operation of the self diagnostics tool, you must ensure that the available storage in your file system is at least 2-3 GB more than the value of `diagnose_file_max_size_gb`.  
`diagnose_tmp_directory` |  `String` Optional. Specify the directory used to read and write temporary files for the [self diagnostics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#self_diagnostics) tool of the agent. The default value is `/tmp/backint-diagnose`. This parameter is available from version 3.3 of the agent.  
`send_metrics_to_monitoring` |  `Boolean` Optional. Specifies whether or not the agent can collect metrics related to the status and throughput of files that are uploaded or downloaded during Backint operations. The agent sends the collected metrics to Cloud Monitoring. This parameter is available from version 3.3 of the agent. The default value is `true`. If your SAP HANA database is running in an on-premises environment, then you must set this parameter's value to `false`. For information about the Backint related metrics, see [Backint metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#backint_metrics_collection).  
`threads` |  `Int` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the number of worker threads. The default value is the number of processors in the host.  
`file_read_timeout_ms` |  `Int` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the maximum amount of time, in milliseconds, that Google Cloud's Agent for SAP waits to open the backup file. The default value is `60000` (60 seconds).  
`buffer_size_mb` |  `Int` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify this parameter to control the size of HTTPS requests to Cloud Storage during backup or restore operations. The default buffer size is 100 MB, which means that a single HTTPS request stream to or from Cloud Storage is kept open until 100 MB of data is transferred. The maximum buffer size is 250 MB. Because Google Cloud's Agent for SAP retries failed HTTPS requests multiple times before failing an operation, buffer sizes smaller than 100 MB result in less data that needs to be retransmitted if a request fails. Larger buffer sizes can improve throughput, but require more memory usage and more time to resend data in the event of a request failure. If you're using the `parallel_streams` parameter, then the required memory usage must be multiplied by that value because each stream requires its own buffer to process the HTTPS requests.  
`retry_backoff_initial` |  `Int` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the initial value, in seconds, for the retry period used in the exponential backoff network retries. The default value is `10`.  
`retry_backoff_max` |  `Int` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the maximum value, in seconds, for the retry period used in the exponential backoff network retries. The default value is `300`.  
`retry_backoff_multiplier` |  `Float` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the multiplier for the retry period used in the exponential backoff network retries. The multiplier must be greater than `1` and the default value is `2`.  
`log_delay_sec` |  `Int` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the logging delay, in seconds, for progress updates during reads and writes to the Cloud Storage bucket. The default value is `60`.  
`client_endpoint` |  `String` This is an optional **advanced tuning parameter.** Don't modify this parameter unless instructed to do so by Customer Care. Its default value rarely needs to be modified. Specify the endpoint of the Cloud Storage client. The default value is `storage.googleapis.com`.  
`object_retention_time` |  `String` Optional. Specify a date and time until which the backup must be retained in your Cloud Storage bucket. This parameter is supported from version 3.7 of the agent. You can set this parameter with the following values:

  * `UTCNow+NUMBERd`: sets the retention time to a future date. For example, to set the retention time to 30 days from the backup creation time, set `"object_retention_time": "UTCNow**+30d** "` in your Backint configuration file.
  * A specific timestamp represented in the [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) format `YYYY-MM-DD'T'HH:MM:SS.SS'Z'` or `YYYY-MM-DD'T'HH:MM:SS'Z'` when milliseconds are zero. For example, `2024-06-25T13:25:00Z`.

If you're specifying this parameter, then you also need to specify `object_retention_mode`. For more information about this parameter, see [Supported customizations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#supported_customizations).  
`object_retention_mode` |  `String` Optional. Specify the retention mode that you want to set for the retention configuration of the backup you're uploading to your Cloud Storage bucket. The supported values are `Locked` and `Unlocked`. This parameter is supported from version 3.7 of the agent. If you're specifying this parameter, then you also need to specify `object_retention_time`. For more information about this parameter, see [Supported customizations](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#supported_customizations).  
  
## Troubleshooting

To troubleshoot problems with version 3.15 (latest) of Google Cloud's Agent for SAP, see [Google Cloud's Agent for SAP troubleshooting guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/troubleshooting).

## Get support

If you need help resolving a problem with Google Cloud's Agent for SAP, then gather the required diagnostic information and contact Cloud Customer Care. For more information, see [Google Cloud's Agent for SAP for SAP HANA diagnostic information](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/getting-support-diag-info).

## What's next

  * To learn how to create Backint based backups and recover your SAP HANA database by using them, see [back up and recover SAP HANA by using Backint](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#back_up_and_recover_sap_hana_by_using_backint).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
