---
url: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql/
title: Configure a Cloud SQL (MySQL) instance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:29.754396+00:00
---

# Configure a Cloud SQL (MySQL) instance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-cloud-sql-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Cloud SQL (MySQL) instance Stay organized with collections  Save and categorize content based on your preferences. 

App Design Center lets you configure connections and [instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings) for [Cloud SQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/introduction), a fully managed service for running MySQL relational databases. Configurable parameters are based on the [terraform-google-sql-db](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql) Terraform module.

## Component connections

The following table includes the components that you can connect to a Cloud SQL (MySQL) instance, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can connect and read and write data to the Cloud SQL (MySQL) instance.
  * The Cloud SQL connection metadata is added to the Compute Engine instance template.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the Compute Engine instance template service account.
  * The Compute Engine service account is added as an IAM user to the Cloud SQL instance.

| [Connect from Compute Engine](https://docs.cloud.google.com/sql/docs/mysql/connect-compute-engine)  
[Secret Manager](https://docs.cloud.google.com/application-design-center/docs/configure-secret-manager) | 

  * The Secret Manager **Secret Data** field contains the password for the default user.

| [Use Secret Manager to handle secrets in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/use-secret-manager)  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can connect to the Cloud SQL (MySQL) instance.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the service account.
  * The service account IAM information is added to the Cloud SQL instance.

| [Roles and permissions](https://docs.cloud.google.com/sql/docs/mysql/roles-and-permissions)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can read and write data to the Cloud SQL (MySQL) instance.
  * The Cloud SQL connection metadata is added to the Cloud Run service.
  * The `roles/cloudsql.instanceUser` and `roles/cloudsql.client` roles are added to the Cloud Run service account.
  * The Cloud Run service account is added as an IAM user to the Cloud SQL instance.

| [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)  
  
## Required configuration parameters

If your template includes a Cloud SQL (MySQL) component, you must configure the following parameters before you deploy.

Parameter name | Description and constraint information | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Cloud SQL resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Name** | [name](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.name) | [Create a MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen)  
**Database Version** | [databaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.database_version) | [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion)  
**Region** | [region](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.region) | [Manage instance locations](https://docs.cloud.google.com/sql/docs/mysql/locations)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Zone** | [gceZone](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.gce_zone) | [Manage instance locations](https://docs.cloud.google.com/sql/docs/mysql/locations)  
| **Edition** | [edition](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.edition) | [Introduction to Cloud SQL for MySQL editions](https://docs.cloud.google.com/sql/docs/mysql/editions-intro)  
| **Availability Type** | [availabilityType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.availability_type) | [Availability in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/availability)  
| **Enable Default Db** | If selected, create a default database. In the **Db Name** field, enter the name of the default database. | [Create a database on the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases#create)  
| **Enable Default User** | If selected, create a default user. Enter a **User Name** and **User Password** for the default user. | [Default MySQL user](https://docs.cloud.google.com/sql/docs/mysql/users#root-users)  
| **Root Password** | [rootPassword](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.root_password) | Initial root password when the instance is created.  
| **Machine** | Select a machine series and type for your instance. The options that you select determine available storage type and configuration options. You can't change the machine series after you create your instance. | [Machine series overview](https://docs.cloud.google.com/sql/docs/mysql/machine-series-overview)  
Disk Autoresize | **Disk Autoresize** | [storageAutoResize](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.storage_auto_resize) | [Enable automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen)  
**Disk Autoresize Limit** | [storageAutoResizeLimit](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.storage_auto_resize_limit) | [Automatic storage increase limit](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-limit-2ndgen)  
| **Disk Size** | [dataDiskSizeGb](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.data_disk_size_gb) | [Storage capacity](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-capacity-2ndgen)  
| **Disk Type** | [dataDiskType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.data_disk_type) | [Storage type](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#storage-type-2ndgen)  
| **Pricing Plan** | [pricingPlan](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.pricing_plan) | [SqlPricingPlan](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#sqlpricingplan)  
Backup Configuration | **Binary Log Enabled** | [binaryLogEnabled](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.binary_log_enabled) | [Create a MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen)  
**Enabled** | [enabled](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.enabled) | [Create a MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen)  
**Start Time** | [start_time](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.start_time) | [Create a MySQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#create-2nd-gen)  
**Region** | [location](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.location) | [Custom backup locations](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#custom-backup-location)  
**Zone** | [location](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.location) | [Custom backup locations](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backups#custom-backup-location)  
**Transaction Log Retention Days** | [transactionLogRetentionDays](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.transaction_log_retention_days) | [Log retention period](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#log-retention-period)  
**Retained Backups** | [retainedBackups](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupRetentionSettings.FIELDS.retained_backups) | [Logs and disk usage](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#disk-usage)  
**Retention Unit** | [retentionUnit](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupRetentionSettings.FIELDS.retention_unit) | [Logs and disk usage](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#disk-usage)  
IP Configuration | **Authorized Network Key** | [authorizedNetworks[]](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#IpConfiguration.FIELDS.authorized_networks) | [Authorize with authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks)  
**Authorized Network Value** | [authorizedNetworks[]](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#IpConfiguration.FIELDS.authorized_networks) | [Authorize with authorized networks](https://docs.cloud.google.com/sql/docs/mysql/authorize-networks)  
**IPv4 Enabled** | [ipv4Enabled](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#IpConfiguration.FIELDS.ipv4_enabled) | [Configure Public IP](https://docs.cloud.google.com/sql/docs/mysql/configure-ip)  
**Private Network** | [privateNetwork](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#IpConfiguration.FIELDS.private_network) | [Configure Private IP](https://docs.cloud.google.com/sql/docs/mysql/configure-private-ip)  
**SSL Mode** | [sslMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#IpConfiguration.FIELDS.ssl_mode) | [SSL mode](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#ssl-mode)  
**Allocated IP Range** | [allocatedIpRange](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#IpConfiguration.FIELDS.allocated_ip_range) | [Allocated IP address ranges for services](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range)  
**Enable Private Path for Google Cloud Services** | [Private path for Google Cloud services](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#private-path) | [Create an instance that supports private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access-and-private-service-connect#create-psa-psc-instance)  
**PSC Enabled** | [pscEnabled](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PscConfig.FIELDS.psc_enabled) | [Private Service Connect overview](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect)  
**PSC Allowed Consumer Projects** | [allowedConsumerProjects](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PscConfig.FIELDS.allowed_consumer_projects) | [Create an instance that supports private services access and Private Service Connect](https://docs.cloud.google.com/sql/docs/mysql/configure-private-services-access-and-private-service-connect#create-psa-psc-instance)  
| **Maintenance Version** | [maintenanceVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.maintenance_version) | [Self-service maintenance](https://docs.cloud.google.com/sql/docs/mysql/maintenance#self-service-maintenance)  
| **User Host** | The host for the default user. | [host](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users#User.FIELDS.host)  
| **Deletion protection** | If selected, the Cloud SQL instance cannot be deleted. | [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection)  
| **User Deletion Policy** | To allow the user to be abandoned rather than deleted, enter `ABANDON`. | MySQL users cannot be deleted if they have been granted SQL roles.  
| **Data Cache Enabled** | [Data cache](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#data-cache-mysql) | [Data cache overview](https://docs.cloud.google.com/sql/docs/mysql/data-cache)  
Additional Databases | **Name** | [name](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases#Database.FIELDS.name) | [Create and manage databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases)  
**Collation** | [collation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.collation) | [Create and manage databases](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases)  
Additional Users | **Name** | [name](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users#User.FIELDS.name) | [About MySQL users and roles](https://docs.cloud.google.com/sql/docs/mysql/users)  
**Password** | Enter a password, or select **Random Password** to generate a password. | [About MySQL users and roles](https://docs.cloud.google.com/sql/docs/mysql/users)  
**Type** | [SqlUserType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users#sqlusertype) | [About MySQL users and roles](https://docs.cloud.google.com/sql/docs/mysql/users)  
**Host** | [host](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users#User.FIELDS.host) | [About MySQL users and roles](https://docs.cloud.google.com/sql/docs/mysql/users)  
IAM Users | **ID** | The IAM user's ID. | [IAM authentication](https://docs.cloud.google.com/sql/docs/mysql/iam-authentication)  
**Email** | The IAM user's email. | [Add an individual IAM user or service account to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#creating-a-database-user)  
**Type** | [type](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/users#User.FIELDS.type) | [Add an individual IAM user or service account to a Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/add-manage-iam-users#creating-a-database-user)  
| **Random Instance Name** | Add a random suffix to the end of the instance name. | [random_instance_name](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs)  
| **Replica Database Version** | The read replica database version to use. Only use during a database update. | [SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/SqlDatabaseVersion)  
| **Master Instance Name** | [masterInstanceName](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.master_instance_name) | [Create read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica)  
| **Instance Type** | [instanceType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DatabaseInstance.FIELDS.instance_type) | [SqlInstanceType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#sqlinstancetype)  
| **Secondary Zone** | The preferred zone for the replica instance. | [secondaryZone](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#LocationPreference.FIELDS.secondary_zone)  
| **Follow GAE Application** | The App Engine application to follow. Must be in the same region as the Cloud SQL instance. | [followGaeApplication](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#LocationPreference.FIELDS.follow_gae_application)  
| **Activation Policy** | [activationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.activation_policy) | [Activation Policy](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance#activation_policy)  
| **Deletion Protection Enabled** | [deletionProtectionEnabled](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.deletion_protection_enabled) | [Prevent deletion of an instance](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection)  
| **Read Replica Deletion Protection Enabled** | To block Terraform from deleting replica SQL Instances, select the checkbox. | [Considering deletion protection for read replicas](https://docs.cloud.google.com/sql/docs/mysql/deletion-protection#considering-for-read-replicas)  
Maintenance Window | **Maintenance Window Day** | [day](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#MaintenanceWindow.FIELDS.day) | [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance)  
**Maintenance Window Hour** | [hour](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#MaintenanceWindow.FIELDS.hour) | [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance)  
**Maintenance Window Update Track** | [updateTrack](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#MaintenanceWindow.FIELDS.update_track) | [About maintenance on Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/maintenance)  
Database flags | **Name** | [databaseFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.database_flags) | [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags)  
**Value** | [databaseFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.database_flags) | [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags)  
User Labels | **Key** | Key label for the Cloud SQL instance. | [userLabels](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.user_labels)  
**Value** | Value label for the Cloud SQL instance. | [userLabels](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.user_labels)  
Deny Maintenance Period | **End Date** | [endDate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DenyMaintenancePeriod.FIELDS.end_date) | [Configure a deny maintenance period](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window#configure-deny-maintenance)  
**Start Date** | [startDate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DenyMaintenancePeriod.FIELDS.start_date) | [Configure a deny maintenance period](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window#configure-deny-maintenance)  
**Time** | [time](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#DenyMaintenancePeriod.FIELDS.time) | [Configure a deny maintenance period](https://docs.cloud.google.com/sql/docs/mysql/set-maintenance-window#configure-deny-maintenance)  
Insights Config | **Query Plans Per Minute** | [queryPlansPerMinute](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#InsightsConfig.FIELDS.query_plans_per_minute) | [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)  
**Query String Length** | [queryStringLength](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#InsightsConfig.FIELDS.query_string_length) | [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights)  
**Record Application Tags** | [recordApplicationTags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#InsightsConfig.FIELDS.record_application_tags) | [Enable query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights)  
**Record Client Address** | [recordClientAddress](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#InsightsConfig.FIELDS.record_client_address) | [Enable query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights#enable-insights)  
Password Validation Policy Config | **Enable Password Policy** | [enablePasswordPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PasswordValidationPolicy.FIELDS.enable_password_policy) | [Set password policy](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#password)  
**Min Length** | [minLength](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PasswordValidationPolicy.FIELDS.min_length) | [Set password policy](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#password)  
**Complexity** | [complexity](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PasswordValidationPolicy.FIELDS.complexity) | [Set password policy](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#password)  
**Disallow Username Substring** | [disallowUsernameSubstring](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PasswordValidationPolicy.FIELDS.disallow_username_substring) | [Set password policy](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#password)  
**Reuse Interval** | [reuseInterval](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#PasswordValidationPolicy.FIELDS.reuse_interval) | [Set password policy](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#password)  
Read Replicas | **Name** | [read_replicas](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs) | [Read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas)  
**Name Override** | A string to override the default read replica name. | [read_replicas](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs)  
| **Read Replica Name Suffix** | The optional suffix to add to the read instance name. | [Read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication#read-replicas)  
| **DB Charset** | [charset](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases#Database.FIELDS.charset) | [Create a database on the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases#create)  
| **DB Collation** | [collation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/databases#Database.FIELDS.collation) | [Create a database on the Cloud SQL instance](https://docs.cloud.google.com/sql/docs/mysql/create-manage-databases#create)  
| **Create Timeout** | The optional timeout that is applied to limit long database creates. | [create_timeout](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs)  
| **Update Timeout** | The optional timeout that is applied to limit long database updates. | [update_timeout](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs)  
| **Delete Timeout** | The optional timeout that is applied to limit long database deletes. | [delete_timeout](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs)  
| **Encryption Key Name** | [encryption_key_name](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#encryption_key_name-1) | [About client-side encryption](https://docs.cloud.google.com/sql/docs/mysql/client-side-encryption)  
| **Read Replica Deletion Protection** | If selected, blocks Terraform from deleting replica SQL Instances. | [deletion_protection](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#deletion_protection-1)  
| **Enable Random Password Special** | If selected, enables special characters in generated random passwords. | [enable_random_password_special](https://github.com/terraform-google-modules/terraform-google-sql-db/tree/main/modules/mysql#inputs)  
| **Connector Enforcement** | [connectorEnforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#Settings.FIELDS.connector_enforcement) | [Cloud SQL Language Connectors overview](https://docs.cloud.google.com/sql/docs/mysql/language-connectors)  
| **Enable Google ML Integration** | [enable_google_ml_integration](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance#enable_google_ml_integration-1) | [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-overview)  
| **Database Integration Roles** | The roles required by the default database instance service account for integration with Google Cloud services. | [Before you begin](https://docs.cloud.google.com/sql/docs/postgres/integrate-cloud-sql-with-vertex-ai#before-you-begin)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
