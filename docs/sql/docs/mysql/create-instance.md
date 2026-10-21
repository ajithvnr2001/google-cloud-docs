---
url: https://docs.cloud.google.com/sql/docs/mysql/create-instance/
title: Create instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:10.145394+00:00
---

# Create instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/create-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-instance "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance "View this page for the SQL Server database engine")

Cloud SQL for MySQL lets you deploy fully managed relational databases on Google Cloud. You can provision instances tailored to your workload while automating routine maintenance such as operating system patching, backups, and failover.

Before provisioning an instance, review feature availability in the [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro). For detailed information about all instance settings, see [Instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings).

## Key concepts

A newly-created instance has four system databases: 

  * [`information_schema`](https://dev.mysql.com/doc/refman/8.4/en/information-schema.html): Provides access to database metadata, information about the MySQL server.
  * [`mysql`](https://dev.mysql.com/doc/refman/8.4/en/system-schema.html): The system schema. It contains tables that store information required by the MySQL server as it runs.
  * [`performance_schema`](https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html): A feature for monitoring MySQL Server execution at a low level.
  * [`sys`](https://dev.mysql.com/doc/refman/8.4/en/sys-schema.html): Contains a set of objects that helps DBAs and developers interpret data collected by the performance schema.



The maximum number of instances you can have in a single project depends on the [network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture#overview) of those instances:

  * New SQL network architecture: You can have up to 1,000 instances per project.
  * Old SQL network architecture: You can have up to 100 instances per project.
  * Using both architectures: Your limit will be somewhere between 100 and 1,000, depending on the distribution of your instances across the two architectures.



[File a support case](https://support.google.com/googlecloud/answer/1041916) to request an increase. Read replicas are counted as instances.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  5. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  6. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  7. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  8. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). 

  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. Make sure you have the following roles on your user account: 
     * [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/mysql/iam-roles#roles)
     * [Compute Viewer](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer)

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

[Learn more](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions) about roles and permissions. 




## Create a MySQL instance

**Tip** : If you plan on using private networking, then you can deploy both the private networking setup of your choice and the Cloud SQL instance along with clients such as Compute Engine VMs by using Terraform. For more information, see [ Simplified Cloud Networking Configuration Solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions). 

### Console

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. Select **New instance**.
  4. On the **Choose your database engine** panel of the **Create an instance** page, click **Choose MySQL**.
  5. In the **Choose a Cloud SQL edition** section of the **Create a SQL Server instance** page, select the Cloud SQL edition for your instance: `Enterprise` or `Enterprise Plus`.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro).

  6. Select the edition preset for your instance. To see the available presets, click the **Edition preset** menu. **Note:** To learn about how edition presets differ from one another, click **Compare edition presets**.
  7. In the **Instance info** section, select the database version for your instance. To see the available versions, click the **Database version** menu. 
     * If you select MySQL 8.0 and MySQL 8.0.35 or later for the **Minor version** , then the [Enable automatic minor version upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade) checkbox is automatically selected for your instance. If you don't want to enable automatic version upgrade, then clear the checkbox. **Caution** : After the instance is created, you can't disable automatic minor version upgrade.
     * If you select MySQL 8.0 and MySQL 8.0.34 or earlier for the **Minor version** , then the **Enable automatic minor version upgrade** checkbox isn't available.

The database version can't be edited after the instance has been created.

Note: Only MySQL 8.0.31 and later are compatible with Cloud SQL Enterprise Plus edition. By default, MySQL 8.4 and 9.7 is Cloud SQL Enterprise Plus edition.
  8. In the **Instance ID** field of the **Instance info** pane, enter an ID for your instance.  
Don't include sensitive or personally identifiable information in your instance name. 

You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

  9. Set a password for the **root** user.

Although there's an option to set **No password** , this isn't recommended for security reasons.

To see the password in clear text, click the **Show password** icon.

You can either enter the password manually or click **Generate** to have Cloud SQL create a password for you automatically.

  10. Optional: Configure a password policy for the instance as follows: 
     1. Select the **Enable password policies** checkbox. Note: When you enable a password policy, statements that create users or change user passwords can cause additional latency due to password policy verification. 
     2. Click the **Set password policy** button, set one or more of the following options, and click **Save**. 
        * **Minimum length** : Specifies the minimum number of characters that the password must have.
        * **Password complexity** : Checks if the password is a combination of lowercase, uppercase, numeric, and non-alphanumeric characters.
        * **Restrict password reuse** : Specifies the number of previous passwords that you can't reuse. 

Supported only on Cloud SQL for MySQL 8.0 and later. 

        * **Disallow username** : Prevents the use of the username in the password.
Note: When you deselect the **Enable password policies** checkbox, the password policy parameters are reset.
  11. In the **Choose region and zonal availability** section, select the region and zone for your instance. Region availability might be different based on your Cloud SQL for MySQL edition. For more information, see [About instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings). 

Place your instance in the same region as the resources that access it. The region you select can't be modified in the future. In most cases, you don't need to specify a zone.

**Note:** If there is a resource location constraint on your organization policy, you must select one of the regions that the organization policy allows. You see a message about Resource Location Restriction in the **Choose region and zonal availability** section if a constraint exists. [Learn more](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 

If you are configuring your instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability), you can select both a primary and secondary zone.

The following conditions apply when the secondary zone is used during instance creation:

     * The zones default to `Any` for the primary zone and `Any (different from primary)` for the secondary zone.
     * If both the primary and secondary zones are specified, they must be distinct zones.
  12. In the **Customize your instance** section, update the settings for your instance. Click **Show configuration option** to display the groups of settings. Then, expand the groups you want to review and customize settings. A **Summary** of all the options you select is shown on the right. Customizing these instance settings is optional. Defaults are assigned in every case where no customizations are made. 

The following table is a quick reference to instance settings. For more details about each setting, see the [instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) page. 

Setting | Notes  
---|---  
**Machine type**  
Machine type | Select from Shared core or Dedicated core. For Shared core, each machine type is classified by the number of CPUs (cores) and amount of memory for your instance.   
Cores | The number of vCPUs for your instance. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#cpus-postgres).   
Memory | The amount of memory for your instance, in GBs. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#memory-postgres).   
Custom | For the Dedicated core machine type, instead of selecting a predefined configuration, select the **Custom** button to create an instance with a custom configuration. When you select this option, you need to select the number of cores and amount of memory for your instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/create-instance#machine-types).   
**Data cache**  
Enable data cache | By default, the option to enable data cache is selected automatically for Cloud SQL for MySQL Enterprise Plus edition instances. If you don't want to enable data cache, then clear the **Enable data cache** checkbox. For more information about data cache, see [data cache](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#data-cache).   
**Storage**  
Storage type | Determines whether your instance uses SSD or HDD storage. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-type-2ndgen).   
Storage capacity | The amount of storage provisioned for the instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-capacity-2ndgen).   
Enable automatic storage increases | Determines whether Cloud SQL automatically provides more storage for your instance when free space runs low. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen).   
**Encryption**  
Google-managed encryption| The default option.  
Customer key-managed encryption key (CMEK)| Select to use your key with Google Cloud Key Management Service. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/cmek).  
**Connections**  
Private IP | Adds a private IP address for your instance. Choose either a [private services access](https://docs.cloud.google.com/sql/docs/mysql/about-private-services-access) connection, a [Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect) connection, or both for your instance. Your selection provides the private network connection for your instance. In all cases, additional configuration is required.   
  
To select and configure private services access, do the following:
     1. Select the **Private Services Access (PSA)** checkbox.
     2. From the **VPC network** drop-down menu, select the name of the network that your instance connects to.
     3. From the **Allocated IP range** drop-down menu, select **Automatic** or a specific named IP range from the drop-down menu.
For more information about configuring private services access, see [Configure private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access). Your instance can have both a public IP address and a private IP address. To select and configure Private Service Connect, do the following:
     1. Select the **Private Service Connect (PSC)** checkbox.
     2. Click **Add an Endpoint**.
     3. In the **Endpoint setup** section, do the following: 
        * In the **New Endpoint** card, select the project where you want to set up the endpoint from the **Project** drop-down.
        * Select a network for your endpoint from the **Network** drop-down.
        * If the Network Connectivity API isn't enabled yet, then click **Enable**.
     4. To set up the permissions for creating the service connection policy automatically, click **Confirm Network Setup**.
For more information about configuring Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect).
     * Learn more about [Private IP connection options](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#private-ip).
     * Learn more about [allocated IP address ranges](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated_ip_address_ranges).
**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following: 
     1. If you haven't already enabled the Cloud DNS API, [enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) for your Google Cloud project.
     2. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
     3. Add a private IP address to the instance.
     4. Specify an associated network for the instance.
     5. Optionally, specify an allocated IP range for the instance.  
Public IP | Adds a public IP address for your instance. You can then add authorized networks to connect to the instance. Your instance can have both a public and a private IP address. Learn more about using [public IP](https://docs.cloud.google.com/sql/docs/mysql/connect-overview#public_ip).  
Authorized networks| Add the name for the new network and the Network address. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks#authorized-networks).  
Allow Data API |  By selecting this checkbox, you let authorized users to call the [Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance) to execute SQL statements on the instance. For instances with Private IP only, this allows authorized users to call the Data API from the public internet.  
Enable private path |  By selecting this checkbox, you let other Google Cloud services, such as BigQuery, access data in Cloud SQL and make queries against this data over a private connection. **Note:** This checkbox is enabled only if you select the **Private IP** check box, and you add or select an authorized network to create a private connection.  
Enable Managed Connection Pooling |  By selecting this checkbox, you enable Managed Connection Pooling for your instance. Managed Connection Pooling lets you scale your workloads by optimizing resource utilization and connection latency Cloud SQL instances using pooling and multiplexing. For more information about Managed Connection Pooling, see [Managed Connection Pooling overview](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling).  
**Security**  
Server certificate authority mode  |  Choose the type of certificate authority (CA) that signs the server certificate for this Cloud SQL instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies). By default, when you create an instance in Google Cloud console, the instance uses the **Google managed internal certificate authority** (`GOOGLE_MANAGED_INTERNAL_CA`), which is the per-instance CA option.  
Automatic server certificate rotation  |  If you select either the Google-managed CAS certificate authority (CA) (`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CAS internal certificate authority (`CUSTOMER_MANAGED_CAS_CA`) option as the server CA mode for the instance, then you can choose whether to rotate the server certificate for the instance automatically. For more information about rotating Cloud SQL server certificates automatically, see [ Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#automatic-server-certificate-rotation-cas). By default, this option is disabled.  
**Data protection**  
Backup tier | The [backup option](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options) of your instance. You can choose between [enhanced backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options#enhanced-backups) and [standard backups](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backup-options#standard-backups).   
Automate backups | The window of time when you would like backups to start. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#backups-and-binary-logging-2ndgen).   
Choose where to store your backups| Select Multi-region for most use cases. If you need to store backups in a specific region, for example, if there are regulatory reasons to do so, select Region and select your region from the Location drop-down menu.  
Choose how many automated backups to store| The number of automated backups you would like to retain (from 1 to 365 days). [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#backup-retention).   
Enable point-in-time recovery | Enables point-in-time recovery and write-ahead logging. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#backups-and-binary-logging-2ndgen). **Note:** To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations. PITR is enabled by default during instance creation in the following conditions: In **Cloud SQL Enterprise Plus edition** :
     * PITR is enabled by default, regardless of how you create the instance.
In **Cloud SQL Enterprise edition** :
     * If you create the instance in Google Cloud console, PITR is enabled by default.
     * If you create the instance using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or Cloud SQL Admin API, then PITR is disabled by default. In this case, you must enable PITR manually if you want to use it.  
Enable deletion protection | Determines whether to protect an instance against accidental deletion. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection).   
Enable retained backups after instance deletion | Determines whether automated and on-demand backups are retained after an instance is deleted. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retained-backups).   
Choose how many days of logs to retain | Configure write-ahead log retention from 1 to 7 days. The default setting is 7 days. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#transaction-log-retention).   
**Maintenance**  
Preferred window | Determines a one-hour window when Cloud SQL can perform disruptive maintenance on your instance. If you do not set the window, then disruptive maintenance can be done at any time. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-window-2ndgen).   
Order of updates | Your preferred timing for instance updates, relative to other instances in the same project. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen).   
**Flags**  
ADD FLAG | You can use database flags to control settings and parameters for your instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/flags).   
**Query insights**  
Enable Query insights |  By selecting this checkbox, you enable query insights for your instance. Query insights provides you with detailed information about your database queries, including query performance, query text, and query execution plans. After you select query insights, you can enable additional features that are associated with query insights. For more information about these features and query insights, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights).  
Performance capture |  When you select the **Enable Query insights** checkbox, you also enable MySQL performance capture automatically. If you don't want to enable MySQL performance capture, then clear the **Performance capture** checkbox. You can enable or disable MySQL performance capture for an existing instance at a later time by updating the instance settings. For more information about MySQL performance capture, see [ Cloud SQL performance capture overview](https://docs.cloud.google.com/sql/docs/mysql/performance-capture).  
**Labels**  
ADD LABEL| Add a key and value for each label that you add. You use labels to help organize your instances.  
  13. Click **Create Instance**. 

Note: It might take a few minutes to create your instance. However, you can [view information about the instance](https://docs.cloud.google.com/sql/docs/mysql/instance-info) while it's being created.




### gcloud

For information about installing and getting started with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), see [Installing gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see the [Cloud Shell documentation](https://docs.cloud.google.com/shell/docs/starting-cloud-shell).

  1. Use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create the instance:
**Note** : If you specify MySQL 8.4 or MySQL 9.7 for the database version (or don't specify a database version at all) and don't specify an edition, then the default Cloud SQL edition of the instance is Enterprise Plus.

For Cloud SQL Enterprise Plus edition instances:
    
    gcloud sql instances create INSTANCE_NAME \
        --region=REGION \
        --tier=TIER \
        --database-version=DATABASE_VERSION \
        --edition=ENTERPRISE_PLUS
        

**Note** : If you specify a database version earlier than MySQL 8.4 and you don't specify an edition, then the default Cloud SQL edition of the instance is Enterprise. If you specify MySQL 8.4 for the database version, but the region you specify doesn't support Cloud SQL Enterprise Plus edition, then you must specify a [region that supports Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#editions-regions), or create an Cloud SQL Enterprise edition instance instead.

For Cloud SQL Enterprise edition instances:
    
    gcloud sql instances create INSTANCE_NAME \
        --cpu=NUMBER_CPUS \
        --memory=MEMORY_SIZE \
        --region=REGION
        

Or, alternatively, you can use the `--tier` flag if you choose `db-f1-micro` or `db-g1-small` as the machine type: 
    
    gcloud sql instances create INSTANCE_NAME \
          --tier=API_TIER_STRING \
          --region=REGION
      

There are restrictions on the values for vCPUs and memory size:

     * vCPUs must be either 1 or an even number between 2 and 96.
     * Memory must be: 
       * 0.9 to 6.5 GB per vCPU
       * A multiple of 256 MB
       * At least 3.75 GB (3840 MB)

For example, the following command creates a Cloud SQL Enterprise edition instance with two vCPUs and 7,680 MB of memory:
    
    gcloud sql instances create myinstance \
      --database-version=MYSQL_8_0 \
      --cpu=2 \
      --memory=7680MB \
      --region=us-central1
      

The following command creates a Cloud SQL Enterprise Plus edition instance with four cores:
    
    gcloud sql instances create myinstance \
      --database-version=MYSQL_8_0_31 \
      --tier=db-perf-optimized-N-4 \
      --edition=ENTERPRISE_PLUS \
      --region=us-central1
      

The default value for REGION is `us-central1`.

Don't include sensitive or personally identifiable information in your instance name; it is externally visible.   
You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

If you are creating an instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability), you can specify both the primary and secondary zones, using the `--zone` and `--secondary-zone` parameters. The following conditions apply when the secondary zone is used during instance creation or edit:

     * The zones must be valid zones.
     * If the secondary zone is specified, the primary must also be specified.
     * If the primary and secondary zones are specified, they must be distinct zones.
     * If the primary and secondary zones are specified, they must belong to the same region.

You can add more [parameters](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) to determine other instance settings:

Setting | Parameter | Notes  
---|---|---  
**Required parameters**  
Database version | `--database-version` | The [database version](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen), which is based on your Cloud SQL edition.  
Region | `--region` | [ See valid values](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#region-values). **Note:** Some organizations use an organization policy to restrict resource locations. If this type of policy affects your project, you can only select regions the organization policy allows. In the **Location** drop-down menu in the Console, the locations that are not allowed are unavailable. [Learn more](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).   
**Set password policy**  
Enable password policy | `--enable-password-policy` | Enables the password policy when used. By default, the password policy is disabled. When disabled using the `--clear-password-policy` parameter, the other password policy parameters are reset. Note: When you enable a password policy, statements that create users or change user passwords can cause additional latency due to password policy verification.  
Minimum length | `--password-policy-min-length` | Specifies the minimum number of characters that the password must have.  
Password complexity | `--password-policy-complexity` | Enables the password complexity check to ensure that the password contains one of each of these types of characters: lowercase, uppercase, numeric, and non-alphanumeric. Set the value to `COMPLEXITY_DEFAULT`.  
Restrict password reuse | `--password-policy-reuse-interval` | Specifies the number of previous passwords that you can't reuse. Supported only on Cloud SQL for MySQL 8.0 and later.  
Disallow username | `--password-policy-disallow-username-substring` | Prevents the use of the username in the password. Use the `--no-password-policy-disallow-username-substring` parameter to disable the check.  
**Connectivity**  
Managed Connection Pooling | `--enable-connection-pooling` | Enables [Managed Connection Pooling](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling) in the new instance. You can configure advanced Managed Connection Pooling settings after your instance is created. **Note:** This feature is only available for Cloud SQL Enterprise Plus edition instances that are configured to meet Managed Connection Pooling [requirements.](https://docs.cloud.google.com/sql/docs/mysql/managed-connection-pooling#requirements)  
Private IP |  **Private services access** `--network` `--no-assign-ip` (optional) `--allocated-ip-range-name` (optional) `--enable-google-private-path` (optional)   
  
**Private Service Connect** `--no-assign-ip` `--enable-private-service-connect` `--allowed-psc-projects` `--psc-auto-connections` `--enable-psc-auto-connection-policy` | `--network`: specifies the name of the VPC network you want to use for this instance. Private services access must already be configured for the network. On new or empty projects, you must enable `servicenetworking.googleapis.com`, allocate an IP range, and configure VPC Network Peering before creating the instance. Available only for the beta command (`gcloud beta sql instances create`). `--no-assign-ip`: Instance will only have a private IP address. `--allocated-ip-range-name`: if specified, sets a range name for which an IP range is allocated. For example, `google-managed-services-default`. The range name should comply with `RFC-1035` and be within 1-63 characters. (`gcloud alpha sql instances create`). `--enable-google-private-path`: if you use this parameter, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private connection. This parameter is valid only if:
     * You use the `--no-assign-ip` parameter.
     * You use the `--network` parameter to specify the name of the VPC network that you want to use to create a private connection.
**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following: 
     1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
     2. Add a private IP address to the instance.
     3. Specify an associated network for the instance.
     4. Optionally, specify an allocated IP range for the instance.
For Cloud SQL instances that use Private Service Connect for private IP connections, use the following flags: `--enable-private-service-connect`: enables private network connections to the Cloud SQL instance using Private Service Connect. For more information, see [Overview of Private Service Connect in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect). `--allowed-psc-projects`: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances. `--psc-auto-connections`: if you're setting up endpoints automatically for a Cloud SQL instance, then use the flag to specify the consumer networks and projects for the Private Service Connect endpoints. `--enable-psc-auto-connection-policy`: if specified, Google Cloud creates or updates a service connection policy in the consumer network and project for the Private Service Connect endpoint. For more information about configuring Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect).  
Data API Access | `--data-api-access` | Controls connectivity to the instance using [Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance). It's disallowed by default. Set the value to `ALLOW_DATA_API` to let users use the Data API to connect to the instance. For instances configured with a private IP address only, authorized users can call the Data API on the instance from the public internet. Set the value to `DISALLOW_DATA_API` to disallow using the Data API.   
Public IP | `--authorized-networks` | For public IP connections, only connections from authorized networks can connect to your instance. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/configure-ip).   
SSL Enforcement  |  `--ssl-mode` `--require-ssl` | The `ssl-mode` parameter enforces the SSL/TLS enforcement for the connections. For more information, see [Settings for Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#ssl-mode). The `require-ssl` parameter determines whether SSL connections over IP are enforced or not. `require-ssl` is a legacy parameter. Use `ssl-mode` instead. For more information, see [IpConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#ipconfiguration).  
Server CA mode | `--server-ca-mode` | The `--server-ca-mode` flag configures the type of [server certificate authority (CA)](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) for an instance. You can select one of the following options:
     * `GOOGLE_MANAGED_INTERNAL_CA`: this is the default value. With this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance.
     * `GOOGLE_MANAGED_CAS_CA`: with this option, a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service) is used. The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. This option is supported only on MySQL 8.0.30 and later. 
     * `CUSTOMER_MANAGED_CAS_CA`: with this option, you define the CA hierarchy and manage the rotation of the CA certificates. You create a CA pool in CA Service in the same region of your instance. One of the CAs in the pool is used to sign the server certificate. This option is supported only on MySQL 8.0.30 and later. For more information, see [Use a customer-managed CA](https://docs.cloud.google.com/sql/docs/mysql/customer-managed-ca).  
Automatic server certificate rotation | `--server-certificate-rotation-mode` | The `--server-certificate-rotation-mode` flag configures the type of server certificate rotation mode of the instance. You can select one of the following options:
     * `NO_AUTOMATIC_ROTATION`: this is the default value. With this option, there won't be no automatic server certificate rotation. Server certificates must be rotated manually.
     * `AUTOMATIC_ROTATION_DURING_MAINTENANCE`: With this option, automatic server certificate rotation is enabled during Cloud SQL scheduled maintenance or self-service maintenance updates. Requires `server_ca_mode` to be `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA`.   
Network architecture | [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create#--enforce-new-sql-network-architecture) | Enforce the use of the new network architecture for the instance upon creation. Using this flag when you create an instance before that project has been fully upgraded to the new network architecture can lead to IP address overconsumption or a failure to create instances if there aren't sufficient IP addresses remaining in the allocated IP range. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).   
**Machine type and storage**  
Machine type | `--tier` | Used to specify a shared-core instance (`db-f1-micro` or `db-g1-small`). For a custom instance configuration, use the `--cpu` or `--memory` parameters instead. See [Choose a machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview) for possible configurations.   
Storage type | `--storage-type` | Determines whether your instance uses SSD or HDD storage. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-type-2ndgen).   
Storage capacity | `--storage-size` | The amount of storage provisioned for the instance, in GB. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-capacity-2ndgen).   
Automatic storage increase | `--storage-auto-increase` | Determines whether Cloud SQL automatically provides more storage for your instance when free space runs low. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen).   
Automatic storage increase limit | `--storage-auto-increase-limit` | Determines how large Cloud SQL can automatically grow storage, in GB. The default value is `unlimited`, which allows storage to grow up to the maximum available storage for the instance tier. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-limit-2ndgen).   
Data cache (optional) | `--enable-data-cache` | Enables or deactivates the data cache for instances. For more information, see [data cache](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#data-cache).   
**Automatic backups and high availability**  
High availability | `--availability-type` | For a highly-available instance, set to `REGIONAL`. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/configure-ha).   
Secondary zone | `--secondary-zone` | If you're creating an instance for [high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability), you can specify both the primary and secondary zones using the `--zone` and `--secondary-zone parameters`. The following restrictions apply when the secondary zone is used during instance creation or edit: 
     * The zones must be valid zones.
     * If the secondary zone is specified, the primary must also be specified.
If the primary and secondary zones are specified, they must be distinct zones. If the primary and secondary zones are specified, they must belong to the same region. | Automatic backups | `--backup-start-time` | The window of time when you would like backups to start. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#backups-and-binary-logging-2ndgen).   
Retention settings for automated backups | `--retained-backups-count` | The number of automated backups to retain. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention).  
Binary logging | `--enable-bin-log` | Binary logging enables replication and point-in-time recovery. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#backups-and-binary-logging-2ndgen).   
Retention settings for binary logging | `--retained-transaction-log-days` | The number of days to retain binary logs for point-in-time recovery. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#retention).  
Point-in-time recovery | `--enable-point-in-time-recovery` |  Enables point-in-time recovery and write-ahead logging. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#backups-postgres).   
**Note:** To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations. PITR is enabled by default during instance creation in the following conditions: In **Cloud SQL Enterprise Plus edition** :
     * PITR is enabled by default, regardless of how you create the instance.
In **Cloud SQL Enterprise edition** :
     * If you create the instance in the Google Cloud console, PITR is enabled by default.
     * If you create the instance using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the Cloud SQL Admin API, then PITR is disabled by default, and you must enable PITR manually to use it.  
**Add database flags**  
Database flags | `--database-flags` | You can use database flags to control settings and parameters for your instance. [Learn more about database flags](https://docs.cloud.google.com/sql/docs/mysql/flags). [Learn more about how to format this parameter](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create).   
**Maintenance schedule**  
Maintenance window | `--maintenance-window-day`,   
`--maintenance-window-hour` | Determines a one-hour window when Cloud SQL can perform disruptive maintenance on your instance. If you don't set the window, then disruptive maintenance can be done at any time. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-window-2ndgen).   
Maintenance timing | `--maintenance-release-channel` | Your preferred timing for instance updates, relative to other instances in the same project. Use `preview` for earlier updates, and `production` for later updates. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#maintenance-timing-2ndgen).   
**Automatic minor version upgrade**  
Enable automatic minor version upgrade | `--enable-auto-upgrade-minor-version` | For MySQL 8.0 instances that you specify a minor version of 8.0.35 or later, for example `--database-version=MYSQL_8_0_35`. Enable [automatic minor version upgrades](https://docs.cloud.google.com/sql/docs/mysql/upgrade-minor-db-version#auto-upgrade) to the [default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support) of Cloud SQL for MySQL 8.0 during each [regular scheduled maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance). If you create your instance without specifying a minor version (`--database-version=MYSQL_8_0`), then automatic minor version upgrades are enabled for your instance by default. **Caution** : After the instance is created, you can't disable automatic minor version upgrade.  
**[Query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)**  
| `--insights-config-query-insights-enabled` | Enables query insights to provide query and query plan analytics.   
| `--insights-config-enhanced-query-insights-enabled` | Enables enhanced query insights for Cloud SQL Enterprise Plus edition to provide more detailed query analytics.  
| `--performance-capture-config` | Use this flag to configure MySQL performance capture settings for your MySQL instance. When you enable query insights or enhanced query insights, you also enable MySQL performance capture with default trigger conditions.  
  
You can configure or disable performance capture with the `--performance-capture-config` flag in the same create command or by updating the instance later. For more information, see [Configure MySQL performance capture](https://docs.cloud.google.com/sql/docs/mysql/configure-performance-capture).   
**Custom SAN**  
Add a custom subject alternative name (SAN) | `--custom-subject-alternative-names=DNS_NAMES` |  If you want to use a custom DNS name to connect to a Cloud SQL instance instead of using an IP address, then configure the custom subject alternative name (SAN) setting while creating the instance. The custom DNS name that you insert into the custom SAN setting is added to the SAN field of the server certificate of the instance. This lets you use the custom DNS name with hostname validation securely.  Before you can use the custom DNS name in your clients and applications, you must set up the mapping between the DNS name and the IP address. This is known as _DNS resolution_. You can add a comma-separated list of up to three custom DNS names to the custom SAN setting. **Note:** This feature is available for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#ca-hierarchies) instances only. To create the instance, you must use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command.  
  2. Note the automatically assigned IP address. 

If you are not using the Cloud SQL Auth Proxy, you will use this address as the host address that your applications or tools use to connect to the instance.

  3. Set the password for the "root@%" MySQL user: 
         
         gcloud sql users set-password root \
               --host=% \
               --instance INSTANCE_NAME \
               --password PASSWORD
               




### Terraform

To create an instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "mysql_pvp_instance_name" {
      name             = "mysql-pvp-instance-name"
      region           = "asia-northeast1"
      database_version = "MYSQL_8_0"
      root_password    = "abcABC123!"
      settings {
        tier = "db-f1-micro"
        password_validation_policy {
          min_length                  = 6
          complexity                  = "COMPLEXITY_DEFAULT"
          reuse_interval              = 2
          disallow_username_substring = true
          enable_password_policy      = true
        }
      }
      # set `deletion_protection` to true, will ensure that one cannot accidentally delete this instance by
      # use of Terraform whereas `deletion_protection_enabled` flag protects this instance at the GCP level.
      deletion_protection = false
    }

#### Apply the changes

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

  1. Launch [Cloud Shell](https://shell.cloud.google.com/).
  2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
         
         export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.




## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

  1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
         
         mkdir DIRECTORY && cd DIRECTORY && touch main.tf

  2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

  3. Review and modify the sample parameters to apply to your environment.
  4. Save your changes.
  5. Initialize Terraform. You only need to do this once per directory. 
         
         terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
         
         terraform init -upgrade




## Apply the changes

  1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
         
         terraform plan

Make corrections to the configuration as necessary.

  2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply

Wait until Terraform displays the "Apply complete!" message.

  3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 

**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 

#### Delete the changes

To delete your changes, do the following:

  1. To disable deletion protection, in your Terraform configuration file set the `deletion_protection` argument to `false`. 
         
         deletion_protection =  "false"

  2. Apply the updated Terraform configuration by running the following command and entering `yes` at the prompt: 
         
         terraform apply



  3. Remove resources previously applied with your Terraform configuration by running the following command and entering `yes` at the prompt:
         
         terraform destroy




### REST v1

**Prerequisites for Private IP using private services access on new projects:**

The following API request configures the instance to use private IP (`ipConfiguration.privateNetwork`). Before you create an instance that uses a private IP address using private services access in a new or empty project, you must ensure that the Service Networking API is enabled and that VPC Network Peering is configured for your VPC network. Otherwise, instance creation will fail with `SERVICE_NETWORKING_NOT_ENABLED` or `NETWORK_NOT_PEERED`.

Run the following `gcloud` commands to set up the prerequisites:

  1. **Enable the Service Networking API and the Compute Engine API:**
         
         gcloud services enable   
             sqladmin.googleapis.com   
             compute.googleapis.com   
             servicenetworking.googleapis.com   
             --project=PROJECT_ID
             

  2. **Allocate an IP address range for VPC Network Peering:**
         
         gcloud compute addresses create google-managed-services-default   
             --global   
             --purpose=VPC_PEERING   
             --prefix-length=16   
             --network=projects/PROJECT_ID/global/networks/default   
             --project=PROJECT_ID
             

  3. **Establish the private connection (VPC Network Peering):**
         
         gcloud services vpc-peerings connect   
             --service=servicenetworking.googleapis.com   
             --ranges=google-managed-services-default   
             --network=default   
             --project=PROJECT_ID
             




For more details, see [Configure private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access).

#### Create the instance

This example creates an instance. Some optional parameters, such as backups and binary logging are also included. For a complete list of parameters for this call, see the [Instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert) page. For information about instance settings, including valid values for region, see [Instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen). 

Don't include sensitive or personally identifiable information in your instance ID; it is externally visible.   
You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: your instance ID
  * DATABASE_VERSION: the database version. For example: `MYSQL_9_7`, `MYSQL_8_4` or `MYSQL_8_0_37`. If you don't specify a database version, the default database version is `MYSQL_8_4`.
  * REGION: the region
  * MACHINE_TYPE: your machine type
  * EDITION_TYPE: your Cloud SQL edition **Note** : If you specify `MYSQL_8_4` or `MYSQL_9_7` for the database version (or don't specify a database version) and don't specify an edition type, then the default Cloud SQL edition of the instance is `ENTERPRISE_PLUS`. If you specify a database version earlier than MySQL 8.4 and don't specify an edition type, then the default Cloud SQL edition of the instance is `ENTERPRISE`. If you specify `MYSQL_8_4` for the database version (or don't specify a database version), but the region you specify doesn't support Cloud SQL Enterprise Plus edition, then you must specify a [region that supports Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#editions-regions), or create an Cloud SQL Enterprise edition instance instead..
  * DATA_CACHE_ENABLED: (optional) set to `true` to enable data cache for your instance
  * PRIVATE_NETWORK: specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network. 

Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following:

    1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
    2. Add a private IP address to the instance.
    3. Specify an associated network for the instance.
    4. Optionally, specify an allocated IP range for the instance.
  * AUTHORIZED_NETWORKS: for public IP connections, specify the connections from authorized networks that can connect to your instance.
  * CA_MODE: specify a [certificate authority hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) for the instance, either `GOOGLE_MANAGED_INTERNAL_CA` or `GOOGLE_MANAGED_CAS_CA`. If you don't specify `serverCaMode`, then the default configuration is `GOOGLE_MANAGED_INTERNAL_CA`. This feature is in [Preview](https://cloud.google.com/products#launch-stages).
  * SERVER_CERTIFICATE_ROTATION_MODE: For automatic server certificate rotation for 
  * SERVER_CERTIFICATE_ROTATION_MODE: for automatic server certificate rotation for your instance, specify `AUTOMATIC_ROTATION_DURING_MAINTENANCE`. If you don't specify `serverCertificateRotationMode`, then the default configuration is `NO_AUTOMATIC_ROTATION`.
  * DNS_NAMES: add a comma-separated list of up to three DNS names to the [server certificate](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance) of your Cloud SQL instance. You can secure multiple DNS names with a single certificate. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) and for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) instances only.



**Note:** For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

If you set the `enablePrivatePathForGoogleCloudServices` parameter to `true`, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private connection. By setting this parameter to `false`, other Google Cloud services can't access data in Cloud SQL over a private connection.

If you set `dataApiAccess` to `ALLOW_DATA_API`, then you allow authorized users to use [Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance) to connect to your instance. For Private IP only instances, this allows authorized users to connect from the public internet.

To set a password policy while creating an instance, include the [passwordValidationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#passwordValidationPolicy) object in the request. Set the following parameters, as required: 

  * `enablePasswordPolicy`: enables the password policy when set to `true`.

To remove the password policy, you can use a `PATCH` request with `null` as the value for `enablePasswordPolicy`. In this case, the other password policy parameters are reset. 

**Note:** When you enable a password policy, statements that create users or change user passwords can cause additional latency due to password policy verification.
  * `minLength`: specifies the minimum number of characters that the password must have.
  * `complexity`: checks if the password is a combination of lowercase, uppercase, numeric, and non-alphanumeric characters. The default value is `COMPLEXITY_DEFAULT`.
  * `reuseInterval`: specifies the number of previous passwords that you can't reuse. 

Supported only on Cloud SQL for MySQL 8.0 and later. 

  * `disallowUsernameSubstring`: prevents the use of the username in the password when set to `true`.



You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

To configure the instance for query insights, make the appropriate replacements in the `insightsConfig` section:

  * QUERY_INSIGHTS_ENABLED: set to `true` to enable query insights for your instance.
  * RECORD_CLIENT_ADDRESS: set to `true` to store the client IP addresses where queries are coming from and helps you group that data to run metrics against it. Queries come from more than one host. Reviewing graphs for queries from client IP addresses can help identify the source of a problem.
  * RECORD_APPLICATION_TAGS: set to `true` to store application tags that help you determine the APIs and model-view-controller (MVC) routes that are making requests and group the data to run metrics against it. This option requires you to comment queries with a specific set of tags. You can do this by using the sqlcommenter open source object-relational mapping (ORM) auto-instrumentation library. This information helps Query Insights identify the source of a problem and the MVC the problem is coming from. Application paths help you with application monitoring.
  * QUERY_STRING_LENGTH: set to the query length limit in bytes, Sets the default query length limit. Higher query lengths are more useful for analytical queries, but they also require more memory. Changing the query length requires you to restart the instance. You can still add tags to queries that exceed the length limit. For Cloud SQL Enterprise edition, you can specify a value in bytes from `256` to `4500`. The default query length is `1024` bytes. For Cloud SQL Enterprise Plus edition, you can specify a limit in bytes from `1` to `1048576`. The default value is `1024` bytes (1 KB). 
  * QUERY_PLANS_PER_MINUTE: set to the number of query plans to capture per minute. By default, a maximum of 5 executed query plan samples are captured per minute across all databases on the instance. Increasing the sampling rate is likely to give you more data points but might add a performance overhead. To disable sampling, set this value to `0`. For Cloud SQL Enterprise edition, you can change the value from 0 to 20. For Cloud SQL Enterprise Plus edition, you can increase the maximum up to 200 to provide more data points. 
  * ENABLE_ENHANCED_QUERY_INSIGHTS_ENABLED: set to `true` to enable enhanced query insights for your instance.




For the `performanceCaptureConfig` field, include the following flag settings. If you don't set values for the flags, then the monitoring agent uses the default values for the thresholds. For more detailed information about the triggers set by these flags, see [Performance capture triggers](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#performance-capture-triggers).

  * PERFORMANCE_CAPTURE_ENABLED: set to `false` to disable MySQL performance capture for your instance. If `queryInsightsEnabled` is set to `true`, then performance capture is enabled automatically and applies the default values to threshold-based trigger conditions.
  * PROBING_INTERVAL_SECONDS: an integer between `30` and `86400`. The time interval, in seconds, between metric probes. Default is `30`.
  * PROBE_THRESHOLD: the number of consecutive times a threshold must be exceeded to trigger a performance capture. Valid range is `1` to `20`. Default is `3`.
  * RUNNING_THREADS_THRESHOLD: for primary instances, the minimum number of active threads considered to be over the threshold. For example, `10`. Must be greater than or equal to `10`. If not set, then the default is based on the size of the instance. Default is `MIN(600, cpuCount * 20)`. This default is either `600` or the number of vCPUs on the instance multiplied by `20`, whichever is smaller.
  * SECONDS_BEHIND_SOURCE_THRESHOLD: for read replicas, the minimum replication lag, in seconds, considered to be over the threshold. Must be greater than `1`. Default is `900`.
  * TRANSACTION_DURATION_THRESHOLD: the duration, in seconds, of an uncommitted transaction before the transaction is tracked and included in a performance capture log. For example, `300`. Minimum value is `60`. Default is `3600`.
  * SECONDS: the duration, in seconds, of the long-running transactions to be ended automatically. This limit can't be set to a value less than the value you set for the `transactionDurationThreshold` (TRANSACTION_DURATION_THRESHOLD) parameter.
  * TRANSACTION_TYPE: determines the categories of transactions to end. Possible values are: 
    * `READ_ONLY_TRANSACTIONS`: ends only read-only or `SELECT` queries. This is the default if `transactionKillType` is unspecified.
    * `ALL_TRANSACTIONS`: ends any running query that exceeds the threshold, including queries with write operations. This includes `INSERT`, `UPDATE`, `DELETE`, and other `DDL` statements.
  * EXCLUSION_LIST: a list of strings to exempt. You can provide the entries as `user@host` or a standalone user, which defaults to `user@%`. The list supports the wildcards `%` and `_` for matching in the host portion.
  * CPU_UTILIZATION_THRESHOLD_PERCENT: the overall CPU usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * MEMORY_USAGE_THRESHOLD_PERCENT: the overall memory usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT: the threshold for transactions that are allowed to be in a `LOCK WAIT` state. For example, `50`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * SEMAPHORE_WAIT_THRESHOLD_COUNT: the threshold for the number of threads waiting on InnoDB semaphores from the `SHOW ENGINE INNODB STATUS` command. For example, `20`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * HISTORY_LIST_LENGTH_THRESHOLD_COUNT: the threshold for the InnoDB History List Length (HLL) count that's allowed for the database. For example, `100000`. Minimum value is `10000` and the maximum is `10000000`. Default is `0`, which is disabled.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "dataCacheConfig": {
          "dataCacheEnabled": DATA_CACHE_ENABLED
        },
        "backupConfiguration": {
          "binaryLogEnabled": true,
          "enabled": true
        },
        "passwordValidationPolicy": {
          "enablePasswordPolicy": true
          "minLength": "MIN_LENGTH",
          "complexity": COMPLEXITY_DEFAULT,
          "reuseInterval": "REUSE_INTERVAL",
          "disallowUsernameSubstring": "DISALLOW_USERNAME_SUBSTRING"
        },
        "ipConfiguration": {
          "privateNetwork": "PRIVATE_NETWORK",
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          "ipv4Enabled": false,
          "enablePrivatePathForGoogleCloudServices": true,
          "serverCaMode": "CA_MODE",
          "serverCertificateRotationMode": "SERVER_CERTIFICATE_ROTATION_MODE",
          "customSubjectAlternativeNames": "DNS_NAMES"
        },
        "dataApiAccess": "ALLOW_DATA_API",
        "insightsConfig" : {
           "queryInsightsEnabled" : QUERY_INSIGHTS_ENABLED,
           "recordClientAddress" : RECORD_CLIENT_ADDRESS,
           "recordApplicationTags" : RECORD_APPLICATION_TAGS,
           "queryStringLength" : QUERY_STRING_LENGTH,
           "queryPlansPerMinute" : QUERY_PLANS_PER_MINUTE,
           "enableEnhancedQueryInsightsEnabled": ENABLE_ENHANCED_QUERY_INSIGHTS_ENABLED
        },
        "performanceCaptureConfig": {
           "enabled": PERFORMANCE_CAPTURE_ENABLED,
           "probingIntervalSeconds": PROBING_INTERVAL_SECONDS,
           "probeThreshold": PROBE_THRESHOLD,
           "runningThreadsThreshold": RUNNING_THREADS_THRESHOLD,
           "secondsBehindSourceThreshold": SECONDS_BEHIND_SOURCE_THRESHOLD,
           "cpuUtilizationThresholdPercent": CPU_UTILIZATION_THRESHOLD_PERCENT,
           "memoryUsageThresholdPercent": MEMORY_USAGE_THRESHOLD_PERCENT,
           "transactionLockWaitThresholdCount": TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT,
           "semaphoreWaitThresholdCount": SEMAPHORE_WAIT_THRESHOLD_COUNT,
           "historyListLengthThresholdCount": HISTORY_LIST_LENGTH_THRESHOLD_COUNT,
           "transactionDurationThreshold": TRANSACTION_DURATION_THRESHOLD,
           "transactionKillThresholdSeconds": SECONDS,
           "transactionKillType": TRANSACTION_TYPE,
           "transactionKillExcludedUserHosts": [ EXCLUSION_LIST
         ]
       },
      }
     "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE"
    }
    
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2019-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

The response is a [long-running operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/operations), which might take a few minutes to complete. 

#### Update the root password

When the instance finishes initializing, update the root password:

Before using any of the request data, make the following replacements: 

  * project-id: your project ID
  * instance-id: instance ID created in prior step
  * root-password: desired root password



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?host=%25&name=root

Request JSON body: 
    
    
    {
      "name": "root",
      "host": "%",
      "password": "root-password"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?host=%25&name=root"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id/users?host=%25&name=root" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2019-09-26T14:32:30.592Z",
      "startTime": "2019-09-26T14:32:30.594Z",
      "endTime": "2019-09-26T14:32:33.518Z",
      "operationType": "UPDATE_USER",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

#### Retrieve the IPv4 address

Retrieve the automatically assigned IPv4 address for the new instance:

Before using any of the request data, make the following replacements: 

  * project-id: your project ID
  * instance-id: instance ID created in prior step



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0_18",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "db-f1-micro",
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference": {
          "zone": "us-west1-a",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "backupConfiguration": {
          "startTime": "18:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "1",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      },
      "etag": "--redacted--",
      "ipAddresses": [
        {
          "type": "PRIMARY",
          "ipAddress": "10.0.0.1"
        }
      ],
      "serverCaCert": {
        ...
      },
      "instanceType": "CLOUD_SQL_INSTANCE",
      "project": "project-id",
      "serviceAccountEmailAddress": "redacted@gcp-sa-cloud-sql.iam.gserviceaccount.com",
      "backendType": "SECOND_GEN",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/project-id/instances/instance-id",
      "connectionName": "project-id:region:instance-id",
      "name": "instance-id",
      "region": "us-west1",
      "gceZone": "us-west1-a"
    }
    

Look for the `ipAddress` field in the response.

### REST v1beta4

**Prerequisites for Private IP using private services access on new projects:**

The following API request configures the instance to use private IP (`ipConfiguration.privateNetwork`). Before you create an instance that uses a private IP address using private services access in a new or empty project, you must ensure that the Service Networking API is enabled and that VPC Network Peering is configured for your VPC network. Otherwise, instance creation will fail with `SERVICE_NETWORKING_NOT_ENABLED` or `NETWORK_NOT_PEERED`.

Run the following `gcloud` commands to set up the prerequisites:

  1. **Enable the Service Networking API and the Compute Engine API:**
         
         gcloud services enable   
             sqladmin.googleapis.com   
             compute.googleapis.com   
             servicenetworking.googleapis.com   
             --project=PROJECT_ID
             

  2. **Allocate an IP address range for VPC Network Peering:**
         
         gcloud compute addresses create google-managed-services-default   
             --global   
             --purpose=VPC_PEERING   
             --prefix-length=16   
             --network=projects/PROJECT_ID/global/networks/default   
             --project=PROJECT_ID
             

  3. **Establish the private connection (VPC Network Peering):**
         
         gcloud services vpc-peerings connect   
             --service=servicenetworking.googleapis.com   
             --ranges=google-managed-services-default   
             --network=default   
             --project=PROJECT_ID
             




For more details, see [Configure private services access](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access).

#### Create the instance

This example creates an instance. Some optional parameters, such as backups and binary logging are also included. For a complete list of parameters for this call, see the [instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) page. For information about instance settings, including valid values for region, see [Instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#settings-2ndgen)

Don't include sensitive or personally identifiable information in your instance ID; it is externally visible.   
You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: your instance ID
  * DATABASE_VERSION: the database version. For example: `MYSQL_9_7`, `MYSQL_8_4` or `MYSQL_8_0_37`. If you don't specify a database version, the default database version is `MYSQL_8_4`.
  * REGION: the region
  * MACHINE_TYPE: your machine type
  * EDITION_TYPE: your Cloud SQL edition **Note** : If you specify `MYSQL_8_4` or `MYSQL_9_7` for the database version (or don't specify a database version) and don't specify an edition type, then the default Cloud SQL edition of the instance is `ENTERPRISE_PLUS`. If you specify a database version earlier than MySQL 8.4 and don't specify an edition type, then the default Cloud SQL edition of the instance is `ENTERPRISE`. If you specify `MYSQL_8_4` for the database version, but the region you selected doesn't support Cloud SQL Enterprise Plus edition, then you must specify a [region that supports Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/editions-intro#editions-regions), or create an Cloud SQL Enterprise edition instance instead.. 
  * DATA_CACHE_ENABLED: (optional) set to `true` to enable data cache for your instance
  * PRIVATE_NETWORK: specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.
  * CA_MODE: specify a [certificate authority hierarchy](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) for the instance, either `GOOGLE_MANAGED_INTERNAL_CA` or `GOOGLE_MANAGED_CAS_CA`. If you don't specify `serverCaMode`, then the default configuration is `GOOGLE_MANAGED_INTERNAL_CA`. This feature is in [Preview](https://cloud.google.com/products#launch-stages).
  * SERVER_CERTIFICATE_ROTATION_MODE: For automatic server certificate rotation for your instance, specify `AUTOMATIC_ROTATION_DURING_MAINTENANCE`. If you don't specify `serverCertificateRotationMode`, then the default configuration is `NO_AUTOMATIC_ROTATION`.
  * DNS_NAMES: add a comma-separated list of up to three DNS names to the [server certificate](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance) of your Cloud SQL instance. You can secure multiple DNS names with a single certificate. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) and for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/mysql/authorize-ssl#certificate_authority_ca_hierarchies) instances only.



You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated-ip).

**Note:** For the `ipv4Enabled` parameter, set the value to `true` if you're using a public IP address for your instance or `false` if your instance has a private IP address.

If you set the `enablePrivatePathForGoogleCloudServices` parameter to `true`, then you allow other Google Cloud services, such as BigQuery, to access data in Cloud SQL and make queries against this data over a private connection. By setting this parameter to `false`, other Google Cloud services can't access data in Cloud SQL over a private connection.

If you set `dataApiAccess` to `ALLOW_DATA_API`, then you allow authorized users to use the [Data API](https://docs.cloud.google.com/sql/docs/mysql/executesql-instance) to connect to and execute SQL statements on your instance. For Private IP-only instances, enabling Data API access lets authorized users connect and execute SQL statements from the public internet.

**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following: 

  1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
  2. Add a private IP address to the instance.
  3. Specify an associated network for the instance.
  4. Optionally, specify an allocated IP range for the instance.



To set a password policy while creating an instance, include the [passwordValidationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#passwordValidationPolicy) object in the request. Set the following parameters, as required: 

  * `enablePasswordPolicy`: Enables the password policy when set to `true`.

To remove the password policy, you can use a `PATCH` request with `null` as the value for `enablePasswordPolicy`. In this case, the other password policy parameters are reset. 

**Note:** When you enable a password policy, statements that create users or change user passwords can cause additional latency due to password policy verification.
  * `minLength`: Specifies the minimum number of characters that the password must have.
  * `complexity`: Checks if the password is a combination of lowercase, uppercase, numeric, and non-alphanumeric characters. The default value is `COMPLEXITY_DEFAULT`.
  * `reuseInterval`: Specifies the number of previous passwords that you can't reuse. 

Supported only on Cloud SQL for MySQL 8.0 and later. 

  * `disallowUsernameSubstring`: Prevents the use of the username in the password when set to `true`.



To configure the instance for query insights, make the appropriate replacements in the `insightsConfig` section:

  * QUERY_INSIGHTS_ENABLED: set to `true` to enable query insights for your instance.
  * RECORD_CLIENT_ADDRESS: set to `true` to store the client IP addresses where queries are coming from and helps you group that data to run metrics against it. Queries come from more than one host. Reviewing graphs for queries from client IP addresses can help identify the source of a problem.
  * RECORD_APPLICATION_TAGS: set to `true` to store application tags that help you determine the APIs and model-view-controller (MVC) routes that are making requests and group the data to run metrics against it. This option requires you to comment queries with a specific set of tags. You can do this by using the sqlcommenter open source object-relational mapping (ORM) auto-instrumentation library. This information helps Query Insights identify the source of a problem and the MVC the problem is coming from. Application paths help you with application monitoring.
  * QUERY_STRING_LENGTH: set to the query length limit in bytes, Sets the default query length limit. Higher query lengths are more useful for analytical queries, but they also require more memory. Changing the query length requires you to restart the instance. You can still add tags to queries that exceed the length limit. For Cloud SQL Enterprise edition, you can specify a value in bytes from `256` to `4500`. The default query length is `1024` bytes. For Cloud SQL Enterprise Plus edition, you can specify a limit in bytes from `1` to `1048576`. The default value is `1024` bytes (1 KB). 
  * QUERY_PLANS_PER_MINUTE: set to the number of query plans to capture per minute. By default, a maximum of 5 executed query plan samples are captured per minute across all databases on the instance. Increasing the sampling rate is likely to give you more data points but might add a performance overhead. To disable sampling, set this value to `0`. For Cloud SQL Enterprise edition, you can change the value from 0 to 20. For Cloud SQL Enterprise Plus edition, you can increase the maximum up to 200 to provide more data points. 
  * ENABLE_ENHANCED_QUERY_INSIGHTS_ENABLED: set to `true` to enable enhanced query insights for your instance.




For the `performanceCaptureConfig` section, include the following settings. If you don't set values for these instance settings, then performance capture uses the default values for the thresholds. For more detailed information about the thresholds set by the triggers, see [Performance capture triggers](https://docs.cloud.google.com/sql/docs/mysql/performance-capture#performance-capture-triggers).

  * PERFORMANCE_CAPTURE_ENABLED: set to `false` to disable MySQL performance capture for your instance. If `queryInsightsEnabled` is set to `true`, then MySQL performance capture is enabled automatically and applies the default values to threshold-basedvtrigger conditions.
  * PROBING_INTERVAL_SECONDS: an integer between `30` and `86400`. The time interval, in seconds, between metric probes. Default is `30`.
  * PROBE_THRESHOLD: the number of consecutive times a threshold must be exceeded to trigger a performance capture. Valid range is `1` to `20`. Default is `3`.
  * RUNNING_THREADS_THRESHOLD: for primary instances, the minimum number of active threads considered to be over the threshold. For example, `10`. Must be greater than or equal to `10`. If not set, then the default is based on the size of the instance. Default is `MIN(600, cpuCount * 20)`. This default is either `600` or the number of vCPUs on the instance multiplied by `20`, whichever is smaller.
  * SECONDS_BEHIND_SOURCE_THRESHOLD: for read replicas, the minimum replication lag, in seconds, considered to be over the threshold. Must be greater than `1`. Default is `900`.
  * TRANSACTION_DURATION_THRESHOLD: the duration, in seconds, of an uncommitted transaction before the transaction is tracked and included in a performance capture log. For example, `300`. Minimum value is `60`. Default is `3600`.
  * SECONDS: the duration, in seconds, of the long-running transactions to be ended automatically. This limit can't be set to a value less than the value you set for the `transactionDurationThreshold` (TRANSACTION_DURATION_THRESHOLD) parameter.
  * TRANSACTION_TYPE: determines the categories of transactions to end. Possible values are: 
    * `READ_ONLY_TRANSACTIONS`: ends only read-only or `SELECT` queries. This is the default if `transactionKillType` is unspecified.
    * `ALL_TRANSACTIONS`: ends any running query that exceeds the threshold, including queries with write operations. This includes `INSERT`, `UPDATE`, `DELETE`, and other `DDL` statements.
  * EXCLUSION_LIST: a list of strings to exempt. You can provide the entries as `user@host` or a standalone user, which defaults to `user@%`. The list supports the wildcards `%` and `_` for matching in the host portion.
  * CPU_UTILIZATION_THRESHOLD_PERCENT: the overall CPU usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * MEMORY_USAGE_THRESHOLD_PERCENT: the overall memory usage percentage to exceed consistently. For example, `90`. Minimum value is `10` and the maximum is `99`. Default is `0`, which is disabled.
  * TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT: the threshold for transactions that are allowed to be in a `LOCK WAIT` state. For example, `50`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * SEMAPHORE_WAIT_THRESHOLD_COUNT: the threshold for the number of threads waiting on InnoDB semaphores from the `SHOW ENGINE INNODB STATUS` command. For example, `20`. Minimum value is `10` and the maximum is `10000`. Default is `0`, which is disabled.
  * HISTORY_LIST_LENGTH_THRESHOLD_COUNT: the threshold for the InnoDB History List Length (HLL) count that's allowed for the database. For example, `100000`. Minimum value is `10000` and the maximum is `10000000`. Default is `0`, which is disabled.



HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "dataCacheConfig" {
          "dataCacheEnabled": DATA_CACHE_ENABLED
        },
        "backupConfiguration": {
          "binaryLogEnabled": true,
          "enabled": true
        },
        "passwordValidationPolicy": {
          "enablePasswordPolicy": true
          "minLength": "MIN_LENGTH",
          "complexity": COMPLEXITY_DEFAULT,
          "reuseInterval": "REUSE_INTERVAL",
          "disallowUsernameSubstring": "DISALLOW_USERNAME_SUBSTRING",
        },
        "ipConfiguration": {
          "privateNetwork": "PRIVATE_NETWORK",
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          "ipv4Enabled": false,
          "enablePrivatePathForGoogleCloudServices": true,
          "serverCaMode": "CA_MODE",
          "serverCertificateRotationMode": "SERVER_CERTIFICATE_ROTATION_MODE",
          "customSubjectAlternativeNames": "DNS_NAMES"
        },
        "dataApiAccess": "ALLOW_DATA_API",
        "insightsConfig": {
           "queryInsightsEnabled" : QUERY_INSIGHTS_ENABLED,
           "recordClientAddress" : RECORD_CLIENT_ADDRESS,
           "recordApplicationTags" : RECORD_APPLICATION_TAGS,
           "queryStringLength" : QUERY_STRING_LENGTH,
           "queryPlansPerMinute" : QUERY_PLANS_PER_MINUTE,
           "enableEnhancedQueryInsightsEnabled": ENABLE_ENHANCED_QUERY_INSIGHTS_ENABLED
        },
        
        "performanceCaptureConfig": {
           "enabled": PERFORMANCE_CAPTURE_ENABLED,
          "probingIntervalSeconds": PROBING_INTERVAL_SECONDS,
          "probeThreshold": PROBE_THRESHOLD,
          "runningThreadsThreshold": RUNNING_THREADS_THRESHOLD,
          "secondsBehindSourceThreshold": SECONDS_BEHIND_SOURCE_THRESHOLD,
          "cpuUtilizationThresholdPercent": CPU_UTILIZATION_THRESHOLD_PERCENT,
          "memoryUsageThresholdPercent": MEMORY_USAGE_THRESHOLD_PERCENT,
          "transactionLockWaitThresholdCount": TRANSACTION_LOCK_WAIT_THRESHOLD_COUNT,
          "semaphoreWaitThresholdCount": SEMAPHORE_WAIT_THRESHOLD_COUNT,
          "historyListLengthThresholdCount": HISTORY_LIST_LENGTH_THRESHOLD_COUNT,
          "transactionDurationThreshold": TRANSACTION_DURATION_THRESHOLD,
          "transactionKillThresholdSeconds": SECONDS,
          "transactionKillType": TRANSACTION_TYPE,
          "transactionKillExcludedUserHosts": [ EXCLUSION_LIST
         ]
        },
        
      },
      "sqlNetworkArchitecture": "NEW_NETWORK_ARCHITECTURE",
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "status": "PENDING",
      "user": "user@example.com",
      "insertTime": "2019-09-25T22:19:33.735Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

The response is a [long-running operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations), which might take a few minutes to complete. 

#### Update the root password

When the instance finishes initializing, update the root password: 

Before using any of the request data, make the following replacements: 

  * project-id: your project ID
  * instance-id: instance ID created in prior step
  * root-password: desired root password



HTTP method and URL: 
    
    
    PUT https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?host=%25&name=root

Request JSON body: 
    
    
    {
      "name": "root",
      "host": "%",
      "password": "root-password"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?host=%25&name=root"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id/users?host=%25&name=root" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#operation",
      "targetLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "status": "DONE",
      "user": "user@example.com",
      "insertTime": "2019-09-26T14:32:30.592Z",
      "startTime": "2019-09-26T14:32:30.594Z",
      "endTime": "2019-09-26T14:32:33.518Z",
      "operationType": "UPDATE_USER",
      "name": "operation-id",
      "targetId": "instance-id",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/operations/operation-id",
      "targetProject": "project-id"
    }
    

The response is a [long-running operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations), which might take a few minutes to complete. 

#### Retrieve the IPv4 address

Retrieve the automatically assigned IPv4 address for the new instance: 

Before using any of the request data, make the following replacements: 

  * project-id: your project ID
  * instance-id: instance ID created in prior step



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "MYSQL_8_0_18",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "db-f1-micro",
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference": {
          "zone": "us-west1-a",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "backupConfiguration": {
          "startTime": "18:00",
          "kind": "sql#backupConfiguration",
          "enabled": true,
          "binaryLogEnabled": true
        },
        "settingsVersion": "1",
        "storageAutoResizeLimit": "0",
        "storageAutoResize": true,
        "dataDiskSizeGb": "10"
      },
      "etag": "--redacted--",
      "ipAddresses": [
        {
          "type": "PRIMARY",
          "ipAddress": "10.0.0.1"
        }
      ],
      "serverCaCert": {
        ...
      },
      "instanceType": "CLOUD_SQL_INSTANCE",
      "project": "project-id",
      "serviceAccountEmailAddress": "redacted@gcp-sa-cloud-sql.iam.gserviceaccount.com",
      "backendType": "SECOND_GEN",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances/instance-id",
      "connectionName": "project-id:region:instance-id",
      "name": "instance-id",
      "region": "us-west1",
      "gceZone": "us-west1-a"
    }
    

Look for the `ipAddress` field in the response. 

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) is constructed for this task, see the [APIs Explorer on the instances:insert page](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert). 

### Generate the write endpoint

A write endpoint is a global domain name service (DNS) name that resolves to the IP address of the current primary instance automatically. This endpoint redirects incoming connections to the new primary instance automatically in case of a replica [failover or switchover](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas) operation. You can use the write endpoint in a SQL connection string instead of an IP address. By using a write endpoint, you can avoid having to make application connection changes when a region outage occurs.

For more information about using a write endpoint to connect to an instance, see [Connect to an instance using a write endpoint](https://docs.cloud.google.com/sql/docs/mysql/connect-to-instance-using-write-endpoint).

## Specify the database minor version for MySQL 8.0

You can specify the minor version of an existing MySQL 8.0 instance by using `gcloud` or the REST API.

### gcloud

Use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command with the `--database-version` flag.

Replace the following variables before running the command:

  * INSTANCE_NAME: The name of the instance.
  * DATABASE_VERSION: The database minor version of the instance: `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_8_0_27`, `MYSQL_8_0_28`, `MYSQL_8_0_30`, `MYSQL_8_0_31`, `MYSQL_8_0_32`, `MYSQL_8_0_33`, `MYSQL_8_0_34`, `MYSQL_8_0_35`, `MYSQL_8_0_36`, `MYSQL_8_0_37`, `MYSQL_8_0_39`, `MYSQL_8_0_40`, `MYSQL_8_0_41`, `MYSQL_8_0_42`, `MYSQL_8_0_43`, `MYSQL_8_0_44`, `MYSQL_8_0_45`, or `MYSQL_8_0_46` (default minor version for MySQL 8.0). If you specify `MYSQL_8_0`, the default minor version is used. 

If you don't specify this flag, then the default major version, `MYSQL_8_0`, is used.



    
    
    gcloud sql instances create INSTANCE_NAME \
    --database-version=DATABASE_VERSION

If you're creating a MySQL 8.0.35 or later instance, then you can enable automatic minor version upgrades by specifying the `--enable-auto-upgrade-minor-version` flag. When you enable automatic minor version upgrades, your instance is upgraded to the [default minor version](https://docs.cloud.google.com/sql/docs/mysql/db-versions#database-version-support) of Cloud SQL for MySQL 8.0 during its [regular scheduled maintenance update](https://docs.cloud.google.com/sql/docs/mysql/maintenance). This flag isn't available for MySQL 8.0.34 and earlier versions. 
    
    
    gcloud sql instances create INSTANCE_NAME \
    --database-version=DATABASE_VERSION \
    --enable-auto-upgrade-minor-version

For detailed information, see the documentation on [creating an instance by using `gcloud`](https://docs.cloud.google.com/sql/docs/mysql/create-instance#gcloud). 

### REST v1

Use a POST request with the [ instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances/insert) method and the `databaseVersion` flag. 
    
    
        POST https://sqladmin.googleapis.com/v1/projects/project-id/instances

Before using any of the request data, replace these variables: 

  * project_id: The ID of the project.
  * instance_id: The name of the instance.
  * databaseVersion: The database version of the instance: `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_8_0_27`, `MYSQL_8_0_28`, `MYSQL_8_0_30`, `MYSQL_8_0_31`, `MYSQL_8_0_32`, `MYSQL_8_0_33`, `MYSQL_8_0_34`, `MYSQL_8_0_35`, `MYSQL_8_0_36`, `MYSQL_8_0_37`, `MYSQL_8_0_39`, `MYSQL_8_0_40`, `MYSQL_8_0_41`, `MYSQL_8_0_42`, `MYSQL_8_0_43`, `MYSQL_8_0_44`, `MYSQL_8_0_45`, or `MYSQL_8_0_46` (default minor version for MySQL 8.0). If you specify `MYSQL_8_0`, as the version, then the default minor version is used. If you don't specify the `databaseVersion` flag, then the default major version, `MYSQL_8_0`, is used.



For detailed information, see the documentation about [ creating an instance by using the REST v1 API](https://docs.cloud.google.com/sql/docs/mysql/create-instance#rest-v1). 

### REST v1beta4

Use a POST request with the [ instances:insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert) method and the `databaseVersion` flag. 
    
    
      POST https://sqladmin.googleapis.com/sql/v1beta4/projects/project-id/instances

Before using any of the request data, replace these variables:

  * project_id: The ID of the project.
  * instance_id: The name of the instance.
  * databaseVersion: The database version of the instance: `MYSQL_8_0_18`, `MYSQL_8_0_26`, `MYSQL_8_0_27`, `MYSQL_8_0_28`, `MYSQL_8_0_30`, `MYSQL_8_0_31`, `MYSQL_8_0_32`, `MYSQL_8_0_33`. `MYSQL_8_0_34`, `MYSQL_8_0_35`, `MYSQL_8_0_36`, `MYSQL_8_0_37`, `MYSQL_8_0_39`, `MYSQL_8_0_40`, `MYSQL_8_0_41`, `MYSQL_8_0_42`, `MYSQL_8_0_43`, `MYSQL_8_0_44`, `MYSQL_8_0_45`, or `MYSQL_8_0_46` (default minor version for MySQL 8.0). If you specify `MYSQL_8_0`, then the default minor version is used. If you don't specify the `databaseVersion` flag, then the default major version, `MYSQL_8_0`, is used.



For detailed information, see the documentation about [ creating an instance by using the REST v1beta4 API](https://docs.cloud.google.com/sql/docs/mysql/create-instance#rest-v1beta4). 

### Database minor version for read replicas, clones, and PITR

When [creating a read replica](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica), you can specify the database minor version of the read replica. By default, new read replicas are created on the default minor version.

When [cloning an instance](https://docs.cloud.google.com/sql/docs/mysql/clone-instance#cloning-an-instance), the newly created instance has that same minor version as that of the source.

When [performing a point-in-time recovery](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#perform-pitr), the newly created instance has the same database minor version as that of the source.

## Machine types

Determines memory and virtual cores available for your Cloud SQL instance. You can configure machine types from different machine series. The availability of different machine series is determined by your Cloud SQL edition and region.

  * **For Cloud SQL Enterprise Plus edition instances:** Cloud SQL offers predefined machine types in these machine series:

    * [N2](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n2_machine_types) series.
    * [C4A](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4a) series.
    * [C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) series.
  * **For Cloud SQL Enterprise edition instances:** Cloud SQL offers both predefined and custom machine types in these machine series:

    * [general purpose - shared core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-shared-core) series.
    * [general purpose - dedicated core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-dedicated-core) series.
    * [N4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n4) series.



If you require real-time processing, such as online transaction processing (OLTP), make sure that your instance has enough memory to contain the entire working set. However, there are other factors that can impact memory requirements, such as number of active connections, and internal overhead processes. Perform load testing to avoid performance issues in your production environment.

When you configure your instance, select sufficient memory and vCPUs to handle your needs, and scale up your instance as your requirements increase. A machine configuration with insufficient vCPUs might lose its SLA coverage. For more information, see [Operational guidelines](https://docs.cloud.google.com/sql/docs/mysql/operational-guidelines).

For more information, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview).

## Troubleshoot

Issue | Troubleshooting | Error message: `The zone or region does not have sufficient resources to handle the request at the moment.` | The selected zone lacks capacity for the requested resources or the VM type at the time of the instance creation request. There might be simultaneous high operational demand in that specific regional location at the time of request. To resolve this issue, retry creating the instance in another zone or retry creating the instance in the same zone that received the error at a different time of day.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider`. | There are no more available addresses in the allocated IP range. There can be several possible scenarios: 

  * The size of the allocated IP range for the private service connection is smaller than /24.
  * The size of the allocated IP range for the private service connection is too small for the number of Cloud SQL instances.
  * The requirement on the size of allocated IP range will be larger if instances are created in multiple regions. See [allocated range size](https://docs.cloud.google.com/sql/docs/mysql/private-ip#allocated_range_size)

To resolve this issue, you can either expand the existing allocated IP range or allocate an additional IP range to the private service connection. For more information, see [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access#allocate-ip-address-range). If you used the `--allocated-ip-range-name` flag while creating the Cloud SQL instance, you may only expand the specified IP range. If you're allocating a new range, take care that the allocation doesn't overlap with any existing allocations. After creating a new IP range, update the vpc peering with the following command:
    
    
    gcloud services vpc-peerings update \
    --service=servicenetworking.googleapis.com \
    --ranges=OLD_RESERVED_RANGE_NAME,NEW_RESERVED_RANGE_NAME \
    --network=VPC_NETWORK \
    --project=PROJECT_ID \
    --force
        

If you're expanding an existing allocation, take care to increase only the allocation range and not decrease it. For example, if the original allocation was 10.0.10.0/24, then make the new allocation at least 10.0.10.0/23. In general, if starting from a /24 allocation, decrementing the /mask by 1 for each condition (additional instance type group, additional region) is a good rule of thumb. For example, if trying to create both instance type groups on the same allocation, going from /24 to /23 is enough.  After expanding an existing IP range, update the vpc peering with following command:
    
    
    gcloud services vpc-peerings update \
    --service=servicenetworking.googleapis.com \
    --ranges=RESERVED_RANGE_NAME \
    --network=VPC_NETWORK \
    --project=PROJECT_ID
          
  
Error message: `Failed to create subnetwork. Router status is temporarily unavailable. Please try again later. Help Token: [token-ID]`. | Try to create the Cloud SQL instance again.  
Error message: `HTTPError 400: Invalid request: Incorrect Service Networking config for instance: PROJECT_ID:INSTANCE_NAME:SERVICE_NETWORKING_NOT_ENABLED.` |  Enable the [Service Networking API](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/getting-started) using the following command and try to create the Cloud SQL instance again.
    
    
    gcloud services enable servicenetworking.googleapis.com \
    --project=PROJECT_ID
          
  
Error message: `Failed to create subnetwork. Required 'compute.projects.get' permission for PROJECT_ID`. | When you create an instance using with a Private IP address, a service account is created just-in-time using the Service Networking API. If you have only recently enabled the Service Networking API, then the service account might not get created and the instance creation fails. In this case, you must wait for the service account to propagate throughout the system or manually add it with the required permissions.  
Error message: `More than 3 subject alternative names are not allowed.` | You're trying to use a custom SAN to add more than three DNS names to the server certificate of a Cloud SQL instance. You can't add more than three DNS names to the instance.  
Error message: `Subject alternative names %s is too long. The maximum length is 253 characters.` | Make sure that any DNS names that you want to add to the server certificate of a Cloud SQL instance don't have more than 253 characters.  
Error message: `Subject alternative name %s is invalid.` | Verify that the DNS names that you want to add to the server certificate of a Cloud SQL instance meet the following criteria:

  * They don't have wildcard characters.
  * They don't have trailing dots.
  * They meet [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034) specifications.

  
  
## What's next

  1. [Create a MySQL database on the instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases).
  2. [Create MySQL users on the instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users).
  3. [Secure and control access to the instance](https://docs.cloud.google.com/sql/docs/mysql/instance-access-control).
  4. [Connect to the instance with a MySQL client](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip).
  5. [Import data into the database](https://docs.cloud.google.com/sql/docs/mysql/import-export).
  6. [Learn about instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
