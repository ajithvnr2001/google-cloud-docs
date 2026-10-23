---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery/
title: Backup and recovery for SAP HANA by using Backint \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:43.955108+00:00
---

# Backup and recovery for SAP HANA by using Backint  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Backup and recovery for SAP HANA by using Backint Stay organized with collections  Save and categorize content based on your preferences. 

This planning guide focuses solely on the _Backint_ feature of Google Cloud's Agent for SAP, which lets you perform backup and recovery operations for SAP HANA. For information about the agent and all its features, see [Google Cloud's Agent for SAP planning guide](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning).

For your SAP HANA systems, you can perform backup and recovery operations using the Backint feature of Google Cloud's Agent for SAP. This feature is available for SAP HANA systems running on Google Cloud, on Bare Metal Solution, on premises, or on other cloud providers.

The Backint feature of the agent is certified by SAP. This feature is integrated with SAP HANA so that you can store and retrieve backups directly from Cloud Storage by using SAP-native backup and recovery functions.

For information about how to configure this feature, see [Configure Backint based backup and recovery for SAP HANA](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery).

For information about performing backup and recovery operations for SAP HANA using Backint, see [Performing backup and recovery using Backint](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#performing_backup_and_recovery_using_backint).

For information about the SAP certification of the Backint feature, see:

  * SAP Note [2031547](https://launchpad.support.sap.com/#/notes/2031547)
  * [Backint for SAP HANA certification](https://wiki.scn.sap.com/wiki/pages/viewpage.action?pageId=451067853)



## Monthly cost estimate

You incur charges for the storage you use in Cloud Storage. For information about the charges, see [Cloud Storage pricing](https://cloud.google.com/storage/pricing).

To estimate the monthly Cloud Storage cost, you can use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

Use the following information to help you better estimate the cost:

  * Total size for full, delta, and incremental backups required in a month, including a projected growth rate.
  * The daily rate of change in terms of the SAP HANA log volume backups created by your SAP HANA database. You need to multiply this rate by the amount of days that you plan on keeping the log backups according to your backup strategy.
  * The location and type of the Cloud Storage bucket that fits your backup strategy. Single-region buckets must be used only for testing purposes.
  * The storage class of the Cloud Storage bucket. Select a class that aligns with how often you would need to access the data.
  * The estimated amount of Class A and Class B operations with Cloud Storage, for both backup and recovery, in a month. For information about these operations, see [Operation that fall into each class](https://cloud.google.com/storage/pricing#operations-by-class).
  * The estimated network egress for inter-, intra- and multi-region operations, such as when recovering a database using a backup. For more information, see [Data transfer within Google Cloud](https://cloud.google.com/storage/pricing#network-buckets).

Network ingress into Cloud Storage is free and therefore you don't need to include it in your estimate.




## Backint configuration file

You configure the Backint feature of Google Cloud's Agent for SAP by specifying parameters in a separate configuration file that the agent creates when you enable the feature.

By default, the configuration file is named `parameters.json`, and its default location is `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/parameters.json`.

`SID` is a placeholder variable for the SID of your SAP system.

You can either use a single configuration or use separate configuration files for each of the following: SAP HANA data volume, SAP HANA log volume, and SAP HANA backup catalog. You can also perform other customizations like renaming the files, and moving them to different directories. For instructions to perform these customizations, see [Customize the Backint configuration file](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#customize_the_backint_configuration_file).

## Storing backups in Cloud Storage buckets

The Backint feature of Google Cloud's Agent for SAP stores your SAP HANA backups in a Cloud Storage bucket. The following sections provide information about creating Cloud Storage buckets and how Google Cloud's Agent for SAP stores backups in the buckets.

**Note:** When storing backups in Cloud Storage buckets the [object quotas](https://docs.cloud.google.com/storage/quotas#objects) apply. Consider these limits while doing sizing calculations.

### Creating Cloud Storage buckets

When you create a bucket, you must select the bucket location and the bucket storage class.

A bucket location can be _regional_ , _dual-regional_ , or _multi-regional_. You need to choose a bucket depending on your need to restrict the location of your data, your latency requirements for backups and restores, as well as your need for protection against regional outages. For more information, see [Bucket locations](https://docs.cloud.google.com/storage/docs/locations).

Select dual-regional or multi-regional buckets in regions that are the same as or close to the regions in which your SAP HANA instances are running.

Choose a storage class based on how long you need to keep your backups, how frequently you expect to access them, and the cost. For more information, see [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes).

### Backup organization in the bucket

Google Cloud's Agent for SAP uses folders in your Cloud Storage bucket to organize your SAP HANA backups.

The agent creates a folder for each SAP HANA database, system or tenant, that you're backing up using the Backint feature. Inside the folder of a database, the agent creates separate folders for storing the backups of the SAP HANA data volume, the SAP HANA log volume, and the SAP HANA backup catalog.

To name the backups, the agent follows the SAP HANA [Naming Conventions](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/6d004299160140eba1460ccebfb5c4e4.html?q=databackup_0_1&locale=en-US).

The following are example paths for SAP HANA backups in a Cloud Storage bucket:

  * For the backups of the system database:
        
        BUCKET_NAME/SID/usr/sap/SID/SYS/global/hdb/backint/SYSTEMDB

  * For the backups of a tenant database:
        
        BUCKET_NAME/SID/usr/sap/SID/SYS/global/hdb/backint/DB_TENANT_SID

Replace the following

    * `BUCKET_NAME`: the name of your Cloud Storage bucket
    * `SID`: the system ID of your SAP system
    * `TENANT_SID`: the system ID of your tenant database



### Best practices for organizing backups

Use the following best practices for organizing backups in your Cloud Storage bucket:

  * Don't rename the folders or files inside your Cloud Storage bucket.

Renaming a folder or file effectively changes the backup path, which is an action that violates the standards enforced by SAP on third-party backup tools. Renaming a folder or file causes the Backint mechanism to fail during database recovery operations until you revert the folder or file to the name they had when the backup was created.

  * Don't use the same Cloud Storage bucket to store the backups of two or more SAP HANA databases that have the same SAP system ID (SID).

In Cloud Storage, Google Cloud's Agent for SAP organizes the SAP HANA backups in SID-specific folders. Therefore, if you use the same bucket to store backups of SAP HANA databases with the same SID, then backup operations can overwrite or delete backups.

The exceptions to this best practice are SAP HANA databases installed in high-availability (HA), disaster recovery (DR), or scale-out deployments, where all the SAP HANA nodes have the same SID. For these systems, the backups are stored in the same Cloud Storage bucket because during normal operations only one SAP HANA instance is active and writes to backups. For more information, see Using Backint in SAP HANA deployments.




### Supported customizations

While creating Backint based backups for your SAP HANA database, you can use the following customizations:

Backint configuration parameter | Use case  
---|---  
`metadata` |  To support activities such as lifecycle management of backups, you can associate key-value as metadata with your backup files in your Cloud Storage bucket. You can do this by including the `metadata` parameter while running the `configurebackint` command. This optional configuration parameter is available from version 3.3 of Google Cloud's Agent for SAP.  
`object_retention_time` and `object_retention_mode` |  To set a retention policy for each backup that you upload to your Cloud Storage bucket, instead of using a retention policy at the bucket level, you can use the [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock) feature provided by Cloud Storage. To use this feature, you need to [enable object retention](https://docs.cloud.google.com/storage/docs/using-object-lock#enable-retentions) for your bucket. Once you do so, you can set the retention time and retention mode while creating backups, by using the combination of the `object_retention_time` and `object_retention_mode` parameters.  
`folder_prefix` and `recovery_folder_prefix` |  To organize backups of different SAP HANA systems in the same Cloud Storage bucket, you must specify the `folder_prefix` parameter while creating backups. For this parameter, you can specify a single folder like `folder1`, or a multi-level path of folders like `folder1/folder2/folder3`.  This configuration parameter is available from version 3.1 of Google Cloud's Agent for SAP. When you specify `folder_prefix`, the path to your files are automatically changed to the following format:

  * For the backup of a system database, the path is: `BUCKET_NAME/folder_prefix/SID/usr/sap/SID/SYS/global/hdb/backint/SYSTEMDB/basepath/ebid.bak`
  * For the restore of a system database, the path is: `BUCKET_NAME/recovery_folder_prefix/SID/usr/sap/SID/SYS/global/hdb/backint/SYSTEMDB/basepath/ebid.bak`

If you've used the `folder_prefix` parameter while creating backups, then the agent automatically uses it during recovery operations, unless you specify the `recovery_folder_prefix` parameter.  **Warning:** Changing the value of this parameter changes the path for your backup files, which can lead to failures during database recovery operations. Therefore, before you change this parameter's value, make sure to test backup and recovery with the new parameter value in a non-production environment.   
`shorten_folder_path` |  To automatically shorten the path to the files in your Cloud Storage bucket, you can specify the `shorten_folder_path` boolean parameter while running the `configurebackint` command. This configuration parameter is available from version 3.3 of Google Cloud's Agent for SAP. When you specify this parameter, the path to your files are automatically shortened to the following format:

  * For the backup of a system database, the path is reduced from `BUCKET_NAME/SID/usr/sap/SID/SYS/global/hdb/backint/SYSTEMDB/basepath/ebid.bak` to `BUCKET_NAME/SID/SYSTEMDB/basepath/ebid.bak`. 
  * For the backup of a tenant database, the path is reduced from `BUCKET_NAME/SID/usr/sap/SID/SYS/global/hdb/backint/DB_TENANT_SID/basepath/ebid.bak` to `BUCKET_NAME/SID/DB_TENANT_SID/basepath/ebid.bak`. 

If you also use the `folder_prefix` and/or `recovery_folder_prefix` parameters, then the shortened path includes the folder prefix as follows: `BUCKET_NAME/FOLDER_PREFIX/SID/...`.  **Warning:** Changing the value of this parameter changes the path for your backup files, which can lead to failures during database recovery operations. Therefore, before you change this parameter's value, make sure to test backup and recovery with the new parameter value in a non-production environment.   
  
## Encryption options for backups

By design, Cloud Storage always encrypts your data before it is stored in a bucket. To apply an additional layer of encryption to the data, you can use one of the following options:

Encryption option | Description  
---|---  
Use a [Customer-managed encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) with the Backint feature of Google Cloud's Agent for SAP.  |  To use a customer-managed encryption key, you must specify the path to the key on the `kms_key` parameter in your `PARAMETERS.json` file. You also need to give the service account used by the agent access to the key. For information about giving a service account access to an encryption key, see [Assign a Cloud Key Management Service key to a service agent](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access).   
Use a [Customer-supplied encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys) with the Backint feature of Google Cloud's Agent for SAP.  |  To use a customer-supplied encryption key, specify the path to the key on the `encryption_key` parameter in your `PARAMETERS.json` file. The key must be a base64-encoded AES-256 key string, as described in [Customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).   
Use [SAP HANA Backup Encryption](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/5f837a57ce5e468d9db21c8683bc84da.html).  |  This option is available from SAP HANA 2.0 SP01. You can encrypt the backups of your SAP HANA data and log volumes using AES 256-bit encryption. Backups of the SAP HANA backup catalog are never encrypted. This encryption requires you to create a [Backup Encryption Root Key](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/41bd12cc20204a64998f08829602bb0b.html) and perform additional configuration as described in the SAP HANA document [Encryption Configuration](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/fc2fa4e464dc4e57912b3f99f0f30a80.html). From SAP HANA 2.0 SPS07, unless you disable it, encryption for the `/hana/data`, `/hana/log`, and `/hanabackup` volumes are enabled by default during the installation. For information about how to create a backup of the root key, see the SAP document [Back Up Root Keys](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/b1e7562e2c704c19bd86f2f9f4feedc4.html).  
**Warning:** Irrespective of the encryption option that you use, make sure to store the encryption key in a secure location. If the encryption key is lost, then any file that is encrypted with the key is no longer usable.

Backup encryption requires additional memory and CPU resources during the backup and recovery operations. While encrypting backups typically won't have any impact on the database performance during backup or recovery operations, you might notice an impact on the overall system performance depending on the size of the SAP HANA database and the expected higher CPU usage.

### Encryption restrictions

The following restrictions apply to using encryption for backups:

  * If you specify both `kms_key` and `encryption_key` parameters, then Google Cloud's Agent for SAP fails and exits with a status of `1`.
  * If you specify the `parallel_streams` parameter with either the `kms_key` or the `encryption_key` parameter, then Google Cloud's Agent for SAP fails and exits with a status of `1`.



## Compression options for backups

Compressing a backup reduces its size, which reduces the space that it uses in your Cloud Storage bucket, and which in turn reduces your storage cost. However, compressing backups requires more CPU usage during backup operations and it can impact the overall performance during both backup and recovery operations.

As an alternative to compressing backups, consider using the [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass) feature of Cloud Storage, which automatically transitions objects in your bucket to appropriate storage class based on the object's access pattern.

To compress your SAP HANA backups, you can use one of the following options:

Compression option | Description  
---|---  
Use the SAP HANA data backup compression |  **This is the recommended option, if you require backup compression.** From SAP HANA 2.0 SPS06, SAP HANA supports LZ4 compression algorithms when performing backup operations. By default, compression is disabled. For instructions to enable this compression, see the SAP HANA document [ Configure Data Backup Compression](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/86943e9f8d5343c59577755edff8296b.html).  
Use the Cloud Storage compression |  To use the built-in compression that the agent can perform while writing backups to your Cloud Storage bucket, use the `compress` parameter in `PARAMETERS.json`. We recommend that you don't enable this compression.  
  
## Multistreaming data backups

For versions prior to SAP HANA 2.0 SP05, SAP HANA supports multistreaming for databases larger than 128 GB. As of SAP HANA 2.0 SP05, this threshold is configurable by means of the SAP HANA parameter `parallel_data_backup_backint_size_threshold`, which specifies the minimum database backup size in GB for multistreaming to be enabled.

Multistreaming is useful for increasing throughput and for backing up databases that are larger than 5 TB, which is the maximum size for a single object in Cloud Storage.

To enable multistreaming, you set the SAP HANA parameter `parallel_data_backup_backint_channels` with the number of channels to be used. The optimum number of channels that you use for multistreaming depends on which SAP HANA is running.

Also consider the throughput capability of the data disk attached to your SAP HANA instance, as well as the bandwidth that your administrator allocates for backup activities. You can adjust the throughput by changing the number of streams, or limit throughput by using the `rate_limit_mb` parameter in `PARAMETERS.json`.

For a multi-regional Cloud Storage bucket, start with 8 channels. For a regional bucket, start with 12 channels. Adjust the number of channels as necessary to meet your backup performance objectives.

As stated in the SAP HANA documentation, each additional channel requires an I/O buffer of 512 MB. Specify the size of the I/O buffer by appropriately using the `data_backup_buffer_size` parameter in the `backup` section of the `global.ini` file. For more information regarding the effect of the I/O buffer size on backup times, see the SAP Note [2657261 - Long Backup duration with Backint in HANA DB](https://launchpad.support.sap.com/#/notes/2657261). As of HANA 2.0 SP05, SAP specifies a maximum value of 4 GB for this parameter. Testing in Google Cloud has not shown a benefit in increasing the buffer size significantly beyond the default, but this might vary for your workload.

For more information about multistreaming, in the SAP HANA Administration Guide that is specific to your SAP HANA version, see [Multistreaming Data Backups with Third-Party Backup Tools](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/2.0.00/en-US).

## Parallel uploads

For the SAP HANA log backup files, you can improve the upload performance by enabling the parallel upload feature of the Google Cloud's Agent for SAP. This feature is especially useful for the SAP HANA log backup files because they cannot be multi-streamed from SAP HANA.

For the SAP HANA data backups, you can tune the number of SAP HANA backup channels by using the SAP HANA parameter `parallel_data_backup_backint_channels`.

When parallel upload is enabled, Google Cloud's Agent for SAP splits each individual backup file that is received from SAP HANA into multiple parts that are then uploaded in parallel, which improves the upload performance. As the parts are received by Cloud Storage, they are reassembled and stored as the original single file that was received by Google Cloud's Agent for SAP from SAP HANA. The single file is subject to the 5 TB size limit for objects in Cloud Storage.

### Configuring parallel upload

You enable the parallel upload feature by specifying the `parallel_streams` parameters in your `PARAMETERS.json` file.

For information about this parameter, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#configuration_parameters).

### Parallel upload restrictions

The following restrictions apply to the parallel upload feature:

  * If you enable encryption using either the `encryption_key` or `kms_key` parameter, then you cannot use parallel upload. Encryption is incompatible with parallel upload. If you specify the `parallel_streams` parameter with either of these encryption parameters, then Google Cloud's Agent for SAP fails and exits with a status of `1`.
  * If you enable compression, then you cannot use parallel upload. Compression is incompatible with parallel upload. If you specify the `parallel_streams` parameter and omit the `compress` parameter in your configuration, then Google Cloud's Agent for SAP fails and exits with status of `1`.
  * If your Cloud Storage bucket implements a retention policy, then the bucket does not support parallel uploads. A retention policy prevents the reassembly of the parts into a single file, which causes the upload to fail.



### Tuning parallel uploads

For the SAP HANA log volume backups, parallel uploads can significantly improve the backup throughput because SAP HANA does not multistream the log backups.

In most cases, it is sufficient to specify the `parallel_streams` parameter in your Backint configuration file, with a value of 32 or less. For very large log volumes, you can maximize the throughput by specifying a high value such as `32` for `parallel_streams` and increasing the values for the SAP HANA parameters `log_segment_size_mb` and `max_log_backup_size`.

To limit the network bandwidth that your backups use, use the Backint configuration parameter `rate_limit_mb` to set the maximum amount of bandwidth that parallel uploads can use.

## Authentication and access control

Google Cloud uses [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts) to identify programs such as Google Cloud's Agent for SAP and to control which Google Cloud resources the programs can access.

### Required Cloud Storage permissions

To allow Google Cloud's Agent for SAP store and retrieve backups from a Cloud Storage bucket, the service account used by the host must be granted the IAM role **Storage Object Admin (`storage.objectAdmin`)**.

For instructions to set the IAM role, see [Set IAM roles](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#set_iam_roles).

### Service account considerations

If SAP HANA is running on a Compute Engine instance, then by default, Google Cloud's Agent for SAP uses the service account of the compute instance. If you use the compute instance's service account, then the agent gets the same project-level permissions as all of the other programs and processes that use the compute instance's service account.

For the strictest access control, [create a separate service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for the agent and grant the service account access to the Cloud Storage bucket at the bucket level.

If SAP HANA is not running on a Compute Engine instance, then you must [create a service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) for the agent. Create the service account in the Google Cloud project that contains the Cloud Storage bucket that the Google Cloud's Agent for SAP uses for backup and recovery.

When you create a service account for Google Cloud's Agent for SAP, you also need to [create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys). You store the key on the SAP HANA host and specify the path to the key to the `service_account_key` parameter in `PARAMETERS.json`. When SAP HANA is running on a Compute Engine instance, specifying the path to a key directs Google Cloud's Agent for SAP to use the service account that is associated with the key instead of the compute instance's service account.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

If you use a _customer-managed encryption key_ that is generated by Cloud Key Management Service to encrypt your backups in Cloud Storage, then you need to give your service account access to that encryption key. For more information, see [Assign a Cloud Key Management Service key to a service agent](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access).

### Access to Cloud APIs and metadata servers

Google Cloud's Agent for SAP requires access to Google Cloud IP addresses and hosts during the backup and recovery operations.

For more information, see [Enable access to Cloud APIs and metadata servers](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#enable_api_ip_access).

## Proxy servers and the agent

By default, Google Cloud's Agent for SAP bypasses any HTTP proxy and does not read proxy environment variables, such as `http_proxy`, `https_proxy`, or `no_proxy`, in the operating system.

Routing backups through a proxy negatively impacts the performance and reliability of all proxy traffic during sending or retrieving of backups from Cloud Storage. Consequently, Google Cloud strongly advises against using HTTP proxies with the Google Cloud's Agent for SAP.

If you have no alternative or your organization understands the performance implications and has the expertise that is required to support the performance of routing backups through a proxy server, then you can configure the agent to use a proxy.

The proxy settings for the Google Cloud's Agent for SAP are contained in the `net.properties` file:
    
    
    /usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/jre/conf/net.properties

### Bypassing proxy servers for backups and recoveries

Although Google Cloud's Agent for SAP bypasses proxy servers by default, you can make the bypass explicit by specifying the required Google Cloud domain names and IP addresses on the `http.nonProxyHosts` parameter in the `net.properties` file: `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/jre/conf/net.properties`. For example:
    
    
    http.nonProxyHosts=localhost|127.*|[::1]|*.googleapis.com|169.254.169.254|metadata.google.internal

### Using a proxy server for backups and recoveries

Routing backups through a proxy negatively impacts the performance and reliability of all proxy traffic during sending or retrieving of backups from Cloud Storage. Consequently, Google Cloud strongly advises against using HTTP proxies with the Google Cloud's Agent for SAP.

To configure Google Cloud's Agent for SAP to send backups through a proxy server, specify the proxy host and port number parameters in the `net.properties` file: `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/jre/conf/net.properties`.

For queries to the Compute Engine instance metadata, Google Cloud's Agent for SAP cannot use a proxy, and so you must specify the domain name and IP address for the instance metadata on the `http.nonProxyHosts` parameter.

The following example shows a valid proxy configuration for Google Cloud's Agent for SAP in the `net.properties` file:
    
    
    http.proxyHost=PROXY_HOST
    http.proxyPort=PROXY_PORT
    http.nonProxyHosts=localhost|127.*|[::1]|169.254.169.254|metadata.google.internal
    https.proxyHost=PROXY_HOST
    https.proxyPort=PROXY_PORT

## Tuning performance

The performance of backing up and recovering your SAP HANA databases depends on the total database size and the resources available to your SAP HANA host. You can improve the performance by using the following configuration options available in SAP HANA and Google Cloud's Agent for SAP:

  * Enable multistreaming by using the SAP HANA parameter `parallel_data_backup_backint_channels`. Also, specify the size of the I/O buffer using the SAP HANA parameter `data_backup_buffer_size`. For more information, see Multistreaming data backups.
  * Enable parallel uploads by specifying a value for the `parallel_streams` parameter in your Backint configuration file, `PARAMETERS.json`. This configuration can notably improve the performance for sending the SAP HANA log backups to Cloud Storage. For more information, see Parallel uploads.
  * If you require compressing backups, then use SAP HANA's built-in compression, which is the recommended compression option. For more information, see Compression options for backups.
  * Optimize the configuration related to SAP HANA log backups, as described in the SAP HANA document [Find the Optimal Log Backup Configuration](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/8f5faaa19b46461db35f57cf766c3dcf.html?q=log_segment_size_mb). See the SAP HANA Administration guide for your SAP HANA version.
  * If your SAP HANA system is running on a Compute Engine instance, then make sure that it's using SAP-certified Persistent Disk or Hyperdisk volumes. Using any other disk type can negatively impact backup performance, especially for the SAP HANA data volume. For information about the certified disk types, see [Supported disk types](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#supported_disk_types_2).



## Self diagnostics

To enable you to test your network connection and access to the Cloud Storage bucket, from version 3.0, Google Cloud's Agent for SAP includes a tool for performing self diagnostics.

When you run this tool, it creates several temporary files on your file system. You need at least 18 GB of available disk space in `/tmp` to create these temporary files. These files are then uploaded to your Cloud Storage bucket, are restored, verified, and then deleted. This tool prints any issues with your API access.

You can also test the backup performance by enabling the `compress` parameters, and by specifying different values for parameters such as `parallel_streams` and `threads`. While using this tool, you can use the optional parameters `diagnose_file_max_size_gb` and `diagnose_tmp_directory`. For more information about these parameters, see their descriptions in [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#configuration_parameters).

For instructions to perform the self diagnostics for Google Cloud's Agent for SAP, see [Validate backup and recovery](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-backint-backup-recovery#validate_backup_and_recovery).

## Backint metrics collection

For Backint based operations, Google Cloud's Agent for SAP can collect metrics that indicate the status and throughput of uploaded and downloaded files. These metrics are collected immediately after a file is uploaded or downloaded. This is an optional feature that is enabled by default. To disable this feature, set the value of `send_metrics_to_monitoring` parameter to `false` in the `PARAMETERS.json` configuration file. For more information about Monitoring pricing, see [Monitoring costs](https://cloud.google.com/stackdriver/pricing#monitoring-costs).

The following table describes the Backint related metrics that Google Cloud's Agent for SAP can collect. The metric strings in this table must be prefixed with `workload.googleapis.com/`. This prefix has been omitted from the entries in the following table.

**Metric** | **Labels** | **Description**  
---|---|---  
`sap/agent/backint/backup/status` | `fileName`: The name of the uploaded file.  
`fileSize`: The size of the uploaded file, in bytes. The value `0` indicates that the upload was unsuccessful. | This metric is sent for every file uploaded to your Cloud Storage bucket. 

  * The value `true` indicates that the file was uploaded successfully.
  * The value `false` indicates that the file failed to upload.

  
`sap/agent/backint/backup/throughput` | `fileName`: The name of the uploaded file.  
`fileSize`: The size of the uploaded file, in bytes.  
`transferTime`: The total time, in seconds, that the transfer took to complete. This includes all the network, disk, and memory operations. | This metric is sent if the upload was successful and the `fileSize` is at least `1 GB`. The metric value indicates the average network transfer speed in MBps.   
`sap/agent/backint/restore/status` | `fileName`: The name of the downloaded file.  
`fileSize`: The size of the downloaded file, in bytes. The value `0` indicates that the download was unsuccessful. | This metric is sent for every file downloaded from your Cloud Storage bucket. 

  * The value `true` indicates that the file was downloaded successfully.
  * The value `false` indicates that the file failed to download.

  
`sap/agent/backint/restore/throughput` | `fileName`: The name of the downloaded file.  
`fileSize`: The size of the downloaded file, in bytes.  
`transferTime`: The total time, in seconds, that the transfer took to complete. This includes all the network, disk, and memory operations. | This metric is sent if the download was successful and the fileSize is at least `1 GB`. The value indicates the average network transfer speed in MBps.   
  
## Logging

In addition to the logs kept by SAP HANA in `backup.log`, the Backint feature of Google Cloud's Agent for SAP writes operational and communication-error events to log files in the following directory: `/usr/sap/SID/SYS/global/hdb/opt/backint/backint-gcs/logs`.

These logs can also be found in the main log file of Google Cloud's Agent for SAP, which is located in the directory `/var/log/google-cloud-sap-agent/`.

When the size of a log file reaches 25 MB, Google Cloud's Agent for SAP rotates the log files.

By default, Google Cloud's Agent for SAP sends the Backint related log files to [Cloud Logging](https://docs.cloud.google.com/logging/docs). You can disable this by setting the `log_to_cloud` parameter, in your `PARAMETERS.json` file, with the value `false`.

## Using Backint in SAP HANA deployments

The following sections provide scenario-specific planning information for using the Backint feature of Google Cloud's Agent for SAP, with SAP HANA.

### Using Backint in HA deployments

In an SAP HANA high-availability (HA) cluster, you need to install Google Cloud's Agent for SAP on each node in the cluster, and enable the Backint feature.

Use the same Backint configuration and the same Cloud Storage bucket specifications for each SAP HANA instance in the HA cluster. You can use the same bucket specifications because during normal operations, only the active SAP HANA instance in an HA configuration writes backups to Cloud Storage, and the secondary system is in replication mode. This is true for the backups of the SAP HANA data volume, SAP HANA log volume, and the SAP HANA backup catalog. Also, application clustering software such as Pacemaker prevents split-brain scenarios, in which more than one SAP HANA instance in a cluster thinks that it is the primary instance.

During maintenance activities, when clustering might be disabled, if the standby database is removed from replication and brought back online, you need to make sure that backups are triggered only on the primary database. You can use the following options for this:

  * In your `PARAMETERS.json` file, update the `bucket` parameter to point to a different Cloud Storage bucket.
  * Break the symbolic link for `/usr/sap/SID/SYS/global/hdb/opt/hdbbackint` so that the sending backups to Cloud Storage fails. This option is more useful in the short term if you plan to reconfigure the new database as the standby database.



Because Google Cloud's Agent for SAP is unaware of which SAP HANA instance is the active one, and because the agent has no mechanism to schedule or trigger backups, you need to use SAP mechanisms such as the SAP ABAP transaction `DB13` to manage the scheduling and triggers for backups. SAP ABAP applications connect to the HA cluster through the virtual IP, and therefore the backup trigger is always routed to the active SAP HANA instance.

If the backup trigger is defined locally on each server, for example as a local operating system script, and both the primary and secondary systems think that they are the active system, then they both might attempt to write backups to the Cloud Storage bucket.

If you don't manage these situations, then you might observe more than one SAP HANA instance in your HA cluster writing backups to Cloud Storage, which could overwrite backups or even delete them.

### Using Backint in DR scenarios

In a disaster recovery (DR) configuration, where a recovery instance of SAP HANA in another Google Cloud region is kept in sync by using asynchronous SAP HANA System Replication, use different Cloud Storage buckets for the backup and recovery operations. To configure this, specify the bucket names to the `bucket` and `recovery_bucket` parameters in your `PARAMETERS.json` file.

While the DR system is usually in replication mode and therefore cannot run a backup itself, during regular disaster recovery testing, the recovery instance is brought online and could trigger backups. If it does, and the recovery system doesn't use a different Cloud Storage bucket, then the backups might overwrite data from the primary database.

In the case of an actual disaster that requires you to recover from a backup to your DR region, you can update the Backint feature configuration to reference the multi-regional Cloud Storage bucket that your primary HA system uses.

### Using Backint in scale-out systems

In SAP HANA scale-out systems, you need to install the Google Cloud's Agent for SAP on each node in the system.

To simplify the management of the `PARAMETERS.json` files and, if you are using one, the agent's service account key, you can place these files in a shared NFS directory.

For information from SAP on file system layout recommendations for SAP HANA, in the SAP HANA Server Installation and Update Guide for your SAP HANA version, see [Recommended File System Layout](https://help.sap.com/docs/SAP_HANA_PLATFORM/2c1988d620e04368aa4103bf26f17727/4c24d332a37b4a3caad3e634f9900a45.html).

### Using Backint with high isolation level databases

The [Database isolation](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/d84c28a3cf324e59aa17f301b13497a9.html?locale=en-US) feature of SAP HANA provides OS level protection for your tenant databases. When you enable database isolation, you can configure a dedicated OS user and authenticated communication to run the processes of each tenant database.

When you enable the Backint feature of Google Cloud's Agent for SAP for use with high isolation level databases, then the agent sets the required permissions on the Backint binaries. After enabling the feature, you can use separate `PARAMETERS.json` configuration files for each database.

For information about how to configure the Backint feature for high isolation databases, see the SAP document [Set the isolation level to high for backups with third-party backup tools](https://help.sap.com/docs/SAP_HANA_PLATFORM/6b94445c94ae495c83a19646e7c3fd56/d9d208be546e4af2b89a9dbfbad42ea3.html).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
