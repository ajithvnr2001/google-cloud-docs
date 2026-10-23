---
url: https://docs.cloud.google.com/sql/docs/mysql/instance-settings/
title: About instance settings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:06.636839+00:00
---

# About instance settings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/instance-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About instance settings Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/instance-settings "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings "View this page for the SQL Server database engine")

This page provides information about the settings available for Cloud SQL instances.

## Settings for Cloud SQL for MySQL

Setting | Modifiable after creation? | Possible values  
---|---|---  
Instance ID | N |  Composed of lowercase letters, numbers, and hyphens; must start with a letter. The total length must be 98 characters or less.   
Region | N | The instance's region. For a list of all available regions by Cloud SQL edition, see [Region availability](https://docs.cloud.google.com/sql/docs/mysql/region-availability-overview).  
Zone | Y | The possible values depend on the region.   
Database version | N |  For Cloud SQL Enterprise Plus edition, MySQL 8.0.31 and later: 
    
    
    Console string      API enum string
    **MySQL 8.4** (default)  MYSQL_8_4
    **MySQL 8.0**            MYSQL_8_0
    

For Cloud SQL Enterprise edition: 
    
    
    Console string       API enum string
    **MySQL 8.4** (default)  MYSQL_8_4
    **MySQL 8.0**            MYSQL_8_0
    **MySQL 5.7**            MYSQL_5_7
    **MySQL 5.6**            MYSQL_5_6
      
  
Automatic minor version upgrade | Y | [ Upgrades MySQL 8.0 instances automatically](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade) to the default minor version during scheduled maintenance updates. Available only for MySQL 8.0.35 and later.   
SSL mode | Y | Enforces/enables SSL as follows: 

  * `ALLOW_UNENCRYPTED_AND_ENCRYPTED`: allows non-SSL/non-TLS and SSL/TLS connections. For SSL connections, the client certificate isn't verified. This is the default value.
  * `ENCRYPTED_ONLY`: only allows connections encrypted with SSL/TLS.
  * `TRUSTED_CLIENT_CERTIFICATE_REQUIRED`: only allows connections encrypted with SSL/TLS and with valid client certificates.

When you use these values, you must set `requireSsl` to a compatible value or unset to avoid the conflict between values of two settings. For more information, see [IpConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ipconfiguration).   
Server CA mode | Y |  Lets you configure the server certificate authority (CA) for an instance. You can select one of the following available server CA options:

  * `GOOGLE_MANAGED_INTERNAL_CA`: this is the default value for instances created with the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), the Cloud SQL Admin API, and Terraform. With this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance.
  * `GOOGLE_MANAGED_CAS_CA`: with this option, a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service) is used. The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. For Cloud SQL Auth Proxy connections, to connect to an instance configured with the shared CA option, use the Cloud SQL Auth Proxy version 2.13.0 or later.
  * `CUSTOMER_MANAGED_CAS_CA`: with this option, you manage the CA hierarchy and the rotation of CA certificates. Before you can create an instance with this option, using CA Service, you create a CA pool in the same region as your instance and at least one CA in that pool. When you create your instance, you specify the CA pool. Your request is delegated to a project-specific service account, which has the permission to use the CA pool. The service account requests a CA from the pool and Cloud SQL uses that CA to sign the server certificate for the instance. For Cloud SQL Auth Proxy connections, to connect to an instance configured with the customer-managed CA option, use the Cloud SQL Auth Proxy version 2.14.3 or later. 

