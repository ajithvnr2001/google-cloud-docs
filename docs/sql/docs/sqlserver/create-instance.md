---
url: https://docs.cloud.google.com/sql/docs/sqlserver/create-instance/
title: Create instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:22.484201+00:00
---

# Create instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/create-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Create instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/create-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/create-instance "View this page for the PostgreSQL database engine") | SQL Server

Cloud SQL for SQL Server lets you deploy fully managed relational databases on Google Cloud. You can provision instances tailored to your workload while automating routine maintenance such as operating system patching, backups, and failover.

Before provisioning an instance, review feature availability in the [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro). For detailed information about all instance settings, see [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings).

## Key concepts

A newly-created instance has a `sqlserver` database.

After creating a Cloud SQL for SQL Server instance, you add databases to it by [creating](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases) or [importing](https://docs.cloud.google.com/sql/docs/sqlserver/import-export) them.

The maximum number of instances you can have in a single project depends on the [network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture#overview) of those instances:

  * New SQL network architecture: You can have up to 1,000 instances per project.
  * Old SQL network architecture: You can have up to 100 instances per project.
  * Using both architectures: Your limit will be somewhere between 100 and 1,000, depending on the distribution of your instances across the two architectures.



[File a support case](https://support.google.com/googlecloud/answer/1041916) to request an increase. Read replicas are counted as instances.

## Choose between Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition

When creating a Cloud SQL for SQL Server instance, you choose the machine configuration from several different machine families, depending on the Cloud SQL edition. See [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview) for details.

**Note:** Beginning April 12, 2027, you won't be able to create new instances of Cloud SQL for SQL Server 2017. Starting on October 13, 2027, SQL Server 2017 will reach end of life (EOL) and Microsoft will stop releasing [security updates](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17#understand-the-sql-server-lifecycle). Cloud SQL for SQL Server will stop supporting SQL Server 2017 after this date.

### Simultaneous multithreading

Simultaneous multithreading (SMT) on Cloud SQL for SQL Server lets you run two virtual CPUs (vCPUs) as independent, separate threads on one physical core. SMT is enabled by default; however, you can disable it, and this might reduce your licensing costs.

**Important:** Disabling SMT reduces the number of virtual CPUs (vCPUs) per core from two to one, which in turn reduces your SQL Server licensing costs. Disabling SMT doesn't change the Compute Engine price for SQL Server. You are billed for the number of vCPUs defined in the SQL Server CPU configuration. To learn more about how you are billed for Cloud SQL for SQL Server instances, see [SQL Server pricing](https://cloud.google.com/sql/pricing#sql-server).

Disabling SMT might impact your instance performance. To understand the impact of disabling SMT on your instance's performance, we recommend that you [perform load testing](https://docs.cloud.google.com/compute/docs/tutorials/load-testing-sql-server-hammerdb) on your instance.

**Note:** You can only set the number of threads per core on Cloud SQL for SQL Server instances that have six vCPUs or more.

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
     * [Cloud SQL Admin](https://docs.cloud.google.com/sql/docs/sqlserver/iam-roles#roles)
     * [Compute Viewer](https://docs.cloud.google.com/compute/docs/access/iam#compute.viewer)

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

[Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/roles-and-permissions) about roles and permissions. 




## Create a SQL Server instance

**Tip** : If you plan on using private networking, then you can deploy both the private networking setup of your choice and the Cloud SQL instance along with clients such as Compute Engine VMs by using Terraform. For more information, see [ Simplified Cloud Networking Configuration Solutions](https://github.com/GoogleCloudPlatform/cloudnetworking-config-solutions). 

### Console

**Note:** If you plan to integrate with Managed Service for Microsoft Active Directory, review the [ prerequisites for integration](https://docs.cloud.google.com/sql/docs/sqlserver/ad#prerequisites-for-integration). Additionally, note the [ procedures and constraints](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#integrating-different-project) for integrating with a Managed Microsoft AD domain in a different project. 

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click **Create instance**.
  3. Select **New instance**.
  4. On the **Choose your database engine** panel of the **Create an instance** page, click **Choose SQL Server**.
  5. In the **Choose a Cloud SQL edition** section of the **Create a SQL Server instance** page, select the Cloud SQL edition for your instance: `Enterprise` or `Enterprise Plus`.

For more information about Cloud SQL editions, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro).

  6. Select the edition preset for your instance. To see the available presets, click the **Edition preset** menu. **Note:** To learn about how edition presets differ from one another, click **Compare edition presets**.
  7. In the **Instance info** section, select the database version for your instance. To see the available versions, click the **Database version** menu.
  8. In the **Instance ID** field of the **Instance info** pane, enter an ID for your instance.  
Don't include sensitive or personally identifiable information in your instance name. 

You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

  9. In the **Password** field, enter a password for the user.

To see the password in clear text, click the **Show password** icon.

You can either enter the password manually or click **Generate** to have Cloud SQL create a password for you automatically.

  10. In the **Choose region and zonal availability** section, select the region and zone for your instance. Region availability might be different based on your Cloud SQL for SQL Server edition. For more information, see [About instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings). 

Place your instance in the same region as the resources that access it. The region you select can't be modified in the future. In most cases, you don't need to specify a zone.

**Note:** If there is a resource location constraint on your organization policy, you must select one of the regions that the organization policy allows. You see a message about Resource Location Restriction in the **Choose region and zonal availability** section if a constraint exists. [Learn more](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations). 

If you are configuring your instance for [high availability](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability), you can select both a primary and secondary zone.

The following conditions apply when the secondary zone is used during instance creation:

     * The zones default to `Any` for the primary zone and `Any (different from primary)` for the secondary zone.
     * If both the primary and secondary zones are specified, they must be distinct zones.
  11. In the **Customize your instance** section, update the settings for your instance. Click **Show configuration option** to display the groups of settings. Then, expand the groups you want to review and customize settings. A **Summary** of all the options you select is shown on the right. Customizing these instance settings is optional. Defaults are assigned in every case where no customizations are made. 

The following table is a quick reference to instance settings. For more details about each setting, see the [instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings) page. 

Setting | Notes  
---|---  
**Machine type**  
Machine type | Select from Lightweight, Standard (Most common), or High memory. Each machine type is classified by the number of CPUs (cores) and amount of memory for your instance.   
Cores | The number of vCPUs for your instance. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#cpus-postgres).   
Memory | The amount of memory for your instance, in GBs. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#memory-postgres).   
Custom | For the Dedicated core machine type, instead of selecting a predefined configuration, select the **Custom** button to create an instance with a custom configuration. When you select this option, you need to select the number of cores and amount of memory for your instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/create-instance#machine-types).   
**Data cache**  
Enable data cache | By default, the option to enable data cache is selected automatically for Cloud SQL for SQL Server Enterprise Plus edition instances. If you don't want to enable data cache, then clear the **Enable data cache** checkbox. For more information about data cache, see [data cache](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#data-cache).   
**Storage**  
Storage type | Determines whether your instance uses SSD or HDD storage. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#storage-type-2ndgen).   
Storage capacity | The amount of storage provisioned for the instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#storage-capacity-2ndgen).   
Enable automatic storage increases | Determines whether Cloud SQL automatically provides more storage for your instance when free space runs low. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen).   
**Encryption**  
Google-managed encryption| The default option.  
Customer key-managed encryption key (CMEK)| Select to use your key with Google Cloud Key Management Service. [Learn more](https://docs.cloud.google.com/sql/docs/mysql/cmek).  
**Connections**  
Private IP | Adds a private IP address for your instance. Choose either a [private services access](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-services-access) connection, a [Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect) connection, or both for your instance. Your selection provides the private network connection for your instance. In all cases, additional configuration is required.   
  
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
For more information about configuring Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect).
     * Learn more about [Private IP connection options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#private-ip).
     * Learn more about [allocated IP address ranges](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated_ip_address_ranges).
**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following: 
     1. If you haven't already enabled the Cloud DNS API, [enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) for your Google Cloud project.
     2. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
     3. Add a private IP address to the instance.
     4. Specify an associated network for the instance.
     5. Optionally, specify an allocated IP range for the instance.  
Public IP | Adds a public IP address for your instance. You can then add authorized networks to connect to the instance. Your instance can have both a public and a private IP address. Learn more about using [public IP](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#public_ip).  
Authorized networks| Add the name for the new network and the Network address. [Learn more](https://docs.cloud.google.com/sql/docs/postgres/authorize-networks#authorized-networks).  
Allow Data API |  By selecting this checkbox, you let authorized users to call the [Data API](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance) to execute SQL statements on the instance. For instances with Private IP only, this allows authorized users to call the Data API from the public internet.  
**Security**  
Server certificate authority mode  |  Choose the type of certificate authority (CA) that signs the server certificate for this Cloud SQL instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies). By default, when you create an instance in Google Cloud console, the instance uses the **Google managed internal certificate authority** (`GOOGLE_MANAGED_INTERNAL_CA`), which is the per-instance CA option.  
Automatic server certificate rotation  |  If you select either the Google-managed CAS certificate authority (CA) (`GOOGLE_MANAGED_CAS_CA`) or the customer-managed CAS internal certificate authority (`CUSTOMER_MANAGED_CAS_CA`) option as the server CA mode for the instance, then you can choose whether to rotate the server certificate for the instance automatically. For more information about rotating Cloud SQL server certificates automatically, see [ Enable automatic server certificate rotation](https://docs.cloud.google.com/sql/docs/sqlserver/manage-ssl-instance#automatic-server-certificate-rotation-cas). By default, this option is disabled.  
**Data protection**  
Backup tier | The [backup option](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options) of your instance. You can choose between [enhanced backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options#enhanced-backups) and [standard backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backup-options#standard-backups).   
Automate backups | The window of time when you would like backups to start.   
Choose where to store your backups| Select Multi-region for most use cases. If you need to store backups in a specific region, for example, if there are regulatory reasons to do so, select Region and select your region from the Location drop-down menu.  
Choose how many automated backups to store| The number of automated backups you would like to retain (from 1 to 365 days). [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#backup-retention).   
Enable point-in-time recovery | Enables point-in-time recovery and transaction logging. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#pitr). **Note:** To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations. PITR is enabled by default during instance creation in the following conditions: In **Cloud SQL Enterprise Plus edition** :
     * PITR is enabled by default, regardless of how you create the instance.
In **Cloud SQL Enterprise edition** :
     * If you create the instance in Google Cloud console, PITR is enabled by default.
     * If you create the instance using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or Cloud SQL Admin API, then PITR is disabled by default. In this case, you must enable PITR manually if you want to use it.  
Enable deletion protection | Determines whether to protect an instance against accidental deletion. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/deletion-protection).   
Enable retained backups after instance deletion | Determines whether automated and on-demand backups are retained after an instance is deleted. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#retained-backups).   
Choose how many days of logs to retain | Configure write-ahead log retention from 1 to 7 days. The default setting is 7 days. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#transaction-log-retention).   
**Maintenance**  
Preferred window | Determines a one-hour window when Cloud SQL can perform disruptive maintenance on your instance. If you do not set the window, then disruptive maintenance can be done at any time. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#maintenance-window-2ndgen).   
Order of updates | Your preferred timing for instance updates, relative to other instances in the same project. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#maintenance-timing-2ndgen).   
**Flags**  
ADD FLAG | You can use database flags to control settings and parameters for your instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/flags).   
**Query insights**  
Enable Query insights |  By selecting this checkbox, you enable query insights for your instance. Query insights provides you with detailed information about your database queries, including query performance, query text, and query execution plans. After you select query insights, you can enable additional features that are associated with query insights. For more information about these features and query insights, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights).  
**Labels**  
ADD LABEL| Add a key and value for each label that you add. You use labels to help organize your instances.  
  12. Click **Create Instance**. 

Note: It might take a few minutes to create your instance. However, you can [view information about the instance](https://docs.cloud.google.com/sql/docs/sqlserver/instance-info) while it's being created.




### gcloud

For information about installing and getting started with the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), see [Installing gcloud CLI](https://docs.cloud.google.com/sdk/docs/install). For information about starting Cloud Shell, see the [Cloud Shell documentation](https://docs.cloud.google.com/shell/docs/starting-cloud-shell).

You must use `gcloud` version 243.0.0 or later.

  1. Use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create the instance:

For Cloud SQL Enterprise Plus edition instances:
    
    gcloud sql instances create INSTANCE_NAME \
          --database-version=DATABASE_VERSION \
          --region=REGION \
          --tier=TIER \
          --root-password=ROOT_PASSWORD \
          --edition=ENTERPRISE_PLUS
        

For Cloud SQL Enterprise edition instances:
    
    gcloud sql instances create INSTANCE_NAME \
          --database-version=DATABASE_VERSION \
          --region=REGION \
          --cpu=NUMBER_OF_vCPUs \
          --memory=MEMORY_SIZE \
          --root-password=ROOT_PASSWORD \
          --edition=ENTERPRISE
        

Don't include sensitive or personally identifiable information in your instance name.  


You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

The values for vCPUs and memory size are limited for Cloud SQL Enterprise edition. For more information, see Choose between Cloud SQL Enterprise Plus edition and Cloud SQL Enterprise edition.

For example, the following string creates an instance with two vCPUs and 7,680 MB of memory:
    
    gcloud sql instances create myinstance \
        --database-version=SQLSERVER_2017_STANDARD \
        --region=us-central1 \
        --cpu=2 \
        --memory=7680MB \
        --root-password=EXAMPLE_PASSWORD \
        --edition=ENTERPRISE
        

For details about different machine configurations, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

To learn about the parameters for instance settings, see [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create).

**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following:

     1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
     2. Add a private IP address to the instance.
     3. Specify an associated network for the instance.
     4. Optionally, specify an allocated IP range for the instance.

The default value for REGION is `us-central1`.

Don't include sensitive or personally identifiable information in your instance name; it is externally visible.   
You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

If you are creating an instance for [high availability](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability), you can specify both the primary and secondary zones, using the `--zone` and `--secondary-zone` parameters. The following conditions apply when the secondary zone is used during instance creation or edit:

     * The zones must be valid zones.
     * If the secondary zone is specified, the primary must also be specified.
     * If the primary and secondary zones are specified, they must be distinct zones.
     * If the primary and secondary zones are specified, they must belong to the same region.

You can add more [parameters](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) to determine other instance settings:

Setting | Parameter | Notes  
---|---|---  
**Required parameters**  
Database version | `--database-version` | The [database version](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#settings-2ndgen), which is based on your Cloud SQL edition.  
Region | `--region` | [ See valid values](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#region-values). **Note:** Some organizations use an organization policy to restrict resource locations. If this type of policy affects your project, you can only select regions the organization policy allows. In the **Location** drop-down menu in the Console, the locations that are not allowed are unavailable. [Learn more](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations).   
**Connectivity**  
Private IP |  **Private services access** `--network` `--no-assign-ip` (optional) `--allocated-ip-range-name` (optional) `--enable-google-private-path` (optional)   
  
**Private Service Connect** `--no-assign-ip` `--enable-private-service-connect` `--allowed-psc-projects` `--psc-auto-connections` `--enable-psc-auto-connection-policy` | `--network`: specifies the name of the VPC network you want to use for this instance. Private services access must already be configured for the network. On new or empty projects, you must enable `servicenetworking.googleapis.com`, allocate an IP range, and configure VPC Network Peering before creating the instance. Available only for the beta command (`gcloud beta sql instances create`). `--no-assign-ip`: Instance will only have a private IP address. `--allocated-ip-range-name`: if specified, sets a range name for which an IP range is allocated. For example, `google-managed-services-default`. The range name should comply with `RFC-1035` and be within 1-63 characters. (`gcloud alpha sql instances create`). **Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following: 
     1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
     2. Add a private IP address to the instance.
     3. Specify an associated network for the instance.
     4. Optionally, specify an allocated IP range for the instance.
For Cloud SQL instances that use Private Service Connect for private IP connections, use the following flags: `--enable-private-service-connect`: enables private network connections to the Cloud SQL instance using Private Service Connect. For more information, see [Overview of Private Service Connect in Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/about-private-service-connect). `--allowed-psc-projects`: a comma-separated list of allowed project IDs or numbers from where Private Service Connect endpoints can connect to Cloud SQL instances. `--psc-auto-connections`: if you're setting up endpoints automatically for a Cloud SQL instance, then use the flag to specify the consumer networks and projects for the Private Service Connect endpoints. `--enable-psc-auto-connection-policy`: if specified, Google Cloud creates or updates a service connection policy in the consumer network and project for the Private Service Connect endpoint. For more information about configuring Private Service Connect, see [Configure Private Service Connect](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-service-connect).  
Data API Access | `--data-api-access` | Controls connectivity to the instance using [Data API](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance). It's disallowed by default. Set the value to `ALLOW_DATA_API` to let users use the Data API to connect to the instance. For instances configured with a private IP address only, authorized users can call the Data API on the instance from the public internet. Set the value to `DISALLOW_DATA_API` to disallow using the Data API.   
Public IP | `--authorized-networks` | For public IP connections, only connections from authorized networks can connect to your instance. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ip).   
Server CA mode | `--server-ca-mode` | The `--server-ca-mode` flag configures the type of [server certificate authority (CA)](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies) for an instance. You can select one of the following options:
     * `GOOGLE_MANAGED_INTERNAL_CA`: this is the default value. With this option, an internal CA dedicated to each Cloud SQL instance signs the server certificate for that instance.
     * `GOOGLE_MANAGED_CAS_CA`: with this option, a CA hierarchy consisting of a root CA and subordinate server CAs managed by Cloud SQL and hosted on Google Cloud Certificate Authority Service (CA Service) is used. The subordinate server CAs in a region sign the server certificates and are shared across instances in the region. 
     * `CUSTOMER_MANAGED_CAS_CA`: with this option, you define the CA hierarchy and manage the rotation of the CA certificates. You create a CA pool in CA Service in the same region of your instance. One of the CAs in the pool is used to sign the server certificate. For more information, see [Use a customer-managed CA](https://docs.cloud.google.com/sql/docs/sqlserver/customer-managed-ca).  
Automatic server certificate rotation | `--server-certificate-rotation-mode` | The `--server-certificate-rotation-mode` flag configures the type of server certificate rotation mode of the instance. You can select one of the following options:
     * `NO_AUTOMATIC_ROTATION`: this is the default value. With this option, there won't be no automatic server certificate rotation. Server certificates must be rotated manually.
     * `AUTOMATIC_ROTATION_DURING_MAINTENANCE`: With this option, automatic server certificate rotation is enabled during Cloud SQL scheduled maintenance or self-service maintenance updates. Requires `server_ca_mode` to be `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA`.   
Network architecture | [`--enforce-new-sql-network-architecture`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/create#--enforce-new-sql-network-architecture) | Enforce the use of the new network architecture for the instance upon creation. Using this flag when you create an instance before that project has been fully upgraded to the new network architecture can lead to IP address overconsumption or a failure to create instances if there aren't sufficient IP addresses remaining in the allocated IP range. For more information, see [Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated-ip).   
**Machine type and storage**  
Machine type | `--tier`  
Storage type | `--storage-type` | Determines whether your instance uses SSD or HDD storage. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#storage-type-2ndgen).   
Storage capacity | `--storage-size` | The amount of storage provisioned for the instance, in GB. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#storage-capacity-2ndgen).   
Automatic storage increase | `--storage-auto-increase` | Determines whether Cloud SQL automatically provides more storage for your instance when free space runs low. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-2ndgen).   
Automatic storage increase limit | `--storage-auto-increase-limit` | Determines how large Cloud SQL can automatically grow storage, in GB. The default value is `unlimited`, which allows storage to grow up to the maximum available storage for the instance tier. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#automatic-storage-increase-limit-2ndgen).   
**Automatic backups and high availability**  
High availability | `--availability-type` | For a highly-available instance, set to `REGIONAL`. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha).   
Secondary zone | `--secondary-zone` | If you're creating an instance for [high availability](https://docs.cloud.google.com/sql/docs/sqlserver/high-availability), you can specify both the primary and secondary zones using the `--zone` and `--secondary-zone parameters`. The following restrictions apply when the secondary zone is used during instance creation or edit: 
     * The zones must be valid zones.
     * If the secondary zone is specified, the primary must also be specified.
If the primary and secondary zones are specified, they must be distinct zones. If the primary and secondary zones are specified, they must belong to the same region. | Automatic backups | `--backup-start-time` | The window of time when you would like backups to start.   
Retention settings for automated backups | `--retained-backups-count` | The number of automated backups to retain. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#retention).  
Retention settings for transaction logs | `--retained-transaction-log-days` | The number of days to retain transaction logs for point-in-time recovery. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#retention).  
Point-in-time recovery | `--enable-point-in-time-recovery` |  Enables point-in-time recovery and transaction logs. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#backups-postgres).   
**Note:** To speed up instance creation when PITR is enabled, Cloud SQL uses an initial [instant snapshot](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) for PITR instead of a [standard backup](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options). This snapshot is later converted to a standard backup in the background to support restore operations. PITR is enabled by default during instance creation in the following conditions: In **Cloud SQL Enterprise Plus edition** :
     * PITR is enabled by default, regardless of how you create the instance.
In **Cloud SQL Enterprise edition** :
     * If you create the instance in the Google Cloud console, PITR is enabled by default.
     * If you create the instance using the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, or the Cloud SQL Admin API, then PITR is disabled by default, and you must enable PITR manually to use it.  
**Add database flags**  
Database flags | `--database-flags` | You can use database flags to control settings and parameters for your instance. [Learn more about database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags).   
**Maintenance schedule**  
Maintenance window | `--maintenance-window-day`,   
`--maintenance-window-hour` | Determines a one-hour window when Cloud SQL can perform disruptive maintenance on your instance. If you don't set the window, then disruptive maintenance can be done at any time. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#maintenance-window-2ndgen).   
Maintenance timing | `--maintenance-release-channel` | Your preferred timing for instance updates, relative to other instances in the same project. Use `preview` for earlier updates, and `production` for later updates. [Learn more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#maintenance-timing-2ndgen).   
**[Query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights)**  
| `--insights-config-query-insights-enabled` | Enables query insights to provide query and query plan analytics.   
**Custom SAN**  
Add a custom subject alternative name (SAN) | `--custom-subject-alternative-names=DNS_NAMES` |  If you want to use a custom DNS name to connect to a Cloud SQL instance instead of using an IP address, then configure the custom subject alternative name (SAN) setting while creating the instance. The custom DNS name that you insert into the custom SAN setting is added to the SAN field of the server certificate of the instance. This lets you use the custom DNS name with hostname validation securely.  Before you can use the custom DNS name in your clients and applications, you must set up the mapping between the DNS name and the IP address. This is known as _DNS resolution_. You can add a comma-separated list of up to three custom DNS names to the custom SAN setting. **Note:** This feature is available for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#ca-hierarchies) instances only. To create the instance, you must use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command.  
  2. Note the automatically assigned IP address. 

If you are not using the Cloud SQL Auth Proxy, you will use this address as the host address that your applications or tools use to connect to the instance.

  3. Set the password for the user: 
         
         gcloud sql users set-password sqlserver no-host --instance=[INSTANCE_NAME] \
                --password=[PASSWORD]
               




### Terraform

To create an instance, use a [Terraform resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance).
    
    
    resource "google_sql_database_instance" "default" {
      name             = "sqlserver-instance"
      region           = "us-central1"
      database_version = "SQLSERVER_2019_STANDARD"
      root_password    = "INSERT-PASSWORD-HERE"
      settings {
        tier = "db-custom-2-7680"
      }
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
             




For more details, see [Configure private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access).

#### 1\. Create the instance

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [ Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings).

Also see the [ Instances:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances/insert) page. For information about instance settings, including valid values for regions, see [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings). For information about machine types, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

Don't include sensitive or personally identifiable information in `instance-id`; the value is externally visible.  
  
You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

The `collation` field (not shown in the following basic API call) lets you set a default value for the [ type of collation](https://docs.microsoft.com/sql/relational-databases/collations/collation-and-unicode-support#Server-level-collations) used for the databases in your instance. This collation default is permanent at the instance level but not at the database level. You can change this default with a database administration tool, but only for a specific database that you are creating or updating. You cannot change the collation default for an instance after creating the instance (unless you recreate the instance). For information about collations in SQL Server, see [ Collation and Unicode support](https://docs.microsoft.com/sql/relational-databases/collations/collation-and-unicode-support). For a prototype of a JSON request, see [ Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#settings). You can specify the following example string for the `collation` parameter: `SQL_Latin1_General_CP1_CI_AS`.

The `timeZone` field (not shown in the following basic API call) lets you to set a time zone for an instance. After you create an instance, you can change the time zone of an instance. For more information and a list of accepted strings, see [ Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1/instances#Settings). You can specify the following example string for the `timeZone` field: `"Pacific Standard Time"`. [See more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#timezone).

To create an instance that is integrated with Managed Microsoft AD, specify a domain, such as `subdomain.mydomain.com`, for the `domain` field. For more information, see [Creating an instance with Windows Authentication](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#creating-an-instance-with-windows-authentication). Additionally, note the [ procedures and constraints](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#integrating-different-project) for integrating with a Managed Microsoft AD domain in a different project. 

For information on setting the value of machine-type in the request body, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following:

  1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
  2. Add a private IP address to the instance.
  3. Specify an associated network for the instance.
  4. Optionally, specify an allocated IP range for the instance.



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID.
  * INSTANCE_ID: the instance ID.
  * REGION: the region name.
  * DATABASE_VERSION: an enum string of the database version. For example: `SQLSERVER_2017_STANDARD`.
  * PASSWORD: the password for the `root` user.
  * MACHINE_TYPE: an enum string of the machine (tier) type. For example:   
`db-perf-optimized-N-4`.
  * EDITION_TYPE: your Cloud SQL edition. The default value is `ENTERPRISE`.
  * DATA_CACHE_ENABLED: (optional) to enable Data cache for your instance, set the value of this parameter to `true`.
  * PRIVATE_NETWORK: specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.
  * CA_MODE: specify a [certificate authority hierarchy](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies) for the instance, either `GOOGLE_MANAGED_INTERNAL_CA` or `GOOGLE_MANAGED_CAS_CA`. If you don't specify `serverCaMode`, then the default configuration is `GOOGLE_MANAGED_INTERNAL_CA`. This feature is in [Preview](https://cloud.google.com/products#launch-stages).
  * SERVER_CERTIFICATE_ROTATION_MODE: For automatic server certificate rotation for your instance, specify `AUTOMATIC_ROTATION_DURING_MAINTENANCE`. If you don't specify `serverCertificateRotationMode`, then the default configuration is `NO_AUTOMATIC_ROTATION`.
  * DNS_NAMES: add a comma-separated list of up to three DNS names to the [server certificate](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance) of your Cloud SQL instance. You can secure multiple DNS names with a single certificate. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) and for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies) instances only.



If you set `dataApiAccess` to `ALLOW_DATA_API`, then you allow authorized users to use [Data API](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance) to connect to your instance. For Private IP only instances, this allows authorized users to connect from the public internet.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated-ip).

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "backupConfiguration": {
          "enabled": true
        },
        "dataCacheConfig": {
          "dataCacheEnabled": DATA_CACHE_ENABLED
        },
        "ipConfiguration": {
          "privateNetwork": "PRIVATE_NETWORK",
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          "ipv4Enabled": false,
          "serverCaMode": "CA_MODE",
          "serverCertificateRotationMode": "SERVER_CERTIFICATE_ROTATION_MODE",
          "customSubjectAlternativeNames": "DNS_NAMES"
        },
        "dataApiAccess": "ALLOW_DATA_API"
      },
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
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

After the instance is created, you can further [configure the default user account](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users). 

#### 2\. Retrieve the IPv4 address of the instance

Optionally, you can retrieve the automatically-assigned IPv4 address. In the response, that address is in the `ipAddress` field.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: your instance ID, created in the previous step



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "DATABASE_VERSION",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "MACHINE_TYPE",
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference": {
          "zone": "ZONE",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "backupConfiguration": {
          "startTime": "19:00",
          "kind": "sql#backupConfiguration",
          "enabled": true
        },
        "settingsVersion": "1",
        "dataDiskSizeGb": "10"
      },
      "etag": "--redacted--",
      "ipAddresses": [
        {
          "type": "PRIMARY",
          "**ipAddress** ": "10.0.0.1"
        }
      ],
      "serverCaCert": {
        ...
      },
      "instanceType": "CLOUD_SQL_INSTANCE",
      "project": "PROJECT_ID",
      "serviceAccountEmailAddress": "redacted@gcp-sa-cloud-sql.iam.gserviceaccount.com",
      "backendType": "BACKEND_TYPE",
      "selfLink": "https://sqladmin.googleapis.com/v1/projects/PROJECT_ID/instances/INSTANCE_ID",
      "connectionName": "PROJECT_ID:REGION:INSTANCE_ID",
      "name": "INSTANCE_ID",
      "region": "REGION",
      "gceZone": "ZONE"
    }
    

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
             




For more details, see [Configure private services access](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-services-access).

#### 1\. Create the instance

Not all possible fields are shown in the following basic API call. For a prototype of a JSON request, see [ Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances#settings).

Also see the [ Instances:insert](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/insert) page. For information about instance settings, including valid values for regions, see [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings). For information about machine types, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview). 

Don't include sensitive or personally identifiable information in `instance-id`; the value is externally visible.  
  
You do not need to include the project ID in the instance name. This is done automatically where appropriate (for example, in the log files). 

The `collation` field (not shown in the following basic API call) lets you to set a default value for the [ type of collation](https://docs.microsoft.com/sql/relational-databases/collations/collation-and-unicode-support#Server-level-collations) used for the databases in your instance. This collation default is permanent at the instance level but not at the database level. You can change this default with a database administration tool, but only for a specific database that you are creating or updating. You can't change the collation default for an instance after creating the instance (unless you recreate the instance). For information about collations in SQL Server, see [ Collation and Unicode support](https://docs.microsoft.com/sql/relational-databases/collations/collation-and-unicode-support). For a prototype of a JSON request, see [ Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances#settings). You can specify the following example string for the `collation` parameter: `SQL_Latin1_General_CP1_CI_AS`.

The `timeZone` field (not shown in the following basic API call) lets you to set a time zone for an instance. After you create an instance, you can change the time zone of an instance. For more information and a list of accepted strings, see [ Settings](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances#Settings). You can specify the following example string for the `timeZone` field: `"Pacific Standard Time"`. [See more](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#timezone).

To create an instance that is integrated with Managed Service for Microsoft Active Directory, specify a domain, such as `subdomain.mydomain.com`, for the `domain` field. For more information, see [ Creating an instance with Windows Authentication](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#creating-an-instance-with-windows-authentication). Additionally, note the [ procedures and constraints](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ad#integrating-different-project) for integrating with a Managed Microsoft AD domain in a different project. 

For information on setting the value of machine-type in the request body, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview). 

**Note:** Cloud SQL generates a write endpoint automatically for your Cloud SQL Enterprise Plus edition instance if you do the following:

  1. [Enable the Cloud DNS API](https://docs.cloud.google.com/sql/docs/sqlserver/configure-private-ip#connect-write-endpoint) for your Google Cloud project (if this API isn't enabled).
  2. Add a private IP address to the instance.
  3. Specify an associated network for the instance.
  4. Optionally, specify an allocated IP range for the instance.



Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID.
  * INSTANCE_ID: the instance ID.
  * REGION: the region name.
  * DATABASE_VERSION: an enum string of the database version. 
  * MACHINE_TYPE: an enum string of the machine (tier) type. For example:   
`db-perf-optimized-N-4`.
  * PASSWORD: the password for the `root` user.
  * MACHINE_TYPE: an enum string of the machine (tier) type, as: `db-custom-[CPUS]-[MEMORY_MBS]`.
  * EDITION_TYPE: your Cloud SQL edition. The default value is `ENTERPRISE`.
  * DATA_CACHE_ENABLED: (optional) to enable Data cache for your instance, set the value of this parameter to `true`.
  * PRIVATE_NETWORK: specify the name of the Virtual Private Cloud (VPC) network that you want to use for this instance. Private services access must already be configured for the network.
  * AUTHORIZED_NETWORKS: For public IP connections, specify the connections from authorized networks that can connect to your instance.
  * CA_MODE: specify a [certificate authority hierarchy](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies) for the instance, either `GOOGLE_MANAGED_INTERNAL_CA` or `GOOGLE_MANAGED_CAS_CA`. If you don't specify `serverCaMode`, then the default configuration is `GOOGLE_MANAGED_INTERNAL_CA`. This feature is in [Preview](https://cloud.google.com/products#launch-stages).
  * SERVER_CERTIFICATE_ROTATION_MODE: For automatic server certificate rotation for your instance, specify `AUTOMATIC_ROTATION_DURING_MAINTENANCE`. If you don't specify `serverCertificateRotationMode`, then the default configuration is `NO_AUTOMATIC_ROTATION`.
  * DNS_NAMES: add a comma-separated list of up to three DNS names to the [server certificate](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance) of your Cloud SQL instance. You can secure multiple DNS names with a single certificate. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages) and for [`CUSTOMER_MANAGED_CAS_CA`](https://docs.cloud.google.com/sql/docs/sqlserver/authorize-ssl#certificate_authority_ca_hierarchies) instances only.



If you set `dataApiAccess` to `ALLOW_DATA_API`, then you allow authorized users to use [Data API](https://docs.cloud.google.com/sql/docs/sqlserver/executesql-instance) to connect to your instance. For Private IP only instances, this allows authorized users to connect from the public internet.

You can use the `sqlNetworkArchitecture` field to enforce the use of the new network architecture for the instance upon creation, even if the project isn't fully upgraded. For more details about the new network architecture and its implications, see [ Upgrade an instance to the new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture) and [Allocate an IP address range](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated-ip).

HTTP method and URL: 
    
    
    POST https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances

Request JSON body: 
    
    
    {
      "name": "INSTANCE_ID",
      "region": "REGION",
      "databaseVersion": "DATABASE_VERSION",
      "rootPassword": "PASSWORD",
      "settings": {
        "tier": "MACHINE_TYPE",
        "edition": "EDITION_TYPE",
        "backupConfiguration": {
          "enabled": true
        },
        "dataCacheConfig": {
          "dataCacheEnabled": DATA_CACHE_ENABLED
        },
        "ipConfiguration": {
          "privateNetwork": "PRIVATE_NETWORK",
          "authorizedNetworks": [AUTHORIZED_NETWORKS],
          "ipv4Enabled": false,
          "serverCaMode": "CA_MODE",
          "serverCertificateRotationMode": "SERVER_CERTIFICATE_ROTATION_MODE",
          "customSubjectAlternativeNames": "DNS_NAMES"
        },
        "dataApiAccess": "ALLOW_DATA_API"
      },
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
      "insertTime": "2020-01-01T19:13:21.834Z",
      "operationType": "CREATE",
      "name": "OPERATION_ID",
      "targetId": "INSTANCE_ID",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/operations/OPERATION_ID",
      "targetProject": "PROJECT_ID"
    }
    

After the instance is created, you can further [configure the default user account](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users). 

#### 2\. Retrieve the IPv4 address of the instance

Optionally, you can retrieve the automatically-assigned IPv4 address. In the response, that address is in the `ipAddress` field.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your project ID
  * INSTANCE_ID: your instance ID, created in the previous step



HTTP method and URL: 
    
    
    GET https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "kind": "sql#instance",
      "state": "RUNNABLE",
      "databaseVersion": "DATABASE_VERSION",
      "settings": {
        "authorizedGaeApplications": [],
        "tier": "MACHINE_TYPE",
        "kind": "sql#settings",
        "pricingPlan": "PER_USE",
        "replicationType": "SYNCHRONOUS",
        "activationPolicy": "ALWAYS",
        "ipConfiguration": {
          "authorizedNetworks": [],
          "ipv4Enabled": true
        },
        "locationPreference": {
          "zone": "ZONE",
          "kind": "sql#locationPreference"
        },
        "dataDiskType": "PD_SSD",
        "backupConfiguration": {
          "startTime": "19:00",
          "kind": "sql#backupConfiguration",
          "enabled": true
        },
        "settingsVersion": "1",
        "dataDiskSizeGb": "10"
      },
      "etag": "--redacted--",
      "ipAddresses": [
        {
          "type": "PRIMARY",
          "**ipAddress** ": "10.0.0.1"
        }
      ],
      "serverCaCert": {
        ...
      },
      "instanceType": "CLOUD_SQL_INSTANCE",
      "project": "PROJECT_ID",
      "serviceAccountEmailAddress": "redacted@gcp-sa-cloud-sql.iam.gserviceaccount.com",
      "backendType": "BACKEND_TYPE",
      "selfLink": "https://sqladmin.googleapis.com/sql/v1beta4/projects/PROJECT_ID/instances/INSTANCE_ID",
      "connectionName": "PROJECT_ID:REGION:INSTANCE_ID",
      "name": "INSTANCE_ID",
      "region": "REGION",
      "gceZone": "ZONE"
    }
    

To see how the [underlying REST API request](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/insert) is constructed for this task, see the [APIs Explorer on the instances:insert page](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/rest/v1beta4/instances/insert). 

### Generate the write endpoint

A write endpoint is a global domain name service (DNS) name that resolves to the IP address of the current primary instance automatically. This endpoint redirects incoming connections to the new primary instance automatically in case of a replica [failover or switchover](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas) operation. You can use the write endpoint in a SQL connection string instead of an IP address. By using a write endpoint, you can avoid having to make application connection changes when a region outage occurs.

For more information about using a write endpoint to connect to an instance, see [Connect to an instance using a write endpoint](https://docs.cloud.google.com/sql/docs/sqlserver/connect-to-instance-using-write-endpoint).

## Machine types

Determines memory and virtual cores available for your Cloud SQL instance. You can configure machine types from different machine series. The availability of different machine series is determined by your Cloud SQL edition and region.

  * **For Cloud SQL Enterprise Plus edition instances:** Cloud SQL offers predefined machine types in these machine series:

    * [N2](https://docs.cloud.google.com/sqlserver/machine-series-overview#n2_machine_types) series.
    * [Memory-optimized N2](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview#memory-optimized-N2) series.
    * [C4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#c4) series.
  * **For Cloud SQL Enterprise edition instances:** Cloud SQL offers both predefined and custom machine types in these machine series:

    * [general purpose - dedicated core](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#gp-dedicated-core) series.
    * [N4](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview#n4) series.



If you require real-time processing, such as online transaction processing (OLTP), make sure that your instance has enough memory to contain the entire working set. However, there are other factors that can impact memory requirements, such as number of active connections, and internal overhead processes. Perform load testing to avoid performance issues in your production environment.

When you configure your instance, select sufficient memory and vCPUs to handle your needs, and scale up your instance as your requirements increase. A machine configuration with insufficient vCPUs might lose its SLA coverage. For more information, see [Operational guidelines](https://docs.cloud.google.com/sql/docs/sqlserver/operational-guidelines).

For more information, see [Choose a machine series](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview).

## Troubleshoot

Issue | Troubleshooting | Error message: `The zone or region does not have sufficient resources to handle the request at the moment.` | The selected zone lacks capacity for the requested resources or the VM type at the time of the instance creation request. There might be simultaneous high operational demand in that specific regional location at the time of request. To resolve this issue, retry creating the instance in another zone or retry creating the instance in the same zone that received the error at a different time of day.  
---|---  
Error message: `Failed to create subnetwork. Couldn't find free blocks in allocated IP ranges. Please allocate new ranges for this service provider`. | There are no more available addresses in the allocated IP range. There can be several possible scenarios: 

  * The size of the allocated IP range for the private service connection is smaller than /24.
  * The size of the allocated IP range for the private service connection is too small for the number of Cloud SQL instances.
  * The requirement on the size of allocated IP range will be larger if instances are created in multiple regions. See [allocated range size](https://docs.cloud.google.com/sql/docs/sqlserver/private-ip#allocated_range_size)

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

  1. [Create a SQL Server database on the instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-databases).
  2. [Create SQL Server users on the instance](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).
  3. [Secure and control access to the instance](https://docs.cloud.google.com/sql/docs/sqlserver/instance-access-control).
  4. [Connect to the instance with a SQL Server client](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip).
  5. [Import data into the database](https://docs.cloud.google.com/sql/docs/sqlserver/import-export).
  6. [Learn about instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
