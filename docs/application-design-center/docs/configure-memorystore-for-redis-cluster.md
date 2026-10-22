---
url: https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis-cluster/
title: Configure a Memorystore for Redis Cluster \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:48.953500+00:00
---

# Configure a Memorystore for Redis Cluster  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Memorystore for Redis Cluster Stay organized with collections  Save and categorize content based on your preferences. 

In App Design Center, you can configure a [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview) to provide horizontally scalable, high-availability Redis caching that shards data across primary nodes and replicates it across optional replica nodes. You can customize the cluster's component connections and configuration parameters based on the [terraform-google-memorystore](https://github.com/terraform-google-modules/terraform-google-memorystore/tree/main/modules/redis-cluster) Terraform module.

## Component connections

The following table includes the components that you can connect to a Memorystore for Redis Cluster, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can cache data in the Memorystore for Redis Cluster.
  * The Memorystore for Redis Cluster connection information is added to the Cloud Run environment variables.
  * The `roles/redis.editor` role is added to the Cloud Run service account.

| [Connect to a Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance)  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The instance template can cache data in the Memorystore for Redis Cluster.
  * App Design Center adds the Memorystore for Redis Cluster connection information to the compute instance metadata.

| [Connect to a Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance)  
[Service Account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * App Design Center adds the `roles/redis.editor` role to the service account credentials to let the service account manage the cluster.

| [Connect to a Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/connect-cluster-instance)  
VPC Network | 

  * App Design Center deploys the Memorystore for Redis Cluster into the selected VPC network.
  * App Design Center adds the VPC network information to the Memorystore for Redis Cluster network parameters.

| [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/cluster/networking#networking_setup_guidance)  
  
## Required configuration parameters

If your template includes a Memorystore for Redis Cluster component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Name** | [name](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.name) | [Create instances](https://docs.cloud.google.com/memorystore/docs/cluster/create-instances)  
**Project ID** | The project where you want to deploy the Memorystore for Redis Cluster resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | [locationId](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations#Location.FIELDS.location_id) | [Supported regions](https://docs.cloud.google.com/memorystore/docs/cluster/locations#supported_regions)  
**Network** | [network](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#PscConfig.FIELDS.network) | [Networking setup guidance](https://docs.cloud.google.com/memorystore/docs/cluster/networking#networking_setup_guidance)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Shard Count** | [shardCount](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.shard_count) | [Shards](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview#shards)  
| **Replica Count** | [replicaCount](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.replica_count) | [Primary and replica nodes](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview#primary_and_replica_nodes)  
| **Transit Encryption Mode** | [transitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.transit_encryption_mode) | [About in-transit encryption](https://docs.cloud.google.com/memorystore/docs/cluster/about-in-transit-encryption)  
| **Authorization Mode** | [authorizationMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.authorization_mode) | [About IAM authentication](https://docs.cloud.google.com/memorystore/docs/cluster/about-iam-auth)  
| **Node Type** | [nodeType](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.node_type) | [Cluster and node specification](https://docs.cloud.google.com/memorystore/docs/cluster/cluster-node-specification)  
| **Zone Distribution Config Mode** | [mode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#ZoneDistributionConfig.FIELDS.mode) | [Single-zone instances](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances)  
Maintenance Window | **Day** | [day](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#ClusterWeeklyMaintenanceWindow.FIELDS.day) | [About maintenance on Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance)  
**Hours** | [hours](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay#FIELDS.hours) | [About maintenance on Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance)  
**Minutes** | [minutes](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay#FIELDS.minutes) | [About maintenance on Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance)  
**Seconds** | [seconds](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay#FIELDS.seconds) | [About maintenance on Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance)  
**Nanos** | [nanos](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/TimeOfDay#FIELDS.nanos) | [About maintenance on Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/about-maintenance)  
Persistence Config | **Persistence Mode** | [persistenceMode](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#ClusterPersistenceConfig.FIELDS.mode) | [Persistence overview](https://docs.cloud.google.com/memorystore/docs/cluster/persistence-overview)  
**RDB Snapshot Period** | [rdbSnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#RDBConfig.FIELDS.rdb_snapshot_period) | [About RDB snapshots](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence)  
**RDB Snapshot Start Time** | [rdbSnapshotStartTime](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#RDBConfig.FIELDS.rdb_snapshot_start_time) | [About RDB snapshots](https://docs.cloud.google.com/memorystore/docs/cluster/about-rdb-persistence)  
**AOF Config** | [AofConfig](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#ClusterPersistenceConfig.FIELDS.aof_config) | [About AOF snapshots](https://docs.cloud.google.com/memorystore/docs/cluster/about-aof-persistence)  
| **Enable APIs** | By default, enables the redis.googleapis.com API. | [Google Cloud Memorystore for Redis Cluster API](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest)  
| **Service Connection Policy** | [ServiceConnectionPolicy](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.serviceConnectionPolicies#resource:-serviceconnectionpolicy) | [Create a service connection policy](https://docs.cloud.google.com/memorystore/docs/cluster/instance-provisioning-vpc#create_a_service_connection_policy)  
Redis Config | **Max Memory Clients** | [redisConfigs](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.redis_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters)  
**Max Memory** | [redisConfigs](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.redis_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters)  
**Max Memory Policy** | [redisConfigs](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.redis_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters)  
**Notify Key Space Events** | [redisConfigs](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.redis_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters)  
**Slow Log - Log Slower Than** | [redisConfigs](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.redis_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters)  
**Max Clients** | [redisConfigs](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.redis_configs) | [Modifiable configuration parameters](https://docs.cloud.google.com/memorystore/docs/cluster/supported-instance-configurations#modifiable_configuration_parameters)  
| **Zone Distribution Config Zone** | [zone](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#ZoneDistributionConfig.FIELDS.zone) | [Single-zone instances](https://docs.cloud.google.com/memorystore/docs/cluster/single-zone-instances)  
| **Deletion Protection Enabled** | By default, enables the cluster deletion protection. | [Prevent deletion of a cluster](https://docs.cloud.google.com/memorystore/docs/cluster/deletion-protection#setting_or_removing_deletion_protection_on_an_existing_instance)  
| **KMS Key** | [customerManagedKey](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#Cluster.FIELDS.kms_key) | [Use customer-managed encryption keys (CMEK) ](https://docs.cloud.google.com/memorystore/docs/cluster/use-cmek)  
Labels | **Key** | label | [Create and manage labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
**Value** | label | [Create and manage labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
  
## Cross region replication parameters

Parameter name | Description and constraints | Background information  
---|---|---  
**Cluster Role** | [clusterRole](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#CrossClusterReplicationConfig.FIELDS.cluster_role) | [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication)  
**Primary Cluster** | [primaryCluster](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#CrossClusterReplicationConfig.FIELDS.primary_cluster) | [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication)  
**Secondary Clusters** | [secondaryClusters](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters#CrossClusterReplicationConfig.FIELDS.secondary_clusters) | [About cross-region replication](https://docs.cloud.google.com/memorystore/docs/cluster/about-cross-region-replication)  
  
For instructions on performing cross-region replication operations—such as attach, switchover, and detach—see the [Terraform google_redis_cluster resource documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/redis_cluster).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
