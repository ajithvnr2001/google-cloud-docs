---
url: https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis/
title: Configure a Memorystore for Redis instance \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:14:46.253328+00:00
---

# Configure a Memorystore for Redis instance  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-memorystore-for-redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Memorystore for Redis instance Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Redis is a fully managed Redis service for Google Cloud. Applications running on Google Cloud achieve extreme performance by leveraging the highly scalable, available, secure Redis service without the burden of managing complex Redis deployments. For more information, see [Memorystore for Redis overview](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview).

This document describes the connection and parameters you configure when using App Design Center to create a Memorystore for Redis instance. The configuration parameters are based on the [terraform-google-memorystore](https://github.com/terraform-google-modules/terraform-google-memorystore) Terraform module.

## Component connections

The following table includes the components that you can connect to a Memorystore for Redis instance, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can manage and cache data in the Memorystore instance.
  * The Memorystore connection information is added to the Compute Engine instance template metadata.
  * The `roles/redis.editor` role is added to the Compute Engine service account.

| [Deployment options for Redis on Google Cloud](https://docs.cloud.google.com/compute/docs/redis/deployment-options)  
[service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can manage the Memorystore for Redis instance.
  * The `roles/redis.editor` role is added to the service account.

| [The Memorystore for Redis service account](https://docs.cloud.google.com/memorystore/docs/redis/access-control#the_service_account)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can cache data in the Memorystore for Redis instance.
  * The Memorystore for Redis connection information is added to the Cloud Run environment variables.
  * The `roles/redis.editor` role is added to the Cloud Run service account.

| [Connecting to a Redis instance from a Cloud Run service](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run)  
  
## Required configuration parameters

If your template includes a Memorystore for Redis component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Memorystore for Redis resource. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | [locationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.location_id) | [Regions and zones](https://docs.cloud.google.com/memorystore/docs/redis/instances#regions_and_zones)  
**Zone** | [locationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.location_id) | [Regions and zones](https://docs.cloud.google.com/memorystore/docs/redis/instances#regions_and_zones)  
**Name** | [name](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.name) | [Create and manage Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Display Name** | [displayName](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.display_name) | [Create and manage Redis instances](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances)  
| **Tier** | [Tier](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.tier) | [Redis tier capabilities](https://docs.cloud.google.com/memorystore/docs/redis/redis-tiers)  
| **Memory Size GB** | [memorySizeGb](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.memory_size_gb) | [Capacity tiers](https://docs.cloud.google.com/memorystore/docs/redis/instances#capacity_tiers)  
| **Redis Version** | [redisVersion](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.redis_version) | [Supported versions](https://docs.cloud.google.com/memorystore/docs/redis/supported-versions)  
| **Connect Mode** | [ConnectMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.connect_mode) | [Connection modes](https://docs.cloud.google.com/memorystore/docs/redis/networking#connection_modes)  
| **Replica Count** | [replicaCount](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.replica_count) | [About read replicas](https://docs.cloud.google.com/memorystore/docs/redis/about-read-replicas)  
| **Auth Enabled** | [authEnabled](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.auth_enabled) | [About Redis AUTH](https://docs.cloud.google.com/memorystore/docs/redis/about-redis-auth)  
| **Transit Encryption Mode** | [TransitEncryptionMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.transit_encryption_mode) | [About in-transit encryption](https://docs.cloud.google.com/memorystore/docs/redis/about-in-transit-encryption)  
Maintenance Policy | **Description** | [description](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#MaintenancePolicy.FIELDS.description) | [About maintenance on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)  
**Day** | [day](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow.FIELDS.day) | [About maintenance on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)  
**Hours** | [hours](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow.FIELDS.hours) | [About maintenance on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)  
**Minutes** | [minutes](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow.FIELDS.minutes) | [About maintenance on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)  
**Seconds** | [seconds](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow.FIELDS.seconds) | [About maintenance on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)  
**Nanos** | [nanos](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#WeeklyMaintenanceWindow.FIELDS.nanos) | [About maintenance on Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/about-maintenance)  
Persistence Config | **Persistence Mode** | [persistenceMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#PersistenceConfig.FIELDS.persistence_mode) | [About RDB snapshots](https://docs.cloud.google.com/memorystore/docs/redis/about-rdb-snapshots)  
**RDB Snapshot Period** | [rdbSnapshotPeriod](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#PersistenceConfig.FIELDS.rdb_snapshot_period) | [About RDB snapshots](https://docs.cloud.google.com/memorystore/docs/redis/about-rdb-snapshots)  
| **Read Replicas Mode** | [ReadReplicasMode](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.read_replicas_mode) | [About read replicas](https://docs.cloud.google.com/memorystore/docs/redis/about-read-replicas)  
| **Authorized Network** | [authorizedNetwork](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.authorized_network) | [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc)  
| **Enable APIs** | By default, enables the redis.googleapis.com API. | [Google Cloud Memorystore for Redis API](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest)  
| **Alternative Location ID** | [alternativeLocationId](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.alternative_location_id) | [Regions and zones](https://docs.cloud.google.com/memorystore/docs/redis/instances#regions_and_zones)  
| **Reserved IP Range** | [reservedIpRange](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.reserved_ip_address_range) | [Creating a Redis instance with a specific IP address range](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#creating_a_redis_instance_with_a_specific_ip_address_range)  
| **Secondary IP Range** | [secondaryIpRange](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.secondary_ip_range) | [Creating a Redis instance with a specific IP address range](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances#creating_a_redis_instance_with_a_specific_ip_address_range)  
Labels | **Key** | [labels](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.labels) | [Creating and managing labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
**Value** | [labels](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.labels) | [Creating and managing labels](https://docs.cloud.google.com/bigtable/docs/creating-managing-labels)  
| **Customer Managed Key** | [customerManagedKey](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance.FIELDS.customer_managed_key) | [About customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/memorystore/docs/redis/about-cmek)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
