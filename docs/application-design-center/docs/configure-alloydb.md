---
url: https://docs.cloud.google.com/application-design-center/docs/configure-alloydb/
title: Configure an AlloyDB for PostgreSQL cluster and instance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:51.739699+00:00
---

# Configure an AlloyDB for PostgreSQL cluster and instance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure an AlloyDB for PostgreSQL cluster and instance Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB is a fully managed, PostgreSQL-compatible database service built for your most demanding enterprise workloads, including high transaction rates, large data sizes, and real-time analytics. For more information, see [ AlloyDB overview](https://docs.cloud.google.com/alloydb/docs/overview).

This document describes the parameters you can configure when using App Design Center to create an AlloyDB cluster and instances. The configuration parameters are based on the [terraform-google-alloy-db](https://github.com/GoogleCloudPlatform/terraform-google-alloy-db/tree/v6.1.0) module.

## Before you begin

Create a private services access configuration in a Virtual Private Cloud (VPC) network that resides in the same Google Cloud project where you'll create your AlloyDB instances.

For more information, see the following:

  * [Private service access overview](https://docs.cloud.google.com/alloydb/docs/about-private-services-access).
  * [Enable private service access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).



## Component connections

You can connect the following components to an AlloyDB instance:

Component | Description | Background Information  
---|---|---  
[Compute Engine instance templates](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can connect to the AlloyDB instance.
  * The AlloyDB resource metadata information is added to the instance template.
  * The `[roles/alloydb.admin](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions)` role is added to the Compute Engine instance template service account.

| [Connection overview](https://docs.cloud.google.com/alloydb/docs/connection-overview)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can connect to the AlloyDB instance.
  * The AlloyDB resource metadata is added to the Cloud Run environment variables.
  * The AlloyDB `roles/alloydb.admin` role is added to the Cloud Run service account.

| [Connect from Cloud Run](https://docs.cloud.google.com/alloydb/docs/quickstart/integrate-cloud-run)  
  
## Required configuration parameters

The following table describes the required parameters for configuring an AlloyDB cluster and a primary instance:

Parameter name | Description and constraint information  | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the AlloyDB instance. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Cluster ID** | The ID of the AlloyDB cluster. | [Create cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create)  
**Region** | The location where the AlloyDB cluster is deployed. | [AlloyDB locations](https://docs.cloud.google.com/alloydb/docs/locations)  
  
## Optional configuration parameters

The following table describes the optional parameters for configuring an AlloyDB cluster and a primary instance:

Feature | Subfeature | Parameter name | Description and constraint information | Background information  
---|---|---|---|---  
Primary instance |  | **Instance ID** | [name](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances#Instance.FIELDS.name) | [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create)  
| **Display name** | [displayName](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1beta/projects.locations.clusters.instances#Instance.FIELDS.display_name) | [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create)  
Database flags | **Key** | [databaseFlags](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.database_flags) | [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags)  
**Value** | [databaseFlags](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.database_flags) | [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags)  
Labels | **Key** | [labels](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.labels) | [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)  
**Value** | [labels](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.labels) | [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)  
Annotations | **Key** | [annotations](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.annotations) | [annotations](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#annotations-1)  
**Value** | [annotations](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.annotations) | [annotations](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#annotations-1)  
| **GCE Zone** | [gceZone](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.gce_zone) | [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones)  
| **Availability Type** | [availabilityType](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.availability_type) | [Test a primary instance for high availability](https://docs.cloud.google.com/alloydb/docs/test-high-availability)  
| **Machine CPU Count** | [cpuCount](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#MachineConfig.FIELDS.cpu_count) | [Sizing and deployment recommendations](https://docs.cloud.google.com/alloydb/docs/use-sizing-recommendations)  
| **Machine Type** | [machineType](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#MachineConfig.FIELDS.machine_type) | [Create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create)  
| **SSL Mode** | [sslMode](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/SslConfig#sslmode) | [Configure SSL enforcement mode](https://docs.cloud.google.com/alloydb/docs/instance-ssl)  
| **Require Connectors** | [requireConnectors](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#ClientConnectionConfig.FIELDS.require_connectors) | [Control connector enforcement](https://docs.cloud.google.com/alloydb/docs/enforce-connectors)  
Query Insights Config | **Query String Length** | [queryStringLength](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.query_string_length) | [About Query Insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview)  
**Record Application Tags** | [recordApplicationTags](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.record_application_tags) | [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)  
**Record Client Address** | [recordClientAddress](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.record_client_address) | [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)  
**Query Plans Per Minute** | [queryPlansPerMinute](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.query_plans_per_minute) | [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)  
| **Enable Public IP** | [enablePublicIP](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#InstanceNetworkConfig.FIELDS.enable_public_ip) | [Connect using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip)  
| **Enable Outbound Public IP** | [enableOutboundPublicIP](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#InstanceNetworkConfig.FIELDS.enable_outbound_public_ip) | [Connect using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip)  
| **CIDR Range** | [cidrRange](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#AuthorizedNetwork.FIELDS.cidr_range) | [Public IP](https://docs.cloud.google.com/alloydb/docs/connection-overview#public-ip)  
|  | **Network Self Link** | [network](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#NetworkConfig.FIELDS.network) | [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity)  
|  | **Cluster Type** | [clusterType](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.cluster_type) | [Cross-region replication overview](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/about-cross-region-replication)  
Cluster Labels |  | **Key** | [labels](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.labels) | [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)  
| **Value** | [labels](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.labels) | [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)  
|  | **Cluster Display Name** | [displayName](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.display_name) | [Create a cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create)  
Cluster Initial User |  | **User** | [initialUser](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.initial_user) | [Create a new cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create#procedure)  
| **Password** | [initialUser](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.initial_user) | [Create a new cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create#procedure)  
|  | **Skip Await Major Version Upgrade** | [skip_await_major_version_upgrade](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_cluster#skip_await_major_version_upgrade-1) | [Database in-place major version upgrade overview](https://docs.cloud.google.com/alloydb/docs/major-version-upgrade-inplace-overview)  
|  | **Subscription Type** | [subscriptionType](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.subscription_type) | [Free trial cluster overview](https://docs.cloud.google.com/alloydb/docs/free-trial-cluster)  
|  | **Cluster Encryption Key Name** | [encryptionConfig](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.encryption_config) | [About CMEK](https://docs.cloud.google.com/alloydb/docs/cmek)  
Automated Backup Policy |  | **Region** | [location](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#AutomatedBackupPolicy.FIELDS.location) | [On-demand backup locations](https://docs.cloud.google.com/alloydb/docs/backup/overview#on-demand-backups-locations)  
| **Backup Window** | [backupWindow](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#AutomatedBackupPolicy.FIELDS.backup_window) | [Continuous backup and recovery](https://docs.cloud.google.com/alloydb/docs/backup/overview#continuous)  
| **Enabled** | [enabled](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#AutomatedBackupPolicy.FIELDS.enabled) | [Data backup and recovery overview](https://docs.cloud.google.com/alloydb/docs/backup/overview)  
Weekly Schedule | **Days of Week** | [daysOfWeek](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#WeeklySchedule.FIELDS.days_of_week) | [Automated backup configuration attributes](https://docs.cloud.google.com/alloydb/docs/backup/configure#attributes)  
**Start Time** | [startTimes](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#WeeklySchedule.FIELDS.start_times) | [Automated backup configuration attributes](https://docs.cloud.google.com/alloydb/docs/backup/configure#attributes)  
| **Quantity Based Retention Count** | [count](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#QuantityBasedRetention.FIELDS.count) | [Automated backup configuration attributes](https://docs.cloud.google.com/alloydb/docs/backup/configure#attributes)  
| **Time Based Retention Count** | [retentionPeriod](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#TimeBasedRetention.FIELDS.retention_period) | [Automated backup configuration attributes](https://docs.cloud.google.com/alloydb/docs/backup/configure#attributes)  
Labels | **Key** | [labels](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#AutomatedBackupPolicy.FIELDS.labels) | [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)  
**Value** | [labels](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#AutomatedBackupPolicy.FIELDS.labels) | [Best practices for labels](https://docs.cloud.google.com/resource-manager/docs/best-practices-labels)  
| **Backup Encryption Key Name** | [encryptionConfig](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Backup.FIELDS.encryption_config) | [Backups and restoration](https://docs.cloud.google.com/alloydb/docs/cmek#backups_and_restoration)  
|  | **Continuous Backup Enable** | [enabled](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#ContinuousBackupConfig.FIELDS.enabled) | [Continuous backup and recovery](https://docs.cloud.google.com/alloydb/docs/backup/overview#continuous)  
|  | **Continuous Backup Recovery Window Days** | [recoveryWindowDays](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#ContinuousBackupConfig.FIELDS.recovery_window_days) | [Continuous backup and recovery](https://docs.cloud.google.com/alloydb/docs/backup/overview#continuous)  
Maintenance Update Policy | Maintenance Windows | **Day** | [day](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#MaintenanceWindow.FIELDS.day) | [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance)  
Start Time | **Hours** | [startTime](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#MaintenanceWindow.FIELDS.start_time) | [Maintenance overview](https://docs.cloud.google.com/alloydb/docs/maintenance)  
|  | **Continuous Backup Encryption Key Name** | [kmsKeyName](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#ContinuousBackupConfig.FIELDS.encryption_config) | [Backups and restoration](https://docs.cloud.google.com/alloydb/docs/cmek#backups_and_restoration)  
Read Pool Instance(s) |  | **Instance ID** | [name](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.name) | [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)  
| **Display Name** | [displayName](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.display_name) | [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)  
| **Node Count** | [nodeCount](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#ReadPoolConfig.FIELDS.node_count) | [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)  
Database Flags | **Key** | [databaseFlags](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.database_flags) | [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags)  
**Value** | [databaseFlags](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.database_flags) | [Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags)  
| **Machine CPU Count** | [cpuCount](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#MachineConfig.FIELDS.cpu_count) | [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)  
| **Machine Type** | [machineType](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#MachineConfig.FIELDS.machine_type) | [Create a read pool instance](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)  
| **SSL Mode** | [sslMode](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/SslConfig#FIELDS.ssl_mode) | [Configure SSL enforcement mode](https://docs.cloud.google.com/alloydb/docs/instance-ssl)  
| **Require Connectors** | [requireConnectors](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#ClientConnectionConfig.FIELDS.require_connectors) | [About the AlloyDB Auth Proxy](https://docs.cloud.google.com/alloydb/docs/auth-proxy/overview)  
Query Insights Config | **Query String Length** | [queryStringLength](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.query_string_length) | [About Query Insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview)  
**Record Application Tags** | [recordApplicationTags](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.record_application_tags) | [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)  
**Record Client Address** | [recordClientAddress](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.record_client_address) | [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)  
**Query Plans Per Minute** | [queryPlansPerMinute](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#QueryInsightsInstanceConfig.FIELDS.query_plans_per_minute) | [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-query-insights)  
| **Enable Public IP** | [publicIpAddress](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#Instance.FIELDS.public_ip_address) | [Connect using public IP](https://docs.cloud.google.com/alloydb/docs/connect-public-ip)  
| **CIDR Range** | [cidrRange](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#AuthorizedNetwork.FIELDS.cidr_range) | [Public IP](https://docs.cloud.google.com/alloydb/docs/connection-overview#public-ip)  
|  | **Primary Cluster Name** | [primaryClusterName](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#SecondaryConfig.FIELDS.primary_cluster_name) | [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create)  
|  | **Allocated IP Range** | [allocatedIpRange](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#NetworkConfig.FIELDS.allocated_ip_range) | [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity)  
|  | **Database Version** | [databaseVersion](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.database_version) | [Database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies)  
|  | **PSC Enabled** | [pscEnabled](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances#ClientConnectionConfig.FIELDS.psc_enabled) | [Private Service Connect overview](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect)  
|  | **PSC Allowed Consumer Projects** | [allowed_consumer_projects](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#allowed_consumer_projects-1) | [Allowed Private Service Connect projects](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#allowed-projects)  
PSC Auto Connections |  | **Consumer Network** | [consumer_network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#consumer_network-1) | [Allowed Private Service Connect projects](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#allowed-projects)  
| **Consumer Project** | [consumer_project](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_instance#consumer_project-1) | [Allowed Private Service Connect projects](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#allowed-projects)  
|  | **Deletion Policy** | [deletion_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_cluster#deletion_policy-1) | [deletion_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/alloydb_cluster#deletion_policy-1)  
|  | **Network Attachment Resource** | [networkAttachment](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters#PscInterfaceConfig.FIELDS.network_attachment_resource) | [Network attachment](https://docs.cloud.google.com/alloydb/docs/about-private-service-connect#network_attachment)  
Restore Cluster | Restore Backup Source | **Backup Name** | [restoreBackupSource](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/create#request-body) | [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr)  
Restore Continuous Backup Source | **Cluster** | [cluster](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/restore#ContinuousBackupSource.FIELDS.cluster) | [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr)  
**Point in Time** | [pointInTime](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters/restore#ContinuousBackupSource.FIELDS.point_in_time) | [Use point-in-time recovery (PITR)](https://docs.cloud.google.com/alloydb/docs/backup/restore-pitr)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
