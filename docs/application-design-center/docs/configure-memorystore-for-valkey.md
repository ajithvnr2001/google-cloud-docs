---
url: https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-valkey/
title: Configure a Memorystore for Valkey instance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:50:44.714794+00:00
---

# Configure a Memorystore for Valkey instance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-valkey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Memorystore for Valkey instance Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Valkey is a fully managed Valkey service for Google Cloud which supports both Cluster Mode Enabled and Cluster Mode Disabled instances. Applications running on Google Cloud can achieve extreme performance by leveraging the highly scalable, available, and secure Valkey service without the burden of managing complex Valkey deployments. For more information, see [Memorystore for Valkey overview](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview).

This document describes the connections and parameters you can configure when using App Design Center to create a Memorystore for Valkey instance. The configuration parameters are based on the [terraform-google-memorystore](https://github.com/terraform-google-modules/terraform-google-memorystore/tree/main/modules/valkey) Terraform module.

## Component connections

The following table includes the components that you can connect to a Memorystore for Valkey instance and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can cache data in the Memorystore for Valkey instance.
  * App Design Center adds the Memorystore for Valkey connection information to the Cloud Run environment variables.
  * App Design Center adds the `roles/memorystore.dbConnectionUser` role to the Cloud Run service account.

| [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance)  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The instance template can cache data in the Memorystore for Valkey instance.
  * App Design Center adds the Memorystore for Valkey connection information to the compute instance metadata.

| [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance)  
[Service Account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * App Design Center adds the `roles/memorystore.editor` role to the service account credentials to let the service account manage the instance.

| [Connect to a Memorystore for Valkey instance](https://docs.cloud.google.com/memorystore/docs/valkey/connect-instance)  
VPC network | 

  * App Design Center deploys the Memorystore for Valkey instance into the selected VPC network.
  * App Design Center adds the VPC network information to the Memorystore for Valkey network parameters.

| [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/valkey/networking#networking_setup_guidance)  
KMS key | 

  * The Memorystore for Valkey instance uses the connected KMS key for data-at-rest encryption.
  * App Design Center passes the KMS key ID into the Memorystore for Valkey instance configuration.

| [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/valkey/use-cmek)  
  
## Required configuration parameters

If your template includes a Memorystore for Valkey component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Name** | [name](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.name) | [Create instances](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances)  
**Project ID** | The project where you want to deploy the Memorystore for Valkey resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | [locationId](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations#Location.FIELDS.location_id) | [Supported regions](https://docs.cloud.google.com/memorystore/docs/valkey/locations#supported_regions)  
**Network** | [network](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PscConfig.FIELDS.network) | [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/valkey/networking#networking_setup_guidance)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Shard count** | [shardCount](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.shard_count) | [Shards](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview#shards)  
| **Replica count** | [replicaCount](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.replica_count) | [Primary and replica nodes](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview#primary_and_replica_nodes)  
| **Transit encryption mode** | [transitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.transit_encryption_mode) | [About in-transit encryption](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption)  
| **Authorization mode** | [authorizationMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.authorization_mode) | [About IAM authentication](https://docs.cloud.google.com/memorystore/docs/valkey/about-iam-auth)  
| **Node type** | [nodeType](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.node_type) | [Instance and node specification](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification)  
| **Zone distribution configuration mode** | [mode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ZoneDistributionConfig.FIELDS.mode) | [Single-zone instances](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances)  
Maintenance windows | **Day** | [day](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow.FIELDS.day) | [About maintenance on Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)  
**Hours** | [hours](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay#FIELDS.hours) | [About maintenance on Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)  
**Minutes** | [minutes](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay#FIELDS.minutes) | [About maintenance on Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)  
**Seconds** | [seconds](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay#FIELDS.seconds) | [About maintenance on Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)  
**Nanos** | [nanos](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/Shared.Types/TimeOfDay#FIELDS.nanos) | [About maintenance on Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)  
Persistence configuration | **Persistence mode** | [persistenceMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PersistenceConfig.FIELDS.mode) | [Persistence overview](https://docs.cloud.google.com/memorystore/docs/valkey/persistence-overview)  
**RDB snapshot period** | [rdbSnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RDBConfig.FIELDS.rdb_snapshot_period) | [About RDB snapshots](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence)  
**RDB snapshot start time** | [rdbSnapshotStartTime](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#RDBConfig.FIELDS.rdb_snapshot_start_time) | [About RDB snapshots](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-persistence)  
**AOF configuration** | [aofConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#PersistenceConfig.FIELDS.aof_config) | [About AOF snapshots](https://docs.cloud.google.com/memorystore/docs/valkey/about-aof-persistence)  
| **Enable APIs** | App Design Center enables the memorystore.googleapis.com API by default. | [Google Cloud Memorystore for Valkey API](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest)  
| **Service connection policy** | [ServiceConnectionPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.serviceConnectionPolicies#resource:-serviceconnectionpolicy) | [Create a service connection policy](https://docs.cloud.google.com/memorystore/docs/valkey/instance-provisioning-vpc#create_a_service_connection_policy)  
Engine configuration | **maxmemory-clients** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**maxmemory** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**maxmemory-policy** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**notify-keyspace-events** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**slowlog-log-slower-than** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**maxclients** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**databases** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
**cluster-databases** | [engineConfigs](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/valkey/supported-instance-configurations#modifiable_configuration_parameters)  
| **Zone distribution configuration zone** | [zone](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ZoneDistributionConfig.FIELDS.zone) | [Single-zone instances](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances)  
| **Deletion protection enabled** | App Design Center enables cluster deletion protection by default. | [Prevent deletion of a cluster](https://docs.cloud.google.com/memorystore/docs/valkey/deletion-protection#setting_or_removing_deletion_protection_on_an_existing_instance)  
| **KMS key** | [customerManagedKey](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.kms_key) | [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/valkey/use-cmek)  
Labels | **Key** | label | [Create and manage labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
**Value** | label | [Create and manage labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
| **Zonal distribution configuration mode** | [Zone distribution mode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#zonedistributionmode) | [Single-zone instances](https://docs.cloud.google.com/memorystore/docs/valkey/single-zone-instances)  
| **Cluster mode** | [mode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.mode) | [Enable and disable cluster mode](https://docs.cloud.google.com/memorystore/docs/valkey/cluster-mode-enabled-and-disabled)  
| **Engine version** | [engineVersion](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.engine_version) | [Supported versions](https://docs.cloud.google.com/memorystore/docs/valkey/supported-versions)  
| **Server CA mode** | [serverCaMode](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.server_ca_mode) | [Certificate Authorities](https://docs.cloud.google.com/memorystore/docs/valkey/about-in-transit-encryption#certificate-authorities)  
| **Server CA pool** | [serverCaPool](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.server_ca_pool) | [Secure your data by using a customer-managed Certificate Authority (CA)](https://docs.cloud.google.com/memorystore/docs/valkey/use-customer-managed-ca)  
| **Network project** | The project that hosts the shared VPC network. | [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc)  
| **Maintenance version** | [maintenanceVersion](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#Instance.FIELDS.maintenance_version) | [About maintenance on Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/about-maintenance)  
Backup configuration | **Automated backup configuration** | [automatedBackupConfig](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#automatedbackupconfig) | [About backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups)  
**Cloud Storage source** | [uri](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#GcsBackupSource.FIELDS.uris) | [About backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups)  
**Managed backup source** | [managedBackupSource](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#ManagedBackupSource.FIELDS.backup) | [About backups](https://docs.cloud.google.com/memorystore/docs/valkey/backups)  
  
## Cross region replication parameters

Parameter name | Description and constraints | Background information  
---|---|---  
**Instance role** | [instanceRole](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#CrossInstanceReplicationConfig.FIELDS.instance_role) | [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication)  
**Primary cluster** | [primaryInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#CrossInstanceReplicationConfig.FIELDS.primary_instance) | [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication)  
**Secondary clusters** | [secondaryInstance](https://docs.cloud.google.com/memorystore/docs/valkey/reference/rest/v1/projects.locations.instances#CrossInstanceReplicationConfig.FIELDS.secondary_instances) | [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/valkey/about-cross-region-replication)  
  
For more information about performing cross-region replication operations—such as attach, switchover, and detach—see the [Terraform google_memorystore_instance resource documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/memorystore_instance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