For more information, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies).  
Automatic server certificate rotation | Y | To enable, set `serverCertificationRotationMode` to `AUTOMATIC_ROTATION_DURING_MAINTENANCE`. To disable, set `serverCertificationRotationMode` to `NO_AUTOMATIC_ROTATION_DURING_MAINTENANCE`.   
[Set edition](https://docs.cloud.google.com/sql/docs/mysql/choose-edition) | Y | `ENTERPRISE` or `ENTERPRISE PLUS` **Note:** If the database version for your instance is MySQL 8.4, then the default Cloud SQL edition is Enterprise Plus.   
Set password policy | Y | Configured or not.  
Private IP | After it's activated, it can't be deactivated. | Activated or deactivated.  
Public IP | Y | Activated or deactivated.  
Data Api Access | Y | Activated or deactivated.  
Authorized networks | Y | If Public IP is enabled, IP addresses authorized to connect to the instance. You can also specify this value as an IP address range, in [ CIDR notation](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation).  
Private path for Google Cloud services | Y | Activated or deactivated.  
Data API access | Y | Allowed or disallowed (default).  
Data cache | Y | Activated (default) or deactivated.  
[Machine type](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview) | Y | 

  * **For Cloud SQL Enterprise Plus edition instances:** Cloud SQL offers predefined machine types in these machine series:
    * [N2](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n2_machine_types) series.
    * [C4A](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a) series.
    * [C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) series.
  * **For Cloud SQL Enterprise edition instances:** Cloud SQL offers both predefined and custom machine types in these machine series:
    * [general purpose - shared core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-shared-core) series.
    * [general purpose - dedicated core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-dedicated-core) series.
    * [N4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n4) series.

[Learn more.](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview)  
Cores | Y |  For Cloud SQL Enterprise Plus edition:  
2 to 128 ([predefined machine types](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview) only)  
  
For Cloud SQL Enterprise edition:  
1 to 96 (must be either 1 or an even number)  
Partial for shared vCPU   
Memory | Y |  For Cloud SQL Enterprise Plus edition: 6.75 GB to 8 GB per vCPU.   
The 6.75 GB to 1 vCPU ratio is for the `[db-perf-optimized-N-128](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview)` machine type only. All other machine types have the 8 GB to 1 vCPU ratio.   
For Cloud SQL Enterprise edition: 0.9 GB to 6.5 GB per vCPU (must be a multiple of 256 MB and at least 3.75 GB).   
Storage type | N |  **SSD** (default value)  
**HDD** (Cloud SQL Enterprise edition only)  
**Google Cloud Hyperdisk Balanced**  
Storage capacity | Y   
(Increase only) |  Standard and high memory machine types: up to 64 TB.  
Shared-core machine types (`db-f1-micro` and `db-g1-small`): up to 3054 GB.   
  
Note that creating or increasing storage capacity to 64 TB might increase latency of common operations, such as backups, dependent on your workload.   
[ Google Cloud Hyperdisk settings](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk) | Y |  This setting is only applicable for Cloud SQL Enterprise Plus edition instances using the C4 or C4A machine series, and for Cloud SQL Enterprise edition instances using the N4 machine series.  
  
**Provisioned IOPS** : 4,000 (default value)  
**Provisioned throughput** : 170 (default value)  
  
For more information about Google Cloud Hyperdisk settings, see [Google Cloud Hyperdisk Balanced](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview#hyperdisk).   
Enable automatic storage increases | Y |  **On** (default value)  
**Off**  
Data encryption method | N |  **Google-owned and Google-managed encryption key** (default value)  
**Cloud KMS key**  
Automatic storage increase limit | Y |  In GBs. `unlimited` in the gcloud CLI or `0` in the Cloud SQL Admin API (the default) means there is no limit (other than the maximum available storage for the instance tier).   
Automated backups | Y  
(select a preferred 4-hour window, or Any (default)) |  **On** (default value)  
**Off**  
Locations options | Y | **Multi-region** (default value)  
**Region** There is also a drop-down menu with a list of multi-regions when you select **Multi-region** or regions when you select **Region**.   
Instance deletion protection | Y | Activated or deactivated.  
Retain backups after instance deletion | Y | Activated or deactivated.  
Take a final backup at instance deletion | Y | Activated or deactivated.  
Set the retention period for a final backup | Y | The retention period for the final backup. This value can can be set to a maximum of 365 days. The default value is 30 days.  
Enable point-in-time recovery (PITR) | Y  
(see note) |  **On**   
**Off** The default value varies by instance. For more information, see [Use PITR](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr).  
Availability: Single zone | Y  
| **On** (default value)  
**Off**  
High availability (regional) | Y  
| **On**  
**Off** (default value)  
Maintenance: Maintenance window | Y |  **Any** (default value)  
**Day of the week and hour of the day**  
Maintenance: Maintenance timing | Y |  **Any** (default value)  
**Canary** (also **Week 1** (was **Earlier**) / **Preview**)  
**Stable** (also **Week 2** (was **Later**) / **Production**)  
**Week 5**  
Database flags | Y | See [Configuring Database Flags](https://docs.cloud.google.com/sql/docs/mysql/flags).   
  
Instance ID
    

The instance ID is the name of the instance. It is used to uniquely identify your instance within the project. Choose an instance name that is aligned with the purpose of the instance when possible.

The total length of `project-ID:instance-ID` must be 98 characters or less.

You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files).  **Important:** You should be aware that some resource identifiers (such as project IDs) might be retained beyond the life of your project. For this reason, avoid storing sensitive information in resource identifiers. ...see naming guidelines
Region
    The Google Cloud region where your instance is located. You can only set the region during instance creation. To improve performance, keep your data close to the services that need it. For more information, see [Instance Locations](https://docs.cloud.google.com/sql/docs/mysql/locations). 
Zone
    The Google Cloud zone where your instance is located. If you are connecting from a Compute Engine instance, select the zone where the Compute Engine instance is located. Otherwise, accept the default zone. You can edit the instance later to change the zone, if needed. For more information, see [Instance Locations](https://docs.cloud.google.com/sql/docs/mysql/locations). 
Machine Type
    

Determines memory and virtual cores available for your Cloud SQL instance. You can configure machine types from different machine series. The availability of different machine series is determined by your Cloud SQL edition and region.

  * **For Cloud SQL Enterprise Plus edition instances:** Cloud SQL offers predefined machine types in these machine series:

    * [N2](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n2_machine_types) series.
    * [C4A](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a) series.
    * [C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) series.
  * **For Cloud SQL Enterprise edition instances:** Cloud SQL offers both predefined and custom machine types in these machine series:

    * [general purpose - shared core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-shared-core) series.
    * [general purpose - dedicated core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-dedicated-core) series.
    * [N4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n4) series.

If you require real-time processing, such as online transaction processing (OLTP), make sure that your instance has enough memory to contain the entire working set. However, there are other factors that can impact memory requirements, such as number of active connections, and internal overhead processes. Perform load testing to avoid performance issues in your production environment. When you configure your instance, select sufficient memory and vCPUs to handle your needs, and scale up your instance as your requirements increase. A machine configuration with insufficient vCPUs might lose its SLA coverage. For more information, see [Operational guidelines](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines). For more information, see [Choose a machine series](/sql/docs/mysql/machine-series-overview). **Note:** The `db-f1-micro` and `db-g1-small` machine types aren't included in the Cloud SQL SLA. These machine types are configured to use a shared-core CPU, and are designed to provide low-cost test and development instances only. Don't use them for production instances.

Your machine type affects the cost of your instance. For more information, see [Instance Pricing](https://cloud.google.com/sql/pricing#2nd-gen-instance-pricing). You can also see pricing for various scenarios with the [Pricing Calculator](https://cloud.google.com/products/calculator).

Database version
    Unless you need a capability provided only by a specific version, accept the default database version (MySQL 8.4). For `gcloud` command and REST API usage, see [ the reference documentation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion). 
Automatic minor version upgrade
     Available only for instances running Cloud SQL for MySQL 8.0.35 or later. You can configure your instance to receive minor version upgrades automatically during its regularly scheduled maintenance events. This setting is enabled by default for MySQL 8.0 instances that you create without specifying a minor version. For more information, see [Automatic upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade). 
Storage type
    

Storage type is determined by the machine type you select for your instance. Each machine type belongs to a specific machine series, and each machine series offers different storage type options.

Storage type by Cloud SQL editions and machine series:

  * **Cloud SQL Enterprise Plus edition C4 machine series** : Google Cloud Hyperdisk Balanced
  * **Cloud SQL Enterprise Plus edition C4A machine series** : Google Cloud Hyperdisk Balanced
  * **Cloud SQL Enterprise Plus edition N2 machine series** : SSD
  * **Cloud SQL Enterprise edition N4 machine series** : Google Cloud Hyperdisk Balanced
  * **Cloud SQL Enterprise edition general purpose shared or dedicated core machine series** : SSD or HDD



For the N2 machine series, choosing **SSD** , the default and only value, provides your instance with SSD storage. For the general purpose shared or dedicated core machine series, **SSD** is the default value and provides lower latency and higher data throughput. If you don't need high-performance access to your data, for example for long-term storage or rarely accessed data, then you can reduce your costs by choosing a different machine series that uses **HDD**.  


For the C4, C4A, and N4 machine series, choosing **Google Cloud Hyperdisk Balanced** , the default and only value, provides a scalable, high-performance storage service. To learn more about Google Cloud Hyperdisk Balanced and its limitations, see [Storage options overview](https://docs.cloud.google.com/sql/docs/mysql/storage-options-overview).

Set password policy
    

The password policy for the instance. It includes the following options:

  * **Minimum length** : Specifies the minimum number of characters that the password must have.
  * **Password complexity** : Checks if the password is a combination of lowercase, uppercase, numeric, and non-alphanumeric characters.
  * **Restrict password reuse** : Specifies the number of previous passwords that you cannot reuse. Supported only on Cloud SQL for MySQL 8.0 and later.
  * **Disallow username** : Prevents the use of the username in the password.


Cores
    

The number of CPUs for your instance. You can also choose to create an instance with less than one CPU (a shared code instance, or shared vCPU). 

Memory
    

The amount of memory available for your instance. For performance-sensitive workloads such as online transaction processing (OLTP), make sure that your instance has enough memory to contain the entire working set. However, there are other factors that can impact memory requirements, such as number of active connections. Perform load testing to avoid performance issues in production.

SSL mode
    

(Optional) The SSL/TLS options for a database connection. Cloud SQL uses SSL/TLS to establish secure, authenticated, and encrypted connections to instances. You can use the SSL mode setting `sslMode`to enforce all database connections to an instance to use SSL/TLS encryption. You can also use this setting to enforce verification of client certificates. This setting gives you more granular controls over your SSL connections compared to `requireSsl`. We recommend that you use `sslMode`. For more information, see [IpConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ipconfiguration). You can enforce SSL when you create an instance or update it for any existing instance.

Server CA mode
    

(Optional) When you create an instance, you can select the server CA mode for the instance.

  * `GOOGLE_MANAGED_INTERNAL_CA`: this is the default value. Cloud SQL creates a new self-signed server CA for each instance.
  * `GOOGLE_MANAGED_CAS_CA`: the instance uses a server CA hierarchy hosted by Certificate Authority Service and the issuing CAs are shared across all instances in the same region. Supported only on MySQL 8.0.30 and later. 
  * `CUSTOMER_MANAGED_CAS_CA`: the instance uses a server CA that you create from a CA pool. With this option, you manage the CA hierarchy and the rotation of CA certificates. Supported only on MySQL 8.0.30 and later. 



For more information about these options, see [Certificate authority (CA) hierarchies](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies).

Automatic server certificate rotation
    

Choose whether to enable automatic server certificate rotation for the instance. Automatically rotates the server certificate for your instance during your regularly scheduled [maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance) or when you [perform self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/self-service-maintenance) up to 180 days before the certificate expires. By default, this option is disabled.

This feature is available only for instances that are configured with `serverCaMode` as `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA` only.

For more information about rotating Cloud SQL server certificates automatically, see [Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#automatic-server-certificate-rotation-cas).

Storage capacity
    

Choose a capacity to fit your database size. After you have created your instance, you can manually increase the storage capacity by [editing your instance configuration](https://docs.cloud.google.com/sql/docs/mysql/edit-instance), but you cannot decrease it. Increasing the storage capacity does not cause downtime.

The amount of storage capacity allocated for your instance affects the cost of your instance. For more information, see [Storage and Networking Pricing](https://cloud.google.com/sql/pricing#2nd-gen-storage-networking-prices).

For read replicas, the storage capacity must always be at least as high as the storage capacity of the primary instance. When a primary instance is resized, all read replicas are resized, if needed, so that they have at least as much storage capacity as the updated primary instance.

**Note:** Setting your storage capacity too small without enabling automatic storage increases can cause your instance to lose its SLA. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines)  
  
Cloud SQL may override the enable automatic storage increases and automatic storage increase limit settings to perform critical database maintenance. 
Enable automatic storage increases
    

If you enable this setting, Cloud SQL checks your available storage every 30 seconds. If the available storage falls below a threshold size, Cloud SQL automatically adds additional storage capacity. If the available storage repeatedly falls below the threshold size, Cloud SQL continues to add storage until it reaches the maximum of 64 TB.

**Note:** Automatic storage increases are permanent, but you can [manually shrink your storage capacity](https://docs.cloud.google.com/sql/docs/mysql/about-storage-shrink) if it becomes larger than your application needs. When you enable automatic storage increases, spikes in storage requirements result in incremental, permanent increases in storage size and cost for your instance. If the instance runs out of available storage, it goes offline, and the [Cloud SQL SLA](https://cloud.google.com/sql/sla) may not cover the outage. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines). 

The automatic storage increase setting of a primary instance automatically applies to any read replicas of that instance. The automatic storage increase setting cannot be independently set for read replicas.

**Note:** When an instance is nearly out of storage capacity, it's automatically stopped to prevent the loss of information. Enabling this setting might prevent such an operation. 

#### Threshold

The threshold size depends on the amount of storage provisioned for your instance:

**Google Cloud Hyperdisk Balanced**
    
    
    MAX(5, (provisioned storage) * 5 / 100)  
    
        The threshold size is rounded up to the nearest whole number.

  
For example, the threshold calculation for a 66 GB instance using Google Cloud Hyperdisk balanced is:  

    
    
    MAX(5, (66 * 0.05)) = MAX(5, 3.3) = 5 GB

**SSD or HDD**
    
    
    MIN(5 + (provisioned storage)/25, 25)  
    
        The threshold size is rounded down to the nearest whole number.

  
For example, the threshold calculation for a 66 GB instance using SSD or HDD is:  

    
    
    MIN(5 + (66/25), 25) = MIN(5 + 2.6, 25) = MIN(7, 25) = 7 GB

#### Amount of storage added

For Google Cloud Hyperdisk Balanced, the amount of storage added is 15% of the current provisioned storage, but can't be smaller than 5 GB. This can be calculated using the following:
    
    
    MAX(5, (provisioned storage) * 15 / 100)  
    
    The threshold size is rounded down to the nearest whole number.

For all other storage types, including SSD and HDD, the amount of storage added to the instance is equal to the threshold size, which cannot be larger than 25 GB.

#### Considerations for large disks

For Google Cloud Hyperdisk Balanced, instances provisioned with storage of more than 100 GB have a minimum possible empty space of 5% of the provisioned capacity.

For all other storage types and instances provisioned with storage of 500 GB or more, the threshold size is always 25 GB and the amount of storage added is always 25 GB. As a result, the maximum possible empty space is 50 GB. If you don't manually resize the instance with disk space that's greater than 5 TB, then the disk can remain at 99% capacity even though the instance has empty space.

Before an operation that rapidly grows disk space usage, such as a large import or a query that requires a large temp table, manually resize the disk, rather than depend on automatic storage increase to keep up. For Google Cloud Hyperdisk Balanced, storage increases that happen too frequently in a short timespan (4 hours), these increases might be subject to throttling. This might result in an instance running out of available space even though automatic storage increases are enabled and the storage size is below the [automatic storage increase limit](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-limit-2ndgen).

The file system uses some space internally for file system metadata. This space isn't included in the disk usage metric ([`database/disk/bytes_used`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics)). For large disks, the reserved space can take 1% to 3% of total disk size, so you might see the automatic storage increase occur before the disk usage reaches the threshold.

Data encryption method
    

By default, your Cloud SQL instance is encrypted with a Google-owned and managed key. If you want to control this key, then use a customer-managed encryption key (CMEK) in Cloud Key Management Service (KMS). Cloud KMS integrates with Cloud SQL.

Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions. In addition, you can use various encryption keys across resources. Using Cloud KMS also lets you track key usage, view audit logs, and control key life cycles.

Instead of Google owning and managing the keys that protect your data, you control and manage these keys in Cloud KMS.

For more information about CMEKs, see [About customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/sql/docs/mysql/cmek).

Automatic storage increase limit
    

If you enable the  automatic storage increase setting, you can provide a specific limit on how large the storage for your instance can automatically grow. Keep in mind that the bigger the size of the instance, the greater the operational latency.

You can't decrease storage size, so this limit can prevent your instance size from growing too large (due to a temporary increase in traffic). Keep in mind that when an instance becomes unable to add storage that it needs, the instance likely stops accepting incoming connections and could go offline.

By default, there is no limit on automatic storage increases other than the maximum available storage for the instance tier. 

To set the limit when you create the instance, use the `--storage-auto-increase-limit=INTEGER_VALUE_OF_GB` parameter, as described on the [create instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#gcloud) page. The value in GB must be at least the current storage size of the instance (minimum 10 GB) and cannot exceed the maximum storage capacity for the instance. To set the limit on an existing instance, use the same parameter with the `gcloud sql instances patch` command. 

To remove an existing automatic storage increase limit using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), run the `gcloud sql instances patch` command with `--storage-auto-increase-limit=unlimited` (the `--storage-auto-increase-limit` flag doesn't accept `0`): 
    
    
    gcloud sql instances patch INSTANCE_NAME \
      --storage-auto-increase-limit=unlimited

Setting `--storage-auto-increase-limit=unlimited` removes the custom limit so that storage can automatically increase up to the maximum available storage for the instance tier. In the Cloud SQL Admin API, setting the [`settings.storageAutoResizeLimit`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.Settings.FIELDS.storage_auto_resize_limit) field to `0` (the default value) removes the limit. 

The automatic storage increase limit setting of a primary instance automatically applies to any read replicas of that instance. The automatic storage increase limit setting cannot be independently set for read replicas.

Automated backups and point-in-time recovery
    

These options determine if automated backups are performed and if binary logging is enabled.

Both options add a small performance cost and use additional storage, but are required for the creation of replicas and clones, and for point-in-time recovery. When you select this option, you can also select a timeframe when automated backups occur. 

Automated backups happen daily, during the time window you choose. At the end of seven days, the oldest backup is deleted. 

For information about point-in-time recovery, see [ Overview of point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr).

For information about replication, see [ Replication Options](https://docs.cloud.google.com/sql/docs/mysql/replication). For information about cloning instances, see [Cloning Instances](https://docs.cloud.google.com/sql/docs/mysql/clone-instance).

**Note:** Enabling or disabling point-in-time recovery causes the instance to be restarted. Existing database connections are closed and must be reopened. 

To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations.

Retention settings for automated backups
    

The default value for the number of retained backups is 7 but you can change it to any value in the range of 1 to 365.

See [ Automated backup and transaction log retention](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention) for more information. 

Location options
    

You can choose to store backups in multiple or single regions. **Multi-region** is the default, and the recommended choice because it provides protection against downtime when a region becomes unavailable. Backups are stored in regions that are closest to the instance.

You also have the option of selecting a custom location for your backup. Only use this option if required by regulation or if an organization policy requires your backups to be in specific multiple or single regions. See [Custom locations](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#custom-backup-location) for more information. 

Instance deletion protection
    

Protects an instance against accidental deletion. If this setting is enabled, you must deactivate it before deleting the instance. See [ Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection). 

Retain backups after instance deletion
    

Retains on-demand and automated backups for an instance after the instance is deleted. For more information about this setting, see [ Retained backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retained-backups). 

Take a final backup at instance deletion
    

Takes a final backup of an instance at time of instance deletion. Use `final-backup-retention-days` to set the retention period for the final backup. If no retention period is set, then the retention period is set to default, which is 30 days. For more information about this setting, see [ Take a final backup before instance deletion](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backup). 

Set the retention period for the final backup
    

Sets the retention period for the final backup. The retention period can be set to a maximum of 365 days. If the `final-backup-retention-days` value isn't set when you enable `final-backup`, then the default retention period of 30 days is used. For more information about this setting, see [ Take a final backup before instance deletion](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#final-backup). 

Enable point-in-time recovery
    

Point-in-time recovery lets you recover from a backup, starting from a specific point in time. 

For information about point-in-time recovery, see [Overview of point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr).

Availability: Zonal
    

Puts your instance and backups in a single zone. When you select this option, there is no failover in the event of an outage. Recommended only for test and development purposes. 

High availability (regional)
    

When you select **High availability (regional)** , if there is an outage, your instance fails over to another zone in the region where your instance is located, as long as the failover zone is not having an outage. It is recommended that you select **High availability (regional)** for instances in your production environment. 

See the [Overview of the high availability configuration](https://docs.cloud.google.com/sql/docs/mysql/high-availability). 

Maintenance window
    

The day and hour that your maintenance events for the Cloud SQL instance are scheduled. For Cloud SQL Enterprise Plus edition primary instances, the maintenance downtime is typically less than 1 second. For all other instances, maintenance downtime is typically 60 seconds or less on average.

Read replicas don't support maintenance window settings at this time.

For more information about maintenance, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance#management).

Maintenance timing
    

Your preference about the relative timing of maintenance updates. You can receive your updates one or two weeks after the notification and test your maintenance updates in a test environment before your production instances get the update. You can also choose to receive the maintenance update five weeks ("`week5`") after the notification is sent out. The maintenance timing setting doesn't affect the maintenance version that Cloud SQL applies to your instance.

If you don't set the maintenance timing setting, Cloud SQL chooses the timing of updates to your instance (within its maintenance window, if applicable).

For more information about maintenance, see [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance#management).

Private IP
    Configures your instance to use private IP. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/private-ip). 
Public IP
    If enabled, your instance is allocated a public IPv4 address. When you deactivate Public IP, that address is released; you can reenable Public IP later, but you receive a different IPv4 address. By default, the public IP address is blocked for all addresses. Use Authorized networks to enable access. 
Data Api Access
     Controls whether to allow connections to the instance using the Data API. If activated, you can use [`executeSql`](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance) to execute statements on the instance. This setting is deactivated by default. 
Authorized networks
    You can add specific IP addresses or ranges of addresses to open your instance to those addresses. 

For information about configuring IP addresses, see [Configuring IP connectivity](https://docs.cloud.google.com/sql/docs/mysql/configure-ip). 

Private path for Google Cloud services
    

This configuration setting lets other Google Cloud services, such as BigQuery, access data in Cloud SQL and make queries against this data over a private connection. The configuration is available only when you configure your instance to use a private IP address, and you configure an authorized network to create a private connection.

In the Google Cloud console, configure a private path by selecting the **Enable private path** checkbox. For the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), use the `--enable-google-private-path` flag when you create the instance. 

Data API access
    

This setting controls connectivity to the instance using [Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance). It's disallowed by default. When allowed, authorized users can use Data API to connect to the instance. For instances with Private IP only, it allows authorized users to connect from the public internet.

In the Google Cloud console, configure Data API access by selecting the **Allow Data API** checkbox. For the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), use the `--data-api-access=ALLOW_DATA_API` flag when you create the instance. 

Data cache
    

Data cache is enabled automatically for Cloud SQL for MySQL Enterprise Plus edition instances. Data cache utilizes local SSDs to extend a buffer pool from memory to the SSD tier. Cloud SQL manages this setting. Caching your entire working set provides maximum performance when using data cache. You can use the Google Cloud console, [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), or Cloud SQL Admin API to turn this setting on or off for your Cloud SQL for MySQL Enterprise Plus edition instances.

Activation policy
    The activation policy is used only to start or stop the instance. You change the activation policy by [starting and stopping the instance](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance). Stopping the instance prevents further instance charges.
Database flags
    

You can set specific database flags on the Cloud SQL instance.

For a complete list of the database flags you can set, see [Configure Database Flags](https://docs.cloud.google.com/sql/docs/mysql/flags).

## Impact of changing instance settings

**Warning:** Moving an instance to a different zone causes instance downtime. The operation involves data replication across zones, meaning downtime duration scales directly with the size of the instance's disk.

For most instance settings, Cloud SQL applies the change immediately and connectivity to the instance is unaffected.

For MySQL instances, changing either the machine type or the zone of the instance results in the instance going offline for several minutes. Plan to make these kinds of changes when your application can handle an outage of this length.

If you're using Cloud SQL Enterprise Plus edition, then you can make some instance setting changes, such as scale up vCPUs or enable or disable data cache, with near-zero downtime. For more information, see [Availability in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/availability).

## What's next

  * Learn how to [edit your instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance).
  * Learn more about [database flags](https://docs.cloud.google.com/sql/docs/mysql/flags).
  * Learn how to [authorize IP access for your instance](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks).
  * Learn more about [replication options](https://docs.cloud.google.com/sql/docs/replication).
  * See [pricing](https://cloud.google.com/sql/pricing) for your instance. 
  * Learn more about [options for connecting to your instance](https://docs.cloud.google.com/sql/docs/mysql/external-connection-methods).
  * Learn how to [configure a public IP address for your instance](https://docs.cloud.google.com/sql/docs/mysql/configure-ip).
  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
